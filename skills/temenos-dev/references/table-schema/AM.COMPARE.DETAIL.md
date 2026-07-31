# AM.COMPARE.DETAIL — Table Schema

> Source: `INSERTS/I_F.AM.COMPARE.DETAIL` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.CMD.DESCRIPTION` | `AmCompareDetail_Description` |  |  |  |
| 2 | `AM.CMD.SESSION` | `AmCompareDetail_Session` | TField |  | Defaulted from AM.COMPARE. The AM.COMPARE key. |
| 3 | `AM.CMD.SESSION.TYPE` | `AmCompareDetail_SessionType` | TField |  | SESSION.TYPE Defaulted from AM.COMPARE. Specifies the type of process to compare and rebalance portfolio. Accepts the values �RAISE CASH� in addition to SECURITY, CURRENCY and HEDGING. When FILE.NAME is AM.GROUP.PORT, this field allows only �RAISE CASH� and �SECURITY� Validation Rules: Alphabetic Field length increased from 8 to 10 |
| 4 | `AM.CMD.COMPARE.NO` | `AmCompareDetail_CompareNo` | TField |  | Defaults from AM.COMPARE. The AM.COMPARE id is taken from the COMPARE.CODE |
| 5 | `AM.CMD.PORTFOLIO.NO` | `AmCompareDetail_PortfolioNo` | TField |  | The portfolio being processed in this request. Taken from the AM.COMPARE.DETAILS key. |
| 6 | `AM.CMD.RBL.OUTPUT.TYPE` | `AmCompareDetail_RblOutputType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `AM.CMD.CRITERIA` | `AmCompareDetail_Criteria` | TField |  | CRITERIA Defaults from AM.COMPARE. A valid AM.CRITERIA record to use a pre-defined selection configuration. Accepts criteria record with file name as �AM.GROUP.PORT� and �ACCOUNT� The criteria entered depends on REBALANCE.LEVEL field. Validation Rules: Alpha numeric. |
| 8 | `AM.CMD.FIELD` | `AmCompareDetail_Field` |  |  |  |
| 9 | `AM.CMD.OPERAND` | `AmCompareDetail_Operand` |  |  |  |
| 10 | `AM.CMD.VALUE` | `AmCompareDetail_Value` |  |  |  |
| 11 | `AM.CMD.MATRIX` | `AmCompareDetail_Matrix` | TField |  | Defaulted from AM.COMPARE. The matrix that has been "forced" on this portfolio overiding its default from the investment program. |
| 12 | `AM.CMD.CONSOLIDATE` | `AmCompareDetail_Consolidate` | TField |  | CONSOLIDATE Defaulted from AM.COMPARE. Instruction button: Used to process a consolidate comparison of portfolios. Need to set a matrix and a currency. Input not allowed for groups Validation Rules: Alphabetic |
| 13 | `AM.CMD.CONSOLIDATE.CCY` | `AmCompareDetail_ConsolidateCcy` | TField |  | Defaulted from AM.COMPARE. The CCY involved in comparison consolidation. |
| 14 | `AM.CMD.ROUNDING.TYPE` | `AmCompareDetail_RoundingType` | TField |  | Valid rounding types are UP, DOWN and CLOSER |
| 15 | `AM.CMD.OPEN.ORDERS` | `AmCompareDetail_OpenOrders` | TField |  | Defaulted from AM.COMPARE. Records if open orders have been included in the valuation for this portfolio. |
| 16 | `AM.CMD.EXCLUDE.PORTFOLIOS` | `AmCompareDetail_ExcludePortfolios` |  |  |  |
| 17 | `AM.CMD.VALUATE.PORTFOLIO` | `AmCompareDetail_ValuatePortfolio` | TField |  | Defaulted from AM.COMPARE. Was the portfolio valuation updated "Online" during the rebalancing request. |
| 18 | `AM.CMD.COMPARE` | `AmCompareDetail_Compare` | TField |  | Defaulted from AM.COMPARE. Has the comparison process being requested for this portfolio. |
| 19 | `AM.CMD.CLEAR.SCENARIO` | `AmCompareDetail_ClearScenario` | TField |  | Defaulted from AM.COMPARE. Have the scenarios been cleared for this portfolio. |
| 20 | `AM.CMD.REBAL.SELL` | `AmCompareDetail_RebalSell` | TField |  | Defaulted from AM.COMPARE. Is rebalancing of SELL positions required. |
| 21 | `AM.CMD.REBAL.BUY` | `AmCompareDetail_RebalBuy` | TField |  | Defaulted from AM.COMPARE. Is rebalancing of BUY positions required. |
| 22 | `AM.CMD.GENERATE.ORDER` | `AmCompareDetail_GenerateOrder` | TField |  | Defaulted from AM.COMPARE. Has order generation from the scenarios proposed been requested. |
| 23 | `AM.CMD.AXIS` | `AmCompareDetail_Axis` |  |  |  |
| 24 | `AM.CMD.REBUILD.AXIS` | `AmCompareDetail_RebuildAxis` | TField |  | Defaulted from AM.COMPARE. Did the AXIS need rebuilding for this modelling session. |
| 25 | `AM.CMD.FILTER.FIELD` | `AmCompareDetail_FilterField` |  |  |  |
| 26 | `AM.CMD.FILTER.OPR` | `AmCompareDetail_FilterOpr` |  |  |  |
| 27 | `AM.CMD.FILTER.VALUE` | `AmCompareDetail_FilterValue` |  |  |  |
| 28 | `AM.CMD.FIL.SUB.FUNC` | `AmCompareDetail_FilSubFunc` |  |  |  |
| 29 | `AM.CMD.FIL.MAIN.FUNC` | `AmCompareDetail_FilMainFunc` |  |  |  |
| 30 | `AM.CMD.APPLY.FILTER` | `AmCompareDetail_ApplyFilter` | TField |  | Defaulted from AM.COMPARE. Instruction button: used to process a filter on proposed orders |
| 31 | `AM.CMD.NO.ORD.GEN` | `AmCompareDetail_NoOrdGen` | TField |  | The number of orders generated during the rebalancing session for this portfolio. |
| 32 | `AM.CMD.ORD.GEN.HOW` | `AmCompareDetail_OrdGenHow` | TField |  | A free text field detailing the type of order generated. |
| 33 | `AM.CMD.CHECK.ORDER` | `AmCompareDetail_CheckOrder` | TField |  | Defaulted from AM.COMPARE. Has constraints checking on all orders generated been requested |
| 34 | `AM.CMD.SHADOW.MODEL` | `AmCompareDetail_ShadowModel` | TField |  | SHADOW.MODEL Defaulted from AM.COMPARE. Creates a shadow model(Copy of a model prefixed with 'S-' ) based on the matrix specified in the INVESTMENT.PROGRAM. Accepts the values YES, NO and NULL. If the value is "Yes" then it creates the shadow model based on the matrix specified in the INVESTMENT.PROGRAM If the value is "No" then it uses the matrix specified in the MATRIX field. Input not allowed for groups. Validation Rules: Alphabetic |
| 35 | `AM.CMD.ONLINE.COB` | `AmCompareDetail_OnlineCob` | TField |  | Defaulted from AM.COMPARE. Details if the rebalancing session took place using an online high-volume service or during the Close of business. |
| 36 | `AM.CMD.START` | `AmCompareDetail_Start` | TField |  | Defaulted from AM.COMPARE. Always "YES" |
| 37 | `AM.CMD.SAM.CODE` | `AmCompareDetail_SamCode` |  |  |  |
| 38 | `AM.CMD.DEVIATION` | `AmCompareDetail_Deviation` |  |  |  |
| 39 | `AM.CMD.OUTBOUND` | `AmCompareDetail_Outbound` |  |  |  |
| 40 | `AM.CMD.CASH.OVERDRAFT` | `AmCompareDetail_CashOverdraft` |  |  |  |
| 41 | `AM.CMD.LAST.COMPARE` | `AmCompareDetail_LastCompare` |  |  |  |
| 42 | `AM.CMD.MANUAL.SELECTED` | `AmCompareDetail_ManualSelected` |  |  |  |
| 43 | `AM.CMD.GRID.CODE` | `AmCompareDetail_GridCode` |  |  |  |
| 44 | `AM.CMD.RESERVED.3` | `AmCompareDetail_Reserved3` |  |  |  |
| 45 | `AM.CMD.RESERVED.2` | `AmCompareDetail_Reserved2` |  |  |  |
| 46 | `AM.CMD.SCENARIO` | `AmCompareDetail_Scenario` |  |  |  |
| 47 | `AM.CMD.SCENARIO.LIST` | `AmCompareDetail_ScenarioList` | TField |  | A list of the scenarios found for this portfolio and modelling session. |
| 48 | `AM.CMD.SCENARIO.SAVED` | `AmCompareDetail_ScenarioSaved` | TField |  | A link to the scenario generated during the rebalancing session before any orders have been generated. |
| 49 | `AM.CMD.SAM.COUNTER` | `AmCompareDetail_SamCounter` | TField |  | Always "1" |
| 50 | `AM.CMD.LAST.ACTIONS` | `AmCompareDetail_LastActions` |  |  |  |
| 51 | `AM.CMD.PRICE.SET` | `AmCompareDetail_PriceSet` | TField |  | Defaulted from AM.COMPARE. The alternate price set to be used for this rebalancing session. |
| 52 | `AM.CMD.CASH.NDAYS` | `AmCompareDetail_CashNdays` | TField |  | Defaulted from AM.COMPARE. The no. days worh of projected cash added to the portfolio valuation during rebalancing. |
| 53 | `AM.CMD.PRO.ERRORS` | `AmCompareDetail_ProErrors` |  |  |  |
| 54 | `AM.CMD.SVC.MESG` | `AmCompareDetail_SvcMesg` | TField |  | Any messages from the rebalancing engine. |
| 55 | `AM.CMD.SVC.DATE` | `AmCompareDetail_SvcDate` | TField |  | The date which the rebalancing engine processed this portfolio |
| 56 | `AM.CMD.SVC.TIME` | `AmCompareDetail_SvcTime` | TField |  | Specifies the time at which the rebalancing engine completes its work. |
| 57 | `AM.CMD.SVC.WHO` | `AmCompareDetail_SvcWho` | TField |  | The T24 user that processed the request. This will be defined in the TSA.SERVICE record. |
| 58 | `AM.CMD.REBALANCE.LEVEL` | `AmCompareDetail_RebalanceLevel` | TField | Yes | Accepts any one of the following values SEC.ACC.MASTER or AM.GROUP.PORT. Validation Rules: Alphabetic Mandatory field. |
| 59 | `AM.CMD.RAISE.CASH.CCY` | `AmCompareDetail_RaiseCashCcy` |  |  |  |
| 60 | `AM.CMD.RAISE.CASH.AMT` | `AmCompareDetail_RaiseCashAmt` |  |  |  |
| 61 | `AM.CMD.RAISE.CASH.PORT` | `AmCompareDetail_RaiseCashPort` |  |  |  |
| 62 | `AM.CMD.GROUP.CODE` | `AmCompareDetail_GroupCode` | TField |  | Stores the group id to which the portfolio belongs. Associated multi-valued field along with fields starting from the field SAM.CODE till the SCENARIO field. Validation Rules: Alpha numeric NOINPUT field |
| 63 | `AM.CMD.GRP.DEVIATION` | `AmCompareDetail_GrpDeviation` | TField |  | Holds the average of differences from various cellular of each grid that belongs to a compare process. Validation Rules: Numeric NOINPUT field. |
| 64 | `AM.CMD.GRP.OUTBOUND` | `AmCompareDetail_GrpOutbound` | TField |  | Contains the number of cellular that are outbound in each grid of a compare process. Validation Rules: Numeric NOINPUT field. |
| 65 | `AM.CMD.GRP.CASH.OVERDRAFT` | `AmCompareDetail_GrpCashOverdraft` | TField |  | Updated during the compare process. Holds the number of cells in the model that has an overdraft detected for each portfolio. Validation Rules: NOINPUT field. Numeric |
| 66 | `AM.CMD.GRP.GRID.CODE` | `AmCompareDetail_GrpGridCode` | TField |  | Stores the group grid id. Associated multi-valued field along with the fields starting from SAM.CODE till the field SCENARIO. Validation Rules: Alpha numeric NOINPUT field |
| 67 | `AM.CMD.REASON.TYPE` | `AmCompareDetail_ReasonType` | TField |  | Accepts a valid code from AM.REASON.TYPE application. The short description of AM.REASON.TYPE is the encryption for this field. Validation Rules: Alphanumeric |
| 68 | `AM.CMD.REASON.TYPE.DESC` | `AmCompareDetail_ReasonTypeDesc` | TField |  | Determines why rebalancing is performed. Accepts a description that is deflated in AM.SCENARIO. Validation Rules: Alphabetic |
| 69 | `AM.CMD.RBL.ROUND.BUY` | `AmCompareDetail_RblRoundBuy` | TField |  |  |
| 70 | `AM.CMD.RBL.ROUND.SELL` | `AmCompareDetail_RblRoundSell` | TField |  |  |
| 71 | `AM.CMD.PARENT.CHILD` | `AmCompareDetail_ParentChild` | TField |  |  |
| 72 | `AM.CMD.PARENT.REFERENCE` | `AmCompareDetail_ParentReference` | TField |  |  |
| 73 | `AM.CMD.RESERVED.07` | `AmCompareDetail_Reserved07` | TField |  |  |
| 74 | `AM.CMD.RESERVED.06` | `AmCompareDetail_Reserved06` | TField |  |  |
| 75 | `AM.CMD.RESERVED.05` | `AmCompareDetail_Reserved05` | TField |  |  |
| 76 | `AM.CMD.RESERVED.04` | `AmCompareDetail_Reserved04` | TField |  |  |
| 77 | `AM.CMD.RESERVED.03` | `AmCompareDetail_Reserved03` | TField |  |  |
| 78 | `AM.CMD.RESERVED.02` | `AmCompareDetail_Reserved02` | TField |  |  |
| 79 | `AM.CMD.RESERVED.01` | `AmCompareDetail_Reserved01` | TField |  |  |
| 80 | `AM.CMD.LOCAL.REF` | `AmCompareDetail_LocalRef` |  |  |  |
| 81 | `AM.CMD.OVERRIDE` | `AmCompareDetail_Override` |  |  |  |
