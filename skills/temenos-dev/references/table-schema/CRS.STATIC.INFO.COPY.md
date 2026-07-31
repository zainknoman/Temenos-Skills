# CRS.STATIC.INFO.COPY — Table Schema

> Source: `INSERTS/I_F.CRS.STATIC.INFO.COPY` in `CE_CrsReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CE.SIC.DEFAULT.ADDRESS` | `CrsStaticInfoCopy_DefaultAddress` | TField |  | This field is to specify whether the address of the client has to be from CUSTOMER or DE ADDRESS. Options field with options CUSTOMER and DE.ADDRESS. |
| 2 | `CE.SIC.CLIENT.TYPE` | `CrsStaticInfoCopy_ClientType` | TField |  | Field to state whether the customer is an Individual or an Entity Validation Rules: Valid Id from CRS.CLIENT.TYPE table. |
| 3 | `CE.SIC.NAME.1` | `CrsStaticInfoCopy_Name1` | TField |  | Contains the first name of the customer. |
| 4 | `CE.SIC.NAME.2` | `CrsStaticInfoCopy_Name2` | TField |  | Contains the first name of the customer. |
| 5 | `CE.SIC.SHORT.NAME` | `CrsStaticInfoCopy_ShortName` | TField |  | Contains the short name of the customer. Validation Rules: NEW, AMEND or DELETE. |
| 6 | `CE.SIC.STREET` | `CrsStaticInfoCopy_Street` | TField |  | Identifies the first line of the Customer's base address. |
| 7 | `CE.SIC.ADDRESS` | `CrsStaticInfoCopy_Address` |  |  |  |
| 8 | `CE.SIC.TOWN.COUNTRY` | `CrsStaticInfoCopy_TownCountry` | TField |  | Identifies the town and country of the Customer's base address. |
| 9 | `CE.SIC.POST.CODE` | `CrsStaticInfoCopy_PostCode` | TField |  | Identifies the postal code for customer. |
| 10 | `CE.SIC.COUNTRY.SUB.ENTITY` | `CrsStaticInfoCopy_CountrySubEntity` | TField |  | Specifies the sub entity's country details if present Contains the value of the field mentioned in CRS.REPORTING.PARAMETER's FIELD.REF.COU.SUB.ENT field . |
| 11 | `CE.SIC.COUNTRY` | `CrsStaticInfoCopy_Country` | TField |  | Identifies the country for customer |
| 12 | `CE.SIC.SECTOR` | `CrsStaticInfoCopy_Sector` | TField |  | Identifies the sector for customer Valid id from SECTOR table |
| 13 | `CE.SIC.ACCOUNT.OFFICER` | `CrsStaticInfoCopy_AccountOfficer` | TField |  | Identifies the account officer for customer Valid id from DEPT.ACCT.OFFICER table |
| 14 | `CE.SIC.INDUSTRY` | `CrsStaticInfoCopy_Industry` | TField |  | Identifies the industry to which customer belongs to Valid id from INDUSTRY table |
| 15 | `CE.SIC.CUSTOMER.STATUS` | `CrsStaticInfoCopy_CustomerStatus` | TField |  | Identifies the Status of the Customer Valid id from CUSTOMER.STATUS table |
| 16 | `CE.SIC.NATIONALITY` | `CrsStaticInfoCopy_Nationality` | TField |  | Identifies the nationality of the Customer Valid id from COUNTRY table |
| 17 | `CE.SIC.RESIDENCE` | `CrsStaticInfoCopy_Residence` | TField |  | Identifies the residence of the Customer Valid id from COUNTRY table |
| 18 | `CE.SIC.DOMICILE` | `CrsStaticInfoCopy_Domicile` | TField |  | Identifies the domicile of the Customer Valid id from COUNTRY table |
| 19 | `CE.SIC.COMPANY.BOOK` | `CrsStaticInfoCopy_CompanyBook` | TField |  | This field holds the branch of the customer. Accepts the id of the COMPANY which shares customer with currentlysigned in company Valid id from COMPANY table |
| 20 | `CE.SIC.TAX.RESIDENCE` | `CrsStaticInfoCopy_TaxResidence` |  |  |  |
| 21 | `CE.SIC.TIN.COUNTRY` | `CrsStaticInfoCopy_TinCountry` |  |  |  |
| 22 | `CE.SIC.TIN.CODE` | `CrsStaticInfoCopy_TinCode` |  |  |  |
| 23 | `CE.SIC.CP.ROLE.TYPE` | `CrsStaticInfoCopy_CpRoleType` |  |  |  |
| 24 | `CE.SIC.CP.CUST` | `CrsStaticInfoCopy_CpCust` |  |  |  |
| 25 | `CE.SIC.CP.CUSTOMER.NAME` | `CrsStaticInfoCopy_CpCustomerName` |  |  |  |
| 26 | `CE.SIC.CP.CUSTOMER.REFERENCE` | `CrsStaticInfoCopy_CpCustomerReference` |  |  |  |
| 27 | `CE.SIC.CP.DATE.OF.BIRTH` | `CrsStaticInfoCopy_CpDateOfBirth` |  |  |  |
| 28 | `CE.SIC.CP.PLACE.OF.BIRTH` | `CrsStaticInfoCopy_CpPlaceOfBirth` |  |  |  |
| 29 | `CE.SIC.CP.RT.TAX.RESIDENCE` | `CrsStaticInfoCopy_CpRtTaxResidence` |  |  |  |
| 30 | `CE.SIC.CP.TIN` | `CrsStaticInfoCopy_CpTin` |  |  |  |
| 31 | `CE.SIC.CTRLG.PERSON.TYPE` | `CrsStaticInfoCopy_CtrlgPersonType` |  |  |  |
| 32 | `CE.SIC.CP.ADDRESS` | `CrsStaticInfoCopy_CpAddress` |  |  |  |
| 33 | `CE.SIC.CP.RT.ADDRESS.COUNTRY` | `CrsStaticInfoCopy_CpRtAddressCountry` |  |  |  |
| 34 | `CE.SIC.CP.RESERVED.05` | `CrsStaticInfoCopy_CpReserved05` |  |  |  |
| 35 | `CE.SIC.CP.RESERVED.04` | `CrsStaticInfoCopy_CpReserved04` |  |  |  |
| 36 | `CE.SIC.CP.RESERVED.03` | `CrsStaticInfoCopy_CpReserved03` |  |  |  |
| 37 | `CE.SIC.CP.RESERVED.02` | `CrsStaticInfoCopy_CpReserved02` |  |  |  |
| 38 | `CE.SIC.CP.RESERVED.01` | `CrsStaticInfoCopy_CpReserved01` |  |  |  |
| 39 | `CE.SIC.INDICIA` | `CrsStaticInfoCopy_Indicia` | TField |  | System will populate 'YES' if any of the indicia's are met or else 'NO'. |
| 40 | `CE.SIC.SC.DOC.STATUS` | `CrsStaticInfoCopy_ScDocStatus` | TField |  | This field will hold the value UNDOCUMENTED when the self-certification document is not submitted by the clienteven after the cut-off date. |
| 41 | `CE.SIC.REPORTING.JURISDICTION` | `CrsStaticInfoCopy_ReportingJurisdiction` |  |  |  |
| 42 | `CE.SIC.CRS.STATUS` | `CrsStaticInfoCopy_CrsStatus` |  |  |  |
| 43 | `CE.SIC.CHANGE.REASON` | `CrsStaticInfoCopy_ChangeReason` |  |  |  |
| 44 | `CE.SIC.RESERVED.50` | `CrsStaticInfoCopy_Reserved50` | TField |  |  |
| 45 | `CE.SIC.RESERVED.49` | `CrsStaticInfoCopy_Reserved49` | TField |  |  |
| 46 | `CE.SIC.RESERVED.48` | `CrsStaticInfoCopy_Reserved48` | TField |  |  |
| 47 | `CE.SIC.RESERVED.47` | `CrsStaticInfoCopy_Reserved47` | TField |  |  |
| 48 | `CE.SIC.RESERVED.46` | `CrsStaticInfoCopy_Reserved46` | TField |  |  |
| 49 | `CE.SIC.RESERVED.45` | `CrsStaticInfoCopy_Reserved45` | TField |  |  |
| 50 | `CE.SIC.RESERVED.44` | `CrsStaticInfoCopy_Reserved44` | TField |  |  |
| 51 | `CE.SIC.RESERVED.43` | `CrsStaticInfoCopy_Reserved43` | TField |  |  |
| 52 | `CE.SIC.RESERVED.42` | `CrsStaticInfoCopy_Reserved42` | TField |  |  |
| 53 | `CE.SIC.RESERVED.41` | `CrsStaticInfoCopy_Reserved41` | TField |  |  |
| 54 | `CE.SIC.RESERVED.40` | `CrsStaticInfoCopy_Reserved40` | TField |  |  |
| 55 | `CE.SIC.RESERVED.39` | `CrsStaticInfoCopy_Reserved39` | TField |  |  |
| 56 | `CE.SIC.RESERVED.38` | `CrsStaticInfoCopy_Reserved38` | TField |  |  |
| 57 | `CE.SIC.RESERVED.37` | `CrsStaticInfoCopy_Reserved37` | TField |  |  |
| 58 | `CE.SIC.RESERVED.36` | `CrsStaticInfoCopy_Reserved36` | TField |  |  |
| 59 | `CE.SIC.RESERVED.35` | `CrsStaticInfoCopy_Reserved35` | TField |  |  |
| 60 | `CE.SIC.RESERVED.34` | `CrsStaticInfoCopy_Reserved34` | TField |  |  |
| 61 | `CE.SIC.RESERVED.33` | `CrsStaticInfoCopy_Reserved33` | TField |  |  |
| 62 | `CE.SIC.RESERVED.32` | `CrsStaticInfoCopy_Reserved32` | TField |  |  |
| 63 | `CE.SIC.RESERVED.31` | `CrsStaticInfoCopy_Reserved31` | TField |  |  |
| 64 | `CE.SIC.RESERVED.30` | `CrsStaticInfoCopy_Reserved30` | TField |  |  |
| 65 | `CE.SIC.RESERVED.29` | `CrsStaticInfoCopy_Reserved29` | TField |  |  |
| 66 | `CE.SIC.RESERVED.28` | `CrsStaticInfoCopy_Reserved28` | TField |  |  |
| 67 | `CE.SIC.RESERVED.27` | `CrsStaticInfoCopy_Reserved27` | TField |  |  |
| 68 | `CE.SIC.RESERVED.26` | `CrsStaticInfoCopy_Reserved26` | TField |  |  |
| 69 | `CE.SIC.RESERVED.25` | `CrsStaticInfoCopy_Reserved25` | TField |  |  |
| 70 | `CE.SIC.RESERVED.24` | `CrsStaticInfoCopy_Reserved24` | TField |  |  |
| 71 | `CE.SIC.RESERVED.23` | `CrsStaticInfoCopy_Reserved23` | TField |  |  |
| 72 | `CE.SIC.RESERVED.22` | `CrsStaticInfoCopy_Reserved22` | TField |  |  |
| 73 | `CE.SIC.RESERVED.21` | `CrsStaticInfoCopy_Reserved21` | TField |  |  |
| 74 | `CE.SIC.RESERVED.20` | `CrsStaticInfoCopy_Reserved20` | TField |  |  |
| 75 | `CE.SIC.RESERVED.19` | `CrsStaticInfoCopy_Reserved19` | TField |  |  |
| 76 | `CE.SIC.RESERVED.18` | `CrsStaticInfoCopy_Reserved18` | TField |  |  |
| 77 | `CE.SIC.RESERVED.17` | `CrsStaticInfoCopy_Reserved17` | TField |  |  |
| 78 | `CE.SIC.RESERVED.16` | `CrsStaticInfoCopy_Reserved16` | TField |  |  |
| 79 | `CE.SIC.RESERVED.15` | `CrsStaticInfoCopy_Reserved15` | TField |  |  |
| 80 | `CE.SIC.RESERVED.14` | `CrsStaticInfoCopy_Reserved14` | TField |  |  |
| 81 | `CE.SIC.RESERVED.13` | `CrsStaticInfoCopy_Reserved13` | TField |  |  |
| 82 | `CE.SIC.RESERVED.12` | `CrsStaticInfoCopy_Reserved12` | TField |  |  |
| 83 | `CE.SIC.RESERVED.11` | `CrsStaticInfoCopy_Reserved11` | TField |  |  |
| 84 | `CE.SIC.RESERVED.10` | `CrsStaticInfoCopy_Reserved10` | TField |  |  |
| 85 | `CE.SIC.RESERVED.09` | `CrsStaticInfoCopy_Reserved09` | TField |  |  |
| 86 | `CE.SIC.RESERVED.08` | `CrsStaticInfoCopy_Reserved08` | TField |  |  |
| 87 | `CE.SIC.RESERVED.07` | `CrsStaticInfoCopy_Reserved07` | TField |  |  |
| 88 | `CE.SIC.RESERVED.06` | `CrsStaticInfoCopy_Reserved06` | TField |  |  |
| 89 | `CE.SIC.RESERVED.05` | `CrsStaticInfoCopy_Reserved05` | TField |  |  |
| 90 | `CE.SIC.RESERVED.04` | `CrsStaticInfoCopy_Reserved04` | TField |  |  |
| 91 | `CE.SIC.RESERVED.03` | `CrsStaticInfoCopy_Reserved03` | TField |  |  |
| 92 | `CE.SIC.RESERVED.02` | `CrsStaticInfoCopy_Reserved02` | TField |  |  |
| 93 | `CE.SIC.RESERVED.01` | `CrsStaticInfoCopy_Reserved01` | TField |  |  |
| 94 | `CE.SIC.LOCAL.REF` | `CrsStaticInfoCopy_LocalRef` |  |  |  |
| 95 | `CE.SIC.OVERRIDE` | `CrsStaticInfoCopy_Override` |  |  |  |
| 96 | `CE.SIC.RECORD.STATUS` | `CrsStaticInfoCopy_RecordStatus` | String |  |  |
| 97 | `CE.SIC.CURR.NO` | `CrsStaticInfoCopy_CurrNo` | String |  |  |
| 98 | `CE.SIC.INPUTTER` | `CrsStaticInfoCopy_Inputter` |  |  |  |
| 99 | `CE.SIC.DATE.TIME` | `CrsStaticInfoCopy_DateTime` |  |  |  |
| 100 | `CE.SIC.AUTHORISER` | `CrsStaticInfoCopy_Authoriser` | String |  |  |
| 101 | `CE.SIC.CO.CODE` | `CrsStaticInfoCopy_CoCode` | String |  |  |
| 102 | `CE.SIC.DEPT.CODE` | `CrsStaticInfoCopy_DeptCode` | String |  |  |
| 103 | `CE.SIC.AUDITOR.CODE` | `CrsStaticInfoCopy_AuditorCode` | String |  |  |
| 104 | `CE.SIC.AUDIT.DATE.TIME` | `CrsStaticInfoCopy_AuditDateTime` | String |  |  |
