# DX.CREATE.PRICE — Table Schema

> Source: `INSERTS/I_F.DX.CREATE.PRICE` in `DX_Pricing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.CMP.PRICE.SET` | `DxCreatePrice_PriceSet` | TField |  | Its valid value from DX.PRICE.SET. If the revaluation occurs during End of Exchange then PRICE.SET holds the value CLOSING. If the revaluation occurs Online then PRICE.SET holds the value CURRENT. |
| 2 | `DX.CMP.CONTRACT.CODE` | `DxCreatePrice_ContractCode` | TField |  | Its value should be a valid record in DX.CONTRACT.MASTER. |
| 3 | `DX.CMP.MATURITY.DATE` | `DxCreatePrice_MaturityDate` | TField |  | The delivery period or prompt date of the contract transacted. |
| 4 | `DX.CMP.TRADE.CCY` | `DxCreatePrice_TradeCcy` | TField |  | It is the contract currency provided in DX.CONTRACT.MASTER and any currency for FX-OTC options for which currency not defiend at contract level. |
| 5 | `DX.CMP.DELIVERY.CCY` | `DxCreatePrice_DeliveryCcy` | TField |  | It is the contract currency provided in DX.CONTRACT.MASTER and any currency for FX-OTC options for which currency not defiend at contract level. |
| 6 | `DX.CMP.OPTION.TYPE` | `DxCreatePrice_OptionType` | TField |  | It holds two values either CALL or PUT based on the trade. |
| 7 | `DX.CMP.STRIKE.PRICE` | `DxCreatePrice_StrikePrice` | TField |  | The price at which an option holder has the right to buy (Call Options) or sell (Put Options) the underlying instrument, or to cash-settle the option if appropriate, to exercise the option. |
| 8 | `DX.CMP.INT.STRIKE.PRICE` | `DxCreatePrice_IntStrikePrice` | TField |  | Internal number of ticks * tick value for strike price. |
| 9 | `DX.CMP.OPTION.STYLE` | `DxCreatePrice_OptionStyle` | TField |  | This will hold the value either American, European or Carribean options |
| 10 | `DX.CMP.EXOTIC.TYPE` | `DxCreatePrice_ExoticType` |  |  |  |
| 11 | `DX.CMP.USR.FLD.NAME` | `DxCreatePrice_UsrFldName` |  |  |  |
| 12 | `DX.CMP.USR.FLD.VAL` | `DxCreatePrice_UsrFldVal` |  |  |  |
| 13 | `DX.CMP.USR.FLD.PRICE` | `DxCreatePrice_UsrFldPrice` |  |  |  |
| 14 | `DX.CMP.QUOTE.CCY` | `DxCreatePrice_QuoteCcy` | TField |  | The currency of the quoted price in which valuation should be done. If QUOTE.CCY is Null then it defaults to TRADE.CCY. |
| 15 | `DX.CMP.QUOTE.PRICE` | `DxCreatePrice_QuotePrice` | TField |  | The new price in which revaluation should be done and is in QUOTE.CCY. |
| 16 | `DX.CMP.QUOTE.EXC` | `DxCreatePrice_QuoteExc` | TField |  | It is a NOINPUT field. The rate of exchange between the price currency and the quote currency |
| 17 | `DX.CMP.PRICE` | `DxCreatePrice_Price` | TField |  | It holds the quote currency price in which revaluation should be done and is in TRADE.CCY. |
| 18 | `DX.CMP.INT.PRICE` | `DxCreatePrice_IntPrice` | TField |  | It is the calculated internal value of PRICE |
| 19 | `DX.CMP.PRICE.KEY` | `DxCreatePrice_PriceKey` | TField |  | This is the key to this DX.MARKET.PRICE record. The record key comprises the following attributes: price set * exotic type (if applicable) / contract /contract currency / maturity date / call or put (only for options) / strike price (only for options) or P - Participation Rate (only for Performance) / delivery currency / option style * exotic option data, delimited by '/' (for exotic options only). Unique Market Price key will be generated for every combination of Observation Date used in transaction |
| 20 | `DX.CMP.PARTICIPATION.RATE` | `DxCreatePrice_ParticipationRate` | TField |  | It holds the Participation rate when PERFORMANCE is set in DX.CONTRACT.MASTER |
| 21 | `DX.CMP.OBSERVATION.DATE` | `DxCreatePrice_ObservationDate` |  |  |  |
| 22 | `DX.CMP.RESERVED.1` | `DxCreatePrice_Reserved1` |  |  |  |
| 23 | `DX.CMP.LOCAL.REF` | `DxCreatePrice_LocalRef` |  |  |  |
| 24 | `DX.CMP.OVERRIDE` | `DxCreatePrice_Override` |  |  |  |
| 25 | `DX.CMP.RECORD.STATUS` | `DxCreatePrice_RecordStatus` | String |  |  |
| 26 | `DX.CMP.CURR.NO` | `DxCreatePrice_CurrNo` | String |  |  |
| 27 | `DX.CMP.INPUTTER` | `DxCreatePrice_Inputter` |  |  |  |
| 28 | `DX.CMP.DATE.TIME` | `DxCreatePrice_DateTime` |  |  |  |
| 29 | `DX.CMP.AUTHORISER` | `DxCreatePrice_Authoriser` | String |  |  |
| 30 | `DX.CMP.CO.CODE` | `DxCreatePrice_CoCode` | String |  |  |
| 31 | `DX.CMP.DEPT.CODE` | `DxCreatePrice_DeptCode` | String |  |  |
| 32 | `DX.CMP.AUDITOR.CODE` | `DxCreatePrice_AuditorCode` | String |  |  |
| 33 | `DX.CMP.AUDIT.DATE.TIME` | `DxCreatePrice_AuditDateTime` | String |  |  |
