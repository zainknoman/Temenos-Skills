# PPADBR.RECURRENCE.REGISTRATION — Table Schema

> Source: `INSERTS/I_F.PPADBR.RECURRENCE.REGISTRATION` in `PPADBR_DebinRegistration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RR.RECURRENCE.ID` | `PpadbrRecurrenceRegistration_RecurrenceId` | TField |  | Field to store the Recurrence ID which we receive from COELSA |
| 2 | `RR.SELLER.LEGAL.DOC.NO` | `PpadbrRecurrenceRegistration_SellerLegalDocNo` | TField |  | Document reference of the DEBIN participant,SELLER CUIT |
| 3 | `RR.BUYER.LEGAL.DOC.NO` | `PpadbrRecurrenceRegistration_BuyerLegalDocNo` | TField |  | Document reference of the DEBIN participant,BUYER CUIT |
| 4 | `RR.BUYER.CBU.ACCOUNT.NUMBER` | `PpadbrRecurrenceRegistration_BuyerCbuAccountNumber` | TField | Yes | CBU number of the DEBIN participant. Mandatory input |
| 5 | `RR.SELLER.RUBRO` | `PpadbrRecurrenceRegistration_SellerRubro` | TField |  |  |
| 6 | `RR.SELLER.NAME` | `PpadbrRecurrenceRegistration_SellerName` | TField |  | Name of the Seller registered to DEBIN service |
| 7 | `RR.CURRENCY` | `PpadbrRecurrenceRegistration_Currency` | TField |  | Currency should be either ARS or USD |
| 8 | `RR.DETAILS` | `PpadbrRecurrenceRegistration_Details` | TField |  | Text to show to the buyer as description of the request |
| 9 | `RR.CONCEPT.OF.RECURRENCE` | `PpadbrRecurrenceRegistration_ConceptOfRecurrence` | TField |  | Concept for which the request is generated |
| 10 | `RR.BENEFIT` | `PpadbrRecurrenceRegistration_Benefit` | TField |  | Name of the Benefit It must exist within the benefits charged by the seller. |
| 11 | `RR.REFERENCE.VALUE` | `PpadbrRecurrenceRegistration_ReferenceValue` | TField |  | Reference Value associated with the service Indicates a relationship with a particular buyer |
| 12 | `RR.ACTION` | `PpadbrRecurrenceRegistration_Action` | TField |  | Dropdown values:True (Opt in) and False (Drop out) For opt-in - Value should be true For drop-out - Value should be false |
| 13 | `RR.ADHESION.TYPE` | `PpadbrRecurrenceRegistration_AdhesionType` | TField |  | Dropdown values:0 and 1 '0' Means a regular drop-out '1' Means a definitive drop-out. |
| 14 | `RR.RECURRENCE.STATUS` | `PpadbrRecurrenceRegistration_RecurrenceStatus` | TField |  | Not allowed for User input Dropdown Values�:Active, Inactive,Rejected Active - on receiving ACK for opt-in Inactive - on receiving ACK for drop out Rejected - on receiving error response code for opt-in and drop out |
| 15 | `RR.CLEARING.PARTY.REFERENCE` | `PpadbrRecurrenceRegistration_ClearingPartyReference` | TField |  | Document reference of the DEBIN participant Not allowed for User input |
| 16 | `RR.STATUS.DATE` | `PpadbrRecurrenceRegistration_StatusDate` | TField |  | The date of the respective status update is available in this field Not allowed for User input |
| 17 | `RR.RESPONSE.CODE` | `PpadbrRecurrenceRegistration_ResponseCode` | TField |  | Response code from clearing house (COELSA) is updated in this field using API. Noinput field for the user |
| 18 | `RR.RESPONSE.DESCRIPTION` | `PpadbrRecurrenceRegistration_ResponseDescription` | TField |  |  |
| 19 | `RR.ROLE` | `PpadbrRecurrenceRegistration_Role` | TField |  |  |
| 20 | `RR.RESERVED.9` | `PpadbrRecurrenceRegistration_Reserved9` | TField |  |  |
| 21 | `RR.RESERVED.8` | `PpadbrRecurrenceRegistration_Reserved8` | TField |  |  |
| 22 | `RR.RESERVED.7` | `PpadbrRecurrenceRegistration_Reserved7` | TField |  |  |
| 23 | `RR.RESERVED.6` | `PpadbrRecurrenceRegistration_Reserved6` | TField |  |  |
| 24 | `RR.RESERVED.5` | `PpadbrRecurrenceRegistration_Reserved5` | TField |  |  |
| 25 | `RR.RESERVED.4` | `PpadbrRecurrenceRegistration_Reserved4` | TField |  |  |
| 26 | `RR.RESERVED.3` | `PpadbrRecurrenceRegistration_Reserved3` | TField |  |  |
| 27 | `RR.RESERVED.2` | `PpadbrRecurrenceRegistration_Reserved2` | TField |  |  |
| 28 | `RR.RESERVED.1` | `PpadbrRecurrenceRegistration_Reserved1` | TField |  |  |
| 29 | `RR.LOCAL.REF` | `PpadbrRecurrenceRegistration_LocalRef` |  |  |  |
| 30 | `RR.OVERRIDE` | `PpadbrRecurrenceRegistration_Override` |  |  |  |
| 31 | `RR.RECORD.STATUS` | `PpadbrRecurrenceRegistration_RecordStatus` | String |  |  |
| 32 | `RR.CURR.NO` | `PpadbrRecurrenceRegistration_CurrNo` | String |  |  |
| 33 | `RR.INPUTTER` | `PpadbrRecurrenceRegistration_Inputter` |  |  |  |
| 34 | `RR.DATE.TIME` | `PpadbrRecurrenceRegistration_DateTime` |  |  |  |
| 35 | `RR.AUTHORISER` | `PpadbrRecurrenceRegistration_Authoriser` | String |  |  |
| 36 | `RR.CO.CODE` | `PpadbrRecurrenceRegistration_CoCode` | String |  |  |
| 37 | `RR.DEPT.CODE` | `PpadbrRecurrenceRegistration_DeptCode` | String |  |  |
| 38 | `RR.AUDITOR.CODE` | `PpadbrRecurrenceRegistration_AuditorCode` | String |  |  |
| 39 | `RR.AUDIT.DATE.TIME` | `PpadbrRecurrenceRegistration_AuditDateTime` | String |  |  |
