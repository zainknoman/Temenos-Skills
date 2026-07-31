# FS.GA.AUTO.MATURITY — Table Schema

> Source: `INSERTS/I_F.FS.GA.AUTO.MATURITY` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.AUTO.MATURITY.FUND.ID` | `FsGaAutoMaturity_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.AUTO.MATURITY.SERVICE.CODE` | `FsGaAutoMaturity_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 3 | `FS.GA.AUTO.MATURITY.AUTO.OR.MANUAL` | `FsGaAutoMaturity_AutoOrManual` | TField |  | Auto or Manual Multifonds DB Column is FCPT_VAL. |
| 4 | `FS.GA.AUTO.MATURITY.RESERVED10` | `FsGaAutoMaturity_Reserved10` | TField |  |  |
| 5 | `FS.GA.AUTO.MATURITY.RESERVED9` | `FsGaAutoMaturity_Reserved9` | TField |  |  |
| 6 | `FS.GA.AUTO.MATURITY.RESERVED8` | `FsGaAutoMaturity_Reserved8` | TField |  |  |
| 7 | `FS.GA.AUTO.MATURITY.RESERVED7` | `FsGaAutoMaturity_Reserved7` | TField |  |  |
| 8 | `FS.GA.AUTO.MATURITY.RESERVED6` | `FsGaAutoMaturity_Reserved6` | TField |  |  |
| 9 | `FS.GA.AUTO.MATURITY.RESERVED5` | `FsGaAutoMaturity_Reserved5` | TField |  |  |
| 10 | `FS.GA.AUTO.MATURITY.RESERVED4` | `FsGaAutoMaturity_Reserved4` | TField |  |  |
| 11 | `FS.GA.AUTO.MATURITY.RESERVED3` | `FsGaAutoMaturity_Reserved3` | TField |  |  |
| 12 | `FS.GA.AUTO.MATURITY.RESERVED2` | `FsGaAutoMaturity_Reserved2` | TField |  |  |
| 13 | `FS.GA.AUTO.MATURITY.RESERVED1` | `FsGaAutoMaturity_Reserved1` | TField |  |  |
| 14 | `FS.GA.AUTO.MATURITY.RECORD.STATUS` | `FsGaAutoMaturity_RecordStatus` | String |  |  |
| 15 | `FS.GA.AUTO.MATURITY.CURR.NO` | `FsGaAutoMaturity_CurrNo` | String |  |  |
| 16 | `FS.GA.AUTO.MATURITY.INPUTTER` | `FsGaAutoMaturity_Inputter` |  |  |  |
| 17 | `FS.GA.AUTO.MATURITY.DATE.TIME` | `FsGaAutoMaturity_DateTime` |  |  |  |
| 18 | `FS.GA.AUTO.MATURITY.AUTHORISER` | `FsGaAutoMaturity_Authoriser` | String |  |  |
| 19 | `FS.GA.AUTO.MATURITY.CO.CODE` | `FsGaAutoMaturity_CoCode` | String |  |  |
| 20 | `FS.GA.AUTO.MATURITY.DEPT.CODE` | `FsGaAutoMaturity_DeptCode` | String |  |  |
| 21 | `FS.GA.AUTO.MATURITY.AUDITOR.CODE` | `FsGaAutoMaturity_AuditorCode` | String |  |  |
| 22 | `FS.GA.AUTO.MATURITY.AUDIT.DATE.TIME` | `FsGaAutoMaturity_AuditDateTime` | String |  |  |
