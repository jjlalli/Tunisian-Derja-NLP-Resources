# Tunisian Arabic NLP Resources

![Entries](https://img.shields.io/badge/entries-150-blue) ![Open resources](https://img.shields.io/badge/open-90-brightgreen) ![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey) ![PRs welcome](https://img.shields.io/badge/PRs-welcome-orange) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21779464.svg)](https://doi.org/10.5281/zenodo.21779464)

A curated list of datasets, models, tools, and papers for the natural language processing of **Tunisian Arabic** (Tunisian Derja / Tounsi / تونسي, ISO 639-3 code **`aeb`**).

Also on Hugging Face: the inventory as a loadable table at [datasets/fatmajlali/tunisian-nlp-resources](https://huggingface.co/datasets/fatmajlali/tunisian-nlp-resources) (regenerated from these files by `build-dataset-csv.py`), and the open Tunisian datasets and models gathered in one place in the [Tunisian Arabic (Derja) collection](https://huggingface.co/collections/fatmajlali/tunisian-arabic-derja-datasets-and-models).

The goal is to be the single most complete inventory of what exists for Tunisian NLP: text and speech, open and gated, so that researchers, students, and engineers can find what is out there and see clearly where the gaps are.

**This is meant to stay current, and that only works if it isn't maintained by one person.** If you know a resource that is missing, or you built one, or something here is wrong or out of date:

- [**Add a resource**](../../issues/new?template=add-resource.yml) — paste a link, that's enough; formatting and verification are my job
- [**Report something wrong**](../../issues/new?template=correction.yml) — dead links and overstated numbers make this worse than useless
- Or open a pull request directly — see [CONTRIBUTING.md](CONTRIBUTING.md)

Multi-dialect and pan-Arabic resources are welcome; the map records the Tunisian portion honestly rather than counting the whole thing.

## At a glance

| | Entries | Where |
|---|---|---|
| Text datasets, benchmarks, lexicons & papers | 71 | this file |
| Speech corpora (ASR, SLU, translation, TTS) | 28 | [SPEECH.md](SPEECH.md) |
| Pretrained models (LLMs, encoders, ASR, TTS, OCR) | 21 | [MODELS.md](MODELS.md) |
| Researchers, labs & companies | 30 | [PEOPLE.md](PEOPLE.md) |

*Counted as one `###` heading each, so the figures above sum to the entries badge and anyone can reproduce them with `grep -c '^### '`. Two caveats in opposite directions: a few headings group several related items (for example "Classic ASR systems (papers)"), which undercounts individual resources; and a handful of resources are cross-listed under a second category with a pointer to the full entry (PADIC, TArC), which counts them twice. The figure is a heading count, not a claim about distinct artifacts.*

151 access tags are applied across the three resource files (recomputed 5 Sept 2026; reproduce with `grep -o '\*\*\[[a-z -]*\]\*\*' README.md SPEECH.md MODELS.md | sort | uniq -c`): **113 open** · 13 paywalled · 12 paper-only · 8 on request · 3 gated · 2 commercial. Some entries carry more than one tag (scripts open, underlying audio paywalled), so this counts tags rather than resources. At *entry* level, which is what the open badge tracks, `build-dataset-csv.py` resolves the same data to **90 open** of 120 parsed resource entries (grouped entries carrying several different tags are counted as "varies", not as open) — run the script to reproduce. Every entry links to a verifiable source; uncertain Tunisian coverage is flagged rather than dropped, and things checked and found to contain no Tunisian data are recorded under [Confirmed negatives](SPEECH.md#confirmed-negatives).

## Recently added

*Newest first. Contributed entries are credited to whoever pointed them out.*

| Date | Entry | Added by |
|---|---|---|
| 2026-09 | Source re-check across the inventory: links, sizes, authors, years and licences corrected against the primary pages; two empty repos dropped; counts recomputed | [Fatma Jlali](https://github.com/jjlalli) |
| 2026-09 | **First external pull request merged ([#1](https://github.com/jjlalli/Tunisian-Derja-NLP-Resources/pull/1)):** eight additions verified against live row counts and licences, five derivatives flagged under their parents, the untuned-Whisper note given a source, BibTeX URL fixed, counts recomputed — the six rows below | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-09 | [arabic-audio-collection-tunisian-deep-confessions](SPEECH.md#speech-corpora-asr--slu--speech-translation) — 37,156 transcribed chunks / ~20 GB of **spontaneous confessional speech** with paralinguistic markers; a register no other corpus here covers | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-09 | [silma-tts-derja series](MODELS.md#tts-models) — F5-TTS Derja TTS trained on LinTO-TN with a **fully documented recipe** (SNR filtering, single-speaker, 40 epochs); no eval published | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-09 | [whisper-small-tunisian-asr](MODELS.md#asr-models) — **WER 37.99 / CER 18.77 on the TEDxTN test split**, and it ships an 842-utterance pre-fine-tuning baseline quantifying out-of-the-box collapse (median WER 91.7%, worst 2,642.9%) | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-09 | [Tunisian Proverbs with Image Associations](#cultural-and-multimodal-resources) — 999 proverbs, dual word-for-word/dynamic English, four generated images each; **the only text–image Tunisian resource found**, and a new section | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-09 | [senior_tunisian_voice](SPEECH.md#speech-corpora-asr--slu--speech-translation) — 5,377 rows / ~2.4 GB code-switched TN–FR with **both normalised and raw transcript layers**; provenance undocumented | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-09 | Flagged **[Syrinesmati/tunisian-dialect-corpus](#text-corpora-raw--web--social)** as a repackaged slice of the LINAGORA corpus (its own `source` column proves it) with a wrong arXiv citation, and **AzizBelaweid/Tunisian_Language_Dataset** as containing plain English rows | [Amine Troudi](https://github.com/aminetroudi) |
| 2026-08 | **Correction + additions batch (29 Aug):** NADI 2026 final board recorded (below) · [TDMulti](#tdmulti--tunisian-dialectmsa-multitask-corpus) (LREC 2026) · [Romanized Arabic Across Dialects](#romanized-arabic-across-dialects-five-dialect-arabizi-study) (arXiv) · [tunisian-english-parallel-pairs](#community-huggingface-parallel-sets) · five community model releases in [MODELS.md](MODELS.md) (silma-tts-derja, tunisian-xtts, qwen3-telephony ASR, grouped Whisper fine-tunes, first OCR entry) · SLURP-TN upgraded to its LREC 2026 record · author/order fixes on T-HSAB, sub-dialect ID, LinTO, Mahdi; TunSwitch marked preprint-only | maintainer |
| 2026-08 | [Whisperv3-tunisian-codeswitch](MODELS.md#asr-models) — NADI 2026 subtask 1.3, TN↔FR/EN code-switched ASR; **final test leaderboard: 6th of 9 at WER 15.21 (winner 14.41)** — the earlier "3rd, 15.22" reflected a pre-final board — against 0.478 for Tunisian on the 13-dialect model | [Ahmed Wasfy](https://huggingface.co/oddadmix) |
| 2026-08 | [FARUKxAUTO/tunisian-asr-cleaned](SPEECH.md#speech-corpora-asr--slu--speech-translation) — 54k-row Tunisian ASR set behind the model above; **flagged: no card, no licence, provenance unestablished** | [Ahmed Wasfy](https://huggingface.co/oddadmix) |
| 2026-08 | [tunisian-darija-english](#tunisian-darija-english-dhia-azizi) — 553 provenance-tagged Arabizi↔English pairs, 53 cultural categories + from-scratch MT pipeline | [Dhia Azizi](https://github.com/Dhiadev-tn) |
| 2026-07 | [dialect-router-v0.2](MODELS.md#dialect-identification) — 15-label Arabic dialect ID, 11.6M params; **macro-F1 0.905, no per-dialect breakdown published** | [Ahmed Wasfy](https://huggingface.co/oddadmix) |
| 2026-07 | [whisper-large-v3-arabic-dialectal-v2](MODELS.md#asr-models) — 13-dialect ASR with **per-dialect WER; Tunisian is hardest of the 13 (0.478)** | [Ahmed Wasfy](https://huggingface.co/oddadmix) |
| 2026-07 | [lahgtna-omnivoice-v2](MODELS.md#tts-models) — multi-dialect Arabic TTS, Tunisian supported | [Ahmed Wasfy](https://huggingface.co/oddadmix) |
| 2026-07 | [lahgtna-v3-small](SPEECH.md) — dialect-balanced ASR set, 200 Tunisian test clips | [Ahmed Wasfy](https://huggingface.co/oddadmix) |
| 2026-07 | Corrected **CMN2 / NIST SRE** — the ~396h figure covers Tunisian *and* English audio; Tunisian-only share unpublished | maintainer |

## Contents

- [Text corpora (raw / web / social)](#text-corpora-raw--web--social)
- [Sentiment analysis](#sentiment-analysis)
- [Offensive language, hate speech, sarcasm](#offensive-language-hate-speech-sarcasm)
- [Dialect identification (text)](#dialect-identification-text)
- [Treebanks and syntactic resources](#treebanks-and-syntactic-resources)
- [POS tagging](#pos-tagging)
- [Morphology (analyzers and disambiguation)](#morphology-analyzers-and-disambiguation)
- [Named Entity Recognition](#named-entity-recognition)
- [Machine translation and parallel corpora](#machine-translation-and-parallel-corpora)
- [Transliteration and Arabizi](#transliteration-and-arabizi)
- [Orthography (CODA)](#orthography-coda)
- [Lexicons, dictionaries, wordnets](#lexicons-dictionaries-wordnets)
- [Cultural and multimodal resources](#cultural-and-multimodal-resources)
- [LLM evaluation benchmarks](#llm-evaluation-benchmarks)
- [LLM training and evaluation datasets](#llm-training-and-evaluation-datasets)
- [Surveys](#surveys)
- [Shared tasks](#shared-tasks)
- [Other resource lists](#other-resource-lists)

**Separate files:**

- [SPEECH.md](SPEECH.md) — speech corpora (ASR, SLU, speech translation), TTS, speech dialect ID
- [MODELS.md](MODELS.md) — pretrained language models, ASR models, TTS models
- [PEOPLE.md](PEOPLE.md) — researchers, labs, companies

## Access legend

Each entry ends with an access note:

- **[open]** — freely downloadable, no login
- **[gated]** — requires the owner's approval before access is granted
- **[on request]** — obtain by contacting the authors
- **[paywalled]** — behind a publisher or LDC paywall
- **[paper only]** — described in a paper; no dataset download located
- **[commercial]** — a paid product, not a research resource; listed for completeness

A note on scope: some resources are pan-Arabic or Maghrebi and contain Tunisian only as one part. These are included with the Tunisian portion noted, because they are often the only source of a given resource type. Items where Tunisian coverage could not be confirmed are flagged.

---

## Text corpora (raw / web / social)

### [Tunisian Arabic Corpus (tunisiya.org)](http://www.tunisiya.org)
- Raw reference corpus with a searchable concordance interface. Karen McNeil and Miled Faiza.
- ~1.19M words (site count, 4 Sept 2026: 1,189,766) in 12 categories: folktales/proverbs, forums, poetry, TV/movies/plays, blogs, newspapers, web, SMS/Facebook, spoken, fiction, non-fiction, miscellaneous. Begun 2010.
- **[open]** (online search interface; not a single bulk download).

### [CTAB — Corpus of Tunisian Arabizi](https://zenodo.org/record/4780941)
- Raw, unannotated Arabizi (Latin-script) corpus. Amara et al., 2021. Facebook public-page messages kept as-is, grouped by page/period. Companion to tunisiya.org.
- ⚠️ The linked Zenodo record is a superseded version whose files are labelled `CTAB-SAMPLE…` (≈214 kB); Zenodo flags a newer version. The TADT paper cites CTAB as DOI [10.5281/zenodo.4781769](https://doi.org/10.5281/zenodo.4781769) (2,929 comments / 26,232 tokens).
- **[open]** (Zenodo, CC-BY-4.0).

### [tunisian-derja-unified-raw-corpus](https://huggingface.co/datasets/hamzabouajila/tunisian-derja-unified-raw-corpus)
- Aggregated raw corpus, ~802,659 text examples (~860k rows). Merges social media, conversational transcripts, chatbot dialogues, and other public Derja datasets; preserves French/English code-switching. Hamza Bouajila, 2025. Seed corpus for the ESPRIT-Derja model.
- **[open]** (HuggingFace).

### [linagora/Tunisian_Derja_Dataset](https://huggingface.co/datasets/linagora/Tunisian_Derja_Dataset)
- Large aggregated Derja LM corpus, ~2.23M rows / 332 MB, cc-by-sa-4.0. Wajdi Ghezaiel and Jean-Pierre Lorré (LINAGORA), 2025. Aggregates 14 sub-corpora (khaled123 Derja-English, TSAC, TunBERT, TunSwitch, TuDiCoI, QADI-TN, MADAR-TN, TA-Segmentation, Tweet_TN, and more). Used to continual-pretrain the Labess LLM.
- **[open]** (HuggingFace).

### [linagora/fineweb2_Tunisian_Arabic](https://huggingface.co/datasets/linagora/fineweb2_Tunisian_Arabic)
- The Tunisian (`aeb`) portion of FineWeb2, ~265k rows. LINAGORA, June 2025. ODC-By v1.0.
- **[open]** (HuggingFace).

### [Tunisian_reddit](https://huggingface.co/datasets/Lime1/Tunisian_reddit)
- Raw social-media corpus scraped from r/Tunisia (posts + comments, 2009–2022, two CSVs; scraper scripts included). Uncurated; HF size category 100K–1M rows, ~3.4 GB on disk; no exact row count published (the HF viewer cannot convert it). MIT, uploaded Dec 2023.
- **[open]** (HuggingFace).

### [AzizBelaweid/Tunisian_Language_Dataset](https://huggingface.co/datasets/AzizBelaweid/Tunisian_Language_Dataset)
- **269,773** rows, single `text` column, ~618 MB. Licence tag CC-BY-4.0, but the card body says CC BY-SA 4.0 ("the most restrictive license terms of its components") — the two disagree; assume BY-SA. Mohamed Aziz Belaweid, 2024. Publishes its own `create_data.py` and `preprocess.py`, so the build is reproducible — unusual and welcome for a community dump.
- ⚠️ **Not a Tunisian-only corpus, despite the name.** Sampling returns plain English prose (*"On the other hand, I have received an offer from a startup that is willing to pay me 2500 TND"*) interleaved with Derja and MSA news text. The card's `ar`/`fr`/`en` language tags are the accurate description; the title is not. Run language ID and filter before using it as a Derja LM corpus, and do not quote the 270k figure as Tunisian text.
- **[open]** (CC-BY-4.0).

### [Syrinesmati/tunisian-dialect-corpus](https://huggingface.co/datasets/Syrinesmati/tunisian-dialect-corpus)
- **1,180,174** rows, `text` + `source`, ~208 MB parquet. Apache-2.0, 2026.
- ⚠️ **Derivative, not a new corpus — and it says so itself.** The `source` column attributes rows to `linagora/Tunisian_Derja_Dataset::Tunisian_Dialectic_English_Derja`, and the card lists 14 sources in total — LINAGORA sub-corpora (TunSwitch text, TA_Segmentation, Sentiment_Derja…), atakaboudi, tunis-ai, Arbi-Houssem, TADI, TunBERT/TAD, khaled123, T-HSAB, TSAC and others — i.e. this is a cleaned re-aggregation of corpora already listed in this map. Treating it as an independent 1.18M-row resource would double-count them.
- Its `arxiv:2309.11327` tag is the TunSwitch ASR paper — cited because TunSwitch transcripts are one of the included sources, not because this corpus derives from that work.
- Row quality is uneven in the same way the parent is — sampling turns up degenerate repetition (*"أية وحدة ألاي أية وحدة ألاي أية وحدة ألاي"*). The genuine merit is the explicit `source` column: it is one of the few community repackagings in this ecosystem that makes its own provenance checkable.
- **[open]** (Apache-2.0).

### [Nehdi/TuniziBigBench](https://huggingface.co/datasets/Nehdi/TuniziBigBench)
- Despite the name, a raw corpus, not an evaluation benchmark: a single TSV of Tunizi (Arabizi) text scraped from 14,000+ Tunisian YouTube videos, HF size category 1M–10M rows, tagged text-classification. Nov 2024; licence creativeml-openrail-m. **[open]** (HuggingFace).

---

## Sentiment analysis

### [TSAC — Tunisian Sentiment Analysis Corpus](https://github.com/fbougares/TSAC)
- Binary sentiment (positive/negative). Medhaffar, Bougares, Estève, Hadrich-Belguith, 2017.
- ~17,000 Facebook comments from Tunisian radio/TV pages (Mosaïque FM, Jawhara FM, Shems FM, Hiwar Ettounsi TV, Nessma TV; Jan 2015–Jun 2016). HF mirror: 13,669 train / 3,400 test, LGPL-3.0.
- Mirrors: HF [fbougares/tsac](https://huggingface.co/datasets/fbougares/tsac), TensorFlow Datasets (`tsac`).
- Paper: [Sentiment Analysis of Tunisian Dialects (WANLP 2017)](https://aclanthology.org/W17-1307/). **[open]**.

### [TUNIZI — Tunisian Arabizi Sentiment Dataset (v1)](https://github.com/chaymafourati/TUNIZI-Sentiment-Analysis-Tunisian-Arabizi-Dataset)
- Sentiment on Latin-script (Arabizi) Tunisian. Fourati, Messaoudi, Haddad (iCompass), 2020. The linked repo and its HF mirror hold **3,000** YouTube comments (1,500 positive / 1,500 negative); the iCompass-ai repo's `TUNIZI_V1.txt` is described there as 9,210 sentences — the two "v1" releases differ in size.
- Mirrors: [iCompass-ai/TUNIZI](https://github.com/iCompass-ai/TUNIZI) (MIT; `TUNIZI_V1.txt` + `TUNIZI_V2.txt`), HF [chaymafourati/tunizi](https://huggingface.co/datasets/chaymafourati/tunizi) (3,000 rows), [arbml/TUNIZI](https://huggingface.co/datasets/arbml/TUNIZI).
- Paper: [arXiv:2004.14303](https://arxiv.org/abs/2004.14303). **[open]**.

### [TUNIZI v2 — Large Tunisian Arabizi Dataset](https://aclanthology.org/2021.wanlp-1.25/)
- Extended Arabizi sentiment set, ~100k comments (movies, politics, sport…) labeled positive/negative/neutral. iCompass, 2021.
- Hosted as `TUNIZI_V2.txt` in [iCompass-ai/TUNIZI](https://github.com/iCompass-ai/TUNIZI) ("100K sentences"; row count not re-verified here) and on [Zenodo 4275240](https://zenodo.org/records/4275240) (CC-BY-4.0; described as ~100k comments, positive/negative/neutral, 7:1:2 split). Also used for a Zindi competition — a [participant's solution repo](https://github.com/maroxtn/tun-sentiment) and a [Kaggle copy](https://www.kaggle.com/datasets/waalbannyantudre/tunisian-arabizi-dialect-data-sentiment-analysis) exist.
- **[open]**.

### [arbml/Tunisian_Dialect_Corpus](https://huggingface.co/datasets/arbml/Tunisian_Dialect_Corpus)
- Polarity classification (negative/positive), 49,889 rows, Arabic + Arabizi. Aggregated Tunisian tweets/comments.
- **[open]** (HuggingFace).

### [hedhoud12/TunisianSentimentAnalysis](https://huggingface.co/datasets/hedhoud12/TunisianSentimentAnalysis)
- Sentiment corpus, ~23,786 rows. Hedi Naouara (LINAGORA), Oct 2024.
- **[open]** (HuggingFace).

Related: learning word representations for Tunisian sentiment ([arXiv:2010.06857](https://arxiv.org/abs/2010.06857)).

---

## Offensive language, hate speech, sarcasm

### [T-HSAB — Tunisian Hate Speech and Abusive Dataset](https://github.com/Hala-Mulki/T-HSAB-A-Tunisian-Hate-Speech-and-Abusive-Dataset)
- Three classes: normal / abusive / hate. Haddad, Mulki, Oueslati, 2019 (Springer ICALP proceedings, CCIS 1108, pp. 251–263). 6,024 comments per the repo README (the TEET! paper cites 6,039).
- Paper: [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-030-32959-4_18). **[open]** (GitHub).

### [TEET! — Tunisian Dataset for Toxic Speech Detection](https://aclanthology.org/2021.winlp-1.2/)
- Toxic-speech corpus, ~10,000 comments. Gharbi, Haddad, Kchaou, Arfaoui, 2021. Paper is open; a public data repo was not confirmed.
- **[paper only]** ([arXiv:2110.05287](https://arxiv.org/abs/2110.05287)).

### HateTune — Tunisian Dialect Hate Speech Detection Dataset
- Hate speech in Arabic-script Tunisian: 12k+ comments, Hate/Neutral. Kharrat, Mohamed, Mtimet, Benamor, Fourati (MedTech); ICALP 2024 proceedings, published Feb 2025 (CCIS 2339, pp. 63–73). The abstract calls it "the largest publicly available dataset" for the task; the footnoted data link could not be resolved when checked (4 Sept 2026).
- **[paywalled]** (paper — [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-031-79164-2_6); data link unresolved).

### [TDMulti — Tunisian Dialect–MSA Multitask Corpus](https://aclanthology.org/2026.lrec-1.254/)
- First multitask Tunisian corpus manually aligned with MSA: 3,100 social-media comments, 12,400 labels across **hate speech, sentiment polarity, sarcasm, and topic**, with a context-aware cross-attention BERT model. Torjmen, Haddar, LREC 2026 (pp. 3240–3249).
- Cross-listed here under its hate-speech layer; the sentiment/sarcasm/topic layers make it equally relevant to [Sentiment analysis](#sentiment-analysis).
- The abstract says the corpus is "released under an open license", but no repository link was found on the LREC page or in the paper metadata (checked 4 Sept 2026); the paper itself is open access. **[paper only]** until a link surfaces.

---

## Dialect identification (text)

*Datasets and benchmarks. **Trained dialect-ID models** are in [MODELS.md § Dialect identification](MODELS.md#dialect-identification).*

### [MADAR Corpus and Lexicon](https://camel.abudhabi.nyu.edu/madar/)
- Multi-dialect parallel corpus + city/country dialect ID (26-way). Bouamor et al., LREC 2018. Includes **Tunis** (Corpus-26/Corpus-6) and **Sfax** in the lexicon.
- Paper: [LREC 2018](https://aclanthology.org/L18-1535/). **[open]** (free research license via form).

### [NADI — Nuanced Arabic Dialect Identification](https://nadi.dlnlp.ai/)
- Country/province-level dialect ID from tweets, annual 2020–2024. Tunisia is one of ~21 covered countries.
- **[open]** (via shared-task registration). See [Shared tasks](#shared-tasks).

### [IADD — Integrated Arabic Dialect Identification Dataset](https://github.com/JihadZa/IADD)
- Aggregated dialect-ID dataset merging DART, SHAMI, PADIC, AOC, and **TSAC** — so it embeds a Tunisian subset. Jihad Zahir (single author), Data in Brief 40, 2022 (online Dec 2021). 136,317 texts from 9 countries, Tunisia included.
- Data paper: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352340921010519) (CC-BY-4.0). **[open]** (GitHub).

### [QADI — QCRI Arabic Dialect Identification](https://alt.qcri.org/resources/qadi/)
- Country-level dialect-ID tweets across 18 countries; the Tunisian subset is ~8,879 items (as folded into the LinTO Derja aggregate). QCRI.
- **[open]** (QCRI resources page; the download is a password-protected zip of tweet IDs — text must be re-hydrated; Apache-2.0).

### [ArapTweet](https://aclanthology.org/L18-1111/)
- Large multi-dialect Arabic Twitter corpus for gender, age, and language-variety identification, covering 11 Arab regions including Tunisia. Zaghouani and Charfi, LREC 2018.
- **[on request]** (contact authors); Tunisian is one regional subset.

### Multi-Dialect, Multi-Genre Corpus of Informal Written Arabic (LREC 2014)
- Cotterell and Callison-Burch. Informal Arabic across five dialect groups including **Maghrebi** (Tunisian-relevant). Paper: [LREC 2014, #641](http://www.lrec-conf.org/proceedings/lrec2014/summaries/641.html) ([PDF](http://www.lrec-conf.org/proceedings/lrec2014/pdf/641_Paper.pdf)). **[on request]**.

### [Arabic Dialect Identification shared-task data (LREC 2018)](https://github.com/drelhaj/ArabicDialects/tree/master/ArabicSharedTask)
- Dialect-ID train/test data under `ArabicSharedTask/`. ⚠️ The repo carries no README or paper reference and its own description reads "test files not a real project" — recorded, not vouched for.
- **[open]** (GitHub).

### [PADIC — Parallel Arabic Dialect Corpus](https://smart.loria.fr/corpora/)
- Cross-listed. Also usable for dialect ID; one of six dialects is Tunisian. Full details under [Machine translation and parallel corpora](#machine-translation-and-parallel-corpora). **[open]**.

### Sub-dialect identification (within Tunisian)
- [Text and Speech-based Tunisian Arabic Sub-Dialects Identification (LREC 2020)](https://aclanthology.org/2020.lrec-1.787/) — Ben Abdallah, Kchaou, Bougares. Distinguishes Tunis / Sfax / Sousse / Tataouine. A released benchmark rather than an organized competition. **[open]** (paper).

---

## Treebanks and syntactic resources

### [TArC — Tunisian Arabish Corpus](https://github.com/eligugliotta/tarc)
- Multi-layer annotated Arabizi corpus. Gugliotta and Dinarelli; first release 2020, complete release 2022.
- 4,797 sentences / ~43,300 tokens (forum, social, blog, rap), with user metadata (governorate, age range, gender).
- Annotation layers: token classification (arabizi/foreign/emotag), Arabic-script transliteration (CODA-TUN), tokenization with clitic splitting, POS (Penn Arabic Treebank style), lemmatization (in progress). CC BY-NC-SA 4.0.
- Companion annotation tool: [Multi-Task Sequence Prediction System (GitLab)](https://gricad-gitlab.univ-grenoble-alpes.fr/dinarelm/tarc-multi-task-system).
- Papers: [LREC 2022](https://aclanthology.org/2022.lrec-1.121/) ([arXiv:2207.04796](https://arxiv.org/abs/2207.04796)), [LREC 2020](https://aclanthology.org/2020.lrec-1.770/), [WANLP 2020](https://aclanthology.org/2020.wanlp-1.16/). Mirror: HF [arbml/TArC](https://huggingface.co/datasets/arbml/TArC). **[open]**.

### [TTB — Tunisian Treebank + parser](https://github.com/AsmaMekki/TA-Parser)
- Constituency/syntactic treebank and a trained Stanford-parser model. Mekki, Zribi, Ellouze, Belguith, 2020.
- Tunisian constitution (12,378 words) + 1,072 STAC sentences, CODA-TUN orthography; parser trained on ~8,000 sentences / ~79,600 tokens, best F-measure 80.12%.
- Paper: [AICCSA 2020](https://ieeexplore.ieee.org/document/9316462). **[open]** (GitHub; IEEE paper paywalled).

### TADT — Tunisian Arabic Dependency Treebank (Universal Dependencies)
- The first UD treebank for Tunisian (`aeb`). Amal Aissaoui (CUNY), 2026. 100 sentences / 1,466 tokens of Arabizi social-media text (sampled from CTAB), with UPOS, morphological features, lemmas, and dependency relations. Built by cross-dialect transfer from the Algerian NArabizi treebank + manual correction.
- The treebank is being finalized for official UD release; **not yet downloadable**.
- **[paper only]** ([UDW 2026 paper](https://universaldependencies.org/udw26/papers/40_Paper.pdf)).

### [TA-Segmentation Corpus](https://github.com/AsmaMekki/TA-Segmentation-Corpus)
- Sentence-boundary / segmentation annotation with CODA-TA normalization. Mekki et al., 2021. 260,364 words / 33,581 sentences, expert-validated.
- **[open]** (GitHub).

---

## POS tagging

### TArC POS layer
- See [TArC](#treebanks-and-syntactic-resources) ([repo](https://github.com/eligugliotta/tarc)): POS (Penn Arabic Treebank style) is applied to the *arabizi* tokens — 31,510 of the corpus's 43,327 tokens (the rest are tagged foreign/emotag). **[open]**.

### [POS-tagging of Tunisian Dialect Using Standard Arabic Resources (WANLP 2015)](https://aclanthology.org/W15-3207/)
- Hamdi, Nasr, Habash, Gala. Maps Tunisian to an MSA lattice and tags with an MSA tagger (~89% accuracy). Method paper; no standalone gold TD POS corpus released. **[open]** (paper).

### Fine-Grained POS Tagging of Spoken Tunisian Dialect (Springer NLDB 2014)
- Boujelbane, Mallek, Ellouze, Hadrich-Belguith. Builds a TD training corpus by converting an MSA corpus via a bilingual lexicon (~78.5% accuracy).
- **[paywalled]** ([Springer](https://link.springer.com/chapter/10.1007/978-3-319-07983-7_9)).

---

## Morphology (analyzers and disambiguation)

### [Intelligent Tunisian Arabic Morphological Analyzer — evaluation corpus](https://github.com/NadiaBMKarmani/Intelligent-Tunisian-Arabic-Morphological-Analyzer-evaluation-corpus)
- 1,000 Tunisian words used to evaluate the Karmani analyzer. Karmani, Soussou, Alimi, AICCSA 2016.
- Paper: AICCSA 2016 ([IEEE](https://ieeexplore.ieee.org/document/7945666)). **[open]** (GitHub; paper paywalled).

### [Tunisian-Arabic-Lexical-Dictionary](https://github.com/NadiaBMKarmani/Tunisian-Arabic-Lexical-Dictionary)
- XML lexicon of the main Tunisian clitics (repo description: "Main TA clitics"). Same author as the analyzer above.
- **[open]** (GitHub).

### Al-Khalil-TUN — Morphological Analysis of Tunisian Dialect (IJCNLP 2013)
- Zribi, Ellouze Khemakhem, Hadrich Belguith. Adapts the MSA Al-Khalil analyzer with a Tunisian lexicon of 6,030 roots and 6,092 patterns built from the 27,144-word STAC corpus. No public download of the analyzer or lexicon was found.
- **[paper only]** ([paper](https://www.academia.edu/4516863/)).

### [Morphological Disambiguation of Tunisian Dialect (J. King Saud Univ., 2017)](https://www.researchgate.net/publication/313035715_Morphological_Disambiguation_of_Tunisian_Dialect)
- Zribi, Ellouze, Hadrich-Belguith, Blache. ML disambiguation over the analyzer output. Journal of King Saud University – Computer and Information Sciences 29(2), pp. 147–155 (CC BY-NC-ND). **[open]** (article; the ResearchGate link is a bot-walled mirror — use DOI [10.1016/j.jksuci.2017.01.004](https://doi.org/10.1016/j.jksuci.2017.01.004)).

---

## Named Entity Recognition

The most useful openly available NER building blocks are the **Barcha** gazetteers (below). A token-annotated gold NER *corpus* specific to Tunisian has not been openly released yet. Known work:

### [Barcha](https://github.com/wa3dbk/Barcha)
- Open multi-purpose Tunisian resource (MIT). wa3dbk. Its `named_entities/` folder is a set of curated Tunisian entity gazetteers: people (academics/scientists, artists, footballers, media figures, poets, politicians, trade unionists, writers), institutions/associations/companies, government institutions, cities, universities (public and private), ISETs, political parties, and unions. Also ships a `texts/` raw-text folder and a `translation/` folder — the README still lists Tunisian↔English/MSA parallel sets as a TODO, so treat that folder as work in progress.
- These are gazetteers/word lists rather than a token-annotated corpus, but they are the best open NER starting point for Tunisian. **[open]**.

### TUNER — NER of Tunisian Arabic with Bi-LSTM-CRF (2023/2024)
- Mekki, Zribi, Ellouze, Belguith. Hybrid Bi-LSTM-CRF + rules, F-measure 91.43% (abstract); online 2023, IJAIT 33(2) 2024. No public release of the annotated NER corpus was found.
- **[paywalled]** ([World Scientific](https://www.worldscientific.com/doi/10.1142/S0218213023500628)).

### Recognition and Translation of Tunisian Dialect Named Entities into MSA (2021)
- Torjmen and Haddar. No public dataset found.
- **[paper only]** ([ResearchGate](https://www.researchgate.net/publication/349773211)).

---

## Machine translation and parallel corpora

### [PADIC — Parallel Arabic Dialect Corpus](https://smart.loria.fr/corpora/)
- Parallel dialect corpus. Meftouh, Harrat, Abbas, Smaïli (SMarT/LORIA); Tunisian portion by Salma Jamoussi. 2015, extended 2017–2018.
- ~6,400 sentences per variety aligned to MSA. Varieties: Algiers, Annaba, **Tunisian**, Moroccan (Casablanca, Rabat), Syrian, Palestinian + MSA.
- Direct download: [ZIP](https://smart.loria.fr/wp-content/uploads/2020/08/PADIC-20-02-2017.zip); [SourceForge mirror](https://sourceforge.net/projects/padic/).
- Papers: [PACLIC 2015](https://hal.archives-ouvertes.fr/hal-01261587), [ICAT 2018](https://hal.archives-ouvertes.fr/hal-01718858). **[open]**.

### [MADAR Parallel Corpus](https://camel.abudhabi.nyu.edu/madar-parallel-corpus/)
- Corpus-26: 2,000 BTEC sentences translated into 25 city dialects + MSA (includes **Tunis** and **Sfax**). Corpus-6: 12,000 sentences in 5 cities + MSA (includes **Tunis**). Bouamor et al., LREC 2018.
- **[open]** (free research license via form).

### [MDC — Multidialectal Parallel Corpus of Arabic](https://aclanthology.org/L14-1435/)
- 2,000 sentences in MSA, Egyptian, **Tunisian**, Jordanian, Palestinian, Syrian + English. Bouamor, Habash, Oflazer, LREC 2014.
- **[on request]** (paper open; no confirmed open direct download).

### [Parallel resources for Tunisian Arabic Dialect Translation (WANLP 2020)](https://aclanthology.org/2020.wanlp-1.18/)
- Kchaou, Boujelbane, Hadrich-Belguith. Tunisian (social media) ↔ MSA with data augmentation; BLEU up to 15.03.
- **[paper only]** (dataset link not clearly published).

### Rule-based / SMT Tunisian→MSA
- [Rule-Based MT from Tunisian to MSA (Procedia 2020)](https://www.sciencedirect.com/science/article/pii/S1877050920318573) — Sghaier and Zrigui. **[open]**.
- [FST + seq2seq Transformer Tunisian→MSA (ACM TALLIP 2024)](https://dl.acm.org/doi/10.1145/3681788) — BLEU 56.65 (FST) / 66.07 (transformer). **[paywalled]**.
- [Phrase-based SMT + 5,000-sentence Tunis↔MSA corpus (IBIMA)](https://ibima.org/accepted-paper/building-a-tunisian-dialect-into-modern-standard-arabic-parallel-corpus-for-a-phrase-based-machine-translation/) — Sghaier and Zrigui, 34th IBIMA, Nov 2019 (BLEU 49.90). No availability statement on the page. **[on request]**.

### [tunisian-darija-english (Dhia Azizi)](https://huggingface.co/datasets/Dhiadev-tn/tunisian-darija-english)
- 553 Tunisian Arabizi↔English pairs across 53 cultural categories (louage culture, mawsem el zitoun, bac exam culture, el 3aza w mawt…). Every pair provenance-tagged in a `source` column: 500 self-written by the author (native speaker), 53 field-collected from family and community speakers with documented consent; nothing synthetic. Dhia Azizi, 2026; collection ongoing.
- Companion repo: [darija-translator](https://github.com/Dhiadev-tn/darija-translator) — a from-scratch ~15.6M-param encoder-decoder with an Arabizi-aware BPE tokenizer (3/7/9/5 as protected markers), pretrained on *cleaned Moroccan* darija ([atlasia/darija_english](https://huggingface.co/datasets/atlasia/darija_english)) and fine-tuned on the Tunisian pairs. Locked test set; BLEU 3.89 reported honestly as the v1 baseline. The Tunisian data is the 553 pairs — the ~36k pretraining pairs are Moroccan-derived.
- **[open]** (CC BY-NC-SA 4.0 — note the non-commercial clause).

### Community HuggingFace parallel sets
- [tunis-ai/tunisian-msa-parallel-corpus](https://huggingface.co/datasets/tunis-ai/tunisian-msa-parallel-corpus) — 1,000 Derja↔MSA pairs (synthetic pipeline, CC-BY-4.0). Tunisia.AI, 2025. **[open]**. Companion [tunis-ai/tunisian-msa-parallel-corpus-evaluated](https://huggingface.co/datasets/tunis-ai/tunisian-msa-parallel-corpus-evaluated) — the same **1,000 rows** quality-graded (CC-BY-4.0, tagged `aeb`) with `semantic_similarity`, `fluency_score` and `composite_score` per pair alongside raw and cleaned MSA translations. It is the scored view of the corpus, not additional data; the per-pair scores make it the more useful of the two for building an evaluation split.
- [tunis-ai/MADAR-TUN](https://huggingface.co/datasets/tunis-ai/MADAR-TUN) (30,137 rows, cc-by-nc-3.0) — **not** a Derja↔MSA set: it is a mirror of Elisa Gugliotta's MADAR-TUN Arabizi annotations (`arabish`/`class`/`words`/`tokens`/`pos`/`lem` columns). Listed here only because it sits in the tunis-ai collection; credit belongs to the TArC authors. **[open]**.
- [KKKarim711/tunisian-english-parallel-pairs](https://huggingface.co/datasets/KKKarim711/tunisian-english-parallel-pairs) — **237,138** Tunisian/English pairs, JSONL, Apache-2.0, 2026. The card states outright that the pairs are **synthetic**, generated for a data-augmentation and transfer-learning MT project. Comparable in kind and scale to khaled123's ~436k synthetic set below; the Tunisian side reads like spontaneous-speech transcription (*"هذاكة مشى الجهة متاع صالة شاسمها صالة اليوم"*) with visibly machine-produced English. Usable as MT augmentation data, not as a gold reference. **[open]**.
- [NadiaGHEZAIEL/English_to_Tunisian_Dataset](https://huggingface.co/datasets/NadiaGHEZAIEL/English_to_Tunisian_Dataset) (~1.7k) — English→Tunisian. Nov 2025. **[open]**.
- [khaled123/Tunisianderjasynthtranslation](https://huggingface.co/datasets/khaled123/Tunisianderjasynthtranslation) (~436k, synthetic) and the Kaggle [drejja-to-english](https://www.kaggle.com/datasets/khawlajlassi/drejja-to-english) (size not verified) — Derja↔English. **[open]**.
- [Barcha](https://github.com/wa3dbk/Barcha) — has a `translation/` folder, but its README lists Tunisian↔English/MSA parallel sets as a TODO; see [NER](#named-entity-recognition) for what the repo does ship. **[open]**.

### Speech translation corpora with Tunisian↔English/French text
- Pointer entry. [**TuniFra**](https://huggingface.co/datasets/fbougares/TUNIFRA) (Tunisian→French, 15 h), [**TEDxTN**](https://huggingface.co/datasets/fbougares/TEDxTN) (Tunisian→English, ~25 h) and the **IWSLT 2022/2023 Tunisian–English** LDC corpus are three-way (audio + transcript + translation) and are listed in [SPEECH.md](SPEECH.md); their transcript/translation layers are also Tunisian–French / Tunisian–English bitext. TuniFra and TEDxTN are **[open]** (CC BY-NC-ND 4.0); the LDC corpus is **[paywalled]**.

---

## Transliteration and Arabizi

### [Romanized Arabic Across Dialects (five-dialect Arabizi study)](https://arxiv.org/abs/2608.02555)
- The largest human-centered cross-dialect study of Arabizi perception and usage to date, covering Algerian, Egyptian, Lebanese, Moroccan, and **Tunisian** Arabic. Announces two resources: character-level Arabic↔Arabizi alignments from survey-participant transliterations, and a manually curated parallel corpus of Arabic-script sentences with multiple Arabizi transliterations per dialect. Keleg, Ben Abdallah, Yassine, Helwe, Guellil, Ousidhoum, 2026.
- arXiv:2608.02555 (3 Aug 2026, under review). Release links for the two resources were not yet live when checked (29 Aug 2026). **[paper only]** (release announced).

### [TArC](https://github.com/eligugliotta/tarc) + [Multi-Task Sequence Prediction tool](https://aclanthology.org/2020.wanlp-1.16/)
- Annotated Arabizi corpus and the neural tool that transliterates Arabizi→CODA Arabic script and does tokenization/POS. Gugliotta, Dinarelli, Kraif. Code on [GitLab](https://gricad-gitlab.univ-grenoble-alpes.fr/dinarelm/tarc-multi-task-system). **[open]**.

### Masmoudi et al. — Arabizi→Arabic-script transliteration for Tunisian
- [Transliteration of Arabizi into Arabic Script for Tunisian Dialect (ACM TALLIP 2019)](https://dl.acm.org/doi/10.1145/3364319) — rule-based + CRF; the abstract reports a character error rate of 10.47%. **[paywalled]**.
- [Preliminary investigation (CICLing/Springer 2015)](https://link.springer.com/chapter/10.1007/978-3-319-18111-0_46) and an [HMM approach](https://www.researchgate.net/publication/314034927). **[paywalled]**.

### Younes et al. — bi-script Tunisian resources
- [Romanized Tunisian Dialect Transliteration using Sequence Labelling (J. King Saud Univ. 2020)](https://www.sciencedirect.com/science/article/pii/S1319157820303281). **[open]** (paper).
- [Building Bi-script Language Resources for the Tunisian Dialect (Procedia 2021)](https://www.sciencedirect.com/science/article/pii/S1877050921012254) — a Romanized-Tunisian message corpus and two bi-script (Latin↔Arabic) dictionaries; sizes are given in the paper, which could not be re-read for this check (publisher bot wall). Data not openly hosted. **[paper only]**.
- [Seq2Seq double transliteration (Procedia 2018)](https://www.sciencedirect.com/science/article/pii/S1877050918321859). **[open]** (paper).

---

## Orthography (CODA)

### [A Conventional Orthography for Tunisian Arabic (CODA-TUN)](https://aclanthology.org/L14-1214/)
- The canonical Tunisian CODA spec (Arabic-script conventional orthography). Zribi, Boujelbane, Masmoudi, Ellouze, Belguith, Habash, LREC 2014. [PDF](http://www.lrec-conf.org/proceedings/lrec2014/pdf/219_Paper.pdf). **[open]**.

### [CODA* — Unified Guidelines and Resources for Arabic Dialect Orthography](https://camel-guidelines.readthedocs.io/en/latest/orthography/)
- Cross-dialect orthography framework covering 28 city dialects, Tunis included. Habash et al., LREC 2018. [PDF](https://camel.abudhabi.nyu.edu/madar/static/pdfs/2018-LREC-CODA-STAR.pdf). **[open]**.

### [A Conventional Orthography for Maghrebi Arabic (LREC 2016)](https://www.semanticscholar.org/paper/c94db913c93a95b546aad33c2b19e0376fabfdc8)
- Turki, Adel, Daouda, Regragui. Extends CODA across Maghrebi Arabic (Tunisia, Algeria, Morocco, Libya, Mauritania). Not in the ACL Anthology; copies on [ResearchGate](https://www.researchgate.net/publication/311589181_A_Conventional_Orthography_for_Maghrebi_Arabic) and [Academia](https://www.academia.edu/30403052/A_Conventional_Orthography_for_Maghrebi_Arabic). **[open]** (paper).

### NOTA — Normalized Orthography for Tunisian Arabic (Springer 2025)
- Turki, Ellouze, Ben Ammar, Hadj Taieb, Adel, Ben Aouicha, Farri, Bennour; LPKM 2024 (Sfax), Springer LNNS, published Mar 2025. **[paywalled]** ([Springer](https://link.springer.com/chapter/10.1007/978-3-031-85067-7_13)).

---

## Lexicons, dictionaries, wordnets

### [aebWordNet — Lexicon](https://github.com/NadiaBMKarmani/aebWordNet-Lexicon)
- Tunisian (`aeb`) WordNet lexicon (XML). Karmani, Soussou, Alimi (Research Groups on Intelligent Machines, Univ. of Sfax), ACLing 2015. **[open]** (GitHub; [ACLing 2015 paper](https://ieeexplore.ieee.org/document/7422271) paywalled).

### TunDiaWN — Tunisian dialect WordNet (WANLP 2014)
- Bouchlaghem, Elkhlifi, Faiz (EMNLP 2014 Arabic NLP workshop, Doha). Corpus-based wordnet reusing English + Arabic wordnets. Database not found for download.
- **[paper only]** ([WANLP 2014](https://aclanthology.org/W14-3613/)).

### [Peace Corps English–Tunisian Arabic Dictionary](https://archive.org/details/ERIC_ED183017)
- 1977 two-way English↔Tunisian dictionary with phonetic symbols and grammar notes. Companion [Peace Corps Tunisian Arabic course](https://www.livelingua.com/course/peace_corps/spoken_tunisian_arabic). **[open]** (Internet Archive).

### [Derja.Ninja](https://derja.ninja/)
- Community Tunisian↔English dictionary, ~17,000 entries with example sentences and audio. Scraper: [ArmelVidali/derja_ninja_scraper](https://github.com/ArmelVidali/derja_ninja_scraper). **[open]** (web).

### [Webonary "Tunsi" dictionary](https://www.webonary.org/tunsi/)
- Online Tunisian (Latin-script)–German dictionary, 276 entries when checked (Sept 2026); Ramzi Hachani, 2025. **[open]** (web).

### [Wiktionary — Tunisian Arabic](https://en.wiktionary.org/wiki/Category:Tunisian_Arabic_language)
- Collaborative lexicon plus a [Swadesh list](https://en.wiktionary.org/wiki/Appendix:Tunisian_Arabic_Swadesh_list). **[open]**.

### Bilingual lexicons from the literature (Tunisian↔MSA)
- Boujelbane et al., [Building bilingual lexicon to create Dialect Tunisian corpora (HyTra workshop, ACL 2013)](https://aclanthology.org/W13-2813/). **[paper only]**.
- Sadat et al., TDA–MSA lexicon (COLING LG-LP 2014, [ResearchGate](https://www.researchgate.net/publication/293485844)). **[paper only]**.
- [MADAR Lexicon](https://camel.abudhabi.nyu.edu/madar-parallel-corpus/) — 1,045 concepts across 25 cities, Tunis and Sfax included; distributed with the corpus through the CAMeL form. **[open]** (free research licence via form).

---

## Cultural and multimodal resources

### [Tunisian Proverbs with Image Associations](https://huggingface.co/datasets/HabibaAbderrahim/Tunisian-Proverbs-with-Image-Associations-A-Cultural-and-Linguistic-Dataset)
- **999** Tunisian proverbs, each with an Arabic explanation, a `context` field, two English rendering layers (`caption` word-for-word and `dynamic` for the functional equivalent), a `caption_formal` variant, the generation `prompt`, **up to four AI-generated images**, and a `clip_scores` value. Habiba Abderrahim, 2025. DOI [10.57967/hf/5189](https://doi.org/10.57967/hf/5189).
- **The only text–image Tunisian resource found in this survey**, and the reason this section exists. Proverbs (*ظل راجل ولا ظل حيط*, *كل قرده في عين امه غزال*) are exactly the material that pan-Arabic corpora flatten away, and the paired word-for-word / dynamic translations make it usable for idiom and figurative-translation evaluation independent of the images.
- Note that the images are **model-generated interpretations, not photographs or archival material** — they are useful for multimodal and generative work, not as documentary cultural record. `clip_scores` gives a text–image alignment signal but no human validation of cultural accuracy is reported.
- **[open]** (CC-BY-4.0).

---

## LLM evaluation benchmarks

### [TounsiBench](https://github.com/Souha-BH/TounsiBench-Benchmarking-Large-Language-Models-for-Tunisian-Arabic)
- The dedicated Tunisian LLM instruction benchmark. Ben Hassine, Arrak, Addhoum, Wilson, EMNLP 2025 (pp. 34627–34642).
- 744 Tunisian instructions with gold human responses; ten Arabic-claiming LLMs scored by humans and an LLM judge on quality, correctness, relevance, dialectal adherence. Finding: most LLMs struggle in Tunisian.
- Repo: [Souha-BH/TounsiBench-…](https://github.com/Souha-BH/TounsiBench-Benchmarking-Large-Language-Models-for-Tunisian-Arabic) (`data/` = instructions, native gold responses, topic labels, evaluated model outputs; plus a GPT-4o evaluation notebook to score your own model). Paper: [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1756/). **[open]**.

### [How Well Do LLMs Understand Tunisian Arabic?](https://arxiv.org/abs/2511.16683)
- Parallel Tunizi ↔ standard Tunisian ↔ English corpus with sentiment labels; benchmarks LLMs on transliteration, translation, sentiment. arXiv, Nov 2025. **[open]** (arXiv).

### [linagora/TunisianMMLU](https://huggingface.co/datasets/linagora/TunisianMMLU)
- MMLU-style multiple-choice benchmark in Tunisian Derja: 22,027 questions (card figure) over 44 subjects, machine-translated from MMLU, ArabicMMLU and DarijaMMLU. LINAGORA, Feb 2025. CC BY-NC-SA 4.0.
- **[open]** (HuggingFace).

---

## LLM training and evaluation datasets

The instruction / SFT / DPO / synthetic data layer behind the Tunisian LLMs in [MODELS.md](MODELS.md#generative--instruction--chat-llms). Mostly 2025–2026, mostly open, and mostly unreviewed community data, quality varies, so treat sizes as raw counts.

### LINAGORA / Labess training stack
- [linagora/Tunisian_Derja_Dataset](https://huggingface.co/datasets/linagora/Tunisian_Derja_Dataset) — 2.23M-row Derja corpus used for continual pre-training (also listed under raw corpora). **[open]**.
- [wghezaiel/SFT-Tunisian-Derja](https://huggingface.co/datasets/wghezaiel/SFT-Tunisian-Derja) (~40k), [wghezaiel/DPO-Tunisian-Derja](https://huggingface.co/datasets/wghezaiel/DPO-Tunisian-Derja) (~44k), [wghezaiel/SFT_derja_dataset](https://huggingface.co/datasets/wghezaiel/SFT_derja_dataset) (~48k), [wghezaiel/derja_to_msa_dataset](https://huggingface.co/datasets/wghezaiel/derja_to_msa_dataset) (~18k), [wghezaiel/fw_tunisian_derja](https://huggingface.co/datasets/wghezaiel/fw_tunisian_derja) (~37k), [wghezaiel/TunisianWikipedia-QA](https://huggingface.co/datasets/wghezaiel/TunisianWikipedia-QA) (~34k). Wajdi Ghezaiel (LINAGORA), 2025. The SFT/DPO alignment stack behind Labess. **[open]**.

### Tunisia.AI / khaled123 (Khaled Bouzaiene)
- [khaled123/Tunisian_Dialectic_English_Derja](https://huggingface.co/datasets/khaled123/Tunisian_Dialectic_English_Derja) (~1.66M rows, Derja↔English, translations + sentiment + generation), [khaled123/tunisiansynthinstract](https://huggingface.co/datasets/khaled123/tunisiansynthinstract) (~266k synthetic instructions), [khaled123/Tunisianderjasynthtranslation](https://huggingface.co/datasets/khaled123/Tunisianderjasynthtranslation) (~436k), [khaled123/tuniset](https://huggingface.co/datasets/khaled123/tuniset) (~29k). 2024. **[open]**. (Note: this account hosts many datasets of uneven quality — some are noisy dumps; verify before use.)

### Other
- ESPRIT-Derja-Instruct — the 7,013-example Arabic/Arabizi instruction set behind [ESPRIT-Derja-Qwen3-8B-v2](https://huggingface.co/ESPRIT-Group/ESPRIT-Derja-Qwen3-8B-v2) (3,494 GPT-4o-distilled pairs in both scripts + 25 manual). The model card says it "will be published separately"; **not released** as of 4 Sept 2026, so it carries no access tag.
- [Datasmartly/darja-tunisie-chat](https://huggingface.co/datasets/Datasmartly/darja-tunisie-chat) — Tunisian chat dataset, 122,961 rows, 2025. **[gated]** (manual approval; no card).
- [abdouuu/tunisian_chatbot_data](https://huggingface.co/datasets/abdouuu/tunisian_chatbot_data) — ~1,426 instruction pairs, 2024. Weak as a Derja-generation set (questions in Derja, answers largely MSA/English). **[open]**.
- [Syrinesmati/tunisian-question-response-dataset](https://huggingface.co/datasets/Syrinesmati/tunisian-question-response-dataset) — **31,669** instruction/response pairs (25,335 train / 6,334 test) with a `category` field (`student_life`, `cultural_knowledge`, …). CC-BY-4.0, 2026. Answers are in Derja with French/English technical terms transliterated and bracketed (*"استعمل (منديلي) ولا (زوتيرو)"*), and the set covers practical Tunisian topics — certification exams, bibliographic tooling, proverb usage — that the other SFT sets here do not. ⚠️ Style is highly uniform and the definite article is consistently written detached (`الـ سيرتيفيكاسيون`, `الـ لغات`), which points to templated or LLM-generated construction rather than collected text; the card does not state a generation method. Treat as synthetic. Pre-split train/test, which most sets here are not. **[open]**.

---

## Surveys

- [Language resources for Maghrebi Arabic dialects' NLP: a survey (LREV 2020)](https://link.springer.com/article/10.1007/s10579-020-09490-9) — Younes, Souissi, Achour, Ferchichi. Catalogue of Maghrebi (incl. Tunisian) resources; the most thorough survey for Tunisian coverage.
- [Maghrebi Arabic dialect processing: an overview (ICNLSSP 2017)](https://hal.science/hal-01873779v1) — Harrat, Meftouh, Smaïli.
- [Survey on Corpora Availability for the Tunisian Dialect (JCCO 2018)](https://ieeexplore.ieee.org/document/8726213) — Younes et al. Tunisian-specific.
- Critical description of Tunisian Arabic linguistic resources (ACLing 2018) — Mekki, Zribi, Ellouze, Belguith.
- [Arabic natural language processing: an overview (2019)](https://arxiv.org/pdf/1903.02784) — Guellil et al.
- [Natural Language Processing for Dialectal Arabic: A Survey (WANLP 2015)](https://aclanthology.org/W15-3205/) — Shoufan and Al-Ameri.
- [A Survey on Dialect Arabic Processing and Analysis (ACM TALLIP 2025)](https://dl.acm.org/doi/10.1145/3747290).
- [Revisiting Common Assumptions about Arabic Dialects in NLP (ACL 2025)](https://aclanthology.org/2025.acl-long.166/) — Keleg, Goldwater, Magdy.
- [Critical Survey of the Freely Available Arabic Corpora (2017)](https://arxiv.org/abs/1702.07835) — Wajdi Zaghouani. Inventory of open Arabic corpora, dialectal ones included.

---

## Shared tasks

- **NADI — Nuanced Arabic Dialect Identification** ([portal](https://nadi.dlnlp.ai/), [GitHub](https://github.com/UBC-NLP/nadi)). Tunisia is a target country each edition: [2020](https://aclanthology.org/2020.wanlp-1.9/), [2021](https://aclanthology.org/2021.wanlp-1.28/), [2022](https://aclanthology.org/2022.wanlp-1.9/), [2023](https://aclanthology.org/2023.arabicnlp-1.62/), [2024](https://aclanthology.org/2024.arabicnlp-1.79/) (its MT subtask covered Egyptian, Emirati, Jordanian and Palestinian — not Tunisian). NADI 2025 and [NADI 2026](https://nadi.dlnlp.ai/2026/) added speech tracks — see [SPEECH.md](SPEECH.md).
- **[MADAR Shared Task 2019](https://aclanthology.org/W19-4622/)** — city-level dialect ID (25 cities incl. Tunis and Sfax) + Twitter user dialect ID.
- **[IWSLT 2022 / 2023 dialectal speech translation](https://iwslt.org/2022/dialect)** — Tunisian↔English (see [SPEECH.md](SPEECH.md)).
- **[Arabic Dialect Identification (LREC 2018)](https://github.com/drelhaj/ArabicDialects/tree/master/ArabicSharedTask)** — earlier DID benchmark with Tunisian-relevant data.

---

## Other resource lists

- [mena-open-data/tunisian-dataset](https://huggingface.co/collections/mena-open-data/tunisian-dataset) — HuggingFace collection of ~60 Tunisian datasets (61 when checked, Sept 2026); the single richest live index found.
- [linagora/tunisian-arabic-dialect-speech-and-text-modeling](https://huggingface.co/collections/linagora/tunisian-arabic-dialect-speech-and-text-modeling) — LinTO/Labess ecosystem (datasets + models) in one collection.
- [Definitive Guide of Tunisian Dialect NLP Resources](https://github.com/chiraz/Definitive-Guide-of-Tunisian-Dialect-NLP-Resources) — Chiraz Ben Abdelkader.
- [Awesome-Tunisian-DATAI](https://github.com/TounesAI/Awesome-Tunisian-DATAI) — TounesAI.
- [ANLP-RG corpora page (MIRACL, Sfax)](https://sites.google.com/site/anlprg/corpora-corpus).
- [tunis-ai HF collections](https://huggingface.co/tunis-ai) (datasets, models).

---

## How to cite

If this inventory is useful in your research, please cite it:

```bibtex
@misc{jlali2026tunisiannlp,
  author       = {Jlali, Fatma},
  title        = {Tunisian Arabic {NLP} Resources},
  year         = {2026},
  howpublished = {\url{https://github.com/jjlalli/Tunisian-Derja-NLP-Resources}},
  doi          = {10.5281/zenodo.21779464},
  note         = {Open inventory of Tunisian Arabic (aeb) NLP resources}
}
```

*A paper describing this inventory is in preparation; this entry will be updated when it is available.*

## License

The list itself is released under [CC BY 4.0](LICENSE). The linked resources keep their own licenses — check each entry.

---

*Maintained by Fatma Jlali. Contributions and corrections welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Last compiled: September 2026.*
