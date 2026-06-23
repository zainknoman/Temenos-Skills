---
name: temenos-l3-java
description: "Expert assistant for Temenos T24/Transact L3 Java customization development. Covers CSD coding standards, all superclasses (RecordLifecycle, ServiceLifecycle, Enquiry, ActivityLifecycle), all version routine types (ID, CheckRecord, AutoField, Validation, Input, BeforeAuth, Auth), enquiry routines (Build, Conversion, NoFile), full official API package/class/method reference, Core APIs (Amount, Date, Exchange Rate, Customer, Limit, Session, AA Contract), EB.API configuration, DataAccess, Contract API, LocalRef, and AA batch/ActivityLifecycle patterns. Triggers: 'L3 java', 'T24 customization', 'CSD standards', 'write a hook', 'RecordLifecycle', 'ServiceLifecycle', 'Enquiry', 'ActivityLifecycle', 'version routine', 'checkId', 'validateRecord', 'validateField', 'defaultFieldValues', 'postUpdateRequest', 'updateCoreRecord', 'generateSecondaryActivity', 'updateLookupTable', 'setFilterCriteria', 'setValue', 'setIds', 'EB.API', 'NOFILE enquiry', 'PaymentLifecycle', 'PaymentOrderLifecycle', 'DataAccess', 'Contract', 'LocalRefGroup', 'setError', 'isService', 'BigDecimal', 'getAvailableAmount', 'addWorkingDays', 'calculateRate'."
metadata:
  version: 1.5.0
---

# Temenos T24/Transact L3 Java Customization Expert

You are a Temenos T24/Transact L3 Java developer. You know every hook superclass, API pattern, and multivalue field idiom used in real bank customization projects.

---

## Architecture Overview

Temenos L3 Java customizations are deployed as Java classes that extend T24 hook superclasses. They are invoked by the T24 engine at defined lifecycle points. All field access goes through strongly-typed Record objects generated from the T24 data dictionary.

### Key Packages

| Package | Purpose |
|---|---|
| `com.temenos.t24.api.hook.system` | RecordLifecycle, ServiceLifecycle, Enquiry superclasses |
| `com.temenos.t24.api.hook.arrangement` | ActivityLifecycle superclass (AA arrangement hooks) |
| `com.temenos.api` | Core API types (TStructure, TField, TValidationResponse, LocalRef*) |
| `com.temenos.t24.api.complex.eb.templatehook` | RecordLifecycle context/transaction types |
| `com.temenos.t24.api.complex.eb.servicehook` | ServiceLifecycle types |
| `com.temenos.t24.api.complex.eb.enquiryhook` | Enquiry types |
| `com.temenos.t24.api.complex.aa.activityhook` | ActivityLifecycle types (ArrangementContext, TransactionData) |
| `com.temenos.t24.api.arrangement.accounting` | Contract — access arrangement property conditions |
| `com.temenos.t24.api.records.<app>` | Generated record classes per application |
| `com.temenos.t24.api.tables.<app>` | Generated table classes (direct write/delete) |
| `com.temenos.t24.api.system` | DataAccess, Session, Date utilities |

---

## Superclass 1: RecordLifecycle

**Use for:** Transaction-level hooks on any T24 application (CUSTOMER, ACCOUNT, LETTER.OF.CREDIT, FUNDS.TRANSFER, AA.ARRANGEMENT.ACTIVITY, custom apps, etc.)

```java
package com.temenos.t24;

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.<application>.<ApplicationRecord>;

public class MyHook extends RecordLifecycle {
    // Override only the methods you need
}
```

### RecordLifecycle Methods

#### `defaultFieldValues` — Set defaults before user sees screen
```java
@Override
public void defaultFieldValues(String application, String currentRecordId,
        TStructure currentRecord, TStructure unauthorisedRecord,
        TStructure liveRecord, TransactionContext transactionContext) {

    SomeRecord rec = new SomeRecord(currentRecord);
    rec.setSomeField("DEFAULT_VALUE");
    // Local ref field:
    try {
        rec.getLocalRefField("MY.FIELD").setValue("value");
    } catch (Exception e) {}
    currentRecord.set(rec.toStructure());
}
```

#### `validateRecord` — Validate and return errors/overrides
```java
@Override
public TValidationResponse validateRecord(String application, String currentRecordId,
        TStructure currentRecord, TStructure unauthorisedRecord,
        TStructure liveRecord, TransactionContext transactionContext) {

    SomeRecord rec = new SomeRecord(currentRecord);

    String fieldVal = rec.getSomeField().getValue();
    if (fieldVal.isEmpty()) {
        rec.getSomeField().setError("Field is mandatory");
    }

    // Override (soft warning):
    rec.getSomeOtherField().setOverride("OVERRIDE.MESSAGE.CODE");

    currentRecord.set(rec.toStructure());
    return rec.getValidationResponse();
}
```

#### `checkId` — Validate/transform record ID before load
Return value is the (possibly modified) record ID that T24 will use.
```java
@Override
public String checkId(String currentRecordId, TransactionContext transactionContext) {
    // Validate ID format:
    String[] parts = currentRecordId.split("\\.");
    if (parts.length < 2) {
        throw new com.temenos.api.exceptions.T24CoreException("", "EB-INVALID.ID");
    }
    return currentRecordId;
}
```

**Auto-generate a new record ID** (return a completely different ID — T24 uses whatever you return):
```java
@Override
public String checkId(String currentRecordId, TransactionContext transactionContext) {
    // Generate unique card number using epoch nanos:
    String prefix = currentRecordId.split("\\.")[0];
    long uniqueEpoch = (System.currentTimeMillis() * 10000) + (System.nanoTime() % 10000);
    return prefix + ".PC" + uniqueEpoch;
}
```

**Auto-append department code from Session:**
```java
@Override
public String checkId(String currentRecordId, TransactionContext transactionContext) {
    String[] parts = Arrays.copyOf(currentRecordId.split("\\."), 3);
    Session session = new Session(this);
    if (parts[2] == null) {
        currentRecordId += "." + session.getUserRecord().getDepartmentCode().getValue();
    }
    return currentRecordId;
}
```

#### `updateRecord` — Triggered on AUTHORISE, drives linked transactions
Uses `com.temenos.t24.api.complex.eb.templatehook.TransactionData`:
```java
@Override
public void updateRecord(String application, String currentRecordId,
        TStructure currentRecord, TStructure unauthorisedRecord,
        TStructure liveRecord, TransactionContext transactionContext,
        List<com.temenos.t24.api.complex.eb.templatehook.TransactionData> transactionData,
        List<TStructure> currentRecords) {

    SomeRecord rec = new SomeRecord(currentRecord);

    com.temenos.t24.api.complex.eb.templatehook.TransactionData txnData =
        new com.temenos.t24.api.complex.eb.templatehook.TransactionData();
    txnData.setVersionId("TARGET.APPLICATION,VERSION.NAME");
    txnData.setFunction("I");           // I=INPUT, A=AUTHORISE, R=REVERSE
    txnData.setNumberOfAuthoriser("0");
    txnData.setTransactionId("RECORD_ID");
    transactionData.add(txnData);

    // Build the target record
    OtherRecord target = new OtherRecord();
    target.setSomeField("value");
    currentRecords.add(target.toStructure());
}
```

#### `postUpdateRequest` — Post-commit, after authorisation
Uses `com.temenos.t24.api.complex.eb.servicehook.TransactionData`:
```java
@Override
public void postUpdateRequest(String application, String currentRecordId,
        TStructure currentRecord,
        List<com.temenos.t24.api.complex.eb.servicehook.TransactionData> transactionData,
        List<TStructure> currentRecords, TransactionContext transactionContext) {

    SomeRecord rec = new SomeRecord(currentRecord);

    com.temenos.t24.api.complex.eb.servicehook.TransactionData txnData =
        new com.temenos.t24.api.complex.eb.servicehook.TransactionData();
    txnData.setVersionId("TARGET.APPLICATION,AUTH.REC");
    txnData.setFunction("INPUT");
    txnData.setNumberOfAuthoriser("0");
    txnData.setSourceId("OFS.LOAD");
    transactionData.add(txnData);
    currentRecords.add(rec.toStructure());

    // Access build date from servicehook TransactionData:
    String buildDate = transactionData.get(0).getBuildDate();  // yyyyMMdd
}
```

#### `defaultFieldValuesOnHotField` — Fires when a hot field changes
Import: `com.temenos.t24.api.complex.eb.templatehook.InputValue`
```java
@Override
public void defaultFieldValuesOnHotField(String application, String currentRecordId,
        TStructure currentRecord, InputValue currentInputValue,
        TStructure unauthorisedRecord, TStructure liveRecord,
        TransactionContext transactionContext) {

    SomeRecord rec = new SomeRecord(currentRecord);
    try {
        String hotFieldVal = rec.getLocalRefField("HOT.FIELD").getValue();
        if (!hotFieldVal.isEmpty()) {
            DataAccess da = new DataAccess(this);
            OtherRecord other = new OtherRecord(da.getRecord("", "OTHER.APP", "", hotFieldVal));
            rec.setSomeField(other.getSomeField().getValue());
            currentRecord.set(rec.toStructure());
        }
    } catch (Exception e) {}
}
```

---

## Superclass 2: ServiceLifecycle

**Use for:** Background batch services (COB/EOD jobs, scheduled processing queues).

```java
package com.temenos.t24;

import java.util.List;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.servicehook.ServiceData;
import com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData;
import com.temenos.t24.api.complex.eb.servicehook.TransactionControl;
import com.temenos.t24.api.hook.system.ServiceLifecycle;
import com.temenos.t24.api.system.DataAccess;

public class MyBatch extends ServiceLifecycle {

    @Override
    public List<String> getIds(ServiceData serviceData, List<String> controlList) {
        DataAccess da = new DataAccess(this);
        // Select records to process
        return da.selectRecords("", "MY.APPLICATION", "", "WITH STATUS EQ 'PENDING'");
    }

    @Override
    public void updateRecord(String id, ServiceData serviceData, String controlItem,
            TransactionControl transactionControl,
            List<SynchronousTransactionData> transactionData, List<TStructure> records) {

        DataAccess da = new DataAccess(this);
        MyRecord rec = new MyRecord(da.getRecord("MY.APPLICATION", id));

        // Process...
        rec.setStatus("PROCESSED");

        SynchronousTransactionData txnData = new SynchronousTransactionData();
        txnData.setSourceId("OFS.LOAD");
        txnData.setVersionId("MY.APPLICATION,BATCH.VERSION");
        txnData.setFunction("I");
        txnData.setCompanyId(serviceData.getCompanyId());
        txnData.setNumberOfAuthoriser("0");
        txnData.setTransactionId(id);
        transactionData.add(txnData);
        records.add(rec.toStructure());
    }

    @Override
    public void postUpdateRequest(String id, ServiceData serviceData, String controlItem,
            List<com.temenos.t24.api.complex.eb.servicehook.TransactionData> transactionData,
            List<TStructure> records) {
        // Post-authorise actions
    }
}
```

---

## Superclass 3: Enquiry

**Use for:** Custom enquiry result sets with computed IDs or derived data.

```java
package com.temenos.t24;

import java.util.ArrayList;
import java.util.List;
import com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext;
import com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria;
import com.temenos.t24.api.hook.system.Enquiry;
import com.temenos.t24.api.system.DataAccess;

public class MyEnquiry extends Enquiry {

    @Override
    public List<String> setIds(List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {
        DataAccess da = new DataAccess(this);
        List<String> results = new ArrayList<>();

        // Read filter inputs (0-indexed)
        String param1 = filterCriteria.get(0).getValue();
        String param2 = filterCriteria.get(1).getValue();

        try {
            // Compute results and add as delimited strings
            // Each entry = one row; columns separated by agreed delimiter (e.g. "*")
            results.add(param1 + "*" + param2 + "*computed_value");
        } catch (Exception e) {
            // return empty on error
        }
        return results;
    }
}
```

---

## Superclass 4: ActivityLifecycle

**Use for:** Hooks on Arrangement Architecture (AA) activities — lending, deposits, savings lifecycle events. These fire when an AA arrangement activity is processed (new arrangement, update, close, renegotiate, etc.).

Key difference from RecordLifecycle: the `record` parameter is the **property record** currently in scope (e.g., `AaPrdDesPaymentScheduleRecord`, `AaPrdDesInterestRecord`), not the arrangement master record.

```java
package com.temenos.t24;

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.arrangement.accounting.Contract;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.activityhook.TransactionData;
import com.temenos.t24.api.hook.arrangement.ActivityLifecycle;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;
import com.temenos.t24.api.system.DataAccess;
import java.util.List;

public class MyActivityHook extends ActivityLifecycle {
    // Override only the methods you need
}
```

### ActivityLifecycle Methods

#### `defaultFieldValues` — Set defaults before user sees the activity screen
```java
@Override
public void defaultFieldValues(AaAccountDetailsRecord accountDetailRecord,
        AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
        AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
        TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record) {

    String arrangementId = arrangementActivityRecord.getArrangement().getValue();
    String activity = arrangementActivityRecord.getActivity().getValue();

    // Wrap the property record (matches what this hook is bound to in T24 config):
    AaPrdDesPaymentScheduleRecord paySchedule = new AaPrdDesPaymentScheduleRecord(record);

    try {
        // Read from the arrangement's conditions:
        Contract contract = new Contract(this);
        contract.setContractId(arrangementId);
        AaPrdDesTermAmountRecord termAmt = contract.getCommitmentCondition("COMMITMENT");
        String term = termAmt.getTerm().getValue();
        // ... compute and set fields ...
        paySchedule.getPaymentType().get(0)...;
    } catch (Exception e) {}

    record.set(paySchedule.toStructure()); // always commit property record back
}
```

**Alternate short signature** (some T24 versions use 6 params):
```java
public void defaultFieldValues(AaArrangementRecord arrangementRecord,
        AaArrangementActivityRecord arrangementActivityRecord,
        AaProductCatalogRecord productRecord, TStructure record,
        TStructure productPropertyRecord, ArrangementContext arrangementContext) {
    // same body
}
```

#### `validateRecord` — Validate activity input
Returns `TValidationResponse`. Chain to super to apply default platform validation.
```java
@Override
public TValidationResponse validateRecord(AaAccountDetailsRecord accountDetailRecord,
        AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
        AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
        TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record) {

    String activityName = arrangementActivityRecord.getActivity().getValue();
    String arrangement  = arrangementActivityRecord.getArrangement().getValue();
    DataAccess da = new DataAccess(this);

    if (activityName.equals("LENDING-UPDATE-PAYMENT.HOLIDAY")) {
        // Field-level error on a field of the activity record:
        arrangementActivityRecord.getCustomer(0).getCustomer()
            .setError("Payment Holiday not allowed");
        // Or throw hard stop:
        throw new com.temenos.api.exceptions.T24CoreException("", "ERROR.CODE");
    }

    // Chain to super:
    return super.validateRecord(accountDetailRecord, arrangementActivityRecord, arrangementContext,
            arrangementRecord, masterActivityRecord, productPropertyRecord, productRecord, record);
}
```

#### `postCoreTableUpdate` — After authorisation, DB is committed
Equivalent of `postUpdateRequest` in RecordLifecycle. Used for: writing custom tables, triggering OFS, computing calculated fields post-commit. Uses `com.temenos.t24.api.complex.aa.activityhook.TransactionData`.
```java
@Override
public void postCoreTableUpdate(AaAccountDetailsRecord accountDetailRecord,
        AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
        AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
        TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
        List<TransactionData> transactionData, List<TStructure> transactionRecord) {

    String status = arrangementContext.getActivityStatus().toString(); // "AUTH", "INAU"
    String arrangementId = arrangementContext.getArrangementId();

    if (status.equals("AUTH")) {
        // Read local ref fields from the property record:
        AaPrdDesAccountRecord accountObj = new AaPrdDesAccountRecord(record);
        String vibanId = accountObj.getLocalRefField("L.VIBAN.ID").getValue();

        // Write to a custom table:
        MyCustomTable tbl = new MyCustomTable(this);
        MyCustomRecord rec = new MyCustomRecord();
        rec.setMyField(vibanId);
        try {
            tbl.write(arrangementId, rec);
        } catch (Exception e) {}

        // Or trigger an OFS transaction:
        TransactionData txn = new TransactionData();
        txn.setVersionId("APPLICATION,VERSION");
        txn.setFunction("I");
        txn.setNumberOfAuthoriser("0");
        txn.setSourceId("OFS.LOAD");
        transactionData.add(txn);
        transactionRecord.add(someRec.toStructure());
    }
}
```

---

### Contract API — Accessing Arrangement Property Conditions

`Contract` is the central API for reading an arrangement's active conditions from within ActivityLifecycle hooks.

```java
Contract contract = new Contract(this);
contract.setContractId(arrangementId);

// Get condition TStructure for a specific property name:
TStructure acStructure = contract.getConditionForProperty("ACCOUNT");
AaPrdDesAccountRecord acRec = new AaPrdDesAccountRecord(acStructure);

// Get property IDs by class name (returns list — use index 0 for first):
String propId = contract.getPropertyIdsForPropertyClass("PAYMENT.SCHEDULE").get(0);
TStructure schedStructure = contract.getConditionForProperty(propId);
AaPrdDesPaymentScheduleRecord sched = new AaPrdDesPaymentScheduleRecord(schedStructure);

// Get commitment condition:
AaPrdDesTermAmountRecord termAmt = contract.getCommitmentCondition("COMMITMENT");
String term = termAmt.getTerm().getValue();  // e.g. "24M", "2Y"

// Get interest condition by property class:
String interestPropId = contract.getPropertyIdsForPropertyClass("INTEREST").get(0);
AaPrdDesInterestRecord inter = new AaPrdDesInterestRecord(contract.getConditionForProperty(interestPropId));
```

---

### AA Property Record Classes

These wrap `record` (or a TStructure from Contract) to access property-specific fields:

#### AaPrdDesPaymentScheduleRecord
```java
import com.temenos.t24.api.records.aaprddespaymentschedule.AaPrdDesPaymentScheduleRecord;
import com.temenos.t24.api.records.aaprddespaymentschedule.PaymentTypeClass;
import com.temenos.t24.api.records.aaprddespaymentschedule.PercentageClass;

AaPrdDesPaymentScheduleRecord paySchedule = new AaPrdDesPaymentScheduleRecord(record);
List<PaymentTypeClass> payTypes = paySchedule.getPaymentType();

// Access a payment type:
PaymentTypeClass payType = (PaymentTypeClass) paySchedule.getPaymentType().get(0);
String pymtType = payType.getPaymentType().getValue(); // e.g. "DEPOSIT.SAVINGS"

// Set percentage end/start date:
PercentageClass pct = new PercentageClass();
pct.setEndDate("20241231");
pct.setStartDate("20240101");
payType.setPercentage(pct, 0);  // index 0

// Set actual amount:
PercentageClass pct2 = new PercentageClass();
pct2.getActualAmt().setValue("500.00");

// Clear and add:
payType.clearPercentage();
payType.addPercentage(pct2);

record.set(paySchedule.toStructure());
```

#### AaPrdDesTermAmountRecord
```java
import com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord;

AaPrdDesTermAmountRecord termRec = new AaPrdDesTermAmountRecord(record);
String term = termRec.getTerm().getValue();           // "24M" or "2Y"
String matDate = termRec.getMaturityDate().getValue();
termRec.setTerm("12M");
termRec.setMaturityDate("");
// Local ref:
String rollIns = termRec.getLocalRefField("OHB.L.ROLL.INS").getValue();
termRec.getLocalRefField("OHB.L.TERM.MAT").setValue(term);

record.set(termRec.toStructure());
```

**Parsing term string (e.g. "24M", "2Y"):**
```java
String termNum    = term.substring(0, term.length() - 1);  // "24"
String termMarker = term.substring(term.length() - 1);     // "M" or "Y"
int numPayments = termMarker.equals("Y") ? 12 * Integer.parseInt(termNum)
                                        : Integer.parseInt(termNum);
```

#### AaPrdDesInterestRecord
```java
import com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord;
import com.temenos.t24.api.records.aaprddesinterest.FixedRateClass;

AaPrdDesInterestRecord inter = new AaPrdDesInterestRecord(record);
FixedRateClass fixedRate = new FixedRateClass();
fixedRate.setFixedRate("5.5");
inter.setFixedRate(fixedRate, 0);
record.set(inter.toStructure());
```

#### AaArrPaymentScheduleRecord — Live Payment Schedule (vs AaPrdDesPaymentScheduleRecord)
`AaPrdDesPaymentScheduleRecord` = design-time (entered on screen).  
`AaArrPaymentScheduleRecord` = live/running schedule retrieved via `Contract.getConditionForProperty()`.
```java
import com.temenos.t24.api.records.aaarrpaymentschedule.AaArrPaymentScheduleRecord;

String propId = contract.getPropertyIdsForPropertyClass("PAYMENT.SCHEDULE").get(0);
TStructure schedStructure = contract.getConditionForProperty(propId);
AaArrPaymentScheduleRecord liveSched = new AaArrPaymentScheduleRecord(schedStructure);
String numPayments = liveSched.getPaymentType().get(0).getPercentage().get(0).getNumPayments().getValue();
```

#### AaBillDetailsRecord — Reading AA.BILL.DETAILS
Use the generated record class — **never use `da.getFieldValue()` for field reads**.
```java
import com.temenos.t24.api.records.aabilldetails.AaBillDetailsRecord;

// Correct way to read bill fields:
AaBillDetailsRecord billDtlRec = new AaBillDetailsRecord(da.getRecord("AA.BILL.DETAILS", billId));
String property  = billDtlRec.getProperty().getValue();       // maps to PROPERTY field
String payDate   = billDtlRec.getPaymentDate().getValue();    // maps to PAYMENT.DATE
String payAmtStr = billDtlRec.getPaymentAmount().getValue();  // maps to PAYMENT.AMOUNT
BigDecimal payAmt = payAmtStr.isEmpty() ? BigDecimal.ZERO : new BigDecimal(payAmtStr);
```

#### AaArrTermAmountRecord — Live/Running Condition (vs AaPrdDesTermAmountRecord)
`AaPrdDesTermAmountRecord` = **design-time** product condition (what the user enters on screen).
`AaArrTermAmountRecord` = **live/running** condition after booking (actual values in effect).
```java
import com.temenos.t24.api.records.aaarrtermamount.AaArrTermAmountRecord;

// Read the live (running) term amount for a booked arrangement:
AaArrTermAmountRecord arrTermRec = new AaArrTermAmountRecord(record);
String term = arrTermRec.getTerm().toString();  // e.g. "24M"

// From Contract API (live condition):
AaArrTermAmountRecord liveTerm = contract.getCommitmentCondition("COMMITMENT");
// Note: contract.getCommitmentCondition() returns AaArrTermAmountRecord in the live AA context
```

#### AaPrdDesDormancyRecord
```java
import com.temenos.t24.api.records.aaprddesdormancy.AaPrdDesDormancyRecord;
import com.temenos.t24.api.records.aaprddesdormancy.StatusClass;

AaPrdDesDormancyRecord dormRec = new AaPrdDesDormancyRecord(record);
List<StatusClass> statusList = dormRec.getStatus();
for (int i = 0; i < statusList.size(); i++) {
    String statusVal = statusList.get(i).getStatus().getValue();
    String period    = statusList.get(i).getPeriod().getValue();
    if ("Abandoned".equalsIgnoreCase(statusVal)) {
        statusList.get(i).setPeriod("365D");
        dormRec.setStatus(statusList.get(i), i);
    }
}
record.set(dormRec.toStructure());
```

#### AaPrdDesLimitRecord
```java
import com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord;

AaPrdDesLimitRecord limitRec = new AaPrdDesLimitRecord(da.getRecord("AA.PRD.DES.LIMIT", propId));
// Or query by arrangement ID pattern:
List<String> limitIds = da.selectRecords("", "AA.PRD.DES.LIMIT", "", "WITH @ID LIKE " + arrangementId + "...");
```

#### AaPrdDesChargeRecord
```java
import com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord;

AaPrdDesChargeRecord chargeRecord = new AaPrdDesChargeRecord(record);
String insPer    = chargeRecord.getLocalRefField("L.INS.PERC").getValue();
String disbComp  = chargeRecord.getLocalRefField("L.DISB.COMP").getValue();
chargeRecord.setFixedAmount("1250.00");
record.set(chargeRecord.toStructure());
```

#### AaPrdDesAccountRecord (as property)
```java
import com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord;

AaPrdDesAccountRecord acctRec = new AaPrdDesAccountRecord(record);
String acctRef  = acctRec.getAccountReference().getValue();
String agreement = acctRec.getLocalRefField("JO.AGREEMENT").getValue();
String consEnd  = acctRec.getLocalRefField("OHB.L.CONS.END").getValue();
```

#### AaPrdDesBalanceMaintenanceRecord + AaArrBalanceMaintenanceRecord
```java
import com.temenos.t24.api.records.aaprddesbalancemaintenance.AaPrdDesBalanceMaintenanceRecord;
import com.temenos.t24.api.records.aaarrbalancemaintenance.*;

AaArrBalanceMaintenanceRecord aaBalMaint = new AaArrBalanceMaintenanceRecord(record);

// Iterate bill references and outstanding amounts:
List<BillRefClass> bills = aaBalMaint.getBillRef();
double total = 0.0;
for (int i = 0; i < bills.size(); i++) {
    List<PropertyClass> props = bills.get(i).getProperty();
    for (int j = 0; j < props.size(); j++) {
        double amt = Double.parseDouble(props.get(j).getOsPropAmt().getValue());
        total += amt;
        aaBalMaint.getBillRef().get(i).getProperty(j).getNewPropAmt().setValue("0");
    }
}

// Set adjustment amount for a balance type:
List<AdjustPropClass> adjProps = aaBalMaint.getAdjustProp();
for (int k = 0; k < adjProps.size(); k++) {
    List<AdjBalTypeClass> adjBalTypes = adjProps.get(k).getAdjBalType();
    for (int l = 0; l < adjBalTypes.size(); l++) {
        if (adjBalTypes.get(l).getAdjBalType().getValue().equals("CURACCOUNT")) {
            aaBalMaint.getAdjustProp().get(k).getAdjBalType(l).getAdjBalAmt().setValue(String.valueOf(total));
        }
    }
}
record.set(aaBalMaint.toStructure());
```

---

### ArrangementContext API
```java
String arrangementId = arrangementContext.getArrangementId();      // String (not TField)
String status = arrangementContext.getActivityStatus().toString(); // "AUTH", "INAU", "IHLD"
```

---

### AaArrangementActivityRecord — Key Fields
```java
String arrangementId = arrangementActivityRecord.getArrangement().getValue();
String activity      = arrangementActivityRecord.getActivity().getValue();    // "LENDING-NEW-ARRANGEMENT"
String product       = arrangementActivityRecord.getProduct().getValue();
String currency      = arrangementActivityRecord.getCurrency().getValue();
// getEffectiveDate() returns a TDate — use either .getValue() or .toString() (both return YYYYMMDD):
String effDate       = arrangementActivityRecord.getEffectiveDate().getValue();  // preferred
// String effDate    = arrangementActivityRecord.getEffectiveDate().toString();   // also works
String commodity     = arrangementActivityRecord.getLocalRefField("IS.PRODUCT").getValue();

// Customers (MV):
List<CustomerClass> cusList = arrangementActivityRecord.getCustomer();
String custNo = arrangementActivityRecord.getCustomer(0).getCustomer().getValue();

// Linked applications:
String accountNum = arrangementRecord.getLinkedAppl(0).getLinkedApplId().toString();

// Set error on the activity field:
arrangementActivityRecord.getActivity().setError("EB-SOME.ERROR.CODE");
// Set error on a customer field:
arrangementActivityRecord.getCustomer(0).getCustomer().setError("SOME.ERROR.CODE");
```

---

### AaAccountDetailsRecord — Arrangement Status
```java
AaAccountDetailsRecord acctDet = new AaAccountDetailsRecord(da.getRecord("AA.ACCOUNT.DETAILS", arrangementId));
String ageStatus = acctDet.getArrAgeStatus().getValue(); // "PERFORMING", "NON-PERFORMING", etc.
```

---

### AA Activity History — Counting Past Activities
```java
import com.temenos.t24.api.records.aaactivityhistory.*;

AaActivityHistoryRecord actHist = new AaActivityHistoryRecord(da.getRecord("AA.ACTIVITY.HISTORY", arrangementId));
int count = 0;
for (EffectiveDateClass effDateEntry : actHist.getEffectiveDate()) {
    for (ActivityRefClass actRef : effDateEntry.getActivityRef()) {
        if (actRef.getActivity().getValue().equals(targetActivityName)) {
            count++;
        }
    }
}
```

---

### EB.CONTRACT.BALANCES — Reading Balance Types
```java
import com.temenos.t24.api.records.ebcontractbalances.*;

EbContractBalancesRecord ecb = new EbContractBalancesRecord(
    da.getRecord("", "EB.CONTRACT.BALANCES", "", accountNum));

for (int i = 0; i < ecb.getTypeSysdate().size(); i++) {
    String type = ecb.getTypeSysdate(i).getCurrAssetType().toString();
    if (type.equals("CURACCOUNT")) {
        String amt = ecb.getTypeSysdate(i).getMatDate(0).getDebitMvmt().getValue();
    }
    if (type.equals("TOTCOMMITMENT")) { /* ... */ }
    if (type.equals("DEFEREDPFT"))    { /* ... */ }
}
```

---

#### `updateLookupTable` — Update concat files post-action
T24 POST.ROUTINE. Invoker: `AA.UPDATE.LOOKUP.TABLE.INVOKER`. Returns `boolean` — `true` if update needed.
```java
@Override
public boolean updateLookupTable(AaAccountDetailsRecord accountDetailRecord,
        AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
        AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
        TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
        List<LookupData> lookupDataList) {

    if (needsUpdate) {
        LookupData element = new LookupData();
        // Set table name, key, sorting order, entry to add/delete
        lookupDataList.set(0, element);
        return true;
    }
    return false;
}
```

#### `generateSecondaryActivity` — Generate a secondary AA activity post-commit
T24 POST.ROUTINE. Invoker: `AA.GENERATE.SECONDARY.ACTIVITY.INVOKER`. Only fires if all values are set.
```java
@Override
public void generateSecondaryActivity(AaAccountDetailsRecord accountDetailRecord,
        AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
        AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
        TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
        SecondaryActivity secondaryActivity) {

    // Properties separated by VM marker; property and field name separated by SM marker
    secondaryActivity.setActivity("LENDING-UPDATE-RATE");
    secondaryActivity.setProperty("INTEREST");
    secondaryActivity.setFieldName("FIXED.RATE");
    secondaryActivity.setFieldValue("5.5");
    // All values must be set for secondary activity to be generated
}
```

### Table Write Pattern in postCoreTableUpdate
```java
MyCustomTable tbl = new MyCustomTable(this);
MyCustomRecord rec = tbl.read(arrangementId);  // read existing
rec.setStatus("CLOSED");
tbl.write(arrangementId, rec);                 // write back
// Or write new:
MyCustomRecord newRec = new MyCustomRecord();
newRec.setStatus("OPEN");
tbl.write(arrangementId, newRec);
```

---

### Session in ActivityLifecycle
```java
Session session = new Session(this);
String today       = session.getCurrentVariable("!TODAY");
CompanyRecord comp = session.getCompanyRecord();
String mnemonic    = comp.getFinancialMne().getValue();
```

---

### ActivityLifecycle: Common Activity Names
```
LENDING-NEW-ARRANGEMENT
LENDING-CHANGE-DEFERPFT
LENDING-UPDATE-PAYMENT.HOLIDAY
LENDING-RENEGOTIATE-ARRANGEMENT
DEPOSITS-NEW-ARRANGEMENT
DEPOSITS-SALARY.CR-ARRANGEMENT
DEPOSITS-CLOSE-ARRANGEMENT
DEPOSITS-UPDATE-PO.WITHDRAWAL
ACCOUNTS-UPDATE-BALANCE
```

---

### ActivityLifecycle: Code Generation Rules

1. **`record` is a property record**, not the arrangement record. Wrap it with the property-specific class matching what this hook is bound to in T24.
2. **Always commit**: `record.set(propRec.toStructure())` — same as RecordLifecycle's `currentRecord.set(...)`.
3. **`TransactionData` import**: `com.temenos.t24.api.complex.aa.activityhook.TransactionData` — different from all RecordLifecycle/ServiceLifecycle variants.
4. **`postCoreTableUpdate`** is the AA equivalent of `postUpdateRequest` — runs after authorisation and DB commit.
5. **Conditional `record.set`**: Only call `record.set(...)` when you actually modified the property record. Some files skip it when no changes were made to avoid side effects.
6. **`arrangementContext.getArrangementId()`** returns a `String` directly, not a `TField` — no `.getValue()` needed.
7. **`getActivity().setError()`** sets the error on the activity field of the `arrangementActivityRecord`, which stops the activity.
8. **Multiple property records from one `record`**: You can wrap the same `record` TStructure in multiple record classes (e.g., both `AaPrdDesBalanceMaintenanceRecord` and `AaArrBalanceMaintenanceRecord`) and call `record.set()` for each — last write wins per field.

---

## TransactionContext API

Available on all RecordLifecycle methods as the `transactionContext` parameter:

```java
// Current function (INPUT, AUTH, DELETE, REVERSE, REAUTH):
String function = transactionContext.getCurrentFunction().toString();
// Conditionally apply logic:
if (function.equals("AUTH")) { /* auth-only logic */ }
if (function.equals("INPUT")) { /* input-only logic */ }
if (function.equals("DELETE")) { /* delete-only logic */ }

// Current version ID (e.g. "CUSTOMER,JIB.OFS.UPDATE"):
String versionId = transactionContext.getCurrentVersionId();
if (versionId.contains("DECISION")) { /* version-specific logic */ }
```

---

## DataAccess — File Handling

Declare one `DataAccess` instance in the parent hook method; pass it to sub-methods. Do not re-create it in every sub-method.

```java
DataAccess da = new DataAccess(this);

// Read from live table of current company:
SomeRecord rec = new SomeRecord(da.getRecord("APPLICATION.NAME", "RECORD_ID"));

// Read history directly with $HIS suffix in 2-arg form:
SomeRecord hist2 = new SomeRecord(da.getRecord("APPLICATION.NAME$HIS", "RECORD_ID;1"));
// Or with explicit company mnemonic and file suffix (4-arg form):
// fileSuffix: "" = live, "$NAU" = unauthorised, "$HIS" = history, "$SIM" = simulation, "$DEL" = deleted
SomeRecord rec2 = new SomeRecord(da.getRecord("BNK", "APPLICATION.NAME", "", "RECORD_ID"));
SomeRecord rNau = new SomeRecord(da.getRecord("BNK", "APPLICATION.NAME", "$NAU", "RECORD_ID"));

// da.getRecord() can return null — check before wrapping in a record class:
TStructure rawRec = da.getRecord("EB.JIB.GOAML.TXN.LIST", txnPurpose);
if (rawRec == null) return;
SomeRecord typedRec = new SomeRecord(rawRec);

// Read from history table (most recent history record):
SomeRecord hist = new SomeRecord(da.getHistoryRecord("APPLICATION.NAME", "RECORD_ID"));

// Get OFS response from OFS.REQUEST.DETAILS table:
TStructure ordRec = da.getRequestResponse(requestDetailId, exists);

// Select IDs matching criteria:
List<String> ids = da.selectRecords("", "APPLICATION.NAME", "", "WITH FIELD EQ 'VALUE'");
// With company prefix (e.g. for multi-company):
List<String> ids2 = da.selectRecords("BNK", "CARD.ISSUE", "", "WITH STATUS EQ 'ACTIVE'");

// Cross-reference lookup — get related record IDs from concat file:
List<String> accountIds = da.getConcatValues("CUSTOMER.ACCOUNT", customerId);
for (String accountId : accountIds) {
    AccountRecord accRec = new AccountRecord(da.getRecord("ACCOUNT", accountId));
    // ...
}

// 3-arg getFieldValue — read arbitrary field from a TStructure you already fetched:
// Use ONLY when you don't have (or can't use) the generated getter.
// The TStructure must have been fetched from the same app.
TStructure cusRec = da.getRecord("", "CUSTOMER", "", customerId);
String fieldVal = da.getFieldValue("CUSTOMER", "SHORT.NAME", cusRec).getValue();

// Get current T24 runtime directory:
String dir = da.getCurrentDirectory();
```

### Table Direct Write/Delete/Release
```java
MyAppTable tbl = new MyAppTable(this);
MyAppRecord rec = new MyAppRecord();
rec.setMyField("value");
tbl.write("RECORD_ID", rec);
tbl.delete("RECORD_ID");

// Release lock on a data file:
tbl.release("RECORD_ID");
```

---

## Session Utilities

Declare one `Session` instance in the parent hook method; reuse in sub-methods.

```java
import com.temenos.t24.api.system.Session;

Session session = new Session(this);

// Company:
String companyId   = session.getCompanyId();
CompanyRecord comp = session.getCompanyRecord();
String localCcy    = session.getLocalCurrency();
String compMne     = comp.getFinancialMne().getValue();

// User:
String userId      = session.getUserId();            // OPERATOR common variable
String userLang    = session.getUserLanguage();
UserRecord userRec = session.getUserRecord();
String deptCode    = userRec.getDepartmentCode().getValue();
String today       = session.getCurrentVariable("!TODAY");
List<String> roles = session.getUserRoles();
List<String> overrideClasses = session.getUserOverrideClass();

// System state:
String onlineStatus = session.getOnlineStatus(); // "ONLINE", "BATCH", "RECOVERY"
boolean isInstalled = session.isProductInstalled("AA");

// Cache operations:
session.clearLookupCache();
TStructure cachedRec = session.getCachedRecord("APPLICATION", "RECORD_ID");

// Publish:
session.publishMessage(interfaceId, record, response);

// Route to another version after current record commits:
// setNextVersion(versionId, function, recordId, generateId)
TBoolean generateId = new TBoolean();
generateId.set(false);
session.setNextVersion("TARGET.VERSION,FUNC", "INPUT", currentRecordId, generateId);
// generateId.set(true) = T24 auto-generates the record ID for the next version

// Delete a current variable:
session.deleteCurrentVariable("!MYVAR");
```

### isService() — COB/Batch Guard
Use in ActivityLifecycle or RecordLifecycle when an update must not run during COB:
```java
// Returns true if running under TSA.SERVICE (COB/batch)
if (isService()) {
    return; // stop execution during COB
}
```
AA COB jobs go through AA.ARRANGEMENT.ACTIVITY via OFS; `isService()` lets you distinguish online vs. COB execution.

---

## Date API

```java
import com.temenos.t24.api.system.Date;

Date date = new Date(this);  // standard hook context
// or no-arg constructor when used as a class-level field (also seen in real code):
// Date date = new Date();  — works but loses hook context; use new Date(this) inside methods

// Get today's date (T24 business date, not system clock):
String today = date.getDates().getToday().getValue();  // YYYYMMDD — preferred; uses T24 business date

// Add/subtract working days (equivalent to CDT in JBC):
String resultDate = date.addWorkingDays(inDate, inOffsetDays);

// Count working days between two dates (equivalent to CDD in JBC):
int workingDays = date.getWorkingDayDifference(startDate, endDate);

// Count calendar months between two dates:
int months = date.getMonthDifference(startDate, endDate);

// Date format conversions:
String julian     = date.gregorianToJulian(gregorianDate);  // YYYYMMDD → YYYYDDD
String gregorian  = date.julianToGregorian(julianDate);      // YYYYDDD → YYYYMMDD

// Check if date is holiday or working day (calls AWD core routine):
String dayType = date.getDayType(dateVal); // "HOLIDAY" or "WORKING.DAY"

// Add days/months/years (Java LocalDate style):
LocalDate d = LocalDate.parse(dateStr, DateTimeFormatter.ofPattern("yyyyMMdd"));
String newDate = d.plusDays(n).format(DateTimeFormatter.ofPattern("yyyyMMdd"));
// also: d.plusMonths(n), d.plusYears(n)

// Add frequency (cycle dates, like CFQ in JBC):
date.addFrequency(dateVal, frequency);
```

---

## LocalRef — MultiValue and SubValue Fields

T24 local ref fields support multivalue (MV) sets. Use `LocalRefList` + `LocalRefGroup`:

```java
import com.temenos.api.LocalRefGroup;
import com.temenos.api.LocalRefList;
import com.temenos.api.LocalRefClass;

// Read MV list:
LocalRefList mvList = cusRec.getLocalRefGroups("MY.FIELD");
int size = mvList.size();

// Iterate and validate:
for (int i = 0; i < size; i++) {
    try {
        String val = mvList.get(i).getLocalRefField("MY.FIELD").getValue();
        if (val.isEmpty()) {
            LocalRefGroup grp = cusRec.createLocalRefGroup("MY.FIELD");
            grp.getLocalRefField("MY.FIELD").setError("MY.FIELD is mandatory");
            mvList.set(i, grp);   // update existing row
        }
    } catch (Exception e) {}
}

// Add a new MV row:
LocalRefGroup newGrp = cusRec.createLocalRefGroup("MY.FIELD");
newGrp.getLocalRefField("MY.FIELD").setValue("value");
cusRec.getLocalRefGroups("MY.FIELD").add(size, newGrp);

// Single local ref field (not MV):
String val = rec.getLocalRefField("SINGLE.FIELD").getValue();
rec.getLocalRefField("SINGLE.FIELD").setValue("new value");
rec.getLocalRefField("SINGLE.FIELD").setError("Error message");

// LocalRefClass (raw multi-occurrence — read all values of a local ref field):
// Use getLocalRef(), NOT getLocalRefGroups(), for simple repeating local ref fields
LocalRefClass localRef = rec.getLocalRef("L.FIELD");
localRef.add("value");                       // append a new value
String contains = localRef.toString();       // all values as string for .contains() check
int count = localRef.get().size();           // number of values
String val = localRef.get(0).toString();     // first value as string
// Can also call on arrangementActivityRecord:
LocalRefClass odClose = arrangementActivityRecord.getLocalRef("L.OD.CLOSE");
String firstVal = odClose.size() > 0 ? odClose.get(0).toString() : "";
```

### LocalRefGroup error in validateRecord (multi-field group pattern)
When a LocalRefGroup has multiple sub-fields and you need to set an error on one:
```java
// 1. Get the list
LocalRefList grpList = cusRec.getLocalRefGroups("NAME.3");
int listSize = grpList.size();

try {
    for (int i = 0; i <= listSize; i++) {  // note: <= to cover empty list case
        String val = "";
        try { val = grpList.get(i).getLocalRefField("NAME.3").getValue(); } catch (Exception e) {}

        if (val.isEmpty()) {
            // Create a new group, set error, then add or replace:
            LocalRefGroup grp = cusRec.createLocalRefGroup("NAME.3");
            grp.getLocalRefField("NAME.3").setError("NAME.3 is mandatory");
            if (listSize <= 0) {
                cusRec.getLocalRefGroups("NAME.3").add(i, grp);   // no existing row → add
            } else {
                cusRec.getLocalRefGroups("NAME.3").set(i, grp);   // row exists → replace
            }
            currentRecord.set(cusRec.toStructure());
            return cusRec.getValidationResponse();
        }
    }
} catch (Exception e) {}
```

**IMPORTANT:** Always wrap LocalRef operations in try-catch. The field may not exist on older records.

---

---

## Triggering Linked Transactions (OFS)

### From updateRecord (RecordLifecycle):
```java
import com.temenos.t24.api.complex.eb.templatehook.TransactionData;

TransactionData txn = new TransactionData();
txn.setVersionId("APPLICATION,VERSION.CODE");
txn.setFunction("I");               // I, A, R, D
txn.setTransactionId("ID");
txn.setNumberOfAuthoriser("0");
txn.setSourceId("OFS.LOAD");
transactionData.add(txn);
currentRecords.add(targetRec.toStructure());
```

### From postUpdateRequest (RecordLifecycle or ServiceLifecycle):
```java
import com.temenos.t24.api.complex.eb.servicehook.TransactionData;

TransactionData txn = new TransactionData();
txn.setVersionId("APPLICATION,VERSION.CODE");
txn.setFunction("INPUTT");
txn.setNumberOfAuthoriser("0");
txn.setSourceId("BUILD.CONTROL");
transactionData.add(txn);
records.add(rec.toStructure());
```

### SynchronousTransactionData (ServiceLifecycle updateRecord):
```java
import com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData;

SynchronousTransactionData txn = new SynchronousTransactionData();
txn.setVersionId("APPLICATION,VERSION");
txn.setFunction("I");
txn.setCompanyId("COMPANYID");
txn.setNumberOfAuthoriser("0");
txn.setTransactionId("ID");
transactionData.add(txn);
records.add(rec.toStructure());
```

---

## Error Handling in Hooks

```java
import com.temenos.api.exceptions.T24CoreException;
import com.temenos.api.exceptions.T24IOException;  // for table write failures

// Throw a T24 error with an EB.ERROR code (preferred — CSD compliant):
throw new T24CoreException("", "EB-CSD.SOME.ERROR.CODE");

// Single-arg form — for dynamic error messages built at runtime:
throw new T24CoreException("Invalid account: " + accountId);
throw new T24CoreException("Amount " + amount + " exceeds daily limit");

// Field-level error (shows on screen, blocks save):
rec.getSomeField().setError("Human readable message or ERROR.CODE");

// Field-level override (shows warning, user can confirm):
rec.getSomeField().setOverride("OVERRIDE.CODE");

// Safe field access — guard against null when field may not exist:
import java.util.Optional;
String val = Optional.ofNullable(rec.getSomeField().getValue()).orElse("");

// Table write may throw T24IOException — catch specifically:
try {
    myTable.write(recordId, myRec);
} catch (T24IOException e) {
    // table write failed — log and continue or re-throw
}
```

## Logging Pattern

```java
import java.util.logging.Logger;
import java.util.logging.Level;

// Declare logger as a class-level field:
private Logger m_logger = Logger.getLogger(MyHookClass.class.getName());

// Usage:
m_logger.log(Level.INFO, "Processing arrangement: " + arrangementId);
m_logger.log(Level.SEVERE, "Exception occurred: " + e.getMessage());

// Optional: file logging (use T24 server path accessible at runtime):
import java.util.logging.FileHandler;
import java.util.logging.SimpleFormatter;
// FileHandler setup only if file path is known and writable — wrap in try-catch IOException
```

**Note:** `System.out.println()` is visible in T24 TAFJ logs but is discouraged in production (CSD rule). Use Logger in production code.

---

## Common Record Access Patterns

### Customer Record
```java
import com.temenos.t24.api.records.customer.CustomerRecord;

CustomerRecord cusRec = new CustomerRecord(currentRecord);
String nationality = cusRec.getNationality().getValue();
String addressType = cusRec.getAddressType().getValue();
String addressCountry = cusRec.getAddressCountry().getValue();
String gender = cusRec.getGender().getValue();
String dob = cusRec.getDateOfBirth().getValue();
String maritalStatus = cusRec.getMaritalStatus().getValue();
String residence = cusRec.getResidence().getValue();
String birthIncorpDate = cusRec.getBirthIncorpDate().getValue();
List<TField> postingRestricts = cusRec.getPostingRestrict();
cusRec.setPostingRestrict("POSTING.CODE", index);
// local ref:
String customField = cusRec.getLocalRefField("CUST.FIELD").getValue();
```

### Account Record
```java
import com.temenos.t24.api.records.account.AccountRecord;
import com.temenos.t24.api.party.Account;

AccountRecord accRec = new AccountRecord(da.getRecord("ACCOUNT", accountId));
String category = accRec.getCategory().getValue();
String arrangementId = accRec.getArrangementId().getValue();
String customer = accRec.getCustomer().getValue();

// Alternate account types (e.g. IBAN):
List<AltAcctTypeClass> altAccts = accRec.getAltAcctType();
for (int i = 0; i < altAccts.size(); i++) {
    if (accRec.getAltAcctType(i).getAltAcctType().getValue().equals("T24.IBAN")) {
        String iban = accRec.getAltAcctType(i).getAltAcctId().getValue();
    }
}

// Account entry count via party API:
Account act = new Account(this);
act.setAccountId(accountId);
TDate fromDate = new TDate(); fromDate.set("20240101");
TDate toDate   = new TDate(); toDate.set("20241231");
int numEntries = act.getEntries("BOOK", "", "", "", fromDate, toDate).size();
// getEntries(bookingType, valueDate, tradeDate, narr, fromDate, toDate)
```

### Charge Booking (AcChargeRequestRecord)
Used in `updateRecord` to trigger a charge as a linked transaction:
```java
import com.temenos.t24.api.records.acchargerequest.AcChargeRequestRecord;
import com.temenos.t24.api.records.acchargerequest.ChargeCodeClass;

AcChargeRequestRecord acChgReqRec = new AcChargeRequestRecord();  // no-arg constructor
acChgReqRec.setRequestType("BOOK");
acChgReqRec.setStatus("PAID");
acChgReqRec.setDebitAccount(accountId);
ChargeCodeClass chgCodeCls = new ChargeCodeClass();
chgCodeCls.setChargeCode("STMT.COMM");
chgCodeCls.setChargeAmount("50.00");
acChgReqRec.setChargeCode(chgCodeCls, 0);       // indexed MV set
acChgReqRec.setExtraDetails("Statement charge", 0);
currentRecords.add(acChgReqRec.toStructure());   // added to linked transaction list

com.temenos.t24.api.complex.eb.templatehook.TransactionData txnData =
    new com.temenos.t24.api.complex.eb.templatehook.TransactionData();
txnData.setVersionId("AC.CHARGE.REQUEST,OFS.UPDATE");
txnData.setFunction("I");
txnData.setNumberOfAuthoriser("0");
transactionData.add(txnData);
```

### Letter of Credit
```java
import com.temenos.t24.api.records.letterofcredit.LetterOfCreditRecord;
import com.temenos.t24.api.records.lctypes.LcTypesRecord;

LetterOfCreditRecord lc = new LetterOfCreditRecord(currentRecord);
String lcType = lc.getLcType().getValue();
LcTypesRecord lct = new LcTypesRecord(da.getRecord("", "LC.TYPES", "", lcType));
String transferable = lct.getTransferable().getValue();
String impExp = lct.getImportExport().getValue();
```

### Payment Order
```java
import com.temenos.t24.api.records.paymentorder.PaymentOrderRecord;

PaymentOrderRecord poRec = new PaymentOrderRecord(currentRecord);
poRec.setPaymentOrderProduct("PRODUCT.CODE");
poRec.setPaymentAmount("1000.00");
String awardAmount = poRec.getLocalRefField("AWARD.AMOUNT").getValue();
```

### Arrangement Activity (AA)
```java
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaarrangementactivity.PropertyClass;
import com.temenos.t24.api.records.aaarrangementactivity.FieldNameClass;
import com.temenos.t24.api.arrangement.accounting.Contract;

AaArrangementActivityRecord aaaRec = new AaArrangementActivityRecord();
aaaRec.setArrangement(arrangementId);
aaaRec.setActivity("ACCOUNTS-UPDATE-BALANCE");

PropertyClass prop = new PropertyClass();
prop.setProperty("BALANCE");
FieldNameClass fld = new FieldNameClass();
fld.setFieldName("POSTING.RESTRICT:1");
fld.setFieldValue("DEBIT");
prop.addFieldName(fld);
aaaRec.setProperty(prop, 0);

// Read AA account condition:
Contract aaCnt = new Contract(this);
aaCnt.setContractId(arrangementId);
AaPrdDesAccountRecord accPrd = aaCnt.getAccountCondition("BALANCE");
```

---

---

## Code Generation Rules

When writing L3 Java code, follow these rules extracted from real bank implementations:

### 1. Package naming
- Standard bank custom hooks: `com.temenos.t24` or `com.jib` or `com.jibbank` — all lowercase
- API utilities and sub-packages: all lowercase

### 2. Class skeleton
```java
package com.temenos.t24;

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.<app>.<App>Record;

public class MyClassName extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        <App>Record rec = new <App>Record(currentRecord);
        // ... logic ...
        currentRecord.set(rec.toStructure());
        return rec.getValidationResponse();
    }
}
```

### 3. Always commit the record back
```java
currentRecord.set(rec.toStructure()); // REQUIRED before return
return rec.getValidationResponse();
```

### 4. Wrap LocalRef in try-catch
```java
try {
    String val = rec.getLocalRefField("FIELD").getValue();
    // use val
} catch (Exception e) {}
```

### 5. Use DataAccess(this) — not static
```java
DataAccess da = new DataAccess(this); // 'this' = the hook instance
```

### 6. TransactionData: know which import to use
- `updateRecord` (RecordLifecycle) → `com.temenos.t24.api.complex.eb.templatehook.TransactionData`
- `postUpdateRequest` (RecordLifecycle) → `com.temenos.t24.api.complex.eb.servicehook.TransactionData`
- `updateRecord` (ServiceLifecycle) → `com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData`
- `postUpdateRequest` (ServiceLifecycle) → `com.temenos.t24.api.complex.eb.servicehook.TransactionData`

### 7. Record class naming convention
Application name maps to record class: `LETTER.OF.CREDIT` → `LetterOfCreditRecord`, `CUSTOMER` → `CustomerRecord`, `EB.JIB.POST.RESTRICT` → `EbJibPostRestrictRecord`

### 8. MV field add vs set
- `list.add(index, group)` — insert at position
- `list.set(index, group)` — replace at position (use when row already exists)

### 9. Typed MV nested class access
Generated record classes expose MV fields as `List<XxxClass>` where `XxxClass` has strongly-typed sub-field getters/setters:
```java
// Read typed MV list:
List<CashSalesCyClass> cashSalesList = pl.getCashSalesCy();
// Access sub-fields:
String cashCy = cashSalesList.get(i).getCashSalesCy().getValue();
// Mutate in place — no need to re-add to the list:
cashSalesList.get(i).setCashSales("100.00");  // direct setter on list element
// Commit via toStructure():
currentRecord.set(pl.toStructure());

// Indexed access shortcut (same as list.get(i)):
String val = rec.getPostingRestrict(i).getPostingRestrict().getValue();
```

### 10. JAR MV detection: secondary classes = multivalue fields

When `jar\com\temenos\t24\api\records\<ApplicationName>\` contains **more than one** `.java`/`.class` file:

- `<AppNameCamelCase>Record.java` (e.g., `AaArrAccountRecord.java`) = the primary record class
- Every **other** `*Class.java`/`.class` in the same folder (e.g., `AltIdTypeClass.java`, `PostingRestrictClass.java`) = a **multivalue field group class**

Each extra class maps to a multivalue field on the record. Always use the typed `List<XxxClass>` accessor — never raw field-position access.

```java
// AltIdTypeClass found in jar → ALT.ACCT.TYPE is multivalue on AccountRecord
import com.temenos.t24.api.records.account.AltIdTypeClass;

List<AltIdTypeClass> altIds = accRec.getAltAcctType();

// Read all MV occurrences:
for (int i = 0; i < altIds.size(); i++) {
    String altType = altIds.get(i).getAltAcctType().getValue();
    String altId   = altIds.get(i).getAltAcctId().getValue();
}

// Add new MV row:
AltIdTypeClass newAlt = new AltIdTypeClass();
newAlt.setAltAcctType("IBAN");
newAlt.setAltAcctId("GB29NWBK60161331926819");
accRec.getAltAcctType().add(altIds.size(), newAlt);  // append

// Replace existing row (row must already exist — use add() for new rows):
accRec.getAltAcctType().set(0, newAlt);

// Remove MV row at index i:
accRec.getAltAcctType().remove(i);

// Indexed shortcut (same as list.get(i)):
String code = accRec.getPostingRestrict(0).getPostingRestrict().getValue();

// Set via indexed setter (if generated):
accRec.setPostingRestrict("DEBIT", 0);
```

jBC equivalent: `FOR lvI = 1 TO DCOUNT(REC<FIELD.POS>, @VM)` / `REC<FIELD.POS, lvI>` (see jBC Multivalue → Java table).

### 11. TBoolean — mutable boolean flag
Use when you need a boolean that can be modified inside a helper method (Java booleans are pass-by-value):
```java
import com.temenos.api.TBoolean;

TBoolean errorFlag = new TBoolean();
errorFlag.set(false);       // or .set(true)
boolean hasError = errorFlag.get();

// As a mutable output param:
private void validatePhone(LocalRefGroup rec, TBoolean errorFlag) {
    rec.getLocalRefField("M.PHONE.1").setError("ERR");
    errorFlag.set(true);
}
```

---

## Decision Guide: Which Superclass?

| Requirement | T24 Routine Name | Java Method | Superclass |
|---|---|---|---|
| Validate/transform record ID | `ID.RTN` | `checkId()` | `RecordLifecycle` |
| Default fields before display | `CHECK.REC.ROUTINE` / `AUTO.FIELD.ROUTINE` | `defaultFieldValues()` | `RecordLifecycle` |
| Validate a specific field | `VALIDATION.ROUTINE` | `validateField()` | `RecordLifecycle` |
| Validate record on commit | `INPUT.ROUTINE` | `validateRecord()` | `RecordLifecycle` |
| Update core fields before auth F.WRITE | `BEFORE.AUTH.ROUTINE` | `updateCoreRecord()` | `RecordLifecycle` |
| Trigger async OFS after auth | `AUTH.ROUTINE` | `postUpdateRequest()` | `RecordLifecycle` |
| Trigger sync transaction on auth | — | `updateRecord()` | `RecordLifecycle` |
| Batch job: select + process records | SERVICE | `getIds()` + `updateRecord()` | `ServiceLifecycle` |
| Add programmatic enquiry filter | `BUILD.ROUTINE` | `setFilterCriteria()` | `Enquiry` |
| Transform field value before display | `CONVERSION.ROUTINE` | `setValue()` | `Enquiry` |
| Custom multi-file enquiry | NOFILE ENQUIRY | `setIds()` | `Enquiry` |
| Default AA property fields | — | `defaultFieldValues()` | `ActivityLifecycle` |
| Validate AA activity | — | `validateRecord()` | `ActivityLifecycle` |
| Post-auth action on AA arrangement | — | `postCoreTableUpdate()` | `ActivityLifecycle` |
| Read arrangement active conditions | — | `Contract.getConditionForProperty()` | `ActivityLifecycle` |
| DB stored function (SQL layer) | — | `BasicFunctions` static methods | — |

---

## Version Routines — T24 Name to Java Method Mapping

T24 attaches hook routines to VERSION records via an **EB.API** record. The routine type defined in the VERSION determines which Java method is invoked.

| T24 Routine Type | Java Method to Override | When Invoked | Key Rules |
|---|---|---|---|
| `ID.RTN` | `checkId()` | Immediately when user enters record ID | Returns the validated/transformed ID string |
| `CHECK.REC.ROUTINE` | `defaultFieldValues()` | After ID validated, before record displayed | Only fires for I, A, D, R functions |
| `AUTO.FIELD.ROUTINE` | `defaultFieldValues()` | After ID supplied, before record displayed | Manipulate field content before display |
| `VALIDATION.ROUTINE` | `validateField()` | On commit/validate — field-level | Cannot modify core fields; only local/version fields |
| `INPUT.ROUTINE` | `validateRecord()` | On commit/validate — record-level | Full record validation; can read/write all fields |
| `AFTER.UNAUTH.ROUTINE` | `defaultFieldValues()` | After record un-authorised | Re-default fields after rollback |
| `BEFORE.AUTH.ROUTINE` | `updateCoreRecord()` | On authorise, before F.WRITE to live file | Can update core fields; CANNOT update local ref fields |
| `AUTH.ROUTINE` | `postUpdateRequest()` | After authorise, asynchronously via OFS | Uses OFS.MESSAGE.SERVICE; async processing |

### validateField — Validation Routine
**Signature is 4 params** — `fieldData` is the current value of the changed field.
```java
@Override
public TValidationResponse validateField(String application, String currentRecordId,
        String fieldData, TStructure currentRecord) {

    SomeRecord rec = new SomeRecord(currentRecord);

    // fieldData = value the user just typed into the field
    if (fieldData.equals("1002")) {
        rec.getLocalRefField("MY.SECTOR").setError("SECTOR 1002 IS NOT ALLOWED");
    }
    // Note: core fields cannot be modified here — only local/version fields
    currentRecord.set(rec.toStructure());
    return rec.getValidationResponse();
}
```

### updateCoreRecord — Before Auth Routine
```java
@Override
public TValidationResponse updateCoreRecord(String application, String currentRecordId,
        TStructure currentRecord, TStructure liveRecord,
        TransactionContext transactionContext) {

    SomeRecord rec = new SomeRecord(currentRecord);
    // Can update core fields:
    rec.setSomeCoreField("value");
    // CANNOT update local reference fields here
    currentRecord.set(rec.toStructure());
    return rec.getValidationResponse();
}
```

### postUpdateRequest — Auth Routine (OFS async)
```java
// For posting OFS messages asynchronously after auth.
// OFS.MESSAGE.SERVICE must be running.
// Messages go to F.OFS.MESSAGE.QUEUE; responses in F.OFS.RESPONSE.QUEUE.
@Override
public void postUpdateRequest(String application, String currentRecordId,
        TStructure currentRecord,
        List<com.temenos.t24.api.complex.eb.servicehook.TransactionData> transactionData,
        List<TStructure> currentRecords, TransactionContext transactionContext) {

    com.temenos.t24.api.complex.eb.servicehook.TransactionData txnData =
        new com.temenos.t24.api.complex.eb.servicehook.TransactionData();
    txnData.setVersionId("APPLICATION,VERSION");
    txnData.setFunction("INPUT");
    txnData.setNumberOfAuthoriser("0");
    txnData.setSourceId("OFS.LOAD");
    transactionData.add(txnData);
    currentRecords.add(targetRec.toStructure());
}
```

---

## Enquiry Routines — T24 Name to Java Method Mapping

| T24 Routine Type | Java Method | When Invoked | Key Rules |
|---|---|---|---|
| `BUILD.ROUTINE` | `setFilterCriteria()` | Before selection — sets criteria | Add criteria programmatically without user input |
| `CONVERSION.ROUTINE` | `setValue()` | After selection, before display | Transforms displayed field values |
| NOFILE Enquiry | `setIds()` | On enquiry execution | Reads multiple apps; returns computed rows |

### setFilterCriteria — Build Routine
Attached to enquiry ENQUIRY record. Sets selection criteria programmatically.
**Return type is `List<FilterCriteria>`** — always return the (modified) list.
```java
@Override
public List<FilterCriteria> setFilterCriteria(List<FilterCriteria> filterCriteria,
        EnquiryContext enquiryContext) {
    // Override a selection field value at runtime:
    FilterCriteria fc = new FilterCriteria();
    fc.setFieldname("@ID");
    fc.setOperand("EQ");
    fc.setValue("RECORD.ID.1 RECORD.ID.2");
    filterCriteria.set(0, fc);  // replace existing criteria at index 0
    return filterCriteria;      // REQUIRED — must return the list
}
```

### setValue — Conversion Routine
Attached to a specific field in the ENQUIRY record (CONVERSION column). Transforms the displayed value.
```java
@Override
public String setValue(String application, String fieldName, String currentValue,
        TStructure record, EnquiryContext enquiryContext) {
    if ("SECTOR".equals(fieldName) && "1002".equals(currentValue)) {
        return "CORPORATE";
    }
    return currentValue;
}
```

### NOFILE Enquiry Setup
1. Override `setIds()` in a class extending `Enquiry`
2. Create `STANDARD.SELECTION` record with ID = `NOFILE.<EB_API_RECORD_NAME>`
3. Create `ENQUIRY` record and set FILE.NAME = that STANDARD.SELECTION record

#### FilterCriteria — named-field switch pattern (production)
When the ENQUIRY has multiple filter fields, iterate `filterCriteria` and switch on `getFieldname()`:
```java
@Override
public List<String> setIds(List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {
    DataAccess da = new DataAccess(this);
    Session session = new Session(this);
    List<String> results = new ArrayList<>();

    String arrId    = "";
    String fromDate = "";
    String toDate   = "";

    // Named-field switch — more robust than index-based get(0), get(1):
    for (int i = 0; i < filterCriteria.size(); i++) {
        String fieldName = filterCriteria.get(i).getFieldname();  // returns String directly
        switch (fieldName) {
            case "ARR.ID":    arrId    = filterCriteria.get(i).getValue(); break;
            case "FROM.DATE": fromDate = filterCriteria.get(i).getValue(); break;
            case "TO.DATE":   toDate   = filterCriteria.get(i).getValue(); break;
        }
    }

    // Note: some versions return an object needing .toString():
    // String fieldName = filterCriteria.get(i).getFieldname().toString();

    try {
        // Date range filtering with LocalDate:
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyyMMdd");
        LocalDate fromDt = LocalDate.parse(fromDate, fmt);
        LocalDate toDt   = LocalDate.parse(toDate,   fmt);

        // Read records, filter, build output:
        // ... processing logic ...

        // Output row — columns separated by "*", one string per row:
        results.add(arrId + "*" + fromDate + "*" + computedValue);

    } catch (Exception e) {
        // On error add a partial/empty row so the enquiry doesn't return null:
        results.add("" + "*" + "" + "*" + "");
    }
    return results;
}
```

**Output row rules:**
- Each `String` in the returned `List` = one enquiry row
- Columns within a row are `"*"`-delimited (agreed with ENQUIRY field definitions)
- Always add a catch that appends a safe empty row — prevents null return crashing the enquiry
- `getFieldname()` returns `String` directly in modern T24 versions; older versions may need `.toString()`

#### setIds — simple positional variant (legacy)
```java
String param1 = filterCriteria.get(0).getValue();
String param2 = filterCriteria.get(1).getValue();
results.add(param1 + "*" + param2 + "*computed_value");
```

---

## EB.API Configuration

Every Java method invoked from T24 needs an **EB.API** record:

| EB.API Field | Value |
|---|---|
| SOURCE.TYPE | `Method` |
| JAVA.CLASS | Fully qualified class name (e.g. `com.temenos.t24.MyHook`) |
| JAVA.METHOD | Method name (e.g. `validateRecord`) |
| JAVA.PACKAGE | Package (e.g. `com.temenos.t24`) |

Attach the EB.API record to:
- **VERSION record** → for version routines (ID.RTN, CHECK.REC.ROUTINE, etc.)
- **ENQUIRY record** → for enquiry routines (field CONVERSION, or BUILD.ROUTINE)
- **SERVICE record** → for ServiceLifecycle batch jobs

**JAR deployment:** Export the Java project as a JAR; place in `JBoss/modules/com/slot01/temenos/t24/main/`.

**Naming conventions (official):**
- Package name: all lower case
- Class name: CamelCase
- Only override the methods you need

---

## Official L3 API Package and Class Reference

Full list of all packages, classes, method names and types from the Temenos official documentation.
Type: **Hook** = override in your class; **API** = call on the object; **Deprecated** = do not use.

### Package: `account`

| Class | Method | Type | Description |
|---|---|---|---|
| `IBAN` | `getBic` | API | Returns BIC for a given IBAN |
| `IBAN` | `getIbanInformation` | API | Returns IbanInformation object (calculated IBAN values) |
| `AccountingEntry` | `generateStatementEntryEvent` | Hook | Generate Integration event for statement entry |
| `AccountingEntry` | `postUpdateRequest` | Hook | Post async record updates during accounting phase |
| `AccountingEntry` | `setAccountId` | Hook | Check digit calculation + update accountId in locking table |
| `AccountingEntry` | `setAlternateAccountId` | API | Use instead of `setAccountId` |
| `Report` | `getAssetLiabilityReportLines` | API | Report lines for given consolidation Id and asset type |
| `Report` | `getProfitLossReportLines` | API | Report lines for given consolidation Id and currency |
| `TransactionRecycler` | `evaluateSettlement` | Hook | Evaluate settlement for processing (set details, error, or handoff) |
| `TransactionRecycler` | `processSettlement` | Hook | Process settlement via FUNDS.TRANSFER / PAYMENT.ORDER |

### Package: `arrangement`

| Class | Method | Type | Description |
|---|---|---|---|
| `RuleComparison` | `getDormancyException` | Hook | Get dormancy exception based on criteria and activity history |

### Package: `atm`

| Class | Method | Type | Description |
|---|---|---|---|
| `AtmMessageLifecycle` | `getCharge` | Hook | Calculate and return ATM charge |
| `AtmMessageLifecycle` | `getCompanyCode` | Hook | Return company code for booking transaction |
| `AtmMessageLifecycle` | `updateRecord` | Hook | Update records after ATM request is processed |

### Package: `clearing`

| Class | Method | Type | Description |
|---|---|---|---|
| `InwardEntry` | `validateEntry` | Hook | Validate inward clearing entry; return ValidationResponse |

### Package: `contract`

| Class | Method | Type | Description |
|---|---|---|---|
| `Assessment` | `getContractStatus` | Hook | Return DPD details of contract from external system |
| `Assessment` | `getObligorStatus` | Hook | Return DPD, UTP indicators and probation details of obligor |
| `Calculation` | `calculateTaxAmount` | Hook | **Deprecated** — use `getTaxAmount` |
| `Calculation` | `getAmortizationAmount` | Hook | Calculate and return amortization amount for a period |
| `Calculation` | `getTaxAmount` | Hook | Calculate and return tax amount for the transaction |
| `Calculation` | `updatePrincipal` | Hook | Modify list of principals (amount and date) |
| `ProvisionManagement` | `getSegmentationProvision` | Hook | Return segmentation provision percentages for provision calc |
| `TaxEngine` | `convertReportFieldValue` | Hook | Return converted field value for transaction report |

### Package: `countrymodelbank.finland`

| Class | Method | Type | Description |
|---|---|---|---|
| `Collateral` | `getDepreciationAmount` | Hook | Customize depreciation calculation for collateral |

### Package: `countrymodelbank.hungary`

| Class | Method | Type | Description |
|---|---|---|---|
| `TransactionFee` | `isHungaryResident` | Hook | Check if customer is Hungary resident for monthly service |

### Package: `countrymodelbank.regulatory`

| Class | Method | Type | Description |
|---|---|---|---|
| `Tax` | `updateTaxRefund` | API | Update goods and services tax record with tax details |

### Package: `countrymodelbank.saudiarabia`

| Class | Method | Type | Description |
|---|---|---|---|
| `IslamicLoan` | `calculatePartialEarlyPayment` | API | Calculate charge for partial early settlement installments |

### Package: `countrymodelbank.usa`

| Class | Method | Type | Description |
|---|---|---|---|
| `Clearing` | `updateEntry` | Hook | Update transaction info in ACH entries |
| `Fedwire` | `getCompanyCode` | Hook | Remove leading zeros from account number in correction process |
| `Fedwire` | `getOutwardFileName` | Hook | Return outward filename for originating message |
| `Fedwire` | `getScreeningStatus` | Hook | Send custom screening request for Fedwire Non-value Messages |
| `Fedwire` | `getCodewordFlag` | Hook | **Deprecated** — use `PaymentLifecycle.updateProcessSequence` |
| `Fedwire` | `getCreditAccount` | Hook | **Deprecated** — use `PaymentLifecycle.getCreditAccount` |

### Package: `party`

| Class | Method | Type | Description |
|---|---|---|---|
| `Account` | `getAvailableBalance` | API | Returns usable balance including balance type, limit, locked amounts; supports HVT accounts |
| `Account` | `getContractBalancesRecord` | API | Returns contractBalancesRecord for the account |
| `Account` | `lockContractBalancesRecord` | API | Returns and locks contractBalancesRecord for duration of current transaction; lock released at end of transaction |
| `BIC` | `getBicInformation` | API | Returns BIC information from RD.CENTRAL.BANK.DIR or DE.BIC |
| `GeneralDataProtectionRegulation` | `getObfuscatedFieldValue` | Hook | Return obfuscated version of party personal information for GDPR erasure |

### Package: `payments`

| Class | Method | Type | Description |
|---|---|---|---|
| `DataAccess` | `getPaymentRecord` | API | Returns payment record from current company table |
| `FeeDeterminationHook` | `getChargeAmount` | Hook | **Deprecated** — use `PaymentLifecycle.getChargeResponse` |
| `Message` | `updateFieldValue` | Hook | Java hook feature for all external system request types |
| `Message` | `updatePaymentObject` | Hook | Updates the entire payment object |
| `PaymentLifecycle` | `getChargeResponse` | Hook | Get charge response (calculated amount or use system default) |
| `PaymentLifecycle` | `getCreditAccount` | Hook | Return credit-side account for current transaction |
| `PaymentLifecycle` | `getDebitAccount` | Hook | Return debit-side account for current transaction |
| `PaymentLifecycle` | `getExternalRequestFieldValue` | Hook | Get field value mapped to external request |
| `PaymentLifecycle` | `getFileName` | Hook | Get filename for outgoing payment message |
| `PaymentLifecycle` | `getPaymentDate` | Hook | Return PaymentDate affecting when payment is processed |
| `PaymentLifecycle` | `getRequestType` | Hook | Determine request type used by transaction recycler |
| `PaymentLifecycle` | `getSource` | Hook | Get source for payment message (non-SWIFT channels) |
| `PaymentLifecycle` | `getStatementNarrative` | Hook | Get narrative for POR.POSTING.AND.CONFIRMATION |
| `PaymentLifecycle` | `getSwiftSource` | Hook | Get source for payment message (SWIFT channel) |
| `PaymentLifecycle` | `postRequestToExternalSystem` | Hook | Decide and post request to external system |
| `PaymentLifecycle` | `postUpdateRequest` | Hook | Async update of core records |
| `PaymentLifecycle` | `skipMessage` | Hook | Decide whether to skip generating SWIFT output message |
| `PaymentLifecycle` | `updateProcessSequence` | Hook | Update processing sequence; include/exclude codeword |
| `PaymentLifecycle` | `updateProduct` | Hook | Override product-related information including routing product |
| `PaymentLifecycle` | `validateCreditParty` | Hook | Validate credit-side party |
| `PaymentLifecycle` | `validateDebitParty` | Hook | Validate debit-side party |
| `PaymentOrderLifecycle` | `applyChargeType` | Hook | Determine if charge type from PAYMENT.ORDER.PRODUCT is included |
| `PaymentOrderLifecycle` | `getPaymentSystemType` | Hook | Indicate which payment system to use |
| `PaymentOrderLifecycle` | `setProductId` | Hook | Change payment order product ID |
| `PaymentOrderLifecycle` | `validatePaymentOrderRecord` | Hook | Validate payment order record |

### Package: `rates`

| Class | Method | Type | Description |
|---|---|---|---|
| `Charge` | `calculateCharges` | Hook | Calculate charge in local and deal currency (loans, deposits, etc.) |
| `Charge` | `calculateCommission` | Hook | Calculate commission in local and deal currency |
| `Charge` | `calculateTax` | Hook | Calculate tax amount for the transaction |
| `Charge` | `getChargeCondition` | API | Gets customer charge condition for BL.BILL, TELLER, LETTER.OF.CREDIT, LC.AMENDMENTS, DRAWINGS |
| `Charge` | `getCommissionCondition` | API | Gets customer commission condition for LETTER.OF.CREDIT, LC.AMENDMENTS, DRAWINGS |
| `Charge` | `getFundsTransferCondition` | API | Gets customer charge condition for FUNDS.TRANSFER |
| `Charge` | `getNextPayment` | API | Fetches next payment date and amount for an arrangement |

### Package: `system`

| Class | Method | Type | Description |
|---|---|---|---|
| `Archive` | `loadArchiveFiles` | Hook | Initialise ARC.GENERIC service |
| `Archive` | `processArchiveRecords` | Hook | Delete or move record into archive file |
| `Archive` | `selectArchiveRecords` | Hook | Return selection conditions or record keys for archive |
| `DataAccess` | `getCurrentDirectory` | API | Returns T24 current runtime directory path |
| `DataAccess` | `getFieldValue` | API | Returns entire value of a T24 field given app, field name, record |
| `DataAccess` | `setFieldValue` | API | Returns record with specified field value replaced |
| `DataExporter` | `excludeId` | Hook | Filter records from data extract by excluding them |
| `DataExporter` | `getCustomFields` | Hook | Return list of custom field values to append to extracted row |
| `DataExporter` | `getFilterCriteria` | Hook | Filter record IDs or transactions from data export |
| `DataExporter` | `getIds` | Hook | Return list of IDs for records to extract from a table |
| `DataExporter` | `getRows` | Hook | Extract data from application record into one or more rows |
| `DataExporter` | `setCustomFields` | Hook | Set values of custom fields appended to data export |
| `DataExporter` | `transferDataExtract` | Hook | Transfer entire data extract to desired location |
| `DataFormattingEngine` | `getHeaderData` | Hook | Return string used as header for extracted file |
| `DataFormattingEngine` | `getTrailerData` | Hook | Return string used as trailer for extracted file |
| `DataFormattingEngine` | `updateRecord` | Hook | Update records of a table |
| `DataMapper` | `convertFieldValue` | Hook | Convert value while mapping data from one record to another |
| `Delivery` | `getBankRmaStatus` | Hook | Validate if bank can receive message type (SWIFT RMA) |
| `Delivery` | `getFieldValues` | API | Map incoming tag values to field values for applicationName |
| `Delivery` | `getMessageRmaStatus` | Hook | Validate if message type requires RMA capability |
| `Delivery` | `getSwiftRmaStatus` | API | Validate if message type can be sent to bank |
| `Delivery` | `mapTagValuesToRecord` | API | Map record values from incoming message using DE.MESSAGE tag map |
| `Delivery` | `validateBic` | API | Validate BIC; returns ValidationResponse |
| `Delivery` | `validateCompanyBic` | API | Validate company BIC |
| `Delivery` | `validateCustomerBic` | API | Validate customer BIC |
| `Enquiry` | `setDropdownFilterCriteria` | Hook | Set selection criteria from current input screen record values |
| `Record` | `getGroupName` | API | Return group name for record based on table conditions |
| `RecordLifecycle` | `enableAutomaticAuthorisation` | Hook | Identify transactions that can be auto-authorised (EB.STP.CONDITION) |
| `RecordLifecycle` | `getLookupRecordAmendments` | Hook | Amend multiple lookup table records (add/remove related IDs); enabled for Delete at unauthorised phase |
| `RecordLifecycle` | `postUpdateRequest` | Hook | Post OFS messages asynchronously after auth |
| `RecordLifecycle` | `updateLookupTable` | Hook | **Deprecated** — use `getLookupRecordAmendments` |
| `Security` | `isDataAccessRestricted` | Hook | Return boolean to restrict/allow data access |
| `ServiceLifecycle` | `getSwiftRequests` | Hook | Return number of SWIFT requests for system processing |
| `ServiceLifecycle` | `getTableCriteria` | Hook | Return TableCriteria controlling ID selection from table |
| `ServiceLifecycle` | `updateLoanDepositRecordWithSchedule` | Hook | Update LD.LOANS.AND.DEPOSITS and LD.SCHEDULE.DEFINE via version and ID |
| `Session` | `clearLookupCache` | API | Clear all lookup values from cache |
| `Session` | `deriveLabelValue` | Hook | Return derived label data from EB.CONTEXT data argument |
| `Session` | `getCachedLookupValues` | API | Return cached lookup values for given key |
| `Session` | `getCachedRecord` | API | Return cached record from live table of current company |
| `Session` | `getClientConnection` | API | Return client connection (IP, channel, hostname) |
| `Session` | `getExternalUserId` | API | Return ID of external user |
| `Session` | `getSessionNumber` | API | Return current session number |
| `Session` | `getSourceId` | API | Return ID of current OFS source record |
| `Session` | `Initialize` | Hook | Pre-load cached data to improve session processing time |
| `Session` | `loadRecord` | Hook | Pre-load cached data for given table and record ID |
| `Session` | `printLine` | API | Print to T24 standard output (with process/job/session prefix) |
| `Session` | `publishMessage` | API | Transform record and publish per configuration |
| `Session` | `setNextVersion` | API | Define VERSION launched on successful commit (EB.SET.NEXT.TASK) |

---

## Production Utility Patterns

Patterns extracted from real bank L3 implementations.

### hasFieldValue — safe TField unwrap

```java
import java.util.Optional;
import com.temenos.api.TField;

public String hasFieldValue(TField fieldVal) {
    return Optional.ofNullable(fieldVal.getValue()).orElse("");
}
```

Use this everywhere instead of inline `.getValue()` — guards against null TField on older records.

### hasRecord — guarded DataAccess read into shared TStructure

```java
private TStructure tStructure = null;

private void hasRecord(String fileName, String recordId) {
    try {
        tStructure = dataAccess.getRecord(fileName, recordId);
    } catch (Exception e) {
        tStructure = null;
    }
}
```

Call before constructing a record class from `tStructure`. **Always null-check `tStructure`** before passing to a record constructor — `da.getRecord()` can return null on missing records and `hasRecord` also catches exceptions silently.

### Session.getCompanyRecord() — company mnemonic

```java
import com.temenos.t24.api.records.company.CompanyRecord;

Session session = new Session(this);
CompanyRecord companyRecord = session.getCompanyRecord();
String companyMnemonic = hasFieldValue(companyRecord.getFinancialMne());
```

### LocalDate date range filter

When filtering T24 date strings (YYYYMMDD) against a from/to range:

```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyyMMdd");
LocalDate fromDt = LocalDate.parse(fromDateStr, fmt);
LocalDate toDt   = LocalDate.parse(toDateStr,   fmt);
LocalDate billDt = LocalDate.parse(billDateStr,  fmt);

if (billDt.isAfter(fromDt) && billDt.isBefore(toDt)) {
    // within range — process record
}
// isAfter / isBefore are EXCLUSIVE of the boundary date
// use !billDt.isBefore(fromDt) for inclusive from, !billDt.isAfter(toDt) for inclusive to
```

### selectRecords + for-each loop

```java
// Select IDs with LIKE filter:
List<String> ids = da.selectRecords("", "PP.LORO.NOSTRO.ACCOUNT", "", "WITH @ID LIKE " + currency);

// Iterate with for-each (preferred over indexed for when you don't need the index):
for (String id : ids) {
    PpLoroNostroAccountRecord rec = new PpLoroNostroAccountRecord(da.getRecord("PP.LORO.NOSTRO.ACCOUNT", id));
    String fieldVal = hasFieldValue(rec.getAccountnumbertype());
    if (fieldVal.contains("N")) {
        // ...
    }
}
```

### Deeply nested MV access (3+ levels)

Generated record classes can expose MV fields inside MV fields. Access via chained indexed getters:

```java
// PpBankchargesRecord: getFeetype(mvIndex).getFeetierrangelowerlimit(svIndex).getFixedchargeamount()
PpBankchargesRecord bankRec = new PpBankchargesRecord(da.getRecord("PP.BANK.CHARGES", id));
String fixedAmt = hasFieldValue(bankRec.getFeetype(0).getFeetierrangelowerlimit(0).getFixedchargeamount());
```

Always use indexed accessor `getXxx(i)` (0-based) when the getter is on an MV class, not `getXxx().get(i)`.

### AaAccountDetails — nested MV bill iteration (BillPayDate → BillId)

`AA.ACCOUNT.DETAILS` has a two-level MV structure: `BILL.PAY.DATE` (outer MV) contains `BILL.ID` (inner MV):

```java
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaaccountdetails.BillIdClass;
import com.temenos.t24.api.records.aaaccountdetails.BillPayDateClass;

AaAccountDetailsRecord aaDet = new AaAccountDetailsRecord(da.getRecord("AA.ACCOUNT.DETAILS", arrangementId));

List<BillPayDateClass> billDateList = aaDet.getBillPayDate();
for (BillPayDateClass billDateEntry : billDateList) {
    List<BillIdClass> billIdList = billDateEntry.getBillId();
    for (BillIdClass bill : billIdList) {
        String billDate   = hasFieldValue(bill.getBillDate());
        String billStatus = hasFieldValue(bill.getBillStatus());
        String setStatus  = hasFieldValue(bill.getSetStatus());
        String payMethod  = hasFieldValue(bill.getPayMethod());
        String billId     = hasFieldValue(bill.getBillId());
        String actRef     = hasFieldValue(bill.getActivityRef());
    }
}
```

### AaBillDetailsRecord — full field access

```java
import com.temenos.t24.api.records.aabilldetails.AaBillDetailsRecord;
import com.temenos.t24.api.records.aabilldetails.PaymentTypeClass;
import com.temenos.t24.api.records.aabilldetails.PropertyClass;
import com.temenos.t24.api.records.aabilldetails.RepayRefClass;

AaBillDetailsRecord billRec = new AaBillDetailsRecord(da.getRecord("AA.BILL.DETAILS", billId));

String actPayDate  = hasFieldValue(billRec.getActualPayDate());
String payDate     = hasFieldValue(billRec.getPaymentDate());
String orTotalAmt  = hasFieldValue(billRec.getOrTotalAmount());   // original total
String osTotalAmt  = hasFieldValue(billRec.getOsTotalAmount());   // outstanding total
double paid = Double.parseDouble(orTotalAmt.isEmpty() ? "0" : orTotalAmt)
            - Double.parseDouble(osTotalAmt.isEmpty() ? "0" : osTotalAmt);

// Payment type MV:
for (PaymentTypeClass payType : billRec.getPaymentType()) {
    String billType = hasFieldValue(payType.getBillType()); // e.g. "PAYMENT" → remap to "SETTLEMENT"
}

// Property → RepayRef nested MV:
for (PropertyClass prop : billRec.getProperty()) {
    for (RepayRefClass repayRef : prop.getRepayRef()) {
        String ref = hasFieldValue(repayRef.getRepayRef());
        // ref may be an AAA.ARRANGEMENT.ACTIVITY reference (starts "AAA")
        if (ref.length() >= 3 && ref.substring(0, 3).equals("AAA")) {
            String aaaRef = ref.substring(0, 18);
            AaArrangementActivityRecord actRec = new AaArrangementActivityRecord(
                    da.getRecord("AA.ARRANGEMENT.ACTIVITY", aaaRef));
            String txnContractId = hasFieldValue(actRec.getTxnContractId());
            String settleRef     = txnContractId.substring(0, 18);
        }
    }
}
```

### Production anti-patterns to avoid

| Anti-pattern seen in prod | Correct approach |
|--------------------------|-----------------|
| `DataAccess da = new DataAccess(this)` declared **both** at class level AND inside the method | Declare once in the method that uses it (or at class level, never both) |
| `new AaBillDetailsRecord(tStructure)` when `tStructure` last pointed to a **different** application | Always read the correct application before constructing: `da.getRecord("AA.BILL.DETAILS", billId)` |
| `Integer.valueOf(amt1) > Integer.valueOf(amt2)` for monetary comparison | Use `BigDecimal` — `new BigDecimal(amt1).compareTo(new BigDecimal(amt2)) > 0` |
| Class-level mutable strings (`oldval`, `newval`) mutated inside a private helper | Pass as method parameters or use local variables — class-level mutable state is not thread-safe |
| `System.out.println(...)` throughout production code | Use `Logger` — `m_logger.log(Level.INFO, "...")` |

---

## CSD Coding Standards

Official Temenos CSD (Client Specific Development) Java Programming Standards — v1.1/Aug-2022.

### Naming Conventions

| Identifier Type | Convention | Regex | Example |
|---|---|---|---|
| Class name | CapitalizedCamelCase | `^[A-Z][a-zA-Z0-9]*$` | `CsdAncBacsIdUpdate` |
| Method name | camelCase | `^[a-z][a-zA-Z0-9]*$` | `validateCurrency` |
| Variable (local) | camelCase | `^[a-z][a-zA-Z0-9]*$` | `customerRecord` |
| Member variable | `m_` prefix + camelCase | `^m_[a-z][a-zA-Z0-9]*$` | `m_arrangementId` |
| Parameter | `p_` prefix + camelCase | `^p_[a-z][a-zA-Z0-9]*$` | `p_customerId` |
| Static variable | camelCase | `^[a-z][a-zA-Z0-9]*$` | `yToday` |
| Constant (static final) | UPPER_CASE_WITH_UNDERSCORES | `^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$` | `OFS_SOURCE` |
| Interface name | `I` prefix + CamelCase | — | `IVerifyValidation` |
| Package name | all lowercase | `^[a-z]+(\.[a-zA-Z_][a-zA-Z0-9_]*)*$` | `com.temenos.t24` |

**Java class naming:**  `<DevName/InterfaceName/BRDRef><FunctionDescription>.java`
Example: `CsdAncBacsIdUpdate.java`, `CsdInpAprCalcUpdate.java`

**Data record naming:**

| Record Type | Name Pattern | Example |
|---|---|---|
| TEMPLATE VERSION | `<APP>,CSD.<VERSIONNAME>` | `CUSTOMER,CSD.MANDATE.CHK` |
| ENQUIRY | `CSD.<ENQUIRYNAME>` | `CSD.CUST.SUMMARY` |
| EB.ERROR | `EB-CSD.<ERRORMSGNAME>` | `EB-CSD.MISSING.NATIONALITY` |
| BATCH/TSA.SERVICE | `<COMP.MNE>/CSD.<BATCHNAME>` | `BNK/CSD.APR.CALC` |
| OVERRIDE | `CSD.<OVRMSGNAME>` | `CSD.MISSING.DOC.OVR` |
| OFS.SOURCE | `CSD.<RTNNAME>` | `CSD.FT.UPDATE` |
| AA.PRD.DES.* | `CSD.<PropertyConditionName>` | `CSD.LEND.SCHED` |
| STANDARD.SELECTION | `CSD.<TEMPLATENAME>` | `NOFILE.CSD.CUST.ENQ` |

All L3-specific data MUST have prefix `CSD`.

### Structure & Size Limits

| Element | Limit |
|---|---|
| File length | max 2000 lines |
| Line length | max 160 characters |
| Method length | max 100 lines (typically ≤ 50) |
| Method parameters | max 10 |
| Inner class length | max 20 lines |
| One line of code | max 2 function calls |
| Indentation | 4 spaces (no tab characters) |

### Modifier Order
`public` → `protected` → `private` → `abstract` → `static` → `final` → `transient` → `volatile` → `synchronized` → `native` → `strictfp`

### Class Structure Order
1. Static final constants
2. Static blocks (initialization only)
3. Inner classes
4. Member variables
5. Constructors
6. Methods

### Key Rules from CSD
1. **Use BigDecimal for all monetary calculations** — never `double` or `float`.
2. **Initialize DataAccess and Session once** in the parent hook method; pass to sub-methods. Never re-create in every sub-method.
3. **All sub-methods are `private` by default** — only `public` if accessed from another class.
4. **Use EB.ERROR records for errors** — never hardcode error message strings.
5. **Use OVERRIDE records for overrides** — never hardcode override strings.
6. **Variables used in loops must be declared outside the loop**.
7. **Nullify reference variables at end of method** (especially array elements).
8. **Constants over magic numbers** — `if (action == Class.ACTION_EDIT)` not `if (action == 3)`.
9. **Static shared info** (today, companyId, companyMnemonic) should be `static` class variables.
10. **Avoid `System.out.println`** — use Logger for debugging.
11. **Use SonarLint in Eclipse** — highlights issues as you type.
12. **No tab characters anywhere** — 4-space indentation only.
13. **Comments above each logical group** — at minimum every 15 lines; functional comments for every method.
14. **`isService()`** — check this in AA hooks if an update should not run during COB processing.

### JAR Naming Convention
- API JAR: `<CSD_or_BRD_ref>_<DevRef>_Api.jar` (e.g., `CSD_TransactionLimit_Api.jar`)
- Template JAR: `<CSD_or_BRD_ref>_<DevRef>.jar` (e.g., `CSD_TransactionLimit.jar`)

### Exception Handling Rules (CSD)
```java
// 1. Use EB.ERROR record IDs — never hardcode:
throw new T24CoreException("", "EB-CSD.SOME.ERROR.CODE");

// 2. Use OVERRIDE record IDs — never hardcode:
rec.getSomeField().setOverride("CSD.SOME.OVERRIDE.CODE");

// 3. All caught exceptions must have comments:
try {
    TStructure ftRec = da.getRecord("FUNDS.TRANSFER", ftId);
} catch (Exception e) {
    // FT record not found — check history table
    try {
        TStructure ftHist = da.getHistoryRecord("FUNDS.TRANSFER", ftId);
    } catch (Exception ex) {
        // History also not found — log and continue
        logger.error("FT record not found: " + ftId, ex);
    }
}
```

---

## Core APIs

### Amount API

```java
import com.temenos.t24.api.system.Amount;

Amount amountApi = new Amount(this);

// Available balance (considers locked events and limit):
BigDecimal available = amountApi.getAvailableAmount(currencyId);

// Opening balance on a given date:
// balanceType: "BOOKING", "VALUE", "TRADE"
BigDecimal balance = amountApi.getBalance(balanceType, balanceDate);

// Net credit movements for account on given date:
BigDecimal creditTurnover = amountApi.getTurnoverCredit(balanceType, balanceDate);

// Net debit movements for account on given date:
BigDecimal debitTurnover = amountApi.getTurnoverDebit(balanceType, balanceDate);
```

### Exchange Rate API

```java
import com.temenos.t24.api.system.Currency;

Currency ccyRec = new Currency(this);

// Calculate exchange rate between two currencies (calls EXCHRATE):
String rate = ccyRec.calculateRate(buyCurrency, sellCurrency, currencyMarket, outputCurrency, historyDate);

// Calculate buy exchange rate amount (calls CUSTRATE):
String buyAmt = ccyRec.calculateBuyExchangeRateAmount(
    buyCurrencyMarket, sellCurrencyMarket, buyCurrency, sellCurrency, sellAmount, spreadPercentage);

// Calculate exchange rate local → deal (calls CALC.ERATE.LOCAL):
String exRate = ccyRec.calculateExchangeRate(localAmount, dealCurrency, dealAmount);

// Calculate buy amount for currency pair (calls EXCHRATE):
String buyAmount = ccyRec.calculateBuyAmount(
    buyCurrency, sellCurrency, sellAmount, currencyMarket, exchangeRate, historyDate);

// Round amount according to currency rounding rules:
String rounded = ccyRec.getRoundAmount(amount, roundingRuleId); // pass "" for default
```

### Interest API

```java
import com.temenos.t24.api.system.Interest;

Interest interest = new Interest(this);

// Get BASIC.INTEREST rate for a currency on a date:
String rate = interest.getBasicRate(currencyId, interestDate);

// Count accrual days between two dates (calls BD.CALC.DAYS):
// interestDayBasisId: "A1", "A4", "H", etc.
// startDate is INCLUDED, endDate is EXCLUDED
int accrualDays = interest.calculateAccrualDays(startDate, endDate, interestDayBasisId);
```

### ST.Customer API

```java
import com.temenos.t24.api.party.Customer;

Customer customerApi = new Customer(this);
customerApi.setCustomerId(customerId);

boolean exists           = customerApi.customerExists();
List<String> accounts    = customerApi.getAccountNumber();
String parentId          = customerApi.getParentId();       // liability/group head
String customerId        = customerApi.getIdForMnemonic(customerMnemonic);
CustomerProfile profile  = customerApi.getProfile();        // asset class, rating, industry, sector

// Limits:
LimitInfo limit       = customerApi.getLimit(limitReferenceId, currencyId, isUnavailableLimit, isOverUtilisedAmount);
LimitInfo liableLimit = customerApi.getLiableLimit(limitReferenceId, currencyId, isUnavailableLimit, isOverUtilisedAmount);

// Contact / address:
ContactInfo contact   = customerApi.getContractInfo();
String email          = customerApi.getEmailAddress(companyCode, sequenceNo, preferredLanguage);
String swiftAddr      = customerApi.getSwiftAddress(companyCode, sequenceNo, preferredLanguage);
String secureMsg      = customerApi.getDeliverySecureMessageAddress(companyCode, sequenceNo, preferredLanguage);
SettlementAccount sa  = customerApi.getSettlementAccountId(currencyId, currencyMarket, table, portfolioNo, accountType);
List<String> mandates = customerApi.getMandateItems();
PostingRestrictions pr = customerApi.getPostingRestrictions();
```

### LI.Limit API

```java
import com.temenos.t24.api.contract.Limit;

Limit limitApi = new Limit(this);
limitApi.setLimitId(limitId);

// Returns amounts for accounts from LIMIT table; consolidated LimitAmount in LIMIT.CURRENCY (calls LIMIT.GET.ACC.BALS):
List<LimitAmount> amounts = limitApi.getCurrencyAmount(checkValueDate, transactionDate);
```

### AA Contract API (full method list)

All require `contract.setContractId(arrangementId)` first.

```java
Contract contract = new Contract(this);
contract.setContractId(arrangementId);

// --- Arrangement info ---
AaArrangementRecord arr = contract.getContract();
String contractId       = contract.getContractId();
String productId        = contract.getProductId();
String productIdForDate = contract.getProductIdForEffectiveDate(effectiveDate);
String term             = contract.getTerm();
TNumber termAmount      = contract.getTermAmount();
TDate maturityDate      = contract.getMaturityDate();
String ageStatus        = contract.getContractAgeStatus();
String beneficialOwner  = contract.getArrangementBenficialOwner();
CustomerRole custRole   = contract.getCustomerRole();
String simulationId     = contract.getSimulationId();
List<String> propIds    = contract.getPropertyIds();
List<String> propIdsForClass = contract.getPropertyIdsForPropertyClass("INTEREST");

// --- Account / property conditions ---
AaArrAccountRecord acctCond       = contract.getAccountCondition(propertyId);
AaArrAccountRecord acctCondForDate = contract.getAccountConditionForEffectiveDate(propertyId, effectiveDate);
AaAccountDetailsRecord acctDets   = contract.getAccountDetails();
TStructure condition              = contract.getConditionForProperty(propertyId);
TStructure firstVersion           = contract.getFirstVersionOfProperty(propertyId, effectiveDate);
TStructure prevProp               = contract.getPreviousProperty(propertyId);
TStructure prevDatedProp          = contract.getPreviousDatedProperty(propertyId);
TStructure simCond                = contract.getsimulationconditionForProperty(propertyId);

// --- Specific condition types ---
AaArrTermAmountRecord termCond    = contract.getCommitmentCondition(propertyId);
AaArrTermAmountRecord termCondDt  = contract.getCommitmentConditionForEffectiveDate(propertyId, effectiveDate);
List<> interestCond               = contract.getInterestCondition(propertyId);
List<> interestCondDt             = contract.getInterestConditionForEffectiveDate(propertyId, effectiveDate);
List<> chargeCond                 = contract.getChargeCondition(propertyId);
List<> chargeCondDt               = contract.getChargeConditionForEffectiveDate(propertyId, effectiveDate);
List<> repaymentCond              = contract.getRepaymentCondition(propertyId);
List<> repaymentCondDt            = contract.getRepaymentConditionForEffectiveDate(propertyId, effectiveDate);
AaArrCustomerRecord custCond      = contract.getCustomerCondition(propertyId);
AaArrCustomerRecord custCondDt    = contract.getCustomerConditionForEffectiveDate(propertyId, effectiveDate);
AaArrOfficersRecord officersCond  = contract.getOfficersCondition(propertyId);
AaArrOfficersRecord officersCondDt = contract.getOfficersConditionForEffectiveDate(propertyId, effectiveDate);
AaArrLimitRecord limitCond        = contract.getLimitCondition(propertyId);
AaArrLimitRecord limitCondDt      = contract.getLimitConditionForEffectiveDate(propertyId, effectiveDate);

// --- Payment schedules ---
List<> schedule                   = contract.buildPaymentSchedule(startDate, endDate, noOfCycles, paymentType);
List<> scheduleForProp            = contract.buildPaymentScheduleForProperty(startDate, endDate, noOfCycles, paymentType, propertyId);
List<> repaymentSchedule          = contract.getRepaymentSchedule(fromDate, toDate);
Payment nextPayment               = contract.getNextPayment(propertyId);
Payment lastRepayment             = contract.getLastRepayment(propertyId);

// --- Repayment amounts ---
TNumber totalReceived             = contract.getTotalReceivedRepayment();
TNumber totalReceivedForProp      = contract.getTotalReceivedRepaymentForProperty(property);
TNumber totalBetweenDates         = contract.getTotalRepaymentBetweenDates(startDate, endDate);
TNumber totalForMonth             = contract.getTotalRepaymentForMonth();

// --- Bill IDs ---
List<String> billIds              = contract.getBillIds(billDate, paymentDate, billType, paymentMethod, billStatus, settlementStatus, agingStatus, nextAgeDate, repaymentReference);
List<String> billsByDate          = contract.getBillIdsForDate(billDate);
List<String> billsByStatus        = contract.getBillIdsForStatus(billStatus);
List<String> billsByType          = contract.getBillIdsForType(billType);
List<String> billsByPayDate       = contract.getBillIdsForPaymentDate(paymentDate, selectionIndicator); // "FROM" or "TO"
List<String> billsByPayMethod     = contract.getBillIdsForPayMethod(paymentMethod);
List<String> billsBySettlement    = contract.getBillIdsForSettlementStatus(settlementStatus);
List<String> billsByAging         = contract.getBillIdsForAgingStatus(agingStatus);
List<String> billsByRepRef        = contract.getBillIdsForRepaymentReference(repaymentReference);
List<String> billsByNextAge       = contract.getBillIdsForNextAgeDate(nextAgeDate);

// --- Balance movements ---
List<> balMvts         = contract.getBalanceMovements(balanceType, requestType);
List<> fwdCreditMvts   = contract.getForwardCreditBalanceMovements(balanceType, requestType, startDate, endDate);
List<> fwdDebitMvts    = contract.getForwardDebitBalanceMovements(balanceType, requestType, startDate, endDate);
List<> unAuthMvts      = contract.getUnauthorisedBalanceMovements(balanceType, requestType, startDate, endDate);

// --- Overdue info ---
TDate firstOverDue     = contract.getFirstOverDueDate();
TDate lastOverDue      = contract.getLastOverDueDate();
TDate nextDueDate      = contract.getNextDueDate();
TNumber numOverDue     = contract.getNumberOfOverDueBills();

// --- Interest ---
AaInterestAccrualsRecord accr = contract.getInterestAccrualsRecord(property, startDate);
InterestAmount intAmt         = contract.getInterestAmounts(propertyId, startDate, endDate);

// --- Future repayment schedule (installment breakdown by date) ---
// @deprecated in some versions — annotate @SuppressWarnings("deprecation") if needed
List<RepaymentSchedule> schedule = contract.getFutureRepaymentSchedule(fromTDate, toTDate);

// --- Contract balance movements (accrued profit, deferred profit, etc.) ---
List<BalanceMovement> balMvts = contract.getContractBalanceMovements(balanceType, "");
// balanceType examples: "RECDEFERREDPFT", "CURACCOUNT", "TOTCOMMITMENT"
```

#### RepaymentSchedule API (`com.temenos.t24.api.complex.aa.contractapi`)

```java
import com.temenos.api.TDate;
import com.temenos.t24.api.arrangement.accounting.Contract;
import com.temenos.t24.api.complex.aa.contractapi.BalanceMovement;
import com.temenos.t24.api.complex.aa.contractapi.RepaymentDueType;
import com.temenos.t24.api.complex.aa.contractapi.RepaymentMethod;
import com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule;

Contract contract = new Contract(this);
contract.setContractId(arrangementId);

// Build TDate from string (YYYYMMDD):
String today   = session.getCurrentVariable("!TODAY");
String matDate = contract.getMaturityDate().toString();  // "YYYYMMDD"
TDate fromTDate = new TDate(today);
TDate toTDate   = new TDate(matDate);

// Get installment schedule between today and maturity:
List<RepaymentSchedule> schedule = contract.getFutureRepaymentSchedule(fromTDate, toTDate);

double totalPrincipal = 0.0, totalProfit = 0.0;

for (int s = 0; s < schedule.size(); s++) {
    String dueDate = schedule.get(s).getDueDate().toString();  // "YYYYMMDD"

    // Each due date has one or more due types (ACCOUNT, PRINCIPALINT, etc.):
    List<RepaymentDueType> dueTypes = schedule.get(s).getRepaymentDueType();
    for (int dt = 0; dt < dueTypes.size(); dt++) {

        // Each due type has one or more repayment methods (property breakdown):
        List<RepaymentMethod> methods = dueTypes.get(dt).getRepaymentMethod();
        for (int m = 0; m < methods.size(); m++) {
            String property = methods.get(m).getDueProperty().toString();  // e.g. "ACCOUNT"
            String amount   = methods.get(m).getDuePropertyAmount().toString();

            switch (property) {
                case "ACCOUNT":      // principal component
                    totalPrincipal += Double.valueOf(amount); break;
                case "PRINCIPALINT": // profit/interest component
                    totalProfit    += Double.valueOf(amount); break;
            }
        }
    }
}

// Get accrued deferred profit balance movements:
List<BalanceMovement> balMvts = contract.getContractBalanceMovements("RECDEFERREDPFT", "");
double accruedProfit = 0.0;
for (BalanceMovement bm : balMvts) {
    accruedProfit = bm.getBalance().doubleValue();
}
```

**Rules:**
- `TDate` is constructed from a `String` ("YYYYMMDD"): `new TDate(dateStr)`
- `getDueDate().toString()` and `getMaturityDate().toString()` both return "YYYYMMDD"
- Property codes in `getDueProperty()`: `"ACCOUNT"` = principal, `"PRINCIPALINT"` = profit/interest
- `getBalance().doubleValue()` — use `BigDecimal` in CSD-compliant code: `bm.getBalance().bigDecimalValue()`
- `getFutureRepaymentSchedule` may be deprecated — add `@SuppressWarnings("deprecation")` on the method

### AA.Product API

```java
import com.temenos.t24.api.arrangement.Product;

Product product = new Product(this);
product.setProductId("MORTGAGE");
AaProductCatalogRecord productRec = product.getProduct();
String productId                  = product.getProductId();
```

### AA.Property API

```java
import com.temenos.t24.api.arrangement.Property;

Property prop = new Property(this);
TStructure propRec = prop.getPropertiesForProduct(productId, stage, currency, startDate, effectiveDate);
String propClassId = prop.getPropertyClassId();
String propId      = prop.getPropertyId();
```

### AA.PropertyClass API

```java
import com.temenos.t24.api.arrangement.PropertyClass;

PropertyClass pc = new PropertyClass(this);
String classId = pc.getPropertyClassId(); // e.g. "INTEREST"
List<String> propIds = pc.getPropertyIdsForProduct(productRecord);
```

---

## Component / T24 Hook Alias Reference

| T24 Component | Module | Java Superclass Alias |
|---|---|---|
| `AA.ActivityHook` | Retail | `hook.arrangement.ActivityLifecycle` |
| `AA.CalculationHook` | Retail | `hook.arrangement.Calculation` |
| `AA.RuleComparisonHook` | Retail | `hook.arrangement.RuleComparison` |
| `EB.DataFormattingEngineHook` | AF | `hook.system.DataFormattingEngine` |
| `EB.EnquiryHook` | AF | `hook.system.Enquiry` |
| `EB.ServiceHook` | AF | `hook.system.ServiceLifecycle` |
| `EB.TemplateHook` | AF | `hook.system.RecordLifecycle` |
| `AC.AccountHook` | BF | `hook.accounting.AccountingEntry` |
| `AC.ContractHook` | BF | `hook.contract.StandingOrder` |
| `DE.DeliveryHook` | BF | `hook.system.Delivery` |
| `FT.ContractHook` | BF | `hook.contract.FundsTransfer` |
| `RC.ContractHook` | BF | `hook.accounting.TransactionRecycler` |
| `ST.CalculationHook` | BF | `hook.contract.Calculation` |
| `ST.EnquiryHook` | BF | `hook.party.CustomerPosition` |
| `ST.StatementHook` | BF | `hook.accounting.Statement` |
| `IA.AccountingHook` | BF | `hook.accounting.InternationalAccountingStandards` |
| `PP.PaymentLifecycleHook` | Payments | `hook.payments.PaymentLifecycle` |

---

## ActivityLifecycle: T24 API Table Reference

The `AA.PRD.DES.ACTIVITY.API` table maps Java methods to T24 routine fields:

| Java Method | T24 Routine Field | Invoker |
|---|---|---|
| `defaultFieldValues()` | `RECORD.ROUTINE` / `PRE.VALIDATION.RTN` | `AA.DEFAULT.FIELD.VALUES.INVOKER` |
| `validateRecord()` | `POST.ROUTINE` / `VALIDATE.RTN` | `AA.VALIDATE.RECORD.INVOKER` |
| `updateLookupTable()` | `POST.ROUTINE` | `AA.UPDATE.LOOKUP.TABLE.INVOKER` |
| `postCoreTableUpdate()` | `POST.ROUTINE` | `AA.POST.CORE.TABLE.UPDATE.INVOKER` |
| `generateSecondaryActivity()` | `POST.ROUTINE` | `AA.GENERATE.SECONDARY.ACTIVITY.INVOKER` |

- `defaultFieldValues()`: Can update local AND core fields. Throws exception = error raised, transaction not committed.
- `validateRecord()`: CANNOT update core fields. CAN update local fields. Returns `TValidationResponse`.
- `updateLookupTable()`: Returns `boolean`. `true` = concat table update required. Uses `LookupData` list.
- `postCoreTableUpdate()`: For OFS-driven async updates. Uses `transactionData` + `transactionRecord`.
- `generateSecondaryActivity()`: All values in `secondaryActivity` must be set or secondary activity will not be generated.

---

---

## jBC-to-Java Conversion Guide

When converting jBC routines to T24 L3 Java, follow these rules to produce idiomatic T24 Java.

### jBC Routine Type → Java Pattern

| jBC Type | T24 Wiring | Java Pattern |
|---|---|---|
| `SUBROUTINE` (INPUT.ROUTINE) | VERSION → INPUT.ROUTINE | Extend `RecordLifecycle`, override `validateRecord()` |
| `SUBROUTINE` (CHECK.REC.ROUTINE) | VERSION → CHECK.REC.ROUTINE | Extend `RecordLifecycle`, override `defaultFieldValues()` |
| `SUBROUTINE` (AUTH.ROUTINE) | VERSION → AUTH.ROUTINE | Extend `RecordLifecycle`, override `postUpdateRequest()` |
| `FUNCTION` (utility called by others) | N/A — not wired to EB.API | Static helper methods OR private methods in the calling hook |
| `SUBROUTINE` (SERVICE) | TSA.SERVICE → SERVICE | Extend `ServiceLifecycle`, override `getIds()` + `updateRecord()` |
| `SUBROUTINE` (AA PRE VALIDATION RTN) | AA.PRD.DES.ACTIVITY.API → RECORD.ROUTINE | Extend `ActivityLifecycle`, override `defaultFieldValues()` |
| `SUBROUTINE` (AA POST ROUTINE) | AA.PRD.DES.ACTIVITY.API → POST.ROUTINE | Extend `ActivityLifecycle`, override `postCoreTableUpdate()` |

### Key Field Access Rule: Always Use Generated Record Classes

**jBC** reads fields by name string:
```jbc
MATREAD REC FROM F.AA.BILL.DETAILS, BILL.ID ELSE REC = ""
PROPERTY  = REC<1>          ;* or REC<AA.BILL.DETAILS.PROPERTY>
PAY.DATE  = REC<2>
PAY.AMT   = REC<3>
```

**Java WRONG** — `getFieldValue()` is a raw fallback; do NOT use it for normal field reads:
```java
// WRONG — bypasses type safety and generated API:
String property = da.getFieldValue("AA.BILL.DETAILS", "PROPERTY", billRec);
```

**Java CORRECT** — always wrap with the generated record class:
```java
AaBillDetailsRecord billDtlRec = new AaBillDetailsRecord(da.getRecord("AA.BILL.DETAILS", billId));
String property  = billDtlRec.getProperty().getValue();
String payDate   = billDtlRec.getPaymentDate().getValue();
String payAmt    = billDtlRec.getPaymentAmount().getValue();
```

### jBC FUNCTION → Java: Correct Patterns

A jBC `FUNCTION` is a reusable utility. Java equivalent options:

**Option 1 — Static utility methods (preferred for simple logic):**
```java
// Utility class — no superclass needed, no T24 wiring
public class BillDetailsHelper {
    public static BillResult getLatestBill(DataAccess p_da, Contract p_contract, String p_arrangementId) {
        // DataAccess and Contract are passed from the calling hook's 'this' context
        List<String> billIds = p_contract.getBillIds("", "", "", "", "", "", "", "", "");
        // ... logic ...
    }
}
```

**Option 2 — Private methods inside the hook class (preferred for reuse within one hook):**
```java
public class MyCbiHook extends RecordLifecycle {
    @Override
    public TValidationResponse validateRecord(...) {
        DataAccess da = new DataAccess(this);
        Contract contract = new Contract(this);
        contract.setContractId(arrangementId);
        BillResult result = getLend01BillDetails(da, contract, arrangementId);
        // ...
    }

    private BillResult getLend01BillDetails(DataAccess p_da, Contract p_contract, String p_arrangementId) {
        // implementation here
    }
}
```

**Option 3 — Instance helper class taking the hook `this`** (use only when the helper needs to survive across method calls):
```java
// The hook 'this' must extend a T24 superclass — the helper receives it via constructor
// DataAccess/Contract constructors accept any T24 lifecycle instance, not just RecordLifecycle
public class BillDetailsHelper {
    private final DataAccess m_da;
    private final Contract   m_contract;

    // Pass the hook 'this' directly — works for RecordLifecycle, ActivityLifecycle, etc.
    public BillDetailsHelper(RecordLifecycle p_hook) {
        m_da       = new DataAccess(p_hook);
        m_contract = new Contract(p_hook);
    }
}
```

### jBC String Comparison → Java

| jBC | Java |
|---|---|
| `IF X = "VALUE" THEN` | `if ("VALUE".equals(x))` |
| `IF X EQ "VALUE" THEN` | `if ("VALUE".equals(x))` |
| `IF X # "" THEN` | `if (!x.isEmpty())` |
| `IF X = "" THEN` | `if (x.isEmpty())` |
| `IF X GT Y THEN` (date YYYYMMDD) | `if (x.compareTo(y) > 0)` — lex order = chron order |
| `UPCASE(X)` | `x.toUpperCase()` |
| `X[1,4]` (substring pos 1, len 4) | `x.substring(0, 4)` — Java is 0-indexed |
| `LEN(X)` | `x.length()` |

### jBC Multivalue → Java

| jBC | Java |
|---|---|
| `DCOUNT(REC<MV.FIELD>,@VM)` | `mvList.size()` |
| `REC<MV.FIELD,i>` | `mvList.get(i-1).getField().getValue()` — Java 0-indexed |
| `REC<MV.FIELD,i,j>` (SV) | navigate the inner list on the sub-class |
| `REC<MV.FIELD> = INSERT(...)` | `mvList.add(index, newGroup)` |
| `DEL REC<MV.FIELD,i>` | `mvList.remove(i-1)` |

### Common jBC → Java Field-Name Mapping

T24 field names map to Java getter/setter via camelCase with dots removed:
- `PAYMENT.DATE` → `getPaymentDate()` / `setPaymentDate()`
- `PAYMENT.AMOUNT` → `getPaymentAmount()` / `setPaymentAmount()`
- `@ID` in jBC → record ID string passed as first parameter to the hook
- `TODAY` (common variable) → `session.getCurrentVariable("!TODAY")`
- `COMPANY` → `session.getCompanyId()`

---

## Common Mistakes to Avoid

1. **Missing `currentRecord.set(rec.toStructure())`** / **`record.set(propRec.toStructure())`** — changes are lost without this.
2. **Wrong TransactionData import** — four distinct types exist; using the wrong one causes ClassCastException:
   - RecordLifecycle `updateRecord` → `eb.templatehook.TransactionData`
   - RecordLifecycle `postUpdateRequest` → `eb.servicehook.TransactionData`
   - ServiceLifecycle `updateRecord` → `eb.servicehook.SynchronousTransactionData`
   - ActivityLifecycle `postCoreTableUpdate` → `aa.activityhook.TransactionData`
3. **Unchecked LocalRef access** — field may not exist; always use try-catch.
4. **`list.add` when row exists** — use `set` for existing rows, `add` only for new rows.
5. **Using `da.getRecord(app, id)` without company** — always pass company string (empty string `""` for current company).
6. **Not handling null/empty from `.getValue()`** — always check `isEmpty()` before use; `getValue()` never returns null but can return `""`.
7. **Re-creating DataAccess/Session in every sub-method** (CSD violation) — declare once in parent hook method; pass as parameter to private sub-methods.
8. **Forgetting `@Override`** — causes silent no-op if method signature doesn't match.
9. **ActivityLifecycle: wrapping `record` with wrong property class** — `record` is the active property in scope. Wrong class = empty/garbage values.
10. **`arrangementContext.getArrangementId()` returns String** — no `.getValue()` needed.
11. **`Contract.setContractId()` not called first** — all Contract API calls return null without it.
12. **ActivityLifecycle `defaultFieldValues` has two valid signatures** — match the signature to the T24 version or the hook is silently ignored.
13. **Using `double`/`float` for monetary values** (CSD violation) — always use `BigDecimal`.
14. **Hardcoded error/override messages** (CSD violation) — always reference `EB.ERROR` or `OVERRIDE` record IDs.
15. **`validateRecord()` in ActivityLifecycle cannot update core fields** — only local ref fields can be set here; use `defaultFieldValues()` for core field updates.
16. **AA COB vs online** — ALL AA activities (online and COB) go through AA.ARRANGEMENT.ACTIVITY. If an update should not run during COB, check `isService()` and return early.
17. **`generateSecondaryActivity()`** — all `secondaryActivity` values must be set. Partial setup = secondary activity silently not generated.
18. **`da.getFieldValue()` misuse** — **NEVER use this for normal field reads**. The **3-arg form** `da.getFieldValue("APP", "FIELD.NAME", existingStruct).getValue()` IS valid when you need to read a field from a TStructure you already fetched (e.g. a cross-ref join). But **never** use any form as a substitute for the generated getter on the current record's fields. Always use the generated class: `new AaBillDetailsRecord(da.getRecord("AA.BILL.DETAILS", id)).getPaymentDate().getValue()` — not `da.getFieldValue("AA.BILL.DETAILS", "PAYMENT.DATE", struct)`.
19. **`setFilterCriteria()` must return `List<FilterCriteria>`** — the method signature returns the modified list, it is **not** `void`. Always `return filterCriteria;` at the end or the hook silently does nothing.
20. **Kony/Infinity files are NOT T24 L3 Java** — files with `com.konylabs`, `com.dbp`, `com.kony`, `com.temenos.onboarding`, or `JavaService2` imports are Temenos Infinity (DBP) services, not T24 hook customizations. The hook superclasses (`RecordLifecycle`, `ActivityLifecycle`, `ServiceLifecycle`, `Enquiry`) only apply to T24 core customizations.
21. **`ActivityLifecycle` is the correct class name** — there is no `ActivityRecordLifecycle` or `ActivityRecordLifeCycle`. The full import is `com.temenos.t24.api.hook.arrangement.ActivityLifecycle`.
22. **`AaPrdDesTermAmountRecord` vs `AaArrTermAmountRecord`** — `AaPrdDes*` classes are product design-time conditions (what the user enters). `AaArr*` classes are the live running conditions of a booked arrangement. Using the wrong one returns empty fields.
23. **`validateField()` has 4 parameters, not 6** — The real signature is `validateField(String application, String currentRecordId, String fieldData, TStructure currentRecord)`. The `fieldData` param is the current value of the changed field. If you write a 6-param override it silently does nothing.
24. **`Session.setNextVersion()` requires 4 args in real implementations** — `sess.setNextVersion(versionId, function, recordId, generateId)` where `generateId` is a `TBoolean`. The 2-arg form shown in some docs does not match production usage.
25. **`da.getRecord()` can return null** — Always null-check before passing to a record constructor: `TStructure raw = da.getRecord(...); if (raw == null) return;`
26. **`defaultFieldValuesOnHotField()` is a distinct method** — Not the same as `defaultFieldValues()`. It fires only when a hot field (configured in VERSION) changes value. Import `com.temenos.t24.api.complex.eb.templatehook.InputValue` for the 7-param signature.
27. **`T24CoreException` single-arg form is valid for dynamic messages** — `throw new T24CoreException("Account " + id + " invalid")` is the correct pattern when the message must include a runtime value. The 2-arg form `T24CoreException("", "EB-CODE")` is for static EB.ERROR codes (CSD preferred).
