# DE Applications, Field Equates, and $USING Packages

## T24 Package Reference

### EB.SystemTables
Common system table accessors used in all handoff routines.

| Method | Returns |
|--------|---------|
| `EB.SystemTables.getRNew(fieldEquate)` | Field value from the current transaction record (new/live values) |
| `EB.SystemTables.setRNew(fieldEquate, value)` | Set field on current transaction record |
| `EB.SystemTables.getIdNew()` | Current transaction ID |
| `EB.SystemTables.getToday()` | Today's date in T24 internal format |
| `EB.SystemTables.getLccy()` | Local currency code |

### FT.Contract.FundsTransfer — key field equates

| Equate | Meaning |
|--------|---------|
| `FT.Contract.FundsTransfer.TransactionType` | FT transaction type code |
| `FT.Contract.FundsTransfer.DebitAcctNo` | Debit account number |
| `FT.Contract.FundsTransfer.CreditAcctNo` | Credit account number |
| `FT.Contract.FundsTransfer.DebitCurrency` | Debit currency code |
| `FT.Contract.FundsTransfer.CreditCurrency` | Credit currency code |
| `FT.Contract.FundsTransfer.DebitAmount` | Debit amount (CCY-prefixed) |
| `FT.Contract.FundsTransfer.CreditAmount` | Credit amount (CCY-prefixed) |
| `FT.Contract.FundsTransfer.AmountDebited` | Total amount debited (CCY-prefixed) |
| `FT.Contract.FundsTransfer.AmountCredited` | Total amount credited (CCY-prefixed) |
| `FT.Contract.FundsTransfer.TotalChargeAmount` | Total charges (CCY-prefixed) |
| `FT.Contract.FundsTransfer.CoCode` | Company code |
| `FT.Contract.FundsTransfer.DeptCode` | Department code |
| `FT.Contract.FundsTransfer.DateTime` | Transaction datetime (`YYYYMMDDHHMMSS`) |
| `FT.Contract.FundsTransfer.LocalRef` | Multi-value local reference field |
| `FT.Contract.FundsTransfer.DeliveryOutref` | DE delivery output reference (multi-value) |
| `FT.Contract.FundsTransfer.DebitValueDate` | Debit value date |
| `FT.Contract.FundsTransfer.CreditValueDate` | Credit value date |
| `FT.Contract.FundsTransfer.DebitTheirRef` | Debit party their reference |
| `FT.Contract.FundsTransfer.CreditTheirRef` | Credit party their reference |

### TT.Contract.Teller — key field equates

| Equate | Meaning |
|--------|---------|
| `TT.Contract.Teller.TeTransactionCode` | Teller transaction type code |
| `TT.Contract.Teller.TeAccountOne` | Account 1 (typically debit) |
| `TT.Contract.Teller.TeAccountTwo` | Account 2 (typically credit) |
| `TT.Contract.Teller.TeCustomerOne` | Customer on account 1 |
| `TT.Contract.Teller.TeCustomerTwo` | Customer on account 2 |
| `TT.Contract.Teller.TeCurrencyOne` | Currency for account 1 |
| `TT.Contract.Teller.TeCurrencyTwo` | Currency for account 2 |
| `TT.Contract.Teller.TeAmountLocalOne` | LCY amount on account 1 |
| `TT.Contract.Teller.TeAmountLocalTwo` | LCY amount on account 2 |
| `TT.Contract.Teller.TeChrgAmtLocal` | Charge amount in LCY |
| `TT.Contract.Teller.TeNewCustBal` | New customer balance |
| `TT.Contract.Teller.TeDrDenom` | Denomination (DR side) |
| `TT.Contract.Teller.TeDrUnit` | Units (DR side) |
| `TT.Contract.Teller.TeExposureDateOne` | Exposure date for account 1 |
| `TT.Contract.Teller.TeExposureDateTwo` | Exposure date for account 2 |
| `TT.Contract.Teller.TeNarrativeOne` | Narrative for account 1 |
| `TT.Contract.Teller.TeNarrativeTwo` | Narrative for account 2 |
| `TT.Contract.Teller.TeDeptCode` | Department code |
| `TT.Contract.Teller.TeCoCode` | Company code |
| `TT.Contract.Teller.TeDateTime` | DateTime (`YYYYMMDDHHMMSS`) |

### AC.AccountOpening.Account — key field equates
`$USING AC.AccountOpening` | T24 app: `ACCOUNT` | INSERTS prefix: `AC.`

| Equate | Pos | Meaning |
|--------|-----|---------|
| `AC.AccountOpening.Account.Customer` | 1 | Linked customer ID |
| `AC.AccountOpening.Account.Category` | 2 | Account category code |
| `AC.AccountOpening.Account.AccountTitle1` | 3 | Account title line 1 |
| `AC.AccountOpening.Account.AccountTitle2` | 4 | Account title line 2 |
| `AC.AccountOpening.Account.ShortTitle` | 5 | Short title |
| `AC.AccountOpening.Account.Mnemonic` | 6 | Account mnemonic |
| `AC.AccountOpening.Account.Currency` | 8 | Account currency |
| `AC.AccountOpening.Account.AccountOfficer` | 11 | Account officer |
| `AC.AccountOpening.Account.PostingRestrict` | 13 | Posting restriction |
| `AC.AccountOpening.Account.OnlineActualBal` | 25 | Online actual balance |
| `AC.AccountOpening.Account.OnlineClearedBal` | 26 | Online cleared balance |
| `AC.AccountOpening.Account.WorkingBalance` | 27 | Current working balance |
| `AC.AccountOpening.Account.ArrangementId` | 181 | Linked AA arrangement ID |
| `AC.AccountOpening.Account.CoCode` | 252 | Company code |

### ST.Customer.Customer — key field equates
`$USING ST.Customer` | T24 app: `CUSTOMER` | INSERTS prefix: `EB.CUS.`
Aliases are derived from the INSERTS second column (`Customer_<field>` → `<field>`), NOT from the `EB.CUS.` prefix.

| Equate | Pos | Meaning |
|--------|-----|---------|
| `ST.Customer.Customer.Mnemonic` | 1 | Customer mnemonic |
| `ST.Customer.Customer.ShortName` | 2 | Customer short name |
| `ST.Customer.Customer.Name1` | 3 | Full name line 1 |
| `ST.Customer.Customer.Name2` | 4 | Full name line 2 |
| `ST.Customer.Customer.Street` | 5 | Street address |
| `ST.Customer.Customer.TownCountry` | 7 | Town and country |
| `ST.Customer.Customer.PostCode` | 8 | Postal code |
| `ST.Customer.Customer.Country` | 9 | Country of residence |
| `ST.Customer.Customer.Sector` | 23 | Sector classification |
| `ST.Customer.Customer.AccountOfficer` | 24 | Account officer |
| `ST.Customer.Customer.Nationality` | 28 | Nationality code |
| `ST.Customer.Customer.Language` | 45 | Language: `'1'`=English, `'2'`=Arabic |
| `ST.Customer.Customer.PostingRestrict` | 46 | Posting restriction |
| `ST.Customer.Customer.DateOfBirth` | 64 | Date of birth |
| `ST.Customer.Customer.LocalRef` | 179 | Local reference (multi-value) |
| `ST.Customer.Customer.CoCode` | 186 | Company code |

### AA.Framework.Arrangement — key field equates
`$USING AA.Framework` | T24 app: `AA.ARRANGEMENT` | INSERTS prefix: `AA.ARR.`
Aliases: strip leading `AA.`, camelCase remainder (e.g. `AA.ARR.CURRENCY` → `ArrCurrency`).

| Equate | Pos | Meaning |
|--------|-----|---------|
| `AA.Framework.Arrangement.ArrCustomer` | 1 | Primary customer ID |
| `AA.Framework.Arrangement.ArrCurrency` | 8 | Arrangement currency |
| `AA.Framework.Arrangement.ArrCoCode` | 9 | Company code |
| `AA.Framework.Arrangement.ArrArrStatus` | 11 | Arrangement status |
| `AA.Framework.Arrangement.ArrStartDate` | 12 | Arrangement start/effective date |
| `AA.Framework.Arrangement.ArrLinkedApplId` | 14 | Linked application ID (e.g. ACCOUNT number) |
| `AA.Framework.Arrangement.ArrProductLine` | 15 | Product line (e.g. `LENDING`) |
| `AA.Framework.Arrangement.ArrProductGroup` | 16 | Product group |
| `AA.Framework.Arrangement.ArrProduct` | 17 | Product code |

### AA.PaymentSchedule.AccountDetails — key field equates
`$USING AA.PaymentSchedule` | T24 app: `AA.ACCOUNT.DETAILS` | INSERTS prefix: `AA.AD.`
Aliases: strip leading `AA.`, camelCase (e.g. `AA.AD.MATURITY.DATE` → `AdMaturityDate`).

| Equate | Pos | Meaning |
|--------|-----|---------|
| `AA.PaymentSchedule.AccountDetails.AdContractDate` | 1 | Contract date |
| `AA.PaymentSchedule.AccountDetails.AdValueDate` | 2 | Value date |
| `AA.PaymentSchedule.AccountDetails.AdStartDate` | 3 | Start date |
| `AA.PaymentSchedule.AccountDetails.AdMaturityDate` | 6 | Maturity / expiry date |
| `AA.PaymentSchedule.AccountDetails.AdArrAgeStatus` | 7 | Arrangement age/delinquency status |
| `AA.PaymentSchedule.AccountDetails.AdCoolingDate` | 9 | Cooling-off end date |

### BF.ConBalanceUpdates.EBContractBalances — key field equates
`$USING BF.ConBalanceUpdates` | T24 app: `EB.CONTRACT.BALANCES` | INSERTS prefix: `ECB.`

| Equate | Pos | Meaning |
|--------|-----|---------|
| `BF.ConBalanceUpdates.EBContractBalances.Currency` | 1 | Balance currency |
| `BF.ConBalanceUpdates.EBContractBalances.TypeSysdate` | 2 | Balance type + sysdate (MV key) |
| `BF.ConBalanceUpdates.EBContractBalances.OpenBalance` | 5 | Opening balance (MV per type) |
| `BF.ConBalanceUpdates.EBContractBalances.Application` | 19 | Source application |
| `BF.ConBalanceUpdates.EBContractBalances.Customer` | 22 | Customer ID |
| `BF.ConBalanceUpdates.EBContractBalances.OnlineActualBal` | 70 | Online actual balance |
| `BF.ConBalanceUpdates.EBContractBalances.WorkingBalance` | 72 | Working balance |
| `BF.ConBalanceUpdates.EBContractBalances.DateTime` | _(sys)_ | DateTime (`YYYYMMDDHHMMSS`) |

Read: `BF.ConBalanceUpdates.EBContractBalances.Read(id, err)` — falls back to `.ReadHis(id:';1', err)` for closed accounts.

### ST.CurrencyConfig.Currency — key field equates

| Equate | Meaning |
|--------|---------|
| `ST.CurrencyConfig.Currency.EbCurCcyName` | Multi-lingual currency name; `<1,1>` = English, `<1,2>` = Arabic |

### FT.Config.TxnTypeCondition — key field equates

| Equate | Meaning |
|--------|---------|
| `FT.Config.TxnTypeCondition.FtSixDescription` | Multi-lingual transaction description; `<1,1>` = English, `<1,2>` = Arabic |

### `<PKG>.LocalDevelopments.<Pkg>DeEventMapping` — field equates

| Equate | Meaning |
|--------|---------|
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HDrDeMapping` | Multi-value: DR DE.MAPPING key(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HDrCategory` | Multi-value: DR account category filter(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HDrDocCode` | Multi-value: DR document code(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HDrUserRef` | Multi-value: DR user reference(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HDrParamCode` | Multi-value: DR parameter code(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HCrDeMapping` | Multi-value: CR DE.MAPPING key(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HCrCategory` | Multi-value: CR account category filter(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HCrDocCode` | Multi-value: CR document code(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HCrUserRef` | Multi-value: CR user reference(s) |
| `<PKG>.LocalDevelopments.<Pkg>DeEventMapping.<Pkg>HCrParamCode` | Multi-value: CR parameter code(s) |

### `<PKG>.LocalDevelopments.<Pkg>GatewayParam` — field equates

| Equate | Meaning |
|--------|---------|
| `<PKG>.LocalDevelopments.<Pkg>GatewayParam.<Pkg>HUsername` | API username |
| `<PKG>.LocalDevelopments.<Pkg>GatewayParam.<Pkg>HPassword` | API password |
| `<PKG>.LocalDevelopments.<Pkg>GatewayParam.<Pkg>HEndpointUrl` | API endpoint URL |
| `<PKG>.LocalDevelopments.<Pkg>GatewayParam.<Pkg>HTokenUrl` | OAuth token URL |

### DE Applications for T24 Configuration

| Application | Purpose |
|-------------|---------|
| `DE.MESSAGE` | Defines variable names for a message type; ID = numeric (SWIFT range 100-999; print outside range) |
| `DE.MAPPING` | Maps variables in DE.MESSAGE to positions in F.DE.O.HANDOFF; ID = `<MsgType>.<App>.<CurrNo>` e.g. `900.FT.1` |
| `DE.PRODUCT` | Decides carrier, address, format version, language; ID = `<Company>.[C-Cust|A-Acct.]<MsgType>.<App>` |
| `DE.ADDRESS` | Holds physical delivery address (PRINT/SWIFT/EMAIL/SMS/SECUREMSG) per customer |
| `DE.CARRIER` | Details of each carrier (PRINT/SWIFT/XML); links Format Module + Carrier Module + Interface |
| `DE.FORMAT.PRINT` | Print advice layout; ID = `<MsgType>.<AppFormat>.<Version>.<Language>` e.g. `900.1.1.GB` |
| `DE.FORMAT.SWIFT` | SWIFT data content layout; ID = `<MsgType>.<AppFormat>.<Version>` e.g. `900.1.1` (one per type) |
| `DE.FORMAT.XML` | XML layout for EMAIL/SMS/SECUREMSG; ID = same format as FORMAT.PRINT |
| `DE.FORM.TYPE` | Defines form width (chars), depth (lines), and target printer |
| `DE.TRANSLATION` | Translation table for TABLE conversion; ID = prefix+value e.g. `SW20`, `FTAC` |
| `DE.AUTO.TRANSLATION` | Utility to populate DE.TRANSLATION from T24 files |
| `DE.ROUTING` | Live index updated when DE.PRODUCT authorised; speeds DE.PRODUCT lookup |
| `DE.O.HEADER` | Tracks status of each outward advice; ID = Delivery Reference ID |
| `DE.I.HEADER` | Tracks status of each inward message; ID = Delivery Reference ID (starts with R) |
| `DE.DISP.CONTROL` | Disposition control rules; ID = numeric; conditions based on DE.O.HEADER fields |
| `DE.ALTERNATE` | Re-route address override; ID mirrors DE.PRODUCT but ends with carrier sequence |
| `DE.PARM` | System parameters; record `SYSTEM.STATUS` lists valid carriers |
| `DE.BIC` | SWIFT BIC directory; used to validate `DE.ADDRESS.DELIVERY.ADDRESS` |
| `DE.BIC.PARAMETER` | Parameter for BIC validation (field VALIDATE.BIC) |
| `DE.INTERFACE` | Interface routing definition; links external SWIFT/email gateway to DE |
| `DE.CUSTOMER.PREFERENCES` | IB customer alert preferences; auto-creates DE.PRODUCT records |
| `DE.MESSAGE.GROUP` | Groups message types for DE.CUSTOMER.PREFERENCES |
| `EB.TRANSFORM` | XSLT stylesheet record for XML carrier; ID = `DE.<FORMAT.XML ID>.<CARRIER>` |
| `FT.TXN.TYPE.CONDITION` | FT transaction type config; must have `DR.ADVICE.REQD=Y` and `CR.ADVICE.REQD=Y` |
| `CATEGORY` | Account category codes (validated in event mapping) |

#### DE.MESSAGE — Key Fields

| Field | Values / Notes |
|-------|----------------|
| `FIELD.NAME` | Variable name (e.g. `DATE`, `TRANS.REF`) |
| `LENGTH` | Max characters (for SWIFT: follow standard e.g. date=6) |
| `PRINT.TYPE` | `A`=alphanumeric, `N`=numeric (default `A`) |
| `SINGLE.MULTI` | `S`=single, `M`=multi-value (default `S`) |
| `MANDATORY` | `Y`=mandatory; if no value in HANDOFF → message goes to REPAIR |
| `COPIES` | `Y`/`NO` — `NO` prevents copies for this message type |
| `TRANSLATION` | `Y`/`NO` — if `NO` only first language in LANGUAGE table allowed |
| `DELETE` | `Y`/`NO` — `NO` prevents deletion |
| `APPLICATION.QUEUE` | Inward: T24 app to receive the message (default FT if blank); must exist in EB.PRODUCT |
| `INWARD.OFS.RTN` | Inward: routine to generate OFS string; must exist in PGM.FILE |
| `IN.OFS.VERSION` | Inward: record ID in VERSION application |
| `OFS.SOURCE` | Inward: record ID in OFS.SOURCE application |

#### DE.MAPPING — Key Fields

| Field | Notes |
|-------|-------|
| `DESCRIPTION` | Free text |
| `INPUT.REC.NO` | Row in F.DE.O.HANDOFF containing R.NEW (e.g. `1`) |
| `INPUT.REC.DESC` | Description of Input Rec No |
| `INPUT.FILE` | STANDARD.SELECTION name (e.g. `FUNDS.TRANSFER`) |
| `FIELD.NAME` | Variable name from DE.MESSAGE |
| `INPUT.POSITION` | Position in F.DE.O.HANDOFF (e.g. `2.2`) or `1` for INPUT.REC.NO row |
| `INPUT.NAME` | Field name in INPUT.FILE for field-name mapping (e.g. `DEBIT.CURRENCY`) |
| `HEADER.NAME` | Field in DE.O.HEADER to copy this value into |

DE.MAPPING ID components: APP component is first 2 chars of what's passed to APPLICATION.HANDOFF (e.g. `FTAC` → reads `900.FT.1`; `AC` = sub-product code, usable in DE.PRODUCT).

#### DE.PRODUCT — ID Format and Search Order

**ID**: `<COMPANY.CODE>[.C-<CustNo>|.A-<AcctNo>].<MsgType>.<App>`
- Examples: `GB0010001.900.FT`, `GB0010001.C-111204.900.FT`, `GB0010001.A-15377.950.ALL`
- `MsgType` = DE.MESSAGE ID or `ALL`; `App` = two-char app code + optional sub-product, or `ALL`

**Search order** (most specific wins):
1. Account-specific (`A-<AcctNo>`)
2. Customer-specific (`C-<CustNo>`)
3. Message-specific (no customer/account)
4. Application-specific (ALL message types)
5. Most generic: `ALL.ALL`

**Key fields**:
| Field | Values |
|-------|--------|
| `MESSAGE.STATUS` | `NORMAL`/`NONE`=format and send; `HOLD`=map only (→F.DE.O.HOLD.KEY); `DELETE`=map only, discard |
| `CARRIER.ADDR.NO` | e.g. `PRINT.1`, `SWIFT.1`, `EMAIL.1`, `SMS.1`; multi-value (multiple carriers) |
| `LANGUAGE` | Language code for formatting |
| `FORMAT` | Format version number used in DE.FORMAT.PRINT ID |
| `COPIES` | Number of copies (default 1; ignored for SWIFT) |
| `MDR.CUSTOMER` | Additional customers for copies (PRINT/EMAIL only; customer/account-level products only) |

#### DE.ADDRESS — ID Format

`<COMPANY.CODE>.C-<CustomerNo>.<TYPE>.<SeqNo>` or `<COMPANY.CODE>.A-<AcctNo>.<TYPE>.<SeqNo>`
- Examples: `GB0010001.C-100224.PRINT.1`, `GB0010001.C-100336.EMAIL.1`
- `PRINT.1` created automatically when CUSTOMER record authorised (cannot be reversed/deleted/edited)
- `EMAIL.1`, `SMS.1`, `SECUREMSG.1` created from CUSTOMER fields EMAIL, SMS, SECURE.MESSAGE
- `SWIFT.1` must be created manually; `DELIVERY.ADDRESS` = BIC code

**Key fields**:
| Field | Notes |
|-------|-------|
| `DELIVERY.ADDRESS` | SWIFT BIC code (for SWIFT/TELEX addresses) |
| `HOLD.OUTPUT` | `Y` = write to F.CUSTOMER.HOLD instead of printing; retrieve via HOLD.CONTROL |

#### DE.CARRIER — Key Fields

| Field | Values |
|-------|--------|
| `FORMAT.MODULE` | `PRINT` → DE.FORMAT.PRINT; `SWIFT` → DE.FORMAT.SWIFT; `XML` → DE.FORMAT.XML |
| `CARRIER.MODULE` | `PRINT` = physical printer; `SWIFT` = default SWIFT queue; `GENERIC` = via Interface |
| `INTERFACE` | ID of record in DE.INTERFACE (used when CARRIER.MODULE=GENERIC) |
| `OUT.IF.ROUTINE` | Routine invoked after formatting to transport the message |

#### DE.FORMAT.PRINT — Key Fields

| Field | Notes |
|-------|-------|
| `FORM.TYPE` | ID of DE.FORM.TYPE record (defines width/depth/printer) |
| `LINES` | Row position on page (`+00`=same row, `+02`=2 rows down) |
| `INDENT` | Column position |
| `FIELD.TEXT` | Variable name from DE.MESSAGE, or string in `"quotes"`, or keyword (`TO.ADDRESS`) |
| `CONVERSION` | `DATE/F`=full date; `WORDS`=amount in words (reads DE.WORDS); `TABLE XXX`=DE.TRANSLATION lookup; `LINK*App>Field>Pos`=read another T24 app; `CUS*FIELD`=read DE.ADDRESS field; `AMT`=remove sign |
| `MASK` | Display mask (e.g. `/` delimiter in transaction ref) |
| `DEPENDENT.ON` | Variable name for conditional print |
| `DEPEND.OPERAND` | `EQ`, `NE`, `GT`, `LT` |
| `DEPEND.COND` | Condition value |
| `PAGE.OVERFLOW` | `YES`=allow field to overflow to next page; `NO`=goes to repair |

#### DE.O.HEADER — Key Fields

| Field | Values |
|-------|--------|
| `MESSAGE.TYPE` | DE.MESSAGE ID (from DE.MAPPING first component) |
| `APPLICATION.FORMAT` | Passed by application logic; second component of DE.FORMAT.PRINT ID |
| `APPLICATION` | Two-char application code (e.g. FT, FX) |
| `DISPOSITION` | `UNFORMATTED` → `FORMATTED` → `REPAIR` (advice-level) |
| `MSG.DISPOSITION` | Per-copy status: `UNFORMATTED`, `FORMATTED`, `ACK`, `REPAIR`, `DELETED`, `HOLD`, `RESUBMIT`, `REROUTE` |

To **resubmit** a repaired advice: change `DISPOSITION` to `Resubmit` and authorise → moves from repair queue to unformatted queue; history preserved.
To **re-route**: change `MSG.DISPOSITION` to `REROUTE` → system reads DE.ALTERNATE for replacement carrier/address.

#### DE.I.HEADER — Key Fields

| Field | Values |
|-------|--------|
| `MESSAGE.TYPE` | Extracted from incoming SWIFT message |
| `DISPOSITION` | `UNFORMATTED` (received correctly) → `OFS FORMATTED` (processed) |
| `CARRIER.ADDR.NO` | Carrier by which message was received |
| `TO.ADDRESS` | BIC of receiving bank (from SWIFT header) |
| `FROM.ADDRESS` | BIC of sending bank (from SWIFT header) |

### EB.LocalReferences.GetLocRef

Used in FT handoff to retrieve local-reference positions:
```jBC
EB.LocalReferences.GetLocRef('FUNDS.TRANSFER','ENTRY.NO', EntryNoPos)
EB.LocalReferences.GetLocRef('FUNDS.TRANSFER','ENTRY.OP', EntryOpPos)
EB.LocalReferences.GetLocRef('FUNDS.TRANSFER','ENTRY.CONF', EntryConfPos)

entryNo   = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.LocalRef)<1,EntryNoPos>
entryOp   = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.LocalRef)<1,EntryOpPos>
entryConf = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.LocalRef)<1,EntryConfPos>
```

### DE.Outward.OPrintWords

Converts a numeric amount to words (Arabic or English):
```jBC
DE.Outward.OPrintWords(amount:'*':currencyCode, wordsVar, 'AR', LineLength, NoOfLines, ErrMsg)
CHANGE '*' TO ' ' IN wordsVar
```
- Language code `'AR'` = Arabic words; `'EN'` = English words.
- Uses `*` as separator between amount and currency in the input string.

### EB.Logging

```jBC
$INSERT I_Logger
sMessage<EB.Logging.EbLogMsgAppln>   = "DE.O.HEADER"
sMessage<EB.Logging.EbLogMsgRoutine> = "<PKG>.DE.PRINT.INTERFACE"
sMessage<EB.Logging.EbLogMsgModule>  = "DE"
sMessage<EB.Logging.EbLogMsgLogParam>= sContext
sMessage<EB.Logging.EbLogMsgDesc>    = "Description"
sMessage<EB.Logging.EbLogMsgDetails> = payload
sMessage<EB.Logging.EbLogMsgLogLevel>= "INFO"   ;* or "ERROR"
Logger.info(sContext, sMessage)
Logger.error(sContext, sMessage)
```

### EB.Template — Table Definition Methods

Used in template routines (`.b` suffix, called once at startup):

| Method | Purpose |
|--------|---------|
| `setTableName('APP.NAME')` | Full T24 application name |
| `setTableTitle('Screen Title')` | Screen/enquiry title |
| `setTableStereotype('H')` | `H`=Header, `U`=Unauthorised, `L`=Live, `W`=Work, `T`=Transaction |
| `setTableProduct('EB')` | Product (must exist on EB.PRODUCT) |
| `setTableClassification('INT')` | File classification |
| `setTableSystemclearfile('Y')` | Clear on system clear flag |
| `setTableEquateprefix('<PKG>.H')` | Generates `I_F.<PKG>.DE.EVENT.MAPPING` |

### EB.Template — Field Definition Methods

Used in `.FIELDS` routines:

| Method | Purpose |
|--------|---------|
| `EB.SystemTables.setF(Z, "XX<FIELD.NAME")` | Define field; `<` = multi-value, `-` = sub-value, `>` = sub-multi-value |
| `EB.SystemTables.setN(Z, '35')` | Field length |
| `EB.SystemTables.setT(Z, 'A')` | Type: `A`=Alpha, `ANY`=Any |
| `EB.SystemTables.setCheckfile(Z, "TABLE":@FM:descField:@FM:"L.A")` | Validate against another table |
| `EB.SystemTables.setV(Z + 9)` | Total number of fields (usually last field Z + padding) |
