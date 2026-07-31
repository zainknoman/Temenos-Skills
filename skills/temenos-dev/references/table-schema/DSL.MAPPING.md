# DSL.MAPPING — Table Schema

> Source: `INSERTS/I_F.DSL.MAPPING` in `DS_Installer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DSL.MAP.DESCRIPTION` | `DslMapping_Description` |  |  |  |
| 2 | `DSL.MAP.APPLN.FIELD.NAME` | `DslMapping_ApplnFieldName` |  |  |  |
| 3 | `DSL.MAP.DSL.NAME` | `DslMapping_DslName` |  |  |  |
| 4 | `DSL.MAP.RESERVED03` | `DslMapping_Reserved03` |  |  |  |
| 5 | `DSL.MAP.RESERVED02` | `DslMapping_Reserved02` |  |  |  |
| 6 | `DSL.MAP.RESERVED01` | `DslMapping_Reserved01` |  |  |  |
| 7 | `DSL.MAP.RESERVED.7` | `DslMapping_Reserved7` | TField |  |  |
| 8 | `DSL.MAP.RESERVED.6` | `DslMapping_Reserved6` | TField |  |  |
| 9 | `DSL.MAP.RESERVED.5` | `DslMapping_Reserved5` | TField |  |  |
| 10 | `DSL.MAP.RESERVED.4` | `DslMapping_Reserved4` | TField |  |  |
| 11 | `DSL.MAP.RESERVED.3` | `DslMapping_Reserved3` | TField |  |  |
| 12 | `DSL.MAP.RESERVED.2` | `DslMapping_Reserved2` | TField |  |  |
| 13 | `DSL.MAP.RESERVED.1` | `DslMapping_Reserved1` | TField |  |  |
| 14 | `DSL.MAP.RECORD.STATUS` | `DslMapping_RecordStatus` | String |  |  |
| 15 | `DSL.MAP.CURR.NO` | `DslMapping_CurrNo` | String |  |  |
| 16 | `DSL.MAP.INPUTTER` | `DslMapping_Inputter` |  |  |  |
| 17 | `DSL.MAP.DATE.TIME` | `DslMapping_DateTime` |  |  |  |
| 18 | `DSL.MAP.AUTHORISER` | `DslMapping_Authoriser` | String |  |  |
| 19 | `DSL.MAP.CO.CODE` | `DslMapping_CoCode` | String |  |  |
| 20 | `DSL.MAP.DEPT.CODE` | `DslMapping_DeptCode` | String |  |  |
| 21 | `DSL.MAP.AUDITOR.CODE` | `DslMapping_AuditorCode` | String |  |  |
| 22 | `DSL.MAP.AUDIT.DATE.TIME` | `DslMapping_AuditDateTime` | String |  |  |
