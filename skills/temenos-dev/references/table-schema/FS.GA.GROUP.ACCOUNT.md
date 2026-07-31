# FS.GA.GROUP.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GA.GROUP.ACCOUNT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.GROUP.ACCOUNT.GROUP.ACCOUNT.NUMBER` | `FsGaGroupAccount_GroupAccountNumber` |  |  |  |
| 2 | `FS.GA.GROUP.ACCOUNT.CHART.OF.ACCOUNTS.CODE` | `FsGaGroupAccount_ChartOfAccountsNumber` |  |  |  |
| 3 | `FS.GA.GROUP.ACCOUNT.GL.ACCOUNT` | `FsGaGroupAccount_CashAccountNumber` |  |  |  |
| 4 | `FS.GA.GROUP.ACCOUNT.SUFFIX.NUMBER.FROM` | `FsGaGroupAccount_SuffixNumberFrom` |  |  |  |
| 5 | `FS.GA.GROUP.ACCOUNT.SUFFIX.NUMBER.TO` | `FsGaGroupAccount_SuffixNumberTo` |  |  |  |
| 6 | `FS.GA.GROUP.ACCOUNT.TAX.PRICING.FACTOR.CODE` | `FsGaGroupAccount_TaxCalculationCode` |  |  |  |
| 7 | `FS.GA.GROUP.ACCOUNT.SIGN` | `FsGaGroupAccount_Sign` |  |  |  |
| 8 | `FS.GA.GROUP.ACCOUNT.TAX.CODE.2` | `FsGaGroupAccount_TaxCode2` |  |  |  |
| 9 | `FS.GA.GROUP.ACCOUNT.FLAG.CGT.OFFSET` | `FsGaGroupAccount_FlagCgtOffset` |  |  |  |
| 10 | `FS.GA.GROUP.ACCOUNT.RESERVED10` | `FsGaGroupAccount_Reserved10` |  |  |  |
| 11 | `FS.GA.GROUP.ACCOUNT.RESERVED9` | `FsGaGroupAccount_Reserved9` |  |  |  |
| 12 | `FS.GA.GROUP.ACCOUNT.RESERVED8` | `FsGaGroupAccount_Reserved8` |  |  |  |
| 13 | `FS.GA.GROUP.ACCOUNT.RESERVED7` | `FsGaGroupAccount_Reserved7` |  |  |  |
| 14 | `FS.GA.GROUP.ACCOUNT.RESERVED6` | `FsGaGroupAccount_Reserved6` |  |  |  |
| 15 | `FS.GA.GROUP.ACCOUNT.RESERVED5` | `FsGaGroupAccount_Reserved5` |  |  |  |
| 16 | `FS.GA.GROUP.ACCOUNT.RESERVED4` | `FsGaGroupAccount_Reserved4` |  |  |  |
| 17 | `FS.GA.GROUP.ACCOUNT.RESERVED3` | `FsGaGroupAccount_Reserved3` |  |  |  |
| 18 | `FS.GA.GROUP.ACCOUNT.RESERVED2` | `FsGaGroupAccount_Reserved2` |  |  |  |
| 19 | `FS.GA.GROUP.ACCOUNT.RESERVED1` | `FsGaGroupAccount_Reserved1` |  |  |  |
| 20 | `FS.GA.GROUP.ACCOUNT.RECORD.STATUS` | `FsGaGroupAccount_RecordStatus` |  |  |  |
| 21 | `FS.GA.GROUP.ACCOUNT.CURR.NO` | `FsGaGroupAccount_CurrNo` |  |  |  |
| 22 | `FS.GA.GROUP.ACCOUNT.INPUTTER` | `FsGaGroupAccount_Inputter` |  |  |  |
| 23 | `FS.GA.GROUP.ACCOUNT.DATE.TIME` | `FsGaGroupAccount_DateTime` |  |  |  |
| 24 | `FS.GA.GROUP.ACCOUNT.AUTHORISER` | `FsGaGroupAccount_Authoriser` |  |  |  |
| 25 | `FS.GA.GROUP.ACCOUNT.CO.CODE` | `FsGaGroupAccount_CoCode` |  |  |  |
| 26 | `FS.GA.GROUP.ACCOUNT.DEPT.CODE` | `FsGaGroupAccount_DeptCode` |  |  |  |
| 27 | `FS.GA.GROUP.ACCOUNT.AUDITOR.CODE` | `FsGaGroupAccount_AuditorCode` |  |  |  |
| 28 | `FS.GA.GROUP.ACCOUNT.AUDIT.DATE.TIME` | `FsGaGroupAccount_AuditDateTime` |  |  |  |
