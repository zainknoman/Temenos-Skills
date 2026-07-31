# DX.CO.ASSIGN.AUTO — Table Schema

> Source: `INSERTS/I_F.DX.CO.ASSIGN.AUTO` in `DX_CloseoutAssign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COAAS.CONTRACT.CODE` | `DxCoAssignAuto_ContractCode` | TField |  | The contract code of the option to be expired Validation Rules: Should be valid for DX.CONTRACT.MASTER |
| 2 | `DX.COAAS.OPTION.STYLE` | `DxCoAssignAuto_OptionStyle` | TField |  | The OPTION.STYLE from the DX.CONTRACT.MASTER e.g. AMERICAN. |
| 3 | `DX.COAAS.MATURITY.DATE` | `DxCoAssignAuto_MaturityDate` | TField | Yes | The maturity / delivery month of the option to be expired. Validation Rules: Up to 11 characters in DATE format The field CONTRACT.CODE must be populated prior to this field Must be in the format: MONTHLY TRADES = Month/Year e.g. SEP00 DAILY TRADES = Day/Month/Year e.g. 15SEP00 Mandatory field |
| 4 | `DX.COAAS.DECLARATION.DATE` | `DxCoAssignAuto_DeclarationDate` | TField |  | The declaration date calculated from DX.CONTRACT.MASTER date formula. Validation Rules: NOINPUT Display date format, e.g 24 JAN 2000 |
| 5 | `DX.COAAS.STRIKE` | `DxCoAssignAuto_Strike` | TField |  | The STRIKE.PRICE of the trades to be assigned. |
| 6 | `DX.COAAS.INT.STRIKE` | `DxCoAssignAuto_IntStrike` | TField |  | Intenal strike price defaulted from STRIKE field Validation Rules: NOINPUT |
| 7 | `DX.COAAS.CALL.PUT` | `DxCoAssignAuto_CallPut` | TField | Yes | Select CALL or PUT for option series. Validation Rules: Should be one of CALL or PUT Mandatory field |
| 8 | `DX.COAAS.TOT.ASSIGN.LOTS` | `DxCoAssignAuto_TotAssignLots` | TField |  | The total number of lots which must be assigned to customers found selling this option. Validation Rules: Integer value Must be equal or less than total number of oustanding open sell lots. |
| 9 | `DX.COAAS.UNAUTH.AUTH` | `DxCoAssignAuto_UnauthAuth` | TField |  | If set as AUTHORISED this field will create all close out records with status of authorised. Validation Rules: One of AUTHORISED or UNAUTHORISED or blank |
| 10 | `DX.COAAS.CLOSEOUT.ID` | `DxCoAssignAuto_CloseoutId` |  |  |  |
| 11 | `DX.COAAS.CONTRACT.CCY` | `DxCoAssignAuto_ContractCcy` | TField | Yes | Defines the contract currency. The option trade is selected based on the contract currency. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 12 | `DX.COAAS.DELIVERY.CCY` | `DxCoAssignAuto_DeliveryCcy` | TField | Yes | Defines the delivery currency. The option trade is selected based on the delivery currency. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 13 | `DX.COAAS.STRIKE.OPERAND` | `DxCoAssignAuto_StrikeOperand` | TField |  | The operand field is used to select the trades based on the strike quote or strike price provided. Availableoperands are EQ, GEand LE |
| 14 | `DX.COAAS.STRIKE.QUOTE` | `DxCoAssignAuto_StrikeQuote` | TField |  | Holds the strike price in the quote currency which is STRIKE.QUOTE in trade. |
| 15 | `DX.COAAS.MARKET.PRICE` | `DxCoAssignAuto_MarketPrice` | TField |  | Holds the market price of the security at the time of exercise. |
| 16 | `DX.COAAS.CASH.SETTLE.CCY` | `DxCoAssignAuto_CashSettleCcy` | TField |  | Holds the delivery currency for the options with underlying as SECURITY.MASTER when the SETTLEMENT.METHOD isCASH. The exchange rate between this currency and contract currency is defined in DLV.CCY.RATE field. |
| 17 | `DX.COAAS.DLV.CCY.RATE` | `DxCoAssignAuto_DlvCcyRate` | TField |  | Holds the exchange rate between trade currency and settlement currecny. |
| 18 | `DX.COAAS.SETTLE.INSTRUMENT` | `DxCoAssignAuto_SettleInstrument` | TField |  | The alternate settlement instrument which is settled on exercise. |
| 19 | `DX.COAAS.SETT.INSTR.CONT.SIZE` | `DxCoAssignAuto_SettInstrContSize` | TField | Yes | The contract size of the alternate settlement instrument which is mandatory when settled using alternateunderlying. |
| 20 | `DX.COAAS.SETT.INSTR.PRICE` | `DxCoAssignAuto_SettInstrPrice` | TField | Yes | The price of the alternate settlement instrument which is mandatory when settled using alternate underlying. |
| 21 | `DX.COAAS.QUOTE.CCY` | `DxCoAssignAuto_QuoteCcy` | TField |  | The currency in which the SPOT.EXCHANGE.RATE is quoted. |
| 22 | `DX.COAAS.SPOT.EXCHANGE.RATE` | `DxCoAssignAuto_SpotExchangeRate` | TField |  | Holds the current exchange rate between the currency pairs of an FX option quoted in the QUOTE.CCY i.e basecurrency being the strike quote currency for generic FX-OTC options and delivery currency for fx options. |
| 23 | `DX.COAAS.FX.PAYOUT.CCY` | `DxCoAssignAuto_FxPayoutCcy` | TField |  | Currency in which the payout is to be made for FX options. |
| 24 | `DX.COAAS.SPOT.PAYOUT.RATE` | `DxCoAssignAuto_SpotPayoutRate` | TField |  | Holds the exchange rate between QUOTE.CCY and FX.PAYOUT.CCY. |
| 25 | `DX.COAAS.TRANS.ID` | `DxCoAssignAuto_TransId` |  |  |  |
| 26 | `DX.COAAS.SETTLEMENT.CCY` | `DxCoAssignAuto_SettlementCcy` |  |  |  |
| 27 | `DX.COAAS.SETTLEMENT.AMOUNT` | `DxCoAssignAuto_SettlementAmount` |  |  |  |
| 28 | `DX.COAAS.VALUE.DATE` | `DxCoAssignAuto_ValueDate` |  |  |  |
| 29 | `DX.COAAS.UNDERLYING.MAT.DATE` | `DxCoAssignAuto_UnderlyingMatDate` | TField |  |  |
| 30 | `DX.COAAS.RESERVED2` | `DxCoAssignAuto_Reserved2` | TField |  |  |
| 31 | `DX.COAAS.RESERVED1` | `DxCoAssignAuto_Reserved1` | TField |  |  |
| 32 | `DX.COAAS.LOCAL.REF` | `DxCoAssignAuto_LocalRef` |  |  |  |
| 33 | `DX.COAAS.OVERRIDE` | `DxCoAssignAuto_Override` |  |  |  |
| 34 | `DX.COAAS.RECORD.STATUS` | `DxCoAssignAuto_RecordStatus` | String |  |  |
| 35 | `DX.COAAS.CURR.NO` | `DxCoAssignAuto_CurrNo` | String |  |  |
| 36 | `DX.COAAS.INPUTTER` | `DxCoAssignAuto_Inputter` |  |  |  |
| 37 | `DX.COAAS.DATE.TIME` | `DxCoAssignAuto_DateTime` |  |  |  |
| 38 | `DX.COAAS.AUTHORISER` | `DxCoAssignAuto_Authoriser` | String |  |  |
| 39 | `DX.COAAS.CO.CODE` | `DxCoAssignAuto_CoCode` | String |  |  |
| 40 | `DX.COAAS.DEPT.CODE` | `DxCoAssignAuto_DeptCode` | String |  |  |
| 41 | `DX.COAAS.AUDITOR.CODE` | `DxCoAssignAuto_AuditorCode` | String |  |  |
| 42 | `DX.COAAS.AUDIT.DATE.TIME` | `DxCoAssignAuto_AuditDateTime` | String |  |  |
| 43 | `DX.COAAS.CLOSEOUT.TXN.AMT` | `DxCoAssignAuto_CloseoutTxnAmt` |  |  |  |
| 44 | `DX.COAAS.BUYER` | `DxCoAssignAuto_Buyer` |  |  |  |
| 45 | `DX.COAAS.B.FEE.TAX.TYPE` | `DxCoAssignAuto_BFeeTaxType` |  |  |  |
| 46 | `DX.COAAS.B.FEE.TAX.CCY` | `DxCoAssignAuto_BFeeTaxCcy` |  |  |  |
| 47 | `DX.COAAS.B.FEE.TAX.AMT` | `DxCoAssignAuto_BFeeTaxAmt` |  |  |  |
| 48 | `DX.COAAS.B.SYS.FEE.TAX.AMT` | `DxCoAssignAuto_BSysFeeTaxAmt` |  |  |  |
| 49 | `DX.COAAS.B.FEE.TAX.CODE` | `DxCoAssignAuto_BFeeTaxCode` |  |  |  |
| 50 | `DX.COAAS.SELLER` | `DxCoAssignAuto_Seller` |  |  |  |
| 51 | `DX.COAAS.S.FEE.TAX.TYPE` | `DxCoAssignAuto_SFeeTaxType` |  |  |  |
| 52 | `DX.COAAS.S.FEE.TAX.CCY` | `DxCoAssignAuto_SFeeTaxCcy` |  |  |  |
| 53 | `DX.COAAS.S.FEE.TAX.AMT` | `DxCoAssignAuto_SFeeTaxAmt` |  |  |  |
| 54 | `DX.COAAS.S.SYS.FEE.TAX.AMT` | `DxCoAssignAuto_SSysFeeTaxAmt` |  |  |  |
| 55 | `DX.COAAS.S.FEE.TAX.CODE` | `DxCoAssignAuto_SFeeTaxCode` |  |  |  |
| 56 | `DX.COAAS.OBSERVATION.DATE` | `DxCoAssignAuto_ObservationDate` |  |  |  |
| 57 | `DX.COAAS.OBSERVED.SPOT.RATE` | `DxCoAssignAuto_ObservedSpotRate` |  |  |  |
| 58 | `DX.COAAS.PARTICIPATION.RATE` | `DxCoAssignAuto_ParticipationRate` | TField | Yes | This field holds the participation rate Validation Rules: Input is mandatory when PERFORMANCE is set as YES in CONTRACT.CODE used This will be one of the selection criteria for the selection of TRANS.ID list |
| 59 | `DX.COAAS.PERFORMANCE` | `DxCoAssignAuto_Performance` |  |  |  |
| 60 | `DX.COAAS.AVERAGE.SPOT` | `DxCoAssignAuto_AverageSpot` | TField |  | This field holds the average spot, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FIXED.STRIKE in DX.CONTRACT.MASTER Computed as Average Spot = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 61 | `DX.COAAS.AVERAGE.STRIKE` | `DxCoAssignAuto_AverageStrike` | TField |  | This field holds the average strike, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FLOATING.STRIKE in DX.CONTRACT.MASTER Computed as Average Strike = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 62 | `DX.COAAS.SAFEKEEP.ACCT.NO` | `DxCoAssignAuto_SafekeepAcctNo` |  |  |  |
| 63 | `DX.COAAS.SAFEKEEP.FEE.LCY` | `DxCoAssignAuto_SafekeepFeeLcy` |  |  |  |
| 64 | `DX.COAAS.SK.ACY.LCY.RATE` | `DxCoAssignAuto_SkAcyLcyRate` |  |  |  |
| 65 | `DX.COAAS.SAFEKEEP.FEE.ACY` | `DxCoAssignAuto_SafekeepFeeAcy` |  |  |  |
| 66 | `DX.COAAS.TRADE.CCY` | `DxCoAssignAuto_TradeCcy` |  |  |  |
| 67 | `DX.COAAS.SETT.AMT.TRD.CCY` | `DxCoAssignAuto_SettAmtTrdCcy` |  |  |  |
| 68 | `DX.COAAS.B.FEE.TAX.AC.CCY` | `DxCoAssignAuto_BFeeTaxAcCcy` |  |  |  |
| 69 | `DX.COAAS.S.FEE.TAX.AC.CCY` | `DxCoAssignAuto_SFeeTaxAcCcy` |  |  |  |
| 70 | `DX.COAAS.CU.SETT.ACCOUNT` | `DxCoAssignAuto_CuSettAccount` |  |  |  |
| 71 | `DX.COAAS.CU.SETT.AC.CCY` | `DxCoAssignAuto_CuSettAcCcy` |  |  |  |
| 72 | `DX.COAAS.SETT.AMT.AC.CCY` | `DxCoAssignAuto_SettAmtAcCcy` |  |  |  |
| 73 | `DX.COAAS.EX.RATE.AC.CCY` | `DxCoAssignAuto_ExRateAcCcy` |  |  |  |
| 74 | `DX.COAAS.PARENT.CHILD.REF` | `DxCoAssignAuto_ParentChildRef` | TField |  |  |
