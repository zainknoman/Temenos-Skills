# FS.GI.DIST.FA.ID.DOC — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.FA.ID.DOC` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.FA.ID.DOC.PARENT.REF.ID` | `FsGiDistFaIdDoc_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.FA.ID.DOC.ORA.ROWID` | `FsGiDistFaIdDoc_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.FA.ID.DOC.PARENT.TYPE` | `FsGiDistFaIdDoc_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.FA.ID.DOC.PARENT.ID` | `FsGiDistFaIdDoc_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.FA.ID.DOC.DOCUMENT.TYPE` | `FsGiDistFaIdDoc_DocumentType` | TField |  | Type of the document. Multifonds DB Column is DOC_ID. |
| 6 | `FS.GI.DIST.FA.ID.DOC.DOCUMENT.ID.NUMBER` | `FsGiDistFaIdDoc_DocumentIdNumber` | TField |  | Document ID reference number. Multifonds DB Column is ID_NUMBER. |
| 7 | `FS.GI.DIST.FA.ID.DOC.DOCUMENT.ISSUING.COUNTRY` | `FsGiDistFaIdDoc_DocumentIssuingCountry` | TField |  | It specifies country code (in 2 letter ISO code) in which the document was issued. Multifonds DB Column is NISSUER. |
| 8 | `FS.GI.DIST.FA.ID.DOC.ISSUE.DATE` | `FsGiDistFaIdDoc_IssueDate` | TField |  | Date (in DD/MM/YYYY format) when the document issued. Multifonds DB Column is DISSUE. |
| 9 | `FS.GI.DIST.FA.ID.DOC.AML.DOC.EXPIRY.DATE` | `FsGiDistFaIdDoc_AmlDocExpiryDate` | TField |  | Date (in DD/MM/YYYY format) when the document expired. Multifonds DB Column is DEXPIRY. |
| 10 | `FS.GI.DIST.FA.ID.DOC.RECEIVED.DATE` | `FsGiDistFaIdDoc_ReceivedDate` | TField |  | Date (in DD/MM/YYYY format) when the document received. Multifonds DB Column is DRECEIVE. |
| 11 | `FS.GI.DIST.FA.ID.DOC.DOCUMENT.REVOKED.FLAG` | `FsGiDistFaIdDoc_DocumentRevokedFlag` | TField |  | Flag allows to indicate that the document has been revoked. Multifonds DB Column is FLG_REVOKED. |
| 12 | `FS.GI.DIST.FA.ID.DOC.REVOKE.END.DATE` | `FsGiDistFaIdDoc_RevokeEndDate` | TField |  | Date (in DD/MM/YYYY format) when the document revoked. Multifonds DB Column is DREVOKE. |
| 13 | `FS.GI.DIST.FA.ID.DOC.TAX.ID.COMMENT` | `FsGiDistFaIdDoc_TaxIdComment` | TField |  | Free text field that allows upto 250 alpha numerical characters for tax document related comments Multifonds DB Column is COMMENTS. |
| 14 | `FS.GI.DIST.FA.ID.DOC.RESERVED10` | `FsGiDistFaIdDoc_Reserved10` | TField |  |  |
| 15 | `FS.GI.DIST.FA.ID.DOC.RESERVED9` | `FsGiDistFaIdDoc_Reserved9` | TField |  |  |
| 16 | `FS.GI.DIST.FA.ID.DOC.RESERVED8` | `FsGiDistFaIdDoc_Reserved8` | TField |  |  |
| 17 | `FS.GI.DIST.FA.ID.DOC.RESERVED7` | `FsGiDistFaIdDoc_Reserved7` | TField |  |  |
| 18 | `FS.GI.DIST.FA.ID.DOC.RESERVED6` | `FsGiDistFaIdDoc_Reserved6` | TField |  |  |
| 19 | `FS.GI.DIST.FA.ID.DOC.RESERVED5` | `FsGiDistFaIdDoc_Reserved5` | TField |  |  |
| 20 | `FS.GI.DIST.FA.ID.DOC.RESERVED4` | `FsGiDistFaIdDoc_Reserved4` | TField |  |  |
| 21 | `FS.GI.DIST.FA.ID.DOC.RESERVED3` | `FsGiDistFaIdDoc_Reserved3` | TField |  |  |
| 22 | `FS.GI.DIST.FA.ID.DOC.RESERVED2` | `FsGiDistFaIdDoc_Reserved2` | TField |  |  |
| 23 | `FS.GI.DIST.FA.ID.DOC.RESERVED1` | `FsGiDistFaIdDoc_Reserved1` | TField |  |  |
| 24 | `FS.GI.DIST.FA.ID.DOC.LOCAL.REF` | `FsGiDistFaIdDoc_LocalRef` |  |  |  |
| 25 | `FS.GI.DIST.FA.ID.DOC.OVERRIDE` | `FsGiDistFaIdDoc_Override` |  |  |  |
| 26 | `FS.GI.DIST.FA.ID.DOC.RECORD.STATUS` | `FsGiDistFaIdDoc_RecordStatus` | String |  |  |
| 27 | `FS.GI.DIST.FA.ID.DOC.CURR.NO` | `FsGiDistFaIdDoc_CurrNo` | String |  |  |
| 28 | `FS.GI.DIST.FA.ID.DOC.INPUTTER` | `FsGiDistFaIdDoc_Inputter` |  |  |  |
| 29 | `FS.GI.DIST.FA.ID.DOC.DATE.TIME` | `FsGiDistFaIdDoc_DateTime` |  |  |  |
| 30 | `FS.GI.DIST.FA.ID.DOC.AUTHORISER` | `FsGiDistFaIdDoc_Authoriser` | String |  |  |
| 31 | `FS.GI.DIST.FA.ID.DOC.CO.CODE` | `FsGiDistFaIdDoc_CoCode` | String |  |  |
| 32 | `FS.GI.DIST.FA.ID.DOC.DEPT.CODE` | `FsGiDistFaIdDoc_DeptCode` | String |  |  |
| 33 | `FS.GI.DIST.FA.ID.DOC.AUDITOR.CODE` | `FsGiDistFaIdDoc_AuditorCode` | String |  |  |
| 34 | `FS.GI.DIST.FA.ID.DOC.AUDIT.DATE.TIME` | `FsGiDistFaIdDoc_AuditDateTime` | String |  |  |
