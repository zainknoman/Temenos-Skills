# FS.GA.SCALE — Table Schema

> Source: `INSERTS/I_F.FS.GA.SCALE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SCALE.SCALE` | `FsGaScale_ScaleCode` |  |  |  |
| 2 | `FS.GA.SCALE.SCALE.CODE.DESCRIPTION` | `FsGaScale_ScaleCodeDescription` |  |  |  |
| 3 | `FS.GA.SCALE.PRICING.FACTOR.CODE` | `FsGaScale_CalculationCode` |  |  |  |
| 4 | `FS.GA.SCALE.LOWEST` | `FsGaScale_Lowest` |  |  |  |
| 5 | `FS.GA.SCALE.HIGHEST` | `FsGaScale_Highest` |  |  |  |
| 6 | `FS.GA.SCALE.MINIMUM` | `FsGaScale_Minimum` |  |  |  |
| 7 | `FS.GA.SCALE.MAXIMUM` | `FsGaScale_Maximum` |  |  |  |
| 8 | `FS.GA.SCALE.SCALE.MINIMUM.AMOUNT.CCY` | `FsGaScale_ScaleMinimumAmountCcy` |  |  |  |
| 9 | `FS.GA.SCALE.SCALE.MAXIMUM.AMOUNT.CCY` | `FsGaScale_ScaleMaximumAmountCcy` |  |  |  |
| 10 | `FS.GA.SCALE.EFFECTIVE.DATE` | `FsGaScale_EffectiveDate` |  |  |  |
| 11 | `FS.GA.SCALE.FEES.ADJUST.FOR.SCALE` | `FsGaScale_FeesAdjustForScale` |  |  |  |
| 12 | `FS.GA.SCALE.RESERVED10` | `FsGaScale_Reserved10` |  |  |  |
| 13 | `FS.GA.SCALE.RESERVED9` | `FsGaScale_Reserved9` |  |  |  |
| 14 | `FS.GA.SCALE.RESERVED8` | `FsGaScale_Reserved8` |  |  |  |
| 15 | `FS.GA.SCALE.RESERVED7` | `FsGaScale_Reserved7` |  |  |  |
| 16 | `FS.GA.SCALE.RESERVED6` | `FsGaScale_Reserved6` |  |  |  |
| 17 | `FS.GA.SCALE.RESERVED5` | `FsGaScale_Reserved5` |  |  |  |
| 18 | `FS.GA.SCALE.RESERVED4` | `FsGaScale_Reserved4` |  |  |  |
| 19 | `FS.GA.SCALE.RESERVED3` | `FsGaScale_Reserved3` |  |  |  |
| 20 | `FS.GA.SCALE.RESERVED2` | `FsGaScale_Reserved2` |  |  |  |
| 21 | `FS.GA.SCALE.RESERVED1` | `FsGaScale_Reserved1` |  |  |  |
| 22 | `FS.GA.SCALE.RECORD.STATUS` | `FsGaScale_RecordStatus` |  |  |  |
| 23 | `FS.GA.SCALE.CURR.NO` | `FsGaScale_CurrNo` |  |  |  |
| 24 | `FS.GA.SCALE.INPUTTER` | `FsGaScale_Inputter` |  |  |  |
| 25 | `FS.GA.SCALE.DATE.TIME` | `FsGaScale_DateTime` |  |  |  |
| 26 | `FS.GA.SCALE.AUTHORISER` | `FsGaScale_Authoriser` |  |  |  |
| 27 | `FS.GA.SCALE.CO.CODE` | `FsGaScale_CoCode` |  |  |  |
| 28 | `FS.GA.SCALE.DEPT.CODE` | `FsGaScale_DeptCode` |  |  |  |
| 29 | `FS.GA.SCALE.AUDITOR.CODE` | `FsGaScale_AuditorCode` |  |  |  |
| 30 | `FS.GA.SCALE.AUDIT.DATE.TIME` | `FsGaScale_AuditDateTime` |  |  |  |
