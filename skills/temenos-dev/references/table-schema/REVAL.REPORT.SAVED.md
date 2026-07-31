# REVAL.REPORT.SAVED — Table Schema

> Source: `INSERTS/I_F.REVAL.REPORT.SAVED` in `AC_CurrencyPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REVAL.R.UNIQUE.TXN.ID` | `RevalReportSaved_UniqueTxnId` |  |  |  |
| 2 | `REVAL.R.REVAL.TYPE` | `RevalReportSaved_RevalType` |  |  |  |
| 3 | `REVAL.R.REVAL.RATE` | `RevalReportSaved_RevalRate` |  |  |  |
| 4 | `REVAL.R.DAYS.SINCE.SPOT` | `RevalReportSaved_DaysSinceSpot` |  |  |  |
| 5 | `REVAL.R.FOR.AMOUNT` | `RevalReportSaved_ForAmount` |  |  |  |
| 6 | `REVAL.R.BEF.LCY.AMOUNT` | `RevalReportSaved_BefLcyAmount` |  |  |  |
| 7 | `REVAL.R.AFT.LCY.AMOUNT` | `RevalReportSaved_AftLcyAmount` |  |  |  |
| 8 | `REVAL.R.PL.AMOUNT` | `RevalReportSaved_PlAmount` |  |  |  |
| 9 | `REVAL.R.PL.ADJ.AMOUNT` | `RevalReportSaved_PlAdjAmount` |  |  |  |
| 10 | `REVAL.R.STATUS` | `RevalReportSaved_Status` |  |  |  |
| 11 | `REVAL.R.IFRS.DEAL.AMT.TODATE` | `RevalReportSaved_IfrsDealAmtTodate` | TField |  | Stores the Un-realised Profit or Loss at Deal Level in local currency till todate. |
| 12 | `REVAL.R.IFRS.DEAL.AMT.TODAY` | `RevalReportSaved_IfrsDealAmtToday` | TField |  | Stores the Un-realised Profit or Loss at Deal Level in local currency for today. |
| 13 | `REVAL.R.IFRS.NPV.RATE` | `RevalReportSaved_IfrsNpvRate` | TField |  | The value in this field is the key used to obtain the discount rate from PERIODIC.INTEREST table, which is used for calculating the NPV of the deal. |
| 14 | `REVAL.R.IFRS.NPV.METHOD` | `RevalReportSaved_IfrsNpvMethod` | TField |  | The value in this field indicates the method of discounting used. A value S indicates SIMPLE method and C indicates COMPOUND method. |
| 15 | `REVAL.R.IFRS.NPV.AMT.TODATE` | `RevalReportSaved_IfrsNpvAmtTodate` | TField |  | Stores the Net Present Value of the Unrealised Profit or loss in local currency till todate. |
| 16 | `REVAL.R.IFRS.NPV.AMT.TODAY` | `RevalReportSaved_IfrsNpvAmtToday` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 17 | `REVAL.R.IFRS.REVALUE` | `RevalReportSaved_IfrsRevalue` | TField |  | Indicates whether the deal is revalued under IFRS or not. Updated with value 'YES' when transactions are revalued, if the field IFRS.REVALUE in POS.TRANSACTION has value 'YES'. |
| 18 | `REVAL.R.DDESK.REVLETTER.TXNID` | `RevalReportSaved_Ddesk.Revletter.Txnid` |  |  |  |
| 19 | `REVAL.R.RESERVED.2` | `RevalReportSaved_Reserved2` | TField |  | Reserved for Future use Validation Rules: No Input Allowed |
| 20 | `REVAL.R.RESERVED.1` | `RevalReportSaved_Reserved1` | TField |  | Reserved for Future use Validation Rules: No Input Allowed |
