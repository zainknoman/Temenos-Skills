# PP.RISK.FILTER.OUTPUT — Table Schema

> Source: `INSERTS/I_F.PP.RISK.FILTER.OUTPUT` in `PP_RiskFilterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RFO.CompanyID` | `PpRiskFilterOutput_Companyid` | TField |  | Indicates the company ID of the limit breached payment. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PP.RFO.FTNumber` | `PpRiskFilterOutput_Ftnumber` | TField |  | Specifies the unique ID of the breached payment. Validation Rules: 16 alphanumeric characters. |
| 3 | `PP.RFO.TransactionAmount` | `PpRiskFilterOutput_Transactionamount` | TField |  | Spcifies the transaction amount of hte breached payment. Validation Rules: 1. 1-15 Numeric characters. |
| 4 | `PP.RFO.TransactionCurrency` | `PpRiskFilterOutput_Transactioncurrency` | TField |  | Specifies the payment Currency Code of the breached payment. Validation Rules : 1. 3 Characters. |
| 5 | `PP.RFO.DebitValueDate` | `PpRiskFilterOutput_Debitvaluedate` | TField |  | This field is a no input filed. System will populate the DebitValueDate from the payment order. |
| 6 | `PP.RFO.CreditValueDate` | `PpRiskFilterOutput_Creditvaluedate` | TField |  | Specifies the CreditValueDate from the breached payment order. |
| 7 | `PP.RFO.FilterID` | `PpRiskFilterOutput_Filterid` |  |  |  |
| 8 | `PP.RFO.TransactionAmountLimit` | `PpRiskFilterOutput_Transactionamountlimit` |  |  |  |
| 9 | `PP.RFO.TRNLimitBreach` | `PpRiskFilterOutput_Trnlimitbreach` |  |  |  |
| 10 | `PP.RFO.DailyAmountLimit` | `PpRiskFilterOutput_Dailyamountlimit` |  |  |  |
| 11 | `PP.RFO.DailyLimitBreach` | `PpRiskFilterOutput_Dailylimitbreach` |  |  |  |
| 12 | `PP.RFO.WeeklyAmountLimit` | `PpRiskFilterOutput_Weeklyamountlimit` |  |  |  |
| 13 | `PP.RFO.WeeklyLimitBreach` | `PpRiskFilterOutput_Weeklylimitbreach` |  |  |  |
| 14 | `PP.RFO.MonthlyAmountLimit` | `PpRiskFilterOutput_Monthlyamountlimit` |  |  |  |
| 15 | `PP.RFO.MonthlyLimitBreach` | `PpRiskFilterOutput_Monthlylimitbreach` |  |  |  |
| 16 | `PP.RFO.PaymentsPerDay` | `PpRiskFilterOutput_Paymentsperday` |  |  |  |
| 17 | `PP.RFO.PPDLimitBreach` | `PpRiskFilterOutput_Ppdlimitbreach` |  |  |  |
| 18 | `PP.RFO.PaymentsPerWeek` | `PpRiskFilterOutput_Paymentsperweek` |  |  |  |
| 19 | `PP.RFO.PPWLimitBreach` | `PpRiskFilterOutput_Ppwlimitbreach` |  |  |  |
| 20 | `PP.RFO.PaymentsPerMonth` | `PpRiskFilterOutput_Paymentspermonth` |  |  |  |
| 21 | `PP.RFO.PPMLimitBreach` | `PpRiskFilterOutput_Ppmlimitbreach` |  |  |  |
| 22 | `PP.RFO.CUR.TransactionAmountLimit` | `PpRiskFilterOutput_CurTransactionamountlimit` |  |  |  |
| 23 | `PP.RFO.CUR.TRNLimitBreach` | `PpRiskFilterOutput_CurTrnlimitbreach` |  |  |  |
| 24 | `PP.RFO.CUR.DailyAmountLimit` | `PpRiskFilterOutput_CurDailyamountlimit` |  |  |  |
| 25 | `PP.RFO.CUR.DailyLimitBreach` | `PpRiskFilterOutput_CurDailylimitbreach` |  |  |  |
| 26 | `PP.RFO.CUR.WeeklyAmountLimit` | `PpRiskFilterOutput_CurWeeklyamountlimit` |  |  |  |
| 27 | `PP.RFO.CUR.WeeklyLimitBreach` | `PpRiskFilterOutput_CurWeeklylimitbreach` |  |  |  |
| 28 | `PP.RFO.CUR.MonthlyAmountLimit` | `PpRiskFilterOutput_CurMonthlyamountlimit` |  |  |  |
| 29 | `PP.RFO.CUR.MonthlyLimitBreach` | `PpRiskFilterOutput_CurMonthlylimitbreach` |  |  |  |
| 30 | `PP.RFO.CUR.PaymentsPerDay` | `PpRiskFilterOutput_CurPaymentsperday` |  |  |  |
| 31 | `PP.RFO.CUR.PPDLimitBreach` | `PpRiskFilterOutput_CurPpdlimitbreach` |  |  |  |
| 32 | `PP.RFO.CUR.PaymentsPerWeek` | `PpRiskFilterOutput_CurPaymentsperweek` |  |  |  |
| 33 | `PP.RFO.CUR.PPWLimitBreach` | `PpRiskFilterOutput_CurPpwlimitbreach` |  |  |  |
| 34 | `PP.RFO.CUR.PaymentsPerMonth` | `PpRiskFilterOutput_CurPaymentspermonth` |  |  |  |
| 35 | `PP.RFO.CUR.PPMLimitBreach` | `PpRiskFilterOutput_CurPpmlimitbreach` |  |  |  |
| 36 | `PP.RFO.Action` | `PpRiskFilterOutput_Action` | TField |  | Contains all the override messages which the user agreed to during Input. During the validation of a transaction, the system may provide the user with a series of screen override messages to indicate an anomaly. Indicates the action whether its A(Approved) or R(Reject). Possible Values: A - Approved R - Reject Validation Rules: 1. 1 Character. |
| 37 | `PP.RFO.OldID` | `PpRiskFilterOutput_Oldid` | TField |  | Used for internal purpose. Holds the ID of the previous live record of store table. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 38 | `PP.RFO.OVERRIDE` | `PpRiskFilterOutput_Override` |  |  |  |
| 39 | `PP.RFO.RECORD.STATUS` | `PpRiskFilterOutput_RecordStatus` | String |  |  |
| 40 | `PP.RFO.CURR.NO` | `PpRiskFilterOutput_CurrNo` | String |  |  |
| 41 | `PP.RFO.INPUTTER` | `PpRiskFilterOutput_Inputter` |  |  |  |
| 42 | `PP.RFO.DATE.TIME` | `PpRiskFilterOutput_DateTime` |  |  |  |
| 43 | `PP.RFO.AUTHORISER` | `PpRiskFilterOutput_Authoriser` | String |  |  |
| 44 | `PP.RFO.CO.CODE` | `PpRiskFilterOutput_CoCode` | String |  |  |
| 45 | `PP.RFO.DEPT.CODE` | `PpRiskFilterOutput_DeptCode` | String |  |  |
| 46 | `PP.RFO.AUDITOR.CODE` | `PpRiskFilterOutput_AuditorCode` | String |  |  |
| 47 | `PP.RFO.AUDIT.DATE.TIME` | `PpRiskFilterOutput_AuditDateTime` | String |  |  |
