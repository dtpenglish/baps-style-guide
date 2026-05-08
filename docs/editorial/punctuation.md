# 3.9 Punctuation
## 3.9.1 Quotation Marks
SAP uses **typographers' (curly) quotes** throughout — single and double — and reserves the two marks for distinct purposes.

- **Single quotes — primary mark.** Use ' ' for highlighting a word or phrase: a term in a special or technical sense, a motto presented as a phrase, the gloss of an Indic term, the title of a short work, a quoted excerpt of authoritative text.
- **Double quotes — speech only.** Use " " for direct speech and dialogue: someone quoted as saying or shouting something.
- **Nested.** Inside double-quoted speech, use single quotes; inside single-quoted highlights, use double — invert the marks at each level.
- Always use **typographers' (curly) quotes**: ' ' " ". Straight quotes (`'` `"`) are typewriter relics; reserve them for code samples and form-field examples.

When typing in source files, plain straight `'` and `"` are auto-converted to the curly forms when the site renders, so authors don't need to enter the Unicode characters by hand. Where you genuinely need to show a *literal* straight quote (e.g. when documenting a code sample), wrap it in backticks so the auto-conversion skips it.

For quotation marks specifically around translations of Indic terms, see [Quotation Marks](quotation-marks.md).

## 3.9.2 Dashes
| Mark | Use |
|---|---|
| Hyphen (`-`) | Simple compounds: *non-violence*, *forty-three*, *well-known*, *selfless-love*. |
| En dash (`–`) | Number and date ranges: *pp. 12–18*, *2000–2025*. Place pairs: *Mumbai–Ahmedabad*. Complex compounds: *Hindu–Christian dialogue*, *Vedanta–Yoga synthesis*. |
| Em dash (`—`) | Parenthetical breaks: *Bhagwan Swaminarayan — then known as Sahajanand Swami — addressed the assembly.* |

In InDesign, use the proper Unicode characters (en dash <kbd>U+2013</kbd>, em dash <kbd>U+2014</kbd>), not double or triple hyphens.

For compound modifiers with numbers (*twenty-nine members*, *a 5-pound bag*, *an 18th-century novel*) and the rules on hyphenation between numerals and units, see [Numbers §3.7.5](numbers.md#375-compound-modifiers-and-unit-spacing).

## 3.9.3 Series and the Oxford Comma
Use the Oxford (serial) comma in lists of three or more:

> The Vachanamrut, the Shikshapatri, and the Swamini Vato are foundational texts.

Not:

> The Vachanamrut, the Shikshapatri and the Swamini Vato are foundational texts.

## 3.9.4 Ellipses
A genuine ellipsis is a single character (<kbd>U+2026</kbd>: …), not three full stops with spaces. When indicating omitted text within a quotation, use a single ellipsis with a space on each side: *the discourse … turned to the nature of bhakti.*

## 3.9.5 Spacing
- **One space** after a period, comma, colon, semicolon — never two.
- **No space** before a footnote superscript: *…the discourse.¹*
- **No space** around an em dash in tight contexts (print preference); a single space on each side in this guide and in digital contexts: *…the discourse — and the silence that followed.*

## 3.9.6 Footnote Superscripts — Placement
Place the superscript number **after the punctuation** when the note refers to the whole sentence or phrase. Place it **before the punctuation** (immediately after the word) when the note refers to a specific word or term.

| Reference of the note | Placement | Example |
|---|---|---|
| Whole sentence or quotation | After the closing punctuation | *…the term used was 'bahyadrashti'.¹* |
| Specific word | Immediately after the word, before the punctuation | *…the term used was 'bahyadrashti'¹.* |

### 3.9.6.1 Footnote Numbers with Colons and Semicolons
The superscript goes **before** a colon or semicolon, regardless of what the note refers to:

- The study claimed that 'results were reproducible'²; however, later attempts failed.
- He raised three concerns³: funding, scope, and timing.

This is the BrE convention; commas and full stops still take the superscript after, per the rule above.

### 3.9.6.2 Footnote Numbers with Quoted Material
When the footnote refers specifically to **quoted material** within a sentence, the superscript goes immediately after the closing quotation mark:

- According to Wilson, the policy was 'fundamentally flawed'² in its approach to regulation.

When the footnote refers to a specific word *inside* the quoted text, place it immediately after that word:

- The manuscript referred to '*alien*¹ visitors' throughout the text.

When the sentence ends with quoted material and the note refers to the whole sentence or quotation, the superscript follows the final punctuation:

- Smith argued that 'economic factors were the primary cause of the uprising'.⁴

Apply these rules consistently within a publication.

## 3.9.7 Abbreviations and Acronyms

### 3.9.7.1 Periods — Truncations vs. Contractions
The general principle: a period marks something **omitted at the end** of a word; no period when only **interior letters** are dropped.

| Type | Period? | Examples |
|---|---|---|
| **Truncation** (end omitted) | ✅ Yes | *Mon.*, *Tues.*, *Wed.*, *Prof.*, *vol.*, *cont.*, *etc.* |
| **Contraction** (interior dropped) | ❌ No | *Mr*, *Mrs*, *Dr*, *Revd*, *St* (Saint), *Ltd* |
| **All-cap acronym / initialism** (2+ letters) | ❌ No | *BAPS*, *CMS*, *EPUB*, *PDF*, *USA*, *BBC*, *NATO*, *PhD*, *CEO* |
| **Personal name initials** | ❌ No (BrE) | *TS Eliot*, *RK Narayan* (no spaces, no periods). The older *T. S. Eliot* form is acceptable but unspaced is preferred. |
| **Classical Latin abbreviations** | ✅ Yes | *V.S.* (Vikram Samvat), *e.g.*, *i.e.*, *etc.* |

*V.S.* takes a non-breaking space before the year: *V.S.&nbsp;2080*. (In Markdown source: `V.S.&nbsp;2080`.)

### 3.9.7.2 Acronyms vs. Initialisms
- **Acronyms** are pronounced as words: *NATO*, *NASA*, *BAPS*, *AIDS*, *COVID*. No full stops between letters.
- **Initialisms** are spelled out letter by letter: *BBC*, *MEP*, *USA*, *CMS*, *PDF*. No full stops between letters.

### 3.9.7.3 Capitalization by Length
- **Five letters or fewer** — uppercased throughout: *BAPS*, *NASA*, *NATO*, *AIDS*, *COVID*, *EPUB*.
- **Six letters or more** — usually initial capital plus lowercase: *Unesco*, *Unicef*, *Interpol*, *Benelux*.
- Exceptions follow the entity's own convention — some longer acronyms (e.g. *UNESCO*) are styled all-caps by the organization itself; follow the established form.

### 3.9.7.4 Articles before Acronyms
- **Initialisms** generally take *the*: *the BBC*, *the EU*, *the UK*, *the WHO*.
- **Acronyms** generally do not: *NATO meets in Brussels*, *NASA launched*, *BAPS publishes*.
- Company and university names follow the entity's own convention: *ICI*, *IBM*, *UCL*.

### 3.9.7.5 First Mention — Spell Out, Then Abbreviate
On first appearance in a document, write out the full term followed by the abbreviation in parentheses:

> The Emissions Trading Scheme (ETS) should enable us to meet our targets.

Subsequent mentions use the abbreviation alone. In long documents, repeat the spell-out at the first occurrence in each major section.

If an abbreviation appears only once or twice in a piece, dispense with it — use the full form throughout. Well-known abbreviations (*BAPS*, *EU*, *UN*, *USA*) need not be spelled out on first use.

### 3.9.7.6 Plurals of Abbreviations
Add a lowercase *s* — **no apostrophe**:

- *MEPs*, *NGOs*, *PCs*, *CDs*
- *1920s*, *747s*

Apostrophe-*s* is reserved for the possessive: *MEPs' salaries*, *the BBC's coverage*.

For abbreviations ending in *S*, the plural can take a final *s* (*SOSs*) or be left to stand for both singular and plural where unambiguous (*PES* = "public employment service(s)"). Use the full plural term when ambiguity threatens.

### 3.9.7.7 Commas with *i.e.*, *e.g.*, and *etc.*
*i.e.* and *e.g.* take a comma **before** them in running text and a comma **after** them. This is the Oxford-aligned style; SAP retains the comma after for clarity in formal and devotional writing, even though some BrE publications omit it.

- ✅ The soul experiences three states, **i.e., waking, dreaming, and deep sleep.**
- ✅ Several rituals are common, **e.g., puja, arti, and havan.**
- ❌ The soul experiences three states, *i.e. waking, dreaming, and deep sleep.* *(no comma after)*
- ❌ The soul experiences three states *i.e., waking, dreaming, and deep sleep.* *(no comma before)*

*etc.* takes a comma **before** it when it follows a list of three or more items, and a comma **after** it only when the sentence continues:

- ✅ He renounced wealth, possessions, status, **etc.** *(end of sentence — no comma after)*
- ✅ The shop sold notebooks, pens, paper, **etc.,** at wholesale prices. *(sentence continues — comma after)*
- ❌ He renounced wealth and **and etc.** *(redundant — drop *and*)*

Use *etc.* only at the end of a list, never with *and* preceding it. In formal writing where the implied additional items might be unclear, *and so on* or *and similar items* often reads better than *etc.*

## 3.9.8 Vertical Lists

### 3.9.8.1 Bullets, Numbers, or Letters?
- **Bullets** — for unordered lists where items have no inherent sequence or hierarchy.
- **Numbers** — for ordered lists: steps in a process, ranked items, sequences where order matters.
- **Letters** — when items must be referenceable elsewhere ("see item c") but no specific order is implied.

### 3.9.8.2 Parallel Construction
All items in a list must share the same logical and grammatical structure:

- all single words of the same part of speech (all nouns, all adjectives, all verb phrases);
- all phrases of the same construction;
- all subordinate clauses; or
- all main clauses (full sentences).

When the structure breaks, the meaning becomes ambiguous and the list looks ragged.

### 3.9.8.3 Punctuation and Capitalization
The conventions depend on whether the items are short fragments that continue from the lead-in, or full sentences in their own right.

**Short phrases that continue from the lead-in** (lead-in + any item reads as one sentence) — lowercase first word, comma after each, period only at the end:

> Sources of funding for community programmes include
>
> - grant funds,
> - earmarked funds,
> - federal funds, and
> - general funds.

If items contain internal commas, use semicolons in place of commas to keep the structure clear:

> Recent developments in language teaching include
>
> - more opportunities for students to speak in the target language;
> - greater emphasis on effective communication and less on error correction;
> - the use of interweaving, spiraling, and recycling techniques; and
> - the connection of language learning with instruction in other subject areas.

**Full sentences** — capitalize each item's first word and end with terminal punctuation; **no** *and* / *or* between the last two:

> Employees who do not pass the certification exam will be retested:
>
> - Candidates who scored below 550 must retake the full battery.
> - Candidates who scored 550 or higher may be permitted a partial administration.
> - No more than three sessions may be scheduled in one calendar year.

If even one item is a full sentence, treat all items as sentences (caps + periods).

**Standalone bullet lists** (catalog-style, not connecting back to a lead-in clause) — the SAP default for short reference lists: capitalize the first word, no end punctuation. Used widely on this site:

> Pages in this section
>
> - Tone & Voice
> - Capitalization
> - Italics
> - Plurals

### 3.9.8.4 Introducing a List
- **Colon** — when the lead-in is a complete sentence (a main clause that could end with a period at that point).
  > The Vachanamrut quotes from three primary sources:
- **No punctuation** — when the lead-in is an incomplete construction that needs the items to complete it.
  > The discourse drew from
  >
  > - the Vedas,
  > - the Bhagavad Gita, and
  > - the Vachanamrut.

A colon should not appear after an incomplete lead-in (*"such as:"*, *"include:"*, *"are:"* — when the words before the colon couldn't logically end a sentence).

## 3.9.9 Apostrophes

### 3.9.9.1 Possessive — Singular Nouns
Form the possessive of a singular noun by adding **'s** — even when the noun ends in *s*, *x*, *z*, or another sibilant:

- Dickens**'s** novels
- Hopkins**'s** poetry
- Bess**'s** dress
- Charles**'s** journey
- the *kothari***'s** assistant
- Bhagwan Swaminarayan**'s** discourses

This follows Chicago and Oxford convention. (AP style would use *Dickens'*, *Hopkins'* — SAP retains the **'s**.)

### 3.9.9.2 Possessive — Plural Nouns
- **Plural ending in *s*** — apostrophe only:
  - the boys**'** books
  - the devotees**'** offerings
  - the Joneses**'** house
  - the sadhus**'** assembly
- **Plural not ending in *s*** — apostrophe + *s*:
  - children**'s** room
  - women**'s** club
  - men**'s** hostel
  - people**'s** choice

### 3.9.9.3 Exceptions — Plural-Form Names and Uninflected Nouns
**Place names and proper names that are plural in form** (ending in *s*) take only an apostrophe in the possessive:

- the United States**'** policy
- Beverly Hills**'** tax hike
- the Beatles**'** first album
- Cisco Systems**'** CEO

**Uninflected nouns** — those whose singular and plural forms are identical and end in *s* (*politics*, *economics*, *mathematics*) — also take only an apostrophe:

- politics**'** downside
- economics**'** central insight

### 3.9.9.4 Plurals of Abbreviations and Single Letters
- **Multi-letter abbreviations** — *no* apostrophe (*CDs*, *NGOs*, *MEPs*, *PhDs*, *1920s*). See [3.9.7.6](#3976-plurals-of-abbreviations).
- **Single letters** — *use* an apostrophe for clarity, since the bare *s* could be misread:
  - mind your **p's** and **q's**
  - cross your **t's** and dot your **i's**
  - she earned all **A's**

### 3.9.9.5 Possessive vs. Attributive in Names and Titles
A noun before another noun can be either **possessive** (apostrophe) or **attributive** (no apostrophe — functioning as an adjective). Both can be grammatically correct; established usage decides which form to use:

| Form | Notes |
|---|---|
| **Mother's Day**, **Father's Day** | Singular possessive. Established usage. |
| **Veterans Day** | Attributive (no apostrophe). U.S. official name. |
| **Mothers' Day** | Plural possessive. Sometimes used; less common. |
| **Buyer's / Buyers' / Buyers Guide** | All in circulation. Pick one and stay consistent. |

For organization names, follow the entity's own form on its official site or publications: *Federal Judges Association*, *Bankers School* (no apostrophe by their own choice).

### 3.9.9.6 Apostrophes in Degrees and Years
- **Degrees** — *bachelor's degree*, *master's degree*, *doctor's degree* take an apostrophe (singular possessive), lowercase. The full form *Bachelor of Arts*, *Master of Science*, *Doctor of Philosophy* takes initial caps and no apostrophe. Abbreviations follow the no-periods rule from [3.9.7.1](#3971-periods-truncations-vs-contractions): *BA*, *BSc*, *MA*, *MSc*, *PhD*, *MBA*, *MD*, *EdD*. Use **BrE-default forms** — *MSc* (not *MS* / *M.S.*), *MA* (not *M.A.*); *PhD* is fine in either variety.
- **Year omitted from a date** — use a closing single quote (**'**, right single quote / U+2019), not an opening single quote:
  - the class of '75   ✅
  - the '60s   ✅
  - in '47, India gained independence   ✅

In Word and most editors with smart-quote autocorrect, the apostrophe at the start of *'75* is auto-formatted as an opening quote (*‘75*). Type the apostrophe twice and delete the first one to force a closing apostrophe.

### 3.9.9.7 What an Apostrophe Doesn't Do
The apostrophe marks possession or contraction — never an ordinary plural:

- ❌ apple**'s** for sale   ✅ apples for sale
- ❌ tomato**'s**, banana**'s**   ✅ tomatoes, bananas
- ❌ in the 1990**'s**   ✅ in the 1990s

This applies to family names too: *the Joneses* (plural), *the Joneses' house* (possessive plural).

## 3.9.10 Commas with *such as* and *like*

### 3.9.10.1 Restrictive vs. Nonrestrictive
Whether to use a comma before *such as* (or *like*) depends on whether the examples that follow are essential to the meaning of the sentence.

**Nonrestrictive — use commas.** The examples illustrate a general statement; removing them leaves the sentence still true.

> Citrus fruits, **such as** oranges and grapefruits, are high in vitamin C.
> *(Without the examples: "Citrus fruits are high in vitamin C." Still true.)*

> Some sea creatures, **such as** hermit crabs, shed their shells.

**Restrictive — no commas.** The examples narrow the statement and are essential to its meaning; removing them changes or distorts the truth.

> Trees **such as** oaks and elms don't grow at this altitude.
> *(Without the examples: "Trees don't grow at this altitude." Now incorrectly absolute — the original sentence was specific to those species.)*

> Foods **such as** pizza and ice cream aren't very good for you.

The same logic applies to *like* used to introduce examples.

### 3.9.10.2 *such as* vs. *like*
The two phrases are not interchangeable in formal writing.

- ***such as*** — introduces specific examples that **belong to** the category being described.
- ***like*** — introduces things that are **similar to** the category but not necessarily included in it.

> I want to live in a big city, **like** Boston or Chicago.
> *(meaning: a city resembling Boston or Chicago — not necessarily one of those two.)*

> I want to live in a big city, **such as** Boston or Chicago.
> *(meaning: a city, possibly Boston or Chicago themselves.)*

In formal SAP writing — including translations and devotional prose — prefer ***such as*** when listing actual examples drawn from the category. Use *like* only when comparison rather than inclusion is intended.

### 3.9.10.3 No Colon after *such as*
Don't follow *such as* with a colon — the phrase itself signals that examples are coming:

- ❌ Several rituals are common, **such as: puja, arti, and havan.**
- ✅ Several rituals are common, **such as puja, arti, and havan.**

A colon is appropriate after a complete clause that doesn't already include *such as*: *Several rituals are common: puja, arti, and havan.*

### 3.9.10.4 How Many Examples
*such as* is best used to introduce **one to three** examples (occasionally four if all are single words). For longer lists, recast as a vertical list (see [3.9.8](#398-vertical-lists)) or as an "X include the following: …" sentence.

## 3.9.11 Open Questions
- Period inside or outside quotation marks (American vs British)?
- Spaced or unspaced em dashes in print? This guide uses spaced (` — `); print publications may differ.
