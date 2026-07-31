# SECURITY.TRANS — Table Schema

> Source: `INSERTS/I_F.SECURITY.TRANS` in `SC_ScoSecurityPositionUpdate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SCT.SECURITY.ACCOUNT` | `SecurityTrans_SecurityAccount` | TField |  | The portfolio effected by the Security movement recorded in the SECURITY.TRANS record. This will either be the portfolio ID, in which case it will be enriched from the SEC.ACC.MASTER record thatdefines the portfolio on T24 or be the depository record in which case it will contain XXXXXX-999, where XXXXXX isthe Customer number of the depository and the suffix 999 defines that this is a depository record. Validation Rules: No input field, automatically updated by the system. |
| 2 | `SC.SCT.SECURITY.NUMBER` | `SecurityTrans_SecurityNumber` | TField |  | The number of the Security that this movement is associated with. This field will contain the ID of the SECURITY.MASTER record that defines the security associated with thesecurity movement that this SECURITY.TRANS record represents. Validation Rules: No input field, automatically updated by the system when the SECURITY.TRANS record is created. |
| 3 | `SC.SCT.DEPOSITORY` | `SecurityTrans_Depository` | TField |  | The Depository to which the Securities will be delivered or from which they will be received. Must be set-up on the CUSTOMER.SECURITY file as a Depository. Validation Rules: No input field, automatically updated by the system when the SECURITY.TRANS record is created. |
| 4 | `SC.SCT.NOMINEE.CODE` | `SecurityTrans_NomineeCode` | TField |  | If the security movement represented by this SECURITY.TRANS record is from/to a position that is held by nomineethen this field will contain the Nominee Code of the the nominee. Will exist on the NOMINEE.CODE file. Validation Rules: No input field automatically updated by the system from the transaction that created the SECURITY.TRANS record. |
| 5 | `SC.SCT.MATURITY.DATE` | `SecurityTrans_MaturityDate` | TField |  | The maturity date of the security. Will be populated from the MATURITY.DATE field on the SECURITY.MASTER record for the security. Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 6 | `SC.SCT.INTEREST.RATE` | `SecurityTrans_InterestRate` | TField |  | The interest rate of the security. Will be populated from the INTEREST.RATE field on the SECURITY.MASTER record for the security. As theINTEREST.RATE field is multi-valued this field will be populated from the interest rate current at the time of thesecurity movement that gave rise to the SECURITY.TRANS record. Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 7 | `SC.SCT.SUB.ACCOUNT` | `SecurityTrans_SubAccount` | TField |  | This field contains the sub-account of the security position updated by this securities transaction. This sub account is defined in CUSTOMER.SECURITY record for this depository. |
| 8 | `SC.SCT.TRADE.DATE` | `SecurityTrans_TradeDate` | TField |  | The Trade Date of the transaction that gave rise to the security movement represented by the SECURITY.TRANSrecord. This is the date of the trade rather than the date the security position is credited or debited with the security- which is the value date. Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 9 | `SC.SCT.REF.NO.SEQUENCE` | `SecurityTrans_RefNoSequence` | TField |  | This is the ID of the T24 transaction that produced the security movement represented by the SECURITY.TRANSrecord. From the suffix of the transaction ID the application can be identified and hence the original transactionenquired upon. The following applications update the SECURITY.TRANS file. They can be identified from the following suffixes ; BDRDSC - REDEMPTION.CUS CAPISC - CAPTL.INCREASE.CUS DIARSC - ENTITLEMENT POSTSC - POSITION.TRANSFER SCTRSC -SEC.TRADE SECTSC - SECURITY.TRANSFER STKDSC - STOCK.DIV.CUS Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 10 | `SC.SCT.ISSUE.DATE` | `SecurityTrans_IssueDate` | TField |  | This Issue Date of the security. Will default from the ISSUE.DATE field on the SECURITY.MASTER record for the security. Validation Rules: No input field automatically updated when the SECURITY.TRANS record is created. |
| 11 | `SC.SCT.VALUE.DATE` | `SecurityTrans_ValueDate` | TField |  | The Value Date of the transaction that gave rise to the security movement represented by the SECURITY.TRANSrecord. This is the date that the transaction is settled and hence the date that the portfolio will pay for or receivemoney for the securities. Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 12 | `SC.SCT.TRANS.TYPE` | `SecurityTrans_TransType` | TField |  | Transaction type Examples: |
| 13 | `SC.SCT.STOCK.EXCHANGE` | `SecurityTrans_StockExchange` | TField |  | Stock Exchange Examples: |
| 14 | `SC.SCT.SECURITY.CURRENCY` | `SecurityTrans_SecurityCurrency` | TField |  | This is the currency of the security. It is the currency in which the security was issued and usually quoted. It will default from the SECURITY.CURRENCY field of the SECURITY.MASTER record for the security in theSECURITY.NUMBER field. Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 15 | `SC.SCT.PRICE.TYPE` | `SecurityTrans_PriceType` | TField |  | The PRICE.TYPE of the security in the SECURITY.NUMBER field of the SECURITY.TRANS record. Must exist on thePRICE.TYPE file. The PRICE.TYPE file contains all the details of how the security price is quoted and the rules on its calculation- for example whether it is quoted as a percentage or not. Validation Rules: No input field automatically updated by the system when the SECURITY.TRANS record is created. |
| 16 | `SC.SCT.TRADE.CURRENCY` | `SecurityTrans_TradeCurrency` | TField |  | Trade currency Examples: |
| 17 | `SC.SCT.NO.NOMINAL` | `SecurityTrans_NoNominal` |  |  |  |
| 18 | `SC.SCT.PRICE` | `SecurityTrans_Price` |  |  |  |
| 19 | `SC.SCT.NO.NOMINAL.TOTAL` | `SecurityTrans_NoNominalTotal` | TField |  | Total nominal amount Examples: |
| 20 | `SC.SCT.GROSS.AMT.SEC.CURR` | `SecurityTrans_GrossAmtSecCurr` | TField |  | Gross amount, security currency Examples: |
| 21 | `SC.SCT.GROSS.AMT.TRD.CURR` | `SecurityTrans_GrossAmtTrdCurr` | TField |  | Gross amount, trade currency Examples: |
| 22 | `SC.SCT.NET.TRADE` | `SecurityTrans_NetTrade` | TField |  | Net trade flag Examples: |
| 23 | `SC.SCT.LAST.PAYMENT.DATE` | `SecurityTrans_LastPaymentDate` | TField |  | Last payment date Examples: |
| 24 | `SC.SCT.INTEREST.DAYS` | `SecurityTrans_InterestDays` | TField |  | Accrued Interest days Examples: |
| 25 | `SC.SCT.INTEREST.AMT` | `SecurityTrans_InterestAmt` | TField |  | Accrued interest amount Examples: |
| 26 | `SC.SCT.BROKER.COMMS` | `SecurityTrans_BrokerComms` | TField |  | Broker commission Examples: |
| 27 | `SC.SCT.STOCK.EXCHNGE.FEES` | `SecurityTrans_StockExchngeFees` | TField |  | Stock exchange fees. Examples: |
| 28 | `SC.SCT.OTHER.FOREIGN.FEES` | `SecurityTrans_OtherForeignFees` | TField |  | Other foreign fees. Examples: |
| 29 | `SC.SCT.COMMISSION` | `SecurityTrans_Commission` | TField |  | Commission Examples: |
| 30 | `SC.SCT.STAMP.TAX` | `SecurityTrans_StampTax` | TField |  | Stamp tax amount Examples: |
| 31 | `SC.SCT.EBV.FEES` | `SecurityTrans_EbvFees` | TField |  | EBV fees. Examples: |
| 32 | `SC.SCT.FEES.MISC` | `SecurityTrans_FeesMisc` | TField |  | Miscellaneous fees Examples: |
| 33 | `SC.SCT.NET.AMT.TRADE` | `SecurityTrans_NetAmtTrade` | TField |  | Net amount trade currency Examples: |
| 34 | `SC.SCT.ACCOUNT.NUMBER` | `SecurityTrans_AccountNumber` | TField |  | Account number Examples: |
| 35 | `SC.SCT.ACCOUNT.CURRENCY` | `SecurityTrans_AccountCurrency` | TField |  | Account currency. Examples: |
| 36 | `SC.SCT.AMOUNT.DUE` | `SecurityTrans_AmountDue` | TField |  | Amount due. Examples: |
| 37 | `SC.SCT.REF.CURRENCY` | `SecurityTrans_RefCurrency` | TField |  | Portfolio reference currency Examples: |
| 38 | `SC.SCT.EXCH.RATE.SEC.BASE` | `SecurityTrans_ExchRateSecBase` | TField |  | Exchange rate local to security currency Examples: |
| 39 | `SC.SCT.EXCH.RATE.TRD.BASE` | `SecurityTrans_ExchRateTrdBase` | TField |  | Exchange rate local to trade currency Examples: |
| 40 | `SC.SCT.EXCH.RATE.BASE.ACC` | `SecurityTrans_ExchRateBaseAcc` | TField |  | Exchange rate local to account currency Examples: |
| 41 | `SC.SCT.EXCH.RATE.BASE.REF` | `SecurityTrans_ExchRateBaseRef` | TField |  | Exchange rate local to portfolio reference currency Examples: |
| 42 | `SC.SCT.MARKET.TYPE` | `SecurityTrans_MarketType` | TField |  | Market type, Normal or Spot Examples: |
| 43 | `SC.SCT.CUST.BROKER.NUMBER` | `SecurityTrans_CustBrokerNumber` | TField |  | Customer/Broker number Examples: |
| 44 | `SC.SCT.BROKER.DEPO` | `SecurityTrans_BrokerDepo` |  |  |  |
| 45 | `SC.SCT.DELIVERY.INSTR` | `SecurityTrans_DeliveryInstr` | TField |  | Delivery instructions. Examples: |
| 46 | `SC.SCT.COST.INVST.SEC.CCY` | `SecurityTrans_CostInvstSecCcy` | TField |  | Cost of investment in security currency. Examples: |
| 47 | `SC.SCT.COST.INVST.REF.CCY` | `SecurityTrans_CostInvstRefCcy` | TField |  | Cost of investment in portfolio reference currency. Examples: |
| 48 | `SC.SCT.COST.INVS.BASE.CCY` | `SecurityTrans_CostInvsBaseCcy` | TField |  | Cost of investment in local currency. Examples: |
| 49 | `SC.SCT.PROF.LOSS.SEC.CCY` | `SecurityTrans_ProfLossSecCcy` | TField |  | Profit or loss, security currency. Examples: |
| 50 | `SC.SCT.PROF.LOSS.BASE.CCY` | `SecurityTrans_ProfLossBaseCcy` | TField |  | Profit or loss, local currency. Examples: |
| 51 | `SC.SCT.RLZ.MRK.GAINS.PORT` | `SecurityTrans_RlzMrkGainsPort` | TField |  | Realsied market gains. Examples: |
| 52 | `SC.SCT.RLZ.CCY.GAINS.PORT` | `SecurityTrans_RlzCcyGainsPort` | TField |  | Realised currency gains Examples: |
| 53 | `SC.SCT.REVERSAL.DATE` | `SecurityTrans_ReversalDate` | TField |  | Reversal date. Examples: |
| 54 | `SC.SCT.OTHER.REV.NUMBERS` | `SecurityTrans_OtherRevNumbers` | TField |  | Examples: |
| 55 | `SC.SCT.EXPIRED.OPTION.FLG` | `SecurityTrans_ExpiredOptionFlg` | TField |  | Expired option flag. Examples: |
| 56 | `SC.SCT.GROSS.COST.SEC.CCY` | `SecurityTrans_GrossCostSecCcy` | TField |  | Gross cost, security currency Examples: |
| 57 | `SC.SCT.GROSS.COST.REF.CCY` | `SecurityTrans_GrossCostRefCcy` | TField |  | Gross cost, portfolio reference currency Examples: |
| 58 | `SC.SCT.GROSS.COST.BSE.CCY` | `SecurityTrans_GrossCostBseCcy` | TField |  | Gross cost, local currency Examples: |
| 59 | `SC.SCT.DATE.UPDATED` | `SecurityTrans_DateUpdated` | TField |  | Date updated. Examples: |
| 60 | `SC.SCT.BROKER.TYPE` | `SecurityTrans_BrokerType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 12 characters may be entered. |
| 61 | `SC.SCT.NARRATIVE` | `SecurityTrans_Narrative` |  |  |  |
| 62 | `SC.SCT.CAP.INT.AMT` | `SecurityTrans_CapIntAmt` | TField |  | This field holds the capitalised interest amount for the trade underlying the record. Validation Rules: No Input Allowed |
| 63 | `SC.SCT.CG.TRADE.TIME` | `SecurityTrans_CgTradeTime` | TField |  | This field indicates the trade date &amp; time recorded for the trade done. It is used in ordering the trades forthe purposes of capital gains calculations. Validation Rules: No Input Allowed |
| 64 | `SC.SCT.CGT.BASE.AMT.CCY` | `SecurityTrans_CgtBaseAmtCcy` | TField |  | This field will contain the currency of the CG base amount on which the CGT was calculated. Validation Rules: No Input Allowed Valid Currency |
| 65 | `SC.SCT.CGT.BASE.AMOUNT` | `SecurityTrans_CgtBaseAmount` | TField |  | This field contains the base amount on which the CGT is calculated. Validation Rules: No Input Allowed |
| 66 | `SC.SCT.CGT.TAX.CODE` | `SecurityTrans_CgtTaxCode` |  |  |  |
| 67 | `SC.SCT.CGT.TAX.RATE` | `SecurityTrans_CgtTaxRate` |  |  |  |
| 68 | `SC.SCT.CGT.TAX.AMT.LCL` | `SecurityTrans_CgtTaxAmtLcl` |  |  |  |
| 69 | `SC.SCT.CGT.TAX.AMOUNT` | `SecurityTrans_CgtTaxAmount` |  |  |  |
| 70 | `SC.SCT.CGT.PARAM.COND` | `SecurityTrans_CgtParamCond` | TField |  | The condition id allocated to this transaction relating to application CG.PARAM.CONDITION. This will determinethe Capital Gains method and tax to be applied. |
| 71 | `SC.SCT.CGT.SRC.LCL.TAX` | `SecurityTrans_CgtSrcLclTax` | TField |  | This indicates whether the tax is to be deducted by the bank (LOCAL) or the depositor (SOURCE). Validation Rules: Either SOURCE or LOCAL. |
| 72 | `SC.SCT.ODD.RTS.CGT` | `SecurityTrans_OddRtsCgt` | TField |  | Field indicating whether the transaction is for rounding of rights relating to a corporate action. This flag isdetermined by the system. Validation Rules: Y or blank |
| 73 | `SC.SCT.BOOK.COST.SEC.CCY` | `SecurityTrans_BookCostSecCcy` | TField |  | This field contains the net cost of the transaction in security currency. Validation Rules: No input, system generated field |
| 74 | `SC.SCT.BOOK.COST.REF.CCY` | `SecurityTrans_BookCostRefCcy` | TField |  | This field will contain the net cost of the security transaction in the reference currency of the underlyingportfolio. Validation Rules: None, system generated field |
| 75 | `SC.SCT.BOOK.COST.BSE.CCY` | `SecurityTrans_BookCostBseCcy` | TField |  | This field contains the net cost of the security transaction in the local currency. Validation Rules: No input, system generated field |
| 76 | `SC.SCT.GR.BK.COST.SEC.CCY` | `SecurityTrans_GrBkCostSecCcy` | TField |  | This field contains the gross cost of the security transaction in the security currency. Validation Rules: No input, system generated field |
| 77 | `SC.SCT.GR.BK.COST.REF.CCY` | `SecurityTrans_GrBkCostRefCcy` | TField |  | This field contains the gross cost of the transaction in portfolio reference currency. Validation Rules: No input, system generated field |
| 78 | `SC.SCT.GR.BK.COST.BSE.CCY` | `SecurityTrans_GrBkCostBseCcy` | TField |  | This field will contain the gross cost of the security transaction in local currency Validation Rules: No input, system generated field |
| 79 | `SC.SCT.PROF.LOSS.SREF.CCY` | `SecurityTrans_ProfLossSrefCcy` | TField |  | This field will contain the realised profit/loss, if any, in the portfolio reference currency as measured againstthe average cost of the security position. Any amount reported here in respect of depository positions (suffixed "-999") should be ignored. Validation Rules: No input, system generated field |
| 80 | `SC.SCT.UNSETTLED.NOMINAL` | `SecurityTrans_UnsettledNominal` | TField |  | The nominal of securities relating to this transaction that remain unsettled. Validation Rules: None, system generated field. |
| 81 | `SC.SCT.ADJUST.NOM` | `SecurityTrans_AdjustNom` | TField |  | New field containing the adjustment nominal. Validation Rules: |
| 82 | `SC.SCT.ODD.LOT.NOMINAL` | `SecurityTrans_OddLotNominal` | TField |  | This field is automatically updated if the ODD.LOT.CONSOLID field in CUSTOMER.SECURITY is set to NO and : - - - Validation Rules: |
| 83 | `SC.SCT.BROKER` | `SecurityTrans_Broker` |  |  |  |
| 84 | `SC.SCT.UNSETT.NOM.CR` | `SecurityTrans_UnsettNomCr` |  |  |  |
| 85 | `SC.SCT.SETT.REV.DT` | `SecurityTrans_SettRevDt` |  |  |  |
| 86 | `SC.SCT.SETT.NOM` | `SecurityTrans_SettNom` |  |  |  |
| 87 | `SC.SCT.REV.NOM` | `SecurityTrans_RevNom` |  |  |  |
| 88 | `SC.SCT.UNSETT.NOM` | `SecurityTrans_UnsettNom` |  |  |  |
| 89 | `SC.SCT.CUM.EX.IND` | `SecurityTrans_CumExInd` |  |  |  |
| 90 | `SC.SCT.CONTRA.TRANS` | `SecurityTrans_ContraTrans` | TField |  | Transaction contra'd by this transaction. |
| 91 | `SC.SCT.WHT.TAX` | `SecurityTrans_WhtTax` |  |  |  |
| 92 | `SC.SCT.SEGMENT` | `SecurityTrans_Segment` | TField |  | Segment, linked to dealer desks. |
| 93 | `SC.SCT.DEF.DEAL.DESK` | `SecurityTrans_DefDealDesk` | TField |  | Default dealer desk allocated to this transaction. |
| 94 | `SC.SCT.ACT.DEAL.DESK` | `SecurityTrans_ActDealDesk` | TField |  | Actual dealer desk that actioned the transaction. |
| 95 | `SC.SCT.PARENT.TXN.ID` | `SecurityTrans_ParentTxnId` | TField |  | This field is used to capture the contract id of the parent transaction that created the child securitytransaction. This will be the Id of the parent application that then called the Composite Module Manager (CMM) tocreate the child security contract. Validation Rules: System populated field. |
| 96 | `SC.SCT.SBL.DIV.RATE` | `SecurityTrans_SblDivRate` | TField |  | The field will hold the rate at which the Stock Borrow/ Lend transaction takes place. |
| 97 | `SC.SCT.CU.TAX.CODE` | `SecurityTrans_CuTaxCode` |  |  |  |
| 98 | `SC.SCT.CU.TAX.TYPE` | `SecurityTrans_CuTaxType` |  |  |  |
| 99 | `SC.SCT.CU.TAX.TCY` | `SecurityTrans_CuTaxTcy` |  |  |  |
| 100 | `SC.SCT.CU.TAX.LCY` | `SecurityTrans_CuTaxLcy` |  |  |  |
| 101 | `SC.SCT.INT.CTR` | `SecurityTrans_IntCtr` | TField |  | Interest counter |
| 102 | `SC.SCT.TRFR.EFF.DATE` | `SecurityTrans_TrfrEffDate` | TField |  | Effective date of transfer. |
| 103 | `SC.SCT.MAN.TAX.TCY` | `SecurityTrans_ManTaxTcy` |  |  |  |
| 104 | `SC.SCT.MAN.TAX.LCY` | `SecurityTrans_ManTaxLcy` |  |  |  |
| 105 | `SC.SCT.EXT.CUSTODIAN` | `SecurityTrans_ExtCustodian` | TField |  | To identify the external custodian where position is held.. |
| 106 | `SC.SCT.MARGIN.FACTOR` | `SecurityTrans_MarginFactor` | TField |  | This field used in the calculation of consideration using the Columbian Yield Method. |
| 107 | `SC.SCT.INV.INT.CTR` | `SecurityTrans_InvIntCtr` | TField |  | This field will hold the interest counter value arising from each transaction. Calculation will be performed inthe same way it is performed for cost invested fields in SECURITY.TRANS and SECURITY.POSITION. |
| 108 | `SC.SCT.PARENT` | `SecurityTrans_Parent` | TField |  | Allowed value is YES This field is to determine whether the order is a parent order |
| 109 | `SC.SCT.PARENT.REFERENCE` | `SecurityTrans_ParentReference` | TField |  | This field will accept alphanumeric Value Unique parent reference that is common for both parent and child orders and will serve as a link. |
| 110 | `SC.SCT.CHARGE.TAX.TYPE` | `SecurityTrans_ChargeTaxType` |  |  |  |
| 111 | `SC.SCT.CHARGE.TAX.AMT` | `SecurityTrans_ChargeTaxAmt` |  |  |  |
| 112 | `SC.SCT.CANCEL.BY.DATE` | `SecurityTrans_CancelByDate` | TField |  | Trade is allowed for cancellation until the date defined in this field. Field will be calculated based on cooling off period defined at SECURITY.MASTER for 1.Initial purchase for the portfolio in the instrument 2.Subsequent purchase for the same instrument by that portfolio and is within the Cancel by date of the initialpurchase. Field will be mapped from SEC.TRADE for Customer Transaction. No input, system generated field |
| 113 | `SC.SCT.TAXLOT.ALLOCATE` | `SecurityTrans_TaxlotAllocate` |  |  |  |
| 114 | `SC.SCT.QTY.ALLOTED` | `SecurityTrans_QtyAlloted` |  |  |  |
| 115 | `SC.SCT.CG.EXEMPT` | `SecurityTrans_CgExempt` | TField |  |  |
| 116 | `SC.SCT.CG.TAX.EFF.DATE` | `SecurityTrans_CgTaxEffDate` | TField |  |  |
| 117 | `SC.SCT.STAPLED.SECURITY` | `SecurityTrans_StapledSecurity` | TField |  | This field will denote if the security is parent stapled or Child component security This field will hold either PARENT or CHILD or blank |
| 118 | `SC.SCT.STAPLED.COMPONENT.ID` | `SecurityTrans_StapledComponentId` | TField |  | This field holds the id of SC.STAPLED.COMPONENT record and the value split corresponding to the security used inthis transaction.The value split percentage was used to derive the cost of the child security from the cost of thestaple security Format : StapledComponentId*ValueSplit |
| 119 | `SC.SCT.CG.EX.RATE.SETT` | `SecurityTrans_CgExRateSett` | TField |  |  |
| 120 | `SC.SCT.CG.EX.RATE.TRADE` | `SecurityTrans_CgExRateTrade` | TField |  |  |
| 121 | `SC.SCT.CU.TAX.EFF.DATE` | `SecurityTrans_CuTaxEffDate` |  |  |  |
| 122 | `SC.SCT.SALE.SAFE.FEES` | `SecurityTrans_SaleSafeFees` | TField |  |  |
