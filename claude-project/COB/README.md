# COB Claude Project kit

A ready-made [Claude Project](https://claude.ai/projects) for Temenos Transact COB (Close of Business)
work. It carries the same knowledge as the `temenos-admin` skill's COB reference, for people who use
claude.ai instead of Claude Code.

## Set it up

1. In claude.ai, create a project named **Temenos COB Assistant**.
2. Paste the whole of `project-instructions.md` into the project's **custom instructions**.
3. Upload the three files in `knowledge/` to the project's **knowledge**:
   - `cob-reference.md`: distilled reference, verified against R23 and R25 table schemas
   - `cob-foundation-transcript.md`: COB Foundation course narration, slide by slide
   - `cob-implementation-transcript.md`: COB Implementation course narration, slide by slide
4. Optional: also upload `docs/COB/COB Foundation.pdf` and `docs/COB/COB Implementation.pdf` (8 MB and
   16 MB) so Claude can see the slide screenshots. Each page is one slide with its OCR text below.
5. Start chats from `starter-prompts.md`.

## Where the files come from

| File | Source | In git |
|---|---|---|
| `project-instructions.md`, `starter-prompts.md`, this README | Written for this kit | Yes |
| `knowledge/cob-reference.md` | Copy of `skills/temenos-admin/references/cob.md`, with repo-only terms removed | Yes |
| `knowledge/*-transcript.md` | Narration from `docs/COB/*.ocr/`, made by `pipeline/docx_extract.py` | No (Temenos course text, like `docs/`) |

Rebuild after the skill or the course files change (Windows, uses the built-in OCR engine):

```
py -3 pipeline/docx_extract.py --docx "D:/Learning/COB/COB Foundation.docx" --topic COB --transcript claude-project/COB/knowledge/cob-foundation-transcript.md
py -3 pipeline/docx_extract.py --docx "D:/Learning/COB/COB Implementation.docx" --topic COB --transcript claude-project/COB/knowledge/cob-implementation-transcript.md
py -3 pipeline/pdf_extract.py --pdfs docs --vectordb vectordb --cache cache/pdf_extracts
```

Then copy `skills/temenos-admin/references/cob.md` over `knowledge/cob-reference.md` and remove the
`query_docs.py` block and the repo terms ("Layer A", skill names) from the copy.
