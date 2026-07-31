# Install & Runtime Reference

Source: `C:\R25` root files and `TAFJ_HOME` (`TAFJ/`), verified 2026-07-31.

## Starting / accessing this environment

From `INSTALL-GUIDE.md` (prepared for this specific install):

1. Open `<R25_ROOT>\jboss-eap-8.1`.
2. Double-click `startjboss.bat`.
3. Leave the JBoss console window open — startup takes a few minutes.
4. Browse to:
   - Transact Explorer: `http://localhost:8090/transact-explorer-wa`
   - Conventional Browser: `http://localhost:8090/BrowserWeb`
5. Login: `INPUTT` / `AUTHOR`, password `123456`.

These are environment-specific defaults captured from one install's own
access guide, not universal T24 defaults — verify against the target
environment's own documentation before reusing them.

## Known bug: JDK 21 + obsolete `tools.jar` reference

**Symptom:** compiling a routine via Design Studio or a TAFJ command window fails with:
```
Error: Could not find or load main class ...\jdk21\lib\tools.jar
```

**Root cause:** JDK 21 removed `lib\tools.jar` (it was a JDK 8-era file). Some
R25 TAFJ compiler launchers still append it to `TAFJ_CLASSPATH`:
- `TAFJ_HOME\bin\tCompile.bat`
- `TAFJ_HOME\bin\tComponentBuild.bat`
- `TAFJ_HOME\bin\tComponentBuildProcess.bat`
- `TAFJ_HOME\bin\tComponentReport.bat`
- `TAFJ_HOME\bin\tJavadocMerge.bat`

**Fix:** remove the obsolete `set TAFJ_CLASSPATH=...%JAVA_HOME%\lib\tools.jar`
line from each of the five launchers. A ready-made, idempotent PowerShell
script exists for this at the root of a real R25 install
(`Fix-R25-JDK21-Compilation.ps1`):
- Requires Administrator PowerShell and JDK 21 configured as `JAVA_HOME`.
- Backs up each file once as `<file>.pre-jdk21.bak` before editing.
- Only removes the exact obsolete `TAFJ_CLASSPATH` line — does not touch
  `tafj_conf.bat` conditional checks or unrelated `*Tools.jar` references.
- Safe to re-run; verifies all five launchers afterward and exits non-zero if
  any obsolete entry remains.
- After running, close and reopen Design Studio / any TAFJ command window
  before recompiling.

If you hit this error on a different R25 install, the same targeted fix
(strip that one `TAFJ_CLASSPATH` line from those five `.bat` files) applies —
don't reach for a broader JDK downgrade unless the environment specifically
requires JDK 8/11 for other reasons.

## Application server support

Confirmed present in this install: **JBoss EAP 8.1**. Per the official PDFs
in `docs/TAFJ-Admin/`, R25 additionally documents:
- `TAFJ-AS-JBossInstall-v7-EAP.pdf` / `TAFJ-AS-JBossInstall-v8-EAP.pdf`
- `TAFJ-AS WebLogicInstall.pdf`
- `TAFJ-AS-Websphere-Liberty-Profile-Install.pdf`
- `TAFJ-AS-Azure Service Bus.pdf`, `TAFJ-AS-Dynamic Channel Configuration.pdf`,
  `TAFJ-AS-Online-Transaction.pdf`, `TAFJ-AS-TAFJ.pdf`

Query `python pipeline/query_docs.py "<question>" --topic TAFJ-Admin` for
install-guide specifics per app server — don't guess at deployment steps.

## Development tooling

- `DesignStudioT24-R25.2/` — the Eclipse-based Design Studio IDE. Fresh
  workspaces show an empty `workspace/.metadata` until a project is imported.
- `TAFJ-Eclipse.pdf`, `TAFJ-Eclipse-debugging-T24-JBC-Invoked-via-IRIS.pdf` —
  Eclipse setup and JBC remote-debugging-via-IRIS specifics.
