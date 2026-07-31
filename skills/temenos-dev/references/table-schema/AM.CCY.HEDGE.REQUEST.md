# AM.CCY.HEDGE.REQUEST — Table Schema

> Source: `INSERTS/I_F.AM.CCY.HEDGE.REQUEST` in `AM_CurrencyHedging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.HDG.RQ.DESCRIPTION` | `AmCcyHedgeRequest_Description` | TField |  | This field can hold a short description for this AM.CCY.HEDGE.REQUEST record |
| 2 | `AM.HDG.RQ.LONG.DESC` | `AmCcyHedgeRequest_LongDesc` | TField |  | This field can hold a longer description for this AM.CCY.HEDGE.REQUEST record |
| 3 | `AM.HDG.RQ.CRITERIA` | `AmCcyHedgeRequest_Criteria` | TField |  | This field can hold a predefined criteria record from the AM.CRITERIA application. If present this criteria will be used to initially restrict the portfolios that are selected for sweeping. |
| 4 | `AM.HDG.RQ.FIELD` | `AmCcyHedgeRequest_Field` |  |  |  |
| 5 | `AM.HDG.RQ.OPERAND` | `AmCcyHedgeRequest_Operand` |  |  |  |
| 6 | `AM.HDG.RQ.VALUE` | `AmCcyHedgeRequest_Value` |  |  |  |
| 7 | `AM.HDG.RQ.ASS.TYPE` | `AmCcyHedgeRequest_AssType` |  |  |  |
| 8 | `AM.HDG.RQ.SUB.ASS.TYPE` | `AmCcyHedgeRequest_SubAssType` |  |  |  |
| 9 | `AM.HDG.RQ.RESERVED.10` | `AmCcyHedgeRequest_Reserved10` | TField |  |  |
| 10 | `AM.HDG.RQ.FWD.FLOW.ACTIVE` | `AmCcyHedgeRequest_FwdFlowActive` | TField |  | This field determines whether forward flows are to be included in the valuation of currency accounts. Setting this to Yes informs the cash management service that the value of various forward flows should be included. The number of days for each flow type can be amended elsewhere in this application and default from values entered in the AM.PARAMETER application. Available options: Yes, No |
| 11 | `AM.HDG.RQ.COUPON.DAYS` | `AmCcyHedgeRequest_CouponDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from bond coupons. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 12 | `AM.HDG.RQ.DIVIDEND.DAYS` | `AmCcyHedgeRequest_DividendDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from equity dividends. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 13 | `AM.HDG.RQ.INTEREST.DAYS` | `AmCcyHedgeRequest_InterestDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from interest payments from bonds. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 14 | `AM.HDG.RQ.REDEMPTION.DAYS` | `AmCcyHedgeRequest_RedemptionDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from bond redemptions. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 15 | `AM.HDG.RQ.MM.DAYS` | `AmCcyHedgeRequest_MmDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from money market repayments. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 16 | `AM.HDG.RQ.FX.DAYS` | `AmCcyHedgeRequest_FxDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from FOREX contract settlements. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 17 | `AM.HDG.RQ.OPEN.ORDERS` | `AmCcyHedgeRequest_OpenOrders` | TField |  | This field is used to determine if the value of open security orders are to be considered when valuing the accounts. Setting this to Yes will have the proposed purchase price of the securities removed from the value of the appropriate currency account.. Available options: Yes, No |
| 18 | `AM.HDG.RQ.OPERATION.TYPE` | `AmCcyHedgeRequest_OperationType` | TField | Yes | This field determines which type of currency hedging is to take place. The Forward operation results in a single forward FOREX deal whilst the Swap operation results in a spot deal and a forward FOREX deal Available options: Forward, Swap This field is mandatory. |
| 19 | `AM.HDG.RQ.TRADED.DATE` | `AmCcyHedgeRequest_TradedDate` | TField | Yes | This field holds the trade date that is to be used for resulting FOREX orders. This field defaults to the system date and must not be less than this date. This field is mandatory |
| 20 | `AM.HDG.RQ.VALUE.DATE` | `AmCcyHedgeRequest_ValueDate` | TField | Yes | This field holds the value date that is to be used for resulting FOREX orders. This field defaults to the system date plus 2 days and must be greater or equal to the traded date. This field is mandatory |
| 21 | `AM.HDG.RQ.TXN.THRESHOLD` | `AmCcyHedgeRequest_TxnThreshold` | TField |  | This field holds the minimum amount that is to be transfered between accounts. This amount is expressed in portfolio reference currency |
| 22 | `AM.HDG.RQ.ROUNDING.SIZE` | `AmCcyHedgeRequest_RoundingSize` | TField |  | This field holds the rounding parameter to be used to determine how amounts are to be rounded. This field enables the rounding of the initial proposed nominal while capturing the sweep request. It should be a multiple of trading units given in SECURITY.MASTER application. This is applied only while capturing the request. This is not applied in case any amendments made to the intial proposed nominal. |
| 23 | `AM.HDG.RQ.MIN.CASH.AMT` | `AmCcyHedgeRequest_MinCashAmt` | TField |  | This field holds the cash value beyond which a non-portfolio currency account is considered to be exposed ie portfolio accounts not in the portfolio base currency whose values are greater than this value will be considered for hedging. This amount is expressed in system base currency |
| 24 | `AM.HDG.RQ.START` | `AmCcyHedgeRequest_Start` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes starts the cash management service. Available options: Yes, No |
| 25 | `AM.HDG.RQ.CLEAR.DETAIL` | `AmCcyHedgeRequest_ClearDetail` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that all existing AM.CCY.HEDGE.DETAIL records for this request should be deleted. This may not be set to Yes when the Recalculate field is set to Yes. Available options: Yes, No |
| 26 | `AM.HDG.RQ.BUILD.DETAIL` | `AmCcyHedgeRequest_BuildDetail` | TField |  | This field is part of the set of control fields which manage the cash management service. Setting this to Yes informs the cash management service that the criteria and parameters entered in this application should be processed and relevent AM.CCY.HEDGE.DETAIL records should be created for the proposed sweeping FOREX trades. Available options: Yes, No |
| 27 | `AM.HDG.RQ.GENERATE.ORDER` | `AmCcyHedgeRequest_GenerateOrder` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that FOREX orders should be created for all AM.CCY.HEDGE.DETAIL records relating to this request. AM.CCY.HEDGE.DETAIL records that are awaiting recalculation will not be processed. Available options: Yes, No |
| 28 | `AM.HDG.RQ.RECALCULATE` | `AmCcyHedgeRequest_Recalculate` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that any AM.CCY.HEDGE.DETAIL records that have been flagged as requiring recalculation should be picked up and recalculated. This field does not need to be used if the AM.PARAMETER field AUTO.RECALC.CM field is set to Yes Available options: Yes, No |
| 29 | `AM.HDG.RQ.ONLINE.VALUATION` | `AmCcyHedgeRequest_OnlineValuation` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that any AM.CCY.HEDGE.REQUEST records that have been flagged as requiring revaluation should be picked up and valuated. Available options: Yes, No |
| 30 | `AM.HDG.RQ.CHECKSUM` | `AmCcyHedgeRequest_Checksum` |  |  |  |
| 31 | `AM.HDG.RQ.EXCLUDE.PORTFOLIOS` | `AmCcyHedgeRequest_ExcludePortfolios` |  |  |  |
| 32 | `AM.HDG.RQ.OPERATION` | `AmCcyHedgeRequest_Operation` |  |  |  |
| 33 | `AM.HDG.RQ.ROUNDING.RULE` | `AmCcyHedgeRequest_RoundingRule` |  |  |  |
| 34 | `AM.HDG.RQ.START.HEDGE.PRE` | `AmCcyHedgeRequest_StartHedgePre` | TField |  |  |
| 35 | `AM.HDG.RQ.RESERVED.4` | `AmCcyHedgeRequest_Reserved4` | TField |  |  |
| 36 | `AM.HDG.RQ.RESERVED.3` | `AmCcyHedgeRequest_Reserved3` | TField |  |  |
| 37 | `AM.HDG.RQ.LOCAL.REF` | `AmCcyHedgeRequest_LocalRef` |  |  |  |
| 38 | `AM.HDG.RQ.OVERRIDE` | `AmCcyHedgeRequest_Override` |  |  |  |
| 39 | `AM.HDG.RQ.PORT.ID` | `AmCcyHedgeRequest_PortId` |  |  |  |
| 40 | `AM.HDG.RQ.POS.ID` | `AmCcyHedgeRequest_PosId` |  |  |  |
| 41 | `AM.HDG.RQ.POS.DESC` | `AmCcyHedgeRequest_PosDesc` |  |  |  |
| 42 | `AM.HDG.RQ.POS.CCY` | `AmCcyHedgeRequest_PosCcy` |  |  |  |
| 43 | `AM.HDG.RQ.POS.PORT.ID` | `AmCcyHedgeRequest_PosPortId` |  |  |  |
| 44 | `AM.HDG.RQ.POS.AST` | `AmCcyHedgeRequest_PosAst` |  |  |  |
| 45 | `AM.HDG.RQ.POS.SAT` | `AmCcyHedgeRequest_PosSat` |  |  |  |
| 46 | `AM.HDG.RQ.RESERVED.11` | `AmCcyHedgeRequest_Reserved11` |  |  |  |
| 47 | `AM.HDG.RQ.POS.VEX.ID` | `AmCcyHedgeRequest_PosVexId` |  |  |  |
| 48 | `AM.HDG.RQ.RESERVED.12` | `AmCcyHedgeRequest_Reserved12` |  |  |  |
| 49 | `AM.HDG.RQ.EXTRA.VEX.ID` | `AmCcyHedgeRequest_ExtraVexId` |  |  |  |
| 50 | `AM.HDG.RQ.RESERVED.13` | `AmCcyHedgeRequest_Reserved13` |  |  |  |
| 51 | `AM.HDG.RQ.RECORD.STATUS` | `AmCcyHedgeRequest_RecordStatus` | String |  |  |
| 52 | `AM.HDG.RQ.CURR.NO` | `AmCcyHedgeRequest_CurrNo` | String |  |  |
| 53 | `AM.HDG.RQ.INPUTTER` | `AmCcyHedgeRequest_Inputter` |  |  |  |
| 54 | `AM.HDG.RQ.DATE.TIME` | `AmCcyHedgeRequest_DateTime` |  |  |  |
| 55 | `AM.HDG.RQ.AUTHORISER` | `AmCcyHedgeRequest_Authoriser` | String |  |  |
| 56 | `AM.HDG.RQ.CO.CODE` | `AmCcyHedgeRequest_CoCode` | String |  |  |
| 57 | `AM.HDG.RQ.DEPT.CODE` | `AmCcyHedgeRequest_DeptCode` | String |  |  |
| 58 | `AM.HDG.RQ.AUDITOR.CODE` | `AmCcyHedgeRequest_AuditorCode` | String |  |  |
| 59 | `AM.HDG.RQ.AUDIT.DATE.TIME` | `AmCcyHedgeRequest_AuditDateTime` | String |  |  |
