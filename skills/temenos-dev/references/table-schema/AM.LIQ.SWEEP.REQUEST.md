# AM.LIQ.SWEEP.REQUEST — Table Schema

> Source: `INSERTS/I_F.AM.LIQ.SWEEP.REQUEST` in `AM_LiquiditySweeping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.LIQ.RQ.DESCRIPTION` | `AmLiqSweepRequest_Description` | TField |  | This field can hold a short description for this AM.SWEEP.REQUEST record |
| 2 | `AM.LIQ.RQ.LONG.DESC` | `AmLiqSweepRequest_LongDesc` | TField |  | This field can hold a longer description for this AM.LIQ.SWEEP.REQUEST record |
| 3 | `AM.LIQ.RQ.CRITERIA` | `AmLiqSweepRequest_Criteria` | TField |  | This field can hold a predefined criteria record from the AM.CRITERIA application. If present this criteria will be used to initially restrict the portfolios that are selected for sweeping. |
| 4 | `AM.LIQ.RQ.FIELD` | `AmLiqSweepRequest_Field` |  |  |  |
| 5 | `AM.LIQ.RQ.OPERAND` | `AmLiqSweepRequest_Operand` |  |  |  |
| 6 | `AM.LIQ.RQ.VALUE` | `AmLiqSweepRequest_Value` |  |  |  |
| 7 | `AM.LIQ.RQ.SESSION.CCY` | `AmLiqSweepRequest_SessionCcy` | TField | Yes | This field holds the currency of the accounts to be swept. This currency will be used to identify the cash account that is to be examined. The value entered here must exist in the CURRENCY application. This field is mandatory. |
| 8 | `AM.LIQ.RQ.SECURITY.ID` | `AmLiqSweepRequest_SecurityId` | TField | Yes | This field holds a security instrument ID which must be a valid record n the SEC.ACC.MASTER application The currency of the security must match the session currency entered. This field is mandatory. |
| 9 | `AM.LIQ.RQ.FWD.FLOW.ACTIVE` | `AmLiqSweepRequest_FwdFlowActive` | TField |  | This field determines whether forward flows are to be included in the valuation of currency accounts. Setting this to Yes informs the cash management service that the value of various forward flows should be included. The number of days for each flow type can be amended elsewhere in this application and default from values entered in the AM.PARAMETER application. Available options: Yes, No |
| 10 | `AM.LIQ.RQ.COUPON.DAYS` | `AmLiqSweepRequest_CouponDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from bond coupons. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 11 | `AM.LIQ.RQ.DIVIDEND.DAYS` | `AmLiqSweepRequest_DividendDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from equity dividends. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 12 | `AM.LIQ.RQ.INTEREST.DAYS` | `AmLiqSweepRequest_InterestDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from interest payments from bonds. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 13 | `AM.LIQ.RQ.REDEMPTION.DAYS` | `AmLiqSweepRequest_RedemptionDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from bond redemptions. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 14 | `AM.LIQ.RQ.MM.DAYS` | `AmLiqSweepRequest_MmDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from money market repayments. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 15 | `AM.LIQ.RQ.FX.DAYS` | `AmLiqSweepRequest_FxDays` | TField |  | This field contains the number of working days in the future to be included when checking for cash flows resulting from FOREX contract settlements. This field will default to the value from the same field in the relevant AM.PARAMETER record |
| 16 | `AM.LIQ.RQ.OPEN.ORDERS` | `AmLiqSweepRequest_OpenOrders` | TField |  | This field is used to determine if the value of open security orders are to be considered when valuing the accounts. Setting this to Yes will have the proposed purchase price of the securities removed from the value of the appropriate currency account.. Available options: Yes, No |
| 17 | `AM.LIQ.RQ.SHORT.BALANCES` | `AmLiqSweepRequest_ShortBalances` | TField | Yes | This field is used to determine whether only accounts with a short ballance ie a balance less than 0 be considered. Setting this field to Yes means that only accounts whose total value is short shall be processed. Available options: Yes, No This field is mandatory. |
| 18 | `AM.LIQ.RQ.TRADED.DATE` | `AmLiqSweepRequest_TradedDate` | TField | Yes | This field holds the trade date that is to be used for resulting security orders. This field defaults to the system date and must not be less than this date. This field is mandatory |
| 19 | `AM.LIQ.RQ.VALUE.DATE` | `AmLiqSweepRequest_ValueDate` | TField | Yes | This field holds the value date that is to be used for resulting security orders. This field defaults to the system date plus 2 days and must be greater or equal to the traded date. This field is mandatory |
| 20 | `AM.LIQ.RQ.MIN.CASH.AMT` | `AmLiqSweepRequest_MinCashAmt` | TField |  | This field holds the required target cash value that the session currency account should be adjusted through the buying or selling of the identified security. |
| 21 | `AM.LIQ.RQ.START` | `AmLiqSweepRequest_Start` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes starts the cash management service. Available options: Yes, No |
| 22 | `AM.LIQ.RQ.CLEAR.DETAIL` | `AmLiqSweepRequest_ClearDetail` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash amnagement service that all existing AM.SWEEP.DETAIL records for this request should be deleted. This may not be set to Yes when the Recalculate field is set to Yes. Available options: Yes, No |
| 23 | `AM.LIQ.RQ.BUILD.DETAIL` | `AmLiqSweepRequest_BuildDetail` | TField |  | This field is part of the set of control fields which manage the cash management service. Setting this to Yes informs the cash management service that the criteria and parameters entered in this application should be processed and relevent AM.SWEEP.DETAIL records should be created for the proposed sweeping FOREX trades. Available options: Yes, No |
| 24 | `AM.LIQ.RQ.GENERATE.ORDER` | `AmLiqSweepRequest_GenerateOrder` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that security orders should be created for all AM.LIQ.SWEEP.DETAIL records relating to this request. AM.LIQ.SWEEP.DETAIL records that are awaiting recalculation will not be processed. Available options: Yes, No |
| 25 | `AM.LIQ.RQ.RECALCULATE` | `AmLiqSweepRequest_Recalculate` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that any AM.LIQ.SWEEP.DETAIL records that have been flagged as requiring recalculation should be picked up and recalculated. This field does not need to be used if the AM.PARAMETER field AUTO.RECALC.CM field is set to Yes Available options: Yes, No |
| 26 | `AM.LIQ.RQ.ONLINE.VALUATION` | `AmLiqSweepRequest_OnlineValuation` | TField |  | This field is part of the set of control fields which manage the cash management service Setting this to Yes informs the cash management service that any AM.LIQ.SWEEP.REQUEST records that have been flagged as requiring revaluation should be picked up and valuated. Available options: Yes, No |
| 27 | `AM.LIQ.RQ.EXCLUDE.PORTFOLIOS` | `AmLiqSweepRequest_ExcludePortfolios` |  |  |  |
| 28 | `AM.LIQ.RQ.OPERATION` | `AmLiqSweepRequest_Operation` |  |  |  |
| 29 | `AM.LIQ.RQ.ROUNDING.RULE` | `AmLiqSweepRequest_RoundingRule` |  |  |  |
| 30 | `AM.LIQ.RQ.ROUNDING.SIZE` | `AmLiqSweepRequest_RoundingSize` |  |  |  |
| 31 | `AM.LIQ.RQ.RESERVED.5` | `AmLiqSweepRequest_Reserved5` | TField |  |  |
| 32 | `AM.LIQ.RQ.RESERVED.4` | `AmLiqSweepRequest_Reserved4` | TField |  |  |
| 33 | `AM.LIQ.RQ.RESERVED.3` | `AmLiqSweepRequest_Reserved3` | TField |  |  |
| 34 | `AM.LIQ.RQ.LOCAL.REF` | `AmLiqSweepRequest_LocalRef` |  |  |  |
| 35 | `AM.LIQ.RQ.OVERRIDE` | `AmLiqSweepRequest_Override` |  |  |  |
| 36 | `AM.LIQ.RQ.RECORD.STATUS` | `AmLiqSweepRequest_RecordStatus` | String |  |  |
| 37 | `AM.LIQ.RQ.CURR.NO` | `AmLiqSweepRequest_CurrNo` | String |  |  |
| 38 | `AM.LIQ.RQ.INPUTTER` | `AmLiqSweepRequest_Inputter` |  |  |  |
| 39 | `AM.LIQ.RQ.DATE.TIME` | `AmLiqSweepRequest_DateTime` |  |  |  |
| 40 | `AM.LIQ.RQ.AUTHORISER` | `AmLiqSweepRequest_Authoriser` | String |  |  |
| 41 | `AM.LIQ.RQ.CO.CODE` | `AmLiqSweepRequest_CoCode` | String |  |  |
| 42 | `AM.LIQ.RQ.DEPT.CODE` | `AmLiqSweepRequest_DeptCode` | String |  |  |
| 43 | `AM.LIQ.RQ.AUDITOR.CODE` | `AmLiqSweepRequest_AuditorCode` | String |  |  |
| 44 | `AM.LIQ.RQ.AUDIT.DATE.TIME` | `AmLiqSweepRequest_AuditDateTime` | String |  |  |
