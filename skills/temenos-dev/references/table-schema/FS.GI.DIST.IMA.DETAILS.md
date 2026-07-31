# FS.GI.DIST.IMA.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.IMA.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.IMA.DETAILS.PARENT.REF.ID` | `FsGiDistImaDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.IMA.DETAILS.ORA.ROWID` | `FsGiDistImaDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.IMA.DETAILS.PARENT.TYPE` | `FsGiDistImaDetails_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.IMA.DETAILS.PARENT.TYPE.ID` | `FsGiDistImaDetails_ParentTypeId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.IMA.DETAILS.LEGAL.ENTITY.ID` | `FsGiDistImaDetails_LegalEntityId` | TField |  | Legal Entity ID linked to the investment management Agreement of the entity. Multifonds DB Column is NTFC. |
| 6 | `FS.GI.DIST.IMA.DETAILS.TA.FUND.ID` | `FsGiDistImaDetails_TaFundId` | TField |  | Fund ID linked to the investment Management agreement of the entity Multifonds DB Column is NPTF. |
| 7 | `FS.GI.DIST.IMA.DETAILS.SHARE.CLASS.CODE` | `FsGiDistImaDetails_ShareClassCode` | TField |  | Fund Share class linked to the investment management agreement of the entity Multifonds DB Column is TPART. |
| 8 | `FS.GI.DIST.IMA.DETAILS.IMA.RECEIVED.FLAG` | `FsGiDistImaDetails_ImaReceivedFlag` | TField |  | Flag indicates that the Investment Management Agreement has been received. Multifonds DB Column is FLG_IMA. |
| 9 | `FS.GI.DIST.IMA.DETAILS.IMA.DETAILS.ID` | `FsGiDistImaDetails_ImaDetailsId` | TField |  | Unique internal investment management agreement identifier. Multifonds DB Column is INTERNAL_ID. |
| 10 | `FS.GI.DIST.IMA.DETAILS.FUND.ID` | `FsGiDistImaDetails_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 11 | `FS.GI.DIST.IMA.DETAILS.CLASS.CURRENCY` | `FsGiDistImaDetails_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 12 | `FS.GI.DIST.IMA.DETAILS.RESERVED10` | `FsGiDistImaDetails_Reserved10` | TField |  |  |
| 13 | `FS.GI.DIST.IMA.DETAILS.RESERVED9` | `FsGiDistImaDetails_Reserved9` | TField |  |  |
| 14 | `FS.GI.DIST.IMA.DETAILS.RESERVED8` | `FsGiDistImaDetails_Reserved8` | TField |  |  |
| 15 | `FS.GI.DIST.IMA.DETAILS.RESERVED7` | `FsGiDistImaDetails_Reserved7` | TField |  |  |
| 16 | `FS.GI.DIST.IMA.DETAILS.RESERVED6` | `FsGiDistImaDetails_Reserved6` | TField |  |  |
| 17 | `FS.GI.DIST.IMA.DETAILS.RESERVED5` | `FsGiDistImaDetails_Reserved5` | TField |  |  |
| 18 | `FS.GI.DIST.IMA.DETAILS.RESERVED4` | `FsGiDistImaDetails_Reserved4` | TField |  |  |
| 19 | `FS.GI.DIST.IMA.DETAILS.RESERVED3` | `FsGiDistImaDetails_Reserved3` | TField |  |  |
| 20 | `FS.GI.DIST.IMA.DETAILS.RESERVED2` | `FsGiDistImaDetails_Reserved2` | TField |  |  |
| 21 | `FS.GI.DIST.IMA.DETAILS.RESERVED1` | `FsGiDistImaDetails_Reserved1` | TField |  |  |
| 22 | `FS.GI.DIST.IMA.DETAILS.LOCAL.REF` | `FsGiDistImaDetails_LocalRef` |  |  |  |
| 23 | `FS.GI.DIST.IMA.DETAILS.OVERRIDE` | `FsGiDistImaDetails_Override` |  |  |  |
| 24 | `FS.GI.DIST.IMA.DETAILS.RECORD.STATUS` | `FsGiDistImaDetails_RecordStatus` | String |  |  |
| 25 | `FS.GI.DIST.IMA.DETAILS.CURR.NO` | `FsGiDistImaDetails_CurrNo` | String |  |  |
| 26 | `FS.GI.DIST.IMA.DETAILS.INPUTTER` | `FsGiDistImaDetails_Inputter` |  |  |  |
| 27 | `FS.GI.DIST.IMA.DETAILS.DATE.TIME` | `FsGiDistImaDetails_DateTime` |  |  |  |
| 28 | `FS.GI.DIST.IMA.DETAILS.AUTHORISER` | `FsGiDistImaDetails_Authoriser` | String |  |  |
| 29 | `FS.GI.DIST.IMA.DETAILS.CO.CODE` | `FsGiDistImaDetails_CoCode` | String |  |  |
| 30 | `FS.GI.DIST.IMA.DETAILS.DEPT.CODE` | `FsGiDistImaDetails_DeptCode` | String |  |  |
| 31 | `FS.GI.DIST.IMA.DETAILS.AUDITOR.CODE` | `FsGiDistImaDetails_AuditorCode` | String |  |  |
| 32 | `FS.GI.DIST.IMA.DETAILS.AUDIT.DATE.TIME` | `FsGiDistImaDetails_AuditDateTime` | String |  |  |
