# EB.CONTRACT.BALANCES — Table Schema

> Source: `INSERTS/I_F.EB.CONTRACT.BALANCES` in `BF_ConBalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ECB.CURRENCY` | `EbContractBalances_Currency` | TField |  | CURRENCY Indicates the currency of the balances record. Indicates the currency of the associated contract leg and the currency of the various P&amp;L accounting movements raised in respect of the contract. Validation Rules: 3 Alpha-numeric Currency code. Internal file, no input . |
| 2 | `ECB.TYPE.SYSDATE` | `EbContractBalances_TypeSysdate` |  |  |  |
| 3 | `ECB.VALUE.DATE` | `EbContractBalances_ValueDate` |  |  |  |
| 4 | `ECB.MAT.DATE` | `EbContractBalances_MatDate` |  |  |  |
| 5 | `ECB.OPEN.BALANCE` | `EbContractBalances_OpenBalance` |  |  |  |
| 6 | `ECB.OPEN.BAL.LCL` | `EbContractBalances_OpenBalLcl` |  |  |  |
| 7 | `ECB.CREDIT.MVMT` | `EbContractBalances_CreditMvmt` |  |  |  |
| 8 | `ECB.CR.MVMT.LCL` | `EbContractBalances_CrMvmtLcl` |  |  |  |
| 9 | `ECB.DEBIT.MVMT` | `EbContractBalances_DebitMvmt` |  |  |  |
| 10 | `ECB.DB.MVMT.LCL` | `EbContractBalances_DbMvmtLcl` |  |  |  |
| 11 | `ECB.NAU.MVMT` | `EbContractBalances_NauMvmt` |  |  |  |
| 12 | `ECB.NAU.TXN.ID` | `EbContractBalances_NauTxnId` |  |  |  |
| 13 | `ECB.CURR.ASSET.TYPE` | `EbContractBalances_CurrAssetType` |  |  |  |
| 14 | `ECB.CONSOL.KEY` | `EbContractBalances_ConsolKey` | TField |  | Contains the key of the Consolidation record ( in the CONSOLIDATE.ASST.LIAB) into which the details if this record is being consolidated. Validation Rules: Alphanumeric, as specified in the Consolidate Conditions file (CONSOLIDATE.COND) Internal file, no input |
| 15 | `ECB.OPEN.ASSET.TYPE` | `EbContractBalances_OpenAssetType` | TField |  | This field holds the opening asset type for applications such as Accounts, Securities and DX where the main principal type can change sign. Validation Rules: Valid hard-coded Balance type Multi-value field associated with Balance.Type Internal file, no input |
| 16 | `ECB.CO.CODE` | `EbContractBalances_CoCode` | String |  | Contains the company code of the transaction. |
| 17 | `ECB.POSS.SIGN.CHANGE` | `EbContractBalances_PossSignChange` | TField |  | This field holds a flag to indicate if the contract has changed sign during the day. It is automatically set to 'Y' if CURR.ASSET.TYPE not equal to OPEN.ASSET.TYPE. For example if a debit transaction has caused the sign of an account to move from credit to debit, then the Open.Asset.Type would be 'CREDIT' while the CURR.ASSET.TYPE would be 'DEBIT' and the POSS.SIGN.CHANGE would be set to 'Y'. The Close of Business would then : 1 Raise the required entries to move the balance of this contract from the CREDIT side to the DEBIT side of the Consolidate.Asset.Liab record 2 Initialize the flag. Validation Rules: 'Y' or blank Internal field, no input . |
| 18 | `ECB.NS.UPDATE.INDICATOR` | `EbContractBalances_NsUpdateIndicator` | TField |  | This field is reserved for future use.. |
| 19 | `ECB.APPLICATION` | `EbContractBalances_Application` | TField |  | This field holds the underlying application, e.g ACCOUNT. It can be used for reporting/enquiry drilldown |
| 20 | `ECB.PRODUCT` | `EbContractBalances_Product` | TField |  | This field holds the product code of the contract e.g. AC, FDO |
| 21 | `ECB.DATE.LAST.UPDATE` | `EbContractBalances_DateLastUpdate` | TField |  | This field records the date of the last system update. |
| 22 | `ECB.CUSTOMER` | `EbContractBalances_Customer` | TField |  | This field is reserved for future use. |
| 23 | `ECB.INTEREST.RATE` | `EbContractBalances_InterestRate` | TField |  | This field is reserved for future use.. |
| 24 | `ECB.INTEREST.KEY` | `EbContractBalances_InterestKey` | TField |  | This field is reserved for future use.. |
| 25 | `ECB.INTEREST.BASIS` | `EbContractBalances_InterestBasis` | TField |  | Interest day basis of the contracts |
| 26 | `ECB.INTEREST.SPREAD` | `EbContractBalances_InterestSpread` | TField |  | This field is reserved for future use.. |
| 27 | `ECB.REPORT.ITEM` | `EbContractBalances_ReportItem` |  |  |  |
| 28 | `ECB.REPORT.VALUE` | `EbContractBalances_ReportValue` |  |  |  |
| 29 | `ECB.PREV.CONSOL.KEY` | `EbContractBalances_PrevConsolKey` | TField |  | This field holds the previous day's consol key, it should hold the same value as in the field CONSOL.KEY , unless a static change has occurred during the Close of Business. Validation Rules: Alphanumeric, as specified in the Consolidate Conditions file (CONSOLIDATE.COND) Internal file, no input |
| 30 | `ECB.PREV.ASSET.TYPE` | `EbContractBalances_PrevAssetType` | TField |  | This field holds the opening asset type for the previous day, for applications such as Accounts, Securities and DX where the main principal type can change sign. It should the same value as in the field OPEN.ASSET.TYPE unless a sign change has occurred during the Close of Business. Validation Rules: Valid hard-coded Balance type Internal file, no input |
| 31 | `ECB.CONTRACT.VALUE.DATE` | `EbContractBalances_ContractValueDate` | TField |  | CONTRACT.VALUE.DATE is one of the static information which is displayed in reports generated in EOD. Hence field is updated to be extracted at EOD for reporting purposes. Validation rules: No input field -Updated by system |
| 32 | `ECB.BALANCE.TYPE` | `EbContractBalances_BalanceType` |  |  |  |
| 33 | `ECB.ACTIVITY.ID` | `EbContractBalances_ActivityId` |  |  |  |
| 34 | `ECB.LAST.CAP.DATE` | `EbContractBalances_LastCapDate` |  |  |  |
| 35 | `ECB.STMT.ENT.IDS` | `EbContractBalances_StmtEntIds` |  |  |  |
| 36 | `ECB.STMT.SPLIT.ID` | `EbContractBalances_StmtSplitId` | TField |  | When the STMT.ENTRY IDs updated in STMT.ENT.IDS field exceed the threshold then we will update the remaining IDs in EB.CONTRACT.ENTRIES table. In this field we will update the total number of splits happened to handle the limits |
| 37 | `ECB.CONSOL.ENT.IDS` | `EbContractBalances_ConsolEntIds` |  |  |  |
| 38 | `ECB.CONSOL.SPLIT.ID` | `EbContractBalances_ConsolSplitId` | TField |  | If the RE.CONSOL.SPEC.ENTRY raised for the contract exceed the limit then system will split the entry IDs and updates the remaining entries in EB.CONTRACT.ENTRIES. This field hold the total number of such entry split present for the contract |
| 39 | `ECB.CATEG.ENT.IDS` | `EbContractBalances_CategEntIds` |  |  |  |
| 40 | `ECB.CATEG.SPLIT.ID` | `EbContractBalances_CategSplitId` | TField |  | If the CATEG.ENTRY raised for the contract exceed the limit then system will split the entry IDs and updates the remaining entries in EB.CONTRACT.ENTRIES. This field hold the number of such entry split present for the contract |
| 41 | `ECB.ACCR.CATEGORY` | `EbContractBalances_AccrCategory` |  |  |  |
| 42 | `ECB.ACCR.CRF.TYPE` | `EbContractBalances_AccrCrfType` |  |  |  |
| 43 | `ECB.ACCR.BOOKING.DATE` | `EbContractBalances_AccrBookingDate` |  |  |  |
| 44 | `ECB.ACCR.TRANS.CODE` | `EbContractBalances_AccrTransCode` |  |  |  |
| 45 | `ECB.ACCR.SYSTEM.ID` | `EbContractBalances_AccrSystemId` |  |  |  |
| 46 | `ECB.ACCR.AMOUNT` | `EbContractBalances_AccrAmount` |  |  |  |
| 47 | `ECB.ACCR.AMOUNT.LCY` | `EbContractBalances_AccrAmountLcy` |  |  |  |
| 48 | `ECB.ACCR.OPP.AMOUNT` | `EbContractBalances_AccrOppAmount` |  |  |  |
| 49 | `ECB.ACCR.EXRATE` | `EbContractBalances_AccrExrate` |  |  |  |
| 50 | `ECB.ACCR.NAU.AMT` | `EbContractBalances_AccrNauAmt` |  |  |  |
| 51 | `ECB.ACCR.NAU.AMT.LCY` | `EbContractBalances_AccrNauAmtLcy` |  |  |  |
| 52 | `ECB.ACCR.NAU.OPP.AMT` | `EbContractBalances_AccrNauOppAmt` |  |  |  |
| 53 | `ECB.ACCR.NAU.EXRATE` | `EbContractBalances_AccrNauExrate` |  |  |  |
| 54 | `ECB.ACTIVITY.MONTHS` | `EbContractBalances_ActivityMonths` |  |  |  |
| 55 | `ECB.BAL.TYPE` | `EbContractBalances_BalType` |  |  |  |
| 56 | `ECB.BT.ACT.MONTHS` | `EbContractBalances_BtActMonths` |  |  |  |
| 57 | `ECB.COLLAT.RIGHT` | `EbContractBalances_CollatRight` |  |  |  |
| 58 | `ECB.COLLATERAL` | `EbContractBalances_Collateral` |  |  |  |
| 59 | `ECB.STMT.PROC.DATE` | `EbContractBalances_StmtProcDate` |  |  |  |
| 60 | `ECB.NO.OF.STMT` | `EbContractBalances_NoOfStmt` |  |  |  |
| 61 | `ECB.RISK.LIMIT.REF` | `EbContractBalances_RiskLimitRef` | TField |  | Contains secured limit reference ID of the contract |
| 62 | `ECB.RISK.COLL.RGT.ID` | `EbContractBalances_RiskCollRgtId` |  |  |  |
| 63 | `ECB.RISK.COLL.ID` | `EbContractBalances_RiskCollId` |  |  |  |
| 64 | `ECB.COLL.CCY` | `EbContractBalances_CollCcy` |  |  |  |
| 65 | `ECB.ALLOC.AMT` | `EbContractBalances_AllocAmt` |  |  |  |
| 66 | `ECB.CATEG.PROCESS.DATE` | `EbContractBalances_CategProcessDate` |  |  |  |
| 67 | `ECB.CATEG.ENTRY.IDS` | `EbContractBalances_CategEntryIds` |  |  |  |
| 68 | `ECB.OPEN.ACTUAL.BAL` | `EbContractBalances_OpenActualBal` | TField |  | Contains the actual (uncleared) balance or 'Ledger Balance' of the account as at the start of the day. |
| 69 | `ECB.OPEN.CLEARED.BAL` | `EbContractBalances_OpenClearedBal` | TField |  | Contains the cleared balance of the account as at the start of the day. This includes the value of all entries over the account except any credit entries or reversal debit with exposure dates in the future. |
| 70 | `ECB.ONLINE.ACTUAL.BAL` | `EbContractBalances_OnlineActualBal` | TField |  | Contains the current actual balance of the account.This is same as the actual balance at the start of day (Open Actual Balance) plus the value of all fully authorized entries since the start of day. |
| 71 | `ECB.ONLINE.CLEARED.BAL` | `EbContractBalances_OnlineClearedBal` | TField |  | Contains the current cleared balance of the account. This is same as the cleared balance at the start of day (Open Cleared Balance) plus the value of all fully authorized entries since the start of day, except any credit or reversal debit entries with future exposure dates. |
| 72 | `ECB.WORKING.BALANCE` | `EbContractBalances_WorkingBalance` | TField |  | Contains the present balance of the account which is used for checking by the Limits System etc. At the start of day this is same as the cleared balance (Online Cleared Balance). For Nostro and Internal Accounts, it is updated by all entries when they are fully authorized. For other Customer accounts it is updated by debit entries when they are validated and by credit entries when they are fully authorized, except for any credit or reversal debit entries with exposure dates in the future. For credit and reversal debit entries with exposure dates in the future, this field is updated at start of day on the appropriate date, by the program FWD.EXPOSURE. |
| 73 | `ECB.OPEN.AVAILABLE.BAL` | `EbContractBalances_OpenAvailableBal` | TField |  | This includes the value of all entries over the account except any credit entries or reversal debit with exposure dates in the future. |
| 74 | `ECB.AVAILABLE.DATE` | `EbContractBalances_AvailableDate` |  |  |  |
| 75 | `ECB.AV.AUTH.DB.MVMT` | `EbContractBalances_AvAuthDbMvmt` |  |  |  |
| 76 | `ECB.AV.NAU.DB.MVMT` | `EbContractBalances_AvNauDbMvmt` |  |  |  |
| 77 | `ECB.AV.AUTH.CR.MVMT` | `EbContractBalances_AvAuthCrMvmt` |  |  |  |
| 78 | `ECB.AV.NAU.CR.MVMT` | `EbContractBalances_AvNauCrMvmt` |  |  |  |
| 79 | `ECB.AVAILABLE.BAL` | `EbContractBalances_AvailableBal` |  |  |  |
| 80 | `ECB.FORWARD.MVMTS` | `EbContractBalances_ForwardMvmts` |  |  |  |
| 81 | `ECB.FIRST.AF.DATE` | `EbContractBalances_FirstAfDate` | TField |  | This field will hold the first available date of the ladder. |
| 82 | `ECB.NEXT.AF.DATE` | `EbContractBalances_NextAfDate` | TField |  | Contains the next exposure or value date for an entry for this account that lies outside the current available dates window. This is used by the start of day processing that updates the available balance fields. If the NEXT.AF.DATE becomes due then the relevant forward entries are incorporated into the available balances. |
| 83 | `ECB.NEXT.EXP.DATE` | `EbContractBalances_NextExpDate` | TField |  | Contains the next immediate future exposure date for an account. Usually the minimum of EXPOSURE.DATES field. |
| 84 | `ECB.EXPOSURE.DATES` | `EbContractBalances_ExposureDates` |  |  |  |
| 85 | `ECB.INITIATOR.TYPE` | `EbContractBalances_InitiatorType` |  |  |  |
| 86 | `ECB.DATE.LAST` | `EbContractBalances_DateLast` |  |  |  |
| 87 | `ECB.AMNT.LAST` | `EbContractBalances_AmntLast` |  |  |  |
| 88 | `ECB.TRANS.LAST` | `EbContractBalances_TransLast` |  |  |  |
| 89 | `ECB.LAST.AC.BAL.UPD` | `EbContractBalances_LastAcBalUpd` | TField |  | The system date of the last time the account record was moved |
| 90 | `ECB.BALANCE.MOVED` | `EbContractBalances_BalanceMoved` | TField |  | Field to indicate whether balance related field values are moved from Account to ECB |
| 91 | `ECB.AUTH.PAY.MVMT` | `EbContractBalances_AuthPayMvmt` | TField |  | Field to hold the total authorized payable movements for future dated cash based movements to an account under Trade date GL Accounting. Customer's account and bank's positions will be updated on the value date but the movements from the trade will he held under "Payable" Balances in the Balance Sheet GL on the trade date until the value date. When the transaction amount is credit, balance will be updated in this field and the non-contingent asset type 'PAY'. Validation Rules: Standard Amount Format Internal file, no input |
| 92 | `ECB.AUTH.RECEIVE.MVMT` | `EbContractBalances_AuthReceiveMvmt` | TField |  | Field to hold the total authorized receivable movements for future dated cash based movements to an account under Trade date GL Accounting. Customer's account and bank's positions will be updated on the value date but the movements from the trade will he held under "Receivable" Balances in the Balance Sheet GL on the trade date until the value date. When the transaction amount is debit, balance will be updated in this field and the non-contingent asset type 'RECEIVE'. Validation Rules: Standard Amount Format Internal file, no input |
| 93 | `ECB.TRADE.DATED.GL.BAL` | `EbContractBalances_TradeDatedGlBal` | TField |  | Balance field that will represent the cash balance of an Account including future dated movements that will be processed to the account irrespective of the accounting system. It is the sum of the ONLINE.ACTUAL.BALANCE + AUTH.PAY.MVMT + AUTH.RECEIVE.MVMT. Whenever ONLINE.ACTUAL.BALANACE is affected, this balance field will be recalculated and updated irrespective of the accounting system. This field is used for credit checking. Validation Rules: Standard Amount Format Internal file, no input |
| 94 | `ECB.TOT.UNAUTH.CR` | `EbContractBalances_TotUnauthCr` | TField |  | Holds the total unauthorized credit transaction amount. |
| 95 | `ECB.TOT.UNAUTH.DB` | `EbContractBalances_TotUnauthDb` | TField |  | Holds the total unauthorized debit transaction amount. |
| 96 | `ECB.TOT.FWD.UNAU.CR` | `EbContractBalances_TotFwdUnauCr` | TField |  | Contains the total amount of forward unauthorized credit transactions |
| 97 | `ECB.TOT.FWD.UNAU.DB` | `EbContractBalances_TotFwdUnauDb` | TField |  | Total amount of forward unauthorized debit transactions |
| 98 | `ECB.UNAUTH.KEY` | `EbContractBalances_UnauthKey` |  |  |  |
| 99 | `ECB.FWD.UNAUTH.KEY` | `EbContractBalances_FwdUnauthKey` |  |  |  |
| 100 | `ECB.HVT.FLAG` | `EbContractBalances_HvtFlag` | TField |  | The field HVT.FLAG in the account record controls whether an account is high volume or not. If this field is set to Yes it indicates that this is an account, which has a high volume of transactions every day. No or Null indicates that it is not a high volume account. |
| 101 | `ECB.LAST.UPDATE.TIME` | `EbContractBalances_LastUpdateTime` |  |  |  |
| 102 | `ECB.ACCOUNTING.COMPANY` | `EbContractBalances_AccountingCompany` | TField |  | Holds the accounting company of the underline contract record. This company ID will be determined based on AU rules. Only set when accounting companies are linked to the normal T24 business company This field will be updated only if AU product is installed in the company Validation Rules: Must be a valid company record with consolidation mark set as 'A' Internal file, no input |
| 103 | `ECB.CCY.LIST` | `EbContractBalances_CcyList` |  |  |  |
| 104 | `ECB.FROM.DATE` | `EbContractBalances_FromDate` |  |  |  |
| 105 | `ECB.LOCKED.AMT` | `EbContractBalances_LockedAmt` |  |  |  |
| 106 | `ECB.AUTH.FUT.EXP.BAL` | `EbContractBalances_AuthFutExpBal` | TField |  | This field will hold the sum of all authorized future exposure dated credits entries for the account. This will hold balances for any future exposure date irrespective of cash flow ladder days defined in ACCOUNT.PARAMETER, this is because even for current Available.Balance ladder we extend the cash flow window size for real entries. The balance in the field will be reversed when the transaction is reversed.This field is updated only for AR accounts with Component as Credit Check . |
| 107 | `ECB.UNAU.FUT.EXP.BAL` | `EbContractBalances_UnauFutExpBal` | TField |  | This field will hold the sum of all unauthorized future exposure dated credits entries for the account. This will hold balances for any future exposure date irrespective of cash flow ladder days defined in ACCOUNT.PARAMETER, this is because even for current Available.Balance ladder we extend the cash flow window size for real entries. The balance in the field will be reversed when the transaction is deleted.This field is updated only for AR accounts with Component as Credit Check . |
| 108 | `ECB.UNAU.FWD.MVMT` | `EbContractBalances_UnauFwdMvmt` | TField |  | This field will hold sum of all unauthorized Forward entries for the given account within cash flow days defined in the account parameter. The balance in the field will be reversed when the transaction is deleted.This field is updated only for AR accounts with Component as Credit Check . |
| 109 | `ECB.SWEEP.ACCOUNT` | `EbContractBalances_SweepAccount` |  |  |  |
| 110 | `ECB.PROJECTED.CR.AMT` | `EbContractBalances_ProjectedCrAmt` |  |  |  |
| 111 | `ECB.PROJECTED.DR.AMT` | `EbContractBalances_ProjectedDrAmt` |  |  |  |
| 112 | `ECB.PROJECTED.RESERVED.07` | `EbContractBalances_ProjectedReserved07` |  |  |  |
| 113 | `ECB.PROJECTED.RESERVED.06` | `EbContractBalances_ProjectedReserved06` |  |  |  |
| 114 | `ECB.PROJECTED.RESERVED.05` | `EbContractBalances_ProjectedReserved05` |  |  |  |
| 115 | `ECB.PROJECTED.RESERVED.04` | `EbContractBalances_ProjectedReserved04` |  |  |  |
| 116 | `ECB.PROJECTED.RESERVED.03` | `EbContractBalances_ProjectedReserved03` |  |  |  |
| 117 | `ECB.PROJECTED.RESERVED.02` | `EbContractBalances_ProjectedReserved02` |  |  |  |
| 118 | `ECB.PROJECTED.RESERVED.01` | `EbContractBalances_ProjectedReserved01` |  |  |  |
| 119 | `ECB.COLLATERAL.RIGHT.ID` | `EbContractBalances_CollateralRightId` |  |  |  |
| 120 | `ECB.CO.ALLOCATED.BALANCE` | `EbContractBalances_CoAllocatedBalance` |  |  |  |
| 121 | `ECB.CO.UTILISED.BALANCE` | `EbContractBalances_CoUtilisedBalance` |  |  |  |
| 122 | `ECB.CO.UNUTILISED.BALANCE` | `EbContractBalances_CoUnutilisedBalance` |  |  |  |
| 123 | `ECB.CR.FROM.DATE` | `EbContractBalances_CrFromDate` |  |  |  |
| 124 | `ECB.CR.LOCKED.AMT` | `EbContractBalances_CrLockedAmt` |  |  |  |
| 125 | `ECB.CR.FROM.DATE.RESERVED.1` | `EbContractBalances_CrFromDateReserved1` |  |  |  |
| 126 | `ECB.CR.FROM.DATE.RESERVED.2` | `EbContractBalances_CrFromDateReserved2` |  |  |  |
| 127 | `ECB.CR.FROM.DATE.RESERVED.3` | `EbContractBalances_CrFromDateReserved3` |  |  |  |
| 128 | `ECB.VIRTUAL.BALANCE.AMT` | `EbContractBalancesHis_VirtualBalanceAmt` | TField |  |  |
| 129 | `ECB.CURRENT.EXPOSURE.DATE` | `EbContractBalances_CurrentExposureDate` | TField |  | Indicates the date when the exposure amount in summary account under daylight structure was reset to zero. The date updated in this field is based on the time zone's calender date. The exposure in the summary account under daylight structure will be reset based on online service AC.CLEAR.SUMMARY.EXPOSURE. Once the reset is success, the date in the summary account will be cycled to the current local zone date of the company in which summary account is created. The current exposure date of summary account will also be updated in its respective transaction accounts. If the date is cycled in summary account based on the service, the current exposure date in transaction account will be cycled to be in sync with summary account only post the first exposure impact in the transaction account for that day. |
| 130 | `ECB.END.OF.REC.CRF` | `EbContractBalances_EndOfRecCrf` | TField |  | There is no business functionality behind this field. This field is to indicate the last field in ECB. It will not have any value |
