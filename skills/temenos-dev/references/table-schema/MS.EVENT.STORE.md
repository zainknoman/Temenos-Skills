# MS.EVENT.STORE — Table Schema

> Source: `INSERTS/I_F.MS.EVENT.STORE` in `EB_MicroService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.ES.DESCRIPTION` | `MsEventStore_Description` |  |  |  |
| 2 | `MS.ES.PARENT.APPLICATION` | `MsEventStore_ParentApplication` | TField |  | Parent application name for events were triggered into SO. |
| 3 | `MS.ES.PARENT.TXN.ID` | `MsEventStore_ParentTxnId` | TField |  | Parent application reference ID for events were triggered into SO. |
| 4 | `MS.ES.PARENT.FUNCTION` | `MsEventStore_ParentFunction` | TField |  | Function performed in the Parent Transaction |
| 5 | `MS.ES.TXN.USER` | `MsEventStore_TxnUser` | TField |  | User ID who has created the Parent Transaction |
| 6 | `MS.ES.COMPANY` | `MsEventStore_Company` | TField |  | Company of Parent Transaction |
| 7 | `MS.ES.SO.EVENT.RESPONSE` | `MsEventStore_SoEventResponse` | TField |  | Future Use |
| 8 | `MS.ES.OVERALL.STATUS` | `MsEventStore_OverallStatus` | TField |  | Pending , Success, Failed, To be setup in EB.LOOKUP, MS.TRANSACT.STAGE Pending - Once the transaction is committed in T24, the status of the field would be Pending. Success - Once the events are processed by MS, SO sends a success response. |
| 9 | `MS.ES.COMPENSATORY.TRANSACT.STATUS` | `MsEventStore_CompensatoryTransactStatus` | TField |  | Holds the status of the Compensatory transaction status, SUCCESS/FAILED. SUCCESS - 1. When no compensatory OFS request. 2. When the compensatory OFS request processed successfully by OFS.MESSAGE.SERVICE. FAILED - When compensatory OFS request processed unsuccessfully by OFS.MESSAGE.SERVICE. |
| 10 | `MS.ES.VARIABLE.NAME` | `MsEventStore_VariableName` |  |  |  |
| 11 | `MS.ES.VARIABLE.VALUE` | `MsEventStore_VariableValue` |  |  |  |
| 12 | `MS.ES.RESERVED.20` | `MsEventStore_Reserved20` |  |  |  |
| 13 | `MS.ES.RESERVED.19` | `MsEventStore_Reserved19` |  |  |  |
| 14 | `MS.ES.RESERVED.18` | `MsEventStore_Reserved18` |  |  |  |
| 15 | `MS.ES.RESERVED.17` | `MsEventStore_Reserved17` |  |  |  |
| 16 | `MS.ES.RESERVED.16` | `MsEventStore_Reserved16` |  |  |  |
| 17 | `MS.ES.RESERVED.15` | `MsEventStore_Reserved15` | TField |  | Reserved Field |
| 18 | `MS.ES.RESERVED.14` | `MsEventStore_Reserved14` | TField |  | Reserved Field |
| 19 | `MS.ES.RESERVED.13` | `MsEventStore_Reserved13` | TField |  | Reserved Field |
| 20 | `MS.ES.RESERVED.12` | `MsEventStore_Reserved12` | TField |  | Reserved Field |
| 21 | `MS.ES.RESERVED.11` | `MsEventStore_Reserved11` | TField |  | Reserved Field |
| 22 | `MS.ES.RESERVED.10` | `MsEventStore_Reserved10` | TField |  | Reserved Field |
| 23 | `MS.ES.RESERVED.9` | `MsEventStore_Reserved9` | TField |  | Reserved Field |
| 24 | `MS.ES.RESERVED.8` | `MsEventStore_Reserved8` | TField |  | Reserved Field |
| 25 | `MS.ES.RESERVED.7` | `MsEventStore_Reserved7` | TField |  | Reserved Field |
| 26 | `MS.ES.RESERVED.6` | `MsEventStore_Reserved6` | TField |  | Reserved Field |
| 27 | `MS.ES.RESERVED.5` | `MsEventStore_Reserved5` | TField |  | Reserved Field |
| 28 | `MS.ES.RESERVED.4` | `MsEventStore_Reserved4` | TField |  | Reserved Field |
| 29 | `MS.ES.RESERVED.3` | `MsEventStore_Reserved3` | TField |  | Reserved Field |
| 30 | `MS.ES.RESERVED.2` | `MsEventStore_Reserved2` | TField |  | Reserved Field |
| 31 | `MS.ES.RESERVED.1` | `MsEventStore_Reserved1` | TField |  | Reserved Field |
| 32 | `MS.ES.LOCAL.REF` | `MsEventStore_LocalRef` |  |  |  |
| 33 | `MS.ES.OVERRIDE` | `MsEventStore_Override` |  |  |  |
| 34 | `MS.ES.RECORD.STATUS` | `MsEventStore_RecordStatus` | String |  |  |
| 35 | `MS.ES.CURR.NO` | `MsEventStore_CurrNo` | String |  |  |
| 36 | `MS.ES.INPUTTER` | `MsEventStore_Inputter` |  |  |  |
| 37 | `MS.ES.DATE.TIME` | `MsEventStore_DateTime` |  |  |  |
| 38 | `MS.ES.AUTHORISER` | `MsEventStore_Authoriser` | String |  |  |
| 39 | `MS.ES.CO.CODE` | `MsEventStore_CoCode` | String |  |  |
| 40 | `MS.ES.DEPT.CODE` | `MsEventStore_DeptCode` | String |  |  |
| 41 | `MS.ES.AUDITOR.CODE` | `MsEventStore_AuditorCode` | String |  |  |
| 42 | `MS.ES.AUDIT.DATE.TIME` | `MsEventStore_AuditDateTime` | String |  |  |
