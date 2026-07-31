# PZ.OPEN.BANKING.DIR — Table Schema

> Source: `INSERTS/I_F.PZ.OPEN.BANKING.DIR` in `RT_OpenBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PZO.CUSTOMER` | `PzOpenBankingDir_Customer` |  |  |  |
| 2 | `PZO.COMPANY.ID` | `PzOpenBankingDir_CompanyId` |  |  |  |
| 3 | `PZO.RESERVED.23` | `PzOpenBankingDir_Reserved23` | TField |  |  |
| 4 | `PZO.RESERVED.22` | `PzOpenBankingDir_Reserved22` | TField |  |  |
| 5 | `PZO.RESERVED.21` | `PzOpenBankingDir_Reserved21` | TField |  |  |
| 6 | `PZO.LEGAL.NAME` | `PzOpenBankingDir_LegalName` | TField |  | Name of the regulated entity in the Competent Authority Register; for example ABN Amro |
| 7 | `PZO.NCA.URN` | `PzOpenBankingDir_NcaUrn` | TField |  | TPPs unique reference number of entity in National Competent Authority Register e.g. 100008 |
| 8 | `PZO.DATE.TIME.CREATED` | `PzOpenBankingDir_DateTimeCreated` | TField | Yes | Mandatory field containing the date and time, the entity was created inside the directory (format: should be astandard T24 Date - Time field). Field can accept past, current, future dates Validation Rules - Should be a valid UTC ISO8601 date time format say 2019-01-01T01:01:01Z. No change field. |
| 9 | `PZO.GLOBAL.URN` | `PzOpenBankingDir_GlobalUrn` | TField |  | The unique reference number made up of the home country code the NCA and the reference number at the NCA. Forexample GB-FCA-100008. This will be used to link the record to the incoming API feed.A cross reference file shouldbe created to link the Global URN and CUSTOMER.ID in @ID.Space should not be allowed within the text entered. |
| 10 | `PZO.NCA.CODE` | `PzOpenBankingDir_NcaCode` | TField |  | This is the ID of the record in the National Competent Authority table, which contains NCA data for this record. |
| 11 | `PZO.PSP.CATEGORY` | `PzOpenBankingDir_PspCategory` | TField |  | Drop-down list, should list TPP(Third Party Provider) valid categories e.g. Payment Institution, Electronic MoneyInstitution, Credit Institution, Post Office, Member States, Central Bank |
| 12 | `PZO.PSP.ROLE` | `PzOpenBankingDir_PspRole` |  |  |  |
| 13 | `PZO.ROLE.COUNTRIES` | `PzOpenBankingDir_RoleCountries` |  |  |  |
| 14 | `PZO.DELETED` | `PzOpenBankingDir_Deleted` | TField |  | Field to indicate the status of the directory. Allowed values are TRUE - The record is deleted from the directory FALSE - The record is still live in the directory. |
| 15 | `PZO.SERVICE.PASSPORTS` | `PzOpenBankingDir_ServicePassports` |  |  |  |
| 16 | `PZO.SERVICE.COUNTRIES` | `PzOpenBankingDir_ServiceCountries` |  |  |  |
| 17 | `PZO.COMMERCIAL.NAME` | `PzOpenBankingDir_CommercialName` |  |  |  |
| 18 | `PZO.COMP.AUTHORITY.URL` | `PzOpenBankingDir_CompAuthorityUrl` | TField |  | URL to the Competent Authority source of this data.For example; https://www.fca.org.uk/Company=123 |
| 19 | `PZO.WEBSITE` | `PzOpenBankingDir_Website` | TField |  | Website of the entity as specified in the National Competent Authority Register.For examplehttp://www.google.com/compliance. |
| 20 | `PZO.LEGAL.ENT.IDENTIFIER` | `PzOpenBankingDir_LegalEntIdentifier` | TField |  | The Legal Entity Identifier of the entity as specified in the Competent Authority Register. Will acceptalphanumeric characters |
| 21 | `PZO.INTERFACE` | `PzOpenBankingDir_Interface` | TField |  | Free txt fields to input Name of interface |
| 22 | `PZO.STATUS` | `PzOpenBankingDir_Status` | TField |  | The status of the entity in the directory. This will be Inactive for inactive entities, Active for activeentities, and Blocked for blocked entities and Closed for entities that are no longer active. Contains Options such as ACTIVE, INACTIVE, CLOSED, BLOCKED |
| 23 | `PZO.SET.ACTIVE` | `PzOpenBankingDir_SetActive` | TField |  | ASPSPs will be able to control individual TPP status by setting this flag. Option selected here from list willtake priority over STATUS field. Available options are:Null = Means same as the value in STATUS field. This is thedefault value.Y= TPP is Active and is in operation.N= TPP is Blocked i.e. Any request received from this TPP willbe rejected This flag is expected to remain unchanged, even in event of any update received from electronicdownload. User should only be able to update this field by manually editing it. |
| 24 | `PZO.AUTHORISATION.DATE` | `PzOpenBankingDir_AuthorisationDate` | TField | Yes | Auto updated when status field is set to Active. This field maintains date and time the entity was authorised bythe NCA.This field is mandatory if particular entity has been Authorised by NCA.Standard ISO8601 UTC Date timeformat. |
| 25 | `PZO.BLOCK.DATE` | `PzOpenBankingDir_BlockDate` | TField |  | Auto updated when TPP status set to Block. This field will record the system date and time the TPP was blocked.Standard ISO8601 UTC Date time format. |
| 26 | `PZO.INTERNALLY.BLOCKED.ON` | `PzOpenBankingDir_InternallyBlockedOn` | TField |  | No input field. Records date and time when the bank has blocked a TPP (using SET.ACTIVE= No). This field isexpected to reset to blank with SET.ACTIVE= Yes/ Null |
| 27 | `PZO.DATE.CLOSED` | `PzOpenBankingDir_DateClosed` | TField | Yes | Mandatory field when the status is Closed.Auto updated when TPP Status set to Closed. This field maintains thedate the entity was withdrawn from the NCA Register.Standard ISO8601 UTC Date time format. |
| 28 | `PZO.VERSION.NO` | `PzOpenBankingDir_VersionNo` | TField |  | Auto updated the version number of this record. This version will increment each time a new version is publishedand refers to the version number in the NCA directory. This may be part of a regular download (daily) or based on areal time update when the source data changes. |
| 29 | `PZO.SANDBOX.URL` | `PzOpenBankingDir_SandboxUrl` | TField | No | Optional Field to specify the URL. |
| 30 | `PZO.TEST.URL` | `PzOpenBankingDir_TestUrl` | TField | No | Optional field to specify the URL. |
| 31 | `PZO.SPECIFICATION.URL` | `PzOpenBankingDir_SpecificationUrl` | TField | No | Optional field to specify the URL. |
| 32 | `PZO.DOCUMENTATION.URL` | `PzOpenBankingDir_DocumentationUrl` | TField | No | Optional field to specify the URL to be documented. |
| 33 | `PZO.IP.ADDRESS` | `PzOpenBankingDir_IpAddress` | TField | No | Optional field to specify IP address of the current system generated. |
| 34 | `PZO.EXT.SRC.PROVIDER` | `PzOpenBankingDir_ExtSrcProvider` | TField |  | The External(Third Party) resource provider to be entered. |
| 35 | `PZO.CONN.MTD` | `PzOpenBankingDir_ConnMtd` | TField |  | Specifies the connection method. |
| 36 | `PZO.FIRST.ADDRESS.LINE` | `PzOpenBankingDir_FirstAddressLine` | TField |  | First line of the address of the Regulated Entity as specified in the Competent Authority Register |
| 37 | `PZO.SECOND.ADDRESS.LINE` | `PzOpenBankingDir_SecondAddressLine` | TField |  | Second line of the address of the Regulated Entity as specified in the Competent Authority Register |
| 38 | `PZO.TOWN.COUNTRY` | `PzOpenBankingDir_TownCountry` | TField |  | Postal town of the Regulated Entity as specified in the Competent Authority Register |
| 39 | `PZO.POST.CODE` | `PzOpenBankingDir_PostCode` | TField |  | Postal town of the Regulated Entity as specified in the Competent Authority Register |
| 40 | `PZO.PHONE` | `PzOpenBankingDir_Phone` | TField |  | Phone number of the Regulated Entity as specified in the Competent Authority Register |
| 41 | `PZO.EMAIL` | `PzOpenBankingDir_Email` | TField |  | Email address of the Regulated Entity as specified in the Competent Authority Register |
| 42 | `PZO.FAX` | `PzOpenBankingDir_Fax` | TField |  | Fax number of the Regulated Entity as specified in the Competent Authority Register |
| 43 | `PZO.COUNTRY` | `PzOpenBankingDir_Country` | TField |  | Country of the Regulated Entity as specified in the Competent Authority Register Eg: United Kingdom |
| 44 | `PZO.LOGO.URL` | `PzOpenBankingDir_LogoUrl` | TField |  | The URL where the Entity LOGO is defined. |
| 45 | `PZO.PAYMENT.TEMPLATES` | `PzOpenBankingDir_PaymentTemplates` |  |  |  |
| 46 | `PZO.TIME.ZONE` | `PzOpenBankingDir_TimeZone` | TField |  | This field will hold the time zone where the INTERFACE is located |
| 47 | `PZO.ALTERNATE.ID` | `PzOpenBankingDir_AlternateId` | TField |  | This field is auto-populated when the user is validating or approving the record. This field is combination of field INTERFACE.NAME and GLOBA.URN |
| 48 | `PZO.RESERVED.20` | `PzOpenBankingDir_Reserved20` | TField |  |  |
| 49 | `PZO.RESERVED.19` | `PzOpenBankingDir_Reserved19` | TField |  |  |
| 50 | `PZO.RESERVED.18` | `PzOpenBankingDir_Reserved18` | TField |  |  |
| 51 | `PZO.RESERVED.17` | `PzOpenBankingDir_Reserved17` | TField |  |  |
| 52 | `PZO.RESERVED.16` | `PzOpenBankingDir_Reserved16` | TField |  |  |
| 53 | `PZO.RESERVED.15` | `PzOpenBankingDir_Reserved15` | TField |  |  |
| 54 | `PZO.RESERVED.14` | `PzOpenBankingDir_Reserved14` | TField |  |  |
| 55 | `PZO.RESERVED.13` | `PzOpenBankingDir_Reserved13` | TField |  |  |
| 56 | `PZO.RESERVED.12` | `PzOpenBankingDir_Reserved12` | TField |  |  |
| 57 | `PZO.RESERVED.11` | `PzOpenBankingDir_Reserved11` | TField |  |  |
| 58 | `PZO.RESERVED.10` | `PzOpenBankingDir_Reserved10` | TField |  |  |
| 59 | `PZO.RESERVED.09` | `PzOpenBankingDir_Reserved09` | TField |  |  |
| 60 | `PZO.RESERVED.08` | `PzOpenBankingDir_Reserved08` | TField |  |  |
| 61 | `PZO.RESERVED.07` | `PzOpenBankingDir_Reserved07` | TField |  |  |
| 62 | `PZO.RESERVED.06` | `PzOpenBankingDir_Reserved06` | TField |  |  |
| 63 | `PZO.RESERVED.05` | `PzOpenBankingDir_Reserved05` | TField |  |  |
| 64 | `PZO.RESERVED.04` | `PzOpenBankingDir_Reserved04` | TField |  |  |
| 65 | `PZO.RESERVED.03` | `PzOpenBankingDir_Reserved03` | TField |  |  |
| 66 | `PZO.RESERVED.02` | `PzOpenBankingDir_Reserved02` | TField |  |  |
| 67 | `PZO.RESERVED.01` | `PzOpenBankingDir_Reserved01` | TField |  |  |
| 68 | `PZO.LOCAL.REF` | `PzOpenBankingDir_LocalRef` |  |  |  |
| 69 | `PZO.RECORD.STATUS` | `PzOpenBankingDir_RecordStatus` | String |  |  |
| 70 | `PZO.CURR.NO` | `PzOpenBankingDir_CurrNo` | String |  |  |
| 71 | `PZO.INPUTTER` | `PzOpenBankingDir_Inputter` |  |  |  |
| 72 | `PZO.DATE.TIME` | `PzOpenBankingDir_DateTime` |  |  |  |
| 73 | `PZO.AUTHORISER` | `PzOpenBankingDir_Authoriser` | String |  |  |
| 74 | `PZO.CO.CODE` | `PzOpenBankingDir_CoCode` | String |  |  |
| 75 | `PZO.DEPT.CODE` | `PzOpenBankingDir_DeptCode` | String |  |  |
| 76 | `PZO.AUDITOR.CODE` | `PzOpenBankingDir_AuditorCode` | String |  |  |
| 77 | `PZO.AUDIT.DATE.TIME` | `PzOpenBankingDir_AuditDateTime` | String |  |  |
