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

## T24 Infobasic Programming Standards

Source: T24 Programming Standards (Temenos User Guide) and TAM Coding Standards.

### Program Structure Rules

- All routines in T24 are called **subroutines**. Routines must not be executed directly from jSHELL.
- **TEMPLATE** programs must be less than **2000 lines**. New templates should contain very little code; all logic must be delegated to named subroutines (FIELD.DEFINITIONS, CHECK.FIELDS, CROSSVAL, etc.).
- **Subroutines** must be less than **600 lines**. Ideally viewable on a single screen (80 chars × 23 lines).
- TAM standard (stricter): routines should not exceed **300 lines**; GOSUB paragraphs should not exceed **75 lines**; CALL routines should have no more than **4 arguments**.
- All code must be modular: each unit/paragraph < 100 lines, single entry and single exit point.
- Do NOT write top-down code. Each routine must have one main controlling section; detailed code is written as GOSUB subroutines.
- Do not assume field 1 will be input before field 2 — client versions may reorder fields.
- Avoid deeply nested IFs. If an IF exceeds 20 lines, convert to a GOSUB.
- Labels, Variables, and Routines must not share the same names.
- Labels must exist on their own line with no other text appended.
- Do not use multi-statement lines.
- Do not comment out code — delete it.

### Naming Conventions

#### Variable Prefixes

| Level | Defined In | Prefix | Example |
|-------|-----------|--------|---------|
| Global | `I_COMMON` | `C$` | `C$EB.PHANTOM.ID` |
| Product Level | `I_XX.COMMON` (e.g., `I_RP.COMMON`) | `XX$` (e.g., `RP$`) | `RP$REPO.TYPE` |
| Subroutine Level | Local to routine | (none) | `ACCT.ID` |

- Product-level variables are defined in `I_XX.COMMON` and available to all subroutines that include that common block.
- Subroutine-level variables have no prefix and can only be passed to other subroutines as CALL arguments.

#### File and Record Variable Conventions

- **File variables** must be named `F.filename` where `filename` is the EXACT name of the file.
  - Example: `F.ACCOUNT`, `F.CUSTOMER`, `F.FUNDS.TRANSFER`
- **Record variables** must be named `R.filename`.
  - Example: `R.ACCOUNT`, `R.CUSTOMER`
- Fields must never be referenced by their field number (except in conversion routines). Always use the field names from standard inserts.

#### Subroutine Header Comment Format

```infobasic
*********************************************************************
    SUBROUTINE XXXXXXXX (IN.PARAM.REC, IN.PARAM.ID, OUT.PARAM.REC)
*********************************************************************
* Company Name      :  Bank Name
* Developed By      :  Temenos Application Management
*-------------------------------------------------------------------
* Subroutine Type   :  VERSION/ENQUIRY/MAINLINE/PHANTOM/COB
* Attached to       :  VERSION Name / ENQUIRY Name / BATCH Record ID
* Attached as       :  CONVERSION/BUILD.ROUTINE/FIELD.VAL.RTN
* In Parameter      :
*     IN.PARAM.NAME     - Name of the query
*     IN.PARAM.ID       - Record ID
* Out Parameter     :
*     OUT.PARAM         - Array of records selected
*-------------------------------------------------------------------
* Modification Details:
*-------------------------------------------------------------------
* 23/07/2009 - ODR-2009-XX-XXXX
* Development for fetching T24 account number for IBAN
```

### Forbidden Constructs

| Construct | Reason / Alternative |
|-----------|---------------------|
| `STOP` | Terminates the session abruptly. Never use. |
| `ABORT` | Same as STOP. Never use. |
| `RETURN TO` | Creates non-linear control flow. Never use. |
| `GOTO` | Even to exit a unit or retry a locked record. Never use. |
| `FOR…NEXT` | Inefficient. Use `LOOP…REMOVE` instead. |
| Multi-statement lines (`A=1 ; B=2`) | Hard to read. One statement per line. |
| Field number references | Breaks upgrades. Use insert-file field names. |
| Common variables as CALL arguments | Can cause unexpected errors. Do not pass `ETEXT` etc. as arguments. |
| Commented-out code | Delete dead code, do not comment it out. |

### LOOP...REMOVE Preference

```infobasic
* Preferred over FOR...NEXT for dynamic array traversal
LOOP
    REMOVE ITEM FROM ARRAY SETTING POS
    WHILE ITEM:POS
    * process ITEM
REPEAT
```

### CHECK.ROUTINE.EXIST Pattern

When calling API interfaces or user-defined subroutines, never use the program variable as the call flag (it gets replaced by a memory address after the first call). Always use `CHECK.ROUTINE.EXIST` — but call it only once at initialisation.

```infobasic
* In initialisation section — call once only
CALL CHECK.ROUTINE.EXIST('MY.CUSTOM.RTN', RTN.EXISTS)

* In main process section
IF RTN.EXISTS THEN
    CALL MY.CUSTOM.RTN(ARG1, ARG2)
END
```

### Standard Routine Structure

```infobasic
*------------------------------------------------------------
SUBROUTINE MY.ROUTINE(IN.REC, IN.ID, OUT.REC)
*------------------------------------------------------------
* ... header comment block ...
$INCLUDE GLOBUS.BP I_COMMON
$INCLUDE GLOBUS.BP I_EQUATE
*
GOSUB INITIALISATION
GOSUB MAIN.PROCESS
RETURN
*--------------*
INITIALISATION:
*--------------*
* Initialise variables and open files here
RETURN
*--------------*
MAIN.PROCESS:
*--------------*
* Main business logic — delegate to further GOSUB paragraphs
RETURN
END
```

---

## EB.COMPILE — On-Site Development

`EB.COMPILE` is the T24 utility for compiling and cataloguing Infobasic programs in the on-site (client) environment.

### Usage

```
EB.COMPILE <BPFILE> <PROGRAMNAME>
```

- Compiles the source in `<BPFILE>` and catalogues the object into `JBCDEV_LIB` (typically `$HOME/lib`).
- Produces object code as `$PROGRAMNAME`.
- Any compile errors must be resolved before the catalogue step runs.

### Example

```
EB.COMPILE TRG.BP TRG.RTN1
```

- Source: `TRG.BP` file, program `TRG.RTN1`
- Output: `$TRG.RTN1` in `JBCDEV_LIB`

### Steps

1. Write / edit source in the BP file.
2. Run `EB.COMPILE <BPFILE> <PROGNAME>`.
3. Check for compile errors. If errors: fix source and recompile.
4. On success, the object code is catalogued into the shared library.
5. Create or update the `PGM.FILE` record for the routine (set `PGM.TYPE = 'S'` for subroutines).
6. Create an `EB.API` entry if the routine is called via an API hook mechanism.

---

## Calling jBC from Java (TAFJ)

Source: "Calling JBC subroutine from Java" (Mahmudur Rahman).

In Temenos Transact running on TAFJ, Java L3 code can invoke Infobasic (jBC) subroutines using the `TAFJRuntime` API. This allows Java hooks to call existing jBC business logic without rewriting it.

### callJBC — No Return Value

Use `callJBC()` when the jBC subroutine has no return parameter (void logic only).

```java
TAFJRuntime runtime = TAFJRuntimeFactory.getTAFJRuntime(T24Context);
runtime.callJBC("CUS.FILE.GEN.SERVICE");
```

Corresponding jBC subroutine (no OUT arguments):

```infobasic
SUBROUTINE CUS.FILE.GEN.SERVICE
$INSERT I_COMMON
$INSERT I_EQUATE
GOSUB PROCESS
RETURN
PROCESS:
    CRT "Calling From Java"
RETURN
END
```

### invokeJBC — With Return Value / Parameters

Use `invokeJBC()` when the jBC subroutine has input and/or output parameters, including dynamic arrays (FM/VM/SM).

```java
// Prepare jVar input parameters
jVarClient inOne   = jVarClientFactory.get("ABC");
jVarClient inTwo   = jVarClientFactory.get("500");
jVarClient inThree = jVarClientFactory.get("USD");

// OUT parameters
jVarClient out = jVarClientFactory.get();   // OUT<FM,VM,SM>
jVarClient err = jVarClientFactory.get();   // Error message

// Call the jBC subroutine
TAFJRuntime runtime = TAFJRuntimeFactory.getTAFJRuntime(T24Context);
runtime.invokeJBC("FT.CUSTOM.CHECK", inOne, inTwo, inThree, out, err);
```

Corresponding jBC subroutine:

```infobasic
SUBROUTINE FT.CUSTOM.CHECK(IN1, IN2, IN3, OUTPUT, ERR_MESS)
* IN1, IN2, IN3 : input parameters
* OUTPUT        : output dyn array (FM / VM / SM)
* ERR_MESS      : error message (if any)
ERR_MESS = ""
OUTPUT = ""
IF NUM(IN2) NE 1 THEN
    ERR_MESS = "A Mandatory Numeric Value Need To Input As 3rd Variable!"
END ELSE
    OUTPUT<1,1,1> = "F1V1S1"
    OUTPUT<1,2,1> = "AMOUNT:" : IN2
    OUTPUT<1,2,2> = "F1V2S2"
    OUTPUT<2,1>   = "STATUS:OK"
END
END
```

### Extracting Multi-Value Output from jBC

```java
// getSM and getVM are local helper methods that split the DynArray using FM/VM/SM separators
String fm1_vm2_sm1 = getSM(out, 1, 2, 1);  // OUT<1,2,1>
String fm1_vm2_sm2 = getSM(out, 1, 2, 2);  // OUT<1,2,2>
String fm1_vm1_sm1 = getSM(out, 1, 1, 1);  // OUT<1,1,1>
String fm2_vm1     = getVM(out, 2, 1);      // OUT<2,1>
```

### Summary: callJBC vs invokeJBC

| Method | Use For | Return Value | Input Format |
|--------|---------|-------------|-------------|
| `callJBC()` | SUBROUTINES with no return | None | N/A |
| `invokeJBC()` | FUNCTIONS / routines with output | Supported via `jVarClient` | `jVarClient` (supports FM/VM/SM DynArrays) |

---

## TEMPLATE Program Structure Details

A TEMPLATE is the central entry-point program for a T24 application's customization layer. It orchestrates multiple subroutines across the transaction lifecycle.

### Full Lifecycle Sequence

```
User opens record
    → TEMPLATE.L (Load)          — open files, init common variables
    → XX.FIELD.DEFINITIONS       — set defaults before display
    
User tabs out of a field
    → XX.CHECK.FIELDS            — field-level validation

User commits / saves record
    → XX.CROSSVAL                — cross-field record-level validation
    → XX.OVERRIDE                — generate override warnings
    
Record written to $NAU
    (→ AFTER.UNAU.RTN if set on VERSION)
    
Record authorised
    → BEFORE.AUTH.RTN (if set)   — pre-auth validation, can modify R.NEW
    → F.WRITE to live file
    → AUTH.ROUTINE (if set)      — post-auth actions, explicit WRITE needed
    
Accounting stage
    → XX.ACCOUNTING              — produce accounting entries
```

### Data Access Inserts

Insert files provide field-name constants for each application. They must be included at the top of every template subroutine that accesses that application's fields.

```infobasic
$INCLUDE GLOBUS.BP I_COMMON          ;* global common variables (C$, LCCY, etc.)
$INCLUDE GLOBUS.BP I_EQUATE          ;* standard equates (AM, VM, SM delimiters)
$INCLUDE GLOBUS.BP I_F.ACCOUNT       ;* AC.xxx field name constants
$INCLUDE GLOBUS.BP I_F.FUNDS.TRANSFER ;* FT.xxx field name constants
```

### Common Variables in I_COMMON (Key Subset)

| Variable | Description |
|----------|-------------|
| `R.NEW` | Current record image being processed |
| `R.OLD` | Previous (pre-edit) record image |
| `ID.NEW` | Current record ID |
| `ID.OLD` | Previous record ID |
| `COMI` | Last field value entered by the user (on tab-out) |
| `LCCY` | Local currency of the current company |
| `OPERATOR` | Current user ID |
| `APPLICATION` | Current application name |
| `ETEXT` | Error text variable — set to raise an error |
| `C$EB.PHANTOM.ID` | Phantom (batch) process ID |

### Error Handling Pattern

```infobasic
* Raise a validation error from any hook routine
ETEXT = 'EB-MY.ERROR.ID'    ;* references an EB.ERROR record ID
RETURN

* Alternatively using the error subroutine
CALL ERROR.RTN('EB-MY.ERROR.ID', ERR.ARGS, ERR.LEVEL)
```

- Error messages are stored as `EB.ERROR` records. Never hardcode error text strings.
- Override messages are stored as `OVERRIDE` records. Pass the record ID to `STORE.OVERRIDE`.

### Multithreaded Service Components

A multithreaded T24 service (COB job) comprises three subroutines controlled by `BATCH.JOB.CONTROL`:

| Component | Naming Convention | Purpose |
|-----------|------------------|---------|
| Load Routine | `<JOB>.LOAD` | Initialise common variables (`I_<JOB.NAME>.COMMON`) |
| Select Routine | `<JOB>.SELECT` | Form and execute SELECT; call `BATCH.BUILD.LIST` to store results |
| Record Routine | `<JOB>` (no suffix) | Process each individual record ID from the select list |

```infobasic
* In the .SELECT routine:
EXECUTE SELECT.STATEMENT RTNLIST SELECT.LIST
CALL BATCH.BUILD.LIST(CONTROL.ARRAY, SELECT.LIST)   ;* mandatory

* In the .LOAD routine:
$INCLUDE GLOBUS.BP I_GIFT.VOUCHER.COMMON
* Initialise all variables from the common block
```

Note: In a componentised environment, the `I_<JOB>.COMMON` insert is replaced by `.component` properties and constants — the `.LOAD` routine is then optional.
