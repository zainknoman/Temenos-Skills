# FS.GA.CORRESPONDENT.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.ACCOUNTS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORRESPONDENT.ACCOUNTS.CORRESPONDENT.NUMBER` | `FsGaCorrespondentAccounts_CorrespondentNumber` | TField |  | Correspondent Number Multifonds DB Column is NCORRESP. |
| 2 | `CORRESPONDENT.ACCOUNTS.ACCOUNT.NUMBER` | `FsGaCorrespondentAccounts_AccountNumber` | TField |  | Account number Multifonds DB Column is NRUBR. |
| 3 | `CORRESPONDENT.ACCOUNTS.GL.ACCOUNT.SUFFIX` | `FsGaCorrespondentAccounts_SuffixNumber` |  |  |  |
| 4 | `CORRESPONDENT.ACCOUNTS.CORRESPONDENT.ACCOUNT.TYPE` | `FsGaCorrespondentAccounts_CorrespondentAccountType` | TField |  | Correspondent Account type Multifonds DB Column is TYPE_CPT. |
| 5 | `CORRESPONDENT.ACCOUNTS.DWH.EXPORT` | `FsGaCorrespondentAccounts_DwhExport` | TField |  | DWH Export Multifonds DB Column is DWH_EXPORT. |
| 6 | `CORRESPONDENT.ACCOUNTS.GFDB.CC` | `FsGaCorrespondentAccounts_GfdbCcFlag` |  |  |  |
| 7 | `CORRESPONDENT.ACCOUNTS.CHART` | `FsGaCorrespondentAccounts_Chart` | TField |  | Chart Multifonds DB Column is CPDC. |
| 8 | `CORRESPONDENT.ACCOUNTS.RECORD.STATUS` | `FsGaCorrespondentAccounts_RecordStatus` | String |  |  |
| 9 | `CORRESPONDENT.ACCOUNTS.CURR.NO` | `FsGaCorrespondentAccounts_CurrNo` | String |  |  |
| 10 | `CORRESPONDENT.ACCOUNTS.INPUTTER` | `FsGaCorrespondentAccounts_Inputter` |  |  |  |
| 11 | `CORRESPONDENT.ACCOUNTS.DATE.TIME` | `FsGaCorrespondentAccounts_DateTime` |  |  |  |
| 12 | `CORRESPONDENT.ACCOUNTS.AUTHORISER` | `FsGaCorrespondentAccounts_Authoriser` | String |  |  |
| 13 | `CORRESPONDENT.ACCOUNTS.CO.CODE` | `FsGaCorrespondentAccounts_CoCode` | String |  |  |
| 14 | `CORRESPONDENT.ACCOUNTS.DEPT.CODE` | `FsGaCorrespondentAccounts_DeptCode` | String |  |  |
| 15 | `CORRESPONDENT.ACCOUNTS.AUDITOR.CODE` | `FsGaCorrespondentAccounts_AuditorCode` | String |  |  |
| 16 | `CORRESPONDENT.ACCOUNTS.AUDIT.DATE.TIME` | `FsGaCorrespondentAccounts_AuditDateTime` | String |  |  |
