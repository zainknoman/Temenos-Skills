# CZ.CDP.REQUEST.CAPTURE — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.REQUEST.CAPTURE` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CDRC.PARTY.ID` | `CzCdpRequestCapture_PartyId` | TField | Yes | Valid Id to the application mentioned in PARTY.APPLICATION field mandatory field Validation Rules: Should have a valid entry in the application mentioned in PARTY.APPLICATION field |
| 2 | `CZ.CDRC.PARTY.APPLICATION` | `CzCdpRequestCapture_PartyApplication` | TField | Yes | Defines the party application to which the party Id belongs to. The field is defaulted with a value of CUSTOMER. In higher releases where Customer activity and CDP processing functionality enhanced for PERSON.ENTITY as well, the field is allowed input with options CUSTOMER or PERSON.ENTITY. It is mandatory that for a proper processing, user must ensure that this field is set with the appropriate party application relevant to the application being configured |
| 3 | `CZ.CDRC.REQUEST.TYPE` | `CzCdpRequestCapture_RequestType` | TField | Yes | Type of request mandatory field Validation Rules:This Field should contain the Valid Id to CDP.REQUEST.TYPE |
| 4 | `CZ.CDRC.CAPTURE.METHOD` | `CzCdpRequestCapture_CaptureMethod` | TField |  | method of request capture This is a NOINPUT field. This field is populated as MANUAL if captured through the application or �AUTO� if updated by a process The Regulation allows to capture the request mode either by electronic or manual |
| 5 | `CZ.CDRC.DATE.LOGGED` | `CzCdpRequestCapture_DateLogged` | TField |  | Date when the request is logged This is a NOINPUT field. Validation Rules: This field is set to TODAY the first time it is created |
| 6 | `CZ.CDRC.ORG.EXP.DATE` | `CzCdpRequestCapture_OrgExpDate` | TField |  | Original expiry date of the request This is a NOINPUT field. Validation Rules: calculated based on the Request Type entered along with the expiry days as prescribed under GDPR towards compliance |
| 7 | `CZ.CDRC.NEW.EXP.DATE` | `CzCdpRequestCapture_NewExpDate` | TField |  | New expiry date GDPR allows extension of time limits under genuine reasons on the request raised Will be used if Request needs to be extended, and new expiry date input after recording the reason for delay Validation Rules : New expiry date cannot be backdated |
| 8 | `CZ.CDRC.CURR.EXP.DATE` | `CzCdpRequestCapture_CurrExpDate` | TField |  | Current expiry date Validation Rules: 1. Current expiry date will be defaulted with new.exp.date 2. If new.exp.date is empty, the same will be defaulted with org.exp.date |
| 9 | `CZ.CDRC.REQUEST.STATUS` | `CzCdpRequestCapture_RequestStatus` | TField |  | Status of the request captured Validation Rules:1.Valid status from EB.LOOKUP for CDP.REQUEST.STATUS.OPTIONS 2. Values allowed are INITIATED, INPROGESS, EXTENDED, COMPLETED, REJECTED |
| 10 | `CZ.CDRC.CHANNEL` | `CzCdpRequestCapture_Channel` | TField |  | Validation Rules : Should have a valid entry in EB.CHANNEL. |
| 11 | `CZ.CDRC.NEW.OFFICER` | `CzCdpRequestCapture_NewOfficer` | TField |  | Officer in charge of initiating action Validation Rules:1.This Field should contain the Valid Id to DEPT.ACCT.OFFICER 2. Defaulted from CUSTOMER record, if empty |
| 12 | `CZ.CDRC.NEW.ACTION` | `CzCdpRequestCapture_NewAction` | TField |  | Validation Rules:Valid status from EB.LOOKUP for CDP.ACTION.OPTIONS 2. Values allowed are NEW, EXTEND,IN.PROGRESS, COMPLETE, REJECT 3. Made NULL once a history of new action is populated in action |
| 13 | `CZ.CDRC.NEW.ACTION.NOTES` | `CzCdpRequestCapture_NewActionNotes` |  |  |  |
| 14 | `CZ.CDRC.ACTION.DATE` | `CzCdpRequestCapture_ActionDate` |  |  |  |
| 15 | `CZ.CDRC.ACTION.OFFICER` | `CzCdpRequestCapture_ActionOfficer` |  |  |  |
| 16 | `CZ.CDRC.ACTION` | `CzCdpRequestCapture_Action` |  |  |  |
| 17 | `CZ.CDRC.ACTION.NOTES` | `CzCdpRequestCapture_ActionNotes` |  |  |  |
| 18 | `CZ.CDRC.ACTION.RESERVED.05` | `CzCdpRequestCapture_ActionReserved05` |  |  |  |
| 19 | `CZ.CDRC.ACTION.RESERVED.04` | `CzCdpRequestCapture_ActionReserved04` |  |  |  |
| 20 | `CZ.CDRC.ACTION.RESERVED.03` | `CzCdpRequestCapture_ActionReserved03` |  |  |  |
| 21 | `CZ.CDRC.ACTION.RESERVED.02` | `CzCdpRequestCapture_ActionReserved02` |  |  |  |
| 22 | `CZ.CDRC.ACTION.RESERVED.01` | `CzCdpRequestCapture_ActionReserved01` |  |  |  |
| 23 | `CZ.CDRC.REQUEST.COMPLETED` | `CzCdpRequestCapture_RequestCompleted` | TField |  | This field should be set as Y or blank To set the flag to Y if request is completed Validation Rules : 1. Allowed only when system status is completed 2. If set to yes, all other fields are disabled |
| 24 | `CZ.CDRC.APPROVE.REQUEST` | `CzCdpRequestCapture_ApproveRequest` | TField |  | This field should be set as Y or blank To set the flag to Y if request is approved This is a no change field. Once set to yes, cannot be changed. |
| 25 | `CZ.CDRC.DATE.COMPLETED` | `CzCdpRequestCapture_DateCompleted` | TField |  | This is a NOINPUT field Validation Rules : Set to the current date when REQUEST.COMPLETED is set to Y |
| 26 | `CZ.CDRC.DATE.LAST.UPDATED` | `CzCdpRequestCapture_DateLastUpdated` | TField |  | This is a NOINPUT field Validation Rules : Set to today each time record is changed. |
| 27 | `CZ.CDRC.SYSTEM.STATUS` | `CzCdpRequestCapture_SystemStatus` | TField |  | This is a system updated NOINPUT field. The values possible are INITIATED, CANCELLED, ERROR and COMPLETED. It is based on this field that the REQUEST.COMPLETED field is set and other internal processing like resubmission (in case of error) is done. |
| 28 | `CZ.CDRC.INTERNAL.ACTION` | `CzCdpRequestCapture_InternalAction` | TField |  | Field that helps the user to enable internal actions on the requests namely RESUBMIT and CANCEL. Validation Rules: 1. Values allowed are RESUBMIT, CANCEL 2. Cannot be marked as CANCEL once the request is approved or if request is completed. 3. RESUBMIT is allowed only when the SYSTEM.STATUS is marked as ERROR |
| 29 | `CZ.CDRC.PURPOSE` | `CzCdpRequestCapture_Purpose` |  |  |  |
| 30 | `CZ.CDRC.CONTRACT.APPLICATION` | `CzCdpRequestCapture_ContractApplication` | TField |  | This field has application name that is considered for active contract erasure through the request Validation Rules: The field is applicable only when ALLOW.CONTRACT.ERASURE is set to YES in CZ.CDP.PARAMETER This is a NOCHANGE field and updated by system if Contract erasure is tured on and the ERASURE.TRIGGER set up is either AUTO or MANUAL. The field is allowed input for contract erasure when the set up in CZ.CDP.PARAMETER>ERASURE.TRIGGER is NONE. |
| 31 | `CZ.CDRC.CONTRACT.ID` | `CzCdpRequestCapture_ContractId` | TField |  | This field has the contract ID that is considered for active contract erasure through the request. Validation Rules: The field is applicable only when ALLOW.CONTRACT.ERASURE is set to YES in CZ.CDP.PARAMETER This is a NOCHANGE field and updated by system if Contract erasure is turned on and the ERASURE.TRIGGER set up is either AUTO or MANUAL. The field is allowed input for contract erasure when the set up in CZ.CDP.PARAMETER>ERASURE.TRIGGER is NONE. |
| 32 | `CZ.CDRC.CONTRACT.LEAD.COMPANY` | `CzCdpRequestCapture_ContractLeadCompany` | TField |  | This field has the lead company Id of the contract ID that is considered for active contract erasure through the request. Validation Rules: The field is applicable only when ALLOW.CONTRACT.ERASURE is set to YES in CZ.CDP.PARAMETER This is a NOCHANGE field and updated by system if Contract erasure is tured on and the ERASURE.TRIGGER set up is either AUTO or MANUAL. The field is allowed input for contract erasure when the set up in CZ.CDP.PARAMETER>ERASURE.TRIGGER is NONE. |
| 33 | `CZ.CDRC.EXT.SYSTEM` | `CzCdpRequestCapture_ExtSystem` |  |  |  |
| 34 | `CZ.CDRC.EXT.REQUEST.STATUS` | `CzCdpRequestCapture_ExtRequestStatus` |  |  |  |
| 35 | `CZ.CDRC.EXT.PURPOSE` | `CzCdpRequestCapture_ExtPurpose` |  |  |  |
| 36 | `CZ.CDRC.EXT.PURPOSE.STATUS` | `CzCdpRequestCapture_ExtPurposeStatus` |  |  |  |
| 37 | `CZ.CDRC.EXT.EVENT.DATE` | `CzCdpRequestCapture_ExtEventDate` |  |  |  |
| 38 | `CZ.CDRC.EXT.RESERVED.02` | `CzCdpRequestCapture_ExtReserved02` |  |  |  |
| 39 | `CZ.CDRC.EXT.RESERVED.01` | `CzCdpRequestCapture_ExtReserved01` |  |  |  |
| 40 | `CZ.CDRC.LOCAL.REF` | `CzCdpRequestCapture_LocalRef` |  |  |  |
| 41 | `CZ.CDRC.OVERRIDE` | `CzCdpRequestCapture_Override` |  |  |  |
| 42 | `CZ.CDRC.RECORD.STATUS` | `CzCdpRequestCapture_RecordStatus` | String |  |  |
| 43 | `CZ.CDRC.CURR.NO` | `CzCdpRequestCapture_CurrNo` | String |  |  |
| 44 | `CZ.CDRC.INPUTTER` | `CzCdpRequestCapture_Inputter` |  |  |  |
| 45 | `CZ.CDRC.DATE.TIME` | `CzCdpRequestCapture_DateTime` |  |  |  |
| 46 | `CZ.CDRC.AUTHORISER` | `CzCdpRequestCapture_Authoriser` | String |  |  |
| 47 | `CZ.CDRC.CO.CODE` | `CzCdpRequestCapture_CoCode` | String |  |  |
| 48 | `CZ.CDRC.DEPT.CODE` | `CzCdpRequestCapture_DeptCode` | String |  |  |
| 49 | `CZ.CDRC.AUDITOR.CODE` | `CzCdpRequestCapture_AuditorCode` | String |  |  |
| 50 | `CZ.CDRC.AUDIT.DATE.TIME` | `CzCdpRequestCapture_AuditDateTime` | String |  |  |
