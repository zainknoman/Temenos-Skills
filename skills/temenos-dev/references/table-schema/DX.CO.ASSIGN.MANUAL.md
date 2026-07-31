# DX.CO.ASSIGN.MANUAL — Table Schema

> Source: `INSERTS/I_F.DX.CO.ASSIGN.MANUAL` in `DX_CloseoutAssign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COASN.TRANS.ID` | `DxCoAssignManual_TransId` |  |  |  |
| 2 | `DX.COASN.CO.LOTS` | `DxCoAssignManual_CoLots` |  |  |  |
| 3 | `DX.COASN.SETTLEMENT.CCY` | `DxCoAssignManual_SettlementCcy` |  |  |  |
| 4 | `DX.COASN.SETTLEMENT.AMOUNT` | `DxCoAssignManual_SettlementAmount` |  |  |  |
| 5 | `DX.COASN.VALUE.DATE` | `DxCoAssignManual_ValueDate` |  |  |  |
| 6 | `DX.COASN.CLOSEOUT.TXN.AMT` | `DxCoAssignManual_CloseoutTxnAmt` |  |  |  |
| 7 | `DX.COASN.BUYER` | `DxCoAssignManual_Buyer` |  |  |  |
| 8 | `DX.COASN.UNAUTH.AUTH` | `DxCoAssignManual_UnauthAuth` | TField |  | If set as AUTHORISED this field will create all close out records with status of authorised. Validation Rules: One of AUTHORISED or UNAUTHORISED or blank |
| 9 | `DX.COASN.CLOSEOUT.ID` | `DxCoAssignManual_CloseoutId` |  |  |  |
| 10 | `DX.COASN.MARKET.PRICE` | `DxCoAssignManual_MarketPrice` | TField |  | Holds the market price of the security at the time of exercise. |
| 11 | `DX.COASN.CASH.SETTLE.CCY` | `DxCoAssignManual_CashSettleCcy` | TField |  | Holds the delivery currency for the options with underlying as SECURITY.MASTER when the SETTLEMENT.METHOD isCASH. The exchange rate between this currency and contract currency is defined in DLV.CCY.RATE field. |
| 12 | `DX.COASN.DLV.CCY.RATE` | `DxCoAssignManual_DlvCcyRate` | TField |  | Holds the exchange rate between trade currency and settlement currecny. |
| 13 | `DX.COASN.SETTLE.INSTRUMENT` | `DxCoAssignManual_SettleInstrument` | TField |  | The alternate settlement instrument which is settled on exercise. |
| 14 | `DX.COASN.SETT.INSTR.CONT.SIZE` | `DxCoAssignManual_SettInstrContSize` | TField | Yes | The contract size of the alternate settlement instrument which is mandatory when settled using alternateunderlying. |
| 15 | `DX.COASN.SETT.INSTR.PRICE` | `DxCoAssignManual_SettInstrPrice` | TField | Yes | The price of the alternate settlement instrument which is mandatory when settled using alternate underlying. |
| 16 | `DX.COASN.QUOTE.CCY` | `DxCoAssignManual_QuoteCcy` | TField |  | The currency in which the SPOT.EXCHANGE.RATE is quoted. |
| 17 | `DX.COASN.SPOT.EXCHANGE.RATE` | `DxCoAssignManual_SpotExchangeRate` | TField |  | Holds the current exchange rate between the currency pairs of an FX option quoted in the QUOTE.CCY i.e basecurrency being the strike quote currency for generic FX-OTC options and delivery currency for fx options. |
| 18 | `DX.COASN.FX.PAYOUT.CCY` | `DxCoAssignManual_FxPayoutCcy` | TField |  | Currency in which the payout is to be made for FX options. |
| 19 | `DX.COASN.SPOT.PAYOUT.RATE` | `DxCoAssignManual_SpotPayoutRate` | TField |  | Holds the exchange rate between QUOTE.CCY and FX.PAYOUT.CCY. |
| 20 | `DX.COASN.RESERVED09` | `DxCoAssignManual_Reserved09` | TField |  |  |
| 21 | `DX.COASN.RESERVED08` | `DxCoAssignManual_Reserved08` | TField |  |  |
| 22 | `DX.COASN.RESERVED02` | `DxCoAssignManual_Reserved02` | TField |  |  |
| 23 | `DX.COASN.RESERVED01` | `DxCoAssignManual_Reserved01` | TField |  |  |
| 24 | `DX.COASN.LOCAL.REF` | `DxCoAssignManual_LocalRef` |  |  |  |
| 25 | `DX.COASN.OVERRIDE` | `DxCoAssignManual_Override` |  |  |  |
| 26 | `DX.COASN.RECORD.STATUS` | `DxCoAssignManual_RecordStatus` | String |  |  |
| 27 | `DX.COASN.CURR.NO` | `DxCoAssignManual_CurrNo` | String |  |  |
| 28 | `DX.COASN.INPUTTER` | `DxCoAssignManual_Inputter` |  |  |  |
| 29 | `DX.COASN.DATE.TIME` | `DxCoAssignManual_DateTime` |  |  |  |
| 30 | `DX.COASN.AUTHORISER` | `DxCoAssignManual_Authoriser` | String |  |  |
| 31 | `DX.COASN.CO.CODE` | `DxCoAssignManual_CoCode` | String |  |  |
| 32 | `DX.COASN.DEPT.CODE` | `DxCoAssignManual_DeptCode` | String |  |  |
| 33 | `DX.COASN.AUDITOR.CODE` | `DxCoAssignManual_AuditorCode` | String |  |  |
| 34 | `DX.COASN.AUDIT.DATE.TIME` | `DxCoAssignManual_AuditDateTime` | String |  |  |
| 35 | `DX.COASN.B.FEE.TAX.TYPE` | `DxCoAssignManual_BFeeTaxType` |  |  |  |
| 36 | `DX.COASN.B.FEE.TAX.CCY` | `DxCoAssignManual_BFeeTaxCcy` |  |  |  |
| 37 | `DX.COASN.B.FEE.TAX.AMT` | `DxCoAssignManual_BFeeTaxAmt` |  |  |  |
| 38 | `DX.COASN.B.SYS.FEE.TAX.AMT` | `DxCoAssignManual_BSysFeeTaxAmt` |  |  |  |
| 39 | `DX.COASN.B.FEE.TAX.CODE` | `DxCoAssignManual_BFeeTaxCode` |  |  |  |
| 40 | `DX.COASN.SELLER` | `DxCoAssignManual_Seller` |  |  |  |
| 41 | `DX.COASN.S.FEE.TAX.TYPE` | `DxCoAssignManual_SFeeTaxType` |  |  |  |
| 42 | `DX.COASN.S.FEE.TAX.CCY` | `DxCoAssignManual_SFeeTaxCcy` |  |  |  |
| 43 | `DX.COASN.S.FEE.TAX.AMT` | `DxCoAssignManual_SFeeTaxAmt` |  |  |  |
| 44 | `DX.COASN.S.SYS.FEE.TAX.AMT` | `DxCoAssignManual_SSysFeeTaxAmt` |  |  |  |
| 45 | `DX.COASN.S.FEE.TAX.CODE` | `DxCoAssignManual_SFeeTaxCode` |  |  |  |
| 46 | `DX.COASN.OBSERVATION.DATE` | `DxCoAssignManual_ObservationDate` |  |  |  |
| 47 | `DX.COASN.OBSERVED.SPOT.RATE` | `DxCoAssignManual_ObservedSpotRate` |  |  |  |
| 48 | `DX.COASN.PARTICIPATION.RATE` | `DxCoAssignManual_ParticipationRate` | TField |  | This field holds the participation rate, defaulted from DX.TRADE record Validation Rules: NOINPUT field All the TRANS.ID mentioned should have the same Participation rate, else error will be raised |
| 49 | `DX.COASN.PERFORMANCE` | `DxCoAssignManual_Performance` |  |  |  |
| 50 | `DX.COASN.AVERAGE.SPOT` | `DxCoAssignManual_AverageSpot` | TField |  | This field holds the average spot, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FIXED.STRIKE in DX.CONTRACT.MASTER Computed as Average Spot = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 51 | `DX.COASN.AVERAGE.STRIKE` | `DxCoAssignManual_AverageStrike` | TField |  | This field holds the average strike, that will be used for calculation of Settlement amount Validation Rules: Updated only when ASIAN.TYPE = FLOATING.STRIKE in DX.CONTRACT.MASTER Computed as Average Strike = 1/N * (Sum of observed spot price) where N is the number of observation dates Can be modified by user |
| 52 | `DX.COASN.SAFEKEEP.ACCT.NO` | `DxCoAssignManual_SafekeepAcctNo` |  |  |  |
| 53 | `DX.COASN.SAFEKEEP.FEE.LCY` | `DxCoAssignManual_SafekeepFeeLcy` |  |  |  |
| 54 | `DX.COASN.SK.ACY.LCY.RATE` | `DxCoAssignManual_SkAcyLcyRate` |  |  |  |
| 55 | `DX.COASN.SAFEKEEP.FEE.ACY` | `DxCoAssignManual_SafekeepFeeAcy` |  |  |  |
| 56 | `DX.COASN.TRADE.CCY` | `DxCoAssignManual_TradeCcy` |  |  |  |
| 57 | `DX.COASN.SETT.AMT.TRD.CCY` | `DxCoAssignManual_SettAmtTrdCcy` |  |  |  |
| 58 | `DX.COASN.B.FEE.TAX.AC.CCY` | `DxCoAssignManual_BFeeTaxAcCcy` |  |  |  |
| 59 | `DX.COASN.S.FEE.TAX.AC.CCY` | `DxCoAssignManual_SFeeTaxAcCcy` |  |  |  |
| 60 | `DX.COASN.CU.SETT.ACCOUNT` | `DxCoAssignManual_CuSettAccount` |  |  |  |
| 61 | `DX.COASN.CU.SETT.AC.CCY` | `DxCoAssignManual_CuSettAcCcy` |  |  |  |
| 62 | `DX.COASN.SETT.AMT.AC.CCY` | `DxCoAssignManual_SettAmtAcCcy` |  |  |  |
| 63 | `DX.COASN.EX.RATE.AC.CCY` | `DxCoAssignManual_ExRateAcCcy` |  |  |  |
| 64 | `DX.COASN.PARENT.CHILD.REF` | `DxCoAssignManual_ParentChildRef` | TField |  |  |
