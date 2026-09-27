# Component Analyzer Implementation Guide

## 1. What the routine does

The analyzer accepts a T24 application name and produces a structured report.

Example:

    EB.COMPONENT.ANALYZER.MAIN CUSTOMER

The report is organized as:

    APPLICATION
    VERSION
    ENQUIRY
    ROUTINES
    JBC COMPONENT
    SERVICES
    DEPENDENCY SUMMARY
    WARNINGS

It is intentionally metadata-first. A relationship is reported as direct only when the
routine can prove it from a T24 record or source text.

## 2. R19 service model

R19 describes a service as the trigger that executes a batch. A batch is a set of jobs,
and a job processes a set of records.

For a multi-threaded routine:

    <JOB>.LOAD
        initialise common state

    <JOB>.SELECT
        select IDs and call BATCH.BUILD.LIST

    <JOB>.FILTER
        optional single-threaded filtering before list creation

    <JOB>
        process one ID received from BATCH.JOB.CONTROL

BATCH.JOB.CONTROL controls the execution. Multiple service agents execute the record
routine against IDs from the list.

The analyzer therefore does not treat a routine name by itself as proof of a service.
It uses PGM.FILE/BATCH/TSA metadata first and uses routine naming only as a candidate hint.

## 3. Metadata positions used

These positions are based on the R19 material supplied for this implementation and the
documented T24 records already validated during design.

### PGM.FILE

    1  TYPE
    4  BATCH.JOB / BATCH.JOB.CONTROL

TYPE B is treated as a batch program.

### BATCH

    4  BATCH.ENVIRONMENT
    6  JOB.NAME
    8  FREQUENCY

R19 configuration describes the BATCH record ID as the PGM.FILE/job ID.

### TSA.SERVICE

    1  DESCRIPTION
    2  SERVER.NAME
    3  WORK.PROFILE
    4  USER
    5  SERVICE.CONTROL
    6  REVIEW.TIME
    7  TIME.OUT

### TSA.WORKLOAD.PROFILE

    2  TIME
    3  AGENTS.REQUIRED

TIME and AGENTS.REQUIRED may be multivalue.

### ENQUIRY

    2  FILE.NAME
    8  BUILD.ROUTINE
    10 FIELD.NAMES
    11 OPERATION
    14 CONVERSION
    19 ENQUIRY.NAME

The important correction is that the standard field is FILE.NAME, not ENQUIRY.FILE.NAME.

### VERSION

The implementation keeps the R19/historical routine positions centralized:

    52 AUT.NEW.CONTENT
    59 VALIDATION.RTN
    63 INPUT.ROUTINE
    64 AUTH.ROUTINE
    74 ID.RTN
    75 CHECK.REC.RTN
    76 AFTER.UNAU.RTN
    77 BEFORE.AUTH.RTN

Before deploying to another release, compare these with the target I_F.VERSION insert
and update the constants in the implementation if the local schema differs.

## 4. Source analysis

The routine tries:

    LIST-ITEM BP <ROUTINE>

using EXECUTE ... CAPTURING.

The parser searches source text for:

    $PACKAGE
    $USING
    $INSERT
    CALL OPF
    CALL F.READ
    CALL F.WRITE
    CALL F.DELETE
    CALL F.MATREAD
    CALL EB.READLIST
    CALL DAS
    CALL EB.API
    GOSUB
    CALL

For file access, the parser reports the literal F.* token when one is present.

For componentized source, the report also looks for:

    component
    method
    property
    constant
    table
    metamodelVersion

and records a component hint. Full .component source should be analyzed from the
component project source when available.

## 5. Why source analysis is best-effort

T24 application records can prove metadata relationships, but source-level relationships
such as:

    VERSION -> routine -> F.ACCOUNT

require routine source.

The analyzer therefore distinguishes:

    DIRECT METADATA
    DIRECT SOURCE
    NAME CANDIDATE
    UNRESOLVED

This prevents a developer report from presenting a naming convention as a proven dependency.

## 6. Expected CUSTOMER report

A successful run should let a developer answer:

- What is CUSTOMER?
- Is it a batch program?
- Which versions use custom routines?
- Which enquiries use CUSTOMER?
- Which enquiry build/conversion routines are involved?
- Which routines read/write CUSTOMER?
- Which other T24 files are accessed?
- Which EB.API records reference those routines?
- Which JBC component artefacts are present?
- Which jobs/services are configured?
- How many service agents are configured?
- What is the execution path from service to batch to routine?
- Which relationships could not be proven?

## 7. Production deployment

Compile/deploy the following as a group:

    EB.COMPONENT.ANALYZER.MAIN
    EB.COMPONENT.ANALYZER

Deploy the .component declaration through the normal component build/deployment process
when componentized APIs are required.

The mainline itself is deliberately a PROGRAM wrapper so a developer can execute it
without having to invoke a component API.

Do not use INPUT/CRT inside business routines. The mainline uses CRT only as a developer
utility/reporting wrapper. For GUI-safe integration, return the report through the
component method or persist it in a dedicated developer/report application.
