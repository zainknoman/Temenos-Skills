# FS.GA.CORRESPONDENT.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.ACCOUNT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.ACCOUNT.PARENT.REF.ID` | `FsGaCorrespondentAccount_ParentRefId` |  |  |  |
| 2 | `FS.GA.CORRESPONDENT.ACCOUNT.ORA.ROWID` | `FsGaCorrespondentAccount_OraRowid` |  |  |  |
| 3 | `FS.GA.CORRESPONDENT.ACCOUNT.CORRESPONDENT` | `FsGaCorrespondentAccount_Correspondent` |  |  |  |
| 4 | `FS.GA.CORRESPONDENT.ACCOUNT.GL.ACCOUNT` | `FsGaCorrespondentAccount_GlAccount` |  |  |  |
| 5 | `FS.GA.CORRESPONDENT.ACCOUNT.GL.ACCOUNT.SUFFIX` | `FsGaCorrespondentAccount_GlAccountSuffix` |  |  |  |
| 6 | `FS.GA.CORRESPONDENT.ACCOUNT.CPT.TYPE` | `FsGaCorrespondentAccount_CptType` |  |  |  |
| 7 | `FS.GA.CORRESPONDENT.ACCOUNT.GFDB.CC` | `FsGaCorrespondentAccount_GfdbCc` |  |  |  |
| 8 | `FS.GA.CORRESPONDENT.ACCOUNT.CHART.OF.ACCOUNTS.CODE` | `FsGaCorrespondentAccount_ChartOfAccountsCode` |  |  |  |
| 9 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED10` | `FsGaCorrespondentAccount_Reserved10` |  |  |  |
| 10 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED9` | `FsGaCorrespondentAccount_Reserved9` |  |  |  |
| 11 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED8` | `FsGaCorrespondentAccount_Reserved8` |  |  |  |
| 12 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED7` | `FsGaCorrespondentAccount_Reserved7` |  |  |  |
| 13 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED6` | `FsGaCorrespondentAccount_Reserved6` |  |  |  |
| 14 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED5` | `FsGaCorrespondentAccount_Reserved5` |  |  |  |
| 15 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED4` | `FsGaCorrespondentAccount_Reserved4` |  |  |  |
| 16 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED3` | `FsGaCorrespondentAccount_Reserved3` |  |  |  |
| 17 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED2` | `FsGaCorrespondentAccount_Reserved2` |  |  |  |
| 18 | `FS.GA.CORRESPONDENT.ACCOUNT.RESERVED1` | `FsGaCorrespondentAccount_Reserved1` |  |  |  |
| 19 | `FS.GA.CORRESPONDENT.ACCOUNT.LOCAL.REF` | `FsGaCorrespondentAccount_LocalRef` |  |  |  |
| 20 | `FS.GA.CORRESPONDENT.ACCOUNT.OVERRIDE` | `FsGaCorrespondentAccount_Override` |  |  |  |
| 21 | `FS.GA.CORRESPONDENT.ACCOUNT.RECORD.STATUS` | `FsGaCorrespondentAccount_RecordStatus` |  |  |  |
| 22 | `FS.GA.CORRESPONDENT.ACCOUNT.CURR.NO` | `FsGaCorrespondentAccount_CurrNo` |  |  |  |
| 23 | `FS.GA.CORRESPONDENT.ACCOUNT.INPUTTER` | `FsGaCorrespondentAccount_Inputter` |  |  |  |
| 24 | `FS.GA.CORRESPONDENT.ACCOUNT.DATE.TIME` | `FsGaCorrespondentAccount_DateTime` |  |  |  |
| 25 | `FS.GA.CORRESPONDENT.ACCOUNT.AUTHORISER` | `FsGaCorrespondentAccount_Authoriser` |  |  |  |
| 26 | `FS.GA.CORRESPONDENT.ACCOUNT.CO.CODE` | `FsGaCorrespondentAccount_CoCode` |  |  |  |
| 27 | `FS.GA.CORRESPONDENT.ACCOUNT.DEPT.CODE` | `FsGaCorrespondentAccount_DeptCode` |  |  |  |
| 28 | `FS.GA.CORRESPONDENT.ACCOUNT.AUDITOR.CODE` | `FsGaCorrespondentAccount_AuditorCode` |  |  |  |
| 29 | `FS.GA.CORRESPONDENT.ACCOUNT.AUDIT.DATE.TIME` | `FsGaCorrespondentAccount_AuditDateTime` |  |  |  |
