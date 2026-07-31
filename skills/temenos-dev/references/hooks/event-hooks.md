# T24 Hook Reference — All Domains

> Generated 2026-06-20T03:39:43.046735+00:00. Covers all hook types across all JAR prefixes.

---

## Lifecycle Hooks (RecordLifecycle)

Fire during T24 record processing: input → validate → authorise → post-update.

### RecordLifecycle API — standard override points

| Method | Signature | When called |
|--------|-----------|-------------|
| `validateRecord` | `void validateRecord(TypeRecord record)` | Before the record is committed |
| `authoriseRecord` | `void authoriseRecord(TypeRecord record)` | When the record is submitted for authorisation |
| `postUpdateRequest` | `void postUpdateRequest(TypeRecord record)` | After the update is written to the database |
| `defaultFieldValues` | `void defaultFieldValues(TypeRecord record)` | To pre-populate field defaults on new records |
| `checkId` | `void checkId(TypeRecord record)` | To validate the record ID format |

*No concrete RecordLifecycle subclasses detected in analysed JARs (these are typically L3 customization classes, not shipped in product JARs).*

---

## AA Activity Hooks (ActivityLifecycle)

Fire during Arrangement Architecture activity processing.

*No ActivityLifecycle hooks found.*

---

## Service Hooks (ServiceLifecycle)

Fire during background service and batch processing.

*No ServiceLifecycle hooks found.*

---

## Validation Hooks

Classes ending `Validation`. Pattern: `record.setError("FIELD.NAME", "message")` / `record.getRNew().getFieldValue("FIELD.NAME")`

*No validation hooks found.*

---

## Authorization Hooks

Classes ending `Authorization`. Called when a record is submitted for authorisation.

*No authorization hooks found.*

---

## T24 User Exit Points — Event Framework

T24 is designed with extensibility as a core feature. All applications provide **exit points** (also called trigger points) where custom routines can be attached and invoked. The application exits its standard flow, executes the custom routine, then returns to the standard flow.

### Exit Point Categories

| Category | When It Fires | What Can Be Done |
|----------|---------------|-----------------|
| ID-level | Before the record is loaded; after the user enters an ID | Validate, transform, or reject the record ID |
| Record-level (read) | After ID resolved, before display | Default-populate fields; perform record-level checks |
| Field-level | When the user tabs out of a field | Field validation; auto-populate related fields |
| Record-level (commit) | When the user commits the record | Cross-field validation; generate overrides |
| After Unauthorised | After the record is written to `$NAU` | Write to ancillary files; trigger interfaces |
| Before Authorisation | During authorisation, before live file write | Pre-auth checks; still can modify `R.NEW` |
| Authorisation | During authorisation, after live file write | Post-auth file updates; interface triggers |

---

## VERSION Record Hook Fields

The `VERSION` application is the primary mechanism for attaching event hooks to T24 applications. Each hook field on the VERSION record defines a subroutine name (prefixed with `@` where required) that fires at a specific stage.

### Full VERSION Hook Field Reference

| VERSION Field | Hook Name | Stage | Trigger Condition | Notes |
|---------------|-----------|-------|------------------|-------|
| `ID.RTN` | ID Routine | ID entry | User enters a record ID | Manipulate/validate ID; uses `ID.NEW`, `ID.OLD`, `ID.NEW.LAST`. Prefix with `@` |
| `CHECK.REC.RTN` | Check Record Routine | After ID, before display | Record fetched, before screen render | Record-level check; used to validate category, status, etc. Prefix with `@` |
| `VALIDATION.RTN` | Validation Routine | On tab-out and on commit | Per-field as user tabs, plus full-record on commit | Field-level validation; read values from `R.NEW` or `COMI` |
| `INPUT.ROUTINE` | Input Routine | On commit, after VALIDATION.RTN | Record commit only | Record-level validation; read values from `R.NEW` only |
| `AUTO.NEW.CONTENT` | Auto Field Routine | After ID, per specified field | One specific field (set in `AUTOM.FIELD.NO`) | Populate/modify a field before display. Prefix with `@`; attach to specific field |
| `AFTER.UNAU.RTN` | After Unauthorised Routine | After write to `$NAU` | Record committed to unauthorised state | Write ancillary files. Changes to `R.NEW` NOT reflected — explicit `F.WRITE` required. Prefix with `@` |
| `BEFORE.AUTH.RTN` | Before Auth Routine | Authorisation, before live file write | `.AUTHORISE` function | Can still modify `R.NEW`; changes ARE reflected. Prefix with `@`. Must have `EB.API` entry |
| `AUTH.ROUTINE` | Authorisation Routine | Authorisation, after live file write | `.AUTHORISE` function | Changes to `R.NEW` NOT reflected without explicit `F.WRITE`. No `@` prefix required |

### Execution Ordering at Authorisation Stage

```
User clicks AUTHORISE
    │
    ├─→ BEFORE.AUTH.RTN  (before F.WRITE to live file; R.NEW changes reflected)
    │
    ├─→ F.WRITE to live file
    │
    └─→ AUTH.ROUTINE     (after F.WRITE; R.NEW changes need explicit F.WRITE)
```

### Key Common Variables in Hook Routines

| Variable | Description | Available In |
|----------|-------------|-------------|
| `R.NEW` | Current record being processed | All hook stages |
| `R.OLD` | Previous record image before edit | All hook stages |
| `ID.NEW` | Current record ID | All hook stages |
| `ID.OLD` | Previous record ID | All hook stages |
| `ID.NEW.LAST` | Last committed ID | ID routines |
| `COMI` | Last field value entered (on tab-out) | Validation routine (tab-out context) |
| `APPLICATION` | Current application name | All hook stages |
| `ETEXT` | Error text — set this to raise an error | Validation, Input, Check Record routines |

---

## VERSION.CONTROL — Conditional Field Attributes

`VERSION.CONTROL` is a T24 application that extends the VERSION application with conditional field attribute control.

- One `VERSION.CONTROL` record can be linked to multiple `VERSION` records via the `VERSION.TYPE` field on `VERSION`.
- If the `VERSION.CONTROL` record ID equals the application name itself, its routines apply to the base application (not just a specific version).
- `VERSION.CONTROL` does NOT replace `VERSION` — it is an addition.

---

## BEFORE.AUTH.RTN — Detailed Specification

Source: Core Banking Programming Routines Guide (R19).

### Purpose

`BEFORE.AUTH.RTN` fires during the authorisation stage of an INAU (input-awaiting-authorisation) record, before the record is written to the live file. It is the last opportunity to modify `R.NEW` such that the changes are saved to the authorised record without requiring an explicit `F.WRITE`.

### Attachment

- Attach to the `BEFORE.AUTH.RTN` field of the `VERSION` record.
- Prefix the routine name with `@`.
- The routine must have an entry in the `EB.API` application.

### Sample Code Pattern

```infobasic
*----------------------------------------------------------------------
SUBROUTINE MY.BEFORE.AUTH(PROG.NAME, ID, LOCK.REC, REC.STATUS)
*----------------------------------------------------------------------
* Subroutine Type  : VERSION
* Attached to      : ACCOUNT,MY.VERSION
* Attached as      : BEFORE.AUTH.RTN
* Purpose          : Count accounts before authorisation and store count
*----------------------------------------------------------------------
$INCLUDE GLOBUS.BP I_COMMON
$INCLUDE GLOBUS.BP I_EQUATE
$INCLUDE GLOBUS.BP I_F.ACCOUNT
$INCLUDE GLOBUS.BP I_F.CUSTOMER

GOSUB MAIN.PROCESS
RETURN
*------------*
MAIN.PROCESS:
*------------*
* Get customer from current record
CUST.ID = R.NEW<AC.CUSTOMER>
* Read concat file to count accounts
CALL F.READ('F.CUSTOMER.ACCOUNT', CUST.ID, CUST.ACC.REC, F.CUSTOMER.ACCOUNT, ERR)
ACCT.COUNT = DCOUNT(CUST.ACC.REC, AM)
* Write count to a local reference field (will be saved without explicit F.WRITE)
R.NEW<AC.L.ACCT.COUNT> = ACCT.COUNT
RETURN
END
```

---

## AUTH.ROUTINE — Detailed Specification

Source: Core Banking Programming Routines Guide (R19).

### Purpose

`AUTH.ROUTINE` fires at the authorisation stage, invoked just prior to the final update of files (after `F.WRITE` to live file). Used to write to ancillary/local files based on the authorised record data.

### Key Differences from BEFORE.AUTH.RTN

- **AUTH.ROUTINE** fires after `F.WRITE` to the live file. Changes to `R.NEW` are NOT reflected unless an explicit `F.WRITE` is made.
- Before making any ancillary `F.WRITE` calls, the routine should NOT call `JOURNAL.UPDATE` — T24 core handles journalling.

### Attachment

- Attach to the `AUTH.ROUTINE` field of the `VERSION` record.
- No `@` prefix required (unlike `BEFORE.AUTH.RTN` and `AFTER.UNAU.RTN`).
- Routine name must be an existing catalogued program.

### Sample Code Pattern

```infobasic
*----------------------------------------------------------------------
SUBROUTINE MY.AUTH.RTN(PROG.NAME, ID, LOCK.REC, REC.STATUS)
*----------------------------------------------------------------------
* Subroutine Type  : VERSION
* Attached to      : FUNDS.TRANSFER,MY.FT.VERSION
* Attached as      : AUTH.ROUTINE
* Purpose          : Write FT details to a flat file for interface
*----------------------------------------------------------------------
$INCLUDE GLOBUS.BP I_COMMON
$INCLUDE GLOBUS.BP I_EQUATE
$INCLUDE GLOBUS.BP I_F.FUNDS.TRANSFER

GOSUB WRITE.INTERFACE.FILE
RETURN
*-------------------*
WRITE.INTERFACE.FILE:
*-------------------*
OUT.REC = ''
OUT.REC<1> = R.NEW<FT.DEBIT.ACCT.NO>
OUT.REC<2> = R.NEW<FT.CREDIT.ACCT.NO>
OUT.REC<3> = R.NEW<FT.DEBIT.VALUE.DATE>
OUT.REC<4> = R.NEW<FT.DEBIT.AMOUNT>
OUT.REC<5> = R.NEW<FT.DEBIT.CURRENCY>
* Write to interface file — JOURNAL.UPDATE NOT called here (core handles it)
CALL F.WRITE('F.TEMENOS.TRAINING', ID, OUT.REC, F.TEMENOS.TRAINING, ERR)
RETURN
END
```

---

## AFTER.UNAU.RTN — Detailed Specification

Source: Core Banking Programming Routines Guide (R19).

### Purpose

`AFTER.UNAU.RTN` fires after the record is written to the `$NAU` (unauthorised) file, when the user commits the transaction. Used to write data to ancillary files based on the committed (but not yet authorised) record.

### Key Constraints

- Fires once the record is committed to `$NAU`.
- Changes made to `R.NEW` within this routine are NOT reflected in the `$NAU` record.
- If changes to the `$NAU` record are required, an explicit `F.WRITE` to the `$NAU` file must be made.
- Do NOT call `JOURNAL.UPDATE` — T24 core handles journalling.

### Attachment

- Attach to the `AFTER.UNAU.RTN` field of the `VERSION` record.
- Prefix the routine name with `@`.
- Routine must have an entry in the `EB.API` application.

---

## Auto Field Routines — Detailed Specification

Source: Core Banking Programming Routines Guide (R19).

### Purpose

Auto Field Routines manipulate the content of a specific field before it is displayed to the user. They execute after the record ID is supplied and the record is fetched, but before the screen is rendered.

### Attachment

- Attach to the `AUTO.NEW.CONTENT` field in the `VERSION` application, prefixed with `@`.
- The associated field number is specified in the `AUTOM.FIELD.NO` field of the `VERSION`.
- The routine must have a `PGM.FILE` entry with `PGM.TYPE = 'S'`.
- Must have an `EB.API` entry.

### Example Use Case

Populate the `DEBIT.CURRENCY` field automatically when the user tabs out of `DEBIT.ACCT.NO`.

```infobasic
SUBROUTINE MY.AUTO.FIELD(PROG.NAME, ID, LOCK.REC, REC.STATUS)
$INCLUDE GLOBUS.BP I_COMMON
$INCLUDE GLOBUS.BP I_F.FUNDS.TRANSFER
$INCLUDE GLOBUS.BP I_F.ACCOUNT
* COMI contains the last-entered DEBIT.ACCT.NO value
ACCT.ID = COMI
CALL F.READ('F.ACCOUNT', ACCT.ID, ACCT.REC, F.ACCOUNT, ERR)
IF NOT(ERR) THEN
    R.NEW<FT.DEBIT.CURRENCY> = ACCT.REC<AC.CURRENCY>
END
RETURN
END
```

---

## Java API Aliases for Hook Superclasses

Source: CSD Java Programming Standards (V1.1/Aug-22).

These aliases map T24 hook component names to their Java superclass packages used in Design Studio / L3 Java development.

| Component Name | Java Alias (Superclass Package) |
|----------------|--------------------------------|
| `EB.TemplateHook` (AF — core template) | `hook.system.RecordLifecycle` |
| `EB.EnquiryHook` (AF — enquiry) | `hook.system.Enquiry` |
| `EB.ServiceHook` (AF — service/batch) | `hook.system.ServiceLifecycle` |
| `EB.DataFormattingEngineHook` (AF) | `hook.system.DataFormattingEngine` |
| `AA.ActivityHook` (Retail) | `hook.arrangement.ActivityLifecycle` |
| `AA.CalculationHook` (Retail) | `hook.arrangement.Calculation` |
| `AA.RuleComparisonHook` (Retail) | `hook.arrangement.RuleComparison` |
| `AC.AccountHook` (BF) | `hook.accounting.AccountingEntry` |
| `AC.ContractHook` (BF) | `hook.contract.StandingOrder` |
| `DE.DeliveryHook` (BF) | `hook.system.Delivery` |
| `FT.ContractHook` (BF) | `hook.contract.FundsTransfer` |
| `RC.ContractHook` (BF) | `hook.accounting.TransactionRecycler` |
| `ST.CalculationHook` (BF) | `hook.contract.Calculation` |
| `ST.EnquiryHook` (BF) | `hook.party.CustomerPosition` |
| `ST.StatementHook` (BF) | `hook.accounting.Statement` |
| `IA.AccountingHook` (BF) | `hook.accounting.InternationalAccountingStandards` |
| `PP.PaymentLifecycleHook` (Payments) | `hook.payments.PaymentLifecycle` |

### isService() Guard Pattern

In AA hooks triggered during both online and COB (batch) processing, use `isService()` to skip updates that should not run during batch:

```java
// isService() returns true if currently running as a TSA.SERVICE (batch)
if (!session.isService()) {
    // Only execute during online (non-batch) processing
    doOnlineSpecificUpdate();
}
```

This is critical because AA batch processing routes all activities through the same template code as online — COB executes the hook using OFS messages, making the execution path identical.
