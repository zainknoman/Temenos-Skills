# FS.GA.OPTION.MARGIN.CALCULATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.MARGIN.CALCULATION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.MARGIN.CALCULATION.PARENT.REF.ID` | `FsGaOptionMarginCalculation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPTION.MARGIN.CALCULATION.ORA.ROWID` | `FsGaOptionMarginCalculation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPTION.MARGIN.CALCULATION.OPTION.ID` | `FsGaOptionMarginCalculation_OptionId` | TField |  | Option Security ID Multifonds DB Column is NOPT. |
| 4 | `FS.GA.OPTION.MARGIN.CALCULATION.CALCULATION.CODE` | `FsGaOptionMarginCalculation_CalculationCode` | TField |  | Corresponds to calculation code Multifonds DB Column is CODE_CALC. |
| 5 | `FS.GA.OPTION.MARGIN.CALCULATION.CALCULATION.TYPE.1` | `FsGaOptionMarginCalculation_CalculationType1` | TField |  | Calculation Type 1 Multifonds DB Column is TYP_CALC1. |
| 6 | `FS.GA.OPTION.MARGIN.CALCULATION.CALCULATION.TYPE.2` | `FsGaOptionMarginCalculation_CalculationType2` | TField |  | Calculation Type 2 Multifonds DB Column is TYP_CALC2. |
| 7 | `FS.GA.OPTION.MARGIN.CALCULATION.PERCENT` | `FsGaOptionMarginCalculation_Percent` | TField |  | Percent of margin calculation Multifonds DB Column is COEFF_CAL2. |
| 8 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED10` | `FsGaOptionMarginCalculation_Reserved10` | TField |  |  |
| 9 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED9` | `FsGaOptionMarginCalculation_Reserved9` | TField |  |  |
| 10 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED8` | `FsGaOptionMarginCalculation_Reserved8` | TField |  |  |
| 11 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED7` | `FsGaOptionMarginCalculation_Reserved7` | TField |  |  |
| 12 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED6` | `FsGaOptionMarginCalculation_Reserved6` | TField |  |  |
| 13 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED5` | `FsGaOptionMarginCalculation_Reserved5` | TField |  |  |
| 14 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED4` | `FsGaOptionMarginCalculation_Reserved4` | TField |  |  |
| 15 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED3` | `FsGaOptionMarginCalculation_Reserved3` | TField |  |  |
| 16 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED2` | `FsGaOptionMarginCalculation_Reserved2` | TField |  |  |
| 17 | `FS.GA.OPTION.MARGIN.CALCULATION.RESERVED1` | `FsGaOptionMarginCalculation_Reserved1` | TField |  |  |
| 18 | `FS.GA.OPTION.MARGIN.CALCULATION.LOCAL.REF` | `FsGaOptionMarginCalculation_LocalRef` |  |  |  |
| 19 | `FS.GA.OPTION.MARGIN.CALCULATION.OVERRIDE` | `FsGaOptionMarginCalculation_Override` |  |  |  |
| 20 | `FS.GA.OPTION.MARGIN.CALCULATION.RECORD.STATUS` | `FsGaOptionMarginCalculation_RecordStatus` | String |  |  |
| 21 | `FS.GA.OPTION.MARGIN.CALCULATION.CURR.NO` | `FsGaOptionMarginCalculation_CurrNo` | String |  |  |
| 22 | `FS.GA.OPTION.MARGIN.CALCULATION.INPUTTER` | `FsGaOptionMarginCalculation_Inputter` |  |  |  |
| 23 | `FS.GA.OPTION.MARGIN.CALCULATION.DATE.TIME` | `FsGaOptionMarginCalculation_DateTime` |  |  |  |
| 24 | `FS.GA.OPTION.MARGIN.CALCULATION.AUTHORISER` | `FsGaOptionMarginCalculation_Authoriser` | String |  |  |
| 25 | `FS.GA.OPTION.MARGIN.CALCULATION.CO.CODE` | `FsGaOptionMarginCalculation_CoCode` | String |  |  |
| 26 | `FS.GA.OPTION.MARGIN.CALCULATION.DEPT.CODE` | `FsGaOptionMarginCalculation_DeptCode` | String |  |  |
| 27 | `FS.GA.OPTION.MARGIN.CALCULATION.AUDITOR.CODE` | `FsGaOptionMarginCalculation_AuditorCode` | String |  |  |
| 28 | `FS.GA.OPTION.MARGIN.CALCULATION.AUDIT.DATE.TIME` | `FsGaOptionMarginCalculation_AuditDateTime` | String |  |  |
