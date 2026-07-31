# Object Relationship Graph

> Manually curated 2026-06-20. Runtime object graph derived from domain knowledge; not extractable from JAR bytecode.

---

## Relationship Model

```
Class ─── reads/writes ──► T24 Application
Class ─── fires ─────────► Event
Class ─── implements ────► Hook Interface
Hook ─── fires on ───────► Lifecycle Phase
Event ─── triggers ──────► Listener Class
Product ─── depends on ──► Product
Application ─── linked ──► Application (via linked.appl)
```

---

## Class to Application Relationships

| Class | Reads | Writes | Notes |
|-------|-------|--------|-------|
| `AaArrangementActivityRecord` | `AA.ARRANGEMENT.ACTIVITY` | `AA.ARRANGEMENT.ACTIVITY` | Activity hook's primary input record |
| `AaArrangementRecord` | `ARRANGEMENT` | — | Master arrangement — read-only in hooks |
| `AaAccountDetailsRecord` | `AA.ACCOUNT.DETAILS` | `AA.ACCOUNT.DETAILS` | Arrangement status and linked account |
| `AaPrdDesPaymentScheduleRecord` | property record | property record | Wraps `record` param in ActivityLifecycle |
| `AaPrdDesTermAmountRecord` | property record | property record | Term, maturity, amount |
| `AaPrdDesInterestRecord` | property record | property record | Interest rate and basis |
| `AaPrdDesChargeRecord` | property record | property record | Charge/fee amounts |
| `AaPrdDesAccountRecord` | property record | property record | Linked account reference |
| `Contract` (API) | `ARRANGEMENT`, `AA.PRODUCT`, property tables | — | Read-only arrangement conditions API |
| `CustomerRecord` | `CUSTOMER` | `CUSTOMER` | RecordLifecycle on CUSTOMER |
| `EbContractBalancesRecord` | `EB.CONTRACT.BALANCES` | — | Balance types per account |
| `DataAccess.getRecord()` | Any T24 application | — | Generic read via Java DataAccess |
| `DataAccess.selectRecords()` | Any T24 application | — | SELECT query against any application |
| `TransactionData` (updateRecord) | — | Target application | Creates child record via T24 engine |
| `TtContractRecord` | `TT.CONTRACT` | `TT.CONTRACT` | Teller contract (ATM/teller hooks) |
| `FundsTransferRecord` | `FUNDS.TRANSFER` | `FUNDS.TRANSFER` | Payments hooks |

---

## Class to Event Relationships

| Class / Application | Fires Event | Event Name | When |
|--------------------|------------|-----------|------|
| `CUSTOMER` (on auth) | Yes | `CUSTOMER.CREATED` | New customer authorised |
| `CUSTOMER` (on amend auth) | Yes | `CUSTOMER.AMENDED` | Customer amended and authorised |
| `ACCOUNT` (on auth) | Yes | `ACCOUNT.OPENED` | Account opened |
| `ACCOUNT` (on close) | Yes | `ACCOUNT.CLOSED` | Account closed |
| `FUNDS.TRANSFER` (on auth) | Yes | `FUNDS.TRANSFER.AUTHORISED` | FT authorised |
| `AA.ARRANGEMENT.ACTIVITY` (on auth) | Yes | `AA.ARRANGEMENT.ACTIVITY.AUTHORISED` | Activity authorised |
| `ARRANGEMENT` (on open auth) | Yes | `ARRANGEMENT.OPENED` | New arrangement opened |
| `ARRANGEMENT` (on close auth) | Yes | `ARRANGEMENT.CLOSED` | Arrangement closed |
| `TP.PAYMENT.ORDER` (on auth) | Yes | `PAYMENT.ORDER.AUTHORISED` | Payment order authorised |

---

## Class to Hook Relationships

### RecordLifecycle Hook Bindings

| T24 Application | Hook Binding Location | Typical Hook Methods |
|----------------|----------------------|---------------------|
| `CUSTOMER` | `VERSION.CUSTOMER,*` — `HOOK.CLASS` field | defaultFieldValues, validateRecord |
| `ACCOUNT` | `VERSION.ACCOUNT,*` — `HOOK.CLASS` field | checkId, defaultFieldValues, validateRecord |
| `FUNDS.TRANSFER` | `VERSION.FUNDS.TRANSFER,*` — `HOOK.CLASS` | validateRecord, updateRecord |
| `TT.CONTRACT` | `VERSION.TT.CONTRACT,*` — `HOOK.CLASS` | validateRecord |
| Custom applications | `VERSION.<APP>,*` — `HOOK.CLASS` | All RecordLifecycle methods |

### ActivityLifecycle Hook Bindings

| AA Property Class | Hook Binding (AA.PRODUCT config) | Hook Class |
|------------------|----------------------------------|-----------|
| `PAYMENT.SCHEDULE` | Property `PAYMENT.SCHEDULE` → HOOK.CLASS | Extends ActivityLifecycle |
| `INTEREST` | Property `INTEREST` → HOOK.CLASS | Extends ActivityLifecycle (or Calculation) |
| `COMMITMENT` | Property `COMMITMENT` → HOOK.CLASS | Extends ActivityLifecycle |
| `CHARGE` | Property `CHARGE` → HOOK.CLASS | Extends ActivityLifecycle (or Calculation) |
| `ACCOUNT` | Property `ACCOUNT` → HOOK.CLASS | Extends ActivityLifecycle |

### ServiceLifecycle Hook Bindings

| COB Service | Service Application | Hook Class |
|------------|--------------------|-----------| 
| Custom batch | `COB.SERVICE` → `SERVICE.ROUTINE` | Extends ServiceLifecycle |
| AA batch | `AA.COB.SERVICE` → routine | Extends ServiceLifecycle or jBC |

---

## Product to Product Relationships

| Product | Depends On | Via |
|---------|-----------|-----|
| AA (Arrangement Architecture) | CUSTOMER, ACCOUNT | Arrangement links customer and account |
| AA Lending | ACCOUNT, FUNDS.TRANSFER | Disbursement and repayment FTs |
| AA Deposits | ACCOUNT | Settlement account |
| TPH (Payment Hub) | FUNDS.TRANSFER, ACCOUNT, CUSTOMER | Settlement, debit/credit |
| ATM/Teller | ACCOUNT, CUSTOMER | Cash withdrawal/deposit linked to account |
| DE (Document Engine) | Any authorised application | Event fires on application auth |
| COB Services | All product applications | Processes all live records at EOD |
| Limits (CR) | CUSTOMER, ACCOUNT, AA Lending | Credit limit linked to customer/arrangement |

---

## Application Link Relationships

T24 applications are linked via the `LINKED.APPL` mechanism:

| Primary Application | Linked Application | Relationship |
|--------------------|-------------------|-------------|
| `ARRANGEMENT` | `ACCOUNT` | One arrangement → linked current account |
| `ARRANGEMENT` | `FUNDS.TRANSFER` | AA disbursement/settlement FTs |
| `ACCOUNT` | `AC.ENTRY` | Account → posting entries |
| `FUNDS.TRANSFER` | `ACCOUNT` | FT debits/credits linked accounts |
| `CUSTOMER` | `ACCOUNT` | Customer → all accounts |
| `CUSTOMER` | `ARRANGEMENT` | Customer → all arrangements |
| `TP.PAYMENT.ORDER` | `FUNDS.TRANSFER` | Payment order → resulting FT |
| `TT.CONTRACT` | `ACCOUNT` | Teller transaction → customer account |

---

## Full Relationship Matrix

### AA Framework Object Web

```
AA.PRODUCT ─ defines ──────────────────────► Property Classes
                                                    │
                                                    │ instantiated as
                                                    ▼
AA.ARRANGEMENT.ACTIVITY ─ creates/amends ──► ARRANGEMENT
        │                                         │
        │ triggers ActivityLifecycle              │ links to
        │ hooks for each property                 ▼
        ▼                                   ACCOUNT (AA.ACCOUNT.DETAILS)
  Property Records                                │
  (AaPrdDesXxx)                                   │ has balances in
        │                                         ▼
        │ read via Contract API             EB.CONTRACT.BALANCES
        ▼
  Contract.getConditionForProperty()
        │
        │ returns
        ▼
  TStructure → wrapped as AaPrdDesXxxRecord
```

### EB.API Record Lifecycle Web

```
VERSION ─ HOOK.CLASS ──────────────────────► RecordLifecycle subclass
                                                    │
                                                    │ called at each lifecycle point
                                                    ▼
T24 Application record ─── validated by ──► validateRecord()
                        ─── defaulted by ──► defaultFieldValues()
                        ─── authorised by ──► updateRecord() / postUpdateRequest()
                        ─── ID checked by ──► checkId()
```

### Event Framework Web

```
T24 Application (AUTHORISE)
        │
        │ fires
        ▼
EB.EVENT.DEFINITION
        │
        │ routes to
        ▼
Event Listener Class (Java, extends EventListener)
  OR
DE ApplicationHandoff routine (jBC)
  OR
External notification (webhook, JMS)
```
