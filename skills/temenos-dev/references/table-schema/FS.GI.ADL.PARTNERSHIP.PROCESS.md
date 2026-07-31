# FS.GI.ADL.PARTNERSHIP.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.ADL.PARTNERSHIP.PROCESS` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.ADL.PARTNERSHIP.PROCESS.PARENT.REF.ID` | `FsGiAdlPartnershipProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.ADL.PARTNERSHIP.PROCESS.ORA.ROWID` | `FsGiAdlPartnershipProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.ADL.PARTNERSHIP.PROCESS.EXCHANGE.GROUP` | `FsGiAdlPartnershipProcess_ExchangeGroup` | TField |  | Fund exchange group. Multifonds DB Column is P_CGROUPE_COURS. |
| 4 | `FS.GI.ADL.PARTNERSHIP.PROCESS.FUND.ID` | `FsGiAdlPartnershipProcess_FundId` | TField |  | Master Fund internal ID. Multifonds DB Column is P_MULTIFONDS_ID. |
| 5 | `FS.GI.ADL.PARTNERSHIP.PROCESS.CALC.DATE` | `FsGiAdlPartnershipProcess_CalcDate` | TField |  | ADL calculation procesing date. Multifonds DB Column is P_DATE_CAL. |
| 6 | `FS.GI.ADL.PARTNERSHIP.PROCESS.ADL.PROCESS` | `FsGiAdlPartnershipProcess_AdlProcess` | TField |  | ADL process used for processing. Multifonds DB Column is P_ADL_PROCESS. |
| 7 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED10` | `FsGiAdlPartnershipProcess_Reserved10` | TField |  |  |
| 8 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED9` | `FsGiAdlPartnershipProcess_Reserved9` | TField |  |  |
| 9 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED8` | `FsGiAdlPartnershipProcess_Reserved8` | TField |  |  |
| 10 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED7` | `FsGiAdlPartnershipProcess_Reserved7` | TField |  |  |
| 11 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED6` | `FsGiAdlPartnershipProcess_Reserved6` | TField |  |  |
| 12 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED5` | `FsGiAdlPartnershipProcess_Reserved5` | TField |  |  |
| 13 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED4` | `FsGiAdlPartnershipProcess_Reserved4` | TField |  |  |
| 14 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED3` | `FsGiAdlPartnershipProcess_Reserved3` | TField |  |  |
| 15 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED2` | `FsGiAdlPartnershipProcess_Reserved2` | TField |  |  |
| 16 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RESERVED1` | `FsGiAdlPartnershipProcess_Reserved1` | TField |  |  |
| 17 | `FS.GI.ADL.PARTNERSHIP.PROCESS.LOCAL.REF` | `FsGiAdlPartnershipProcess_LocalRef` |  |  |  |
| 18 | `FS.GI.ADL.PARTNERSHIP.PROCESS.OVERRIDE` | `FsGiAdlPartnershipProcess_Override` |  |  |  |
| 19 | `FS.GI.ADL.PARTNERSHIP.PROCESS.RECORD.STATUS` | `FsGiAdlPartnershipProcess_RecordStatus` | String |  |  |
| 20 | `FS.GI.ADL.PARTNERSHIP.PROCESS.CURR.NO` | `FsGiAdlPartnershipProcess_CurrNo` | String |  |  |
| 21 | `FS.GI.ADL.PARTNERSHIP.PROCESS.INPUTTER` | `FsGiAdlPartnershipProcess_Inputter` |  |  |  |
| 22 | `FS.GI.ADL.PARTNERSHIP.PROCESS.DATE.TIME` | `FsGiAdlPartnershipProcess_DateTime` |  |  |  |
| 23 | `FS.GI.ADL.PARTNERSHIP.PROCESS.AUTHORISER` | `FsGiAdlPartnershipProcess_Authoriser` | String |  |  |
| 24 | `FS.GI.ADL.PARTNERSHIP.PROCESS.CO.CODE` | `FsGiAdlPartnershipProcess_CoCode` | String |  |  |
| 25 | `FS.GI.ADL.PARTNERSHIP.PROCESS.DEPT.CODE` | `FsGiAdlPartnershipProcess_DeptCode` | String |  |  |
| 26 | `FS.GI.ADL.PARTNERSHIP.PROCESS.AUDITOR.CODE` | `FsGiAdlPartnershipProcess_AuditorCode` | String |  |  |
| 27 | `FS.GI.ADL.PARTNERSHIP.PROCESS.AUDIT.DATE.TIME` | `FsGiAdlPartnershipProcess_AuditDateTime` | String |  |  |
