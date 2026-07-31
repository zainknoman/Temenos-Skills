# CRS.REPORT.BASE — Table Schema

> Source: `INSERTS/I_F.CRS.REPORT.BASE` in `CE_CrsReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CE.CRB.CUSTOMER.ID` | `CrsReportBase_CustomerId` | TField |  | Customer number from the ID |
| 2 | `CE.CRB.STATUS.DATE` | `CrsReportBase_StatusDate` | TField |  | Date on which the base file is updated. |
| 3 | `CE.CRB.REPORTING.YEAR` | `CrsReportBase_ReportingYear` | TField |  | Year to which the base data pertains to. The field will be taken from the ID. |
| 4 | `CE.CRB.CLIENT.TYPE` | `CrsReportBase_ClientType` | TField |  | INDIVIDUAL or ORGANISATION based on whether the client is an individual or a legal entity. |
| 5 | `CE.CRB.NAME.1` | `CrsReportBase_Name1` | TField |  | The field will be updated from CUSTOMER record (first name). |
| 6 | `CE.CRB.NAME.2` | `CrsReportBase_Name2` | TField |  | The field will be updated from CUSTOMER record (last name). |
| 7 | `CE.CRB.SHORT.NAME` | `CrsReportBase_ShortName` | TField |  | The field will be updated from CUSTOMER record. |
| 8 | `CE.CRB.STREET` | `CrsReportBase_Street` | TField |  | The field will be updated from CUSTOMER (STREET) or DE.ADDRESS (STREET ADDRESS) record based onCRS.REPORTING.PARAMETER setting. |
| 9 | `CE.CRB.ADDRESS` | `CrsReportBase_Address` |  |  |  |
| 10 | `CE.CRB.TOWN.COUNTRY` | `CrsReportBase_TownCountry` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (TOWN COUNTRY) based on CRS.REPORTING.PARAMETERsetting. |
| 11 | `CE.CRB.POST.CODE` | `CrsReportBase_PostCode` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (POST CODE) based on CRS.REPORTING.PARAMETERsetting. |
| 12 | `CE.CRB.COUNTRY.SUB.ENTITY` | `CrsReportBase_CountrySubEntity` | TField |  | Specifies the sub entity's country details if present Contains the value of the field mentioned in CRS.REPORTING.PARAMETER's FIELD.REF.COU.SUB.ENT field . |
| 13 | `CE.CRB.COUNTRY` | `CrsReportBase_Country` | TField |  | The field will be updated from CUSTOMER or DE.ADDRESS record (COUNTRY). |
| 14 | `CE.CRB.SECTOR` | `CrsReportBase_Sector` | TField |  | Identifies the sector for customer The field will be updated from CUSTOMER record. Valid ID from SECTOR table |
| 15 | `CE.CRB.ACCOUNT.OFFICER` | `CrsReportBase_AccountOfficer` | TField |  | Identifies the account officer for customer The field will be updated from CUSTOMER record. Valid ID from DEPT.ACCT.OFFICER table |
| 16 | `CE.CRB.INDUSTRY` | `CrsReportBase_Industry` | TField |  | Identifies the industry to which customer belongs to The field will be updated from CUSTOMER record. Valid ID from INDUSTRY table |
| 17 | `CE.CRB.CUSTOMER.STATUS` | `CrsReportBase_CustomerStatus` | TField |  | Identifies the Status of the Customer The field will be updated from CUSTOMER record. Valid ID from CUSTOMER.STATUS table |
| 18 | `CE.CRB.NATIONALITY` | `CrsReportBase_Nationality` | TField |  | Identifies the nationality of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 19 | `CE.CRB.RESIDENCE` | `CrsReportBase_Residence` | TField |  | Identifies the residence of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 20 | `CE.CRB.DOMICILE` | `CrsReportBase_Domicile` | TField |  | Identifies the domicile of the Customer The field will be updated from CUSTOMER record. Valid ID from COUNTRY table |
| 21 | `CE.CRB.COMPANY.BOOK` | `CrsReportBase_CompanyBook` | TField |  | This field holds the branch of the customer. Accepts the id of the COMPANY which shares customer with currentlysigned in company The field will be updated from CUSTOMER record. Valid ID from COMPANY table |
| 22 | `CE.CRB.BIRTH.INCORP.DATE` | `CrsReportBase_BirthIncorpDate` | TField |  |  |
| 23 | `CE.CRB.TAX.RESIDENCE` | `CrsReportBase_TaxResidence` |  |  |  |
| 24 | `CE.CRB.TIN.COUNTRY` | `CrsReportBase_TinCountry` |  |  |  |
| 25 | `CE.CRB.TIN.CODE` | `CrsReportBase_TinCode` |  |  |  |
| 26 | `CE.CRB.EIN` | `CrsReportBase_Ein` | TField |  | Field to specify the Employer Identification Number of the Financial Institution. |
| 27 | `CE.CRB.CP.CUST` | `CrsReportBase_CpCust` |  |  |  |
| 28 | `CE.CRB.CP.CUST.NAME.ONE` | `CrsReportBase_CpCustNameOne` |  |  |  |
| 29 | `CE.CRB.CP.CUST.NAME.TWO` | `CrsReportBase_CpCustNameTwo` |  |  |  |
| 30 | `CE.CRB.ROLE.TYPE` | `CrsReportBase_RoleType` |  |  |  |
| 31 | `CE.CRB.CP.NATIONALITY` | `CrsReportBase_CpNationality` |  |  |  |
| 32 | `CE.CRB.CP.CUST.TIN` | `CrsReportBase_CpCustTin` |  |  |  |
| 33 | `CE.CRB.CP.TIN.COUNTRY` | `CrsReportBase_CpTinCountry` |  |  |  |
| 34 | `CE.CRB.CP.STREET` | `CrsReportBase_CpStreet` |  |  |  |
| 35 | `CE.CRB.CP.ADDRESS` | `CrsReportBase_CpAddress` |  |  |  |
| 36 | `CE.CRB.CP.TOWN.COUNTRY` | `CrsReportBase_CpTownCountry` |  |  |  |
| 37 | `CE.CRB.CP.POST.CODE` | `CrsReportBase_CpPostCode` |  |  |  |
| 38 | `CE.CRB.CP.COUNTRY.SUB.ENTITY` | `CrsReportBase_CpCountrySubEntity` |  |  |  |
| 39 | `CE.CRB.CP.COUNTRY` | `CrsReportBase_CpCountry` |  |  |  |
| 40 | `CE.CRB.CP.BIRTH.DATE` | `CrsReportBase_CpBirthDate` |  |  |  |
| 41 | `CE.CRB.CTRLG.PERSON.TYPE` | `CrsReportBase_CtrlgPersonType` |  |  |  |
| 42 | `CE.CRB.REL.RESERVED.5` | `CrsReportBase_RelReserved5` |  |  |  |
| 43 | `CE.CRB.REL.RESERVED.4` | `CrsReportBase_RelReserved4` |  |  |  |
| 44 | `CE.CRB.REL.RESERVED.3` | `CrsReportBase_RelReserved3` |  |  |  |
| 45 | `CE.CRB.REL.RESERVED.2` | `CrsReportBase_RelReserved2` |  |  |  |
| 46 | `CE.CRB.REL.RESERVED.1` | `CrsReportBase_RelReserved1` |  |  |  |
| 47 | `CE.CRB.INDICIA` | `CrsReportBase_Indicia` | TField |  | System will populate 'YES' if any of the indicia is met or else 'NO'. The field will be updated from CRS.CUST.SUPP.INFO record |
| 48 | `CE.CRB.SC.DOC.STATUS` | `CrsReportBase_ScDocStatus` | TField |  | This field will hold the value UNDOCUMENTED when the self-certification document is not submitted by the clienteven after the cut-off date. The field will be updated from CRS.CUST.SUPP.INFO record |
| 49 | `CE.CRB.REPORTING.JURISDICTION` | `CrsReportBase_ReportingJurisdiction` |  |  |  |
| 50 | `CE.CRB.CRS.STATUS` | `CrsReportBase_CrsStatus` |  |  |  |
| 51 | `CE.CRB.ACCOUNT` | `CrsReportBase_Account` |  |  |  |
| 52 | `CE.CRB.ACC.OPEN.DATE` | `CrsReportBase_AccOpenDate` |  |  |  |
| 53 | `CE.CRB.ACCOUNT.TYPE` | `CrsReportBase_AccountType` |  |  |  |
| 54 | `CE.CRB.ACCT.PORT.CCY` | `CrsReportBase_AcctPortCcy` |  |  |  |
| 55 | `CE.CRB.ACC.BALANCE` | `CrsReportBase_AccBalance` |  |  |  |
| 56 | `CE.CRB.ACC.EXCH.RATE` | `CrsReportBase_AccExchRate` |  |  |  |
| 57 | `CE.CRB.ACC.BAL.USD` | `CrsReportBase_AccBalUsd` |  |  |  |
| 58 | `CE.CRB.REPORTNG.CCY` | `CrsReportBase_ReportngCcy` |  |  |  |
| 59 | `CE.CRB.REPORTNG.BAL` | `CrsReportBase_ReportngBal` |  |  |  |
| 60 | `CE.CRB.ACC.ACCOUNT.REF` | `CrsReportBase_AccAccountRef` |  |  |  |
| 61 | `CE.CRB.ACC.ACCOUNT.ACTION` | `CrsReportBase_AccAccountAction` |  |  |  |
| 62 | `CE.CRB.PAYMENT.TYPE` | `CrsReportBase_PaymentType` |  |  |  |
| 63 | `CE.CRB.PAYMENT.AMT` | `CrsReportBase_PaymentAmt` |  |  |  |
| 64 | `CE.CRB.RCY.PAYMENT.AMT` | `CrsReportBase_RcyPaymentAmt` |  |  |  |
| 65 | `CE.CRB.REP.PYMT.TYPE` | `CrsReportBase_RepPymtType` |  |  |  |
| 66 | `CE.CRB.RESERVED.1` | `CrsReportBase_Reserved1` |  |  |  |
| 67 | `CE.CRB.CON.PYMT.AMT` | `CrsReportBase_ConPymtAmt` |  |  |  |
| 68 | `CE.CRB.CON.RCY.PYMT.AMT` | `CrsReportBase_ConRcyPymtAmt` |  |  |  |
| 69 | `CE.CRB.ACC.DOC.TYPE.INDIC` | `CrsReportBase_AccDocTypeIndic` |  |  |  |
| 70 | `CE.CRB.ACC.CRCTD.ACCOUNT.REF` | `CrsReportBase_AccCrctdAccountRef` |  |  |  |
| 71 | `CE.CRB.ACC.CORRECTION.STATUS` | `CrsReportBase_AccCorrectionStatus` |  |  |  |
| 72 | `CE.CRB.ACC.RESERVED.2` | `CrsReportBase_AccReserved2` |  |  |  |
| 73 | `CE.CRB.ACC.RESERVED.1` | `CrsReportBase_AccReserved1` |  |  |  |
| 74 | `CE.CRB.TOT.ACC.BAL.DEP` | `CrsReportBase_TotAccBalDep` | TField |  | Field to hold the Total depository balance of the customer. The field will be updated from ST.AGGREGATE.BALANCES record |
| 75 | `CE.CRB.TOT.ACC.BAL.CUST` | `CrsReportBase_TotAccBalCust` | TField |  | Field to hold the Total Custodial balance of the customer. The field will be updated from ST.AGGREGATE.BALANCES record |
| 76 | `CE.CRB.EXISTING.NEW` | `CrsReportBase_ExistingNew` | TField |  | Field to hold the customer type as Existing/New. Identified based on CUSTOMER.SINCE field in Customer record. If Customer Since field value is blank or less than1st January 2016, will be updated as EXISTING, otherwise NEW. |
| 77 | `CE.CRB.REPORT.TYPE` | `CrsReportBase_ReportType` | TField |  | Field to hold the Report type, updated based on the request type defined in CRS.XML.REQUEST Values are: OECD1 - New Report OECD2 - Correction Report OECD3 - Deletion Report OECD0 - No change in ReportingFI information |
| 78 | `CE.CRB.TRANS.COUNTRY` | `CrsReportBase_TransCountry` | TField |  | The field will be updated from the field LOCAL.COUNTRY in COMPANY record. |
| 79 | `CE.CRB.REC.COUNTRY` | `CrsReportBase_RecCountry` | TField |  | The field specifies the Receiving country to which the report will be sent. |
| 80 | `CE.CRB.TIMESTAMP` | `CrsReportBase_Timestamp` | TField |  | The field will be updated with the time of generation of XML report. |
| 81 | `CE.CRB.COM.NAME` | `CrsReportBase_ComName` | TField |  | The field will be updated from the field COMPANY.NAME in COMPANY record. |
| 82 | `CE.CRB.COM.ADDRESS` | `CrsReportBase_ComAddress` |  |  |  |
| 83 | `CE.CRB.COM.TIN` | `CrsReportBase_ComTin` | TField |  | The field will be updated from the field EIN in CRS.PARAMETER record. |
| 84 | `CE.CRB.MSG.REF.ID` | `CrsReportBase_MsgRefId` | TField |  | The field will be updated with unique Message Reference ID for the report. Format - CRS.REPORT.BASE.ID.SEQNO.TIME |
| 85 | `CE.CRB.CRCTD.MSG.REF.ID` | `CrsReportBase_CrctdMsgRefId` | TField |  | The field will be updated with Corrected Message Reference ID for correction report. |
| 86 | `CE.CRB.ACCT.HOLDER.TYPE` | `CrsReportBase_AcctHolderType` | TField |  | The field will be updated with Account Holder type from the field CRS.CODE in CRS.CLIENT.TYPE record. |
| 87 | `CE.CRB.DORMANT.ACCOUNT` | `CrsReportBase_DormantAccount` | TField |  | The field will be updated as YES if CRS.CUST.SUPP.INFO>DORMANT.STATUS is set. |
| 88 | `CE.CRB.MESSAGE.TYPE.INDIC` | `CrsReportBase_MessageTypeIndic` | TField |  | The field will be updated with MessageTypeIndic to be reported in XML report. Values are : CRS701 - New Report CRS702 - Correction Report CRS703 - NIL Report |
| 89 | `CE.CRB.LOCAL.TAGS` | `CrsReportBase_LocalTags` |  |  |  |
| 90 | `CE.CRB.LOCAL.VALUES` | `CrsReportBase_LocalValues` |  |  |  |
| 91 | `CE.CRB.LOCAL.TAGS.XSLT` | `CrsReportBase_LocalTagsXslt` | TField |  | This field is updated with the complete list of local tag names separated by * which will then be referred internally by the system logic during report generation. |
| 92 | `CE.CRB.LOCAL.VALUES.XSLT` | `CrsReportBase_LocalValuesXslt` | TField |  | This field is updated with the tag values corresponding to the local tag names specified in LOCAL.TAGS.XSLT.The values are separated by * and will be referred internally by the system logic during report generation. |
