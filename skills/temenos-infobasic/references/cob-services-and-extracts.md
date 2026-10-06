# Multi-threaded COB / Service Jobs

**Sources (authoritative only):** Temenos *T24 Programming Standards* (`docs/.../Programming
Standards_v02.pdf`, pp. 28–30); *T2BTT R06* training (JOURNAL.UPDATE in batch); *JBC
Precompiler Rules* (rules 25–26); R23 inserts `I_BATCH.FILES` (`EB_Service.jar`) and
`I_COMMON` (`EB_SystemTables.jar`). Proven skeleton in this repo:
`tests/golden/infobasic-cob-service/` (template `templates/infobasic/cob-service`).

"It is MANDATORY to write multi threaded batch jobs … Multi-threading of routines is mandatory
to ensure that transaction management is provided by the system." (Programming Standards p. 29)

## The routine set

| Routine | Mandatory | Contract (Programming Standards) |
|---------|-----------|----------------------------------|
| `I_<JOB>.COMMON` | — | "Typically a local common will be created for each main process" |
| `<JOB>.LOAD` | yes | Sets up the common. "Invoked once per agent and should avoid any locks and any writes to database" |
| `<JOB>.SELECT` | yes | Builds the list file with `BATCH.BUILD.LIST`. Called after `.LOAD`, once per job (or per `CONTROL.LIST` stage) |
| `<JOB>(list_record_id)` | yes | Processes **one** piece of work. "Invoked by the system with the transaction management wrapped around it … should avoid Selects/Clearfiles" |
| `<JOB>.POST` | no | "Processing required after the list file and all multi-threading has finished". Must be defined in `BATCH` |

`<JOB>` is the name on `PGM.FILE` and in the `BATCH` record. For a standard multi-thread job,
`PGM.FILE` `BATCH.JOB` = `@BATCH.JOB.CONTROL` (the default when left null). Every new `BATCH`
record also needs a `BATCH.NEW.COMPANY` record.

## Skeleton

`I_B.MY.JOB.COMMON`:

```basic
    COM /B.MY.JOB/ FN.ACCOUNT, F.ACCOUNT, Y.PARAM.REC
```

`B.MY.JOB.LOAD`: opens and parameter reads only, no writes and no locks.

```basic
    SUBROUTINE B.MY.JOB.LOAD
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_B.MY.JOB.COMMON
    FN.ACCOUNT = 'F.ACCOUNT' ; F.ACCOUNT = ''
    CALL OPF(FN.ACCOUNT, F.ACCOUNT)
    RETURN
END
```

`B.MY.JOB.SELECT`:

```basic
    SUBROUTINE B.MY.JOB.SELECT
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_BATCH.FILES
    $INSERT I_B.MY.JOB.COMMON
    SEL.CMD = 'SELECT ':FN.ACCOUNT:' WITH CATEGORY EQ 1001'
    SEL.LIST = '' ; NO.OF.REC = '' ; SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)
    CALL BATCH.BUILD.LIST('', SEL.LIST)
    RETURN
END
```

`B.MY.JOB` (record routine):

```basic
    SUBROUTINE B.MY.JOB(Y.ID)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.ACCOUNT
    $INSERT I_B.MY.JOB.COMMON
    R.ACC = '' ; Y.ERR = ''
    CALL F.READ(FN.ACCOUNT, Y.ID, R.ACC, F.ACCOUNT, Y.ERR)
    IF Y.ERR THEN RETURN
    ...                                   ;* process exactly this one id
    RETURN
END
```

`$USING` equivalents (verified in R23 component classes): `EB.DataAccess.Opf`,
`EB.DataAccess.Readlist`, `EB.Service.BatchBuildList`.

## `BATCH.BUILD.LIST(ListParameters, IdList)`

| Position | Meaning |
|----------|---------|
| `ListParameters<1>` | Must be null |
| `ListParameters<2>` | Extract file name — the work list is a straight copy of the ids in this file |
| `ListParameters<3>` | Extract selection — `SELECT`/`SSELECT` criteria applied to the extract file |
| `ListParameters<4>` | Ids per work-list record (default 1). Higher = fewer list records, but **all ids in one list record are one transaction and hold their locks together** |
| `IdList` | Ids prepared by the `.SELECT` routine |

Pass `''` + `SEL.LIST` for the common case. The pre-built-extract form (`<2>`/`<3>`) avoids
a `SELECT` on a large file.

## Multi-stage jobs — `CONTROL.LIST`

`CONTROL.LIST` (`I_BATCH.FILES`: "Controls if select process must be called more than once").
The `.SELECT` routine fills it on its first call. The system then calls `.SELECT` again for each
stage, and each stage runs multi-threaded:

```basic
    IF CONTROL.LIST EQ '' THEN
        CONTROL.LIST = 'STAGE.ONE':FM:'STAGE.TWO'
    END
    BEGIN CASE
    CASE CONTROL.LIST<1,1> EQ 'STAGE.ONE'
        SEL.CMD = '...'
    CASE CONTROL.LIST<1,1> EQ 'STAGE.TWO'
        SEL.CMD = '...'
    END CASE
```

Reading the current stage from `CONTROL.LIST<1,1>` is how projects commonly do it. The
standards document describes the mechanism but does not show the indexing, so confirm it on the
target release.

## Other commons available to batch code (`I_BATCH.FILES`, R23)

`SESSION.NO` (agent number), `KEYS.PROCESSED`, `BATCH.THREAD.KEY`, `JOB.PROGRESS`, `BATCH.INFO`
(`<1>` process name, `<2>` routine, `<3>` job name), `PROCESS.NAME`, `SELECT.STATEMENT`,
`SELECTION.MODE` (PREDEFINED/ALL/CRITERIA/FILTER), `BULK.NUMBER`, `JOB.USER`,
`C$BATCH.START.DATE`, `RUNNING.UNDER.SCHEDULER`. `RUNNING.UNDER.BATCH` and `BATCH.DETAILS` are in
`I_COMMON`. The layout of `BATCH.DETAILS` is not documented in the sources here — ask before
relying on a position in it.

## Rules (Programming Standards p. 29, T2BTT, Precompiler rules)

| Rule | Source |
|------|--------|
| All new batch processes are multi-threaded | Standards p. 29 |
| Test `RUNNING.UNDER.BATCH` to know you are in COB — not the SPF status | Standards p. 29 |
| Do not call template programs from batch; move the logic into a subroutine both can call | Standards p. 29 |
| Never prompt; use `CRT` for progress (with care at volume). No `HUSH`/`!HUSHIT` | Standards p. 29 |
| Terminate on error with `FATAL.ERROR` and a meaningful `TEXT` (logged to `EB.EOD.ERROR`); never `STOP` | Standards p. 29 |
| No `SELECT`/`CLEAR-FILE` in the record routine | Standards p. 29 |
| No locks or database writes in `.LOAD`; all file opens belong in `.LOAD` | Standards p. 30; Precompiler rule 25 |
| `BATCH.BUILD.LIST` must be called from the `.SELECT` routine | Precompiler rule 26 |
| In batch mode an `F.WRITE` is **not** followed by `JOURNAL.UPDATE` | T2BTT R06 |
| End-of-day reports are attached to `EB.PRINT` (routine, REPGEN or enquiry) | Standards p. 29 |
| Do not `SELECT` files likely to grow large; use concat files | Standards p. 33 |

## Producing an output file from a job

The sources don't prescribe a pattern for this. What follows is derived from the rules above,
so present it as a design choice, not as a Temenos standard. Agents run in parallel, so the
record routine should not write a shared sequential file. Each record writes its own result
(for example to a work file keyed by id), and the single-threaded `.POST` routine assembles the
file with `OPENSEQ`/`WRITESEQ`/`CLOSESEQ`. When the output is a report, the standard route is
`EB.PRINT`.

## DFE (Data Framework Extract) hooks

`DFE.PARAMETER` / `DFE.MAPPING` contain routine hook fields, verified in `table-schema`:
`DFE.PARAM.HEADER.DETAILS`, `DFE.PARAM.RESPONSE.ROUTINE`, `DFE.MAP.ID.ROUTINE`,
`DFE.MAP.USER.DEF.RTN`, `DFE.MAP.FIELD.CONV`, `DFE.MAP.PRE.PROCESS.RTN`,
`DFE.MAP.POST.UPDATE.RTN`, `DFE.MAP.INDIV.RECORD.RTN`, `DFE.MAP.ONLINE.RESP.RTN`.
The calling contract (arguments, return) of each hook is **not documented** in the sources
available here. HALT and ask the developer for it, or find it in the DFE user guide through
Layer B, before generating a DFE routine.
