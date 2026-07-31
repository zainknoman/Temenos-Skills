# FS.GA.DAY.COUNT.CONVENTION.CALC — Table Schema

> Source: `INSERTS/I_F.FS.GA.DAY.COUNT.CONVENTION.CALC` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DAY.COUNT.CONVENTION.CALC.PARENT.REF.ID` | `FsGaDayCountConventionCalc_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DAY.COUNT.CONVENTION.CALC.ORA.ROWID` | `FsGaDayCountConventionCalc_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DAY.COUNT.CONVENTION.CALC.DAY.COUNT.CONVENTION` | `FsGaDayCountConventionCalc_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 4 | `FS.GA.DAY.COUNT.CONVENTION.CALC.NUMERATOR.LOGIC` | `FsGaDayCountConventionCalc_NumeratorLogic` | TField |  | The numerator representing the calculation logic Multifonds DB Column is NBJMOIS. |
| 5 | `FS.GA.DAY.COUNT.CONVENTION.CALC.DENOMINATOR.LOGIC` | `FsGaDayCountConventionCalc_DenominatorLogic` | TField |  | The denominator representing the calculation logic Multifonds DB Column is NBJAN. |
| 6 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED10` | `FsGaDayCountConventionCalc_Reserved10` | TField |  |  |
| 7 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED9` | `FsGaDayCountConventionCalc_Reserved9` | TField |  |  |
| 8 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED8` | `FsGaDayCountConventionCalc_Reserved8` | TField |  |  |
| 9 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED7` | `FsGaDayCountConventionCalc_Reserved7` | TField |  |  |
| 10 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED6` | `FsGaDayCountConventionCalc_Reserved6` | TField |  |  |
| 11 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED5` | `FsGaDayCountConventionCalc_Reserved5` | TField |  |  |
| 12 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED4` | `FsGaDayCountConventionCalc_Reserved4` | TField |  |  |
| 13 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED3` | `FsGaDayCountConventionCalc_Reserved3` | TField |  |  |
| 14 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED2` | `FsGaDayCountConventionCalc_Reserved2` | TField |  |  |
| 15 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RESERVED1` | `FsGaDayCountConventionCalc_Reserved1` | TField |  |  |
| 16 | `FS.GA.DAY.COUNT.CONVENTION.CALC.LOCAL.REF` | `FsGaDayCountConventionCalc_LocalRef` |  |  |  |
| 17 | `FS.GA.DAY.COUNT.CONVENTION.CALC.OVERRIDE` | `FsGaDayCountConventionCalc_Override` |  |  |  |
| 18 | `FS.GA.DAY.COUNT.CONVENTION.CALC.RECORD.STATUS` | `FsGaDayCountConventionCalc_RecordStatus` | String |  |  |
| 19 | `FS.GA.DAY.COUNT.CONVENTION.CALC.CURR.NO` | `FsGaDayCountConventionCalc_CurrNo` | String |  |  |
| 20 | `FS.GA.DAY.COUNT.CONVENTION.CALC.INPUTTER` | `FsGaDayCountConventionCalc_Inputter` |  |  |  |
| 21 | `FS.GA.DAY.COUNT.CONVENTION.CALC.DATE.TIME` | `FsGaDayCountConventionCalc_DateTime` |  |  |  |
| 22 | `FS.GA.DAY.COUNT.CONVENTION.CALC.AUTHORISER` | `FsGaDayCountConventionCalc_Authoriser` | String |  |  |
| 23 | `FS.GA.DAY.COUNT.CONVENTION.CALC.CO.CODE` | `FsGaDayCountConventionCalc_CoCode` | String |  |  |
| 24 | `FS.GA.DAY.COUNT.CONVENTION.CALC.DEPT.CODE` | `FsGaDayCountConventionCalc_DeptCode` | String |  |  |
| 25 | `FS.GA.DAY.COUNT.CONVENTION.CALC.AUDITOR.CODE` | `FsGaDayCountConventionCalc_AuditorCode` | String |  |  |
| 26 | `FS.GA.DAY.COUNT.CONVENTION.CALC.AUDIT.DATE.TIME` | `FsGaDayCountConventionCalc_AuditDateTime` | String |  |  |
