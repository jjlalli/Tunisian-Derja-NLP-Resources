# Tunisian Arabic Models

Pretrained language models, ASR models, and TTS models for Tunisian Arabic (`aeb`). Datasets are in [README.md](README.md) and [SPEECH.md](SPEECH.md). Access legend is defined in [README.md](README.md).

## Contents

- [Generative / instruction / chat LLMs](#generative--instruction--chat-llms)
- [Pretrained text language models (encoders, Tunisian-specific)](#pretrained-text-language-models-encoders-tunisian-specific)
- [General Arabic models that include Tunisian](#general-arabic-models-that-include-tunisian)
- [ASR models](#asr-models)
- [TTS models](#tts-models)

---

## Generative / instruction / chat LLMs

Until recently there was no open Tunisian decoder LLM. As of 2025–2026 several exist. They are early, small, and (by their own model cards) not reliably factual, but the space is genuinely open and moving fast.

### [Labess-7b-chat](https://huggingface.co/linagora/Labess-7b-chat-16bit)
- Instruction-tuned Tunisian Derja chat model. Wajdi Ghezaiel and Jean-Pierre Lorré (LINAGORA), 2025. 7B, Apache-2.0.
- Continual pre-training of `inceptionai/jais-adapted-7b-chat` on [linagora/Tunisian_Derja_Dataset](https://huggingface.co/datasets/linagora/Tunisian_Derja_Dataset) (2.23M-row Derja corpus). Trained on the Jean Zay supercomputer (GENCI/IDRIS).
- Variants: [Labess-7b-chat](https://huggingface.co/linagora/Labess-7b-chat), [Labess-7b-chat-16bit](https://huggingface.co/linagora/Labess-7b-chat-16bit), [Labess-7b-chat-gguf](https://huggingface.co/linagora/Labess-7b-chat-gguf), plus a community quant [tensorblock/Labess-7b-chat-16bit-GGUF](https://huggingface.co/tensorblock/Labess-7b-chat-16bit-GGUF). **[open]**.

### [ESPRIT-Derja-Qwen3-8B-v2](https://huggingface.co/ESPRIT-Group/ESPRIT-Derja-Qwen3-8B-v2)
- Tunisian instruct model. ESPRIT School of Engineering (Mourad Zerai), 2026. Qwen3-8B + LoRA on ~7,013 bilingual Arabic/Arabizi Tunisian instruction pairs (ESPRIT-Derja-Instruct, distilled from GPT-4o). The first Tunisian instruct model that explicitly handles Arabizi (3=ع, 7=ح, 9=ق…). Apache-2.0.
- Card is honest that it is conversation-optimized, not factually reliable. Earlier version: [ESPRIT-Derja-8B-v1](https://huggingface.co/ESPRIT-Group/ESPRIT-Derja-8B-v1). **[open]**.

For the datasets that train and evaluate these models (Tunisian_Derja_Dataset, TunisianMMLU, the wghezaiel SFT/DPO stack, synthetic instruction sets), see the [LLM training and evaluation datasets](README.md#llm-training-and-evaluation-datasets) section of the README.

---

## Pretrained text language models (encoders, Tunisian-specific)

### [TunBERT](https://github.com/instadeepai/tunbert)
- The canonical Tunisian BERT. iCompass + InstaDeep, 2021. BERT-base (~110M params), pretrained on ~500k Tunisian social-media comments (~67 MB Common-Crawl-based).
- First pretrained BERT for Tunisian; evaluated on sentiment, Tunisian dialect ID, and reading-comprehension QA (SOTA at the time). Two releases: [PyTorch/NeMo (instadeepai)](https://github.com/instadeepai/tunbert) and [TensorFlow (iCompass-ai)](https://github.com/iCompass-ai/TunBERT).
- Paper: [arXiv:2111.13138](https://arxiv.org/abs/2111.13138); [SN Computer Science 2022](https://link.springer.com/article/10.1007/s42979-022-01541-y). **[open]**.

### [tunis-ai/TunBERT](https://huggingface.co/tunis-ai/TunBERT)
- HF-hosted, ready-to-use conversion of TunBERT (NeMo → safetensors) wired for `transformers` text classification; fine-tuned/evaluated on TSAC. The most-used TunBERT on the Hub. ~0.1B params, MIT. **[open]**.

### [ziedsb19/tunbert_zied](https://huggingface.co/ziedsb19/tunbert_zied)
- Independent Tunisian RoBERTa-style masked LM. Zied Sbabti, 2021. Trained on ~600,000 Tunisian phrases; handles Arabizi (use `BertTokenizer`, not `AutoTokenizer`). **[open]**.

### [hamzabouajila/distilled_tunbert](https://huggingface.co/hamzabouajila/distilled_tunbert)
- Distilled TunBERT (DistilBERT student, ~66M params, ~1.83× faster). Hamza Bouajila, 2025. Teacher = tunis-ai/TunBERT; trained on the open [tunisian-derja-unified-raw-corpus](https://huggingface.co/datasets/hamzabouajila/tunisian-derja-unified-raw-corpus). Good for classification, not embeddings (card is honest about this). MIT. **[open]**.

### [Chaima/TunBerto](https://huggingface.co/Chaima/TunBerto)
- Likely a Tunisian RoBERTa (probably Chayma Fourati), but **no model card or metadata** — unverified. **[open]** (undocumented).

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
- SpeechBrain semi-supervised WavLM-large + CTC. Zaiem et al., 2023. WER/CER: TARIC 10.55/6.22, IWSLT 39.53/21.18, TunSwitch-TO 25.54/9.67. [Demo](https://huggingface.co/spaces/SalahZa/Tunisian-Speech-Recognition). Paper [arXiv:2309.11327](https://arxiv.org/abs/2309.11327). **[open]**.

### [SalahZa/Code_Switched_Tunisian_Speech_Recognition](https://huggingface.co/SalahZa/Code_Switched_Tunisian_Speech_Recognition)
- Code-switched ASR (wav2vec2 TN/FR/EN, SpeechBrain). WER/CER: TunSwitch-CS 29.47/12.44. [Demo](https://huggingface.co/spaces/SalahZa/Code-Switched-Tunisian-SpeechToText). Apache-2.0. **[open]**.

### [linagora/linto-asr-ar-tn-0.1](https://huggingface.co/linagora/linto-asr-ar-tn-0.1)
- Kaldi TDNN / Vosk + SRILM LM. LINAGORA, 2025. WER/CER: TARIC 16.06/10.60, TunSwitch-CS 20.51/17.72, TunSwitch-TO 22.54/11.13. Android/Raspberry-Pi variant. Training code: [linagora-labs/ASR_train_kaldi_tunisian](https://github.com/linagora-labs/ASR_train_kaldi_tunisian). Apache-2.0. **[open]**.

### [TuniSpeech-AI/whisper-tunisian-dialect](https://huggingface.co/TuniSpeech-AI/whisper-tunisian-dialect)
- Whisper-large-v2 fine-tuned (LoRA merged, ~2B params). Sghaier, Bellagha, Zrigui, 2026. WER 24.74 / CER 8.32 on TuniSpeech-21h. [Demo](https://huggingface.co/spaces/TuniSpeech-AI/TuniSpeech-Model). cc-by-nc-4.0. **[open]** (weights).

### [oddadmix/whisper-large-v3-arabic-dialectal-v2](https://huggingface.co/oddadmix/whisper-large-v3-arabic-dialectal-v2)
- Whisper-large-v3 (1.54B) fine-tuned for **13 Arabic dialects**, Tunisian among them. Ahmed Wasfy (oddadmix), 2026. Trained on [`oddadmix/lahgtna-v3-small`](https://huggingface.co/datasets/oddadmix/lahgtna-v3-small) (52k train / 2.6k test, dialect-balanced).
- **The per-dialect evaluation is the useful part for Tunisian NLP.** On a balanced test of 200 held-out clips per dialect, Tunisian is the hardest of all 13: **WER 0.478 / CER 0.193**, against an overall 0.320 and Saudi/Gulf 0.169. Ordering (easiest → hardest): Gulf 0.169, Iraqi 0.254, Egyptian 0.271, Syrian 0.272, Palestinian 0.301, Yemeni 0.304, Lebanese 0.317, Moroccan 0.340, Libyan 0.343, Bahraini 0.348, Algerian 0.386, Sudanese 0.399, **Tunisian 0.478**.
- The author reports the same ordering across eight fine-tuned models (Whisper large/turbo/medium/small, Nemotron, Qwen3-ASR, Cohere), i.e. Maghrebi-hardest is model-independent on this test set.
- Apache-2.0. **[open]**. Sibling models in the [Arabic ASR Models collection](https://huggingface.co/collections/oddadmix/arabic-asr-models) (13 items).

### Classic ASR systems (papers)
- [ASR system for Tunisian dialect (Kaldi, TARIC), LRE 2018](https://link.springer.com/article/10.1007/s10579-017-9402-y) — Masmoudi et al. WER 22.6% on TARIC. **[paywalled]** (preprint on [ResearchGate](https://www.researchgate.net/publication/319988998)).
- [Tunisian Dialectal End-to-end ASR based on DeepSpeech (Procedia 2021)](https://www.sciencedirect.com/science/article/pii/S1877050921011984) — WER 24.4%. **[open]**.

Note: general Arabic XLSR/Whisper models (e.g., jonatasgrosman/wav2vec2-large-xlsr-53-arabic) are used as Tunisian baselines but degrade sharply out-of-the-box (WER often 50–100%+). Not Tunisian-specific.

---

## TTS models

### [oddadmix/lahgtna-omnivoice-v2 (لهجتنا)](https://huggingface.co/oddadmix/lahgtna-omnivoice-v2)
- Multi-dialect Arabic TTS built on OmniVoice / Qwen3-0.6B-Base (0.6B params), aiming at a single unified model across Arabic dialects. Ahmed Wasfy (oddadmix), 2026. **Tunisia is ticked on the dialect roadmap**, alongside Egypt, Saudi, Morocco, Iraq, Sudan, Palestine, Lebanon, Syria, Libya, Bahrain, Yemen, Algeria.
- Trained on roughly **250 hours of speech across all supported dialects** (author's figure, in conversation); the Tunisian-only share is not published. Supports diacritized Arabic input for pronunciation. Code: [Oddadmix/Lahgtna-OmniVoice](https://github.com/Oddadmix/Lahgtna-OmniVoice). [Demo Space](https://huggingface.co/spaces/oddadmix/Lahgtna-OmniVoice-Demo).
- **[open]**. Per-dialect TTS quality for Tunisian is not separately evaluated — treat as "Tunisian supported", not "Tunisian validated".

- [TunArTTS](https://github.com/elyadata/TunArTTS) baselines (Tacotron2, FastSpeech2) — see [SPEECH.md](SPEECH.md). **[open]** (research).
- [Habibi-TTS](https://github.com/SWivid/Habibi-TTS) — multi-dialect Arabic TTS; Tunisian coverage unconfirmed. **[open]**.
- Community/commercial Tunisian TTS (SpeechGen, community fine-tunes) — see [SPEECH.md](SPEECH.md#text-to-speech-tts).

