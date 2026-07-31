# US.STATE — Table Schema

> Source: `INSERTS/I_F.US.STATE` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.ST.DESCRIPTION` | `UsState_Description` | TField |  | The field will have the name of the US State. |
| 2 | `US.ST.IRS.CODE` | `UsState_IrsCode` | TField |  | Shows the IRS code of the State Max 2 numeric characters |
| 3 | `US.ST.LOCAL.REF` | `UsState_LocalRef` |  |  |  |
| 4 | `US.ST.STATE.CODE` | `UsState_StateCode` | TField |  | This field is used to store IRS state code |
| 5 | `US.ST.COUNTY.NAME` | `UsState_CountyName` |  |  |  |
| 6 | `US.ST.COUNTY.CODE` | `UsState_CountyCode` |  |  |  |
| 7 | `US.ST.ESCHEAT.HDR.BRANCH` | `UsState_EscheatHdrBranch` | TField |  | Escheat head branch code |
| 8 | `US.ST.COUNTRY.CODE` | `UsState_CountryCode` | TField |  | Shows the Country Code Max 2 characters Possible values: CA and US |
| 9 | `US.ST.STATE.WHT.APPLICABLE` | `UsState_StateWhtApplicable` | TField |  | Indicate the state is tax withhelding. Possible values: YES and NO |
| 10 | `US.ST.RECORD.STATUS` | `UsState_RecordStatus` | String |  |  |
| 11 | `US.ST.CURR.NO` | `UsState_CurrNo` | String |  |  |
| 12 | `US.ST.INPUTTER` | `UsState_Inputter` |  |  |  |
| 13 | `US.ST.DATE.TIME` | `UsState_DateTime` |  |  |  |
| 14 | `US.ST.AUTHORISER` | `UsState_Authoriser` | String |  |  |
| 15 | `US.ST.CO.CODE` | `UsState_CoCode` | String |  |  |
| 16 | `US.ST.DEPT.CODE` | `UsState_DeptCode` | String |  |  |
| 17 | `US.ST.AUDITOR.CODE` | `UsState_AuditorCode` | String |  |  |
| 18 | `US.ST.AUDIT.DATE.TIME` | `UsState_AuditDateTime` | String |  |  |
