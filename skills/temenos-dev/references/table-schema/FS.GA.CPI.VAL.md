# FS.GA.CPI.VAL — Table Schema

> Source: `INSERTS/I_F.FS.GA.CPI.VAL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CPI.VAL.INTERNAL.SECURITY.ID` | `FsGaCpiVal_SecurityId` |  |  |  |
| 2 | `CPI.VAL.PERIOD.DATE` | `FsGaCpiVal_PeriodDate` | TField |  | Period Date Multifonds DB Column is DPERIOD. |
| 3 | `CPI.VAL.CPI.VALUE` | `FsGaCpiVal_CpiValue` | TField |  | CPI value Multifonds DB Column is CPI_VALUE. |
| 4 | `CPI.VAL.FLG.SEL` | `FsGaCpiVal_FlgSel` | TField |  | FLG SEL Multifonds DB Column is FLG_SEL. |
| 5 | `CPI.VAL.RECORD.STATUS` | `FsGaCpiVal_RecordStatus` | String |  |  |
| 6 | `CPI.VAL.CURR.NO` | `FsGaCpiVal_CurrNo` | String |  |  |
| 7 | `CPI.VAL.INPUTTER` | `FsGaCpiVal_Inputter` |  |  |  |
| 8 | `CPI.VAL.DATE.TIME` | `FsGaCpiVal_DateTime` |  |  |  |
| 9 | `CPI.VAL.AUTHORISER` | `FsGaCpiVal_Authoriser` | String |  |  |
| 10 | `CPI.VAL.CO.CODE` | `FsGaCpiVal_CoCode` | String |  |  |
| 11 | `CPI.VAL.DEPT.CODE` | `FsGaCpiVal_DeptCode` | String |  |  |
| 12 | `CPI.VAL.AUDITOR.CODE` | `FsGaCpiVal_AuditorCode` | String |  |  |
| 13 | `CPI.VAL.AUDIT.DATE.TIME` | `FsGaCpiVal_AuditDateTime` | String |  |  |
