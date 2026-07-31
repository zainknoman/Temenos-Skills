# CZ.CDP.REQUEST.TYPE — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.REQUEST.TYPE` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CRT.DESCRIPTION` | `CzCdpRequestType_Description` |  |  |  |
| 2 | `CZ.CRT.REQUEST.TYPE` | `CzCdpRequestType_RequestType` | TField | Yes | Field to capture the Right that the data subject wants to excercise. Validation Rules: 1.Mandatory field 2.Values allowed are SAR, OBJECT, ERASURE, PORTABILITY, RESTRICTION, RECTIFICATION |
| 3 | `CZ.CRT.EXPIRY.DAYS` | `CzCdpRequestType_ExpiryDays` | TField | Yes | No of days to complete the request To be input manually and the value defined here will be considered to calculate the expiry date automatically in the CDP.REQUEST.CAPTURE Validation Rules:1. Values allowed are 1-999 2. Not allowed for erasure 3. Mandatory for Request Type other than Erasure |
| 4 | `CZ.CRT.INCLUDE.HISTORY` | `CzCdpRequestType_IncludeHistory` | TField |  | Field that denotes whether or not history records need to be included in the processing. This is allowed only for SAR and Data Portability request types. Validation Rules: 1. Values allowed are YES or NO 2. If none specificed (Null), then it is considered to be equivalent to NO. |
| 5 | `CZ.CRT.DELINK.PTY.RLN.API` | `CzCdpRequestType_DelinkPtyRlnApi` | TField |  | Contains the hook routine, which will be called during erasure to delink the associated relations corresponding to the partyId and partyApplication from CUSTOMER.RELATIONSHIP and PARTY.RELATIONSHIP records Validation: Should have an EB.API record for the routine mentioned here |
| 6 | `CZ.CRT.RESERVED.09` | `CzCdpRequestType_Reserved09` | TField |  |  |
| 7 | `CZ.CRT.RESERVED.08` | `CzCdpRequestType_Reserved08` | TField |  |  |
| 8 | `CZ.CRT.RESERVED.07` | `CzCdpRequestType_Reserved07` | TField |  |  |
| 9 | `CZ.CRT.RESERVED.06` | `CzCdpRequestType_Reserved06` | TField |  |  |
| 10 | `CZ.CRT.RESERVED.05` | `CzCdpRequestType_Reserved05` | TField |  |  |
| 11 | `CZ.CRT.RESERVED.04` | `CzCdpRequestType_Reserved04` | TField |  |  |
| 12 | `CZ.CRT.RESERVED.03` | `CzCdpRequestType_Reserved03` | TField |  |  |
| 13 | `CZ.CRT.RESERVED.02` | `CzCdpRequestType_Reserved02` | TField |  |  |
| 14 | `CZ.CRT.RESERVED.01` | `CzCdpRequestType_Reserved01` | TField |  |  |
| 15 | `CZ.CRT.RECORD.STATUS` | `CzCdpRequestType_RecordStatus` | String |  |  |
| 16 | `CZ.CRT.CURR.NO` | `CzCdpRequestType_CurrNo` | String |  |  |
| 17 | `CZ.CRT.INPUTTER` | `CzCdpRequestType_Inputter` |  |  |  |
| 18 | `CZ.CRT.DATE.TIME` | `CzCdpRequestType_DateTime` |  |  |  |
| 19 | `CZ.CRT.AUTHORISER` | `CzCdpRequestType_Authoriser` | String |  |  |
| 20 | `CZ.CRT.CO.CODE` | `CzCdpRequestType_CoCode` | String |  |  |
| 21 | `CZ.CRT.DEPT.CODE` | `CzCdpRequestType_DeptCode` | String |  |  |
| 22 | `CZ.CRT.AUDITOR.CODE` | `CzCdpRequestType_AuditorCode` | String |  |  |
| 23 | `CZ.CRT.AUDIT.DATE.TIME` | `CzCdpRequestType_AuditDateTime` | String |  |  |
