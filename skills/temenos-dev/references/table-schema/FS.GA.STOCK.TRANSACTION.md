# FS.GA.STOCK.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.STOCK.TRANSACTION` in `FS_StockTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STOCK.TRANSACTION.PARENT.REF.ID` | `FsGaStockTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STOCK.TRANSACTION.ORA.ROWID` | `FsGaStockTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STOCK.TRANSACTION.CUSTODIAN` | `FsGaStockTransaction_Custodian` | TField |  | Custodian where the units of the transaction would be lodged Multifonds DB Column is NDEPOSI. |
| 4 | `FS.GA.STOCK.TRANSACTION.INTERNAL.SECURITY.ID` | `FsGaStockTransaction_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.STOCK.TRANSACTION.FUND.ID` | `FsGaStockTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.STOCK.TRANSACTION.MANAGER.CODE` | `FsGaStockTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 7 | `FS.GA.STOCK.TRANSACTION.CORRESPONDENT.SUB.ACCOUNT.NO` | `FsGaStockTransaction_CorrespondentSubAccountNo` | TField |  | Cash Correspondent Sub Account No Multifonds DB Column is NSUFFCORR. |
| 8 | `FS.GA.STOCK.TRANSACTION.CORRESPONDENT` | `FsGaStockTransaction_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 9 | `FS.GA.STOCK.TRANSACTION.COUNTERPARTY` | `FsGaStockTransaction_Counterparty` | TField |  | Counterparty of the transaction Multifonds DB Column is NCORRESP_EXEC. |
| 10 | `FS.GA.STOCK.TRANSACTION.CORRESPONDENT.ACCOUNT.NO` | `FsGaStockTransaction_CorrespondentAccountNo` | TField |  | Cash Correspondent Account No Multifonds DB Column is NRUBRCORR. |
| 11 | `FS.GA.STOCK.TRANSACTION.CORRESPONDENT.ADJ.NUMBER` | `FsGaStockTransaction_CorrespondentAdjNumber` | TField |  | Correspondent adj number Multifonds DB Column is NCORRESP_ADJ. |
| 12 | `FS.GA.STOCK.TRANSACTION.COUNTERPARTY.CORRESPONDENT` | `FsGaStockTransaction_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 13 | `FS.GA.STOCK.TRANSACTION.PRICE.TYPE.INDICATOR` | `FsGaStockTransaction_PriceTypeIndicator` | TField |  | Deal level flag to indicate if the price of the bond tyransacted is clean or dirty. Multifonds DB Column is TYP_PRICE_INDICATOR. |
| 14 | `FS.GA.STOCK.TRANSACTION.INTEREST.RATE.TYPE` | `FsGaStockTransaction_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 15 | `FS.GA.STOCK.TRANSACTION.ACCRUED.INTEREST.INCLUSION` | `FsGaStockTransaction_AccruedInterestInclusion` | TField |  | Flag to denote if accrued interest on a lent/borrowed security needs to be included in engagement amount Multifonds DB Column is FLG_ACC_INT. |
| 16 | `FS.GA.STOCK.TRANSACTION.FUND.STRATEGY` | `FsGaStockTransaction_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 17 | `FS.GA.STOCK.TRANSACTION.QUOTATION.PLACE` | `FsGaStockTransaction_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 18 | `FS.GA.STOCK.TRANSACTION.DEAL.CURRENCY` | `FsGaStockTransaction_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 19 | `FS.GA.STOCK.TRANSACTION.FUND.LINK.ID` | `FsGaStockTransaction_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 20 | `FS.GA.STOCK.TRANSACTION.IFRS.TAG` | `FsGaStockTransaction_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 21 | `FS.GA.STOCK.TRANSACTION.OPERATION.CODE` | `FsGaStockTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 22 | `FS.GA.STOCK.TRANSACTION.CONFIRMED` | `FsGaStockTransaction_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 23 | `FS.GA.STOCK.TRANSACTION.INTERPORT.TRADES` | `FsGaStockTransaction_InterportTrades` | TField |  | Interport trades Multifonds DB Column is FLG_INTERPORT_TRADES. |
| 24 | `FS.GA.STOCK.TRANSACTION.COEFFICIENT.CORPORATE.ACTION` | `FsGaStockTransaction_CoefficientCorporateAction` | TField |  | Enter a CA coefficient which is taken into account to calc the dividend, coupon, split, reverse split, spin off, exchange of security into one new security ID or several security ID on the sec lent. Multifonds DB Column is COEF_CORP. |
| 25 | `FS.GA.STOCK.TRANSACTION.TO.BE.ANNOUNCED.SECURITY` | `FsGaStockTransaction_ToBeAnnouncedSecurity` | TField |  | The transaction will not be settled unless the TBA flag is unchecked. Therefore, If the actual security information is not received enable the flag so that the transaction will remain unsettled. Multifonds DB Column is FLG_TBA. |
| 26 | `FS.GA.STOCK.TRANSACTION.SERVICE.CODE` | `FsGaStockTransaction_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 27 | `FS.GA.STOCK.TRANSACTION.UNIQUE.LOT.ID.GROUP` | `FsGaStockTransaction_UniqueLotIdGroup` | TField |  | This is a 3 digit alpha numeric value which will be predefined in the messages UNQ_LOT. User will not be able to change the group once the fund has any lot generating transaction in it. Multifonds DB Column is UNQ_LOT_GRP. |
| 28 | `FS.GA.STOCK.TRANSACTION.NON.RESIDENT.TAXABLE.AMOUNT` | `FsGaStockTransaction_NonResidentTaxableAmount` | TField |  | Non Resident Taxable book cost, This is related to Korean Fund of Funds where three different NAV prices (Normal NAV, Taxable NAV, Non resident Taxable NAV) to be maintained. Multifonds DB Column is MNT_NRTX. |
| 29 | `FS.GA.STOCK.TRANSACTION.TAXABLE.AMOUNT` | `FsGaStockTransaction_TaxableAmount` | TField |  | Taxable book cost, This is related to Korean Fund of Funds where three different NAV prices (Normal NAV, Taxable NAV, Non resident Taxable NAV) to be maintained. Multifonds DB Column is MNT_TX. |
| 30 | `FS.GA.STOCK.TRANSACTION.ADJUSTED.ENGAGEMENT` | `FsGaStockTransaction_AdjustedEngagement` | TField |  | The &quot;TBA&quot; flag must be checked, whether the transaction is manually accounted in Multifonds or interfaced, to indicate that it is a TBA trade Multifonds DB Column is ADJ_ENG. |
| 31 | `FS.GA.STOCK.TRANSACTION.45.DAY.INCLUSION` | `FsGaStockTransaction_45DayInclusion` |  |  |  |
| 32 | `FS.GA.STOCK.TRANSACTION.MATURITY.CODE` | `FsGaStockTransaction_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 33 | `FS.GA.STOCK.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaStockTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 34 | `FS.GA.STOCK.TRANSACTION.LENDING.ALLOCATION` | `FsGaStockTransaction_LendingAllocation` | TField |  | Flag to denote of a security lending booked in pool needs to be allocated to all sub funds or only impact a single sub fund Multifonds DB Column is FLG_TPARTS_APS. |
| 35 | `FS.GA.STOCK.TRANSACTION.CALCULATION.PAYMENT.DATE` | `FsGaStockTransaction_CalculationPaymentDate` | TField |  | Logic to decide if payment date falls on a non working day should it process paymet on same date or prior/next working day. Multifonds DB Column is CTR_DATE. |
| 36 | `FS.GA.STOCK.TRANSACTION.PAYMENT.DATE.CALCULATION` | `FsGaStockTransaction_PaymentDateCalculation` | TField |  | Logic to decide if payment date falls on a non working day should it process paymet on same date or prior/next working day. Multifonds DB Column is CALC_PMNT_DATE. |
| 37 | `FS.GA.STOCK.TRANSACTION.PRICING.FACTOR.CODE` | `FsGaStockTransaction_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 38 | `FS.GA.STOCK.TRANSACTION.RESTRICTED.SECURITY` | `FsGaStockTransaction_RestrictedSecurity` | TField |  | Transaction on a security which is privately placed and therefore restricted from trading within the lock up period. Multifonds DB Column is RESTRICTED_NOVAL. |
| 39 | `FS.GA.STOCK.TRANSACTION.EXCLUDE.DIVIDEND` | `FsGaStockTransaction_ExcludeDividend` | TField |  | Flag to denote if the transaction is ex dividend even if the trade date is less than entitlement date of dividend Multifonds DB Column is FLG_XCLUDE_COUP_DIV. |
| 40 | `FS.GA.STOCK.TRANSACTION.COEFFICIENT.GUARANTEE` | `FsGaStockTransaction_CoefficientGuarantee` | TField |  | Guarantee coefficient applicable on a security lending/borrowing transction to impact the engagement amount Multifonds DB Column is COEF_GAR. |
| 41 | `FS.GA.STOCK.TRANSACTION.CAPSTOCK.PRICE.DATE` | `FsGaStockTransaction_CapstockPriceDate` | TField |  | This is the price date as of which the subscription/redemption price needs to be applied for the capstock. Multifonds DB Column is PRICE_DATE. |
| 42 | `FS.GA.STOCK.TRANSACTION.INCOME.TYPE` | `FsGaStockTransaction_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 43 | `FS.GA.STOCK.TRANSACTION.MULTILAYER.POOLING.DRILL` | `FsGaStockTransaction_MultilayerPoolingDrill` | TField |  | The flag to denote if an increase/decrease on pool units need to be impact other funds or only stanalone. Multifonds DB Column is FLG_AUTOUP_STANDALONE. |
| 44 | `FS.GA.STOCK.TRANSACTION.TRADING.YIELD` | `FsGaStockTransaction_TradingYield` | TField |  | Usually the trading yield for yield based bonds.Also the YTM calculated for bonds as per effective yield Multifonds DB Column is RENDEMENT. |
| 45 | `FS.GA.STOCK.TRANSACTION.PROVISION.ACCRUAL` | `FsGaStockTransaction_ProvisionAccrual` | TField |  | Flag to determine if the provision on a security lending transaction should be accrued in the NAV Multifonds DB Column is FLG_LEN. |
| 46 | `FS.GA.STOCK.TRANSACTION.SEC.TRANSACTION.TAX.INDICATOR` | `FsGaStockTransaction_SecTransactionTaxIndicator` | TField |  | Indicator whether a transaction has been subject to security transaction tax for CGT computation. Multifonds DB Column is CGT_IND_STT_FLG. |
| 47 | `FS.GA.STOCK.TRANSACTION.DAYS.OF.ACCRUED.INTEREST` | `FsGaStockTransaction_DaysOfAccruedInterest` | TField |  | Number of days of purchase/sale interest in a transaction done on an interest bearing instrument Multifonds DB Column is NBJOURS. |
| 48 | `FS.GA.STOCK.TRANSACTION.TIS.AVAILABILITY` | `FsGaStockTransaction_TisAvailability` | TField |  | used to control that all positions that have these values set, require the injection of the TIS Multifonds DB Column is TIS_AVAIL. |
| 49 | `FS.GA.STOCK.TRANSACTION.COMMISSION.BASE` | `FsGaStockTransaction_CommissionBase` | TField |  | Flag to determine if the commission should be based on the historic cost or the market value Multifonds DB Column is FLG_MKT_VAL. |
| 50 | `FS.GA.STOCK.TRANSACTION.LOAN.UNDERLYING.IDENTIFIER` | `FsGaStockTransaction_LoanUnderlyingIdentifier` | TField |  | Underlying flag to denote that lending is done for a pool of securities on a single contract Multifonds DB Column is FLG_UNDERLYER. |
| 51 | `FS.GA.STOCK.TRANSACTION.COLLATERAL.REUSE` | `FsGaStockTransaction_CollateralReuse` | TField |  | Flag to denote if the transaction is made out of a collateral position which was received Multifonds DB Column is FLG_COLL_REUSE. |
| 52 | `FS.GA.STOCK.TRANSACTION.FIXED.COMMISSION.RATE` | `FsGaStockTransaction_FixedCommissionRate` | TField |  | Fixed commission rate applied on a lending/borrowing contract for commission accrual Multifonds DB Column is COM_LEN_NEW. |
| 53 | `FS.GA.STOCK.TRANSACTION.COMMISSION.START.DATE` | `FsGaStockTransaction_CommissionStartDate` | TField |  | Lending/ borrowing commission accrual start date if different from settlement date Multifonds DB Column is DVALEUR_COM. |
| 54 | `FS.GA.STOCK.TRANSACTION.MANUAL.SETTLEMENT` | `FsGaStockTransaction_ManualSettlement` | TField |  | Flag at deal level to override the contractual settlement specific to the deal. Multifonds DB Column is CSETTLE_MANU. |
| 55 | `FS.GA.STOCK.TRANSACTION.CUMULATIVE.COMMISSION` | `FsGaStockTransaction_CumulativeCommission` | TField |  | Flag to determine if the commission should be computed on a cumulative basis . Multifonds DB Column is FLG_CUMULATIVE_MAT. |
| 56 | `FS.GA.STOCK.TRANSACTION.INTEREST.RATE` | `FsGaStockTransaction_InterestRate` | TField |  | Interest rate applicable on the interest bearing instrument in the transaction Multifonds DB Column is TXINT. |
| 57 | `FS.GA.STOCK.TRANSACTION.DELAY.DAYS` | `FsGaStockTransaction_DelayDays` | TField |  | Delay days to be applied on coupon/ paydown transactions to trigger payment Multifonds DB Column is DELAY_DAYS. |
| 58 | `FS.GA.STOCK.TRANSACTION.TRANSACTION.NUMBER` | `FsGaStockTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 59 | `FS.GA.STOCK.TRANSACTION.IG.PER.UNIT` | `FsGaStockTransaction_IgPerUnit` | TField |  | Target fund income per unit attributed to income generate from real estate Multifonds DB Column is IG_PART. |
| 60 | `FS.GA.STOCK.TRANSACTION.CAPITALIZATION.FREQUENCY` | `FsGaStockTransaction_CapitalizationFrequency` | TField |  | Frequency of capitalisation for lending/borrowing commission calculation Multifonds DB Column is CFREQCOM. |
| 61 | `FS.GA.STOCK.TRANSACTION.RATE.OF.INTEREST` | `FsGaStockTransaction_RateOfInterest` | TField |  | This flag allows user to define the ROI for Security Lending / Borrowing Multifonds DB Column is FIXED_RATE. |
| 62 | `FS.GA.STOCK.TRANSACTION.CAPITALIZATION` | `FsGaStockTransaction_Capitalization` | TField |  | Capitalisation method for sec lending /borrowing commission calculation Multifonds DB Column is CAPITALISATION. |
| 63 | `FS.GA.STOCK.TRANSACTION.BLOCKING.SECURITY.LENT` | `FsGaStockTransaction_BlockingSecurityLent` | TField |  | Flag to automatically block the security lent position in the portfolio Multifonds DB Column is FLG_BLK_SEC. |
| 64 | `FS.GA.STOCK.TRANSACTION.RATE.TYPE.CODE` | `FsGaStockTransaction_RateTypeCode` | TField |  | Select the appropriate code to be used in the French annual reporting. Multifonds DB Column is TYP_RISK. |
| 65 | `FS.GA.STOCK.TRANSACTION.SPREAD.PERCENT` | `FsGaStockTransaction_SpreadPercent` | TField |  | Spread rate to be applied on commission rate for commission calculation Multifonds DB Column is PCT_SPREAD. |
| 66 | `FS.GA.STOCK.TRANSACTION.CURRENCY.CODE.FOR.COMMISSION` | `FsGaStockTransaction_CurrencyCodeForCommission` | TField |  | Currency code for commission for Pool increase or decrease transaction Multifonds DB Column is CMON_TR_FEES. |
| 67 | `FS.GA.STOCK.TRANSACTION.PRICE.INDICATOR` | `FsGaStockTransaction_PriceIndicator` | TField |  | Price indicator to denote if the price of the bond is dirty or clean Multifonds DB Column is TYP_INT_COURS. |
| 68 | `FS.GA.STOCK.TRANSACTION.MANUAL.LOT.SELECTION` | `FsGaStockTransaction_ManualLotSelection` | TField |  | Flag to denote that the lots relieved have been manually selected Multifonds DB Column is FLG_MANUAL_LOT. |
| 69 | `FS.GA.STOCK.TRANSACTION.FOR.COMMISSION` | `FsGaStockTransaction_ForCommission` | TField |  | To Include Commission in Pool increase or decrease transaction Multifonds DB Column is FLG_COM_POOL. |
| 70 | `FS.GA.STOCK.TRANSACTION.ENTRY.NUMBER.REPAYMENT` | `FsGaStockTransaction_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 71 | `FS.GA.STOCK.TRANSACTION.GRAND.FATHER.OR.TIS.REPORTING` | `FsGaStockTransaction_GrandFatherOrTisReporting` | TField |  | Grand Father or Non Grand Father i.e TIS Reporting applicable Multifonds DB Column is GDF_TISR. |
| 72 | `FS.GA.STOCK.TRANSACTION.LOT.NUMBER` | `FsGaStockTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 73 | `FS.GA.STOCK.TRANSACTION.NON.ACCRUAL.STATUS` | `FsGaStockTransaction_NonAccrualStatus` | TField |  | Flag to denote whether the security is in a defaulted status Multifonds DB Column is FLG_NON_ACC_STATUS. |
| 74 | `FS.GA.STOCK.TRANSACTION.COMMISSION.FEE.AMOUNT` | `FsGaStockTransaction_CommissionFeeAmount` | TField |  | Commision amount for Pool increase or decrease transaction Multifonds DB Column is MNT_TR_FEES. |
| 75 | `FS.GA.STOCK.TRANSACTION.AKTIENGEWINN.PER.UNIT` | `FsGaStockTransaction_AktiengewinnPerUnit` | TField |  | Increase in value of units attributable to gain on shares. Multifonds DB Column is ACTIENGEWINN_PART. |
| 76 | `FS.GA.STOCK.TRANSACTION.EXCH.RATE.SETTLEMENT.TO.DEAL` | `FsGaStockTransaction_ExchRateSettlementToDeal` | TField |  | The exchange rate between the settlement and deal currency Multifonds DB Column is TCHG_PTF. |
| 77 | `FS.GA.STOCK.TRANSACTION.TRANSACTION.PRICE` | `FsGaStockTransaction_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 78 | `FS.GA.STOCK.TRANSACTION.INTERIM.PROFIT` | `FsGaStockTransaction_InterimProfit` | TField |  | Interim profit amount while transacting on a target fund. Multifonds DB Column is ZWIST. |
| 79 | `FS.GA.STOCK.TRANSACTION.POOL.FUND.PRICE` | `FsGaStockTransaction_PoolFundPrice` | TField |  | Pool fund Price for Pool increase or decrease transaction Multifonds DB Column is TCOURS_POOL. |
| 80 | `FS.GA.STOCK.TRANSACTION.ACCRUED.INTEREST.AMOUNT` | `FsGaStockTransaction_AccruedInterestAmount` | TField |  | Purchase/sale interest on a interest bearing instrument Multifonds DB Column is MINT_OPER. |
| 81 | `FS.GA.STOCK.TRANSACTION.COMMISSION.USANCE.CODE` | `FsGaStockTransaction_CommissionUsanceCode` | TField |  | Usance code for security lending commission calculation Multifonds DB Column is CUSA_LEN. |
| 82 | `FS.GA.STOCK.TRANSACTION.LENDING.AMOUNT` | `FsGaStockTransaction_LendingAmount` | TField |  | Lending commission amount on a security lending deal. Multifonds DB Column is MNT_LEN. |
| 83 | `FS.GA.STOCK.TRANSACTION.LENDING.COMMISSION.AMOUNT` | `FsGaStockTransaction_LendingCommissionAmount` | TField |  | Provision commission amount on a lending transaction Multifonds DB Column is MNT_COMM_LEN. |
| 84 | `FS.GA.STOCK.TRANSACTION.FACE.VALUE.AMOUNT` | `FsGaStockTransaction_FaceValueAmount` | TField |  | The Face value amount for Mortgage backed securities Multifonds DB Column is MONTANT_FACIAL. |
| 85 | `FS.GA.STOCK.TRANSACTION.TRANSACTION.FEES.AMOUNT` | `FsGaStockTransaction_TransactionFeesAmount` | TField |  | This field denotes the fee amount of the transaction Multifonds DB Column is MFRAIS_OPER. |
| 86 | `FS.GA.STOCK.TRANSACTION.DISCOUNT.AMOUNT` | `FsGaStockTransaction_DiscountAmount` | TField |  | This is the discount amount offered to a unit holder Multifonds DB Column is MNT_DISCOUNT. |
| 87 | `FS.GA.STOCK.TRANSACTION.PERFORMANCE.FEES.PER.UNIT` | `FsGaStockTransaction_PerformanceFeesPerUnit` | TField |  | Performance fees per unit applied on a transaction. Multifonds DB Column is PF_PART. |
| 88 | `FS.GA.STOCK.TRANSACTION.COMMISSION.TYPE` | `FsGaStockTransaction_CommissionType` | TField |  | Commission type for lending/borrowing transactions Multifonds DB Column is TYP_COM. |
| 89 | `FS.GA.STOCK.TRANSACTION.MINIMUM.LENDING.COMMISSION` | `FsGaStockTransaction_MinimumLendingCommission` | TField |  | Minimum commission amount on a lending transaction Multifonds DB Column is MNT_COMM_MIN. |
| 90 | `FS.GA.STOCK.TRANSACTION.PERFORMANCE.FEES.AMOUNT` | `FsGaStockTransaction_PerformanceFeesAmount` | TField |  | Performance fees amount applied on a transaction. Multifonds DB Column is MNT_PF_FEES. |
| 91 | `FS.GA.STOCK.TRANSACTION.TRADE.FACTOR` | `FsGaStockTransaction_TradeFactor` | TField |  | The Trading factor for Mortgage backed securities Multifonds DB Column is FACTEUR. |
| 92 | `FS.GA.STOCK.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaStockTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 93 | `FS.GA.STOCK.TRANSACTION.UNREC.TAX.IN.AMOUNT.TYPE.1` | `FsGaStockTransaction_UnrecTaxInAmountType1` | TField |  | Unrecoverable tax amount on Income , type 1 Multifonds DB Column is MNTUNRECTAX. |
| 94 | `FS.GA.STOCK.TRANSACTION.UNREC.TAX.IN.AMOUNT.TYPE.2` | `FsGaStockTransaction_UnrecTaxInAmountType2` | TField |  | Unrecoverable tax amount on Income , type 2 Multifonds DB Column is MNTUNRECTAX_2. |
| 95 | `FS.GA.STOCK.TRANSACTION.COUPON.FREQUENCY.CODE` | `FsGaStockTransaction_CouponFrequencyCode` | TField |  | Frequency of payment of coupon/ commission Multifonds DB Column is CFREQCOUP. |
| 96 | `FS.GA.STOCK.TRANSACTION.REC.TAX.IN.AMOUNT.TYPE.1` | `FsGaStockTransaction_RecTaxInAmountType1` | TField |  | Recoverable tax amount on Income , type 1 Multifonds DB Column is MNTRECTAX. |
| 97 | `FS.GA.STOCK.TRANSACTION.RETROCESSION.COMMISSION.AMOUNT` | `FsGaStockTransaction_RetrocessionCommissionAmount` | TField |  | Recoverable tax amount on Income , type 2 Multifonds DB Column is MNTRECTAX_2. |
| 98 | `FS.GA.STOCK.TRANSACTION.HOLDING.PERIOD.TAX.IN.PERCENT` | `FsGaStockTransaction_HoldingPeriodTaxInPercent` | TField |  | Holding period tax percentage on Income Multifonds DB Column is HOLD_TAX. |
| 99 | `FS.GA.STOCK.TRANSACTION.KEST.AMOUNT` | `FsGaStockTransaction_KestAmount` | TField |  | This field is record the Kest Tax Amount Multifonds DB Column is MNT_KEST. |
| 100 | `FS.GA.STOCK.TRANSACTION.AMOUNT.OF.CAPITAL.GAIN` | `FsGaStockTransaction_AmountOfCapitalGain` | TField |  | Amount of capital gain on a disposition Multifonds DB Column is MNT_GAIN_CAP. |
| 101 | `FS.GA.STOCK.TRANSACTION.NET.SETTLEMENT.AMOUNT` | `FsGaStockTransaction_NetSettlementAmount` | TField |  | Net settlement amount on a transaction Multifonds DB Column is MONTNET_CPT. |
| 102 | `FS.GA.STOCK.TRANSACTION.ACCOUNTING.METHOD` | `FsGaStockTransaction_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 103 | `FS.GA.STOCK.TRANSACTION.CONTRACT.NUMBER` | `FsGaStockTransaction_ContractNumber` | TField |  | Contract number of lot being relieved Multifonds DB Column is CONTRAT_FLG. |
| 104 | `FS.GA.STOCK.TRANSACTION.HISTORICAL.DATE` | `FsGaStockTransaction_HistoricalDate` | TField |  | Historical acquisition date of a lot Multifonds DB Column is DATE_HIST. |
| 105 | `FS.GA.STOCK.TRANSACTION.HOLDING.PERIOD.TAX.IN.AMOUNT` | `FsGaStockTransaction_HoldingPeriodTaxInAmount` | TField |  | Holding period tax Amount on Income Multifonds DB Column is MNTHOLD_TAX. |
| 106 | `FS.GA.STOCK.TRANSACTION.TAXABLE.INCOME.2.PER.SHARE` | `FsGaStockTransaction_TaxableIncome2PerShare` | TField |  | The taxable income 2 per share in unit Multifonds DB Column is TIS2_PART. |
| 107 | `FS.GA.STOCK.TRANSACTION.TAXABLE.INCOME.3.PER.SHARE` | `FsGaStockTransaction_TaxableIncome3PerShare` | TField |  | The taxable income 3 per share in unit Multifonds DB Column is TIS3_PART. |
| 108 | `FS.GA.STOCK.TRANSACTION.TAXABLE.INCOME.PER.SHARE.UNIT` | `FsGaStockTransaction_TaxableIncomePerShareUnit` | TField |  | The taxable income per share in unit Multifonds DB Column is TIS_PART. |
| 109 | `FS.GA.STOCK.TRANSACTION.MARGIN.SUFFIX.NUMBER` | `FsGaStockTransaction_MarginSuffixNumber` | TField |  | Future margin account suffix number Multifonds DB Column is NSUFF_MARG. |
| 110 | `FS.GA.STOCK.TRANSACTION.ACCOUNTING.DATE` | `FsGaStockTransaction_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 111 | `FS.GA.STOCK.TRANSACTION.GROSS.AMOUNT.IN.LOCAL.CCY` | `FsGaStockTransaction_GrossAmountInLocalCcy` | TField |  | Gross amount in security currency Multifonds DB Column is MONTANT_OPER. |
| 112 | `FS.GA.STOCK.TRANSACTION.NET.AMOUNT.IN.BASE.CURRENCY` | `FsGaStockTransaction_NetAmountInBaseCurrency` | TField |  | Net Amount of fund base currency Multifonds DB Column is MONTNET_OPER_PTF. |
| 113 | `FS.GA.STOCK.TRANSACTION.INITIAL.MARGIN.AMOUNT` | `FsGaStockTransaction_InitialMarginAmount` | TField |  | Initial margin amount of future Multifonds DB Column is MNT_MARG. |
| 114 | `FS.GA.STOCK.TRANSACTION.INV.FUNDS.TAX.1.PER.UNIT` | `FsGaStockTransaction_InvFundsTax1PerUnit` | TField |  | Investment Funds Tax 1 Per Unit Multifonds DB Column is TG1_PART. |
| 115 | `FS.GA.STOCK.TRANSACTION.INV.FUNDS.TAX.3.PER.UNIT` | `FsGaStockTransaction_InvFundsTax3PerUnit` | TField |  | Investment Funds Tax 3 Per Unit Multifonds DB Column is TG3_PART. |
| 116 | `FS.GA.STOCK.TRANSACTION.INV.FUNDS.TAX.2.PER.UNIT` | `FsGaStockTransaction_InvFundsTax2PerUnit` | TField |  | Investment Funds Tax 2 Per Unit Multifonds DB Column is TG2_PART. |
| 117 | `FS.GA.STOCK.TRANSACTION.NAV.PRICE.DATE` | `FsGaStockTransaction_NavPriceDate` | TField |  | NAV Price date of the pool fund Multifonds DB Column is NAV_PRICE_DATE. |
| 118 | `FS.GA.STOCK.TRANSACTION.NET.AMOUNT.IN.SECURITY.CCY` | `FsGaStockTransaction_NetAmountInSecurityCcy` | TField |  | Net amount in security currency Multifonds DB Column is MONTNET_OPER. |
| 119 | `FS.GA.STOCK.TRANSACTION.3DEC.OPERATION.NET.EXCL.AMOUNT` | `FsGaStockTransaction_3decOperationNetExclAmount` |  |  |  |
| 120 | `FS.GA.STOCK.TRANSACTION.DELAY.COMPENSATION.AMOUNT.TYPE` | `FsGaStockTransaction_DelayCompensationAmountType` | TField |  | Delay compensation Amount type Multifonds DB Column is DELAYED_COMP_AMT_TYPE. |
| 121 | `FS.GA.STOCK.TRANSACTION.KEST.PER.UNIT` | `FsGaStockTransaction_KestPerUnit` | TField |  | German witholding tax per unit Multifonds DB Column is KEST_PART. |
| 122 | `FS.GA.STOCK.TRANSACTION.OPERATION.EXCLUSION.NET.AMOUNT` | `FsGaStockTransaction_OperationExclusionNetAmount` | TField |  | Operation Exclusion Net Amount Multifonds DB Column is MONTNET_OPER_EXL. |
| 123 | `FS.GA.STOCK.TRANSACTION.LENDING.MATURITY.DATE` | `FsGaStockTransaction_LendingMaturityDate` | TField |  | Security lending maturity date Multifonds DB Column is DECH_LEN. |
| 124 | `FS.GA.STOCK.TRANSACTION.SETTLE.DATE` | `FsGaStockTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 125 | `FS.GA.STOCK.TRANSACTION.3DECIMAL.OPER.INTEREST.AMOUNT` | `FsGaStockTransaction_3decimalOperInterestAmount` |  |  |  |
| 126 | `FS.GA.STOCK.TRANSACTION.3DECIMAL.OPERATION.FEE.AMOUNT` | `FsGaStockTransaction_3decimalOperationFeeAmount` |  |  |  |
| 127 | `FS.GA.STOCK.TRANSACTION.3DECIMAL.OPERATION.NET.AMOUNT` | `FsGaStockTransaction_3decimalOperationNetAmount` |  |  |  |
| 128 | `FS.GA.STOCK.TRANSACTION.AMORTISATION.SOLD.COST.AMOUNT` | `FsGaStockTransaction_AmortisationSoldCostAmount` | TField |  | Amortisation sold cost amount Multifonds DB Column is AMORT_COST_SOLD_FCY. |
| 129 | `FS.GA.STOCK.TRANSACTION.INV.FUNDS.TAX.1.AMOUNT` | `FsGaStockTransaction_InvFundsTax1Amount` | TField |  | Investment Funds Tax 1 Amount Multifonds DB Column is MNT_TG1. |
| 130 | `FS.GA.STOCK.TRANSACTION.INV.FUNDS.TAX.2.AMOUNT` | `FsGaStockTransaction_InvFundsTax2Amount` | TField |  | Investment Funds Tax 2 Amount Multifonds DB Column is MNT_TG2. |
| 131 | `FS.GA.STOCK.TRANSACTION.SECURITY.FOREX.VCI.SETTLEMENT` | `FsGaStockTransaction_SecurityForexVciSettlement` | TField |  | Security Forex VCI Settlement Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 132 | `FS.GA.STOCK.TRANSACTION.STLMT.DAYS.CALC.FOR.BANK.DEBT` | `FsGaStockTransaction_StlmtDaysCalcForBankDebt` | TField |  | Stlmt Days Calc For Bank Debt Multifonds DB Column is FLG_PAR_NEAR_PAR. |
| 133 | `FS.GA.STOCK.TRANSACTION.3DECIMAL.CPT.EXCEL.NET.AMOUNT` | `FsGaStockTransaction_3decimalCptExcelNetAmount` |  |  |  |
| 134 | `FS.GA.STOCK.TRANSACTION.UNDERLYING.CONTRACT.LENT` | `FsGaStockTransaction_UnderlyingContractLent` | TField |  | Contract no of lent contract Multifonds DB Column is NCONTRAT_LEN. |
| 135 | `FS.GA.STOCK.TRANSACTION.MARGIN.ACCOUNT.NUMBER` | `FsGaStockTransaction_MarginAccountNumber` | TField |  | Future margin account number Multifonds DB Column is NRUBR_MARG. |
| 136 | `FS.GA.STOCK.TRANSACTION.INCOME.EQUALISATION.PER.UNIT` | `FsGaStockTransaction_IncomeEqualisationPerUnit` | TField |  | Income Equalisation Per Unit Multifonds DB Column is RNI_PART. |
| 137 | `FS.GA.STOCK.TRANSACTION.TRADE.DATE` | `FsGaStockTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 138 | `FS.GA.STOCK.TRANSACTION.DELAYED.COMPENSATION.AMOUNT` | `FsGaStockTransaction_DelayedCompensationAmount` | TField |  | Delayed compensation Amount Multifonds DB Column is DELAYED_COMP_AMT. |
| 139 | `FS.GA.STOCK.TRANSACTION.DESCRIPTION` | `FsGaStockTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 140 | `FS.GA.STOCK.TRANSACTION.FUND.AMORTISATION.COST.SOLD` | `FsGaStockTransaction_FundAmortisationCostSold` | TField |  | Fund Amortization Cost Sold Multifonds DB Column is AMORT_COST_SOLD_PTF. |
| 141 | `FS.GA.STOCK.TRANSACTION.FUND.WITHHOLDING.TAX.AMOUNT` | `FsGaStockTransaction_FundWithholdingTaxAmount` | TField |  | Fund Withholding tax amount Multifonds DB Column is MNTHOLD_TAX_PTF. |
| 142 | `FS.GA.STOCK.TRANSACTION.KOREAN.NONTAXABLE.PER.SHARE` | `FsGaStockTransaction_KoreanNontaxablePerShare` | TField |  | Korean Nontaxable per Share Multifonds DB Column is TCOURS_NRTX. |
| 143 | `FS.GA.STOCK.TRANSACTION.MIGRATION.AMORT.DEAL.AMOUNT` | `FsGaStockTransaction_MigrationAmortDealAmount` | TField |  | Migration amort deal amount Multifonds DB Column is MIG_MNT_AMORT_DEAL. |
| 144 | `FS.GA.STOCK.TRANSACTION.MIGRATION.AMORT.FUND.AMOUNT` | `FsGaStockTransaction_MigrationAmortFundAmount` | TField |  | Migration amort fund amount Multifonds DB Column is MIG_MNT_AMORT_PTF. |
| 145 | `FS.GA.STOCK.TRANSACTION.TG1.AMOUNT.IN.FUND.CURRENCY` | `FsGaStockTransaction_Tg1AmountInFundCurrency` | TField |  | TG1 amount in fund currency Multifonds DB Column is MNT_TG1_PTF. |
| 146 | `FS.GA.STOCK.TRANSACTION.TG2.AMOUNT.IN.FUND.CURRENCY` | `FsGaStockTransaction_Tg2AmountInFundCurrency` | TField |  | TG2 amount in fund currency Multifonds DB Column is MNT_TG2_PTF. |
| 147 | `FS.GA.STOCK.TRANSACTION.TG3.AMOUNT.IN.FUND.CURRENCY` | `FsGaStockTransaction_Tg3AmountInFundCurrency` | TField |  | TG3 amount in fund currency Multifonds DB Column is MNT_TG3_PTF. |
| 148 | `FS.GA.STOCK.TRANSACTION.LENDING.CTR.ACCOUNT.NUMBER` | `FsGaStockTransaction_LendingCtrAccountNumber` | TField |  | Lending CTR Account Number Multifonds DB Column is NRUBR_LEN_CTR. |
| 149 | `FS.GA.STOCK.TRANSACTION.OPERATION.PERF.FEES.AMOUNT` | `FsGaStockTransaction_OperationPerfFeesAmount` | TField |  | Operation Perf fees amount Multifonds DB Column is MNT_PF_FEES_PTF. |
| 150 | `FS.GA.STOCK.TRANSACTION.PROCEEDS.ADJUSTMENT.AMOUNT` | `FsGaStockTransaction_ProceedsAdjustmentAmount` | TField |  | Proceeds adjustment amount Multifonds DB Column is MNT_PROCEEDS_ADJ. |
| 151 | `FS.GA.STOCK.TRANSACTION.TAXABLE.INCOME.2.AMOUNT` | `FsGaStockTransaction_TaxableIncome2Amount` | TField |  | The Taxable income 2 amount Multifonds DB Column is MNT_TIS2. |
| 152 | `FS.GA.STOCK.TRANSACTION.TAXABLE.INCOME.3.AMOUNT` | `FsGaStockTransaction_TaxableIncome3Amount` | TField |  | The Taxable income 3 amount Multifonds DB Column is MNT_TIS3. |
| 153 | `FS.GA.STOCK.TRANSACTION.TAXABLE.INCOME.AMOUNT` | `FsGaStockTransaction_TaxableIncomeAmount` | TField |  | The Taxable income amount Multifonds DB Column is MNT_TIS. |
| 154 | `FS.GA.STOCK.TRANSACTION.EXTERNAL.CONTRACT.NUMBER` | `FsGaStockTransaction_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 155 | `FS.GA.STOCK.TRANSACTION.FUND.FX.SETTLEMENT.VCI` | `FsGaStockTransaction_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 156 | `FS.GA.STOCK.TRANSACTION.FUND.PIK.OPERATION.AMOUNT` | `FsGaStockTransaction_FundPikOperationAmount` | TField |  | Fund Pik Operation Amount Multifonds DB Column is PIK_MINT_OPER_PTF. |
| 157 | `FS.GA.STOCK.TRANSACTION.INTEREST.AMOUNT.SMOOTHING` | `FsGaStockTransaction_InterestAmountSmoothing` | TField |  | Interest Amount Smoothing Multifonds DB Column is MNT_INT_SMOOTH. |
| 158 | `FS.GA.STOCK.TRANSACTION.LENDING.CTR.SUFFIX.NUMBER` | `FsGaStockTransaction_LendingCtrSuffixNumber` | TField |  | Lending CTR Suffix Number Multifonds DB Column is NSUFF_LEN_CTR. |
| 159 | `FS.GA.STOCK.TRANSACTION.CPT.EXCLUSION.NET.AMOUNT` | `FsGaStockTransaction_CptExclusionNetAmount` | TField |  | CPT Exclusion Net Amount Multifonds DB Column is MONTNET_CPT_EXL. |
| 160 | `FS.GA.STOCK.TRANSACTION.PIK.FACTOR` | `FsGaStockTransaction_PikFactor` | TField |  | Factor for PIK security Multifonds DB Column is PIK_FACTOR. |
| 161 | `FS.GA.STOCK.TRANSACTION.FUND.AMORTISSEMENT.AMOUNT` | `FsGaStockTransaction_FundAmortissementAmount` | TField |  | Fund Amortissement Amount Multifonds DB Column is AMORTISSEMENT_PTF. |
| 162 | `FS.GA.STOCK.TRANSACTION.GST.REVISED.UPDATED.DATE` | `FsGaStockTransaction_GstRevisedUpdatedDate` | TField |  | GST Revised Updated Date Multifonds DB Column is GST_DUPDATED_REV. |
| 163 | `FS.GA.STOCK.TRANSACTION.KOREAN.TAXABLE.PER.SHARE` | `FsGaStockTransaction_KoreanTaxablePerShare` | TField |  | Korean Taxable per Share Multifonds DB Column is TCOURS_TX. |
| 164 | `FS.GA.STOCK.TRANSACTION.PIK.AMOUNT.OPER.3DECIMAL` | `FsGaStockTransaction_PikAmountOper3decimal` | TField |  | PIK Amount Oper 3Decimal Multifonds DB Column is PIK_MINT_OPER_3DEC. |
| 165 | `FS.GA.STOCK.TRANSACTION.PIK.OPER.3DECIMAL.AMOUNT` | `FsGaStockTransaction_PikOper3decimalAmount` | TField |  | PIK Oper 3Decimal amount Multifonds DB Column is PIK_MONTANT_OPER_3DEC. |
| 166 | `FS.GA.STOCK.TRANSACTION.REP.INTEREST.CALCULATION` | `FsGaStockTransaction_RepInterestCalculation` | TField |  | Rep Interest Calculation Multifonds DB Column is CUSA_REP. |
| 167 | `FS.GA.STOCK.TRANSACTION.3DECIMAL.CPT.NET.AMOUNT` | `FsGaStockTransaction_3decimalCptNetAmount` |  |  |  |
| 168 | `FS.GA.STOCK.TRANSACTION.ACQUIRED.AMORTISED.COST` | `FsGaStockTransaction_AcquiredAmortisedCost` | TField |  | Acquired amortized cost Multifonds DB Column is MNT_AMORT_COST. |
| 169 | `FS.GA.STOCK.TRANSACTION.FUND.FOREX.VCI.SECURITY` | `FsGaStockTransaction_FundForexVciSecurity` | TField |  | Fund Forex VCI Security Multifonds DB Column is SEC_PTF_FX_VCI. |
| 170 | `FS.GA.STOCK.TRANSACTION.FUND.NON.TAXABLE.AMOUNT` | `FsGaStockTransaction_FundNonTaxableAmount` | TField |  | Fund Non Taxable Amount Multifonds DB Column is MNT_NTX_PTF. |
| 171 | `FS.GA.STOCK.TRANSACTION.OPERATION.NUMBER.ORIGIN` | `FsGaStockTransaction_OperationNumberOrigin` | TField |  | Operation number origin Multifonds DB Column is NECRITUR_PTF_ORIG_RP. |
| 172 | `FS.GA.STOCK.TRANSACTION.ORIGINAL.DEPOSIT.NUMBER` | `FsGaStockTransaction_OriginalDepositNumber` | TField |  | Original deposit number Multifonds DB Column is NDEPOSI_ORIG. |
| 173 | `FS.GA.STOCK.TRANSACTION.ACCOUNTING.DATE.ORIGIN` | `FsGaStockTransaction_AccountingDateOrigin` | TField |  | Accounting date origin Multifonds DB Column is DCTA_ORIG_RP. |
| 174 | `FS.GA.STOCK.TRANSACTION.AMORTISATION.COST.SOLD` | `FsGaStockTransaction_AmortisationCostSold` | TField |  | Amortization Cost Sold Multifonds DB Column is AMORT_COST_SOLD. |
| 175 | `FS.GA.STOCK.TRANSACTION.GST.REVISED.UPDATED.BY` | `FsGaStockTransaction_GstRevisedUpdatedBy` | TField |  | GST Revised Updated By Multifonds DB Column is GST_UPDATED_BY_REV. |
| 176 | `FS.GA.STOCK.TRANSACTION.INV.FUNDS.TAX.3.AMOUNT` | `FsGaStockTransaction_InvFundsTax3Amount` | TField |  | Inv Funds Tax 3 Amount Multifonds DB Column is MNT_TG3. |
| 177 | `FS.GA.STOCK.TRANSACTION.LENDING.ACCOUNT.NUMBER` | `FsGaStockTransaction_LendingAccountNumber` | TField |  | Lending Account Number Multifonds DB Column is NRUBR_LEN. |
| 178 | `FS.GA.STOCK.TRANSACTION.LENDING.COMMISSION.OLD` | `FsGaStockTransaction_LendingCommissionOld` | TField |  | Lending Commission Old Multifonds DB Column is COM_LEN_OLD. |
| 179 | `FS.GA.STOCK.TRANSACTION.OPERATION.AKTIEN.ZWIST` | `FsGaStockTransaction_OperationAktienZwist` | TField |  | Operation aktien zwist Multifonds DB Column is AKTIENZWIST_PTF. |
| 180 | `FS.GA.STOCK.TRANSACTION.REPRISE.ACCOUNT.NUMBER` | `FsGaStockTransaction_RepriseAccountNumber` | TField |  | Reprise Account Number Multifonds DB Column is NRUBR_REP. |
| 181 | `FS.GA.STOCK.TRANSACTION.COMMISSION.ADJUSTMENT` | `FsGaStockTransaction_CommissionAdjustment` | TField |  | Commission adjustment Multifonds DB Column is FLG_COMM_ADJUST. |
| 182 | `FS.GA.STOCK.TRANSACTION.FUND.OPERATION.AMOUNT` | `FsGaStockTransaction_FundOperationAmount` | TField |  | Fund operation amount Multifonds DB Column is MINT_OPER_PTF. |
| 183 | `FS.GA.STOCK.TRANSACTION.LENDING.SUFFIX.NUMBER` | `FsGaStockTransaction_LendingSuffixNumber` | TField |  | Lending Suffix Number Multifonds DB Column is NSUFF_LEN. |
| 184 | `FS.GA.STOCK.TRANSACTION.ORIGINAL.ENTRY.NUMBER` | `FsGaStockTransaction_OriginalEntryNumber` | TField |  | Original entry number Multifonds DB Column is NECRITUR_ORIGIN. |
| 185 | `FS.GA.STOCK.TRANSACTION.REPRISE.SUFFIX.NUMBER` | `FsGaStockTransaction_RepriseSuffixNumber` | TField |  | Reprise Suffix Number Multifonds DB Column is NSUFF_REP. |
| 186 | `FS.GA.STOCK.TRANSACTION.3DECIMAL.OPER.AMOUNT` | `FsGaStockTransaction_3decimalOperAmount` |  |  |  |
| 187 | `FS.GA.STOCK.TRANSACTION.FUND.DISCOUNT.AMOUNT` | `FsGaStockTransaction_FundDiscountAmount` | TField |  | Fund discount amount Multifonds DB Column is MNT_DISCOUNT_PTF. |
| 188 | `FS.GA.STOCK.TRANSACTION.GST.REVISED.CLAIM.ID` | `FsGaStockTransaction_GstRevisedClaimId` | TField |  | GST Revised Claim ID Multifonds DB Column is GST_CLAIM_ID_REV. |
| 189 | `FS.GA.STOCK.TRANSACTION.OPERATION.TIS.AMOUNT` | `FsGaStockTransaction_OperationTisAmount` | TField |  | Operation tis amount Multifonds DB Column is MNT_TIS_PTF. |
| 190 | `FS.GA.STOCK.TRANSACTION.QUANTITY` | `FsGaStockTransaction_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 191 | `FS.GA.STOCK.TRANSACTION.AMORTISSMENT.AMOUNT` | `FsGaStockTransaction_AmortissmentAmount` | TField |  | Amortissment Amount Multifonds DB Column is AMORTISSEMENT. |
| 192 | `FS.GA.STOCK.TRANSACTION.FEE.NON.CAPITALISED` | `FsGaStockTransaction_FeeNonCapitalised` | TField |  | Fee Non Capitalised Multifonds DB Column is FEES_NON_CAPITALISED. |
| 193 | `FS.GA.STOCK.TRANSACTION.GAIN.OR.LOSS.AMOUNT` | `FsGaStockTransaction_GainOrLossAmount` | TField |  | Gain or loss amount Multifonds DB Column is MNT_GP_TAX. |
| 194 | `FS.GA.STOCK.TRANSACTION.LENDING.TYPE.AMOUNT` | `FsGaStockTransaction_LendingTypeAmount` | TField |  | Lending Type Amount Multifonds DB Column is MNT_TYP_LEN. |
| 195 | `FS.GA.STOCK.TRANSACTION.MIGRATION.UNIT.COST` | `FsGaStockTransaction_MigrationUnitCost` | TField |  | Migration unit cost Multifonds DB Column is MIG_UNIT_COST. |
| 196 | `FS.GA.STOCK.TRANSACTION.OLD.CONTRACT.NUMBER` | `FsGaStockTransaction_OldContractNumber` | TField |  | Old Contract Number Multifonds DB Column is NCONTRAT_OLD. |
| 197 | `FS.GA.STOCK.TRANSACTION.PIK.INTEREST.AMOUNT` | `FsGaStockTransaction_PikInterestAmount` | TField |  | PIK Interest Amount Multifonds DB Column is PIK_MINT_OPER. |
| 198 | `FS.GA.STOCK.TRANSACTION.SECURITY.VALUE.DATE` | `FsGaStockTransaction_SecurityValueDate` | TField |  | Security Value Date Multifonds DB Column is DVALEUR_SEC. |
| 199 | `FS.GA.STOCK.TRANSACTION.CAPITALIZATION.DAY` | `FsGaStockTransaction_CapitalizationDay` | TField |  | Capitalization Day Multifonds DB Column is DATCOMM. |
| 200 | `FS.GA.STOCK.TRANSACTION.FUND.SPREAD.AMOUNT` | `FsGaStockTransaction_FundSpreadAmount` | TField |  | Fund Spread Amount Multifonds DB Column is MINT_SPREAD_PTF. |
| 201 | `FS.GA.STOCK.TRANSACTION.LENDING.COMMISSION` | `FsGaStockTransaction_LendingCommission` | TField |  | Lending Commission Multifonds DB Column is COM_LEN. |
| 202 | `FS.GA.STOCK.TRANSACTION.NON.TAXABLE.AMOUNT` | `FsGaStockTransaction_NonTaxableAmount` | TField |  | Non Taxable Amount Multifonds DB Column is MNT_NTX. |
| 203 | `FS.GA.STOCK.TRANSACTION.NON.TAXABLE.PRICE` | `FsGaStockTransaction_NonTaxablePrice` | TField |  | Non Taxable Price Multifonds DB Column is TCOURS_NTX. |
| 204 | `FS.GA.STOCK.TRANSACTION.CONFIRMATION.DATE` | `FsGaStockTransaction_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 205 | `FS.GA.STOCK.TRANSACTION.NEGATIVE.INTEREST` | `FsGaStockTransaction_NegativeInterest` | TField |  | Negative interest Multifonds DB Column is FLG_INT_NEG. |
| 206 | `FS.GA.STOCK.TRANSACTION.OLD.EXCHANGE.RATE` | `FsGaStockTransaction_OldExchangeRate` | TField |  | Old exchange rate Multifonds DB Column is TCHG_OLD. |
| 207 | `FS.GA.STOCK.TRANSACTION.PIK.INTEREST.RATE` | `FsGaStockTransaction_PikInterestRate` | TField |  | PIK Interest Rate Multifonds DB Column is PIK_TXINT. |
| 208 | `FS.GA.STOCK.TRANSACTION.REP.MATURITY.DATE` | `FsGaStockTransaction_RepMaturityDate` | TField |  | REP Maturity date Multifonds DB Column is DECH_REP. |
| 209 | `FS.GA.STOCK.TRANSACTION.TIS.2.FUND.AMOUNT` | `FsGaStockTransaction_Tis2FundAmount` | TField |  | TIS 2 fund amount Multifonds DB Column is MNT_TIS2_PTF. |
| 210 | `FS.GA.STOCK.TRANSACTION.TIS.3.FUND.AMOUNT` | `FsGaStockTransaction_Tis3FundAmount` | TField |  | TIS 3 fund amount Multifonds DB Column is MNT_TIS3_PTF. |
| 211 | `FS.GA.STOCK.TRANSACTION.FCY.AMORTISATION` | `FsGaStockTransaction_FcyAmortisation` | TField |  | FCY Amortization Multifonds DB Column is AMORTISSEMENT_FCY. |
| 212 | `FS.GA.STOCK.TRANSACTION.FUND.KEST.AMOUNT` | `FsGaStockTransaction_FundKestAmount` | TField |  | Fund Kest Amount Multifonds DB Column is MNT_KEST_PTF. |
| 213 | `FS.GA.STOCK.TRANSACTION.FUND.NRTX.AMOUNT` | `FsGaStockTransaction_FundNrtxAmount` | TField |  | Fund NRTX Amount Multifonds DB Column is MNT_NRTX_PTF. |
| 214 | `FS.GA.STOCK.TRANSACTION.FUND.OPER.AMOUNT` | `FsGaStockTransaction_FundOperAmount` | TField |  | Fund Oper Amount Multifonds DB Column is MONTANT_OPER_PTF. |
| 215 | `FS.GA.STOCK.TRANSACTION.FUND.RISK.AMOUNT` | `FsGaStockTransaction_FundRiskAmount` | TField |  | Fund Risk Amount Multifonds DB Column is MINT_RISK_PTF. |
| 216 | `FS.GA.STOCK.TRANSACTION.GST.CONFIRMATION` | `FsGaStockTransaction_GstConfirmation` | TField |  | GST Confirmation Multifonds DB Column is GST_CONFIRM. |
| 217 | `FS.GA.STOCK.TRANSACTION.GST.UPDATED.DATE` | `FsGaStockTransaction_GstUpdatedDate` | TField |  | GST Updated date Multifonds DB Column is GST_DUPDATED. |
| 218 | `FS.GA.STOCK.TRANSACTION.INCOME.CHARACTER.IDENTIFIER` | `FsGaStockTransaction_IncomeCharacterIdentifier` | TField |  | Income Character Multifonds DB Column is INCOMECHAR_FLG. |
| 219 | `FS.GA.STOCK.TRANSACTION.PERCENTAGE.OWNED` | `FsGaStockTransaction_PercentageOwned` | TField |  | Percentage Owned Multifonds DB Column is PERC_OWNED. |
| 220 | `FS.GA.STOCK.TRANSACTION.REPRISE.CURRENCY` | `FsGaStockTransaction_RepriseCurrency` | TField |  | Currency Multifonds DB Column is CMON_REPRISE. |
| 221 | `FS.GA.STOCK.TRANSACTION.SETTLEMENT.DATE1` | `FsGaStockTransaction_SettlementDate1` | TField |  | Settlement Date1 Multifonds DB Column is D_SETTLEMENT. |
| 222 | `FS.GA.STOCK.TRANSACTION.TOTAL.RITC.VALUE` | `FsGaStockTransaction_TotalRitcValue` | TField |  | Total RITC Value Multifonds DB Column is MFRAIS_RITC. |
| 223 | `FS.GA.STOCK.TRANSACTION.TRANSACTION.FEES` | `FsGaStockTransaction_TransactionFees` | TField |  | Transaction fees Multifonds DB Column is FLAG_TR_FEES. |
| 224 | `FS.GA.STOCK.TRANSACTION.AC.ENTRY.NUMBER` | `FsGaStockTransaction_AcEntryNumber` | TField |  | AC Entry Number Multifonds DB Column is NECRITUR_AC. |
| 225 | `FS.GA.STOCK.TRANSACTION.ADJUSTMENT.FUND` | `FsGaStockTransaction_AdjustmentFund` | TField |  | Adjustment Fund Multifonds DB Column is NPTF_ORIGIN. |
| 226 | `FS.GA.STOCK.TRANSACTION.BO.ENTRY.NUMBER` | `FsGaStockTransaction_BoEntryNumber` | TField |  | BO Entry number Multifonds DB Column is NECRITUR_BO. |
| 227 | `FS.GA.STOCK.TRANSACTION.BOND.TAX.OR.CGT` | `FsGaStockTransaction_BondTaxOrCgt` | TField |  | Bond Tax Or CGT Multifonds DB Column is FLG_CGT_BONDTAX. |
| 228 | `FS.GA.STOCK.TRANSACTION.FEE.CAPITALISED` | `FsGaStockTransaction_FeeCapitalised` | TField |  | Fee Capitalised Multifonds DB Column is FEES_CAPITALISED. |
| 229 | `FS.GA.STOCK.TRANSACTION.FUND.TAX.AMOUNT` | `FsGaStockTransaction_FundTaxAmount` | TField |  | Fund tax amount Multifonds DB Column is MNT_TX_PTF. |
| 230 | `FS.GA.STOCK.TRANSACTION.OPERATION.ZWIST` | `FsGaStockTransaction_OperationZwist` | TField |  | Operation zwist Multifonds DB Column is ZWIST_PTF. |
| 231 | `FS.GA.STOCK.TRANSACTION.AUTOMATIC.HIFO` | `FsGaStockTransaction_AutomaticHifo` | TField |  | Automatic HIFO Multifonds DB Column is AUTO_HIFO. |
| 232 | `FS.GA.STOCK.TRANSACTION.RATE.OF.EXCHANGE` | `FsGaStockTransaction_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 233 | `FS.GA.STOCK.TRANSACTION.FEE.SETTLEMENT` | `FsGaStockTransaction_FeeSettlement` | TField |  | Fee Settlement Multifonds DB Column is MFRAIS_SETTLE. |
| 234 | `FS.GA.STOCK.TRANSACTION.GST.UPDATED.BY` | `FsGaStockTransaction_GstUpdatedBy` | TField |  | GST Updated By Multifonds DB Column is GST_UPDATED_BY. |
| 235 | `FS.GA.STOCK.TRANSACTION.KNOWLEDGE.DATE` | `FsGaStockTransaction_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 236 | `FS.GA.STOCK.TRANSACTION.SETTLEMENT.DAY` | `FsGaStockTransaction_SettlementDay` | TField |  | Settlement Day Multifonds DB Column is SETTLE_DT. |
| 237 | `FS.GA.STOCK.TRANSACTION.STATUS.PENDING` | `FsGaStockTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 238 | `FS.GA.STOCK.TRANSACTION.TAX.BOOK.PRICE` | `FsGaStockTransaction_TaxBookPrice` | TField |  | Tax Book Price Multifonds DB Column is TCOURS_TBC. |
| 239 | `FS.GA.STOCK.TRANSACTION.IG.ZWIST.FUND` | `FsGaStockTransaction_IgZwistFund` | TField |  | IG ZWIST Fund Multifonds DB Column is IG_ZWIST_PTF. |
| 240 | `FS.GA.STOCK.TRANSACTION.SPREAD.AMOUNT` | `FsGaStockTransaction_SpreadAmount` | TField |  | Spread Amount Multifonds DB Column is MINT_SPREAD. |
| 241 | `FS.GA.STOCK.TRANSACTION.CHECK.DATE` | `FsGaStockTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 242 | `FS.GA.STOCK.TRANSACTION.GST.CLAIM.ID` | `FsGaStockTransaction_GstClaimId` | TField |  | GST Claim ID Multifonds DB Column is GST_CLAIM_ID. |
| 243 | `FS.GA.STOCK.TRANSACTION.FIRST.COUPON.DATE` | `FsGaStockTransaction_FirstCouponDate` | TField |  | First Coupon Date Multifonds DB Column is DATCOUPON. |
| 244 | `FS.GA.STOCK.TRANSACTION.RATE.CAPITAL` | `FsGaStockTransaction_RateCapital` | TField |  | Rate Capital Multifonds DB Column is RATE_CAPITAL. |
| 245 | `FS.GA.STOCK.TRANSACTION.AKTIENZWIST` | `FsGaStockTransaction_Aktienzwist` | TField |  | Aktienzwist Multifonds DB Column is AKTIENZWIST. |
| 246 | `FS.GA.STOCK.TRANSACTION.RISK.AMOUNT` | `FsGaStockTransaction_RiskAmount` | TField |  | Risk Amount Multifonds DB Column is MINT_RISK. |
| 247 | `FS.GA.STOCK.TRANSACTION.SHARE.CLASS.CODE` | `FsGaStockTransaction_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 248 | `FS.GA.STOCK.TRANSACTION.CHECKED.BY` | `FsGaStockTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 249 | `FS.GA.STOCK.TRANSACTION.FACE.VALUE` | `FsGaStockTransaction_FaceValue` | TField |  | Face Value Multifonds DB Column is FACE_VALUE. |
| 250 | `FS.GA.STOCK.TRANSACTION.MANAGER.ID` | `FsGaStockTransaction_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 251 | `FS.GA.STOCK.TRANSACTION.REP.SPREAD` | `FsGaStockTransaction_RepSpread` | TField |  | REP Spread Multifonds DB Column is SPREAD_REP. |
| 252 | `FS.GA.STOCK.TRANSACTION.CAT.CODE` | `FsGaStockTransaction_CatCode` | TField |  | CAT Code Multifonds DB Column is CAT_CODE. |
| 253 | `FS.GA.STOCK.TRANSACTION.IG.ZWIST` | `FsGaStockTransaction_IgZwist` | TField |  | IG ZWIST Multifonds DB Column is IG_ZWIST. |
| 254 | `FS.GA.STOCK.TRANSACTION.REP.RATE` | `FsGaStockTransaction_RepRate` | TField |  | REP Rate Multifonds DB Column is RATE_REP. |
| 255 | `FS.GA.STOCK.TRANSACTION.TRADE.ID` | `FsGaStockTransaction_TradeId` | TField |  | Trade Id Multifonds DB Column is TRADEID. |
| 256 | `FS.GA.STOCK.TRANSACTION.GL.ACCOUNT` | `FsGaStockTransaction_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 257 | `FS.GA.STOCK.TRANSACTION.ARCHIVE` | `FsGaStockTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 258 | `FS.GA.STOCK.TRANSACTION.FCHDEP` | `FsGaStockTransaction_Fchdep` | TField |  | FCHDEP Multifonds DB Column is FCHDEP. |
| 259 | `FS.GA.STOCK.TRANSACTION.MODULE.IDENTIFIER` | `FsGaStockTransaction_ModuleIdentifier` | TField |  | Module Multifonds DB Column is FLG_MODULE. |
| 260 | `FS.GA.STOCK.TRANSACTION.DEAL.STATUS.CODE` | `FsGaStockTransaction_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 261 | `FS.GA.STOCK.TRANSACTION.VA.TAX` | `FsGaStockTransaction_VaTax` | TField |  | VA Tax Multifonds DB Column is FLG_TAX_VA. |
| 262 | `FS.GA.STOCK.TRANSACTION.CLIV` | `FsGaStockTransaction_Cliv` | TField |  | CLIV Multifonds DB Column is CLIV. |
| 263 | `FS.GA.STOCK.TRANSACTION.LINE` | `FsGaStockTransaction_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 264 | `FS.GA.STOCK.TRANSACTION.TOM` | `FsGaStockTransaction_Tom` | TField |  | TOM Multifonds DB Column is FLG_TOM. |
| 265 | `FS.GA.STOCK.TRANSACTION.OPERATION.TYPE` | `FsGaStockTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 266 | `FS.GA.STOCK.TRANSACTION.RESERVED10` | `FsGaStockTransaction_Reserved10` | TField |  |  |
| 267 | `FS.GA.STOCK.TRANSACTION.RESERVED9` | `FsGaStockTransaction_Reserved9` | TField |  |  |
| 268 | `FS.GA.STOCK.TRANSACTION.RESERVED8` | `FsGaStockTransaction_Reserved8` | TField |  |  |
| 269 | `FS.GA.STOCK.TRANSACTION.RESERVED7` | `FsGaStockTransaction_Reserved7` | TField |  |  |
| 270 | `FS.GA.STOCK.TRANSACTION.RESERVED6` | `FsGaStockTransaction_Reserved6` | TField |  |  |
| 271 | `FS.GA.STOCK.TRANSACTION.RESERVED5` | `FsGaStockTransaction_Reserved5` | TField |  |  |
| 272 | `FS.GA.STOCK.TRANSACTION.RESERVED4` | `FsGaStockTransaction_Reserved4` | TField |  |  |
| 273 | `FS.GA.STOCK.TRANSACTION.RESERVED3` | `FsGaStockTransaction_Reserved3` | TField |  |  |
| 274 | `FS.GA.STOCK.TRANSACTION.RESERVED2` | `FsGaStockTransaction_Reserved2` | TField |  |  |
| 275 | `FS.GA.STOCK.TRANSACTION.RESERVED1` | `FsGaStockTransaction_Reserved1` | TField |  |  |
| 276 | `FS.GA.STOCK.TRANSACTION.LOCAL.REF` | `FsGaStockTransaction_LocalRef` |  |  |  |
| 277 | `FS.GA.STOCK.TRANSACTION.OVERRIDE` | `FsGaStockTransaction_Override` |  |  |  |
| 278 | `FS.GA.STOCK.TRANSACTION.RECORD.STATUS` | `FsGaStockTransaction_RecordStatus` | String |  |  |
| 279 | `FS.GA.STOCK.TRANSACTION.CURR.NO` | `FsGaStockTransaction_CurrNo` | String |  |  |
| 280 | `FS.GA.STOCK.TRANSACTION.INPUTTER` | `FsGaStockTransaction_Inputter` |  |  |  |
| 281 | `FS.GA.STOCK.TRANSACTION.DATE.TIME` | `FsGaStockTransaction_DateTime` |  |  |  |
| 282 | `FS.GA.STOCK.TRANSACTION.AUTHORISER` | `FsGaStockTransaction_Authoriser` | String |  |  |
| 283 | `FS.GA.STOCK.TRANSACTION.CO.CODE` | `FsGaStockTransaction_CoCode` | String |  |  |
| 284 | `FS.GA.STOCK.TRANSACTION.DEPT.CODE` | `FsGaStockTransaction_DeptCode` | String |  |  |
| 285 | `FS.GA.STOCK.TRANSACTION.AUDITOR.CODE` | `FsGaStockTransaction_AuditorCode` | String |  |  |
| 286 | `FS.GA.STOCK.TRANSACTION.AUDIT.DATE.TIME` | `FsGaStockTransaction_AuditDateTime` | String |  |  |
