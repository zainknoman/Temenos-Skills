# FS.GA.CALCULATION.OPTIONS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CALCULATION.OPTIONS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CALCULATION.OPTIONS.OPTION.NUMBER` | `FsGaCalculationOptions_OptionNumber` | TField |  | Option Number Multifonds DB Column is NOPT. |
| 2 | `CALCULATION.OPTIONS.PRICING.FACTOR.CODE` | `FsGaCalculationOptions_CalculationCode` |  |  |  |
| 3 | `CALCULATION.OPTIONS.CALCULATION.TYPE.1` | `FsGaCalculationOptions_CalculationType1` | TField |  | Calculation Type 1 Multifonds DB Column is TYP_CALC1. |
| 4 | `CALCULATION.OPTIONS.CALCULATION.TYPE.2` | `FsGaCalculationOptions_CalculationType2` | TField |  | Calculation Type 2 Multifonds DB Column is TYP_CALC2. |
| 5 | `CALCULATION.OPTIONS.COEFFICIENT.PERCENTAGE` | `FsGaCalculationOptions_CoefficientPercentage` | TField |  | Coefficient Percentage Multifonds DB Column is COEFF_CAL2. |
| 6 | `CALCULATION.OPTIONS.RECORD.STATUS` | `FsGaCalculationOptions_RecordStatus` | String |  |  |
| 7 | `CALCULATION.OPTIONS.CURR.NO` | `FsGaCalculationOptions_CurrNo` | String |  |  |
| 8 | `CALCULATION.OPTIONS.INPUTTER` | `FsGaCalculationOptions_Inputter` |  |  |  |
| 9 | `CALCULATION.OPTIONS.DATE.TIME` | `FsGaCalculationOptions_DateTime` |  |  |  |
| 10 | `CALCULATION.OPTIONS.AUTHORISER` | `FsGaCalculationOptions_Authoriser` | String |  |  |
| 11 | `CALCULATION.OPTIONS.CO.CODE` | `FsGaCalculationOptions_CoCode` | String |  |  |
| 12 | `CALCULATION.OPTIONS.DEPT.CODE` | `FsGaCalculationOptions_DeptCode` | String |  |  |
| 13 | `CALCULATION.OPTIONS.AUDITOR.CODE` | `FsGaCalculationOptions_AuditorCode` | String |  |  |
| 14 | `CALCULATION.OPTIONS.AUDIT.DATE.TIME` | `FsGaCalculationOptions_AuditDateTime` | String |  |  |
