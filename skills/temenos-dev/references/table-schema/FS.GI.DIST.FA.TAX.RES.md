# FS.GI.DIST.FA.TAX.RES — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.FA.TAX.RES` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.FA.TAX.RES.PARENT.REF.ID` | `FsGiDistFaTaxRes_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.FA.TAX.RES.ORA.ROWID` | `FsGiDistFaTaxRes_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.FA.TAX.RES.PARENT.ID.TYPE` | `FsGiDistFaTaxRes_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.FA.TAX.RES.PARENT.ID` | `FsGiDistFaTaxRes_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.FA.TAX.RES.TAX.RESIDENCE` | `FsGiDistFaTaxRes_TaxResidence` | TField |  | It specifies the country code (2 letter ISO format) to which the entity linked as tax residence. Multifonds DB Column is CTAX_RESIDENCE. |
| 6 | `FS.GI.DIST.FA.TAX.RES.TAX.ID.NUMBER` | `FsGiDistFaTaxRes_TaxIdNumber` | TField |  | Tax Identification number. Multifonds DB Column is CTAX_NO. |
| 7 | `FS.GI.DIST.FA.TAX.RES.TAX.ID.COMMENT` | `FsGiDistFaTaxRes_TaxIdComment` | TField |  | Free text field that allows upto 120 alpha numerical characters for tax residence and identification number comments. Multifonds DB Column is COMMENTS. |
| 8 | `FS.GI.DIST.FA.TAX.RES.RESERVED10` | `FsGiDistFaTaxRes_Reserved10` | TField |  |  |
| 9 | `FS.GI.DIST.FA.TAX.RES.RESERVED9` | `FsGiDistFaTaxRes_Reserved9` | TField |  |  |
| 10 | `FS.GI.DIST.FA.TAX.RES.RESERVED8` | `FsGiDistFaTaxRes_Reserved8` | TField |  |  |
| 11 | `FS.GI.DIST.FA.TAX.RES.RESERVED7` | `FsGiDistFaTaxRes_Reserved7` | TField |  |  |
| 12 | `FS.GI.DIST.FA.TAX.RES.RESERVED6` | `FsGiDistFaTaxRes_Reserved6` | TField |  |  |
| 13 | `FS.GI.DIST.FA.TAX.RES.RESERVED5` | `FsGiDistFaTaxRes_Reserved5` | TField |  |  |
| 14 | `FS.GI.DIST.FA.TAX.RES.RESERVED4` | `FsGiDistFaTaxRes_Reserved4` | TField |  |  |
| 15 | `FS.GI.DIST.FA.TAX.RES.RESERVED3` | `FsGiDistFaTaxRes_Reserved3` | TField |  |  |
| 16 | `FS.GI.DIST.FA.TAX.RES.RESERVED2` | `FsGiDistFaTaxRes_Reserved2` | TField |  |  |
| 17 | `FS.GI.DIST.FA.TAX.RES.RESERVED1` | `FsGiDistFaTaxRes_Reserved1` | TField |  |  |
| 18 | `FS.GI.DIST.FA.TAX.RES.LOCAL.REF` | `FsGiDistFaTaxRes_LocalRef` |  |  |  |
| 19 | `FS.GI.DIST.FA.TAX.RES.OVERRIDE` | `FsGiDistFaTaxRes_Override` |  |  |  |
| 20 | `FS.GI.DIST.FA.TAX.RES.RECORD.STATUS` | `FsGiDistFaTaxRes_RecordStatus` | String |  |  |
| 21 | `FS.GI.DIST.FA.TAX.RES.CURR.NO` | `FsGiDistFaTaxRes_CurrNo` | String |  |  |
| 22 | `FS.GI.DIST.FA.TAX.RES.INPUTTER` | `FsGiDistFaTaxRes_Inputter` |  |  |  |
| 23 | `FS.GI.DIST.FA.TAX.RES.DATE.TIME` | `FsGiDistFaTaxRes_DateTime` |  |  |  |
| 24 | `FS.GI.DIST.FA.TAX.RES.AUTHORISER` | `FsGiDistFaTaxRes_Authoriser` | String |  |  |
| 25 | `FS.GI.DIST.FA.TAX.RES.CO.CODE` | `FsGiDistFaTaxRes_CoCode` | String |  |  |
| 26 | `FS.GI.DIST.FA.TAX.RES.DEPT.CODE` | `FsGiDistFaTaxRes_DeptCode` | String |  |  |
| 27 | `FS.GI.DIST.FA.TAX.RES.AUDITOR.CODE` | `FsGiDistFaTaxRes_AuditorCode` | String |  |  |
| 28 | `FS.GI.DIST.FA.TAX.RES.AUDIT.DATE.TIME` | `FsGiDistFaTaxRes_AuditDateTime` | String |  |  |
