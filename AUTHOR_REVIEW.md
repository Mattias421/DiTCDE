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

- SDXL likelihood in this chapter is described as a latent-space density. Confirm whether the reported BPD values are computed over autoencoder latents and state the latent dimensionality and any scaling or Jacobian correction. Without an invertible image transform and its Jacobian, this is not an exact image-space likelihood.
- The CFG derivation gives the unconditional score at `omega=0`. The PACS/CLEVR tables report prompt-ranking scores at CFG 0 that vary with prompt. Confirm the actual score path and whether prompt conditioning remains active in the likelihood calculation.
- State the number and identities of PACS classes used. The current manuscript reports nine classes, while the standard PACS benchmark is usually described with seven; the experimental subset or any expanded class set needs explanation.
- Confirm the SDXL training-data description and exact CFG configuration from the checkpoint and pipeline used. The present text avoids an unsupported dataset assertion.
- The text-to-image tables use FID and CLIP values with particular generated and reference sets. Confirm sample counts, preprocessing, and whether the reference sets are comparable before interpreting absolute FID values.

## Missing material and remaining math checks

- Restore or identify the missing figure and data for the ODE-step comparison in `chapters/icfm_results.tex`; the associated one-step and twenty-step claims have been removed pending evidence.
- Several chapter and citation references remain unresolved in the full document build (for example `ch:diffusion`, `ch:ll`, `ch:cfm`, and `ch:cfmse`). Reference and bibliography repairs were outside this pass.
- The forward/backward Schr\"odinger equations, Gaussian potential expressions, and exact conventions for potential normalisation should receive a final author check against the chosen reference, especially if they are used as a formal derivation rather than an overview.
- The regression optima in the revised Grad-TTS chapter are population statements. Exact equality to the target density or score requires a suitable function class, the stated training distribution, and global optimisation; finite models and empirical training only approximate these optima.
