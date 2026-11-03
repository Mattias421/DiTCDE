# Sheffield formatting review

Compared with `../Example_thesis_format_0.docx` and https://sheffield.ac.uk/rpi/pgr/examination/formatting (3 November 2026).

## Implemented

- A4 pages, 25.4 mm margins matching the example, 11 pt body text with 1.5 spacing.
- University cover and original logo extracted from the supplied example. Mattias Cross retained as sole author; Anton Ragni removed from the author field.
- Continuous Arabic page count including preliminary pages, bibliography and index; cover counted but number hidden.
- One-page abstract copied verbatim from the existing Short Summary in `summary.tex` (210 whitespace-separated words).
- Contents, lists of tables and figures, notation, and draft declaration using the example wording.
- Wide results table split into three panels with identical data and larger type; equation wrapped and notation indentation corrected.

## Author completion required

- Complete `thesis_metadata.tex`: full thesis title, faculty, school, submission month/year; confirm full author name.
- Review `abstract.tex` for final scope and findings. It currently reuses an existing draft and still uses first-person plural.
- Complete and personally confirm `frontmatter.tex`: all GenAI uses, systems/versions, publishers, URLs, use of outputs, academic integrity statement, and publications. Remove the draft notice only after review. This is a template, not a declaration made on the author's behalf.
- Add acknowledgements, preface or accompanying-material lists only if relevant. The example explicitly makes the listed sections conditional on relevance.
- Existing unresolved citations: `rudin`, `bogachev`; unresolved chapter references: `ch:ll`, `ch:cfmse`. These need repair before submission.
- Existing unfinished chapter text and placeholder figure captions remain; formatting alignment does not make the manuscript submission-ready.

## Validation

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` succeeds. PDF page size is A4; abstract occupies one page; no overfull boxes remain. Cover and revised table checked visually. Existing reference/citation warnings remain as listed above.
