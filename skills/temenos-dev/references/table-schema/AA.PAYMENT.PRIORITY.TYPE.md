# AA.PAYMENT.PRIORITY.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.PAYMENT.PRIORITY.TYPE` in `AA_PaymentPriority.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PP.DESCRIPTION` | `AaPaymentPriorityType_Description` |  |  |  |
| 2 | `AA.PP.PRIORITY.RULE.TYPE` | `AaPaymentPriorityType_PriorityRuleType` | TField |  | This field is used to specify how the payment Priority will apply to an arrangement. This can have any of the below Nine options. 1) Balances - Payment will be applied on arrangement's current balances. (e.g. current principal, accrued interest, etc.). 2) Bill Date - For product with bills and due amounts, payment to the due amounts will be bill date wise (e.g., all amount on bill 1 followed by all amounts of bill 2, etc.). 3) Interest Rate - Order of payment will be based upon Interest Rate of the Arrangement. 4) Outs Amount -Order of payment will be based on Outstanding Amount of Drawing Arrangement. 5) Product -Order of payment will be based upon Product. 6) Product Group - Order of payment will be based upon Product Group. 7) Property - For product with bills and due amounts, payment to the due amounts will be Property wise(e.g. all Principal amounts followed by all Interest amounts, etc.) 8) Routine - Order of payment will be based on the user defined routine. System will not honor the othe+B6r priority rule type. 9) Start Date - Order of payment will be based on the arrangement start date |
| 3 | `AA.PP.PRIORITY.ORDER` | `AaPaymentPriorityType_PriorityOrder` | TField | Yes | This field specifies the order based on which the priority will be determined. The order could be a predefined order, or a user defined order based on priority rule type. For billed amounts, in addition to specifying whether Properties or Dates will be given priority, the user must decide in which order multiple bills will be processed. This field can be used to specify the order in which multiple bills has to be procesed. This field can accept 1. Highest to Lowest - Order of processing will start from highest value. 2. Lowest to Highest - Order of processing will start from Lowest value. 3. Newest to Oldest - Order of processing will start from New Bill. 4. Oldest to Newest - Order of processing will start from Old bill. 5. Priority.List - User defined list specified in PRIORITY.RULE.LIST field in Payment priority condition. Validations: 1. Mandatory field except for Routine Rule Type. 2. The values Oldest to Newest/ Newest to Oldest are allowed only for the following Priority Rule type. o Bill Date o Start Date 3. The values Highest to Lowest/ Lowest to Highest are allowed only for the following Priority Rule types. o Interest Rate o Amount 4. The value Priority List is allowed only for the following Priority Rule types. o Product Group o Product o Property o Balances |
| 4 | `AA.PP.RESERVED.1` | `AaPaymentPriorityType_PriorityReserved1` |  |  |  |
| 5 | `AA.PP.RESERVED.2` | `AaPaymentPriorityType_PriorityReserved2` |  |  |  |
| 6 | `AA.PP.PRIORITY.RULE.ADD.INFO` | `AaPaymentPriorityType_PriorityRuleAddInfo` | TField |  | Specified any additional information required for prioritising. Input allowed only for Priority Rule type Interest rate to specify the Interest property name based on which the prioritization will be done. |
| 7 | `AA.PP.RESERVED.3` | `AaPaymentPriorityType_PriorityReserved3` |  |  |  |
| 8 | `AA.PP.RESERVED.4` | `AaPaymentPriorityType_PriorityReserved4` |  |  |  |
| 9 | `AA.PP.RESERVED.5` | `AaPaymentPriorityType_PriorityReserved5` |  |  |  |
| 10 | `AA.PP.PRIORITISE.ROUTINE` | `AaPaymentPriorityType_PrioritiseRoutine` | TField |  | Option to attach a local routine to return the arrangement priority. Can be defined only when PRIORITY.RULE.TYPE is �Routine� |
| 11 | `AA.PP.RESERVED.6` | `AaPaymentPriorityType_Reserved6` | TField |  | Reserved for Future Use. |
| 12 | `AA.PP.RESERVED.7` | `AaPaymentPriorityType_Reserved7` | TField |  | Reserved for Future Use. |
| 13 | `AA.PP.RESERVED.8` | `AaPaymentPriorityType_Reserved8` | TField |  | Reserved for Future Use. |
| 14 | `AA.PP.RESERVED.9` | `AaPaymentPriorityType_Reserved9` | TField |  | Reserved for Future Use. |
| 15 | `AA.PP.RESERVED.10` | `AaPaymentPriorityType_Reserved10` | TField |  | Reserved for Future Use. |
| 16 | `AA.PP.RECORD.STATUS` | `AaPaymentPriorityType_RecordStatus` | String |  |  |
| 17 | `AA.PP.CURR.NO` | `AaPaymentPriorityType_CurrNo` | String |  |  |
| 18 | `AA.PP.INPUTTER` | `AaPaymentPriorityType_Inputter` |  |  |  |
| 19 | `AA.PP.DATE.TIME` | `AaPaymentPriorityType_DateTime` |  |  |  |
| 20 | `AA.PP.AUTHORISER` | `AaPaymentPriorityType_Authoriser` | String |  |  |
| 21 | `AA.PP.CO.CODE` | `AaPaymentPriorityType_CoCode` | String |  |  |
| 22 | `AA.PP.DEPT.CODE` | `AaPaymentPriorityType_DeptCode` | String |  |  |
| 23 | `AA.PP.AUDITOR.CODE` | `AaPaymentPriorityType_AuditorCode` | String |  |  |
| 24 | `AA.PP.AUDIT.DATE.TIME` | `AaPaymentPriorityType_AuditDateTime` | String |  |  |
