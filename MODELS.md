# Tunisian Arabic Models

Pretrained language models, ASR models, and TTS models for Tunisian Arabic (`aeb`). Datasets are in [README.md](README.md) and [SPEECH.md](SPEECH.md). Access legend is defined in [README.md](README.md).

## Contents

- [Generative / instruction / chat LLMs](#generative--instruction--chat-llms)
- [Pretrained text language models (encoders, Tunisian-specific)](#pretrained-text-language-models-encoders-tunisian-specific)
- [General Arabic models that include Tunisian](#general-arabic-models-that-include-tunisian)
- [ASR models](#asr-models)
- [TTS models](#tts-models)
- [Dialect identification](#dialect-identification)
- [OCR](#ocr)

---

## Generative / instruction / chat LLMs

Until recently there was no open Tunisian decoder LLM. As of 2025–2026 several exist. They are early, small, and (by their own model cards) not reliably factual, but the space is genuinely open and moving fast.

### [Labess-7b-chat](https://huggingface.co/linagora/Labess-7b-chat-16bit)
- Instruction-tuned Tunisian Derja chat model. Wajdi Ghezaiel and Jean-Pierre Lorré (LINAGORA), 2025. 7B, Apache-2.0.
- Continual pre-training of `inceptionai/jais-adapted-7b-chat` on [linagora/Tunisian_Derja_Dataset](https://huggingface.co/datasets/linagora/Tunisian_Derja_Dataset) (2.23M-row Derja corpus). Trained on the Jean Zay supercomputer (GENCI/IDRIS).
- Variants: [Labess-7b-chat](https://huggingface.co/linagora/Labess-7b-chat), [Labess-7b-chat-16bit](https://huggingface.co/linagora/Labess-7b-chat-16bit), [Labess-7b-chat-gguf](https://huggingface.co/linagora/Labess-7b-chat-gguf), plus a community quant [tensorblock/Labess-7b-chat-16bit-GGUF](https://huggingface.co/tensorblock/Labess-7b-chat-16bit-GGUF). **[open]**.

### [ESPRIT-Derja-Qwen3-8B-v2](https://huggingface.co/ESPRIT-Group/ESPRIT-Derja-Qwen3-8B-v2)
- Tunisian instruct model. ESPRIT School of Engineering (Mourad Zerai), 2026. Qwen3-8B + LoRA (rank 32) on 7,013 Arabic/Arabizi Tunisian instruction examples (ESPRIT-Derja-Instruct: 3,494 GPT-4o-distilled pairs in both scripts + 25 manual; not yet released separately). The first Tunisian instruct model that explicitly handles Arabizi (3=ع, 7=ح, 9=ق…). Apache-2.0.
- Card is honest that it is conversation-optimized, not factually reliable. Earlier version: [ESPRIT-Derja-8B-v1](https://huggingface.co/ESPRIT-Group/ESPRIT-Derja-8B-v1) (README only, no weights). **[open]**.

For the datasets that train and evaluate these models (Tunisian_Derja_Dataset, TunisianMMLU, the wghezaiel SFT/DPO stack, synthetic instruction sets), see the [LLM training and evaluation datasets](README.md#llm-training-and-evaluation-datasets) section of the README.

---

## Pretrained text language models (encoders, Tunisian-specific)

### [TunBERT](https://github.com/instadeepai/tunbert)
- The canonical Tunisian BERT. iCompass + InstaDeep, 2021. BERT-base architecture (12 layers, 768 hidden; the HF conversion has 110M params), pretrained on ~500k Tunisian social-media comments (~67 MB Common-Crawl-based).
- First pretrained BERT for Tunisian; evaluated on sentiment, Tunisian dialect ID, and reading-comprehension QA (SOTA at the time). Two mirrors, each shipping both the PyTorch/NeMo and the TensorFlow checkpoints: [instadeepai/tunbert](https://github.com/instadeepai/tunbert) (archived read-only Jun 2026) and [iCompass-ai/TunBERT](https://github.com/iCompass-ai/TunBERT). MIT.
- Paper: [arXiv:2111.13138](https://arxiv.org/abs/2111.13138); refereed version: [SN Computer Science 4(2):194, 2023](https://link.springer.com/article/10.1007/s42979-022-01541-y). **[open]**.

### [tunis-ai/TunBERT](https://huggingface.co/tunis-ai/TunBERT)
- HF-hosted, ready-to-use conversion of TunBERT (NeMo → safetensors) wired for `transformers` text classification (tagged `dataset:tsac`; the card reports no fine-tuning numbers). The most-downloaded TunBERT on the Hub. ~0.1B params, MIT. **[open]**.

### [ziedsb19/tunbert_zied](https://huggingface.co/ziedsb19/tunbert_zied)
- Independent Tunisian RoBERTa-style masked LM. Zied Sbabti, 2021. Trained on ~600,000 Tunisian phrases; handles Arabizi (use `BertTokenizer`, not `AutoTokenizer`). **[open]**.

### [hamzabouajila/distilled_tunbert](https://huggingface.co/hamzabouajila/distilled_tunbert)
- Distilled TunBERT (DistilBERT student, ~66M params, ~1.83× faster). Hamza Bouajila, 2025. Teacher = tunis-ai/TunBERT; trained on the open [tunisian-derja-unified-raw-corpus](https://huggingface.co/datasets/hamzabouajila/tunisian-derja-unified-raw-corpus). Good for classification, not embeddings (card is honest about this). MIT. **[open]**.

---

## General Arabic models that include Tunisian

Not Tunisian-specific — Tunisian appears only as part of pan-Arabic dialect data. Useful as baselines or fine-tuning bases.

- [MARBERT / MARBERTv2](https://huggingface.co/UBC-NLP/MARBERT) (UBC-NLP) — dialectal + MSA BERT trained on 1B tweets. Covers Tunisian as part of pan-Arabic data.
- [CAMeLBERT-DA](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da) (CAMeL Lab) — dialectal-Arabic BERT trained on 54 GB from 28 dialect corpora; includes Tunisian corpora among many.
- [AraBERT / AraGPT2 / AraELECTRA](https://github.com/aub-mind/arabert) (AUB MIND) — primarily MSA; AraBERTv0.2-Twitter adds dialect/tweet coverage.
- [DziriBERT](https://github.com/alger-ia/dziribert) (Algerian) and DarijaBERT (Moroccan) — **not Tunisian**, but the same monodialectal North-African BERT lineage as TunBERT; included for regional context.

---

## ASR models

### [SalahZa/Tunisian_Automatic_Speech_Recognition](https://huggingface.co/SalahZa/Tunisian_Automatic_Speech_Recognition)
- SpeechBrain semi-supervised WavLM-large + CTC. Ben Abdallah, Kabboudi, Kanoun, Zaiem, 2023 (no licence tag on the repo). WER/CER: TARIC 10.55/6.22, IWSLT 39.53/21.18, TunSwitch-TO 25.54/9.67. [Demo](https://huggingface.co/spaces/SalahZa/Tunisian-Speech-Recognition). Paper [arXiv:2309.11327](https://arxiv.org/abs/2309.11327). **[open]**.

### [SalahZa/Code_Switched_Tunisian_Speech_Recognition](https://huggingface.co/SalahZa/Code_Switched_Tunisian_Speech_Recognition)
- Code-switched ASR (wav2vec2 TN/FR/EN, SpeechBrain). WER/CER: TunSwitch-CS 29.47/12.44. [Demo](https://huggingface.co/spaces/SalahZa/Code-Switched-Tunisian-SpeechToText) (Space in runtime error when checked, Sept 2026). Apache-2.0. **[open]**.

### [linagora/linto-asr-ar-tn-0.1](https://huggingface.co/linagora/linto-asr-ar-tn-0.1)
- Kaldi TDNN / Vosk + SRILM LM. LINAGORA, uploaded Sept 2024 (paper 2025). WER/CER: TARIC 16.06/10.60, TunSwitch-CS 20.51/17.72, TunSwitch-TO 22.54/11.13. Android/Raspberry-Pi variant. Training code: [linagora-labs/ASR_train_kaldi_tunisian](https://github.com/linagora-labs/ASR_train_kaldi_tunisian). Apache-2.0. **[open]**.

### [TuniSpeech-AI/whisper-tunisian-dialect](https://huggingface.co/TuniSpeech-AI/whisper-tunisian-dialect)
- Whisper-large-v2 fine-tuned (LoRA merged; 1.54B params). Sghaier, Bellagha, Zrigui, 2026. WER 24.74 / CER 8.32 on TuniSpeech-21h — the figures are on the dataset card, not the model card. [Demo](https://huggingface.co/spaces/TuniSpeech-AI/TuniSpeech-Model). cc-by-nc-4.0. **[open]** (weights).

### [oddadmix/whisper-large-v3-arabic-dialectal-v2](https://huggingface.co/oddadmix/whisper-large-v3-arabic-dialectal-v2)
- Whisper-large-v3 (1.54B) fine-tuned for **13 Arabic dialects**, Tunisian among them. Ahmed Wasfy (oddadmix), 2026. Trained on [`oddadmix/lahgtna-v3-small`](https://huggingface.co/datasets/oddadmix/lahgtna-v3-small) (52k train / 2.6k test, dialect-balanced).
- **The per-dialect evaluation is the useful part for Tunisian NLP.** On a balanced test of 200 held-out clips per dialect, Tunisian is the hardest of all 13: **WER 0.478 / CER 0.193**, against an overall 0.320 and Saudi/Gulf 0.169. Ordering (easiest → hardest): Gulf 0.169, Iraqi 0.254, Egyptian 0.271, Syrian 0.272, Palestinian 0.301, Yemeni 0.304, Lebanese 0.317, Moroccan 0.340, Libyan 0.343, Bahraini 0.348, Algerian 0.386, Sudanese 0.399, **Tunisian 0.478**.
- The card reports overall WER for eight fine-tuned models (Whisper large/turbo/medium/small, Nemotron, Qwen3-ASR, Cohere) and states that Maghrebi (Tunisian/Algerian/Moroccan) is the hardest group "across every model"; per-dialect tables are given for this model only.
- Apache-2.0. **[open]**. Sibling models in the [Arabic ASR Models collection](https://huggingface.co/collections/oddadmix/arabic-asr-models) (13 items).

### [oddadmix/Whisperv3-tunisian-codeswitch](https://huggingface.co/oddadmix/Whisperv3-tunisian-codeswitch)
- Whisper-large-v3 **full** fine-tune (1.54B params) for Tunisian ↔ French/English **code-switched** ASR, built for **NADI 2026 subtask 1.3**. Ahmed Wasfy (oddadmix), uploaded 28 Jul 2026.
- **Final NADI 2026 test leaderboard (CodaBench, read 29 Aug 2026): 6th of 9 entries at WER 15.21 (CER 5.86); the winning entry scored 14.41.** The card's own "third place blind test" claim reflects an earlier leaderboard state and is superseded. Author-reported validation: WER 17.26 / CER 6.91. Trained on [`FARUKxAUTO/tunisian-asr-cleaned`](SPEECH.md#speech-corpora-asr--slu--speech-translation) (46k, dense TN↔FR code-switch) plus NADI TEDx train replay; 2 epochs, spec-augment, lr 5e-6. Greedy decode with `language="ar"`.
- **Why it matters here:** it is the counter-evidence to the dialect-difficulty reading of the 13-dialect model above. Tunisian scored worst of 13 there (WER 0.478) on a model split across every dialect; a Tunisian-focused fine-tune with code-switch data scored 15.21 on the NADI 2026 final test leaderboard (winner: 14.41). The gap looks like allocation of training data and capacity, not intrinsic difficulty of the dialect.
- ⚠️ **Not comparable to the SalahZa code-switched numbers above** — those are TunSwitch-CS, these are the NADI 2026 blind test. Different test sets, no shared reference point published.
- ⚠️ **No license declared** on the repo (the base Whisper-large-v3 is Apache-2.0, but this fine-tune states nothing), and the card's usage snippet still points at a differently-named repo (`nadi2026-subtask1.3-...-faruk-v7`), so it appears to be a rename or mirror. Weights are present and ungated. **[open]** (weights; licence unstated).

### [medfadiabaidi/whisper-small-tunisian-asr](https://huggingface.co/medfadiabaidi/whisper-small-tunisian-asr)
- `openai/whisper-small` (244M) fine-tuned on [TEDxTN](SPEECH.md#speech-corpora-asr--slu--speech-translation). Declared in the card's `model-index`: **WER 37.99 / CER 18.77** on the TEDxTN test split. 2025.
- **Why it is worth listing despite the modest score:** it is the only entry here reporting WER on the *TEDxTN test split*, so it supplies a reference point on a corpus that is open, code-switched, and widely available — unlike TARIC (on request) or the NADI blind sets (not public). The card cites TEDxTN as ~22 h against the ~25 h given in the corpus entry; the discrepancy is unexplained.
- **It also ships the baseline it beat**, which is the more broadly useful artefact. `baseline_results.csv` commits per-utterance reference/prediction pairs with WER/CER for the untuned `whisper-small` on the same 842 TEDxTN test utterances, and the repo's `summary.json` states the corpus-level result: **baseline WER 116.2% / CER 83.5%** against 37.99 / 18.77 after fine-tuning (15,703 training samples, 15 epochs). The first row alone is a repetition-loop output at 386% WER. That file is the concrete evidence behind the out-of-the-box degradation note at the end of this section.
- ⚠️ **No licence declared** (base `whisper-small` is Apache-2.0, but this fine-tune states nothing). Checkpoint shards and TensorBoard logs are committed alongside the final weights. **[open]** (weights; licence unstated).

### Classic ASR systems (papers)
- [ASR system for Tunisian dialect (Kaldi, TARIC), LRE 2018](https://link.springer.com/article/10.1007/s10579-017-9402-y) — Masmoudi, Bougares, Ellouze, Estève, Belguith; LRE 52, pp. 249–267. WER 22.6% (abstract). **[paywalled]** (preprint on [ResearchGate](https://www.researchgate.net/publication/319988998)).
- [Tunisian Dialectal End-to-end ASR based on DeepSpeech (Procedia 2021)](https://www.sciencedirect.com/science/article/pii/S1877050921011984) — Messaoudi et al., Procedia CS 189, pp. 183–190. **[open]** (CC BY-NC-ND).

Note: general Arabic XLSR/Whisper models (e.g., jonatasgrosman/wav2vec2-large-xlsr-53-arabic) are used as Tunisian baselines but degrade sharply out-of-the-box. Not Tunisian-specific. Published per-utterance evidence for this is scarce, but [`medfadiabaidi/whisper-small-tunisian-asr`](#medfadiabaidiwhisper-small-tunisian-asr) commits a `baseline_results.csv` of untuned `whisper-small` on 842 TEDxTN test utterances, with a corpus-level **baseline WER of 116.2%** (its `summary.json`). WER above 100% means the failure mode is **repetition-loop collapse** rather than graceful degradation (the file's first utterance scores 386%), so corpus-level averages over untuned Arabic Whisper are dominated by degenerate outputs rather than by typical performance — worth knowing when picking a baseline.

---

### [KBayoud/qwen3-asr-tunisian-telephony-augmented](https://huggingface.co/KBayoud/qwen3-asr-tunisian-telephony-augmented)
- Qwen3-ASR (`Qwen3ASRForConditionalGeneration`) fine-tune, uploaded 4 Aug 2026 (KBayoud). **No model card at all** — "Tunisian telephony, augmented" is the repo name, nothing more is documented. **[gated]** (manual approval required for the weights).

### Community Whisper fine-tunes for Tunisian (Jul–Aug 2026, grouped)
- Small community ASR releases, grouped in one entry: [awaxsama/whisper-small-tunisian-arabic](https://huggingface.co/awaxsama/whisper-small-tunisian-arabic) and [whisper-tiny-tunisian-arabic](https://huggingface.co/awaxsama/whisper-tiny-tunisian-arabic) (Aug 2026, Apache-2.0, trained on [linagora/linto-dataset-audio-ar-tn-augmented](https://huggingface.co/datasets/linagora/linto-dataset-audio-ar-tn-augmented)) · [maxvu0/whisper-large-v2-tunisian-lora](https://huggingface.co/maxvu0/whisper-large-v2-tunisian-lora) (17 Aug 2026, LoRA adapter; licence "[More Information Needed]").
- Evaluation: the awaxsama repos commit an `evaluation/final_metrics.json` — aggregate WER 0.389 (small) and 0.622 (tiny) over TunSwitch-CS/TO and one other set — while their cards headline much lower in-training eval WERs; maxvu0 publishes none. The whisper-tiny card names no training set. The steady stream of such releases is itself a signal that the LinTO/TunSwitch training sets are being used. (houssemtn/whisper-tiny-tunisian-onthefly, previously grouped here, is an empty repo and was dropped.) **[open]** (weights on all three).

## TTS models

### [oddadmix/lahgtna-omnivoice-v2 (لهجتنا)](https://huggingface.co/oddadmix/lahgtna-omnivoice-v2)
- Multi-dialect Arabic TTS built on OmniVoice (Qwen3-0.6B backbone; 0.6B params), aiming at a single unified model across Arabic dialects. Ahmed Wasfy (oddadmix), 2026. **Tunisia is ticked on the dialect roadmap**, alongside Egypt, Saudi, Morocco, Iraq, Sudan, Palestine, Lebanon, Syria, Libya, Bahrain, Yemen, Algeria.
- Trained on roughly **250 hours of speech across all supported dialects** (author's figure, in conversation); the Tunisian-only share is not published. Supports diacritized Arabic input for pronunciation. Code: [Oddadmix/Lahgtna-OmniVoice](https://github.com/Oddadmix/Lahgtna-OmniVoice). [Demo Space](https://huggingface.co/spaces/oddadmix/Lahgtna-OmniVoice-Demo).
- **[open]** (no licence tag on the repo). Per-dialect TTS quality for Tunisian is not separately evaluated — treat as "Tunisian supported", not "Tunisian validated".

- [TunArTTS](https://github.com/elyadata/TunArTTS) baselines (Tacotron2, FastSpeech2) — see [SPEECH.md](SPEECH.md). **[open]** (research).
- [Habibi-TTS](https://github.com/SWivid/Habibi-TTS) — multi-dialect Arabic TTS; Tunisian is a supported dialect ID but not one of its 7 benchmark subsets. **[open]**.
- Community/commercial Tunisian TTS (SpeechGen, community fine-tunes) — see [SPEECH.md](SPEECH.md#text-to-speech-tts).

### [Ghazouaniwala/silma-tts-derja](https://huggingface.co/Ghazouaniwala/silma-tts-derja-v2) (series)
- F5-TTS Tunisian Derja fine-tunes of [silma-ai/silma-tts](https://huggingface.co/silma-ai/silma-tts), trained on the [LinTO Tunisian audio dataset](SPEECH.md#speech-corpora-asr--slu--speech-translation). Apache-2.0. Five repos uploaded Jul 2026: `silma-tts-derja`, `-v2`, `-v2-1`, `-v3a`, `-v4a`.
- **Documented recipe, which is rare in this corner of the ecosystem.** The v2 card states the deliberate choices: `speaker_mode=single` (speaker `AbdelAzizErwi`), moderate text normalisation, SNR ≥ 15.0 dB audio-quality filtering, phonemisation disabled, 40 epochs — framed explicitly as improving the *signal* rather than the architecture. One `model.pt` per repo (the raw-vs-EMA A/B exists only as sample WAVs, not as separate weights). Load via the F5-TTS v1.1.7 / SILMA pipeline (`model.pt` + `vocab.txt` + `config.yaml`).
- Carries correct CC-BY attribution to the LinTO dataset ([arXiv:2504.02604](https://arxiv.org/abs/2504.02604)) and an explicit responsible-use clause requiring documented speaker consent for voice cloning — worth noting given how many voice datasets in this map ship neither.
- ⚠️ **No evaluation published**: no MOS, no synthesis-WER, no A/B results despite the card referencing them. Treat as "Tunisian TTS trained on open Tunisian data with a legible recipe", not as validated quality. The v3a and v4a cards keep the "v2 recipe" heading but change the recipe lines: multi-speaker, SNR ≥ 8.0 dB, 30 epochs (v3a) / 40 epochs (v4a).
- **[open]** (Apache-2.0).

---

### [Mui17/tunisian-xtts-v1](https://huggingface.co/Mui17/tunisian-xtts-v1)
- XTTS-based Tunisian TTS, uploaded 14 Aug 2026, Apache-2.0 (Mui17). Community release; no published evaluation. **[open]**.

## Dialect identification

*Trained models only. The **datasets and benchmarks** for Arabic dialect ID (MADAR, NADI, IADD, QADI, the LREC 2018 shared task, and Tunisian sub-dialect ID) are in [README.md § Dialect identification (text)](README.md#dialect-identification-text); **speech-based** dialect ID is in [SPEECH.md](SPEECH.md).*

### [oddadmix/dialect-router-v0.2](https://huggingface.co/oddadmix/dialect-router-v0.2)
- Arabic dialect identification: text classification into **15 labels — 13 Arabic dialects, MSA, and English**. Tunisian is label `tn`. Ahmed Wasfy (oddadmix), 2026. Fine-tune of [`asafaya/bert-mini-arabic`](https://huggingface.co/asafaya/bert-mini-arabic); **11.6M parameters**, 512-token input. Built as the routing backbone of the Lahgtna TTS pipeline, but usable standalone.
- Reported on the model card: **accuracy 0.9359, macro-F1 0.9052** across all 15 classes. **The macro-F1 is the figure to quote** — with uneven label distribution, overall accuracy flatters. **No per-dialect breakdown is published, so Tunisian-specific performance is unknown.**
- The card's own stated limitations land on Tunisian specifically: *"Code-switched text (e.g. Arabic + French in Maghrebi dialects, or Arabic + English) may confuse the classifier; heavily mixed input may be routed to `en`"* — and Tunisian is named in the adjacent-dialect confusion group (`ma / dz / tn`). Both matter for Derja, which is routinely French-code-switched.
- v0.2 expands 10 → 13 dialects (adds Bahraini, Algerian, Yemeni), adds an English label, renames `mo` → `ma`.
- MIT licence (stated in the card body; no `license:` metadata tag). **[open]**.

---

## OCR

### [Ghazouaniwala/trocr-tunisian-arabic](https://huggingface.co/Ghazouaniwala/trocr-tunisian-arabic)
- TrOCR fine-tune for Tunisian Arabic text recognition, uploaded 2 Aug 2026 (Ghazouaniwala). The registry's first OCR entry; the repo has no model card and no licence tag (checked 4 Sept 2026). **[open]**.
