# PERSON.ENTITY — Table Schema

> Source: `INSERTS/I_F.PERSON.ENTITY` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PER.ENT.PERSON.ENTITY` | `PersonEntity_PersonEntity` | TField | Yes | This field is used to distinguish if the record is for a real person or a legal entity. Validation rules Mandatory field Valid options PERSON ENTITY |
| 2 | `PER.ENT.NAME` | `PersonEntity_Name` |  |  |  |
| 3 | `PER.ENT.STREET` | `PersonEntity_Street` |  |  |  |
| 4 | `PER.ENT.ADDRESS` | `PersonEntity_Address` |  |  |  |
| 5 | `PER.ENT.TOWN.COUNTRY` | `PersonEntity_TownCountry` |  |  |  |
| 6 | `PER.ENT.POST.CODE` | `PersonEntity_PostCode` |  |  |  |
| 7 | `PER.ENT.COUNTRY` | `PersonEntity_Country` |  |  |  |
| 8 | `PER.ENT.PHONE` | `PersonEntity_Phone` |  |  |  |
| 9 | `PER.ENT.EMAIL` | `PersonEntity_Email` |  |  |  |
| 10 | `PER.ENT.SOCIAL.NTW.ID` | `PersonEntity_SocialNtwId` |  |  |  |
| 11 | `PER.ENT.GENDER` | `PersonEntity_Gender` | TField | No | This field contains the customer's GENDER Validation rules Optional input Valid options are MALE FEMALE Becomes a no input field when the field PERSON.ENTITY is ENTITY |
| 12 | `PER.ENT.BIRTH.INCORP.DATE` | `PersonEntity_BirthIncorpDate` | TField | No | This field is used to record either Birth date for a person Or the date the company was incorporated for en entity Validation rules Optional input Standard T24 date field |
| 13 | `PER.ENT.LEGAL.ID` | `PersonEntity_LegalId` |  |  |  |
| 14 | `PER.ENT.LEGAL.DOC.NAME` | `PersonEntity_LegalDocName` |  |  |  |
| 15 | `PER.ENT.STATUS` | `PersonEntity_Status` | TField | Yes | This field is used to define the status of the relationship with the bank of the person or entity defined . Validation rules Mandatory field Valid options are ACTIVE - This person or entity has become a customer of the bank ENROLMENT - This status is used to identify that this customer is no longer a prospect ans is being enrolled as an actual customer EX-CUSTOMER- This status implies the customer has left the bank and is no longer a customer. NONE - This status is used to identify person.entity records who have no relation with the bank. The details are held for informational purposes. These details may be used to record relationship details with customers of the bank. PROSPECT - This status is used to identify that this person.entity may become a banks customer at a future date. CLOSED - This status is used to enable the user to manually take the decision to close a PERSON.ENTITY when is not needed any more (the customer to which they are related as a Director, Auditor has been closed), that is, PERSON.ENTITY not linked to customer. ACTIVE EX-CUSTOMER - This status is used to indicates that the person or entity has stopped their relationship with the bank as a customer but the bank still maintains their details for their non-customer role. The following STATUS changes are allowed Current Status Subsequent Status PROSPECT ENROLMENT/ACTIVE/NONE ENROLMENT PROSPECT/ACTIVE/NONE ACTIVE PROSPECT/ENROLMENT/ACTIVE NONE PROSPECT/ENROLMENT/ACTIVE EX-CUSTOMER ACTIVE &#160; &#160; |
| 16 | `PER.ENT.REG.COUNTRY` | `PersonEntity_RegCountry` | TField | No | This field is used to identify which country an entity has been registered Validation rules Optional input 2 type SSS uppercase country code characters Must be a valid record on the COUNTRY table No input if the field PERSON.ENTITY is person |
| 17 | `PER.ENT.CUSTOMER` | `PersonEntity_Customer` | TField |  | This field will be updated with the id to the Customer record that is created when a PERSON.ENTITY Status is changed to ACTIVE. Validation rules No input System generated field |
| 18 | `PER.ENT.LOCAL.REF` | `PersonEntity_LocalRef` |  |  |  |
| 19 | `PER.ENT.ADDRESS.COUNTRY` | `PersonEntity_AddressCountry` | TField |  | Defines which country is the country of the address being captured, it may be different to the residence. Already exists into Customer table. Must be a valid country code from the COUNTRY table. |
| 20 | `PER.ENT.ADDRESS.TYPE` | `PersonEntity_AddressType` | TField |  | Identifies the nature of the address.Same EB.LOOKUP as CUSTOMER |
| 21 | `PER.ENT.BUILDING.NUMBER` | `PersonEntity_BuildingNumber` | TField |  | Represents the number that identifies the position of a building on a street |
| 22 | `PER.ENT.BUILDING.NAME` | `PersonEntity_BuildingName` | TField |  | Represents the name of the building, entrance |
| 23 | `PER.ENT.FLAT.NUMBER` | `PersonEntity_FlatNumber` | TField |  | The number that identifies apartment and unit that have other dwellings above or below, often with shared access and common areas. |
| 24 | `PER.ENT.PO.BOX.NUMBER` | `PersonEntity_PoBoxNumber` | TField |  | Identifies the postal office (PO) box number. |
| 25 | `PER.ENT.COUNTRY.SUBDIVISION` | `PersonEntity_CountrySubdivision` | TField |  | Represents a subdivision of a country. |
| 26 | `PER.ENT.SALUTATION` | `PersonEntity_Salutation` | TField |  | Represents the greeting used for communication with the client. |
| 27 | `PER.ENT.ADDRESS.PURPOSE` | `PersonEntity_AddressPurpose` | TField |  | Represents the special purpose of the address. Same values or EB.LOOKUP on CUSTOMER |
| 28 | `PER.ENT.ADDRESS.ITEM1` | `PersonEntity_AddressItem1` |  |  |  |
| 29 | `PER.ENT.ADDRESS.ITEM2` | `PersonEntity_AddressItem2` |  |  |  |
| 30 | `PER.ENT.TITLE` | `PersonEntity_Title` | TField |  | Holds the title for the customer name. Already exists into Customer table.Must use the same EB.LOOKUP as CUSTOMER |
| 31 | `PER.ENT.IDD.PREFIX.PHONE` | `PersonEntity_IddPrefixPhone` |  |  |  |
| 32 | `PER.ENT.RESERVED.2` | `PersonEntity_Reserved2` |  |  |  |
| 33 | `PER.ENT.OVERRIDE` | `PersonEntity_Override` |  |  |  |
| 34 | `PER.ENT.RECORD.STATUS` | `PersonEntity_RecordStatus` | String |  |  |
| 35 | `PER.ENT.CURR.NO` | `PersonEntity_CurrNo` | String |  |  |
| 36 | `PER.ENT.INPUTTER` | `PersonEntity_Inputter` |  |  |  |
| 37 | `PER.ENT.DATE.TIME` | `PersonEntity_DateTime` |  |  |  |
| 38 | `PER.ENT.AUTHORISER` | `PersonEntity_Authoriser` | String |  |  |
| 39 | `PER.ENT.CO.CODE` | `PersonEntity_CoCode` | String |  |  |
| 40 | `PER.ENT.DEPT.CODE` | `PersonEntity_DeptCode` | String |  |  |
| 41 | `PER.ENT.AUDITOR.CODE` | `PersonEntity_AuditorCode` | String |  |  |
| 42 | `PER.ENT.AUDIT.DATE.TIME` | `PersonEntity_AuditDateTime` | String |  |  |
| 43 | `PER.ENT.CONTACT.TYPE` | `PersonEntity_ContactType` |  |  |  |
| 44 | `PER.ENT.CONTACT.DATA` | `PersonEntity_ContactData` |  |  |  |
| 45 | `PER.ENT.AUTO.UPD.DEL.ADD` | `PersonEntity_AutoUpdDelAdd` |  |  |  |
| 46 | `PER.ENT.DEPARTMENT` | `PersonEntity_Department` | TField |  | Identifies a division of a large organisation or building |
| 47 | `PER.ENT.SUB.DEPARTMENT` | `PersonEntity_SubDepartment` | TField |  | Identifies a sub-division of a large organisation or building |
| 48 | `PER.ENT.FLOOR` | `PersonEntity_Floor` | TField |  | Floor or storey within a building |
| 49 | `PER.ENT.TOWN.LOCATION.NAME` | `PersonEntity_TownLocationName` | TField |  | Specific location name within the town. |
| 50 | `PER.ENT.DISTRICT.NAME` | `PersonEntity_DistrictName` | TField |  | Identifies a subdivision within a country sub-division. |
