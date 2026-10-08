# t24skills — the Temenos-Skills command line

One command for the everyday Temenos-Skills actions and for every pipeline stage. You don't need
to remember the 21 `python pipeline/...` commands. The code is in `pipeline/t24skills.py`.

## Starting it

| Where | Command |
|---|---|
| PowerShell, in the repository folder | `.\t24skills.cmd <command>`. PowerShell never runs a program from the current folder without `.\` |
| cmd.exe, in the repository folder | `t24skills <command>` |
| Anywhere, by full path | `D:\Personal\Projects\Temenos-Skills\t24skills.cmd <command>` |
| Anywhere, by name | `t24skills <command>`, once the repository is on your PATH (see below) |
| Git Bash / sh | `./t24skills <command>` |
| Any shell | `python pipeline/t24skills.py <command>` (use `py` on Windows if `python` is not on the PATH) |

### Put it on your PATH (once)

Add the repository folder to your user PATH, then open a **new** terminal:

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";D:\Personal\Projects\Temenos-Skills", "User")
```

After that, `t24skills status` works from any folder, in PowerShell and in cmd.exe. Windows
adds the `.cmd` itself. To undo it, remove the entry from the user `Path` variable (*System
Properties → Environment Variables*). The examples below assume the PATH is set. Without it, write
`.\t24skills.cmd` in the repository folder.

Commands always run from the repository root. A file path you pass (to `verify`) is resolved
against the folder you started in. `t24skills --help` and `t24skills <command> --help` list
every option.

## Commands

| Command | What it does | Options |
|---|---|---|
| `status` | What is built: each release's knowledge DB, T24Tools exports, the vectordb, templates, the compile install, and whether the help page is stale | `--json` |
| `fields APP` | Every field of an application: position, SV/MV, type, jBC name | `--release`, `--json` |
| `fields APP --check F1,F2` | The Field Verification Gate: are these field names real? | `--release`, `--json` |
| `rules "QUESTION"` | Search the business-rule PDFs (Layer B). Never use it for field names | `--topic`, `-n`, `--json` |
| `topics` | The topics `rules --topic` accepts, with PDF and chunk counts and the largest PDFs | `--json` |
| `samples [FILTER]` | List the artefact samples: one golden case per artefact type, grouped by language and group | `--language`, `--json` |
| `sample NAME` | Show one sample's requirement, inputs and generated files, print one file, or copy them | `--file`, `--out`, `--force`, `--json` |
| `template [ID]` | A template's inputs, its sample values and a generate command that works; no ID lists all 59 | `--json` |
| `generate ID` | Generate an artefact from a template with your own inputs, plus the field check | `--set`, `--inputs`, `--from-sample`, `--release`, `--today`, `--out`, `--force`, `--json` |
| `verify FILE --app APP` | Accuracy gate for one generated file: field check + compile | `--release`, `--no-compile`, `--no-app`, `--install`, `--json` |
| `golden` | Run every golden case (field check + compile) | `--case`, `--release`, `--install`, `--json` |
| `diff [OLD NEW]` | What changed between two releases (default R23 → R25) | `--full`, `--json` |
| `stages` | The pipeline stages, in execution order, with their commands | `--json` |
| `run STAGE` | Run one pipeline stage: `r23`, `docs`, `refs`, `sepa`, `r25`, `golden`, `export`, `help` | `--release`, `--dry-run`, `--json` |

Without `--release`, commands use **R23**, the same default as the pipeline scripts. Pass `--release R25` for the
installed R25 Model Bank.

## Exit codes

| Code | Meaning | Examples |
|---|---|---|
| `0` | OK | fields verified, verify PASS, every golden case PASS |
| `1` | The check ran and failed | a field is NOT FOUND, verify FAIL, a golden case FAILs, a stage step exits non-zero |
| `2` | It cannot run | no knowledge DB or vectordb, unknown application or topic, missing file, unknown release or option |

In PowerShell read it with `$LASTEXITCODE`; in sh with `$?`.

## status

```powershell
t24skills status
```

```text
Temenos-Skills at D:\Personal\Projects\Temenos-Skills (default release R23)
  R23: 4,596 apps, 162,842 fields, 62,238 jBC names (temenos_knowledge.db, 2026-10-02T19:38:08Z)
       T24Tools fields.json: 2026-10-05T10:43:51Z
  R25: 4,838 apps, 171,858 fields, 69,119 jBC names (releases/R25/temenos_knowledge.db, 2026-10-02T19:38:14Z)
       T24Tools fields.json: 2026-10-06T14:40:47Z
  Business-rule docs (vectordb): built 2026-08-09T09:17:59Z
  Templates: 59 types, 59 golden cases, templates.json exported
  Compile install: C:\R25 (R25)
  Help page: 2026-10-08T08:05:23Z
```

When a skill, template or pipeline file is newer than the help page, the last line ends with
`-- STALE, run: t24skills run help`.

## fields

List an application's fields:

```powershell
t24skills fields CUSTOMER --release R25
```

```text
CUSTOMER in R25: 201 fields
     1  EB.CUS.MNEMONIC                          SV       TField       ST.Customer.Customer.EbCusMnemonic
     2  EB.CUS.SHORT.NAME                        MV                    ST.Customer.Customer.EbCusShortName
     3  EB.CUS.NAME.1                            MV                    ST.Customer.Customer.EbCusNameOne
     ...
```

The columns are position, field (EQU) name, SV/MV, type and componentised (jBC) name. A blank
means the value was not captured. It never means "optional".

Check field names before writing code (the Field Verification Gate). Names are case-insensitive and separated by commas:

```powershell
t24skills fields CUSTOMER --check EB.CUS.MNEMONIC,EB.CUS.SECTOR,EB.CUS.NOPE --release R25
```

```text
VERIFIED   EB.CUS.MNEMONIC  (pos 1, SV)  jBC ST.Customer.Customer.EbCusMnemonic
VERIFIED   EB.CUS.SECTOR  (pos 23, SV)  jBC ST.Customer.Customer.EbCusSector
NOT FOUND  EB.CUS.NOPE  -- never guess a field name; ask the developer
```

Exit code `1`, because one field is missing. An unknown application exits `2`:

```text
t24skills: no schema for application 'NOAPP' in R23
```

## rules

```powershell
t24skills rules "account dormancy status inactive" --topic ACCOUNT -n 2
```

```text
--- ACCOUNT/Understanding Account Number Format.pdf (page 5, score 0.374) ---
... 5 Dormancy The ...
```

- **`--topic`** limits the search to one documentation folder, such as `ACCOUNT`, `AA`, `Temenos_Applications` or `TAFJ-Admin`. The full list is in the [table below](#topics-for-rules---topic-generated-from-the-vectordb), or run `t24skills topics`.
  - A topic is **not** a T24 application. There is no `CUSTOMER` topic: the CUSTOMER user guide is under `Temenos_Applications`, and the Microbanking one under `Microbanking`.
  - Names are not case-sensitive (`--topic temenos_applications` works). Quote a name with spaces: `--topic "Basics & Fundamentals"`.
  - An unknown topic exits `2` and suggests close names:

    ```text
    t24skills: unknown topic 'tph'. Did you mean: TPH - Copy, TPH-Clearing, TPH-R21? List them with: t24skills topics
    ```

  - Leave `--topic` out to search every topic.
- **`-n`** sets the number of results (default 5).
- **Wording matters.** The search is TF-IDF, so write the question with T24's own terms. A single word not in the vocabulary scores 0.
- **Field names** always come from `fields`, never from `rules`.

Finding the CUSTOMER documentation:

```powershell
t24skills rules "customer legal id document name" -n 3                              # every topic
t24skills rules "customer legal id document name" --topic Temenos_Applications -n 3 # the T24 user guides
```

```text
--- Temenos_Applications/Temenos T24 User Guides_Part1/Customer.pdf (page 9, score 0.556) ---
```

## topics

```powershell
t24skills topics
t24skills topics --json      # {"count", "chunks", "topics": [{"topic", "files", "chunks", "examples"}]}
```

```text
54 topics for rules --topic. Names are not case-sensitive; quote names with spaces.
  TOPIC                                         PDFS CHUNKS  LARGEST PDF
  AA                                              30   2584  Core Banking AA Lending Product Building Implementation CB3P
  ACCOUNT                                          5    181  Accounts_AC.pdf
  ...
```

It takes under a second: it reads Chroma's own SQLite file read-only. The help page's
table below is generated from the same data when the help is rebuilt.

## samples and sample

Every artefact type has one sample: a golden case under `tests\golden\<name>\`. It holds the
requirement, the inputs it was generated from, and the generated files, which compile on R25.
The help page **Command line → Samples** lists all 59 with the commands to show, generate and
compile each one.

```powershell
t24skills samples                        # all 59, by language and group
t24skills samples --language jbc         # only jBC
t24skills samples table                  # name, type, group or requirement contains "table"
```

```text
jBC (componentised) > Tables
  jbc-local-table                            Local table definition (componentised, EB.Template)

59 samples. Show one: t24skills sample <name>
```

Show one sample. Give the case name or the template id:

```powershell
t24skills sample jbc-local-table
t24skills sample jbc/local-table         # the same sample
```

```text
jbc-local-table: Local table definition (componentised, EB.Template)
  Template:     jbc/local-table  (jBC (componentised) > Tables)
  Skill:        temenos-jbc
  Requirement:  Define a sample parameter table.
  Applications: -
  Compiled:     yes, on R25
  Folder:       tests/golden/jbc-local-table
  Inputs:
    PACKAGE = GOLDEN.Api
    TABLE_NAME = GOLDEN.JBC.PARAMETER
    ...

===== GOLDEN.JBC.PARAMETER.b (main) =====
*-----------------------------------------------------------------------------
* Program    : GOLDEN.JBC.PARAMETER
...
```

Print one file, or copy the files to a folder as a starting point:

```powershell
t24skills sample infobasic-vvr --file V.GOLDEN.VVR.b      # just that file's code
t24skills sample jbc/local-table --out .\mywork          # copies the .b and .component files
t24skills sample jbc/local-table --out .\mywork --force  # overwrite files already there
```

- **`--out`** copies the files byte for byte, CRLF line endings included. Without `--force` it refuses to overwrite: exit `2`, naming the files.
- **Saving a file:** use `--out` rather than redirecting `--file` output with `>`. Windows PowerShell 5.1 writes `>` output as UTF-16.
- **An unknown name** exits `2` with close names: `no sample 'local'. Did you mean: infobasic-local-table, jbc-local-table?`
- **JSON:** `sample --json` returns every file's content under `files`, plus `userInputs`, `expectedFields` and `mainFile`.

## template and generate

Generate verified code from the command line, the same way the T24Tools Artefact Generator does.
`template` shows what a type needs. `generate` fills it in for a release and checks every field.

```powershell
t24skills template                     # all 59 template ids
t24skills template jbc/validation      # one template (a sample name such as jbc-local-table works too)
```

```text
jbc/validation: Validation routine (VVR)  (Version routines)
  Reject the record when a field is empty. Generates the .b routine and its .component declaration.
  Generates: {{PACKAGE}}.component, {{ROUTINE_NAME}}.b

  INPUT              KIND          SAMPLE VALUE
  PACKAGE            package       GOLDEN.Validation
  ROUTINE_NAME       routineName   V.CUS.MNEMONIC.CHECK
  METHOD_NAME        identifier    vCusMnemonicCheck
  DESCRIPTION        text          Reject CUSTOMER input when MNEMONIC is empty
  AUTHOR             text          golden-case
  APP                app           CUSTOMER
  FIELD              field of APP  EB.CUS.MNEMONIC
  ERROR_TEXT         text          MNEMONIC IS MANDATORY

Try it with the sample's inputs (change any --set):
  t24skills generate jbc/validation --set PACKAGE=GOLDEN.Validation --set ROUTINE_NAME=V.CUS.MNEMONIC.CHECK ... --release R25 --out .\work
```

Generate. Give every input with `--set`, or start from the sample with `--from-sample` and change only what differs:

```powershell
t24skills generate jbc/validation --set PACKAGE=MYBANK.Validation --set ROUTINE_NAME=V.CUS.SECTOR.CHECK `
  --set METHOD_NAME=vCusSectorCheck --set DESCRIPTION="Reject an empty sector" --set AUTHOR=zain `
  --set APP=CUSTOMER --set FIELD=EB.CUS.SECTOR --set ERROR_TEXT="SECTOR IS MANDATORY" --release R25 --out .\work

t24skills generate jbc/validation --from-sample --set ROUTINE_NAME=V.CUS.SECTOR.CHECK `
  --set METHOD_NAME=vCusSectorCheck --set FIELD=EB.CUS.SECTOR --set ERROR_TEXT="SECTOR IS MANDATORY" --release R25 --out .\work
```

```text
Generated jbc/validation for R25: GOLDEN.Validation.component, V.CUS.SECTOR.CHECK.b
  VERIFIED in CUSTOMER (V.CUS.SECTOR.CHECK.b): ST.Customer.Customer.EbCusSector
Wrote 2 files to D:\...\work
Compile it: t24skills verify D:\...\work\V.CUS.SECTOR.CHECK.b --app CUSTOMER --release R25
```

Then compile it on R25 with the printed `verify` command. That compile gives `COMPILE: OK` / `PASS`.

**Inputs**

- **A field input is the EQU name**, such as `EB.CUS.SECTOR`. The generator turns it into what the language needs in that release: the EQU name for Infobasic, the componentised name for jBC (`ST.Customer.Customer.EbCusSector`), or the getter for Java.
- **Release matters.** jBC names differ between R23 and R25, so generate for the release you deploy to.
- **Filled in for you:** `TODAY` (or `--today 2026-10-08`), the record class and component names, and any *fixed* input (shown as `(fixed)` in `template`).
- **Many values at once:** `--inputs my-inputs.json`, a JSON object such as `{"APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR"}`. This avoids PowerShell quoting. `--set` values override the file.
- **One field per field input.** The several-fields forms are only in T24Tools.

**Output**

- **Without `--out`** the files are printed. With `--out DIR` they are written there, with the same line endings as the golden cases. Existing files are not overwritten without `--force`.
- **Field check:** every generated Infobasic / jBC routine is field-checked against each application input. For Java, javac is the check: run `verify`.

| Result | Exit |
|---|---|
| Generated, every field verified | `0` |
| A field does not exist in the release, has no jBC name, or is multi-value where a Java template needs a single value (`NOT GENERATED: EB.CUS.SHORT.NAME is a multi-value field (MV) ...`) | `1` |
| A missing or unknown input, an unknown template or application, or files already there | `2` |

With the sample's inputs and date (`--from-sample --today 2026-10-02`), `generate` reproduces each
golden case byte for byte, for all 59 templates.

## verify

```powershell
t24skills verify out\V.CUS.CHECK.b --app CUSTOMER --release R25
t24skills verify out\V.CUS.CHECK.b --app CUSTOMER --app ACCOUNT --release R25   # reads two applications
t24skills verify out\V.CUS.CHECK.b --app CUSTOMER --no-compile                  # field check only
t24skills verify out\CustomerHook.java --release R25                            # Java: javac is the field gate
t24skills verify out\MY.PARAMETER.b --no-app --release R25                      # a new local table: reads no application
```

A golden file, from inside its folder. The relative path is resolved against the folder you are in:

```powershell
cd D:\Personal\Projects\Temenos-Skills\tests\golden\infobasic-vvr
t24skills verify V.GOLDEN.VVR.b --app CUSTOMER --release R25
# without the PATH set:  ..\..\..\t24skills.cmd verify V.GOLDEN.VVR.b --app CUSTOMER --release R25
```

```text
VERIFIED in CUSTOMER: EB.CUS.MNEMONIC
Compile install: C:\R25 (R25)
COMPILE: OK
PASS
```

- **Compile install:** `--install PATH` picks the T24 install to compile against. Without it, the CLI uses `$T24_INSTALL`, then the first of `C:\R25`, `E:\Temenos` that exists.
- **No writes to the install:** the install is only read. Builds go to `build/verify/`.
- **Skipped compile:** a compile that cannot run is reported as `SKIPPED` and counts as `FAIL`.

## golden

```powershell
t24skills golden --release R25                          # all 59 cases
t24skills golden --release R25 --case jbc-local-table   # one case (folder name under tests\golden)
```

```text
PASS  jbc-local-table                          OK
1 PASS, 0 FAIL, 0 PEND on R25
```

The full run compiles 59 cases and takes a while. Run it with plenty of free memory, or one
`--case` at a time.

## diff

```powershell
t24skills diff                  # R23 -> R25
t24skills diff R23 R25 --full --json > build\r23-r25.json
```

```text
R23 -> R25
  apps_added       245
  apps_removed     3
  apps_changed     557
  fields_added     2,580
  fields_removed   651
  fields_moved     177
  jbc_renamed      1,740
```

`--full` adds every changed application: fields added, removed and moved, and jBC names renamed.

## stages and run

```powershell
t24skills stages                              # list them
t24skills run export --release R25 --dry-run  # show the commands, run nothing
t24skills run help                            # rebuild this help page
t24skills run golden --release R25
t24skills run export --release R25            # gated: golden cases first, then the T24Tools export
t24skills run r23                             # rebuild R23 knowledge (extract takes ~90 min the first time)
t24skills run r25                             # R25 DB, read-only from C:\R25, + the R23 -> R25 report
```

`--dry-run` prints the exact commands:

```text
...\python.exe ...\pipeline\release_t24tools.py --release R25
```

A stage stops at the first step that fails: `Stage r23 stopped: step exited 1` (exit code `1`).
On success it prints `Stage help done (16.6 s)`.

## JSON output (for other programs)

Add `--json` to any command. Stdout is then exactly one JSON object:

```json
{
 "schemaVersion": 1,
 "command": "fields",
 "ok": true,
 "release": "R25",
 "app": "CUSTOMER",
 "known": true,
 "verified": [
  {"field": "EB.CUS.MNEMONIC", "position": 1, "javaAlias": "Customer_Mnemonic", "type": "TField",
   "mandatory": "Yes", "description": "Specifies an alternative easy means ...", "kind": "SV",
   "jbc": ["ST.Customer.Customer.EbCusMnemonic"]}
 ],
 "missing": []
}
```

A command that cannot run:

```json
{"schemaVersion": 1, "command": "fields", "ok": false,
 "error": {"type": "CANNOT_RUN", "message": "no schema for application 'NOAPP' in R23"}}
```

Rules for a caller:

- Parse stdout whatever the exit code is. Exit `1` still prints a full result with `"ok": false`, for example the `missing` fields or the failing golden cases.
- Treat exit `2` (an `error` object) as "the environment is not ready".
- With `run --json`, the stage's own output goes to **stderr**, so stdout stays one object: `{"stage", "steps": [{"command", "exitCode", "seconds"}], ...}`.
- `schemaVersion` changes only when a field is renamed or removed. New fields can appear at any time.

PowerShell:

```powershell
$r = t24skills fields CUSTOMER --check EB.CUS.MNEMONIC --release R25 --json | ConvertFrom-Json
if (-not $r.ok) { $r.missing }
```

Node (for example, the Temenos-Engineering-Platform adapter):

```js
import { execFile } from 'node:child_process';
execFile('python', ['pipeline/t24skills.py', 'fields', 'CUSTOMER', '--check', 'EB.CUS.MNEMONIC', '--release', 'R25', '--json'],
  { cwd: process.env.TEMENOS_SKILLS_HOME }, (err, stdout) => {
    if (err && err.code === 2) throw new Error(JSON.parse(stdout).error.message);
    const result = JSON.parse(stdout);   // exit 0 or 1: a result either way
    console.log(result.ok, result.missing);
  });
```

## Testing the CLI

```powershell
py -m pytest tests/pipeline/test_t24skills.py -v   # CLI tests on a temporary DB (no T24 install needed)
py -m pytest tests/pipeline -q                     # the whole suite
```

Then run the examples above against your real DBs and check the exit codes.
