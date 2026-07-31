# FS.GA.MATURITY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.MATURITY.CODE` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MATURITY.CODE.MATURITY.CODE` | `FsGaMaturityCode_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 2 | `FS.GA.MATURITY.CODE.PERIOD.CODE.DENOMINATOR` | `FsGaMaturityCode_PeriodCodeDenominator` | TField |  | Enter the number corresponding to the denominator of the fraction of the maturity relative to one Year (If maturity code >= one year, enter 1). Multifonds DB Column is NBR_1. |
| 3 | `FS.GA.MATURITY.CODE.PERIOD.CODE.NUMERATOR` | `FsGaMaturityCode_PeriodCodeNumerator` | TField |  | Enter the number corresponding to the numerator of the fraction of the maturity relative to one year (leave blank if 1). Multifonds DB Column is NBR_2. |
| 4 | `FS.GA.MATURITY.CODE.DURATION.TYPE` | `FsGaMaturityCode_DurationType` | TField |  | Specify the duration type with regard to yield curve parameter like day, month or year. Multifonds DB Column is TAUX_DUR. |
| 5 | `FS.GA.MATURITY.CODE.NUMBER.3` | `FsGaMaturityCode_Number3` | TField |  | Number 3 Multifonds DB Column is NBR_3. |
| 6 | `FS.GA.MATURITY.CODE.RESERVED10` | `FsGaMaturityCode_Reserved10` | TField |  |  |
| 7 | `FS.GA.MATURITY.CODE.RESERVED9` | `FsGaMaturityCode_Reserved9` | TField |  |  |
| 8 | `FS.GA.MATURITY.CODE.RESERVED8` | `FsGaMaturityCode_Reserved8` | TField |  |  |
| 9 | `FS.GA.MATURITY.CODE.RESERVED7` | `FsGaMaturityCode_Reserved7` | TField |  |  |
| 10 | `FS.GA.MATURITY.CODE.RESERVED6` | `FsGaMaturityCode_Reserved6` | TField |  |  |
| 11 | `FS.GA.MATURITY.CODE.RESERVED5` | `FsGaMaturityCode_Reserved5` | TField |  |  |
| 12 | `FS.GA.MATURITY.CODE.RESERVED4` | `FsGaMaturityCode_Reserved4` | TField |  |  |
| 13 | `FS.GA.MATURITY.CODE.RESERVED3` | `FsGaMaturityCode_Reserved3` | TField |  |  |
| 14 | `FS.GA.MATURITY.CODE.RESERVED2` | `FsGaMaturityCode_Reserved2` | TField |  |  |
| 15 | `FS.GA.MATURITY.CODE.RESERVED1` | `FsGaMaturityCode_Reserved1` | TField |  |  |
| 16 | `FS.GA.MATURITY.CODE.RECORD.STATUS` | `FsGaMaturityCode_RecordStatus` | String |  |  |
| 17 | `FS.GA.MATURITY.CODE.CURR.NO` | `FsGaMaturityCode_CurrNo` | String |  |  |
| 18 | `FS.GA.MATURITY.CODE.INPUTTER` | `FsGaMaturityCode_Inputter` |  |  |  |
| 19 | `FS.GA.MATURITY.CODE.DATE.TIME` | `FsGaMaturityCode_DateTime` |  |  |  |
| 20 | `FS.GA.MATURITY.CODE.AUTHORISER` | `FsGaMaturityCode_Authoriser` | String |  |  |
| 21 | `FS.GA.MATURITY.CODE.CO.CODE` | `FsGaMaturityCode_CoCode` | String |  |  |
| 22 | `FS.GA.MATURITY.CODE.DEPT.CODE` | `FsGaMaturityCode_DeptCode` | String |  |  |
| 23 | `FS.GA.MATURITY.CODE.AUDITOR.CODE` | `FsGaMaturityCode_AuditorCode` | String |  |  |
| 24 | `FS.GA.MATURITY.CODE.AUDIT.DATE.TIME` | `FsGaMaturityCode_AuditDateTime` | String |  |  |
