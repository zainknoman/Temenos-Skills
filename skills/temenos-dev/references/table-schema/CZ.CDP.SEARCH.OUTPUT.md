# CZ.CDP.SEARCH.OUTPUT — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.SEARCH.OUTPUT` in `CZ_AccessAndPortable.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CSO.PARTY.ID` | `CzCdpSearchOutput_PartyId` | TField |  | The identifier for the customer who has requested his/her financial institution to furnish the personal data details held about him/her with them. Defaulted from ID of this application Validation Rule: Valid T24 Customer and this is a NOINPUT field |
| 2 | `CSO.PARTY.APPL` | `CzCdpSearchOutput_PartyAppl` | TField |  | This field indicates the application to which the party belongs Identifier to indicate the type of relationship the requestor has maintained with the bank. Validation Rule: Valid application name This is a NOINPUT field This is currently supported for CUSTOMER application and so defaulted as "CUSTOMER" |
| 3 | `CSO.REQ.CAP.ID` | `CzCdpSearchOutput_ReqCapId` | TField |  | This field indicates the reference to the Customer's Request placed within Rights management and the resultant of which is being held in this table as a data dump. Defaulted from ID of this application Validation Rule: This is a NOINPUT field |
| 4 | `CSO.REQ.TYPE` | `CzCdpSearchOutput_ReqType` | TField |  | This field indicates the type of request for which the data is being held in this table. The values could be either "SAR"(Subject Access Request) or "PORTABLE"(Portability request) Defaulted from ID of this application Validation Rule: This is a NOINPUT field The allowed request types are â€œSARâ€� or "PORTABLE" |
| 5 | `CSO.APPLICATION.NAME` | `CzCdpSearchOutput_ApplicationName` | TField |  | This field indicates T24 table in relation to the customer ID which was part of the CDP.DATA.DEFINITION search Defaulted from ID of this application Validation Rule: This is a NOINPUT field |
| 6 | `CSO.CREATION.DATE` | `CzCdpSearchOutput_CreationDate` | TField |  | This field indicates the date on which the data was extracted and stored in this table Validation Rule: This is a NOINPUT field |
| 7 | `CSO.COMPANY.ID` | `CzCdpSearchOutput_CompanyId` | TField |  | This field indicates the institution or its branch where the personal data of the customer is held Defaulted from ID of this application Validation Rule: This is a NOINPUT field |
| 8 | `CSO.CONTRACT.ID` | `CzCdpSearchOutput_ContractId` |  |  |  |
| 9 | `CSO.CONTRACT.COMPANY.ID` | `CzCdpSearchOutput_ContractCompanyId` |  |  |  |
| 10 | `CSO.SOURCE.TYPE` | `CzCdpSearchOutput_SourceType` |  |  |  |
| 11 | `CSO.FIELD.NAME` | `CzCdpSearchOutput_FieldName` |  |  |  |
| 12 | `CSO.CONTENT` | `CzCdpSearchOutput_Content` |  |  |  |
| 13 | `CSO.ATTRIBUTE` | `CzCdpSearchOutput_Attribute` |  |  |  |
| 14 | `CSO.PURPOSE` | `CzCdpSearchOutput_Purpose` |  |  |  |
| 15 | `CSO.EXCLUDE` | `CzCdpSearchOutput_Exclude` |  |  |  |
| 16 | `CSO.RESERVED.15` | `CzCdpSearchOutput_Reserved15` |  |  |  |
| 17 | `CSO.RESERVED.14` | `CzCdpSearchOutput_Reserved14` |  |  |  |
| 18 | `CSO.RESERVED.13` | `CzCdpSearchOutput_Reserved13` |  |  |  |
| 19 | `CSO.RESERVED.12` | `CzCdpSearchOutput_Reserved12` |  |  |  |
| 20 | `CSO.RESERVED.11` | `CzCdpSearchOutput_Reserved11` |  |  |  |
| 21 | `CSO.REC.SPLIT` | `CzCdpSearchOutput_RecSplit` | TField |  | This field indicates the number of splits for the master record when the number of contracts is going beyond 150 records Validation Rule: This is a NOINPUT field |
| 22 | `CSO.RESERVED.10` | `CzCdpSearchOutput_Reserved10` | TField |  |  |
| 23 | `CSO.RESERVED.09` | `CzCdpSearchOutput_Reserved09` | TField |  |  |
| 24 | `CSO.RESERVED.08` | `CzCdpSearchOutput_Reserved08` | TField |  |  |
| 25 | `CSO.RESERVED.07` | `CzCdpSearchOutput_Reserved07` | TField |  |  |
| 26 | `CSO.RESERVED.06` | `CzCdpSearchOutput_Reserved06` | TField |  |  |
| 27 | `CSO.RESERVED.05` | `CzCdpSearchOutput_Reserved05` | TField |  |  |
| 28 | `CSO.RESERVED.04` | `CzCdpSearchOutput_Reserved04` | TField |  |  |
| 29 | `CSO.RESERVED.03` | `CzCdpSearchOutput_Reserved03` | TField |  |  |
| 30 | `CSO.RESERVED.02` | `CzCdpSearchOutput_Reserved02` | TField |  |  |
| 31 | `CSO.RESERVED.01` | `CzCdpSearchOutput_Reserved01` | TField |  |  |
| 32 | `CSO.RECORD.STATUS` | `CzCdpSearchOutput_RecordStatus` | String |  |  |
| 33 | `CSO.CURR.NO` | `CzCdpSearchOutput_CurrNo` | String |  |  |
| 34 | `CSO.INPUTTER` | `CzCdpSearchOutput_Inputter` |  |  |  |
| 35 | `CSO.DATE.TIME` | `CzCdpSearchOutput_DateTime` |  |  |  |
| 36 | `CSO.AUTHORISER` | `CzCdpSearchOutput_Authoriser` | String |  |  |
| 37 | `CSO.CO.CODE` | `CzCdpSearchOutput_CoCode` | String |  |  |
| 38 | `CSO.DEPT.CODE` | `CzCdpSearchOutput_DeptCode` | String |  |  |
| 39 | `CSO.AUDITOR.CODE` | `CzCdpSearchOutput_AuditorCode` | String |  |  |
| 40 | `CSO.AUDIT.DATE.TIME` | `CzCdpSearchOutput_AuditDateTime` | String |  |  |
