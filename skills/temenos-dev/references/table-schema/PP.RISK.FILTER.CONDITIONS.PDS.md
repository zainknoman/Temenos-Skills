# PP.RISK.FILTER.CONDITIONS.PDS — Table Schema

> Source: `INSERTS/I_F.PP.RISK.FILTER.CONDITIONS.PDS` in `PP_RiskFilterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RFC.CompanyID` | `PpRiskFilterConditionsPds_Companyid` | TField |  |  |
| 2 | `PP.RFC.DebitCreditIndicator` | `PpRiskFilterConditionsPds_Debitcreditindicator` | TField |  |  |
| 3 | `PP.RFC.CurrencyCode` | `PpRiskFilterConditionsPds_Currencycode` | TField |  |  |
| 4 | `PP.RFC.IncomingMessageType` | `PpRiskFilterConditionsPds_Incomingmessagetype` | TField |  |  |
| 5 | `PP.RFC.CTRBTRIndicator` | `PpRiskFilterConditionsPds_Ctrbtrindicator` | TField |  |  |
| 6 | `PP.RFC.BICCode` | `PpRiskFilterConditionsPds_Biccode` | TField |  |  |
| 7 | `PP.RFC.StartDate` | `PpRiskFilterConditionsPds_Startdate` | TField |  |  |
| 8 | `PP.RFC.EndDate` | `PpRiskFilterConditionsPds_Enddate` | TField |  |  |
| 9 | `PP.RFC.LimitCurrencyCode` | `PpRiskFilterConditionsPds_Limitcurrencycode` | TField |  |  |
| 10 | `PP.RFC.TransactionAmountLimit` | `PpRiskFilterConditionsPds_Transactionamountlimit` | TField |  |  |
| 11 | `PP.RFC.DailyAmountLimit` | `PpRiskFilterConditionsPds_Dailyamountlimit` | TField |  |  |
| 12 | `PP.RFC.WeeklyAmountLimit` | `PpRiskFilterConditionsPds_Weeklyamountlimit` | TField |  |  |
| 13 | `PP.RFC.MonthlyAmountLimit` | `PpRiskFilterConditionsPds_Monthlyamountlimit` | TField |  |  |
| 14 | `PP.RFC.NumberOfPaymentsPerDay` | `PpRiskFilterConditionsPds_Numberofpaymentsperday` | TField |  |  |
| 15 | `PP.RFC.NumberOfPaymentsPerWeek` | `PpRiskFilterConditionsPds_Numberofpaymentsperweek` | TField |  |  |
| 16 | `PP.RFC.NumberOfPaymentsPerMonth` | `PpRiskFilterConditionsPds_Numberofpaymentspermonth` | TField |  |  |
| 17 | `PP.RFC.Reset.Accumulator` | `PpRiskFilterConditionsPds_ResetAccumulator` | TField |  |  |
| 18 | `PP.RFC.RESERVED.5` | `PpRiskFilterConditionsPds_Reserved5` | TField |  |  |
| 19 | `PP.RFC.RESERVED.4` | `PpRiskFilterConditionsPds_Reserved4` | TField |  |  |
| 20 | `PP.RFC.RESERVED.3` | `PpRiskFilterConditionsPds_Reserved3` | TField |  |  |
| 21 | `PP.RFC.RESERVED.2` | `PpRiskFilterConditionsPds_Reserved2` | TField |  |  |
| 22 | `PP.RFC.RESERVED.1` | `PpRiskFilterConditionsPds_Reserved1` | TField |  |  |
| 23 | `PP.RFC.LOCAL.REF` | `PpRiskFilterConditionsPds_LocalRef` |  |  |  |
| 24 | `PP.RFC.LinkID` | `PpRiskFilterConditionsPds_Linkid` | TField |  |  |
| 25 | `PP.RFC.OVERRIDE` | `PpRiskFilterConditionsPds_Override` |  |  |  |
