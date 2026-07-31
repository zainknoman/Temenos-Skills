# FS.GA.YIELD.ADJUSTMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.YIELD.ADJUSTMENT` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.YIELD.ADJUSTMENT.PARENT.REF.ID` | `FsGaYieldAdjustment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.YIELD.ADJUSTMENT.ORA.ROWID` | `FsGaYieldAdjustment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.YIELD.ADJUSTMENT.GROUP.LEVEL` | `FsGaYieldAdjustment_GroupLevel` | TField |  | This field displays any number in order of which rating adjustment will be performed Multifonds DB Column is GRP_LEVEL. |
| 4 | `FS.GA.YIELD.ADJUSTMENT.CODE` | `FsGaYieldAdjustment_Code` | TField |  | This field displays any user defined code up to 4 decimal places Multifonds DB Column is YLD_GRP_CODE. |
| 5 | `FS.GA.YIELD.ADJUSTMENT.LOGIC.CODE` | `FsGaYieldAdjustment_LogicCode` | TField |  | This field displays the logical code for weighted average life Multifonds DB Column is LOGICAL_CODE. |
| 6 | `FS.GA.YIELD.ADJUSTMENT.THRESHOLD` | `FsGaYieldAdjustment_Threshold` | TField |  | Threshold Multifonds DB Column is THRESHOLD. |
| 7 | `FS.GA.YIELD.ADJUSTMENT.RATING.ADJUSTMENT` | `FsGaYieldAdjustment_RatingAdjustment` | TField |  | This field displays the rating adjustment number. System adjusts the rating value to a higher category by the number defined in this column Multifonds DB Column is RATING_ADJ. |
| 8 | `FS.GA.YIELD.ADJUSTMENT.RESERVED10` | `FsGaYieldAdjustment_Reserved10` | TField |  |  |
| 9 | `FS.GA.YIELD.ADJUSTMENT.RESERVED9` | `FsGaYieldAdjustment_Reserved9` | TField |  |  |
| 10 | `FS.GA.YIELD.ADJUSTMENT.RESERVED8` | `FsGaYieldAdjustment_Reserved8` | TField |  |  |
| 11 | `FS.GA.YIELD.ADJUSTMENT.RESERVED7` | `FsGaYieldAdjustment_Reserved7` | TField |  |  |
| 12 | `FS.GA.YIELD.ADJUSTMENT.RESERVED6` | `FsGaYieldAdjustment_Reserved6` | TField |  |  |
| 13 | `FS.GA.YIELD.ADJUSTMENT.RESERVED5` | `FsGaYieldAdjustment_Reserved5` | TField |  |  |
| 14 | `FS.GA.YIELD.ADJUSTMENT.RESERVED4` | `FsGaYieldAdjustment_Reserved4` | TField |  |  |
| 15 | `FS.GA.YIELD.ADJUSTMENT.RESERVED3` | `FsGaYieldAdjustment_Reserved3` | TField |  |  |
| 16 | `FS.GA.YIELD.ADJUSTMENT.RESERVED2` | `FsGaYieldAdjustment_Reserved2` | TField |  |  |
| 17 | `FS.GA.YIELD.ADJUSTMENT.RESERVED1` | `FsGaYieldAdjustment_Reserved1` | TField |  |  |
| 18 | `FS.GA.YIELD.ADJUSTMENT.LOCAL.REF` | `FsGaYieldAdjustment_LocalRef` |  |  |  |
| 19 | `FS.GA.YIELD.ADJUSTMENT.OVERRIDE` | `FsGaYieldAdjustment_Override` |  |  |  |
| 20 | `FS.GA.YIELD.ADJUSTMENT.RECORD.STATUS` | `FsGaYieldAdjustment_RecordStatus` | String |  |  |
| 21 | `FS.GA.YIELD.ADJUSTMENT.CURR.NO` | `FsGaYieldAdjustment_CurrNo` | String |  |  |
| 22 | `FS.GA.YIELD.ADJUSTMENT.INPUTTER` | `FsGaYieldAdjustment_Inputter` |  |  |  |
| 23 | `FS.GA.YIELD.ADJUSTMENT.DATE.TIME` | `FsGaYieldAdjustment_DateTime` |  |  |  |
| 24 | `FS.GA.YIELD.ADJUSTMENT.AUTHORISER` | `FsGaYieldAdjustment_Authoriser` | String |  |  |
| 25 | `FS.GA.YIELD.ADJUSTMENT.CO.CODE` | `FsGaYieldAdjustment_CoCode` | String |  |  |
| 26 | `FS.GA.YIELD.ADJUSTMENT.DEPT.CODE` | `FsGaYieldAdjustment_DeptCode` | String |  |  |
| 27 | `FS.GA.YIELD.ADJUSTMENT.AUDITOR.CODE` | `FsGaYieldAdjustment_AuditorCode` | String |  |  |
| 28 | `FS.GA.YIELD.ADJUSTMENT.AUDIT.DATE.TIME` | `FsGaYieldAdjustment_AuditDateTime` | String |  |  |
