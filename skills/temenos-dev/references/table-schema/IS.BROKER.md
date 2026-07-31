# IS.BROKER — Table Schema

> Source: `INSERTS/I_F.IS.BROKER` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.BRO.NAME` | `IsBroker_Name` | TField |  | This field is used to specify the Broker name. The customer name would be defaulted. User can still provide the Broker Name overwriting the defaulted name. Validation Rules: 1. Standard T24 Alphanumeric Field |
| 2 | `IS.BRO.STATUS` | `IsBroker_Status` | TField | Yes | This field defines the status of the Broker. The values to the field are defined in the EB.LOOKUP table with prefix "IS.STATUS" Validation Rules: 1. Valid values are Active and Inactive. 2. Field Mandatory. |
| 3 | `IS.BRO.OPERATION` | `IsBroker_Operation` | TField | Yes | The operations that the Broker could perform. The valid Broker operations are Buy, Sell and Both. Validation Rules: 1. The Valid values are Buy, Sell, Both. 2. Field Mandatory. |
| 4 | `IS.BRO.WASH.CATEG` | `IsBroker_WashCateg` | TField |  | The Broker Wash Account Category customised for the Vendor. If this field is Null, then BUY.WASH.CAT or SELL.WASH.CAT will be used based on the Broker operation in the Contract. Validation Rules: 1. Must be a valid record from the table CATEGORY. 2. Valid Internal category ranging from 10000 to 19999 |
| 5 | `IS.BRO.COMPANY` | `IsBroker_Company` |  |  |  |
| 6 | `IS.BRO.CURRENCY` | `IsBroker_Currency` |  |  |  |
| 7 | `IS.BRO.BROKER.ACCT` | `IsBroker_BrokerAcct` |  |  |  |
| 8 | `IS.BRO.BENEFICIARY` | `IsBroker_Beneficiary` |  |  |  |
| 9 | `IS.BRO.RESERVED.15` | `IsBroker_Reserved15` |  |  |  |
| 10 | `IS.BRO.RESERVED.14` | `IsBroker_Reserved14` |  |  |  |
| 11 | `IS.BRO.RESERVED.13` | `IsBroker_Reserved13` |  |  |  |
| 12 | `IS.BRO.RESERVED.12` | `IsBroker_Reserved12` |  |  |  |
| 13 | `IS.BRO.RESERVED.11` | `IsBroker_Reserved11` |  |  |  |
| 14 | `IS.BRO.BR.FEE.TYPE` | `IsBroker_BrFeeType` | TField |  | Contains the commission type to be used for calculation broker fee Validation Rules: Must be a valid record in FT.COMMISSION.TYPE |
| 15 | `IS.BRO.BR.FEE.CCY` | `IsBroker_BrFeeCcy` | TField |  | The currency to be used for calculation of broker fee The system will defualt the local currency Validation Rules: Must be a valid record in CURRENCY |
| 16 | `IS.BRO.BR.FEE.SETTLEMENT` | `IsBroker_BrFeeSettlement` | TField |  | This field is used to opt whether broker fee amount needs to be credited to "Broker Fee Wash Account" an internal account created with the value in BR.FEE.WASH.CATEG [or] Income PL category set up in FT.COMMISSION.TYPE&gt;CATEGORY.ACCOUNT. Wash Account is used for crediting / parking the broker fee collected. |
| 17 | `IS.BRO.BR.FEE.SHARE.PERC` | `IsBroker_BrFeeSharePerc` | TField |  | This field is used for capturing the Broker fee share percentage of the Broker fee amount to be paid to the Buy Broker. Value givenin this field is used to calculate the Broker fee amount to be paid to the Buy Broker. It should be a Numeric value 0-100 with decimals. |
| 18 | `IS.BRO.BR.FEE.TAX.BASE.AMT` | `IsBroker_BrFeeTaxBaseAmt` | TField |  | The base amount on which the broker tax has to be calculated Validation Rules: Valid values are Bank Share, Broker Share and Both |
| 19 | `IS.BRO.BR.FEE.WASH.CATEG` | `IsBroker_BrFeeWashCateg` | TField |  | The category for broker fee payment wash account Validation Rules: Must be a valid record in CATEGORY and should be in the range 10000-19999 |
| 20 | `IS.BRO.BR.PAYMENT.FREQ` | `IsBroker_BrPaymentFreq` | TField |  | The frequency for which the broker fee payment must be made |
| 21 | `IS.BRO.BR.LAST.PAYMENT.DATE` | `IsBroker_BrLastPaymentDate` | TField |  | the date on which the previous broker fee payment has been done Validation Rules: Standard T24 Date Field |
| 22 | `IS.BRO.MOV.TO.HIST.DAYS` | `IsBroker_MovToHistDays` | TField |  | The number of days after which BROKER.FEE.BALANCES record for this broker has to be archived |
| 23 | `IS.BRO.RESERVED.1` | `IsBroker_Reserved1` |  |  |  |
| 24 | `IS.BRO.LOCAL.REF` | `IsBroker_LocalRef` |  |  |  |
| 25 | `IS.BRO.OVERRIDE` | `IsBroker_Override` |  |  |  |
| 26 | `IS.BRO.RECORD.STATUS` | `IsBroker_RecordStatus` | String |  |  |
| 27 | `IS.BRO.CURR.NO` | `IsBroker_CurrNo` | String |  |  |
| 28 | `IS.BRO.INPUTTER` | `IsBroker_Inputter` |  |  |  |
| 29 | `IS.BRO.DATE.TIME` | `IsBroker_DateTime` |  |  |  |
| 30 | `IS.BRO.AUTHORISER` | `IsBroker_Authoriser` | String |  |  |
| 31 | `IS.BRO.CO.CODE` | `IsBroker_CoCode` | String |  |  |
| 32 | `IS.BRO.DEPT.CODE` | `IsBroker_DeptCode` | String |  |  |
| 33 | `IS.BRO.AUDITOR.CODE` | `IsBroker_AuditorCode` | String |  |  |
| 34 | `IS.BRO.AUDIT.DATE.TIME` | `IsBroker_AuditDateTime` | String |  |  |
