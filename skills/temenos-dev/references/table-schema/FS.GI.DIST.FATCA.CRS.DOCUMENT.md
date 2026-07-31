# FS.GI.DIST.FATCA.CRS.DOCUMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.FATCA.CRS.DOCUMENT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.PARENT.REF.ID` | `FsGiDistFatcaCrsDocument_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.ORA.ROWID` | `FsGiDistFatcaCrsDocument_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.PARENT.ID.TYPE` | `FsGiDistFatcaCrsDocument_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.PARENT.ID` | `FsGiDistFatcaCrsDocument_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.MANDATORY.FLAG` | `FsGiDistFatcaCrsDocument_MandatoryFlag` | TField | Yes | Flag allows to specify whether the manually entered documents are mandatory or not. Multifonds DB Column is DOC_MAND. |
| 6 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.DOCUMENT.SET.ID` | `FsGiDistFatcaCrsDocument_FatcaDocumentSetId` | TField |  | It specifies the Document Set ID which can be maually set or automatically populated by the system based on match rules. Multifonds DB Column is FAT_SET_ID. |
| 7 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.NUMBER.MAND.DOC` | `FsGiDistFatcaCrsDocument_NumberMandDoc` | TField | Yes | Number of mandatory documents. Multifonds DB Column is FAT_NO_OF_MAND. |
| 8 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.DOCUMENT.ID` | `FsGiDistFatcaCrsDocument_FatcaDocumentId` | TField |  | Type of the document. Multifonds DB Column is FAT_DOC_ID. |
| 9 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.DOCUMENT.ATTRIBUTE` | `FsGiDistFatcaCrsDocument_DocumentAttribute` | TField |  | It specifies the attribute of the document. Multifonds DB Column is FAT_ATTRIB. |
| 10 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.RECEIVED.FLAG` | `FsGiDistFatcaCrsDocument_FatcaReceivedFlag` | TField |  | Flag allows to indicates that the document has been received. Multifonds DB Column is FAT_FLG_RECEIVED. |
| 11 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.RECEIVED.DATE` | `FsGiDistFatcaCrsDocument_FatcaReceivedDate` | TField |  | Date (in DD/MM/YYYY format) when the document was received. Multifonds DB Column is FAT_DRECEIVED. |
| 12 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.EXPIRY.DATE` | `FsGiDistFatcaCrsDocument_FatcaExpiryDate` | TField |  | Date (in DD/MM/YYYY format) when the document expired. Multifonds DB Column is FAT_DEXPIRY. |
| 13 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.EFFECTIVE.DATE` | `FsGiDistFatcaCrsDocument_FatcaEffectiveDate` | TField |  | Date (in DD/MM/YYYY format) when the document was issued. Multifonds DB Column is FAT_DISSUE. |
| 14 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.FILE.NAME` | `FsGiDistFatcaCrsDocument_FatcaFileName` | TField |  | The file name of the document. Multifonds DB Column is FAT_FILE_NAME. |
| 15 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.FATCA.COMMENT` | `FsGiDistFatcaCrsDocument_FatcaComment` | TField |  | Free text field that allows upto 250 alpha numerical characters for FATCA document comments. Multifonds DB Column is FAT_COMMENTS. |
| 16 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.INTERNAL.ID` | `FsGiDistFatcaCrsDocument_InternalId` | TField |  | Unique internal document identifier. Multifonds DB Column is INTERNAL_ID. |
| 17 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED10` | `FsGiDistFatcaCrsDocument_Reserved10` | TField |  |  |
| 18 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED9` | `FsGiDistFatcaCrsDocument_Reserved9` | TField |  |  |
| 19 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED8` | `FsGiDistFatcaCrsDocument_Reserved8` | TField |  |  |
| 20 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED7` | `FsGiDistFatcaCrsDocument_Reserved7` | TField |  |  |
| 21 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED6` | `FsGiDistFatcaCrsDocument_Reserved6` | TField |  |  |
| 22 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED5` | `FsGiDistFatcaCrsDocument_Reserved5` | TField |  |  |
| 23 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED4` | `FsGiDistFatcaCrsDocument_Reserved4` | TField |  |  |
| 24 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED3` | `FsGiDistFatcaCrsDocument_Reserved3` | TField |  |  |
| 25 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED2` | `FsGiDistFatcaCrsDocument_Reserved2` | TField |  |  |
| 26 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RESERVED1` | `FsGiDistFatcaCrsDocument_Reserved1` | TField |  |  |
| 27 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.LOCAL.REF` | `FsGiDistFatcaCrsDocument_LocalRef` |  |  |  |
| 28 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.OVERRIDE` | `FsGiDistFatcaCrsDocument_Override` |  |  |  |
| 29 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.RECORD.STATUS` | `FsGiDistFatcaCrsDocument_RecordStatus` | String |  |  |
| 30 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.CURR.NO` | `FsGiDistFatcaCrsDocument_CurrNo` | String |  |  |
| 31 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.INPUTTER` | `FsGiDistFatcaCrsDocument_Inputter` |  |  |  |
| 32 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.DATE.TIME` | `FsGiDistFatcaCrsDocument_DateTime` |  |  |  |
| 33 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.AUTHORISER` | `FsGiDistFatcaCrsDocument_Authoriser` | String |  |  |
| 34 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.CO.CODE` | `FsGiDistFatcaCrsDocument_CoCode` | String |  |  |
| 35 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.DEPT.CODE` | `FsGiDistFatcaCrsDocument_DeptCode` | String |  |  |
| 36 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.AUDITOR.CODE` | `FsGiDistFatcaCrsDocument_AuditorCode` | String |  |  |
| 37 | `FS.GI.DIST.FATCA.CRS.DOCUMENT.AUDIT.DATE.TIME` | `FsGiDistFatcaCrsDocument_AuditDateTime` | String |  |  |
