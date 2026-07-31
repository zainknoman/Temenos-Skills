# FS.GI.WEM.CONTROL.THRESHOLD.PARAM — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.CONTROL.THRESHOLD.PARAM` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.WEM.CONTROL.THRESHOLD.PARAM.EXCHANGE.GROUP` | `FsGiWemControlThresholdParam_ExchangeGroup` | TField |  | Exchange group for which the threshold is defined. Multifonds DB Column is CGROUPE_COURS. |
| 2 | `GI.WEM.CONTROL.THRESHOLD.PARAM.FUND.ID` | `FsGiWemControlThresholdParam_FundId` | TField |  | Fund ID for which the threshold is defined. Multifonds DB Column is NPTF. |
| 3 | `GI.WEM.CONTROL.THRESHOLD.PARAM.SHARE.CLASS.CODE` | `FsGiWemControlThresholdParam_ShareClassCode` | TField |  | Share class code for which the threshold is defined. Multifonds DB Column is TPART. |
| 4 | `GI.WEM.CONTROL.THRESHOLD.PARAM.AMT.VARIATION.PCT.NB.OF.DAY` | `FsGiWemControlThresholdParam_AmtVariationPctNbOfDay` | TField |  | Value of threshold as amount, percentage of variation or numberof days. Multifonds DB Column is MNT_PCT. |
| 5 | `GI.WEM.CONTROL.THRESHOLD.PARAM.PAYMENT.CURRENCY` | `FsGiWemControlThresholdParam_PaymentCurrency` | TField |  | Currency of the threshold amount. Multifonds DB Column is CMON. |
| 6 | `GI.WEM.CONTROL.THRESHOLD.PARAM.EFFECTIVE.DATE` | `FsGiWemControlThresholdParam_EffectiveDate` | TField |  | Effective date from which the threshold is held. Multifonds DB Column is EFT_DATE. |
| 7 | `GI.WEM.CONTROL.THRESHOLD.PARAM.CONTROL.ID` | `FsGiWemControlThresholdParam_ControlId` | TField |  | Unique control identification number. Multifonds DB Column is TYP_CTRL_ID. |
| 8 | `GI.WEM.CONTROL.THRESHOLD.PARAM.THRESHOLD.TYPE` | `FsGiWemControlThresholdParam_ThresholdType` | TField |  | WEM control threshold type. Multifonds DB Column is TYP_THRESH. |
| 9 | `GI.WEM.CONTROL.THRESHOLD.PARAM.CONTROL.SEQUENCE` | `FsGiWemControlThresholdParam_ControlSequence` | TField |  | WEM control threshold sequence number. Multifonds DB Column is CTRL_SEQ. |
| 10 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED10` | `FsGiWemControlThresholdParam_Reserved10` | TField |  |  |
| 11 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED9` | `FsGiWemControlThresholdParam_Reserved9` | TField |  |  |
| 12 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED8` | `FsGiWemControlThresholdParam_Reserved8` | TField |  |  |
| 13 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED7` | `FsGiWemControlThresholdParam_Reserved7` | TField |  |  |
| 14 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED6` | `FsGiWemControlThresholdParam_Reserved6` | TField |  |  |
| 15 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED5` | `FsGiWemControlThresholdParam_Reserved5` | TField |  |  |
| 16 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED4` | `FsGiWemControlThresholdParam_Reserved4` | TField |  |  |
| 17 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED3` | `FsGiWemControlThresholdParam_Reserved3` | TField |  |  |
| 18 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED2` | `FsGiWemControlThresholdParam_Reserved2` | TField |  |  |
| 19 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RESERVED1` | `FsGiWemControlThresholdParam_Reserved1` | TField |  |  |
| 20 | `GI.WEM.CONTROL.THRESHOLD.PARAM.LOCAL.REF` | `FsGiWemControlThresholdParam_LocalRef` |  |  |  |
| 21 | `GI.WEM.CONTROL.THRESHOLD.PARAM.OVERRIDE` | `FsGiWemControlThresholdParam_Override` |  |  |  |
| 22 | `GI.WEM.CONTROL.THRESHOLD.PARAM.RECORD.STATUS` | `FsGiWemControlThresholdParam_RecordStatus` | String |  |  |
| 23 | `GI.WEM.CONTROL.THRESHOLD.PARAM.CURR.NO` | `FsGiWemControlThresholdParam_CurrNo` | String |  |  |
| 24 | `GI.WEM.CONTROL.THRESHOLD.PARAM.INPUTTER` | `FsGiWemControlThresholdParam_Inputter` |  |  |  |
| 25 | `GI.WEM.CONTROL.THRESHOLD.PARAM.DATE.TIME` | `FsGiWemControlThresholdParam_DateTime` |  |  |  |
| 26 | `GI.WEM.CONTROL.THRESHOLD.PARAM.AUTHORISER` | `FsGiWemControlThresholdParam_Authoriser` | String |  |  |
| 27 | `GI.WEM.CONTROL.THRESHOLD.PARAM.CO.CODE` | `FsGiWemControlThresholdParam_CoCode` | String |  |  |
| 28 | `GI.WEM.CONTROL.THRESHOLD.PARAM.DEPT.CODE` | `FsGiWemControlThresholdParam_DeptCode` | String |  |  |
| 29 | `GI.WEM.CONTROL.THRESHOLD.PARAM.AUDITOR.CODE` | `FsGiWemControlThresholdParam_AuditorCode` | String |  |  |
| 30 | `GI.WEM.CONTROL.THRESHOLD.PARAM.AUDIT.DATE.TIME` | `FsGiWemControlThresholdParam_AuditDateTime` | String |  |  |
