# 7.2 Alt Text Guidelines
Alt text — the *alternative text* read aloud by screen readers in place of an image — is part of the editorial content of an accessible EPUB. Write it with the same care you bring to a caption.

## 7.2.1 The Three Questions
For every image, ask:

1. **What is this image of?** — the subject, in plain words.
2. **Why is it here?** — what does it contribute to the page?
3. **What would a reader miss without it?** — the answer is what your alt text needs to convey.

If the answer to question 3 is 'nothing — it's purely decorative', the image should be marked decorative (empty alt) rather than given a description. Examples: ornamental dividers, repeated logos, background textures.

## 7.2.2 What Good Alt Text Looks Like
| Image | Weak | Strong |
|---|---|---|
| A photo of Pramukh Swami Maharaj garlanding a murti | 'Image' | 'Pramukh Swami Maharaj garlands the murti of Bhagwan Swaminarayan during the Patotsav celebration at Sarangpur Mandir.' |
| A diagram of the Akshardham complex layout | 'Akshardham' | 'Aerial view of Akshardham, New Delhi, showing the central monument flanked by gardens, the lotus-shaped lake to the north, and the surrounding boundary structures.' |
| A devotee performing arti | 'A man doing arti' | 'A devotee performs evening arti before the murti of Bhagwan Swaminarayan, holding a five-wick lamp and small bell.' |

## 7.2.3 Length and Detail
- **One to two sentences** is the right length for most editorial images.
- **More detail** is appropriate when the image carries information not in the surrounding text — a diagram, a chart, or a photograph the article specifically discusses.
- **Less detail** when the caption already conveys the key information; alt text shouldn't repeat the caption verbatim.

## 7.2.4 Conventions for Our Publications
- **Identify people by name** when they're identifiable and named in the surrounding text. 'A sadhu' is weaker than 'Aksharvatsaldas Swami' if the article names him.
- **Identify locations** when meaningful: 'Sarangpur Mandir' rather than 'a temple'.
- **Don't editorialise.** Alt text describes what is shown, not what we feel about it. Avoid words like *beautiful*, *magnificent*, *blessed*.
- **Don't begin with 'Image of' or 'Photo of'**. Screen readers already announce that an image is present. Start with the subject.
- **Use the [macron-only convention](../diacritics/macron-convention.md)** for transliterated terms in alt text, the same as in body text.

## 7.2.5 Decorative vs Informative
Mark an image **decorative** (empty alt attribute, often shown as 'Decorative' in InDesign's Object Export Options) when:

- It is repeated across pages with no varying meaning (logos, page ornaments).
- It is purely visual filler with no informational role.
- The information it carries is fully duplicated in nearby text.

Mark an image **informative** (with descriptive alt text) when:

- It illustrates a specific event, person, or place referenced in the text.
- It is a diagram, chart, or map.
- It would be referred to in conversation about the page.

## 7.2.6 In InDesign
Alt text is set per-image via **Object Export Options → Alt Text** (right-click the image → Object Export Options, or use <kbd>Cmd/Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>). For batch application during production, use the `AddAltText.jsx` script — see [Scripts & Tools](../scripts/index.md).

The script's caption pre-population feature (added in v17) reads the InDesign caption associated with each image and pre-fills the alt-text field, leaving the editor to refine rather than draft from scratch. This is faster and more consistent than free-form drafting.

## 7.2.7 Validation
Before exporting an EPUB:

1. Run **Window → Articles** and verify every content image is in the Articles panel.
2. Confirm decorative images are tagged as such (Object Export Options → Alt Text → Custom → leave blank, or select 'From Structure' with appropriate tagging).
3. After EPUB export, run **DAISY Ace** for an accessibility report. Address any 'image without alternative text' warnings before delivery.

## 7.2.8 Related
- [Reading Order](reading-order.md) — how images fit into the document's narrative sequence
- [Scripts & Tools](../scripts/index.md) — `AddAltText.jsx` reference
