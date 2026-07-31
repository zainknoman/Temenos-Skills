# PROLENDER.CREATE — Table Schema

> Source: `INSERTS/I_F.PROLENDER.CREATE` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRL.CR.REQ` | `ProlenderCreate_Req` | TField |  |  |
| 2 | `PRL.CR.DESCRIPTION` | `ProlenderCreate_Description` | TField |  |  |
| 3 | `PRL.CR.CUID` | `ProlenderCreate_Cuid` | TField |  |  |
| 4 | `PRL.CR.USERID` | `ProlenderCreate_Userid` | TField |  |  |
| 5 | `PRL.CR.PASSWORD` | `ProlenderCreate_Password` | TField |  |  |
| 6 | `PRL.CR.REQUEST.ID` | `ProlenderCreate_RequestId` | TField |  |  |
| 7 | `PRL.CR.TIME.STAMP` | `ProlenderCreate_TimeStamp` | TField |  |  |
| 8 | `PRL.CR.STATUS.CODE` | `ProlenderCreate_StatusCode` | TField |  |  |
| 9 | `PRL.CR.ENTITY.TYPE` | `ProlenderCreate_EntityType` | TField |  |  |
| 10 | `PRL.CR.MESSAGE.CODE` | `ProlenderCreate_MessageCode` |  |  |  |
| 11 | `PRL.CR.MESSAGE.TEXT` | `ProlenderCreate_MessageText` |  |  |  |
| 12 | `PRL.CR.MEMBER.ID` | `ProlenderCreate_MemberId` | TField |  |  |
| 13 | `PRL.CR.CIF.NO` | `ProlenderCreate_CifNo` |  |  |  |
| 14 | `PRL.CR.RELATION.CODE` | `ProlenderCreate_RelationCode` |  |  |  |
| 15 | `PRL.CR.IS.STAFF` | `ProlenderCreate_IsStaff` |  |  |  |
| 16 | `PRL.CR.LOAN.OFFICER.BR` | `ProlenderCreate_LoanOfficerBr` | TField |  |  |
| 17 | `PRL.CR.LOAN.OFFICER` | `ProlenderCreate_LoanOfficer` | TField |  |  |
| 18 | `PRL.CR.APPROVING.OFFICER` | `ProlenderCreate_ApprovingOfficer` | TField |  |  |
| 19 | `PRL.CR.LOAN.OFFICER.UN` | `ProlenderCreate_LoanOfficerUn` | TField |  |  |
| 20 | `PRL.CR.APPROV.OFFICER.UN` | `ProlenderCreate_ApprovOfficerUn` | TField |  |  |
| 21 | `PRL.CR.LOAN.TYPE` | `ProlenderCreate_LoanType` | TField |  |  |
| 22 | `PRL.CR.PRODUCT.TYPE` | `ProlenderCreate_ProductType` | TField |  |  |
| 23 | `PRL.CR.PURPOSE.DESC` | `ProlenderCreate_PurposeDesc` | TField |  |  |
| 24 | `PRL.CR.TTL.LOAN.AMOUNT` | `ProlenderCreate_TtlLoanAmount` | TField |  |  |
| 25 | `PRL.CR.APPLY.DATE` | `ProlenderCreate_ApplyDate` | TField |  |  |
| 26 | `PRL.CR.OPENING.DATE` | `ProlenderCreate_OpeningDate` | TField |  |  |
| 27 | `PRL.CR.MATURITY.DATE` | `ProlenderCreate_MaturityDate` | TField |  |  |
| 28 | `PRL.CR.REVIEW.DATE` | `ProlenderCreate_ReviewDate` | TField |  |  |
| 29 | `PRL.CR.TERM.OF.LOAN` | `ProlenderCreate_TermOfLoan` | TField |  |  |
| 30 | `PRL.CR.AMORT` | `ProlenderCreate_Amort` | TField |  |  |
| 31 | `PRL.CR.LINK.CHEQ.ACCT.NO` | `ProlenderCreate_LinkCheqAcctNo` | TField |  |  |
| 32 | `PRL.CR.PMT.SOURCE` | `ProlenderCreate_PmtSource` | TField |  |  |
| 33 | `PRL.CR.PMT.TYPE` | `ProlenderCreate_PmtType` | TField |  |  |
| 34 | `PRL.CR.PMT` | `ProlenderCreate_Pmt` | TField |  |  |
| 35 | `PRL.CR.PMT.FREQ` | `ProlenderCreate_PmtFreq` | TField |  |  |
| 36 | `PRL.CR.FIRST.PAY.DATE` | `ProlenderCreate_FirstPayDate` | TField |  |  |
| 37 | `PRL.CR.INT.FREQ` | `ProlenderCreate_IntFreq` | TField |  |  |
| 38 | `PRL.CR.INT.FIRST.PAY.DATE` | `ProlenderCreate_IntFirstPayDate` | TField |  |  |
| 39 | `PRL.CR.PRINCIPLE.PMT` | `ProlenderCreate_PrinciplePmt` | TField |  |  |
| 40 | `PRL.CR.PROPERTY.TAX` | `ProlenderCreate_PropertyTax` | TField |  |  |
| 41 | `PRL.CR.NOMINAL.RATE` | `ProlenderCreate_NominalRate` | TField |  |  |
| 42 | `PRL.CR.PLUS.RATE` | `ProlenderCreate_PlusRate` | TField |  |  |
| 43 | `PRL.CR.IS.VARIABLE.RATE` | `ProlenderCreate_IsVariableRate` | TField |  |  |
| 44 | `PRL.CR.INSTITUTION.NUMBER` | `ProlenderCreate_InstitutionNumber` | TField |  |  |
| 45 | `PRL.CR.BRANCH.NUMBER` | `ProlenderCreate_BranchNumber` | TField |  |  |
| 46 | `PRL.CR.PRODUCER.NUMBER` | `ProlenderCreate_ProducerNumber` | TField |  |  |
| 47 | `PRL.CR.CUMIS.DEBIT.ACCT` | `ProlenderCreate_CumisDebitAcct` | TField |  |  |
| 48 | `PRL.CR.CUMIS.CERT.NUMBER` | `ProlenderCreate_CumisCertNumber` | TField |  |  |
| 49 | `PRL.CR.RATE.SCHEDULE` | `ProlenderCreate_RateSchedule` | TField |  |  |
| 50 | `PRL.CR.RATE.INDEX` | `ProlenderCreate_RateIndex` | TField |  |  |
| 51 | `PRL.CR.CLASS.CODE` | `ProlenderCreate_ClassCode` | TField |  |  |
| 52 | `PRL.CR.COLLAT.CODE` | `ProlenderCreate_CollatCode` | TField |  |  |
| 53 | `PRL.CR.COLLAT.SUB.TYPE` | `ProlenderCreate_CollatSubType` | TField |  |  |
| 54 | `PRL.CR.RESOLUTION.DATE` | `ProlenderCreate_ResolutionDate` | TField |  |  |
| 55 | `PRL.CR.RESOLUTION.FREQ` | `ProlenderCreate_ResolutionFreq` | TField |  |  |
| 56 | `PRL.CR.PROGRESS.DRAW` | `ProlenderCreate_ProgressDraw` | TField |  |  |
| 57 | `PRL.CR.IS.TAX.ADDED` | `ProlenderCreate_IsTaxAdded` | TField |  |  |
| 58 | `PRL.CR.PRE.PMT.PENALTY` | `ProlenderCreate_PrePmtPenalty` | TField |  |  |
| 59 | `PRL.CR.MIN.PMT` | `ProlenderCreate_MinPmt` | TField |  |  |
| 60 | `PRL.CR.DEALER.CODE` | `ProlenderCreate_DealerCode` | TField |  |  |
| 61 | `PRL.CR.SOURCE` | `ProlenderCreate_Source` | TField |  |  |
| 62 | `PRL.CR.BASE.RATE` | `ProlenderCreate_BaseRate` | TField |  |  |
| 63 | `PRL.CR.TOTAL.MKT.VALUE` | `ProlenderCreate_TotalMktValue` | TField |  |  |
| 64 | `PRL.CR.TOTAL.PRIOR.ENCUMB` | `ProlenderCreate_TotalPriorEncumb` | TField |  |  |
| 65 | `PRL.CR.ASSET.TYPE` | `ProlenderCreate_AssetType` |  |  |  |
| 66 | `PRL.CR.ASSET.DESC` | `ProlenderCreate_AssetDesc` |  |  |  |
| 67 | `PRL.CR.FINANCIAL.INSTI` | `ProlenderCreate_FinancialInsti` |  |  |  |
| 68 | `PRL.CR.COLLATERAL.TYPE` | `ProlenderCreate_CollateralType` |  |  |  |
| 69 | `PRL.CR.COLLATERAL.CODE` | `ProlenderCreate_CollateralCode` |  |  |  |
| 70 | `PRL.CR.COLLATERAL.DESC` | `ProlenderCreate_CollateralDesc` |  |  |  |
| 71 | `PRL.CR.PARCEL.ID` | `ProlenderCreate_ParcelId` |  |  |  |
| 72 | `PRL.CR.COLLATERAL.VALUE` | `ProlenderCreate_CollateralValue` |  |  |  |
| 73 | `PRL.CR.ESTATE.TYPE` | `ProlenderCreate_EstateType` |  |  |  |
| 74 | `PRL.CR.PROP.FREE.FORM` | `ProlenderCreate_PropFreeForm` |  |  |  |
| 75 | `PRL.CR.MAILING.HEADER` | `ProlenderCreate_MailingHeader` |  |  |  |
| 76 | `PRL.CR.UNIT.NUMBER` | `ProlenderCreate_UnitNumber` |  |  |  |
| 77 | `PRL.CR.UNIT.TYPE` | `ProlenderCreate_UnitType` |  |  |  |
| 78 | `PRL.CR.STREET.NUMBER` | `ProlenderCreate_StreetNumber` |  |  |  |
| 79 | `PRL.CR.STREET.NAME` | `ProlenderCreate_StreetName` |  |  |  |
| 80 | `PRL.CR.STREET.TYPE` | `ProlenderCreate_StreetType` |  |  |  |
| 81 | `PRL.CR.STREET.DIR` | `ProlenderCreate_StreetDir` |  |  |  |
| 82 | `PRL.CR.CITY` | `ProlenderCreate_City` |  |  |  |
| 83 | `PRL.CR.PROVINCE` | `ProlenderCreate_Province` |  |  |  |
| 84 | `PRL.CR.POSTAL.CODE` | `ProlenderCreate_PostalCode` |  |  |  |
| 85 | `PRL.CR.COUNTRY` | `ProlenderCreate_Country` |  |  |  |
| 86 | `PRL.CR.IS.REVENUE` | `ProlenderCreate_IsRevenue` |  |  |  |
| 87 | `PRL.CR.PRIORITY` | `ProlenderCreate_Priority` |  |  |  |
| 88 | `PRL.CR.SOLICITR.NAME` | `ProlenderCreate_SolicitrName` |  |  |  |
| 89 | `PRL.CR.SOLICITR.CONTACT` | `ProlenderCreate_SolicitrContact` |  |  |  |
| 90 | `PRL.CR.APPRAISR.NAME` | `ProlenderCreate_AppraisrName` |  |  |  |
| 91 | `PRL.CR.APPRAISR.CONTACT` | `ProlenderCreate_AppraisrContact` |  |  |  |
| 92 | `PRL.CR.MARKET.VALUE` | `ProlenderCreate_MarketValue` |  |  |  |
| 93 | `PRL.CR.MARKET.VALUE.DT` | `ProlenderCreate_MarketValueDt` |  |  |  |
| 94 | `PRL.CR.PURCHASE.PRICE` | `ProlenderCreate_PurchasePrice` |  |  |  |
| 95 | `PRL.CR.ANNUAL.TAXES` | `ProlenderCreate_AnnualTaxes` |  |  |  |
| 96 | `PRL.CR.MUNICIPALITY.NO` | `ProlenderCreate_MunicipalityNo` |  |  |  |
| 97 | `PRL.CR.SERIAL.NUMBER` | `ProlenderCreate_SerialNumber` |  |  |  |
| 98 | `PRL.CR.SERIAL.MODEL` | `ProlenderCreate_SerialModel` |  |  |  |
| 99 | `PRL.CR.SERIAL.MAKE` | `ProlenderCreate_SerialMake` |  |  |  |
| 100 | `PRL.CR.SERIAL.YEAR` | `ProlenderCreate_SerialYear` |  |  |  |
| 101 | `PRL.CR.REGISTERED.OWNER1` | `ProlenderCreate_RegisteredOwner1` |  |  |  |
| 102 | `PRL.CR.REGISTERED.OWNER2` | `ProlenderCreate_RegisteredOwner2` |  |  |  |
| 103 | `PRL.CR.REGISTERED.OWNER3` | `ProlenderCreate_RegisteredOwner3` |  |  |  |
| 104 | `PRL.CR.SERIAL.PPR` | `ProlenderCreate_SerialPpr` |  |  |  |
| 105 | `PRL.CR.CERT.ACCOUNT.NO` | `ProlenderCreate_CertAccountNo` |  |  |  |
| 106 | `PRL.CR.MAT.DATE` | `ProlenderCreate_MatDate` |  |  |  |
| 107 | `PRL.CR.INT.RATE` | `ProlenderCreate_IntRate` |  |  |  |
| 108 | `PRL.CR.LEGAL.DESCRIPTION` | `ProlenderCreate_LegalDescription` |  |  |  |
| 109 | `PRL.CR.COLLATERAL.ID` | `ProlenderCreate_CollateralId` |  |  |  |
| 110 | `PRL.CR.DISABILITY` | `ProlenderCreate_Disability` | TField |  |  |
| 111 | `PRL.CR.LIFE` | `ProlenderCreate_Life` | TField |  |  |
| 112 | `PRL.CR.LOSS.OF.EMPLMT` | `ProlenderCreate_LossOfEmplmt` | TField |  |  |
| 113 | `PRL.CR.CRITICAL.ILLNESS` | `ProlenderCreate_CriticalIllness` | TField |  |  |
| 114 | `PRL.CR.DISABTY.PREMIUM` | `ProlenderCreate_DisabtyPremium` | TField |  |  |
| 115 | `PRL.CR.LIFE.PREMIUM` | `ProlenderCreate_LifePremium` | TField |  |  |
| 116 | `PRL.CR.CMHC.PREMIUM` | `ProlenderCreate_CmhcPremium` | TField |  |  |
| 117 | `PRL.CR.IS.CMHC.FINANCED` | `ProlenderCreate_IsCmhcFinanced` | TField |  |  |
| 118 | `PRL.CR.FINCD.CMHC.PREMIUM` | `ProlenderCreate_FincdCmhcPremium` | TField |  |  |
| 119 | `PRL.CR.CMHC.ACCOUNT.NO` | `ProlenderCreate_CmhcAccountNo` | TField |  |  |
| 120 | `PRL.CR.GE.ACCOUNT.NO` | `ProlenderCreate_GeAccountNo` | TField |  |  |
| 121 | `PRL.CR.PRI.LIFE.WAIV.RESN` | `ProlenderCreate_PriLifeWaivResn` | TField |  |  |
| 122 | `PRL.CR.PRI.DSBL.WAIV.RESN` | `ProlenderCreate_PriDsblWaivResn` | TField |  |  |
| 123 | `PRL.CR.SEC.LIFE.WAIV.RESN` | `ProlenderCreate_SecLifeWaivResn` | TField |  |  |
| 124 | `PRL.CR.SEC.DSBL.WAIV.RESN` | `ProlenderCreate_SecDsblWaivResn` | TField |  |  |
| 125 | `PRL.CR.IS.INSU.FINANCED` | `ProlenderCreate_IsInsuFinanced` | TField |  |  |
| 126 | `PRL.CR.HLD.ACCT.NO` | `ProlenderCreate_HldAcctNo` | TField |  |  |
| 127 | `PRL.CR.HLD.AMT` | `ProlenderCreate_HldAmt` | TField |  |  |
| 128 | `PRL.CR.HLD.EXPIRY.DATE` | `ProlenderCreate_HldExpiryDate` | TField |  |  |
| 129 | `PRL.CR.PAT.PMT.FREQ` | `ProlenderCreate_PatPmtFreq` |  |  |  |
| 130 | `PRL.CR.PAT.START.DATE` | `ProlenderCreate_PatStartDate` |  |  |  |
| 131 | `PRL.CR.PAT.STOP.DATE` | `ProlenderCreate_PatStopDate` |  |  |  |
| 132 | `PRL.CR.PAT.TRANS.CODE` | `ProlenderCreate_PatTransCode` |  |  |  |
| 133 | `PRL.CR.PAT.INSTI.NAME` | `ProlenderCreate_PatInstiName` |  |  |  |
| 134 | `PRL.CR.PAT.INSTI.ADDRESS` | `ProlenderCreate_PatInstiAddress` |  |  |  |
| 135 | `PRL.CR.PAT.INSTI.PH.AREA` | `ProlenderCreate_PatInstiPhArea` |  |  |  |
| 136 | `PRL.CR.PAT.INSTI.PH.LOCAL` | `ProlenderCreate_PatInstiPhLocal` |  |  |  |
| 137 | `PRL.CR.PAT.BANK.NO` | `ProlenderCreate_PatBankNo` |  |  |  |
| 138 | `PRL.CR.PAT.TRANSIT.NO` | `ProlenderCreate_PatTransitNo` |  |  |  |
| 139 | `PRL.CR.PAT.ACCT.NO` | `ProlenderCreate_PatAcctNo` |  |  |  |
| 140 | `PRL.CR.PAT.ACCT.NAME` | `ProlenderCreate_PatAcctName` |  |  |  |
| 141 | `PRL.CR.PAT.AMOUNT` | `ProlenderCreate_PatAmount` |  |  |  |
| 142 | `PRL.CR.PAT.MULT.FRQ.TRANS` | `ProlenderCreate_PatMultFrqTrans` |  |  |  |
| 143 | `PRL.CR.FEE.CHARGE.CODE` | `ProlenderCreate_FeeChargeCode` |  |  |  |
| 144 | `PRL.CR.FEE.AMOUNT` | `ProlenderCreate_FeeAmount` |  |  |  |
| 145 | `PRL.CR.IS.FEE.FINANCED` | `ProlenderCreate_IsFeeFinanced` |  |  |  |
| 146 | `PRL.CR.COLL.SUBTYPE` | `ProlenderCreate_CollSubtype` | TField |  |  |
| 147 | `PRL.CR.RESERVED.6` | `ProlenderCreate_Reserved6` |  |  |  |
| 148 | `PRL.CR.ARRANGEMENT.ID` | `ProlenderCreate_ArrangementId` | TField |  |  |
| 149 | `PRL.CR.LOAN.DAO` | `ProlenderCreate_LoanDao` | TField |  |  |
| 150 | `PRL.CR.APPROVE.DAO` | `ProlenderCreate_ApproveDao` | TField |  |  |
| 151 | `PRL.CR.CAPPED.RATE` | `ProlenderCreate_CappedRate` | TField |  |  |
| 152 | `PRL.CR.LTV.RATIO` | `ProlenderCreate_LtvRatio` | TField |  |  |
| 153 | `PRL.CR.RESERVED.3` | `ProlenderCreate_Reserved3` |  |  |  |
| 154 | `PRL.CR.RESERVED.2` | `ProlenderCreate_Reserved2` |  |  |  |
| 155 | `PRL.CR.RESERVED.1` | `ProlenderCreate_Reserved1` | TField |  |  |
| 156 | `PRL.CR.RECORD.STATUS` | `ProlenderCreate_RecordStatus` | String |  |  |
| 157 | `PRL.CR.CURR.NO` | `ProlenderCreate_CurrNo` | String |  |  |
| 158 | `PRL.CR.INPUTTER` | `ProlenderCreate_Inputter` |  |  |  |
| 159 | `PRL.CR.DATE.TIME` | `ProlenderCreate_DateTime` |  |  |  |
| 160 | `PRL.CR.AUTHORISER` | `ProlenderCreate_Authoriser` | String |  |  |
| 161 | `PRL.CR.CO.CODE` | `ProlenderCreate_CoCode` | String |  |  |
| 162 | `PRL.CR.DEPT.CODE` | `ProlenderCreate_DeptCode` | String |  |  |
| 163 | `PRL.CR.AUDITOR.CODE` | `ProlenderCreate_AuditorCode` | String |  |  |
| 164 | `PRL.CR.AUDIT.DATE.TIME` | `ProlenderCreate_AuditDateTime` | String |  |  |
