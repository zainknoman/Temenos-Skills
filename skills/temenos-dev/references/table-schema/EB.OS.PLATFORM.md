# EB.OS.PLATFORM — Table Schema

> Source: `INSERTS/I_F.EB.OS.PLATFORM` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.OS.PLM.DESCRIPTION` | `EbOsPlatform_Description` |  |  |  |
| 2 | `EB.OS.PLM.RESERVED.1` | `EbOsPlatform_Reserved1` | TField |  |  |
| 3 | `EB.OS.PLM.RESERVED.2` | `EbOsPlatform_Reserved2` | TField |  |  |
| 4 | `EB.OS.PLM.RESERVED.3` | `EbOsPlatform_Reserved3` | TField |  |  |
| 5 | `EB.OS.PLM.RESERVED.4` | `EbOsPlatform_Reserved4` | TField |  |  |
| 6 | `EB.OS.PLM.RESERVED.5` | `EbOsPlatform_Reserved5` | TField |  |  |
| 7 | `EB.OS.PLM.RESERVED.6` | `EbOsPlatform_Reserved6` | TField |  |  |
| 8 | `EB.OS.PLM.RESERVED.7` | `EbOsPlatform_Reserved7` | TField |  |  |
| 9 | `EB.OS.PLM.RESERVED.8` | `EbOsPlatform_Reserved8` | TField |  |  |
| 10 | `EB.OS.PLM.RESERVED.9` | `EbOsPlatform_Reserved9` | TField |  |  |
| 11 | `EB.OS.PLM.RESERVED.10` | `EbOsPlatform_Reserved10` | TField |  |  |
| 12 | `EB.OS.PLM.LOCAL.REF` | `EbOsPlatform_LocalRef` |  |  |  |
| 13 | `EB.OS.PLM.OVERRIDE` | `EbOsPlatform_Override` |  |  |  |
| 14 | `EB.OS.PLM.RECORD.STATUS` | `EbOsPlatform_RecordStatus` | String |  |  |
| 15 | `EB.OS.PLM.CURR.NO` | `EbOsPlatform_CurrNo` | String |  |  |
| 16 | `EB.OS.PLM.INPUTTER` | `EbOsPlatform_Inputter` |  |  |  |
| 17 | `EB.OS.PLM.DATE.TIME` | `EbOsPlatform_DateTime` |  |  |  |
| 18 | `EB.OS.PLM.AUTHORISER` | `EbOsPlatform_Authoriser` | String |  |  |
| 19 | `EB.OS.PLM.CO.CODE` | `EbOsPlatform_CoCode` | String |  |  |
| 20 | `EB.OS.PLM.DEPT.CODE` | `EbOsPlatform_DeptCode` | String |  |  |
| 21 | `EB.OS.PLM.AUDITOR.CODE` | `EbOsPlatform_AuditorCode` | String |  |  |
| 22 | `EB.OS.PLM.AUDIT.DATE.TIME` | `EbOsPlatform_AuditDateTime` | String |  |  |
