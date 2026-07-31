# FS.GA.ACCRUALMETHOD.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCRUALMETHOD.EXCEPTION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCRUALMETHOD.EXCEPTION.FUND.ID` | `FsGaAccrualmethodException_Fund` |  |  |  |
| 2 | `ACCRUALMETHOD.EXCEPTION.SECURITY.TYPE` | `FsGaAccrualmethodException_SecurityType` | TField |  | Security Type Multifonds DB Column is CGTI. |
| 3 | `ACCRUALMETHOD.EXCEPTION.ACCRUAL.METHOD` | `FsGaAccrualmethodException_AccrualMethod` | TField |  | Accrual Method Multifonds DB Column is ACCRUAL_METHOD. |
| 4 | `ACCRUALMETHOD.EXCEPTION.RECORD.STATUS` | `FsGaAccrualmethodException_RecordStatus` | String |  |  |
| 5 | `ACCRUALMETHOD.EXCEPTION.CURR.NO` | `FsGaAccrualmethodException_CurrNo` | String |  |  |
| 6 | `ACCRUALMETHOD.EXCEPTION.INPUTTER` | `FsGaAccrualmethodException_Inputter` |  |  |  |
| 7 | `ACCRUALMETHOD.EXCEPTION.DATE.TIME` | `FsGaAccrualmethodException_DateTime` |  |  |  |
| 8 | `ACCRUALMETHOD.EXCEPTION.AUTHORISER` | `FsGaAccrualmethodException_Authoriser` | String |  |  |
| 9 | `ACCRUALMETHOD.EXCEPTION.CO.CODE` | `FsGaAccrualmethodException_CoCode` | String |  |  |
| 10 | `ACCRUALMETHOD.EXCEPTION.DEPT.CODE` | `FsGaAccrualmethodException_DeptCode` | String |  |  |
| 11 | `ACCRUALMETHOD.EXCEPTION.AUDITOR.CODE` | `FsGaAccrualmethodException_AuditorCode` | String |  |  |
| 12 | `ACCRUALMETHOD.EXCEPTION.AUDIT.DATE.TIME` | `FsGaAccrualmethodException_AuditDateTime` | String |  |  |
