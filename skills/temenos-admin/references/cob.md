# COB (Close of Business) Reference

Source: two Temenos training courses, read in this order:

1. **COB Foundation** (TRIPRCOB) — 88 slides: stages, BATCH, TSA.SERVICE, running and monitoring COB, errors.
2. **COB Implementation** (TR3PRCOBIA / TR3PRCOBIB) — 188 slides: tSM/tSA internals, LIST files, multi-threaded jobs,
   service configuration, externalised reports, predefined IDs, priority records, scheduler, elastic scaling,
   exit APIs, JMS queue processing, Redis externalised cache.

Both are Word files of slide screenshots, OCR'd into `docs/COB/COB Foundation.pdf` and
`docs/COB/COB Implementation.pdf` (page N = slide N). Search them with:

```
py -3 pipeline/query_docs.py "<question>" --topic COB -n 5
```

The screenshots come from an R24 Model Bank (dates in May 2024). Field names below were checked against
the R23 and R25 knowledge DBs (`fields` table). **Verified** = present in both releases unless a release is
named. **Not in Layer A** = the app has no `I_F.*` insert in the JARs, so the name comes only from the
training screenshots. Say so when you use it.

---

## 1. What COB is

- COB marks the end of the day's financial transactions and rolls the bank date to the next working day.
- It runs on every working day. It processes the day's scheduled events: accruals, interest
  capitalisation, loan schedules, internal accounting, reports.
- Example: accrual (daily interest not yet due) must run before capitalisation (interest falls due).
  That is why jobs run in a strict order.

## 2. Stages

| Stage | Letter | What runs there | Example |
|---|---|---|---|
| Application | A | Individual application processes | Forex, Funds Transfer |
| System Wide | S | Jobs common to core banking | Interest accrual, capitalisation |
| Reporting | R | Report generation and printing | Trial balance, transaction journal |
| Start of Day | D | Start-of-day operations and the date change | Standing orders |
| Online | O | Non-critical work after the system is back online | Temp work-file clean-up |

- **Batch stage** = stage letter + 3-digit sequence `000`–`999`, e.g. `A000`, `A100`, `S000`, `R099`. First is `A000`, last `O999`.
- Stage and sequence are never violated. Several BATCH records can share one batch stage.
- With several BATCH records on the same stage, EB.SORT.BATCH **randomises the batches** but never the
  order of jobs inside a batch. Useful for running several single-threaded jobs in parallel.

### Three execution models

| Model | Who uses it | How |
|---|---|---|
| Traditional / legacy | Pre-R20, L3 customisations | Batches under the five main stages A-S-R-D-O |
| Business-stage COB | L1/L2 COB | Hard-coded sub-stages, each with a default sequence (COB.STAGE.SEQ) |
| Transact Standards 2024 (TS2024) | New clients | COB service runs A-S-R-D only, then auto-triggers ONLINE.SERVICE for O |

### TS2024 rules

- COB runs only the A, S, R and D stages. This shortens COB.
- At the end of COB, A/S/R/D jobs are reset and **ONLINE.SERVICE** starts automatically. It runs the O-stage
  batches in batch-stage order, then resets them. It is Global Processing (GP) compliant and runs in sync with COB.
- Job Times (JT) and Report Times (RT) separate COB and ONLINE jobs.
- New clients, including upgrading clients, **cannot add new batches or new jobs to a batch in any COB stage**.
  No new batch or job can be added to the Online stage. Upgrading clients may keep running the O stage inside COB.
- ONLINE.SERVICE needs no manual SERVICE.CONTROL change, unlike COB.
- Local enablement shown in the course (R24 Model Bank): SPF `SYSTEM` products include `TS2021` (the course
  says TS2021, not TS2022/23/24); TSA.PARAMETER `SYSTEM` attribute `FORCE.TEMN.STANDARDS` = `YES`
  (fields TS.PARM.ATTRIBUTE.NAME / TS.PARM.ATTRIBUTE.VALUE); the same attribute on the OFS.SOURCE used by the
  browser (usually `GCS`; confirm in the TAFJEE EAR's `ejb-jar.xml`). The course also replaced `EB_API.jar`
  and `EB_Service.jar` in `T24lib` with course-supplied JARs. That is training-environment specific. Do not
  advise it for a real bank without Temenos guidance.

### Business-stage COB

- Sub-stage of a main stage that groups BATCH records which may run **in parallel** at that point.
  Example: `ACCRUAL` under SYSTEM groups accrual batches.
- Keep a gap of 20 between business-stage sequences so new stages can be inserted.
- Enable: TSA.PARAMETER `SYSTEM`, field BUSINESS.STAGE.COB = `YES` (verified: TS.PARM.BUSINESS.STAGE.COB).
  **Once enabled it cannot be disabled.**
- At the start of each COB the system migrates BATCH records: if COB.STAGE.SEQ ≠ BATCH.STAGE, it copies
  COB.STAGE.SEQ into BATCH.STAGE, writes the old image to history and the new one to live. COB then runs on
  BATCH.STAGE as usual. Many batches share few sequences, so more run in parallel: better load balancing,
  better agent use, shorter COB.

| MAIN.STAGE | Example COB.STAGE | Meaning |
|---|---|---|
| APPLICATION | A-UNAUTH, A-CONTRACT, A-TIDYUP, A-start | Unauthorised contract processing, … |
| SYSTEM | S-ICPROCESS, ACCRUAL | Interest and charges processing |
| REPORTING | R-PREREPORT | Business processing before reports |
| STARTOFDAY | D-TIDYUP | Clean up work files and logs for the next day |
| ONLINE | O-ONLINE | Online processing |

COB.STAGE.SEQ is no-input and defaults from MAIN.STAGE + COB.STAGE, format `<stage letter>NNN`
(e.g. APPLICATION + A-CONTRACT → `A400`; APPLICATION + A-TIDYUP → `A050`). A COB.STAGE that does not belong
to the chosen MAIN.STAGE is an error.

## 3. Configuration tables

### BATCH — one record per process (verified, prefix `BAT.`)

- ID = `<bank mnemonic>/<process>`, e.g. `BNK/COB.INITIALISE`. Processes are company-specific, so a process
  needed in every company needs a record per company mnemonic.
- A BATCH record **without** a batch stage runs as a service, not in COB.
- Jobs inside a process run in the order defined and **never simultaneously**.

| Field | Meaning |
|---|---|
| BATCH.STAGE | Stage letter + sequence |
| MAIN.STAGE / COB.STAGE / COB.STAGE.SEQ | Business-stage fields (above) |
| PROCESS.STATUS | 0 Ready, 1 Running, 2 Completed, 3 Error |
| BATCH.ENVIRONMENT | e.g. `F` Foreground |
| DEFAULT.PRINTER | Used when a job has no PRINTER.NAME; else DE.FORM.TYPE's SYSTEM printer |
| JOB.NAME (MV) | Routine to run; needs PGM.FILE with TYPE `B` |
| VERIFICATION | A job **in the same record** that must have completed today first |
| FREQUENCY | see below |
| NEXT.RUN.DATE | Set on authorisation / successful run; empty for `D`; user input for `A` |
| PRINTER.NAME | Printer for the job's output |
| DATA | Job parameters, often ENQUIRY.REPORT or REPGEN IDs, e.g. `ENQ EU.FX.PL.TODAY` (an ENQUIRY.REPORT ID, not an enquiry) |
| JOB.STATUS | 0 Ready, 1 Running, 2 Completed, 3 Error |
| LAST.RUN.DATE | No input, set on successful run |
| JOB.MESSAGE | Error text; cleared when the job is fixed and JOB.STATUS becomes 2 |
| SELECT.AHEAD | Batch stage at which to run this job's SELECT early (see §8) |
| CLEAR.STATIC.CACHE | `YES` = clear CACHE.READ cache after every job instead of at stage change |
| ASSOCIATED.JOBS | R25 only (BAT.ASSOCIATED.JOBS) |

FREQUENCY values: `D` every working day; `D nn` every nnth working day; `W` weekly (Friday); `M` last working
day of the month; `M nn` first day of month + nn offset; `Y` last working day of the year; `Y nn` last
working day of the nn'th month; `A` ad hoc (enter NEXT.RUN.DATE manually).

### PGM.FILE — one record per job routine (verified, prefix `EB.PGM.`)

| Field | Meaning |
|---|---|
| TYPE | `B` for batch jobs |
| BATCH.JOB | Null or `@BATCH.JOB.CONTROL` = multi-threaded (`.LOAD`/`.SELECT`/record). `@<routine>` = single-threaded |
| ADDITIONAL.INFO | `.CRITICAL` critical job; `.NUC` no cache; `.NTX` no transaction boundary |
| ACTIVATION.FILE / ACTIVATION.FILENAME | Service reads IDs from an activation (list) file |
| REC.VERIFY | No input; BATCH.JOB.CONTROL sets `Y` when the record routine filters IDs (returns -1/-2) |
| BYPASS.SEL | `Y` (only if REC.VERIFY=Y) = skip the .SELECT criteria, plain select of the whole file |
| BULK.NO | Contracts per LIST record, 1–200; overrides BATCH.BUILD.LIST's bulk parameter |
| PRIORITY.FILE / PRIORITY.TABLE.NAME | Priority processing (§10) |
| EXIT.API | Routine run once after all contracts of the job finish (§12) |
| COMMIT.SIZE | Commit size for queue processing (§13) |
| TIDY.UP.API, SAMPLE.COUNT, JOB.RATING | Exist in R23/R25; not covered by the courses |

### TSA.SERVICE — services, including COB and TSM (verified, prefix `TS.TSM.`)

| Field | Meaning |
|---|---|
| WORK.PROFILE | TSA.WORKLOAD.PROFILE ID (number of agents) |
| SERVICE.CONTROL | START / STOP / AUTO |
| USER | Usually SEAT.USER / INPUTTER |
| REVIEW.TIME | TSM record: how long the tSM sleeps between reviews |
| TIME.OUT | Seconds an agent may go silent before the tSM kills and replaces it |
| ATTRIBUTE.TYPE / ATTRIBUTE.VALUE | e.g. RUN.AT.DEPLOY=YES; RUNNING.UNDER.SCHEDULER (set by the scheduler) |
| FREQUENCY | Business-day frequency for a service, e.g. `10/09/2024 14:00 28` |
| DATE, STARTED, STOPPED, ELAPSED, TRANSACTIONS | Run statistics |
| STOPPAGE.TIME / STOP.COUNT | Per-service crash limits; default from TSA.PARAMETER. STOPPAGE.TIME must exceed TIME.OUT/DEATH.WATCH |
| PRE.COB.CHECK | **R25 only.** Service must finish successfully during the business day before COB can start |

Pre-configured records: `TSM`, `COB` (also company variants like `COB-1`), `ONLINE.SERVICE` (TS2024),
`BNK/EB.EXTERNALISE.REPORT`, `BNK/EB.PREDEFINE.PROCESSING`.

### TSA.PARAMETER — single record `SYSTEM` (verified, prefix `TS.PARM.`)

| Field | Meaning |
|---|---|
| REVIEW.TIME | Default when TSA.SERVICE REVIEW.TIME is blank (course: 60) |
| DEATH.WATCH | Default when TIME.OUT is blank (course: 300 default; screenshots show 999) |
| HIGHEST.AGENT | No input; agents running across all servers |
| STOPPAGE.TIME / STOP.COUNT | Crash window and crashes allowed before the tSM stops a service |
| BUSINESS.STAGE.COB | `YES` enables business-stage COB, irreversible |
| PACKAGE.DEPLOYMENT | `ACTIVE` = tSM starts only services with RUN.AT.DEPLOY=YES |
| QUEUE.JOBS | JMS queue processing: `ALL`, a BATCH ID, or `BATCH-JOB` |
| LIST.JOBS | **R25 only.** Jobs that use the Redis external cache, e.g. `BNK/AA.EOD.PROCESS-AA.SERVICE.PROCESS` |
| COMMIT.SIZE | Commit size for queue flushing |
| ATTRIBUTE.NAME / ATTRIBUTE.VALUE | e.g. FORCE.TEMN.STANDARDS=YES |

### TSA.WORKLOAD.PROFILE — agents per service (**not in Layer A**)

- AGENTS.REQUIRED, optionally by time of day (application-server time). Example: fewer COB agents at 23:00
  while an interface is busy.
- The TSM's own profile must never have more than one agent.
- Elastic fields (§11): ELASTIC.DATETIME, ELASTIC.QUEUE.DEPTH, ELASTIC.JOB.NAME, ELASTIC.TOTAL
  (ELASTIC.MAX/ELASTIC.MIN not used).
- Thumb rule: number of tSAs = processors × 4 per server.

### Other tables

| Table | Use | Layer A |
|---|---|---|
| DATES | Bank dates per company; `<co>-COB` record during COB | Not in Layer A |
| EB.EOD.ERROR | One record per company per day, ID `<company>.<yyyymmdd>`, multi-valued errors, FIX.REQUIRED, DATE.RESOLVED | Not in Layer A |
| EB.EOD.ERROR.DETAIL | One record per error: process, job, routine | Not in Layer A |
| TSA.STATUS | One record per agent (live) | Verified `TS.TSS.` |
| TSA.RUNNING.SERVICE | Live agent counts, queue depth, current job | Verified `TSA.RS.` |
| TSA.SERVICES.COB | Scheduler: services per COB stage | Verified `TSS.COB.` |
| EB.PREDEFINE.CONTRACTS | IDs to process per job | Verified `PRE.CON.` |
| TSA.ERROR.LIST | Contracts that killed an agent | Verified `TS.EL.` |
| JOB.TIMES / JOB.TIMES.HISTORY / REPORT.TIMES | Job and report statistics | Not in Layer A |
| T24.SESSION | Live session per T24.SESSION.NO | Verified `T24.SESS.` |
| F.BATCH.STATUS, F.LOCKING, F.JOB.LIST.n | Framework work files | Work files, no schema |

## 4. Runtime: tSM and tSAs

- **tSM** (Temenos Service Manager) controls COB. It reads TSA.SERVICE records with SERVICE.CONTROL=START,
  reads their workload profiles, starts missing agents, replaces dead ones, then sleeps REVIEW.TIME.
- **tSA** (Temenos Service Agent) runs the BATCH jobs. The first agent started becomes the tSM.
  Every agent first asks "am I the tSM?" (TSA.STATUS NEXT.SERVICE).
- Only **one tSM per server**; any number of tSAs. Multi-server COB needs the **Multi Server (MS)** module;
  each server runs its own tSM that watches only its own tSAs.
- Heartbeat: each tSA updates LAST.CONTACT, JOB.PROGRESS and LAST.MESSAGE in F.TSA.STATUS about every 60 s.
  If an agent misses TIME.OUT, the tSM kills it at OS level and starts a substitute.
- tSM liveness: its last contact is kept in F.LOCKING key `TSM:<server>`. In phantom mode a tSA relaunches the
  tSM if it has not reported for more than 120 s.
- App-server start flow: `START.TSM` posted to the JMS EXEC queue → Phantom MDB runs `tRun START.TSM` →
  BATCH.JOB.CONTROL reads the profile and posts `tSA 1..n` back to the queue → MDB starts each as a thread.
  COB is multi-threaded inside the application server.

## 5. Running COB

Before every run: **clear EB.EOD.ERROR** (fix and set DATE.RESOLVED on errors needing a fix). COB will not
start with unresolved errors: the critical job COB.CHECK.EB.EOD.ERROR fails.

Then set SERVICE.CONTROL = `START` on TSA.SERVICE `TSM` and `COB`, commit and authorise both.

| Mode | How |
|---|---|
| Servlet | `http://{host}:{port}/TAFJEE/xhtml/execute/dashboard.xhtml`, command `START.TSM`, Execute Command |
| Phantom (background) | TAFJ shell: `tRun START.TSM`. tSM starts the agents itself |
| Interactive / debug | Shell 1: `tRun START.TSM -DEBUG`. Then in other shells `tRun tSA <n>` for each agent it asks for. With TS2024, also start the ONLINE.SERVICE agents |

To stop: set COB SERVICE.CONTROL = `STOP`. Agents show NEXT.SERVICE=STOP and stop after their current
transaction.

### What happens, end to end

1. System mode changes Online → Batch (DATES, CO.BATCH.STATUS).
2. Each tSA calls S.JOB.RUN, which calls **EB.SORT.BATCH once**: picks BATCH records with PROCESS.STATUS ≠ 2,
   sorts by BATCH.STAGE and FREQUENCY into A-S-R-D-O order.
3. For each job, S.JOB.RUN calls **BATCH.JOB.CONTROL** (the heart of COB, once per job). Each job is passed as
   `PROCESS.NAME JOB.NAME RTN JOB.DATA COMPANY.ID NEXT.RUN.DATE ACTIVATION.FILE BATCH.STAGE JIDX BATCH.PROCESS.STATUS`.
4. Stage `A001` job **EB.CYCLE.DATES** creates `DATES <company>-COB` from the pre-COB dates and advances the
   company's own DATES record (TODAY, LAST.WORKING.DAY, NEXT.WORKING.DAY). COB jobs use `<company>-COB`.
5. Stage `D000` job **B.DATE.CHANGE** changes the dates on `<company>-COB`. The system returns to Online at
   the end of D.
6. At the start of the Online stage, **BATCH.DATE.RESET** sets NEXT.RUN.DATE for today's jobs (not `D` or `A`)
   and resets PROCESS.STATUS/JOB.STATUS to 0.
7. TS2024: COB service stops and ONLINE.SERVICE runs the O stage.

**NS (Non Stop) module:** with NS installed users can input during COB. New online transactions use the
`DATES <company>` record, so they get the next working day. COB-created records use `<company>-COB`.
The `-COB` record is kept and updated on the next COB.

## 6. Job internals

### Single- vs multi-threaded

| | Single-threaded | Multi-threaded |
|---|---|---|
| PGM.FILE BATCH.JOB | `@<routine>` | null or `@BATCH.JOB.CONTROL` |
| Routines | One routine with all logic | `<JOB>.LOAD`, `<JOB>.SELECT`, `<JOB>` (record routine) |
| Agents | One | LOAD and record routine on all tSAs, SELECT on one |
| PGM.FILE entries | One | Only `<JOB>` needs one; `.LOAD`/`.SELECT` are found by name |

Multi-threading is simulated by the framework, not OS threads.

Single-threaded jobs still go through a LIST file: BATCH.JOB.CONTROL writes one record (ID `1`, data
`SingleThreaded`), the agent that locks it runs the routine inside one transaction block.

### LIST file and locking

- FLAG.ID = `<process>-<job>-<multivalue position>`, e.g. `BNK/AA.EOD-JOB8-2`.
- The agent that locks `F.BATCH.STATUS <FLAG.ID>` allocates a LIST file: first free `F.JOB.LIST.<n>` found
  via F.LOCKING (created if missing). It writes two F.LOCKING records: `<list file> → FLAG.ID` and
  `FLAG.ID → <list file>`.
- It runs `.SELECT`, which calls **BATCH.BUILD.LIST** to write IDs. `.SELECT` runs once per value of the
  common `CONTROL.LIST` (FM-separated).
- It writes `F.BATCH.STATUS` = `<CONTROL.LIST> VM PROCESSING VM MAX.LIST.ID VM KEYS.PROCESSED` and releases
  the lock. Waiting agents see `PROCESSING` and start the record routine.
- Each agent takes LIST records, locks one, and per contract runs the record routine and deletes the contract
  from the LIST record **in the same transaction**. If the agent dies, its transaction rolls back and other
  agents pick the contract up.
- When the list is empty, one agent drops the processed CONTROL.LIST line or writes `PROCESSED`, then deletes
  both F.LOCKING records.
- Restart after a crash: agents find the F.LOCKING record and reuse the same LIST file. Completed jobs
  (JOB.STATUS 2) are skipped.

### TSA.STATUS JOB.PROGRESS codes seen in the course

| Code | Meaning |
|---|---|
| 1 | Processing contracts |
| 2 | Selecting contracts (running .SELECT) |
| 3 | Managing F.BATCH.STATUS / processing list records |
| 4 | Selecting from the LIST file |
| 5 | Managing the batch record (calling BATCH.JOB.CONTROL, .LOAD) |
| 7 | Executing a single-threaded routine |

### Bulking

- Default, when no bulk number is given: first 100 IDs 1 per LIST record; IDs 101–1,000 10 per record;
  1,001–10,000 100 per record; beyond that 200 per record. Example: 130 IDs → 103 LIST records.
- Fixed bulking: PGM.FILE BULK.NO (1–200) or the 6th position of BATCH.BUILD.LIST's first parameter;
  PGM.FILE wins. Contracts in one LIST record are VM-separated and processed in one transaction, with one
  delete. Fewer I/Os. Use only when the select returns many IDs.

### Record-routine filtering

Record routine returns `-1` (process) or `-2` (skip) in its ID argument → BATCH.JOB.CONTROL sets
PGM.FILE REC.VERIFY=`Y`. Then BYPASS.SEL=`Y` lets the framework do a plain `SELECT FBNK.CUSTOMER` instead of
`SELECT ... WITH SECTOR GT 1200`, which is faster, and the record routine filters.

### Caching during COB

- CACHE.READ static cache is cleared at stage change (A→S…), not after every job, unless BATCH
  CLEAR.STATIC.CACHE=`YES`.
- Common variables in `I_COMMON`: CACHE.OFF (0/null use cache, 1 off) and WRITE.CACHE (0/null write to disk,
  1 write to cache, flushed at TRANSEND). By default reads and writes are cached during COB.
- Turn caching off for one job: PGM.FILE ADDITIONAL.INFO = `.NUC`.

## 7. Errors and crashes

| Type | Raised by | What happens |
|---|---|---|
| jBASE / OS level | Runtime (file open/read, permissions, memory) | Agent crashes to debugger or shell. No EB.EOD.ERROR entry. PROCESS/JOB.STATUS stay 1. Fix, then restart |
| Non-fatal | `FATAL.ERROR` told not to fatal out | Logged to EB.EOD.ERROR + DETAIL, FIX.REQUIRED=YES, contract stays, COB continues |
| Fatal | `FATAL.ERROR` told to fatal out | Logged, contract **removed from the LIST file**, agent crashes. On restart COB resumes minus that contract. Report to Temenos support |
| Critical | Job with PGM.FILE ADDITIONAL.INFO `.CRITICAL` | Service stops, contract never removed, **no EB.EOD.ERROR entry**. Fix, then set COB SERVICE.CONTROL=START again |

- Critical jobs include EB.CYCLE.DATES, B.DATE.CHANGE and COB.CHECK.EB.EOD.ERROR.
- Fatal error in LOAD or SELECT: the tSM stops the service rather than retrying forever.
- Repeated crashes: first DEAD agent writes F.LOCKING `<service>-STOP` with time and count. More than
  STOP.COUNT crashes within STOPPAGE.TIME stops the service. Example: STOPPAGE.TIME=100, STOP.COUNT=3 →
  the fourth crash in 100 s stops it. Works for AUTO services too.
- Corrupt contract: agent silent longer than DEATH.WATCH (loop or slow) → tSM logs it off and records the key
  in TSA.ERROR.LIST. Later agents skip keys found there and remove them from the list. The removal is logged
  in EB.EOD.ERROR with FIX.REQUIRED=YES. TSA.ERROR.LIST is cleared when the job completes.
- Better fatal-error data: SPF REPORT.CORE.DUMP=`Y` (verified) calls JBASECOREDUMP. Call stack, variables and
  transaction reference go to a central log.
- Crash diagnosis: interactive mode shows the error on screen. Phantom mode: AGENT.STATUS shows the agent
  stopped. Read its COMO. The BATCH record shows JOB.STATUS error and JOB.MESSAGE. A missing `.LOAD` routine
  shows as a hang in phantom mode. Recompiling fixed it in the course example.
- Resolving: open the EB.EOD.ERROR record, set DATE.RESOLVED to the fix date, commit and authorise, before the
  next COB.
- Locks: `DBTools ... -s JQL LOCKS` lists table, record and session for current locks.

## 8. Service configuration features

| Feature | Where | Notes |
|---|---|---|
| Select ahead | BATCH SELECT.AHEAD = an earlier batch stage | Idle agents run only list allocation and SELECT early. Not for business-dependent jobs |
| Business-day frequency | TSA.SERVICE FREQUENCY | e.g. `10/09/2024 14:00 28` |
| Package deployment | TSA.PARAMETER PACKAGE.DEPLOYMENT=ACTIVE + TSA.SERVICE attribute RUN.AT.DEPLOY=YES | tSM starts only those services (e.g. BNK/T24.RELEASE.AUTHORISE). tSM mode only. Clear the field afterwards |
| Pre-COB check | TSA.SERVICE PRE.COB.CHECK (R25) | Stand-alone services must complete during the business day. Otherwise COB raises a fatal error. Not for COB, date-change or in-COB services |

## 9. Externalised reports

- Reports marked `IMMEDIATE` print during the job: either DATA `DAT DAILY IMMEDIATE`, or append `IMMEDIATE`
  to the report entry, e.g. `RTN SC.TRADES.TODAY IMMEDIATE`.
- Other reports go to the INT activation file `F.EB.EXTERNALISED.REPORT`, ID
  `<company>-<type>-<report>-<batch stage>`, e.g. `NL0020001-ENQ-JOURNAL.SUMMARY-D900`. Types: ENQ, RPG, RTN.
- The auto service `BNK/EB.EXTERNALISE.REPORT` is set to AUTO during COB and prints them outside COB.
  Output is in HOLD.CONTROL.
- Setup (pre-configured in Model Bank): BATCH and TSA.SERVICE `BNK/EB.EXTERNALISE.REPORT`, FILE.CONTROL
  `EB.EXTERNALISED.REPORT`, PGM.FILE `EB.EXTERNALISE.REPORT`.
- Check the file: `DBTools -u <user> -p <pwd> -s JQL LIST-ITEM F.EB.EXTERNALISED.REPORT` (or COUNT).

## 10. Predefined IDs and priority records

**Predefined IDs:** run a service for chosen IDs only, no code change.
1. EB.PREDEFINE.CONTRACTS, ID = a job name (PGM.FILE TYPE B). BUSINESS.CASE = the CONTROL.LIST value.
   CONTRACTS (MV) = the IDs.
2. BATCH `BNK/EB.PREDEFINE.PROCESSING`, DATA = the service to run.
3. Start TSA.SERVICE `BNK/EB.PREDEFINE.PROCESSING`. EB.EOD.ERROR records the CONTROL.LIST of a fatal error
   to help fill BUSINESS.CASE.

**Priority records** (online services with activation files):
- PGM.FILE ACTIVATION.FILE=YES, then PRIORITY.FILE=YES, then PRIORITY.TABLE.NAME
  (default `<SERVICE>.PRI.LIST`). Create the list files with `JQL CREATE-FILE` plus FILE.CONTROL records.
- Send IDs via the **SERVICE.CONTROL** API:

```
SERVICE = ''
SERVICE<1> = "LOAN.REQUEST.SERVICE"   ;* TSA.SERVICE ID
SERVICE<2> = "LOAN.REQUEST.SERVICE"   ;* PGM.FILE ID
SERVICE<3> = ID.NEW                   ;* activation-file record ID
SERVICE<4> = "1"                      ;* priority flag, "" for normal
CALL SERVICE.CONTROL(SERVICE, '', ID.NEW)   ;* operation: START/STOP/AUTO, or '' to send a message
```

  Priority IDs are processed before normal ones.

## 11. Scheduler, dynamic profiles, elastic scaling

- **TSA.SERVICES.COB** (ID = BATCH name): start or stop stand-alone services at COB stages without adding them
  to COB batches. Fields COB.STAGE (Start, System, Reporting, Start Of Day, Online, End), OPERATION.MODE
  (Start, Auto, Stop), SERVER.NAME, WORK.PROFILE. The service gets attribute RUNNING.UNDER.SCHEDULER.
- **Elastic scaling:** in TSA.WORKLOAD.PROFILE, ELASTIC.DATETIME (blank = ALL), ELASTIC.QUEUE.DEPTH (increasing
  order), ELASTIC.JOB.NAME and ELASTIC.TOTAL. The tSM resizes agents by time, queue depth or current job.
  Multi-server compatible. Course example: COB profile with 1 agent and AA.SERVICE.PROCESS etc. raised to
  2–6 agents. TSA.RUNNING.SERVICE shows total agents, queue depth and current job, rebuilt each review.
- Works for online services too (e.g. BNK/OFS.MESSAGE.SERVICE, profile OFS.WEALTH).

## 12. Exit API

- PGM.FILE EXIT.API: a routine run once after all contracts of the job finish (alerts, local-table updates)
  instead of adding a post-job.
- Multi-threaded batch jobs only. The routine needs an EB.API record. jBC only, no L3 Java API.
- Can read `BATCH.INFO` (`I_BATCH.FILES`) and `AGENT.NUMBER` (`I_TSA.COMMON`).

## 13. JMS queue processing and Redis cache

**Queue processing** (TAFJ only):
- JMS queues replace the JOB.LIST. Agents start processing as soon as the first IDs arrive, without waiting for
  SELECT. No work table, so the DB does not grow.
- IDs flush every 10 records or per commit size (TSA.PARAMETER/PGM.FILE COMMIT.SIZE).
- Dynamic bulking is skipped when writes exceed 500, lock collisions exceed 3, the last commit exceeds the
  review time, for activation/online services, or for jobs with a fixed bulk number.
- Setup: a JMS broker (course used ActiveMQ 5.15.10), queues in the app-server config, then `tafj.properties`
  and TAFJEE properties:

```
temn.tafj.runtime.use.jmsqueues.for.services = true
temn.tafj.runtime.services.queue.pull.timeout = 100
temn.tafj.appserver.execute.servlet.allowed.commands = START.TSM
temn.tafj.appserver.trun.allowed.commands = \btSS\b
```

  Then TSA.PARAMETER QUEUE.JOBS = `ALL`, a BATCH ID (`BNK/SYSTEM.END.OF.DAY3`) or `BATCH-JOB`
  (`BNK/SYSTEM.END.OF.DAY3-IC.COB`).

**Redis externalised cache** (R25 field LIST.JOBS):
- For heavy jobs, e.g. AA.SERVICE.PROCESS with more than 1M AA.NEXT.ACTIVITY records. Not for critical,
  bulked, activation or stand-alone jobs.

```
temn.tafj.runtime.use.external.caching=true
temn.tafj.cache.host=127.0.0.1
temn.tafj.cache.port=6379
temn.tafj.enable.static.cache=true   # or empty: only main/processing lists in Redis
```

- TSA.PARAMETER LIST.JOBS = `BNK/AA.EOD.PROCESS-AA.SERVICE.PROCESS`.
- IDs go to a main list and move to a processing list. On a lock or crash they return to the main list.
  A non-critical fatal error removes them from both and logs EB.EOD.ERROR. Bulking for Redis moves defaults
  to 5000.
- Start Redis (and Docker if used) before the service. Never stop or restart Redis during a run.

## 14. Monitoring and logs

| Tool | What it shows |
|---|---|
| COB Monitor (TAFJEE servlet) | Progress meter, running batch, agent details and COMO |
| ENQ AGENT.STATUS (from TSA.STATUS) | Agent, T24.SESSION.NO, server, status RUNNING/STOPPED/DEAD, PID, current/next service, I/O counters, last message, COMO name |
| `TSA.STATUS L` | Same data from the command line |
| Classic `COB.MONITOR` (`tRun EX`) | Stage progress and % complete |
| ENQ COB.PROGRESS | Progress bar per company |
| ENQ JOB.PROGRESS (from JOB.TIMES) | Jobs by start time, newest first |
| `tRun JT.ANALYSE` | CSV `JT.<date>` in the run directory: stage, batch, job, times, records, throughput, agents |
| `tRun RT.ANALYSE` | CSV `RT.<date>`: per report batch, company, type ENQ/RPG/RTN, timings |
| Grafana (TemnMonitor) | COB panel fed live from Transact; see observability-and-security.md |

- JOB.TIMES: ID `<process>-<job>`, last 10 runs. Fields include START.TIME, END.TIME, THROUGHPUT
  (keys/elapsed×60), COMPLETED, TXN.MANAGEMENT (N when `.NTX`), BULK.NUMBER, READ.WRITE.CACHE,
  LOCK.COLLISION. JOB.TIMES.HISTORY keeps prior images.
- COMO: one log per agent, `tSA_<agent>_<date>_<time>`, under the COMO directory (location set in the
  properties). Not cleared automatically. Keep at least six weeks.

## 15. Quick troubleshooting

| Symptom | Check |
|---|---|
| COB will not start | Unresolved EB.EOD.ERROR (COB.CHECK.EB.EOD.ERROR is critical); pre-COB check services (R25); TSM and COB both START and authorised |
| Agent keeps dying | COMO; TIME.OUT/DEATH.WATCH too low for a slow job; TSA.ERROR.LIST |
| Service stopped itself | STOP.COUNT crashes within STOPPAGE.TIME; fatal error in LOAD/SELECT; critical job failure |
| Job hangs in phantom mode | COMO for missing/uncompiled `.LOAD`/`.SELECT`; locks (`JQL LOCKS`) |
| COB slow | JT.ANALYSE; bulking; BYPASS.SEL; SELECT.AHEAD; business-stage COB; elastic agents; queue processing; Redis |
| Report missing | Not IMMEDIATE → check F.EB.EXTERNALISED.REPORT and that BNK/EB.EXTERNALISE.REPORT ran |
| Dates wrong after COB | DATES `<co>` vs `<co>-COB`; EB.CYCLE.DATES (A001) and B.DATE.CHANGE (D000) |
