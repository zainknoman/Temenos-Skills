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
