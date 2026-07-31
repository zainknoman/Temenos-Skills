# FS.GA.NAV.ACCOUNTING — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.ACCOUNTING` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.ACCOUNTING.PARENT.REF.ID` | `FsGaNavAccounting_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.ACCOUNTING.ORA.ROWID` | `FsGaNavAccounting_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.ACCOUNTING.NAV.GROUP.CODE` | `FsGaNavAccounting_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 4 | `FS.GA.NAV.ACCOUNTING.PROCESS.ID` | `FsGaNavAccounting_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 5 | `FS.GA.NAV.ACCOUNTING.FUND.ID` | `FsGaNavAccounting_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.NAV.ACCOUNTING.VALUATION.TYPE` | `FsGaNavAccounting_ValuationType` | TField |  | Valuation type of the Fund Multifonds DB Column is TYP_TRT. |
| 7 | `FS.GA.NAV.ACCOUNTING.PROCESSING.DATE` | `FsGaNavAccounting_ProcessingDate` | TField |  | Processing date of the simulated fund Multifonds DB Column is DATE_TRT. |
| 8 | `FS.GA.NAV.ACCOUNTING.RESERVED10` | `FsGaNavAccounting_Reserved10` | TField |  |  |
| 9 | `FS.GA.NAV.ACCOUNTING.RESERVED9` | `FsGaNavAccounting_Reserved9` | TField |  |  |
| 10 | `FS.GA.NAV.ACCOUNTING.RESERVED8` | `FsGaNavAccounting_Reserved8` | TField |  |  |
| 11 | `FS.GA.NAV.ACCOUNTING.RESERVED7` | `FsGaNavAccounting_Reserved7` | TField |  |  |
| 12 | `FS.GA.NAV.ACCOUNTING.RESERVED6` | `FsGaNavAccounting_Reserved6` | TField |  |  |
| 13 | `FS.GA.NAV.ACCOUNTING.RESERVED5` | `FsGaNavAccounting_Reserved5` | TField |  |  |
| 14 | `FS.GA.NAV.ACCOUNTING.RESERVED4` | `FsGaNavAccounting_Reserved4` | TField |  |  |
| 15 | `FS.GA.NAV.ACCOUNTING.RESERVED3` | `FsGaNavAccounting_Reserved3` | TField |  |  |
| 16 | `FS.GA.NAV.ACCOUNTING.RESERVED2` | `FsGaNavAccounting_Reserved2` | TField |  |  |
| 17 | `FS.GA.NAV.ACCOUNTING.RESERVED1` | `FsGaNavAccounting_Reserved1` | TField |  |  |
| 18 | `FS.GA.NAV.ACCOUNTING.LOCAL.REF` | `FsGaNavAccounting_LocalRef` |  |  |  |
| 19 | `FS.GA.NAV.ACCOUNTING.OVERRIDE` | `FsGaNavAccounting_Override` |  |  |  |
| 20 | `FS.GA.NAV.ACCOUNTING.RECORD.STATUS` | `FsGaNavAccounting_RecordStatus` | String |  |  |
| 21 | `FS.GA.NAV.ACCOUNTING.CURR.NO` | `FsGaNavAccounting_CurrNo` | String |  |  |
| 22 | `FS.GA.NAV.ACCOUNTING.INPUTTER` | `FsGaNavAccounting_Inputter` |  |  |  |
| 23 | `FS.GA.NAV.ACCOUNTING.DATE.TIME` | `FsGaNavAccounting_DateTime` |  |  |  |
| 24 | `FS.GA.NAV.ACCOUNTING.AUTHORISER` | `FsGaNavAccounting_Authoriser` | String |  |  |
| 25 | `FS.GA.NAV.ACCOUNTING.CO.CODE` | `FsGaNavAccounting_CoCode` | String |  |  |
| 26 | `FS.GA.NAV.ACCOUNTING.DEPT.CODE` | `FsGaNavAccounting_DeptCode` | String |  |  |
| 27 | `FS.GA.NAV.ACCOUNTING.AUDITOR.CODE` | `FsGaNavAccounting_AuditorCode` | String |  |  |
| 28 | `FS.GA.NAV.ACCOUNTING.AUDIT.DATE.TIME` | `FsGaNavAccounting_AuditDateTime` | String |  |  |
