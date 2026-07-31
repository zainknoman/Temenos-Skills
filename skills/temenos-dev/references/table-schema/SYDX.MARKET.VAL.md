# SYDX.MARKET.VAL — Table Schema

> Source: `INSERTS/I_F.SYDX.MARKET.VAL` in `DX_Pricing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SYDX.MKT.DEAL.REFERENCE` | `SydxMarketVal_DealReference` | TField |  | This field holds the deal id. Validation Rules: Upto 20 alpha numeric characters |
| 2 | `SYDX.MKT.TRADE.DATE` | `SydxMarketVal_TradeDate` | TField |  | This field holds trade date and this gets defaulted from the deal |
| 3 | `SYDX.MKT.MATURITY.DATE` | `SydxMarketVal_MaturityDate` | TField |  | This field holds the maturity date and this gets defaulted from the deal |
| 4 | `SYDX.MKT.VALUATION.CCY` | `SydxMarketVal_ValuationCcy` | TField |  | This is currency associated with the valuation amount |
| 5 | `SYDX.MKT.VALUATION.AMT` | `SydxMarketVal_ValuationAmt` | TField |  | Maturity date in the format yyyymmdd for daily contracts or yyyymm for monthly contracts. With the field CONTRACT.CODE defines the deals that this volatility record corresponds to. |
| 6 | `SYDX.MKT.VALOREN.NO` | `SydxMarketVal_ValorenNo` | TField |  | For equity underlying structures, VALOREN number is a unique number assigned to the structure (for e.g. by Telekurs) which would be used subsequently for pricing data. |
| 7 | `SYDX.MKT.PRICE` | `SydxMarketVal_Price` | TField |  | For equity underlying structures and options, if price per unit is available, the valuation will be derived from the price and quantity/lot size. |
| 8 | `SYDX.MKT.B2B.REFERENCE` | `SydxMarketVal_B2bReference` | TField |  | Back to Back deal number. This will be blank for the counterparty deal |
| 9 | `SYDX.MKT.COUNTERPARTY.TRADE` | `SydxMarketVal_CounterpartyTrade` | TField |  | This field signifies the deal as counterparty trade |
| 10 | `SYDX.MKT.MTM.AMOUNT` | `SydxMarketVal_MtmAmount` | TField |  |  |
| 11 | `SYDX.MKT.RESERVED.09` | `SydxMarketVal_Reserved09` | TField |  |  |
| 12 | `SYDX.MKT.RESERVED.08` | `SydxMarketVal_Reserved08` | TField |  |  |
| 13 | `SYDX.MKT.RESERVED.07` | `SydxMarketVal_Reserved07` | TField |  |  |
| 14 | `SYDX.MKT.RESERVED.06` | `SydxMarketVal_Reserved06` | TField |  |  |
| 15 | `SYDX.MKT.RESERVED.05` | `SydxMarketVal_Reserved05` | TField |  |  |
| 16 | `SYDX.MKT.RESERVED.04` | `SydxMarketVal_Reserved04` | TField |  |  |
| 17 | `SYDX.MKT.RESERVED.03` | `SydxMarketVal_Reserved03` | TField |  |  |
| 18 | `SYDX.MKT.RESERVED.02` | `SydxMarketVal_Reserved02` | TField |  |  |
| 19 | `SYDX.MKT.RESERVED.01` | `SydxMarketVal_Reserved01` | TField |  |  |
| 20 | `SYDX.MKT.LOCAL.REF` | `SydxMarketVal_LocalRef` |  |  |  |
| 21 | `SYDX.MKT.OVERRIDE` | `SydxMarketVal_Override` |  |  |  |
| 22 | `SYDX.MKT.RECORD.STATUS` | `SydxMarketVal_RecordStatus` | String |  |  |
| 23 | `SYDX.MKT.CURR.NO` | `SydxMarketVal_CurrNo` | String |  |  |
| 24 | `SYDX.MKT.INPUTTER` | `SydxMarketVal_Inputter` |  |  |  |
| 25 | `SYDX.MKT.DATE.TIME` | `SydxMarketVal_DateTime` |  |  |  |
| 26 | `SYDX.MKT.AUTHORISER` | `SydxMarketVal_Authoriser` | String |  |  |
| 27 | `SYDX.MKT.CO.CODE` | `SydxMarketVal_CoCode` | String |  |  |
| 28 | `SYDX.MKT.DEPT.CODE` | `SydxMarketVal_DeptCode` | String |  |  |
| 29 | `SYDX.MKT.AUDITOR.CODE` | `SydxMarketVal_AuditorCode` | String |  |  |
| 30 | `SYDX.MKT.AUDIT.DATE.TIME` | `SydxMarketVal_AuditDateTime` | String |  |  |
