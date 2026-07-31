# USCORE.MODIFY.DATA — Table Schema

> Source: `INSERTS/I_F.USCORE.MODIFY.DATA` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.MOD.DESCRIPTION` | `UscoreModifyData_Description` | TField |  | Stores brief description about the application and operation. |
| 2 | `USCORE.MOD.FIELD.NAME` | `UscoreModifyData_FieldName` |  |  |  |
| 3 | `USCORE.MOD.FIELD.VALUE` | `UscoreModifyData_FieldValue` |  |  |  |
| 4 | `USCORE.MOD.RESERVED.15` | `UscoreModifyData_Reserved15` |  |  |  |
| 5 | `USCORE.MOD.RESERVED.14` | `UscoreModifyData_Reserved14` |  |  |  |
| 6 | `USCORE.MOD.RESERVED.13` | `UscoreModifyData_Reserved13` |  |  |  |
| 7 | `USCORE.MOD.RESERVED.12` | `UscoreModifyData_Reserved12` |  |  |  |
| 8 | `USCORE.MOD.RESERVED.11` | `UscoreModifyData_Reserved11` |  |  |  |
| 9 | `USCORE.MOD.RETAIN.TABLE` | `UscoreModifyData_RetainTable` | TField |  | Flag to indicate whether original value needs to be retained or not. |
| 10 | `USCORE.MOD.COMPONENT` | `UscoreModifyData_Component` | TField |  | Stores valid EB.COMPONENT record. |
| 11 | `USCORE.MOD.RELEASE.INFO` | `UscoreModifyData_ReleaseInfo` |  |  |  |
| 12 | `USCORE.MOD.RELEASE.ERR` | `UscoreModifyData_ReleaseErr` |  |  |  |
| 13 | `USCORE.MOD.RESERVED.6` | `UscoreModifyData_Reserved6` | TField |  |  |
| 14 | `USCORE.MOD.RESERVED.5` | `UscoreModifyData_Reserved5` | TField |  |  |
| 15 | `USCORE.MOD.RESERVED.4` | `UscoreModifyData_Reserved4` | TField |  |  |
| 16 | `USCORE.MOD.RESERVED.3` | `UscoreModifyData_Reserved3` | TField |  |  |
| 17 | `USCORE.MOD.RESERVED.2` | `UscoreModifyData_Reserved2` | TField |  |  |
| 18 | `USCORE.MOD.RESERVED.1` | `UscoreModifyData_Reserved1` | TField |  |  |
| 19 | `USCORE.MOD.RECORD.STATUS` | `UscoreModifyData_RecordStatus` | String |  |  |
| 20 | `USCORE.MOD.CURR.NO` | `UscoreModifyData_CurrNo` | String |  |  |
| 21 | `USCORE.MOD.INPUTTER` | `UscoreModifyData_Inputter` |  |  |  |
| 22 | `USCORE.MOD.DATE.TIME` | `UscoreModifyData_DateTime` |  |  |  |
| 23 | `USCORE.MOD.AUTHORISER` | `UscoreModifyData_Authoriser` | String |  |  |
| 24 | `USCORE.MOD.CO.CODE` | `UscoreModifyData_CoCode` | String |  |  |
| 25 | `USCORE.MOD.DEPT.CODE` | `UscoreModifyData_DeptCode` | String |  |  |
| 26 | `USCORE.MOD.AUDITOR.CODE` | `UscoreModifyData_AuditorCode` | String |  |  |
| 27 | `USCORE.MOD.AUDIT.DATE.TIME` | `UscoreModifyData_AuditDateTime` | String |  |  |
