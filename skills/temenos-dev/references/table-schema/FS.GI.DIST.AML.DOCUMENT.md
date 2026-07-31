# FS.GI.DIST.AML.DOCUMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AML.DOCUMENT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AML.DOCUMENT.PARENT.REF.ID` | `FsGiDistAmlDocument_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AML.DOCUMENT.ORA.ROWID` | `FsGiDistAmlDocument_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AML.DOCUMENT.PARENT.ID.TYPE` | `FsGiDistAmlDocument_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.AML.DOCUMENT.PARENT.ID` | `FsGiDistAmlDocument_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.MANDATORY.FLAG` | `FsGiDistAmlDocument_AmlDocMandatoryFlag` | TField | Yes | Flag allows to enable the document to be mandatory. Once the flag is set as &apos;Y&apos; the document cannot be deleted. Multifonds DB Column is FLG_MANDATORY. |
| 6 | `FS.GI.DIST.AML.DOCUMENT.AML.DOCUMENT.TYPE` | `FsGiDistAmlDocument_AmlDocumentType` | TField |  | Type of the AML Document. Multifonds DB Column is CDOCUMENT. |
| 7 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.ATTRIBUTE.TYPE` | `FsGiDistAmlDocument_AmlDocAttributeType` | TField |  | It specifies the attribute linked to the specific document. For example: Original, certified copy, copy etc., Multifonds DB Column is CATTRIBUTE. |
| 8 | `FS.GI.DIST.AML.DOCUMENT.FIRST.REQUEST.DATE` | `FsGiDistAmlDocument_FirstRequestDate` | TField |  | Initial date on which the document has been requested. Informative field. Multifonds DB Column is DREQUEST_FIRST. |
| 9 | `FS.GI.DIST.AML.DOCUMENT.LAST.REQUEST.DATE` | `FsGiDistAmlDocument_LastRequestDate` | TField |  | Last date on which the document has been requested. Informative field. Multifonds DB Column is DREQUEST_LAST. |
| 10 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.RECEIVED.FLAG` | `FsGiDistAmlDocument_AmlDocReceivedFlag` | TField |  | Flag allows to indicate that the document has been received. Multifonds DB Column is FLG_RECEIVED. |
| 11 | `FS.GI.DIST.AML.DOCUMENT.RECEIVED.DATE` | `FsGiDistAmlDocument_ReceivedDate` | TField |  | Date on which the document has been received. The field cannot be updated if the flag &quot;Received&quot; is set as &quot;N&quot;. Multifonds DB Column is DRECEIVED. |
| 12 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.EXPIRY.DATE` | `FsGiDistAmlDocument_AmlDocExpiryDate` | TField |  | Expiry date of the document. The field cannot be updated if the flag &quot;Received&quot; is set as &quot;N&quot;. Multifonds DB Column is DEXPIRY. |
| 13 | `FS.GI.DIST.AML.DOCUMENT.ISSUE.DATE` | `FsGiDistAmlDocument_IssueDate` | TField |  | Issuing date of the document. The field cannot be updated if the flag &quot;Received&quot; is set as &quot;N&quot;. Multifonds DB Column is DISSUE. |
| 14 | `FS.GI.DIST.AML.DOCUMENT.FILE.NAME` | `FsGiDistAmlDocument_FileName` | TField |  | The file name of the document. Multifonds DB Column is FILE_NAME. |
| 15 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.ARCHIVE.FLAG` | `FsGiDistAmlDocument_AmlDocArchiveFlag` | TField |  | Document History flag. Multifonds DB Column is FLG_DOC_HISTO. |
| 16 | `FS.GI.DIST.AML.DOCUMENT.RELATED.PARTY.ID` | `FsGiDistAmlDocument_RelatedPartyId` | TField |  | Related Party of the document. An internal ID of the proxy (Investor or Register) linked in the entity relationship having active flag status as &apos;Y&apos;. Multifonds DB Column is RELATED_PARTY. |
| 17 | `FS.GI.DIST.AML.DOCUMENT.ARCHIVE.SEQUENCE` | `FsGiDistAmlDocument_ArchiveSequence` | TField |  | Archive sequence allows the same line with same document parameters to exists multiple times if ticked. Multifonds DB Column is ARCHIVE_SEQ. |
| 18 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.INTERNAL.ID` | `FsGiDistAmlDocument_AmlDocInternalId` | TField |  | Unique internal AML document identifier. Multifonds DB Column is INTERNAL_ID. |
| 19 | `FS.GI.DIST.AML.DOCUMENT.DOC.AML.FLAG` | `FsGiDistAmlDocument_DocAmlFlag` | TField |  | Flag allows to indicate that the document related to AML Multifonds DB Column is DOC_AML_FLAG. |
| 20 | `FS.GI.DIST.AML.DOCUMENT.DOC.TAX.FLAG` | `FsGiDistAmlDocument_DocTaxFlag` | TField |  | Flag allows to indicate that the document related to Tax Multifonds DB Column is DOC_TAX_FLAG. |
| 21 | `FS.GI.DIST.AML.DOCUMENT.DOC.REGULATORY.FLAG` | `FsGiDistAmlDocument_DocRegulatoryFlag` | TField |  | Flag allows to indicate that the document related to Regulatory Multifonds DB Column is DOC_REGULATORY_FLAG. |
| 22 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.TYPE.NUMBER` | `FsGiDistAmlDocument_AmlDocTypeNumber` | TField |  | Number of the Document type Multifonds DB Column is AML_DOC_TYPE_NUMBER. |
| 23 | `FS.GI.DIST.AML.DOCUMENT.DOC.ISSUE.COUNTRY` | `FsGiDistAmlDocument_DocIssueCountry` | TField |  | Issuing country of the document Type Multifonds DB Column is DOC_ISSUE_COUNTRY. |
| 24 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.REVOKED.FLAG` | `FsGiDistAmlDocument_AmlDocRevokedFlag` | TField |  | Flag allows to indicate that the document has been revoked. Multifonds DB Column is AML_DOC_REVOKED_FLAG. |
| 25 | `FS.GI.DIST.AML.DOCUMENT.AML.DOC.REVOKED.DATE` | `FsGiDistAmlDocument_AmlDocRevokedDate` | TField |  | Date on which the document has been revoked. The field cannot be updated if the flag &apos;Revoked&apos; is set as &apos;N&apos; or &apos;Unticked&apos;. Multifonds DB Column is AML_DOC_REVOKED_DATE. |
| 26 | `FS.GI.DIST.AML.DOCUMENT.RESERVED10` | `FsGiDistAmlDocument_Reserved10` | TField |  |  |
| 27 | `FS.GI.DIST.AML.DOCUMENT.RESERVED9` | `FsGiDistAmlDocument_Reserved9` | TField |  |  |
| 28 | `FS.GI.DIST.AML.DOCUMENT.RESERVED8` | `FsGiDistAmlDocument_Reserved8` | TField |  |  |
| 29 | `FS.GI.DIST.AML.DOCUMENT.RESERVED7` | `FsGiDistAmlDocument_Reserved7` | TField |  |  |
| 30 | `FS.GI.DIST.AML.DOCUMENT.RESERVED6` | `FsGiDistAmlDocument_Reserved6` | TField |  |  |
| 31 | `FS.GI.DIST.AML.DOCUMENT.RESERVED5` | `FsGiDistAmlDocument_Reserved5` | TField |  |  |
| 32 | `FS.GI.DIST.AML.DOCUMENT.RESERVED4` | `FsGiDistAmlDocument_Reserved4` | TField |  |  |
| 33 | `FS.GI.DIST.AML.DOCUMENT.RESERVED3` | `FsGiDistAmlDocument_Reserved3` | TField |  |  |
| 34 | `FS.GI.DIST.AML.DOCUMENT.RESERVED2` | `FsGiDistAmlDocument_Reserved2` | TField |  |  |
| 35 | `FS.GI.DIST.AML.DOCUMENT.RESERVED1` | `FsGiDistAmlDocument_Reserved1` | TField |  |  |
| 36 | `FS.GI.DIST.AML.DOCUMENT.LOCAL.REF` | `FsGiDistAmlDocument_LocalRef` |  |  |  |
| 37 | `FS.GI.DIST.AML.DOCUMENT.OVERRIDE` | `FsGiDistAmlDocument_Override` |  |  |  |
| 38 | `FS.GI.DIST.AML.DOCUMENT.RECORD.STATUS` | `FsGiDistAmlDocument_RecordStatus` | String |  |  |
| 39 | `FS.GI.DIST.AML.DOCUMENT.CURR.NO` | `FsGiDistAmlDocument_CurrNo` | String |  |  |
| 40 | `FS.GI.DIST.AML.DOCUMENT.INPUTTER` | `FsGiDistAmlDocument_Inputter` |  |  |  |
| 41 | `FS.GI.DIST.AML.DOCUMENT.DATE.TIME` | `FsGiDistAmlDocument_DateTime` |  |  |  |
| 42 | `FS.GI.DIST.AML.DOCUMENT.AUTHORISER` | `FsGiDistAmlDocument_Authoriser` | String |  |  |
| 43 | `FS.GI.DIST.AML.DOCUMENT.CO.CODE` | `FsGiDistAmlDocument_CoCode` | String |  |  |
| 44 | `FS.GI.DIST.AML.DOCUMENT.DEPT.CODE` | `FsGiDistAmlDocument_DeptCode` | String |  |  |
| 45 | `FS.GI.DIST.AML.DOCUMENT.AUDITOR.CODE` | `FsGiDistAmlDocument_AuditorCode` | String |  |  |
| 46 | `FS.GI.DIST.AML.DOCUMENT.AUDIT.DATE.TIME` | `FsGiDistAmlDocument_AuditDateTime` | String |  |  |
