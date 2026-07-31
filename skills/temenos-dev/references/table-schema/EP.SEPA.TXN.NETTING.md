# EP.SEPA.TXN.NETTING — Table Schema

> Source: `INSERTS/I_F.EP.SEPA.TXN.NETTING` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EP.NET.SETTLEMENT.ACCOUNT` | `EpSepaTxnNetting_SettlementAccount` | TField |  | This field specifies the Customer Accout to which the Credit has to happen. This will be available in the Inward xml message Validation Rules Value upto 16 type ACC(Account Number) Value should exist in ACCOUNT Application |
| 2 | `EP.NET.ORG.FILE.REF` | `EpSepaTxnNetting_OrgFileRef` | TField |  | This field holds the value of SEPA.INWARD.FILES record ID corresponding to the Inward xml message. Validation Rules Value upto 70 type ANY(Any Character) |
| 3 | `EP.NET.ORG.TXN.REF` | `EpSepaTxnNetting_OrgTxnRef` | TField |  | This field holds the value of the Reference for the particular Transaction. Validation Rules Value upto 70 type ANY(Any Character) |
| 4 | `EP.NET.ORG.TXN.AMOUNT` | `EpSepaTxnNetting_OrgTxnAmount` | TField |  | This field specifies the Total Amount of the corresponding Bulk from the PAIN.008 Inward File. Validation Rules Value upto 12 type AMT(AMOUNT) |
| 5 | `EP.NET.ORG.CUST.SIGN` | `EpSepaTxnNetting_OrgCustSign` | TField |  | This field specifies if it is Credit or Debit Transaction. Allowed Values CR DB |
| 6 | `EP.NET.R.TXN.AMOUNT` | `EpSepaTxnNetting_RTxnAmount` |  |  |  |
| 7 | `EP.NET.R.FILE.REF` | `EpSepaTxnNetting_RFileRef` |  |  |  |
| 8 | `EP.NET.R.TXN.REF` | `EpSepaTxnNetting_RTxnRef` |  |  |  |
| 9 | `EP.NET.R.TXN.SIGN` | `EpSepaTxnNetting_RTxnSign` |  |  |  |
| 10 | `EP.NET.RESERVED5` | `EpSepaTxnNetting_Reserved5` |  |  |  |
| 11 | `EP.NET.RESERVED4` | `EpSepaTxnNetting_Reserved4` |  |  |  |
| 12 | `EP.NET.RESERVED3` | `EpSepaTxnNetting_Reserved3` |  |  |  |
| 13 | `EP.NET.RESERVED2` | `EpSepaTxnNetting_Reserved2` |  |  |  |
| 14 | `EP.NET.RESERVED1` | `EpSepaTxnNetting_Reserved1` |  |  |  |
| 15 | `EP.NET.BALANCE.AMOUNT` | `EpSepaTxnNetting_BalanceAmount` | TField |  | This field specifies the Balance Amount after adjusting the values in R.TXN.AMOUNT with the value in ORG.TXN.AMOUNT Validation Rules Value upto 12 type AMT(AMOUNT) |
| 16 | `EP.NET.LINKED.FT.ID` | `EpSepaTxnNetting_LinkedFtId` | TField |  | This fields holds the Key to the FT generated for payment of Crediting the Customer on the settlement date during COB. Validation Rules Value upto 26 type ANY(Any Character) |
