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

## Infobasic Version Routine Types (Template Programs)

T24 Infobasic hooks are attached to VERSION records and execute at defined stages in the template lifecycle. Each is a separate subroutine (< 600 lines) within the overall TEMPLATE (< 2000 lines).

### Routine Summary Table

| Routine Suffix | Full Name Pattern | When it Fires | Purpose |
|----------------|------------------|---------------|---------|
| `XX.FIELD.DEFINITIONS` | `<APP>.XX.FIELD.DEFINITIONS` | Record load / initialise | Define field attributes, defaults, and override attributes before the screen is displayed |
| `XX.CHECK.FIELDS` | `<APP>.XX.CHECK.FIELDS` | Field-level validation (on tab-out and commit) | Perform individual field checks; raise field-level errors |
| `XX.CROSSVAL` | `<APP>.XX.CROSSVAL` | Record-level validation (on commit) | Perform cross-field validations; raise record-level errors |
| `XX.OVERRIDE` | `<APP>.XX.OVERRIDE` | After cross-validation | Generate override messages the user can accept or reject |
| `XX.ACCOUNTING` | `<APP>.XX.ACCOUNTING` | Post-commit accounting stage | Produce accounting entries for the transaction |
| `TEMPLATE.L` | `<APP>.TEMPLATE.L` | Load phase | Called during record load to prepare common variables and open files |
| `XX.SUBROUTINE` | `<APP>.XX.SUBROUTINE` | On demand (called by other routines) | Shared internal utility logic reused across the template routines |

### TEMPLATE (Main Entry Point)

The TEMPLATE program is the controller. It calls each of the subroutine types above in sequence. It must be less than 2000 lines and should contain very little inline code — all logic must be delegated to the named subroutines.

```
* Template structure
GOSUB FIELD.DEFINITIONS   ;* called on record load
GOSUB CHECK.FIELDS        ;* called per field
GOSUB CROSSVAL            ;* called on commit
GOSUB OVERRIDE            ;* called after cross-validation
GOSUB ACCOUNTING          ;* called at accounting stage
RETURN
```

### XX.FIELD.DEFINITIONS

- Called when the record is first displayed to the user.
- Used to set default values, field attributes, and conditional display logic.
- Common variables: `R.NEW` (current record image), `ID.NEW` (record ID).
- Do NOT perform expensive file reads here — use for defaults only.

```infobasic
* Example: default CURRENCY from company local currency
FIELD.DEFINITIONS:
IF R.NEW<AC.CURRENCY> EQ '' THEN
    R.NEW<AC.CURRENCY> = LCCY        ;* LCCY is from I_COMMON
END
RETURN
```

### XX.CHECK.FIELDS

- Called each time the user tabs out of a field and on final commit.
- Must check `COMI` (last input value) or `R.NEW<FIELD.POS>`.
- Raise field errors via `ETEXT` or the standard error mechanism.
- Do not assume fields are entered in order; client versions may present fields in any sequence.

```infobasic
* Example: validate that DEBIT.AMOUNT is positive
CHECK.FIELDS:
IF COMI EQ EB.FIELD.DEBIT.AMOUNT THEN
    IF R.NEW<FT.DEBIT.AMOUNT> LE 0 THEN
        ETEXT = 'EB-AMOUNT.MUST.BE.POSITIVE'
    END
END
RETURN
```

### XX.CROSSVAL

- Called once the user commits (saves) the whole record.
- All fields are available in `R.NEW`.
- Used for inter-field business rule validation.
- Errors raised here block the record from being written.

```infobasic
* Example: cross-validate debit and credit currencies match
CROSSVAL:
IF R.NEW<FT.DEBIT.CURRENCY> NE R.NEW<FT.CREDIT.CURRENCY> THEN
    IF R.NEW<FT.EXCHANGE.RATE> EQ '' THEN
        ETEXT = 'EB-EXCHANGE.RATE.REQUIRED'
    END
END
RETURN
```

### XX.OVERRIDE

- Called after `XX.CROSSVAL` when there are no blocking errors.
- Used to raise non-blocking warnings that the user can accept.
- Set override messages via the standard OVERRIDE mechanism.

```infobasic
* Example: warn if amount exceeds limit
OVERRIDE:
IF R.NEW<AC.WORKING.BALANCE> GT OD.LIMIT THEN
    CALL STORE.OVERRIDE('EB-BALANCE.EXCEEDS.LIMIT', '', '')
END
RETURN
```

### XX.ACCOUNTING

- Called after the record is validated and committed, during the accounting stage.
- Produces `AC.ENTRIES` records or invokes accounting APIs.
- Must not re-validate or raise user-facing errors.

### TEMPLATE.L

- The load phase companion to TEMPLATE.
- Called during record initialisation to open files, set common variables, and prepare product-level state.
- File handles opened here are reused across all subsequent routine calls.

```infobasic
* TEMPLATE.L pattern
GOSUB OPEN.FILES
GOSUB INIT.VARIABLES
RETURN

OPEN.FILES:
CALL OPF('F.ACCOUNT', F.ACCOUNT)
RETURN

INIT.VARIABLES:
PRODUCT.CODE = 'FT'
RETURN
```

### XX.SUBROUTINE

- A shared utility subroutine called by other template routines.
- Follows the standard `SUBROUTINE <name>(args...)` signature.
- Must have a corresponding `EB.API` entry.

---

## VERSION Record Hook Fields (Infobasic)

These fields on the VERSION application control which Infobasic subroutines fire at each stage.

| VERSION Field | Hook Type | Stage | Notes |
|---------------|-----------|-------|-------|
| `ID.RTN` | ID Routine | Before record load | Validates / manipulates the record ID. Uses `ID.NEW`, `ID.OLD`, `ID.NEW.LAST`. Attached with `@` prefix |
| `CHECK.REC.RTN` | Check Record | After ID resolved, before display | Validates the record at record level before displaying to user |
| `VALIDATION.RTN` | Validation Routine | On tab-out and commit | Field-level validation. Values from `R.NEW` or `COMI` |
| `INPUT.ROUTINE` | Input Routine | After VALIDATION.RTN, on commit | Record-level validation. Values from `R.NEW` only |
| `AFTER.UNAU.RTN` | After Unauthorised | After record written to `$NAU` file | Post-commit processing; changes to `R.NEW` are NOT reflected without explicit `F.WRITE` |
| `BEFORE.AUTH.RTN` | Before Auth | Before record written to live file at authorisation | Can still modify `R.NEW`; changes ARE reflected. Attached with `@` prefix |
| `AUTH.ROUTINE` | Authorisation | After `F.WRITE` to live file at authorisation | Updates local files; changes to `R.NEW` are NOT reflected without explicit `F.WRITE` |
| `AUTO.NEW.CONTENT` | Auto Field | After ID resolved, per-field | Populates/modifies a specific field before display. Attached with `@` prefix on the field |

### Difference: Validation Routine vs Input Routine

- **Validation Routine** (`VALIDATION.RTN`): Invoked on committing the record OR on tab-out of a field. Values can be extracted from `R.NEW` or `COMI`.
- **Input Routine** (`INPUT.ROUTINE`): Invoked on commit/validate after the Validation Routine. Values are extracted from `R.NEW` only.

### Difference: Before Auth vs Auth Routine

- **Before Auth** (`BEFORE.AUTH.RTN`): Invoked before `F.WRITE` is made to the live file. Changes to `R.NEW` are reflected in the authorised record.
- **Auth Routine** (`AUTH.ROUTINE`): Invoked after `F.WRITE` is made. Changes to `R.NEW` are NOT reflected unless an explicit `F.WRITE` is made in the routine.

---

## NoFile Enquiry Pattern

A NoFile enquiry extracts data from multiple T24 applications using a custom Infobasic routine when the standard ENQUIRY application cannot join the required files.

### Components

1. **Infobasic routine** — extracts data, returns one outgoing parameter (dynamic array).
2. **STANDARD.SELECTION record** — ID must start with `NOFILE.` to bypass FILE.CONTROL validation.
3. **ENQUIRY record** — references the `NOFILE.xxx` SS ID in `FILE.NAME`.

### STANDARD.SELECTION Field Types

| USR.TYPE | Meaning | Usage |
|----------|---------|-------|
| `R` | Routine | The field whose value is returned by the NoFile subroutine |
| `S` | Selection | A user-input field passed to the routine via `D.FIELDS`/`D.RANGE.AND.VALUE` |

### Common Variables in Routines (I_ENQUIRY.COMMON)

| Variable | Description |
|----------|-------------|
| `D.FIELDS` | Field names from the dynamic selection criteria box |
| `D.LOGICAL.OPERANDS` | Operands used in the selection box |
| `D.RANGE.AND.VALUE` | Values entered by the user in the selection box |
| `O.DATA` | Last extracted field value (used in conversion routines) |
| `R.RECORD` | Full record currently being processed by the enquiry |

### Return Variable Structure

```infobasic
* Accumulate data row-wise; use any delimiter within a row; FM between rows
AC.DET.ARR<-1> = AC.ID : "*" : CR.AMT : "*" : DR.AMT : "*" : CR.TOT.INT : "*" : DR.TOT.INT
```

- `-1` appends a new FM-delimited row.
- Each row's values are separated by `*` (or any chosen delimiter).
- In the ENQUIRY record, use `CONVERSION = F *,1,1` to extract values (`F <delim>,<startpos>,<numpos>`).
- Set `OPERATION = 0` for fields extracted from the routine's return list.

### Sample NoFile Routine Skeleton

```infobasic
SUBROUTINE E.NOF.CUS.AC.DET(AC.DET.ARR)
$INCLUDE GLOBUS.BP I_COMMON
$INCLUDE GLOBUS.BP I_EQUATE
$INCLUDE GLOBUS.BP I_F.ACCOUNT
$INCLUDE GLOBUS.BP I_F.CUSTOMER.ACCOUNT
$INCLUDE GLOBUS.BP I_ENQUIRY.COMMON
GOSUB INITIALISATION
GOSUB OPEN.FILES
GOSUB PROCESS
RETURN
*--------------*
INITIALISATION:
*--------------*
FN.CUSTOMER.ACCOUNT = 'F.CUSTOMER.ACCOUNT'
FV.CUSTOMER.ACCOUNT = ''
RETURN
*----------*
OPEN.FILES:
*----------*
CALL OPF(FN.CUSTOMER.ACCOUNT, FV.CUSTOMER.ACCOUNT)
RETURN
*-------*
PROCESS:
*-------*
LOCATE "CUSTOMER.ID" IN D.FIELDS<1> SETTING CUS.POS THEN
    CUSTOMER.ID = D.RANGE.AND.VALUE<CUS.POS>
END
CALL F.READ(FN.CUSTOMER.ACCOUNT, CUSTOMER.ID, CUS.ACC.REC, FV.CUSTOMER.ACCOUNT, ERR)
LOOP
    REMOVE AC.ID FROM CUS.ACC.REC SETTING AC.POS
    WHILE AC.ID:AC.POS
    * ... process each account ...
    AC.DET.ARR<-1> = AC.ID : "*" : CR.AMT : "*" : DR.AMT
REPEAT
RETURN
END
```

---

## Enquiry Hooks (Java — Transact Extensibility)

From Transact R20+, enquiry hooks can be written in Java via the `Enquiry` superclass (`com.temenos.t24.api.hook.system`).

### Exit Points

| Enquiry Field | Java Method | Description |
|---------------|-------------|-------------|
| `BUILD.ROUTINE` | `setFilterCriteria` | Modify the dynamic selection box before records are selected |
| `CONVERSION` | `setValue` | Modify the value of an individual field before display |
| `CONVERSION` | `setRecord` | Set the entire record contents (used for NoFile enquiry in Java) |
| `SYS.FIELD.NO` in `STANDARD.SELECTION` (SYS.TYPE=R) | `setIds` | Define the list of record IDs to process (NoFile enquiry) |

### setFilterCriteria

```java
// Superclass: com.temenos.t24.api.hook.system.Enquiry
// EB.API field: BUILD.ROUTINE in ENQUIRY record
public List<FilterCriteria> setFilterCriteria(
    List filterCriteria,       // ENQ.DATA<2...4> — user's selection box entries
    EnquiryContext enquiryContext
) {
    // Manipulate filterCriteria list, return modified list
    return filterCriteria;
}
```

- Invoked after the user submits the selection screen.
- `filterCriteria` maps to `ENQ.DATA<2>` (fields), `ENQ.DATA<3>` (operators), `ENQ.DATA<4>` (values).
- Return a new list of `FilterCriteria` to replace or supplement the user's input.

### setValue

```java
// EB.API field: CONVERSION in ENQUIRY record (field-level)
public String setValue(
    String value,              // O.DATA — current field value
    String currentId,          // ID common variable
    TStructure currentRecord,  // R.RECORD — full current record
    List filterCriteria,       // ENQ.SELECTION fields<2...4>
    EnquiryContext enquiryContext
) {
    // Return the new display value for this field
    return value;
}
```

- Invoked for each field with a CONVERSION hook, in field order.
- The returned string is written back to `O.DATA` and displayed.

### setRecord

```java
// EB.API hook: ENQUIRY.CONVERSION.HOOK; field: CONVERSION in ENQUIRY
public void setRecord(
    String value,              // O.DATA
    String currentId,          // ID common variable
    TStructure currentRecord,  // R.RECORD — INOUT parameter
    List filterCriteria,
    EnquiryContext enquiryContext
) {
    // Modify currentRecord directly (INOUT)
    // Primarily for NoFile enquiry — populate record from multiple sources
}
```

- `currentRecord` is an INOUT parameter — changes made to it are seen by the enquiry engine.
- Mainly intended for NoFile enquiry scenarios in Java.

### setIds (NoFile Enquiry in Java)

```java
// SYS.FIELD.NO in STANDARD.SELECTION (SYS.TYPE = 'R')
// EB.API: Source type = method, Java method = setIds
public List<String> setIds(
    List filterCriteria,       // D.FIELDS, D.RANGE.AND.VALUE, D.LOGICAL.OPERANDS
    EnquiryContext enquiryContext
) {
    // Return list of record IDs for the enquiry to process
    return idList;
}
```

- Replaces the standard database SELECT for NoFile enquiries.
- Called during the record selection stage.
- In EB.API: `Source type = method`, `Java Method = setIds`, specify `Java Class` and `Java Package`.

---

## Four-Eye Validation (KC+ / Financial Crime)

The four-eye validation process for KC+ (Know Your Customer plus) is configured through the Authorization and Workflow administration screens rather than via code hooks.

### Configuration Steps

1. **Select Rule Base** — `Home > Configuration > Authorisation and Workflow` (FCM Administrator role)
2. **Add Action Rule for role** — assign the four-eye rule to the appropriate user role
3. **Update Rule Base** — system writes back to FCFF (automated, SYSTEM role)
4. **Select Customer Rule Base** — `Home > Configuration > Authorisation and Workflow`
5. **Activate Rule Base** — `Home > Configuration > Authorisation and Workflow`
6. **Update Rule Base status** — automated update to FCFF (SYSTEM role)

The four-eye validation is a business process configuration (R202510 Financial Crime Mitigation). The underlying transaction hook used is the standard `BEFORE.AUTH.RTN` / `AUTH.ROUTINE` mechanism on the relevant VERSION records for the customer onboarding transaction.
