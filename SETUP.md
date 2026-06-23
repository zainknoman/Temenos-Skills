# VS Code Claude Code setup — step-by-step

## What you need installed
- VS Code
- Claude Code extension (search "Claude Code" in VS Code extensions)
- Python 3.10+
- `pip install javatools` (for JAR extraction)

---

## Step 1 — copy these files into your project root

From this download, copy into the ROOT of your Temenos project folder:

```
your-temenos-project/
├── CLAUDE.md              ← copy this (main context file)
├── .claude/
│   └── settings.json      ← copy this (tells Claude Code where skills are)
├── pipeline/
│   ├── extract.py         ← copy this
│   └── aggregate.py       ← copy this
└── skills/                ← copy your existing Temenos-Skills-master/skills/ folder here
```

---

## Step 2 — open the project in VS Code

```bash
cd your-temenos-project
code .
```

Open the Claude Code panel (icon in sidebar or Ctrl+Shift+C).

---

## Step 3 — verify Claude Code reads CLAUDE.md

In the Claude Code chat panel, type:

> "What T24 applications are we working with and what is the validation gate rule?"

Claude should answer from CLAUDE.md without you explaining anything. If it doesn't know,
check that CLAUDE.md is in the project root (same folder as where you ran `code .`).

---

## Step 4 — verify skills are loaded

Type:

> "List the available T24 sub-skills"

You should see t24-dev, infobasic, temenos-l3-java, jbc-componentise, temenos-de.

---

## Step 5 — run the extraction pipeline (first time only, ~90 min)

Open a terminal in VS Code (Ctrl+`) and run:

```bash
pip install javatools
python pipeline/extract.py --jars jar --cache cache --workers 8
python pipeline/aggregate.py --cache cache --out skills/t24-dev/references
```

After this, `skills/t24-dev/references/` will be populated with the real class indexes.

---

## Step 6 — start developing

You can now give Claude Code requirements like:

> "Write a VVR for CUSTOMER that validates the NATIONALITY field is not empty
>  on authorisation. Use the correct field name from the CUSTOMER schema."

Claude Code will:
1. Load CLAUDE.md context automatically
2. Activate the infobasic sub-skill
3. Look up the CUSTOMER field schema
4. Verify NATIONALITY exists before writing code
5. Generate a complete, compilable VVR with header, $PACKAGE, error handling

---

## When to come back to claude.ai chat

Use this claude.ai chat (or a new one) when you need to:
- Design new pipeline scripts (html_parse.py, pdf_extract.py)
- Analyse large files or zip archives
- Make architectural decisions
- Debug the pipeline itself

Then save the output to disk and Claude Code in VS Code picks it up automatically.
