# DE Array.5 Position Mappings

`Array.5` (parameter 5 of `DE.API.ApplicationHandoff`) is the data carrier. Positions differ by side and application.

## F.DE.O.HANDOFF Row Structure

`F.DE.O.HANDOFF` is a 10-row dimensioned array (rows 0–9 user-populated; row 10 reserved):

| Row | Content |
|-----|---------|
| 0.0 | DELIVERY.KEY — @ID of F.DE.O.HANDOFF record (hardcoded by APPLICATION.HANDOFF) |
| 0.1 | MAPPING.KEY — DE.MAPPING record ID passed by application (hardcoded) |
| 0.2 | BANK.DATE — T24 bank date on which transaction was performed (hardcoded) |
| 1 | Typically `R.NEW` — the entire transaction record |
| 2–8 | Application-specific values (position-mapped in DE.MAPPING) |
| 9 | **User-defined** — populated by custom subroutine only; T24 does not use this |
| 10 | Reserved for later use |

The `Array.5` value passed in parameter 5 of `DE.API.ApplicationHandoff` maps to row 5 of F.DE.O.HANDOFF. All position references (1–30) refer to sub-positions within that row (e.g., `5.1`, `5.2` … `5.30`).

Viewing HANDOFF contents: enquiry `DE.HANDOFF.DETS` → select by DELIVERY.REF.

---

---

## FT (Funds Transfer) — <PKG>.DE.FT.DETAILS

### DR Side (`DrArray.5`)

| Pos | Variable | Source |
|-----|----------|--------|
| 1 | `ftId` | `EB.SystemTables.getIdNew()` |
| 2 | `company` | `getRNew(FT.Contract.FundsTransfer.CoCode)` |
| 3 | `department` | `getRNew(FT.Contract.FundsTransfer.DeptCode)` |
| 4 | `debitCustomerId` | from `debitAccountRecord<AC.AccountOpening.Account.Customer>` |
| 5 | _(empty — CR customer slot)_ | |
| 6 | `debitCustomerLanguage` | `debitCustomerRecord<ST.Customer.Customer.EbCusLanguage>` |
| 7 | _(empty)_ | |
| 8 | `debitCustomerCompany` | `debitCustomerRecord<ST.Customer.Customer.EbCusCoCode>` |
| 9 | _(empty)_ | |
| 10 | `debitAccountBalance` | `FMTS(availableDrBalance,",")` |
| 11 | _(empty)_ | |
| 12 | `debitAccount` | `getRNew(FT.Contract.FundsTransfer.DebitAcctNo)` |
| 13 | _(empty)_ | |
| 14 | `'-':FMTS(debitAmount,",")` | minus-prefixed debit amount |
| 15 | _(empty)_ | |
| 16 | `debitValueDate` | `YYYY-MM-DD HH:MM` |
| 17 | _(empty)_ | |
| 18 | `debitCurrency` (display name) | language-resolved from `ST.CurrencyConfig.Currency.EbCurCcyName` |
| 19 | _(empty)_ | |
| 20 | `totalCommissionAmount` | `getRNew(FT.Contract.FundsTransfer.TotalChargeAmount)` stripped & formatted |
| 21 | _(empty)_ | |
| 22 | `'-':amountDebited` | minus-prefixed `AmountDebited` stripped |
| 23 | `drDescription` | language-resolved from `FT.Config.TxnTypeCondition.FtSixDescription` |
| 24 | `entryNo` | `LocalRef FUNDS.TRANSFER / ENTRY.NO` |
| 25 | `entryOp` | `LocalRef FUNDS.TRANSFER / ENTRY.OP` |
| 26 | `entryConf` | `LocalRef FUNDS.TRANSFER / ENTRY.CONF` |
| 27 | `debitAccountName` | `debitAccountRecord<AC.AccountOpening.Account.AccountTitleOne>` |
| 28 | `debitDocumentCode` | from event mapping `<Pkg>HDrDocCode` |
| 29 | `debitUserRef` | from event mapping `<Pkg>HDrUserRef` |
| 30 | `debitParamCode` | from event mapping `<Pkg>HDrParamCode` |

### CR Side (`CrArray.5`)

| Pos | Variable | Source |
|-----|----------|--------|
| 1 | `ftId` | same as DR |
| 2 | `company` | same as DR |
| 3 | `department` | same as DR |
| 4 | _(empty — DR customer slot)_ | |
| 5 | `creditCustomerId` | from `creditAccountRecord<AC.AccountOpening.Account.Customer>` |
| 6 | _(empty)_ | |
| 7 | `creditCustomerLanguage` | `creditCustomerRecord<ST.Customer.Customer.EbCusLanguage>` |
| 8 | _(empty)_ | |
| 9 | `creditCustomerCompany` | `creditCustomerRecord<ST.Customer.Customer.EbCusCoCode>` |
| 10 | _(empty)_ | |
| 11 | `creditAccountBalance` | `FMTS(availableCrBalance,",")` |
| 12 | _(empty)_ | |
| 13 | `creditAccount` | `getRNew(FT.Contract.FundsTransfer.CreditAcctNo)` |
| 14 | _(empty)_ | |
| 15 | `'+':FMTS(creditAmount,",")` | plus-prefixed credit amount |
| 16 | _(empty)_ | |
| 17 | `creditValueDate` | `YYYY-MM-DD HH:MM` |
| 18 | _(empty)_ | |
| 19 | `creditCurrency` (display name) | language-resolved |
| 20 | `totalCommissionAmount` | same as DR pos 20 |
| 21 | `'+':amountCredited` | plus-prefixed `AmountCredited` stripped |
| 22 | `crDescription` | language-resolved description |
| 24 | `entryNo` | same as DR |
| 25 | `entryOp` | same as DR |
| 26 | `entryConf` | same as DR |
| 27 | `creditAccountName` | `creditAccountRecord<AC.AccountOpening.Account.AccountTitleOne>` |
| 28 | `creditDocumentCode` | from event mapping `<Pkg>HCrDocCode` |
| 29 | `creditUserRef` | from event mapping `<Pkg>HCrUserRef` |
| 30 | `creditParamCode` | from event mapping `<Pkg>HCrParamCode` |

> **Note:** Positions 23 on CR side maps crDescription (shifted one from DR, which uses pos 23 for drDescription). Pos 21 on CR = amount credited; pos 22 = DR uses amountDebited (with minus sign).

---

## TT (Teller) — <PKG>.DE.TT.DETAILS

`Array1.5` (Side 1 / account1) and `Array2.5` (Side 2 / account2) share the same layout:

| Pos | Variable | Source |
|-----|----------|--------|
| 1 | `ttId` | `EB.SystemTables.getIdNew()` |
| 2 | `account1` | `getRNew(TT.Contract.Teller.TeAccountOne)` |
| 3 | `account2` | `getRNew(TT.Contract.Teller.TeAccountTwo)` |
| 4 | `amountLcy1` | `getRNew(TT.Contract.Teller.TeAmountLocalOne)` formatted |
| 5 | `amountLcy2` | `getRNew(TT.Contract.Teller.TeAmountLocalTwo)` formatted |
| 6 | `currency1` | language-resolved CCY name |
| 7 | `currency2` | language-resolved CCY name |
| 8 | `customer1` | `getRNew(TT.Contract.Teller.TeCustomerOne)` |
| 9 | `customer2` | `getRNew(TT.Contract.Teller.TeCustomerTwo)` |
| 10 | `exposureDate1` | `getRNew(TT.Contract.Teller.TeExposureDateOne)` |
| 11 | `exposureDate2` | `getRNew(TT.Contract.Teller.TeExposureDateTwo)` |
| 12 | `valueDate1` | `YYYY-MM-DD HH:MM` |
| 13 | `valueDate2` | `YYYY-MM-DD HH:MM` |
| 14 | `ac1CurrentBalance` | `FMTS(availableBalance1,",")` |
| 15 | `ac2CurrentBalance` | `FMTS(availableBalance2,",")` |
| 16 | `narrative1` | `getRNew(TT.Contract.Teller.TeNarrativeOne)` |
| 17 | `narrative2` | `getRNew(TT.Contract.Teller.TeNarrativeTwo)` |
| 18 | `customer1Company` | `customer1Record<ST.Customer.Customer.EbCusCoCode>` |
| 19 | `customer2Company` | `customer2Record<ST.Customer.Customer.EbCusCoCode>` |
| 20 | `department` | `getRNew(TT.Contract.Teller.TeDeptCode)` |
| 21 | `txnCompany` | `getRNew(TT.Contract.Teller.TeCoCode)` |
| 22 | `customer1Language` | `customer1Record<ST.Customer.Customer.EbCusLanguage>` |
| 23 | `customer2Language` | `customer2Record<ST.Customer.Customer.EbCusLanguage>` |
| 24 | `chargeAmountLcy` | `getRNew(TT.Contract.Teller.TeChrgAmtLocal)` formatted |
| 25 | `newCustomerBalance` | `getRNew(TT.Contract.Teller.TeNewCustBal)` formatted |

---

## ApplicationHandoff Call Pattern

```jBC
Rec1 = ""  ;* not used
Rec2 = ""  ;* not used
Rec3 = ""  ;* not used
Rec4 = ""  ;* not used
Rec5 = Array.5
Rec6 = ""  ;* not used
Rec7 = ""  ;* not used
Rec8 = ""  ;* not used
Rec9 = ""  ;* not used
VKey = ""  ;* OUTPUT — DE message key
MapKey = DrMappingKeys<1,JJ>  ;* DE.MAPPING id
ErrorMsg = ""  ;* OUTPUT — error text

DE.API.ApplicationHandoff(Rec1, Rec2, Rec3, Rec4, Rec5, Rec6, Rec7, Rec8, Rec9, MapKey, VKey, ErrorMsg)
```

### DeliveryOutref Multi-Value Append

```jBC
deliveryRef = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DeliveryOutref)
IF deliveryRef EQ "" THEN
    deliveryRef = VKey
ELSE
    deliveryRef<1,-1> = VKey
END
EB.SystemTables.setRNew(FT.Contract.FundsTransfer.DeliveryOutref, deliveryRef)
```

---

## Amount Strip Pattern

T24 amounts carry a 3-character currency prefix (e.g., `IQD1234567.89`):

```jBC
rawAmount = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.AmountDebited)
strippedAmount = rawAmount[4, LEN(rawAmount)]   ;* remove first 3 chars
formattedAmount = FMTS(strippedAmount, ",")
currency = rawAmount[1, 3]                       ;* extract CCY code
```

For `TotalChargeAmount` the same strip applies but default to `"0"` when blank:
```jBC
IF totalCommissionAmount EQ "" THEN totalCommissionAmount = "0"
totalCommissionAmount = totalCommissionAmount[4, LEN(totalCommissionAmount)]
totalCommissionAmount = FMTS(totalCommissionAmount, ",")
```
