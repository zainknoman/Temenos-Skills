# GENERIC.ACCOUNTING.REQUEST — Table Schema

> Source: `INSERTS/I_F.GENERIC.ACCOUNTING.REQUEST` in `ACCCSM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GAR.REQUEST.TYPE` | `GenericAccountingRequest_RequestType` | TField | Yes | This indicates the Request type. Validation Rule: This is an mandatory options field with the value of 'Null' and 'REVERSE'. By default the value 'REVERSE' will get defaulted. |
| 2 | `GAR.ORIGINAL.TXN.ID` | `GenericAccountingRequest_OriginalTxnId` | TField | Yes | This will be the id of a Clearing Transaction and will represent the id of a Clearing Transaction which must be reversed. The system will validate the AC.INWARD.ENTRY record of the original Clearing Transaction exists and its status is Success. Validation Rule: This is a mandatory field with the maximum length of '75'. The value for this field must be proper AC.INWARD.ENTRY record id with the 'Request Type' ->'BOOK' and the 'Result'-> 'SUCCESS'. |
| 3 | `GAR.CONTRA.TXN.CODE` | `GenericAccountingRequest_ContraTxnCode` | TField |  | The transaction code which should be used for reversal contra entry. Validation Rule: The value for this field is a valid record from 'TRANSACTION' table. If not defined by default CONTRA.DR.TXN/CONTRA.CR.TXN will get considered from AC.ENTRY.PARAM. |
| 4 | `GAR.REASON.CODE` | `GenericAccountingRequest_ReasonCode` | TField |  | This will be a reason code explaining why the original transaction is reversed. Validation Rule: This is a LOOKUP field . The values for this field will get fetched via the EB.LOOKUP > 'GENERIC.ACCOUNTING.REQUEST*XXX' where 'XXX' is options. |
| 5 | `GAR.USER.NOTE` | `GenericAccountingRequest_UserNote` |  |  |  |
| 6 | `GAR.REQUEST.STATUS` | `GenericAccountingRequest_RequestStatus` | TField |  | Will indicate as 'suspended' and will be populated once the reversal request message is processed. Validation Rule: This is a no-input field. |
| 7 | `GAR.CREATION.DATE` | `GenericAccountingRequest_CreationDate` | TField |  |  |
| 8 | `GAR.RESERVED.20` | `GenericAccountingRequest_Reserved20` |  |  |  |
| 9 | `GAR.RESERVED.19` | `GenericAccountingRequest_Reserved19` |  |  |  |
| 10 | `GAR.RESERVED.18` | `GenericAccountingRequest_Reserved18` | TField |  |  |
| 11 | `GAR.RESERVED.17` | `GenericAccountingRequest_Reserved17` | TField |  |  |
| 12 | `GAR.RESERVED.16` | `GenericAccountingRequest_Reserved16` | TField |  |  |
| 13 | `GAR.RESERVED.15` | `GenericAccountingRequest_Reserved15` | TField |  |  |
| 14 | `GAR.RESERVED.14` | `GenericAccountingRequest_Reserved14` | TField |  |  |
| 15 | `GAR.RESERVED.13` | `GenericAccountingRequest_Reserved13` | TField |  |  |
| 16 | `GAR.RESERVED.12` | `GenericAccountingRequest_Reserved12` | TField |  |  |
| 17 | `GAR.RESERVED.11` | `GenericAccountingRequest_Reserved11` | TField |  |  |
| 18 | `GAR.RESERVED.10` | `GenericAccountingRequest_Reserved10` | TField |  |  |
| 19 | `GAR.RESERVED.9` | `GenericAccountingRequest_Reserved9` | TField |  |  |
| 20 | `GAR.RESERVED.8` | `GenericAccountingRequest_Reserved8` | TField |  |  |
| 21 | `GAR.RESERVED.7` | `GenericAccountingRequest_Reserved7` | TField |  |  |
| 22 | `GAR.RESERVED.6` | `GenericAccountingRequest_Reserved6` | TField |  |  |
| 23 | `GAR.RESERVED.5` | `GenericAccountingRequest_Reserved5` | TField |  |  |
| 24 | `GAR.RESERVED.4` | `GenericAccountingRequest_Reserved4` | TField |  |  |
| 25 | `GAR.RESERVED.3` | `GenericAccountingRequest_Reserved3` | TField |  |  |
| 26 | `GAR.RESERVED.2` | `GenericAccountingRequest_Reserved2` | TField |  |  |
| 27 | `GAR.RESERVED.1` | `GenericAccountingRequest_Reserved1` | TField |  |  |
| 28 | `GAR.LOCAL.REF` | `GenericAccountingRequest_LocalRef` |  |  |  |
| 29 | `GAR.OVERRIDE` | `GenericAccountingRequest_Override` |  |  |  |
| 30 | `GAR.RECORD.STATUS` | `GenericAccountingRequest_RecordStatus` | String |  |  |
| 31 | `GAR.CURR.NO` | `GenericAccountingRequest_CurrNo` | String |  |  |
| 32 | `GAR.INPUTTER` | `GenericAccountingRequest_Inputter` |  |  |  |
| 33 | `GAR.DATE.TIME` | `GenericAccountingRequest_DateTime` |  |  |  |
| 34 | `GAR.AUTHORISER` | `GenericAccountingRequest_Authoriser` | String |  |  |
| 35 | `GAR.CO.CODE` | `GenericAccountingRequest_CoCode` | String |  |  |
| 36 | `GAR.DEPT.CODE` | `GenericAccountingRequest_DeptCode` | String |  |  |
| 37 | `GAR.AUDITOR.CODE` | `GenericAccountingRequest_AuditorCode` | String |  |  |
| 38 | `GAR.AUDIT.DATE.TIME` | `GenericAccountingRequest_AuditDateTime` | String |  |  |
