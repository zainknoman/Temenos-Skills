# FX.LIM.ORDER — Table Schema

> Source: `INSERTS/I_F.FX.LIM.ORDER` in `FX_LimitOrder.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.LO.LIM.ORDER.TYPE` | `FxLimOrder_LimOrderType` | TField |  | This field value if left null is a regular FX.LIM.ORDER This field value if set to "INT" then this is a internal order done through TPS |
| 2 | `FX.LO.INT.TYPE.REF` | `FxLimOrder_IntTypeRef` | TField |  | Will have the reference number of the TPS when the LIM.ORDER.TYPE is set as "INT" |
| 3 | `FX.LO.INT.RATE.UTILIZED` | `FxLimOrder_IntRateUtilized` | TField |  | This field will have a value only when LIM.ORDER.TYPE is set as "INT" Set as Y when the rate provided is utilized by TPS and N when the rate is not utilized |
| 4 | `FX.LO.DEAL.TYPE` | `FxLimOrder_DealType` | TField | Yes | This field should contain the type of FOREX deal to be created by the order Validation Rules: Valid inputs are SP - Spot, FW - Forward , SW - Swap Mandatory, No-change field |
| 5 | `FX.LO.COUNTERPARTY` | `FxLimOrder_Counterparty` | TField | Yes | This field should contain the customer reference for whom the FX Order has been undertaken Validation Rules: Must be a valid Customer id, present in CUSTOMER table Mandatory, No-change field |
| 6 | `FX.LO.ORDER.CCY` | `FxLimOrder_OrderCcy` | TField | Yes | This field should contain the currency in which the FX ORDER has been placed Validation Rules: Must be a valid record in CURRENCY table Mandatory, No-change field |
| 7 | `FX.LO.CONTRA.CCY` | `FxLimOrder_ContraCcy` | TField | Yes | This field should contain the other currency of the FX ORDER placed by the customer Validation Rules: Must be a valid record in CURRENCY table Mandatory, No-change field |
| 8 | `FX.LO.VALUE.DATE` | `FxLimOrder_ValueDate` | TField | Yes | This field should contain the value date for SP, FW and 1st leg of SW type contracts Validation Rules: Absolute date as YYYYMMDD Codes like T, TO, S, nnD, nnW, nnM, nnY Mandatory. Can be modified until execution for first time |
| 9 | `FX.LO.VALUE.DATE2` | `FxLimOrder_ValueDate2` | TField | Yes | This field should contain the Value date for 2nd leg of SW type contracts Validation Rules: Absolute date as YYYYMMDD Codes like nnD, nnW, nnM, nnY Mandatory for deal type SW, otherwise input not allowed Can be modified until execution for first time |
| 10 | `FX.LO.EXPIRY.DATE` | `FxLimOrder_ExpiryDate` | TField | Yes | This field should contain expiry date of the FX Order, in local time zone Validation Rules: Standard T24 date format Mandatory if GTC is null Not allowed if GTC is YES Can be modified until execution for first time |
| 11 | `FX.LO.EXPIRY.TIME` | `FxLimOrder_ExpiryTime` | TField | Yes | This field should contain expiry time of the FX Order contract, in local time zone Validation Rules: 24 hour time format: HH:MM Mandatory if GTC is null Not allowed if GTC is YES Can be modified until execution for first time |
| 12 | `FX.LO.GTC` | `FxLimOrder_Gtc` | TField |  | This field denotes that FX ORDER is Good till Cancellation. Therefore, system will not expire the order based on EXPIRY.DATE and EXPIRY.TIME but has to be expired manually Validation Rules: Valid inputs 'YES' or NULL Can be modified until execution for first time |
| 13 | `FX.LO.ORDER.TYPE` | `FxLimOrder_OrderType` | TField | Yes | This field contains definitions for overall type of order, which can be any of the following : Single order - only one order item may be input If done order - exactly two order items must be input Revolving order - exactly two order item must be input Validation Rules: Valid inputs are SINGLE,IFDONE or REVOL Mandatory and can be modified until execution for first time |
| 14 | `FX.LO.BUY.SELL` | `FxLimOrder_BuySell` |  |  |  |
| 15 | `FX.LO.ORDER.ITEM.TYPE` | `FxLimOrder_OrderItemType` |  |  |  |
| 16 | `FX.LO.ORDER.AMT` | `FxLimOrder_OrderAmt` |  |  |  |
| 17 | `FX.LO.CONTRA.AMT` | `FxLimOrder_ContraAmt` |  |  |  |
| 18 | `FX.LO.REQD.LO.RATE` | `FxLimOrder_ReqdLoRate` |  |  |  |
| 19 | `FX.LO.REQD.HI.RATE` | `FxLimOrder_ReqdHiRate` |  |  |  |
| 20 | `FX.LO.ORD.ITEM.STATUS` | `FxLimOrder_OrdItemStatus` |  |  |  |
| 21 | `FX.LO.LIMIT.REFERENCE` | `FxLimOrder_LimitReference` | TField |  | This field should contain the LIMIT reference corresponding to the Order Validation Rules: Should be a valid LIMIT.REFERENCE record Inputtable field if left null will be system defaulted |
| 22 | `FX.LO.OUR.ACCOUNT.PAY` | `FxLimOrder_OurAccountPay` | TField |  | This field should contain the account number details through which the currency sold is to be settled. This information is carried forward to the FOREX record created on execution of the FX.ORDER Validation Rules: Should be a valid record in ACCOUNT application |
| 23 | `FX.LO.OUR.ACCOUNT.REC` | `FxLimOrder_OurAccountRec` | TField |  | This field should contain the account number details through which the currency purchased is to be settled. This information is carried forward to the FOREX record created on execution of the FX.ORDER Validation Rules: Should be a valid record in ACCOUNT application |
| 24 | `FX.LO.CPARTY.CORR.NO` | `FxLimOrder_CpartyCorrNo` | TField |  | This field contains details of the bank to which the counterparty wishes the amount sold by T24 bank to be delivered. This can either be counterpartys bank or the bank of their nominated beneficiary. This information is carried forward to the FOREX record created on execution of the FX.ORDER Validation Rules: Must be a valid record in CUSTOMER application |
| 25 | `FX.LO.CPARTY.CORR.ADD` | `FxLimOrder_CpartyCorrAdd` | TField |  | Validation Rules: |
| 26 | `FX.LO.DEALER.DESK` | `FxLimOrder_DealerDesk` | TField |  | Indicates the dealer desk selected on the contract. Validation Rules: A maximum of 2 characters may be entered. Standard T24 numeric field. |
| 27 | `FX.LO.ACCOUNT.OFFICER` | `FxLimOrder_AccountOfficer` | TField |  | Identifies the account officer responsible for the relationship with the customer. Validation Rules: 1-4 Digit numeric field. The Account Officer Code must appear on the DEPT.ACCT.OFFICER table. |
| 28 | `FX.LO.EXEC.RATE` | `FxLimOrder_ExecRate` | TField | Yes | This field holds the execution Rate of the order. Validation Rules: This is a mandatory input field only when the EXECUTE.ORDER field is set to YES For Internal Rate Requests when the dealer provides the EXEC.RATE system will check the rate against that on the CURRENCY table. If outside the specified tolerance in the CURRENCY/ COMPANY table, the dealer will be asked to confirm the rate by accepting an override. |
| 29 | `FX.LO.EXEC.FWD.RATE` | `FxLimOrder_ExecFwdRate` | TField | Yes | This field holds the execution rate for the forward leg of the FX swap deal. Validation Rules: This is a mandatory input field when EXPIRE.ORDER field is set to YES. |
| 30 | `FX.LO.EXECUTE.ORDER` | `FxLimOrder_ExecuteOrder` | TField |  | The field is set to YES on the expiry date to execute the order. Validation Rules: If CANCEL.ORDER or EXPIRE.ORDER is set to YES, then this cannot be enabled. Input is allowed only when the contract is authorized. If this field is set to YES then no further executions are allowed. |
| 31 | `FX.LO.CANCEL.ORDER` | `FxLimOrder_CancelOrder` | TField |  | This field is set to YES when the order needs to be cancelled. Validation Rules: If EXECUTE.ORDER or EXPIRE.ORDER is set to YES then this field cannot be set to YES. Input is allowed only after the authorization of the contract. IF this field is set to YES, No further executions are allowed. |
| 32 | `FX.LO.EXPIRE.ORDER` | `FxLimOrder_ExpireOrder` | TField |  | The field is set to YES on the expiry date to expire the order. Validation Rules: If CANCEL.ORDER or EXECUTE.ORDER is set to YES, then this cannot be set. Input is allowed only when the contract is authorized. If this field is set to YES, no further executions are allowed. |
| 33 | `FX.LO.ORDER.STATUS` | `FxLimOrder_OrderStatus` | TField |  | This field provides the status of the order. The status are: Active when the deal is initially made. Expired when EXPIRE.ORDER is set to YES on the expiry date Cancelled when the CANCEL.ORDER is set to YES. Executed when the EXECUTE.ORDER is set to YES. |
| 34 | `FX.LO.FOREX.ID` | `FxLimOrder_ForexId` |  |  |  |
| 35 | `FX.LO.DEAL.DATE` | `FxLimOrder_DealDate` | TField |  | Contains the systems date, on validation populates the today�s system date. This is a No - inputtable field. |
| 36 | `FX.LO.LOCAL.REF` | `FxLimOrder_LocalRef` |  |  |  |
| 37 | `FX.LO.NOTES` | `FxLimOrder_Notes` |  |  |  |
| 38 | `FX.LO.RESERVED10` | `FxLimOrder_Reserved10` |  |  |  |
| 39 | `FX.LO.RESERVED9` | `FxLimOrder_Reserved9` |  |  |  |
| 40 | `FX.LO.RESERVED8` | `FxLimOrder_Reserved8` | TField |  |  |
| 41 | `FX.LO.RESERVED7` | `FxLimOrder_Reserved7` | TField |  |  |
| 42 | `FX.LO.RESERVED6` | `FxLimOrder_Reserved6` | TField |  |  |
| 43 | `FX.LO.RESERVED5` | `FxLimOrder_Reserved5` | TField |  |  |
| 44 | `FX.LO.RESERVED4` | `FxLimOrder_Reserved4` | TField |  |  |
| 45 | `FX.LO.RESERVED3` | `FxLimOrder_Reserved3` | TField |  |  |
| 46 | `FX.LO.RESERVED2` | `FxLimOrder_Reserved2` | TField |  |  |
| 47 | `FX.LO.RESERVED1` | `FxLimOrder_Reserved1` | TField |  |  |
| 48 | `FX.LO.OVERRIDE` | `FxLimOrder_Override` |  |  |  |
| 49 | `FX.LO.RECORD.STATUS` | `FxLimOrder_RecordStatus` | String |  |  |
| 50 | `FX.LO.CURR.NO` | `FxLimOrder_CurrNo` | String |  |  |
| 51 | `FX.LO.INPUTTER` | `FxLimOrder_Inputter` |  |  |  |
| 52 | `FX.LO.DATE.TIME` | `FxLimOrder_DateTime` |  |  |  |
| 53 | `FX.LO.AUTHORISER` | `FxLimOrder_Authoriser` | String |  |  |
| 54 | `FX.LO.CO.CODE` | `FxLimOrder_CoCode` | String |  |  |
| 55 | `FX.LO.DEPT.CODE` | `FxLimOrder_DeptCode` | String |  |  |
| 56 | `FX.LO.AUDITOR.CODE` | `FxLimOrder_AuditorCode` | String |  |  |
| 57 | `FX.LO.AUDIT.DATE.TIME` | `FxLimOrder_AuditDateTime` | String |  |  |
