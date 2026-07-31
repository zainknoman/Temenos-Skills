# FS.GI.TXN.ORDER.CONTACT.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER.CONTACT.DETAILS` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.PARENT.REF.ID` | `FsGiTxnOrderContactDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.ORA.ROWID` | `FsGiTxnOrderContactDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.ORDER.ID` | `FsGiTxnOrderContactDetails_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 4 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.AGENT.ID` | `FsGiTxnOrderContactDetails_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.SELECT` | `FsGiTxnOrderContactDetails_Select` | TField |  | Flag when ticked indicates the record as selected. Multifonds DB Column is CSELECT. |
| 6 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.REGISTER.ID` | `FsGiTxnOrderContactDetails_RegisterId` | TField |  | Register internal Id. Multifonds DB Column is NREGISTER. |
| 7 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.ID.TYPE` | `FsGiTxnOrderContactDetails_ContactIdType` | TField |  | Contact List type of the entity. Multifonds DB Column is NCONT_TYPE. |
| 8 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTRACT.ID.LIST` | `FsGiTxnOrderContactDetails_ContractIdList` | TField |  | Contact List Id of the entity. Multifonds DB Column is NCONT_LIST. |
| 9 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.LIST.NAME` | `FsGiTxnOrderContactDetails_ContactListName` | TField |  | Contact list name of the entity. Multifonds DB Column is CONT_LIST_NAME. |
| 10 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.ID` | `FsGiTxnOrderContactDetails_ContactId` | TField |  | Contact ID of the entity. Multifonds DB Column is NCONTACT. |
| 11 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.NAME` | `FsGiTxnOrderContactDetails_ContactName` | TField |  | Contact name. Multifonds DB Column is CONT_NAME. |
| 12 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.FIRST.NAME` | `FsGiTxnOrderContactDetails_ContactFirstName` | TField |  | Contact first name. Multifonds DB Column is CONT_FIRSTNAME. |
| 13 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.COMM.CHANNEL` | `FsGiTxnOrderContactDetails_ContactCommChannel` | TField |  | Communication channel of the contact. Multifonds DB Column is CONT_COMM_CHANNEL. |
| 14 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CONTACT.ADDRESS` | `FsGiTxnOrderContactDetails_ContactAddress` | TField |  | Address of the contact. Multifonds DB Column is CONT_ADDRESS. |
| 15 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED10` | `FsGiTxnOrderContactDetails_Reserved10` | TField |  |  |
| 16 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED9` | `FsGiTxnOrderContactDetails_Reserved9` | TField |  |  |
| 17 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED8` | `FsGiTxnOrderContactDetails_Reserved8` | TField |  |  |
| 18 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED7` | `FsGiTxnOrderContactDetails_Reserved7` | TField |  |  |
| 19 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED6` | `FsGiTxnOrderContactDetails_Reserved6` | TField |  |  |
| 20 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED5` | `FsGiTxnOrderContactDetails_Reserved5` | TField |  |  |
| 21 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED4` | `FsGiTxnOrderContactDetails_Reserved4` | TField |  |  |
| 22 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED3` | `FsGiTxnOrderContactDetails_Reserved3` | TField |  |  |
| 23 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED2` | `FsGiTxnOrderContactDetails_Reserved2` | TField |  |  |
| 24 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RESERVED1` | `FsGiTxnOrderContactDetails_Reserved1` | TField |  |  |
| 25 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.LOCAL.REF` | `FsGiTxnOrderContactDetails_LocalRef` |  |  |  |
| 26 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.OVERRIDE` | `FsGiTxnOrderContactDetails_Override` |  |  |  |
| 27 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.RECORD.STATUS` | `FsGiTxnOrderContactDetails_RecordStatus` | String |  |  |
| 28 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CURR.NO` | `FsGiTxnOrderContactDetails_CurrNo` | String |  |  |
| 29 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.INPUTTER` | `FsGiTxnOrderContactDetails_Inputter` |  |  |  |
| 30 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.DATE.TIME` | `FsGiTxnOrderContactDetails_DateTime` |  |  |  |
| 31 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.AUTHORISER` | `FsGiTxnOrderContactDetails_Authoriser` | String |  |  |
| 32 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.CO.CODE` | `FsGiTxnOrderContactDetails_CoCode` | String |  |  |
| 33 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.DEPT.CODE` | `FsGiTxnOrderContactDetails_DeptCode` | String |  |  |
| 34 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.AUDITOR.CODE` | `FsGiTxnOrderContactDetails_AuditorCode` | String |  |  |
| 35 | `FS.GI.TXN.ORDER.CONTACT.DETAILS.AUDIT.DATE.TIME` | `FsGiTxnOrderContactDetails_AuditDateTime` | String |  |  |
