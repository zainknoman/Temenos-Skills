# FS.GI.APP.DOC.COPY — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.DOC.COPY` in `FS_Address.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.DOC.COPY.PARENT.REF.ID` | `FsGiAppDocCopy_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.DOC.COPY.ORA.ROWID` | `FsGiAppDocCopy_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.DOC.COPY.PARENT.ID.TYPE` | `FsGiAppDocCopy_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is ID_TYPE. |
| 4 | `FS.GI.APP.DOC.COPY.PARENT.ID` | `FsGiAppDocCopy_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID. |
| 5 | `FS.GI.APP.DOC.COPY.FUND.ID` | `FsGiAppDocCopy_FundId` | TField |  | Fund is in scope for the document type Multifonds DB Column is MULTIFONDS_ID. |
| 6 | `FS.GI.APP.DOC.COPY.SHARE.CLASS.CODE` | `FsGiAppDocCopy_ShareClassCode` | TField |  | Fund share class is in scope for the document type Multifonds DB Column is TPART. |
| 7 | `FS.GI.APP.DOC.COPY.DOCUMENT.TYPE` | `FsGiAppDocCopy_DocumentType` | TField |  | Type of the document linked to the address. Multifonds DB Column is DOC_TYPE. |
| 8 | `FS.GI.APP.DOC.COPY.AGENT.COPY.FLAG` | `FsGiAppDocCopy_AgentCopyFlag` | TField |  | It specify a copy of the investor report to be send to the linked agent. Multifonds DB Column is FLG_AGENT_COPY. |
| 9 | `FS.GI.APP.DOC.COPY.PHYSICAL.ADDRESS.NUMBER` | `FsGiAppDocCopy_PhysicalAddressNumber` | TField |  | Physical Address Number with which this document copy is associated Multifonds DB Column is CADRESSE. |
| 10 | `FS.GI.APP.DOC.COPY.ADDRESS.TYPE.DOC` | `FsGiAppDocCopy_AddressTypeDoc` | TField |  | Physical Address Type linked to the document. Multifonds DB Column is ADR_TYPE. |
| 11 | `FS.GI.APP.DOC.COPY.ELECTRONIC.ADDRESS.NUMBER` | `FsGiAppDocCopy_ElectronicAddressNumber` | TField |  | Electronic address number linked to the document. Multifonds DB Column is NADRESSE. |
| 12 | `FS.GI.APP.DOC.COPY.ELECT.ADDRESS.TYPE` | `FsGiAppDocCopy_ElectAddressType` | TField |  | Electronic address type linked to the document. Multifonds DB Column is ELEC_TYPE_ADR. |
| 13 | `FS.GI.APP.DOC.COPY.MODIFIED.FLAG` | `FsGiAppDocCopy_ModifiedFlag` | TField |  | It specify the modification in document links to the Address Multifonds DB Column is FLG_MODIF. |
| 14 | `FS.GI.APP.DOC.COPY.PENDING.DOCUMENT.FLAG` | `FsGiAppDocCopy_PendingDocumentFlag` | TField |  | Document pending flag. Only for technical use when the record is in pending mode. Multifonds DB Column is PND_COPY. |
| 15 | `FS.GI.APP.DOC.COPY.DOC.INTERNAL.ID` | `FsGiAppDocCopy_DocInternalId` | TField |  | Unique internal document copy identifier. Multifonds DB Column is INTERNAL_ID. |
| 16 | `FS.GI.APP.DOC.COPY.CLASS.CURRENCY` | `FsGiAppDocCopy_ClassCurrency` | TField |  | Fund Share Class Currency Multifonds DB Column is CLASS_CURRENCY. |
| 17 | `FS.GI.APP.DOC.COPY.TA.FUND.ID` | `FsGiAppDocCopy_TaFundId` | TField |  | TA Fund is an Internal ID with combination of Fund ID and Class Currency. Multifonds DB Column is NPTF. |
| 18 | `FS.GI.APP.DOC.COPY.RESERVED10` | `FsGiAppDocCopy_Reserved10` | TField |  |  |
| 19 | `FS.GI.APP.DOC.COPY.RESERVED9` | `FsGiAppDocCopy_Reserved9` | TField |  |  |
| 20 | `FS.GI.APP.DOC.COPY.RESERVED8` | `FsGiAppDocCopy_Reserved8` | TField |  |  |
| 21 | `FS.GI.APP.DOC.COPY.RESERVED7` | `FsGiAppDocCopy_Reserved7` | TField |  |  |
| 22 | `FS.GI.APP.DOC.COPY.RESERVED6` | `FsGiAppDocCopy_Reserved6` | TField |  |  |
| 23 | `FS.GI.APP.DOC.COPY.RESERVED5` | `FsGiAppDocCopy_Reserved5` | TField |  |  |
| 24 | `FS.GI.APP.DOC.COPY.RESERVED4` | `FsGiAppDocCopy_Reserved4` | TField |  |  |
| 25 | `FS.GI.APP.DOC.COPY.RESERVED3` | `FsGiAppDocCopy_Reserved3` | TField |  |  |
| 26 | `FS.GI.APP.DOC.COPY.RESERVED2` | `FsGiAppDocCopy_Reserved2` | TField |  |  |
| 27 | `FS.GI.APP.DOC.COPY.RESERVED1` | `FsGiAppDocCopy_Reserved1` | TField |  |  |
| 28 | `FS.GI.APP.DOC.COPY.LOCAL.REF` | `FsGiAppDocCopy_LocalRef` |  |  |  |
| 29 | `FS.GI.APP.DOC.COPY.OVERRIDE` | `FsGiAppDocCopy_Override` |  |  |  |
| 30 | `FS.GI.APP.DOC.COPY.RECORD.STATUS` | `FsGiAppDocCopy_RecordStatus` | String |  |  |
| 31 | `FS.GI.APP.DOC.COPY.CURR.NO` | `FsGiAppDocCopy_CurrNo` | String |  |  |
| 32 | `FS.GI.APP.DOC.COPY.INPUTTER` | `FsGiAppDocCopy_Inputter` |  |  |  |
| 33 | `FS.GI.APP.DOC.COPY.DATE.TIME` | `FsGiAppDocCopy_DateTime` |  |  |  |
| 34 | `FS.GI.APP.DOC.COPY.AUTHORISER` | `FsGiAppDocCopy_Authoriser` | String |  |  |
| 35 | `FS.GI.APP.DOC.COPY.CO.CODE` | `FsGiAppDocCopy_CoCode` | String |  |  |
| 36 | `FS.GI.APP.DOC.COPY.DEPT.CODE` | `FsGiAppDocCopy_DeptCode` | String |  |  |
| 37 | `FS.GI.APP.DOC.COPY.AUDITOR.CODE` | `FsGiAppDocCopy_AuditorCode` | String |  |  |
| 38 | `FS.GI.APP.DOC.COPY.AUDIT.DATE.TIME` | `FsGiAppDocCopy_AuditDateTime` | String |  |  |
