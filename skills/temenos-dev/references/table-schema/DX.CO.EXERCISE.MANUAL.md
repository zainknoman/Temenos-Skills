# DX.CO.EXERCISE.MANUAL — Table Schema

> Source: `INSERTS/I_F.DX.CO.EXERCISE.MANUAL` in `DX_CloseoutExercise.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COEXR.TRANS.ID` | `DxCoExerciseManual_TransId` |  |  |  |
| 2 | `DX.COEXR.CO.LOTS` | `DxCoExerciseManual_CoLots` |  |  |  |
| 3 | `DX.COEXR.SETTLEMENT.CCY` | `DxCoExerciseManual_SettlementCcy` |  |  |  |
| 4 | `DX.COEXR.SETTLEMENT.AMOUNT` | `DxCoExerciseManual_SettlementAmount` |  |  |  |
| 5 | `DX.COEXR.VALUE.DATE` | `DxCoExerciseManual_ValueDate` |  |  |  |
| 6 | `DX.COEXR.CLOSEOUT.TXN.AMT` | `DxCoExerciseManual_CloseoutTxnAmt` |  |  |  |
| 7 | `DX.COEXR.BUYER` | `DxCoExerciseManual_Buyer` |  |  |  |
| 8 | `DX.COEXR.UNAUTH.AUTH` | `DxCoExerciseManual_UnauthAuth` | TField |  | If set as AUTHORISED this field will create all close out records with status of authorised. Validation Rules: One of AUTHORISED or UNAUTHORISED or blank |
| 9 | `DX.COEXR.CLOSEOUT.ID` | `DxCoExerciseManual_CloseoutId` |  |  |  |
| 10 | `DX.COEXR.MARKET.PRICE` | `DxCoExerciseManual_MarketPrice` | TField |  | Holds the market price of the security at the time of exercise. |
| 11 | `DX.COEXR.CASH.SETTLE.CCY` | `DxCoExerciseManual_CashSettleCcy` | TField |  | Holds the delivery currency for the options with underlying as SECURITY.MASTER when the SETTLEMENT.METHOD isCASH. The exchange rate between this currency and contract currency is defined in DLV.CCY.RATE field. |
| 12 | `DX.COEXR.DLV.CCY.RATE` | `DxCoExerciseManual_DlvCcyRate` | TField |  | Holds the exchange rate between trade currency and settlement currecny. |
| 13 | `DX.COEXR.SETTLE.INSTRUMENT` | `DxCoExerciseManual_SettleInstrument` | TField |  | The alternate settlement instrument which is settled on exercise. |
| 14 | `DX.COEXR.SETT.INSTR.CONT.SIZE` | `DxCoExerciseManual_SettInstrContSize` | TField | Yes | The contract size of the alternate settlement instrument which is mandatory when settled using alternateunderlying. |
| 15 | `DX.COEXR.SETT.INSTR.PRICE` | `DxCoExerciseManual_SettInstrPrice` | TField | Yes | The price of the alternate settlement instrument which is mandatory when settled using alternate underlying. |
| 16 | `DX.COEXR.QUOTE.CCY` | `DxCoExerciseManual_QuoteCcy` | TField |  | The currency in which the SPOT.EXCHANGE.RATE is quoted. |
| 17 | `DX.COEXR.SPOT.EXCHANGE.RATE` | `DxCoExerciseManual_SpotExchangeRate` | TField |  | Holds the current exchange rate between the currency pairs of an FX option quoted in the QUOTE.CCY i.e basecurrency being the strike quote currency for generic FX-OTC options and delivery currency for fx options. |
| 18 | `DX.COEXR.FX.PAYOUT.CCY` | `DxCoExerciseManual_FxPayoutCcy` | TField |  | Currency in which the payout is to be made for FX options. |
| 19 | `DX.COEXR.SPOT.PAYOUT.RATE` | `DxCoExerciseManual_SpotPayoutRate` | TField |  | Holds the exchange rate between QUOTE.CCY and FX.PAYOUT.CCY. |
| 20 | `DX.COEXR.RESERVED05` | `DxCoExerciseManual_Reserved05` | TField |  |  |
| 21 | `DX.COEXR.RESERVED04` | `DxCoExerciseManual_Reserved04` | TField |  |  |
| 22 | `DX.COEXR.RESERVED03` | `DxCoExerciseManual_Reserved03` | TField |  |  |
| 23 | `DX.COEXR.RESERVED02` | `DxCoExerciseManual_Reserved02` | TField |  |  |
| 24 | `DX.COEXR.LOCAL.REF` | `DxCoExerciseManual_LocalRef` |  |  |  |
| 25 | `DX.COEXR.OVERRIDE` | `DxCoExerciseManual_Override` |  |  |  |
| 26 | `DX.COEXR.RECORD.STATUS` | `DxCoExerciseManual_RecordStatus` | String |  |  |
| 27 | `DX.COEXR.CURR.NO` | `DxCoExerciseManual_CurrNo` | String |  |  |
| 28 | `DX.COEXR.INPUTTER` | `DxCoExerciseManual_Inputter` |  |  |  |
| 29 | `DX.COEXR.DATE.TIME` | `DxCoExerciseManual_DateTime` |  |  |  |
| 30 | `DX.COEXR.AUTHORISER` | `DxCoExerciseManual_Authoriser` | String |  |  |
| 31 | `DX.COEXR.CO.CODE` | `DxCoExerciseManual_CoCode` | String |  |  |
| 32 | `DX.COEXR.DEPT.CODE` | `DxCoExerciseManual_DeptCode` | String |  |  |
| 33 | `DX.COEXR.AUDITOR.CODE` | `DxCoExerciseManual_AuditorCode` | String |  |  |
| 34 | `DX.COEXR.AUDIT.DATE.TIME` | `DxCoExerciseManual_AuditDateTime` | String |  |  |
| 35 | `DX.COEXR.B.FEE.TAX.TYPE` | `DxCoExerciseManual_BFeeTaxType` |  |  |  |
| 36 | `DX.COEXR.B.FEE.TAX.CCY` | `DxCoExerciseManual_BFeeTaxCcy` |  |  |  |
| 37 | `DX.COEXR.B.FEE.TAX.AMT` | `DxCoExerciseManual_BFeeTaxAmt` |  |  |  |
| 38 | `DX.COEXR.B.SYS.FEE.TAX.AMT` | `DxCoExerciseManual_BSysFeeTaxAmt` |  |  |  |
| 39 | `DX.COEXR.B.FEE.TAX.CODE` | `DxCoExerciseManual_BFeeTaxCode` |  |  |  |
| 40 | `DX.COEXR.SELLER` | `DxCoExerciseManual_Seller` |  |  |  |
| 41 | `DX.COEXR.S.FEE.TAX.TYPE` | `DxCoExerciseManual_SFeeTaxType` |  |  |  |
| 42 | `DX.COEXR.S.FEE.TAX.CCY` | `DxCoExerciseManual_SFeeTaxCcy` |  |  |  |
| 43 | `DX.COEXR.S.FEE.TAX.AMT` | `DxCoExerciseManual_SFeeTaxAmt` |  |  |  |
| 44 | `DX.COEXR.S.SYS.FEE.TAX.AMT` | `DxCoExerciseManual_SSysFeeTaxAmt` |  |  |  |
| 45 | `DX.COEXR.S.FEE.TAX.CODE` | `DxCoExerciseManual_SFeeTaxCode` |  |  |  |
| 46 | `DX.COEXR.OBSERVATION.DATE` | `DxCoExerciseManual_ObservationDate` |  |  |  |
| 47 | `DX.COEXR.OBSERVED.SPOT.RATE` | `DxCoExerciseManual_ObservedSpotRate` |  |  |  |
| 48 | `DX.COEXR.PARTICIPATION.RATE` | `DxCoExerciseManual_ParticipationRate` | TField |  | This field holds the participation rate, defaulted from DX.TRADE record Validation Rules: NOINPUT field All the TRANS.ID mentioned should have the same Participation rate, else error will be raised |
| 49 | `DX.COEXR.PERFORMANCE` | `DxCoExerciseManual_Performance` |  |  |  |
| 50 | `DX.COEXR.AVERAGE.SPOT` | `DxCoExerciseManual_AverageSpot` | TField |  | This field holds the average spot, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FIXED.STRIKE in DX.CONTRACT.MASTER Computed as Average Spot = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 51 | `DX.COEXR.AVERAGE.STRIKE` | `DxCoExerciseManual_AverageStrike` | TField |  | This field holds the average strike, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FLOATING.STRIKE in DX.CONTRACT.MASTER Computed as Average Strike = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 52 | `DX.COEXR.CREATION` | `DxCoExerciseManual_Creation` | TField |  | This field determines if the record is being generated during the COB as result of Autoexercise of Cash settledoptions Validation Rules: NOINPUT field, updated by System |
| 53 | `DX.COEXR.SAFEKEEP.ACCT.NO` | `DxCoExerciseManual_SafekeepAcctNo` |  |  |  |
| 54 | `DX.COEXR.SAFEKEEP.FEE.LCY` | `DxCoExerciseManual_SafekeepFeeLcy` |  |  |  |
| 55 | `DX.COEXR.SK.ACY.LCY.RATE` | `DxCoExerciseManual_SkAcyLcyRate` |  |  |  |
| 56 | `DX.COEXR.SAFEKEEP.FEE.ACY` | `DxCoExerciseManual_SafekeepFeeAcy` |  |  |  |
| 57 | `DX.COEXR.TRADE.CCY` | `DxCoExerciseManual_TradeCcy` |  |  |  |
| 58 | `DX.COEXR.SETT.AMT.TRD.CCY` | `DxCoExerciseManual_SettAmtTrdCcy` |  |  |  |
| 59 | `DX.COEXR.B.FEE.TAX.AC.CCY` | `DxCoExerciseManual_BFeeTaxAcCcy` |  |  |  |
| 60 | `DX.COEXR.S.FEE.TAX.AC.CCY` | `DxCoExerciseManual_SFeeTaxAcCcy` |  |  |  |
| 61 | `DX.COEXR.CU.SETT.ACCOUNT` | `DxCoExerciseManual_CuSettAccount` |  |  |  |
| 62 | `DX.COEXR.CU.SETT.AC.CCY` | `DxCoExerciseManual_CuSettAcCcy` |  |  |  |
| 63 | `DX.COEXR.SETT.AMT.AC.CCY` | `DxCoExerciseManual_SettAmtAcCcy` |  |  |  |
| 64 | `DX.COEXR.EX.RATE.AC.CCY` | `DxCoExerciseManual_ExRateAcCcy` |  |  |  |
| 65 | `DX.COEXR.PARENT.CHILD.REF` | `DxCoExerciseManual_ParentChildRef` | TField |  |  |
