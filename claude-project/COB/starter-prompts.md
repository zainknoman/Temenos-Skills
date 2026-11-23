# COB project: starter prompts

Paste any of these into a chat inside the Claude Project. Replace the angle-bracket parts.

## Running COB

```
Walk me through starting COB in phantom mode on <release> from a clean state.
Include the pre-checks, the exact records to change, and how I confirm it is running.
```

```
COB is running. How do I stop it cleanly after the current transactions and restart it later?
```

```
We are on TS2024. Explain what happens to the Online stage, ONLINE.SERVICE, and which jobs are reset at the end of COB.
```

## Troubleshooting

```
COB will not start. Here is what I see: <paste AGENT.STATUS / COMO lines / TSA.SERVICE COB record>.
Rank the likely causes and tell me what to check first.
```

```
Agent <n> keeps getting marked DEAD during job <PROCESS-JOB>. TIME.OUT is <x>, DEATH.WATCH is <y>.
COMO tail: <paste>. What is happening and how do I fix it?
```

```
The COB service stopped itself during <job>. What could have stopped it and how do I resume without losing data?
```

```
Explain the difference between non-fatal, fatal and critical COB errors.
For each, what lands in EB.EOD.ERROR and what do I do before the next COB?
```

```
A report did not print after COB. It is defined in BATCH <id> DATA as <entry>. Where is it and why?
```

## Configuration

```
Show me the BATCH, PGM.FILE and TSA.SERVICE records I need for a new multi-threaded service <name>
that processes <application> records. Flag anything that TS2024 forbids.
```

```
Should we enable business-stage COB? Explain what changes, the benefit, and the risks. Is it reversible?
```

```
Configure TSA.SERVICES.COB so service <BNK/X> starts at the System stage with <n> agents and stops at End.
```

```
Set up elastic agents so COB uses <n> agents normally and <m> during AA.SERVICE.PROCESS.
```

## Performance

```
Here is our JT.ANALYSE output: <paste CSV rows>. Which jobs should we tune first and which COB features fit each one?
```

```
Compare bulking, BYPASS.SEL, SELECT.AHEAD, JMS queue processing and the Redis cache for a job selecting 2 million IDs.
Give preconditions and limits for each.
```

## Internals and development

```
Explain step by step what BATCH.JOB.CONTROL, F.BATCH.STATUS, F.LOCKING and F.JOB.LIST do while three agents run one multi-threaded job,
and what happens if all three crash right after the SELECT.
```

```
Write a multi-threaded COB job <JOB.NAME> that <business rule>. Give the .LOAD, .SELECT and record routines
and the PGM.FILE and BATCH records. Mark any field you could not verify.
```

```
Write an EXIT.API routine for job <JOB> that writes a completion row to <file>, and show how to register it.
```
