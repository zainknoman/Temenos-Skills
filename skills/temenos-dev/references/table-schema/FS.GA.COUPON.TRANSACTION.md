# FS.GA.COUPON.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUPON.TRANSACTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COUPON.TRANSACTION.AP.SERVICE` | `FsGaCouponTransaction_ApService` | TField |  | AP Multifonds DB Column is CSERVICE. |
| 2 | `COUPON.TRANSACTION.GLOBAL.AMOUNT` | `FsGaCouponTransaction_GlobalAmount` | TField |  | Global amount Multifonds DB Column is MNTGLOBAL. |
| 3 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX.AMOUNT` | `FsGaCouponTransaction_UnrecoverableTaxAmount` | TField |  | Unrecoverable tax amount Multifonds DB Column is MNTUNRECTAX. |
| 4 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX.2.AMOUNT` | `FsGaCouponTransaction_UnrecoverableTax2Amount` | TField |  | Unrecoverable tax 2 amount Multifonds DB Column is MNTUNRECTAX_2. |
| 5 | `COUPON.TRANSACTION.SERVICE.CODE.POT` | `FsGaCouponTransaction_ServiceCodePot` | TField |  | Service code Pot Multifonds DB Column is CSERV_POT. |
| 6 | `COUPON.TRANSACTION.GROSS.AMNT.IN.LOCAL.CCY` | `FsGaCouponTransaction_GrossAmount` |  |  |  |
| 7 | `COUPON.TRANSACTION.UNFRANKED.NCFI.AMOUNT` | `FsGaCouponTransaction_UnfrankedNcfiAmount` | TField |  | Unfranked NCFI Amount Multifonds DB Column is MNTUNFRANKED_NCFI. |
| 8 | `COUPON.TRANSACTION.UNFRANKED.NCFI.AMOUNT.FUND.ID` | `FsGaCouponTransaction_UnfrankedNcfiAmountFund` | TField |  | Unfranked NCFI Amount fund Multifonds DB Column is MNTUNFRANKED_NCFI_PTF. |
| 9 | `COUPON.TRANSACTION.RECOVERABLE.FATCA.AMOUNT` | `FsGaCouponTransaction_RecoverableFatcaAmount` | TField |  | Recoverable fatca amount Multifonds DB Column is MNT_FATCA2. |
| 10 | `COUPON.TRANSACTION.RECOVERABLE.FATCA.TAX2.AMOUNT` | `FsGaCouponTransaction_RecoverableFatcaTax2Amount` | TField |  | Recoverable fatca tax2 amount Multifonds DB Column is MNTFATCATAX2_PTF. |
| 11 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX.AMOUNT.FCY` | `FsGaCouponTransaction_UnrecoverableTaxAmountFcy` | TField |  | Unrecoverable tax amount fcy Multifonds DB Column is MNTUNRECTAX_FCY. |
| 12 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX.2.AMOUNT.FCY` | `FsGaCouponTransaction_UnrecoverableTax2AmountFcy` | TField |  | Unrecoverable tax 2 amount fcy Multifonds DB Column is MNTUNRECTAX_2_FCY. |
| 13 | `COUPON.TRANSACTION.FUND.ID` | `FsGaCouponTransaction_Fund` |  |  |  |
| 14 | `COUPON.TRANSACTION.SECURITY` | `FsGaCouponTransaction_Security` | TField |  | Security Multifonds DB Column is NOVAL. |
| 15 | `COUPON.TRANSACTION.CORRESPONDANT` | `FsGaCouponTransaction_Correspondant` | TField |  | Correspondant Multifonds DB Column is NCORRESP. |
| 16 | `COUPON.TRANSACTION.CONTRACT.NUMBER` | `FsGaCouponTransaction_ContractNumber` | TField |  | Contract number Multifonds DB Column is NCONTRAT. |
| 17 | `COUPON.TRANSACTION.ENTRY` | `FsGaCouponTransaction_Entry` | TField |  | Entry Multifonds DB Column is NECRITUR. |
| 18 | `COUPON.TRANSACTION.LINE` | `FsGaCouponTransaction_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 19 | `COUPON.TRANSACTION.STATUS` | `FsGaCouponTransaction_Status` | TField |  | Status Multifonds DB Column is CSTATUS. |
| 20 | `COUPON.TRANSACTION.DEPOSIT.NUMBER` | `FsGaCouponTransaction_DepositNumber` | TField |  | Deposit Number Multifonds DB Column is NDEPOSI. |
| 21 | `COUPON.TRANSACTION.DESCRIPTION` | `FsGaCouponTransaction_Description` | TField |  | Description Multifonds DB Column is XLIBELLE. |
| 22 | `COUPON.TRANSACTION.OP.CODE` | `FsGaCouponTransaction_OpCode` | TField |  | Op Code Multifonds DB Column is COPER. |
| 23 | `COUPON.TRANSACTION.LOCAL.CURRENCY` | `FsGaCouponTransaction_Currency` |  |  |  |
| 24 | `COUPON.TRANSACTION.PAYMENT.DATE` | `FsGaCouponTransaction_PaymentDate` | TField |  | Payment date Multifonds DB Column is DPAYMNT. |
| 25 | `COUPON.TRANSACTION.ACCOUNTING.DATE` | `FsGaCouponTransaction_AccountingDate` | TField |  | Accounting Date Multifonds DB Column is DJOURNAL. |
| 26 | `COUPON.TRANSACTION.VALUE.DATE` | `FsGaCouponTransaction_ValueDate` | TField |  | Value Date Multifonds DB Column is DVALEUR. |
| 27 | `COUPON.TRANSACTION.ENTITLEMENT.DATE` | `FsGaCouponTransaction_EntitlementDate` | TField |  | Entitlement Date Multifonds DB Column is DEXEC. |
| 28 | `COUPON.TRANSACTION.CORRESPONDENT.ACCOUNT.NUMBER` | `FsGaCouponTransaction_CorrespondentAccountNumber` | TField |  | Correspondent account number Multifonds DB Column is NRUBRDB. |
| 29 | `COUPON.TRANSACTION.CORRESPONDENT.GL.ACCOUNT.SUFFIX` | `FsGaCouponTransaction_CorrespondentSuffixNumber` | TField |  | Correspondent suffix number Multifonds DB Column is NSUFFDB. |
| 30 | `COUPON.TRANSACTION.CREDIT.ACCOUNT` | `FsGaCouponTransaction_CreditAccount` | TField |  | Credit account Multifonds DB Column is NRUBRCR. |
| 31 | `COUPON.TRANSACTION.SUFFIX.CREDIT` | `FsGaCouponTransaction_SuffixCredit` | TField |  | Suffix credit Multifonds DB Column is NSUFFCR. |
| 32 | `COUPON.TRANSACTION.SETTLEMENT.CURRENCY.CODE` | `FsGaCouponTransaction_SettlementCurrencyCode` | TField |  | Settlement currency code Multifonds DB Column is CMONDB. |
| 33 | `COUPON.TRANSACTION.CURRENCY.CREDIT` | `FsGaCouponTransaction_CurrencyCredit` | TField |  | Currency credit Multifonds DB Column is CMONCR. |
| 34 | `COUPON.TRANSACTION.NOMINAL.AMOUNT` | `FsGaCouponTransaction_NominalAmount` | TField |  | Nominal amount Multifonds DB Column is NOMINAL. |
| 35 | `COUPON.TRANSACTION.QUANTITY` | `FsGaCouponTransaction_Quantity` | TField |  | Quantity Multifonds DB Column is QUANTITE. |
| 36 | `COUPON.TRANSACTION.UNIT.AMOUNT` | `FsGaCouponTransaction_UnitAmountInSecurityCcy` |  |  |  |
| 37 | `COUPON.TRANSACTION.UNIT.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaCouponTransaction_UnitAmountInSettlementCcy` | TField |  | Unit amount in settlement ccy Multifonds DB Column is MNTUNIT_CORR. |
| 38 | `COUPON.TRANSACTION.PERCENTAGE.OF.CORESPONDENT.FEE` | `FsGaCouponTransaction_PercentageOfCorespondentFee` | TField |  | Percentage of corespondent fee Multifonds DB Column is PCOMCORR. |
| 39 | `COUPON.TRANSACTION.CORRESPONDENT.FEE.AMOUNT` | `FsGaCouponTransaction_CorrespondentFeeAmount` | TField |  | Correspondent fee amount Multifonds DB Column is MNTCOMCORR. |
| 40 | `COUPON.TRANSACTION.PERCENTAGE.OF.UNRECOVRABLE.TAX` | `FsGaCouponTransaction_PercentageOfUnrecovrableTax` | TField |  | Percentage of unrecovrable tax Multifonds DB Column is PUNRECTAX. |
| 41 | `COUPON.TRANSACTION.PERCENTAGE.OF.RECOVERABLE.TAX` | `FsGaCouponTransaction_PercentageOfRecoverableTax` | TField |  | Percentage of recoverable tax Multifonds DB Column is PRECTAX. |
| 42 | `COUPON.TRANSACTION.RECOVERABLE.TAX.AMOUNT` | `FsGaCouponTransaction_RecoverableTaxAmount` | TField |  | Recoverable tax amount Multifonds DB Column is MNTRECTAX. |
| 43 | `COUPON.TRANSACTION.NET.DIVIDEND.AMOUNT` | `FsGaCouponTransaction_NetDividendAmount` | TField |  | Net Dividend Amount Multifonds DB Column is MNTNET. |
| 44 | `COUPON.TRANSACTION.RATE.OF.EXCHANGE` | `FsGaCouponTransaction_ExchangeRate` |  |  |  |
| 45 | `COUPON.TRANSACTION.INTEREST.RATE.FOR.CASH` | `FsGaCouponTransaction_InterestRateForCash` | TField |  | Interest rate for cash Multifonds DB Column is TXINT. |
| 46 | `COUPON.TRANSACTION.ARCHIVE` | `FsGaCouponTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 47 | `COUPON.TRANSACTION.NET.AMOUNT.IN.FUND.LOCAL.CURRENCY` | `FsGaCouponTransaction_NetAmountInFundCurrency` | TField |  | Net amount in fund currency Multifonds DB Column is MNTNET_PTF. |
| 48 | `COUPON.TRANSACTION.EXCH.RATE.SETLMNT.AND.FUND.CCY` | `FsGaCouponTransaction_ExchRateSetlmntAndFundCcy` | TField |  | Exch rate setlmnt and fund Ccy Multifonds DB Column is TCHG_PTF. |
| 49 | `COUPON.TRANSACTION.MANUAL.SETLMNT.FLAG.FOR.CASH` | `FsGaCouponTransaction_ManualSetlmntFlagForCash` | TField |  | Manual setlmnt flag for cash Multifonds DB Column is CSETTLE_MANU. |
| 50 | `COUPON.TRANSACTION.PERCNTG.OF.UNRECOVERABLE.TAX.2` | `FsGaCouponTransaction_PercntgOfUnrecoverableTax2` | TField |  | Percntg of unrecoverable tax 2 Multifonds DB Column is PUNRECTAX_2. |
| 51 | `COUPON.TRANSACTION.PERCNTG.OF.RECOVERABLE.TAX.2` | `FsGaCouponTransaction_PercntgOfRecoverableTax2` | TField |  | Percntg of recoverable tax 2 Multifonds DB Column is PRECTAX_2. |
| 52 | `COUPON.TRANSACTION.RECOVERABLE.TAX.2.AMOUNT` | `FsGaCouponTransaction_RecoverableTax2Amount` | TField |  | Recoverable tax 2 amount Multifonds DB Column is MNTRECTAX_2. |
| 53 | `COUPON.TRANSACTION.TAX.CURRENCY.CODE.TAX.CCY` | `FsGaCouponTransaction_TaxCurrencyCodeTaxCcy` | TField |  | Tax currency code TAX_CCY Multifonds DB Column is CMON_IMPOT. |
| 54 | `COUPON.TRANSACTION.EX.RATE.STLMNT.CCY.AND.TAX.CCY` | `FsGaCouponTransaction_ExRateStlmntCcyAndTaxCcy` | TField |  | Ex rate stlmnt Ccy and tax Ccy Multifonds DB Column is TCHG_IMPOT. |
| 55 | `COUPON.TRANSACTION.TAX.AMOUNT` | `FsGaCouponTransaction_TaxAmount` | TField |  | Tax amount Multifonds DB Column is MNT_IMPOT. |
| 56 | `COUPON.TRANSACTION.TAX.AMOUNT.2` | `FsGaCouponTransaction_TaxAmount2` | TField |  | Tax amount 2 Multifonds DB Column is MNT_IMPOT_2. |
| 57 | `COUPON.TRANSACTION.NACC.MNGR` | `FsGaCouponTransaction_NaccMngr` | TField |  | Nacc Mngr Multifonds DB Column is NACC_MNGR. |
| 58 | `COUPON.TRANSACTION.PIK.INTEREST.RATE` | `FsGaCouponTransaction_PikInterestRate` | TField |  | Pik interest rate Multifonds DB Column is PIK_TXINT. |
| 59 | `COUPON.TRANSACTION.PIK.FACTOR` | `FsGaCouponTransaction_PikFactor` | TField |  | Pik factor Multifonds DB Column is PIK_FACTOR. |
| 60 | `COUPON.TRANSACTION.MARKET.VALUE.USED.FORBONDS` | `FsGaCouponTransaction_MarketValueUsedForbonds` | TField |  | Market value used forbonds Multifonds DB Column is MARKET_VALUE. |
| 61 | `COUPON.TRANSACTION.PIK.GROSS.AMNT.IN.LOCAL.CCY` | `FsGaCouponTransaction_PikGrossAmount` | TField |  | Pik gross amount Multifonds DB Column is MNTGLOBAL_PIK. |
| 62 | `COUPON.TRANSACTION.CORRESPONDENT.FEE.AMT.ON.BONDS` | `FsGaCouponTransaction_CorrespondentFeeAmtOnBonds` | TField |  | Correspondent fee amt on bonds Multifonds DB Column is MNTCOMCORR_PIK. |
| 63 | `COUPON.TRANSACTION.ACCRUED.DAYS.NUMBER` | `FsGaCouponTransaction_AccruedDaysNumber` | TField |  | Accrued days number Multifonds DB Column is NBJOURS. |
| 64 | `COUPON.TRANSACTION.NET.INPUTTED.MANUALLY.FLAG` | `FsGaCouponTransaction_NetInputtedManuallyFlag` | TField |  | Net inputted manually flag Multifonds DB Column is FLAG_BRUT. |
| 65 | `COUPON.TRANSACTION.MBS.FACTOR` | `FsGaCouponTransaction_MbsFactor` | TField |  | MBS factor Multifonds DB Column is FACTOR. |
| 66 | `COUPON.TRANSACTION.MANAGER.CODE` | `FsGaCouponTransaction_Manager` |  |  |  |
| 67 | `COUPON.TRANSACTION.UNIT.AMOUNT.CALCULATED.FLAG` | `FsGaCouponTransaction_UnitAmountCalculatedFlag` | TField |  | Unit amount calculated flag Multifonds DB Column is FLAG_CALCUL. |
| 68 | `COUPON.TRANSACTION.NUMBR.FOR.CAPITAL.POSITION.ADJ` | `FsGaCouponTransaction_NumbrForCapitalPositionAdj` | TField |  | Numbr for capital position adj Multifonds DB Column is NECRITUR_ADJ. |
| 69 | `COUPON.TRANSACTION.STATUS.PENDING` | `FsGaCouponTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 70 | `COUPON.TRANSACTION.PCR.FLAG` | `FsGaCouponTransaction_PcrFlag` | TField |  | PCR flag Multifonds DB Column is FLG_PCR. |
| 71 | `COUPON.TRANSACTION.PCR.2.FLAG` | `FsGaCouponTransaction_Pcr2Flag` | TField |  | PCR 2 flag Multifonds DB Column is FLG_PCR_2. |
| 72 | `COUPON.TRANSACTION.PCUR.FLAG` | `FsGaCouponTransaction_PcurFlag` | TField |  | PCUR Flag Multifonds DB Column is FLG_PCUR. |
| 73 | `COUPON.TRANSACTION.PCUR.2.FLAG` | `FsGaCouponTransaction_Pcur2Flag` | TField |  | PCUR 2 Flag Multifonds DB Column is FLG_PCUR_2. |
| 74 | `COUPON.TRANSACTION.NET.PIK` | `FsGaCouponTransaction_NetPik` | TField |  | Net PIK Multifonds DB Column is MNT_NET_PIK. |
| 75 | `COUPON.TRANSACTION.KEST` | `FsGaCouponTransaction_Kest` | TField |  | Kest Multifonds DB Column is MNTUNIT_RETAX_1. |
| 76 | `COUPON.TRANSACTION.KOST` | `FsGaCouponTransaction_Kost` | TField |  | Kost Multifonds DB Column is MNTUNIT_RETAX_2. |
| 77 | `COUPON.TRANSACTION.NET.AMOUNT.UNIT` | `FsGaCouponTransaction_NetUnitAmount` | TField |  | Net unit amount Multifonds DB Column is NET_UNIT_AMOUNT. |
| 78 | `COUPON.TRANSACTION.TAX.FACC` | `FsGaCouponTransaction_TaxFacc` | TField |  | Tax Facc Multifonds DB Column is TAX_FACC. |
| 79 | `COUPON.TRANSACTION.INTERNAL.DESCRIPTION` | `FsGaCouponTransaction_InternalDescription` | TField |  | Internal Description Multifonds DB Column is TXT_OST. |
| 80 | `COUPON.TRANSACTION.PERCENT.PAYABLE.TAX` | `FsGaCouponTransaction_PercentPayableTax` | TField |  | Percent payable tax Multifonds DB Column is PCT_TAX_1. |
| 81 | `COUPON.TRANSACTION.PAYABLE.TAX.AMOUNT` | `FsGaCouponTransaction_PayableTaxAmount` | TField |  | Payable tax amount Multifonds DB Column is MNT_TAX_1. |
| 82 | `COUPON.TRANSACTION.TAX1.FLAG` | `FsGaCouponTransaction_Tax1Flag` | TField |  | Tax-1 flag Multifonds DB Column is FLG_TAX_1. |
| 83 | `COUPON.TRANSACTION.AWV.Z4.NACHMELDUNG` | `FsGaCouponTransaction_AwvZ4Nachmeldung` | TField |  | AWV Z4 nachmeldung Multifonds DB Column is FLG_AWV. |
| 84 | `COUPON.TRANSACTION.RATE.PAYABLE.TAX.2` | `FsGaCouponTransaction_RatePayableTax2` | TField |  | Rate payable tax 2 Multifonds DB Column is PCT_TAX_2. |
| 85 | `COUPON.TRANSACTION.PAYABLE.TAX.2.AMOUNT` | `FsGaCouponTransaction_PayableTax2Amount` | TField |  | Payable tax 2 amount Multifonds DB Column is MNT_TAX_2. |
| 86 | `COUPON.TRANSACTION.TAX2.FLAG` | `FsGaCouponTransaction_Tax2Flag` | TField |  | Tax-2 flag Multifonds DB Column is FLG_TAX_2. |
| 87 | `COUPON.TRANSACTION.DCOUP` | `FsGaCouponTransaction_Dcoup` | TField |  | Dcoup Multifonds DB Column is DCOUP. |
| 88 | `COUPON.TRANSACTION.AMORTIZATION.AMOUNT.DEAL.CCY` | `FsGaCouponTransaction_AmortizationAmountDealCcy` | TField |  | Amortization amount deal Ccy Multifonds DB Column is MNT_AMORTISSEMENT_DEAL. |
| 89 | `COUPON.TRANSACTION.AMORTIZATION.AMOUNT` | `FsGaCouponTransaction_AmortizationAmount` | TField |  | Amortization amount Multifonds DB Column is MNT_AMORTISSEMENT. |
| 90 | `COUPON.TRANSACTION.COEFFCORPORATE.ACTION` | `FsGaCouponTransaction_CoeffcorporateAction` | TField |  | Coeff.corporate action Multifonds DB Column is COEF_CORP. |
| 91 | `COUPON.TRANSACTION.UNDERLYING.FUTURE.TYPE` | `FsGaCouponTransaction_UnderlyingFutureType` | TField |  | Underlying future type Multifonds DB Column is CHOIX. |
| 92 | `COUPON.TRANSACTION.SEC.LENDING.TAX.PERCENTAGE` | `FsGaCouponTransaction_SecLendingTaxPercentage` | TField |  | Sec Lending Tax Percentage Multifonds DB Column is PSECLENTAX. |
| 93 | `COUPON.TRANSACTION.SECURITY.LENDING.TAX.AMOUNT` | `FsGaCouponTransaction_SecurityLendingTaxAmount` | TField |  | Security Lending Tax Amount Multifonds DB Column is MNTSECLENTAX. |
| 94 | `COUPON.TRANSACTION.FUTURE.NUMBER` | `FsGaCouponTransaction_FutureNumber` | TField |  | Future number Multifonds DB Column is NFUT. |
| 95 | `COUPON.TRANSACTION.DIVIDEND.EXECUTION.DATE` | `FsGaCouponTransaction_DividendExecutionDate` | TField |  | Dividend execution date Multifonds DB Column is DEXEC_DIV. |
| 96 | `COUPON.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaCouponTransaction_ExternalReference` | TField |  | External reference Multifonds DB Column is EXT_REF. |
| 97 | `COUPON.TRANSACTION.FEES.PERCENTAGE` | `FsGaCouponTransaction_FeesPercentage` | TField |  | Fees Percentage Multifonds DB Column is MFRAIS1. |
| 98 | `COUPON.TRANSACTION.FEES.2.PERCENTAGE` | `FsGaCouponTransaction_Fees2Percentage` | TField |  | Fees 2 Percentage Multifonds DB Column is MFRAIS2. |
| 99 | `COUPON.TRANSACTION.FEES.AMOUNT` | `FsGaCouponTransaction_FeesAmount` | TField |  | Fees Amount Multifonds DB Column is MNTFRAIS1. |
| 100 | `COUPON.TRANSACTION.FEES.2.AMOUNT` | `FsGaCouponTransaction_Fees2Amount` | TField |  | Fees 2 Amount Multifonds DB Column is MNTFRAIS2. |
| 101 | `COUPON.TRANSACTION.PAYABLE.FEE.1` | `FsGaCouponTransaction_PayableFee1` | TField |  | Payable fee 1 Multifonds DB Column is FLG_FEE1. |
| 102 | `COUPON.TRANSACTION.PAYABLE.FEE.2` | `FsGaCouponTransaction_PayableFee2` | TField |  | Payable fee 2 Multifonds DB Column is FLG_FEE2. |
| 103 | `COUPON.TRANSACTION.STOCK.DIVIDEND.FLAG` | `FsGaCouponTransaction_StockDividendFlag` | TField |  | Stock dividend flag Multifonds DB Column is STK_DIV. |
| 104 | `COUPON.TRANSACTION.SETTLED.FLAG` | `FsGaCouponTransaction_SettledFlag` | TField |  | Settled Flag Multifonds DB Column is SETTLED_INC. |
| 105 | `COUPON.TRANSACTION.RECORD.DATE` | `FsGaCouponTransaction_RecordDate` | TField |  | Record date Multifonds DB Column is DRECORD. |
| 106 | `COUPON.TRANSACTION.LAST.FIRST.COUPON.DATE` | `FsGaCouponTransaction_LastCouponDate` | TField |  | Last coupon date Multifonds DB Column is DLASTCOUP_ORIG. |
| 107 | `COUPON.TRANSACTION.CHECK.DATE` | `FsGaCouponTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 108 | `COUPON.TRANSACTION.CHECKED.BY` | `FsGaCouponTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 109 | `COUPON.TRANSACTION.AUTO.MANUAL.TAX` | `FsGaCouponTransaction_AutoManualTax` | TField |  | Auto manual tax Multifonds DB Column is TAX_MANUAL_AUTO. |
| 110 | `COUPON.TRANSACTION.FVA.TAG` | `FsGaCouponTransaction_FvaTag` | TField |  | FVA Tag Multifonds DB Column is CGTI_IFRS. |
| 111 | `COUPON.TRANSACTION.LONG.DESC` | `FsGaCouponTransaction_LongDescription` |  |  |  |
| 112 | `COUPON.TRANSACTION.CASH.DIVIDEND.FLAG` | `FsGaCouponTransaction_CashDividendFlag` | TField |  | Cash dividend flag Multifonds DB Column is FLG_CASH_DIV. |
| 113 | `COUPON.TRANSACTION.DIVIDEND.TYPE` | `FsGaCouponTransaction_DividendType` | TField |  | Dividend type Multifonds DB Column is DIV_TYPE. |
| 114 | `COUPON.TRANSACTION.ELECTION.STATUS` | `FsGaCouponTransaction_ElectionStatus` | TField |  | Election status Multifonds DB Column is ELECTION_STATUS. |
| 115 | `COUPON.TRANSACTION.INSTRUCTION.STATUS` | `FsGaCouponTransaction_InstructionStatus` | TField |  | Instruction status Multifonds DB Column is INSTRUCTION_STATUS. |
| 116 | `COUPON.TRANSACTION.AUTO` | `FsGaCouponTransaction_Auto` | TField |  | Auto Multifonds DB Column is FLG_AUTO_PROCESS. |
| 117 | `COUPON.TRANSACTION.CASH.RATIO` | `FsGaCouponTransaction_CashRatio` | TField |  | Cash ratio Multifonds DB Column is CASH_RATIO. |
| 118 | `COUPON.TRANSACTION.CA.TRANSACTION.CODE` | `FsGaCouponTransaction_CaOperationCode` | TField |  | CA operation code Multifonds DB Column is COPER_CA. |
| 119 | `COUPON.TRANSACTION.SEQUENCE.NUMBER` | `FsGaCouponTransaction_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is NSEQ. |
| 120 | `COUPON.TRANSACTION.SUB.SEQUENCE.NUMBER` | `FsGaCouponTransaction_SubSequenceNumber` | TField |  | Sub Sequence Number Multifonds DB Column is NSUB_SEQ. |
| 121 | `COUPON.TRANSACTION.PA.MODULE.FLAG` | `FsGaCouponTransaction_PaModuleFlag` | TField |  | PA module flag Multifonds DB Column is FLG_PA_MODULE. |
| 122 | `COUPON.TRANSACTION.PA.CD.STATUS` | `FsGaCouponTransaction_PaCdStatus` | TField |  | PA CD status Multifonds DB Column is PA_CDSTATUS. |
| 123 | `COUPON.TRANSACTION.MAXIMUM.RECOVERABLE.RATE` | `FsGaCouponTransaction_MaximumRecoverableRate` | TField |  | Maximum Recoverable rate Multifonds DB Column is KRRECTAX. |
| 124 | `COUPON.TRANSACTION.CREATE.COPY.FLAG` | `FsGaCouponTransaction_CreateCopyFlag` | TField |  | Create copy flag Multifonds DB Column is FLG_CREATE_COPY. |
| 125 | `COUPON.TRANSACTION.HOLDING.PERIOD.TAX` | `FsGaCouponTransaction_HoldingPeriodTax` | TField |  | Holding Period Tax Multifonds DB Column is HOLD_TAX. |
| 126 | `COUPON.TRANSACTION.FEES.HOLD` | `FsGaCouponTransaction_FeesHold` | TField |  | Fees hold Multifonds DB Column is CFRAIS_HOLD. |
| 127 | `COUPON.TRANSACTION.OPERATION.CODE.HOLD` | `FsGaCouponTransaction_OperationCodeHold` | TField |  | Operation code hold Multifonds DB Column is COPER_HOLD. |
| 128 | `COUPON.TRANSACTION.MNT.TAX.1` | `FsGaCouponTransaction_MntTax1` | TField |  | Mnt Tax 1 Multifonds DB Column is MNTHOLD_TAX. |
| 129 | `COUPON.TRANSACTION.MNT.HOLD.TAX.PTF` | `FsGaCouponTransaction_MntHoldTaxPtf` | TField |  | MNT hold Tax ptf Multifonds DB Column is MNTHOLD_TAX_PTF. |
| 130 | `COUPON.TRANSACTION.TR.ACCOUNT.NUMBER` | `FsGaCouponTransaction_TrAccountNumber` | TField |  | TR account number Multifonds DB Column is NRUBR_TR. |
| 131 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX.IN.FUND.CCY` | `FsGaCouponTransaction_UnrecoverableTaxInFundCcy` | TField |  | Unrecoverable Tax In Fund Ccy Multifonds DB Column is MNTUNRECTAX_PTF. |
| 132 | `COUPON.TRANSACTION.UNRECOVERABL.TAX.2.IN.FUND.CCY` | `FsGaCouponTransaction_UnrecoverablTax2InFundCcy` | TField |  | Unrecoverabl Tax 2 In Fund Ccy Multifonds DB Column is MNTUNRECTAX_2_PTF. |
| 133 | `COUPON.TRANSACTION.RECOVERABLE.TAX.IN.FUND.CCY` | `FsGaCouponTransaction_RecoverableTaxInFundCcy` | TField |  | Recoverable Tax In Fund Ccy Multifonds DB Column is MNTRECTAX_PTF. |
| 134 | `COUPON.TRANSACTION.RECOVERABLE.TAX.2.IN.FUND.CCY` | `FsGaCouponTransaction_RecoverableTax2InFundCcy` | TField |  | Recoverable Tax 2 In Fund Ccy Multifonds DB Column is MNTRECTAX_2_PTF. |
| 135 | `COUPON.TRANSACTION.GLOBAL.AMOUNT.IN.FUND.CCY` | `FsGaCouponTransaction_GlobalAmountInFundCcy` | TField |  | Global Amount in Fund Ccy Multifonds DB Column is MNTGLOBAL_PTF. |
| 136 | `COUPON.TRANSACTION.MNT.GLOBAL.PIK.PTF` | `FsGaCouponTransaction_MntGlobalPikPtf` | TField |  | MNT global PIK PTF Multifonds DB Column is MNTGLOBAL_PIK_PTF. |
| 137 | `COUPON.TRANSACTION.MNT.NET.2` | `FsGaCouponTransaction_MntNet2` | TField |  | Mnt net 2 Multifonds DB Column is MNT_NET_2. |
| 138 | `COUPON.TRANSACTION.MNT.NET.2.PTF` | `FsGaCouponTransaction_MntNet2Ptf` | TField |  | Mnt net 2 PTF Multifonds DB Column is MNT_NET_2_PTF. |
| 139 | `COUPON.TRANSACTION.SEC.SETTL.FX.VCI` | `FsGaCouponTransaction_SecSettlFxVci` | TField |  | Sec Settl FX VCI Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 140 | `COUPON.TRANSACTION.SEC.FX.VCI.FUND.ID` | `FsGaCouponTransaction_SecFxVciFund` | TField |  | Sec FX VCI fund Multifonds DB Column is SEC_PTF_FX_VCI. |
| 141 | `COUPON.TRANSACTION.FUND.FX.VCI.SETTLE` | `FsGaCouponTransaction_FundFxVciSettle` | TField |  | Fund FX VCI settle Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 142 | `COUPON.TRANSACTION.TAX.ON.FRANKED.DIVIDEND` | `FsGaCouponTransaction_TaxOnFrankedDividend` | TField |  | Tax on Franked Dividend Multifonds DB Column is PFRANKTAX. |
| 143 | `COUPON.TRANSACTION.FRANKING.CREDITS` | `FsGaCouponTransaction_FrankingCredits` | TField |  | Franking Credits Multifonds DB Column is MNTFRANKTAX. |
| 144 | `COUPON.TRANSACTION.CONDUIT.FORIEN.INCOME.RATE` | `FsGaCouponTransaction_ConduitForienIncomeRate` | TField |  | Conduit Forien Income Rate Multifonds DB Column is CFI_RATE. |
| 145 | `COUPON.TRANSACTION.CONDUIT.FORIEN.INCOME.AMOUNT` | `FsGaCouponTransaction_ConduitForienIncomeAmount` | TField |  | Conduit Forien Income Amount Multifonds DB Column is MNT_CFI. |
| 146 | `COUPON.TRANSACTION.FRANKING.DIVIDENT.PER.SHARE` | `FsGaCouponTransaction_FrankingDividentPerShare` | TField |  | Franking Divident Per Share Multifonds DB Column is PFRANK_INC. |
| 147 | `COUPON.TRANSACTION.TAX.BASIS` | `FsGaCouponTransaction_TaxBasis` | TField |  | Tax Basis Multifonds DB Column is TAX_BASIS. |
| 148 | `COUPON.TRANSACTION.SECURITY.TYPE` | `FsGaCouponTransaction_SecurityType` | TField |  | Security Type Multifonds DB Column is CGTI. |
| 149 | `COUPON.TRANSACTION.FRANKING.CREDITS.IN.FUND.CCY` | `FsGaCouponTransaction_FrankingCreditsInFundCcy` | TField |  | Franking Credits in Fund Ccy Multifonds DB Column is MNTFRANKTAX_PTF. |
| 150 | `COUPON.TRANSACTION.GROSS.AMOUNT.IN.FUND.CCY` | `FsGaCouponTransaction_GrossAmountInFundCcy` | TField |  | Gross Amount in Fund Ccy Multifonds DB Column is MNTGROSS_PTF. |
| 151 | `COUPON.TRANSACTION.GLOBAL.AMOUNT.SPREAD` | `FsGaCouponTransaction_GlobalAmountSpread` | TField |  | Global amount spread Multifonds DB Column is MNTGLOBAL_SPRD. |
| 152 | `COUPON.TRANSACTION.COM.CORR.SPREAD.AMOUNT` | `FsGaCouponTransaction_ComCorrSpreadAmount` | TField |  | Com Corr spread amount Multifonds DB Column is MNTCOMCORR_SPRD. |
| 153 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX.SPREAD.AMNT` | `FsGaCouponTransaction_UnrecoverableTaxSpreadAmnt` | TField |  | Unrecoverable tax spread amnt Multifonds DB Column is MNTUNRECTAX_SPRD. |
| 154 | `COUPON.TRANSACTION.UNRECOVERABLE.TAX2.SPREAD.AMNT` | `FsGaCouponTransaction_UnrecoverableTax2SpreadAmnt` | TField |  | Unrecoverable tax2 spread amnt Multifonds DB Column is MNTUNRECTAX_2_SPRD. |
| 155 | `COUPON.TRANSACTION.SECLEN.TAX.SPREAD.AMOUNT` | `FsGaCouponTransaction_SeclenTaxSpreadAmount` | TField |  | Seclen tax spread amount Multifonds DB Column is MNTSECLENTAX_SPRD. |
| 156 | `COUPON.TRANSACTION.RECOVERABLE.TAX.SPREAD.AMOUNT` | `FsGaCouponTransaction_RecoverableTaxSpreadAmount` | TField |  | Recoverable tax spread amount Multifonds DB Column is MNTRECTAX_SPRD. |
| 157 | `COUPON.TRANSACTION.RECOVERABLE.TAX2.SPREAD.AMOUNT` | `FsGaCouponTransaction_RecoverableTax2SpreadAmount` | TField |  | Recoverable tax2 spread amount Multifonds DB Column is MNTRECTAX_2_SPRD. |
| 158 | `COUPON.TRANSACTION.HOLDING.TAX.SPREAD.AMOUNT` | `FsGaCouponTransaction_HoldingTaxSpreadAmount` | TField |  | Holding tax spread amount Multifonds DB Column is MNTHOLD_TAX_SPRD. |
| 159 | `COUPON.TRANSACTION.TAX1.SPREAD.AMOUNT` | `FsGaCouponTransaction_Tax1SpreadAmount` | TField |  | Tax1 spread amount Multifonds DB Column is MNT_TAX_1_SPRD. |
| 160 | `COUPON.TRANSACTION.TAX2.SPREAD.AMOUNT` | `FsGaCouponTransaction_Tax2SpreadAmount` | TField |  | Tax2 spread amount Multifonds DB Column is MNT_TAX_2_SPRD. |
| 161 | `COUPON.TRANSACTION.FEES1.SPREAD.AMOUNT` | `FsGaCouponTransaction_Fees1SpreadAmount` | TField |  | Fees1 spread amount Multifonds DB Column is MNTFRAIS1_SPRD. |
| 162 | `COUPON.TRANSACTION.FEES2.SPREAD.AMOUNT` | `FsGaCouponTransaction_Fees2SpreadAmount` | TField |  | Fees2 spread amount Multifonds DB Column is MNTFRAIS2_SPRD. |
| 163 | `COUPON.TRANSACTION.NET.SPREAD.AMOUNT` | `FsGaCouponTransaction_NetSpreadAmount` | TField |  | Net spread amount Multifonds DB Column is MNTNET_SPRD. |
| 164 | `COUPON.TRANSACTION.SPREAD.RATE` | `FsGaCouponTransaction_SpreadRate` | TField |  | Spread rate Multifonds DB Column is SPREAD_RATE. |
| 165 | `COUPON.TRANSACTION.REINVESTMENT.DATE` | `FsGaCouponTransaction_ReinvestmentDate` | TField |  | Reinvestment Date Multifonds DB Column is DREINV. |
| 166 | `COUPON.TRANSACTION.REINVESTMENT.TRANSACTION.PRICE` | `FsGaCouponTransaction_ReinvestmentPrice` | TField |  | Reinvestment Price Multifonds DB Column is COURS_REINV. |
| 167 | `COUPON.TRANSACTION.TOFA.TYPE` | `FsGaCouponTransaction_TofaType` | TField |  | Tofa type Multifonds DB Column is TOFA_TYPE. |
| 168 | `COUPON.TRANSACTION.FUND.CFI.AMOUNT` | `FsGaCouponTransaction_FundCfiAmount` | TField |  | Fund CFI amount Multifonds DB Column is MNT_CFI_PTF. |
| 169 | `COUPON.TRANSACTION.THE.FATCA.RATE.PRECENTAGE` | `FsGaCouponTransaction_TheFatcaRatePrecentage` | TField |  | The Fatca rate precentage Multifonds DB Column is PFATCA_TAX1. |
| 170 | `COUPON.TRANSACTION.PAYABLE.FATCA.AMOUNT` | `FsGaCouponTransaction_PayableFatcaAmount` | TField |  | Payable fatca amount Multifonds DB Column is MNT_FATCA1. |
| 171 | `COUPON.TRANSACTION.PAYABLE.FATCA.AMOUNT.FUND.CCY` | `FsGaCouponTransaction_PayableFatcaAmountFundCcy` | TField |  | Payable fatca amount fund CCY Multifonds DB Column is MNTFATCATAX1_PTF. |
| 172 | `COUPON.TRANSACTION.PAYABLE.FATCA.AMOUNT.SPREAD` | `FsGaCouponTransaction_PayableFatcaAmountSpread` | TField |  | Payable fatca amount spread Multifonds DB Column is MNTFATCATAX1_SPRD. |
| 173 | `COUPON.TRANSACTION.FATCA.RECOVRABLE.RATE.PERCNTGE` | `FsGaCouponTransaction_FatcaRecovrableRatePercntge` | TField |  | Fatca recovrable rate percntge Multifonds DB Column is PFATCA_TAX2. |
| 174 | `COUPON.TRANSACTION.RECOVERABLE.FATCA.AMNT.SPREAD` | `FsGaCouponTransaction_RecoverableFatcaAmntSpread` | TField |  | Recoverable fatca amnt spread Multifonds DB Column is MNTFATCATAX2_SPRD. |
| 175 | `COUPON.TRANSACTION.FATCA.TAX1.FLAG` | `FsGaCouponTransaction_FatcaTax1Flag` | TField |  | Fatca Tax1 flag Multifonds DB Column is FLG_FATCATAX1. |
| 176 | `COUPON.TRANSACTION.FATCA.TAX2.FLAG` | `FsGaCouponTransaction_FatcaTax2Flag` | TField |  | Fatca Tax2 flag Multifonds DB Column is FLG_FATCATAX2. |
| 177 | `COUPON.TRANSACTION.TAX.INC` | `FsGaCouponTransaction_TaxInc` | TField |  | Tax Inc Multifonds DB Column is TAX_INC. |
| 178 | `COUPON.TRANSACTION.NON.ACCRUAL.STATUS` | `FsGaCouponTransaction_NonAccrualStatus` | TField |  | Non Accrual Status Multifonds DB Column is FLG_NON_ACC_STATUS. |
| 179 | `COUPON.TRANSACTION.AMOUNT.RECEIVED.IN.DEAL.CCY` | `FsGaCouponTransaction_AmountReceivedInDealCcy` | TField |  | Amount received in deal Ccy Multifonds DB Column is AMOUNT_RECEIVED. |
| 180 | `COUPON.TRANSACTION.AMOUNT.RECEIVED.IN.FUND.CCY` | `FsGaCouponTransaction_AmountReceivedInFundCcy` | TField |  | Amount received in fund Ccy Multifonds DB Column is AMOUNT_RECEIVED_PTF. |
| 181 | `COUPON.TRANSACTION.NET.AMOUNT.IN.NATIVE.CCY` | `FsGaCouponTransaction_NetAmountInNativeCcy` | TField |  | Net Amount in native Ccy Multifonds DB Column is MNTNET_FCY. |
| 182 | `COUPON.TRANSACTION.EXCHANGE.RATE.IN.NATIVE.CCY` | `FsGaCouponTransaction_ExchangeRateInNativeCcy` | TField |  | Exchange rate in native Ccy Multifonds DB Column is TCHG_FCY. |
| 183 | `COUPON.TRANSACTION.45.DAY.FLAG` | `FsGaCouponTransaction_45DayFlag` |  |  |  |
| 184 | `COUPON.TRANSACTION.TRANSACTION.ID` | `FsGaCouponTransaction_TransactionId` | TField |  | Transaction Id Multifonds DB Column is TRANSACTION_ID. |
| 185 | `COUPON.TRANSACTION.TRADE.ID` | `FsGaCouponTransaction_TradeId` | TField |  | Trade ID Multifonds DB Column is TRADEID. |
| 186 | `COUPON.TRANSACTION.KNOWLEDGE.DATE` | `FsGaCouponTransaction_KnowledgeDate` | TField |  | Knowledge date Multifonds DB Column is KNOWLEDGEDATE. |
| 187 | `COUPON.TRANSACTION.LOT.ID` | `FsGaCouponTransaction_LotId` | TField |  | Lot ID Multifonds DB Column is LOTID. |
| 188 | `COUPON.TRANSACTION.INCOME.LAG.PRC.FLAG` | `FsGaCouponTransaction_IncomeLagPrcFlag` | TField |  | Income LAG PRC flag Multifonds DB Column is FLG_INC_LAG_PRC. |
| 189 | `COUPON.TRANSACTION.TAXABLE.FACTOR` | `FsGaCouponTransaction_TaxableFactor` | TField |  | Taxable factor Multifonds DB Column is FACTOR_TAX. |
| 190 | `COUPON.TRANSACTION.TAX.FREE.FACTOR` | `FsGaCouponTransaction_TaxFreeFactor` | TField |  | Tax free factor Multifonds DB Column is FACTOR_TAX_FREE. |
| 191 | `COUPON.TRANSACTION.TAXABLE.AMOUNT` | `FsGaCouponTransaction_TaxableAmount` | TField |  | Taxable amount Multifonds DB Column is MNT_TAX_CMV. |
| 192 | `COUPON.TRANSACTION.TAXFREE.AMOUNT` | `FsGaCouponTransaction_TaxfreeAmount` | TField |  |  |
| 193 | `COUPON.TRANSACTION.AGS.QUANTITY` | `FsGaCouponTransaction_AgsQuantity` | TField |  | AGS Quantity Multifonds DB Column is AGS_QUANTITE. |
| 194 | `COUPON.TRANSACTION.NON.AGS.QUANTITY` | `FsGaCouponTransaction_NonAgsQuantity` | TField |  | Non AGS Quantity Multifonds DB Column is NON_AGS_QUANTITE. |
| 195 | `COUPON.TRANSACTION.CA.TYPE` | `FsGaCouponTransaction_CaType` | TField |  | CA Type Multifonds DB Column is CA_TYPE. |
| 196 | `COUPON.TRANSACTION.COUNTRY.CODE.COUNTRY` | `FsGaCouponTransaction_CountryCodeCountry` | TField |  | Country code COUNTRY Multifonds DB Column is CPAYSVAL. |
| 197 | `COUPON.TRANSACTION.RECORD.STATUS` | `FsGaCouponTransaction_RecordStatus` | String |  |  |
| 198 | `COUPON.TRANSACTION.CURR.NO` | `FsGaCouponTransaction_CurrNo` | String |  |  |
| 199 | `COUPON.TRANSACTION.INPUTTER` | `FsGaCouponTransaction_Inputter` |  |  |  |
| 200 | `COUPON.TRANSACTION.DATE.TIME` | `FsGaCouponTransaction_DateTime` |  |  |  |
| 201 | `COUPON.TRANSACTION.AUTHORISER` | `FsGaCouponTransaction_Authoriser` | String |  |  |
| 202 | `COUPON.TRANSACTION.CO.CODE` | `FsGaCouponTransaction_CoCode` | String |  |  |
| 203 | `COUPON.TRANSACTION.DEPT.CODE` | `FsGaCouponTransaction_DeptCode` | String |  |  |
| 204 | `COUPON.TRANSACTION.AUDITOR.CODE` | `FsGaCouponTransaction_AuditorCode` | String |  |  |
| 205 | `COUPON.TRANSACTION.AUDIT.DATE.TIME` | `FsGaCouponTransaction_AuditDateTime` | String |  |  |
