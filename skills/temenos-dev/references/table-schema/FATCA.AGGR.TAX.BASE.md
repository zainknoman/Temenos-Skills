# FATCA.AGGR.TAX.BASE — Table Schema

> Source: `INSERTS/I_F.FATCA.AGGR.TAX.BASE` in `FE_FatcaReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FE.AGG.TB.STATUS.DATE` | `FatcaAggrTaxBase_StatusDate` | TField |  | Date on which the base file is updated. |
| 2 | `FE.AGG.TB.BASE.YEAR` | `FatcaAggrTaxBase_BaseYear` | TField |  | Year to which the base data pertains to. The field will be taken from the ID. |
| 3 | `FE.AGG.TB.RESERVED.1` | `FatcaAggrTaxBase_Reserved1` | TField |  |  |
| 4 | `FE.AGG.TB.REPORT.TYPE` | `FatcaAggrTaxBase_ReportType` | TField |  | Based on the request From FATCA.XML.REQUEST Will be updated as FATCA1 -NEW, FATCA2- CORRECTION,FATCA3-VOID,FATCA4-AMEND. |
| 5 | `FE.AGG.TB.TRANS.COUNTRY` | `FatcaAggrTaxBase_TransCountry` | TField |  | The field will be updated from the field LOCAL.COUNTRY in COMPANY record. |
| 6 | `FE.AGG.TB.REC.COUNTRY` | `FatcaAggrTaxBase_RecCountry` | TField |  | The field will be same as the TRANS.COUNTRY if status field from FATCA.PARAMETER equals IGA1 otherwise updated as US. |
| 7 | `FE.AGG.TB.TIMESTAMP` | `FatcaAggrTaxBase_Timestamp` | TField |  | Time of the request for generating xml will be updated. |
| 8 | `FE.AGG.TB.COM.NAME` | `FatcaAggrTaxBase_ComName` | TField |  | The field will be updated from the field COMPANY.NAME in COMPANY record. |
| 9 | `FE.AGG.TB.COM.ADDRESS` | `FatcaAggrTaxBase_ComAddress` |  |  |  |
| 10 | `FE.AGG.TB.COM.TIN` | `FatcaAggrTaxBase_ComTin` | TField |  | This field will be mapped with the value in EIN field of FATCA.PARAMETER record. |
| 11 | `FE.AGG.TB.MSG.REF.ID` | `FatcaAggrTaxBase_MsgRefId` | TField |  | The field will be updated as FATCA.TAX.BASE.ID.SEQ.NO (seq.no will be 1 for the new record). |
| 12 | `FE.AGG.TB.CRCTD.MSG.REF.ID` | `FatcaAggrTaxBase_CrctdMsgRefId` | TField |  | The field is used for updating the amended message reference. |
| 13 | `FE.AGG.TB.FI.RETURN.REF` | `FatcaAggrTaxBase_FiReturnRef` | TField |  | The field will be updated from the field FI.RETURN.REF in FATCA.POOL.BALANCE record. |
| 14 | `FE.AGG.TB.FI.RETURN.ACTION` | `FatcaAggrTaxBase_FiReturnAction` | TField |  | The field will be updated from the field FI.RETURN.ACTION in FATCA.POOL.BALANCE record. |
| 15 | `FE.AGG.TB.DUE.DILIGENCE.IND` | `FatcaAggrTaxBase_DueDiligenceInd` | TField |  | The field used to define whether an account is a Reportable Account or an account held by a Non-participating Financial Institution. The field will be updated from the field DUE.DILIGENCE.IND in FATCA.REPORTING.PARAMETER record. |
| 16 | `FE.AGG.TB.THRESHOLD.IND` | `FatcaAggrTaxBase_ThresholdInd` | TField |  | The field used to define the thresholds in the due diligence process. The field will be updated from the field THRESHOLD.IND in FATCA.REPORTING.PARAMETER record. |
| 17 | `FE.AGG.TB.FI.REGISTER.ID` | `FatcaAggrTaxBase_FiRegisterId` | TField |  | The field used to indicates the first three digits of the FI's (Financial Institution) name. The field will be updated from the field FI.REGISTER.ID in FATCA.POOL.BALANCE record. |
| 18 | `FE.AGG.TB.TIN.CODE.TYPE` | `FatcaAggrTaxBase_TinCodeType` | TField |  | The field used to define the TIN.CODE.TYPE as ITIN for individuals and EIN for Entities. If GIIN is present,the field is updated as other. |
| 19 | `FE.AGG.TB.FATCA.USER.ID` | `FatcaAggrTaxBase_FatcaUserId` | TField |  | This field will be updated with the corresponding FATCA.TAX.BASE record Id |
| 20 | `FE.AGG.TB.ACCOUNT` | `FatcaAggrTaxBase_Account` |  |  |  |
| 21 | `FE.AGG.TB.ACC.OPEN.DATE` | `FatcaAggrTaxBase_AccOpenDate` |  |  |  |
| 22 | `FE.AGG.TB.ACCOUNT.TYPE` | `FatcaAggrTaxBase_AccountType` |  |  |  |
| 23 | `FE.AGG.TB.ACCT.PORT.CCY` | `FatcaAggrTaxBase_AcctPortCcy` |  |  |  |
| 24 | `FE.AGG.TB.ACC.BALANCE` | `FatcaAggrTaxBase_AccBalance` |  |  |  |
| 25 | `FE.AGG.TB.ACC.EXCH.RATE` | `FatcaAggrTaxBase_AccExchRate` |  |  |  |
| 26 | `FE.AGG.TB.ACC.BAL.USD` | `FatcaAggrTaxBase_AccBalUsd` |  |  |  |
| 27 | `FE.AGG.TB.REPORTNG.CCY` | `FatcaAggrTaxBase_ReportngCcy` |  |  |  |
| 28 | `FE.AGG.TB.REPORTNG.BAL` | `FatcaAggrTaxBase_ReportngBal` |  |  |  |
| 29 | `FE.AGG.TB.ACC.ACCOUNT.REF` | `FatcaAggrTaxBase_AccAccountRef` |  |  |  |
| 30 | `FE.AGG.TB.ACC.ACCOUNT.ACTION` | `FatcaAggrTaxBase_AccAccountAction` |  |  |  |
| 31 | `FE.AGG.TB.PAYMENT.TYPE` | `FatcaAggrTaxBase_PaymentType` |  |  |  |
| 32 | `FE.AGG.TB.PAYMENT.AMT` | `FatcaAggrTaxBase_PaymentAmt` |  |  |  |
| 33 | `FE.AGG.TB.USD.PAYMENT.AMT` | `FatcaAggrTaxBase_UsdPaymentAmt` |  |  |  |
| 34 | `FE.AGG.TB.REP.PYMT.TYPE` | `FatcaAggrTaxBase_RepPymtType` |  |  |  |
| 35 | `FE.AGG.TB.REP.PYMT.CCY` | `FatcaAggrTaxBase_RepPymtCcy` |  |  |  |
| 36 | `FE.AGG.TB.CON.PYMT.AMT` | `FatcaAggrTaxBase_ConPymtAmt` |  |  |  |
| 37 | `FE.AGG.TB.CON.USD.PYMT.AMT` | `FatcaAggrTaxBase_ConUsdPymtAmt` |  |  |  |
| 38 | `FE.AGG.TB.CLIENT.TYPE` | `FatcaAggrTaxBase_ClientType` |  |  |  |
| 39 | `FE.AGG.TB.ACC.RESERVED.2` | `FatcaAggrTaxBase_AccReserved2` |  |  |  |
| 40 | `FE.AGG.TB.ACC.RESERVED.1` | `FatcaAggrTaxBase_AccReserved1` |  |  |  |
| 41 | `FE.AGG.TB.CUSTOMER` | `FatcaAggrTaxBase_Customer` |  |  |  |
| 42 | `FE.AGG.TB.NAME.1` | `FatcaAggrTaxBase_Name1` |  |  |  |
| 43 | `FE.AGG.TB.NAME.2` | `FatcaAggrTaxBase_Name2` |  |  |  |
| 44 | `FE.AGG.TB.SHORT.NAME` | `FatcaAggrTaxBase_ShortName` |  |  |  |
| 45 | `FE.AGG.TB.STREET` | `FatcaAggrTaxBase_Street` |  |  |  |
| 46 | `FE.AGG.TB.ADDRESS` | `FatcaAggrTaxBase_Address` |  |  |  |
| 47 | `FE.AGG.TB.TOWN.COUNTRY` | `FatcaAggrTaxBase_TownCountry` |  |  |  |
| 48 | `FE.AGG.TB.POST.CODE` | `FatcaAggrTaxBase_PostCode` |  |  |  |
| 49 | `FE.AGG.TB.COUNTRY.SUB.ENTITY` | `FatcaAggrTaxBase_CountrySubEntity` |  |  |  |
| 50 | `FE.AGG.TB.COUNTRY` | `FatcaAggrTaxBase_Country` |  |  |  |
| 51 | `FE.AGG.TB.SECTOR` | `FatcaAggrTaxBase_Sector` |  |  |  |
| 52 | `FE.AGG.TB.ACCOUNT.OFFICER` | `FatcaAggrTaxBase_AccountOfficer` |  |  |  |
| 53 | `FE.AGG.TB.INDUSTRY` | `FatcaAggrTaxBase_Industry` |  |  |  |
| 54 | `FE.AGG.TB.CUSTOMER.STATUS` | `FatcaAggrTaxBase_CustomerStatus` |  |  |  |
| 55 | `FE.AGG.TB.NATIONALITY` | `FatcaAggrTaxBase_Nationality` |  |  |  |
| 56 | `FE.AGG.TB.RESIDENCE` | `FatcaAggrTaxBase_Residence` |  |  |  |
| 57 | `FE.AGG.TB.DOMICILE` | `FatcaAggrTaxBase_Domicile` |  |  |  |
| 58 | `FE.AGG.TB.COMPANY.BOOK` | `FatcaAggrTaxBase_CompanyBook` |  |  |  |
| 59 | `FE.AGG.TB.BIRTH.INCORP.DATE` | `FatcaAggrTaxBase_BirthIncorpDate` |  |  |  |
| 60 | `FE.AGG.TB.US.PLACE.OF.BIRTH` | `FatcaAggrTaxBase_UsPlaceOfBirth` |  |  |  |
| 61 | `FE.AGG.TB.TAX.DOMICILE` | `FatcaAggrTaxBase_TaxDomicile` |  |  |  |
| 62 | `FE.AGG.TB.CITIZENSHIP` | `FatcaAggrTaxBase_Citizenship` |  |  |  |
| 63 | `FE.AGG.TB.GREENCARD` | `FatcaAggrTaxBase_Greencard` |  |  |  |
| 64 | `FE.AGG.TB.TAX.RESIDENCE` | `FatcaAggrTaxBase_TaxResidence` |  |  |  |
| 65 | `FE.AGG.TB.TIN.COUNTRY` | `FatcaAggrTaxBase_TinCountry` |  |  |  |
| 66 | `FE.AGG.TB.TIN.CODE` | `FatcaAggrTaxBase_TinCode` |  |  |  |
| 67 | `FE.AGG.TB.EIN` | `FatcaAggrTaxBase_Ein` |  |  |  |
| 68 | `FE.AGG.TB.SOCIAL.SEC.NO` | `FatcaAggrTaxBase_SocialSecNo` |  |  |  |
| 69 | `FE.AGG.TB.GIIN` | `FatcaAggrTaxBase_Giin` |  |  |  |
| 70 | `FE.AGG.TB.SPONSOR.GIIN` | `FatcaAggrTaxBase_SponsorGiin` |  |  |  |
| 71 | `FE.AGG.TB.SELF.CLASS` | `FatcaAggrTaxBase_SelfClass` |  |  |  |
| 72 | `FE.AGG.TB.INDICIA` | `FatcaAggrTaxBase_Indicia` |  |  |  |
| 73 | `FE.AGG.TB.FATCA.STATUS` | `FatcaAggrTaxBase_FatcaStatus` |  |  |  |
| 74 | `FE.AGG.TB.STATUS.NARRATIVE` | `FatcaAggrTaxBase_StatusNarrative` |  |  |  |
| 75 | `FE.AGG.TB.STATUS.CHANGE.DATE` | `FatcaAggrTaxBase_StatusChangeDate` |  |  |  |
| 76 | `FE.AGG.TB.STATUS.TYPE` | `FatcaAggrTaxBase_StatusType` |  |  |  |
| 77 | `FE.AGG.TB.TOT.ACC.BAL.DEP` | `FatcaAggrTaxBase_TotAccBalDep` |  |  |  |
| 78 | `FE.AGG.TB.TOT.ACC.BAL.CUST` | `FatcaAggrTaxBase_TotAccBalCust` |  |  |  |
| 79 | `FE.AGG.TB.EXISTING.NEW` | `FatcaAggrTaxBase_ExistingNew` |  |  |  |
| 80 | `FE.AGG.TB.RELATION.CUST` | `FatcaAggrTaxBase_RelationCust` |  |  |  |
| 81 | `FE.AGG.TB.RELATION.CODE` | `FatcaAggrTaxBase_RelationCode` |  |  |  |
| 82 | `FE.AGG.TB.REL.CUST.NAME.1` | `FatcaAggrTaxBase_RelCustName1` |  |  |  |
| 83 | `FE.AGG.TB.REL.CUST.NAME.2` | `FatcaAggrTaxBase_RelCustName2` |  |  |  |
| 84 | `FE.AGG.TB.REL.ALIAS` | `FatcaAggrTaxBase_RelAlias` |  |  |  |
| 85 | `FE.AGG.TB.ROLE.TYPE` | `FatcaAggrTaxBase_RoleType` |  |  |  |
| 86 | `FE.AGG.TB.REL.NATIONALITY` | `FatcaAggrTaxBase_RelNationality` |  |  |  |
| 87 | `FE.AGG.TB.REL.RESIDENCE` | `FatcaAggrTaxBase_RelResidence` |  |  |  |
| 88 | `FE.AGG.TB.REL.DOMICILE` | `FatcaAggrTaxBase_RelDomicile` |  |  |  |
| 89 | `FE.AGG.TB.REL.STREET` | `FatcaAggrTaxBase_RelStreet` |  |  |  |
| 90 | `FE.AGG.TB.REL.ADDRESS` | `FatcaAggrTaxBase_RelAddress` |  |  |  |
| 91 | `FE.AGG.TB.REL.TOWN.COUNTRY` | `FatcaAggrTaxBase_RelTownCountry` |  |  |  |
| 92 | `FE.AGG.TB.REL.POST.CODE` | `FatcaAggrTaxBase_RelPostCode` |  |  |  |
| 93 | `FE.AGG.TB.REL.COUNTRY` | `FatcaAggrTaxBase_RelCountry` |  |  |  |
| 94 | `FE.AGG.TB.REL.CNTY.SUB.ENT` | `FatcaAggrTaxBase_RelCntySubEnt` |  |  |  |
| 95 | `FE.AGG.TB.REL.BIRTH.DATE` | `FatcaAggrTaxBase_RelBirthDate` |  |  |  |
| 96 | `FE.AGG.TB.REL.OWN.PERC` | `FatcaAggrTaxBase_RelOwnPerc` |  |  |  |
| 97 | `FE.AGG.TB.REL.CUST.TIN` | `FatcaAggrTaxBase_RelCustTin` |  |  |  |
| 98 | `FE.AGG.TB.REL.ADDR.COUNTRY` | `FatcaAggrTaxBase_RelAddrCountry` |  |  |  |
| 99 | `FE.AGG.TB.REL.TIN.COUNTRY` | `FatcaAggrTaxBase_RelTinCountry` |  |  |  |
| 100 | `FE.AGG.TB.REL.ENTITY.TYPE` | `FatcaAggrTaxBase_RelEntityType` |  |  |  |
| 101 | `FE.AGG.TB.REL.FATCA.STATUS` | `FatcaAggrTaxBase_RelFatcaStatus` |  |  |  |
| 102 | `FE.AGG.TB.REL.CUST.TIN.TYPE` | `FatcaAggrTaxBase_RelCustTinType` |  |  |  |
| 103 | `FE.AGG.TB.REL.RESERVED.4` | `FatcaAggrTaxBase_RelReserved4` |  |  |  |
| 104 | `FE.AGG.TB.REL.RESERVED.3` | `FatcaAggrTaxBase_RelReserved3` |  |  |  |
| 105 | `FE.AGG.TB.REL.RESERVED.2` | `FatcaAggrTaxBase_RelReserved2` |  |  |  |
| 106 | `FE.AGG.TB.REL.RESERVED.1` | `FatcaAggrTaxBase_RelReserved1` |  |  |  |
| 107 | `FE.AGG.TB.ACCT.HOLDER.TYPE` | `FatcaAggrTaxBase_AcctHolderType` |  |  |  |
| 108 | `FE.AGG.TB.FATCA.BASE.ID` | `FatcaAggrTaxBase_FatcaBaseId` |  |  |  |
