# FS.GA.ACCOUNTING.DATE.ROLLOVER — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTING.DATE.ROLLOVER` in `FS_Scheduler.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.PARENT.REF.ID` | `FsGaAccountingDateRollover_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.ORA.ROWID` | `FsGaAccountingDateRollover_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.FUND.ID` | `FsGaAccountingDateRollover_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.BOOK.CURRENCY` | `FsGaAccountingDateRollover_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 5 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.ACCOUNTING.DATE` | `FsGaAccountingDateRollover_AccountingDate` | TField |  | Old fund accounting date of the fund ID Multifonds DB Column is DCTA_SAV. |
| 6 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.ACCOUNTING.DATE.NEW` | `FsGaAccountingDateRollover_AccountingDateNew` | TField |  | New fund accounting date of the fund ID Multifonds DB Column is DCTA_NEW. |
| 7 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED10` | `FsGaAccountingDateRollover_Reserved10` | TField |  |  |
| 8 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED9` | `FsGaAccountingDateRollover_Reserved9` | TField |  |  |
| 9 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED8` | `FsGaAccountingDateRollover_Reserved8` | TField |  |  |
| 10 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED7` | `FsGaAccountingDateRollover_Reserved7` | TField |  |  |
| 11 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED6` | `FsGaAccountingDateRollover_Reserved6` | TField |  |  |
| 12 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED5` | `FsGaAccountingDateRollover_Reserved5` | TField |  |  |
| 13 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED4` | `FsGaAccountingDateRollover_Reserved4` | TField |  |  |
| 14 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED3` | `FsGaAccountingDateRollover_Reserved3` | TField |  |  |
| 15 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED2` | `FsGaAccountingDateRollover_Reserved2` | TField |  |  |
| 16 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RESERVED1` | `FsGaAccountingDateRollover_Reserved1` | TField |  |  |
| 17 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.LOCAL.REF` | `FsGaAccountingDateRollover_LocalRef` |  |  |  |
| 18 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.OVERRIDE` | `FsGaAccountingDateRollover_Override` |  |  |  |
| 19 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.RECORD.STATUS` | `FsGaAccountingDateRollover_RecordStatus` | String |  |  |
| 20 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.CURR.NO` | `FsGaAccountingDateRollover_CurrNo` | String |  |  |
| 21 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.INPUTTER` | `FsGaAccountingDateRollover_Inputter` |  |  |  |
| 22 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.DATE.TIME` | `FsGaAccountingDateRollover_DateTime` |  |  |  |
| 23 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.AUTHORISER` | `FsGaAccountingDateRollover_Authoriser` | String |  |  |
| 24 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.CO.CODE` | `FsGaAccountingDateRollover_CoCode` | String |  |  |
| 25 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.DEPT.CODE` | `FsGaAccountingDateRollover_DeptCode` | String |  |  |
| 26 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.AUDITOR.CODE` | `FsGaAccountingDateRollover_AuditorCode` | String |  |  |
| 27 | `FS.GA.ACCOUNTING.DATE.ROLLOVER.AUDIT.DATE.TIME` | `FsGaAccountingDateRollover_AuditDateTime` | String |  |  |
