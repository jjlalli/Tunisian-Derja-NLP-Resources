# Tunisian Arabic Speech Resources

Speech corpora (ASR, spoken language understanding, speech translation), text-to-speech resources, and speech dialect identification for Tunisian Arabic (`aeb`). For pretrained ASR/TTS **models**, see [MODELS.md](MODELS.md). Access legend is defined in [README.md](README.md).

## Contents

- [Speech corpora (ASR / SLU / speech translation)](#speech-corpora-asr--slu--speech-translation)
- [Text-to-speech (TTS)](#text-to-speech-tts)
- [Speech / spoken dialect identification](#speech--spoken-dialect-identification)
- [Speech benchmark and encoder analyses](#speech-benchmark-and-encoder-analyses)
- [Speech shared tasks](#speech-shared-tasks)
- [Confirmed negatives](#confirmed-negatives)

---

## Speech corpora (ASR / SLU / speech translation)

### [TARIC — Tunisian Arabic Railway Interaction Corpus](https://aclanthology.org/L14-1385/)
- ~20 hours of authentic railway-station dialogues (ticket booking, scheduling), with manual phonetic annotation, segmentation, and a rule-based phonetic dictionary. Masmoudi, Ellouze Khmekhem, Estève, Hadrich Belguith, Habash (MIRACL + LIUM), 2014.
- The earliest Tunisian ASR corpus; still used as a test set. Audio not openly released.
- **[on request]** ([HAL PDF](https://hal.science/hal-01433247)).

### [STAC — Spoken Tunisian Arabic Corpus](https://www.researchgate.net/publication/307583782)
- ~4.8 hours of spontaneous speech (radio/TV/interviews), manually transcribed and phonetically annotated per CODA-TUN. Zribi, Ellouze, Hadrich Belguith, Blache, 2015. First Tunisian corpus with multiple annotation layers.
- **[on request]** (via [Inès Zribi's resource page](https://sites.google.com/site/ineszribi/ressources/corpus)).

### [TunSwitch (TunSwitch-TO + TunSwitch-CS)](https://zenodo.org/records/8370566)
- Code-switching speech (SpeechBrain format). Ben Abdallah, Kabboudi, Kanoun, Zaiem (Télécom Paris + Tunis Business School), 2023/2024.
- ~3h Tunisian-only + ~9h code-switched TN/FR/EN labeled, plus ~153h weakly-labeled audio (18 GB total); includes a 4-gram KenLM LM and language-level annotation. A key open code-switching resource.
- Mirror: HF [tunis-ai/TunSwitch](https://huggingface.co/datasets/tunis-ai/TunSwitch). Paper: [ICASSP 2024 / arXiv:2309.11327](https://arxiv.org/abs/2309.11327). **[open]** (CC-BY-4.0).

### [LinTO Audio & Textual Datasets for Tunisian Arabic](https://huggingface.co/datasets/linagora/linto-dataset-audio-ar-tn)
- ~93 hours of audio (~81.6h labeled), 20,895 files / ~76k segments; aggregated from YouTube, podcasts, MASC, TunSwitch, OneStory, etc. Naouara, Louradour, Lorré (LINAGORA Labs), 2025. The largest openly-packaged Tunisian ASR training collection.
- Companion [augmented set](https://huggingface.co/datasets/linagora/linto-dataset-audio-ar-tn-augmented) and a large text corpus. Paper: [arXiv:2504.02604](https://arxiv.org/abs/2504.02604). **[open]** (CC-BY-4.0).

### [TARIC-SLU](https://aclanthology.org/2024.lrec-main.1357/)
- Spoken language understanding extension of TARIC: ~8 hours, 108 speakers, railway dialogues annotated with dialogue acts/slots (60 concepts, 2,500+ values). Mdhaffar, Bougares, de Mori, Zaiem, Ravanelli, Estève, 2024.
- SpeechBrain recipe: [elyadata/TARIC-SLU](https://github.com/elyadata/TARIC-SLU). **[open]**.

### [SLURP-TN](https://huggingface.co/datasets/Elyadata/SLURP-TN)
- Tunisian version of the SLURP SLU resource: ~5 hours, 4,165 sentences, 55 native speakers, 6 domains. Elleuch, Mdhaffar, Estève, Bougares (LIA Avignon + Elyadata), 2026.
- Paper: [arXiv:2603.21940](https://arxiv.org/abs/2603.21940). **[open]** (HuggingFace).

### [TEDxTN](https://huggingface.co/datasets/fbougares/TEDxTN)
- First publicly available Tunisian→English speech-translation corpus: 108 TEDx talks (~25 hours), code-switched Tunisian, speakers from 11+ regions; audio + Tunisian transcript + English translation + annotation guidelines. Bougares, Mdhaffar, Elleuch, Estève, ArabicNLP 2025.
- Data: [fbougares/TEDxTN](https://huggingface.co/datasets/fbougares/TEDxTN) (HuggingFace). Paper: [ACL](https://aclanthology.org/2025.arabicnlp-main.22/) / [arXiv:2511.10780](https://arxiv.org/abs/2511.10780). **[open]**.

### [TuniFra](https://huggingface.co/datasets/fbougares/TUNIFRA)
- The first open Tunisian↔French code-switch speech-translation corpus: 15 hours of native Tunisian speech, orthographically transcribed and manually translated into French, for ASR and Tunisian→French speech translation. Choux, Avila, Crego, Bougares (Elyadata), Laurent, ArabicNLP 2025.
- Data: [fbougares/TUNIFRA](https://huggingface.co/datasets/fbougares/TUNIFRA) (HuggingFace). Paper: [ACL](https://aclanthology.org/2025.arabicnlp-main.5/) / [PDF](https://aclanthology.org/2025.arabicnlp-main.5.pdf). Used as a training resource in NADI 2026.
- **[open]** (HuggingFace).

### [TuDiCoI — Tunisian Dialogue Corpus of Interactions](https://huggingface.co/datasets/arbml/TuDiCoI)
- Spoken railway-ticket dialogue corpus (Derja), transcribed. Small (~hundreds of dialogue turns; arbml mirror ~434 rows). One of the earliest Tunisian dialogue resources.
- **[open]** (HuggingFace arbml mirror).

### [IWSLT 2022 Tunisian Conversational Speech (LDC2022E01 / LDC2025S05)](https://catalog.ldc.upenn.edu/LDC2025S05)
- Large three-way (audio + transcript + English translation) conversational telephone speech corpus, ~160–210h transcribed (CODA orthography), 8 kHz. Basis of the IWSLT dialectal speech-translation task.
- Data-prep and scoring code is open: [kevinduh/iwslt22-dialect](https://github.com/kevinduh/iwslt22-dialect); task page [iwslt.org/2022/dialect](https://iwslt.org/2022/dialect). Example systems: [ON-TRAC (arXiv:2205.01987)](https://arxiv.org/abs/2205.01987), [CMU (IWSLT 2022)](https://aclanthology.org/2022.iwslt-1.27/).
- **[paywalled]** (LDC membership/fee).

### [TuniSpeech-21h](https://www.scitepress.org/Papers/2026/144577/144577.pdf)
- Multi-domain corpus: 21h 6m, 32,294 segments, 187 speakers (120 M / 67 F); social-media + broadcast (politics, sports, culture, cooking, etc.). Sghaier, Bellagha, Zrigui (Univ. of Monastir), ICAART 2026. Ships with a Wav2Vec2 vs Whisper benchmark (best: Whisper-large-v2, WER 24.74%).
- **[on request]** (corpus specs and eval protocol in the paper; fine-tuned model is public — see [MODELS.md](MODELS.md)).

### [OpenSLR SLR46 — Tunisian_MSA](https://www.openslr.org/46/)
- 11.2 hours of read/prompted utterances by 118 Tunisian speakers — but the **content is Modern Standard Arabic**, not Derja. Useful for Tunisian-accent MSA acoustic modeling only.
- **[open]** (Apache 2.0).

### [CALL MY NET 2 (CMN2) / 2018 NIST SRE (LDC2020S04)](https://catalog.ldc.upenn.edu/LDC2020S04)
- Tunisian Arabic conversational telephone speech (PSTN + VOIP, 8 kHz) collected in Tunis via the Call My Net 2 protocol, plus English web-video audio from the VAST project. LDC gives **~396 hours for the release as a whole** — the Tunisian-only portion is not stated separately, so treat 396h as an upper bound, not a Tunisian figure.
- Collected for **speaker recognition** (NIST SRE18/19), not ASR or language modelling: no transcripts of the kind ASR training needs.
- **[paywalled]** (LDC; fee shown only after login).

### [Arbi-Houssem/Tunisian_dataset_STT-TTS15s_filtred1.0](https://huggingface.co/datasets/Arbi-Houssem/Tunisian_dataset_STT-TTS15s_filtred1.0)
- ~3h50m, 1,029 clips, up to 18 speakers, timestamped Derja transcripts (YouTube-sourced). Usable for STT and TTS. 2024.
- **[open]** (HuggingFace).

### [oddadmix/lahgtna-v3-small](https://huggingface.co/datasets/oddadmix/lahgtna-v3-small)
- Dialect-**balanced** multi-dialect Arabic ASR set: ~54.6k rows, 52k train / 2.6k test, 13 dialects including Tunisian, seed 42, undiacritized `clean_text` field. Ahmed Wasfy (oddadmix), 2026.
- Tunisian is 200 clips in the held-out test split — small, but it is the balance that makes it useful: it supports **like-for-like comparison of Tunisian against twelve other Arabic dialects under identical conditions**, which very few Tunisian resources allow. See the per-dialect WER table in [MODELS.md](MODELS.md#asr-models).
- Part of the wider [Arabic Voice Collection](https://huggingface.co/collections/oddadmix/arabic-voice-collection). **[open]**.

---

## Text-to-speech (TTS)

### [TunArTTS — Tunisian Arabic Text-To-Speech Corpus](https://aclanthology.org/2024.lrec-main.1467/)
- First Tunisian TTS resource: 3+ hours, single male speaker, 44.1 kHz, manually diacritized. Laouirine, Kammoun, Bougares, LREC-COLING 2024. Tacotron2 + FastSpeech2 baselines (best MOS 3.88 via transfer from LJSpeech).
- Repo: [elyadata/TunArTTS](https://github.com/elyadata/TunArTTS). **[open]** (for research).

### [Habibi — Unified-Dialectal Arabic Speech Synthesis](https://arxiv.org/abs/2601.13802)
- Multi-dialect Arabic TTS framework + benchmark (12+ dialects, zero-shot voice cloning). Code: [SWivid/Habibi-TTS](https://github.com/SWivid/Habibi-TTS). Whether Tunisian is among its 7 benchmark subsets is **unconfirmed**. **[open]** (Tunisian coverage uncertain).

### Community and commercial Tunisian TTS
- [SpeechGen Tunisian TTS (ar-TN)](https://speechgen.io/en/tts-arabic-tunisia/) — commercial text-to-speech with Tunisian voices (e.g., Hedi, Reem). Not open/research; noted for completeness. **[commercial]**.
- Community fine-tunes and TTS-oriented sets on HuggingFace: the [Arbi-Houssem/Tunisian_dataset_STT-TTS](https://huggingface.co/datasets/Arbi-Houssem/Tunisian_dataset_STT-TTS15s_filtred1.0) series, [kalil99x/fixed-tts-tunisian](https://huggingface.co/datasets/kalil99x/fixed-tts-tunisian2) series (2025), [deepdml/Tunisian_MSA](https://huggingface.co/datasets/deepdml/Tunisian_MSA) (2026). **[open]** (quality varies).

---

## Speech / spoken dialect identification

### [ADI-20 — Arabic Dialect Identification dataset](https://arxiv.org/abs/2511.10070)
- 3,556 hours across 19 dialects + MSA; expands ADI-17 and explicitly **adds Tunisian**. Elleuch et al., Interspeech 2025. The first large spoken-ADI set to include Tunisian.
- **[open]** (paper; data per authors).

### [Text and Speech-based Tunisian Sub-Dialects Identification (LREC 2020)](https://aclanthology.org/2020.lrec-1.787/)
- Distinguishes Tunisian sub-dialects (Tunis / Sfax / Sousse / Tataouine) from text and speech. Kchaou, Ben Abdallah, Bougares. **[open]** (paper).

---

## Speech benchmark and encoder analyses

- [Performance Analysis of Speech Encoders for Low-Resource SLU and ASR in Tunisian Dialect (ArabicNLP 2024)](https://aclanthology.org/2024.arabicnlp-1.12/) — Mdhaffar, Elleuch, Bougares, Estève. SSL encoders evaluated on TARIC-SLU. **[open]**.
- [Tunisian Dialectal End-to-end ASR based on DeepSpeech (Procedia 2021)](https://www.sciencedirect.com/science/article/pii/S1877050921011984) — WER 24.4% / CER 18.7%. **[open]**.

---

## Speech shared tasks

### [NADI 2025 — First Multidialectal Arabic Speech Processing Shared Task](https://arxiv.org/abs/2509.02038)
- Subtask 1: spoken dialect ID (built on ADI-20, so includes Tunisian); Subtask 2: multidialectal ASR; Subtask 3: diacritic restoration. Talafha et al., 2025.
- Winning system: [ELYADATA & LIA at NADI 2025 (arXiv:2511.10090)](https://arxiv.org/abs/2511.10090) — ADI 1st (79.83%), ASR 2nd.

### [NADI 2026 — Multidialectal Arabic Speech Processing](https://nadi.dlnlp.ai/2026/)
- Speech-focused, and strongly Tunisian-relevant. Tasks include country-level / mixed / **code-switched ASR** (subtask 1.3 is Tunisian⇄English⇄French code-switching, Tunisian matrix language, ~38h train + 1h dev), spoken dialect ID, dialectal TTS, spoken language translation (8 dialects→English), and SLU (intent + slot filling). Baselines: Whisper-Large-v3, ECAPA-TDNN, OmniVoice. Training resources cited include TEDxTN, TuniFra, and SLURP-TN.
- Registration deadline reported July 20, 2026. Organizer roster not independently confirmed (Elyadata/Bougares involvement reported).
- Tunisian training data released for the task (Fethi Bougares' HuggingFace): [fbougares/NADI_TUN_ASR_2026](https://huggingface.co/datasets/fbougares/NADI_TUN_ASR_2026) (~26.5k, code-switched Tunisian ASR) and [fbougares/NADI_Whitehouse_AST_2026](https://huggingface.co/datasets/fbougares/NADI_Whitehouse_AST_2026) (speech translation). **[open]**.

### [SLURP-TN baselines](https://github.com/elyadata/SLURP-TN-baselines)
- Baseline SpeechBrain recipes for the SLURP-TN dataset. Elyadata. **[open]** (GitHub).

### [IWSLT 2022 / 2023 dialectal speech translation](https://iwslt.org/2022/dialect)
- Tunisian↔English speech translation task. Data prep/scoring: [kevinduh/iwslt22-dialect](https://github.com/kevinduh/iwslt22-dialect).
