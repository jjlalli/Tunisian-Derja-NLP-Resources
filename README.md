# Tunisian Arabic NLP Resources

![Entries](https://img.shields.io/badge/entries-135-blue) ![Open resources](https://img.shields.io/badge/open-91-brightgreen) ![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey) ![PRs welcome](https://img.shields.io/badge/PRs-welcome-orange)

A curated list of datasets, models, tools, and papers for the natural language processing of **Tunisian Arabic** (Tunisian Derja / Tounsi / تونسي, ISO 639-3 code **`aeb`**).

The goal is to be the single most complete inventory of what exists for Tunisian NLP: text and speech, open and gated, so that researchers, students, and engineers can find what is out there and see clearly where the gaps are.

**This is meant to stay current, and that only works if it isn't maintained by one person.** If you know a resource that is missing, or you built one, or something here is wrong or out of date:

- [**Add a resource**](../../issues/new?template=add-resource.yml) — paste a link, that's enough; formatting and verification are my job
- [**Report something wrong**](../../issues/new?template=correction.yml) — dead links and overstated numbers make this worse than useless
- Or open a pull request directly — see [CONTRIBUTING.md](CONTRIBUTING.md)

Multi-dialect and pan-Arabic resources are welcome; the map records the Tunisian portion honestly rather than counting the whole thing.

## At a glance

| | Entries | Where |
|---|---|---|
| Text datasets, benchmarks, lexicons & papers | 66 | this file |
| Speech corpora (ASR, SLU, translation, TTS) | 24 | [SPEECH.md](SPEECH.md) |
| Pretrained models (LLMs, encoders, ASR, TTS) | 14 | [MODELS.md](MODELS.md) |
| Researchers, labs & companies | 30 | [PEOPLE.md](PEOPLE.md) |

Of the 123 access-tagged resources: **91 open** · 11 paywalled · 10 paper-only · 9 on request · 2 gated. Every entry links to a verifiable source; uncertain Tunisian coverage is flagged rather than dropped.

## Recently added

*Newest first. Contributed entries are credited to whoever pointed them out.*

| Date | Entry | Added by |
|---|---|---|
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

A note on scope: some resources are pan-Arabic or Maghrebi and contain Tunisian only as one part. These are included with the Tunisian portion noted, because they are often the only source of a given resource type. Items where Tunisian coverage could not be confirmed are flagged.

---

## Text corpora (raw / web / social)

### [Tunisian Arabic Corpus (tunisiya.org)](http://www.tunisiya.org)
- Raw reference corpus with a searchable concordance interface. Karen McNeil and Miled Faiza.
- ~2,006 texts / ~882,000 words: folklore, songs, proverbs, blogs, email, Facebook, forums, transcribed radio.
- **[open]** (online search interface; not a single bulk download).

### [CTAB — Corpus of Tunisian Arabizi](https://zenodo.org/record/4780941)
- Raw, unannotated Arabizi (Latin-script) corpus. Amara et al., 2021. Facebook public-page messages kept as-is, grouped by page/period. Companion to tunisiya.org.
- **[open]** (Zenodo).

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
- Raw social-media corpus scraped from Reddit. Small/uncurated; size not documented.
- **[open]** (HuggingFace).

---

## Sentiment analysis

### [TSAC — Tunisian Sentiment Analysis Corpus](https://github.com/fbougares/TSAC)
- Binary sentiment (positive/negative). Medhaffar, Bougares, Estève, Hadrich-Belguith, 2017.
- ~17,000 Facebook comments from Tunisian radio/TV pages (2015–2016), mixed Arabic script and Arabizi. The most-cited Tunisian sentiment corpus.
- Mirrors: HF [fbougares/tsac](https://huggingface.co/datasets/fbougares/tsac), TensorFlow Datasets (`tsac`).
- Paper: [Sentiment Analysis of Tunisian Dialects (WANLP 2017)](https://aclanthology.org/W17-1307/). **[open]**.

### [TUNIZI — Tunisian Arabizi Sentiment Dataset (v1)](https://github.com/chaymafourati/TUNIZI-Sentiment-Analysis-Tunisian-Arabizi-Dataset)
- Sentiment on Latin-script (Arabizi) Tunisian. Fourati, Messaoudi, Haddad (iCompass), 2020. ~9k YouTube comments.
- Mirrors: [Zenodo 4275240](https://zenodo.org/records/4275240), [iCompass-ai/TUNIZI](https://github.com/iCompass-ai/TUNIZI), HF [chaymafourati/tunizi](https://huggingface.co/datasets/chaymafourati/tunizi), [arbml/TUNIZI](https://huggingface.co/datasets/arbml/TUNIZI).
- Paper: [arXiv:2004.14303](https://arxiv.org/abs/2004.14303). **[open]**.

### [TUNIZI v2 — Large Tunisian Arabizi Dataset](https://aclanthology.org/2021.wanlp-1.25/)
- Extended Arabizi sentiment set, ~100k comments (movies, politics, sport…) labeled positive/negative/neutral. iCompass, 2021.
- Distributed via a [Zindi challenge](https://github.com/maroxtn/tun-sentiment) and on [Kaggle](https://www.kaggle.com/datasets/waalbannyantudre/tunisian-arabizi-dialect-data-sentiment-analysis). No single canonical repo for the full 100k.
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
- Three classes: normal / abusive / hate. Mulki, Haddad et al., 2019. ~6,075 comments.
- Paper: [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-030-32959-4_18). **[open]** (GitHub).

### [TEET! — Tunisian Dataset for Toxic Speech Detection](https://aclanthology.org/2021.winlp-1.2/)
- Toxic-speech corpus, ~10,000 comments. Gharbi, Haddad, Kchaou, Arfaoui, 2021. Paper is open; a public data repo was not confirmed.
- **[paper only]** ([arXiv:2110.05287](https://arxiv.org/abs/2110.05287)).

### HateTune — Tunisian Dialect Hate Speech Detection Dataset
- Hate speech in Arabic-script Tunisian, 2024. Behind a Springer paywall; dataset access unconfirmed.
- **[paywalled]** ([Springer chapter](https://link.springer.com/chapter/10.1007/978-3-031-79164-2_6)).

---

## Dialect identification (text)

### [MADAR Corpus and Lexicon](https://camel.abudhabi.nyu.edu/madar/)
- Multi-dialect parallel corpus + city/country dialect ID (26-way). Bouamor et al., LREC 2018. Includes **Tunis** (Corpus-26/Corpus-6) and **Sfax** in the lexicon.
- Paper: [LREC 2018](https://aclanthology.org/L18-1535/). **[open]** (free research license via form).

### [NADI — Nuanced Arabic Dialect Identification](https://nadi.dlnlp.ai/)
- Country/province-level dialect ID from tweets, annual 2020–2024. Tunisia is one of ~21 covered countries.
- **[open]** (via shared-task registration). See [Shared tasks](#shared-tasks).

### [IADD — Integrated Arabic Dialect Identification Dataset](https://github.com/JihadZa/IADD)
- Aggregated dialect-ID dataset merging DART, SHAMI, PADIC, AOC, and **TSAC** — so it embeds a Tunisian subset. Zahir et al., 2021.
- Data paper: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352340921010519). **[open]** (GitHub).

### [QADI — QCRI Arabic Dialect Identification](https://alt.qcri.org/resources/qadi/)
- Country-level dialect-ID tweets across 18 countries; the Tunisian subset is ~8,879 items (as folded into the LinTO Derja aggregate). QCRI.
- **[open]** (QCRI resources page).

### [ArapTweet](https://aclanthology.org/L18-1111/)
- Large multi-dialect Arabic Twitter corpus for gender, age, and language-variety identification, covering 11 Arab regions including Tunisia. Zaghouani and Charfi, LREC 2018.
- **[on request]** (contact authors); Tunisian is one regional subset.

### Multi-Dialect, Multi-Genre Corpus of Informal Written Arabic (LREC 2014)
- Cotterell and Callison-Burch. Informal Arabic across five dialect groups including **Maghrebi** (Tunisian-relevant). Paper: [LREC 2014](https://aclanthology.org/L14-1006/). **[on request]**.

### [Arabic Dialect Identification shared-task data (LREC 2018)](https://github.com/drelhaj/ArabicDialects/tree/master/ArabicSharedTask)
- Dialect-ID train/test data including Maghrebi/Tunisian-relevant material.
- **[open]** (GitHub).

### [PADIC — Parallel Arabic Dialect Corpus](https://smart.loria.fr/corpora/)
- Also usable for dialect ID; one of six dialects is Tunisian. Full details under [Machine translation and parallel corpora](#machine-translation-and-parallel-corpora).

### Sub-dialect identification (within Tunisian)
- [Text and Speech-based Tunisian Arabic Sub-Dialects Identification (LREC 2020)](https://aclanthology.org/2020.lrec-1.787/) — Kchaou, Ben Abdallah, Bougares. Distinguishes Tunis / Sfax / Sousse / Tataouine. A released benchmark rather than an organized competition. **[open]** (paper).

---

## Treebanks and syntactic resources

### [TArC — Tunisian Arabish Corpus](https://github.com/eligugliotta/tarc)
- Multi-layer annotated Arabizi corpus. Gugliotta and Dinarelli; first release 2020, complete release 2022.
- 4,797 sentences / ~43,300 tokens (forum, social, blog, rap), with user metadata (governorate, age range, gender).
- Annotation layers: token classification (arabizi/foreign/emotag), Arabic-script transliteration (CODA-TUN), tokenization with clitic splitting, POS (Penn Arabic Treebank style), lemmatization (in progress). CC BY-NC-SA 4.0.
- Companion annotation tool: [Multi-Task Sequence Prediction System (GitLab)](https://gricad-gitlab.univ-grenoble-alpes.fr/dinarelm/tarc-multi-task-system).
- Papers: [LREC 2022](https://aclanthology.org/2022.lrec-1.121/) ([arXiv:2207.04796](https://arxiv.org/abs/2207.04796)), [LREC 2020](https://aclanthology.org/2020.lrec-1.770/), [WANLP 2020](https://aclanthology.org/2020.wanlp-1.16/). Mirror: HF [arbml/TArC](https://huggingface.co/datasets/arbml/TArC). **[open]**.

### [TTB — Tunisian Treebank + parser](https://github.com/AsmaMekki/TA-Parser)
- Constituency/syntactic treebank and a trained Stanford-parser model. Mekki, Zribi, Ellouze, Belguith (ANLP-RG, Sfax), 2020.
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
- See [TArC](#treebanks-and-syntactic-resources): ~43k Arabizi tokens with Penn Arabic Treebank-style POS. **[open]**.

### [POS-tagging of Tunisian Dialect Using Standard Arabic Resources (WANLP 2015)](https://aclanthology.org/W15-3207/)
- Hamdi, Nasr, Habash, Gala. Maps Tunisian to an MSA lattice and tags with an MSA tagger (~89% accuracy). Method paper; no standalone gold TD POS corpus released. **[open]** (paper).

### Fine-Grained POS Tagging of Spoken Tunisian Dialect (Springer NLDB 2014)
- Boujelbane, Mallek, Ellouze, Hadrich-Belguith. Builds a TD training corpus by converting an MSA corpus via a bilingual lexicon (~78.5% accuracy).
- **[paywalled]** ([Springer](https://link.springer.com/chapter/10.1007/978-3-319-07983-7_9)).

---

## Morphology (analyzers and disambiguation)

### [Intelligent Tunisian Arabic Morphological Analyzer — evaluation corpus](https://github.com/NadiaBMKarmani/Intelligent-Tunisian-Arabic-Morphological-Analyzer-evaluation-corpus)
- 1,000 Tunisian words used to evaluate the Karmani analyzer. Nadia Ben Mohamed Karmani (REGIM, Sfax), ~2016.
- Paper: AICCSA 2016 ([IEEE](https://ieeexplore.ieee.org/document/7945666)). **[open]** (GitHub; paper paywalled).

### [Tunisian-Arabic-Lexical-Dictionary](https://github.com/NadiaBMKarmani/Tunisian-Arabic-Lexical-Dictionary)
- XML lexicon of the main Tunisian clitics, used by the Karmani analyzer/tokenizer.
- **[open]** (GitHub).

### Al-Khalil-TUN — Morphological Analysis of Tunisian Dialect (IJCNLP 2013)
- Zribi, Ellouze Khemakhem, Hadrich Belguith. Adapts the MSA Al-Khalil analyzer with a purpose-built Tunisian lexicon (~30k words). Analyzer and lexicon not publicly downloadable.
- **[paper only]** ([paper](https://www.academia.edu/4516863/)).

### [Morphological Disambiguation of Tunisian Dialect (J. King Saud Univ., 2017)](https://www.researchgate.net/publication/313035715_Morphological_Disambiguation_of_Tunisian_Dialect)
- Zribi, Ellouze, Hadrich-Belguith, Blache. ML disambiguation over the analyzer output (~87–88% accuracy). Journal of King Saud University – Computer and Information Sciences 29(2), pp. 147–155. **[open]** (article).

---

## Named Entity Recognition

The most useful openly available NER building blocks are the **Barcha** gazetteers (below). A token-annotated gold NER *corpus* specific to Tunisian has not been openly released yet. Known work:

### [Barcha](https://github.com/wa3dbk/Barcha)
- Open multi-purpose Tunisian resource (MIT). wa3dbk. Its `named_entities/` folder is a set of curated Tunisian entity gazetteers: people (academics/scientists, artists, footballers, media figures, poets, politicians, trade unionists, writers), institutions/associations/companies, government institutions, cities, universities (public and private), ISETs, political parties, and unions. Also ships a `texts/` raw-text folder and a `translation/` folder (Tunisian↔English/MSA).
- These are gazetteers/word lists rather than a token-annotated corpus, but they are the best open NER starting point for Tunisian. **[open]**.

### TUNER — NER of Tunisian Arabic with Bi-LSTM-CRF (2023)
- Hybrid Bi-LSTM-CRF + rules, F-measure 91.43%; involves an annotated Tunisian NER corpus that is not publicly released.
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
- [Phrase-based SMT + 5,000-sentence Tunis↔MSA corpus (IBIMA)](https://ibima.org/accepted-paper/building-a-tunisian-dialect-into-modern-standard-arabic-parallel-corpus-for-a-phrase-based-machine-translation/) — Sghaier and Zrigui. **[on request]**.

### Community HuggingFace parallel sets
- [tunis-ai/tunisian-msa-parallel-corpus](https://huggingface.co/datasets/tunis-ai/tunisian-msa-parallel-corpus) and [tunis-ai/MADAR-TUN](https://huggingface.co/datasets/tunis-ai/MADAR-TUN) (~30k) — Derja↔MSA. Tunisia.AI, 2025. **[open]**.
- [NadiaGHEZAIEL/English_to_Tunisian_Dataset](https://huggingface.co/datasets/NadiaGHEZAIEL/English_to_Tunisian_Dataset) (~1.7k) — English→Tunisian. Nov 2025. **[open]**.
- [khaled123/Tunisianderjasynthtranslation](https://huggingface.co/datasets/khaled123/Tunisianderjasynthtranslation) (~436k, synthetic) and the Kaggle [drejja-to-english](https://www.kaggle.com/datasets/khawlajlassi/drejja-to-english) (~13k) — Derja↔English. **[open]**.
- [Barcha](https://github.com/wa3dbk/Barcha) — its `translation/` folder holds Tunisian↔English/MSA parallel data (also has NER gazetteers and raw texts; see [NER](#named-entity-recognition)). **[open]**.

### Speech translation corpora with Tunisian↔English/French text
- **TuniFra** (Tunisian↔French, 15h), **TEDxTN** and **IWSLT 2022/2023 Tunisian–English** are three-way (audio + transcript + translation) and are listed in [SPEECH.md](SPEECH.md); their transcript/translation layers are also Tunisian–French / Tunisian–English bitext.

---

## Transliteration and Arabizi

### [TArC](https://github.com/eligugliotta/tarc) + [Multi-Task Sequence Prediction tool](https://aclanthology.org/2020.wanlp-1.16/)
- Annotated Arabizi corpus and the neural tool that transliterates Arabizi→CODA Arabic script and does tokenization/POS. Gugliotta, Dinarelli, Kraif. Code on [GitLab](https://gricad-gitlab.univ-grenoble-alpes.fr/dinarelm/tarc-multi-task-system). **[open]**.

### Masmoudi et al. — Arabizi→Arabic-script transliteration for Tunisian
- [Transliteration of Arabizi into Arabic Script for Tunisian Dialect (ACM TALLIP 2019)](https://dl.acm.org/doi/10.1145/3364319) — rule-based + CRF, WER 14.55%. **[paywalled]**.
- [Preliminary investigation (CICLing/Springer 2015)](https://link.springer.com/chapter/10.1007/978-3-319-18111-0_46) and an [HMM approach](https://www.researchgate.net/publication/314034927). **[paywalled]**.

### Younes et al. — bi-script Tunisian resources
- [Romanized Tunisian Dialect Transliteration using Sequence Labelling (J. King Saud Univ. 2020)](https://www.sciencedirect.com/science/article/pii/S1319157820303281). **[open]** (paper).
- [Building Bi-script Language Resources for the Tunisian Dialect (Procedia 2021)](https://www.sciencedirect.com/science/article/pii/S1877050921012254) — 284,894 Romanized messages; two bi-script dictionaries (Latin→Arabic 293,570 entries; Arabic→Latin 155,954 entries). Data not openly hosted. **[paper only]**.
- [Seq2Seq double transliteration (Procedia 2018)](https://www.sciencedirect.com/science/article/pii/S1877050918321859). **[open]** (paper).

---

## Orthography (CODA)

### [A Conventional Orthography for Tunisian Arabic (CODA-TUN)](https://aclanthology.org/L14-1214/)
- The canonical Tunisian CODA spec (Arabic-script conventional orthography). Zribi, Boujelbane, Masmoudi, Ellouze, Belguith, Habash, LREC 2014. [PDF](http://www.lrec-conf.org/proceedings/lrec2014/pdf/219_Paper.pdf). **[open]**.

### [CODA* — Unified Conventional Orthography for Dialectal Arabic](https://camel-guidelines.readthedocs.io/en/latest/orthography/)
- Cross-dialect orthography framework (covers Tunisian). Habash et al., LREC 2018. [PDF](https://camel.abudhabi.nyu.edu/madar/static/pdfs/2018-LREC-CODA-STAR.pdf). **[open]**.

### [A Conventional Orthography for Maghrebi Arabic (LREC 2016)](https://aclanthology.org/L16-1352/)
- Turki, Adel, Gibson, Zribi. Extends CODA across Maghrebi (incl. Tunisian). **[open]**.

### NOTA — Normalized Orthography for Tunisian Arabic (Springer 2025)
- Adaptation/normalization of CODA* for Tunisian. **[paywalled]** ([Springer](https://link.springer.com/chapter/10.1007/978-3-031-85067-7_13)).

---

## Lexicons, dictionaries, wordnets

### [aebWordNet — Lexicon](https://github.com/NadiaBMKarmani/aebWordNet-Lexicon)
- Tunisian (`aeb`) WordNet in ISO-LMF format. Karmani, Soussou, Alimi (REGIM, Sfax), 2015. Built from the Peace Corps English–TA dictionary and projected from Princeton WordNet 3.1 (~18,209 synsets). **[open]** (GitHub; [ACLing 2015 paper](https://ieeexplore.ieee.org/document/7422271) paywalled).

### TunDiaWN — Tunisian dialect WordNet (WANLP 2014)
- Bouchlaghem and Elkhlifi. Corpus-based wordnet reusing English + Arabic wordnets. Database not found for download.
- **[paper only]** ([WANLP 2014](https://aclanthology.org/W14-3613/)).

### [Peace Corps English–Tunisian Arabic Dictionary](https://archive.org/details/ERIC_ED183017)
- 1977 two-way English↔Tunisian dictionary with phonetics and grammar notes; the seed lexicon (5,133 words) for aebWordNet. Companion [Peace Corps Tunisian Arabic course](https://www.livelingua.com/course/peace_corps/spoken_tunisian_arabic). **[open]** (Internet Archive).

### [Derja.Ninja](https://derja.ninja/)
- Community Tunisian↔English dictionary, ~17,000 entries with example sentences and audio. Scraper: [ArmelVidali/derja_ninja_scraper](https://github.com/ArmelVidali/derja_ninja_scraper). **[open]** (web).

### [Webonary "Tunsi" dictionary](https://www.webonary.org/tunsi/)
- Online Tunisian Arabic dictionary. **[open]** (web).

### [Wiktionary — Tunisian Arabic](https://en.wiktionary.org/wiki/Category:Tunisian_Arabic_language)
- Collaborative lexicon plus a [Swadesh list](https://en.wiktionary.org/wiki/Appendix:Tunisian_Arabic_Swadesh_list). **[open]**.

### Bilingual lexicons from the literature (Tunisian↔MSA)
- Boujelbane et al., [Building bilingual lexicon to create Dialect Tunisian corpora (WANLP 2013)](https://aclanthology.org/W13-2813/). **[paper only]**.
- Sadat et al., TDA–MSA lexicon (COLING LG-LP 2014, [ResearchGate](https://www.researchgate.net/publication/293485844)). **[paper only]**.
- [MADAR Lexicon](http://nlp.qatar.cmu.edu/madar/) — multi-dialect, includes Tunis and Sfax entries. **[on request]**.

---

## LLM evaluation benchmarks

### [TounsiBench](https://github.com/Souha-BH/TounsiBench-Benchmarking-Large-Language-Models-for-Tunisian-Arabic)
- The dedicated Tunisian LLM instruction benchmark. Ben Hassine, Arrak, Addhoum, Wilson (CoCoA Lab, Univ. of Michigan-Flint), EMNLP 2025.
- 744 Tunisian instructions with gold human responses; ten Arabic-claiming LLMs scored by humans and an LLM judge on quality, correctness, relevance, dialectal adherence. Finding: most LLMs struggle in Tunisian.
- Repo: [Souha-BH/TounsiBench-…](https://github.com/Souha-BH/TounsiBench-Benchmarking-Large-Language-Models-for-Tunisian-Arabic) (`data/` = instructions, native gold responses, topic labels, evaluated model outputs; plus a GPT-4o evaluation notebook to score your own model). Paper: [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1756/). **[open]**.

### [How Well Do LLMs Understand Tunisian Arabic?](https://arxiv.org/abs/2511.16683)
- Parallel Tunizi ↔ standard Tunisian ↔ English corpus with sentiment labels; benchmarks LLMs on transliteration, translation, sentiment. Mahdi et al., 2025. **[open]** (arXiv).

### [linagora/TunisianMMLU](https://huggingface.co/datasets/linagora/TunisianMMLU)
- MMLU-style multiple-choice evaluation benchmark in Tunisian Derja, ~21.7k rows. LINAGORA, 2025. Built to evaluate the Labess LLM in-dialect.
- **[open]** (HuggingFace).

### [Nehdi/TuniziBigBench](https://huggingface.co/datasets/Nehdi/TuniziBigBench)
- Benchmark dataset for Tunisian/local dialects, LLM-eval oriented. Size/tasks not fully verified. **[open]** (HuggingFace).

---

## LLM training and evaluation datasets

The instruction / SFT / DPO / synthetic data layer behind the Tunisian LLMs in [MODELS.md](MODELS.md#generative--instruction--chat-llms). Mostly 2025–2026, mostly open, and mostly unreviewed community data, quality varies, so treat sizes as raw counts.

### LINAGORA / Labess training stack
- [linagora/Tunisian_Derja_Dataset](https://huggingface.co/datasets/linagora/Tunisian_Derja_Dataset) — 2.23M-row Derja corpus used for continual pre-training (also listed under raw corpora). **[open]**.
- [wghezaiel/SFT-Tunisian-Derja](https://huggingface.co/datasets/wghezaiel/SFT-Tunisian-Derja) (~40k), [wghezaiel/DPO-Tunisian-Derja](https://huggingface.co/datasets/wghezaiel/DPO-Tunisian-Derja) (~44k), [wghezaiel/SFT_derja_dataset](https://huggingface.co/datasets/wghezaiel/SFT_derja_dataset) (~48k), [wghezaiel/derja_to_msa_dataset](https://huggingface.co/datasets/wghezaiel/derja_to_msa_dataset) (~18k), [wghezaiel/fw_tunisian_derja](https://huggingface.co/datasets/wghezaiel/fw_tunisian_derja) (~37k), [wghezaiel/TunisianWikipedia-QA](https://huggingface.co/datasets/wghezaiel/TunisianWikipedia-QA) (~34k). Wajdi Ghezaiel (LINAGORA), 2025. The SFT/DPO alignment stack behind Labess. **[open]**.

### ESPRIT
- ESPRIT-Derja-Instruct — ~7,013 bilingual Arabic/Arabizi Tunisian instruction pairs distilled from GPT-4o; trains the [ESPRIT-Derja-Qwen3-8B](https://huggingface.co/ESPRIT-Group/ESPRIT-Derja-Qwen3-8B-v2) model. **[open]** (bundled with the model repo).

### Tunisia.AI / khaled123 (Khaled Bouzaiene)
- [khaled123/Tunisian_Dialectic_English_Derja](https://huggingface.co/datasets/khaled123/Tunisian_Dialectic_English_Derja) (~1.66M rows, Derja↔English, translations + sentiment + generation), [khaled123/tunisiansynthinstract](https://huggingface.co/datasets/khaled123/tunisiansynthinstract) (~266k synthetic instructions), [khaled123/Tunisianderjasynthtranslation](https://huggingface.co/datasets/khaled123/Tunisianderjasynthtranslation) (~436k), [khaled123/tuniset](https://huggingface.co/datasets/khaled123/tuniset) (~29k). 2024. **[open]**. (Note: this account hosts many datasets of uneven quality — some are noisy dumps; verify before use.)

### Other
- [Datasmartly/darja-tunisie-chat](https://huggingface.co/datasets/Datasmartly/darja-tunisie-chat) — Tunisian chat dataset, 2025. **[gated]** (must accept conditions; no card).
- [abdouuu/tunisian_chatbot_data](https://huggingface.co/datasets/abdouuu/tunisian_chatbot_data) — ~1,426 instruction pairs, 2024. Weak as a Derja-generation set (questions in Derja, answers largely MSA/English). **[open]**.

---

## Surveys

- [Language resources for Maghrebi Arabic dialects' NLP: a survey (LREV 2020)](https://link.springer.com/article/10.1007/s10579-020-09490-9) — Younes, Souissi, Achour, Ferchichi. Catalogs 158 Maghrebi (incl. Tunisian) resources. The most thorough survey for Tunisian coverage.
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

- **NADI — Nuanced Arabic Dialect Identification** ([portal](https://nadi.dlnlp.ai/), [GitHub](https://github.com/UBC-NLP/nadi)). Tunisia is a target country each edition: [2020](https://aclanthology.org/2020.wanlp-1.9/), [2021](https://aclanthology.org/2021.wanlp-1.28/), [2022](https://aclanthology.org/2022.wanlp-1.9/), [2023](https://aclanthology.org/2023.arabicnlp-1.62/), [2024](https://aclanthology.org/2024.arabicnlp-1.79/) (includes a Tunisian→MSA MT subtask). NADI 2025 and [NADI 2026](https://nadi.dlnlp.ai/2026/) added speech tracks — see [SPEECH.md](SPEECH.md).
- **[MADAR Shared Task 2019](https://aclanthology.org/W19-4622/)** — city-level dialect ID (25 cities incl. Tunis and Sfax) + Twitter user dialect ID.
- **[IWSLT 2022 / 2023 dialectal speech translation](https://iwslt.org/2022/dialect)** — Tunisian↔English (see [SPEECH.md](SPEECH.md)).
- **[Arabic Dialect Identification (LREC 2018)](https://github.com/drelhaj/ArabicDialects/tree/master/ArabicSharedTask)** — earlier DID benchmark with Tunisian-relevant data.

---

## Other resource lists

- [mena-open-data/tunisian-dataset](https://huggingface.co/collections/mena-open-data/tunisian-dataset) — HuggingFace collection of ~55 Tunisian datasets; the single richest live index found.
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
  title        = {Tunisian Arabic {NLP} Resources: A Curated Inventory},
  year         = {2026},
  howpublished = {\url{https://github.com/jjlalli/Tunisian-NLP-Resources}},
  note         = {Living inventory of datasets, models, and papers for Tunisian Arabic (aeb)}
}
```

*A paper describing this inventory is in preparation; this entry will be updated when it is available.*

## License

The list itself is released under [CC BY 4.0](LICENSE). The linked resources keep their own licenses — check each entry.

---

*Maintained by Fatma Jlali. Contributions and corrections welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Last compiled: July 2026.*
