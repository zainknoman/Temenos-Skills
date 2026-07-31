# FS.GI.DIST.AGENT.COMM.SUB.SCALE — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.COMM.SUB.SCALE` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.PARENT.REF.ID` | `FsGiDistAgentCommSubScale_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.ORA.ROWID` | `FsGiDistAgentCommSubScale_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.SCALE.ID` | `FsGiDistAgentCommSubScale_ScaleId` | TField |  | Commission Scale ID Multifonds DB Column is CBAREME. |
| 4 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.CALCULATION.TYPE` | `FsGiDistAgentCommSubScale_CalculationType` | TField |  | Scale Calculation type Multifonds DB Column is CCALCUL. |
| 5 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.AGGREGATION.METHOD` | `FsGiDistAgentCommSubScale_AggregationMethod` | TField |  | Asset Aggregation method to calculate capital basis to compare with the scale Multifonds DB Column is AGGRTN_MHTD. |
| 6 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.CONDITION` | `FsGiDistAgentCommSubScale_Condition` | TField |  | Range based on threshold condition. Multifonds DB Column is CONDITION. |
| 7 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.THRESHOLDS` | `FsGiDistAgentCommSubScale_Thresholds` | TField |  | Range based on threshold. Multifonds DB Column is THRESHOLDS. |
| 8 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RANGE.IN.AMOUNT.START` | `FsGiDistAgentCommSubScale_RangeInAmountStart` | TField |  | Amount to be taken into account for scale commission calculation at start of range. Multifonds DB Column is MNT_MIN. |
| 9 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RANGE.IN.AMOUNT.END` | `FsGiDistAgentCommSubScale_RangeInAmountEnd` | TField |  | Amount to be taken into account for scale commission calculation at end of range. Multifonds DB Column is MNT_MAX. |
| 10 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.DURATION.START.OF.RANGE` | `FsGiDistAgentCommSubScale_DurationStartOfRange` | TField |  | Field activated and automatically populated when the a Alternative feesa checkbox is ticked and the a Duration (months) a End of rangea field is entered. Multifonds DB Column is MONTH_MIN. |
| 11 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.DURATION.END.OF.RANGE` | `FsGiDistAgentCommSubScale_DurationEndOfRange` | TField | Yes | Field is conditionally mandatory if a Range in percentagea &amp; a Range in amount a End of rangea are not defined. Multifonds DB Column is MONTH_MAX. |
| 12 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.MAXIMUM.PERCENTAGE` | `FsGiDistAgentCommSubScale_MaximumPercentage` | TField |  | Maximum commission percentage. Multifonds DB Column is PCT_MAX. |
| 13 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.SUBSCALE.RANGE.IN.AMT.START` | `FsGiDistAgentCommSubScale_SubscaleRangeInAmtStart` | TField |  | Amount to be taken into account for sub scale commission calculation at start of range. Multifonds DB Column is SUB_MNT_MIN. |
| 14 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.SUBSCALE.RANGE.IN.AMOUNT.END` | `FsGiDistAgentCommSubScale_SubscaleRangeInAmountEnd` | TField |  | Amount to be taken into account for sub scale commission calculation at end of range. Multifonds DB Column is SUB_MNT_MAX. |
| 15 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.SUB.SCALE.DUR.START.OF.RANGE` | `FsGiDistAgentCommSubScale_SubScaleDurStartOfRange` | TField |  | Field activated and automatically populated when the a Alternative feesa checkbox is ticked and the a Duration (months) a End of rangea field is entered. Multifonds DB Column is SUB_MONTH_MIN. |
| 16 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.SUBSCALE.DURATON.END.OF.RANGE` | `FsGiDistAgentCommSubScale_SubscaleDuratonEndOfRange` | TField |  | Sub scale duration at end of range. Multifonds DB Column is SUB_MONTH_MAX. |
| 17 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.COMMISSION.PERCENTAGE` | `FsGiDistAgentCommSubScale_CommissionPercentage` | TField |  | Commission percentage. Multifonds DB Column is PC_MNT. |
| 18 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.BASIS.POINTS` | `FsGiDistAgentCommSubScale_BasisPoints` | TField |  | Scale basis points. Multifonds DB Column is BASIS_POINTS. |
| 19 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.COMMISSION.AMOUNT` | `FsGiDistAgentCommSubScale_CommissionAmount` | TField |  | Commission amount. Multifonds DB Column is PC_AMOUNT. |
| 20 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED10` | `FsGiDistAgentCommSubScale_Reserved10` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED9` | `FsGiDistAgentCommSubScale_Reserved9` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED8` | `FsGiDistAgentCommSubScale_Reserved8` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED7` | `FsGiDistAgentCommSubScale_Reserved7` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED6` | `FsGiDistAgentCommSubScale_Reserved6` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED5` | `FsGiDistAgentCommSubScale_Reserved5` | TField |  |  |
| 26 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED4` | `FsGiDistAgentCommSubScale_Reserved4` | TField |  |  |
| 27 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED3` | `FsGiDistAgentCommSubScale_Reserved3` | TField |  |  |
| 28 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED2` | `FsGiDistAgentCommSubScale_Reserved2` | TField |  |  |
| 29 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RESERVED1` | `FsGiDistAgentCommSubScale_Reserved1` | TField |  |  |
| 30 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.LOCAL.REF` | `FsGiDistAgentCommSubScale_LocalRef` |  |  |  |
| 31 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.OVERRIDE` | `FsGiDistAgentCommSubScale_Override` |  |  |  |
| 32 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.RECORD.STATUS` | `FsGiDistAgentCommSubScale_RecordStatus` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.CURR.NO` | `FsGiDistAgentCommSubScale_CurrNo` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.INPUTTER` | `FsGiDistAgentCommSubScale_Inputter` |  |  |  |
| 35 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.DATE.TIME` | `FsGiDistAgentCommSubScale_DateTime` |  |  |  |
| 36 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.AUTHORISER` | `FsGiDistAgentCommSubScale_Authoriser` | String |  |  |
| 37 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.CO.CODE` | `FsGiDistAgentCommSubScale_CoCode` | String |  |  |
| 38 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.DEPT.CODE` | `FsGiDistAgentCommSubScale_DeptCode` | String |  |  |
| 39 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.AUDITOR.CODE` | `FsGiDistAgentCommSubScale_AuditorCode` | String |  |  |
| 40 | `FS.GI.DIST.AGENT.COMM.SUB.SCALE.AUDIT.DATE.TIME` | `FsGiDistAgentCommSubScale_AuditDateTime` | String |  |  |
