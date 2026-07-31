# OA.APPLICATION.USER.STATUS — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.USER.STATUS` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.AUS.DESCRIPTION` | `OaApplicationUserStatus_Description` |  |  |  |
| 2 | `OA.AUS.FULL.DESCRIPTION` | `OaApplicationUserStatus_FullDescription` |  |  |  |
| 3 | `OA.AUS.RESERVED.FIELD.5` | `OaApplicationUserStatus_ReservedField5` | TField |  |  |
| 4 | `OA.AUS.RESERVED.FIELD.4` | `OaApplicationUserStatus_ReservedField4` | TField |  |  |
| 5 | `OA.AUS.RESERVED.FIELD.3` | `OaApplicationUserStatus_ReservedField3` | TField |  |  |
| 6 | `OA.AUS.RESERVED.FIELD.2` | `OaApplicationUserStatus_ReservedField2` | TField |  |  |
| 7 | `OA.AUS.RESERVED.FIELD.1` | `OaApplicationUserStatus_ReservedField1` | TField |  |  |
| 8 | `OA.AUS.RECORD.STATUS` | `OaApplicationUserStatus_RecordStatus` | String |  |  |
| 9 | `OA.AUS.CURR.NO` | `OaApplicationUserStatus_CurrNo` | String |  |  |
| 10 | `OA.AUS.INPUTTER` | `OaApplicationUserStatus_Inputter` |  |  |  |
| 11 | `OA.AUS.DATE.TIME` | `OaApplicationUserStatus_DateTime` |  |  |  |
| 12 | `OA.AUS.AUTHORISER` | `OaApplicationUserStatus_Authoriser` | String |  |  |
| 13 | `OA.AUS.CO.CODE` | `OaApplicationUserStatus_CoCode` | String |  |  |
| 14 | `OA.AUS.DEPT.CODE` | `OaApplicationUserStatus_DeptCode` | String |  |  |
| 15 | `OA.AUS.AUDITOR.CODE` | `OaApplicationUserStatus_AuditorCode` | String |  |  |
| 16 | `OA.AUS.AUDIT.DATE.TIME` | `OaApplicationUserStatus_AuditDateTime` | String |  |  |
