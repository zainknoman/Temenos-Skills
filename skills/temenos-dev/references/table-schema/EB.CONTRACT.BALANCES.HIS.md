# EB.CONTRACT.BALANCES.HIS — Table Schema

> Source: `INSERTS/I_F.EB.CONTRACT.BALANCES.HIS` in `BF_ConBalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ECB.CURRENCY` | `EbContractBalancesHis_Currency` | TField |  |  |
| 2 | `ECB.TYPE.SYSDATE` | `EbContractBalancesHis_TypeSysdate` |  |  |  |
| 3 | `ECB.VALUE.DATE` | `EbContractBalancesHis_ValueDate` |  |  |  |
| 4 | `ECB.MAT.DATE` | `EbContractBalancesHis_MatDate` |  |  |  |
| 5 | `ECB.OPEN.BALANCE` | `EbContractBalancesHis_OpenBalance` |  |  |  |
| 6 | `ECB.OPEN.BAL.LCL` | `EbContractBalancesHis_OpenBalLcl` |  |  |  |
| 7 | `ECB.CREDIT.MVMT` | `EbContractBalancesHis_CreditMvmt` |  |  |  |
| 8 | `ECB.CR.MVMT.LCL` | `EbContractBalancesHis_CrMvmtLcl` |  |  |  |
| 9 | `ECB.DEBIT.MVMT` | `EbContractBalancesHis_DebitMvmt` |  |  |  |
| 10 | `ECB.DB.MVMT.LCL` | `EbContractBalancesHis_DbMvmtLcl` |  |  |  |
| 11 | `ECB.NAU.MVMT` | `EbContractBalancesHis_NauMvmt` |  |  |  |
| 12 | `ECB.NAU.TXN.ID` | `EbContractBalancesHis_NauTxnId` |  |  |  |
| 13 | `ECB.CURR.ASSET.TYPE` | `EbContractBalancesHis_CurrAssetType` |  |  |  |
| 14 | `ECB.CONSOL.KEY` | `EbContractBalancesHis_ConsolKey` | TField |  |  |
| 15 | `ECB.OPEN.ASSET.TYPE` | `EbContractBalancesHis_OpenAssetType` | TField |  |  |
| 16 | `ECB.CO.CODE` | `EbContractBalancesHis_CoCode` | String |  |  |
| 17 | `ECB.POSS.SIGN.CHANGE` | `EbContractBalancesHis_PossSignChange` | TField |  |  |
| 18 | `ECB.NS.UPDATE.INDICATOR` | `EbContractBalancesHis_NsUpdateIndicator` | TField |  |  |
| 19 | `ECB.APPLICATION` | `EbContractBalancesHis_Application` | TField |  |  |
| 20 | `ECB.PRODUCT` | `EbContractBalancesHis_Product` | TField |  |  |
| 21 | `ECB.DATE.LAST.UPDATE` | `EbContractBalancesHis_DateLastUpdate` | TField |  |  |
| 22 | `ECB.CUSTOMER` | `EbContractBalancesHis_Customer` | TField |  |  |
| 23 | `ECB.INTEREST.RATE` | `EbContractBalancesHis_InterestRate` | TField |  |  |
| 24 | `ECB.INTEREST.KEY` | `EbContractBalancesHis_InterestKey` | TField |  |  |
| 25 | `ECB.INTEREST.BASIS` | `EbContractBalancesHis_InterestBasis` | TField |  |  |
| 26 | `ECB.INTEREST.SPREAD` | `EbContractBalancesHis_InterestSpread` | TField |  |  |
| 27 | `ECB.REPORT.ITEM` | `EbContractBalancesHis_ReportItem` |  |  |  |
| 28 | `ECB.REPORT.VALUE` | `EbContractBalancesHis_ReportValue` |  |  |  |
| 29 | `ECB.PREV.CONSOL.KEY` | `EbContractBalancesHis_PrevConsolKey` | TField |  |  |
| 30 | `ECB.PREV.ASSET.TYPE` | `EbContractBalancesHis_PrevAssetType` | TField |  |  |
| 31 | `ECB.CONTRACT.VALUE.DATE` | `EbContractBalancesHis_ContractValueDate` | TField |  |  |
| 32 | `ECB.BALANCE.TYPE` | `EbContractBalancesHis_BalanceType` |  |  |  |
| 33 | `ECB.ACTIVITY.ID` | `EbContractBalancesHis_ActivityId` |  |  |  |
| 34 | `ECB.LAST.CAP.DATE` | `EbContractBalancesHis_LastCapDate` |  |  |  |
| 35 | `ECB.STMT.ENT.IDS` | `EbContractBalancesHis_StmtEntIds` |  |  |  |
| 36 | `ECB.STMT.SPLIT.ID` | `EbContractBalancesHis_StmtSplitId` | TField |  |  |
| 37 | `ECB.CONSOL.ENT.IDS` | `EbContractBalancesHis_ConsolEntIds` |  |  |  |
| 38 | `ECB.CONSOL.SPLIT.ID` | `EbContractBalancesHis_ConsolSplitId` | TField |  |  |
| 39 | `ECB.CATEG.ENT.IDS` | `EbContractBalancesHis_CategEntIds` |  |  |  |
| 40 | `ECB.CATEG.SPLIT.ID` | `EbContractBalancesHis_CategSplitId` | TField |  |  |
| 41 | `ECB.ACCR.CATEGORY` | `EbContractBalancesHis_AccrCategory` |  |  |  |
| 42 | `ECB.ACCR.CRF.TYPE` | `EbContractBalancesHis_AccrCrfType` |  |  |  |
| 43 | `ECB.ACCR.BOOKING.DATE` | `EbContractBalancesHis_AccrBookingDate` |  |  |  |
| 44 | `ECB.ACCR.TRANS.CODE` | `EbContractBalancesHis_AccrTransCode` |  |  |  |
| 45 | `ECB.ACCR.SYSTEM.ID` | `EbContractBalancesHis_AccrSystemId` |  |  |  |
| 46 | `ECB.ACCR.AMOUNT` | `EbContractBalancesHis_AccrAmount` |  |  |  |
| 47 | `ECB.ACCR.AMOUNT.LCY` | `EbContractBalancesHis_AccrAmountLcy` |  |  |  |
| 48 | `ECB.ACCR.OPP.AMOUNT` | `EbContractBalancesHis_AccrOppAmount` |  |  |  |
| 49 | `ECB.ACCR.EXRATE` | `EbContractBalancesHis_AccrExrate` |  |  |  |
| 50 | `ECB.ACCR.NAU.AMT` | `EbContractBalancesHis_AccrNauAmt` |  |  |  |
| 51 | `ECB.ACCR.NAU.AMT.LCY` | `EbContractBalancesHis_AccrNauAmtLcy` |  |  |  |
| 52 | `ECB.ACCR.NAU.OPP.AMT` | `EbContractBalancesHis_AccrNauOppAmt` |  |  |  |
| 53 | `ECB.ACCR.NAU.EXRATE` | `EbContractBalancesHis_AccrNauExrate` |  |  |  |
| 54 | `ECB.ACTIVITY.MONTHS` | `EbContractBalancesHis_ActivityMonths` |  |  |  |
| 55 | `ECB.BAL.TYPE` | `EbContractBalancesHis_BalType` |  |  |  |
| 56 | `ECB.BT.ACT.MONTHS` | `EbContractBalancesHis_BtActMonths` |  |  |  |
| 57 | `ECB.COLLAT.RIGHT` | `EbContractBalancesHis_CollatRight` |  |  |  |
| 58 | `ECB.COLLATERAL` | `EbContractBalancesHis_Collateral` |  |  |  |
| 59 | `ECB.STMT.PROC.DATE` | `EbContractBalancesHis_StmtProcDate` |  |  |  |
| 60 | `ECB.NO.OF.STMT` | `EbContractBalancesHis_NoOfStmt` |  |  |  |
| 61 | `ECB.RISK.LIMIT.REF` | `EbContractBalancesHis_RiskLimitRef` | TField |  |  |
| 62 | `ECB.RISK.COLL.RGT.ID` | `EbContractBalancesHis_RiskCollRgtId` |  |  |  |
| 63 | `ECB.RISK.COLL.ID` | `EbContractBalancesHis_RiskCollId` |  |  |  |
| 64 | `ECB.COLL.CCY` | `EbContractBalancesHis_CollCcy` |  |  |  |
| 65 | `ECB.ALLOC.AMT` | `EbContractBalancesHis_AllocAmt` |  |  |  |
| 66 | `ECB.CATEG.PROCESS.DATE` | `EbContractBalancesHis_CategProcessDate` |  |  |  |
| 67 | `ECB.CATEG.ENTRY.IDS` | `EbContractBalancesHis_CategEntryIds` |  |  |  |
| 68 | `ECB.OPEN.ACTUAL.BAL` | `EbContractBalancesHis_OpenActualBal` | TField |  |  |
| 69 | `ECB.OPEN.CLEARED.BAL` | `EbContractBalancesHis_OpenClearedBal` | TField |  |  |
| 70 | `ECB.ONLINE.ACTUAL.BAL` | `EbContractBalancesHis_OnlineActualBal` | TField |  |  |
| 71 | `ECB.ONLINE.CLEARED.BAL` | `EbContractBalancesHis_OnlineClearedBal` | TField |  |  |
| 72 | `ECB.WORKING.BALANCE` | `EbContractBalancesHis_WorkingBalance` | TField |  |  |
| 73 | `ECB.OPEN.AVAILABLE.BAL` | `EbContractBalancesHis_OpenAvailableBal` | TField |  |  |
| 74 | `ECB.AVAILABLE.DATE` | `EbContractBalancesHis_AvailableDate` |  |  |  |
| 75 | `ECB.AV.AUTH.DB.MVMT` | `EbContractBalancesHis_AvAuthDbMvmt` |  |  |  |
| 76 | `ECB.AV.NAU.DB.MVMT` | `EbContractBalancesHis_AvNauDbMvmt` |  |  |  |
| 77 | `ECB.AV.AUTH.CR.MVMT` | `EbContractBalancesHis_AvAuthCrMvmt` |  |  |  |
| 78 | `ECB.AV.NAU.CR.MVMT` | `EbContractBalancesHis_AvNauCrMvmt` |  |  |  |
| 79 | `ECB.AVAILABLE.BAL` | `EbContractBalancesHis_AvailableBal` |  |  |  |
| 80 | `ECB.FORWARD.MVMTS` | `EbContractBalancesHis_ForwardMvmts` |  |  |  |
| 81 | `ECB.FIRST.AF.DATE` | `EbContractBalancesHis_FirstAfDate` | TField |  |  |
| 82 | `ECB.NEXT.AF.DATE` | `EbContractBalancesHis_NextAfDate` | TField |  |  |
| 83 | `ECB.NEXT.EXP.DATE` | `EbContractBalancesHis_NextExpDate` | TField |  |  |
| 84 | `ECB.EXPOSURE.DATES` | `EbContractBalancesHis_ExposureDates` |  |  |  |
| 85 | `ECB.INITIATOR.TYPE` | `EbContractBalancesHis_InitiatorType` |  |  |  |
| 86 | `ECB.DATE.LAST` | `EbContractBalancesHis_DateLast` |  |  |  |
| 87 | `ECB.AMNT.LAST` | `EbContractBalancesHis_AmntLast` |  |  |  |
| 88 | `ECB.TRANS.LAST` | `EbContractBalancesHis_TransLast` |  |  |  |
| 89 | `ECB.LAST.AC.BAL.UPD` | `EbContractBalancesHis_LastAcBalUpd` | TField |  |  |
| 90 | `ECB.BALANCE.MOVED` | `EbContractBalancesHis_BalanceMoved` | TField |  |  |
| 91 | `ECB.AUTH.PAY.MVMT` | `EbContractBalancesHis_AuthPayMvmt` | TField |  |  |
| 92 | `ECB.AUTH.RECEIVE.MVMT` | `EbContractBalancesHis_AuthReceiveMvmt` | TField |  |  |
| 93 | `ECB.TRADE.DATED.GL.BAL` | `EbContractBalancesHis_TradeDatedGlBal` | TField |  |  |
| 94 | `ECB.TOT.UNAUTH.CR` | `EbContractBalancesHis_TotUnauthCr` | TField |  |  |
| 95 | `ECB.TOT.UNAUTH.DB` | `EbContractBalancesHis_TotUnauthDb` | TField |  |  |
| 96 | `ECB.TOT.FWD.UNAU.CR` | `EbContractBalancesHis_TotFwdUnauCr` | TField |  |  |
| 97 | `ECB.TOT.FWD.UNAU.DB` | `EbContractBalancesHis_TotFwdUnauDb` | TField |  |  |
| 98 | `ECB.UNAUTH.KEY` | `EbContractBalancesHis_UnauthKey` |  |  |  |
| 99 | `ECB.FWD.UNAUTH.KEY` | `EbContractBalancesHis_FwdUnauthKey` |  |  |  |
| 100 | `ECB.HVT.FLAG` | `EbContractBalancesHis_HvtFlag` | TField |  |  |
| 101 | `ECB.LAST.UPDATE.TIME` | `EbContractBalancesHis_LastUpdateTime` |  |  |  |
| 102 | `ECB.ACCOUNTING.COMPANY` | `EbContractBalancesHis_AccountingCompany` | TField |  |  |
| 103 | `ECB.CCY.LIST` | `EbContractBalancesHis_CcyList` |  |  |  |
| 104 | `ECB.FROM.DATE` | `EbContractBalancesHis_FromDate` |  |  |  |
| 105 | `ECB.LOCKED.AMT` | `EbContractBalancesHis_LockedAmt` |  |  |  |
| 106 | `ECB.AUTH.FUT.EXP.BAL` | `EbContractBalancesHis_AuthFutExpBal` | TField |  |  |
| 107 | `ECB.UNAU.FUT.EXP.BAL` | `EbContractBalancesHis_UnauFutExpBal` | TField |  |  |
| 108 | `ECB.UNAU.FWD.MVMT` | `EbContractBalancesHis_UnauFwdMvmt` | TField |  |  |
| 109 | `ECB.SWEEP.ACCOUNT` | `EbContractBalancesHis_SweepAccount` |  |  |  |
| 110 | `ECB.PROJECTED.CR.AMT` | `EbContractBalancesHis_ProjectedCrAmt` |  |  |  |
| 111 | `ECB.PROJECTED.DR.AMT` | `EbContractBalancesHis_ProjectedDrAmt` |  |  |  |
| 112 | `ECB.PROJECTED.RESERVED.07` | `EbContractBalancesHis_ProjectedReserved07` |  |  |  |
| 113 | `ECB.PROJECTED.RESERVED.06` | `EbContractBalancesHis_ProjectedReserved06` |  |  |  |
| 114 | `ECB.PROJECTED.RESERVED.05` | `EbContractBalancesHis_ProjectedReserved05` |  |  |  |
| 115 | `ECB.PROJECTED.RESERVED.04` | `EbContractBalancesHis_ProjectedReserved04` |  |  |  |
| 116 | `ECB.PROJECTED.RESERVED.03` | `EbContractBalancesHis_ProjectedReserved03` |  |  |  |
| 117 | `ECB.PROJECTED.RESERVED.02` | `EbContractBalancesHis_ProjectedReserved02` |  |  |  |
| 118 | `ECB.PROJECTED.RESERVED.01` | `EbContractBalancesHis_ProjectedReserved01` |  |  |  |
| 119 | `ECB.COLLATERAL.RIGHT.ID` | `EbContractBalancesHis_CollateralRightId` |  |  |  |
| 120 | `ECB.CO.ALLOCATED.BALANCE` | `EbContractBalancesHis_CoAllocatedBalance` |  |  |  |
| 121 | `ECB.CO.UTILISED.BALANCE` | `EbContractBalancesHis_CoUtilisedBalance` |  |  |  |
| 122 | `ECB.CO.UNUTILISED.BALANCE` | `EbContractBalancesHis_CoUnutilisedBalance` |  |  |  |
| 123 | `ECB.CR.FROM.DATE` | `EbContractBalancesHis_CrFromDate` |  |  |  |
| 124 | `ECB.CR.LOCKED.AMT` | `EbContractBalancesHis_CrLockedAmt` |  |  |  |
| 125 | `ECB.CR.FROM.DATE.RESERVED.1` | `EbContractBalancesHis_CrFromDateReserved1` |  |  |  |
| 126 | `ECB.CR.FROM.DATE.RESERVED.2` | `EbContractBalancesHis_CrFromDateReserved2` |  |  |  |
| 127 | `ECB.CR.FROM.DATE.RESERVED.3` | `EbContractBalancesHis_CrFromDateReserved3` |  |  |  |
| 128 | `ECB.VIRTUAL.BALANCE.AMT` | `EbContractBalancesHis_VirtualBalanceAmt` | TField |  |  |
| 129 | `ECB.CURRENT.EXPOSURE.DATE` | `EbContractBalances_CurrentExposureDate` | TField |  | Indicates the date when the exposure amount in summary account under daylight structure was reset to zero. The date updated in this field is based on the time zone's calender date. The exposure in the summary account under daylight structure will be reset based on online service AC.CLEAR.SUMMARY.EXPOSURE. Once the reset is success, the date in the summary account will be cycled to the current local zone date of the company in which summary account is created. The current exposure date of summary account will also be updated in its respective transaction accounts. If the date is cycled in summary account based on the service, the current exposure date in transaction account will be cycled to be in sync with summary account only post the first exposure impact in the transaction account for that day. |
| 130 | `ECB.END.OF.REC.CRF` | `EbContractBalances_EndOfRecCrf` | TField |  | There is no business functionality behind this field. This field is to indicate the last field in ECB. It will not have any value |
