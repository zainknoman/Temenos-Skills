# FS.GI.FUND.SHARECLASS.EXT — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.SHARECLASS.EXT` in `FS_FundShareClassStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.SHARECLASS.EXT.PARENT.REF.ID` | `FsGiFundShareclassExt_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.SHARECLASS.EXT.ORA.ROWID` | `FsGiFundShareclassExt_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.SHARECLASS.EXT.SECURITY.ID` | `FsGiFundShareclassExt_SecurityId` | TField |  | Security Identification number. Multifonds DB Column is NOVAL. |
| 4 | `FS.GI.FUND.SHARECLASS.EXT.EXT.ID.TYPE` | `FsGiFundShareclassExt_ExtIdType` | TField |  | External ID Type of the security. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.FUND.SHARECLASS.EXT.EXTERNAL.ID` | `FsGiFundShareclassExt_ExternalId` | TField |  | External ID details of the security. Multifonds DB Column is SEC_ID. |
| 6 | `FS.GI.FUND.SHARECLASS.EXT.PARENT.ID.TYPE` | `FsGiFundShareclassExt_ParentIdType` | TField |  | Parent ID type. Multifonds DB Column is ID_TYPE. |
| 7 | `FS.GI.FUND.SHARECLASS.EXT.CURRENCY` | `FsGiFundShareclassExt_Currency` | TField |  | Currency of the security. Multifonds DB Column is CMON. |
| 8 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED10` | `FsGiFundShareclassExt_Reserved10` | TField |  |  |
| 9 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED9` | `FsGiFundShareclassExt_Reserved9` | TField |  |  |
| 10 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED8` | `FsGiFundShareclassExt_Reserved8` | TField |  |  |
| 11 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED7` | `FsGiFundShareclassExt_Reserved7` | TField |  |  |
| 12 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED6` | `FsGiFundShareclassExt_Reserved6` | TField |  |  |
| 13 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED5` | `FsGiFundShareclassExt_Reserved5` | TField |  |  |
| 14 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED4` | `FsGiFundShareclassExt_Reserved4` | TField |  |  |
| 15 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED3` | `FsGiFundShareclassExt_Reserved3` | TField |  |  |
| 16 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED2` | `FsGiFundShareclassExt_Reserved2` | TField |  |  |
| 17 | `FS.GI.FUND.SHARECLASS.EXT.RESERVED1` | `FsGiFundShareclassExt_Reserved1` | TField |  |  |
| 18 | `FS.GI.FUND.SHARECLASS.EXT.LOCAL.REF` | `FsGiFundShareclassExt_LocalRef` |  |  |  |
| 19 | `FS.GI.FUND.SHARECLASS.EXT.OVERRIDE` | `FsGiFundShareclassExt_Override` |  |  |  |
| 20 | `FS.GI.FUND.SHARECLASS.EXT.RECORD.STATUS` | `FsGiFundShareclassExt_RecordStatus` | String |  |  |
| 21 | `FS.GI.FUND.SHARECLASS.EXT.CURR.NO` | `FsGiFundShareclassExt_CurrNo` | String |  |  |
| 22 | `FS.GI.FUND.SHARECLASS.EXT.INPUTTER` | `FsGiFundShareclassExt_Inputter` |  |  |  |
| 23 | `FS.GI.FUND.SHARECLASS.EXT.DATE.TIME` | `FsGiFundShareclassExt_DateTime` |  |  |  |
| 24 | `FS.GI.FUND.SHARECLASS.EXT.AUTHORISER` | `FsGiFundShareclassExt_Authoriser` | String |  |  |
| 25 | `FS.GI.FUND.SHARECLASS.EXT.CO.CODE` | `FsGiFundShareclassExt_CoCode` | String |  |  |
| 26 | `FS.GI.FUND.SHARECLASS.EXT.DEPT.CODE` | `FsGiFundShareclassExt_DeptCode` | String |  |  |
| 27 | `FS.GI.FUND.SHARECLASS.EXT.AUDITOR.CODE` | `FsGiFundShareclassExt_AuditorCode` | String |  |  |
| 28 | `FS.GI.FUND.SHARECLASS.EXT.AUDIT.DATE.TIME` | `FsGiFundShareclassExt_AuditDateTime` | String |  |  |
