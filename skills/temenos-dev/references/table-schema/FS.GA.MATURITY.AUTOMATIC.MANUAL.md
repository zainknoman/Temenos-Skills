# FS.GA.MATURITY.AUTOMATIC.MANUAL — Table Schema

> Source: `INSERTS/I_F.FS.GA.MATURITY.AUTOMATIC.MANUAL` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.FUND.ID` | `FsGaMaturityAutomaticManual_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.GTI.CODE` | `FsGaMaturityAutomaticManual_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 3 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.SERVICE.CODE` | `FsGaMaturityAutomaticManual_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 4 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED10` | `FsGaMaturityAutomaticManual_Reserved10` | TField |  |  |
| 5 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED9` | `FsGaMaturityAutomaticManual_Reserved9` | TField |  |  |
| 6 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED8` | `FsGaMaturityAutomaticManual_Reserved8` | TField |  |  |
| 7 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED7` | `FsGaMaturityAutomaticManual_Reserved7` | TField |  |  |
| 8 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED6` | `FsGaMaturityAutomaticManual_Reserved6` | TField |  |  |
| 9 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED5` | `FsGaMaturityAutomaticManual_Reserved5` | TField |  |  |
| 10 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED4` | `FsGaMaturityAutomaticManual_Reserved4` | TField |  |  |
| 11 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED3` | `FsGaMaturityAutomaticManual_Reserved3` | TField |  |  |
| 12 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED2` | `FsGaMaturityAutomaticManual_Reserved2` | TField |  |  |
| 13 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RESERVED1` | `FsGaMaturityAutomaticManual_Reserved1` | TField |  |  |
| 14 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.RECORD.STATUS` | `FsGaMaturityAutomaticManual_RecordStatus` | String |  |  |
| 15 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.CURR.NO` | `FsGaMaturityAutomaticManual_CurrNo` | String |  |  |
| 16 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.INPUTTER` | `FsGaMaturityAutomaticManual_Inputter` |  |  |  |
| 17 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.DATE.TIME` | `FsGaMaturityAutomaticManual_DateTime` |  |  |  |
| 18 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.AUTHORISER` | `FsGaMaturityAutomaticManual_Authoriser` | String |  |  |
| 19 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.CO.CODE` | `FsGaMaturityAutomaticManual_CoCode` | String |  |  |
| 20 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.DEPT.CODE` | `FsGaMaturityAutomaticManual_DeptCode` | String |  |  |
| 21 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.AUDITOR.CODE` | `FsGaMaturityAutomaticManual_AuditorCode` | String |  |  |
| 22 | `FS.GA.MATURITY.AUTOMATIC.MANUAL.AUDIT.DATE.TIME` | `FsGaMaturityAutomaticManual_AuditDateTime` | String |  |  |
