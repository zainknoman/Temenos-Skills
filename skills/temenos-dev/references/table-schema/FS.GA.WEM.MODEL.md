# FS.GA.WEM.MODEL — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.MODEL` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.MODEL.PARENT.REF.ID` | `FsGaWemModel_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.MODEL.ORA.ROWID` | `FsGaWemModel_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.MODEL.MODEL.ID` | `FsGaWemModel_ModelId` | TField |  | ID of the Model Multifonds DB Column is MODEL_ID. |
| 4 | `FS.GA.WEM.MODEL.NAME` | `FsGaWemModel_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 5 | `FS.GA.WEM.MODEL.DESCRIPTION` | `FsGaWemModel_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 6 | `FS.GA.WEM.MODEL.STREAM.ID` | `FsGaWemModel_StreamId` | TField |  | Stream ID Multifonds DB Column is STREAM_ID. |
| 7 | `FS.GA.WEM.MODEL.RESERVED10` | `FsGaWemModel_Reserved10` | TField |  |  |
| 8 | `FS.GA.WEM.MODEL.RESERVED9` | `FsGaWemModel_Reserved9` | TField |  |  |
| 9 | `FS.GA.WEM.MODEL.RESERVED8` | `FsGaWemModel_Reserved8` | TField |  |  |
| 10 | `FS.GA.WEM.MODEL.RESERVED7` | `FsGaWemModel_Reserved7` | TField |  |  |
| 11 | `FS.GA.WEM.MODEL.RESERVED6` | `FsGaWemModel_Reserved6` | TField |  |  |
| 12 | `FS.GA.WEM.MODEL.RESERVED5` | `FsGaWemModel_Reserved5` | TField |  |  |
| 13 | `FS.GA.WEM.MODEL.RESERVED4` | `FsGaWemModel_Reserved4` | TField |  |  |
| 14 | `FS.GA.WEM.MODEL.RESERVED3` | `FsGaWemModel_Reserved3` | TField |  |  |
| 15 | `FS.GA.WEM.MODEL.RESERVED2` | `FsGaWemModel_Reserved2` | TField |  |  |
| 16 | `FS.GA.WEM.MODEL.RESERVED1` | `FsGaWemModel_Reserved1` | TField |  |  |
| 17 | `FS.GA.WEM.MODEL.LOCAL.REF` | `FsGaWemModel_LocalRef` |  |  |  |
| 18 | `FS.GA.WEM.MODEL.OVERRIDE` | `FsGaWemModel_Override` |  |  |  |
| 19 | `FS.GA.WEM.MODEL.RECORD.STATUS` | `FsGaWemModel_RecordStatus` | String |  |  |
| 20 | `FS.GA.WEM.MODEL.CURR.NO` | `FsGaWemModel_CurrNo` | String |  |  |
| 21 | `FS.GA.WEM.MODEL.INPUTTER` | `FsGaWemModel_Inputter` |  |  |  |
| 22 | `FS.GA.WEM.MODEL.DATE.TIME` | `FsGaWemModel_DateTime` |  |  |  |
| 23 | `FS.GA.WEM.MODEL.AUTHORISER` | `FsGaWemModel_Authoriser` | String |  |  |
| 24 | `FS.GA.WEM.MODEL.CO.CODE` | `FsGaWemModel_CoCode` | String |  |  |
| 25 | `FS.GA.WEM.MODEL.DEPT.CODE` | `FsGaWemModel_DeptCode` | String |  |  |
| 26 | `FS.GA.WEM.MODEL.AUDITOR.CODE` | `FsGaWemModel_AuditorCode` | String |  |  |
| 27 | `FS.GA.WEM.MODEL.AUDIT.DATE.TIME` | `FsGaWemModel_AuditDateTime` | String |  |  |
