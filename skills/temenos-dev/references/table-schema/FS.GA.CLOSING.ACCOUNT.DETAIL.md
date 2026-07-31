# FS.GA.CLOSING.ACCOUNT.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.CLOSING.ACCOUNT.DETAIL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CLOSING.ACCOUNT.DETAIL.GL.ACCOUNT` | `FsGaClosingAccountDetail_GlAccount` |  |  |  |
| 2 | `FS.GA.CLOSING.ACCOUNT.DETAIL.FREQUENCY.CODE` | `FsGaClosingAccountDetail_FrequencyCode` |  |  |  |
| 3 | `FS.GA.CLOSING.ACCOUNT.DETAIL.DEBIT.ACCOUNT` | `FsGaClosingAccountDetail_DebitAccount` |  |  |  |
| 4 | `FS.GA.CLOSING.ACCOUNT.DETAIL.CREDIT.ACCOUNT` | `FsGaClosingAccountDetail_CreditAccount` |  |  |  |
| 5 | `FS.GA.CLOSING.ACCOUNT.DETAIL.CHART.OF.ACCOUNTS.CODE` | `FsGaClosingAccountDetail_ChartOfAccountsCode` |  |  |  |
| 6 | `FS.GA.CLOSING.ACCOUNT.DETAIL.EQUALISATION.ADJ.CLOSING.ACC` | `FsGaClosingAccountDetail_EqualisationAdjClosingAcc` |  |  |  |
| 7 | `FS.GA.CLOSING.ACCOUNT.DETAIL.AGS.APPLICABLE` | `FsGaClosingAccountDetail_AgsApplicable` |  |  |  |
| 8 | `FS.GA.CLOSING.ACCOUNT.DETAIL.ZERO.ACC.FLAG.GERMAN.EQUALIZ` | `FsGaClosingAccountDetail_ZeroAccFlagGermanEqualiz` |  |  |  |
| 9 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED10` | `FsGaClosingAccountDetail_Reserved10` |  |  |  |
| 10 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED9` | `FsGaClosingAccountDetail_Reserved9` |  |  |  |
| 11 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED8` | `FsGaClosingAccountDetail_Reserved8` |  |  |  |
| 12 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED7` | `FsGaClosingAccountDetail_Reserved7` |  |  |  |
| 13 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED6` | `FsGaClosingAccountDetail_Reserved6` |  |  |  |
| 14 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED5` | `FsGaClosingAccountDetail_Reserved5` |  |  |  |
| 15 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED4` | `FsGaClosingAccountDetail_Reserved4` |  |  |  |
| 16 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED3` | `FsGaClosingAccountDetail_Reserved3` |  |  |  |
| 17 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED2` | `FsGaClosingAccountDetail_Reserved2` |  |  |  |
| 18 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RESERVED1` | `FsGaClosingAccountDetail_Reserved1` |  |  |  |
| 19 | `FS.GA.CLOSING.ACCOUNT.DETAIL.RECORD.STATUS` | `FsGaClosingAccountDetail_RecordStatus` |  |  |  |
| 20 | `FS.GA.CLOSING.ACCOUNT.DETAIL.CURR.NO` | `FsGaClosingAccountDetail_CurrNo` |  |  |  |
| 21 | `FS.GA.CLOSING.ACCOUNT.DETAIL.INPUTTER` | `FsGaClosingAccountDetail_Inputter` |  |  |  |
| 22 | `FS.GA.CLOSING.ACCOUNT.DETAIL.DATE.TIME` | `FsGaClosingAccountDetail_DateTime` |  |  |  |
| 23 | `FS.GA.CLOSING.ACCOUNT.DETAIL.AUTHORISER` | `FsGaClosingAccountDetail_Authoriser` |  |  |  |
| 24 | `FS.GA.CLOSING.ACCOUNT.DETAIL.CO.CODE` | `FsGaClosingAccountDetail_CoCode` |  |  |  |
| 25 | `FS.GA.CLOSING.ACCOUNT.DETAIL.DEPT.CODE` | `FsGaClosingAccountDetail_DeptCode` |  |  |  |
| 26 | `FS.GA.CLOSING.ACCOUNT.DETAIL.AUDITOR.CODE` | `FsGaClosingAccountDetail_AuditorCode` |  |  |  |
| 27 | `FS.GA.CLOSING.ACCOUNT.DETAIL.AUDIT.DATE.TIME` | `FsGaClosingAccountDetail_AuditDateTime` |  |  |  |
