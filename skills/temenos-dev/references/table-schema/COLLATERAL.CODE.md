# COLLATERAL.CODE — Table Schema

> Source: `INSERTS/I_F.COLLATERAL.CODE` in `CO_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COLL.CODE.DESCRIPTION` | `CollateralCode_Description` |  |  |  |
| 2 | `COLL.CODE.SHORT.NAME` | `CollateralCode_ShortName` |  |  |  |
| 3 | `COLL.CODE.COLLATERAL.TYPE` | `CollateralCode_CollateralType` |  |  |  |
| 4 | `COLL.CODE.PERCENT.DATE.FQU` | `CollateralCode_PercentDateFqu` | TField | No | Determines when the system is to perform a recalculation of the percentage of cover applicable to collateral rights held under this code. A combined date &amp; frequency field which determines if and when the system is to automatically recalculate the value of the PERCENTAGE COVER (field 4) of collateral right main file records belonging to this code. When such a recalculation is performed, the date part of this field is automatically cycled according to the frequency part. Validation Rules: 17 type FQU (frequency format). (Optional input) |
| 5 | `COLL.CODE.REVIEW.FQU` | `CollateralCode_ReviewFqu` | TField | No | The default review frequency applicable to this category of collateral right. The content of this field is used to generate a default value for the REVIEW DATE FQU (field 6) when input is made to the collateral right main file using this code. The permitted values of the frequency code are as follows: BSNSS - business (working) days; date is to be cycled each business day, DAILY - date is to be cycled daily (ie. each calendar day), WEEKn - where n is a number in the range 1 to 9; date is to be cycled every n weeks, TWMTH - twice monthly; date cycles twice monthly on the 15th and last day of each month, Mmmdd - where mm is a number in the range 1 to 12 and dd is a number in the range 1 to 31; describes a cycle on a particular day (dd) each month or every mm months. These frequency codes correspond to the equivalent codes contained in the standard date/frequency combined format. Validation Rules: 5 alphanumeric characters (frequency code). (Optional input) |
| 6 | `COLL.CODE.RECORD.STATUS` | `CollateralCode_RecordStatus` | String |  |  |
| 7 | `COLL.CODE.CURR.NO` | `CollateralCode_CurrNo` | String |  |  |
| 8 | `COLL.CODE.INPUTTER` | `CollateralCode_Inputter` |  |  |  |
| 9 | `COLL.CODE.DATE.TIME` | `CollateralCode_DateTime` |  |  |  |
| 10 | `COLL.CODE.AUTHORISER` | `CollateralCode_Authoriser` | String |  |  |
| 11 | `COLL.CODE.CO.CODE` | `CollateralCode_CoCode` | String |  |  |
| 12 | `COLL.CODE.DEPT.CODE` | `CollateralCode_DeptCode` | String |  |  |
| 13 | `COLL.CODE.AUDITOR.CODE` | `CollateralCode_AuditorCode` | String |  |  |
| 14 | `COLL.CODE.AUDIT.DATE.TIME` | `CollateralCode_AuditDateTime` | String |  |  |
| 15 | `COLL.CODE.CO.ALLOCATED.BAL.TYPE` | `CollateralCode_CoAllocatedBalType` | TField |  | The allocated AC.BALANCE.TYPE asset created will be defined here if user wants to report the particular collateral code to GL. Validation Rules: Must contain valid AC.BALANCE.TYPE record id. REPORTING.TYPE must be CONTINGENT and ENTRY.TYPE must be SPECIAL. |
| 16 | `COLL.CODE.CO.UTILISED.BAL.TYPE` | `CollateralCode_CoUtilisedBalType` | TField |  | The utilized AC.BALANCE.TYPE asset created will be defined here if user wants to report the particular collateral code to GL. Validation Rules: Must contain valid AC.BALANCE.TYPE record id. REPORTING.TYPE must be CONTINGENT and ENTRY.TYPE must be SPECIAL. |
| 17 | `COLL.CODE.CO.UNUTILISED.BAL.TYPE` | `CollateralCode_CoUnutilisedBalType` | TField |  | The unutilized AC.BALANCE.TYPE asset created will be defined here if user wants to report the particular collateral code to GL. Validation Rules: Must contain valid AC.BALANCE.TYPE record id. REPORTING.TYPE must be CONTINGENT and ENTRY.TYPE must be SPECIAL. |
| 18 | `COLL.CODE.LOCAL.REF` | `CollateralCode_LocalRef` |  |  |  |
