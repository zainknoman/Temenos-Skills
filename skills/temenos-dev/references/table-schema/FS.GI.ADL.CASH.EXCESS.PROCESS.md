# FS.GI.ADL.CASH.EXCESS.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.ADL.CASH.EXCESS.PROCESS` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.ADL.CASH.EXCESS.PROCESS.PARENT.REF.ID` | `FsGiAdlCashExcessProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.ADL.CASH.EXCESS.PROCESS.ORA.ROWID` | `FsGiAdlCashExcessProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.ADL.CASH.EXCESS.PROCESS.EXCHANGE.GROUP` | `FsGiAdlCashExcessProcess_ExchangeGroup` | TField |  | Fund exchange group. Multifonds DB Column is P_CGROUPE_COURS. |
| 4 | `FS.GI.ADL.CASH.EXCESS.PROCESS.FUND.ID` | `FsGiAdlCashExcessProcess_FundId` | TField |  | Master Fund internal ID. Multifonds DB Column is P_MULTIFONDS_ID. |
| 5 | `FS.GI.ADL.CASH.EXCESS.PROCESS.CALC.DATE` | `FsGiAdlCashExcessProcess_CalcDate` | TField |  | ADL calculation procesing date. Multifonds DB Column is P_DATE_CAL. |
| 6 | `FS.GI.ADL.CASH.EXCESS.PROCESS.ADL.PROCESS` | `FsGiAdlCashExcessProcess_AdlProcess` | TField |  | ADL process used for processing. Multifonds DB Column is P_ADL_PROCESS. |
| 7 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED10` | `FsGiAdlCashExcessProcess_Reserved10` | TField |  |  |
| 8 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED9` | `FsGiAdlCashExcessProcess_Reserved9` | TField |  |  |
| 9 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED8` | `FsGiAdlCashExcessProcess_Reserved8` | TField |  |  |
| 10 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED7` | `FsGiAdlCashExcessProcess_Reserved7` | TField |  |  |
| 11 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED6` | `FsGiAdlCashExcessProcess_Reserved6` | TField |  |  |
| 12 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED5` | `FsGiAdlCashExcessProcess_Reserved5` | TField |  |  |
| 13 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED4` | `FsGiAdlCashExcessProcess_Reserved4` | TField |  |  |
| 14 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED3` | `FsGiAdlCashExcessProcess_Reserved3` | TField |  |  |
| 15 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED2` | `FsGiAdlCashExcessProcess_Reserved2` | TField |  |  |
| 16 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RESERVED1` | `FsGiAdlCashExcessProcess_Reserved1` | TField |  |  |
| 17 | `FS.GI.ADL.CASH.EXCESS.PROCESS.LOCAL.REF` | `FsGiAdlCashExcessProcess_LocalRef` |  |  |  |
| 18 | `FS.GI.ADL.CASH.EXCESS.PROCESS.OVERRIDE` | `FsGiAdlCashExcessProcess_Override` |  |  |  |
| 19 | `FS.GI.ADL.CASH.EXCESS.PROCESS.RECORD.STATUS` | `FsGiAdlCashExcessProcess_RecordStatus` | String |  |  |
| 20 | `FS.GI.ADL.CASH.EXCESS.PROCESS.CURR.NO` | `FsGiAdlCashExcessProcess_CurrNo` | String |  |  |
| 21 | `FS.GI.ADL.CASH.EXCESS.PROCESS.INPUTTER` | `FsGiAdlCashExcessProcess_Inputter` |  |  |  |
| 22 | `FS.GI.ADL.CASH.EXCESS.PROCESS.DATE.TIME` | `FsGiAdlCashExcessProcess_DateTime` |  |  |  |
| 23 | `FS.GI.ADL.CASH.EXCESS.PROCESS.AUTHORISER` | `FsGiAdlCashExcessProcess_Authoriser` | String |  |  |
| 24 | `FS.GI.ADL.CASH.EXCESS.PROCESS.CO.CODE` | `FsGiAdlCashExcessProcess_CoCode` | String |  |  |
| 25 | `FS.GI.ADL.CASH.EXCESS.PROCESS.DEPT.CODE` | `FsGiAdlCashExcessProcess_DeptCode` | String |  |  |
| 26 | `FS.GI.ADL.CASH.EXCESS.PROCESS.AUDITOR.CODE` | `FsGiAdlCashExcessProcess_AuditorCode` | String |  |  |
| 27 | `FS.GI.ADL.CASH.EXCESS.PROCESS.AUDIT.DATE.TIME` | `FsGiAdlCashExcessProcess_AuditDateTime` | String |  |  |
