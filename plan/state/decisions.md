# Decisions

## Licensing / publishing (2026-10-02)

- **Temenos-Skills** is a private repo for personal use. It may hold Temenos-derived knowledge (schemas, descriptions, PDF index).
- **T24Tools** is public (repo + GitHub Pages). It contains only self-authored code and generic sample data. Nothing exported from Temenos-Skills is committed to it; users load their own `fields.json` locally (file picker, IndexedDB, never uploaded).
- Public or shared material uses generic `SAMPLE.*` / `TEST.*` names instead of bank/client identifiers. Real T24 identifiers are never renamed (`OFS.GLOBUS.MANAGER`, `GLOBUS.BP`, `SOURCE.TYPE` `GLOBUS`, schema fields such as `IDPMS.BOE.HBL.NUMBER`).

## tCompile invocation (verified 2026-10-02, R25, JDK 21)

Write-free compile against the read-only `C:\R25` install:

1. Copy `C:\R25\TAFJ\conf\tafj.properties` **out** of R25 into the scratch dir and override these keys to scratch paths:
   - `temn.tafj.directory.basic`
   - `temn.tafj.directory.java`
   - `temn.tafj.directory.classes`
   - `temn.tafj.runtime.directory.current`
   - `temn.tafj.runtime.directory.como`
   - `temn.tafj.directory.updates`
2. Set these **environment variables** to a scratch log dir (read by `TAFJ\bin\tafj_conf.bat` and passed as `-D` to the JVM). Without them, every compile appends to `C:\R25\TAFJ\log\compiler.log`:
   - `temenos.log.directory`
   - `temenos.log.directory.t24`
   - `temenos.log.directory.como`
3. Run: `cmd /c C:\R25\TAFJ\bin\tCompile.bat -cf <absolute path to scratch .properties> <absolute path to .b>`. `-cf` accepts an absolute path.

Result: `SPIKE.HELLO.b` compiled to `classes/com/temenos/t24/SPIKE_HELLO_cl.class`, and a scan of `C:\R25` (78,926 files, skipping `TAFJ/3rdParty` and `TAFJ/appserver`) found **0** files newer than the marker. That scan takes ~4 s in Python (`os.walk`); Git Bash `find` over the same tree takes 10+ minutes, so don't use it.

Output format:
- Success: exit 0, `Compiling...  0 error | 1 compiled`, `Compilation completed for 1 file(s).`
- Failure: exit 1, lines like `[ERROR] (line 2) SPIKE.BAD, expecting RPAREN`, `Compilation completed for 1 file(s). 4 errors`, file listed under `Files With Error :`.
- Every output contains the word "error" (`0 error`, `Files With Error :`), so a substring check is wrong. Failure = non-zero exit **or** any `[ERROR]` line **or** no `Compilation completed` line.
- The compiler reports undefined legacy field EQUs as `The variable 'AC.NOT.A.FIELD' is not initialised.`

Incident: the first two trial compiles ran before the log env vars were found and appended to `C:\R25\TAFJ\log\compiler.log`. That was a log append only; no config, source, data or class files under `C:\R25` changed.

## Releases (found 2026-10-02)

- `jar/` (the pipeline source for `temenos_knowledge.db`, `table-schema/`, `component_fields`) is **R23**: `META-INF/MANIFEST.MF` says `R23_AMR.0`, signed 2023-05-22.
- `C:\R25\bnk\t24lib` (used by the compile gate) is **R25**: `R25_AMR.0`, signed 2025-03-26. Component classes differ, e.g. `component_ST_Customer_16_cl` has 1,152 int constants in R23 vs 1,254 in R25.
- Exports must be labelled with the release of the JARs the DB was built from: `--release` is now required (an earlier export was wrongly labelled R25).
- Pending: per-release knowledge (build R25 from `C:\R25\bnk\t24lib`, read-only) so T24Tools can offer a release choice.

## Componentised field names (2026-10-02)

- Source of truth: `public static int _<Record>_<Field>` constants assigned their field position in `<clinit>` of `com/temenos/t24/component_<Mod>_<Name>_<n>_cl.class` (2,006 classes in R23).
- Record names are not unique across components (`AA.Customer`, `DX.Customer` define their own `Customer` tables), so a constant is joined to `fields` on (app, position) **only if** its name spells the EQU name with or without the app prefix (`EbCusMnemonic` ~ `EB.CUS.MNEMONIC`, `Category` ~ `AC.CATEGORY`, `AccountTitleOne` ~ `AC.ACCOUNT.TITLE.1`).
- R23 result: 62,238 of 162,842 fields (38%) in 1,815 apps; 62 fields appear in two components (e.g. ACCOUNT via `AC.AccountOpening` and `AZ.Contract`) — the export uses the component with the most fields.

## R25 knowledge DB (built 2026-10-02)

Built by `pipeline/build_release.py --release R25` into `releases/R25/temenos_knowledge.db` (git-ignored), reading only from `C:\R25` (write guard clean). The R25 JavaDoc ships as a self-extracting `T24.javadoc.jar` (`java -jar` generates the HTML), so it is copied into `build/releases/R25/javadoc/` and generated there.

| | R23 (`jar/`) | R25 (`C:\R25\bnk\t24lib`) |
|---|---|---|
| Applications | 4,596 | 4,838 |
| Fields | 162,842 | 171,887 |
| Enriched from JavaDoc | 96,159 | 101,461 |
| Component classes | 2,006 | 2,090 |
| Fields with a jBC name | 62,238 | 69,119 |

R23 → R25 (`pipeline/release_diff.py`, report in `build/releases/R23-to-R25.md`): 245 apps added, 3 removed, 557 changed; 2,580 fields added, 651 removed, 177 moved; **1,740 jBC names changed** -- R25 keeps the app prefix in many local/country modules where R23 dropped it (`ARACCT...Reserved7` -> `...AracctSweepReserved7`) and spells numbers as digits (`AchXrefReservedOneTwo` -> `AchXrefReserved12`). jBC written with R23 names for those fields will not compile on R25.

## Templates added without a compiler (2026-10-06)

> Superseded: all of them now compile on R25 and the flags are gone -- see "R25 compile of the 2026-10-06 templates" below.

33 artefact templates (14 Infobasic, 11 jBC, 8 Java) were added while `C:\R25` was not available. Each
has a golden case marked `"compiled": false`: it renders byte for byte, its fields verify on R23 and
R25, and the Java hooks compile against the R23 hook/record JARs in `jar/` with stub classes for the
TAFJ runtime (`com.temenos.api.*`, `T24Context`), which checks every `@Override`, getter and import
against the real classes. `export_templates` exports them as `proven: true, compiled: false`;
T24Tools badges them "not compiled yet". `run_golden.py` reports such a case as `PEND` (not `FAIL`)
when the compile is `SKIPPED`, and as `PASS ... now compiles` once R25 compiles it -- then drop the
flag. The templates are generic (SAMPLE/GOLDEN names). Every API they call is verified against
authoritative sources: the R23 JARs (inserts, `component_*_cl` classes, `javap`), the R25 JavaDoc
in `build/releases/R25/javadoc`, and the Temenos PDFs in `docs/`. Public third-party T24 code
(personal GitHub repos) was used only to find candidate topics. It is **not** a source of truth,
and nothing was copied from it.

- R23 `RecordLifecycle.updateCoreRecord` returns `void` and takes 10 parameters (javap; R25
  JavaDoc agrees). Corrected in `skills/temenos-l3/SKILL.md` on 2026-10-06, which previously showed a
  5-parameter `TValidationResponse` version.
- VCRR has no VERSION hook field; it was not added. `AUTH.ROUTINE` covers that stage.

## Compile install is selectable; R23 compile on E:\Temenos (2026-10-06)

`compile_check.find_install()` picks the T24 install: `--install PATH` (on `run_golden.py`,
`verify_artefact.py`, `release_t24tools.py`) > `$T24_INSTALL` > the first of `C:\R25`, `E:\Temenos`
that exists. `C:\R25` stays first, so an R25 machine behaves exactly as before (same paths, inherits
`JAVA_HOME`). For other installs: `bnk` may live under `T24\bnk` (TAFJ-installer layout); the release
is read from a `t24lib` JAR manifest and printed (`Compile install: E:\Temenos (R23)`); tCompile gets
the install's bundled `3rdParty\JDK` (R23 `.bat` files break on `JAVA_HOME=C:\Program Files\...`;
`$T24_JAVA_HOME` overrides); and a moved install's stale `tafj.home`/`t24.home` are repointed in the
**scratch** properties copy only. The write guard covers whichever install is used and skips
unreadable entries (a broken JBoss module link in `E:\Temenos`).

First R23 run (`python pipeline/run_golden.py`, auto-selected `E:\Temenos`, R23 SP6): 56/58 PASS,
no write-guard hits. All 25 previously proven cases compile on R23; 31 of the 33 `"compiled": false`
cases compile on R23. Two fail on real compiler errors:
- `infobasic-local-table`: `No component defined. $PACKAGE is mandatory` -- needs `$PACKAGE` + a
  `.component` like the other legacy cases.
- `jbc-complex-get`: `table definitions must be in their own files` -- the DTO must move out of the
  `.component` into its own `.complex` file.

The `"compiled": false` flags were **not** changed: T24Tools and the help page define "compiled" as
"compiles on R25". Run `run_golden.py` on the R25 machine before dropping them. (Done the same day:
both failures fixed, 59/59 PASS on R25 -- next section.)

## R25 compile of the 2026-10-06 templates (2026-10-06)

`python pipeline/run_golden.py --release R25` on the R25 machine (`Compile install: C:\R25 (R25)`):
56/58 PASS on the first run, the same two failures as on R23. Both fixed against authoritative R25
sources (`C:\R25\bnk\T24_BP\TEMPLATE.b` / `TEMPLATE.FIELDS.b` and the TAFJ sample project
`C:\R25\TAFJ\samples\basic\CBI`, which is identical to the CBI handover copy used as a second
reference):
- `infobasic-local-table`: kept the TAFJ Infobasic style (`I_Table`, `CALL Table.*`), added
  `$PACKAGE` + a `.component` with a `private method` per routine (as R25's own `TEMPLATE.b` has
  `$PACKAGE EB.Template`), and `Table.triggerField` -> `Table.trigger` (the name `TEMPLATE.b` uses).
- New type `jbc/local-table`: the componentised style (`$USING EB.Template`,
  `EB.Template.setTable*`, `EB.Template.TableDefineid/TableAddfielddefinition/TableAddfield/
  TableSetauditposition()`). Both styles are valid; the developer chooses.
- `jbc-complex-get`: the DTO is defined only in the `.complex` file; the `public table` block in
  the `.component` was removed (`table definitions must be in their own files`).

The `.FIELDS.b` routines (not the case's main file, so not compiled by `run_golden.py`) were compiled
separately with `verify_artefact.py --release R25`: OK. Second run: **59/59 PASS on R25**. All 33
`"compiled": false` flags removed (`make_goldens.py`: the cases moved into `CASES`;
`CASES_NOT_COMPILED` is empty), so every exported type is proven on R25.

## Java access to multi-value fields (2026-10-07)

`record_parse.py` now stores `field_kinds.group_getter`: how Java reaches a multi-value field's
first value, read from the record class's methods (an accessor name is never derived from a class
name: `AltIdTypeClass` comes from `getAltAcctType`). `''` = a list of TField (`get<F>(int)` returns
TField and `set<F>(CharSequence, int)` exists); `<G>` = the record's `get<G>(int)` returns the field's
group class and `set<G>(<Group>Class, int)` exists (this includes a group's first field, whose record
list holds the group class, not TField); NULL = not reachable in one indexed step (nested groups,
sub-values, `List<String>` audit fields). javap of the R25 classes: `get<F>(int)` is `List.get(i)`
(throws on an empty list), `set<F>(v, i)` / `set<G>(g, i)` go through `prepareArrayForSet` (grow the
list) -- hence guarded reads, indexed writes, and a group written back on the record.

Rebuilt for R23 (`jar/`) and R25 from `E:\DesignStudioR25\R25-tafj-t24lib\t24lib` (R25_AMR.0,
2,153 JARs; no TAFJ runtime there). R25: 7,523 MV and 21,257 MV-GROUP fields reachable; 6,392 /
6,689 not. `export_t24tools.py` appends `[groupGetter, groupClass]` to multi-value field tuples
(schema version unchanged: readers of the first seven values are unaffected).
`artefact_templates.java_multi_value()` (ported in T24Tools `render.js`, same tests on both sides)
rewrites the three ways a Java template uses a field. Golden cases `java-record-lifecycle-default-mv`,
`-validate-mv-group`, `-post-update-mv-group`: PASS with javac on the R23 install (`E:\Temenos`) and
against the R25 record classes with TAFJ stand-ins; still `"compiled": false` until an R25 install run.

## Command line `t24skills` (2026-10-08)

`pipeline/t24skills.py`, launched by `t24skills.cmd` (Windows) / `t24skills` (sh). Guide: `CLI.md`.
- **One CLI over the existing functions, not new logic.** `validate_fields.py`, `query_docs.py` and
  `run_golden.py` were split into a function + an unchanged `main()` (text output and exit codes are
  the same; `validate_fields.py` output was compared byte for byte with the previous version).
- **`--json` is the contract for other programs**: one object on stdout,
  `{"schemaVersion": 1, "command", "ok", ...}`. `schemaVersion` changes only when a key is renamed or
  removed. Exit 0 = ok, 1 = the check ran and failed (stdout still has the full result), 2 = cannot run
  (no DB / vectordb, unknown app, topic, template or file). `run --json` sends the stage's own output
  to stderr.
- **Default release R23**, the same as the pipeline scripts. Commands run from the repository root;
  file paths (`verify FILE`, `--out`, `--inputs`) resolve against the folder the user started in.
- **`rules` topics** are read from Chroma's own `vectordb/chroma.sqlite3`, read-only (~1 s; the Chroma
  API takes ~30 s for 32,657 chunks), with the API as the fallback. The topic check only runs when an
  exact `--topic` returns nothing, so a normal search costs nothing extra.
- **`generate`** uses `artefact_templates.resolve/render` (the code T24Tools' `render.js` mirrors), then
  field-checks every generated `.b` against each application input, as T24Tools does. One field per
  field input: the several-fields forms exist only in T24Tools' `multiField.js`. With each sample's
  inputs and date it reproduces all 59 golden cases byte for byte (checked 2026-10-08). Files are
  written with the platform's line ends, the same as `make_goldens.py`.
- **`sample --out`** copies the golden files byte for byte (CRLF kept) and never overwrites without `--force`.
- **`verify --no-app`** exposes `verify(no_app_ok=True)`, which `run_golden.py` already used for the
  local-table cases, so a new local table can be compiled from the CLI.
- **The help page's CLI pages are generated**, so they cannot drift: the stages from `STAGES`, the topic
  table from the vectordb, and the Samples page from the golden cases + templates. Every command on the
  Samples page was executed on 2026-10-08 (59 samples x 5 commands, all exit 0).
- **Consumers:** T24Tools reads only exported files; `templates.json` re-exported byte-identical (the new
  catalogue `group` / `groups` keys are not exported). Temenos-Engineering-Platform still imports
  pipeline modules through inline Python; its `compareReleases` and `searchRules` calls were already
  broken (ImportError, `float.strip`). Switching it to `t24skills --json` is CLAUDE.md P10.
