# FS.GA.CUSTODIAN — Table Schema

> Source: `INSERTS/I_F.FS.GA.CUSTODIAN` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUSTODIAN.CORRESPONDENT` | `FsGaCustodian_Correspondent` | TField |  | Correspondent Multifonds DB Column is NCORRESP. |
| 2 | `CUSTODIAN.FUND.ID` | `FsGaCustodian_Fund` |  |  |  |
| 3 | `CUSTODIAN.CORRESPONDENT.ACCOUNT` | `FsGaCustodian_CorrespondentAccount` | TField |  | Correspondent Account Multifonds DB Column is NCORRESP_ACCOUNT. |
| 4 | `CUSTODIAN.GL.ACOUNT` | `FsGaCustodian_GlAcount` | TField |  | GL Acount Multifonds DB Column is DFLT_ACCOUNT. |
| 5 | `CUSTODIAN.DWH.EXPORT` | `FsGaCustodian_DwhExport` | TField |  | DWH export Multifonds DB Column is DWH_EXPORT. |
| 6 | `CUSTODIAN.LOCAL.CURRENCY` | `FsGaCustodian_Currency` |  |  |  |
| 7 | `CUSTODIAN.ACCOUNT.STATUS` | `FsGaCustodian_AccountStatus` | TField |  | Account Status Multifonds DB Column is ACCOUNT_STATUS. |
| 8 | `CUSTODIAN.DEPOSITARY.STATUS` | `FsGaCustodian_DepositaryStatus` | TField |  | Depositary Status Multifonds DB Column is DEPOSITARY_STATUS. |
| 9 | `CUSTODIAN.RECORD.STATUS` | `FsGaCustodian_RecordStatus` | String |  |  |
| 10 | `CUSTODIAN.CURR.NO` | `FsGaCustodian_CurrNo` | String |  |  |
| 11 | `CUSTODIAN.INPUTTER` | `FsGaCustodian_Inputter` |  |  |  |
| 12 | `CUSTODIAN.DATE.TIME` | `FsGaCustodian_DateTime` |  |  |  |
| 13 | `CUSTODIAN.AUTHORISER` | `FsGaCustodian_Authoriser` | String |  |  |
| 14 | `CUSTODIAN.CO.CODE` | `FsGaCustodian_CoCode` | String |  |  |
| 15 | `CUSTODIAN.DEPT.CODE` | `FsGaCustodian_DeptCode` | String |  |  |
| 16 | `CUSTODIAN.AUDITOR.CODE` | `FsGaCustodian_AuditorCode` | String |  |  |
| 17 | `CUSTODIAN.AUDIT.DATE.TIME` | `FsGaCustodian_AuditDateTime` | String |  |  |
