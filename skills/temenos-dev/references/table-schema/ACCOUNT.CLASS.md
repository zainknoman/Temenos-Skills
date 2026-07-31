# ACCOUNT.CLASS — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.CLASS` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.CLS.DESCRIPTION` | `AccountClass_Description` |  |  |  |
| 2 | `AC.CLS.RECORD.TYPE` | `AccountClass_RecordType` | TField |  |  |
| 3 | `AC.CLS.CATEGORY` | `AccountClass_Category` |  |  |  |
| 4 | `AC.CLS.SECTOR` | `AccountClass_Sector` |  |  |  |
| 5 | `AC.CLS.RESERVED.5` | `AccountClass_Reserved5` | TField |  |  |
| 6 | `AC.CLS.RESERVED.4` | `AccountClass_Reserved4` | TField |  |  |
| 7 | `AC.CLS.RESERVED.3` | `AccountClass_Reserved3` | TField |  |  |
| 8 | `AC.CLS.RESERVED.2` | `AccountClass_Reserved2` | TField |  |  |
| 9 | `AC.CLS.RESERVED.1` | `AccountClass_Reserved1` | TField |  |  |
| 10 | `AC.CLS.LOCAL.REF` | `AccountClass_LocalRef` |  |  |  |
| 11 | `AC.CLS.OVERRIDE` | `AccountClass_Override` |  |  |  |
| 12 | `AC.CLS.RECORD.STATUS` | `AccountClass_RecordStatus` | String |  |  |
| 13 | `AC.CLS.CURR.NO` | `AccountClass_CurrNo` | String |  |  |
| 14 | `AC.CLS.INPUTTER` | `AccountClass_Inputter` |  |  |  |
| 15 | `AC.CLS.DATE.TIME` | `AccountClass_DateTime` |  |  |  |
| 16 | `AC.CLS.AUTHORISER` | `AccountClass_Authoriser` | String |  |  |
| 17 | `AC.CLS.CO.CODE` | `AccountClass_CoCode` | String |  |  |
| 18 | `AC.CLS.DEPT.CODE` | `AccountClass_DeptCode` | String |  |  |
| 19 | `AC.CLS.AUDITOR.CODE` | `AccountClass_AuditorCode` | String |  |  |
| 20 | `AC.CLS.AUDIT.DATE.TIME` | `AccountClass_AuditDateTime` | String |  |  |
