# DE.ADDRESS — Table Schema

> Source: `INSERTS/I_F.DE.ADDRESS` in `PY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.ADD.DELIVERY.ADDRESS` | `DeAddress_Deliveryaddress` |  |  |  |
| 2 | `DE.ADD.ANSWERBACK` | `DeAddress_Answerback` | A (alphanumeric) | Yes | Specifies a Customer's (or Company's) acknowledgment when called up to receive a TELEX message. Validation Rules: 1-20 type A (alphanumeric) characters. Mandatory input for TELEX addresses. Not allowed for SWIFT, PRINT or SIC addresses |
| 3 | `DE.ADD.INSTITUTION.CODE` | `DeAddress_Institutioncode` |  |  |  |
| 4 | `DE.ADD.COUNTRY.CODE` | `DeAddress_Countrycode` |  |  |  |
| 5 | `DE.ADD.AUTHENTICATION` | `DeAddress_Authentication` | TField |  | Not used. Validation Rules: This is a NOINPUT field. |
| 6 | `DE.ADD.BRANCHNAME.TITLE` | `DeAddress_Branchnametitle` |  |  |  |
| 7 | `DE.ADD.NAME.1` | `DeAddress_Name1` |  |  |  |
| 8 | `DE.ADD.NAME.2` | `DeAddress_Name2` |  |  |  |
| 9 | `DE.ADD.STREET.ADDRESS` | `DeAddress_Streetaddress` |  |  |  |
| 10 | `DE.ADD.TOWN.COUNTY` | `DeAddress_Towncounty` |  |  |  |
| 11 | `DE.ADD.POST.CODE` | `DeAddress_Postcode` |  |  |  |
| 12 | `DE.ADD.COUNTRY` | `DeAddress_Country` |  |  |  |
| 13 | `DE.ADD.INSTRUCTIONS` | `DeAddress_Instructions` | TField | No | Not yet implemented. The ID of a special instructions record. Validation Rules: 1-6 numeric characters. (Optional input) |
| 14 | `DE.ADD.INTERFACE.ID` | `DeAddress_InterfaceId` | TField | No | Bank identifier in the front end software. This field is used with STACHEM front-end software. Validation Rules: 0 - 35 alphanumeric characters. (Optional Input) |
| 15 | `DE.ADD.PHONE.1` | `DeAddress_Phone1` | TField |  | This field can contain the first phone number of the customer. This client contact data is required by CRM. This field has been added in correspondence to the customer template. Validation Rules: : Maximum of 16 characters allowed |
| 16 | `DE.ADD.SMS.1` | `DeAddress_Sms1` | TField |  | This field can contain the first SMS(text) number of the customer. This client contact data is required by CRM. This field has been added in correspondence to the customer template. Validation Rules: : Maximum of 16 characters allowed |
| 17 | `DE.ADD.EMAIL.1` | `DeAddress_Email1` | TField |  | This field can contain the first email id of the customer. This client contact data is required by CRM. This field has been added in correspondence to the customer template. Validation Rules: : Increased the field length from 50 to 254 to get inline with CONTACT.DATA field of CUSTOMER record Maximum of 254 characters allowed if EB.OBJECT named EMAIL.FIELD is not defined. Upto 320 characters allowed based on EB.OBJECT named EMAIL.FIELD if defined. |
| 18 | `DE.ADD.CUSTOMER.NO` | `DeAddress_CustomerNo` | TField | No | Specifies the Customer number to whom Secure Message is to be sent. Validation Rules: Valid Customer number Optional Input |
| 19 | `DE.ADD.BLACKOUT.START` | `DeAddress_BlackoutStart` |  |  |  |
| 20 | `DE.ADD.BLACKOUT.END` | `DeAddress_BlackoutEnd` |  |  |  |
| 21 | `DE.ADD.REPLY.TO.ADR` | `DeAddress_ReplyToAdr` |  |  |  |
| 22 | `DE.ADD.ADDR.LOCATION` | `DeAddress_Reserved1` |  |  |  |
| 23 | `DE.ADD.BUILDING.NUMBER` | `DeAddress_BuildingNumber` | TField |  | Represents the number that identifies the position of a building on a street |
| 24 | `DE.ADD.BUILDING.NAME` | `DeAddress_BuildingName` | TField |  | Represents the name of the building, entrance |
| 25 | `DE.ADD.FLAT.NUMBER` | `DeAddress_FlatNumber` | TField |  | The number that identifies apartment and unit that have other dwellings above or below, often with shared access and common areas. |
| 26 | `DE.ADD.TAG25.IND` | `DeAddress_Tag25Ind` | TField | No | Defines whether or not the BIC.CODE to be included in the tag 25P for MT900 ,MT910, MT940,MT941,MT942 swift messages. . If this field is set to 'Y' then BIC.CODE will be included under tag 25P along with the account number, Otherwise it will not be included only Account number exist under tag 25. Validation Rules: Y or NO. Optional input. |
| 27 | `DE.ADD.LOCAL.REF` | `DeAddress_LocalRef` |  |  |  |
| 28 | `DE.ADD.HOLD.OUTPUT` | `DeAddress_HoldOutput` | TField | No | Defines whether or not the output delivery message is to be held. This field allows INPUT for Carriers for which ALLOW.HOLD is set to YES in DE.CARRIER. If this field is set to 'Y' then all output sent to the address will be held. If the output is classified as customer output for PRINT carrier then it will be held in F.CUSTOMER.HOLD file as opposed to F.DE.O.HOLD.KEY file for other carriers. Validation Rules: Y or NO. Optional input. |
| 29 | `DE.ADD.HOLD.MAIL.START` | `DeAddress_HoldMailStart` | TField | No | Defines the Hold Mail Start Date if Hold Output is set to Y. Optional Input |
| 30 | `DE.ADD.HOLD.MAIL.END` | `DeAddress_HoldMailEnd` | TField | No | Defines the Hold Mail End Date if Hold Output is set to Y and Hold Start Date is provided. Optional Input. |
| 31 | `DE.ADD.HOLD.MAIL.OPT` | `DeAddress_HoldMailOpt` | TField |  | Defines the Hold Options Available when Hold Output is set to Y. Valid Values : HELD, DELETED, CLEAR and SEND HELD option is to hold the output delivery message for the carrier address during Hold period. Hold needs to be manually released post the Hold Expiry date DELETED option does not generate output delivery message for the carrier address during Hold Period CLEAR and SEND are applicable only for PRINT Carrier. Once Hold Expiry is reached for a Carrier Address, CLEAR deletes the Hold Records, created during Hold Period, and SEND automatically pushes Held records to PRINT.CUST.OUTPUT file for processing them using Online Service HOLD.MAIL.ONLINE. |
| 32 | `DE.ADD.NAME.ALIAS` | `DeAddress_NameAlias` |  |  |  |
| 33 | `DE.ADD.ADDRESS.COUNTRY` | `DeAddress_AddressCountry` | TField |  | This field defines which country is the country of the address being captured. This is a no-input field for PRINT.1, EMAIL , SMS, SWIFT, ISOMX and TELEX. Validation Rule: Valid record from country to be mentioned. |
| 34 | `DE.ADD.ADDRESS.ITEM1` | `DeAddress_AddressItem1` |  |  |  |
| 35 | `DE.ADD.ADDRESS.ITEM2` | `DeAddress_AddressItem2` |  |  |  |
| 36 | `DE.ADD.ADDRESS` | `DeAddress_Address` |  |  |  |
| 37 | `DE.ADD.ADDRESS.TYP` | `DeAddress_AddressTyp` | TField |  |  |
| 38 | `DE.ADD.ADDRESS.PURPOSE` | `DeAddress_AddressPurpose` | TField |  | Represents the special purpose of an address. To be linked to the same EB.LOOKUP as for same field in Customer. |
| 39 | `DE.ADD.PO.BOX.NUMBER` | `DeAddress_PoBoxNumber` | TField |  | Identifies the postal office (PO) box number. |
| 40 | `DE.ADD.COUNTRY.SUBDIVISION` | `DeAddress_CountrySubdivision` | TField |  | Represents a subdivision of a country. such as state, region, county. etc. This field will be linked to a vetting table or to a virtual table as per the address rules setup. |
| 41 | `DE.ADD.TITLE` | `DeAddress_Title` | TField |  | Holds the title for the customer name as the part of improved client information. Use same EB.LOOKUP as for same field in CUSTOMER. |
| 42 | `DE.ADD.OVERRIDE` | `DeAddress_Override` |  |  |  |
| 43 | `DE.ADD.RECORD.STATUS` | `DeAddress_RecordStatus` | String |  |  |
| 44 | `DE.ADD.CURR.NO` | `DeAddress_CurrNo` | String |  |  |
| 45 | `DE.ADD.INPUTTER` | `DeAddress_Inputter` |  |  |  |
| 46 | `DE.ADD.DATE.TIME` | `DeAddress_DateTime` |  |  |  |
| 47 | `DE.ADD.AUTHORISER` | `DeAddress_Authoriser` | String |  |  |
| 48 | `DE.ADD.CO.CODE` | `DeAddress_CoCode` | String |  |  |
| 49 | `DE.ADD.DEPT.CODE` | `DeAddress_DeptCode` | String |  |  |
| 50 | `DE.ADD.AUDITOR.CODE` | `DeAddress_AuditorCode` | String |  |  |
| 51 | `DE.ADD.AUDIT.DATE.TIME` | `DeAddress_AuditDateTime` | String |  |  |
| 52 | `DE.ADD.SALUTATION` | `DeAddress_Salutation` | TField |  | Represents the greeting used for communication with the client |
| 53 | `DE.ADD.IDD.PREFIX.PHONE` | `DeAddress_IddPrefixPhone` | TField |  | The IDD PREFIX PHONE represents an international call prefix or dial out code for a specific country. A context enquiry IDD PREFIX is attached to it. It is validated against the INT.PREFIX field from COUNTRY table. Can be selected from a list which stores the international country prefixes list. |
| 54 | `DE.ADD.ADDRESS.VALIDATED.BY` | `DeAddress_AddressValidatedBy` | TField |  | Represents the party/service which was used to validate the address, to confirm that it is a real address. Core will not provide any automation. Can be used by country/implementation layer to store the name/identifier of local party/service used to confirm the address. Free text; |
| 55 | `DE.ADD.SMS.IDD.PREFIX.PHONE` | `DeAddress_SmsIddPrefixPhone` | TField |  | The SMS IDD PREFIX PHONE represents an international call prefix or dial out code for a specific country. A context enquiry IDD PREFIX is attached to it. It is validated against the INT.PREFIX field from COUNTRY table. Can be selected from a list which stores the international country prefixes list. User need to be careful in inputting the prefix and number in PHONE and SMS fields. There won't be any validations for prefix and number separately. The PHONE.1 or SMS.1 values should be given without IDD PREFIX if this field hold the value. It will be inputtable only for the non-primary addresses. |
| 56 | `DE.ADD.DEPARTMENT` | `DeAddress_Department` | TField |  | Identifies a division of a large organisation or building |
| 57 | `DE.ADD.SUB.DEPARTMENT` | `DeAddress_SubDepartment` | TField |  | Identifies a sub-division of a large organisation or building |
| 58 | `DE.ADD.FLOOR` | `DeAddress_Floor` | TField |  | Floor or storey within a building |
| 59 | `DE.ADD.TOWN.LOCATION.NAME` | `DeAddress_TownLocationName` | TField |  | Specific location name within the town. |
| 60 | `DE.ADD.DISTRICT.NAME` | `DeAddress_DistrictName` | TField |  | Identifies a subdivision within a country sub-division. |
