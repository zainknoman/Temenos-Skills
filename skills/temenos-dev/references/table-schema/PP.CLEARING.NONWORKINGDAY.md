# PP.CLEARING.NONWORKINGDAY — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.NONWORKINGDAY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CGH.CompanyID` | `PpClearingNonworkingday_Companyid` | TField |  | Indicates the Financial Table Descriptive(FTD) company for which the record is created. This is the NoInput field It gets autopopulated after the validation Example : BNK,GB1 |
| 2 | `PP.CGH.CountryCode` | `PpClearingNonworkingday_Countrycode` |  |  |  |
| 3 | `PP.CGH.Region` | `PpClearingNonworkingday_Region` |  |  |  |
| 4 | `PP.CGH.DayDate` | `PpClearingNonworkingday_Daydate` |  |  |  |
| 5 | `PP.CGH.LOCAL.REF` | `PpClearingNonworkingday_LocalRef` |  |  |  |
| 6 | `PP.CGH.RESERVED.5` | `PpClearingNonworkingday_Reserved5` | TField |  |  |
| 7 | `PP.CGH.RESERVED.4` | `PpClearingNonworkingday_Reserved4` | TField |  |  |
| 8 | `PP.CGH.RESERVED.3` | `PpClearingNonworkingday_Reserved3` | TField |  |  |
| 9 | `PP.CGH.RESERVED.2` | `PpClearingNonworkingday_Reserved2` | TField |  |  |
| 10 | `PP.CGH.RESERVED.1` | `PpClearingNonworkingday_Reserved1` | TField |  |  |
| 11 | `PP.CGH.OVERRIDE` | `PpClearingNonworkingday_Override` |  |  |  |
| 12 | `PP.CGH.RECORD.STATUS` | `PpClearingNonworkingday_RecordStatus` | String |  |  |
| 13 | `PP.CGH.CURR.NO` | `PpClearingNonworkingday_CurrNo` | String |  |  |
| 14 | `PP.CGH.INPUTTER` | `PpClearingNonworkingday_Inputter` |  |  |  |
| 15 | `PP.CGH.DATE.TIME` | `PpClearingNonworkingday_DateTime` |  |  |  |
| 16 | `PP.CGH.AUTHORISER` | `PpClearingNonworkingday_Authoriser` | String |  |  |
| 17 | `PP.CGH.CO.CODE` | `PpClearingNonworkingday_CoCode` | String |  |  |
| 18 | `PP.CGH.DEPT.CODE` | `PpClearingNonworkingday_DeptCode` | String |  |  |
| 19 | `PP.CGH.AUDITOR.CODE` | `PpClearingNonworkingday_AuditorCode` | String |  |  |
| 20 | `PP.CGH.AUDIT.DATE.TIME` | `PpClearingNonworkingday_AuditDateTime` | String |  |  |
