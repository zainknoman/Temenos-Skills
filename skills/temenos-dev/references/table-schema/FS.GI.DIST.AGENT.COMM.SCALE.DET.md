# FS.GI.DIST.AGENT.COMM.SCALE.DET — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.COMM.SCALE.DET` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.PARENT.REF.ID` | `FsGiDistAgentCommScaleDet_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.ORA.ROWID` | `FsGiDistAgentCommScaleDet_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.SCALE.ID` | `FsGiDistAgentCommScaleDet_ScaleId` | TField |  | Commission scale id. Multifonds DB Column is CBAREME. |
| 4 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.CONDITION` | `FsGiDistAgentCommScaleDet_Condition` | TField |  | Range based on threshold condition. Multifonds DB Column is CONDITION. |
| 5 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.THRESHOLDS` | `FsGiDistAgentCommScaleDet_Thresholds` | TField |  | Range based on threshold. Multifonds DB Column is THRESHOLDS. |
| 6 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RANGE.IN.AMOUNT.START` | `FsGiDistAgentCommScaleDet_RangeInAmountStart` | TField |  | Amount to be taken into account for scale commission calculation at start of range. Multifonds DB Column is MNT_MIN. |
| 7 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RANGE.IN.AMOUNT.END` | `FsGiDistAgentCommScaleDet_RangeInAmountEnd` | TField |  | Amount to be taken into account for scale commission calculation at end of range. Multifonds DB Column is MNT_MAX. |
| 8 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.DURATION.START.OF.RANGE` | `FsGiDistAgentCommScaleDet_DurationStartOfRange` | TField |  | Field activated and automatically populated when the a Alternative feesa checkbox is ticked and the a Duration (months) a End of rangea field is entered. Multifonds DB Column is MONTH_MIN. |
| 9 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.DURATION.END.OF.RANGE` | `FsGiDistAgentCommScaleDet_DurationEndOfRange` | TField | Yes | Field is conditionally mandatory if a Range in percentagea &amp; a Range in amount a End of rangea are not defined. Multifonds DB Column is MONTH_MAX. |
| 10 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.MAXIMUM.PERCENTAGE` | `FsGiDistAgentCommScaleDet_MaximumPercentage` | TField |  | Maximum commission percentage. Multifonds DB Column is PCT_MAX. |
| 11 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.COMMISSION.PERCENTAGE` | `FsGiDistAgentCommScaleDet_CommissionPercentage` | TField |  | Commission percentage. Multifonds DB Column is PC_MNT. |
| 12 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.BASIS.POINTS` | `FsGiDistAgentCommScaleDet_BasisPoints` | TField |  | Scale basis points. Multifonds DB Column is BASIS_POINTS. |
| 13 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.COMMISSION.AMOUNT` | `FsGiDistAgentCommScaleDet_CommissionAmount` | TField |  | Commission amount. Multifonds DB Column is PC_AMMOUNT. |
| 14 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.SUB.SCALE.FLAG` | `FsGiDistAgentCommScaleDet_SubScaleFlag` | TField |  | Sub scale flag. Multifonds DB Column is FLG_SUB_SCALE. |
| 15 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED10` | `FsGiDistAgentCommScaleDet_Reserved10` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED9` | `FsGiDistAgentCommScaleDet_Reserved9` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED8` | `FsGiDistAgentCommScaleDet_Reserved8` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED7` | `FsGiDistAgentCommScaleDet_Reserved7` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED6` | `FsGiDistAgentCommScaleDet_Reserved6` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED5` | `FsGiDistAgentCommScaleDet_Reserved5` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED4` | `FsGiDistAgentCommScaleDet_Reserved4` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED3` | `FsGiDistAgentCommScaleDet_Reserved3` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED2` | `FsGiDistAgentCommScaleDet_Reserved2` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RESERVED1` | `FsGiDistAgentCommScaleDet_Reserved1` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.LOCAL.REF` | `FsGiDistAgentCommScaleDet_LocalRef` |  |  |  |
| 26 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.OVERRIDE` | `FsGiDistAgentCommScaleDet_Override` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.RECORD.STATUS` | `FsGiDistAgentCommScaleDet_RecordStatus` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.CURR.NO` | `FsGiDistAgentCommScaleDet_CurrNo` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.INPUTTER` | `FsGiDistAgentCommScaleDet_Inputter` |  |  |  |
| 30 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.DATE.TIME` | `FsGiDistAgentCommScaleDet_DateTime` |  |  |  |
| 31 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.AUTHORISER` | `FsGiDistAgentCommScaleDet_Authoriser` | String |  |  |
| 32 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.CO.CODE` | `FsGiDistAgentCommScaleDet_CoCode` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.DEPT.CODE` | `FsGiDistAgentCommScaleDet_DeptCode` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.AUDITOR.CODE` | `FsGiDistAgentCommScaleDet_AuditorCode` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.COMM.SCALE.DET.AUDIT.DATE.TIME` | `FsGiDistAgentCommScaleDet_AuditDateTime` | String |  |  |
