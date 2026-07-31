# FS.GA.CLOSINGACCOUNT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.CLOSINGACCOUNT.PARAMETER` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLOSINGACCOUNT.PARAMETER.ACCOUNT` | `FsGaClosingaccountParameter_Account` | TField |  | Account Multifonds DB Column is NRUBR. |
| 2 | `CLOSINGACCOUNT.PARAMETER.FREQUENCY.CODE` | `FsGaClosingaccountParameter_FrequencyCode` | TField |  | Frequency Code Multifonds DB Column is CFREQ. |
| 3 | `CLOSINGACCOUNT.PARAMETER.ACCOUNT.DEBIT` | `FsGaClosingaccountParameter_AccountDebit` | TField |  | Account Debit Multifonds DB Column is NRUBR_DB. |
| 4 | `CLOSINGACCOUNT.PARAMETER.ACCOUNT.CREDIT` | `FsGaClosingaccountParameter_AccountCredit` | TField |  | Account Credit Multifonds DB Column is NRUBR_CR. |
| 5 | `CLOSINGACCOUNT.PARAMETER.CHART` | `FsGaClosingaccountParameter_Chart` | TField |  | Chart Multifonds DB Column is CPDC. |
| 6 | `CLOSINGACCOUNT.PARAMETER.EQUALISATION.FLAG` | `FsGaClosingaccountParameter_EqualisationFlag` | TField |  | Equalisation Flag Multifonds DB Column is FLG_EGA. |
| 7 | `CLOSINGACCOUNT.PARAMETER.AGS.FLAG` | `FsGaClosingaccountParameter_AgsFlag` | TField |  | AGS Flag Multifonds DB Column is FLG_AGS. |
| 8 | `CLOSINGACCOUNT.PARAMETER.ZERO.ACCOUNTS.FLAG` | `FsGaClosingaccountParameter_ZeroAccountsFlag` | TField |  | Zero Accounts Flag Multifonds DB Column is FLG_ZERO_ACC. |
| 9 | `CLOSINGACCOUNT.PARAMETER.RECORD.STATUS` | `FsGaClosingaccountParameter_RecordStatus` | String |  |  |
| 10 | `CLOSINGACCOUNT.PARAMETER.CURR.NO` | `FsGaClosingaccountParameter_CurrNo` | String |  |  |
| 11 | `CLOSINGACCOUNT.PARAMETER.INPUTTER` | `FsGaClosingaccountParameter_Inputter` |  |  |  |
| 12 | `CLOSINGACCOUNT.PARAMETER.DATE.TIME` | `FsGaClosingaccountParameter_DateTime` |  |  |  |
| 13 | `CLOSINGACCOUNT.PARAMETER.AUTHORISER` | `FsGaClosingaccountParameter_Authoriser` | String |  |  |
| 14 | `CLOSINGACCOUNT.PARAMETER.CO.CODE` | `FsGaClosingaccountParameter_CoCode` | String |  |  |
| 15 | `CLOSINGACCOUNT.PARAMETER.DEPT.CODE` | `FsGaClosingaccountParameter_DeptCode` | String |  |  |
| 16 | `CLOSINGACCOUNT.PARAMETER.AUDITOR.CODE` | `FsGaClosingaccountParameter_AuditorCode` | String |  |  |
| 17 | `CLOSINGACCOUNT.PARAMETER.AUDIT.DATE.TIME` | `FsGaClosingaccountParameter_AuditDateTime` | String |  |  |
