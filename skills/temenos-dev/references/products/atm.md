# ATM / Teller Reference

> Manually curated 2026-06-20. Sources: TT_* JAR analysis, ATM-POS-INTERFACE functional guide, T24 Technical training.

---

## Key Applications

| Application | Purpose |
|------------|---------|
| `TT.CONTRACT` | Teller transaction/contract input |
| `TT.TELLER` | Teller session — tracks cash in hand |
| `TT.DENOMINATION` | Cash denomination definition per currency |
| `TT.BRANCH.LIMIT` | Branch-level cash holding limit |
| `TT.RECON` | Teller end-of-day reconciliation |
| `TT.STOCK` | Vault / cash stock management |
| `TT.GROUP.CONDITION` | Teller group charge conditions |
| `TT.PASSBOOK` | Passbook update operations |
| `TT.PRINT.SLIP` | Teller receipt/slip printing |

---

## Key Classes (from JAR Analysis)

| Class | JAR | Package | Role |
|-------|-----|---------|------|
| (TT_Contract classes) | `TT_Contract.jar` | `com.temenos.t24` | Teller contract jBC compiled classes |
| (TT_Foundation classes) | `TT_Foundation.jar` | `com.temenos.t24` | ATM/teller foundation framework classes |
| (TT_TellerFinancialService) | `TT_TellerFinancialService.jar` | `com.temenos.t24` | Teller financial service classes |
| `FHMConnection` | `CAATMD_CardtronicsFHM.jar` | `com.temenos.plugin.cardtronicsfhm` | Cardtronics ATM FHM connection thread |
| `FHMListener` | `CAATMD_CardtronicsFHM.jar` | `com.temenos.plugin.cardtronicsfhm` | Cardtronics ATM FHM message listener |
| `FHMParser` | `CAATMD_CardtronicsFHM.jar` | `com.temenos.plugin.cardtronicsfhm` | ATM message parser |
| `ISOUtil` | `CAATMD_CardtronicsFHM.jar` | `com.temenos.plugin.cardtronicsfhm` | ISO 8583 utility |
| `FHMConnection` | `CAATMI_EverlinkFHM.jar` | `com.temenos.plugin.everlinkfhm` | Everlink ATM adapter |
| `ISOConnection` | `CAATMI_ISOListener.jar` | `com.temenos.plugin.isolistener` | Generic ISO 8583 listener |
| `ISOListener` | `CAATMI_ISOListener.jar` | `com.temenos.plugin.isolistener` | ISO 8583 listener (AbstractListener) |
| `ISOParser` | `CAATMI_ISOListener.jar` | `com.temenos.plugin.isolistener` | ISO 8583 parser |

### ATM Adapter JARs

| JAR | Adapter Purpose |
|-----|----------------|
| `CAATMD_CardtronicsFHM.jar` | Cardtronics ATM integration |
| `CAATMI_EverlinkFHM.jar` | Everlink ATM integration |
| `CAATMI_ISOListener.jar` | Generic ISO 8583 ATM listener |

---

## ATM Integration Architecture

T24 ATM integration uses the FHM (Front-end Host Message) pattern with ISO 8583 messaging:

```
ATM Terminal
    |
    |  ISO 8583 message
    v
FHM Listener (CAATMI_ISOListener / FHM adapters)
    |
    |  Internal message format
    v
TT.CONTRACT input (via OFS or direct)
    |
    v
T24 Core (ACCOUNT debit/credit, FUNDS.TRANSFER)
    |
    v
FHM Response → ATM Terminal
```

### ATM Transaction Types

| Type | T24 Application | Description |
|------|----------------|-------------|
| Cash Withdrawal | `TT.CONTRACT` | Debit account, dispense cash |
| Cash Deposit | `TT.CONTRACT` | Accept cash, credit account |
| Balance Inquiry | Account enquiry | Read account balance |
| Mini Statement | Statement enquiry | Last N transactions |
| Fund Transfer | `FUNDS.TRANSFER` or `TP.PAYMENT.ORDER` | Inter-account transfer |
| PIN Change | `CUSTOMER.SECURITY` | Update PIN |
| Cheque Book Request | Application input | Order chequebook |

---

## Cash Management

### Vault Operations

Cash flow hierarchy:
```
Vault (Branch)
    → Till (Teller's cash in hand)
        → Cash Dispense / Accept per transaction
```

Key operations:
- **Vault Top-up**: Branch vault receives cash from central/head office
- **Till Loading**: Teller receives cash from vault at start of day
- **Till Surrender**: Teller returns excess cash to vault during/end of day
- **Branch Limit Enforcement**: `TT.BRANCH.LIMIT` prevents vault exceeding configured maximum

### Till Management

`TT.TELLER` tracks each teller's cash position:

| Field | Purpose |
|-------|---------|
| `TELLER.ID` | Unique teller identifier |
| `CURRENCY` | Currency of the till |
| `OPENING.BALANCE` | Cash at start of day |
| `CURRENT.BALANCE` | Real-time cash in hand |
| `CLOSING.BALANCE` | Cash at end of day |
| `STATUS` | OPEN / CLOSED |

### Branch Cash Limit

`TT.BRANCH.LIMIT` defines:
- Maximum cash allowed in branch vault
- Alert threshold (e.g. 80% of limit triggers notification)
- Currency and denomination breakdown

---

## Denomination Handling

### TT.DENOMINATION Configuration

```
TT.DENOMINATION     USD
    DENOMINATION:1  100    (100 USD notes)
    DENOMINATION:2   50    (50 USD notes)
    DENOMINATION:3   20    (20 USD notes)
    DENOMINATION:4   10    (10 USD notes)
    DENOMINATION:5    5    (5 USD notes)
    DENOMINATION:6    1    (1 USD coin)
    DENOMINATION:7    0.25 (quarter)
```

### Denomination Count at Dispense

T24 automatically calculates optimal denomination mix for cash dispense based on:
1. Requested amount
2. Available denominations in `TT.DENOMINATION`
3. Current stock in `TT.TELLER` per denomination

### Denomination Reconciliation

At end of day, the teller counts physical cash per denomination. `TT.RECON` records:
- Expected count (from system)
- Actual count (teller entry)
- Difference (overage/shortage)
- Approval workflow for discrepancies

---

## Teller Operations

### Transaction Types on TT.CONTRACT

| Transaction | Description |
|-------------|-------------|
| `CASH.PAYMENT` | Cash payment from customer to bank |
| `CASH.WITHDRAWAL` | Cash withdrawal from account |
| `CHEQUE.DEPOSIT` | Deposit cheque to account |
| `CASH.PURCHASE` | Purchase of foreign currency cash |
| `CASH.SALE` | Sale of foreign currency cash |
| `TRAVELLERS.CHEQUE` | Issue/encash travellers cheques |
| `MANAGER.CHEQUE` | Issue manager's cheque |
| `TELLER.TRANSFER` | Transfer between teller tills |

### TT.CONTRACT Key Fields

| Field | Purpose |
|-------|---------|
| `TELLER.ID` | Processing teller |
| `ACCOUNT.DEBIT` | Account to debit |
| `ACCOUNT.CREDIT` | Account to credit |
| `TRANSACTION.TYPE` | Type of teller transaction |
| `AMOUNT` | Transaction amount |
| `CURRENCY` | Transaction currency |
| `DENOMINATION.GIVEN` | Denominations tendered by customer |
| `DENOMINATION.RECEIVED` | Denominations given to customer |
| `EXCHANGE.RATE` | FX rate (for foreign currency) |
| `VALUE.DATE` | Value date |

---

## Code Patterns

### Hook on Teller Transaction (Java)

Bind a `RecordLifecycle` hook to `TT.CONTRACT,VERSION.NAME`:

```java
public class TellerValidationHook extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        // TT.CONTRACT typed record class
        TtContractRecord ttRec = new TtContractRecord(currentRecord);

        // Validate amount limit
        BigDecimal amount = new BigDecimal(ttRec.getAmount().getValue());
        BigDecimal limit  = new BigDecimal("10000");
        if (amount.compareTo(limit) > 0) {
            ttRec.getAmount().setOverride("AMOUNT.EXCEEDS.LIMIT");
        }

        currentRecord.set(ttRec.toStructure());
        return ttRec.getValidationResponse();
    }
}
```

### Reading Teller Balance (jBC)

```basic
$INSERT I_COMMON
$INSERT I_EQUATE
$INSERT I_F.TT.TELLER

FN.TT = 'F.TT.TELLER'
F.TT  = ''
CALL OPF(FN.TT, F.TT)

CALL F.READ(FN.TT, TELLER.ID, R.TT, F.TT, ERR)
IF NOT(ERR) THEN
    CURR.BAL = R.TT<F.TT.TELLER.CURRENT.BALANCE>
END
```

### ATM Balance Enquiry via OFS

```basic
* ATM triggers balance enquiry via OFS
OFS.MSG  = 'ACCOUNT,ACCOUNT.ENQUIRY/I//' : ACCOUNT.NO
CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)

* Extract balance from response
ACC.BAL = FIELD(OFS.MSG, ':::', 2)
```

---

## ATM Parameters Setup

Key ATM configuration applications:

| Application | Purpose | Key Fields |
|-------------|---------|-----------|
| `TT.DENOMINATION` | Denomination notes/coins per currency | Currency, denominations |
| `TT.BRANCH.LIMIT` | Branch vault cash limit | Branch, currency, max amount |
| `TT.GROUP.CONDITION` | Teller group charge rules | Charge table, conditions |
| `CAATM.PARAMETERS` (if exists) | ATM global parameters | ATM count, timeout settings |

### ATM BIN Configuration

ATM card BIN routing is configured to map card BIN ranges to acquiring banks and transaction routing:

```
ATM.BIN     (BIN range)
    BIN.RANGE.START  400000
    BIN.RANGE.END    499999
    ACQUIRING.BANK   VISA.INT
    ROUTING.FLAG     LOCAL / INTERNATIONAL
```
