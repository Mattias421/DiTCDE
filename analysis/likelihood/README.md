# Likelihood experimental facts

This directory records the Grad-TTS rescoring reanalysis and the SDXL VAE configuration used to resolve section 1 of `LIKELIHOOD_COMPLETION.md`. It does not contain new model generations.

## Grad-TTS rescoring

Inputs are `wav2vec2/gtts_ll_w2v.csv` and `wspr/gtts_ll_base.csv` from [diff_ll_audio, revision 0461902](https://github.com/Mattias421/diff_ll_audio/tree/0461902c90b1ed85980f7174f325e1a9a6a6ee7a). Both contain the same 95 recordings and 1560 reference words. There are 8998 wav2vec2 and 309 Whisper candidate rows. Duplicate hypotheses, if present, remain separate rows for uniform sampling.

The script splits saved text on whitespace without additional text normalisation, recomputes word edit counts, and selects the largest original ASR score or Grad-TTS likelihood. A tied score selects the first CSV row. Oracle bounds use the minimum/maximum exact word edit counts rather than the saved `wer` column. Uniform random performance is the expected corpus WER; its exact one-sided p-value is computed by integer convolution of each recording's candidate error-count distribution, including ties in the lower tail.

| System | Original ASR WER % | Grad-TTS WER % | Exact oracle best % | Exact oracle worst % | Expected random % | p versus uniform |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| wav2vec2 | 13.2692 | 19.5513 | 10.1923 | 29.3590 | 20.3471 | 0.0563081 |
| Whisper base | 3.3333 | 4.6795 | 1.5385 | 7.1795 | 4.6428 | 0.5751915 |

These reproduce the main ASR and Grad-TTS columns. The manuscript's wav2vec2 oracle columns change from 10.5/29.0 to 10.2/29.4. Selecting oracle rows using the saved, rounded `wer` column gives 10.4487/28.9744, explaining most of the discrepancy but not establishing the original 10.5 rounding. The random columns change from a reported 20.2/4.3 to expected values of 20.3/4.6; the repository evaluator draws one random candidate per recording, while this reanalysis removes that sampling variability. No claim is made to reproduce the original random draw.

The likelihood-versus-ASR MAPSSWE comparisons use [NIST SCTK revision 9688a26](https://github.com/usnistgov/SCTK/tree/9688a26882a688132a5e414cadcb4c19b6fffaba), with its default minimum of two correct boundary words. wav2vec2 has 194 segments and Z = -9.751; Whisper has 62 segments and Z = -2.248. Both degradations are significant at an unadjusted, per-comparison 5% level. Approximate two-sided normal p-values derived from the rounded Z values are 1.83e-22 and 0.0246. The percentages in SCTK's MAPSSWE segment report have a segment-word denominator; they are not corpus WER. Independently aligned SCTK error totals agree with the Python totals (207/305 and 52/73 errors).

Files:

- `rescoring_verification.json`: metrics, input checksums after CRLF-to-LF normalisation, candidate counts, per-recording selected hypotheses and word errors, exact uniform-selection p-values, and SCTK invocation details.
- `wav2vec2_mapsswe.txt` and `whisper_base_mapsswe.txt`: original NIST reports. Paths in these reports identify the temporary run directory.
- `verify_rescoring.py`: standard-library-only reproducible analysis. Missing input files are downloaded from the pinned repository revision.

To reproduce the WER and uniform-selection test:

```sh
python analysis/likelihood/verify_rescoring.py --data-dir /tmp/thesis-facts-inputs --output-dir /tmp/thesis-facts-results
```

To include MAPSSWE, build `sclite` and `sc_stats` from the pinned NIST source (`sh config.sh` in `src/sclite`, then `make -j2 sclite sc_stats`) and add `--sctk-bin /path/to/SCTK/src/sclite` to the command. The script checks SCTK's error totals against its independent edit-distance results.

## SDXL representation and training data

`sdxl_vae_config.json` was retrieved from the [official checkpoint at revision 4621659](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/462165984030d82259a11f4367a4eed129e94a7b/vae/config.json). The experiment code uses the base checkpoint with no refiner. Four latent channels, eightfold spatial downsampling, and scaling factor 0.13025 give 4 x 64 x 64 or 4 x 128 x 128 latent coordinates at 512 or 1024 image resolution. The historical run did not pin a Hugging Face revision; this is the verified official configuration, not proof of the historical cache revision.

The experiment code samples the VAE encoder posterior, multiplies by the scaling factor, and evaluates density in those scaled coordinates. It applies no encoder-density term or conversion to image density. The image reporting denominator is 3HW, 48 times the latent dimension. The chapter now states this convention rather than treating the numbers as per-latent-coordinate BPD.

The [SDXL technical report, section 2.5](https://arxiv.org/html/2307.01952v1) describes pretraining on an internal dataset. The chapter does not attribute the checkpoint to a specific public dataset such as LAION.

## Image experiment facts still requiring run records

The nominal settings, preprocessing paths, and implementation discrepancies are in `../../LIKELIHOOD_CODE_AUDIT.md`. Actual image sample counts and exact reference-file lists cannot be recovered from scheduler definitions alone. The current image repository has source but no matching experiment metrics. Until saved runs establish the executed revision, the image table values cannot be certified as standard CLIP/FID measurements.
