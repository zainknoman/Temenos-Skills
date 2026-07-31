# DX.CO.EXERCISE.AUTO — Table Schema

> Source: `INSERTS/I_F.DX.CO.EXERCISE.AUTO` in `DX_CloseoutExercise.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COAXR.CUST.OR.PORT` | `DxCoExerciseAuto_CustOrPort` | TField |  | Selection field which controls choice of customer or portfolio trades to be exercised. Default is ALL to exerciseall trades involving the chosen option series. Validation Rules: Must be one of ALL or CUSTOMER or PORTFOLIO |
| 2 | `DX.COAXR.CUSTOMER` | `DxCoExerciseAuto_Customer` | TField |  | The customer for whom option exercise will be performed. Validation Rules: Must be a valid DX.CUSTOMER |
| 3 | `DX.COAXR.PORTFOLIO` | `DxCoExerciseAuto_Portfolio` | TField |  | The customer portfolio on which option expiry will be performed. Validation Rules: Must be valid for SEC.ACC.MASTER Customer must be valid for DX.CUSTOMER |
| 4 | `DX.COAXR.CONTRACT.CODE` | `DxCoExerciseAuto_ContractCode` | TField |  | The contract code of the option to be expired Validation Rules: Should be valid for DX.CONTRACT.MASTER |
| 5 | `DX.COAXR.OPTION.STYLE` | `DxCoExerciseAuto_OptionStyle` | TField |  | Option style defaulted from DX.CONTRACT.MASTER. Validation Rules: NOINPUT One of EUROPEAN or AMERICAN |
| 6 | `DX.COAXR.MATURITY.DATE` | `DxCoExerciseAuto_MaturityDate` | TField | Yes | The maturity / delivery month of the option to be expired. Validation Rules: Up to 11 characters in DATE format The field CONTRACT.CODE must be populated prior to this field Must be in the format: MONTHLY TRADES = Month/Year e.g. SEP00 DAILY TRADES = Day/Month/Year e.g. 15SEP00 Mandatory field |
| 7 | `DX.COAXR.DECLARATION.DATE` | `DxCoExerciseAuto_DeclarationDate` | TField |  | The declaration date calculated from DX.CONTRACT.MASTER date formula. Validation Rules: NOINPUT Display date format, e.g 24 JAN 2000 |
| 8 | `DX.COAXR.STRIKE` | `DxCoExerciseAuto_Strike` | TField | Yes | Strike price for option to be exercised. Validation Rules: Strike must be valid for strike scale and interval on DX.CONTRACT.MASTER Mandatory field |
| 9 | `DX.COAXR.INT.STRIKE` | `DxCoExerciseAuto_IntStrike` | TField |  | Intenal strike price defaulted from STRIKE field Validation Rules: NOINPUT |
| 10 | `DX.COAXR.CALL.PUT` | `DxCoExerciseAuto_CallPut` | TField | Yes | Select CALL or PUT for option series. Validation Rules: Should be one of CALL or PUT Mandatory field |
| 11 | `DX.COAXR.UNAUTH.AUTH` | `DxCoExerciseAuto_UnauthAuth` | TField |  | If set as AUTHORISED this field will create all close out records with status of authorised. Validation Rules: One of AUTHORISED or UNAUTHORISED or blank |
| 12 | `DX.COAXR.CLOSEOUT.ID` | `DxCoExerciseAuto_CloseoutId` |  |  |  |
| 13 | `DX.COAXR.CONTRACT.CCY` | `DxCoExerciseAuto_ContractCcy` | TField | Yes | Specifies the contract currency of option to be exercised. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 14 | `DX.COAXR.DELIVERY.CCY` | `DxCoExerciseAuto_DeliveryCcy` | TField | Yes | Specifies the delivery currency of option to be exercised. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 15 | `DX.COAXR.STRIKE.OPERAND` | `DxCoExerciseAuto_StrikeOperand` | TField |  | The operand field is used to select the trades based on the strike quote or strike price provided. Availableoperands are EQ, GEand LE |
| 16 | `DX.COAXR.STRIKE.QUOTE` | `DxCoExerciseAuto_StrikeQuote` | TField |  | Holds the strike price in the quote currency which is STRIKE.QUOTE in trade. |
| 17 | `DX.COAXR.MARKET.PRICE` | `DxCoExerciseAuto_MarketPrice` | TField |  | Holds the market price of the security at the time of exercise. |
| 18 | `DX.COAXR.CASH.SETTLE.CCY` | `DxCoExerciseAuto_CashSettleCcy` | TField |  | Holds the delivery currency for the options with underlying as SECURITY.MASTER when the SETTLEMENT.METHOD isCASH. The exchange rate between this currency and contract currency is defined in DLV.CCY.RATE field. |
| 19 | `DX.COAXR.DLV.CCY.RATE` | `DxCoExerciseAuto_DlvCcyRate` | TField |  | Holds the exchange rate between trade currency and settlement currecny. |
| 20 | `DX.COAXR.SETTLE.INSTRUMENT` | `DxCoExerciseAuto_SettleInstrument` | TField |  | The alternate settlement instrument which is settled on exercise. |
| 21 | `DX.COAXR.SETT.INSTR.CONT.SIZE` | `DxCoExerciseAuto_SettInstrContSize` | TField | Yes | The contract size of the alternate settlement instrument which is mandatory when settled using alternateunderlying. |
| 22 | `DX.COAXR.SETT.INSTR.PRICE` | `DxCoExerciseAuto_SettInstrPrice` | TField | Yes | The price of the alternate settlement instrument which is mandatory when settled using alternate underlying. |
| 23 | `DX.COAXR.QUOTE.CCY` | `DxCoExerciseAuto_QuoteCcy` | TField |  | The currency in which the SPOT.EXCHANGE.RATE is quoted. |
| 24 | `DX.COAXR.SPOT.EXCHANGE.RATE` | `DxCoExerciseAuto_SpotExchangeRate` | TField |  | Holds the current exchange rate between the currency pairs of an FX option quoted in the QUOTE.CCY i.e basecurrency being the strike quote currency for generic FX-OTC options and delivery currency for fx options. |
| 25 | `DX.COAXR.FX.PAYOUT.CCY` | `DxCoExerciseAuto_FxPayoutCcy` | TField |  | Currency in which the payout is to be made for FX options. |
| 26 | `DX.COAXR.SPOT.PAYOUT.RATE` | `DxCoExerciseAuto_SpotPayoutRate` | TField |  | Holds the exchange rate between QUOTE.CCY and FX.PAYOUT.CCY. |
| 27 | `DX.COAXR.TRANS.ID` | `DxCoExerciseAuto_TransId` |  |  |  |
| 28 | `DX.COAXR.SETTLEMENT.CCY` | `DxCoExerciseAuto_SettlementCcy` |  |  |  |
| 29 | `DX.COAXR.SETTLEMENT.AMOUNT` | `DxCoExerciseAuto_SettlementAmount` |  |  |  |
| 30 | `DX.COAXR.VALUE.DATE` | `DxCoExerciseAuto_ValueDate` |  |  |  |
| 31 | `DX.COAXR.UNDERLYING.MAT.DATE` | `DxCoExerciseAuto_UnderlyingMatDate` | TField |  |  |
| 32 | `DX.COAXR.RESERVED2` | `DxCoExerciseAuto_Reserved2` | TField |  |  |
| 33 | `DX.COAXR.RESERVED1` | `DxCoExerciseAuto_Reserved1` | TField |  |  |
| 34 | `DX.COAXR.LOCAL.REF` | `DxCoExerciseAuto_LocalRef` |  |  |  |
| 35 | `DX.COAXR.OVERRIDE` | `DxCoExerciseAuto_Override` |  |  |  |
| 36 | `DX.COAXR.RECORD.STATUS` | `DxCoExerciseAuto_RecordStatus` | String |  |  |
| 37 | `DX.COAXR.CURR.NO` | `DxCoExerciseAuto_CurrNo` | String |  |  |
| 38 | `DX.COAXR.INPUTTER` | `DxCoExerciseAuto_Inputter` |  |  |  |
| 39 | `DX.COAXR.DATE.TIME` | `DxCoExerciseAuto_DateTime` |  |  |  |
| 40 | `DX.COAXR.AUTHORISER` | `DxCoExerciseAuto_Authoriser` | String |  |  |
| 41 | `DX.COAXR.CO.CODE` | `DxCoExerciseAuto_CoCode` | String |  |  |
| 42 | `DX.COAXR.DEPT.CODE` | `DxCoExerciseAuto_DeptCode` | String |  |  |
| 43 | `DX.COAXR.AUDITOR.CODE` | `DxCoExerciseAuto_AuditorCode` | String |  |  |
| 44 | `DX.COAXR.AUDIT.DATE.TIME` | `DxCoExerciseAuto_AuditDateTime` | String |  |  |
| 45 | `DX.COAXR.CLOSEOUT.TXN.AMT` | `DxCoExerciseAuto_CloseoutTxnAmt` |  |  |  |
| 46 | `DX.COAXR.BUYER` | `DxCoExerciseAuto_Buyer` |  |  |  |
| 47 | `DX.COAXR.B.FEE.TAX.TYPE` | `DxCoExerciseAuto_BFeeTaxType` |  |  |  |
| 48 | `DX.COAXR.B.FEE.TAX.CCY` | `DxCoExerciseAuto_BFeeTaxCcy` |  |  |  |
| 49 | `DX.COAXR.B.FEE.TAX.AMT` | `DxCoExerciseAuto_BFeeTaxAmt` |  |  |  |
| 50 | `DX.COAXR.B.SYS.FEE.TAX.AMT` | `DxCoExerciseAuto_BSysFeeTaxAmt` |  |  |  |
| 51 | `DX.COAXR.B.FEE.TAX.CODE` | `DxCoExerciseAuto_BFeeTaxCode` |  |  |  |
| 52 | `DX.COAXR.SELLER` | `DxCoExerciseAuto_Seller` |  |  |  |
| 53 | `DX.COAXR.S.FEE.TAX.TYPE` | `DxCoExerciseAuto_SFeeTaxType` |  |  |  |
| 54 | `DX.COAXR.S.FEE.TAX.CCY` | `DxCoExerciseAuto_SFeeTaxCcy` |  |  |  |
| 55 | `DX.COAXR.S.FEE.TAX.AMT` | `DxCoExerciseAuto_SFeeTaxAmt` |  |  |  |
| 56 | `DX.COAXR.S.SYS.FEE.TAX.AMT` | `DxCoExerciseAuto_SSysFeeTaxAmt` |  |  |  |
| 57 | `DX.COAXR.S.FEE.TAX.CODE` | `DxCoExerciseAuto_SFeeTaxCode` |  |  |  |
| 58 | `DX.COAXR.OBSERVATION.DATE` | `DxCoExerciseAuto_ObservationDate` |  |  |  |
| 59 | `DX.COAXR.OBSERVED.SPOT.RATE` | `DxCoExerciseAuto_ObservedSpotRate` |  |  |  |
| 60 | `DX.COAXR.PARTICIPATION.RATE` | `DxCoExerciseAuto_ParticipationRate` | TField | Yes | This field holds the participation rate Validation Rules: Input is mandatory when PERFORMANCE is set as YES in CONTRACT.CODE used This will be one of the selection criteria for the selection of TRANS.ID list |
| 61 | `DX.COAXR.PERFORMANCE` | `DxCoExerciseAuto_Performance` |  |  |  |
| 62 | `DX.COAXR.AVERAGE.SPOT` | `DxCoExerciseAuto_AverageSpot` | TField |  | This field holds the average spot, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FIXED.STRIKE in DX.CONTRACT.MASTER Computed as Average Spot = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 63 | `DX.COAXR.AVERAGE.STRIKE` | `DxCoExerciseAuto_AverageStrike` | TField |  | This field holds the average strike, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FLOATING.STRIKE in DX.CONTRACT.MASTER Computed as Average Strike = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 64 | `DX.COAXR.SAFEKEEP.ACCT.NO` | `DxCoExerciseAuto_SafekeepAcctNo` |  |  |  |
| 65 | `DX.COAXR.SAFEKEEP.FEE.LCY` | `DxCoExerciseAuto_SafekeepFeeLcy` |  |  |  |
| 66 | `DX.COAXR.SK.ACY.LCY.RATE` | `DxCoExerciseAuto_SkAcyLcyRate` |  |  |  |
| 67 | `DX.COAXR.SAFEKEEP.FEE.ACY` | `DxCoExerciseAuto_SafekeepFeeAcy` |  |  |  |
| 68 | `DX.COAXR.TRADE.CCY` | `DxCoExerciseAuto_TradeCcy` |  |  |  |
| 69 | `DX.COAXR.SETT.AMT.TRD.CCY` | `DxCoExerciseAuto_SettAmtTrdCcy` |  |  |  |
| 70 | `DX.COAXR.B.FEE.TAX.AC.CCY` | `DxCoExerciseAuto_BFeeTaxAcCcy` |  |  |  |
| 71 | `DX.COAXR.S.FEE.TAX.AC.CCY` | `DxCoExerciseAuto_SFeeTaxAcCcy` |  |  |  |
| 72 | `DX.COAXR.CU.SETT.ACCOUNT` | `DxCoExerciseAuto_CuSettAccount` |  |  |  |
| 73 | `DX.COAXR.CU.SETT.AC.CCY` | `DxCoExerciseAuto_CuSettAcCcy` |  |  |  |
| 74 | `DX.COAXR.SETT.AMT.AC.CCY` | `DxCoExerciseAuto_SettAmtAcCcy` |  |  |  |
| 75 | `DX.COAXR.EX.RATE.AC.CCY` | `DxCoExerciseAuto_ExRateAcCcy` |  |  |  |
