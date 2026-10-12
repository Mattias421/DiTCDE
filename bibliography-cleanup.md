# Bibliography cleanup

`chapters/refs.bib`: 678 records → 401 records. Removed 198 off-topic or placeholder records and consolidated 79 duplicate records (including the neural ODE reference already in `bibliography.bib`).

Reviewed against the introduction, chapter outline and citations in all `.tex` sources. Uncited references relevant to neural differential equations, diffusion, flow matching, optimal transport, likelihood evaluation, speech synthesis, recognition and enhancement were retained. All existing nonempty citation keys still resolve after alias replacement. Removed records remain recoverable from Git history.

`main.tex` now loads `chapters/refs.bib` alongside `bibliography.bib`. Duplicate venue-string declarations were eliminated by expanding abbreviations; the undefined `SPL` abbreviation was expanded to IEEE Signal Processing Letters. Published records were preferred where available, with original editions retained for republished works. This was a local cleanup, not an external metadata verification.

## Consolidated keys

| Retained key | Removed aliases |
| --- | --- |
| `chen-etal-2024-f5tts` | `chenF5TTSFairytalerThat2024` |
| `LJSpeechDataset` | `ljspeech17` |
| `chen2022wavlm` | `chenWavLMLargeScaleSelfSupervised2022` |
| `ronneberger2015unet` | `ronnebergerUNetConvolutionalNetworks2015` |
| `kidger2021thesis` | `kidgerNeuralDifferentialEquations2022` |
| `lipman2024flowmatchingguide` | `lipmanFlowMatchingGuide2024` |
| `li2023styletts2` | `liStyleTTSHumanLevelTexttoSpeech2023` |
| `mehta2024matcha` | `mehtaMatchaTTSFastTTS2024` |
| `ho2021classifierfree` | `hoClassifierFreeDiffusionGuidance2022` |
| `chen2022likelihood` | `chen2021likelihood`, `chenLikelihoodTrainingSchr2023` |
| `lin2022robustuasr` | `linAnalyzingRobustnessUnsupervised2022` |
| `liu2023w2vu2` | `liuEndtoEndUnsupervisedSpeech2023` |
| `pratap2023mms` | `pratapScalingSpeechTechnology2023` |
| `baevski2021w2vu` | `baevskiUnsupervisedSpeechRecognition2021` |
| `baevski2020wav2vec2` | `baevskiWav2vecFrameworkSelfSupervised2020` |
| `liu2018uasrgan` | `liuCompletelyUnsupervisedPhoneme2018` |
| `hori2019cycleconsistencyasr` | `horiCycleconsistencyTrainingEndtoend2019` |
| `radfordRobustSpeechRecognition2022` | `radford2022robustspeechrecognitionlargescale` |
| `goodfellow2014gan` | `goodfellowGenerativeAdversarialNetworks2014`, `goodfellowGenerativeAdversarialNetworks2020` |
| `wu2023diffganuasr` | `wuEnhancingUnsupervisedSpeech2023`, `wuEnhancingUnsupervisedSpeech2023a` |
| `mcauliffe17_mfa` | `mcauliffeMontrealForcedAligner2017` |
| `kim2020glowtts` | `kimGlowTTSGenerativeFlow2020`, `kimGlowTTSGenerativeFlow2020a`, `kimGlowTTSGenerativeFlow2020b` |
| `popov21gradtts` | `popovGradTTSDiffusionProbabilistic2021` |
| `song2021sde` | `songScoreBasedGenerativeModeling2021` |
| `NEURIPS2018_69386f6b` | `chenNeuralOrdinaryDifferential2019`; retained in `bibliography.bib` |
| `karras2022elucidating` | `karrasElucidatingDesignSpace2022` |
| `gonzalez2023investigating` | `gonzalez2024investigating` |
| `wang2024diffusion` | `wangDiffusionbasedSpeechEnhancement2024` |
| `bunne2023schrodinger` | `bunneSchrodingerBridgeGaussian2023`, `bunneSchrOdingerBridge2023` |
| `chen_2023_sb` | `chenSchrodingerBridgesBeat2023` |
| `lay23_interspeech` | `layReducingPriorMismatch2023` |
| `vincent2011connection` | `vincentConnectionScoreMatching2011` |
| `lipman2023flow` | `lipmanFlowMatchingGenerative2022`, `lipmanFlowMatchingGenerative2023` |
| `schrodinger1932theorie` | `schrodingerTheorieRelativisteElectron1932` |
| `liuFlowStraightFast2022a` | `liuFlowStraightFast2022` |
| `hsuHuBERTSelfSupervisedSpeech2021` | (repeated records with the same key) |
| `korostikModifyingFlowMatching2025` | `korostikModifyingFlowMatching2025a` |
| `debortoliDiffusionSchrodingerBridge2021` | (repeated records with the same key) |
| `tongImprovingGeneralizingFlowbased2024` | `tongImprovingGeneralizingFlowbased2023`, `tongImprovingGeneralizingFlowbased2023a` |
| `leonardSurveySchrOdinger2013` | (repeated records with the same key) |
| `sohl-dicksteinDeepUnsupervisedLearning2015a` | `sohl-dicksteinDeepUnsupervisedLearning2015` |
| `mccannConvexityPrincipleInteracting1997` | (repeated records with the same key) |
| `vargasMachinelearningApproachesEmpirical2021` | `vargasMachinelearningApproachesEmpirical` |
| `aldarmakiUnsupervisedAutomaticSpeech2022` | `UnsupervisedAutomaticSpeech` |
| `dejaDiffusionbasedAccentModelling2023` | `DiffusionbasedAccentModelling` |
| `feydyInterpolatingOptimalTransport2018` | `feydyInterpolatingOptimalTransport2019` |
| `genevayLearningGenerativeModels2018` | `genevayLearningGenerativeModels2018a` |
| `kantorovichTranslocationMasses1942` | `kantorovichTranslocationMasses2006` |
| `kimMaximumLikelihoodTraining2022` | `kimMaximumLikelihoodTraining2022a` |
| `knillLanguageIndependentUnsupervised2014` | `knillLanguageIndependentUnsupervised2014a` |
| `kongHiFiGANGenerativeAdversarial2020` | `NEURIPS2020_c5d73680` |
| `luMaximumLikelihoodTraining2022` | `luMaximumLikelihoodTraining2022a` |
| `peyreComputationalOptimalTransport2019` | `peyreComputationalOptimalTransport2019a`, `peyreComputationalOptimalTransport2020` |
| `pooladianMultisampleFlowMatching2023` | `pooladianMultisampleFlowMatching2023a` |
| `radfordLearningTransferableVisual2021` | `radfordLearningTransferableVisual2021a` |
| `shiConditionalSimulationUsing2022` | `shiConditionalSimulationUsing2022a` |
| `shiDiffusionSchrOdinger2023` | `shiDiffusionSchrOdinger2023a` |
| `skillingEigenvaluesMegadimensionalMatrices1989` | `skillingEigenvaluesMegadimensionalMatrices1989a`, `skillingEigenvaluesMegadimensionalMatrices1989b` |
| `chen2019uasrselftrain` | `chenCompletelyUnsupervisedSpeech2019` |

## Removed records

These uncited records concern unrelated humanities, visual perception/cognition, NLP-only topics, specialised applications outside the thesis scope, or imported placeholders.

| Key | Title |
| --- | --- |
| `xi2023cyclenet` | CycleNet: Rethinking Cycle Consistency in Text-Guided Diffusion for Image Manipulation |
| `bahng2025cycleconsistencyrewardlearning` | Cycle Consistency as Reward: Learning Image-Text Alignment without Human Preferences |
| `karpov25_interspeech` | {From Scarcity to Sufficiency: Speech Recognition Pipeline for Zero-resource Language} |
| `park25f_interspeech` | {Character Error Rate Estimation for Semi-Supervised Training of Speech Recognition for Arabic Dialects} |
| `serditova25_interspeech` | {Automatic Speech Recognition Biases in Newcastle English: an Error Analysis} |
| `klejch25_interspeech` | {A Practitioner’s Guide to Building ASR Models for Low-Resource Languages: A Case Study on Scottish Gaelic} |
| `li25ca_interspeech` | {In-context Language Learning for Endangered Languages in Speech Recognition} |
| `hope25_interspeech` | {Voices of `cyborg awesomeness': Posthuman embodiment of nonbinary gender expression in AI speech technologies} |
| `haarnoja2018sac` | Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor |
| `malkin2022trajbalance` | Trajectory balance: Improved credit assignment in GFlowNets |
| `chang2024asrstrugglesaave` | {Self-supervised Speech Representations Still Struggle with African American Vernacular English} |
| `guyon-elisseeff-03` | An Introduction to Variable and Feature Selection |
| `guyon2007causalreport` | Causal Feature Selection |
| `cJones2003` | A sample paper in conference proceedings |
| `eWilliams1999` | Fourier Acoustics: Sound Radiation and Nearfield Acoustic Holography |
| `aSmith2000` | A sample paper in journals |
| `waspaaweb` | (untitled placeholder) |
| `IEEEXploreReqs` | (untitled placeholder) |
| `kendall2018multi` | Multi-task learning using uncertainty to weigh losses for scene geometry and semantics |
| `gidaris2018dynamic` | Dynamic few-shot visual learning without forgetting |
| `adamsSexualPoliticsMeat2018` | The {{Sexual Politics}} of {{Meat}} |
| `agarwalCausalVQARevealing2019` | Towards {{Causal VQA}}: {{Revealing}} and {{Reducing Spurious Correlations}} by {{Invariant}} and {{Covariant Semantic Editing}} |
| `agrawalNocapsNovelObject2019` | Nocaps: Novel Object Captioning at Scale |
| `albelwiSurveySelfSupervisedLearning2022` | Survey on {{Self-Supervised Learning}}: {{Auxiliary Pretext Tasks}} and {{Contrastive Learning Methods}} in {{Imaging}} |
| `anstisMotionAftereffect1998` | The Motion Aftereffect |
| `apidianakiWordTypesTokens2023` | From {{Word Types}} to {{Tokens}} and {{Back}}: {{A Survey}} of {{Approaches}} to {{Word Meaning Representation}} and {{Interpretation}} |
| `asimWordWhoCan2008` | The {{N}} Word: {{Who}} Can Say It, Who Shouldn't, and Why |
| `baddeleyExploringArticulatoryLoop1984` | Exploring the {{Articulatory Loop}} |
| `balsollierGenerativeModelSynthetize2023` | A Generative Model to Synthetize Spatio-Temporal Dynamics of Biomolecules in Cells |
| `barrySEARCHERSharedEmbedding2020` | {{SEARCHER}}: {{Shared Embedding Architecture}} for {{Effective Retrieval}} |
| `beneschTechnologyArtCybernetic1999` | Technology, {{Art}}, and the {{Cybernetic Body}}: {{The Cyborg}} as {{Cultural Other}} in {{Fritz Lang}}'s "{{Metropolis}}" and {{Philip K}}. {{Dick}}'s "{{Do Androids Dream}} of {{Electric Sheep}}?" |
| `bengioGFlowNetFoundations2023` | {{GFlowNet Foundations}} |
| `blakeNeuralTheoryBinocular1989a` | A Neural Theory of Binocular Rivalry |
| `blakeVisualCompetition2002` | Visual Competition |
| `boitoUnwrittenLanguagesDemand2017` | Unwritten Languages Demand Attention Too! {{Word}} Discovery with Encoder-Decoder Models |
| `boothRoleBasalGanglia2007` | The Role of the Basal Ganglia and Cerebellum in Language Processing |
| `bousquetAdvancedLecturesMachine2004` | Advanced Lectures on Machine Learning: {{ML Summer Schools}} 2003, {{Canberra}}, {{Australia}}, {{February}} 2-14, 2003 [and] {{T{\"u}bingen}}, {{Germany}}, {{August}} 4-16, 2003: Revised Lectures |
| `broadbentDetectionIdentificationResponse1987` | From Detection to Identification: {{Response}} to Multiple Targets in Rapid Serial Visual Presentation |
| `brownLanguageModelsAre2020` | Language {{Models}} Are {{Few-Shot Learners}} |
| `brownPolitenessUniversalsLanguage1987` | Politeness: {{Some Universals}} in {{Language Usage}} |
| `bruinsmaAutoregressiveConditionalNeural2023` | Autoregressive {{Conditional Neural Processes}} |
| `cameronWorkingSpokenDiscourse2001` | Working with {{Spoken Discourse}} |
| `campbellGenerativeFlowsDiscrete2024` | Generative {{Flows}} on {{Discrete State-Spaces}}: {{Enabling Multimodal Flows}} with {{Applications}} to {{Protein Co-Design}} |
| `caoComprehensiveSurveyAIGenerated2023` | A {{Comprehensive Survey}} of {{AI-Generated Content}} ({{AIGC}}): {{A History}} of {{Generative AI}} from {{GAN}} to {{ChatGPT}} |
| `capuanoSentimentAnalysisCustomer2021` | Sentiment Analysis for Customer Relationship Management: An Incremental Learning Approach |
| `castellucciLearningSolveNLP2021` | Learning to {{Solve NLP Tasks}} in an {{Incremental Number}} of {{Languages}} |
| `cesaireDiscourseColonialism2023` | Discourse on Colonialism |
| `changWordAcquisitionNeural2022` | Word {{Acquisition}} in {{Neural Language Models}} |
| `ChatGPT` | {{ChatGPT}} |
| `chenMusicLDMEnhancingNovelty2023` | {{MusicLDM}}: {{Enhancing Novelty}} in {{Text-to-Music Generation Using Beat-Synchronous Mixup Strategies}} |
| `cheukDiffrollDiffusionBasedGenerative2023` | Diffroll: {{Diffusion-Based Generative Music Transcription}} with {{Unsupervised Pretraining Capability}} |
| `chiccoSiameseNeuralNetworks2021` | Siamese {{Neural Networks}}: {{An Overview}} |
| `choGenerativeBiasRobust2023` | Generative {{Bias}} for {{Robust Visual Question Answering}} |
| `christensenLimitsDestructionCritical2020` | The {{Limits}} of {{Destruction}}: {{A Critical Analysis}} of the {{Collateral Damage Dispositif}} |
| `copetSimpleControllableMusic2023` | Simple and {{Controllable Music Generation}} |
| `corbettaPETStudyVisuospatial1993` | A {{PET}} Study of Visuospatial Attention |
| `corkinWhatNewAmnesic2002` | What's New with the Amnesic Patient {{HM}}? |
| `crossImmuneInspiredAlgorithm2021` | An {{Immune Inspired Algorithm}} for {{Fault Tolerant Enhanced Multimodal Machine Learning}} |
| `dautumeEpisodicMemoryLifelong2019` | Episodic {{Memory}} in {{Lifelong Language Learning}} |
| `devilliersLinguisticDeterminismUnderstanding2000` | Linguistic Determinism and the Understanding of False |
| `dickAndroidsDreamElectric1968` | Do Androids Dream of Electric Sheep? |
| `DiscourseColonialism2023` | Discourse on {{Colonialism}} |
| `duncanCooperatingBrainSystems1996` | Cooperating Brain Systems in Selective Perception and Action |
| `dunnBinocularRivalryDynamics2020` | Binocular Rivalry Dynamics Associated with High Levels of Self-Reported Autistic Traits Suggest an Imbalance of Cortical Excitation and Inhibition |
| `dunnMixedContinuousCategorical2024` | Mixed {{Continuous}} and {{Categorical Flow Matching}} for {{3D De Novo Molecule Generation}} |
| `duxAttentionalBlinkReview2009` | The Attentional Blink: {{A}} Review of Data and Theory |
| `eelenCritiquePolitenessTheory2014` | A {{Critique}} of {{Politeness Theory}}: {{Volume}} 1 |
| `eisapeProbingIncrementalParse2022` | Probing for {{Incremental Parse States}} in {{Autoregressive Language Models}} |
| `eisenschlosWinoDictProbingLanguage2022` | {{WinoDict}}: {{Probing}} Language Models for in-Context Word Acquisition |
| `eiserbeckElectrophysiologicalChronometryGraded2021` | Electrophysiological {{Chronometry}} of {{Graded Consciousness During}} the {{Attentional Blink}} |
| `enardFOXP2RoleCorticobasal2011` | {{FOXP2}} and the Role of Cortico-Basal Ganglia Circuits in Speech and Language Evolution |
| `ErwinSchrodinger2023` | Erwin {{Schr{\"o}dinger}} |
| `ettingerWhatBERTNot2020` | What {{BERT Is Not}}: {{Lessons}} from a {{New Suite}} of {{Psycholinguistic Diagnostics}} for {{Language Models}} |
| `faircloughCriticalStudyLanguage2013` | : The {{Critical Study}} of {{Language}} |
| `federCausaLMCausalModel2021` | {{CausaLM}}: {{Causal Model Explanation Through Counterfactual Language Models}} |
| `fedorenkoFunctionalSpecificityHighlevel2011` | Functional Specificity for High-Level Linguistic Processing in the Human Brain |
| `frankNumberCognitiveTechnology2008` | Number as a Cognitive Technology: {{Evidence}} from {{Pirah{\~a}}} Language and Cognition |
| `fristonDynamicCausalModelling2003` | Dynamic Causal Modelling |
| `FullDetailsActions` | Full Details and Actions for {{Working}} with Spoken Discourse |
| `futrellNeuralLanguageModels2019` | Neural Language Models as Psycholinguistic Subjects: {{Representations}} of Syntactic State |
| `galvanEnteringPosthumanCollective1997` | Entering the {{Posthuman Collective}} in {{Philip K}}. {{Dick}}'s "{{Do Androids Dream}} of {{Electric Sheep}}?" |
| `garneloConditionalNeuralProcesses2018` | Conditional {{Neural Processes}} |
| `gibneyAgeApologyFacing2008` | The {{Age}} of {{Apology}}: {{Facing Up}} to the {{Past}} |
| `gibsonHowEfficiencyShapes2019` | How Efficiency Shapes Human Language |
| `gilkersonMappingEarlyLanguage2017` | Mapping the Early Language Environment Using All-Day Recordings and Automated Analysis |
| `godardVeryLowResource2018` | A {{Very Low Resource Language Speech Corpus}} for {{Computational Language Documentation Experiments}} |
| `goffmanEssaysFacetoFaceBehavior2017` | : Essays in {{Face-to-Face Behavior}} |
| `goodaleSeparateVisualPathways1992a` | Separate Visual Pathways for Perception and Action |
| `gordonConvolutionalConditionalNeural2020` | Convolutional {{Conditional Neural Processes}} |
| `grandSemanticProjectionRecovers2022` | Semantic Projection Recovers Rich Human Knowledge of Multiple Object Features from Word Embeddings |
| `grenanderRepresentationsKnowledgeComplex1994` | Representations of {{Knowledge}} in {{Complex Systems}} |
| `grenanderRepresentationsKnowledgeComplex1994a` | Representations of {{Knowledge}} in {{Complex Systems}} |
| `grenanderRepresentationsKnowledgeComplex1994b` | Representations of {{Knowledge}} in {{Complex Systems}} |
| `guptaFoxesHoundsHorses2006` | Foxes, {{Hounds}}, and {{Horses}}: {{Who}} or {{Which}}? |
| `hedlinUnsupervisedSemanticCorrespondence2023` | Unsupervised {{Semantic Correspondence Using Stable Diffusion}} |
| `holmesDisturbancesVisionCerebral1918` | Disturbances of Vision by Cerebral Lesions |
| `hoogeboomEquivariantDiffusionMolecule2022` | Equivariant {{Diffusion}} for {{Molecule Generation}} in {{3D}} |
| `hopfingerSelectiveAttentionElectrophysiological` | Selective Attention: {{Electrophysiological}} and Neuromagnetic Studies. |
| `hopfingerSelectiveAttentionElectrophysiological2004` | Selective {{Attention}}: {{Electrophysiological}} and {{Neuromagnetic Studies}} |
| `hopfingerSelectiveAttentionElectrophysiologicala` | Selective Attention: {{Electrophysiological}} and Neuromagnetic Studies. |
| `huangAudioGPTUnderstandingGenerating2023` | {{AudioGPT}}: {{Understanding}} and {{Generating Speech}}, {{Music}}, {{Sound}}, and {{Talking Head}} |
| `huangMakeAnAudioTextToAudioGeneration2023` | Make-{{An-Audio}}: {{Text-To-Audio Generation}} with {{Prompt-Enhanced Diffusion Models}} |
| `huangMDMMolecularDiffusion2022` | {{MDM}}: {{Molecular Diffusion Model}} for {{3D Molecule Generation}} |
| `huebnerBabyBERTaLearningMore2021` | {{BabyBERTa}}: {{Learning More Grammar With Small-Scale Child-Directed Language}} |
| `huebnerStructuredSemanticKnowledge2018` | Structured {{Semantic Knowledge Can Emerge Automatically}} from {{Predicting Word Sequences}} in {{Child-Directed Speech}} |
| `huMembershipInferenceDiffusion2023` | Membership {{Inference}} of {{Diffusion Models}} |
| `huSystematicAssessmentSyntactic2020` | A {{Systematic Assessment}} of {{Syntactic Generalization}} in {{Neural Language Models}} |
| `idiartHowBrainRepresents2019` | How the {{Brain Represents Language}} and {{Answers Questions}}? {{Using}} an {{AI System}} to {{Understand}} the {{Underlying Neurobiological Mechanisms}} |
| `igashovEquivariant3DconditionalDiffusion2024` | Equivariant {{3D-conditional}} Diffusion Model for Molecular Linker Design |
| `InboxMcross2Sheffield` | Inbox - Mcross2@sheffield.Ac.Uk - {{University}} of {{Sheffield Mail}} |
| `jepsonLinguisticAnalysisDiscourse2008` | A {{Linguistic Analysis}} of {{Discourse}} on the {{Killing}} of {{Nonhuman Animals}} |
| `jiangLowResourceTextClassification2023` | ``{{Low-Resource}}'' {{Text Classification}}: {{A Parameter-Free Classification Method}} with {{Compressors}} |
| `jiangMotionDiffuserControllableMultiAgent2023` | {{MotionDiffuser}}: {{Controllable Multi-Agent Motion Prediction Using Diffusion}} |
| `karimiSurveyAlgorithmicRecourse2022` | A {{Survey}} of {{Algorithmic Recourse}}: {{Contrastive Explanations}} and {{Consequential Recommendations}} |
| `kaufEventKnowledgeLarge2022` | Event Knowledge in Large Language Models: The Gap between the Impossible and the Unlikely |
| `kheelKillingGameEcofeminist1996` | The {{Killing Game}}: {{An Ecofeminist Critique}} of {{Hunting}} |
| `kheelLicenseKillEcofeminist1995` | 4 {{License}} to {{Kill}}: {{An Ecofeminist Critique}} of {{Hunters}}' {{Discourse}} |
| `KiyosiIto2023` | Kiyosi {{It{\^o}}} |
| `koenderinkOpticFlow1986` | Optic Flow |
| `lakeOmniglotChallenge3year2019` | The {{Omniglot}} Challenge: A 3-Year Progress Report |
| `LanguagePower2013` | Language and {{Power}} |
| `lavancierSpatialBirthdeathmoveProcesses2021` | Spatial Birth-Death-Move Processes : Basic Properties and Estimation of Their Intensity Functions |
| `leopoldActivityChangesEarly1996` | Activity Changes in Early Visual Cortex Reflect Monkeys' Percepts during Binocular Rivalry |
| `levinsonPragmatics1983` | Pragmatics |
| `liuAudioLDMLearningHolistic2023` | {{AudioLDM}} 2: {{Learning Holistic Audio Generation}} with {{Self-supervised Pretraining}} |
| `liuDiffSingerSingingVoice2022` | {{DiffSinger}}: {{Singing Voice Synthesis}} via {{Shallow Diffusion Mechanism}} |
| `liuPerformanceEvaluationSelforganizing2006` | Performance Evaluation of the Self-Organizing Map for Feature Extraction |
| `liuRelationalMemoryAugmentedLanguage2022` | Relational {{Memory-Augmented Language Models}} |
| `liVisualizingUnderstandingNeural2016` | Visualizing and {{Understanding Neural Models}} in {{NLP}} |
| `logothetisNeuronalCorrelatesSubjective1989` | Neuronal Correlates of Subjective Visual Perception |
| `luccioniStableBiasEvaluating2023` | Stable {{Bias}}: {{Evaluating Societal Representations}} in {{Diffusion Models}} |
| `luoTextguidedDiffusionModel2023` | Text-Guided {{Diffusion Model}} for {{3D Molecule Generation}} |
| `macgregorCausalContributionsDomainGeneral2022` | Causal {{Contributions}} of the {{Domain-General}} ({{Multiple Demand}}) and the {{Language-Selective Brain Networks}} to {{Perceptual}} and {{Semantic Challenges}} in {{Speech Comprehension}} |
| `mackDissociationPositionExtent1985` | The Dissociation of Position and Extent in {{M{\"u}ller-Lyer}} Figures |
| `mahowaldDissociatingLanguageThought2023` | Dissociating Language and Thought in Large Language Models: A Cognitive Perspective |
| `marianiMultiSourceDiffusionModels2023` | Multi-{{Source Diffusion Models}} for {{Simultaneous Music Generation}} and {{Separation}} |
| `markerMakahWhaleHunt2006` | After the {{Makah Whale Hunt}}: {{Indigenous Knowledge}} and {{Limits}} to {{Multicultural Discourse}} |
| `maroisNeuralFateConsciously2004` | The {{Neural Fate}} of {{Consciously Perceived}} and {{Missed Events}} in the {{Attentional Blink}} |
| `mengLocatingEditingFactual2022` | Locating and {{Editing Factual Associations}} in {{GPT}} |
| `miaoParallelLearningOverview2023` | Parallel {{Learning}}: {{Overview}} and {{Perspective}} for {{Computational Learning Across Syn2Real}} and {{Sim2Real}} |
| `mitchellChildrenReasoningMind2000` | Children's {{Reasoning}} and the {{Mind}} |
| `mitropolskyBiologicallyPlausibleParser2021` | A {{Biologically Plausible Parser}} |
| `moutoussisRelationshipCorticalActivation2002` | The Relationship between Cortical Activation and Perception Investigated with Invisible Stimuli |
| `moyal-sharrockWittgensteinMemoryDebate2009` | Wittgenstein and the Memory Debate |
| `naumkinPersonalPronounsSocotran1998` | Personal Pronouns in {{Socotran}} Folklore Texts |
| `navonEquivariantDeepWeight2024` | Equivariant {{Deep Weight Space Alignment}} |
| `nyamapfeneMultimodalModelChild2007` | A {{Multimodal Model}} of {{Child Language Acquisition}} at the {{One-Word Stage}} |
| `oplerReviewAgriculturalHunting1941` | Review of {{The Agricultural}} and {{Hunting Methods}} of the {{Navaho Indians}} |
| `ouyangTrainingLanguageModels2022` | Training Language Models to Follow Instructions with Human Feedback |
| `pavlickSemanticStructureDeep2022` | Semantic {{Structure}} in {{Deep Learning}} |
| `pearlCausalInferenceStatistics2009` | Causal Inference in Statistics: {{An}} Overview |
| `pearlCausality2009` | Causality |
| `pearsonMentalImageryFunctional2015` | Mental {{Imagery}}: {{Functional Mechanisms}} and {{Clinical Applications}} |
| `peineltGiBERTEnhancingBERT2021` | {{GiBERT}}: {{Enhancing BERT}} with {{Linguistic Information}} Using a {{Lightweight Gated Injection Method}} |
| `PhonologicalLoopLanguage` | The Phonological Loop as a Language Learning Device {\textbar} 14 {\textbar} {{Exploring W}} |
| `pinayaFastUnsupervisedBrain2022` | Fast {{Unsupervised Brain Anomaly Detection}} and~{{Segmentation}} with~{{Diffusion Models}} |
| `posnerHowParietalLobes1987` | How Do the Parietal Lobes Direct Covert Attention? |
| `potterMethodStudyingLanguage1984` | : A {{Method}} for {{Studying Language Processing}} |
| `potterRecognitionMemoryRapid1969` | Recognition Memory for a Rapid Sequence of Pictures |
| `raymondTemporarySuppressionVisual1992` | Temporary Suppression of Visual Processing in an {{RSVP}} Task: An Attentional Blink? . |
| `raymondTemporarySuppressionVisual1992a` | Temporary Suppression of Visual Processing in an {{RSVP}} Task: An Attentional Blink? |
| `reevesAttentionGatingShortterm1986` | Attention Gating in Short-Term Visual Memory |
| `reimersSentenceBERTSentenceEmbeddings2019` | Sentence-{{BERT}}: {{Sentence Embeddings}} Using {{Siamese BERT-Networks}} |
| `rentelnApologiesCrossculturalAnalysis2008` | Apologies: {{A}} Cross-Cultural Analysis |
| `riddochRelativePerceptionsMovement1917a` | On the {{Relative Perceptions}} of {{Movement}} and a {{Stationary Object}} in {{Certain Visual Disturbances}} Due to {{Occipital Injuries}} |
| `rogersPrimerBERTologyWhat2020` | A {{Primer}} in {{BERTology}}: {{What}} We Know about How {{BERT}} Works |
| `runcieSILVRGuidedDiffusion2023` | {{SILVR}}: {{Guided Diffusion}} for {{Molecule Generation}} |
| `sariTrainingSpokenLanguage2020` | Training {{Spoken Language Understanding Systems}} with {{Non-Parallel Speech}} and {{Text}} |
| `schiebingerOptimalTransportAnalysisSingleCell2019` | Optimal-{{Transport Analysis}} of {{Single-Cell Gene Expression Identifies Developmental Trajectories}} in {{Reprogramming}} |
| `schneiderMoUsaiTexttoMusic2023` | Mo{\textbackslash}{\textasciicircum}usai: {{Text-to-Music Generation}} with {{Long-Context Latent Diffusion}} |
| `scholkopfCausalRepresentationLearning2021` | Toward {{Causal Representation Learning}} |
| `schulmanChatGPTOptimizingLanguage2022` | {{ChatGPT}}: {{Optimizing Language Models}} for {{Dialogue}} |
| `shanLearnNovelIncremental2020` | Learn\#: {{A Novel}} Incremental Learning Method for Text Classification |
| `shapiroAttentionalBlink1997` | The Attentional Blink |
| `shenGenerativeVisualQuestion2023` | Generative {{Visual Question Answering}} |
| `shufeldtNavajoTanner1888` | The {{Navajo}} Tanner |
| `silverMasteringChessShogi2017` | Mastering {{Chess}} and {{Shogi}} by {{Self-Play}} with a {{General Reinforcement Learning Algorithm}} |
| `sinclairStructuralPersistenceLanguage2022` | Structural {{Persistence}} in {{Language Models}}: {{Priming}} as a {{Window}} into {{Abstract Language Representations}} |
| `spencer-oateyImPolitenessFace2005` | ({{Im}}){{Politeness}}, {{Face}} and {{Perceptions}} of {{Rapport}}: {{Unpackaging}} Their {{Bases}} and {{Interrelationships}} |
| `stibbeLanguagePowerSocial2001` | Language, {{Power}} and the {{Social Construction}} of {{Animals}} |
| `stoerigBlindsightManMonkey1997` | Blindsight in Man and Monkey. |
| `swanDefenseHunting1995` | In Defense of Hunting |
| `syStatisticalCausalModel1993` | A Statistical Causal Model for the Assessment of Dysarthric Speech and the Utility of Computer-Based Speech Recognition |
| `taziIntuitionFrameworkApplying2023` | Beyond {{Intuition}}, a {{Framework}} for {{Applying GPs}} to {{Real-World Data}} |
| `thompsonPronounsVoiceKoyukon1989` | Pronouns and {{Voice}} in {{Koyukon Athapaskan}}: {{A Text-Based Study}} |
| `tongBinocularRivalryVisual1998` | Binocular {{Rivalry}} and {{Visual Awareness}} in {{Human Extrastriate Cortex}} |
| `tramerAdversarialTrainingRobustness2019` | Adversarial {{Training}} and {{Robustness}} for {{Multiple Perturbations}} |
| `tsiamasPushingLimitsZeroshot2024` | Pushing the {{Limits}} of {{Zero-shot End-to-End Speech Translation}} |
| `vigInvestigatingGenderBias2020` | Investigating {{Gender Bias}} in {{Language Models Using Causal Mediation Analysis}} |
| `VleReader` | - {{VleReader}} |
| `wangExtendingMultilingualBERT2020` | Extending {{Multilingual BERT}} to {{Low-Resource Languages}} |
| `weiskrantzBlindsightCaseStudy1990` | Blindsight: {{A}} Case Study and Implications |
| `whorfLanguageThoughtReality2012` | Language, Thought, and Reality: {{Selected}} Writings of {{Benjamin Lee Whorf}} |
| `xuCycleNetRethinkingCycle2023` | {{CycleNet}}: {{Rethinking Cycle Consistency}} in {{Text-Guided Diffusion}} for {{Image Manipulation}} |
| `zhangLimitationsAdversarialTraining2019` | The {{Limitations}} of {{Adversarial Training}} and the {{Blind-Spot Attack}} |
| `zhouLearningDenseCorrespondence2016` | Learning {{Dense Correspondence}} via {{3D-Guided Cycle Consistency}} |
| `zhouLearningPromptVisionLanguage2022` | Learning to {{Prompt}} for {{Vision-Language Models}} |
| `zotero-121` | (untitled placeholder) |

## Validation

All 39 nonempty citation keys resolve. BibTeX with the thesis style succeeds without warnings for currently cited entries. The full retained collection also passes BibTeX, with warnings about pre-existing incomplete metadata in uncited entries. The malformed OpenCLIP author-list syntax was repaired.
