# FS.GI.APP.HOLDING.LIMIT.MAST — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.HOLDING.LIMIT.MAST` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.HOLDING.LIMIT.MAST.PARENT.REF.ID` | `FsGiAppHoldingLimitMast_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.HOLDING.LIMIT.MAST.ORA.ROWID` | `FsGiAppHoldingLimitMast_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.HOLDING.LIMIT.MAST.PARENT.TYPE` | `FsGiAppHoldingLimitMast_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.HOLDING.LIMIT.MAST.PARENT.TYPE.ID` | `FsGiAppHoldingLimitMast_ParentTypeId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.HOLDING.LIMIT.MAST.FUND.ID` | `FsGiAppHoldingLimitMast_FundId` | TField |  | Fund linked to the holding limit check. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.APP.HOLDING.LIMIT.MAST.LIMIT.CURRENCY` | `FsGiAppHoldingLimitMast_LimitCurrency` | TField |  | The currency (in 3 letter format eg: EUR) of the minimum holding limt check. Multifonds DB Column is CMON_LIMIT. |
| 7 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED10` | `FsGiAppHoldingLimitMast_Reserved10` | TField |  |  |
| 8 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED9` | `FsGiAppHoldingLimitMast_Reserved9` | TField |  |  |
| 9 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED8` | `FsGiAppHoldingLimitMast_Reserved8` | TField |  |  |
| 10 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED7` | `FsGiAppHoldingLimitMast_Reserved7` | TField |  |  |
| 11 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED6` | `FsGiAppHoldingLimitMast_Reserved6` | TField |  |  |
| 12 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED5` | `FsGiAppHoldingLimitMast_Reserved5` | TField |  |  |
| 13 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED4` | `FsGiAppHoldingLimitMast_Reserved4` | TField |  |  |
| 14 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED3` | `FsGiAppHoldingLimitMast_Reserved3` | TField |  |  |
| 15 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED2` | `FsGiAppHoldingLimitMast_Reserved2` | TField |  |  |
| 16 | `FS.GI.APP.HOLDING.LIMIT.MAST.RESERVED1` | `FsGiAppHoldingLimitMast_Reserved1` | TField |  |  |
| 17 | `FS.GI.APP.HOLDING.LIMIT.MAST.LOCAL.REF` | `FsGiAppHoldingLimitMast_LocalRef` |  |  |  |
| 18 | `FS.GI.APP.HOLDING.LIMIT.MAST.OVERRIDE` | `FsGiAppHoldingLimitMast_Override` |  |  |  |
| 19 | `FS.GI.APP.HOLDING.LIMIT.MAST.RECORD.STATUS` | `FsGiAppHoldingLimitMast_RecordStatus` | String |  |  |
| 20 | `FS.GI.APP.HOLDING.LIMIT.MAST.CURR.NO` | `FsGiAppHoldingLimitMast_CurrNo` | String |  |  |
| 21 | `FS.GI.APP.HOLDING.LIMIT.MAST.INPUTTER` | `FsGiAppHoldingLimitMast_Inputter` |  |  |  |
| 22 | `FS.GI.APP.HOLDING.LIMIT.MAST.DATE.TIME` | `FsGiAppHoldingLimitMast_DateTime` |  |  |  |
| 23 | `FS.GI.APP.HOLDING.LIMIT.MAST.AUTHORISER` | `FsGiAppHoldingLimitMast_Authoriser` | String |  |  |
| 24 | `FS.GI.APP.HOLDING.LIMIT.MAST.CO.CODE` | `FsGiAppHoldingLimitMast_CoCode` | String |  |  |
| 25 | `FS.GI.APP.HOLDING.LIMIT.MAST.DEPT.CODE` | `FsGiAppHoldingLimitMast_DeptCode` | String |  |  |
| 26 | `FS.GI.APP.HOLDING.LIMIT.MAST.AUDITOR.CODE` | `FsGiAppHoldingLimitMast_AuditorCode` | String |  |  |
| 27 | `FS.GI.APP.HOLDING.LIMIT.MAST.AUDIT.DATE.TIME` | `FsGiAppHoldingLimitMast_AuditDateTime` | String |  |  |
