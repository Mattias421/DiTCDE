# Author review items from the mathematical consistency pass

These points depend on experimental code, omitted figures, or intended modelling choices. They are recorded without changing reported numerical results.

## ASR joint-clock objective

- In `chapters/asr.tex`, the rate is defined as `du/dt = zeta(z_t,h_t)`, while the penalty retains the supplied form `integral_0^U zeta(z_t,h_t) dt - U`. Please confirm whether the integration variable and upper bound are intended: integrating over acoustic time would normally use an acoustic-time horizon, while integrating over token depth would require a corresponding change of measure. The bounds and objective were deliberately preserved in this pass.
- Confirm that the hidden-state update uses `h_t` as the acoustic encoder state and that the discretisation is intended as an Euler step with `Delta t = 1`. The proposed update is conceptual; it does not define how token emissions or the CTC alignment are coupled during training.

## Speech bridge and flow matching

- Confirm that the SB-VE sampling implementation evaluates the denoiser at the current state depth `u_i`, as written in `chapters/flow_matching.tex`. The cited sampler derivation uses the current state and time. The formula is singular at `u_i = 1`, so the implementation needs an endpoint limit or explicit special case.
- The flow-matching target `X_0 - Y` is retained as the reverse-depth velocity, consistent with direct prediction `F(Y,Y,1) + Y`. Confirm that the experimental ODE integrates depth from 1 down to 0 with this sign convention.
- The fixed covariance `c I` leaves nonzero conditional variance at both endpoints when `c > 0`; it does not exactly interpolate individual paired samples. Confirm that this is the intended ICFM path in the derivation and code.
- Check the displayed closed-form Schr\"odinger potentials and their boundary conditions against the cited derivation. The prose now distinguishes path-space laws from time-marginal densities, but the detailed Gaussian potential formula has not been re-derived in this pass.
- The speech enhancement residual equals additive background noise only when the room impulse response is the identity. Confirm that the experiments using reverberant signals do not interpret `Y-X` as noise alone.

## Likelihood experiments

Update, 17 November 2026: the supplied repositories have now been inspected. See [LIKELIHOOD_CODE_AUDIT.md](LIKELIHOOD_CODE_AUDIT.md) for pinned commits and source links. CFG 0 retains text conditioning; image grids match generation/reconstruction and likelihood scales. The code lists seven PACS classes, and image reporting divides latent log-density by RGB dimensions. These findings clarify the questions below, but saved runs still need to be matched to the manuscript tables. The audit also records CLEVR label/prompt issues, CLIP preprocessing, aggregation before ranking, and differing solver tolerances. Synthesis results are preserved. The later Grad-TTS reanalysis updates oracle/random comparator columns from archived candidate scores; see analysis/likelihood/README.md.

- SDXL representation resolved: posterior-sampled scaled VAE latents, four channels with eightfold spatial downsampling and scaling factor 0.13025. Image score denominator is 3HW; this is not image-space likelihood. Official configuration is archived in analysis/likelihood/. Historical checkpoint-cache revision remains unpinned.
- CFG convention resolved: the implementation keeps positive text conditioning at reported CFG 0, with no unconditional/conditional guidance combination. Saved image runs still need to be matched to the tables.
- PACS class count resolved: seven classes, as confirmed by the author. The text and caption use seven, and the random class baseline is 14% (rounded from 100/7). The seven class identities, including house, agree with section 4.1 of the original PACS paper. Exact evaluated image identities still need the manifest.
- SDXL checkpoint and training description resolved: base 1.0 without refiner; section 2.5 of the technical report describes internal pretraining data. The grids match generation/reconstruction and density guidance scales.
- Image run provenance remains open: confirm completed counts, exact reference files, table-to-run mapping, and whether CLIP/FID preprocessing and reporting fixes were present. Source-level budgets and reference selection are documented in the code audit.
- Grad-TTS significance resolved by archived-score reanalysis: both likelihood rescoring degradations versus ASR scores are significant under NIST MAPSSWE; neither improvement over uniform random candidate selection is significant at 5%. Script, per-recording metrics, and raw reports are in analysis/likelihood/.

## Missing material and remaining math checks

- Restore or identify the missing figure and data for the ODE-step comparison in `chapters/icfm_results.tex`; the associated one-step and twenty-step claims have been removed pending evidence.
- Several chapter and citation references remain unresolved in the full document build (for example `ch:diffusion`, `ch:ll`, `ch:cfm`, and `ch:cfmse`). Reference and bibliography repairs were outside this pass.
- The forward/backward Schr\"odinger equations, Gaussian potential expressions, and exact conventions for potential normalisation should receive a final author check against the chosen reference, especially if they are used as a formal derivation rather than an overview.
- The regression optima in the revised Grad-TTS chapter are population statements. Exact equality to the target density or score requires a suitable function class, the stated training distribution, and global optimisation; finite models and empirical training only approximate these optima.
