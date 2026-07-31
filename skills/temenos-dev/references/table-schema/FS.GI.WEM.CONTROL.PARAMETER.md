# FS.GI.WEM.CONTROL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.CONTROL.PARAMETER` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.WEM.CONTROL.PARAM.CONTROL.ID` | `FsGiWemControlParameter_ControlId` | TField |  | Unique control number. Multifonds DB Column is TYP_CTRL_ID. |
| 2 | `GI.WEM.CONTROL.PARAM.CONTROL.SEQUENCE` | `FsGiWemControlParameter_ControlSequence` | TField |  | WEM control sequence number. Multifonds DB Column is CTRL_SEQ. |
| 3 | `GI.WEM.CONTROL.PARAM.THRESHOLD.TYPE` | `FsGiWemControlParameter_ThresholdType` | TField |  | Threshold type. Multifonds DB Column is TYP_THRESH. |
| 4 | `GI.WEM.CONTROL.PARAM.OPERATOR` | `FsGiWemControlParameter_Operator` | TField | Yes | Operator code. This field is mandatory when control type is 2002 and 3006. Multifonds DB Column is COD_OPERATION. |
| 5 | `GI.WEM.CONTROL.PARAM.ERROR.TYPE` | `FsGiWemControlParameter_ErrorType` | TField |  | Error type. For example : '0001 - Warning' or '0002 - Blocking'. Multifonds DB Column is TYP_ERROR. |
| 6 | `GI.WEM.CONTROL.PARAM.FOUR.EYE.FLAG` | `FsGiWemControlParameter_FourEyeFlag` | TField |  | Flag to indicate that four eye functionality is applicable. Multifonds DB Column is FLG_4EYE. |
| 7 | `GI.WEM.CONTROL.PARAM.RESERVED10` | `FsGiWemControlParameter_Reserved10` | TField |  |  |
| 8 | `GI.WEM.CONTROL.PARAM.RESERVED9` | `FsGiWemControlParameter_Reserved9` | TField |  |  |
| 9 | `GI.WEM.CONTROL.PARAM.RESERVED8` | `FsGiWemControlParameter_Reserved8` | TField |  |  |
| 10 | `GI.WEM.CONTROL.PARAM.RESERVED7` | `FsGiWemControlParameter_Reserved7` | TField |  |  |
| 11 | `GI.WEM.CONTROL.PARAM.RESERVED6` | `FsGiWemControlParameter_Reserved6` | TField |  |  |
| 12 | `GI.WEM.CONTROL.PARAM.RESERVED5` | `FsGiWemControlParameter_Reserved5` | TField |  |  |
| 13 | `GI.WEM.CONTROL.PARAM.RESERVED4` | `FsGiWemControlParameter_Reserved4` | TField |  |  |
| 14 | `GI.WEM.CONTROL.PARAM.RESERVED3` | `FsGiWemControlParameter_Reserved3` | TField |  |  |
| 15 | `GI.WEM.CONTROL.PARAM.RESERVED2` | `FsGiWemControlParameter_Reserved2` | TField |  |  |
| 16 | `GI.WEM.CONTROL.PARAM.RESERVED1` | `FsGiWemControlParameter_Reserved1` | TField |  |  |
| 17 | `GI.WEM.CONTROL.PARAM.LOCAL.REF` | `FsGiWemControlParameter_LocalRef` |  |  |  |
| 18 | `GI.WEM.CONTROL.PARAM.OVERRIDE` | `FsGiWemControlParameter_Override` |  |  |  |
| 19 | `GI.WEM.CONTROL.PARAM.RECORD.STATUS` | `FsGiWemControlParameter_RecordStatus` | String |  |  |
| 20 | `GI.WEM.CONTROL.PARAM.CURR.NO` | `FsGiWemControlParameter_CurrNo` | String |  |  |
| 21 | `GI.WEM.CONTROL.PARAM.INPUTTER` | `FsGiWemControlParameter_Inputter` |  |  |  |
| 22 | `GI.WEM.CONTROL.PARAM.DATE.TIME` | `FsGiWemControlParameter_DateTime` |  |  |  |
| 23 | `GI.WEM.CONTROL.PARAM.AUTHORISER` | `FsGiWemControlParameter_Authoriser` | String |  |  |
| 24 | `GI.WEM.CONTROL.PARAM.CO.CODE` | `FsGiWemControlParameter_CoCode` | String |  |  |
| 25 | `GI.WEM.CONTROL.PARAM.DEPT.CODE` | `FsGiWemControlParameter_DeptCode` | String |  |  |
| 26 | `GI.WEM.CONTROL.PARAM.AUDITOR.CODE` | `FsGiWemControlParameter_AuditorCode` | String |  |  |
| 27 | `GI.WEM.CONTROL.PARAM.AUDIT.DATE.TIME` | `FsGiWemControlParameter_AuditDateTime` | String |  |  |
