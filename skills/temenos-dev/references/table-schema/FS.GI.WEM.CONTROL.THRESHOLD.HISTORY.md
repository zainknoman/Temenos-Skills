# FS.GI.WEM.CONTROL.THRESHOLD.HISTORY — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.CONTROL.THRESHOLD.HISTORY` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.WEM.CONTROL.THRESHOLD.HIS.EXCHANGE.GROUP` | `FsGiWemControlThresholdHistory_ExchangeGroup` | TField |  | Exchange group for which the threshold is defined. Multifonds DB Column is CGROUPE_COURS. |
| 2 | `GI.WEM.CONTROL.THRESHOLD.HIS.FUND.ID` | `FsGiWemControlThresholdHistory_FundId` | TField |  | Fund ID for which the threshold is defined. Multifonds DB Column is NPTF. |
| 3 | `GI.WEM.CONTROL.THRESHOLD.HIS.SHARE.CLASS.CODE` | `FsGiWemControlThresholdHistory_ShareClassCode` | TField |  | Share class code for which the threshold is defined. Multifonds DB Column is TPART. |
| 4 | `GI.WEM.CONTROL.THRESHOLD.HIS.AMT.VARIATION.PCT.NB.OF.DAY` | `FsGiWemControlThresholdHistory_AmtVariationPctNbOfDay` | TField |  | Value of threshold as amount, percentage of variation or number of days. Multifonds DB Column is MNT_PCT. |
| 5 | `GI.WEM.CONTROL.THRESHOLD.HIS.PAYMENT.CURRENCY` | `FsGiWemControlThresholdHistory_PaymentCurrency` | TField |  | Currency of the threshold amount. Multifonds DB Column is CMON. |
| 6 | `GI.WEM.CONTROL.THRESHOLD.HIS.EFFECTIVE.DATE` | `FsGiWemControlThresholdHistory_EffectiveDate` | TField |  | Effective date from which the threshold is held. Multifonds DB Column is EFT_DATE. |
| 7 | `GI.WEM.CONTROL.THRESHOLD.HIS.CONTROL.ID` | `FsGiWemControlThresholdHistory_ControlId` | TField |  | Unique control identification number. Multifonds DB Column is TYP_CTRL_ID. |
| 8 | `GI.WEM.CONTROL.THRESHOLD.HIS.THRESHOLD.TYPE` | `FsGiWemControlThresholdHistory_ThresholdType` | TField |  | Threshold type. Multifonds DB Column is TYP_THRESH. |
| 9 | `GI.WEM.CONTROL.THRESHOLD.HIS.CONTROL.SEQUENCE` | `FsGiWemControlThresholdHistory_ControlSequence` | TField |  | WEM control threshold sequence number. Multifonds DB Column is CTRL_SEQ. |
| 10 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED10` | `FsGiWemControlThresholdHistory_Reserved10` | TField |  |  |
| 11 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED9` | `FsGiWemControlThresholdHistory_Reserved9` | TField |  |  |
| 12 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED8` | `FsGiWemControlThresholdHistory_Reserved8` | TField |  |  |
| 13 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED7` | `FsGiWemControlThresholdHistory_Reserved7` | TField |  |  |
| 14 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED6` | `FsGiWemControlThresholdHistory_Reserved6` | TField |  |  |
| 15 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED5` | `FsGiWemControlThresholdHistory_Reserved5` | TField |  |  |
| 16 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED4` | `FsGiWemControlThresholdHistory_Reserved4` | TField |  |  |
| 17 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED3` | `FsGiWemControlThresholdHistory_Reserved3` | TField |  |  |
| 18 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED2` | `FsGiWemControlThresholdHistory_Reserved2` | TField |  |  |
| 19 | `GI.WEM.CONTROL.THRESHOLD.HIS.RESERVED1` | `FsGiWemControlThresholdHistory_Reserved1` | TField |  |  |
| 20 | `GI.WEM.CONTROL.THRESHOLD.HIS.LOCAL.REF` | `FsGiWemControlThresholdHistory_LocalRef` |  |  |  |
| 21 | `GI.WEM.CONTROL.THRESHOLD.HIS.OVERRIDE` | `FsGiWemControlThresholdHistory_Override` |  |  |  |
| 22 | `GI.WEM.CONTROL.THRESHOLD.HIS.RECORD.STATUS` | `FsGiWemControlThresholdHistory_RecordStatus` | String |  |  |
| 23 | `GI.WEM.CONTROL.THRESHOLD.HIS.CURR.NO` | `FsGiWemControlThresholdHistory_CurrNo` | String |  |  |
| 24 | `GI.WEM.CONTROL.THRESHOLD.HIS.INPUTTER` | `FsGiWemControlThresholdHistory_Inputter` |  |  |  |
| 25 | `GI.WEM.CONTROL.THRESHOLD.HIS.DATE.TIME` | `FsGiWemControlThresholdHistory_DateTime` |  |  |  |
| 26 | `GI.WEM.CONTROL.THRESHOLD.HIS.AUTHORISER` | `FsGiWemControlThresholdHistory_Authoriser` | String |  |  |
| 27 | `GI.WEM.CONTROL.THRESHOLD.HIS.CO.CODE` | `FsGiWemControlThresholdHistory_CoCode` | String |  |  |
| 28 | `GI.WEM.CONTROL.THRESHOLD.HIS.DEPT.CODE` | `FsGiWemControlThresholdHistory_DeptCode` | String |  |  |
| 29 | `GI.WEM.CONTROL.THRESHOLD.HIS.AUDITOR.CODE` | `FsGiWemControlThresholdHistory_AuditorCode` | String |  |  |
| 30 | `GI.WEM.CONTROL.THRESHOLD.HIS.AUDIT.DATE.TIME` | `FsGiWemControlThresholdHistory_AuditDateTime` | String |  |  |
