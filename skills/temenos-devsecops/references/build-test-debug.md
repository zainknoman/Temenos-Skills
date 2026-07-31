# Build, Test & Debug Reference

Source: `TAFJ_HOME/bin`, `TAFJ_HOME/samples`, `TAFJ_HOME/Regression`,
`docs/TAFJ-DevSecOps/`, verified 2026-07-31.

## Compiler launchers (`TAFJ_HOME/bin`)

Five compiler-related launchers matter most for build tooling:
`tCompile.bat`, `tComponentBuild.bat`, `tComponentBuildProcess.bat`,
`tComponentReport.bat`, `tJavadocMerge.bat`. Note: these are the exact five
launchers affected by the JDK21 `tools.jar` bug documented in
`temenos-admin`'s `install-and-runtime.md` — check that reference
first if a compile fails with a `tools.jar`-related class-not-found error.

Precompilation rules and remote debugging are documented in:
- `TAFJ-JBC-Precompiler-Rules.pdf` — what the JBC precompiler enforces before
  a routine is allowed to build; consult this before assuming a compile
  error is a simple syntax mistake.
- `TAFJ-JBC-Remote-Debugger.pdf` — remote debugging setup for JBC.

## Unit testing

- `TAFJ-UnitTestFramework.pdf` — the TAFJ unit test framework itself.
- `TAFJ-ApplicationTestFramework.pdf` — application-level test framework
  (broader than unit tests — likely integration/functional scope; verify
  scope against the PDF before assuming which layer a given test belongs in).
- `TF.Test.pdf`, `TAFJ-TF_Core.pdf` — "TF" test-framework core reference.

This project's own CLAUDE.md prescribes a **TDD-first** pattern for complex
routines (generate test stub → get developer confirmation → generate
implementation). When that pattern calls for an Infobasic test stub, ground
it in whichever TAFJ test framework (`TAFJ-UnitTestFramework.pdf` vs.
`TAFJ-ApplicationTestFramework.pdf`) matches the artefact type, rather than
inventing a bespoke EQUATE-only stub if a real framework API exists for it —
query the PDFs to check before choosing.

## Build automation & code quality

- `TAFJ-Maven-Plugin.pdf` — Maven integration for TAFJ builds.
- `JBC-SonarQube-Plugin.pdf` — static analysis integration for jBC code.
- `CodeCoverageReceiver.pdf` — code coverage collection
  (`TAFJ_HOME/CodeCoverageReceiver/` is a real directory in this install).

## Regression / seat tooling

`TAFJ_HOME/Regression/` contains `SeatInject.bat` / `seatInject.sh` +
`bin/`/`lib/`. This is **license-seat injection tooling for the regression
environment, not a general-purpose test suite** — don't treat it as a source
of business-logic test cases.

## Sample code baseline

`TAFJ_HOME/samples/basic/`: `HELLO`, `HELLO.FAILURE`, `HELLO.GR0`,
`LOGGER.b`, `MAIN.PRG.b`, `TEST.SUB.b`, `TEST.SUB1.b`, and a `CBI/`
subfolder — real, minimal, known-good Infobasic. Useful as a first
compile/run smoke test when diagnosing whether a build problem is
environmental (JDK, classpath, compiler launcher) versus specific to a
developer's own routine.
