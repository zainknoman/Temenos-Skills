# temenos-l3-java — Claude Skill

**Version:** 1.3.0  
**Last Updated:** 2026-06-18  
**Platform:** Temenos T24 / Transact (TAFJ environment, R19+)

A Claude Code skill that turns any conversation into a Temenos L3 Java expert session.  
Built from real bank implementation code (JIB/AOAB) and three official Temenos documents:

| Source | Content |
|---|---|
| `Introduction to L3 Java Customisation.pdf` | Official package/class/method API reference |
| `T24 USER GUIDE TO L3 API - Version & Enquiry Routines.pdf` | Version routine types and T24→Java method mappings |
| `CSD - Java Programming Standards.pdf` | Official CSD coding standards, core APIs, AA APIs |

---

## What This Skill Knows

### Hook Superclasses

| Superclass | Package | Use Case |
|---|---|---|
| `RecordLifecycle` | `hook.system.RecordLifecycle` | Transaction-level hooks on any T24 application |
| `ServiceLifecycle` | `hook.system.ServiceLifecycle` | COB/batch jobs (SELECT + RECORD routines) |
| `Enquiry` | `hook.system.Enquiry` | Custom enquiry result sets |
| `ActivityLifecycle` | `hook.arrangement.ActivityLifecycle` | AA Lending/Deposits arrangement activity hooks |

### Version Routine Types → Java Method Mapping

| T24 Routine | Java Method | Trigger Point |
|---|---|---|
| `ID.RTN` | `checkId()` | Record ID entered |
| `CHECK.REC.ROUTINE` | `defaultFieldValues()` | After ID validated (I/A/D/R only) |
| `AUTO.FIELD.ROUTINE` | `defaultFieldValues()` | Before record displayed to user |
| `VALIDATION.ROUTINE` | `validateField()` | Field-level commit validation |
| `INPUT.ROUTINE` | `validateRecord()` | Record-level commit validation |
| `BEFORE.AUTH.ROUTINE` | `updateCoreRecord()` | Before F.WRITE to live file |
| `AUTH.ROUTINE` | `postUpdateRequest()` | After authorise — async OFS |

### Enquiry Routine Types

| Routine | Java Method | Purpose |
|---|---|---|
| `BUILD.ROUTINE` | `setFilterCriteria()` | Set selection criteria programmatically |
| `CONVERSION.ROUTINE` | `setValue()` | Transform field values before display |
| NOFILE ENQUIRY | `setIds()` | Multi-application custom enquiry |

### ActivityLifecycle Methods (AA Arrangements)

| Java Method | AA.PRD.DES.ACTIVITY.API Field | Invoker |
|---|---|---|
| `defaultFieldValues()` | `RECORD.ROUTINE` / `PRE.VALIDATION.RTN` | `AA.DEFAULT.FIELD.VALUES.INVOKER` |
| `validateRecord()` | `POST.ROUTINE` / `VALIDATE.RTN` | `AA.VALIDATE.RECORD.INVOKER` |
| `updateLookupTable()` | `POST.ROUTINE` | `AA.UPDATE.LOOKUP.TABLE.INVOKER` |
| `postCoreTableUpdate()` | `POST.ROUTINE` | `AA.POST.CORE.TABLE.UPDATE.INVOKER` |
| `generateSecondaryActivity()` | `POST.ROUTINE` | `AA.GENERATE.SECONDARY.ACTIVITY.INVOKER` |

### Core APIs Covered

| API | Key Methods |
|---|---|
| **Amount** | `getAvailableAmount`, `getBalance`, `getTurnoverCredit`, `getTurnoverDebit` |
| **Date** | `addWorkingDays`, `getWorkingDayDifference`, `getMonthDifference`, `gregorianToJulian`, `getDayType` |
| **Exchange Rate** | `calculateRate`, `calculateBuyExchangeRateAmount`, `calculateExchangeRate`, `calculateBuyAmount` |
| **Currency** | `getRoundAmount` |
| **Interest** | `getBasicRate`, `calculateAccrualDays` |
| **ST.Customer** | `customerExists`, `getAccountNumber`, `getLimit`, `getLiableLimit`, `getProfile`, `getSettlementAccountId` |
| **LI.Limit** | `getCurrencyAmount` |
| **AA Contract** | 35+ methods: `getConditionForProperty`, `getCommitmentCondition`, `getBillIds*`, `getBalanceMovements`, overdue dates, repayment amounts |
| **AA Product / Property** | `getProduct`, `getPropertiesForProduct`, `getPropertyIdsForPropertyClass` |
| **DataAccess** | `getRecord`, `getHistoryRecord`, `getRequestResponse`, `selectRecords`, `write`, `delete`, `release` |
| **Session (EB.Session)** | `getCompanyId`, `getUserId`, `getCurrentVariable`, `getOnlineStatus`, `isService`, `setNextVersion` |

### CSD Coding Standards
- Naming conventions with regex patterns (class, method, variable, member, parameter, constant)
- Data record naming rules (all custom records must be prefixed `CSD`)
- Size limits (2000 lines/file, 160 chars/line, 100 lines/method, max 10 params)
- Exception handling rules (EB.ERROR + OVERRIDE records, no hardcoded messages)
- BigDecimal for monetary calculations
- JAR naming conventions

---

## How to Use This Skill for Development

### Invoking the Skill

Type `/temenos-l3-java` at the start of your request, or simply describe what you want to build.  
The skill auto-triggers on keywords like: `RecordLifecycle`, `validateRecord`, `ActivityLifecycle`, `postCoreTableUpdate`, `AA hook`, `EB.API`, `T24 customization`, `version routine`, etc.

```
/temenos-l3-java write a validateRecord hook for CUSTOMER that checks NATIONALITY is mandatory for individual customers
```

```
/temenos-l3-java create a ServiceLifecycle batch that selects all PENDING records from MY.TABLE and processes them
```

```
/temenos-l3-java write a postCoreTableUpdate for an AA LENDING arrangement that writes to a custom table after authorisation
```

---

### Development Workflow

#### Step 1 — Identify the Hook Type

Ask yourself which lifecycle event you need:

| Scenario | Hook Type | Java Method |
|---|---|---|
| Validate a field when user commits | RecordLifecycle | `validateRecord()` |
| Set default values when record opens | RecordLifecycle | `defaultFieldValues()` |
| Validate/transform the record ID | RecordLifecycle | `checkId()` |
| Trigger another T24 transaction on AUTH | RecordLifecycle | `updateRecord()` |
| Post-authorise async OFS action | RecordLifecycle | `postUpdateRequest()` |
| COB/batch job on a set of records | ServiceLifecycle | `getIds()` + `updateRecord()` |
| Custom enquiry with computed rows | Enquiry | `setIds()` |
| Default AA property fields | ActivityLifecycle | `defaultFieldValues()` |
| Validate AA activity | ActivityLifecycle | `validateRecord()` |
| Post-commit AA table write or OFS | ActivityLifecycle | `postCoreTableUpdate()` |

#### Step 2 — Write the Class Skeleton

Ask Claude:
```
/temenos-l3-java generate the skeleton for a RecordLifecycle validateRecord hook
for the CUSTOMER application, package com.jib
```

Claude will produce a correctly structured class with:
- Correct package
- Correct imports
- Correct method signature with `@Override`
- `currentRecord.set(rec.toStructure())` before return
- `return rec.getValidationResponse()`

#### Step 3 — Add Business Logic

Describe the rule in plain English:

```
/temenos-l3-java in the validateRecord for CUSTOMER:
- if local ref field CTRY.CODE equals "JO" then local ref field MFZA.CODE is mandatory
- if customer type (CUS.TYPE) is 1 (individual) then local ref field NAME.3 multivalue group is mandatory
```

Claude will generate:
- `getLocalRefField()` / `getLocalRefGroups()` patterns
- Correct `try-catch` wrapping on LocalRef access
- `setError()` with CSD-compliant `EB-CSD.*` error code references
- Proper MV iteration with `.set(i, group)` vs `.add(i, group)` distinction

#### Step 4 — Cross-Record Reads

```
/temenos-l3-java in defaultFieldValues read the LC.TYPES record for the current
LC type and set the transferable flag based on the result
```

Claude will use:
```java
DataAccess da = new DataAccess(this);
LcTypesRecord lct = new LcTypesRecord(da.getRecord("", "LC.TYPES", "", lcType));
```

#### Step 5 — AA Arrangement Hooks

```
/temenos-l3-java write a defaultFieldValues ActivityLifecycle hook that reads
the COMMITMENT condition from the current arrangement and sets the payment
schedule installment amount based on a goal amount local ref field
```

Claude will produce correct `Contract` API usage:
```java
Contract contract = new Contract(this);
contract.setContractId(arrangementId);
AaPrdDesTermAmountRecord termAmt = contract.getCommitmentCondition("COMMITMENT");
```

#### Step 6 — Review Against CSD Standards

Ask Claude to review any code for CSD compliance:

```
/temenos-l3-java review this code for CSD coding standards violations
```

Claude will check for:
- `double`/`float` used for monetary values (should be `BigDecimal`)
- DataAccess/Session re-created in sub-methods (should be declared once)
- Hardcoded error strings (should be `EB-CSD.*` record IDs)
- Method length > 100 lines
- Missing `@Override`
- `System.out.println` instead of Logger

#### Step 7 — Create the EB.API Record

```
/temenos-l3-java what EB.API record do I need for this hook?
```

Claude will generate:
```
SOURCE.TYPE  = Method
JAVA.CLASS   = com.jib.MyCustomerHook
JAVA.METHOD  = validateRecord
JAVA.PACKAGE = com.jib
```

And tell you which VERSION field to attach it to.

---

### Common Prompts and Examples

#### Generate a complete hook from scratch
```
/temenos-l3-java write a complete RecordLifecycle validateRecord hook for
FUNDS.TRANSFER in package com.jib that:
1. Validates debit and credit currencies are not the same
2. Throws T24CoreException if debit account has posting restriction DEBIT
3. Sets an override if amount exceeds 50000 in local currency
```

#### Write an AA batch COB job
```
/temenos-l3-java write a ServiceLifecycle batch that:
- Selects all EB.MY.TABLE records WITH STATUS EQ 'PENDING'
- For each record, triggers version MY.APP,BATCH.VERSION via SynchronousTransactionData
- Sets status to 'PROCESSED' after completion
```

#### Get a Core API pattern
```
/temenos-l3-java how do I calculate the number of working days between two dates?
```

```
/temenos-l3-java how do I read the available balance of an account and compare
it against a transaction amount using BigDecimal?
```

#### Understand a method signature
```
/temenos-l3-java what is the correct method signature for postCoreTableUpdate
in ActivityLifecycle and which TransactionData import do I use?
```

#### Fix a CSD violation
```
/temenos-l3-java I'm using double for an amount calculation — how do I convert
this to BigDecimal properly?
```

---

### Key Things Claude Will Always Enforce

1. **`currentRecord.set(rec.toStructure())`** before every return in RecordLifecycle
2. **Correct TransactionData import** per hook type (4 different imports exist)
3. **`try-catch` on all LocalRef access**
4. **`BigDecimal` for monetary calculations** — never `double`/`float`
5. **EB.ERROR record references** — never hardcoded strings
6. **`Contract.setContractId()` before any Contract API call**
7. **`isService()` guard** in AA hooks if an update must not run during COB
8. **DataAccess and Session declared once** in the parent method

---

## File Structure

```
C:\Users\Lenovo\.claude\skills\temenos-l3-java\
├── SKILL.md        — skill definition loaded by Claude (v1.3.0)
└── README.md       — this file
```

## Skill Sources

All content in `SKILL.md` is sourced exclusively from:
1. `Introduction to L3 Java Customisation.pdf` — Temenos Transact (Updated May 2023)
2. `T24 USER GUIDE TO L3 API - Version & Enquiry Routines.pdf` — Temenos (2020)
3. `CSD - Java Programming Standards.pdf` — Temenos CSD (v1.1, Aug 2022)
4. Real implementation Java files from JIB/AOAB bank projects (for code pattern examples)
