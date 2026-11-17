# Likelihood implementation audit

Inspected repository snapshots on 17 November 2026:
- clevr_diff: `ddc7bf31ce832ca75b5698a31c1b209712a7922d`
- diff_ll_audio: `0461902c90b1ed85980f7174f325e1a9a6a6ee7a`
- speechdiff: `07ec102512bae7633077958eab68bf77a31e3dd6`

These snapshots establish what the available source implements. They do not establish which commit, overrides, or reporting script produced each thesis table. No synthesis experiments were rerun. A subsequent reanalysis of archived Grad-TTS candidate scores reproduced the ASR and likelihood-selected WERs and corrected the oracle/random comparison columns; see analysis/likelihood/README.md.

## Resolved source-level questions

### CFG 0 is conditional without guidance
The SDXL pipeline applies the unconditional/conditional combination only when guidance_scale > 1. At 0 it passes the positive prompt embeddings directly to the network. The same threshold is used for likelihood integration. Thus the row labelled CFG 0 does not evaluate the unconditional score from the chapter's algebraic CFG formula. It means guidance disabled, with text conditioning retained.

Source: [SDXL likelihood branch](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L65-L104); [prompt encoding](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L350-L415).

Both the generation/reconstruction scale and likelihood scale are assigned the same value in the experiment grids. The sample grid sweeps 0, 3, 5, 7. This resolves the missing CFG description at the source level; matching run records remains necessary.

Source: [sample grid](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/sample_ll.py#L85-L96); [PACS ranking grid](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/sdxl_pacs.py#L87-L104).

### PACS has seven configured classes
Both the ranking and sample scripts use dog, elephant, giraffe, guitar, horse, house, person, across art_painting, cartoon, photo, sketch. The thesis class count has been corrected to seven and its random class baseline to 14%, following author confirmation. With seven equiprobable class candidates, chance is 100/7 = 14.29%. The original PACS paper (section 4.1) confirms the same seven categories, including house: [original paper](https://arxiv.org/pdf/1710.03077). The class identities are resolved; exact evaluated image identities still require the run manifest.

Sources: [ranking script](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/sdxl_pacs.py#L55-L56); [sample script](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/sample_ll.py#L86-L87).

The sample grids request 20 repeats, implying 7 x 4 x 20 = 560 evaluations per stage if complete. Confirm completed-run counts rather than assuming all scheduled runs succeeded.

### Latent density is normalised by image dimensions
The pipeline samples from the VAE encoder posterior and multiplies by vae.config.scaling_factor. The likelihood integrates this scaled latent. It returns prior plus divergence integral with no encoder-density or image-space change-of-variables term.

Source: [encoding](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L370-L387); [density output](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L119-L123).

The 1024 sample reporting script divides -log2 density by 3*1024*1024; the 512 reporting script divides by 3*512*512. Therefore these scripts report a latent log-density normalised by the number of RGB image dimensions, not BPD per latent coordinate and not image-space likelihood. Retain numbers pending provenance confirmation; fix the metric definition or recompute consistently. The earlier suspicion of a single fixed denominator across both resolutions is resolved: there are separate resolution-specific reporting scripts.

Sources: [1024 denominator](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/sample_ll.py#L28-L29); [512 denominator](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/lil_sample_ll.py#L28-L29).

The checkpoint is stabilityai/stable-diffusion-xl-base-1.0. Its official VAE configuration has now been checked at Hugging Face revision 462165984030d82259a11f4367a4eed129e94a7b and saved in analysis/likelihood/sdxl_vae_config.json: four latent channels, eightfold spatial downsampling, scaling factor 0.13025. This gives 4 x 64 x 64 and 4 x 128 x 128 latent shapes for 512 and 1024 image resolutions. The RGB denominator is 48 times the latent dimension. Historical checkpoint cache revision remains unpinned.

Source: [checkpoint](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L25-L40).

### Solver tolerances differ across experiments
The image sample grids set Dopri5 atol=rtol=1e-3. Image ranking grids sweep both 1e-3 and 1e-5. The Grad-TTS wav2vec2 and Whisper rescoring entry points pass 1e-5. The blanket 1e-5 statement in the chapter cannot describe all these configured experiments. Match each table to its run overrides.

Sources: [image sample grid](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/sample_ll.py#L67-L96); [image ranking grid](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/sdxl_pacs.py#L87-L97); [Whisper rescoring](https://github.com/Mattias421/diff_ll_audio/blob/0461902c90b1ed85980f7174f325e1a9a6a6ee7a/wspr/wspr_ll.py#L150-L161); [wav2vec2 rescoring](https://github.com/Mattias421/diff_ll_audio/blob/0461902c90b1ed85980f7174f325e1a9a6a6ee7a/wav2vec2/w2v_ll.py#L114-L125).

## Additional issues affecting interpretation

### CLEVR prompts and colour output labels
The colour list is red, green, blue, brown, yellow, gray, purple, cyan, but output ll_blue receives index 1 (green) and ll_green receives index 2 (blue). These two labels are swapped. Candidate prompt construction also omits a space between colour and shape (e.g. 'redsphere'). Confirm whether this exact revision generated the tables; if so, rerun scoring/aggregation as appropriate before drawing colour-composition conclusions.

Source: [CLEVR script](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/sdxl_clevr.py#L55-L128).

### Ranking accuracy averages scores before ranking
The confusion-matrix helpers average log-likelihood over images sharing the true colour, shape, class, or domain, and then compute accuracy across rows of that averaged matrix. This differs from the chapter's stated per-image caption accuracy. Results in increments near 1/7 and 1/8 are compatible with that aggregation, but do not establish provenance. Verify the intended estimand and either describe the aggregation or recompute per-image accuracy.

Source: [aggregation and accuracy](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/_utils.py#L9-L116); [CLEVR grid aggregation](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/grids/sdxl_single.py#L20-L38).

### CLIP pixel preprocessing
sample_ll.py first converts the PIL image to a uint8 tensor via pil_to_tensor, then multiplies by 255 before casting to uint8 again. For ordinary 8-bit RGB inputs this does not preserve pixel values. Confirm the executed preprocessing before treating the tabulated CLIP values as standard CLIP scores.

Source: [CLIP preprocessing](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/sample_ll.py#L19-L36).

### Trajectory evaluation decodes and re-encodes images
The sample script generates a PIL image at each stage and calls the likelihood pipeline on that image, causing a new stochastic VAE encoding. This evaluates the density of a re-encoded image, rather than directly scoring the original intermediate latent. The density call uses the same source/target integration bounds at every stage. In addition, the scheduler helper's 'final' endpoint is sigmas[-2], rather than the appended zero at sigmas[-1]. These details need to be reconciled with statements about exact u=0 endpoints and likelihood along a latent probability-flow trajectory.

Sources: [sample evaluation](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/sample_ll.py#L128-L158); [scheduler bounds](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L181-L234); [density call](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L414-L472).

### Likelihood is numerically estimated
The SDXL density uses a single Rademacher vector for a stochastic divergence estimate plus numerical ODE integration. Describing the implemented values as exact likelihood without qualification overstates numerical precision.

Source: [trace estimator](https://github.com/Mattias421/clevr_diff/blob/ddc7bf31ce832ca75b5698a31c1b209712a7922d/pipeline_stable_diffusion_log_likelihood.py#L65-L119).

## Immediate author decisions
- Identify saved image run configs/results or the commit used to generate the published tables. The current repository snapshots contain no corresponding image results.
- The seven-class baseline is corrected to 14%. Resolve the image metric denominator and per-image versus aggregated ranking definition.
- Confirm which preprocessing and prompt-construction revisions actually ran.
- Grad-TTS significance is resolved by reanalysis of archived candidate scores; see the verification below. The image run provenance remains open.
- Write interpretation only after separating confirmed experimental behaviour from implementation/reporting discrepancies.


## Experimental-facts completion: additional evidence

### Grad-TTS rescoring comparisons verified

Reanalysis of `wav2vec2/gtts_ll_w2v.csv` and `wspr/gtts_ll_base.csv` at the pinned audio repository revision gives 95 recordings and 1560 reference words for each system. The ASR and likelihood-selected WERs reproduce the chapter. Exact oracle bounds and expected random WER replace the old approximate comparator columns, with the changes explicitly documented in the table caption and analysis report.

- wav2vec2: original ASR 13.2692%, likelihood 19.5513%, expected uniform 20.3471%.
- Whisper base: original ASR 3.3333%, likelihood 4.6795%, expected uniform 4.6428%.
- Likelihood versus ASR: two-sided NIST MAPSSWE gives Z=-9.751 (194 segments) and Z=-2.248 (62 segments); both degradations are significant at a per-comparison, unadjusted 5% level.
- Likelihood versus independent uniform candidate selection: exact lower-tail p-values are 0.0563081 and 0.5751915; neither improvement is significant at 5%.

The test alternatives differ; the manuscript now names each comparator explicitly. Reproduction script, input checksums, per-recording metrics, and raw NIST reports are in [analysis/likelihood](analysis/likelihood/README.md). These are new checks on archived scores, not recovery of the original statistical-test logs.

### Image sample counts: configured versus completed

The source defines several sample budgets, not one common 20-repeat budget:

| Entry point / grid | Repeats | Nominal number of images per configuration |
| --- | ---: | ---: |
| PACS sample generation (`grids/sample_ll.py`, `grids/lil_sample_ll.py`) | 20 | 560 per stage |
| PACS ranking (`grids/sdxl_pacs.py`, default config) | 1 | 28 |
| PACS ranking (`grids/robust_sdxl_pacs.py`) | 20 | 560 |
| CLEVR ranking (`grids/sdxl_single.py`, default config) | 1 | 24 |
| CLEVR ranking (`grids/robust_sdxl_single.py`) | 15 | 360 |
| CLIP PACS / CLEVR (`grids/clip.py`) | 20 | 560 / 480 |

The current chapter no longer asserts 20 repeats for all ranking experiments. Completed counts and table-to-grid mappings remain unverified without saved metrics/configs.

The PACS reference set is selected by the first `n_repeats` matching rows for each class/domain in `manifest.csv`. The source converts images to RGB; VAE likelihood preprocessing is delegated to Diffusers' image processor at the requested height/width. FID/CLIP use a separate PIL-to-tensor path. The exact manifest, input image identities, and installed Diffusers/TorchMetrics versions are not in the image repository.

### Additional FID reporting discrepancy

In `sample_ll.py`, FID accumulates real and generated tensors separately for each generation stage. From repeat index 2 onward it logs a new cumulative FID after each image. `grids/sample_ll.py` and `grids/lil_sample_ll.py` then average the successive logged FID values. This is not the final full-set FID. Existing image table values are preserved pending run provenance and/or recomputation. This discrepancy is separate from the CLIP uint8 rescaling issue. The separate CLIP ranking script `clip_score.py` starts from floats divided by 255 before scaling back, so the sample script's double-rescaling finding should not be attributed to that path; it does share the CLEVR prompt/label issues.

### SDXL training-data description resolved

The checkpoint's [technical report, section 2.5](https://arxiv.org/html/2307.01952v1) describes an internal pretraining dataset. The chapter names the exact base checkpoint and does not infer a specific public training corpus.
