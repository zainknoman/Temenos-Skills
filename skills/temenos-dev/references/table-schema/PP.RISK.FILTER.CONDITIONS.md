# PP.RISK.FILTER.CONDITIONS — Table Schema

> Source: `INSERTS/I_F.PP.RISK.FILTER.CONDITIONS` in `PP_RiskFilterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RFC.CompanyID` | `PpRiskFilterConditions_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.RFC.DebitCreditIndicator` | `PpRiskFilterConditions_Debitcreditindicator` | TField |  | Indicates the Debit or Credit indicator. Possible Values: D - Debit C - Credit B - Both Default Value : '*' Validation Rules: 1. 1 Character. |
| 3 | `PP.RFC.CurrencyCode` | `PpRiskFilterConditions_Currencycode` | TField | Yes | Specifies the Transaction Currency Code for which the condition is applicable. Default Value : '*' Validation Rules : 1. Valid record from PPT.CURRENCY Table. 2. 3 Characters. 2. Mandatory when the TransactionAmount is not NULL. |
| 4 | `PP.RFC.IncomingMessageType` | `PpRiskFilterConditions_Incomingmessagetype` | TField |  | Specifies the Message Type for which the condition is applied. Default Value : '*' Validation Rules : 1. Valid record PPT.MSGPAYMENTTYPE table or the defaule value "*" 2. 1-8 AlphaNumeric characters. |
| 5 | `PP.RFC.CTRBTRIndicator` | `PpRiskFilterConditions_Ctrbtrindicator` | TField |  | Specifies whether the condition is applicable for Customer Transfer or Bank Taransfer or for Both. Possible Values: C - Customer B - Bank Default Value : '*' Validation Rules : 1. 1 Character. |
| 6 | `PP.RFC.BICCode` | `PpRiskFilterConditions_Biccode` | TField |  | Specifies the Bank Identification Code.It can be defined at different levels (BIC 11 , 8 , 6, 4 , 2 ) Country wise limit are set by defining 2 characters company code in this field Default Value : '*' |
| 7 | `PP.RFC.StartDate` | `PpRiskFilterConditions_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 8 | `PP.RFC.EndDate` | `PpRiskFilterConditions_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 9 | `PP.RFC.LimitCurrencyCode` | `PpRiskFilterConditions_Limitcurrencycode` | TField |  | Specifies the Currency Code in which amount based limits are defined. Validation Rules : 1. Valid record in the table PPT.CURRENCY. 2. 3 Characters. |
| 10 | `PP.RFC.TransactionAmountLimit` | `PpRiskFilterConditions_Transactionamountlimit` | TField |  | Spcifies the transaction amount limit per transaction. Validation Rules: 1. 1-15 Numeric characters. |
| 11 | `PP.RFC.DailyAmountLimit` | `PpRiskFilterConditions_Dailyamountlimit` | TField |  | Specifies the daily amount limit if there is any. Validation Rules: 1. 1-15 numeric characters. |
| 12 | `PP.RFC.WeeklyAmountLimit` | `PpRiskFilterConditions_Weeklyamountlimit` | TField |  | Specifies the cumulative weekly amount limit. Validation Rules: 1. 1-15 Numeric characters. |
| 13 | `PP.RFC.MonthlyAmountLimit` | `PpRiskFilterConditions_Monthlyamountlimit` | TField |  | Specifies the cumulative monthly amount limit. Validation Rules: 1. 1-15 Numeric characters. |
| 14 | `PP.RFC.NumberOfPaymentsPerDay` | `PpRiskFilterConditions_Numberofpaymentsperday` | TField |  | Specifies the Maximum number of payments allowed for a day. Validation Rules: 1. 1-6 Numeric characters. |
| 15 | `PP.RFC.NumberOfPaymentsPerWeek` | `PpRiskFilterConditions_Numberofpaymentsperweek` | TField |  | Specifies the Maximum number of payments allowed for a week. Validation Rules: 1. 1-6 Numeric characters. |
| 16 | `PP.RFC.NumberOfPaymentsPerMonth` | `PpRiskFilterConditions_Numberofpaymentspermonth` | TField |  | Specifies the Maximum number of payments allowed for a month. Validation Rules: 1. 1-6 Numeric characters. |
| 17 | `PP.RFC.Reset.Accumulator` | `PpRiskFilterConditions_ResetAccumulator` | TField |  | Specifies whether the Accumulator needs to be reset or Not.Used for the Technical purpose Possible Values : Y - YES. N - NO. Validation Rules: 1. 1 Character. |
| 18 | `PP.RFC.RESERVED.5` | `PpRiskFilterConditions_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 19 | `PP.RFC.RESERVED.4` | `PpRiskFilterConditions_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 20 | `PP.RFC.RESERVED.3` | `PpRiskFilterConditions_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 21 | `PP.RFC.RESERVED.2` | `PpRiskFilterConditions_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 22 | `PP.RFC.RESERVED.1` | `PpRiskFilterConditions_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 23 | `PP.RFC.LOCAL.REF` | `PpRiskFilterConditions_LocalRef` |  |  |  |
| 24 | `PP.RFC.LinkID` | `PpRiskFilterConditions_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 25 | `PP.RFC.OVERRIDE` | `PpRiskFilterConditions_Override` |  |  |  |
| 26 | `PP.RFC.RECORD.STATUS` | `PpRiskFilterConditions_RecordStatus` | String |  |  |
| 27 | `PP.RFC.CURR.NO` | `PpRiskFilterConditions_CurrNo` | String |  |  |
| 28 | `PP.RFC.INPUTTER` | `PpRiskFilterConditions_Inputter` |  |  |  |
| 29 | `PP.RFC.DATE.TIME` | `PpRiskFilterConditions_DateTime` |  |  |  |
| 30 | `PP.RFC.AUTHORISER` | `PpRiskFilterConditions_Authoriser` | String |  |  |
| 31 | `PP.RFC.CO.CODE` | `PpRiskFilterConditions_CoCode` | String |  |  |
| 32 | `PP.RFC.DEPT.CODE` | `PpRiskFilterConditions_DeptCode` | String |  |  |
| 33 | `PP.RFC.AUDITOR.CODE` | `PpRiskFilterConditions_AuditorCode` | String |  |  |
| 34 | `PP.RFC.AUDIT.DATE.TIME` | `PpRiskFilterConditions_AuditDateTime` | String |  |  |
