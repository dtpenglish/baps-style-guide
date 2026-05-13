# 3.10 Punctuation

*Last reviewed by the SAP DTP team: 2026-05-13.*

General typographic conventions for SAP English publications. Footnotes, abbreviations, lists, and apostrophes have their own chapters — see the See Also section below.

## 3.10.1 Quotation Marks
SAP uses **typographers' (curly) quotes** throughout – single and double – and reserves the two marks for distinct purposes.

- **Single quotes – primary mark.** Use `‘ ’` for highlighting a word or phrase: a term in a special or technical sense, a motto presented as a phrase, the gloss of an Indic term, the title of a short work, a quoted excerpt of authoritative text.
- **Double quotes – speech only.** Use `“ ”` for direct speech and dialogue: someone quoted as saying or shouting something.
- **Nested.** Inside double-quoted speech, use single quotes; inside single-quoted highlights, use double – invert the marks at each level.
- Always use **typographers' (curly) quotes**: `‘ ’` and `“ ”`. Straight quotes (`'` `"`) are typewriter relics; reserve them for code samples and form-field examples.

When typing in source files, plain straight `'` and `"` are auto-converted to the curly forms when the site renders, so authors don't need to enter the Unicode characters by hand. Where you genuinely need to show a *literal* straight quote – e.g. when documenting a code sample – wrap it in backticks so the auto-conversion skips it. The marks shown in code-style above (`‘ ’`, `“ ”`) use the same trick – backticks tell the renderer to leave them exactly as typed.

For quotation marks specifically around translations of Indic terms, see [3.9 Quotation Marks](quotation-marks.md).

## 3.10.2 Dashes
SAP uses two dash characters: the **hyphen** and the **en dash**. The em dash is **not used** in SAP English publications – its role (parenthetical breaks) is filled by a **spaced en dash**.

| Mark | When | Spacing | Examples |
|---|---|---|---|
| Hyphen (`-`) | Simple compounds | None | *non-violence*, *forty-three*, *well-known*, *selfless-love* |
| En dash (`–`) | Number and date ranges | None (unspaced) | *pp. 12–18*, *2000–2025* |
| En dash (`–`) | Place pairs | None (unspaced) | *Mumbai–Ahmedabad* |
| En dash (`–`) | Complex compounds | None (unspaced) | *Hindu–Christian dialogue*, *Vedanta–Yoga synthesis* |
| En dash (`–`) | **Parenthetical breaks** | **One space each side** | *Bhagwan Swaminarayan – then known as Sahajanand Swami – addressed the assembly.* |

In InDesign, use the proper Unicode character for the en dash (<kbd>U+2013</kbd>), not a double-hyphen `--` or a triple-hyphen `---`. The em dash character (<kbd>U+2014</kbd>) is not used in SAP body prose.

For compound modifiers with numbers (*twenty-nine members*, *a 5-pound bag*, *an 18th-century novel*) and the rules on hyphenation between numerals and units, see [3.8.5 Compound Modifiers and Unit Spacing](numbers.md#385-compound-modifiers-and-unit-spacing).

### 3.10.2.1 Interrupted Dialogue
Use a **spaced en dash** to mark speech sharply cut off — by another speaker, an action, or a sudden break:

- ‘I was just wondering – ’ / ‘Don't ask,’ he snapped.
- ‘I can't believe it’ – he paced the room – ‘not after all this.’

For speech that **trails off** or falters rather than being cut off, use an **ellipsis**, not a dash:

- ‘I thought perhaps … but never mind.’

This matches the BrE convention and the spaced-en-dash rule of [3.10.2](#3102-dashes); CMS uses an unspaced em dash here, which SAP does not.

### 3.10.2.2 Ranges with *from* and *between*
Don't combine *from* or *between* with a range dash — use the word pair or the dash, not both:

- ✅ *from 1990 to 2000* / ✅ *1990–2000* / ❌ *from 1990–2000*
- ✅ *between 1914 and 1918* / ✅ *1914–1918* / ❌ *between 1914–1918*

## 3.10.3 Series and the Oxford Comma
Use the Oxford (serial) comma in lists of three or more:

> The Vachanamrut, the Shikshapatri, and the Swamini Vato are foundational texts.

Not:

> The Vachanamrut, the Shikshapatri and the Swamini Vato are foundational texts.

## 3.10.4 Ellipses
A genuine ellipsis is a single character (<kbd>U+2026</kbd>: …), not three full stops with spaces. When indicating omitted text within a quotation, use a single ellipsis with a space on each side: *the discourse … turned to the nature of bhakti.*

## 3.10.5 Spacing
- **One space** after a period, comma, colon, semicolon – never two.
- **No space** before a footnote superscript: *…the discourse.¹*
- **One space on each side** of an en dash used for a parenthetical break: *…the discourse – and the silence that followed.* (En dashes used for ranges or complex compounds remain unspaced – see [3.10.2](#3102-dashes).)

## 3.10.6 Commas with *such as* and *like*

### 3.10.6.1 Restrictive vs. Nonrestrictive
Whether to use a comma before *such as* (or *like*) depends on whether the examples that follow are essential to the meaning of the sentence.

**Nonrestrictive – use commas.** The examples illustrate a general statement; removing them leaves the sentence still true.

> Citrus fruits, **such as** oranges and grapefruits, are high in vitamin C.
> *(Without the examples: 'Citrus fruits are high in vitamin C.' Still true.)*

> Some sea creatures, **such as** hermit crabs, shed their shells.

**Restrictive – no commas.** The examples narrow the statement and are essential to its meaning; removing them changes or distorts the truth.

> Trees **such as** oaks and elms don't grow at this altitude.
> *(Without the examples: 'Trees don't grow at this altitude.' Now incorrectly absolute – the original sentence was specific to those species.)*

> Foods **such as** pizza and ice cream aren't very good for you.

The same logic applies to *like* used to introduce examples.

### 3.10.6.2 *such as* vs. *like*
The two phrases are not interchangeable in formal writing.

- ***such as*** – introduces specific examples that **belong to** the category being described.
- ***like*** – introduces things that are **similar to** the category but not necessarily included in it.

> I want to live in a big city, **like** Boston or Chicago.
> *(meaning: a city resembling Boston or Chicago – not necessarily one of those two.)*

> I want to live in a big city, **such as** Boston or Chicago.
> *(meaning: a city, possibly Boston or Chicago themselves.)*

In formal SAP writing – including translations and devotional prose – prefer ***such as*** when listing actual examples drawn from the category. Use *like* only when comparison rather than inclusion is intended.

### 3.10.6.3 No Colon after *such as*
Don't follow *such as* with a colon – the phrase itself signals that examples are coming:

- ❌ Several rituals are common, **such as: puja, arti, and havan.**
- ✅ Several rituals are common, **such as puja, arti, and havan.**

A colon is appropriate after a complete clause that doesn't already include *such as*: *Several rituals are common: puja, arti, and havan.*

### 3.10.6.4 How Many Examples
*such as* is best used to introduce **one to three** examples (occasionally four if all are single words). For longer lists, recast as a vertical list (see [3.13 Vertical Lists](lists.md)) or as an "X include the following: …" sentence.

## 3.10.7 Open Questions
- Period inside or outside quotation marks (American vs British)?

## 3.10.8 See Also
- [3.11 Footnotes](footnotes.md) – footnote superscript placement and edge cases.
- [3.12 Abbreviations & Acronyms](abbreviations.md) – periods in *Mr* / *Dr* / *V.S.*; commas with *i.e.* / *e.g.* / *etc.*
- [3.13 Vertical Lists](lists.md) – bullets, numbering, parallel construction.
- [3.14 Apostrophes & Possessives](apostrophes.md) – possessives, plurals of letters, apostrophe of omission.
