# DFE.GROUP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DFE.GROUP.PARAMETER` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DGP.DESCRIPTION` | `DfeGroupParameter_Description` |  |  |  |
| 2 | `DGP.MAPPING.CONDITION` | `DfeGroupParameter_MappingCondition` |  |  |  |
| 3 | `DGP.MAPPING.DEFINITION` | `DfeGroupParameter_MappingDefinition` |  |  |  |
| 4 | `DGP.OFS.VERSION` | `DfeGroupParameter_OfsVersion` |  |  |  |
| 5 | `DGP.RECORD.ROUTINE` | `DfeGroupParameter_RecordRoutine` | TField |  |  |
| 6 | `DGP.MAPPING.ROUTINE` | `DfeGroupParameter_MappingRoutine` | TField |  |  |
| 7 | `DGP.MERGE.HDR.TRAILER` | `DfeGroupParameter_MergeHdrTrailer` | TField |  |  |
| 8 | `DGP.MERGE.DETL.ADDENDA` | `DfeGroupParameter_MergeDetlAddenda` | TField |  |  |
| 9 | `DGP.RESERVED.10` | `DfeGroupParameter_Reserved10` | TField |  |  |
| 10 | `DGP.RESERVED.9` | `DfeGroupParameter_Reserved9` | TField |  |  |
| 11 | `DGP.RESERVED.8` | `DfeGroupParameter_Reserved8` | TField |  |  |
| 12 | `DGP.RESERVED.7` | `DfeGroupParameter_Reserved7` | TField |  |  |
| 13 | `DGP.RESERVED.6` | `DfeGroupParameter_Reserved6` | TField |  |  |
| 14 | `DGP.RESERVED.5` | `DfeGroupParameter_Reserved5` | TField |  |  |
| 15 | `DGP.RESERVED.4` | `DfeGroupParameter_Reserved4` | TField |  |  |
| 16 | `DGP.RESERVED.3` | `DfeGroupParameter_Reserved3` | TField |  |  |
| 17 | `DGP.RESERVED.2` | `DfeGroupParameter_Reserved2` | TField |  |  |
| 18 | `DGP.RESERVED.1` | `DfeGroupParameter_Reserved1` | TField |  |  |
| 19 | `DGP.LOCAL.REF` | `DfeGroupParameter_LocalRef` |  |  |  |
| 20 | `DGP.OVERRIDE` | `DfeGroupParameter_Override` |  |  |  |
| 21 | `DGP.RECORD.STATUS` | `DfeGroupParameter_RecordStatus` | String |  |  |
| 22 | `DGP.CURR.NO` | `DfeGroupParameter_CurrNo` | String |  |  |
| 23 | `DGP.INPUTTER` | `DfeGroupParameter_Inputter` |  |  |  |
| 24 | `DGP.DATE.TIME` | `DfeGroupParameter_DateTime` |  |  |  |
| 25 | `DGP.AUTHORISER` | `DfeGroupParameter_Authoriser` | String |  |  |
| 26 | `DGP.CO.CODE` | `DfeGroupParameter_CoCode` | String |  |  |
| 27 | `DGP.DEPT.CODE` | `DfeGroupParameter_DeptCode` | String |  |  |
| 28 | `DGP.AUDITOR.CODE` | `DfeGroupParameter_AuditorCode` | String |  |  |
| 29 | `DGP.AUDIT.DATE.TIME` | `DfeGroupParameter_AuditDateTime` | String |  |  |
