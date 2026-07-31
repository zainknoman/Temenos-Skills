# FS.GI.FUND.ADL.DEALING.PARAMETERS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.ADL.DEALING.PARAMETERS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.PARENT.REF.ID` | `FsGiFundAdlDealingParameters_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.ORA.ROWID` | `FsGiFundAdlDealingParameters_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.FUND.ID` | `FsGiFundAdlDealingParameters_FundId` | TField |  | MF Fund ID for which ADL parameterisation is scope. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.OPERATION.CODE` | `FsGiFundAdlDealingParameters_OperationCode` | TField |  | The operation code for which the ADL is applicable. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.ADL.DEFAULT.RATE` | `FsGiFundAdlDealingParameters_AdlDefaultRate` | TField |  | Rate in percentage of ADL to be charged by operation code. Multifonds DB Column is ADL_RATE. |
| 6 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.ADL.MAXIMUM.RATE` | `FsGiFundAdlDealingParameters_AdlMaximumRate` | TField |  | Maximum ADL rate till which the default rate can be forced. Multifonds DB Column is ADL_MAX_RATE. |
| 7 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.SSP.RATE.IN` | `FsGiFundAdlDealingParameters_SspRateIn` | TField |  | Rate in percentage of SSP to be charged by operation code. The rate is applied during SSP calculation only if the threshold has been breached with a net inflow. Multifonds DB Column is SSP_RATE_IN. |
| 8 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.SSP.RATE.OUT` | `FsGiFundAdlDealingParameters_SspRateOut` | TField |  | Rate in percentage of SSP to be charged by operation code. The rate is applied during SSP calculation, only if the threshold has been breached with a net outflow. Multifonds DB Column is SSP_RATE_OUT. |
| 9 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.EXCLUDE.FROM.NET.FLAG` | `FsGiFundAdlDealingParameters_ExcludeFromNetFlag` | TField |  | Flag to exclude the operation from net movement of the fund for comparison with the threshold. Multifonds DB Column is FLG_EXCL_NET. |
| 10 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.SELECTED.PRICE` | `FsGiFundAdlDealingParameters_SelectedPrice` | TField |  | Select price code applicable for the type of transaction. Multifonds DB Column is SELECTED_PRICE. |
| 11 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.EXCL.ADL.FROM.AMT.FLG` | `FsGiFundAdlDealingParameters_ExclAdlFromAmtFlg` | TField |  | Flag to indicate that Anti Dilution Levy (ADL) is excluded from order amount. Multifonds DB Column is FLG_TOP_ADL. |
| 12 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.ADL.PARAMETERS.INTERNAL.ID` | `FsGiFundAdlDealingParameters_AdlParametersInternalId` | TField |  | Unique internal identifier for Anti dilution levy record. Multifonds DB Column is INTERNAL_ID. |
| 13 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.ADL.TYPE` | `FsGiFundAdlDealingParameters_AdlType` | TField |  | Type of the Anti Dilution levy method. Multifonds DB Column is FLG_ADL_DEALING. |
| 14 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.THRESHOLD.TYPE` | `FsGiFundAdlDealingParameters_ThresholdType` | TField |  | Method for ADL threshold calculation. Multifonds DB Column is ADL_TYPE. |
| 15 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.SWUNG.FA.FLAG` | `FsGiFundAdlDealingParameters_SwungFaFlag` | TField |  | Flag to include or exclude orders with deal status &apos;Ready for final client trading desk&apos; from the SSP simulation process for thereshold calculation. Multifonds DB Column is FLG_SWUNG_FA. |
| 16 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.THRESHOLD.NAV.PERCENTAGE` | `FsGiFundAdlDealingParameters_ThresholdNavPercentage` | TField |  | Rate in percentage for threshold amount calculation. Multifonds DB Column is ADL_PCT. |
| 17 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.SOFT.THRESHOLD.FLAG` | `FsGiFundAdlDealingParameters_SoftThresholdFlag` | TField |  | Flag to enable soft threshold functionality. It is updatable only when the ADL type is &apos;0005&apos; (ADL charge on cash excess only). Multifonds DB Column is FLG_SFT_THRHLD. |
| 18 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.OPAQUE.SSP.FLAG` | `FsGiFundAdlDealingParameters_OpaqueSspFlag` | TField |  | Flag allows the user to generate some of the reports without ADL amount. Multifonds DB Column is FLG_OPAQUE_SSP. |
| 19 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.THRESHOLD.AMOUNT` | `FsGiFundAdlDealingParameters_ThresholdAmount` | TField |  | Threshold amount. Multifonds DB Column is THRESHOLD_AMT. |
| 20 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.THRESHOLD.CURRENCY` | `FsGiFundAdlDealingParameters_ThresholdCurrency` | TField |  | Threshold currency (in 3 letter ISO format &apos;USD&apos;). Multifonds DB Column is THRESHOLD_CCY. |
| 21 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED10` | `FsGiFundAdlDealingParameters_Reserved10` | TField |  |  |
| 22 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED9` | `FsGiFundAdlDealingParameters_Reserved9` | TField |  |  |
| 23 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED8` | `FsGiFundAdlDealingParameters_Reserved8` | TField |  |  |
| 24 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED7` | `FsGiFundAdlDealingParameters_Reserved7` | TField |  |  |
| 25 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED6` | `FsGiFundAdlDealingParameters_Reserved6` | TField |  |  |
| 26 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED5` | `FsGiFundAdlDealingParameters_Reserved5` | TField |  |  |
| 27 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED4` | `FsGiFundAdlDealingParameters_Reserved4` | TField |  |  |
| 28 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED3` | `FsGiFundAdlDealingParameters_Reserved3` | TField |  |  |
| 29 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED2` | `FsGiFundAdlDealingParameters_Reserved2` | TField |  |  |
| 30 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RESERVED1` | `FsGiFundAdlDealingParameters_Reserved1` | TField |  |  |
| 31 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.LOCAL.REF` | `FsGiFundAdlDealingParameters_LocalRef` |  |  |  |
| 32 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.OVERRIDE` | `FsGiFundAdlDealingParameters_Override` |  |  |  |
| 33 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.RECORD.STATUS` | `FsGiFundAdlDealingParameters_RecordStatus` | String |  |  |
| 34 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.CURR.NO` | `FsGiFundAdlDealingParameters_CurrNo` | String |  |  |
| 35 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.INPUTTER` | `FsGiFundAdlDealingParameters_Inputter` |  |  |  |
| 36 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.DATE.TIME` | `FsGiFundAdlDealingParameters_DateTime` |  |  |  |
| 37 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.AUTHORISER` | `FsGiFundAdlDealingParameters_Authoriser` | String |  |  |
| 38 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.CO.CODE` | `FsGiFundAdlDealingParameters_CoCode` | String |  |  |
| 39 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.DEPT.CODE` | `FsGiFundAdlDealingParameters_DeptCode` | String |  |  |
| 40 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.AUDITOR.CODE` | `FsGiFundAdlDealingParameters_AuditorCode` | String |  |  |
| 41 | `FS.GI.FUND.ADL.DEALING.PARAMETERS.AUDIT.DATE.TIME` | `FsGiFundAdlDealingParameters_AuditDateTime` | String |  |  |
