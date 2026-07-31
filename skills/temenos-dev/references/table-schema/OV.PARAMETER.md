# OV.PARAMETER — Table Schema

> Source: `INSERTS/I_F.OV.PARAMETER` in `OV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OV.PARAM.ONLINE.VAL` | `OvParameter_OnlineVal` | TField | Yes | Field to indicate whether automatic online valuation need to be activated for the current company or not. Validation Rules: Mandatory input. Possible value can be either YES or NO. |
| 2 | `OV.PARAM.EXC.EVENTS` | `OvParameter_ExcEvents` |  |  |  |
| 3 | `OV.PARAM.PRC.TOL.TYPE` | `OvParameter_PrcTolType` | TField |  | Field to indicate the tolerance / base level for price movements to impact the valuation Validation Rules: Single value field Possible value can be either AMOUNT or PERCENTAGE |
| 4 | `OV.PARAM.PRC.TOL.CCY` | `OvParameter_PrcTolCcy` | TField |  | Field to indicate the currency in which the tolerance amount is specified Validation Rules: Single value field Accepts valid currency. |
| 5 | `OV.PARAM.PRC.TOL` | `OvParameter_PrcTol` | TField |  | Field to indicate the tolerance amount for price changes, above which valuation need to be triggered. Validation Rules: Accepts Numeric value |
| 6 | `OV.PARAM.PORTFOLIO` | `OvParameter_Portfolio` | TField |  | Field to indicate whether online valuation is activated for all the portfolio's or not Validation Rules: Single value field and the value �ALL� denotes that the online valuation is activated for all the portfolios. |
| 7 | `OV.PARAM.BUYING.POWER` | `OvParameter_BuyingPower` | TField |  | This field is used to enable buying power Validation Rules: Will accept a value YES |
| 8 | `OV.PARAM.MARGIN.LENDING` | `OvParameter_MarginLending` | TField |  | Enable buying power calculation based on facility OR Margin Can be input only if BUYING.POWER is set "YES" Validation Rules: Will accept a value YES |
| 9 | `OV.PARAM.FACILITY` | `OvParameter_Facility` | TField |  | Maximum facility that bank will provide to increase buying power Validation Rules: A maximum of 9 numeric characters may be entered. |
| 10 | `OV.PARAM.INITIAL.MARGIN` | `OvParameter_InitialMargin` | TField |  | Margin rate used in calculation of buying power Only FACILITY or INITIAL.MARGIN can be set Validation Rules: A maximum of 9 numeric characters may be entered. |
| 11 | `OV.PARAM.MAINT.MARGIN` | `OvParameter_MaintMargin` | TField |  | Margin percentage used to calculate MAINT.MARGIN.AMT field in SEC.ACC.MASTER Can be set only if INITIAL.MARGIN is set Validation Rules: A maximum of 9 numeric characters may be entered. |
| 12 | `OV.PARAM.ADDNL.MARGIN` | `OvParameter_AddnlMargin` | TField |  | Margin percentage used to calculate ADDNL.MARGIN.AMT field in SEC.ACC.MASTER Can be set only if INITIAL.MARGIN and MAINT.MARGIN is set Validation Rules: A maximum of 9 numeric characters may be entered. |
| 13 | `OV.PARAM.ADJ.SHORT.POS` | `OvParameter_AdjShortPos` | TField | Yes | Mandatory if, MARGIN.LENDING is set as "YES". If NO, SEC.ACC.MASTER field SHORT.POS.MGN.AMT will hold the total margin value pertaining to short positions provided INITIAL.MARGIN is set Validation Rules: Possible value can be either YES or NO |
| 14 | `OV.PARAM.BUFFER` | `OvParameter_Buffer` | TField | Yes | Percentage by which margin value of portfolio will be increased before checking for margin call Validation Rules: Mandatory input. A maximum of 9 numeric characters may be entered. |
| 15 | `OV.PARAM.BASIS` | `OvParameter_Basis` | TField |  | Takes "MARKET" as value Accepts 6 alphanumeric characters |
| 16 | `OV.PARAM.TOP.UP.MGN.DAYS` | `OvParameter_TopUpMgnDays` | TField |  | Number of days before which customer should respond for top-up margin call Validation Rules: Numbers of 3 characters may be entered. |
| 17 | `OV.PARAM.SELL.OUT.MGN.DAYS` | `OvParameter_SellOutMgnDays` | TField |  | Number of days before which customer should respond for sell-out margin call Validation Rules: Numbers of 3 characters may be entered |
| 18 | `OV.PARAM.MAINT.MGN.DAYS` | `OvParameter_MaintMgnDays` | TField |  | Number of days before which customer should respond for maintenenace margin call Validation Rules: Numbers of 3 characters may be entered |
| 19 | `OV.PARAM.ADDNL.MGN.DAYS` | `OvParameter_AddnlMgnDays` | TField |  | Number of days before which customer should respond for additional margin call Validation Rules: Numbers of 3 characters may be entered |
| 20 | `OV.PARAM.USER.ROUTINE` | `OvParameter_UserRoutine` | TField |  | User routine that will be triggered to arrive at margin rate locally. |
| 21 | `OV.PARAM.MGN.CALL.EFF.DAYS` | `OvParameter_MgnCallEffDays` | TField |  | Number of days before which customer should respond for margin call Validation Rules: Numbers of 3 characters may be entered |
| 22 | `OV.PARAM.STOCK.HELD` | `OvParameter_StockHeld` | TField |  | This field indicates the number of stocks that a portfolio should hold for it to be considered a diversified portfolio. |
| 23 | `OV.PARAM.STOCK.COUNT.BASIS` | `OvParameter_StockCountBasis` | TField |  | This field allows options ALL,ELIGIBLE,RESTRICTED. a)�ALL�- All the holdings (equities, bonds and managed funds) will be considered. b)�ELIGIBLE� � All eligible stocks (SECURITY.MASTER field MARGINABLE not equal to NO) will be considered. c)RESTRICTED � when the field RESTRICTED is set to YES in SECURITY.MASTER. |
| 24 | `OV.PARAM.HOLDING.PERCENT` | `OvParameter_HoldingPercent` | TField |  | This field holds the holding cap percentage for an individual stock. |
| 25 | `OV.PARAM.HOLDING.ACTION` | `OvParameter_HoldingAction` | TField |  | Allowed values are PORTFOLIO,POSITION,EXCESS. a.PORTFOLIO � when one position breaches the holding cap,Entire portfolio will be treated as a standard portfolio and will apply standard LVRs on all the holdings. b.POSITION � When the holding cap is breached, Entire holding in the stock as standard and will apply standard LVR on that particular holding. c.EXCESS - Will treat the excess holding (in excess of the percentage specified) as standard and apply standard LVR on the excess and diversified LVR on the rest. |
| 26 | `OV.PARAM.DIVERSIF.RTN` | `OvParameter_DiversifRtn` | TField |  | User routine to modify the diversification margin amount of the porfolio. Routine should exist in PGM.FILE. |
| 27 | `OV.PARAM.BUYING.PWR.RTN` | `OvParameter_BuyingPwrRtn` | TField |  | User routine to modify the buying power amount of the porfolio.Routine should exist in PGM.FILE. |
| 28 | `OV.PARAM.ISSUER.DIVERFN` | `OvParameter_IssuerDiverfn` | TField |  | To determine whether issuer diversification should be performed based on margin value check, Net equity check OR both. Allowed values are MARGIN,EQUITY,BOTH. Cannot be set if existing field DIVERSIFICATION is setup. |
| 29 | `OV.PARAM.ISSUER.PERCENTAGE` | `OvParameter_IssuerPercentage` | TField |  | Maximum allowed percentage for issuers (above which diversification will apply say, 25 percent) |
| 30 | `OV.PARAM.APPROVED.ISSUER` | `OvParameter_ApprovedIssuer` |  |  |  |
| 31 | `OV.PARAM.EXCEPT.SUB.ASSET` | `OvParameter_ExceptSubAsset` |  |  |  |
| 32 | `OV.PARAM.NO.OF.ISSUER` | `OvParameter_NoOfIssuer` | TField |  | This field is applicable only if field ISSUER.DIVERSIFICATION is set as MARGIN or BOTH. Margin value check will be performed as a part of core valuation if number of issuer for a portfolio exceeds the setup here. However, If number of issuer is lesser than the setup done here, Core valuation will call the local API defined in ISSUER.DIVERFN.RTN to perform diversification checks. |
| 33 | `OV.PARAM.ISSUER.DIVERFN.RTN` | `OvParameter_IssuerDiverfnRtn` | TField |  | Local routine for performing issuer diversification to be specified.This will be invoked if number of issuer for a portfolio is less than the number specified in NO.OF.ISSUER field and ISSUER.DIVERSIFICATION is not set as net equity check. Should have the valid record in PGM.FILE application |
| 34 | `OV.PARAM.TOP.UP.MGN.RATE` | `OvParameter_TopUpMgnRate` | TField |  | Margin rate for top up that will be compared with security margin ratio in SEC.ACC.MASTER to determine margin call |
| 35 | `OV.PARAM.SELL.OUT.MGN.RATE` | `OvParameter_SellOutMgnRate` | TField |  | Margin rate for sell out that will be compared with security margin ratio in SEC.ACC.MASTER to determine margin call |
| 36 | `OV.PARAM.PRICING.DAYS` | `OvParameter_PricingDays` | TField |  | To hold cut of day of calculating pricing date. Margin rate will applied as zero in calculation of final margin value if backward date calculated using pricing days is greater than the DATE.LAST.PRICE field of SECURITY.MASTER. |
| 37 | `OV.PARAM.EXCEPT.ASSET` | `OvParameter_ExceptAsset` |  |  |  |
| 38 | `OV.PARAM.GLOBAL.LIMIT` | `OvParameter_GlobalLimit` | TField |  | To specify the global limit (i.e. In format 10000.xxx). Enquiry for limit utilization will pick the right limit reference by prefixing customer of portfolio based on the query run (group, individual portfolio, etc.). This will be considered if limit is not setup at subsequent levels |
| 39 | `OV.PARAM.PLEDGE.BY.PCT` | `OvParameter_PledgeByPct` | TField |  |  |
| 40 | `OV.PARAM.PRIORITY.API` | `OvParameter_PriorityApi` | TField |  | The routine defined in the field would be called before writing the trigger event data into OV.ONLINE.VAL.BULK.LIST or OV.ONLINE.VAL.FINAL.LIST table. The routine defined in the field will return 1 or 0 for Queue Prioritization. If the routine returns 1, OV.ONLINE.VAL.BULK.LIST would be updated with the trigger event, else OV.ONLINE.VAL.FINAL.LIST will be updated. The routine consists of 4 arguments listed below : �1st argument will be final list ID(incoming) 2nd argument will return either null or 1. �3rd�and 4th�arguments were reserved for future use. |
| 41 | `OV.PARAM.USE.FACILITY.APPLICATION` | `OvParameter_UseFacilityApplication` | TField |  |  |
| 42 | `OV.PARAM.RESERVED.2` | `OvParameter_Reserved2` | TField |  |  |
| 43 | `OV.PARAM.LOCAL.REF` | `OvParameter_LocalRef` |  |  |  |
| 44 | `OV.PARAM.RECORD.STATUS` | `OvParameter_RecordStatus` | String |  |  |
| 45 | `OV.PARAM.CURR.NO` | `OvParameter_CurrNo` | String |  |  |
| 46 | `OV.PARAM.INPUTTER` | `OvParameter_Inputter` |  |  |  |
| 47 | `OV.PARAM.DATE.TIME` | `OvParameter_DateTime` |  |  |  |
| 48 | `OV.PARAM.AUTHORISER` | `OvParameter_Authoriser` | String |  |  |
| 49 | `OV.PARAM.CO.CODE` | `OvParameter_CoCode` | String |  |  |
| 50 | `OV.PARAM.DEPT.CODE` | `OvParameter_DeptCode` | String |  |  |
| 51 | `OV.PARAM.AUDITOR.CODE` | `OvParameter_AuditorCode` | String |  |  |
| 52 | `OV.PARAM.AUDIT.DATE.TIME` | `OvParameter_AuditDateTime` | String |  |  |
