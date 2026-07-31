# SC.ORDER.TYPE — Table Schema

> Source: `INSERTS/I_F.SC.ORDER.TYPE` in `SC_SctOrderCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ORT.DESCRIPTION` | `ScOrderType_Description` |  |  |  |
| 2 | `SC.ORT.LIMIT.PRICE` | `ScOrderType_LimitPrice` | TField | Yes | The input in this field determines the type of order which needs to be passed on to the broker. If set to YES,the order would be a Price Order with maximum/ minimum price to be specified and LIMIT PRICE would become mandatoryin order Validation Rules: YES/NO field |
| 3 | `SC.ORT.LIMIT.PRICE.CHECK` | `ScOrderType_LimitPriceCheck` | TField |  | Input to this field is allowed only when LIMIT.PRICE is set to YES. This field determines if override needs to beraised when the execution price exceeds the limit price specified in order. If YES, execution price would bechecked against LIMIT.PRICE, else no. Validation Rules: YES/NO field |
| 4 | `SC.ORT.CASH.ORDER` | `ScOrderType_CashOrder` | TField |  | Input to this field determines whether the order is a cash order or not. In case of Cash orders, input of onlycash amount in order is allowed and nominal becomes a no input field Validation Rules: YES/NO field. |
| 5 | `SC.ORT.FULL.TRADE` | `ScOrderType_FullTrade` | TField |  | Field determining whether partial execution of orders with this ORDER TYPE could be partially executed. If thisfield is set to YES and partial execution of order takes place, an override is raised Validation Rules: YES/NO field |
| 6 | `SC.ORT.SWIFT.ORDER.TYPE` | `ScOrderType_SwiftOrderType` | TField |  | The generic order type to be used in SWIFT Messages. Validation Rules: Accepted values are BEST,MARKET,STOP,PRICE and CASH |
| 7 | `SC.ORT.LOCAL.REF` | `ScOrderType_LocalRef` |  |  |  |
| 8 | `SC.ORT.SWITCH.ORDER` | `ScOrderType_SwitchOrder` | TField |  | Input to this field determines whether the order is a Switch order or not. If set to YES, it will indicate that Cash amount or nominals or percentage field can be given in SEC.OPEN.ORDER Validation Rules: YES/NO field |
| 9 | `SC.ORT.IPO.FPO` | `ScOrderType_IpoFpo` | TField |  | Input to this field determines whether the order is a IPO/FPO order or not. If set to YES, it will indicate that bid quantity and bid price can be given in SEC.OPEN.ORDER Validation Rules: YES/NO field |
| 10 | `SC.ORT.CANCEL.ORDER` | `ScOrderType_CancelOrder` | TField |  | Field to denote if the order is a cancellation of an existing trade.If set to YES, it will indicate that Cancel Trade reference can be given in SEC.OPEN.ORDER Validation Rules: YES or Blank field If this field is set, then fields SWITCH.ORDER, IPO.FPO or CASH.ORDER cannot be set to YES denoting invalid combination. |
| 11 | `SC.ORT.LIMIT.PRICE.VAL` | `ScOrderType_LimitPriceVal` | TField |  | If this field is marked as Yes, then the approximate settlement amount(VAL.IN.SETT.CCY ) of a Limit order will be calculated based on the Limit Price given in the order. Validation Rules: Allowed Values - YES or Blank Input allowed only for Limit orders. |
| 12 | `SC.ORT.STOP.ORDER` | `ScOrderType_StopOrder` | TField | Yes | Input to this field determines whether the order is a stop loss order or not. In case of stop orders, input of CURR.PRICE in SEC.OPEN.ORDER will be mandatory and it will be considered as a Stop Price. In case of Stop Limit order, if LIMIT.PRICE is set then in SEC.OPEN.ORDER input of Stop price should be entered in CURR.PRICE field and the Limit price should be entered in LIMIT.PRICE field Validation Rules: YES/NO field. |
| 13 | `SC.ORT.RESERVED.5` | `ScOrderType_Reserved5` | TField |  |  |
| 14 | `SC.ORT.RESERVED.4` | `ScOrderType_Reserved4` | TField |  |  |
| 15 | `SC.ORT.RESERVED.3` | `ScOrderType_Reserved3` | TField |  |  |
| 16 | `SC.ORT.RESERVED.2` | `ScOrderType_Reserved2` | TField |  |  |
| 17 | `SC.ORT.RESERVED.1` | `ScOrderType_Reserved1` | TField |  |  |
| 18 | `SC.ORT.OVERRIDE` | `ScOrderType_Override` |  |  |  |
| 19 | `SC.ORT.RECORD.STATUS` | `ScOrderType_RecordStatus` | String |  |  |
| 20 | `SC.ORT.CURR.NO` | `ScOrderType_CurrNo` | String |  |  |
| 21 | `SC.ORT.INPUTTER` | `ScOrderType_Inputter` |  |  |  |
| 22 | `SC.ORT.DATE.TIME` | `ScOrderType_DateTime` |  |  |  |
| 23 | `SC.ORT.AUTHORISER` | `ScOrderType_Authoriser` | String |  |  |
| 24 | `SC.ORT.CO.CODE` | `ScOrderType_CoCode` | String |  |  |
| 25 | `SC.ORT.DEPT.CODE` | `ScOrderType_DeptCode` | String |  |  |
| 26 | `SC.ORT.AUDITOR.CODE` | `ScOrderType_AuditorCode` | String |  |  |
| 27 | `SC.ORT.AUDIT.DATE.TIME` | `ScOrderType_AuditDateTime` | String |  |  |
