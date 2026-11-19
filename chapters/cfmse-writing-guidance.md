# Writing the deep noise suppression chapter

Follow the technical prose of the surrounding thesis. Begin from a property of the signal or the estimator and frame a question that the experiment can answer. Use British spelling and the thesis notation. Exclude first-person plural throughout, including captions and footnotes.

Calculate paired differences, means and interval endpoints at full precision. Display measured results to three significant figures, including trailing zeros. Preserve exact sample counts, budgets, identifiers and configured parameters. Use the system or procedure as the subject when reporting quantitative comparisons. [Manchester Academic Phrasebank, reporting results](https://www.phrasebank.manchester.ac.uk/reporting-results/)

Open with the modelling question. Where does an enhancement model get the noisy observation: through the state from which generation starts, through an explicit conditioning input, or through both? On VoiceBank–DEMAND a noisy mono spectrum already has the shape of the clean target. On ECHI four microphone signals and enrolment audio specify the desired speaker, while the model generates one mono signal. Use this change of setting to motivate the second experiment.

## Give each comparison a purpose

Introduce the direct U-Net first to establish what a single supervised prediction achieves. Place SGMSE+, SB-VE, ICFM and FM alongside it in the full-data benchmark. Define each generative system by its source and path before discussing its loss or sampling cost. Use “FM path” and “FM objective” explicitly: an ICFM path can be trained with the FM objective. Reserve DDP for direct data prediction at inference. One-evaluation Euler and DDP can call the same network once and produce different estimates.

Refresh the related-work paragraph when revising the chapter. For each relevant speech-enhancement paper, identify the change it actually tests (source, conditioning, path, loss or inference), the task and its comparison system. Cite the experiment that bears on the chapter’s question. A denoising result and a dereverberation result may support different choices of source.

Open each results subsection with the question its rows can answer. Identify the matched items, models and budget, then explain the largest relevant gain and any metric that moves in the opposite direction. For example, switching from 50 ODE evaluations to DDP raises PESQ for the noisy-source ICFM checkpoint and lowers it for Gaussian FM. That comparison estimates the effect of switching inference within each checkpoint. A source-only explanation requires matched paths and training.

## Make a table readable on its own

Report signed change from noisy speech for all five metrics in the order specified in [the experimental guide](cfmse-experimental-guidance.md). Write +0.12 or −0.08 and give SI-SDR changes in dB. Reserve ± for a named measure of uncertainty. When discussing a difference between two systems, name both and give the direction of subtraction.

In each caption give the split, evaluation unit and count, noisy signal, sampler and network function evaluations (NFE). Identify any metric-specific exclusions. Reuse Part II’s bestblue, secondorange and worstred for the best, second-best and worst enhanced scores per metric within a comparable group. Give tied displayed scores the same rank. Colour the noisy zero row red and identify it as the reference in the caption. A negative cell means degradation even when the reference row is red. Separate budgets or protocols into labelled groups before applying colours.

## Match the conclusion to the evidence

Use the speaker sweep to discuss the combined change in training data and optimiser updates under 300 epochs. Use the URGENT splits to discuss transfer of named checkpoints. For ECHI, describe development performance, the overlap with checkpoint selection, the single training seed and the reference-alignment protocol when interpreting SI-SDR. Gaussian-source generation demonstrates that four-channel conditioning can support a mono state. A claim about its advantage over a data-derived source needs a matched mono-source experiment.
