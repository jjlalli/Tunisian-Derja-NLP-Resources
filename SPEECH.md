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
- ~20 hours of authentic railway-station dialogues at the Tunis station ticket offices (4,662 dialogues, 18,657 statements, 71,684 words per the paper), manually transcribed in Arabic script with diacritics, plus a rule-based phonetic (pronunciation) dictionary (grapheme-to-phoneme word error ≈ 9%). Masmoudi, Ellouze Khmekhem, Estève, Hadrich Belguith, Habash (MIRACL Sfax, LIUM Le Mans, CCLS Columbia), LREC 2014.
- The earliest Tunisian ASR corpus; still used as a test set. Audio not openly released.
- **[on request]** (no distribution page found; the TARIC-SLU paper notes the audio "is not" online as of 2024. [HAL record](https://hal.science/hal-01433247), [LREC PDF](http://www.lrec-conf.org/proceedings/lrec2014/pdf/454_Paper.pdf)).

### [STAC — Spoken Tunisian Arabic Corpus](https://www.rcs.cic.ipn.mx/2015_90/)
- ~4.8 hours (4h50m31s per the paper) of spontaneous speech — ~3.5 h of TV/radio talk shows plus ~30 min of re-transcribed TuDiCoI railway dialogues — manually transcribed in two orthographic versions (OTTA and CODA-TUN) with morpho-syntactic and disfluency annotation. Zribi, Ellouze, Hadrich Belguith, Blache, Research in Computing Science 90, 2015 (open access). The authors describe it as the first Tunisian resource with several annotation types.
- **[on request]** (via [Inès Zribi's resource page](https://sites.google.com/site/ineszribi/ressources/corpus)).

### [TunSwitch (TunSwitch-TO + TunSwitch-CS)](https://zenodo.org/records/8370566)
- Code-switching speech (SpeechBrain format). Ben Abdallah, Kabboudi, Kanoun, Zaiem (Tunis Business School, Univ. of Michigan-Dearborn, Abshore, Télécom Paris), 2023/2024.
- ~3h Tunisian-only + ~9h code-switched TN/FR/EN labeled, plus ~153h weakly-labeled audio (18 GB total), with language-level annotation. The paper's 4-gram KenLM rescoring model is **not** in the release (the Zenodo file list has no LM and no `TextData.zip`). A key open code-switching resource.
- Mirror: HF [tunis-ai/TunSwitch](https://huggingface.co/datasets/tunis-ai/TunSwitch). Paper: [arXiv:2309.11327](https://arxiv.org/abs/2309.11327) — the arXiv page says "submitted to ICASSP 2024"; later papers cite it as ICASSP 2024 (pp. 12607–12611), which was not verified against IEEE here, so it is cited as a preprint. **[open]** (CC-BY-4.0).

### [LinTO Audio & Textual Datasets for Tunisian Arabic](https://huggingface.co/datasets/linagora/linto-dataset-audio-ar-tn)
- ~93 hours of audio (~81.6h labeled), 20,895 files / ~76k segments; aggregated from YouTube, podcasts, MASC, TunSwitch, OneStory, etc. Naouara, Lorré, Louradour (LINAGORA Labs), 2025. The largest openly-packaged Tunisian ASR training collection.
- Companion [augmented set](https://huggingface.co/datasets/linagora/linto-dataset-audio-ar-tn-augmented) and a large text corpus. Paper: [arXiv:2504.02604](https://arxiv.org/abs/2504.02604). **[open]** (CC-BY-4.0).

### [TARIC-SLU](https://aclanthology.org/2024.lrec-main.1357/)
- Spoken language understanding extension of TARIC: ~8 hours, 2,043 dialogues / 17,816 utterances, railway dialogues annotated with 60 slot concepts. Mdhaffar, Bougares, de Mori, Zaiem, Ravanelli, Estève, LREC-COLING 2024. (The 108-speaker figure belongs to the original TARIC collection; the SLU splits list 5/39/38 speakers.)
- Project page: [elyadata/TARIC-SLU](https://github.com/elyadata/TARIC-SLU) (README + licence only, CC BY-NC 4.0); the SpeechBrain recipe lives in `speechbrain/recipes/TARIC`. The paper's download link (demo-lia.univ-avignon.fr) did not respond when checked (Sept 2026). **[open]** (CC BY-NC 4.0).

### [SLURP-TN](https://huggingface.co/datasets/Elyadata/SLURP-TN)
- Tunisian version of the SLURP SLU resource: ~5 hours, 4,165 sentences, 55 native speakers, 6 domains. Elleuch, Mdhaffar, Estève, Bougares (LIA Avignon + Elyadata), 2026.
- Paper: [LREC 2026, pp. 1544–1552](https://aclanthology.org/2026.lrec-1.119/) / [arXiv:2603.21940](https://arxiv.org/abs/2603.21940). **[open]** (HuggingFace; CC BY-NC-ND 4.0, research-only).

### [TEDxTN](https://huggingface.co/datasets/fbougares/TEDxTN)
- First publicly available Tunisian→English speech-translation corpus: 108 TEDx talks (~25 hours), code-switched Tunisian, speakers from 11+ regions; Tunisian transcript + English translation + annotation guidelines. Bougares, Mdhaffar, Elleuch, Estève, ArabicNLP 2025.
- Data: [fbougares/TEDxTN](https://huggingface.co/datasets/fbougares/TEDxTN) (HuggingFace, CC BY-NC-ND 4.0) ships the transcript/translation CSVs and a list of talk URLs — **the audio itself is not in the repo** and has to be fetched from the linked talks (the Hediske derivative below carries audio). Paper: [ACL](https://aclanthology.org/2025.arabicnlp-main.22/) / [arXiv:2511.10780](https://arxiv.org/abs/2511.10780). **[open]**.
- Derived, not new audio: [Hediske/tedxtn-tunisian-segmented](https://huggingface.co/datasets/Hediske/tedxtn-tunisian-segmented) — 16,895 utterance-level segments (`audio` + `sentence` + `duration`, ~2.77 GB) cut from TEDxTN for direct Whisper fine-tuning, 2025. Convenience re-segmentation of the corpus above; **no licence declared** on the derivative, so the parent terms should be assumed. Counting it separately would double-count TEDxTN.

### [TuniFra](https://huggingface.co/datasets/fbougares/TUNIFRA)
- The first open Tunisian↔French code-switch speech-translation corpus: 15 hours of native Tunisian speech, orthographically transcribed and manually translated into French, for ASR and Tunisian→French speech translation. Choux, Avila, Crego, Bougares, Laurent (+ Riguidel on the PDF byline), ArabicNLP 2025.
- Data: [fbougares/TUNIFRA](https://huggingface.co/datasets/fbougares/TUNIFRA) (HuggingFace). Paper: [ACL](https://aclanthology.org/2025.arabicnlp-main.5/) / [PDF](https://aclanthology.org/2025.arabicnlp-main.5.pdf).
- **[open]** (HuggingFace; CC BY-NC-ND 4.0).

### [TuDiCoI — Tunisian Dialect Corpus Interlocutor](https://huggingface.co/datasets/arbml/TuDiCoI)
- Spoken railway-ticket dialogue corpus (Derja), transcribed; the original is about 8 hours / 6,533 utterances (per the STAC and TARIC-SLU papers). The arbml HF mirror holds only 434 rows, one column, no card or licence. One of the earliest Tunisian dialogue resources.
- **[open]** (HuggingFace arbml mirror).
- Derived, not new dialogue: [samfatnassi/Tunisian-Railway-Dialogues](https://huggingface.co/datasets/samfatnassi/Tunisian-Railway-Dialogues) — TuDiCoI converted from the academic XML into JSONL chat turns (`system`/`user`/`assistant`) by Kilma.ai, filtered 1,825 → **1,720** dialogues, with an added SNCFT-staff system prompt. CC-BY-4.0, 2026. Useful if you want TuDiCoI in a shape that drops straight into LLM fine-tuning; the underlying speech data is the entry above, so it is a repackaging rather than new collection.

### [IWSLT 2022 Tunisian Conversational Speech (LDC2022E01 / LDC2025S05)](https://catalog.ldc.upenn.edu/LDC2025S05)
- Large three-way (audio + transcript + English translation) conversational telephone speech corpus, 210 h of audio (LDC), of which 175 h carry transcripts and English translations (the IWSLT task used 160 h); orthographic transcripts in Buckwalter transliteration, IPA on a subset; 8 kHz; 1,188 conversations collected 2016–2017. Basis of the IWSLT dialectal speech-translation task.
- Data-prep and scoring code is open: [kevinduh/iwslt22-dialect](https://github.com/kevinduh/iwslt22-dialect); task page [iwslt.org/2022/dialect](https://iwslt.org/2022/dialect). Example systems: [ON-TRAC (arXiv:2205.01987)](https://arxiv.org/abs/2205.01987), [CMU (IWSLT 2022)](https://aclanthology.org/2022.iwslt-1.27/).
- **[paywalled]** (LDC membership/fee).

### [TuniSpeech-21h](https://www.scitepress.org/Papers/2026/144577/144577.pdf)
- Multi-domain corpus: 21h 6m, 32,294 segments, 187 speakers (120 M / 67 F); social-media + broadcast (politics, sports, culture, cooking, etc.). Sghaier, Bellagha, Zrigui (Univ. of Monastir), ICAART 2026. Ships with a Wav2Vec2 vs Whisper benchmark (best: Whisper-large-v2, WER 24.74%).
- **[on request]** (corpus specs and eval protocol in the paper; fine-tuned model is public — see [MODELS.md](MODELS.md)).

### [OpenSLR SLR46 — Tunisian_MSA](https://www.openslr.org/46/)
- 11.2 hours of read/prompted utterances by 118 Tunisian speakers — but the **content is Modern Standard Arabic**, not Derja. Useful for Tunisian-accent MSA acoustic modeling only.
- **[open]** (Apache 2.0).

### [CALL MY NET 2 (CMN2) / 2018 NIST SRE (LDC2020S04)](https://catalog.ldc.upenn.edu/LDC2020S04)
- Tunisian Arabic conversational telephone speech (PSTN + VOIP, 8 kHz) collected by LDC in Tunisia via the Call My Net 2 protocol, plus English web-video audio from the VAST project. LDC gives **~396 hours for the release as a whole** — the Tunisian-only portion is not stated separately, so treat 396h as an upper bound, not a Tunisian figure.
- Collected for **speaker recognition** (NIST SRE18/19), not ASR or language modelling: no transcripts of the kind ASR training needs.
- **[paywalled]** (LDC; fee shown only after login).

### [Arbi-Houssem/Tunisian_dataset_STT-TTS15s_filtred1.0](https://huggingface.co/datasets/Arbi-Houssem/Tunisian_dataset_STT-TTS15s_filtred1.0)
- 1,103 rows (1,032 train / 71 validation) of timestamped Derja transcripts with a `speaker` id; the LinTO aggregate repackages 1,029 of them as ~3h50m. No card, no licence tag. Usable for STT and TTS. 2024.
- **[open]** (HuggingFace).

### [oddadmix/lahgtna-v3-small](https://huggingface.co/datasets/oddadmix/lahgtna-v3-small)
- Dialect-**balanced** multi-dialect Arabic ASR set: ~54.6k rows, 52k train / 2.6k test, 13 dialects including Tunisian, seed 42; columns `audio`, `transcript_text`, `language` (WER is scored on a normalised, undiacritised form of the text). Ahmed Wasfy (oddadmix), 2026.
- Tunisian is 200 clips in the held-out test split — small, but it is the balance that makes it useful: it supports **like-for-like comparison of Tunisian against twelve other Arabic dialects under identical conditions**, which very few Tunisian resources allow. See the per-dialect WER table in [MODELS.md](MODELS.md#asr-models).
- **[open]** (no licence tag).

### [FARUKxAUTO/tunisian-asr-cleaned](https://huggingface.co/datasets/FARUKxAUTO/tunisian-asr-cleaned)
- Tunisian ASR set, **46,034 train / 5,415 validation / 2,707 test** (54,156 rows), 16 kHz audio paired with a `sentence` transcript. ~15.7 GB. Uploaded 16 Mar 2026. On size alone this is one of the largest Tunisian ASR sets listed here, and it is essentially undiscovered (a few dozen downloads when checked).
- Identified as the training data behind [oddadmix/Whisperv3-tunisian-codeswitch](MODELS.md#asr-models), where Ahmed Wasfy describes it as **dense Tunisian↔French code-switch**. That characterisation comes from the model card, not from this dataset's own documentation.
- ⚠️ **Flagged, not vouched for.** The repo has **no dataset card, no license, and no stated provenance** — the author `FARUKxAUTO` publishes nothing else identifying. Given the size, it may aggregate or re-clean existing corpora (TunSwitch, TEDxTN, Common Voice and others are all plausible components), which would mean it double-counts resources already listed above. **Anyone using it should establish provenance first**, and it is recorded here as an unverified entry rather than dropped, per this registry's practice of flagging uncertainty instead of hiding it.
- Ungated, downloadable, parquet. **[open]** (access only; licence and provenance unstated).

### [oddadmix/arabic-audio-collection-tunisian-deep-confessions](https://huggingface.co/datasets/oddadmix/arabic-audio-collection-tunisian-deep-confessions)
- **37,156** transcribed chunks (~175 hours per the card), ~20.0 GB, 16 kHz, segmented from the *Deep Confessions* podcast (Tunisian; the card names the show, not the platform). Fields: `chunk_id`, `audio`, `transcript_text`, `duration`, `original_video_id`. Ahmed Wasfy (oddadmix), 2026.
- **The register is the reason to care.** Transcripts are spontaneous, emotional, first-person speech with dense French/English code-switching and explicit paralinguistic markers — the card lists 18 tags (`<laugh>`, `<cry>`, `<sigh>`, `<pause>`, `<hes>`, `<breath>`, `<cough>`…) — e.g. *"ااه ردبلت وعاودت الباك اللول والباك الثاني خذيته مره ثالثه دونك `<pause>`"*. Nothing else listed here covers this register: TEDxTN is prepared oratory, TARIC/TuDiCoI are task-oriented service dialogues, LinTO is aggregated broadcast and podcast material.
- The card contradicts itself on speakers ("Number of Speakers: 10" in the table, "a single speaker" in the prose); transcripts are AI-assisted and creator-curated.
- ⚠️ Licence is declared as `other` with **no terms given**, and the audio is YouTube-derived from a confessional show — speaker consent for onward redistribution is not documented. Establish terms before any published use.
- **[open]** (access only; licence `other`, terms unstated).

### [Fares11/senior_tunisian_voice](https://huggingface.co/datasets/Fares11/senior_tunisian_voice)
- **5,377** rows, ~2.39 GB. Fields: `audio_id`, `audio`, `transcript`, plus a nested `segments` list carrying `start`/`end` and **both** `transcript` and `transcript_raw` per segment. Apache-2.0, 2026.
- The dual normalised/raw transcript layer is the useful part: it makes the set usable for orthographic normalisation and Derja spelling-variation work, not only ASR. Transcripts are heavily code-switched Tunisian–French (*"و كانت شوية des cliques أنا حتى فال période لي فاتت طلعت مع taxist"*).
- ⚠️ **No dataset card** beyond the YAML header: no stated provenance, speaker count, or collection method. Content references Tunisian media (Mosaïque FM among others), so it is plausibly broadcast- or podcast-sourced, but that is inference from the transcripts, not documentation. The repo name implies elderly speakers; **nothing in the repo confirms a senior-speaker demographic**, which would be a genuine gap-filler if it were documented.
- Its schema matches LinTO's and 5,377 equals LinTO's TunSwitch-CS train count, so it may be a repackaging of data already listed above — unconfirmed.
- **[open]** (Apache-2.0; provenance undocumented).

### Undocumented community audio sets
- [safara/TunisianOnly](https://huggingface.co/datasets/safara/TunisianOnly) — an `audio_files/` directory of `.wav` clips (~92 MB total; file count not verified) with `train.csv` / `dev.csv` / `test.csv` carrying `filename`, `transcription` and `duration` columns, i.e. **transcripts exist**, but the header casing differs between splits, which breaks the HF viewer. ⚠️ No dataset card and no licence, May 2025. Recorded here flagged rather than omitted. **[open]** (access only; no licence).

---

## Text-to-speech (TTS)

### [TunArTTS — Tunisian Arabic Text-To-Speech Corpus](https://aclanthology.org/2024.lrec-main.1467/)
- First Tunisian TTS resource: 3+ hours, single male speaker, 44.1 kHz, manually diacritized. Laouirine, Kammoun, Bougares, LREC-COLING 2024. Tacotron2 + FastSpeech2 baselines (best MOS 3.88 via transfer from LJSpeech).
- Repo: [elyadata/TunArTTS](https://github.com/elyadata/TunArTTS) (scraping/preprocessing + ESPnet scripts; CC BY-NC 4.0). **[open]** (research, non-commercial).

### [Habibi — Unified-Dialectal Arabic Speech Synthesis](https://arxiv.org/abs/2601.13802)
- Multi-dialect Arabic TTS framework + benchmark (12+ dialects, zero-shot voice cloning). Code: [SWivid/Habibi-TTS](https://github.com/SWivid/Habibi-TTS). Tunisian (`TUN`) is a supported inference dialect but **not** one of the 7 benchmark subsets (MSA, SAU, UAE, ALG, IRQ, EGY, MAR). Code MIT; released models CC BY-NC-SA 4.0. **[open]** (Tunisian supported, not benchmarked).

### Community and commercial Tunisian TTS
- [SpeechGen Tunisian TTS (ar-TN)](https://speechgen.io/en/tts-arabic-tunisia/) — commercial text-to-speech with Tunisian voices (e.g., Hedi, Reem). Not open/research; noted for completeness. **[commercial]**.
- Community fine-tunes and TTS-oriented sets on HuggingFace: the [Arbi-Houssem/Tunisian_dataset_STT-TTS](https://huggingface.co/datasets/Arbi-Houssem/Tunisian_dataset_STT-TTS15s_filtred1.0) series, [kalil99x/fixed-tts-tunisian](https://huggingface.co/datasets/kalil99x/fixed-tts-tunisian2) series (2025), [deepdml/Tunisian_MSA](https://huggingface.co/datasets/deepdml/Tunisian_MSA) (Sept 2025; tagged ASR rather than TTS). **[open]** (quality varies).
- [AnanOmri/hamza-belloumi-tunisian-tts](https://huggingface.co/datasets/AnanOmri/hamza-belloumi-tunisian-tts) — 1,784 single-voice clips (~415 MB) segmented from YouTube, 2026. ⚠️ **Tagged `text-to-speech` but ships an `audio` column and no transcript column at all**, so it cannot train TTS as published; it is unaligned audio. No licence declared, and it targets a named public figure's voice, which raises the same consent question the SILMA-Derja card addresses explicitly (see [MODELS.md](MODELS.md#tts-models)). **[open]** (access only; no transcripts, no licence).
- [amenIKh/Tunisian_TTS](https://huggingface.co/amenIKh/Tunisian_TTS) — XTTS-v2 fine-tuned on ~2 h 30 of custom Tunisian audio, 2025. Card reports only training/eval **loss** (0.0274 / 0.0946), which says nothing about intelligibility or naturalness; no MOS, no WER-of-synthesis, no licence. **[open]** (weights; licence unstated).

---

## Speech / spoken dialect identification

### [ADI-20 — Arabic Dialect Identification dataset](https://arxiv.org/abs/2511.10070)
- 3,556 hours across 19 dialects + MSA; expands ADI-17 and explicitly **adds Tunisian**. Elleuch et al., Interspeech 2025. The first large spoken-ADI set to include Tunisian.
- **[open]** (paper + [manifests and YouTube IDs on GitHub](https://github.com/elyadata/ADI-20); the audio itself is not shared "for licencing reasons").

### [Text and Speech-based Tunisian Sub-Dialects Identification (LREC 2020)](https://aclanthology.org/2020.lrec-1.787/)
- Distinguishes Tunisian sub-dialects (Tunis / Sfax / Sousse / Tataouine) from text and speech; the spoken corpus (1,673 utterances) is described as freely distributed. Ben Abdallah, Kchaou, Bougares. **[open]** (paper).

---

## Speech benchmark and encoder analyses

- [Performance Analysis of Speech Encoders for Low-Resource SLU and ASR in Tunisian Dialect (ArabicNLP 2024)](https://aclanthology.org/2024.arabicnlp-1.12/) — Mdhaffar, Elleuch, Bougares, Estève. SSL encoders evaluated on TARIC-SLU. **[open]**.
- [Tunisian Dialectal End-to-end ASR based on DeepSpeech (Procedia 2021)](https://www.sciencedirect.com/science/article/pii/S1877050921011984) — Messaoudi et al., Procedia CS 189, pp. 183–190 (CC BY-NC-ND). **[open]**.

---

## Speech shared tasks

### [NADI 2025 — First Multidialectal Arabic Speech Processing Shared Task](https://arxiv.org/abs/2509.02038)
- Subtask 1: spoken dialect ID over eight dialects (Algeria, Egypt, Jordan, Mauritania, Morocco, Palestine, UAE, Yemen — **Tunisian not included**; the winning team pre-trained on ADI-20); Subtask 2: multidialectal ASR; Subtask 3: diacritic restoration. Talafha et al., 2025.
- Winning system: [ELYADATA & LIA at NADI 2025 (arXiv:2511.10090)](https://arxiv.org/abs/2511.10090) — ADI 1st (79.83%), ASR 2nd. **[open]** (task papers; task data via the organizers).

### [NADI 2026 — Multidialectal Arabic Speech Processing](https://nadi.dlnlp.ai/2026/)
- Speech-focused, and strongly Tunisian-relevant. Tasks include country-level / mixed / **code-switched ASR** (subtask 1.3 is Tunisian⇄English⇄French code-switching), spoken dialect ID, dialectal TTS, spoken language translation (8 dialects→English, none Tunisian), and SLU (intent + slot filling).
- Timeline per the task page: registration opened May 16, data June 16, blind test July 20, 2026. Organised by UBC, KFUPM, Elyadata, KAUST, Avignon Université and NYUAD (Sullivan, Talafha, Ashraf, Bougares, Elleuch, Mdhaffar, Estève, Habash, Abdul-Mageed et al.).
- Tunisian training data released for the task (Fethi Bougares' HuggingFace): [fbougares/NADI_TUN_ASR_2026](https://huggingface.co/datasets/fbougares/NADI_TUN_ASR_2026) (26,466 rows: 24,893 / 731 / 842 — the dev/test counts match the TEDxTN splits; YAML-only card) and [fbougares/NADI_Whitehouse_AST_2026](https://huggingface.co/datasets/fbougares/NADI_Whitehouse_AST_2026) (speech translation). **[open]**.

### [SLURP-TN baselines](https://github.com/elyadata/SLURP-TN-baselines)
- Baseline SpeechBrain recipes for the SLURP-TN dataset. Elyadata. **[open]** (GitHub).

### [IWSLT 2022 / 2023 dialectal speech translation](https://iwslt.org/2022/dialect)
- Tunisian→English speech translation task (the 2023 edition ran under the [low-resource track](https://iwslt.org/2023/low-resource)). Data prep/scoring: [kevinduh/iwslt22-dialect](https://github.com/kevinduh/iwslt22-dialect). **[open]** (scripts); the underlying audio is the LDC Tunisian conversational corpus listed above, which is **[paywalled]**.

---

## Confirmed negatives

Checked and found to contain **no Tunisian data**, recorded so that effort is not wasted re-checking. A negative result is a result: knowing where Tunisian *isn't* saves as much time as knowing where it is.

- **Mozilla Common Voice** — no dedicated Tunisian-dialect subset; Arabic is collected under a single label (as the NADI 2025 overview also notes).
- **MGB-3** (Egyptian) and **MGB-5** (Moroccan) — no Tunisian data.
- **Casablanca** multidialectal ASR (EMNLP 2024) — covers 8 Arabic dialects; **Tunisian is not one of them**.
- **DialectalArabicMMLU** ([arXiv:2510.27543](https://arxiv.org/abs/2510.27543), LREC 2026) — manually translated MMLU-Redux into five dialects (Syrian, Egyptian, Emirati, Saudi, Moroccan). **Tunisian is not among them.** Text rather than speech, listed here because it is the most common false assumption about Arabic dialect benchmark coverage.
- **Global MMLU** ([arXiv:2412.03304](https://arxiv.org/abs/2412.03304)) — 42 languages with human-verified translations; Arabic is included as a single language, with no dialect variants. Its own limitations section states that dialects are out of scope: *"Future work is needed … to take into account how technology serves different dialects (a topic we do not address here)."*
