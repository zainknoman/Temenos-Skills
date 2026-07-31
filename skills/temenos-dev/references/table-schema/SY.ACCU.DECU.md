# SY.ACCU.DECU — Table Schema

> Source: `INSERTS/I_F.SY.ACCU.DECU` in `DP_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.ADC.PRODUCT.TYPE` | `SyAccuDecu_ProductType` | TField |  | This field accepts the below values : ACCMULATOR - Indicates this is an accumulator contract- the underlying security is accumulated or purchased at periodic intervals. DECUMULATOR - Indicates this is an decumulator contract - the underlying security is decumulated/sold at periodic intervals. |
| 2 | `SY.ADC.VARIANT` | `SyAccuDecu_Variant` | TField |  | Product variants can be defined and configured in the SY.PRODUCT.VARIANT application. Linking the product variant in this field will ensure that the corresponding parameters and configuration would be applied to this contract. If this field is NULL, the parameters defined in SY.PRODUCT.DEFINTION for ACCUDECU would be applied. No change field if SUPPRESS.UNDERLYING is set to 'No'. Validation Rules: Only variants with prefix as 'ACCUDECU_' will be accepted. |
| 3 | `SY.ADC.DESCRIPTION` | `SyAccuDecu_Description` |  |  |  |
| 4 | `SY.ADC.CONTRACT.STATUS` | `SyAccuDecu_ContractStatus` | TField |  | The status of the contract is updated in this field. When the contract is created , the status will be 'ACTIVE', subsequently as the contract undergoes various life cycle events, the status is updated as below. ACTIVE - The contract is active. MATURED - The contract is matured. i.e. the contract has completed its full life cycle. KNOCKOUT - The contract is knocked out, i.e. the knock out barrier price is breached. UNWOUND - The contract is terminated early - before the maturity date. NOVATED - The contract is novated, i.e the position is transfered and the contract is terminated. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 5 | `SY.ADC.CONTRACT.IDENTIFIER` | `SyAccuDecu_ContractIdentifier` | TField |  | AD VALOREN number assigned to this contract can be updated in this field. |
| 6 | `SY.ADC.PRINCIPAL.AGENT` | `SyAccuDecu_PrincipalAgent` | TField |  | This field accepts the following values : PRINCIPAL - Indicates that the bank is acting as a principal in this transaction. AGENT - Indicates that the bank is acting as an agent in this transaction. Bank's role in the SY contract is recorded here |
| 7 | `SY.ADC.COUNTERPARTY.TRADE` | `SyAccuDecu_CounterpartyTrade` | TField |  | An Accumulator/Decumulator contract is generally booked as two separate transaction legs. Customer transacts with the bank (Dealer book) - the bank covers or hedges this position by a market side transaction. Setting this field to 'Yes' indicates that this is a market side transaction. This field is used for reporting purposes. |
| 8 | `SY.ADC.OPTION.TYPE` | `SyAccuDecu_OptionType` | TField |  | This field holds the option type of the underlying option. This is auto populated based on the PRODUCT.TYPE field. For ACCUMULATOR contract - the underlying would be a PUT option, for DECUMULATOR contract- the underlying would be a CALL option. |
| 9 | `SY.ADC.TRADE.DATE` | `SyAccuDecu_TradeDate` | TField |  | Holds the trade date of the contract. Trade date cannot be forward dated and should fall between the FIRST.DATE and LAST.DATE of the corresponding product definition record. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 10 | `SY.ADC.VALUE.DATE` | `SyAccuDecu_ValueDate` | TField |  | Date on which the accrual of shares commences. Defaults from the trade date if not input. Value date cannot be earlier than the trade date. Accrual will start from value date of the contract, if knock in price is not given. If knock in price is given then accrual will start from the day on which KNOCK.IN is set. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 11 | `SY.ADC.TERM` | `SyAccuDecu_Term` | TField |  | This field holds the tenor of the contract. The Tenor can be expressed as a number of Days, Weeks or Months. Input in this field has to be in the format nnnD, nnnM or nnnW where nnn is represents the numeric component. D signifies Days (working days) ,M signifies Months and W signifies Weeks |
| 12 | `SY.ADC.MATURITY.DATE` | `SyAccuDecu_MaturityDate` | TField |  | Maturity date is the termination date of the contract. Maturity date will be defaulted based on TERM and VALUE.DATE |
| 13 | `SY.ADC.SECURITY.CODE` | `SyAccuDecu_SecurityCode` | TField |  | The underlying security which is accumulated/decumulated in this contract is captured in this field. Units of this security would be accrued and settled periodically. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 14 | `SY.ADC.STOCK.EXCHANGE` | `SyAccuDecu_StockExchange` | TField |  | The STOCK.EXCHANGE in which the security is traded will be defaulted here. |
| 15 | `SY.ADC.DX.CONTRACT.CODE` | `SyAccuDecu_DxContractCode` | TField |  | As a prerequisite to transact in Accumulator/Decumulator, a DX.CONTRACT.MASTER needs to be set up. The underlying for this contract will be the instrument (From SECURITY.CODE field). The contract master id is captured in this field. When the accumulator/Decumulator contract is committed, an DX.TRADE (PUT option for Accumulator, CALL option for decumulator) would be created for this contract. No change field if SUPPRESS.UNDERLYING is set to 'No'. Validation Rules: This field will accept a DX.CONTRACT.MASTER which has security as the only underlying. This contract should be of type 'Option' and should be set up as a daily maturity contract. |
| 16 | `SY.ADC.CONTRACT.CCY` | `SyAccuDecu_ContractCcy` | TField |  | Contract currency is captured in this field. The Security currency of underlying would be defaulted if this field is left blank. |
| 17 | `SY.ADC.REFERENCE.PRICE` | `SyAccuDecu_ReferencePrice` | TField |  | The spot price of the underlying security (at the time of contract booking) is updated in this field. If left blank, the last price from the underlying security would default. |
| 18 | `SY.ADC.STRIKE.PRICE1` | `SyAccuDecu_StrikePrice1` | TField |  | The forward price at which the accumulation (purchases) or decumulation (sale) of the underlying would be effected is captured in this field. i.e. this would be the price used for the security settlement. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 19 | `SY.ADC.STRIKE.PRICE2` | `SyAccuDecu_StrikePrice2` | TField |  | For contracts with dual strike prices, the second strike price can be updated in this field. This field is used for information purposes. |
| 20 | `SY.ADC.KNOCKIN.PRICE` | `SyAccuDecu_KnockinPrice` | TField |  | This field will allow the user the store the price barrier for knock in. Only when this price barrier is breached, the contract becomes effective.If this field is populated, then accrual would commence only when KNOCK.IN flag is set. Price tracking is outside the system, when the Knock in barrier is breached, this is indicated by setting the KNOCK.IN flag. |
| 21 | `SY.ADC.KNOCKOUT.PRICE` | `SyAccuDecu_KnockoutPrice` | TField |  | This field will allow the user to store the price barrier for knock out. When this price barrier is breached, the contract gets terminated. Price tracking is outside the system, when the Knock out barrier is breached, this is indicated by setting the KNOCK.OUT flag. |
| 22 | `SY.ADC.DAILY.UNITS` | `SyAccuDecu_DailyUnits` | TField |  | This field will hold the number of units(nominal) to be accrued per day. The value should be in multiple of contract size of the underlying DX.CONTRACT.MASTER. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 23 | `SY.ADC.GEARING` | `SyAccuDecu_Gearing` | TField |  | The leverage (gearing) factor for leveraged contracts is captured in this field. The gearing factor would be applied to accruals on those days where the spot price is below STRIKE.PRICE1 for accumulators , spot price is above the STRIKE.PRICE1 for decumulator contracts. For example, if the gearing factor is 2 , and the spot price of the underlying is less than the STRIKE.PRICE1 for an accumulator contract on a particular day, then accrual for that day would be 2 times the quantity specified in DAILY.UNITS. |
| 24 | `SY.ADC.SUPPRESS.UNDERLYING` | `SyAccuDecu_SuppressUnderlying` | TField |  | If this field is set to 'Yes', system will not create the underlying transactions when the contract is committed. It is expected that the underlying transactions will be created manually or interfaced from a different system and the contract can be linked to ACCUDECU using SY.DX.REFERENCE. For such contracts, lifecycle events of the contract such as accrual, fixing etc. should be managed externally (Manually or interfaced from an external system). If this field is set to 'No', underlying transactions will be created by the system. The lifecycle events of the contract will be processed by the system. This field will be defaulted from SY.PRODUCT.VARIANT. If SY.PRODUCT.VARIANT is not defined, then the value will be defaulted from SY.PRODUCT.DEFINITION. The following fields would be "No Change" if SUPPRESS.UNDERLYING field is set to 'No' VARIANT TRADEDATE VALUEDATE DXCONTRACTCODE STRIKEPRICE1 CUSTOMER PORTFOLIO CUSTOMERACCOUNT COUNTERPARTY CPARTYPORTFOLIO COUNTERPARTYACC CONTRACTSTATUS DAILYUNITS |
| 25 | `SY.ADC.MIN.ACCRUAL.PERIOD` | `SyAccuDecu_MinAccrualPeriod` | TField |  | This field is applicable for contracts with guaranteed accumulation/Decumulation. For such contracts, even if the contract gets knocked out early in its lifecycle, the investor is guaranteed settlement of certain units of the underlying. For example, for an accumulator contract with 12 fixing periods, the accumulation for the first 2 periods could be guaranteed. Even if the contract gets knocked out in the first fixing period, the investor still purchases shares for the first 2 fixing period. This field holds the number of guaranteed fixing periods applicable for this contract. In this example, this field will hold the value 2. |
| 26 | `SY.ADC.PROTECTED.DATE` | `SyAccuDecu_ProtectedDate` | TField |  | This field will be populated with the last date of the MIN.ACCRUAL.PERIOD. For example, if the MIN.ACCRUAL.PERIOD is 2, this field would default to the last day of the second fixing period. |
| 27 | `SY.ADC.MIN.PERIOD.KOUT` | `SyAccuDecu_MinPeriodKout` | TField |  | This field will be defaulted from SY.PRODUCT.VARIANT. If SY.PRODUCT.VARIANT is not given, then the value will be defaulted from SY.PRODUCT.DEFINITION, this field can also be amended manually. If this field is set to YES, then the contract will be knocked out immediately with nominal for the entire minimum accrual period. If this field is null or set to NO and the contract gets knocked out within the MIN.ACCRUAL.PERIOD, then accrual would continue unto the PROTECTED.DATE and the guaranteed units of shares will be settled at that point of time. |
| 28 | `SY.ADC.TOT.WORK.DAYS` | `SyAccuDecu_TotWorkDays` | TField |  | The total number of working days(using the holiday calendar of STOCK.EXCHANGE) between value date and maturity date is calculated and stored in this field. If the contract does not gets knocked out, the accrual would happen for these many days. |
| 29 | `SY.ADC.TOTAL.UNITS` | `SyAccuDecu_TotalUnits` | TField |  | This field will hold the maximum number of underlying security that could be settled/delivered by this contract. The value will be calculated based on the following formula DAILY.UNITS * TOT.WORK.DAYS * GEARING. The underlying option would be created for these many units. |
| 30 | `SY.ADC.CUSTOMER` | `SyAccuDecu_Customer` | TField |  | This field records the investor for this contract. For the client trade, this would be the customer, for the counterparty trade, this would be the DEALER.BOOK. The customer should be defined in both CUSTOMER.SECURITY and DX.CUSTOMER. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 31 | `SY.ADC.PORTFOLIO` | `SyAccuDecu_Portfolio` | TField |  | This field will hold the portfolio of the customer for this contract. When left blank, the first portfolio of the CUSTOMER will be defaulted. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 32 | `SY.ADC.CUSTOMER.ACCOUNT` | `SyAccuDecu_CustomerAccount` | TField |  | This account will be used to post the accounting entries for the customer. The same account will be also be the default account on the underlying trade created by the system. The field will be defaulted to the Account specified on the Customer's SEC ACC MASTER record, for the CONTRACT CCY or (if no Account in the CONTRACT CCY is specified) to the Customer's first Account on the SEC ACC MASTER record. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 33 | `SY.ADC.SECURITY.POS` | `SyAccuDecu_SecurityPos` |  |  |  |
| 34 | `SY.ADC.BLOCK.NOMINAL` | `SyAccuDecu_BlockNominal` |  |  |  |
| 35 | `SY.ADC.BLOCK.UNTIL.SC` | `SyAccuDecu_BlockUntilSc` |  |  |  |
| 36 | `SY.ADC.BLOCK.REF.SC` | `SyAccuDecu_BlockRefSc` |  |  |  |
| 37 | `SY.ADC.UNBLK.NOM.PEND` | `SyAccuDecu_UnblkNomPend` |  |  |  |
| 38 | `SY.ADC.RESERVED.44` | `SyAccuDecu_Reserved44` | TField |  |  |
| 39 | `SY.ADC.BLOCK.FUNDS` | `SyAccuDecu_BlockFunds` | TField |  | For accumulator contracts, where there is a forward dated obligation to purchase the underlying security at periodic intervals, a cash block might be required to ensure availability of sufficient funds. The funds can be blocked by placing a cash block in the account or by moving the funds to a different account. This field will be used indicate the preferred action. If it is set to BLOCK then the value in BLOCK.AMOUNT will be blocked by creating a record in AC.LOCKED.EVENTS or if the field is set to DEBIT, then entries will be raised to debit the BLOCK.AMOUNT from BLOCK.ACCOUNT and to credit it to CREDIT.ACCOUNT. If the field is set to null neither blocking nor debiting happens. Once the AC.LOCKED.EVENT ID is generated in BLOCK.REF.AC, fields from BLOCK.FUNDS to BLOCK.REF.AC cannot be amended. |
| 40 | `SY.ADC.BLOCK.AMOUNT` | `SyAccuDecu_BlockAmount` | TField |  | This field total amount of cash that needs to be blocked. |
| 41 | `SY.ADC.BLOCK.ACCOUNT` | `SyAccuDecu_BlockAccount` | TField |  | This field will hold the funding account which would be used to effect the block. |
| 42 | `SY.ADC.CREDIT.ACCOUNT` | `SyAccuDecu_CreditAccount` | TField |  | If the funds are to be moved to a separate account, this account is specified here. |
| 43 | `SY.ADC.BLOCK.UNTIL.AC` | `SyAccuDecu_BlockUntilAc` | TField |  | This field will hold the end date of the cash block. |
| 44 | `SY.ADC.BLOCKED.REF.AC` | `SyAccuDecu_BlockedRefAc` | TField |  | If BLOCK option is chosen in BLOCK.FUNDS, this field will store the ID of AC.LOCKED.EVENTS generated. |
| 45 | `SY.ADC.RESERVED.43` | `SyAccuDecu_Reserved43` | TField |  |  |
| 46 | `SY.ADC.RESERVED.42` | `SyAccuDecu_Reserved42` | TField |  |  |
| 47 | `SY.ADC.COUNTERPARTY` | `SyAccuDecu_Counterparty` | TField |  | The counterparty for the contract is updated in this field. In the client trade, COUNTERPARTY would be the dealer book in the client transaction and it would be the external counterparty for the back to back or counterparty trade. The counterparty should be defined in both CUSTOMER.SECURITY and DX.CUSTOMER. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 48 | `SY.ADC.CPARTY.PORTFOLIO` | `SyAccuDecu_CpartyPortfolio` | TField |  | This field will hold the portfolio of the counterparty. If portfolio exist for the counterparty, then this field will be defaulted with the first portfolio of the counterparty. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 49 | `SY.ADC.COUNTERPARTY.ACC` | `SyAccuDecu_CounterpartyAcc` | TField |  | Defaults the Account over which financial entries relating to the counterparty will be posted. No change field if SUPPRESS.UNDERLYING is set to 'No'. |
| 50 | `SY.ADC.PREMIUM.CCY` | `SyAccuDecu_PremiumCcy` | TField |  | This field will hold the currency in which premium is specified. Default would be CONTRACT.CCY |
| 51 | `SY.ADC.PREMIUM.PER.LOT` | `SyAccuDecu_PremiumPerLot` | TField |  | This field hold the premium per unit of underlying. Premium amount is calculated using the formula TOTAL.UNITS * PREMIUM.PER.LOT |
| 52 | `SY.ADC.PREMIUM.AMT` | `SyAccuDecu_PremiumAmt` | TField |  | This will be the total premium amount that will be collected from the customer for the entire lot. |
| 53 | `SY.ADC.NOTIONAL.AMT` | `SyAccuDecu_NotionalAmt` | TField |  | This field will hold the notional amount for contract. This would be calculated using the formula TOTAL.UNITS * STRIKE.PRICE1. Notional amount is denoted in the contract currency. Off Balance sheet, contingent entries would be posted for this amount. This can be input by the user which would override the calculation done by the system. |
| 54 | `SY.ADC.RUN.NOTIONAL.AMT` | `SyAccuDecu_RunNotionalAmt` | TField |  | As the contract is settled periodically (which is known as FIXING), the pending units are reduced. The outstanding notional (i.e. unsettled) also gets reduced proportionately. The outstanding notional is updated by the system at each fixing. |
| 55 | `SY.ADC.SETTLEMENT.METHOD` | `SyAccuDecu_SettlementMethod` | TField |  | This field will indicate how the delivery of the underlying will happen. For dealer book transaction, this field will be defaulted from DX.CONTRACT.MASTER. This can also be changed manually. Allowed values are PHYSICAL, CASH. CASH - During the Fixing event, SETTLEMENT.AMOUNT will be settled in DELIVERY.CCY PHYSICAL - If SETTLEMENT.INSTRUMENT is defined, then SETTLEMENT.INSTRUMENT will be exercised for the SETTL.INSTR.UNITS at SETT.INSTR.PRICE If SETTLEMENT.INSTRUMENT is not given, then security given in SECURITY.CODE will be exercised for the ACCRUED.UNITS1 at STRIKE.PRICE1. |
| 56 | `SY.ADC.ALTERNATE.REF` | `SyAccuDecu_AlternateRef` | TField |  | This field can be used to store an alternate reference for the contract. This would be especially useful, when the contract is sourced from an external system. The external system reference can be updated here. |
| 57 | `SY.ADC.SY.DX.REFERENCE` | `SyAccuDecu_SyDxReference` | TField |  | This is the unique reference that will bind the structure (ACCUDECU contract) with all its underlying transactions. For example, when an accumulator contract is created, the underlying option is created through DX.TRADE. As the contract gets fixed (periodic settlement), the settlement happens through a SEC.TRADE transaction. All three transactions , SY.ACCU.DECU contract, DX.TRADE and SEC.TRADE will be updated with this reference. This reference can be input by user, if left blank, the contract id would be populated |
| 58 | `SY.ADC.B2B.REFERENCE` | `SyAccuDecu_B2bReference` | TField |  | Accumulator/Decumulator contracts are booked as two transactions. The Client transacts with the bank (dealer book). The bank then covers or hedges this position by entering into a back to back transaction with the counterparty. The reference of the back to back transaction can be stored in this field. |
| 59 | `SY.ADC.UNDERLYING.REF` | `SyAccuDecu_UnderlyingRef` | TField |  | This field will hold the reference of the underlying contract (DX.TRADE ID). |
| 60 | `SY.ADC.SETTLE.INSTRUMENT` | `SyAccuDecu_SettleInstrument` | TField |  |  |
| 61 | `SY.ADC.DELIVERY.CURRENCY` | `SyAccuDecu_DeliveryCurrency` | TField |  | This defaults from the DX.CONTRACT.MASTER only for dealer book transaction. For contracts with SETTLEMENT.METHOD = 'Cash', settlement would take place in this currency. |
| 62 | `SY.ADC.KNOCK.IN` | `SyAccuDecu_KnockIn` | TField |  | This field is applicable for contracts with knock in feature. The contract becomes effective only when the knock in price barrier is breached. Price tracking is done outside the system, occurrence of knock in event (i.e. breach of knock in price) is indicated to the system by setting this flag to 'Yes'. Accrual would commence only when this flag is set to 'Yes' for a knock in contract |
| 63 | `SY.ADC.PRICE.AT.KNOCK.IN` | `SyAccuDecu_PriceAtKnockIn` | TField |  | This is the price of the underlying security at the time of occurrence of the Knock in event. i.e. This is the price which has breached the knock in price barrier. This is stored for information purposes. |
| 64 | `SY.ADC.KNOCK.OUT` | `SyAccuDecu_KnockOut` | TField |  | The contract gets terminated when the Knock out price barrier is breached. Price tracking is done outside the system, occurrence of the knockout event is indicated to the system by setting this flag to 'Yes'. |
| 65 | `SY.ADC.PRICE.AT.KNOCK.OUT` | `SyAccuDecu_PriceAtKnockOut` | TField |  | This is the price of the underlying security at the time of occurrence of the knock out event. This is stored for information purposes. |
| 66 | `SY.ADC.UNWIND` | `SyAccuDecu_Unwind` |  |  |  |
| 67 | `SY.ADC.UNWIND.CHG.CCY` | `SyAccuDecu_UnwindChgCcy` |  |  |  |
| 68 | `SY.ADC.UNWIND.CHG.AMT` | `SyAccuDecu_UnwindChgAmt` |  |  |  |
| 69 | `SY.ADC.UNWIND.CHG.ACC` | `SyAccuDecu_UnwindChgAcc` |  |  |  |
| 70 | `SY.ADC.UNWIND.SPREAD` | `SyAccuDecu_UnwindSpread` |  |  |  |
| 71 | `SY.ADC.UNWIND.TOT.CHARGE` | `SyAccuDecu_UnwindTotCharge` |  |  |  |
| 72 | `SY.ADC.UNWIND.EFF.DATE` | `SyAccuDecu_UnwindEffDate` |  |  |  |
| 73 | `SY.ADC.UNWIND.STATUS` | `SyAccuDecu_UnwindStatus` |  |  |  |
| 74 | `SY.ADC.NEW.DAILY.UNITS` | `SyAccuDecu_NewDailyUnits` |  |  |  |
| 75 | `SY.ADC.NEW.TOTAL.UNITS` | `SyAccuDecu_NewTotalUnits` |  |  |  |
| 76 | `SY.ADC.CPTY.UNWIND.CHG.AMT` | `SyAccuDecu_CptyUnwindChgAmt` |  |  |  |
| 77 | `SY.ADC.UNWIND.RESERVED.3` | `SyAccuDecu_UnwindReserved3` | TField |  |  |
| 78 | `SY.ADC.UNWIND.RESERVED.2` | `SyAccuDecu_UnwindReserved2` | TField |  |  |
| 79 | `SY.ADC.UNWIND.RESERVED.1` | `SyAccuDecu_UnwindReserved1` | TField |  |  |
| 80 | `SY.ADC.SUSPEND.ACCRUAL` | `SyAccuDecu_SuspendAccrual` | TField |  | Trading in the underlying security can be suspended due to various reasons. Trading can be suspended as a result of a Corporate Action. In such situations, the accrual for the accumulator /decumulator contract also needs to be suspended. This is indicated to the system by setting this field to 'Yes'. Once set, accrual and fixing would be suspended between SUSPENSION.DATE and SUSP.RESET.DATE. |
| 81 | `SY.ADC.SUSPENSION.DATE` | `SyAccuDecu_SuspensionDate` | TField |  | Accrual/Fixing suspension start date. |
| 82 | `SY.ADC.SUSP.RESET.DATE` | `SyAccuDecu_SuspResetDate` | TField |  | Accrual/Fixing suspension end date. |
| 83 | `SY.ADC.FIX.SUSPENSION` | `SyAccuDecu_FixSuspension` | TField |  | When this field is set to YES, if the fixing periods falls in the suspension period then all the nominal accrued until the SUSP.RESET.DATE will be fixed on SUSP.RESET.DATE. If this field is NO or Null then all the accrued units until the last suspended fixing period will be done on SUSP.RESET.DATE and the remaining accrued units will be added to the next fixing period. |
| 84 | `SY.ADC.FIXING.FREQUENCY` | `SyAccuDecu_FixingFrequency` | TField |  | Accumulator/Decumulator contracts accrue the underlying security on a daily basis. The accrued units are settled periodically (This periodic settlement is known as fixing). This settlement frequency is captured in this field. Settlement of shares is effected by a SEC.TRADE transaction. |
| 85 | `SY.ADC.FIXING.DATE` | `SyAccuDecu_FixingDate` |  |  |  |
| 86 | `SY.ADC.WORKING.DAYS` | `SyAccuDecu_WorkingDays` |  |  |  |
| 87 | `SY.ADC.SETTLEMENT.DATE` | `SyAccuDecu_SettlementDate` |  |  |  |
| 88 | `SY.ADC.ACCRUED.UNITS1` | `SyAccuDecu_AccruedUnits1` |  |  |  |
| 89 | `SY.ADC.ACCRUED.UNITS2` | `SyAccuDecu_AccruedUnits2` |  |  |  |
| 90 | `SY.ADC.FIXED.STATUS` | `SyAccuDecu_FixedStatus` |  |  |  |
| 91 | `SY.ADC.SETT.INSTR.UNITS` | `SyAccuDecu_SettInstrUnits` |  |  |  |
| 92 | `SY.ADC.SETT.INSTR.PRICE` | `SyAccuDecu_SettInstrPrice` |  |  |  |
| 93 | `SY.ADC.MARKET.PRICE` | `SyAccuDecu_MarketPrice` |  |  |  |
| 94 | `SY.ADC.DLV.EXCH.RATE` | `SyAccuDecu_DlvExchRate` |  |  |  |
| 95 | `SY.ADC.SETTLEMENT.AMOUNT` | `SyAccuDecu_SettlementAmount` |  |  |  |
| 96 | `SY.ADC.CPTY.SETT.AMOUNT` | `SyAccuDecu_CptySettAmount` |  |  |  |
| 97 | `SY.ADC.RESERVED.32` | `SyAccuDecu_Reserved32` | TField |  |  |
| 98 | `SY.ADC.RESERVED.31` | `SyAccuDecu_Reserved31` | TField |  |  |
| 99 | `SY.ADC.RESERVED.30` | `SyAccuDecu_Reserved30` | TField |  |  |
| 100 | `SY.ADC.RESERVED.29` | `SyAccuDecu_Reserved29` | TField |  |  |
| 101 | `SY.ADC.RESERVED.28` | `SyAccuDecu_Reserved28` | TField |  |  |
| 102 | `SY.ADC.RESERVED.27` | `SyAccuDecu_Reserved27` | TField |  |  |
| 103 | `SY.ADC.RESERVED.26` | `SyAccuDecu_Reserved26` | TField |  |  |
| 104 | `SY.ADC.RESERVED.25` | `SyAccuDecu_Reserved25` | TField |  |  |
| 105 | `SY.ADC.RESERVED.24` | `SyAccuDecu_Reserved24` | TField |  |  |
| 106 | `SY.ADC.ACCRUED.UNTIL` | `SyAccuDecu_AccruedUntil` | TField |  | This field will hold the date untill which the nominal is accrued. |
| 107 | `SY.ADC.TRANS.REFERENCE` | `SyAccuDecu_TransReference` | TField |  | This field will hold SY.TRANSACTION ID. |
| 108 | `SY.ADC.FEE.CCY` | `SyAccuDecu_FeeCcy` | TField |  | The field will hold currency in which the fees will be collected |
| 109 | `SY.ADC.FEE.AMT` | `SyAccuDecu_FeeAmt` | TField |  | The field will hold the Fee amount |
| 110 | `SY.ADC.FEE.ACCT` | `SyAccuDecu_FeeAcct` | TField |  | The field will hold the Account from which the fees will be debited. |
| 111 | `SY.ADC.CPTY.FEE.AMT` | `SyAccuDecu_CptyFeeAmt` | TField |  | This field will store the fee amount credited to counterparty. Fee amount entered in existing field FEE.AMT will be debited from customer and credited to PL/suspense category account.Fee entered in CPTY.FEE.AMT will be debited from PL/suspense category account and credited to the counterparty. This field is applicable only for agency booking model contracts. |
| 112 | `SY.ADC.FEE.RESERVED.5` | `SyAccuDecu_FeeReserved5` | TField |  |  |
| 113 | `SY.ADC.FEE.RESERVED.4` | `SyAccuDecu_FeeReserved4` | TField |  |  |
| 114 | `SY.ADC.FEE.RESERVED.3` | `SyAccuDecu_FeeReserved3` | TField |  |  |
| 115 | `SY.ADC.FEE.RESERVED.2` | `SyAccuDecu_FeeReserved2` | TField |  |  |
| 116 | `SY.ADC.FEE.RESERVED.1` | `SyAccuDecu_FeeReserved1` | TField |  |  |
| 117 | `SY.ADC.NOVATION` | `SyAccuDecu_Novation` | TField |  | Initially the field would be blank, at the time of novation, depending on the type of novation, the appropriate value should be selected. Allowed value are 'Internal Novation' 'External Novation'. Validation Rules: Input to this field is not allowed if KNOCK.OUT is set or if UNWIND is set to YES or FULL. Input to this field is not allowed if KNOCK.OUT or UNWIND is set to YES or FULL. |
| 118 | `SY.ADC.NOVATION.EFF.DATE` | `SyAccuDecu_NovationEffDate` | TField |  | This field holds the effective date of novation. The Accrual would be stopped on this date. Defaults to the current system date. |
| 119 | `SY.ADC.NOVATION.FEE.CCY` | `SyAccuDecu_NovationFeeCcy` | TField |  | This field holds the currency of the novation fee. |
| 120 | `SY.ADC.NOVATION.FEE.AMT` | `SyAccuDecu_NovationFeeAmt` | TField |  | This field holds the novation fee amount. |
| 121 | `SY.ADC.NOVATION.FEE.ACC` | `SyAccuDecu_NovationFeeAcc` | TField |  | This field holds the customer account from which the novation fee will be debited. |
| 122 | `SY.ADC.NOVATED.FROM` | `SyAccuDecu_NovatedFrom` | TField |  |  |
| 123 | `SY.ADC.NOVATED.TO` | `SyAccuDecu_NovatedTo` | TField |  |  |
| 124 | `SY.ADC.NOVATION.REFERENCE` | `SyAccuDecu_NovationReference` | TField |  | This field can be used to give the reference of the novated contract |
| 125 | `SY.ADC.PREMIUM.ACC` | `SyAccuDecu_PremiumAcc` | TField |  | The premium amount will be debited from this account. |
| 126 | `SY.ADC.PREM.PAYMENT.DATE` | `SyAccuDecu_PremPaymentDate` | TField |  |  |
| 127 | `SY.ADC.CPTY.PREM.AMT` | `SyAccuDecu_CptyPremAmt` | TField |  | This field will store the premium amount debited from/credited to the counterparty. Debit or Credit from counterparty will be decided based on the field PREMIUM.PAY.RECEIVE set This field is applicable only for agency booking model contracts. |
| 128 | `SY.ADC.PREMIUM.PAY.RECEIVE` | `SyAccuDecu_PremiumPayReceive` | TField |  | This field will say whether the customer has to receive/pay the premium amount. Allowed values: PAY,RECEIVE |
| 129 | `SY.ADC.PREM.RESERVED.5` | `SyAccuDecu_PremReserved5` | TField |  |  |
| 130 | `SY.ADC.PREM.RESERVED.4` | `SyAccuDecu_PremReserved4` | TField |  |  |
| 131 | `SY.ADC.PREM.RESERVED.3` | `SyAccuDecu_PremReserved3` | TField |  |  |
| 132 | `SY.ADC.PREM.RESERVED.2` | `SyAccuDecu_PremReserved2` | TField |  |  |
| 133 | `SY.ADC.PREM.RESERVED.1` | `SyAccuDecu_PremReserved1` | TField |  |  |
| 134 | `SY.ADC.CHGS.RESERVED.20` | `SyAccuDecu_ChgsReserved20` | TField |  |  |
| 135 | `SY.ADC.CHGS.RESERVED.19` | `SyAccuDecu_ChgsReserved19` | TField |  |  |
| 136 | `SY.ADC.CHGS.RESERVED.18` | `SyAccuDecu_ChgsReserved18` | TField |  |  |
| 137 | `SY.ADC.CHGS.RESERVED.17` | `SyAccuDecu_ChgsReserved17` | TField |  |  |
| 138 | `SY.ADC.CHGS.RESERVED.16` | `SyAccuDecu_ChgsReserved16` | TField |  |  |
| 139 | `SY.ADC.CHGS.RESERVED.15` | `SyAccuDecu_ChgsReserved15` | TField |  |  |
| 140 | `SY.ADC.CHGS.RESERVED.14` | `SyAccuDecu_ChgsReserved14` | TField |  |  |
| 141 | `SY.ADC.CHGS.RESERVED.13` | `SyAccuDecu_ChgsReserved13` | TField |  |  |
| 142 | `SY.ADC.CHGS.RESERVED.12` | `SyAccuDecu_ChgsReserved12` | TField |  |  |
| 143 | `SY.ADC.CHGS.RESERVED.11` | `SyAccuDecu_ChgsReserved11` | TField |  |  |
| 144 | `SY.ADC.CU.NET.AMT` | `SyAccuDecu_CuNetAmt` | TField |  | Technical use. Reserved for future |
| 145 | `SY.ADC.CHGS.RESERVED.10` | `SyAccuDecu_ChgsReserved10` | TField |  |  |
| 146 | `SY.ADC.CHGS.RESERVED.9` | `SyAccuDecu_ChgsReserved9` | TField |  |  |
| 147 | `SY.ADC.CHGS.RESERVED.8` | `SyAccuDecu_ChgsReserved8` | TField |  |  |
| 148 | `SY.ADC.CHGS.RESERVED.7` | `SyAccuDecu_ChgsReserved7` | TField |  |  |
| 149 | `SY.ADC.CHGS.RESERVED.6` | `SyAccuDecu_ChgsReserved6` | TField |  |  |
| 150 | `SY.ADC.CHGS.RESERVED.5` | `SyAccuDecu_ChgsReserved5` | TField |  |  |
| 151 | `SY.ADC.CHGS.RESERVED.4` | `SyAccuDecu_ChgsReserved4` | TField |  |  |
| 152 | `SY.ADC.CHGS.RESERVED.3` | `SyAccuDecu_ChgsReserved3` | TField |  |  |
| 153 | `SY.ADC.CHGS.RESERVED.2` | `SyAccuDecu_ChgsReserved2` | TField |  |  |
| 154 | `SY.ADC.CHGS.RESERVED.1` | `SyAccuDecu_ChgsReserved1` | TField |  |  |
| 155 | `SY.ADC.CPTY.NET.AMT` | `SyAccuDecu_CptyNetAmt` | TField |  | Technical use. Reserved for future |
| 156 | `SY.ADC.SETTLEMENT.ROLE` | `SyAccuDecu_SettlementRole` | TField |  | The value given here will be defaulted to PRINCIPAL.AGENT field in the SEC.TRADE generated at time of fixing. The PRINICIPAL.AGENT field in SEC.TRADE is used for stamp tax calculation. It is possible that the bank is acting as a principal for the accumulator contract, but have signed a legal agreement with the customer to the effect that the bank will be acting as agent for the fixing transaction. |
| 157 | `SY.ADC.DEALER.DESK` | `SyAccuDecu_DealerDesk` | TField |  | Identifies the dealer desk relating to the transaction. The same value would be used in the underlying option trade as well. |
| 158 | `SY.ADC.REMAINING.UNITS` | `SyAccuDecu_RemainingUnits` | TField |  | This fields holds the remaining units for the contract, at the time of inception the value in this field would be equal to TOTAL.UNITS, subsequently during the life cycle of the contract, the remaining units would be reduced as a result of fixing, unwinding, knock out and novation events. |
| 159 | `SY.ADC.SUSPEND.BY.SYS` | `SyAccuDecu_SuspendBySys` | TField |  | This field will be updated by the system if the trading is suspended in the stock exchange of the underlying equity. |
| 160 | `SY.ADC.CALC.SETTLE.AMT` | `SyAccuDecu_CalcSettleAmt` | TField |  | This field holds the trigger for calculating the cash settlement amount. Once the market price is keyed in at the time of fixing, and this field needs to be set to 'Yes', to trigger the system to calculate the settlement amount. This calcualtion would happen during the validation/commit of the contract and this flag would be reset. if recalculation is required then , this flag needs to be set to "Yes" again. This settlement amount calculated pertains only to the current fixing period. |
| 161 | `SY.ADC.SY.MASTER` | `SyAccuDecu_SyMaster` | TField |  | This field will hold the SY.MASTER linked to the contract Validation Rules: NOCHANGE field Must be the ID of a valid SY.MASTER file record. |
| 162 | `SY.ADC.RISK.LEVEL` | `SyAccuDecu_RiskLevel` | TField |  | This field holds the product risk rating for the contract This field will be defaulted from SY.MASTER if master linked to the contract Validation Rules: Input to this field is derived from EB.LOOKUP table - RISK.LEVEL*(1-10) |
| 163 | `SY.ADC.CALENDAR` | `SyAccuDecu_Calendar` | TField |  | This field would accept a region which will be referred for building the fixing schedule, working out the total number of working days. The same calendar would be used for the accrual process Validation Rules: Must be the ID of a valid REGION file record. |
| 164 | `SY.ADC.COVERED.CONTRACT` | `SyAccuDecu_CoveredContract` | TField |  | This field will hold the value that decides how the nominal blocking should happen. Validation Rules: NOCHANGE field Allowed values: FULLY.COVERED - Security position blocking will happen for the total units for DECUMULATOR contract. Allows manual input of positions that are to be blocked UNCOVERED - Security position cannot be blocked PARTIALLY.COVERED - User manually enters the quantity that are to be blocked. |
| 165 | `SY.ADC.LIMIT.REF` | `SyAccuDecu_LimitRef` | TField |  | The Limit reference identifying the customer credit line . |
| 166 | `SY.ADC.LIMIT.DETS` | `SyAccuDecu_LimitDets` | TField |  | This field is used to store limit related details. Technical use. |
| 167 | `SY.ADC.PYMT.MSG.REQD` | `SyAccuDecu_PymtMsgReqd` | TField |  | When this field holds the value as YES, then payment message will be generated |
| 168 | `SY.ADC.BEN.BANK` | `SyAccuDecu_BenBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 169 | `SY.ADC.BEN.ADD` | `SyAccuDecu_BenAdd` |  |  |  |
| 170 | `SY.ADC.BEN.ACCT` | `SyAccuDecu_BenAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 171 | `SY.ADC.INTR.BANK` | `SyAccuDecu_IntrBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 172 | `SY.ADC.INTR.ADD` | `SyAccuDecu_IntrAdd` |  |  |  |
| 173 | `SY.ADC.CPTY.NO` | `SyAccuDecu_CptyNo` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 174 | `SY.ADC.CPTY.ADD` | `SyAccuDecu_CptyAdd` |  |  |  |
| 175 | `SY.ADC.CPTY.ACCT` | `SyAccuDecu_CptyAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 176 | `SY.ADC.RESERVED.15` | `SyAccuDecu_Reserved15` | TField |  |  |
| 177 | `SY.ADC.RESERVED.14` | `SyAccuDecu_Reserved14` | TField |  |  |
| 178 | `SY.ADC.RESERVED.13` | `SyAccuDecu_Reserved13` | TField |  |  |
| 179 | `SY.ADC.RESERVED.12` | `SyAccuDecu_Reserved12` | TField |  |  |
| 180 | `SY.ADC.RESERVED.11` | `SyAccuDecu_Reserved11` | TField |  |  |
| 181 | `SY.ADC.RESERVED.10` | `SyAccuDecu_Reserved10` | TField |  |  |
| 182 | `SY.ADC.RESERVED.09` | `SyAccuDecu_Reserved09` | TField |  |  |
| 183 | `SY.ADC.RESERVED.08` | `SyAccuDecu_Reserved08` | TField |  |  |
| 184 | `SY.ADC.RESERVED.07` | `SyAccuDecu_Reserved07` | TField |  |  |
| 185 | `SY.ADC.RESERVED.06` | `SyAccuDecu_Reserved06` | TField |  |  |
| 186 | `SY.ADC.RESERVED.05` | `SyAccuDecu_Reserved05` | TField |  |  |
| 187 | `SY.ADC.RESERVED.04` | `SyAccuDecu_Reserved04` | TField |  |  |
| 188 | `SY.ADC.RESERVED.03` | `SyAccuDecu_Reserved03` | TField |  |  |
| 189 | `SY.ADC.RESERVED.02` | `SyAccuDecu_Reserved02` | TField |  |  |
| 190 | `SY.ADC.RESERVED.01` | `SyAccuDecu_Reserved01` | TField |  |  |
| 191 | `SY.ADC.LOCAL.REF` | `SyAccuDecu_LocalRef` |  |  |  |
| 192 | `SY.ADC.STMT.NOS` | `SyAccuDecu_StmtNos` |  |  |  |
| 193 | `SY.ADC.OVERRIDE` | `SyAccuDecu_Override` |  |  |  |
| 194 | `SY.ADC.RECORD.STATUS` | `SyAccuDecu_RecordStatus` | String |  |  |
| 195 | `SY.ADC.CURR.NO` | `SyAccuDecu_CurrNo` | String |  |  |
| 196 | `SY.ADC.INPUTTER` | `SyAccuDecu_Inputter` |  |  |  |
| 197 | `SY.ADC.DATE.TIME` | `SyAccuDecu_DateTime` |  |  |  |
| 198 | `SY.ADC.AUTHORISER` | `SyAccuDecu_Authoriser` | String |  |  |
| 199 | `SY.ADC.CO.CODE` | `SyAccuDecu_CoCode` | String |  |  |
| 200 | `SY.ADC.DEPT.CODE` | `SyAccuDecu_DeptCode` | String |  |  |
| 201 | `SY.ADC.AUDITOR.CODE` | `SyAccuDecu_AuditorCode` | String |  |  |
| 202 | `SY.ADC.AUDIT.DATE.TIME` | `SyAccuDecu_AuditDateTime` | String |  |  |
