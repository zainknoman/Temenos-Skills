# EB.CASHFLOW — Table Schema

> Source: `INSERTS/I_F.EB.CASHFLOW` in `CW_CashFlow.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IA.CSHF.CUSTOMER.ID` | `EbCashflow_CustomerId` | TField |  | Field denotes the customer related to the contract. |
| 2 | `IA.CSHF.IAS.CLASSIFICATION` | `EbCashflow_IasClassification` | TField |  | This field denotes the IAS.CLASSIFICATION id. IFRS reporting classifications like Eg: AMC, FVOCI etc |
| 3 | `IA.CSHF.IAS.SUB.TYPE` | `EbCashflow_IasSubType` | TField |  | This field denotes the IFRS.SUB.TYPE id assigned to this contract. |
| 4 | `IA.CSHF.ACCOUNTING.METHOD` | `EbCashflow_AccountingMethod` | TField |  | This field will hold the key to IFRS.ACCT.METHODS file. This key is obtained from the IFRS.SUB.TYPE associated with the underlying contract. |
| 5 | `IA.CSHF.ASSET.LIAB.IND` | `EbCashflow_AssetLiabInd` | TField |  | This field is a Asset and Liability indicator, which will denote whether a contract is an asset or liability to the bank. Can be A(Asset) or L(Liability) |
| 6 | `IA.CSHF.CURRENCY` | `EbCashflow_Currency` | TField |  | This field denotes the contract currency. |
| 7 | `IA.CSHF.INTEREST.BASIS` | `EbCashflow_InterestBasis` | TField |  | This field denotes the INTEREST.BASIS of the underlying contract. |
| 8 | `IA.CSHF.MARKET.KEY` | `EbCashflow_MarketKey` | TField |  | This field denotes the market rate for the contract. This can either be a ID in PERIODIC.INTEREST table or the actual rate itself. |
| 9 | `IA.CSHF.MARKET.MARGIN` | `EbCashflow_MarketMargin` | TField |  | Flexibility is given to the user through the field MARKET.MARGIN to include margin as a percentage of the market rate in to the calculation of the fair value. Both positive and negative margin percentage can be inputted. For example if the market rate is 10%. With the positive margin of +0.50%, the net rate for the calculation will be 10.50% and with a negative margin of -0.50%, the net rate for the calculation will be 9.50%. |
| 10 | `IA.CSHF.MARGIN.OPERAND` | `EbCashflow_MarginOperand` | TField |  | This field denotes the OPERAND which will be used along with MARKET.MARGIN. Example: +/- + then market.key will be added with market.margin to arrive at the final rate - then market.key is subtracted from market.margin to arrive at the final rate |
| 11 | `IA.CSHF.CONTRACT.RATE` | `EbCashflow_ContractRate` | TField |  | This field denotes the Rate used in the underlying contract. |
| 12 | `IA.CSHF.VALUE.DATE` | `EbCashflow_ValueDate` | TField |  | This field denotes the value date of the contract. |
| 13 | `IA.CSHF.MATURITY.DATE` | `EbCashflow_MaturityDate` | TField |  | This field denotes the maturity date of the contract. |
| 14 | `IA.CSHF.ACCRUAL.METHOD` | `EbCashflow_AccrualMethod` | TField |  | Field denoting the accrual method followed by the underlying contract. This field will provide the link to the table EB.ACCRUAL.PARAM which determines how accruals are performed by the core accrual processing. |
| 15 | `IA.CSHF.PRFT.LOSS.FLAG` | `EbCashflow_PrftLossFlag` | TField |  | This field denotes whether a contract is fetching profit or loss to a bank.This field value is updated for contracts valued at FAIRVALUE. Profit/Loss is determined by comparing current book balance with the NPV amount. For impaired contracts, Profit/Loss is determined by comparing if current carrying amount(book balance + past dues) is greater than the total recoverable value. |
| 16 | `IA.CSHF.TAKEOVER.DATE` | `EbCashflow_TakeoverDate` | TField |  | Date on which the contract is taken over to IFRS |
| 17 | `IA.CSHF.TAKEOVER.NPV` | `EbCashflow_TakeoverNpv` |  |  |  |
| 18 | `IA.CSHF.TAKEOVER.TYPE` | `EbCashflow_TakeoverType` |  |  |  |
| 19 | `IA.CSHF.CASH.FLOW.DATE` | `EbCashflow_CashFlowDate` |  |  |  |
| 20 | `IA.CSHF.CASH.FLOW.TYPE` | `EbCashflow_CashFlowType` |  |  |  |
| 21 | `IA.CSHF.CASH.FLOW.AMT` | `EbCashflow_CashFlowAmt` |  |  |  |
| 22 | `IA.CSHF.CASHFLOW.CCY` | `EbCashflow_CashflowCcy` |  |  |  |
| 23 | `IA.CSHF.AMOUNT` | `EbCashflow_Amount` |  |  |  |
| 24 | `IA.CSHF.EXLD.FROM.EIR` | `EbCashflow_ExldFromEir` |  |  |  |
| 25 | `IA.CSHF.RESERVED.5` | `EbCashflow_Reserved5` |  |  |  |
| 26 | `IA.CSHF.APR.CALC.EXCLUDE` | `EbCashflow_AprCalcExclude` |  |  |  |
| 27 | `IA.CSHF.RESERVED.3` | `EbCashflow_Reserved3` |  |  |  |
| 28 | `IA.CSHF.RESERVED.2` | `EbCashflow_Reserved2` |  |  |  |
| 29 | `IA.CSHF.RESERVED.1` | `EbCashflow_Reserved1` |  |  |  |
| 30 | `IA.CSHF.ASSET.TYPE` | `EbCashflow_AssetType` |  |  |  |
| 31 | `IA.CSHF.CARRY.COST` | `EbCashflow_CarryCost` |  |  |  |
| 32 | `IA.CSHF.POSTING.DETAILS.ID` | `EbCashflow_PostingDetailsId` | TField |  | This field will have the IFRS.POSTING.DETAILS ID, which will be updated by the system. |
| 33 | `IA.CSHF.EIR.REQD` | `EbCashflow_EirReqd` | TField |  | This field will have a flag to indicate whether EIR re-calculation is required or not. Value can be 'Y' or 'N'. Value of 'Y' indicates re-calculation is required. |
| 34 | `IA.CSHF.RATE.FIX.DATE` | `EbCashflow_RateFixDate` | TField |  | This field denotes the date from which the new rate, in case of a rate fixing contract, will be applicable. |
| 35 | `IA.CSHF.OUTSTANDING.AMT` | `EbCashflow_OutstandingAmt` | TField |  | This field denotes the outstanding amount to the bank as on the rate fix date. This field is mainly used for repricing, updated when IFRS.SUB.TYPE TERM is SHORT. When TERM is set as 'SHORT', the system will calculate the EIR only up to the next rate fixing date and income will be amortised over this period. |
| 36 | `IA.CSHF.AMENDMENT.DATE` | `EbCashflow_AmendmentDate` | TField |  | In case of an amendment to the cash flow, this field will hold the date on which the amendment happened. Note: This field will not contain the system date. It holds the date of amendment as per the cash flow. |
| 37 | `IA.CSHF.EVENT.TYPE` | `EbCashflow_EventType` |  |  |  |
| 38 | `IA.CSHF.RECALC.LOGIC` | `EbCashflow_RecalcLogic` | TField |  | In IFRS.SUB.TYPE, The fields EVENT.TYPE and RECALC.METHOD will form a multi-value set, where different events related to cash flow amendments can be given along with the recalculation methods. The two recalculation methods that are possible are EIR and CARRY.COST When the recalculation method is specified as EIR, the system will recalculate the EIR in case of a cash flow changes due to the corresponding event When the recalculation method is specified as CARRY.COST, then the system will adjust the carrying amount of the contract without recalculating the EIR |
| 39 | `IA.CSHF.EIR` | `EbCashflow_Eir` | TField |  | This field will store the effective rate of interest calculated based on the cash flow projections supplied to the cashflow engine by the applications which is then used by the IFRS processing to calculate the EIR. |
| 40 | `IA.CSHF.AMEND.ASSET.TYP` | `EbCashflow_AmendAssetTyp` |  |  |  |
| 41 | `IA.CSHF.AMD.PRV.YR.AMT` | `EbCashflow_AmdPrvYrAmt` |  |  |  |
| 42 | `IA.CSHF.AMD.PRV.MON.AMT` | `EbCashflow_AmdPrvMonAmt` |  |  |  |
| 43 | `IA.CSHF.AMD.CUR.MON.AMT` | `EbCashflow_AmdCurMonAmt` |  |  |  |
| 44 | `IA.CSHF.RECALC.COMPLETED` | `EbCashflow_RecalcCompleted` | TField |  | When there is a amendment to the cash flow, system raises adjustment entries through the service IFRS.AMENDMENT.SERVICE. Upon completion of the service, this field will be updated as "YES". |
| 45 | `IA.CSHF.EXP.CFLOW.DATE` | `EbCashflow_ExpCflowDate` |  |  |  |
| 46 | `IA.CSHF.EXP.CFLOW.TYPE` | `EbCashflow_ExpCflowType` |  |  |  |
| 47 | `IA.CSHF.EXP.CFLOW.AMT` | `EbCashflow_ExpCflowAmt` |  |  |  |
| 48 | `IA.CSHF.EXP.CFLOW.CCY` | `EbCashflow_ExpCflowCcy` |  |  |  |
| 49 | `IA.CSHF.EXP.AMOUNT` | `EbCashflow_ExpAmount` |  |  |  |
| 50 | `IA.CSHF.EXP.EXLD.EIR` | `EbCashflow_ExpExldEir` |  |  |  |
| 51 | `IA.CSHF.RESERVED.19` | `EbCashflow_Reserved19` |  |  |  |
| 52 | `IA.CSHF.RESERVED.20` | `EbCashflow_Reserved20` |  |  |  |
| 53 | `IA.CSHF.RESERVED.21` | `EbCashflow_Reserved21` |  |  |  |
| 54 | `IA.CSHF.RESERVED.22` | `EbCashflow_Reserved22` |  |  |  |
| 55 | `IA.CSHF.RESERVED.23` | `EbCashflow_Reserved23` |  |  |  |
| 56 | `IA.CSHF.COLLATERAL.ID` | `EbCashflow_CollateralId` |  |  |  |
| 57 | `IA.CSHF.COLLAT.PERCENT` | `EbCashflow_CollatPercent` |  |  |  |
| 58 | `IA.CSHF.COLL.EXPIRY.DAT` | `EbCashflow_CollExpiryDat` |  |  |  |
| 59 | `IA.CSHF.EXP.COLL.DATE` | `EbCashflow_ExpCollDate` |  |  |  |
| 60 | `IA.CSHF.EXP.COLL.AMT` | `EbCashflow_ExpCollAmt` |  |  |  |
| 61 | `IA.CSHF.FEED.OPTION` | `EbCashflow_FeedOption` |  |  |  |
| 62 | `IA.CSHF.RECOVERABLE.AMT` | `EbCashflow_RecoverableAmt` |  |  |  |
| 63 | `IA.CSHF.COLL.RATE.AMORT` | `EbCashflow_CollRateAmort` |  |  |  |
| 64 | `IA.CSHF.COLL.RATE.FV` | `EbCashflow_CollRateFv` |  |  |  |
| 65 | `IA.CSHF.RESERVED.24` | `EbCashflow_Reserved24` |  |  |  |
| 66 | `IA.CSHF.RESERVED.25` | `EbCashflow_Reserved25` |  |  |  |
| 67 | `IA.CSHF.RESERVED.26` | `EbCashflow_Reserved26` |  |  |  |
| 68 | `IA.CSHF.RESERVED.27` | `EbCashflow_Reserved27` |  |  |  |
| 69 | `IA.CSHF.RESERVED.28` | `EbCashflow_Reserved28` |  |  |  |
| 70 | `IA.CSHF.IMPAIRMENT.STATUS` | `EbCashflow_ImpairmentStatus` | TField |  | Field to denote the status of the contract with respect to impairment. Below are the possible values, IMPAIR.EVIDENCE : Evidence of impairment but no loss or no impairment accounting raised. IMPAIRED : Evidence of impairment with loss and impairment accounting raised. UNIMPAIRED : No longer evidence of impairment and impairment loss has been reversed. |
| 71 | `IA.CSHF.IMPAIR.EFF.DATE` | `EbCashflow_ImpairEffDate` |  |  |  |
| 72 | `IA.CSHF.IMPAIRMENT.LOSS` | `EbCashflow_ImpairmentLoss` |  |  |  |
| 73 | `IA.CSHF.DATE.IMP.EVIDENCE` | `EbCashflow_DateImpEvidence` | TField |  | The date that a contract has been impaired for the first time but for which no impairment loss has been raised, status becomes IMPAIR.EVIDENCE This date will not change even when the contract becomes IMPAIRED |
| 74 | `IA.CSHF.DATE.IMPAIRED` | `EbCashflow_DateImpaired` | TField |  | The date that a contract has been impaired for the first time and impairment loss has been raised, status becomes IMPAIRED This date will not change even when the contracts becomes UNIMPAIRED If the contract is UNIMPAIRED and is then IMPAIRED again, then the date will change to the date it is impaired again. |
| 75 | `IA.CSHF.DATE.UNIMPAIRED` | `EbCashflow_DateUnimpaired` | TField |  | The date that a contract has been unimpaired, status has moved from IMPAIRED to UNIMPAIRED This date is not changed until the contract is UNIMPAIRED again. |
| 76 | `IA.CSHF.IMPAIRMENT.CODE` | `EbCashflow_ImpairmentCode` |  |  |  |
| 77 | `IA.CSHF.ACTION.NOTES` | `EbCashflow_ActionNotes` |  |  |  |
| 78 | `IA.CSHF.TRANS.REFERENCE` | `EbCashflow_TransReference` | TField |  | The key to the application that triggered the change to the EB.CASHFLOW record. Usually IFRS.DATA.CAPTURE id is stored here. |
| 79 | `IA.CSHF.RESERVED.32` | `EbCashflow_Reserved32` | TField |  |  |
| 80 | `IA.CSHF.PREV.IAS.CLASS` | `EbCashflow_PrevIasClass` | TField |  | This field denotes the previous IFRS classification under which this contract was classified. |
| 81 | `IA.CSHF.PREV.IAS.SUB.TYPE` | `EbCashflow_PrevIasSubType` | TField |  | This field denotes the previous IFRS.SUB.TYPE under which this contract was classified. |
| 82 | `IA.CSHF.RECLASSIFIED.AMT` | `EbCashflow_ReclassifiedAmt` | TField |  | Reserved for future use. |
| 83 | `IA.CSHF.STATUS` | `EbCashflow_Status` | TField |  | Field denoting the overall status of the EB.CASHFLOW record. Field values can be REV,MAT When contract is matured, status is updated as MAT and on reversal, status is updated as REV |
| 84 | `IA.CSHF.PRODUCT.CATEGORY` | `EbCashflow_ProductCategory` | TField |  | Holds Valid Category from CATEGORY, Category specified in the underlying contract will be populated in this field |
| 85 | `IA.CSHF.STAGE` | `EbCashflow_Stage` | TField |  | Hold the details of the current stage of the contract based on the definition in IFRS.PARAMETER. Values may be 1 or 2 or 3. Stage 1 - as soon as a financial instrument is originated or purchased it is classified as stage 1,includes financial instruments that have not had a significant increase in credit risk since initial recognition or that have low credit risk at the reporting date.For these assets, 12-month expected credit losses (�ECL�) are recognised. Stage 2 - includes financial instruments that have had a significant increase in credit risk since initial recognition but that do not have objective evidence of impairment. Stage 3 - when credit risk increases to the point where the financial instrument is considered as "credit-impaired".These are financial assets that have objective evidence of impairment. Manual movement of stages are also possible, this is enabled via IFRS.DATA.CAPTURE application - OPERATION STAGE.CHANGE or PV.ASSET.DETAIL - by changing the risk classification, which will mapped to corresponding stage in IFRS.PARAMETER. |
| 86 | `IA.CSHF.NEXT.REVIEW.DATE` | `EbCashflow_NextReviewDate` | TField |  | The next review date on which the stage would be reviewed based on the loan classification. |
| 87 | `IA.CSHF.APPLICATION` | `EbCashflow_Application` | TField |  | This field denotes product code of the underlying contract. Eg: AC (Account), LD(LD.LOANS.AND.DEPOSITS) etc. |
| 88 | `IA.CSHF.IFRS9.PRFT.LOSS.FLAG` | `EbCashflow_Ifrs9PrftLossFlag` | TField |  |  |
| 89 | `IA.CSHF.EXPECTED.LIFE.END` | `EbCashflow_ExpectedLifeEnd` | TField |  | Updates the expected life end date from the expected term date contracts. When the field TERM in IFRS.SUB.TYPE is set as EXPECTED it means this is applicable for contracts with an expected term. Cashflow engine will consolidate the contractual cashflows to fit into the expected term for a set of cashflows required for the EIR calculation. All contractual cashflows beyond the expected life end (based on the Expected term and the Start date) will be consolidated under the expected life end. The system will calculate the EIR up to the expected life end date, and the Amortised cost will be calculated as the NPV of the cashflows till the Expected life end. |
| 90 | `IA.CSHF.CALC.TYPE` | `EbCashflow_CalcType` |  |  |  |
| 91 | `IA.CSHF.CALC.RATE` | `EbCashflow_CalcRate` |  |  |  |
| 92 | `IA.CSHF.CONTRACT.TYPE` | `EbCashflow_ContractType` | TField |  | This field holds value as COMMITMENT, when EB.CASHFLOW record is built for AA commitment contract |
| 93 | `IA.CSHF.RESERVED.18` | `EbCashflow_Reserved18` | TField |  |  |
| 94 | `IA.CSHF.RECORD.STATUS` | `EbCashflow_RecordStatus` | String |  | Standard T24 audit field. |
| 95 | `IA.CSHF.CURR.NO` | `EbCashflow_CurrNo` | String |  | Standard T24 audit field. |
| 96 | `IA.CSHF.INPUTTER` | `EbCashflow_Inputter` |  |  |  |
| 97 | `IA.CSHF.DATE.TIME` | `EbCashflow_DateTime` |  |  |  |
| 98 | `IA.CSHF.AUTHORISER` | `EbCashflow_Authoriser` | String |  | Standard T24 audit field. |
| 99 | `IA.CSHF.CO.CODE` | `EbCashflow_CoCode` | String |  | Standard T24 audit field. |
| 100 | `IA.CSHF.DEPT.CODE` | `EbCashflow_DeptCode` | String |  | Standard T24 audit field. |
| 101 | `IA.CSHF.AUDITOR.CODE` | `EbCashflow_AuditorCode` | String |  | Standard T24 audit field. |
| 102 | `IA.CSHF.AUDIT.DATE.TIME` | `EbCashflow_AuditDateTime` | String |  | Standard T24 audit field. |
| 103 | `IA.CSHF.EXCLUDE.OPTION` | `EbCashflow_ExcludeOption` |  |  |  |
| 104 | `IA.CSHF.RESERVED.33` | `EbCashflow_Reserved33` | TField |  |  |
| 105 | `IA.CSHF.FEE.PROPERTY` | `EbCashflow_FeeProperty` |  |  |  |
| 106 | `IA.CSHF.FEE.AMOUNT` | `EbCashflow_FeeAmount` |  |  |  |
| 107 | `IA.CSHF.FEE.SUSP.OPTION` | `EbCashflow_FeeSuspOption` |  |  |  |
| 108 | `IA.CSHF.SUSPEND.DATE` | `EbCashflow_SuspendDate` | TField |  | This field stores the date on which the contract has moved to non-performing status(suspended status) |
| 109 | `IA.CSHF.SUSPEND.FLAG` | `EbCashflow_SuspendFlag` | TField |  | A flag to indicate whether contract is suspended or not. Updated as YES when the contract is non-performing(suspended). |
| 110 | `IA.CSHF.CHARGEOFF.FLAG` | `EbCashflow_ChargeoffFlag` | TField |  | Banks initiate charge-off on a loan when they got the objective evidence that the customer will not repay This field holds the chargeoff status of a contract. Field values can be FULL/PARTIAL/NULL based on whether the contract is fully or partially or not charged off |
| 111 | `IA.CSHF.GAAP.POS.TYPE` | `EbCashflow_GaapPosType` |  |  |  |
| 112 | `IA.CSHF.GAAP.ACCT.METHOD` | `EbCashflow_GaapAcctMethod` |  |  |  |
| 113 | `IA.CSHF.GAAP.POST.DETAIL` | `EbCashflow_GaapPostDetail` |  |  |  |
| 114 | `IA.CSHF.TAKEOVER.FEE.PROPERTY` | `EbCashflow_TakeoverFeeProperty` |  |  |  |
| 115 | `IA.CSHF.TAKEOVER.FEE.AMOUNT` | `EbCashflow_TakeoverFeeAmount` |  |  |  |
| 116 | `IA.CSHF.MODIFICATION.DATE` | `EbCashflow_ModificationDate` | TField |  | This field holds the date of the modification |
| 117 | `IA.CSHF.IFRS.EVENT` | `EbCashflow_IfrsEvent` | TField |  | This field holds the IFRS.EVENT that has triggered the modification Eg: FORBEARANCE. |
| 118 | `IA.CSHF.PREVIOUS.EIR` | `EbCashflow_PreviousEir` | TField |  | This field holds the previous (original) EIR prior to modification |
| 119 | `IA.CSHF.NPV.PREVIOUS.CASHFLOW` | `EbCashflow_NpvPreviousCashflow` | TField |  | This field holds the NPV of the previous cash flow before cashflow modification which is used for Quantitative test |
| 120 | `IA.CSHF.NPV.CURRENT.CASHFLOW` | `EbCashflow_NpvCurrentCashflow` | TField |  | This field holds the NPV of the current cash flow after cashflow modification which is used for Quantitative test |
| 121 | `IA.CSHF.MODIFICATION.PERCENT` | `EbCashflow_ModificationPercent` | TField |  | This field holds the modification percentage which is the % difference in NPV of the existing contractual cashflow at the original EIR (NPV.PREVIOUS.CASHFLOW) to the NPV of the modified cashflow at the the original EIR (NPV.CURRENT.CASHFLOW). |
| 122 | `IA.CSHF.MODIFICATION.GAIN.LOSS` | `EbCashflow_ModificationGainLoss` | TField |  | This field holds the modification gain or loss which is the difference in NPV of the existing contractual cashflow at the original EIR (NPV.PREVIOUS.CASHFLOW) to the NPV of the modified cashflow at the the original EIR (NPV.CURRENT.CASHFLOW). |
| 123 | `IA.CSHF.MODIFICATION.STATUS` | `EbCashflow_ModificationStatus` | TField |  | This field holds the status of the contract after modification If the value in MODIFICATION.PERCENT exceeds the specified threshold in IFRS.PARAMETER, then the modification is deemed �substantial' else 'non-substantial' Flagged as DERECOGNISED if modification is substantial or NON-SUBSTANTIAL if modification is non-substantial |
| 124 | `IA.CSHF.PREV.CONTRACT.ID` | `EbCashflow_PrevContractId` | TField |  |  |
| 125 | `IA.CSHF.MODIFICATION.REF` | `EbCashflow_ModificationRef` | TField |  |  |
| 126 | `IA.CSHF.ORIGINAL.CURR.NO` | `EbCashflow_OriginalCurrNo` |  |  |  |
| 127 | `IA.CSHF.CHARGEOFF.DATE` | `EbCashflow_ChargeoffDate` |  |  |  |
| 128 | `IA.CSHF.CHARGEOFF.AMT` | `EbCashflow_ChargeoffAmt` |  |  |  |
| 129 | `IA.CSHF.FEE.ACCRUAL.ID` | `EbCashflow_FeeAccrualId` |  |  |  |
| 130 | `IA.CSHF.RECOVERY.DATE` | `EbCashflow_RecoveryDate` |  |  |  |
| 131 | `IA.CSHF.RECOVERY.AMT` | `EbCashflow_RecoveryAmt` |  |  |  |
| 132 | `IA.CSHF.WRITEOFF.FLAG` | `EbCashflow_WriteoffFlag` | TField |  | If the loan is considered irrecoverable, then it is written off.This field will hold writeoff status of a loan. Field value can be - WRITE.OFF - Indicates that the loan is completely written off. PARTIAL.WRITE.OFF - Indicates that the loan is partially written off. |
| 133 | `IA.CSHF.OVERRIDE` | `EbCashflow_Override` |  |  |  |
| 134 | `IA.CSHF.BELOW.MARKET.CONTRACT` | `EbCashflow_BelowMarketContract` | TField |  | This text field indicates whether the contract is a below market rate contract. System updated field. Possible values are Yes, No, Null. |
| 135 | `IA.CSHF.MARKET.BASED.EIR` | `EbCashflow_MarketBasedEir` | TField |  | This field stores the Effective Interest Rate(EIR) computed based on the market rate of the contract. Below configuration and condition has to be met in order to compute market based EIR, 1. BELOW.MARKET.ACCTNG field in IFRS.ACCT.METHODS has to be set as Yes. 2. Then the contract will be marked for below market rate accounting, when the CONTRACT.RATE should be lesser than the market rate. |
