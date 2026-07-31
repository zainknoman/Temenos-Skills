# PP.BANKCLAIMSCONTROL — Table Schema

> Source: `INSERTS/I_F.PP.BANKCLAIMSCONTROL` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BCL.CompanyID` | `PpBankclaimscontrol_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.BCL.CorrespondentBIC` | `PpBankclaimscontrol_Correspondentbic` | TField | Yes | This is the sending bank�s BIC against which we will read the bank claims table. This can be defined at different levels (BIC 11, 8, 6, 4, 2, *) Validation Rules: 35 alphanumeric characters. Input to this field is mandatory. The value is validated against field �BICCode� in PPT.BICTABLE at 11,8,6,4 and 2 levels. |
| 3 | `PP.BCL.CurrencyCode` | `PpBankclaimscontrol_Currencycode` | TField |  | Indicates the currency of the payment for which this bank claims control record is created. Possible Values: Value links to field, 'CurrencyCode' in PP.CURRENCY table * (Default Value) |
| 4 | `PP.BCL.ClaimType` | `PpBankclaimscontrol_Claimtype` | TField | Yes | Holds the type of Claim to be raised. Possible Values: Debit MT191 camt.106 Validation Rules: Input to this field is mandatory |
| 5 | `PP.BCL.ClaimTowards` | `PpBankclaimscontrol_Claimtowards` | TField |  | Claim could be generated towards the sending bank or in certain cases sending bank might want us to send the claim to some other BIC. This information is stored in this field. Possible Values: SENDER OTHERBIC |
| 6 | `PP.BCL.ClaimBIC` | `PpBankclaimscontrol_Claimbic` | TField |  | If the claim towards field is 'OTHERBIC' then this field will store the actual BIC value. Otherwise it is hardcoded as SENDER, indicating claim towards the sender BIC. Validation Rules: Accepts upto 35 alphanumeric characters. |
| 7 | `PP.BCL.ClaimBasis` | `PpBankclaimscontrol_Claimbasis` | TField | Yes | Holds the Claims generation threshold. Possible Values: Count Periodic Validation Rules: Input to this field is mandatory. |
| 8 | `PP.BCL.ClaimPeriod` | `PpBankclaimscontrol_Claimperiod` | TField |  | If Claim Basis is set as PERIODIC then this field will hold the exact period. Possible Values: D - Daily W - Weekly M - Monthly |
| 9 | `PP.BCL.ClaimTrigger` | `PpBankclaimscontrol_Claimtrigger` | TField |  | In case claim basis is count then we will define trigger as the count of payments which once reached will trigger the claim generation. So it will be a number. In case claim basis is periodic then if claim period is Daily � Claim will be generated on each working day.In this case acceptable trigger will be 1. Weekly � Trigger is day of the week, Monday(1), Tuesday(2)�Friday(5). In this case acceptable trigger will be 1,2,3,4 or 5. Monthly � Trigger is the day of the month.In this case acceptable trigger could be any value from 1 to 31. |
| 10 | `PP.BCL.IndividualGroupIndicator` | `PpBankclaimscontrol_Individualgroupindicator` | TField |  | Indicates if we need to club all the claims or process them individually. Possible Values: I - Individual G - Group Option Value G will not be available if PH is not installed |
| 11 | `PP.BCL.StartDate` | `PpBankclaimscontrol_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 12 | `PP.BCL.EndDate` | `PpBankclaimscontrol_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 13 | `PP.BCL.RESERVED.5` | `PpBankclaimscontrol_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 14 | `PP.BCL.RESERVED.4` | `PpBankclaimscontrol_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 15 | `PP.BCL.RESERVED.3` | `PpBankclaimscontrol_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 16 | `PP.BCL.RESERVED.2` | `PpBankclaimscontrol_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 17 | `PP.BCL.RESERVED.1` | `PpBankclaimscontrol_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 18 | `PP.BCL.LOCAL.REF` | `PpBankclaimscontrol_LocalRef` |  |  |  |
| 19 | `PP.BCL.LinkID` | `PpBankclaimscontrol_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 20 | `PP.BCL.OVERRIDE` | `PpBankclaimscontrol_Override` |  |  |  |
| 21 | `PP.BCL.RECORD.STATUS` | `PpBankclaimscontrol_RecordStatus` | String |  |  |
| 22 | `PP.BCL.CURR.NO` | `PpBankclaimscontrol_CurrNo` | String |  |  |
| 23 | `PP.BCL.INPUTTER` | `PpBankclaimscontrol_Inputter` |  |  |  |
| 24 | `PP.BCL.DATE.TIME` | `PpBankclaimscontrol_DateTime` |  |  |  |
| 25 | `PP.BCL.AUTHORISER` | `PpBankclaimscontrol_Authoriser` | String |  |  |
| 26 | `PP.BCL.CO.CODE` | `PpBankclaimscontrol_CoCode` | String |  |  |
| 27 | `PP.BCL.DEPT.CODE` | `PpBankclaimscontrol_DeptCode` | String |  |  |
| 28 | `PP.BCL.AUDITOR.CODE` | `PpBankclaimscontrol_AuditorCode` | String |  |  |
| 29 | `PP.BCL.AUDIT.DATE.TIME` | `PpBankclaimscontrol_AuditDateTime` | String |  |  |
