# AM.ENTITY — Table Schema

> Source: `INSERTS/I_F.AM.ENTITY` in `AM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.ENT.DESCRIPTION` | `AmEntity_Description` |  |  |  |
| 2 | `AM.ENT.APPLICATION` | `AmEntity_Application` |  |  |  |
| 3 | `AM.ENT.PRE.PROC.RTN` | `AmEntity_PreProcRtn` |  |  |  |
| 4 | `AM.ENT.OPTION` | `AmEntity_Option` |  |  |  |
| 5 | `AM.ENT.FILE` | `AmEntity_File` |  |  |  |
| 6 | `AM.ENT.FIELD` | `AmEntity_Field` |  |  |  |
| 7 | `AM.ENT.RESERVED.9` | `AmEntity_Reserved9` | TField |  |  |
| 8 | `AM.ENT.RESERVED.8` | `AmEntity_Reserved8` | TField |  |  |
| 9 | `AM.ENT.RESERVED.7` | `AmEntity_Reserved7` | TField |  |  |
| 10 | `AM.ENT.RESERVED.6` | `AmEntity_Reserved6` | TField |  |  |
| 11 | `AM.ENT.RESERVED.5` | `AmEntity_Reserved5` | TField |  |  |
| 12 | `AM.ENT.RESERVED.4` | `AmEntity_Reserved4` | TField |  |  |
| 13 | `AM.ENT.LOCAL.REF` | `AmEntity_LocalRef` |  |  |  |
| 14 | `AM.ENT.RESERVED.2` | `AmEntity_Reserved2` | TField |  |  |
| 15 | `AM.ENT.RESERVED.1` | `AmEntity_Reserved1` | TField |  |  |
| 16 | `AM.ENT.RECORD.STATUS` | `AmEntity_RecordStatus` | String |  |  |
| 17 | `AM.ENT.CURR.NO` | `AmEntity_CurrNo` | String |  |  |
| 18 | `AM.ENT.INPUTTER` | `AmEntity_Inputter` |  |  |  |
| 19 | `AM.ENT.DATE.TIME` | `AmEntity_DateTime` |  |  |  |
| 20 | `AM.ENT.AUTHORISER` | `AmEntity_Authoriser` | String |  |  |
| 21 | `AM.ENT.CO.CODE` | `AmEntity_CoCode` | String |  |  |
| 22 | `AM.ENT.DEPT.CODE` | `AmEntity_DeptCode` | String |  |  |
| 23 | `AM.ENT.AUDITOR.CODE` | `AmEntity_AuditorCode` | String |  |  |
| 24 | `AM.ENT.AUDIT.DATE.TIME` | `AmEntity_AuditDateTime` | String |  |  |
