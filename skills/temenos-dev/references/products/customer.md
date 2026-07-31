# Customer Product Reference

> Manually curated 2026-06-20. Sources: ST_* JAR analysis, T24 Technical training, L3 Java CSD standards.

---

## Key Applications

| Application | Purpose |
|------------|---------|
| `CUSTOMER` | Core customer master record (CIF) |
| `ST.CUSTOMER.LOCAL` | Customer local reference — bank-specific extensions |
| `KYC.QUESTIONNAIRE` | KYC data collection application |
| `CUSTOMER.LINK` | Customer-to-customer relationship links |
| `CUSTOMER.SECURITY` | Customer security / access control |
| `ST.CUST.PRODUCT.PARAM` | Customer product parameter |
| `ST.CUST.DISP.ACC.SUMMARY` | Customer account summary display |
| `ST.NAICS.INDUSTRY` | North American industry classification |
| `CUSTOMER.ACCOUNT.OFFICER` | Account officer assignment |

---

## Key Classes

| Class | Package | JAR | Role |
|-------|---------|-----|------|
| `CustomerRecord` | `com.temenos.t24.api.records.customer` | `ST_Customer.jar` | Typed access to CUSTOMER fields |
| `CustomerServiceAPI` | `com.temenos.services.customer` | `t24-ST_CustomerService-t24service.jar` | Public service API for customer data |
| `CustomerServiceProxyAPI` | `com.temenos.services.customer` | `t24-ST_CustomerService-t24service.jar` | Proxy version of CustomerService API |
| `CustomerService` (interface) | `com.temenos.services.customer` | `t24-ST_CustomerService-t24service.jar` | Service interface |
| `CustomerServiceImpl` | `com.temenos.services.customer` | `t24-ST_CustomerService-t24service.jar` | Service implementation |

### Key Service Data Classes (ST_CustomerService-Data.jar)

| Class | Purpose |
|-------|---------|
| `Address` | Customer address details |
| `AddressField` | Address field container |
| `AddressIDDetails` | Address identification details |
| `AccountOfficer` | Account officer assignment |
| `AggregateBalancesRecord` | Aggregated balance view |
| `Audit` | Audit trail fields |

---

## CUSTOMER Application — Key Fields

| Field | T24 Name | Type | Description |
|-------|---------|------|-------------|
| Customer No | `CUSTOMER` (ID) | Numeric | Unique CIF number |
| Short Name | `SHORT.NAME` | MV | Abbreviated name for display |
| Full Name | `NAME.1` | Single | First line of full name |
| Name Line 2 | `NAME.2` | Single | Second line of name |
| Sector | `SECTOR` | Single | Customer sector code (industry) |
| Nationality | `NATIONALITY` | Single | ISO country code |
| Residence | `RESIDENCE` | Single | Country of residence |
| Language | `LANGUAGE` | Single | Preferred communication language |
| Type | `CUSTOMER.TYPE` | Single | INDIVIDUAL, CORPORATE, etc. |
| Date of Birth | `DATE.OF.BIRTH` | Date | For individuals |
| Tax ID | `TAX.ID` | MV | Tax identification numbers |
| Risk Class | `RISK.CLASS` | Single | AML/KYC risk classification |
| Status | `STATUS` | Single | 1=Active |
| Address | `STREET` / `TOWN.COUNTRY` | MV | Customer address |
| Phone | `PHONE.NUMBER` | MV | Contact numbers |
| Email | `EMAIL.ADDRESS` | MV | Email addresses |

---

## KYC and Compliance

### KYC Fields on CUSTOMER

| Field | Purpose |
|-------|---------|
| `RISK.CLASS` | Overall AML risk classification (LOW, MEDIUM, HIGH) |
| `KYC.COMPLETE` | KYC documentation status |
| `LAST.REVIEW.DATE` | Date of last KYC review |
| `NEXT.REVIEW.DATE` | Scheduled next review |
| `PEP.FLAG` | Politically Exposed Person flag |
| `SANCTION.FLAG` | Sanctions match flag |

### Compliance Hooks

To validate customer data at input time, extend `RecordLifecycle` and bind to the `CUSTOMER` application:

```java
public class CustomerKYCHook extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        CustomerRecord custRec = new CustomerRecord(currentRecord);

        // Mandatory KYC check
        if (custRec.getRiskClass().getValue().isEmpty()) {
            custRec.getRiskClass().setError("RISK.CLASS.MANDATORY");
        }

        // PEP name screening
        String shortName = custRec.getShortName(0).getValue();
        if (isPEP(shortName)) {
            custRec.getPepFlag().setOverride("POSSIBLE.PEP.MATCH");
        }

        currentRecord.set(custRec.toStructure());
        return custRec.getValidationResponse();
    }
}
```

---

## Local References

### LocalRefGroup Pattern

Banks extend CUSTOMER with bank-specific fields using local reference groups defined in `ST.CUSTOMER.LOCAL`:

```java
// Read local reference field from CustomerRecord
CustomerRecord custRec = new CustomerRecord(currentRecord);
String localField = custRec.getLocalRefField("MY.BANK.L.FIELD").getValue();
custRec.getLocalRefField("MY.BANK.L.FIELD").setValue("value");
```

### ST.CUSTOMER.LOCAL

The `ST.CUSTOMER.LOCAL` application stores the local reference data. It is linked to CUSTOMER by the same customer number. Banks define local fields in the `LOCAL.REF.FIELD` group on the `ST.CUST.PARAM` configuration record.

### Key Local Reference Tables

| Table | Purpose |
|-------|---------|
| `ST.CUSTOMER.LOCAL` | Bank-specific customer extension fields |
| `KYC.QUESTIONNAIRE` | KYC questionnaire answers |
| `ST.CUST.PRODUCT.PARAM` | Product eligibility parameters |
| `CUSTOMER.ACCOUNT.OFFICER` | Account officer assignments by product |

---

## Hooks and Events

### Lifecycle Hook Binding

```
VERSION     CUSTOMER,CUSTOMER.OPEN
HOOK.CLASS  com.mybank.customer.CustomerOpenHook
```

### Common Hook Use Cases

| Hook Method | Use Case |
|-------------|---------|
| `checkId` | Validate/format customer number (if manual) |
| `defaultFieldValues` | Set sector, language, country defaults |
| `validateRecord` | Cross-field KYC validation, duplicate name check |
| `postUpdateRequest` | Create linked local reference record, notify CRM |
| `updateRecord` | Create `ST.CUSTOMER.LOCAL` on new customer |

### Customer Events

T24 fires events on CUSTOMER lifecycle transitions. Register listeners in the event framework:

| Event | When Fired |
|-------|-----------|
| `CUSTOMER.CREATED` | New customer authorised |
| `CUSTOMER.AMENDED` | Customer record amended and authorised |
| `CUSTOMER.CLOSED` | Customer status set to closed |
| `CUSTOMER.KYC.COMPLETED` | KYC.COMPLETE field set to YES |

---

## Code Patterns

### Reading CUSTOMER in jBC

```basic
$INSERT I_COMMON
$INSERT I_EQUATE
$INSERT I_F.CUSTOMER

FN.CUST = 'F.CUSTOMER'
F.CUST  = ''
CALL OPF(FN.CUST, F.CUST)

CALL F.READ(FN.CUST, CUST.NO, R.CUST, F.CUST, ERR)
IF ERR THEN
    * Customer not found
END ELSE
    CUST.NAME  = R.CUST<F.CUSTOMER.SHORT.NAME,1>
    CUST.SECTOR = R.CUST<F.CUSTOMER.SECTOR>
END
```

### Reading CUSTOMER in Java (DataAccess)

```java
DataAccess da = new DataAccess(this);
CustomerRecord custRec = new CustomerRecord(da.getRecord("CUSTOMER", customerId));
String shortName = custRec.getShortName(0).getValue();
String sector    = custRec.getSector().getValue();
String residence = custRec.getResidence().getValue();
```

### Creating CUSTOMER via OFS

```basic
OFS.MSG  = 'CUSTOMER,CUSTOMER.OPEN//'
OFS.MSG := 'SHORT.NAME:1:::' : CUST.NAME : '/'
OFS.MSG := 'NAME.1:::' : FULL.NAME : '/'
OFS.MSG := 'SECTOR:::1001/'
OFS.MSG := 'NATIONALITY:::US/'
OFS.MSG := 'RESIDENCE:::US/'
OFS.MSG := 'LANGUAGE:::1/'
CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)

OFS.STAT = FIELD(FIELD(OFS.MSG,'/',3),',',1)
IF OFS.STAT EQ 1 THEN
    NEW.CUST.NO = FIELD(OFS.MSG,'/',1)
END
```
