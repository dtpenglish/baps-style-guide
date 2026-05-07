# 10.6 Transliteration
The largest open-questions list. These questions cover the rules of romanizing Gujarati and Devanagari script — what to do about diacritics, ligatures, the "stray *a*", visarga and anusvara, hyphenation, and the many cases where a single Gujarati word has multiple plausible roman spellings.

## 10.6.1 Source Scripts and Target Script
- Gujarati script (*lippi*) and the corresponding roman transliteration.
- Devanagari script (*lippi*) for Sanskrit and Hindi, and the corresponding roman transliteration.

## 10.6.2 Diacritics — Yes, No, Which?
- **With or without** diacritics?
- Transliterations in **prose vs verse** — different rules?
- If with diacritics, **which system**? Macron, underpoint, overpoint, etc.
- If without diacritics, do we use long-vowel doublings such as **aa / oo / ee**?

For the current rules, see [SAP Diacritics Policy](../diacritics/sap-policy.md) and [Macron-Only Convention](../diacritics/macron-convention.md). The questions above are about **whether and when** those rules should evolve.

## 10.6.3 Ligatures
How to render conjunct consonants:

- *ksha* / *kṣa*
- *pta* / *pṭa*
- *kta*
- …

## 10.6.4 Single-Letter Choices
- Which variation: **jn / gn**? (*jnan* vs *gnan*; *yajna* vs *yagna*.)
- **વ**: *v* or *w*? (*Vachanamrut* vs *Wachanamrut*; *Bhagwan* vs *Bhagvan*.)
- **ળ**: *l* (not *d*)?
- **ઈ / ઇ**: *i* or *y*?
- **Dental vs. retroflex *t* / *d* (Sanskrit / Hindi material)**: South-Indian transliteration distinguishes *t* (retroflex ट) from *th* (dental त), and *d* (retroflex ड) from *dh* (dental द) — so *Lata* would be लटा and *Latha* लता. North-Indian / Hunterian transliteration (which SAP currently follows) uses *t* and *d* for both, accepting the dental/retroflex ambiguity in romanization. Mostly relevant in Sanskrit and Hindi sources; less so for Gujarati base material. Names like *Mata*, *Pita*, *Vidya*, *Bhagwat* — no *th* / *dh* in the SAP convention.

## 10.6.5 Initial Long Vowels
- Initial **ā**: *a* or *aa*? Same with *oo* / *ee*.
  - *arti* / *aarti*
  - *agna* / *aagnaa*

## 10.6.6 The "Stray *a*" in Mid-Word and Word-Final Position
A long-running question: do we keep the inherent *a* of the Devanagari/Gujarati script, drop it, or split the difference? Examples:

- acharan / aacharan / achran / aacharan
- paranu / parnu
- karata / karta
- karavu / karvu
- spashta / spasht
- Atmatrupta / Atmatrupt
- dandavat / dandvat
- darbha / darbh
- dev / deva
- devta / devata
- lok / loka
- garbhagruh / garbhagruha
- ghantadi / ghantdi
- kam / kama
- pran / prana
- pratyaksh / pratyaksha
- rajogun / rajoguna
- Sampraday / Sampradaya
- brahmavidya / brahmvidya

## 10.6.7 Visarga and Anusvara
- **Visarga**: *‑h* or *‑h + vowel*?
- **Anusvar / anusvara**: *n* or *m*?
  - ankh
  - ansh(a) / amsh(a)
  - ang(a)
  - hans(a)
  - hinsa / himsa
  - uchu / unchu

## 10.6.8 Avagraha
> avagrah(a): indicate with an apostrophe — '

(Adopted as a tentative rule.)

## 10.6.9 Hyphenation vs Open Compounds
Hyphenate, leave open as separate words, or close up?

- nagar yatra / nagaryatra / nagar-yatra
- murti pratishtha / murti-pratishtha
- Pramukh Swami / Pramukhswami
- Aksharpurushottam / AksharPurushottam / Akshar-Purushottam
- akshar mukta / akshar-mukta
- Janma Mahotsav / Janmamahotsav / Janma-mahotsav / Janma-Mahotsav / Janmotsav
- Jal-Jhilani / Jal Jhilani

## 10.6.10 When to Split a Gujarati Compound
- mahapuja
- mahamantra
- Bhumapurush / Bhuma-Purush / Bhuma Purush
- Prakrutipurush / Prakruti-Purush / Prakruti Purush
- brahmabhojan / brahma-bhojan / brahma bhojan
- brahmisthiti / brahmi-sthiti / brahmi sthiti
- panchtattva / panch tattva
- sankhyayogi(ni) / sankhya yogi(ni) / sankhya-yogi(ni)

## 10.6.11 Anglicized Words with Alternative Transliterated Spellings
- *atma* / atman
- *champal* / chappal
- *rushi* / rishi
- samskara / sanskar / samskar
- sloka / shlok / shloka

## 10.6.12 Variations in the Gujarati Spelling of the Same Word
- cheshta / cheshtha
- divo / diya
- sat-chit-anand / sat-chid-anand

## 10.6.13 Alternative Transliterations
Two or more roman spellings circulating for the same Gujarati word:

- chikoo / chiku
- chitt / chitta
- Fagun / Fagan / Falgan
- gataryu / gatariyu
- rupchoki / roopchoki
- sanhkya / Samkhya
- jai naad / jay naad
- lila / leela

## 10.6.14 Alternative Anglicizations
- laddu / laddoo / ladoo

## 10.6.15 Caps or Lower Case
- Advaita / advaita
- Dvait / dvaita
- Darshan / darshan
- Uttarayan / dakshinayan

## 10.6.16 Suffixes (and Prefixes?)
- dakshini pagh / dakshi ni pagh / dakshi-ni pagh
- rajasik / rajasic / rajsik / rajsic
- mayik / mayic

## 10.6.17 Festivals
- Jal Jhilani / Jal-Jhilani
- Rathyatra / Rath Yatra / Rath-Yatra

## 10.6.18 How to Use This List
Each item above will eventually become a row in the [glossary](../diacritics/glossary-reference.md), with one preferred form. Until then, treat any of the listed forms as acceptable, but **be consistent within a single publication**.

When the team decides on a preferred form, update this page and add an entry to the [changelog](../changelog.md).

## 10.6.19 Have an Opinion?
Click the pencil icon, or open a [GitHub Issue](https://github.com/dtpenglish/baps-style-guide/issues/new) titled `Translit: <word>` — e.g. `Translit: jn vs gn`.
