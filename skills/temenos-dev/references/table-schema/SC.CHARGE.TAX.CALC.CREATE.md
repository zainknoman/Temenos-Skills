# SC.CHARGE.TAX.CALC.CREATE — Table Schema

> Source: `INSERTS/I_F.SC.CHARGE.TAX.CALC.CREATE` in `SC_SctFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTCC.ACTIVITY` | `ScChargeTaxCalcCreate_Activity` | TField |  |  |
| 2 | `SC.CTCC.CHARGE.TAX.TYPE` | `ScChargeTaxCalcCreate_ChargeTaxType` | TField |  | Charge/Tax type defined in SCDX.CHARGE.PARAMETER for the ACTIVITY. |
| 3 | `SC.CTCC.STOCK.EXCHANGE` | `ScChargeTaxCalcCreate_StockExchange` | TField |  | Stock Exchange ID |
| 4 | `SC.CTCC.SEC.TYPE` | `ScChargeTaxCalcCreate_SecType` | TField |  | Field accepts a valid asset type or sub asset type. A channel identifier can be added as a suffix (separated by a'.', e.g. A-10.ONLINE)to specify separate charge or discounts based on transaction channel. The valid channels are identified fromEB.LOOKUP record �SC.CHANNEL.If the channel matches the channel identifier in transaction, the charge/discount will apply. Validation Rules: Security Type - Field accepts a valid Asset type or Sub Asset Type. Channel - A Valid channel from EB.LOOKUP configured with SC.CHANNEL (added as a suffix separated by '.' |
| 5 | `SC.CTCC.SEC.DOMICILE` | `ScChargeTaxCalcCreate_SecDomicile` | TField |  | Country code - domicile of the security. |
| 6 | `SC.CTCC.TXN.TYPE` | `ScChargeTaxCalcCreate_TxnType` | TField |  | Transaction Type |
| 7 | `SC.CTCC.CUST.GROUP` | `ScChargeTaxCalcCreate_CustGroup` | TField |  | Customer group Duplicates are not allowed |
| 8 | `SC.CTCC.BASE.AMOUNT` | `ScChargeTaxCalcCreate_BaseAmount` |  |  |  |
| 9 | `SC.CTCC.CHG.COMM.CODE` | `ScChargeTaxCalcCreate_ChgCommCode` | TField |  | Identifies the commission code , which will be used to calculate the commission amount on sum of BASE.AMOUNT . Validation Rules: A valid FT.COMMISSION.TYPE record ID. |
| 10 | `SC.CTCC.TAX.CODE` | `ScChargeTaxCalcCreate_TaxCode` | TField |  | Identifies the TAX code , which will be used to calculate the tax amount on sum of BASE.AMOUNT . Validation Rules: A valid TAx record ID / TAX.TYPE.CONDITION prefixed with * |
| 11 | `SC.CTCC.TILL.DATE` | `ScChargeTaxCalcCreate_TillDate` | TField | No | The field is used to specify the date, if any, till which the charge/tax is applicable. For example, if rebate ordiscount is being offered till a specific date (during the promotional period), the end date is specified here. TheTrade Date of the transaction is compared with TILL.DATE, to identify if the charge/discount is applicable. Validation Rules: Standard date format. (Optional input) |
| 12 | `SC.CTCC.SOURCE` | `ScChargeTaxCalcCreate_Source` | TField |  | Identifies the source for calculating the Charge Tax amount, specifically for Fund house charges like entry load.If the field has a value SECURITY.MASTER, the system will check for entry/exit load or switch commission defined inSecurity Master (SM) and use the same for calculation Example: If entry load in SM is 2.25%, the system will calculate the load @2.25% and post the entries to thecategory code defined in SCDX.CHARGE.PARAMETER. If there is no rate defined in SM, the amount will be zero. If the field is blank, the system will check for entry/exit load or switch commission defined in Security Master(SM) and use the same for calculation. The entries will be posted to the category code defined inSCDX.CHARGE.PARAMETER. If no entry/exit load or switch commission is defined in SM, the system will check the SC CHARGE TAX CALC and usethe rates defined therein for the calculation. The entry will be posted to the category defined in FT COMMISSIONTYPE linked to the record. Validation Rules: Accepted Values - SECURITY.MASTER or Blank |
| 13 | `SC.CTCC.START.DATE` | `ScChargeTaxCalcCreate_StartDate` | TField | No | The field is used to specify the date, if any, from when the charge/tax is applicable. Validation Rules: Standard date format. (Optional input) |
| 14 | `SC.CTCC.ADDL.CRITERIA` | `ScChargeTaxCalcCreate_AddlCriteria` |  |  |  |
| 15 | `SC.CTCC.ADDL.CRITERIA.VALUE` | `ScChargeTaxCalcCreate_AddlCriteriaValue` |  |  |  |
| 16 | `SC.CTCC.SWIFT.QUAL` | `ScChargeTaxCalcCreate_SwiftQual` |  |  |  |
| 17 | `SC.CTCC.RESERVED.13` | `ScChargeTaxCalcCreate_Reserved13` | TField |  |  |
| 18 | `SC.CTCC.RESERVED.12` | `ScChargeTaxCalcCreate_Reserved12` | TField |  |  |
| 19 | `SC.CTCC.RESERVED.11` | `ScChargeTaxCalcCreate_Reserved11` | TField |  |  |
| 20 | `SC.CTCC.RESERVED.10` | `ScChargeTaxCalcCreate_Reserved10` | TField |  |  |
| 21 | `SC.CTCC.RESERVED.9` | `ScChargeTaxCalcCreate_Reserved9` | TField |  |  |
| 22 | `SC.CTCC.RESERVED.8` | `ScChargeTaxCalcCreate_Reserved8` | TField |  |  |
| 23 | `SC.CTCC.RESERVED.7` | `ScChargeTaxCalcCreate_Reserved7` | TField |  |  |
| 24 | `SC.CTCC.RESERVED.6` | `ScChargeTaxCalcCreate_Reserved6` | TField |  |  |
| 25 | `SC.CTCC.RESERVED.5` | `ScChargeTaxCalcCreate_Reserved5` | TField |  |  |
| 26 | `SC.CTCC.RESERVED.4` | `ScChargeTaxCalcCreate_Reserved4` | TField |  |  |
| 27 | `SC.CTCC.RESERVED.3` | `ScChargeTaxCalcCreate_Reserved3` | TField |  |  |
| 28 | `SC.CTCC.RESERVED.2` | `ScChargeTaxCalcCreate_Reserved2` | TField |  |  |
| 29 | `SC.CTCC.RESERVED.1` | `ScChargeTaxCalcCreate_Reserved1` | TField |  |  |
| 30 | `SC.CTCC.LOCAL.REF` | `ScChargeTaxCalcCreate_LocalRef` |  |  |  |
| 31 | `SC.CTCC.OVERRIDE` | `ScChargeTaxCalcCreate_Override` |  |  |  |
| 32 | `SC.CTCC.RECORD.STATUS` | `ScChargeTaxCalcCreate_RecordStatus` | String |  |  |
| 33 | `SC.CTCC.CURR.NO` | `ScChargeTaxCalcCreate_CurrNo` | String |  |  |
| 34 | `SC.CTCC.INPUTTER` | `ScChargeTaxCalcCreate_Inputter` |  |  |  |
| 35 | `SC.CTCC.DATE.TIME` | `ScChargeTaxCalcCreate_DateTime` |  |  |  |
| 36 | `SC.CTCC.AUTHORISER` | `ScChargeTaxCalcCreate_Authoriser` | String |  |  |
| 37 | `SC.CTCC.CO.CODE` | `ScChargeTaxCalcCreate_CoCode` | String |  |  |
| 38 | `SC.CTCC.DEPT.CODE` | `ScChargeTaxCalcCreate_DeptCode` | String |  |  |
| 39 | `SC.CTCC.AUDITOR.CODE` | `ScChargeTaxCalcCreate_AuditorCode` | String |  |  |
| 40 | `SC.CTCC.AUDIT.DATE.TIME` | `ScChargeTaxCalcCreate_AuditDateTime` | String |  |  |
