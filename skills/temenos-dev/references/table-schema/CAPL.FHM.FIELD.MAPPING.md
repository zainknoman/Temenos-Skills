# CAPL.FHM.FIELD.MAPPING — Table Schema

> Source: `INSERTS/I_F.CAPL.FHM.FIELD.MAPPING` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.FHM.MAP.FILE.NAME` | `CaplFhmFieldMapping_FileName` | TField |  |  |
| 2 | `CAPL.FHM.MAP.APPL.FIELDS` | `CaplFhmFieldMapping_ApplFields` |  |  |  |
| 3 | `CAPL.FHM.MAP.RESERVED.9` | `CaplFhmFieldMapping_Reserved9` | TField |  |  |
| 4 | `CAPL.FHM.MAP.RESERVED.8` | `CaplFhmFieldMapping_Reserved8` | TField |  |  |
| 5 | `CAPL.FHM.MAP.RESERVED.7` | `CaplFhmFieldMapping_Reserved7` | TField |  |  |
| 6 | `CAPL.FHM.MAP.RESERVED.6` | `CaplFhmFieldMapping_Reserved6` | TField |  |  |
| 7 | `CAPL.FHM.MAP.RESERVED.5` | `CaplFhmFieldMapping_Reserved5` | TField |  |  |
| 8 | `CAPL.FHM.MAP.RESERVED.4` | `CaplFhmFieldMapping_Reserved4` | TField |  |  |
| 9 | `CAPL.FHM.MAP.RESERVED.3` | `CaplFhmFieldMapping_Reserved3` | TField |  |  |
| 10 | `CAPL.FHM.MAP.RESERVED.2` | `CaplFhmFieldMapping_Reserved2` | TField |  |  |
| 11 | `CAPL.FHM.MAP.RESERVED.1` | `CaplFhmFieldMapping_Reserved1` | TField |  |  |
| 12 | `CAPL.FHM.MAP.LOCAL.REF` | `CaplFhmFieldMapping_LocalRef` |  |  |  |
| 13 | `CAPL.FHM.MAP.OVERRIDE` | `CaplFhmFieldMapping_Override` |  |  |  |
| 14 | `CAPL.FHM.MAP.RECORD.STATUS` | `CaplFhmFieldMapping_RecordStatus` | String |  |  |
| 15 | `CAPL.FHM.MAP.CURR.NO` | `CaplFhmFieldMapping_CurrNo` | String |  |  |
| 16 | `CAPL.FHM.MAP.INPUTTER` | `CaplFhmFieldMapping_Inputter` |  |  |  |
| 17 | `CAPL.FHM.MAP.DATE.TIME` | `CaplFhmFieldMapping_DateTime` |  |  |  |
| 18 | `CAPL.FHM.MAP.AUTHORISER` | `CaplFhmFieldMapping_Authoriser` | String |  |  |
| 19 | `CAPL.FHM.MAP.CO.CODE` | `CaplFhmFieldMapping_CoCode` | String |  |  |
| 20 | `CAPL.FHM.MAP.DEPT.CODE` | `CaplFhmFieldMapping_DeptCode` | String |  |  |
| 21 | `CAPL.FHM.MAP.AUDITOR.CODE` | `CaplFhmFieldMapping_AuditorCode` | String |  |  |
| 22 | `CAPL.FHM.MAP.AUDIT.DATE.TIME` | `CaplFhmFieldMapping_AuditDateTime` | String |  |  |
