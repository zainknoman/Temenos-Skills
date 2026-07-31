# FS.GI.DIST.AGENT.COMM.SCALE — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.COMM.SCALE` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.COMM.SCALE.PARENT.REF.ID` | `FsGiDistAgentCommScale_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.COMM.SCALE.ORA.ROWID` | `FsGiDistAgentCommScale_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.COMM.SCALE.SCALE.ID` | `FsGiDistAgentCommScale_ScaleId` | TField |  | Commission scale ID. Multifonds DB Column is CBAREME. |
| 4 | `FS.GI.DIST.AGENT.COMM.SCALE.SCALE.DESCRIPTION` | `FsGiDistAgentCommScale_ScaleDescription` | TField |  | Commission scale description. Multifonds DB Column is LIB_CBAREME. |
| 5 | `FS.GI.DIST.AGENT.COMM.SCALE.CALCULATION.TYPE` | `FsGiDistAgentCommScale_CalculationType` | TField |  | Commission scale calculation type. Multifonds DB Column is CCALCUL. |
| 6 | `FS.GI.DIST.AGENT.COMM.SCALE.PAYMENT.CURRENCY` | `FsGiDistAgentCommScale_PaymentCurrency` | TField |  | Currency code (in 3 letter ISO code, Eg: EUR) in which the amount ranges will be defined. Multifonds DB Column is CMON. |
| 7 | `FS.GI.DIST.AGENT.COMM.SCALE.MIN.SUBSCRIPTION.AMOUNT` | `FsGiDistAgentCommScale_MinSubscriptionAmount` | TField |  | Minimum amount to be taken into account for scale commission calculation. Multifonds DB Column is MNT_MIN. |
| 8 | `FS.GI.DIST.AGENT.COMM.SCALE.MAXIMUM.AMOUNT` | `FsGiDistAgentCommScale_MaximumAmount` | TField |  | Maximum amount to be taken into account for scale commission calculation. Multifonds DB Column is MNT_MAX. |
| 9 | `FS.GI.DIST.AGENT.COMM.SCALE.MINIMUM.COMMISSION` | `FsGiDistAgentCommScale_MinimumCommission` | TField |  | Minimum commission to be applied for the scale commission calculation. Multifonds DB Column is MIN_COMM. |
| 10 | `FS.GI.DIST.AGENT.COMM.SCALE.MAXIMUM.COMMISSION` | `FsGiDistAgentCommScale_MaximumCommission` | TField |  | Maximum commission to be applied for the scale commission calculation. Multifonds DB Column is MAX_COMM. |
| 11 | `FS.GI.DIST.AGENT.COMM.SCALE.AGGREGATION.METHOD` | `FsGiDistAgentCommScale_AggregationMethod` | TField |  | Different options to aggregate assets and calculate the scale capital basis which is compared to the scale to determine the applicable fee rate. Multifonds DB Column is AGGRTN_MHTD. |
| 12 | `FS.GI.DIST.AGENT.COMM.SCALE.ALTERNATE.FEES.FLAG` | `FsGiDistAgentCommScale_AlternateFeesFlag` | TField |  | Flag to specify alternative fees. Multifonds DB Column is FLG_ALT_FEE. |
| 13 | `FS.GI.DIST.AGENT.COMM.SCALE.PERFORMANCE.FEE.CAP` | `FsGiDistAgentCommScale_PerformanceFeeCap` | TField |  | Performance fee cap Ppercentage. Multifonds DB Column is PF_CAP. |
| 14 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED10` | `FsGiDistAgentCommScale_Reserved10` | TField |  |  |
| 15 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED9` | `FsGiDistAgentCommScale_Reserved9` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED8` | `FsGiDistAgentCommScale_Reserved8` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED7` | `FsGiDistAgentCommScale_Reserved7` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED6` | `FsGiDistAgentCommScale_Reserved6` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED5` | `FsGiDistAgentCommScale_Reserved5` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED4` | `FsGiDistAgentCommScale_Reserved4` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED3` | `FsGiDistAgentCommScale_Reserved3` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED2` | `FsGiDistAgentCommScale_Reserved2` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.COMM.SCALE.RESERVED1` | `FsGiDistAgentCommScale_Reserved1` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.COMM.SCALE.LOCAL.REF` | `FsGiDistAgentCommScale_LocalRef` |  |  |  |
| 25 | `FS.GI.DIST.AGENT.COMM.SCALE.OVERRIDE` | `FsGiDistAgentCommScale_Override` |  |  |  |
| 26 | `FS.GI.DIST.AGENT.COMM.SCALE.RECORD.STATUS` | `FsGiDistAgentCommScale_RecordStatus` | String |  |  |
| 27 | `FS.GI.DIST.AGENT.COMM.SCALE.CURR.NO` | `FsGiDistAgentCommScale_CurrNo` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.COMM.SCALE.INPUTTER` | `FsGiDistAgentCommScale_Inputter` |  |  |  |
| 29 | `FS.GI.DIST.AGENT.COMM.SCALE.DATE.TIME` | `FsGiDistAgentCommScale_DateTime` |  |  |  |
| 30 | `FS.GI.DIST.AGENT.COMM.SCALE.AUTHORISER` | `FsGiDistAgentCommScale_Authoriser` | String |  |  |
| 31 | `FS.GI.DIST.AGENT.COMM.SCALE.CO.CODE` | `FsGiDistAgentCommScale_CoCode` | String |  |  |
| 32 | `FS.GI.DIST.AGENT.COMM.SCALE.DEPT.CODE` | `FsGiDistAgentCommScale_DeptCode` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.COMM.SCALE.AUDITOR.CODE` | `FsGiDistAgentCommScale_AuditorCode` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.COMM.SCALE.AUDIT.DATE.TIME` | `FsGiDistAgentCommScale_AuditDateTime` | String |  |  |
