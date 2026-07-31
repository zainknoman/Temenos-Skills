# FS.GA.TAX.TABLE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.TAX.TABLE.DEFINITION` in `FS_Tax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TAX.TABLE.DEFINITION.PARENT.REF.ID` | `FsGaTaxTableDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.TAX.TABLE.DEFINITION.ORA.ROWID` | `FsGaTaxTableDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.NAV.CAL.CODE2` | `FsGaTaxTableDefinition_RecoverableTaxNavCalCode2` | TField |  | Nav calculation code2 for recoverable tax Multifonds DB Column is NAV_INT_REC_2. |
| 4 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CAL.CODE.FOR.CAP.GAINS` | `FsGaTaxTableDefinition_NavCalCodeForCapGains` | TField |  | NAV calculation code for Capital Gain Multifonds DB Column is GAIN_NAV_INT. |
| 5 | `FS.GA.TAX.TABLE.DEFINITION.SPECIAL.OPERATION.CODE` | `FsGaTaxTableDefinition_SpecialOperationCode` | TField |  | Special Operation code (078 Op code has been enhanced has Special Op code to book the foreign dividends without withholding tax under - FDTAX03 screen ) Multifonds DB Column is SPL_COPER. |
| 6 | `FS.GA.TAX.TABLE.DEFINITION.CAPITAL.GAIN.SHORT.TERM.PCT` | `FsGaTaxTableDefinition_CapitalGainShortTermPct` | TField |  | Used to define tax percentage for calculation of short term capital gains tax in tax regime/tables Multifonds DB Column is GAIN_CAP_PCT. |
| 7 | `FS.GA.TAX.TABLE.DEFINITION.TAX.CODE` | `FsGaTaxTableDefinition_TaxCode` | TField |  | Taxation code Multifonds DB Column is CTAX. |
| 8 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CALCULATION.CODE.FOR.TAX.1` | `FsGaTaxTableDefinition_NavCalculationCodeForTax1` | TField |  | Nav calculation code for tax 1 Multifonds DB Column is NAV_INT_TAX_1. |
| 9 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CALCULATION.CODE.FOR.TAX.2` | `FsGaTaxTableDefinition_NavCalculationCodeForTax2` | TField |  | Nav calculation code for tax 2 Multifonds DB Column is NAV_INT_TAX_2. |
| 10 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CAL.CODE.FOR.SEC.LEN.TAX` | `FsGaTaxTableDefinition_NavCalCodeForSecLenTax` | TField |  | NAV Calculation code for Security Lending Tax Multifonds DB Column is NAV_INT_LEN. |
| 11 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CAL.CODE.FOR.CAP.GAIN.L` | `FsGaTaxTableDefinition_NavCalCodeForCapGainL` | TField |  | NAV Calculation code for Long Term Capital Gain Tax Multifonds DB Column is GAIN_NAV_INT_L. |
| 12 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CODE.OF.HOLDING.PERIOD.TAX` | `FsGaTaxTableDefinition_NavCodeOfHoldingPeriodTax` | TField |  | NAV calculation code for Holding Period Tax Multifonds DB Column is NAV_HOLD. |
| 13 | `FS.GA.TAX.TABLE.DEFINITION.ROUNDING.OF.HOLDING.PERIOD.TAX` | `FsGaTaxTableDefinition_RoundingOfHoldingPeriodTax` | TField |  | Rounding of Holding Period Tax Multifonds DB Column is HOLD_ROUND. |
| 14 | `FS.GA.TAX.TABLE.DEFINITION.PURCHASE` | `FsGaTaxTableDefinition_Purchase` | TField |  | Purchase Identifier Multifonds DB Column is FLG_PURCHASE. |
| 15 | `FS.GA.TAX.TABLE.DEFINITION.ACCOUNTING.METHOD` | `FsGaTaxTableDefinition_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 16 | `FS.GA.TAX.TABLE.DEFINITION.PAYABLE.TAX.1.PERCENTAGE` | `FsGaTaxTableDefinition_PayableTax1Percentage` | TField |  | Rate of Tax payable on the income , type of tax 1 Multifonds DB Column is PCT_TAX_1. |
| 17 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CODE.OF.FRANKED.DIVD.TAX` | `FsGaTaxTableDefinition_NavCodeOfFrankedDivdTax` | TField |  | NAV calculation Code for Franked Dividend Tax Multifonds DB Column is NAV_INT_FRANK. |
| 18 | `FS.GA.TAX.TABLE.DEFINITION.FATCA.RECOVERABLE.NAV.CODE` | `FsGaTaxTableDefinition_FatcaRecoverableNavCode` | TField |  | The FATCA Recoverable tax NAV calculation code. Multifonds DB Column is FATCA_NAV_INT_REC. |
| 19 | `FS.GA.TAX.TABLE.DEFINITION.TAX.SECURITY.TYPE` | `FsGaTaxTableDefinition_TaxSecurityType` | TField |  | Define the tax security type for determining the type of instruments (bonds, equities, warrants, etc.) Multifonds DB Column is TAX_SEC_TYPE. |
| 20 | `FS.GA.TAX.TABLE.DEFINITION.TAX.REGIME` | `FsGaTaxTableDefinition_TaxRegime` | TField |  | A group of Tax rules can be defined in the Tax tables against a Tax regime and all the funds defined with the respective Tax regime would follow the tax rules defined under this Tax regime. Multifonds DB Column is TAX_REG. |
| 21 | `FS.GA.TAX.TABLE.DEFINITION.PAYABLE.TAX.2.PERCENTAGE` | `FsGaTaxTableDefinition_PayableTax2Percentage` | TField |  | Rate of Tax payable on the income , type of tax 2 Multifonds DB Column is PCT_TAX_2. |
| 22 | `FS.GA.TAX.TABLE.DEFINITION.TAX.BASIS` | `FsGaTaxTableDefinition_TaxBasis` | TField |  | Tax Basis Multifonds DB Column is TAX_BASIS. |
| 23 | `FS.GA.TAX.TABLE.DEFINITION.UNREC.TAX.NAV.CAL.CODE1` | `FsGaTaxTableDefinition_UnrecTaxNavCalCode1` | TField |  | Nav calculation code1 for unrecoverable tax Multifonds DB Column is NAV_INT_UNREC. |
| 24 | `FS.GA.TAX.TABLE.DEFINITION.UNREC.TAX.NAV.CAL.CODE2` | `FsGaTaxTableDefinition_UnrecTaxNavCalCode2` | TField |  | Nav calculation code2 for unrecoverable tax Multifonds DB Column is NAV_INT_UNREC_2. |
| 25 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.NAV.CAL.CODE1` | `FsGaTaxTableDefinition_RecoverableTaxNavCalCode1` | TField |  | Nav calculation code1 for recoverable tax Multifonds DB Column is NAV_INT_REC. |
| 26 | `FS.GA.TAX.TABLE.DEFINITION.SECURITY.LENDING.TAX` | `FsGaTaxTableDefinition_SecurityLendingTax` | TField |  | corresponds to the security tax at coupon level Multifonds DB Column is SEC_LEN_TAX. |
| 27 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.NAV.CODE2` | `FsGaTaxTableDefinition_RecoverableTaxNavCode2` | TField |  | NAV code2 for recoverable tax Multifonds DB Column is COPER_REC_2. |
| 28 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.CURRENCY2` | `FsGaTaxTableDefinition_RecoverableTaxCurrency2` | TField |  | Currency code2 for recoverable tax Multifonds DB Column is CMON_REC_2. |
| 29 | `FS.GA.TAX.TABLE.DEFINITION.TAX.PERCENT.FOR.CAP.GAIN.L` | `FsGaTaxTableDefinition_TaxPercentForCapGainL` | TField |  | Tax Percent on Lond Term Capital Gain Tax Multifonds DB Column is GAIN_CAP_PCT_L. |
| 30 | `FS.GA.TAX.TABLE.DEFINITION.CAPITAL.GAIN.NAV.CODE` | `FsGaTaxTableDefinition_CapitalGainNavCode` | TField |  | NAV code for Capital Gain Multifonds DB Column is GAIN_COPER. |
| 31 | `FS.GA.TAX.TABLE.DEFINITION.CURRENCY.CODE.FOR.CAPITAL.GAIN` | `FsGaTaxTableDefinition_CurrencyCodeForCapitalGain` | TField |  | Currency Code for Capital Gain Multifonds DB Column is GAIN_CMON. |
| 32 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CODE.FOR.TAX.1` | `FsGaTaxTableDefinition_NavCodeForTax1` | TField |  | NAV code for Tax 1 Multifonds DB Column is COPER_TAX_1. |
| 33 | `FS.GA.TAX.TABLE.DEFINITION.CURRENCY.CODE.FOR.TAX.1` | `FsGaTaxTableDefinition_CurrencyCodeForTax1` | TField |  | Currency code for Tax 1 Multifonds DB Column is CMON_TAX_1. |
| 34 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CODE.FOR.TAX.2` | `FsGaTaxTableDefinition_NavCodeForTax2` | TField |  | NAV code for tax 2 Multifonds DB Column is COPER_TAX_2. |
| 35 | `FS.GA.TAX.TABLE.DEFINITION.CURRENCY.CODE.FOR.TAX.2` | `FsGaTaxTableDefinition_CurrencyCodeForTax2` | TField |  | Currency code for tax 2 Multifonds DB Column is CMON_TAX_2. |
| 36 | `FS.GA.TAX.TABLE.DEFINITION.NUMBER.OF.DAYS.FOR.S` | `FsGaTaxTableDefinition_NumberOfDaysForS` | TField |  | 365 or less days as Short Term Capital Gain Tax Multifonds DB Column is GAIN_NBDAYS_S. |
| 37 | `FS.GA.TAX.TABLE.DEFINITION.NUMBER.OF.DAYS.FOR.L` | `FsGaTaxTableDefinition_NumberOfDaysForL` | TField |  | Over 365 Days as Long Term Capital Gain Tax Multifonds DB Column is GAIN_NBDAYS_L. |
| 38 | `FS.GA.TAX.TABLE.DEFINITION.KR.RECOVERABLE.TAX` | `FsGaTaxTableDefinition_KrRecoverableTax` | TField |  | Kr Recoverable Tax Multifonds DB Column is KRRECTAX. |
| 39 | `FS.GA.TAX.TABLE.DEFINITION.HOLDING.PERIOD.TAX.IN.PERCENT` | `FsGaTaxTableDefinition_HoldingPeriodTaxInPercent` | TField |  | Holding period tax percentage on Income Multifonds DB Column is HOLD_TAX. |
| 40 | `FS.GA.TAX.TABLE.DEFINITION.SEC.LENDING.TAX.NAV.CODE` | `FsGaTaxTableDefinition_SecLendingTaxNavCode` | TField |  | NAV code for Security lending Tax Multifonds DB Column is COPER_LEN. |
| 41 | `FS.GA.TAX.TABLE.DEFINITION.CCY.CODE.FOR.SEC.LENDING.TAX` | `FsGaTaxTableDefinition_CcyCodeForSecLendingTax` | TField |  | Currency code for Security Lending Tax Multifonds DB Column is CMON_LEN. |
| 42 | `FS.GA.TAX.TABLE.DEFINITION.NAV.CODE.FOR.CAP.GAIN.L` | `FsGaTaxTableDefinition_NavCodeForCapGainL` | TField |  | NAV code for Long Term Capital Gain Tax Multifonds DB Column is GAIN_COPER_L. |
| 43 | `FS.GA.TAX.TABLE.DEFINITION.CCY.CODE.FOR.CAP.GAIN.L.TAX` | `FsGaTaxTableDefinition_CcyCodeForCapGainLTax` | TField |  | Currency Code for Long Term Capital Gain Tax Multifonds DB Column is GAIN_CMON_L. |
| 44 | `FS.GA.TAX.TABLE.DEFINITION.TRANSACTION.TYPE.HOLD` | `FsGaTaxTableDefinition_TransactionTypeHold` | TField |  | Transaction Type Hold Multifonds DB Column is COPER_HOLD. |
| 45 | `FS.GA.TAX.TABLE.DEFINITION.CURRENCY.OF.HOLDING.PERIOD.TAX` | `FsGaTaxTableDefinition_CurrencyOfHoldingPeriodTax` | TField |  | Currency of Holding Period Tax Multifonds DB Column is CMON_HOLD. |
| 46 | `FS.GA.TAX.TABLE.DEFINITION.FRANKED.DIVIDEND.TAX.PERCENT` | `FsGaTaxTableDefinition_FrankedDividendTaxPercent` | TField |  | Franked tax percentage on the dividend income Multifonds DB Column is PFRANKTAX. |
| 47 | `FS.GA.TAX.TABLE.DEFINITION.OP.CODE.FOR.FRANKED.DIVD.TAX` | `FsGaTaxTableDefinition_OpCodeForFrankedDivdTax` | TField |  | Operation Code for Franked Dividend Tax Multifonds DB Column is COPER_FRANK. |
| 48 | `FS.GA.TAX.TABLE.DEFINITION.CURRENCY.OF.FRANKED.DIVD.TAX` | `FsGaTaxTableDefinition_CurrencyOfFrankedDivdTax` | TField |  | Currency of Franked Dividend Tax Multifonds DB Column is CMON_FRANK. |
| 49 | `FS.GA.TAX.TABLE.DEFINITION.FATCA.RECOVERABLE.OP.CODE` | `FsGaTaxTableDefinition_FatcaRecoverableOpCode` | TField |  | The FATCA Recoverable NAV Operation code Multifonds DB Column is FATCA_COPER_REC. |
| 50 | `FS.GA.TAX.TABLE.DEFINITION.FATCA.RECOVERABLE.CCY.CODE` | `FsGaTaxTableDefinition_FatcaRecoverableCcyCode` | TField |  | The FATCA Recoverable tax Currency Code Multifonds DB Column is FATCA_CMON_REC. |
| 51 | `FS.GA.TAX.TABLE.DEFINITION.FATCA.RECOVERABLE.PERCENT` | `FsGaTaxTableDefinition_FatcaRecoverablePercent` | TField |  | FATCA Recoverable tax Percentage Multifonds DB Column is PCT_FATCA_REC. |
| 52 | `FS.GA.TAX.TABLE.DEFINITION.UNREALISED.CIT.OPERATION.CODE` | `FsGaTaxTableDefinition_UnrealisedCitOperationCode` | TField |  | Unrealised CIT Operation Code Multifonds DB Column is UNREAL_CIT_COPER. |
| 53 | `FS.GA.TAX.TABLE.DEFINITION.UNREALISED.TR.OPERATION.CODE` | `FsGaTaxTableDefinition_UnrealisedTrOperationCode` | TField |  | Unrealised TR Operation Code Multifonds DB Column is UNREAL_TR_COPER. |
| 54 | `FS.GA.TAX.TABLE.DEFINITION.CORPORATE.INCOME.TAX.COPER` | `FsGaTaxTableDefinition_CorporateIncomeTaxCoper` | TField |  | Corporate Income Tax COPER Multifonds DB Column is CIT_COPER. |
| 55 | `FS.GA.TAX.TABLE.DEFINITION.TAX.RESERVE.OPERATION.CODE` | `FsGaTaxTableDefinition_TaxReserveOperationCode` | TField |  | Tax Reserve Operation Code Multifonds DB Column is TR_COPER. |
| 56 | `FS.GA.TAX.TABLE.DEFINITION.PERCENTAGE.OF.TAX` | `FsGaTaxTableDefinition_PercentageOfTax` | TField |  | Tax income percentage on income Multifonds DB Column is TAX_INC. |
| 57 | `FS.GA.TAX.TABLE.DEFINITION.CURRENCY.CODE` | `FsGaTaxTableDefinition_CurrencyCode` | TField |  | Currency Code like USD, EUR Multifonds DB Column is CODMON. |
| 58 | `FS.GA.TAX.TABLE.DEFINITION.UNREALISED.CIT.PERCENTAGE` | `FsGaTaxTableDefinition_UnrealisedCitPercentage` | TField |  | Unrealised CIT Percentage Multifonds DB Column is UNREAL_CIT_PCT. |
| 59 | `FS.GA.TAX.TABLE.DEFINITION.TAX.DOMICILE` | `FsGaTaxTableDefinition_TaxDomicile` | TField |  | Shows the tax domicile of the securities Multifonds DB Column is CPAYS_TAX. |
| 60 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.NAV.CODE1` | `FsGaTaxTableDefinition_UnrecoverableTaxNavCode1` | TField |  | Operation code1 for unrecoverable tax Multifonds DB Column is COPER_UNREC. |
| 61 | `FS.GA.TAX.TABLE.DEFINITION.UNREALISED.TR.PERCENTAGE` | `FsGaTaxTableDefinition_UnrealisedTrPercentage` | TField |  | Unrealised TR Percentage Multifonds DB Column is UNREAL_TR_PCT. |
| 62 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.CURRENCY1` | `FsGaTaxTableDefinition_UnrecoverableTaxCurrency1` | TField |  | Currency1 for unrecoverable tax Multifonds DB Column is CMON_UNREC. |
| 63 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.NAV.CODE2` | `FsGaTaxTableDefinition_UnrecoverableTaxNavCode2` | TField |  | NAV code2 for unrecoverable tax Multifonds DB Column is COPER_UNREC_2. |
| 64 | `FS.GA.TAX.TABLE.DEFINITION.CORPORATE.INCOME.TAX.PERCENT` | `FsGaTaxTableDefinition_CorporateIncomeTaxPercent` | TField |  | Corporate Income Tax Percent Multifonds DB Column is CIT_PCT. |
| 65 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.CURRENCY2` | `FsGaTaxTableDefinition_UnrecoverableTaxCurrency2` | TField |  | Currency2 for unrecoverable tax Multifonds DB Column is CMON_UNREC_2. |
| 66 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.NAV.CODE1` | `FsGaTaxTableDefinition_RecoverableTaxNavCode1` | TField |  | NAV code1 for recoverable tax Multifonds DB Column is COPER_REC. |
| 67 | `FS.GA.TAX.TABLE.DEFINITION.TAX.RESERVE.PERCENTAGE` | `FsGaTaxTableDefinition_TaxReservePercentage` | TField |  | Tax Reserve Percentage Multifonds DB Column is TR_PCT. |
| 68 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.CURRENCY1` | `FsGaTaxTableDefinition_RecoverableTaxCurrency1` | TField |  | Currency code1 for recoverable tax Multifonds DB Column is CMON_REC. |
| 69 | `FS.GA.TAX.TABLE.DEFINITION.CAPITAL.GAIN.FEE.CODE` | `FsGaTaxTableDefinition_CapitalGainFeeCode` | TField |  | Fee code for Capital Gain Multifonds DB Column is GAIN_CFRAIS. |
| 70 | `FS.GA.TAX.TABLE.DEFINITION.FEES.CODE.FOR.TAX.1` | `FsGaTaxTableDefinition_FeesCodeForTax1` | TField |  | Fees code for Tax 1 Multifonds DB Column is CFRAIS_TAX_1. |
| 71 | `FS.GA.TAX.TABLE.DEFINITION.FEES.CODE.FOR.TAX.2` | `FsGaTaxTableDefinition_FeesCodeForTax2` | TField |  | Fees code for tax 2 Multifonds DB Column is CFRAIS_TAX_2. |
| 72 | `FS.GA.TAX.TABLE.DEFINITION.SEC.LENDING.TAX.FEE.CODE` | `FsGaTaxTableDefinition_SecLendingTaxFeeCode` | TField |  | Fee code for Security Lending Tax Multifonds DB Column is CFRAIS_LEN. |
| 73 | `FS.GA.TAX.TABLE.DEFINITION.FEE.CODE.FOR.CAP.GAIN.L` | `FsGaTaxTableDefinition_FeeCodeForCapGainL` | TField |  | Fee Code for Long Term Capital Gain Tax Multifonds DB Column is GAIN_CFRAIS_L. |
| 74 | `FS.GA.TAX.TABLE.DEFINITION.ENTITLEMENT.DATE` | `FsGaTaxTableDefinition_EntitlementDate` | TField |  | The ex-date, or ex-dividend date, is the date on or after which a security is traded without a previously declared dividend or distribution. Multifonds DB Column is DEXEC. |
| 75 | `FS.GA.TAX.TABLE.DEFINITION.FEES.HOLD` | `FsGaTaxTableDefinition_FeesHold` | TField |  | Fees Hold Multifonds DB Column is CFRAIS_HOLD. |
| 76 | `FS.GA.TAX.TABLE.DEFINITION.UNREC.TAX.IN.PERCENT.TYPE.1` | `FsGaTaxTableDefinition_UnrecTaxInPercentType1` | TField |  | Unrecoverable tax percentage on Income , type 1 Multifonds DB Column is PUNRECTAX. |
| 77 | `FS.GA.TAX.TABLE.DEFINITION.FEE.CODE.OF.FRANKED.DIVD.TAX` | `FsGaTaxTableDefinition_FeeCodeOfFrankedDivdTax` | TField |  | Fee Code for Franked Dividend Tax Multifonds DB Column is CFRAIS_FRANK. |
| 78 | `FS.GA.TAX.TABLE.DEFINITION.FATCA.RECOVERABLE.FEE.CODE` | `FsGaTaxTableDefinition_FatcaRecoverableFeeCode` | TField |  | The FATCA Recoverable Fee. code Multifonds DB Column is FATCA_CFRAIS_REC. |
| 79 | `FS.GA.TAX.TABLE.DEFINITION.BOND.MARKET.TYPE` | `FsGaTaxTableDefinition_BondMarketType` | TField |  | Bond Market Type Multifonds DB Column is BOND_MARKET_TYPE. |
| 80 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.FEE.CODE1` | `FsGaTaxTableDefinition_UnrecoverableTaxFeeCode1` | TField |  | Fees code1 for unrecoverable tax Multifonds DB Column is CFRAIS_UNREC. |
| 81 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.PERCENT.2` | `FsGaTaxTableDefinition_UnrecoverableTaxPercent2` | TField |  | Unrecoverable tax percentage on Income , type 2 Multifonds DB Column is PUNRECTAX_2. |
| 82 | `FS.GA.TAX.TABLE.DEFINITION.UNRECOVERABLE.TAX.FEE.CODE2` | `FsGaTaxTableDefinition_UnrecoverableTaxFeeCode2` | TField |  | Fees code2 for unrecoverable tax Multifonds DB Column is CFRAIS_UNREC_2. |
| 83 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.FEE.CODE1` | `FsGaTaxTableDefinition_RecoverableTaxFeeCode1` | TField |  | Fees code1 for recoverable tax Multifonds DB Column is CFRAIS_REC. |
| 84 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.FEE.CODE2` | `FsGaTaxTableDefinition_RecoverableTaxFeeCode2` | TField |  | Fees code2 for recoverable tax Multifonds DB Column is CFRAIS_REC_2. |
| 85 | `FS.GA.TAX.TABLE.DEFINITION.EXCHANGE.GAIN.LOSS.FOR.S` | `FsGaTaxTableDefinition_ExchangeGainLossForS` | TField |  | Calcualate Exchange Rate Gain Loss on Short Term Capital Gain Multifonds DB Column is GAIN_CALC_TYPE_S. |
| 86 | `FS.GA.TAX.TABLE.DEFINITION.REC.TAX.IN.PERCENT.TYPE.1` | `FsGaTaxTableDefinition_RecTaxInPercentType1` | TField |  | Recoverable tax percentage on Income , type 1 Multifonds DB Column is PRECTAX. |
| 87 | `FS.GA.TAX.TABLE.DEFINITION.EXCHANGE.GAIN.LOSS.FOR.L` | `FsGaTaxTableDefinition_ExchangeGainLossForL` | TField |  | Calcualate Exchange Rate Gain Loss on Long Term Capital Gain Multifonds DB Column is GAIN_CALC_TYPE_L. |
| 88 | `FS.GA.TAX.TABLE.DEFINITION.UNREALISED.CIT.CALC.TYPE` | `FsGaTaxTableDefinition_UnrealisedCitCalcType` | TField |  | Unrealised CIT CALC Type Multifonds DB Column is UNREAL_CIT_CALC_TYPE. |
| 89 | `FS.GA.TAX.TABLE.DEFINITION.UNREALISED.TR.CALC.TYPE` | `FsGaTaxTableDefinition_UnrealisedTrCalcType` | TField |  | Unrealised TR CALC Type Multifonds DB Column is UNREAL_TR_CALC_TYPE. |
| 90 | `FS.GA.TAX.TABLE.DEFINITION.CORPORATE.INCOME.TAX.CALC.TYPE` | `FsGaTaxTableDefinition_CorporateIncomeTaxCalcType` | TField |  | Corporate Income Tax CALC TYPE Multifonds DB Column is CIT_CALC_TYPE. |
| 91 | `FS.GA.TAX.TABLE.DEFINITION.RECOVERABLE.TAX.PERCENT.2` | `FsGaTaxTableDefinition_RecoverableTaxPercent2` | TField |  | Recoverable tax percentage on Income , type 2 Multifonds DB Column is PRECTAX_2. |
| 92 | `FS.GA.TAX.TABLE.DEFINITION.TAX.RESERVE.CALC.TYPE` | `FsGaTaxTableDefinition_TaxReserveCalcType` | TField |  | Tax Reserve CALC Type Multifonds DB Column is TR_CALC_TYPE. |
| 93 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED10` | `FsGaTaxTableDefinition_Reserved10` | TField |  |  |
| 94 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED9` | `FsGaTaxTableDefinition_Reserved9` | TField |  |  |
| 95 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED8` | `FsGaTaxTableDefinition_Reserved8` | TField |  |  |
| 96 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED7` | `FsGaTaxTableDefinition_Reserved7` | TField |  |  |
| 97 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED6` | `FsGaTaxTableDefinition_Reserved6` | TField |  |  |
| 98 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED5` | `FsGaTaxTableDefinition_Reserved5` | TField |  |  |
| 99 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED4` | `FsGaTaxTableDefinition_Reserved4` | TField |  |  |
| 100 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED3` | `FsGaTaxTableDefinition_Reserved3` | TField |  |  |
| 101 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED2` | `FsGaTaxTableDefinition_Reserved2` | TField |  |  |
| 102 | `FS.GA.TAX.TABLE.DEFINITION.RESERVED1` | `FsGaTaxTableDefinition_Reserved1` | TField |  |  |
| 103 | `FS.GA.TAX.TABLE.DEFINITION.LOCAL.REF` | `FsGaTaxTableDefinition_LocalRef` |  |  |  |
| 104 | `FS.GA.TAX.TABLE.DEFINITION.OVERRIDE` | `FsGaTaxTableDefinition_Override` |  |  |  |
| 105 | `FS.GA.TAX.TABLE.DEFINITION.RECORD.STATUS` | `FsGaTaxTableDefinition_RecordStatus` | String |  |  |
| 106 | `FS.GA.TAX.TABLE.DEFINITION.CURR.NO` | `FsGaTaxTableDefinition_CurrNo` | String |  |  |
| 107 | `FS.GA.TAX.TABLE.DEFINITION.INPUTTER` | `FsGaTaxTableDefinition_Inputter` |  |  |  |
| 108 | `FS.GA.TAX.TABLE.DEFINITION.DATE.TIME` | `FsGaTaxTableDefinition_DateTime` |  |  |  |
| 109 | `FS.GA.TAX.TABLE.DEFINITION.AUTHORISER` | `FsGaTaxTableDefinition_Authoriser` | String |  |  |
| 110 | `FS.GA.TAX.TABLE.DEFINITION.CO.CODE` | `FsGaTaxTableDefinition_CoCode` | String |  |  |
| 111 | `FS.GA.TAX.TABLE.DEFINITION.DEPT.CODE` | `FsGaTaxTableDefinition_DeptCode` | String |  |  |
| 112 | `FS.GA.TAX.TABLE.DEFINITION.AUDITOR.CODE` | `FsGaTaxTableDefinition_AuditorCode` | String |  |  |
| 113 | `FS.GA.TAX.TABLE.DEFINITION.AUDIT.DATE.TIME` | `FsGaTaxTableDefinition_AuditDateTime` | String |  |  |
