# Likelihood chapter: completion checklist

The experiment tables are present. Finish by resolving methods questions, writing the interpretation, and checking the compiled chapter. Synthesis metrics are preserved. Grad-TTS rescoring oracle/random comparator columns have been recomputed from archived candidates; see analysis/likelihood/README.md for the old/new values and reproduction steps.

## 1. Resolve experimental facts (suggested: 45–60 minutes)

- [x] Inspect CFG implementation: CFG 0 retains positive text conditioning; the grids match generation/reconstruction and density scales. Methods text corrected. Still match saved runs to tables.
- [x] Correct PACS to seven classes in the text and caption and its random class baseline to 14% (100/7 rounded). The author confirmed the class count. All seven class names, including house, also agree with section 4.1 of the original PACS paper. Exact evaluated image identities still require the manifest.
- [x] Specify SDXL latent shapes (4 x 64 x 64 / 4 x 128 x 128), VAE posterior sampling, scaling factor 0.13025, and absence of image-density conversion. The chapter explicitly defines the RGB-dimension denominator; official configuration is saved in analysis/likelihood/sdxl_vae_config.json.
- [x] State final-data density p_0 evaluation for all three models, distinguish it from p_u, and explain SDXL decoding/re-encoding before scoring. The Matcha trajectory evaluation is now part of the main speech section.
- [ ] Confirm completed image sample counts, reference-file identities, preprocessing revision, and table-to-run mappings from saved outputs. Configured counts, reference-selection rules, CLIP/FID code paths, and their discrepancies are documented in the audit. Checkpoint and training-data description are resolved (base SDXL 1.0, internal pretraining dataset in its technical report).
- [x] Recompute Grad-TTS rescoring comparisons from archived scores: NIST MAPSSWE finds degradation versus original ASR scores significant for both systems (unadjusted per-comparison 5%). Exact uniform-selection tests give p=0.0563 and p=0.5752, so neither improvement over random is significant. The chapter names the comparators, sample counts, and tests; script and reports are in analysis/likelihood/.

Verification of the rescoring reanalysis passed on a fresh download of the pinned candidate files. Both NIST alignment error totals agree with the independent Python word-edit counts, and the rounded manuscript table entries match the report. Chapter/appendix reference labels, citation keys, figure paths, brace balance, and `git diff --check` pass.

See [LIKELIHOOD_CODE_AUDIT.md](LIKELIHOOD_CODE_AUDIT.md) for commit-linked evidence from the three supplied repositories. Before finalising the image conclusions, establish whether the executed revision contains the CLEVR label swap, missing prompt spaces, CLIP pixel rescaling, and averaging-before-ranking behaviour found in the current source. Image BPD uses an RGB denominator on a latent density; solver tolerances also vary by experiment. See AUTHOR_REVIEW.md for the remaining experimental queries. Do not guess missing settings.

## 2. Complete the author discussion (suggested: 90 minutes)

- [x] Distinguish the three questions in the introduction and organise speech results by generation trajectories and transcript rescoring, with references to both models' tables. Separate the Grad-TTS-only adaptation experiment.
- [x] Integrate Matcha-TTS throughout the introduction, models, speech data, density conventions, task-organised results, summary, future work, and enhancement transition. Move its trajectory and rescoring tables from the appendix, preserving every result and significance value. Keep the supplementary SDXL grid in the appendix.
- [ ] Explain the limits of the conclusions: tested models/tasks, numerical integration, feature coordinates/normalisation, and the interpretation of ASR-derived WER.
- [ ] Revisit strong claims such as “malformed density”, “not features of language”, “This is verified”, and skipping half of generation. Decide which conclusions the experiments support and qualify the rest.
- [x] Write the closing transition to probability-path design and speech enhancement (Chapter ch:cfmse), linking the speech likelihood/intelligibility findings to paired restoration, path variance, added noise, and iterative generation, with context from Chapter ch:simulation-free.
- [x] Update the introduction and summary for all three evaluated generators, distinguishing the Grad-TTS and Matcha-TTS trajectory trends and rescoring significance results.

## 3. Editorial closure (suggested: 30–45 minutes)

- [x] Replace “Appendix XXXX” with the labelled Models section and the labelled likelihood-results appendix; retain the appendix reference for the full SDXL grid. Matcha-TTS now appears in the main chapter.
- [x] Replace the CFG placeholder with the source's scale convention and grid settings. Run-to-table mapping remains open.
- [x] Inspect the n-best comparison figure, replace its vector mu heading with “encoder output”, and describe the transcript rows, synthesis columns, alignment, axes, and blank tails in the caption. Plot image data verified unchanged.
- [x] Remove the resolved figure note and appendix table-retention note. Retain the full SDXL table because the main chapter cites it. Move the opening discussion reminders to the section 2 checklist; unresolved experiment and closing-discussion notes remain open.
- [x] Review captions and terminology: distinguish fractional trajectory/adaptation WER from percentage rescoring WER, explain ASV and oracle columns, standardise Matcha-TTS and n-best wording, and add links to the preceding likelihood derivation and subsequent enhancement chapter. Numerical table rows were preserved during the editorial pass; the subsequent experimental-facts reanalysis updates the rescoring oracle/random columns as documented above.

Editorial verification: source checks found no missing reference labels, citation keys, or figure files in the likelihood chapter or appendix. `git diff --check` passed. The edited figure was rendered and visually inspected. Full thesis compilation remains a separate section 4 task.

## 4. Validate (suggested: 30 minutes)

- [ ] Compile and inspect the chapter and appendix, including landscape figures and table widths.
- [ ] Resolve chapter-specific missing references/citations and remaining placeholders.
- [ ] Read the introduction, results takeaways, and conclusion together for consistency.

No pdflatex, latexmk, or tectonic executable was available on PATH during this pass. The repository make.sh targets notation_example rather than main.tex, so it is not a thesis build command.
