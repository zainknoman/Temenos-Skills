# FS.GA.WEM.MODEL.INFO — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.MODEL.INFO` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.WEM.MODEL.NAME` | `FsGaWemModel_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 2 | `GA.WEM.MODEL.DESCRIPTION` | `FsGaWemModel_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 3 | `GA.WEM.MODEL.STREAM.ID` | `FsGaWemModel_StreamId` | TField |  | Stream ID Multifonds DB Column is STREAM_ID. |
| 4 | `GA.WEM.MODEL.RESERVED5` | `FsGaWemModel_Reserved5` | TField |  |  |
| 5 | `GA.WEM.MODEL.RESERVED4` | `FsGaWemModel_Reserved4` | TField |  |  |
| 6 | `GA.WEM.MODEL.RESERVED3` | `FsGaWemModel_Reserved3` | TField |  |  |
| 7 | `GA.WEM.MODEL.RESERVED2` | `FsGaWemModel_Reserved2` | TField |  |  |
| 8 | `GA.WEM.MODEL.RESERVED1` | `FsGaWemModel_Reserved1` | TField |  |  |
| 9 | `GA.WEM.MODEL.LOCAL.REF` | `FsGaWemModel_LocalRef` |  |  |  |
| 10 | `GA.WEM.MODEL.OVERRIDE` | `FsGaWemModel_Override` |  |  |  |
| 11 | `GA.WEM.MODEL.RECORD.STATUS` | `FsGaWemModel_RecordStatus` | String |  |  |
| 12 | `GA.WEM.MODEL.CURR.NO` | `FsGaWemModel_CurrNo` | String |  |  |
| 13 | `GA.WEM.MODEL.INPUTTER` | `FsGaWemModel_Inputter` |  |  |  |
| 14 | `GA.WEM.MODEL.DATE.TIME` | `FsGaWemModel_DateTime` |  |  |  |
| 15 | `GA.WEM.MODEL.AUTHORISER` | `FsGaWemModel_Authoriser` | String |  |  |
| 16 | `GA.WEM.MODEL.CO.CODE` | `FsGaWemModel_CoCode` | String |  |  |
| 17 | `GA.WEM.MODEL.DEPT.CODE` | `FsGaWemModel_DeptCode` | String |  |  |
| 18 | `GA.WEM.MODEL.AUDITOR.CODE` | `FsGaWemModel_AuditorCode` | String |  |  |
| 19 | `GA.WEM.MODEL.AUDIT.DATE.TIME` | `FsGaWemModel_AuditDateTime` | String |  |  |
