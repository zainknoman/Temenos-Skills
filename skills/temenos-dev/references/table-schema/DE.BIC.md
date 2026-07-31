# DE.BIC — Table Schema

> Source: `INSERTS/I_F.DE.BIC` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.BIC.TAG` | `DeBic_Tag` | TField |  | This is the Tag Identifier. Record Identifier : 'BI' |
| 2 | `DE.BIC.FLAG` | `DeBic_Flag` | TField |  | This is the flag which indicates whether or not there has been a change in the record since the last release of the CD. Validation Rules: Contains one of the following values 'A' Addition since last BIC+ Directory 'D' Deletion since last BIC+ Directory 'U' Unchanged since last BIC+ Directory 'M' Modification since last BIC+ Directory 'E' Expired : Reserved for future use. |
| 3 | `DE.BIC.RECORDKEY` | `DeBic_Recordkey` | TField |  | The unique key of the record in the file. The key is made up of the ISO country code and a sequential number of 6 digits. |
| 4 | `DE.BIC.INSTITUTION` | `DeBic_Institution` |  |  |  |
| 5 | `DE.BIC.CITY` | `DeBic_City` | TField |  | This is the city in which the branch of the institution resides. Wherever possible, the field is standardized. This means that main cities are spelled the same way across the file. |
| 6 | `DE.BIC.BRANCH` | `DeBic_Branch` |  |  |  |
| 7 | `DE.BIC.BIC.CODE` | `DeBic_BicCode` | TField |  | Bank Identifier code (bank, country and location code) Bank code (4 char) Country code (2 char) Location code (2 char) |
| 8 | `DE.BIC.BRANCH.CODE` | `DeBic_BranchCode` | TField |  | Branch code associated to the BIC CODE. |
| 9 | `DE.BIC.UNIQ.BIC.CODE` | `DeBic_UniqBicCode` | TField |  | Bank Identifier code (bank, country and location code) Bank code (4 char) Country code (2 char) Location code (2 char) For search purposes, the value is unique within the active records(that is, only records with a modification flag of U,A or M) |
| 10 | `DE.BIC.UNIQ.BR.CODE` | `DeBic_UniqBrCode` | TField |  | Branch code associated to UNIQUE BIC CODE. |
| 11 | `DE.BIC.IBAN.BIC.CODE` | `DeBic_IbanBicCode` | TField |  | Bank Identifier code (bank, country and location code) Bank code (4 char) Country code (2 char) Location code (2 char) BIC issued together with the IBANs to the bank�s clients. |
| 12 | `DE.BIC.IBAN.BR.CODE` | `DeBic_IbanBrCode` | TField |  | Branch code associated to IBAN BIC CODE. |
| 13 | `DE.BIC.ROUTING.BIC.CODE` | `DeBic_RoutingBicCode` | TField |  | This is the routing or processing BIC to which the Euro payment must be sent. ROUTING BIC CODE is meant for SWIFT messaging purposes. When the IBAN BIC CODE is a non-connected BIC(BIC1), the ROUTING BIC CODE is filled to provide an addressable code on the SWIFT network. |
| 14 | `DE.BIC.ROUTING.BR.CODE` | `DeBic_RoutingBrCode` | TField |  | Branch code associated to ROUTING BIC CODE |
| 15 | `DE.BIC.PARENT.BK.CODE` | `DeBic_ParentBkCode` | TField |  | Bank code of the parent BIC. |
| 16 | `DE.BIC.COUNTRY.CODE` | `DeBic_CountryCode` | TField |  | ISO country code of the financial institution. |
| 17 | `DE.BIC.NATIONALID` | `DeBic_Nationalid` | TField |  | National identifier of the bank.This field contains the National bank code for the financial institution (for example, BSC codes for UK banks). |
| 18 | `DE.BIC.UNIQ.NATIONALID` | `DeBic_UniqNationalid` | TField |  | National ID.For search purposes, Value is unique in the data file per country code. The value is unique within the active records(that is, only records with a modification flag of U,A or M) |
| 19 | `DE.BIC.IBAN.CTRY.CODE` | `DeBic_IbanCtryCode` | TField |  | ISO country code prefix of the IBAN that the bank issues. |
| 20 | `DE.BIC.IBAN.NATIONALID` | `DeBic_IbanNationalid` | TField |  | National ID as included in the IBAN. |
| 21 | `DE.BIC.UNIQ.IBAN.NID` | `DeBic_UniqIbanNid` | TField |  | IBAN National ID. For search purposes,value is unique in the data file per IBAN COUNTRY CODE. The value is unique within the active records(that is, only records with a modification flag of U,A or M) |
| 22 | `DE.BIC.OTHER.NID1` | `DeBic_OtherNid1` | TField |  | National identifier of the bank.For some countries, 2 types of national ID co-exist. "Other National ID" fields are used for these special cases. |
| 23 | `DE.BIC.NAT.ID.TYPE` | `DeBic_NatIdType` | TField |  | The name of the national code or the name of the national code providere.g BLZ for German national id |
| 24 | `DE.BIC.CHIPSUID` | `DeBic_Chipsuid` | TField |  | This field contains the Chips Universal ID for the financial institution. |
| 25 | `DE.BIC.SUBTYPE.IND` | `DeBic_SubtypeInd` | TField |  | Type of financial institution. For example : a bank or a broker. |
| 26 | `DE.BIC.SERVICECODES` | `DeBic_Servicecodes` |  |  |  |
| 27 | `DE.BIC.BR.QUALIFIER` | `DeBic_BrQualifier` | TField |  | BIC branch qualifiers. For example : ADM = Adminstration, BKO = Back office. |
| 28 | `DE.BIC.SPECIALCODE` | `DeBic_Specialcode` | TField |  | Specific information from the National record for the financial institution. |
| 29 | `DE.BIC.ADDRESS` | `DeBic_Address` |  |  |  |
| 30 | `DE.BIC.ZIP` | `DeBic_Zip` | TField |  | The full postal code of the branch for the financial institution. Validation Rules: . Wherever possible the field is standardised. |
| 31 | `DE.BIC.LOCATION` | `DeBic_Location` |  |  |  |
| 32 | `DE.BIC.COUNTRY` | `DeBic_Country` |  |  |  |
| 33 | `DE.BIC.POBNUMBER` | `DeBic_Pobnumber` | TField |  | This is the Post Office Box (POB) number that relates to financial institution |
| 34 | `DE.BIC.POBZIP` | `DeBic_Pobzip` | TField |  | This is the zip code for the Post Office Box that the financial institution may use. |
| 35 | `DE.BIC.POBLOCATION` | `DeBic_Poblocation` |  |  |  |
| 36 | `DE.BIC.POBCOUNTRY` | `DeBic_Pobcountry` |  |  |  |
| 37 | `DE.BIC.NID.EXPIRY.DATE` | `DeBic_NidExpiryDate` | TField |  | Date on which the national ID has been removed by the national authority. |
| 38 | `DE.BIC.VALID.FROM` | `DeBic_ValidFrom` | TField |  | The date since the whole record becomes effective due to a change of its attributese.g. BIC activates/deactivated in future |
| 39 | `DE.BIC.OFFICE.TYPE` | `DeBic_OfficeType` | TField |  | The status of the entity in the office hierarchye.g. HO - Head Office, MP - Main Payments Office ; values aligned to BIC Plus directory |
| 40 | `DE.BIC.PARENT.OFF.KEY` | `DeBic_ParentOffKey` | TField |  | The key of the record which is immediately upward in the office hierarchy |
| 41 | `DE.BIC.SWIFT.AUTH.KEY` | `DeBic_SwiftAuthKey` | TField | No | This field is used to maintain the existence of a Swift key with a particular bic code. An input of Null denotes that no swift key exists. Validation Rules: Optional Field Valid values are YES and Null |
| 42 | `DE.BIC.HEAD.OFFICE.KEY` | `DeBic_HeadOfficeKey` | TField |  | The key to the Head Office record |
| 43 | `DE.BIC.LEGAL.TYPE` | `DeBic_LegalType` | TField |  | The status of the entity in the legal hierarchye.g. L - Legal entity |
| 44 | `DE.BIC.LEGAL.PARENT.KEY` | `DeBic_LegalParentKey` | TField |  | The key of the record of the Legal entity |
| 45 | `DE.BIC.GROUP.TYPE` | `DeBic_GroupType` | TField |  | The type of entity that identifies the group ( Parent or Member) |
| 46 | `DE.BIC.INSTITUTION.STUS` | `DeBic_InstitutionStus` | TField |  | This indicates the status of the institution ( Bank, Money Exchange, Payment Institution, etc) |
| 47 | `DE.BIC.CO.OPER.GROUP.KEY` | `DeBic_CoOperGroupKey` | TField |  | If the record indicates a cooperative bank which belongs to a cooperative bank grouping, then this field indicates the Record_Key of the cooperativecentral bank for that group.Hierarchy in this case flows downward.In the case of any such cooperative central bank, the value here is its ownRecord_Key.If the cooperative bank concerned does not belong to a cooperative bank grouping, then the field is empty. |
| 48 | `DE.BIC.ISO.LEI.CODE` | `DeBic_IsoLeiCode` | TField |  | The code of the legal entity identifier |
| 49 | `DE.BIC.TIMEZONE` | `DeBic_Timezone` | TField |  | Timezone for the entity |
| 50 | `DE.BIC.NETWORK.CNTY` | `DeBic_NetworkCnty` | TField |  | Status of the entity being connected to SWIFT; applies only to entity which have a BIC |
| 51 | `DE.BIC.SSI.GROUP.KEY` | `DeBic_SsiGroupKey` | TField |  | The SSI Group the entity belongs to |
| 52 | `DE.BIC.IBAN.KEY` | `DeBic_IbanKey` | TField |  | The key of the record in IBAN Plus which defines the IBAN details for this entity |
| 53 | `DE.BIC.MANUAL` | `DeBic_Manual` | TField |  | Flag to indicate a manually input record Validation Rules: This field is updated as Yes, when the record is modified manually. |
| 54 | `DE.BIC.LOCAL.REF` | `DeBic_LocalRef` |  |  |  |
| 55 | `DE.BIC.RESERVED10` | `DeBic_Reserved10` | TField |  |  |
| 56 | `DE.BIC.RESERVED9` | `DeBic_Reserved9` | TField |  |  |
| 57 | `DE.BIC.RESERVED8` | `DeBic_Reserved8` | TField |  |  |
| 58 | `DE.BIC.RESERVED7` | `DeBic_Reserved7` | TField |  |  |
| 59 | `DE.BIC.RESERVED6` | `DeBic_Reserved6` | TField |  |  |
| 60 | `DE.BIC.RESERVED5` | `DeBic_Reserved5` | TField |  |  |
| 61 | `DE.BIC.RESERVED4` | `DeBic_Reserved4` | TField |  |  |
| 62 | `DE.BIC.RESERVED3` | `DeBic_Reserved3` | TField |  |  |
| 63 | `DE.BIC.RESERVED2` | `DeBic_Reserved2` | TField |  |  |
| 64 | `DE.BIC.RESERVED1` | `DeBic_Reserved1` | TField |  |  |
| 65 | `DE.BIC.RECORD.STATUS` | `DeBic_RecordStatus` | String |  |  |
| 66 | `DE.BIC.CURR.NO` | `DeBic_CurrNo` | String |  |  |
| 67 | `DE.BIC.INPUTTER` | `DeBic_Inputter` |  |  |  |
| 68 | `DE.BIC.DATE.TIME` | `DeBic_DateTime` |  |  |  |
| 69 | `DE.BIC.AUTHORISER` | `DeBic_Authoriser` | String |  |  |
| 70 | `DE.BIC.CO.CODE` | `DeBic_CoCode` | String |  |  |
| 71 | `DE.BIC.DEPT.CODE` | `DeBic_DeptCode` | String |  |  |
| 72 | `DE.BIC.AUDITOR.CODE` | `DeBic_AuditorCode` | String |  |  |
| 73 | `DE.BIC.AUDIT.DATE.TIME` | `DeBic_AuditDateTime` | String |  |  |
