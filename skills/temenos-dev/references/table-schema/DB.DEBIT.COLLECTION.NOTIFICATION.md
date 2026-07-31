# DB.DEBIT.COLLECTION.NOTIFICATION — Table Schema

> Source: `INSERTS/I_F.DB.DEBIT.COLLECTION.NOTIFICATION` in `DB_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DB.DCN.FILE.MSG.ID` | `DbDebitCollectionNotification_FileMsgId` | TField |  |  |
| 2 | `DB.DCN.BULK.FILE.ID` | `DbDebitCollectionNotification_BulkFileId` | TField |  |  |
| 3 | `DB.DCN.DEBIT.COLLECTION.ORDER.ID` | `DbDebitCollectionNotification_DebitCollectionOrderId` | TField |  |  |
| 4 | `DB.DCN.COLLECTION.COMPLETE` | `DbDebitCollectionNotification_CollectionComplete` | TField |  |  |
| 5 | `DB.DCN.COLLECTION.SYSTEM.STATUS` | `DbDebitCollectionNotification_CollectionSystemStatus` | TField |  |  |
| 6 | `DB.DCN.STATUS.REASON.CODE` | `DbDebitCollectionNotification_StatusReasonCode` | TField |  |  |
| 7 | `DB.DCN.COLLECTION.SYSTEM.ID` | `DbDebitCollectionNotification_CollectionSystemId` | TField |  |  |
| 8 | `DB.DCN.COLLECTION.SYSTEM.RESPONSE.ID` | `DbDebitCollectionNotification_CollectionSystemResponseId` | TField |  |  |
| 9 | `DB.DCN.COLLECTION.STATUS.ADD.INFO` | `DbDebitCollectionNotification_CollectionStatusAddInfo` | TField |  |  |
| 10 | `DB.DCN.RESPONSE.ORIGINATOR` | `DbDebitCollectionNotification_ResponseOriginator` | TField |  |  |
| 11 | `DB.DCN.CREATED.BY` | `DbDebitCollectionNotification_CreatedBy` | TField |  |  |
| 12 | `DB.DCN.STATUS` | `DbDebitCollectionNotification_Status` | TField |  |  |
| 13 | `DB.DCN.CONTEXT.NAME` | `DbDebitCollectionNotification_ContextName` |  |  |  |
| 14 | `DB.DCN.CONTEXT.VALUE` | `DbDebitCollectionNotification_ContextValue` |  |  |  |
| 15 | `DB.DCN.CREATION.DATE` | `DbDebitCollectionNotification_CreationDate` | TField |  |  |
| 16 | `DB.DCN.RESERVED.20` | `DbDebitCollectionNotification_Reserved20` | TField |  |  |
| 17 | `DB.DCN.RESERVED.19` | `DbDebitCollectionNotification_Reserved19` | TField |  |  |
| 18 | `DB.DCN.RESERVED.18` | `DbDebitCollectionNotification_Reserved18` | TField |  |  |
| 19 | `DB.DCN.RESERVED.17` | `DbDebitCollectionNotification_Reserved17` | TField |  |  |
| 20 | `DB.DCN.RESERVED.16` | `DbDebitCollectionNotification_Reserved16` | TField |  |  |
| 21 | `DB.DCN.RESERVED.15` | `DbDebitCollectionNotification_Reserved15` | TField |  |  |
| 22 | `DB.DCN.RESERVED.14` | `DbDebitCollectionNotification_Reserved14` | TField |  |  |
| 23 | `DB.DCN.RESERVED.13` | `DbDebitCollectionNotification_Reserved13` | TField |  |  |
| 24 | `DB.DCN.RESERVED.12` | `DbDebitCollectionNotification_Reserved12` | TField |  |  |
| 25 | `DB.DCN.RESERVED.11` | `DbDebitCollectionNotification_Reserved11` | TField |  |  |
| 26 | `DB.DCN.RESERVED.10` | `DbDebitCollectionNotification_Reserved10` | TField |  |  |
| 27 | `DB.DCN.RESERVED.9` | `DbDebitCollectionNotification_Reserved9` | TField |  |  |
| 28 | `DB.DCN.RESERVED.8` | `DbDebitCollectionNotification_Reserved8` | TField |  |  |
| 29 | `DB.DCN.RESERVED.7` | `DbDebitCollectionNotification_Reserved7` | TField |  |  |
| 30 | `DB.DCN.RESERVED.6` | `DbDebitCollectionNotification_Reserved6` | TField |  |  |
| 31 | `DB.DCN.RESERVED.5` | `DbDebitCollectionNotification_Reserved5` | TField |  |  |
| 32 | `DB.DCN.RESERVED.4` | `DbDebitCollectionNotification_Reserved4` | TField |  |  |
| 33 | `DB.DCN.RESERVED.3` | `DbDebitCollectionNotification_Reserved3` | TField |  |  |
| 34 | `DB.DCN.RESERVED.2` | `DbDebitCollectionNotification_Reserved2` | TField |  |  |
| 35 | `DB.DCN.RESERVED.1` | `DbDebitCollectionNotification_Reserved1` | TField |  |  |
| 36 | `DB.DCN.LOCAL.REF` | `DbDebitCollectionNotification_LocalRef` |  |  |  |
| 37 | `DB.DCN.OVERRIDE` | `DbDebitCollectionNotification_Override` |  |  |  |
| 38 | `DB.DCN.RECORD.STATUS` | `DbDebitCollectionNotification_RecordStatus` | String |  |  |
| 39 | `DB.DCN.CURR.NO` | `DbDebitCollectionNotification_CurrNo` | String |  |  |
| 40 | `DB.DCN.INPUTTER` | `DbDebitCollectionNotification_Inputter` |  |  |  |
| 41 | `DB.DCN.DATE.TIME` | `DbDebitCollectionNotification_DateTime` |  |  |  |
| 42 | `DB.DCN.AUTHORISER` | `DbDebitCollectionNotification_Authoriser` | String |  |  |
| 43 | `DB.DCN.CO.CODE` | `DbDebitCollectionNotification_CoCode` | String |  |  |
| 44 | `DB.DCN.DEPT.CODE` | `DbDebitCollectionNotification_DeptCode` | String |  |  |
| 45 | `DB.DCN.AUDITOR.CODE` | `DbDebitCollectionNotification_AuditorCode` | String |  |  |
| 46 | `DB.DCN.AUDIT.DATE.TIME` | `DbDebitCollectionNotification_AuditDateTime` | String |  |  |
