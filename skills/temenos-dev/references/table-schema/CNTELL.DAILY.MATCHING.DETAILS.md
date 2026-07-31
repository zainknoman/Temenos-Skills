# CNTELL.DAILY.MATCHING.DETAILS — Table Schema

> Source: `INSERTS/I_F.CNTELL.DAILY.MATCHING.DETAILS` in `CNTELL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLY.MAT.DTL.COMPANY` | `CntellDailyMatchingDetails_Company` | TField |  | Indicates the company code for the entry. |
| 2 | `DLY.MAT.DTL.REPORT.TYPE` | `CntellDailyMatchingDetails_ReportType` | TField |  | Indicates which report type the entry is relating to. Valid input is IBS for non-contingent entry and OBS for contingent entry. |
| 3 | `DLY.MAT.DTL.ITEM` | `CntellDailyMatchingDetails_Item` | TField |  | Indicates the operation type for entry configured under daily matching parameter. |
| 4 | `DLY.MAT.DTL.DESCRIPTION` | `CntellDailyMatchingDetails_Description` | TField |  | Indicates the description for operation type. |
| 5 | `DLY.MAT.DTL.CURRENCY` | `CntellDailyMatchingDetails_Currency` | TField |  | Indicates the currency for entry. |
| 6 | `DLY.MAT.DTL.TXN.REF` | `CntellDailyMatchingDetails_TxnRef` | TField |  | Indicates the transaction reference for entry. |
| 7 | `DLY.MAT.DTL.ACCOUNT.NUMBER` | `CntellDailyMatchingDetails_AccountNumber` | TField |  | Indicates the account number for entry. |
| 8 | `DLY.MAT.DTL.TXN.CODE` | `CntellDailyMatchingDetails_TxnCode` | TField |  | Indicates the transaction code for transaction or contract, varies by applications. |
| 9 | `DLY.MAT.DTL.DEBIT.AMOUNT` | `CntellDailyMatchingDetails_DebitAmount` | TField |  | Indicates the debit amount for entry. |
| 10 | `DLY.MAT.DTL.CREDIT.AMOUNT` | `CntellDailyMatchingDetails_CreditAmount` | TField |  | Indicates the credit amount for entry. |
| 11 | `DLY.MAT.DTL.REVERSAL.MARKER` | `CntellDailyMatchingDetails_ReversalMarker` | TField |  | Indicates the reversal marker for entry. |
| 12 | `DLY.MAT.DTL.INPUTTER` | `CntellDailyMatchingDetails_Inputter` |  |  |  |
| 13 | `DLY.MAT.DTL.AUTHORISER` | `CntellDailyMatchingDetails_Authoriser` | String |  | Indicates the operator for entry. |
