---
name: temenos-component-analyzer
description: >
  Analyze a T24/Transact application or component and produce a developer-facing
  dependency report covering PGM.FILE, FILE.CONTROL, STANDARD.SELECTION, VERSION,
  ENQUIRY, routines, componentized jBC artefacts, EB.API and Service/Batch/Workload
  configuration. Includes an executable mainline wrapper and R19 multithreading model.
---

# Temenos Component Analyzer

This skill defines a metadata-first T24/Transact component analyzer.

## Scope

For an application such as CUSTOMER, analyze:

1. Application metadata
   - PGM.FILE
   - FILE.CONTROL
   - STANDARD.SELECTION
   - application insert/source hints
2. Versions
   - all VERSION records for the application
   - routine-bearing fields
3. Enquiries
   - enquiries whose FILE.NAME points to the application
   - BUILD.ROUTINE
   - field names
   - operation
   - conversion routines
4. Routines
   - source where available from BP
   - $PACKAGE
   - $USING
   - $INSERT
   - CALL/OPF/F.READ/F.WRITE/F.DELETE/F.MATREAD
   - EB.READLIST
   - DAS
   - EB.API
   - GOSUB/CALL dependencies
5. Componentized jBC
   - component declaration
   - methods
   - properties
   - constants
   - tables
   - scope
   - jBC mappings
6. Services
   - PGM.FILE TYPE B
   - BATCH
   - TSA.SERVICE
   - TSA.WORKLOAD.PROFILE
   - job environment/frequency
   - workload agents
7. Dependency report
   - direct evidence
   - unresolved references
   - source-unavailable warnings
   - service candidates

## R19 multithreading model

A multi-threaded job is represented as:

    <JOB>.LOAD
    <JOB>.SELECT
    <JOB>.FILTER       (optional)
    <JOB>              (record routine)

Execution is controlled by BATCH.JOB.CONTROL.

The SELECT routine is responsible for creating the list through BATCH.BUILD.LIST.
The record routine receives one ID and must not contain its own loop over all IDs.

Configuration is:

    PGM.FILE TYPE = B
        -> BATCH.JOB.CONTROL
        -> BATCH record
        -> TSA.SERVICE
        -> TSA.WORKLOAD.PROFILE

## Running the analyzer

Preferred mainline:

    EB.COMPONENT.ANALYZER.MAIN CUSTOMER

The first argument is read from SENTENCE(1), so no screen INPUT is required.

The mainline calls:

    EB.COMPONENT.ANALYZER

and prints the returned developer report.

## Important limitation

Routine source is not a normal T24 application record. The analyzer therefore attempts to retrieve BP source with LIST-ITEM BP <ROUTINE>. If the local environment does not expose source through that command, the report marks source analysis as unavailable rather than inventing dependencies.

R19 field positions used by the analyzer are centralized in the implementation and should be checked against the target release's I_F inserts before production deployment.
