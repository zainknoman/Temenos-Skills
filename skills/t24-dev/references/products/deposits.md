# Deposits Product Reference

> Manually curated 2026-06-20. Covers both classic TD module and AA-based deposits.

---

## Key Applications

| Application | Purpose |
|------------|---------|
| `TD.DEPOSIT` | Classic term deposit master record |
| `TD.ADVISE` | Term deposit advice/notification |
| `AA.ARRANGEMENT.ACTIVITY` | AA-based deposit opening and amendment |
| `AA.TERM.DEPOSIT` | AA term deposit product application |
| `AA.NOTICE.WITHDRAWAL` | Notice period withdrawal request |
| `AA.MATURITY` | Maturity instruction |
| `AA.SAVINGS.ACCOUNT` | AA savings account product |
| `AA.RECURRING.DEPOSIT` | Recurring deposit product |
| `EB.CONTRACT.BALANCES` | Balance types per arrangement (used for interest, principal) |

---

## Key Classes (AA Deposits from JAR Analysis)

| Class | JAR | Package | Role |
|-------|-----|---------|------|
| `Calculation` | `AA_CalculationHook.jar` | `com.temenos.t24.api.hook.arrangement` | Interest calculation hooks |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `com.temenos.t24.api.hook.arrangement` | General AA activity hook |
| `Bill` | `AA_BillApi.jar` | `com.temenos.t24.api.arrangement` | Bill (charge demand) access API |
| `Contract` | `AA_ContractApi.jar` | `com.temenos.t24.api.arrangement.accounting` | Read arrangement property conditions |
| `NoticeWithdrawalRecord` | `AA_NoticeWithdrawal.jar` | `com.temenos.t24.api.records` | Notice withdrawal data |

### AA Property Record Classes for Deposits

| Property Class | Record Class | Key Fields |
|---------------|-------------|-----------|
| `COMMITMENT` | `AaPrdDesTermAmountRecord` | `getTerm()`, `getMaturityDate()`, `getAmount()` |
| `INTEREST` | `AaPrdDesInterestRecord` | `getFixedRate()`, `getInterestBasis()`, `getRateCalcType()` |
| `PAYMENT.SCHEDULE` | `AaPrdDesPaymentScheduleRecord` | `getPaymentType()`, `getPaymentFrequency()` |
| `ACCOUNT` | `AaPrdDesAccountRecord` | `getAccountReference()` |

---

## Maturity and Rollover

### Rollover Types

| Type | Description |
|------|-------------|
| `NO.ROLLOVER` | Deposit closes at maturity |
| `AUTO.ROLLOVER` | Rolls over automatically at maturity with same terms |
| `ROLLOVER.PRINCIPAL` | Rolls principal only; interest paid out |
| `ROLLOVER.PRINCIPAL.INTEREST` | Rolls principal + interest into new deposit |
| `MANUAL.ROLLOVER` | Waits for manual instruction at maturity |

### Rollover Hook Pattern

Use `generateSecondaryActivity` in `ActivityLifecycle` to trigger rollover:

```java
@Override
public void generateSecondaryActivity(AaAccountDetailsRecord accountDetailRecord,
        AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
        AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
        TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
        SecondaryActivity secondaryActivity) {

    String arrangementId = arrangementContext.getArrangementId();

    // Get rollover instruction from local ref
    AaPrdDesTermAmountRecord termRec = new AaPrdDesTermAmountRecord(record);
    String rollIns = termRec.getLocalRefField("L.ROLL.INS").getValue();

    if ("AUTO.ROLLOVER".equals(rollIns)) {
        secondaryActivity.setActivity("DEPOSITS-ROLLOVER-ARRANGEMENT");
        secondaryActivity.setProperty("COMMITMENT");
        secondaryActivity.setFieldName("TERM");
        // Keep same term
        secondaryActivity.setFieldValue(termRec.getTerm().getValue());
    }
}
```

### Maturity Date Calculation

```java
// In defaultFieldValues or validateRecord:
AaPrdDesTermAmountRecord termRec = new AaPrdDesTermAmountRecord(record);
String term = termRec.getTerm().getValue(); // e.g. "12M", "2Y"

// Parse term
String termNum    = term.substring(0, term.length() - 1);
String termMarker = term.substring(term.length() - 1);
int months = termMarker.equals("Y") ? 12 * Integer.parseInt(termNum)
                                    : Integer.parseInt(termNum);

// Compute maturity date using Date API
com.temenos.t24.api.system.Date dateApi = new com.temenos.t24.api.system.Date(this);
String valueDate = arrangementActivityRecord.getEffectiveDate().toString();
String matDate   = dateApi.addMonths(valueDate, months);
termRec.setMaturityDate(matDate);
record.set(termRec.toStructure());
```

---

## Notice Withdrawal

### Notice Period Types

| Type | Description |
|------|-------------|
| Fixed period | Mandatory notice period (e.g. 30 days) |
| Instant access | No notice required; may have penalty |
| Conditional | Notice waived on penalty payment |

### Penalty Calculation on Early Withdrawal

Early withdrawal penalties are typically configured as a CHARGE property on the deposit product. The penalty logic is implemented in a `Calculation` hook:

```java
// Calculation hook — calculateCharge method
@Override
public void calculateCharge(String arrangementId, String propertyId,
        TStructure chargeRecord, TStructure arrangementRecord) {

    AaPrdDesChargeRecord charge = new AaPrdDesChargeRecord(chargeRecord);
    Contract contract = new Contract(this);
    contract.setContractId(arrangementId);

    // Get principal and rate from COMMITMENT property
    AaPrdDesTermAmountRecord term = (AaPrdDesTermAmountRecord)
        contract.getCommitmentCondition("COMMITMENT");
    BigDecimal principal = new BigDecimal(term.getAmount().getValue());

    // Apply penalty rate (e.g., 1% of principal)
    BigDecimal penaltyRate = new BigDecimal("0.01");
    BigDecimal penaltyAmt = principal.multiply(penaltyRate);
    charge.setFixedAmount(penaltyAmt.toPlainString());

    chargeRecord.set(charge.toStructure());
}
```

---

## Classic TD Module

### TD.DEPOSIT Key Fields

| Field | Purpose |
|-------|---------|
| `CUSTOMER` | Deposit owner customer number |
| `CURRENCY` | Deposit currency |
| `PRINCIPAL.AMOUNT` | Initial deposit amount |
| `TERM` | Term (e.g. 90D, 6M, 1Y) |
| `VALUE.DATE` | Deposit start date |
| `MATURITY.DATE` | Calculated maturity date |
| `INT.RATE` | Fixed interest rate |
| `INT.BASIS` | Interest accrual basis (e.g. ACT/360) |
| `ROLLOVER.TYPE` | Rollover instruction |
| `ROLLOVER.DATE` | Effective date of rollover |
| `PRINCIPAL.SETT.ACCT` | Settlement account for principal |
| `INT.SETT.ACCT` | Settlement account for interest |
| `PAYMENT.METHOD` | How interest is paid (CAPITALISE, CREDIT.ACCOUNT) |

### Reading TD.DEPOSIT in jBC

```basic
$INSERT I_COMMON
$INSERT I_EQUATE
$INSERT I_F.TD.DEPOSIT

FN.TD = 'F.TD.DEPOSIT'
F.TD  = ''
CALL OPF(FN.TD, F.TD)
CALL F.READ(FN.TD, DEPOSIT.ID, R.TD, F.TD, ERR)

PRINCIPAL = R.TD<F.TD.DEPOSIT.PRINCIPAL.AMOUNT>
MATURITY  = R.TD<F.TD.DEPOSIT.MATURITY.DATE>
INT.RATE  = R.TD<F.TD.DEPOSIT.INT.RATE>
```

---

## AA vs Classic TD: When to Use Which

| Scenario | Use AA | Use Classic TD |
|----------|--------|----------------|
| New implementations | Yes | No (legacy) |
| Complex product features (bundles, offset) | Yes | No |
| Simple fixed-term product | Either | Yes |
| Integration with AA lending (linked deposit) | Yes | No |
| Existing TD portfolio | No (unless migrating) | Yes |

---

## Common Activity Names (AA Deposits)

```
DEPOSITS-NEW-ARRANGEMENT
DEPOSITS-CLOSE-ARRANGEMENT
DEPOSITS-ROLLOVER-ARRANGEMENT
DEPOSITS-UPDATE-PO.WITHDRAWAL
DEPOSITS-SALARY.CR-ARRANGEMENT
DEPOSITS-UPDATE-NOTICE.WITHDRAWAL
DEPOSITS-CHANGE-INTEREST.RATE
DEPOSITS-PARTIAL.REDEMPTION
```

---

## Code Patterns

### Open AA Term Deposit via OFS

```basic
OFS.MSG  = 'AA.ARRANGEMENT.ACTIVITY,DEPOSITS.NEW//'
OFS.MSG := 'PRODUCT:::TD.12MONTH/'
OFS.MSG := 'CUSTOMER:1:::' : CUST.NO : '/'
OFS.MSG := 'CURRENCY:::USD/'
OFS.MSG := 'EFFECTIVE.DATE:::' : TODAY : '/'
OFS.MSG := 'TERM:::12M/'
OFS.MSG := 'AMOUNT:::50000/'
CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)

OFS.STAT = FIELD(FIELD(OFS.MSG,'/',3),',',1)
IF OFS.STAT EQ 1 THEN
    ARR.ID = FIELD(OFS.MSG,'/',1)
END
```
