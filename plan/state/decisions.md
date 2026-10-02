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
