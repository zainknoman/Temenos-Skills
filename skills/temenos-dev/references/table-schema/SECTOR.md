# SECTOR — Table Schema

> Source: `INSERTS/I_F.SECTOR` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SEC.DESCRIPTION` | `Sector_Description` |  |  |  |
| 2 | `EB.SEC.SHORT.NAME` | `Sector_ShortName` |  |  |  |
| 3 | `EB.SEC.RISK.EXPO.TYPE` | `Sector_RiskExpoType` | TField |  | Specific codes for certain sectors which have special treatment for risk calculations. Needs to be populated for all sector records. For example 211 � Central bank, 210 � Sovereign, 221 � Bank for International settlement, etc |
| 4 | `EB.SEC.RESERVED.4` | `Sector_Reserved4` | TField |  |  |
| 5 | `EB.SEC.RESERVED.3` | `Sector_Reserved3` | TField |  |  |
| 6 | `EB.SEC.RESERVED.2` | `Sector_Reserved2` | TField |  |  |
| 7 | `EB.SEC.RESERVED.1` | `Sector_Reserved1` | TField |  |  |
| 8 | `EB.SEC.LOCAL.REF` | `Sector_LocalRef` |  |  |  |
| 9 | `EB.SEC.RECORD.STATUS` | `Sector_RecordStatus` | String |  |  |
| 10 | `EB.SEC.CURR.NO` | `Sector_CurrNo` | String |  |  |
| 11 | `EB.SEC.INPUTTER` | `Sector_Inputter` |  |  |  |
| 12 | `EB.SEC.DATE.TIME` | `Sector_DateTime` |  |  |  |
| 13 | `EB.SEC.AUTHORISER` | `Sector_Authoriser` | String |  |  |
| 14 | `EB.SEC.CO.CODE` | `Sector_CoCode` | String |  |  |
| 15 | `EB.SEC.DEPT.CODE` | `Sector_DeptCode` | String |  |  |
| 16 | `EB.SEC.AUDITOR.CODE` | `Sector_AuditorCode` | String |  |  |
| 17 | `EB.SEC.AUDIT.DATE.TIME` | `Sector_AuditDateTime` | String |  |  |
