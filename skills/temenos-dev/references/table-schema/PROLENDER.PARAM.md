# PROLENDER.PARAM — Table Schema

> Source: `INSERTS/I_F.PROLENDER.PARAM` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRL.PAR.COMM.SECTOR` | `ProlenderParam_CommSector` |  |  |  |
| 2 | `PRL.PAR.EXC.CUS.STATUS` | `ProlenderParam_ExcCusStatus` |  |  |  |
| 3 | `PRL.PAR.EXCL.AZ.PRODUCT` | `ProlenderParam_ExclAzProduct` |  |  |  |
| 4 | `PRL.PAR.EXCL.ACC.PRODUCT` | `ProlenderParam_ExclAccProduct` |  |  |  |
| 5 | `PRL.PAR.EXCL.REL.CODE` | `ProlenderParam_ExclRelCode` |  |  |  |
| 6 | `PRL.PAR.BRANCH.CODE` | `ProlenderParam_BranchCode` | TField |  | This field is used to determine if Transit number or Company code is sent as Branch Code If it is TRANSIT then t24 will send the equivalent Transit for the Company code If it is blank or COMPCODE then t24 will send Company code |
| 7 | `PRL.PAR.LOC.LIM.CREATE` | `ProlenderParam_LocLimCreate` | TField |  | If it is set to YES then system will create the Limit record and attach it to Arrangement Chequing Account, If this is set to NO then system will be created by Arrangement Account. |
| 8 | `PRL.PAR.EXCL.AA.PRODUCT` | `ProlenderParam_ExclAaProduct` |  |  |  |
| 9 | `PRL.PAR.INCL.AA.ROLE` | `ProlenderParam_InclAaRole` |  |  |  |
| 10 | `PRL.PAR.EXCL.AA.STATUS` | `ProlenderParam_ExclAaStatus` |  |  |  |
| 11 | `PRL.PAR.LIM.EXPIRY.DATE` | `ProlenderParam_LimExpiryDate` | TField |  | The date defined here will be updated as the Expiry Date for Limits created through 'Create Loan' request |
| 12 | `PRL.PAR.PRL.PMT.FREQ` | `ProlenderParam_PrlPmtFreq` |  |  |  |
| 13 | `PRL.PAR.T24.FREQ` | `ProlenderParam_T24Freq` |  |  |  |
| 14 | `PRL.PAR.PRL.CASE.IND` | `ProlenderParam_PrlCaseInd` | TField |  |  |
| 15 | `PRL.PAR.STAFF.INDUSTRY` | `ProlenderParam_StaffIndustry` |  |  |  |
| 16 | `PRL.PAR.MARITAL.STAT.DESC` | `ProlenderParam_MaritalStatDesc` |  |  |  |
| 17 | `PRL.PAR.MARITAL.STAT.CODE` | `ProlenderParam_MaritalStatCode` |  |  |  |
| 18 | `PRL.PAR.TITLE.DESC` | `ProlenderParam_TitleDesc` |  |  |  |
| 19 | `PRL.PAR.TITLE.CODE` | `ProlenderParam_TitleCode` |  |  |  |
| 20 | `PRL.PAR.CLASS.DESC` | `ProlenderParam_ClassDesc` |  |  |  |
| 21 | `PRL.PAR.CLASS.CODE` | `ProlenderParam_ClassCode` |  |  |  |
| 22 | `PRL.PAR.PRL.TXN.CODE` | `ProlenderParam_PrlTxnCode` |  |  |  |
| 23 | `PRL.PAR.T24.TXN.CODE` | `ProlenderParam_T24TxnCode` |  |  |  |
| 24 | `PRL.PAR.PRL.DISBURSE.ACCT` | `ProlenderParam_PrlDisburseAcct` |  |  |  |
| 25 | `PRL.PAR.T24.CHARG.PROP` | `ProlenderParam_T24ChargProp` |  |  |  |
| 26 | `PRL.PAR.PRL.OWNERS` | `ProlenderParam_PrlOwners` |  |  |  |
| 27 | `PRL.PAR.OWNER.REL` | `ProlenderParam_OwnerRel` |  |  |  |
| 28 | `PRL.PAR.PRL.NON.OWNERS` | `ProlenderParam_PrlNonOwners` |  |  |  |
| 29 | `PRL.PAR.AA.ROLE` | `ProlenderParam_AaRole` |  |  |  |
| 30 | `PRL.PAR.SECURITY.INDICATOR` | `ProlenderParam_SecurityIndicator` |  |  |  |
| 31 | `PRL.PAR.COLLATERAL.CODE` | `ProlenderParam_CollateralCode` |  |  |  |
| 32 | `PRL.PAR.ASSET.TYPE` | `ProlenderParam_AssetType` |  |  |  |
| 33 | `PRL.PAR.ASSET.DESC` | `ProlenderParam_AssetDesc` |  |  |  |
| 34 | `PRL.PAR.ASSET.CATEGORY` | `ProlenderParam_AssetCategory` |  |  |  |
| 35 | `PRL.PAR.ODPC.LOAN.TYPE` | `ProlenderParam_OdpcLoanType` |  |  |  |
| 36 | `PRL.PAR.ODPC.PROD.TYPE` | `ProlenderParam_OdpcProdType` |  |  |  |
| 37 | `PRL.PAR.SRC.TAG` | `ProlenderParam_SrcTag` |  |  |  |
| 38 | `PRL.PAR.DEFAULTED.TAG` | `ProlenderParam_DefaultedTag` |  |  |  |
| 39 | `PRL.PAR.LOG` | `ProlenderParam_Log` | TField |  | Field is used to indicate what type of logging is required. REQUEST, RESPOSNE or BOTH |
| 40 | `PRL.PAR.GEN.PASS` | `ProlenderParam_GenPass` | TField |  | Password for the Generic User for Heart Beat Message processing. Generic User will be defined in OFS.SOURCE |
| 41 | `PRL.PAR.STATUS.DESC` | `ProlenderParam_StatusDesc` |  |  |  |
| 42 | `PRL.PAR.STATUS.CODE` | `ProlenderParam_StatusCode` |  |  |  |
| 43 | `PRL.PAR.ENTITY.DESC` | `ProlenderParam_EntityDesc` |  |  |  |
| 44 | `PRL.PAR.ENTITY.CODE` | `ProlenderParam_EntityCode` |  |  |  |
| 45 | `PRL.PAR.STATE.DESC` | `ProlenderParam_StateDesc` |  |  |  |
| 46 | `PRL.PAR.STATE.CODE` | `ProlenderParam_StateCode` |  |  |  |
| 47 | `PRL.PAR.STREET.DIREC.DESC` | `ProlenderParam_StreetDirecDesc` |  |  |  |
| 48 | `PRL.PAR.STREET.DIREC.CODE` | `ProlenderParam_StreetDirecCode` |  |  |  |
| 49 | `PRL.PAR.LANGUAGE.DESC` | `ProlenderParam_LanguageDesc` |  |  |  |
| 50 | `PRL.PAR.LANGUAGE.CODE` | `ProlenderParam_LanguageCode` |  |  |  |
| 51 | `PRL.PAR.SEX.DESC` | `ProlenderParam_SexDesc` |  |  |  |
| 52 | `PRL.PAR.SEX.CODE` | `ProlenderParam_SexCode` |  |  |  |
| 53 | `PRL.PAR.TAX.DESC` | `ProlenderParam_TaxDesc` |  |  |  |
| 54 | `PRL.PAR.TAX.CODE` | `ProlenderParam_TaxCode` |  |  |  |
| 55 | `PRL.PAR.LOAN.STATUS.DESC` | `ProlenderParam_LoanStatusDesc` |  |  |  |
| 56 | `PRL.PAR.LOAN.STATUS.CODE` | `ProlenderParam_LoanStatusCode` |  |  |  |
| 57 | `PRL.PAR.MISC.TYPE.DESC` | `ProlenderParam_MiscTypeDesc` |  |  |  |
| 58 | `PRL.PAR.MISC.TYPE.CODE` | `ProlenderParam_MiscTypeCode` |  |  |  |
| 59 | `PRL.PAR.OWNED.TYPE.DESC` | `ProlenderParam_OwnedTypeDesc` |  |  |  |
| 60 | `PRL.PAR.OWNED.TYPE.CODE` | `ProlenderParam_OwnedTypeCode` |  |  |  |
| 61 | `PRL.PAR.BOOLEAN.INDIC.DESC` | `ProlenderParam_BooleanIndicDesc` |  |  |  |
| 62 | `PRL.PAR.BOOLEAN.INDIC.CODE` | `ProlenderParam_BooleanIndicCode` |  |  |  |
| 63 | `PRL.PAR.LOAN.TYPE.DESC` | `ProlenderParam_LoanTypeDesc` |  |  |  |
| 64 | `PRL.PAR.LOAN.TYPE.CODE` | `ProlenderParam_LoanTypeCode` |  |  |  |
| 65 | `PRL.PAR.MKT.VALUE.DESC` | `ProlenderParam_MktValueDesc` |  |  |  |
| 66 | `PRL.PAR.MKT.VALUE.CODE` | `ProlenderParam_MktValueCode` |  |  |  |
| 67 | `PRL.PAR.T24.PAY.TYPE` | `ProlenderParam_T24PayType` |  |  |  |
| 68 | `PRL.PAR.PRL.PAY.TYPE` | `ProlenderParam_PrlPayType` |  |  |  |
| 69 | `PRL.PAR.LOC.REPAY.PERCENT` | `ProlenderParam_LocRepayPercent` |  |  |  |
| 70 | `PRL.PAR.INS.COV.DESC` | `ProlenderParam_InsCovDesc` |  |  |  |
| 71 | `PRL.PAR.INS.COV.CODE` | `ProlenderParam_InsCovCode` |  |  |  |
| 72 | `PRL.PAR.ESTATE.TYPE.DESC` | `ProlenderParam_EstateTypeDesc` |  |  |  |
| 73 | `PRL.PAR.ESTATE.TYPE.CODE` | `ProlenderParam_EstateTypeCode` |  |  |  |
| 74 | `PRL.PAR.INS.WAV.RSON.DESC` | `ProlenderParam_InsWavRsonDesc` |  |  |  |
| 75 | `PRL.PAR.INS.WAV.RSON.CODE` | `ProlenderParam_InsWavRsonCode` |  |  |  |
| 76 | `PRL.PAR.COLL.TYPE.DESC` | `ProlenderParam_CollTypeDesc` |  |  |  |
| 77 | `PRL.PAR.COLL.TYPE.CODE` | `ProlenderParam_CollTypeCode` |  |  |  |
| 78 | `PRL.PAR.NO.OF.YEARS` | `ProlenderParam_NoOfYears` | TField |  | Field to store the number of years before which the records in PROLENDER.LOG to be cleared.PROLENDER.LOG table is used to store all OFS request and response of PROLENDER messages.Batch PROLENDER.CLEAR.LOG is used to clear the records in PROLEDNER.LOG table prior to the value defined in NO.OF.YEARS fieldField length - 35Eg:TODAY - 25 Dec 2018NO.OF.YEARS - 5Difference in Year = 2018 -5 = 2013On running PROLENDER.CLEAR.LOG batch it will clear all record in PROLENDER.LOG prior to '25 Dec 2013' |
| 79 | `PRL.PAR.PRL.PRODUCT.TYPE` | `ProlenderParam_PrlProductType` |  |  |  |
| 80 | `PRL.PAR.T24.PRODUCT.TYPE` | `ProlenderParam_T24ProductType` |  |  |  |
| 81 | `PRL.PAR.T24.PRODUCT.GROUP` | `ProlenderParam_T24ProductGroup` |  |  |  |
| 82 | `PRL.PAR.T24.PRODUCT.LIMIT` | `ProlenderParam_T24ProductLimit` |  |  |  |
| 83 | `PRL.PAR.PRL.SCH.FRQ` | `ProlenderParam_PrlSchFrq` |  |  |  |
| 84 | `PRL.PAR.SCH.CHG.PROP` | `ProlenderParam_SchChgProp` |  |  |  |
| 85 | `PRL.PAR.SCH.CHG.AMT` | `ProlenderParam_SchChgAmt` |  |  |  |
| 86 | `PRL.PAR.GE.TXN.CODE` | `ProlenderParam_GeTxnCode` | TField |  | NOT in use |
| 87 | `PRL.PAR.PRL.INDICATOR` | `ProlenderParam_PrlIndicator` | TField |  | Field to indicate the prolender process based on CIF or Membership.Allowed inputs - YES/NO .--&gt; FI using CIF concept should set field PRL.INDICATOR &gt; PROLENDER.PARAM as YES to fetch all the response details based on the CIF ID.--&gt; FI using Member concept should set field PRL.INDICATOR &gt; PROLENDER.PARAM as NO to fetch all the response details based on the Member ID. |
| 88 | `PRL.PAR.LB.LN.CUR.BAL.TYPE` | `ProlenderParam_LbLnCurBalType` | TField |  |  |
| 89 | `PRL.PAR.LB.LN.OAMT.BALTYPE` | `ProlenderParam_LbLnOamtBaltype` | TField |  |  |
| 90 | `PRL.PAR.LB.LN.INRT.PRP.CLS` | `ProlenderParam_LbLnInrtPrpCls` | TField |  |  |
| 91 | `PRL.PAR.LB.LN.INRT.PRP.NAM` | `ProlenderParam_LbLnInrtPrpNam` | TField |  |  |
| 92 | `PRL.PAR.LB.LN.PTFR.PRP.CLS` | `ProlenderParam_LbLnPtfrPrpCls` | TField |  |  |
| 93 | `PRL.PAR.LB.LN.PTFR.PRP.NAM` | `ProlenderParam_LbLnPtfrPrpNam` | TField |  |  |
| 94 | `PRL.PAR.LB.AC.INRT.PRP.CLS` | `ProlenderParam_LbAcInrtPrpCls` | TField |  |  |
| 95 | `PRL.PAR.LB.AC.INRT.PRP.NAM` | `ProlenderParam_LbAcInrtPrpNam` | TField |  |  |
| 96 | `PRL.PAR.LB.AC.PTFR.PRP.CLS` | `ProlenderParam_LbAcPtfrPrpCls` | TField |  |  |
| 97 | `PRL.PAR.LB.AC.PTFR.PRP.NAM` | `ProlenderParam_LbAcPtfrPrpNam` | TField |  |  |
| 98 | `PRL.PAR.ARR.ACT.VERSION` | `ProlenderParam_ArrActVersion` | TField |  | field to store the Version used to post AA.ARRANGEMENT.ACTIVITYeg. AA.ARRANGEMENT.ACTIVITY,PRL |
| 99 | `PRL.PAR.ACCASHPOOL.VERSION` | `ProlenderParam_AccashpoolVersion` | TField |  | Field to store Version used to post AC.CASH.POOL.When a loan is lnked with a coverdraft, system updates the AC cash pool record using the version defined in this field.Eg. AC.CASH.POOL,PRL |
| 100 | `PRL.PAR.SIM.CAP.VERSION` | `ProlenderParam_SimCapVersion` | TField |  | Field to store the Version used to post AA.SIMULATION.CAPTUREvalid records of VERSIONeg. AA.SIMULATION.CAPTURE,AA.DRILL.PAYOFF.PRL |
| 101 | `PRL.PAR.CIF.UPD.VERSION` | `ProlenderParam_CifUpdVersion` | TField |  | Field used to store the version to be used to update the Customer record.Version to be updated for 2 tier.Applicable for FI using CIF concept.Validations - Records of VERSIONeg. CUSTOMER,CAMB.PRL.INPUT |
| 102 | `PRL.PAR.CUS.UPD.VERSION` | `ProlenderParam_CusUpdVersion` | TField |  | Field used to store the version to be used to update the Customer record.Version to be updated for 3 tier.Applicable for FI using Member concept.Validations - Records of VERSIONeg. CUSTOMER,CAMB.PRL.INPUT |
| 103 | `PRL.PAR.EXCL.BRANCH` | `ProlenderParam_ExclBranch` |  |  |  |
| 104 | `PRL.PAR.LIM.ONLY.PROD` | `ProlenderParam_LimOnlyProd` |  |  |  |
| 105 | `PRL.PAR.PRL.PAY.TYPEFRQ` | `ProlenderParam_PrlPayTypefrq` |  |  |  |
| 106 | `PRL.PAR.LIB.PAY.FRQ` | `ProlenderParam_LibPayFrq` |  |  |  |
| 107 | `PRL.PAR.T24.LIAB.PROD` | `ProlenderParam_T24LiabProd` |  |  |  |
| 108 | `PRL.PAR.PRL.LIAB.GRP` | `ProlenderParam_PrlLiabGrp` |  |  |  |
| 109 | `PRL.PAR.HI.RATIO.TXN.CODE` | `ProlenderParam_HiRatioTxnCode` |  |  |  |
| 110 | `PRL.PAR.HI.RATIO.COMP` | `ProlenderParam_HiRatioComp` |  |  |  |
| 111 | `PRL.PAR.LOC.INT.UPD.ACT` | `ProlenderParam_LocIntUpdAct` | TField |  | The LOC Interest update Activity defined here will be update the Debit Interest for the Chequeing Accounts through 'Create Loan' request |
| 112 | `PRL.PAR.LOC.INT.PROP` | `ProlenderParam_LocIntProp` | TField |  | The LOC Interest Property defined here will be update the Debit Interest for the Chequeing Accounts through 'Create Loan' request |
| 113 | `PRL.PAR.PRL.EMP.ADDR` | `ProlenderParam_PrlEmpAddr` |  |  |  |
| 114 | `PRL.PAR.PRL.ADDR.IND` | `ProlenderParam_PrlAddrInd` | TField |  |  |
| 115 | `PRL.PAR.EXCL.PROP` | `ProlenderParam_ExclProp` |  |  |  |
| 116 | `PRL.PAR.PRL.RES.REG` | `ProlenderParam_PrlResReg` | TField |  |  |
| 117 | `PRL.PAR.RESERVED.14` | `ProlenderParam_Reserved14` | TField |  |  |
| 118 | `PRL.PAR.RESERVED.15` | `ProlenderParam_Reserved15` | TField |  |  |
| 119 | `PRL.PAR.RESERVED.16` | `ProlenderParam_Reserved16` | TField |  |  |
| 120 | `PRL.PAR.RESERVED.17` | `ProlenderParam_Reserved17` | TField |  |  |
| 121 | `PRL.PAR.RESERVED.18` | `ProlenderParam_Reserved18` | TField |  |  |
| 122 | `PRL.PAR.RESERVED.19` | `ProlenderParam_Reserved19` | TField |  |  |
| 123 | `PRL.PAR.LOCAL.REF` | `ProlenderParam_LocalRef` |  |  |  |
| 124 | `PRL.PAR.RECORD.STATUS` | `ProlenderParam_RecordStatus` | String |  |  |
| 125 | `PRL.PAR.CURR.NO` | `ProlenderParam_CurrNo` | String |  |  |
| 126 | `PRL.PAR.INPUTTER` | `ProlenderParam_Inputter` |  |  |  |
| 127 | `PRL.PAR.DATE.TIME` | `ProlenderParam_DateTime` |  |  |  |
| 128 | `PRL.PAR.AUTHORISER` | `ProlenderParam_Authoriser` | String |  |  |
| 129 | `PRL.PAR.CO.CODE` | `ProlenderParam_CoCode` | String |  |  |
| 130 | `PRL.PAR.DEPT.CODE` | `ProlenderParam_DeptCode` | String |  |  |
| 131 | `PRL.PAR.AUDITOR.CODE` | `ProlenderParam_AuditorCode` | String |  |  |
| 132 | `PRL.PAR.AUDIT.DATE.TIME` | `ProlenderParam_AuditDateTime` | String |  |  |
