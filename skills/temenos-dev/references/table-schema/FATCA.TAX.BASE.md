# FATCA.TAX.BASE — Table Schema

> Source: `INSERTS/I_F.FATCA.TAX.BASE` in `FE_FatcaReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FE.FTB.CUSTOMER` | `FatcaTaxBase_Customer` | TField |  | Customer number from the ID |
| 2 | `FE.FTB.STATUS.DATE` | `FatcaTaxBase_StatusDate` | TField |  | Date on which the base file is updated. |
| 3 | `FE.FTB.BASE.YEAR` | `FatcaTaxBase_BaseYear` | TField |  | Year to which the base data pertains to. The field will be taken from the ID. |
| 4 | `FE.FTB.CLIENT.TYPE` | `FatcaTaxBase_ClientType` | TField |  | INDIVIDUAL or ORGANISATION based on whether the client is an individual or a legal entity. |
| 5 | `FE.FTB.NAME.1` | `FatcaTaxBase_Name1` | TField |  | The field will be updated from CUSTOMER record (first name). |
| 6 | `FE.FTB.NAME.2` | `FatcaTaxBase_Name2` | TField |  | The field will be updated from CUSTOMER record (last name) |
| 7 | `FE.FTB.SHORT.NAME` | `FatcaTaxBase_ShortName` | TField |  | The field will be updated from CUSTOMER record. |
| 8 | `FE.FTB.STREET` | `FatcaTaxBase_Street` | TField |  | The field will be updated from CUSTOMER (STREET) or DE.ADDRESS (STREET.ADDRESS) record based on FATCA.REPORTING.PARAMETER setting. |
| 9 | `FE.FTB.ADDRESS` | `FatcaTaxBase_Address` |  |  |  |
| 10 | `FE.FTB.TOWN.COUNTRY` | `FatcaTaxBase_TownCountry` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (TOWN.COUNTRY) based on FATCA.REPORTING.PARAMETER setting. |
| 11 | `FE.FTB.POST.CODE` | `FatcaTaxBase_PostCode` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (POST.CODE) based on FATCA.REPORTING.PARAMETER setting. |
| 12 | `FE.FTB.COUNTRY.SUB.ENTITY` | `FatcaTaxBase_CountrySubEntity` | TField |  | This field specifies the sub entity's country details if present The field is the country sub entity updated from field in CUSTOMER or DE.ADDRESS record based on the reporting parameter setting. |
| 13 | `FE.FTB.COUNTRY` | `FatcaTaxBase_Country` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (COUNTRY). |
| 14 | `FE.FTB.SECTOR` | `FatcaTaxBase_Sector` | TField |  | This field specifies the sector for customer The field will be updated from CUSTOMER record. Valid ID from SECTOR table |
| 15 | `FE.FTB.ACCOUNT.OFFICER` | `FatcaTaxBase_AccountOfficer` | TField |  | This field specifies the account officer for customer The field will be updated from CUSTOMER record. Valid ID from DEPT.ACCT.OFFICER table |
| 16 | `FE.FTB.INDUSTRY` | `FatcaTaxBase_Industry` | TField |  | This field specifies the industry to which customer belongs to The field will be updated from CUSTOMER record. Valid ID from INDUSTRY table |
| 17 | `FE.FTB.CUSTOMER.STATUS` | `FatcaTaxBase_CustomerStatus` | TField |  | This field specifies the Status of the Customer The field will be updated from CUSTOMER record. Valid ID from CUSTOMER.STATUS table |
| 18 | `FE.FTB.NATIONALITY` | `FatcaTaxBase_Nationality` | TField |  | This field specifies the nationality of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 19 | `FE.FTB.RESIDENCE` | `FatcaTaxBase_Residence` | TField |  | This field specifies the residence of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 20 | `FE.FTB.DOMICILE` | `FatcaTaxBase_Domicile` | TField |  | This field specifies the domicile of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 21 | `FE.FTB.COMPANY.BOOK` | `FatcaTaxBase_CompanyBook` | TField |  | This field holds the branch of the customer. Accepts the id of the COMPANY which shares customer with currently signed in company The field will be updated from CUSTOMER record. Valid ID from COMPANY table |
| 22 | `FE.FTB.BIRTH.INCORP.DATE` | `FatcaTaxBase_BirthIncorpDate` | TField |  | This field specifies the Birth date/Incorporation date of the customer. The field will be updated from CUSTOMER record. |
| 23 | `FE.FTB.US.PLACE.OF.BIRTH` | `FatcaTaxBase_UsPlaceOfBirth` | TField |  | This field specifies the Birth place of the customer. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 24 | `FE.FTB.TAX.DOMICILE` | `FatcaTaxBase_TaxDomicile` | TField |  | This field specifies the tax domicile of the Customer The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 25 | `FE.FTB.CITIZENSHIP` | `FatcaTaxBase_Citizenship` |  |  |  |
| 26 | `FE.FTB.GREENCARD` | `FatcaTaxBase_Greencard` | TField |  | This field specifies the Greencard details of the Customer The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 27 | `FE.FTB.TAX.RESIDENCE` | `FatcaTaxBase_TaxResidence` | TField |  | This field specifies the Tax Residence of the customer. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record., if present, otherwise updated from the RESIDENCE field of CUSTOMER record. |
| 28 | `FE.FTB.TIN.COUNTRY` | `FatcaTaxBase_TinCountry` |  |  |  |
| 29 | `FE.FTB.TIN.CODE` | `FatcaTaxBase_TinCode` |  |  |  |
| 30 | `FE.FTB.EIN` | `FatcaTaxBase_Ein` | TField |  | This field specifies the Employer Identification Number of the Financial Institution. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 31 | `FE.FTB.SOCIAL.SEC.NO` | `FatcaTaxBase_SocialSecNo` | TField |  | This field specifies the Social Security Number of the customer. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 32 | `FE.FTB.GIIN` | `FatcaTaxBase_Giin` | TField |  | This field specifies the Global Intermediary Identification Number of the Financial Institution. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. If GIIN is blank then value is updated from the field FORM.TYPE which is set as document. |
| 33 | `FE.FTB.SPONSOR.GIIN` | `FatcaTaxBase_SponsorGiin` | TField |  | This field specifies the Global Intermediary Identification Number of the Sponsored entities. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 34 | `FE.FTB.SELF.CLASS` | `FatcaTaxBase_SelfClass` | TField |  | This field specifies the self-classification received from entities. The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 35 | `FE.FTB.RELATION.CUST` | `FatcaTaxBase_RelationCust` |  |  |  |
| 36 | `FE.FTB.RELATION.CODE` | `FatcaTaxBase_RelationCode` |  |  |  |
| 37 | `FE.FTB.REL.CUST.NAME.1` | `FatcaTaxBase_RelCustName1` |  |  |  |
| 38 | `FE.FTB.REL.CUST.NAME.2` | `FatcaTaxBase_RelCustName2` |  |  |  |
| 39 | `FE.FTB.REL.ALIAS` | `FatcaTaxBase_RelAlias` |  |  |  |
| 40 | `FE.FTB.ROLE.TYPE` | `FatcaTaxBase_RoleType` |  |  |  |
| 41 | `FE.FTB.REL.NATIONALITY` | `FatcaTaxBase_RelNationality` |  |  |  |
| 42 | `FE.FTB.REL.RESIDENCE` | `FatcaTaxBase_RelResidence` |  |  |  |
| 43 | `FE.FTB.REL.DOMICILE` | `FatcaTaxBase_RelDomicile` |  |  |  |
| 44 | `FE.FTB.REL.STREET` | `FatcaTaxBase_RelStreet` |  |  |  |
| 45 | `FE.FTB.REL.ADDRESS` | `FatcaTaxBase_RelAddress` |  |  |  |
| 46 | `FE.FTB.REL.TOWN.COUNTRY` | `FatcaTaxBase_RelTownCountry` |  |  |  |
| 47 | `FE.FTB.REL.POST.CODE` | `FatcaTaxBase_RelPostCode` |  |  |  |
| 48 | `FE.FTB.REL.COUNTRY` | `FatcaTaxBase_RelCountry` |  |  |  |
| 49 | `FE.FTB.REL.CNTY.SUB.ENT` | `FatcaTaxBase_RelCntySubEnt` |  |  |  |
| 50 | `FE.FTB.REL.BIRTH.DATE` | `FatcaTaxBase_RelBirthDate` |  |  |  |
| 51 | `FE.FTB.REL.OWN.PERC` | `FatcaTaxBase_RelOwnPerc` |  |  |  |
| 52 | `FE.FTB.REL.CUST.TIN` | `FatcaTaxBase_RelCustTin` |  |  |  |
| 53 | `FE.FTB.REL.ADDR.COUNTRY` | `FatcaTaxBase_RelAddrCountry` |  |  |  |
| 54 | `FE.FTB.REL.TIN.COUNTRY` | `FatcaTaxBase_RelTinCountry` |  |  |  |
| 55 | `FE.FTB.REL.ENTITY.TYPE` | `FatcaTaxBase_RelEntityType` |  |  |  |
| 56 | `FE.FTB.REL.FATCA.STATUS` | `FatcaTaxBase_RelFatcaStatus` |  |  |  |
| 57 | `FE.FTB.REL.CUST.TIN.TYPE` | `FatcaTaxBase_RelCustTinType` |  |  |  |
| 58 | `FE.FTB.REL.RESERVED.4` | `FatcaTaxBase_RelReserved4` |  |  |  |
| 59 | `FE.FTB.REL.RESERVED.3` | `FatcaTaxBase_RelReserved3` |  |  |  |
| 60 | `FE.FTB.REL.RESERVED.2` | `FatcaTaxBase_RelReserved2` |  |  |  |
| 61 | `FE.FTB.REL.RESERVED.1` | `FatcaTaxBase_RelReserved1` |  |  |  |
| 62 | `FE.FTB.INDICIA` | `FatcaTaxBase_Indicia` | TField |  | System will populate 'YES' if any of the indicia is met or else 'NO'. The field will be updated as Yes if Indicia Strength is not blank in FATCA.CUSTOMER.SUPPLEMENTARY.INFO. |
| 63 | `FE.FTB.FATCA.STATUS` | `FatcaTaxBase_FatcaStatus` | TField |  | The field will be updated from field FATCA.STATUS in FATCA.CUSTOMER.SUPPLEMENTARY.INFO record. |
| 64 | `FE.FTB.STATUS.NARRATIVE` | `FatcaTaxBase_StatusNarrative` | TField |  | The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 65 | `FE.FTB.STATUS.CHANGE.DATE` | `FatcaTaxBase_StatusChangeDate` | TField |  | The field will be updated from FATCA.CUSTOMER.SUPPLEMENTARY.INFO (FCSI) record. |
| 66 | `FE.FTB.STATUS.TYPE` | `FatcaTaxBase_StatusType` | TField |  | Field to hold the status of the customer as Reportable or Non-reportable. The field will be updated from the status type for the associated FATCA.STATUS from the FATCA.REPORTING.PARAMETER. |
| 67 | `FE.FTB.ACCOUNT` | `FatcaTaxBase_Account` |  |  |  |
| 68 | `FE.FTB.ACC.OPEN.DATE` | `FatcaTaxBase_AccOpenDate` |  |  |  |
| 69 | `FE.FTB.ACCOUNT.TYPE` | `FatcaTaxBase_AccountType` |  |  |  |
| 70 | `FE.FTB.ACCT.PORT.CCY` | `FatcaTaxBase_AcctPortCcy` |  |  |  |
| 71 | `FE.FTB.ACC.BALANCE` | `FatcaTaxBase_AccBalance` |  |  |  |
| 72 | `FE.FTB.ACC.EXCH.RATE` | `FatcaTaxBase_AccExchRate` |  |  |  |
| 73 | `FE.FTB.ACC.BAL.USD` | `FatcaTaxBase_AccBalUsd` |  |  |  |
| 74 | `FE.FTB.REPORTNG.CCY` | `FatcaTaxBase_ReportngCcy` |  |  |  |
| 75 | `FE.FTB.REPORTNG.BAL` | `FatcaTaxBase_ReportngBal` |  |  |  |
| 76 | `FE.FTB.ACC.ACCOUNT.REF` | `FatcaTaxBase_AccAccountRef` |  |  |  |
| 77 | `FE.FTB.ACC.ACCOUNT.ACTION` | `FatcaTaxBase_AccAccountAction` |  |  |  |
| 78 | `FE.FTB.PAYMENT.TYPE` | `FatcaTaxBase_PaymentType` |  |  |  |
| 79 | `FE.FTB.PAYMENT.AMT` | `FatcaTaxBase_PaymentAmt` |  |  |  |
| 80 | `FE.FTB.USD.PAYMENT.AMT` | `FatcaTaxBase_UsdPaymentAmt` |  |  |  |
| 81 | `FE.FTB.REP.PYMT.TYPE` | `FatcaTaxBase_RepPymtType` |  |  |  |
| 82 | `FE.FTB.REP.PYMT.CCY` | `FatcaTaxBase_RepPymtCcy` |  |  |  |
| 83 | `FE.FTB.CON.PYMT.AMT` | `FatcaTaxBase_ConPymtAmt` |  |  |  |
| 84 | `FE.FTB.CON.USD.PYMT.AMT` | `FatcaTaxBase_ConUsdPymtAmt` |  |  |  |
| 85 | `FE.FTB.ACC.CORRECTION.STATUS` | `FatcaTaxBase_AccCorrectionStatus` |  |  |  |
| 86 | `FE.FTB.ACC.CRCT.ACCOUNT.REF` | `FatcaTaxBase_AccCrctAccountRef` |  |  |  |
| 87 | `FE.FTB.ACC.MERGE.ACCOUNT.REF` | `FatcaTaxBase_AccMergeAccountRef` |  |  |  |
| 88 | `FE.FTB.TOT.ACC.BAL.DEP` | `FatcaTaxBase_TotAccBalDep` | TField |  | The field will be updated from FATCA.AGGREGATE.BALANCE record. |
| 89 | `FE.FTB.TOT.ACC.BAL.CUST` | `FatcaTaxBase_TotAccBalCust` | TField |  | The field will be updated from FATCA.AGGREGATE.BALANCE record. |
| 90 | `FE.FTB.EXISTING.NEW` | `FatcaTaxBase_ExistingNew` | TField |  | Based on the list of client types allowed in FATCA.CUSTOMER.SUPPLEMENTARY.INFO,for the client types Individual, Small Account and High Value account, will be updated as 'EXISTING' if Customer Since (field in Customer) field is blank or less than 1st July 2014 and for rest, if less than 1st Jan 2015. If condition not satisfied, update as 'NEW'. |
| 91 | `FE.FTB.REPORT.TYPE` | `FatcaTaxBase_ReportType` | TField |  | Based on the request From FATCA.XML.REQUEST Will be updated as FATCA1 -NEW, FATCA2-CORRECTION, FATCA3-VOID, FATCA4-AMEND. |
| 92 | `FE.FTB.TRANS.COUNTRY` | `FatcaTaxBase_TransCountry` | TField |  | The field will be updated from the field LOCAL.COUNTRY in COMPANY record. |
| 93 | `FE.FTB.REC.COUNTRY` | `FatcaTaxBase_RecCountry` | TField |  | The field will be same as the TRANS.COUNTRY if status field from FATCA.PARAMETER equals IGA1 otherwise updated as US. |
| 94 | `FE.FTB.TIMESTAMP` | `FatcaTaxBase_Timestamp` | TField |  | Time of the request for generating xml will be updated. |
| 95 | `FE.FTB.COM.NAME` | `FatcaTaxBase_ComName` | TField |  | The field will be updated from the field COMPANY.NAME in COMPANY record. |
| 96 | `FE.FTB.COM.ADDRESS` | `FatcaTaxBase_ComAddress` |  |  |  |
| 97 | `FE.FTB.COM.TIN` | `FatcaTaxBase_ComTin` | TField |  | The field will be updated from the field EIN in FATCA.PARAMETER record. |
| 98 | `FE.FTB.MSG.REF.ID` | `FatcaTaxBase_MsgRefId` | TField |  | The field will be updated as FATCA.TAX.BASE.ID.SEQ.NO (seq.no will be 1 for the new record). |
| 99 | `FE.FTB.CRCTD.MSG.REF.ID` | `FatcaTaxBase_CrctdMsgRefId` | TField |  | The field is used for updating the amended message reference. |
| 100 | `FE.FTB.ACCT.HOLDER.TYPE` | `FatcaTaxBase_AcctHolderType` | TField |  | This data element identifies an entity account holder or payee that is: (1) an owner documented FI with specified US owner(s); (2) a passive NFFE with substantial or controlling US owner(s); (3) a nonparticipating FFI; or (4) a Specified US person. FATCA101 - If the FATCA STATUS of the entity is Owner Documented FI (identified based on Status Type and FATCA.STATUS in FATCA Reporting Parameter) FATCA102 - If the FATCA STATUS of the entity is Passive NFFE (identified based on Status Type and FATCA.STATUS in FATCA Reporting Parameter) FATCA103 - If the FATCA STATUS of the entity is Non-Participating FFI (identified based on Status Type and FATCA.STATUS in FATCA Reporting Parameter) FATCA104 - If the FATCA STATUS in the base record is same as SPEC_US_Person status in FATCA.REPORTING.PARAMETER. FATCA105 - If the FATCA STATUS in the entity is Direct Reporting NFFE (DR_NFFE identified based on Status Type and FATCA.STATUS in FATCA Reporting Parameter) |
| 101 | `FE.FTB.FI.RETURN.REF` | `FatcaTaxBase_FiReturnRef` | TField |  | The field will be updated from the field FI.RETURN.REF in FATCA.POOL.BALANCE record. |
| 102 | `FE.FTB.FI.RETURN.ACTION` | `FatcaTaxBase_FiReturnAction` | TField |  | The field will be updated from the field FI.RETURN.ACTION in FATCA.POOL.BALANCE record. |
| 103 | `FE.FTB.DUE.DILIGENCE.IND` | `FatcaTaxBase_DueDiligenceInd` | TField |  | The field used to define whether an account is a Reportable Account or an account held by a Non-participating Financial Institution. The field will be updated from the field DUE.DILIGENCE.IND in FATCA.REPORTING.PARAMETER record. |
| 104 | `FE.FTB.THRESHOLD.IND` | `FatcaTaxBase_ThresholdInd` | TField |  | The field used to define the thresholds in the due diligence process. The field will be updated from the field THRESHOLD.IND in FATCA.REPORTING.PARAMETER record. |
| 105 | `FE.FTB.FI.REGISTER.ID` | `FatcaTaxBase_FiRegisterId` | TField |  | The field used to indicates the first three digits of the FI's (Financial Institution) name. The field will be updated from the field FI.REGISTER.ID in FATCA.POOL.BALANCE record. |
| 106 | `FE.FTB.TIN.CODE.TYPE` | `FatcaTaxBase_TinCodeType` | TField |  | The field used to define the TIN.CODE.TYPE as ITIN for individuals and EIN for Entities.If GIIN is present,the field is updated as other. |
| 107 | `FE.FTB.FATCA.USER.ID` | `FatcaTaxBase_FatcaUserId` | TField |  | The field used to define the FATCA.ID which is populated from FATCA.REPORTING.PARAMETER |
| 108 | `FE.FTB.FILER.CATEGORY` | `FatcaTaxBase_FilerCategory` | TField |  | The field will be updated from the field FILER.CATEGORY in FATCA.REPORTING.PARAMETER record. The field contains the category of reporting financial institution to be reported in FATCA XML report. |
| 109 | `FE.FTB.ACCOUNT.CLOSED` | `FatcaTaxBase_AccountClosed` | TField |  | The field indicates whether the FATCA.CUSTOMER.SUPPLEMENTARY.INFO become INACTIVE. |
| 110 | `FE.FTB.NO.ACCTS.TO.REP` | `FatcaTaxBase_NoAcctsToRep` | TField |  | The field used to record the status if there are any accounts to report |
