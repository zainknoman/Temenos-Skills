# AM.COMPARE — Table Schema

> Source: `INSERTS/I_F.AM.COMPARE` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.COM.DESCRIPTION` | `AmCompare_Description` |  |  |  |
| 2 | `AM.COM.SESSION` | `AmCompare_Session` | TField |  | A duplicate of COMPARE.CODE used as a unique rebalancing session ID&gt; |
| 3 | `AM.COM.SESSION.TYPE` | `AmCompare_SessionType` | TField |  | Specifies the type of process to compare and rebalance portfolio. Accepts the values �RAISE CASH� in addition to SECURITY, CURRENCY and HEDGING. When FILE.NAME is AM.GROUP.PORT, this field allows only �RAISE CASH� and �SECURITY� Validation Rules: Alphabetic Field length increased from 8 to 10 |
| 4 | `AM.COM.COMPARE.NO` | `AmCompare_CompareNo` | TField |  | A duplicate field which holds the COMPARE.CODE. |
| 5 | `AM.COM.PORTFOLIO.NO` | `AmCompare_PortfolioNo` | TField |  | Not used in this application see AM.COMPARE.DETAILS |
| 6 | `AM.COM.RBL.OUTPUT.TYPE` | `AmCompare_RblOutputType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `AM.COM.CRITERIA` | `AmCompare_Criteria` | TField |  | A valid AM.CRITERIA record to use a pre-defined selection configuration. Accepts criteria record with file name as 'AM.GROUP.PORT' and 'ACCOUNT' The criteria entered depends on REBALANCE.LEVEL field. Validation Rules: Alpha numeric. |
| 8 | `AM.COM.FIELD` | `AmCompare_Field` |  |  |  |
| 9 | `AM.COM.OPERAND` | `AmCompare_Operand` |  |  |  |
| 10 | `AM.COM.VALUE` | `AmCompare_Value` |  |  |  |
| 11 | `AM.COM.MATRIX` | `AmCompare_Matrix` | TField |  | Instruction button: used to process consolidated comparison on selected portfolios. It defines the common matrix process to be used. |
| 12 | `AM.COM.CONSOLIDATE` | `AmCompare_Consolidate` | TField |  | Instruction button: Used to process a consolidate comparison of portfolios. Need to set a matrix and a currency. Input not allowed for groups Validation Rules: Alphabetic |
| 13 | `AM.COM.CONSOLIDATE.CCY` | `AmCompare_ConsolidateCcy` | TField | Yes | Defines the common currency to be used and displayed in the consolidated comparison process of selected portfolios. Mandatory if CONSOLIDATE field is set to YES. |
| 14 | `AM.COM.ROUNDING.TYPE` | `AmCompare_RoundingType` | TField |  | Specifies rounding of nominals. UP: the nominal is to be rounded to the closest round lot above the target. DOWN: the nominal is to be rounded to the closest round lot below the target. CLOSER: the nominal is to be rounded up or down to the closest rounding lot depending on whichever is closer to the target. |
| 15 | `AM.COM.OPEN.ORDERS` | `AmCompare_OpenOrders` | TField |  | If selected this will include open orders in the valuation for the portfolio. It is only possible to select YES for this field if the parameter file is configured to allow open orders. |
| 16 | `AM.COM.EXCLUDE.PORTFOLIOS` | `AmCompare_ExcludePortfolios` |  |  |  |
| 17 | `AM.COM.VALUATE.PORTFOLIO` | `AmCompare_ValuatePortfolio` | TField |  | Instruction button: used to launch an online valuation of portfolios. |
| 18 | `AM.COM.COMPARE` | `AmCompare_Compare` | TField |  | Instruction button: Used to process comparison on selected portfolios. |
| 19 | `AM.COM.CLEAR.SCENARIO` | `AmCompare_ClearScenario` | TField |  | Instruction button: Used to process a clear on scenarios. Only "ALL", "BUY", "SELL", "FLOW" or "FOREX" can be entered This process is not allowed in a mass comparison (CONSOLIDATE field set to YES) |
| 20 | `AM.COM.REBAL.SELL` | `AmCompare_RebalSell` | TField |  | Instruction button: used to process rebalancing routine and proposed orders. |
| 21 | `AM.COM.REBAL.BUY` | `AmCompare_RebalBuy` | TField |  | Instruction button: Used to process rebalancing routine and proposed orders. |
| 22 | `AM.COM.GENERATE.ORDER` | `AmCompare_GenerateOrder` | TField |  | Instruction button: used to process the generating of orders. |
| 23 | `AM.COM.AXIS` | `AmCompare_Axis` |  |  |  |
| 24 | `AM.COM.REBUILD.AXIS` | `AmCompare_RebuildAxis` | TField |  | Instruction button: Used to rebuild AM.AXIS.MEMBER concat file. This concat file is used by enquiry "Eligible list" and by rebalancing buying routine. |
| 25 | `AM.COM.FILTER.FIELD` | `AmCompare_FilterField` |  |  |  |
| 26 | `AM.COM.FILTER.OPR` | `AmCompare_FilterOpr` |  |  |  |
| 27 | `AM.COM.FILTER.VALUE` | `AmCompare_FilterValue` |  |  |  |
| 28 | `AM.COM.FIL.SUB.FUNC` | `AmCompare_FilSubFunc` |  |  |  |
| 29 | `AM.COM.FIL.MAIN.FUNC` | `AmCompare_FilMainFunc` |  |  |  |
| 30 | `AM.COM.APPLY.FILTER` | `AmCompare_ApplyFilter` | TField |  | Instruction button: used to process a filter on proposed orders |
| 31 | `AM.COM.NO.ORD.GEN` | `AmCompare_NoOrdGen` | TField |  | Not used in this application see AM.COMPARE.DETAILS |
| 32 | `AM.COM.ORD.GEN.HOW` | `AmCompare_OrdGenHow` | TField |  | Not used in this application see AM.COMPARE.DETAILS |
| 33 | `AM.COM.CHECK.ORDER` | `AmCompare_CheckOrder` | TField |  | Request constraints checking on all orders generated. |
| 34 | `AM.COM.SHADOW.MODEL` | `AmCompare_ShadowModel` | TField |  | Creates a shadow model(Copy of a model prefixed with 'S-' ) based on the matrix specified in the INVESTMENT.PROGRAM. Accepts the values YES, NO and NULL. If the value is "Yes" then it creates the shadow model based on the matrix specified in the INVESTMENT.PROGRAM If the value is "No" then it uses the matrix specified in the MATRIX field. Input not allowed for groups. Validation Rules: Alphabetic |
| 35 | `AM.COM.ONLINE.COB` | `AmCompare_OnlineCob` | TField |  | Defines whether the rebalancing request should be processed by an online service or during the close of buisiness. |
| 36 | `AM.COM.START` | `AmCompare_Start` | TField |  | Set to "YES" ths will request a rebalancing session to be requested. |
| 37 | `AM.COM.SAM.CODE` | `AmCompare_SamCode` |  |  |  |
| 38 | `AM.COM.DEVIATION` | `AmCompare_Deviation` |  |  |  |
| 39 | `AM.COM.OUTBOUND` | `AmCompare_Outbound` |  |  |  |
| 40 | `AM.COM.CASH.OVERDRAFT` | `AmCompare_CashOverdraft` |  |  |  |
| 41 | `AM.COM.LAST.COMPARE` | `AmCompare_LastCompare` |  |  |  |
| 42 | `AM.COM.MANUAL.SELECTED` | `AmCompare_ManualSelected` |  |  |  |
| 43 | `AM.COM.GRID.CODE` | `AmCompare_GridCode` |  |  |  |
| 44 | `AM.COM.RESERVED.3` | `AmCompare_Reserved3` |  |  |  |
| 45 | `AM.COM.RESERVED.2` | `AmCompare_Reserved2` |  |  |  |
| 46 | `AM.COM.SCENARIO` | `AmCompare_Scenario` |  |  |  |
| 47 | `AM.COM.SCENARIO.LIST` | `AmCompare_ScenarioList` | TField |  | Not used in this application see AM.COMPARE.DETAILS |
| 48 | `AM.COM.SCENARIO.SAVED` | `AmCompare_ScenarioSaved` | TField |  | Not used in this application see AM.COMPARE.DETAILS |
| 49 | `AM.COM.SAM.COUNTER` | `AmCompare_SamCounter` | TField |  | The number of portfolios selected for processing. Update after the service has processed the selection. |
| 50 | `AM.COM.LAST.ACTIONS` | `AmCompare_LastActions` |  |  |  |
| 51 | `AM.COM.PRICE.SET` | `AmCompare_PriceSet` | TField |  | An alternative set of prices to use. Defined in AM.PRICE.SET |
| 52 | `AM.COM.CASH.NDAYS` | `AmCompare_CashNdays` | TField |  | The portfolio valuation is based on the trade date + the projected cash at n days. Projected cash can be set from 0 to 5 days. |
| 53 | `AM.COM.PRO.ERRORS` | `AmCompare_ProErrors` |  |  |  |
| 54 | `AM.COM.SVC.MESG` | `AmCompare_SvcMesg` | TField |  | A free-text message from the processing engine. |
| 55 | `AM.COM.SVC.DATE` | `AmCompare_SvcDate` | TField |  | The date on which the request to run a rebalancing session was requested. |
| 56 | `AM.COM.SVC.TIME` | `AmCompare_SvcTime` | TField |  | The time at which the request to run a rebalancing session was requested. |
| 57 | `AM.COM.SVC.WHO` | `AmCompare_SvcWho` | TField |  | The user/process that has requested the rebalancing session. |
| 58 | `AM.COM.REBALANCE.LEVEL` | `AmCompare_RebalanceLevel` | TField | Yes | Accepts any one of the following values SEC.ACC.MASTER or AM.GROUP.PORT. Validation Rules: Alphabetic Mandatory field. |
| 59 | `AM.COM.RAISE.CASH.CCY` | `AmCompare_RaiseCashCcy` |  |  |  |
| 60 | `AM.COM.RAISE.CASH.AMT` | `AmCompare_RaiseCashAmt` |  |  |  |
| 61 | `AM.COM.RAISE.CASH.PORT` | `AmCompare_RaiseCashPort` |  |  |  |
| 62 | `AM.COM.GROUP.CODE` | `AmCompare_GroupCode` | TField |  | Stores the group id to which the portfolio belongs. Associated multi-valued field along with fields starting from the field SAM.CODE till the SCENARIO field. Validation Rules: Alpha numeric NOINPUT field |
| 63 | `AM.COM.GRP.DEVIATION` | `AmCompare_GrpDeviation` | TField |  | Holds the average of differences from various cellular of each grid that belongs to a compare process. Validation Rules: Numeric NOINPUT field. |
| 64 | `AM.COM.GRP.OUTBOUND` | `AmCompare_GrpOutbound` | TField |  | Contains the number of cellular that are outbound in each grid of a compare process. Validation Rules: Numeric NOINPUT field. |
| 65 | `AM.COM.GRP.CASH.OVERDRAFT` | `AmCompare_GrpCashOverdraft` | TField |  | Updated during the compare process. Holds the number of cells in the model that has an overdraft detected for each portfolio. Validation Rules: NOINPUT field. Numeric |
| 66 | `AM.COM.GRP.GRID.CODE` | `AmCompare_GrpGridCode` | TField |  | Stores the group grid id. Associated multi-valued field along with the fields starting from SAM.CODE till the field SCENARIO. Validation Rules: Alpha numeric NOINPUT field |
| 67 | `AM.COM.REASON.TYPE` | `AmCompare_ReasonType` | TField |  | Accepts a valid code from AM.REASON.TYPE application. The short description of AM.REASON.TYPE is the encryption for this field. Validation Rules: Alphanumeric |
| 68 | `AM.COM.REASON.TYPE.DESC` | `AmCompare_ReasonTypeDesc` | TField |  | Determines why rebalancing is performed. Accepts a description that is deflated in AM.SCENARIO. Validation Rules: Alphabetic |
| 69 | `AM.COM.RBL.ROUND.BUY` | `AmCompare_RblRoundBuy` | TField |  | RBL.ROUND.BUY Specifies rounding rules to calculate the nominal of BUY orders, generated through rebalancing. Automatically defaults the values from RBL.ROUND.BUY field of AM.PARAMETER. Validation Rules: Accepts any one of the following values �UP� or �DOWN� or �CLOSER� UP: The nominal is rounded to the closest round lot above the target. DOWN: The nominal is rounded to the closest round lot below the target. CLOSER: The nominal is rounded up or down to the closest rounding lot dependingon whichever is closer to the target. If the value of RBL.ROUND.BUY in AM.PARAMETER is null then Rebalancing will consider the value given in ROUNDING.TYPE of AM.COMPARE or ROUNDING.TYPE of AM.PARAMETER |
| 70 | `AM.COM.RBL.ROUND.SELL` | `AmCompare_RblRoundSell` | TField |  | RBL.ROUND.SELL Specifies rounding rules to calculate the nominal of SELL orders, generated through rebalancing. Automatically defaults the values from RBL.ROUND.SELL field of AM.PARAMETER. Validation Rules: Accepts any one of the following values �UP� or �DOWN� or �CLOSER� UP: The nominal is rounded to the closest round lot above the target. DOWN: The nominal is rounded to the closest round lot below the target. CLOSER: The nominal is rounded up or down to the closest rounding lot dependingon whichever is closer to the target. If the value of RBL.ROUND.SELL in AM.PARAMETER is null then Rebalancing will consider the value given in ROUNDING.TYPE of AM.COMPARE or ROUNDING.TYPE of AM.PARAMETER |
| 71 | `AM.COM.PARENT.CHILD` | `AmCompare_ParentChild` | TField |  | This field is used to generate parent child SEC.OPEN.ORDERS and will accept a value YES. Parent order will be generated for each security and all the portfolio under that security will be individual child orders. This field is allowed only for portfolio rebalancing and not for group rebalancing. Validation Rules: Alphabetical characters |
| 72 | `AM.COM.PARENT.REFERENCE` | `AmCompare_ParentReference` | TField |  | The parent reference provided in this field will form part of the common reference between parent and child. Validation Rules Alphabetical characters A maximum of 21 characters may be entered |
| 73 | `AM.COM.RESERVED.07` | `AmCompare_Reserved07` | TField |  | Reserved for future |
| 74 | `AM.COM.RESERVED.06` | `AmCompare_Reserved06` | TField |  | Reserved for future |
| 75 | `AM.COM.RESERVED.05` | `AmCompare_Reserved05` | TField |  | Reserved for future |
| 76 | `AM.COM.RESERVED.04` | `AmCompare_Reserved04` | TField |  | Reserved for future |
| 77 | `AM.COM.RESERVED.03` | `AmCompare_Reserved03` | TField |  | Reserved for future |
| 78 | `AM.COM.RESERVED.02` | `AmCompare_Reserved02` | TField |  | Reserved for future |
| 79 | `AM.COM.RESERVED.01` | `AmCompare_Reserved01` | TField |  |  |
| 80 | `AM.COM.LOCAL.REF` | `AmCompare_LocalRef` |  |  |  |
| 81 | `AM.COM.OVERRIDE` | `AmCompare_Override` |  |  |  |
| 82 | `AM.COM.RECORD.STATUS` | `AmCompare_RecordStatus` | String |  |  |
| 83 | `AM.COM.CURR.NO` | `AmCompare_CurrNo` | String |  |  |
| 84 | `AM.COM.INPUTTER` | `AmCompare_Inputter` |  |  |  |
| 85 | `AM.COM.DATE.TIME` | `AmCompare_DateTime` |  |  |  |
| 86 | `AM.COM.AUTHORISER` | `AmCompare_Authoriser` | String |  |  |
| 87 | `AM.COM.CO.CODE` | `AmCompare_CoCode` | String |  |  |
| 88 | `AM.COM.DEPT.CODE` | `AmCompare_DeptCode` | String |  |  |
| 89 | `AM.COM.AUDITOR.CODE` | `AmCompare_AuditorCode` | String |  |  |
| 90 | `AM.COM.AUDIT.DATE.TIME` | `AmCompare_AuditDateTime` | String |  |  |
