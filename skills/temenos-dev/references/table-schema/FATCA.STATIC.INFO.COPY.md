# FATCA.STATIC.INFO.COPY — Table Schema

> Source: `INSERTS/I_F.FATCA.STATIC.INFO.COPY` in `FE_FatcaReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FE.SIC.DEFAULT.ADDRESS` | `FatcaStaticInfoCopy_DefaultAddress` | TField |  | The field specifies the application from which the client's address gets updated for reporting. The field will be updated from DEFAULT.ADDRESS field of FATCA.REPORTING.PARAMETER record |
| 2 | `FE.SIC.CLIENT.TYPE` | `FatcaStaticInfoCopy_ClientType` | TField |  | INDIVIDUAL or ORGANISATION based on whether the client is an individual or a legal entity. |
| 3 | `FE.SIC.NAME.1` | `FatcaStaticInfoCopy_Name1` | TField |  | The field will be updated from CUSTOMER record (first name). |
| 4 | `FE.SIC.NAME.2` | `FatcaStaticInfoCopy_Name2` | TField |  | The field will be updated from CUSTOMER record (last name) |
| 5 | `FE.SIC.SHORT.NAME` | `FatcaStaticInfoCopy_ShortName` | TField |  | The field will be updated from CUSTOMER record. |
| 6 | `FE.SIC.STREET` | `FatcaStaticInfoCopy_Street` | TField |  | The field will be updated from CUSTOMER (STREET) or DE.ADDRESS (STREET.ADDRESS) record based on FATCA.REPORTING.PARAMETER setting. |
| 7 | `FE.SIC.ADDRESS` | `FatcaStaticInfoCopy_Address` |  |  |  |
| 8 | `FE.SIC.TOWN.COUNTRY` | `FatcaStaticInfoCopy_TownCountry` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (TOWN.COUNTRY) based on FATCA.REPORTING.PARAMETER setting. |
| 9 | `FE.SIC.POST.CODE` | `FatcaStaticInfoCopy_PostCode` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (POST.CODE) based on FATCA.REPORTING.PARAMETER setting. |
| 10 | `FE.SIC.COUNTRY.SUB.ENTITY` | `FatcaStaticInfoCopy_CountrySubEntity` | TField |  | Specifies the sub entity's country details if present Contains the value of the field mentioned in CRS.REPORTING.PARAMETER's FIELD.REF.COU.SUB.ENT field . |
| 11 | `FE.SIC.COUNTRY` | `FatcaStaticInfoCopy_Country` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (COUNTRY). |
| 12 | `FE.SIC.SECTOR` | `FatcaStaticInfoCopy_Sector` | TField |  | Identifies the sector for customer The field will be updated from CUSTOMER record. Valid ID from SECTOR table |
| 13 | `FE.SIC.ACCOUNT.OFFICER` | `FatcaStaticInfoCopy_AccountOfficer` | TField |  | Identifies the account officer for customer The field will be updated from CUSTOMER record. Valid ID from DEPT.ACCT.OFFICER table |
| 14 | `FE.SIC.INDUSTRY` | `FatcaStaticInfoCopy_Industry` | TField |  | Identifies the industry to which customer belongs to The field will be updated from CUSTOMER record. Valid ID from INDUSTRY table |
| 15 | `FE.SIC.CUSTOMER.STATUS` | `FatcaStaticInfoCopy_CustomerStatus` | TField |  | Identifies the Status of the Customer The field will be updated from CUSTOMER record. Valid ID from CUSTOMER.STATUS table |
| 16 | `FE.SIC.NATIONALITY` | `FatcaStaticInfoCopy_Nationality` | TField |  | Identifies the nationality of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 17 | `FE.SIC.RESIDENCE` | `FatcaStaticInfoCopy_Residence` | TField |  | Identifies the residence of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 18 | `FE.SIC.DOMICILE` | `FatcaStaticInfoCopy_Domicile` | TField |  | Identifies the domicile of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 19 | `FE.SIC.COMPANY.BOOK` | `FatcaStaticInfoCopy_CompanyBook` | TField |  | This field holds the branch of the customer. Accepts the id of the COMPANY which shares customer with currently signed in company The field will be updated from CUSTOMER record. Valid ID from COMPANY table |
| 20 | `FE.SIC.TAX.DOMICILE` | `FatcaStaticInfoCopy_TaxDomicile` | TField |  | The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 21 | `FE.SIC.CITIZENSHIP` | `FatcaStaticInfoCopy_Citizenship` |  |  |  |
| 22 | `FE.SIC.TAX.RESIDENCE` | `FatcaStaticInfoCopy_TaxResidence` |  |  |  |
| 23 | `FE.SIC.TIN.COUNTRY` | `FatcaStaticInfoCopy_TinCountry` |  |  |  |
| 24 | `FE.SIC.TIN.CODE` | `FatcaStaticInfoCopy_TinCode` |  |  |  |
| 25 | `FE.SIC.INDICIA` | `FatcaStaticInfoCopy_Indicia` | TField |  | System will populate 'YES' if any of the indicia is met or else 'NO'. The field will be updated as Yes if Indicia Strength is not blank in FATCA.CUSTOMER.SUPPLEMENTARY.INFO. |
| 26 | `FE.SIC.RC.ROLE.TYPE` | `FatcaStaticInfoCopy_RcRoleType` |  |  |  |
| 27 | `FE.SIC.RC.ENT.TAX.CLASS` | `FatcaStaticInfoCopy_RcEntTaxClass` |  |  |  |
| 28 | `FE.SIC.RC.CUSTOMER.ID` | `FatcaStaticInfoCopy_RcCustomerId` |  |  |  |
| 29 | `FE.SIC.RC.HOLDER.REF` | `FatcaStaticInfoCopy_RcHolderRef` |  |  |  |
| 30 | `FE.SIC.RC.HOLDER.NAME` | `FatcaStaticInfoCopy_RcHolderName` |  |  |  |
| 31 | `FE.SIC.RC.SUR.NAME` | `FatcaStaticInfoCopy_RcSurName` |  |  |  |
| 32 | `FE.SIC.RC.FIRST.NAME` | `FatcaStaticInfoCopy_RcFirstName` |  |  |  |
| 33 | `FE.SIC.RC.ALIAS` | `FatcaStaticInfoCopy_RcAlias` |  |  |  |
| 34 | `FE.SIC.RC.NATIONALITY` | `FatcaStaticInfoCopy_RcNationality` |  |  |  |
| 35 | `FE.SIC.RC.RESIDENCE` | `FatcaStaticInfoCopy_RcResidence` |  |  |  |
| 36 | `FE.SIC.RC.DOMICILE` | `FatcaStaticInfoCopy_RcDomicile` |  |  |  |
| 37 | `FE.SIC.RC.ADDRESS` | `FatcaStaticInfoCopy_RcAddress` |  |  |  |
| 38 | `FE.SIC.RC.BIRTH.INCO.DATE` | `FatcaStaticInfoCopy_RcBirthIncoDate` |  |  |  |
| 39 | `FE.SIC.RC.PRCNT.OWNERSHIP` | `FatcaStaticInfoCopy_RcPrcntOwnership` |  |  |  |
| 40 | `FE.SIC.RC.HOLDER.TIN` | `FatcaStaticInfoCopy_RcHolderTin` |  |  |  |
| 41 | `FE.SIC.RC.JO.BO.STATUS` | `FatcaStaticInfoCopy_RcJoBoStatus` |  |  |  |
| 42 | `FE.SIC.RC.HOLD.ADDR.COUNTRY` | `FatcaStaticInfoCopy_RcHoldAddrCountry` |  |  |  |
| 43 | `FE.SIC.RC.HOLD.TIN.COUNTRY` | `FatcaStaticInfoCopy_RcHoldTinCountry` |  |  |  |
| 44 | `FE.SIC.RC.LEGAL.ENTITY.TYPE` | `FatcaStaticInfoCopy_RcLegalEntityType` |  |  |  |
| 45 | `FE.SIC.RC.RESERVED.5` | `FatcaStaticInfoCopy_RcReserved5` |  |  |  |
| 46 | `FE.SIC.RC.RESERVED.4` | `FatcaStaticInfoCopy_RcReserved4` |  |  |  |
| 47 | `FE.SIC.RC.RESERVED.3` | `FatcaStaticInfoCopy_RcReserved3` |  |  |  |
| 48 | `FE.SIC.RC.RESERVED.2` | `FatcaStaticInfoCopy_RcReserved2` |  |  |  |
| 49 | `FE.SIC.RC.RESERVED.1` | `FatcaStaticInfoCopy_RcReserved1` |  |  |  |
| 50 | `FE.SIC.STATUS.CHANGE.DATE` | `FatcaStaticInfoCopy_StatusChangeDate` | TField |  | The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 51 | `FE.SIC.STATUS.TYPE` | `FatcaStaticInfoCopy_StatusType` | TField |  | Field to hold the status of the customer as Reportable or Non-reportable. The field will be updated from the status type for the associated FATCA.STATUS from the FATCA.REPORTING.PARAMETER. |
| 52 | `FE.SIC.FATCA.STATUS` | `FatcaStaticInfoCopy_FatcaStatus` | TField |  | The field will be updated from field FATCA.STATUS in FATCA.CUSTOMER.SUPPLEMENTARY.INFO record. |
| 53 | `FE.SIC.CHANGE.REASON` | `FatcaStaticInfoCopy_ChangeReason` |  |  |  |
| 54 | `FE.SIC.RESERVED.50` | `FatcaStaticInfoCopy_Reserved50` | TField |  |  |
| 55 | `FE.SIC.RESERVED.49` | `FatcaStaticInfoCopy_Reserved49` | TField |  |  |
| 56 | `FE.SIC.RESERVED.48` | `FatcaStaticInfoCopy_Reserved48` | TField |  |  |
| 57 | `FE.SIC.RESERVED.47` | `FatcaStaticInfoCopy_Reserved47` | TField |  |  |
| 58 | `FE.SIC.RESERVED.46` | `FatcaStaticInfoCopy_Reserved46` | TField |  |  |
| 59 | `FE.SIC.RESERVED.45` | `FatcaStaticInfoCopy_Reserved45` | TField |  |  |
| 60 | `FE.SIC.RESERVED.44` | `FatcaStaticInfoCopy_Reserved44` | TField |  |  |
| 61 | `FE.SIC.RESERVED.43` | `FatcaStaticInfoCopy_Reserved43` | TField |  |  |
| 62 | `FE.SIC.RESERVED.42` | `FatcaStaticInfoCopy_Reserved42` | TField |  |  |
| 63 | `FE.SIC.RESERVED.41` | `FatcaStaticInfoCopy_Reserved41` | TField |  |  |
| 64 | `FE.SIC.RESERVED.40` | `FatcaStaticInfoCopy_Reserved40` | TField |  |  |
| 65 | `FE.SIC.RESERVED.39` | `FatcaStaticInfoCopy_Reserved39` | TField |  |  |
| 66 | `FE.SIC.RESERVED.38` | `FatcaStaticInfoCopy_Reserved38` | TField |  |  |
| 67 | `FE.SIC.RESERVED.37` | `FatcaStaticInfoCopy_Reserved37` | TField |  |  |
| 68 | `FE.SIC.RESERVED.36` | `FatcaStaticInfoCopy_Reserved36` | TField |  |  |
| 69 | `FE.SIC.RESERVED.35` | `FatcaStaticInfoCopy_Reserved35` | TField |  |  |
| 70 | `FE.SIC.RESERVED.34` | `FatcaStaticInfoCopy_Reserved34` | TField |  |  |
| 71 | `FE.SIC.RESERVED.33` | `FatcaStaticInfoCopy_Reserved33` | TField |  |  |
| 72 | `FE.SIC.RESERVED.32` | `FatcaStaticInfoCopy_Reserved32` | TField |  |  |
| 73 | `FE.SIC.RESERVED.31` | `FatcaStaticInfoCopy_Reserved31` | TField |  |  |
| 74 | `FE.SIC.RESERVED.30` | `FatcaStaticInfoCopy_Reserved30` | TField |  |  |
| 75 | `FE.SIC.RESERVED.29` | `FatcaStaticInfoCopy_Reserved29` | TField |  |  |
| 76 | `FE.SIC.RESERVED.28` | `FatcaStaticInfoCopy_Reserved28` | TField |  |  |
| 77 | `FE.SIC.RESERVED.27` | `FatcaStaticInfoCopy_Reserved27` | TField |  |  |
| 78 | `FE.SIC.RESERVED.26` | `FatcaStaticInfoCopy_Reserved26` | TField |  |  |
| 79 | `FE.SIC.RESERVED.25` | `FatcaStaticInfoCopy_Reserved25` | TField |  |  |
| 80 | `FE.SIC.RESERVED.24` | `FatcaStaticInfoCopy_Reserved24` | TField |  |  |
| 81 | `FE.SIC.RESERVED.23` | `FatcaStaticInfoCopy_Reserved23` | TField |  |  |
| 82 | `FE.SIC.RESERVED.22` | `FatcaStaticInfoCopy_Reserved22` | TField |  |  |
| 83 | `FE.SIC.RESERVED.21` | `FatcaStaticInfoCopy_Reserved21` | TField |  |  |
| 84 | `FE.SIC.RESERVED.20` | `FatcaStaticInfoCopy_Reserved20` | TField |  |  |
| 85 | `FE.SIC.RESERVED.19` | `FatcaStaticInfoCopy_Reserved19` | TField |  |  |
| 86 | `FE.SIC.RESERVED.18` | `FatcaStaticInfoCopy_Reserved18` | TField |  |  |
| 87 | `FE.SIC.RESERVED.17` | `FatcaStaticInfoCopy_Reserved17` | TField |  |  |
| 88 | `FE.SIC.RESERVED.16` | `FatcaStaticInfoCopy_Reserved16` | TField |  |  |
| 89 | `FE.SIC.RESERVED.15` | `FatcaStaticInfoCopy_Reserved15` | TField |  |  |
| 90 | `FE.SIC.RESERVED.14` | `FatcaStaticInfoCopy_Reserved14` | TField |  |  |
| 91 | `FE.SIC.RESERVED.13` | `FatcaStaticInfoCopy_Reserved13` | TField |  |  |
| 92 | `FE.SIC.RESERVED.12` | `FatcaStaticInfoCopy_Reserved12` | TField |  |  |
| 93 | `FE.SIC.RESERVED.11` | `FatcaStaticInfoCopy_Reserved11` | TField |  |  |
| 94 | `FE.SIC.RESERVED.10` | `FatcaStaticInfoCopy_Reserved10` | TField |  |  |
| 95 | `FE.SIC.RESERVED.09` | `FatcaStaticInfoCopy_Reserved09` | TField |  |  |
| 96 | `FE.SIC.RESERVED.08` | `FatcaStaticInfoCopy_Reserved08` | TField |  |  |
| 97 | `FE.SIC.RESERVED.07` | `FatcaStaticInfoCopy_Reserved07` | TField |  |  |
| 98 | `FE.SIC.RESERVED.06` | `FatcaStaticInfoCopy_Reserved06` | TField |  |  |
| 99 | `FE.SIC.RESERVED.05` | `FatcaStaticInfoCopy_Reserved05` | TField |  |  |
| 100 | `FE.SIC.RESERVED.04` | `FatcaStaticInfoCopy_Reserved04` | TField |  |  |
| 101 | `FE.SIC.RESERVED.03` | `FatcaStaticInfoCopy_Reserved03` | TField |  |  |
| 102 | `FE.SIC.RESERVED.02` | `FatcaStaticInfoCopy_Reserved02` | TField |  |  |
| 103 | `FE.SIC.RESERVED.01` | `FatcaStaticInfoCopy_Reserved01` |  |  |  |
| 104 | `FE.SIC.LOCAL.REF` | `FatcaStaticInfoCopy_LocalRef` |  |  |  |
| 105 | `FE.SIC.OVERRIDE` | `FatcaStaticInfoCopy_Override` |  |  |  |
| 106 | `FE.SIC.RECORD.STATUS` | `FatcaStaticInfoCopy_RecordStatus` | String |  |  |
| 107 | `FE.SIC.CURR.NO` | `FatcaStaticInfoCopy_CurrNo` | String |  |  |
| 108 | `FE.SIC.INPUTTER` | `FatcaStaticInfoCopy_Inputter` |  |  |  |
| 109 | `FE.SIC.DATE.TIME` | `FatcaStaticInfoCopy_DateTime` |  |  |  |
| 110 | `FE.SIC.AUTHORISER` | `FatcaStaticInfoCopy_Authoriser` | String |  |  |
| 111 | `FE.SIC.CO.CODE` | `FatcaStaticInfoCopy_CoCode` | String |  |  |
| 112 | `FE.SIC.DEPT.CODE` | `FatcaStaticInfoCopy_DeptCode` | String |  |  |
| 113 | `FE.SIC.AUDITOR.CODE` | `FatcaStaticInfoCopy_AuditorCode` | String |  |  |
| 114 | `FE.SIC.AUDIT.DATE.TIME` | `FatcaStaticInfoCopy_AuditDateTime` | String |  |  |
