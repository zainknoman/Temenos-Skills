# FS.GI.DIST.FATCA.CRS.STATUS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.FATCA.CRS.STATUS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.FATCA.CRS.STATUS.PARENT.REF.ID` | `FsGiDistFatcaCrsStatus_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.FATCA.CRS.STATUS.ORA.ROWID` | `FsGiDistFatcaCrsStatus_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.FATCA.CRS.STATUS.PARENT.ID.TYPE` | `FsGiDistFatcaCrsStatus_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.FATCA.CRS.STATUS.PARENT.ID` | `FsGiDistFatcaCrsStatus_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.FATCA.CRS.STATUS.GIIN.NUMBER` | `FsGiDistFatcaCrsStatus_GiinNumber` | TField |  | GIIN identification number. Each registering FI will be given a FATCA ID that will be used for purposes of establishing and accessing the FI&apos;s online FATCA account. Multifonds DB Column is FAT_GIIN. |
| 6 | `FS.GI.DIST.FATCA.CRS.STATUS.WITHHOLDING.STATUS` | `FsGiDistFatcaCrsStatus_WithholdingStatus` | TField |  | FATCA Withholding Status Multifonds DB Column is FAT_WH_STATUS. |
| 7 | `FS.GI.DIST.FATCA.CRS.STATUS.FATCA.STATUS` | `FsGiDistFatcaCrsStatus_FatcaStatus` | TField |  | FATCA/CRS Status of the entity, depending on the Criteria code. Multifonds DB Column is FAT_STATUS. |
| 8 | `FS.GI.DIST.FATCA.CRS.STATUS.SUB.STATUS` | `FsGiDistFatcaCrsStatus_SubStatus` | TField |  | FATCA/CRS Sub-status of the entity and is considerable as a specification of the corresponding status, depending on the Criteria code. Multifonds DB Column is FAT_SUB_STATUS. |
| 9 | `FS.GI.DIST.FATCA.CRS.STATUS.FATCA.EFFECTIVE.DATE` | `FsGiDistFatcaCrsStatus_FatcaEffectiveDate` | TField |  | Date (DD/MM/YYY) from which the FATCA/CRS is effective. Multifonds DB Column is FAT_DEFFECTIVE. |
| 10 | `FS.GI.DIST.FATCA.CRS.STATUS.FATCA.EXPIRY.DATE` | `FsGiDistFatcaCrsStatus_FatcaExpiryDate` | TField |  | Date (in DD/MM/YYYY format) when the FATCA/CRS is expiried. Multifonds DB Column is FAT_DEXPIRY. |
| 11 | `FS.GI.DIST.FATCA.CRS.STATUS.FATCA.REVOKE.DATE` | `FsGiDistFatcaCrsStatus_FatcaRevokeDate` | TField |  | Date (DD/MM/YYY) from which the FATCA/CRS is revoked. Multifonds DB Column is FAT_DREVOKE. |
| 12 | `FS.GI.DIST.FATCA.CRS.STATUS.LAST.REVIEW.DATE` | `FsGiDistFatcaCrsStatus_LastReviewDate` | TField |  | The last review date (DD/MM/YYYY). The value must be unique for all FATCA/CRS set-ups. Multifonds DB Column is FAT_DLAST_REVIEW. |
| 13 | `FS.GI.DIST.FATCA.CRS.STATUS.NEXT.REVIEW.DATE` | `FsGiDistFatcaCrsStatus_NextReviewDate` | TField |  | The next review date (DD/MM/YYYY). The value must be unique for all FATCA/CRS set-ups. Multifonds DB Column is FAT_DNEXT_REVIEW. |
| 14 | `FS.GI.DIST.FATCA.CRS.STATUS.FATCA.EXEMPTION.REASON` | `FsGiDistFatcaCrsStatus_FatcaExemptionReason` | TField |  | FATCA exempt reason code. Multifonds DB Column is FAT_EXEM_REASON. |
| 15 | `FS.GI.DIST.FATCA.CRS.STATUS.THRESHOLD.STATUS` | `FsGiDistFatcaCrsStatus_ThresholdStatus` | TField |  | FATCA or CRS Sub-threshold status, depending on the Criteria code. Multifonds DB Column is FAT_THHOLD_STATUS. |
| 16 | `FS.GI.DIST.FATCA.CRS.STATUS.LAST.CALCULATION.DATE` | `FsGiDistFatcaCrsStatus_LastCalculationDate` | TField |  | Date Of Last Calculation. Multifonds DB Column is FAT_DLAST_CALC. |
| 17 | `FS.GI.DIST.FATCA.CRS.STATUS.FATCA.FREE.TEXT` | `FsGiDistFatcaCrsStatus_FatcaFreeText` | TField |  | Free text field that allows upto 250 alpha numerical characters for generic information Multifonds DB Column is FAT_TEXT. |
| 18 | `FS.GI.DIST.FATCA.CRS.STATUS.DOCUMENT.STATUS` | `FsGiDistFatcaCrsStatus_DocumentStatus` | TField |  | The field is automatically updated by the system and indicates the document status Multifonds DB Column is FAT_DOC_STATUS. |
| 19 | `FS.GI.DIST.FATCA.CRS.STATUS.INITIAL.DOCUMENT.REQUEST.DATE` | `FsGiDistFatcaCrsStatus_InitialDocumentRequestDate` | TField |  | The initial date (DD/MM/YYYY) when the list of documents has been requested from the investor. Multifonds DB Column is FAT_DINTIAL_REQ. |
| 20 | `FS.GI.DIST.FATCA.CRS.STATUS.LAST.DOCUMENT.REQUEST.DATE` | `FsGiDistFatcaCrsStatus_LastDocumentRequestDate` | TField |  | The last date (DD/MM/YYYY) when the list of documents has been requested from the investor. Multifonds DB Column is FAT_DLAST_REQ. |
| 21 | `FS.GI.DIST.FATCA.CRS.STATUS.USE.DOCUMENT.SET.FLAG` | `FsGiDistFatcaCrsStatus_UseDocumentSetFlag` | TField |  | Flag allows to activate the automatic check of the documents based on the matching rules. Otherwise, the user shall manually enter the document IDs and attributes. Multifonds DB Column is FLG_DOC_SET. |
| 22 | `FS.GI.DIST.FATCA.CRS.STATUS.INTERNAL.ID` | `FsGiDistFatcaCrsStatus_InternalId` | TField |  | Unique internal identifier for FATCA/CRS status record. Multifonds DB Column is INTERNAL_ID. |
| 23 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED10` | `FsGiDistFatcaCrsStatus_Reserved10` | TField |  |  |
| 24 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED9` | `FsGiDistFatcaCrsStatus_Reserved9` | TField |  |  |
| 25 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED8` | `FsGiDistFatcaCrsStatus_Reserved8` | TField |  |  |
| 26 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED7` | `FsGiDistFatcaCrsStatus_Reserved7` | TField |  |  |
| 27 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED6` | `FsGiDistFatcaCrsStatus_Reserved6` | TField |  |  |
| 28 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED5` | `FsGiDistFatcaCrsStatus_Reserved5` | TField |  |  |
| 29 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED4` | `FsGiDistFatcaCrsStatus_Reserved4` | TField |  |  |
| 30 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED3` | `FsGiDistFatcaCrsStatus_Reserved3` | TField |  |  |
| 31 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED2` | `FsGiDistFatcaCrsStatus_Reserved2` | TField |  |  |
| 32 | `FS.GI.DIST.FATCA.CRS.STATUS.RESERVED1` | `FsGiDistFatcaCrsStatus_Reserved1` | TField |  |  |
| 33 | `FS.GI.DIST.FATCA.CRS.STATUS.LOCAL.REF` | `FsGiDistFatcaCrsStatus_LocalRef` |  |  |  |
| 34 | `FS.GI.DIST.FATCA.CRS.STATUS.OVERRIDE` | `FsGiDistFatcaCrsStatus_Override` |  |  |  |
| 35 | `FS.GI.DIST.FATCA.CRS.STATUS.RECORD.STATUS` | `FsGiDistFatcaCrsStatus_RecordStatus` | String |  |  |
| 36 | `FS.GI.DIST.FATCA.CRS.STATUS.CURR.NO` | `FsGiDistFatcaCrsStatus_CurrNo` | String |  |  |
| 37 | `FS.GI.DIST.FATCA.CRS.STATUS.INPUTTER` | `FsGiDistFatcaCrsStatus_Inputter` |  |  |  |
| 38 | `FS.GI.DIST.FATCA.CRS.STATUS.DATE.TIME` | `FsGiDistFatcaCrsStatus_DateTime` |  |  |  |
| 39 | `FS.GI.DIST.FATCA.CRS.STATUS.AUTHORISER` | `FsGiDistFatcaCrsStatus_Authoriser` | String |  |  |
| 40 | `FS.GI.DIST.FATCA.CRS.STATUS.CO.CODE` | `FsGiDistFatcaCrsStatus_CoCode` | String |  |  |
| 41 | `FS.GI.DIST.FATCA.CRS.STATUS.DEPT.CODE` | `FsGiDistFatcaCrsStatus_DeptCode` | String |  |  |
| 42 | `FS.GI.DIST.FATCA.CRS.STATUS.AUDITOR.CODE` | `FsGiDistFatcaCrsStatus_AuditorCode` | String |  |  |
| 43 | `FS.GI.DIST.FATCA.CRS.STATUS.AUDIT.DATE.TIME` | `FsGiDistFatcaCrsStatus_AuditDateTime` | String |  |  |
