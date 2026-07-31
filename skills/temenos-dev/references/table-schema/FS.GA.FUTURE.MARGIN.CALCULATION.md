# FS.GA.FUTURE.MARGIN.CALCULATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.MARGIN.CALCULATION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.MARGIN.CALCULATION.PARENT.REF.ID` | `FsGaFutureMarginCalculation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.MARGIN.CALCULATION.ORA.ROWID` | `FsGaFutureMarginCalculation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.MARGIN.CALCULATION.FUTURE.ID.CODE` | `FsGaFutureMarginCalculation_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 4 | `FS.GA.FUTURE.MARGIN.CALCULATION.CALCULATION.CODE` | `FsGaFutureMarginCalculation_CalculationCode` | TField |  | Corresponds to calculation code Multifonds DB Column is CODE_CALC. |
| 5 | `FS.GA.FUTURE.MARGIN.CALCULATION.CALCULATION.TYPE` | `FsGaFutureMarginCalculation_CalculationType` | TField |  | Calulation Type Multifonds DB Column is TYP_CALC. |
| 6 | `FS.GA.FUTURE.MARGIN.CALCULATION.PER.CENT` | `FsGaFutureMarginCalculation_PerCent` | TField |  | Percent of margin calculation Multifonds DB Column is COEFF_CAL. |
| 7 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED10` | `FsGaFutureMarginCalculation_Reserved10` | TField |  |  |
| 8 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED9` | `FsGaFutureMarginCalculation_Reserved9` | TField |  |  |
| 9 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED8` | `FsGaFutureMarginCalculation_Reserved8` | TField |  |  |
| 10 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED7` | `FsGaFutureMarginCalculation_Reserved7` | TField |  |  |
| 11 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED6` | `FsGaFutureMarginCalculation_Reserved6` | TField |  |  |
| 12 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED5` | `FsGaFutureMarginCalculation_Reserved5` | TField |  |  |
| 13 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED4` | `FsGaFutureMarginCalculation_Reserved4` | TField |  |  |
| 14 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED3` | `FsGaFutureMarginCalculation_Reserved3` | TField |  |  |
| 15 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED2` | `FsGaFutureMarginCalculation_Reserved2` | TField |  |  |
| 16 | `FS.GA.FUTURE.MARGIN.CALCULATION.RESERVED1` | `FsGaFutureMarginCalculation_Reserved1` | TField |  |  |
| 17 | `FS.GA.FUTURE.MARGIN.CALCULATION.LOCAL.REF` | `FsGaFutureMarginCalculation_LocalRef` |  |  |  |
| 18 | `FS.GA.FUTURE.MARGIN.CALCULATION.OVERRIDE` | `FsGaFutureMarginCalculation_Override` |  |  |  |
| 19 | `FS.GA.FUTURE.MARGIN.CALCULATION.RECORD.STATUS` | `FsGaFutureMarginCalculation_RecordStatus` | String |  |  |
| 20 | `FS.GA.FUTURE.MARGIN.CALCULATION.CURR.NO` | `FsGaFutureMarginCalculation_CurrNo` | String |  |  |
| 21 | `FS.GA.FUTURE.MARGIN.CALCULATION.INPUTTER` | `FsGaFutureMarginCalculation_Inputter` |  |  |  |
| 22 | `FS.GA.FUTURE.MARGIN.CALCULATION.DATE.TIME` | `FsGaFutureMarginCalculation_DateTime` |  |  |  |
| 23 | `FS.GA.FUTURE.MARGIN.CALCULATION.AUTHORISER` | `FsGaFutureMarginCalculation_Authoriser` | String |  |  |
| 24 | `FS.GA.FUTURE.MARGIN.CALCULATION.CO.CODE` | `FsGaFutureMarginCalculation_CoCode` | String |  |  |
| 25 | `FS.GA.FUTURE.MARGIN.CALCULATION.DEPT.CODE` | `FsGaFutureMarginCalculation_DeptCode` | String |  |  |
| 26 | `FS.GA.FUTURE.MARGIN.CALCULATION.AUDITOR.CODE` | `FsGaFutureMarginCalculation_AuditorCode` | String |  |  |
| 27 | `FS.GA.FUTURE.MARGIN.CALCULATION.AUDIT.DATE.TIME` | `FsGaFutureMarginCalculation_AuditDateTime` | String |  |  |
