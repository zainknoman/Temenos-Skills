# PPT.RISKFILTERCONDITIONS — Table Schema

> Source: `INSERTS/I_F.PPT.RISKFILTERCONDITIONS` in `PP_RiskFilterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPRFC.RiskFilterConditionID` | `PptRiskfilterconditions_Riskfilterconditionid` |  |  |  |
| 2 | `PPRFC.CompanyID` | `PptRiskfilterconditions_Companyid` |  |  |  |
| 3 | `PPRFC.DebitCreditIndicator` | `PptRiskfilterconditions_Debitcreditindicator` |  |  |  |
| 4 | `PPRFC.CurrencyCode` | `PptRiskfilterconditions_Currencycode` |  |  |  |
| 5 | `PPRFC.IncomingMessageType` | `PptRiskfilterconditions_Incomingmessagetype` |  |  |  |
| 6 | `PPRFC.CTRBTRIndicator` | `PptRiskfilterconditions_Ctrbtrindicator` |  |  |  |
| 7 | `PPRFC.BICCode` | `PptRiskfilterconditions_Biccode` |  |  |  |
| 8 | `PPRFC.StartDateRiskFilterConditions` | `PptRiskfilterconditions_Startdateriskfilterconditions` |  |  |  |
| 9 | `PPRFC.EndDateRiskFilterConditions` | `PptRiskfilterconditions_Enddateriskfilterconditions` |  |  |  |
| 10 | `PPRFC.LimitCurrencyCode` | `PptRiskfilterconditions_Limitcurrencycode` |  |  |  |
| 11 | `PPRFC.TransactionAmountLimit` | `PptRiskfilterconditions_Transactionamountlimit` |  |  |  |
| 12 | `PPRFC.DailyAmountLimit` | `PptRiskfilterconditions_Dailyamountlimit` |  |  |  |
| 13 | `PPRFC.WeeklyAmountLimit` | `PptRiskfilterconditions_Weeklyamountlimit` |  |  |  |
| 14 | `PPRFC.MonthlyAmountLimit` | `PptRiskfilterconditions_Monthlyamountlimit` |  |  |  |
| 15 | `PPRFC.NumberOfPaymentsPerDay` | `PptRiskfilterconditions_Numberofpaymentsperday` |  |  |  |
| 16 | `PPRFC.NumberOfPaymentsPerWeek` | `PptRiskfilterconditions_Numberofpaymentsperweek` |  |  |  |
| 17 | `PPRFC.NumberOfPaymentsPerMonth` | `PptRiskfilterconditions_Numberofpaymentspermonth` |  |  |  |
| 18 | `PPRFC.RACRiskFilterConditions` | `PptRiskfilterconditions_Racriskfilterconditions` |  |  |  |
| 19 | `PPRFC.RSCRiskFilterConditions` | `PptRiskfilterconditions_Rscriskfilterconditions` |  |  |  |
| 20 | `PPRFC.EntryUserID` | `PptRiskfilterconditions_Entryuserid` |  |  |  |
| 21 | `PPRFC.EntryDateTime` | `PptRiskfilterconditions_Entrydatetime` |  |  |  |
| 22 | `PPRFC.ApproverUserID` | `PptRiskfilterconditions_Approveruserid` |  |  |  |
| 23 | `PPRFC.ApprovedDateTime` | `PptRiskfilterconditions_Approveddatetime` |  |  |  |
