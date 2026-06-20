# JavaDoc Index — Key Class Documentation

> Manually curated 2026-06-20 from JAR analysis, L3 Java CSD standards, and T24 Technical Training.
> For the full 157-class API catalog, see [references/apis/java-api.md](../apis/java-api.md).
> For all 77,762 classes, see [references/classes/class-index.md](../classes/class-index.md).

---

## AA Framework Classes

### ActivityLifecycle

**JAR:** `AA_ActivityHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`

Superclass for all AA arrangement activity hooks. Override methods fire at specific points in the AA activity lifecycle.

| Method | Signature (key params) | When Called |
|--------|------------------------|-------------|
| `defaultFieldValues` | `(AaAccountDetailsRecord, AaArrangementActivityRecord, ArrangementContext, AaArrangementRecord, AaArrangementActivityRecord, TStructure, AaProductCatalogRecord, TStructure)` | Before activity screen is shown |
| `generateSecondaryActivity` | `(..., SecondaryActivity)` | After auth — triggers secondary AA activity |
| `postCoreTableUpdate` | `(..., List<TransactionData>, List<TStructure>)` | After auth and DB commit |
| `validateRecord` | `(...) → TValidationResponse` | On activity submit/commit |
| `updateLookupTable` | `(..., List<LookupData>) → TBoolean` | Post-auth — update concat files |
| `setElementData` | `(String, String, List<String>, ...) → void` | Set element-level data |
| `filterElements` | `(List<String>, String, String, String) → List<String>` | Filter available elements |
| `filterAccrualProperties` | `(String, AccrualContext, List<String>, List<String>) → void` | Filter accrual properties |

---

### Calculation

**JAR:** `AA_CalculationHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`

Superclass for AA calculation hooks (interest, charges, amounts).

| Method | When Called | Purpose |
|--------|------------|---------|
| `calculateSourceBalance` | During balance calculation | Compute source balance for interest |
| `calculatePayment` | Payment schedule evaluation | Compute payment amount → `TNumber` |
| `calculateUncSettledAmount` | Unsettled amount calc | Returns unsettled amount |
| `calculateCharge` | Charge evaluation | Compute charge/fee amount |
| `calculateAdjustedCharge` | Adjusted charge calc | Apply adjustments to base charge |
| `SortDrawingsArrangements` | Drawing order | Sort drawings for calculation |

---

### Bill

**JAR:** `AA_BillApi.jar`  **Package:** `com.temenos.t24.api.arrangement`

API for accessing AA bill (charge demand) records. Create a new Bill using a specific arrangement context.

| Method | Returns | Description |
|--------|---------|-------------|
| `setContractId(String)` | `void` | Set the arrangement ID |
| `getContractId()` | `String` | Get the arrangement ID |
| `setBillId(String)` | `void` | Set the bill ID |
| `getBillId()` | `String` | Get the bill ID |
| `getBillRecord()` | `AaBillDetailsRecord` | Retrieve the full bill details record |
| `getVersion()` | `String` | Component version string |
| `getBuildDate()` | `String` | Component build date |

---

### Contract

**JAR:** `AA_ContractApi.jar`  **Package:** `com.temenos.t24.api.arrangement.accounting`

Read-only API for accessing an arrangement's live property conditions. The primary API for ActivityLifecycle hooks to read arrangement data.

| Method | Returns | Description |
|--------|---------|-------------|
| `new Contract(this)` | `Contract` | Construct from hook context |
| `setContractId(String)` | `void` | Set the arrangement ID to query |
| `getConditionForProperty(String propertyId)` | `TStructure` | Get property record TStructure |
| `getPropertyIdsForPropertyClass(String className)` | `List<String>` | Get property IDs for a class name |
| `getCommitmentCondition(String)` | `TStructure` | Get commitment/term condition |

**Usage:**
```java
Contract contract = new Contract(this);
contract.setContractId(arrangementId);
TStructure interestStruct = contract.getConditionForProperty(
    contract.getPropertyIdsForPropertyClass("INTEREST").get(0));
AaPrdDesInterestRecord inter = new AaPrdDesInterestRecord(interestStruct);
```

---

## Core / EB.API Classes

### RecordLifecycle

**JAR:** `EB_API.jar`  **Package:** `com.temenos.t24.api.hook.system`

Superclass for transaction-level hooks on any T24 application.

| Method | Returns | When Called |
|--------|---------|-------------|
| `checkId(String, TransactionContext)` | `String` | On record ID entry — validate/transform ID |
| `defaultFieldValues(String, String, TStructure, TStructure, TStructure, TransactionContext)` | `void` | After record load, before user input |
| `validateField(String, String, String, TStructure, TStructure, TStructure, TransactionContext)` | `TValidationResponse` | On each field change |
| `checkRecord(String, String, TStructure, TStructure, TStructure, TransactionContext)` | `TValidationResponse` | Full record validation before commit |
| `updateRecord(String, String, TStructure, TStructure, TStructure, TransactionContext, List<TransactionData>, List<TStructure>)` | `void` | On AUTHORISE — create linked records |
| `postUpdateRequest(String, String, TStructure, List<TransactionData>, List<TStructure>, TransactionContext)` | `void` | After auth and DB commit |
| `updateCoreRecord(...)` | `void` | Override to write directly to T24 tables |

---

### ServiceLifecycle

**JAR:** `EB_API.jar`  **Package:** `com.temenos.t24.api.hook.system`

Superclass for batch service hooks (COB/EOD).

| Method | Returns | When Called |
|--------|---------|-------------|
| `getIds(ServiceData, List<String>)` | `List<String>` | At start — select IDs to process |
| `updateRecord(String, ServiceData, String, TransactionControl, List<SynchronousTransactionData>, List<TStructure>)` | `void` | Once per ID — process one record |
| `postUpdateRequest(String, ServiceData, String, List<TransactionData>, List<TStructure>)` | `void` | Post-authorise per record |

---

### Enquiry

**JAR:** `EB_API.jar`  **Package:** `com.temenos.t24.api.hook.system`

Superclass for NoFile/computed enquiry hooks.

| Method | Returns | When Called |
|--------|---------|-------------|
| `setIds(List<FilterCriteria>, EnquiryContext)` | `List<String>` | Compute enquiry result rows |
| `setValue(String, String, EnquiryContext)` | `String` | Compute a field value for a row |
| `setFilterCriteria(List<FilterCriteria>, EnquiryContext)` | `void` | Modify/validate filter criteria |

---

### DataAccess

**JAR:** `EB_API.jar` (runtime)  **Package:** `com.temenos.t24.api.system`

File I/O API for Java hooks. Use one instance per hook method call.

| Method | Returns | Description |
|--------|---------|-------------|
| `new DataAccess(this)` | `DataAccess` | Construct from hook context |
| `getRecord(String app, String id)` | `TStructure` | Read live record from current company |
| `getRecord(String company, String app, String suffix, String id)` | `TStructure` | Read with explicit company and suffix (`""`, `"$NAU"`, `"$HIS"`, `"$DEL"`) |
| `getHistoryRecord(String app, String id)` | `TStructure` | Read most recent history record |
| `selectRecords(String company, String app, String suffix, String criteria)` | `List<String>` | SELECT IDs matching criteria |
| `getRequestResponse(String reqId, boolean[] exists)` | `TStructure` | Read OFS.REQUEST.DETAILS response |
| `getCurrentDirectory()` | `String` | Current T24 runtime directory |

---

## Customer Classes

| Class | JAR | Key Methods |
|-------|-----|------------|
| `CustomerRecord` | `ST_Customer.jar` | `getShortName(int mv)`, `getName1()`, `getSector()`, `getNationality()`, `getResidence()`, `getRiskClass()`, `getLocalRefField(String)` |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `getCustomer(String id)`, `createCustomer(...)`, `getCustomerAccounts(String id)` |
| `CustomerServiceProxyAPI` | `t24-ST_CustomerService-t24service.jar` | Proxy wrapper for CustomerServiceAPI |

---

## Account Classes

| Class | JAR | Key Methods |
|-------|-----|------------|
| `AccountRecord` | `AC_API.jar` | `getAccountNumber()`, `getCurrency()`, `getCustomerId()`, `getWorkingBalance()`, `getClearedBalance()`, `getOnlineActualBal()` |
| `EbContractBalancesRecord` | (EB records JAR) | `getTypeSysdate(int)` → `TypeSysdateClass` with `getCurrAssetType()`, `getMatDate(int)` |

---

## Payment Classes

| Class | JAR | Key Methods |
|-------|-----|------------|
| `FundsTransferRecord` | `FT_*.jar` | `getDebitAcctNo()`, `getCreditAcctNo()`, `getDebitAmount()`, `getTransactionType()`, `getValueDate()`, `getPaymentDetails(int)` |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | Extends hook context for payment order — lifecycle methods same as RecordLifecycle |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | Lifecycle hook on PP.PAYMENT processing |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | Lifecycle hook on TP.PAYMENT.ORDER |

---

## Hook Interfaces

### RecordLifecycle

| Method | When | Typical Override |
|--------|------|-----------------|
| `checkId` | ID entry | Validate ID format, auto-append company code |
| `defaultFieldValues` | Before screen | Set today, company, calculated defaults |
| `validateField` | Field change | Real-time field validation |
| `checkRecord` | Pre-commit | Cross-field rules |
| `updateRecord` | AUTHORISE | Create FT, AA activity, or custom record |
| `postUpdateRequest` | Post-auth | Update external system, write custom table |

### ActivityLifecycle

| Method | When | Typical Override |
|--------|------|-----------------|
| `defaultFieldValues` | Before activity screen | Set payment amount, maturity date |
| `validateRecord` | Activity submit | Business rule validation |
| `postCoreTableUpdate` | Post-auth | Write custom table, trigger OFS, send notification |
| `generateSecondaryActivity` | Post-auth | Auto-rollover, follow-up activity |
| `updateLookupTable` | Post-auth | Maintain concat/lookup files |

---

## Utility Classes

| Class | JAR | Key Methods | Description |
|-------|-----|------------|-------------|
| `Session` | `EB_API.jar` | `getCurrentVariable("!TODAY")`, `getCompanyRecord()`, `getUser()` | Session context |
| `Date` (API) | (system JAR) | `addWorkingDays(String date, int days)`, `addMonths(String date, int months)`, `getToday()` | Date arithmetic |
| `EB.SystemTables` (jBC package) | (jBC) | `getToday()`, `getCompany()` | jBC session variables |
| `TValidationResponse` | `com.temenos.api` | `setError(String field, String code)`, `setOverride(...)` | Validation response builder |
| `TStructure` | `com.temenos.api` | `get(String fieldName)` → `TField`, `set(TStructure)` | Generic T24 record container |
| `TField` | `com.temenos.api` | `getValue()`, `setValue(String)`, `setError(String)`, `setOverride(String)` | Single field accessor |
| `TBoolean` | `com.temenos.api` | `TRUE`, `FALSE`, `isTrue()` | Boolean return type for hooks |

---

## TAFJ 'T' Types — TAFJClient.jar Classes

> Source: Transact Extensibility for Java — Lesson 4 (APIs, TAFJ and Complex Classes)

These classes are introduced by Temenos for Java developers and are available in `TAFJClient.jar` (located in `TAFJ/lib/`). The reason for the T Types is mutability — standard Java types like `String` are immutable.

### TStructure

**Package:** `com.temenos.api` (TAFJClient.jar)

A generic container type for records or complex type parameters. It maps Transact data to Java objects.

- TStructure is **not** used to access data directly — it is used to construct instances of records or complex types.
- Record classes (e.g. `FundsTransferRecord`) are instantiated from a TStructure.

```java
// Read a record into TStructure via DataAccess
TStructure ftStruct = da.getRecord("FUNDS.TRANSFER", "FT20010001234");
// Wrap in a typed record class
FundsTransferRecord ft = new FundsTransferRecord(ftStruct);
```

---

### TField

**Package:** `com.temenos.api` (TAFJClient.jar)

Every field in a T24 record is an internal type `TField` (not a plain String). TField provides getters and setters for field values, error messages, and enrichments.

| Method | Description |
|--------|-------------|
| `getValue()` | Get the field value as String |
| `setValue(String)` | Set the field value |
| `getError()` | Get the error message on this field |
| `setError(String)` | Set an error message on this field |
| `getEnrichment()` | Get the enrichment (description) for this field |
| `setEnrichment(String)` | Set enrichment text |

```java
TField f1 = ft.getDebitCurrency();   // get DEBIT.CURRENCY field
String ccy = f1.getValue();
// Set an error if currencies do not match
if (!debitCcy.equals(creditCcy)) {
    f1.setError("Debit and credit currency must match");
}
```

---

### TValidationResponse

**Package:** `com.temenos.api` (TAFJClient.jar)

Holds the validation response for any record. Returned from `validateField` and `checkRecord` hook methods.

```java
TValidationResponse resp = getValidationResponse();
TField f1 = ft.getDebitCurrency();
if (!debitCcy.equals(creditCcy)) {
    f1.setError("CURRENCY_MISMATCH");
    resp.setError(f1);
}
return resp;
```

---

### T24Context

**Package:** TAFJClient.jar

Encapsulates the current session. All Hook classes are instances of T24Context.

- API classes must be constructed using a `T24Context` (`this`) to ensure callbacks are made to the current session.
- `TAFJClient.jar` must be on the Java project classpath (from `TAFJ_HOME/lib`).

```java
DataAccess da = new DataAccess(this);   // "this" is the T24Context
```

---

### TransactionData

**Package:** `com.temenos.t24.api.complex.eb.servicehook`

Packages data required to post a transaction request in **asynchronous** mode. Used as a parameter in `updateRecord` and `postUpdateRequest` hook methods.

---

### SynchronousTransactionData

**Package:** `com.temenos.t24.api.complex.eb.servicehook`

Packages data required to post a transaction request in **synchronous** mode. Used in `ServiceLifecycle.updateRecord`.

---

### FilterCriteria

**Package:** `com.temenos.t24.api.complex.eb.enquiryhook`

Represents objects used for selection criteria in enquiry hooks.

- In T24 terms, corresponds to the `ENQ.DATA` variable used in `ENQUIRY BUILD.ROUTINE`s.
- Used in `Enquiry.setIds(List<FilterCriteria>, EnquiryContext)` and `setFilterCriteria(...)`.

```java
// In Enquiry hook
@Override
public List<String> setIds(List<FilterCriteria> criteria, EnquiryContext ctx) {
    for (FilterCriteria fc : criteria) {
        String field   = fc.getFieldname();
        String operand = fc.getOperand();
        String value   = fc.getValue();
        // build your ID list
    }
    return myIds;
}
```

---

## TAFJ Complex Classes

Complex classes are convenient groupings of related information that do not correspond to a single T24 record field. They are used for more complex in/out parameters (for example, an amount that combines a currency code and a numeric value).

> Example: An amount in T24 can be stored as `"USD250"` (currency embedded in value) or in separate fields `DEBIT.CURRENCY` / `DEBIT.AMOUNT`. A Complex Class models this grouping.

The values in a dynamic selection box of an ENQUIRY (field name, operand, value) are another example of related data held in a Complex Class: `com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria`.

Complex classes provide typed get/set methods rather than raw string manipulation of T24 dynamic arrays.

---

## Calling jBC Subroutines from Java (TAFJ)

> Source: "Calling jBC From Java L3 in Temenos Transact (TAFJ)" — Mahmudur Rahman

TAFJ provides two methods on `TAFJRuntime` to call jBC routines from Java L3 hooks.

### Obtain the Runtime

```java
TAFJRuntime runtime = TAFJRuntimeFactory.getTAFJRuntime(T24Context);
```

`T24Context` is `this` inside any hook class.

---

### callJBC() — No Return Value

Use `callJBC()` to call a jBC `SUBROUTINE` that has no return parameters.

```java
runtime.callJBC("CUS.FILE.GEN.SERVICE");
```

**Corresponding jBC subroutine:**
```basic
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

---

### invokeJBC() — With Return Parameters

Use `invokeJBC()` to call a jBC `SUBROUTINE` or `FUNCTION` that has input and output parameters.

```java
/* Prepare jVar input parameters */
jVarClient inOne   = jVarClientFactory.get("ABC");
jVarClient inTwo   = jVarClientFactory.get("500");
jVarClient inThree = jVarClientFactory.get("USD");

/* OUT parameters */
jVarClient out = jVarClientFactory.get();   // OUT<FM,VM,SM>
jVarClient err = jVarClientFactory.get();   // Error message

/* Call the jBC subroutine */
runtime.invokeJBC("FT.CUSTOM.CHECK", inOne, inTwo, inThree, out, err);
```

**Corresponding jBC subroutine:**
```basic
SUBROUTINE FT.CUSTOM.CHECK(IN1, IN2, IN3, OUTPUT, ERR_MESS)
* IN1, IN2, IN3  : input parameters
* OUTPUT         : output dynamic array (FM / VM / SM)
* ERR_MESS       : error message (if any)
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

---

### Reading Multi-Value Output (DynArray)

The `out` jVarClient contains a dynamic array using T24 field/value/sub-value separators (FM/VM/SM). Use helper methods to extract positions:

```java
String fm1_vm2_sm1 = getSM(out, 1, 2, 1);  // OUT<1,2,1>
String fm1_vm2_sm2 = getSM(out, 1, 2, 2);  // OUT<1,2,2>
String fm1_vm1_sm1 = getSM(out, 1, 1, 1);  // OUT<1,1,1>
String fm2_vm1     = getVM(out, 2, 1);      // OUT<2,1>
```

Where `getFM`, `getVM`, `getSM` are local helper methods that split the DynArray using FM, VM, SM separators.

---

### callJBC() vs invokeJBC() — Summary

| Method | Use For | Return Value | Parameter Type |
|--------|---------|--------------|----------------|
| `callJBC(name)` | `SUBROUTINE` with no return | None — executes logic only | N/A |
| `invokeJBC(name, ...)` | `SUBROUTINE` or `FUNCTION` with parameters | Supported via `jVarClient` OUT params | `jVarClient` (supports DynArray FM/VM/SM) |
