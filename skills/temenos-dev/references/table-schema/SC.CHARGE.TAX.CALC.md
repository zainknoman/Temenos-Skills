# SC.CHARGE.TAX.CALC — Table Schema

> Source: `INSERTS/I_F.SC.CHARGE.TAX.CALC` in `SC_SctFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTC.ACTIVITY` | `ScChargeTaxCalc_Activity` | TField |  | Trading Activity Validation Rules: NOINPUT field. Updated from ID. |
| 2 | `SC.CTC.CHARGE.TAX.TYPE` | `ScChargeTaxCalc_ChargeTaxType` | TField |  | Charge/Tax type defined in SCDX.CHARGE.PARAMETER for the ACTIVITY. Validation Rules: NOINPUT field.Updated from ID. |
| 3 | `SC.CTC.STOCK.EXCHANGE` | `ScChargeTaxCalc_StockExchange` | TField |  | Stock Exchange ID Validation Rules: NOINPUT field. Updated from ID. |
| 4 | `SC.CTC.SEC.TYPE` | `ScChargeTaxCalc_SecType` | TField |  | Security Type Validation Rules: NOINPUT field. Updated from ID. |
| 5 | `SC.CTC.SEC.DOMICILE` | `ScChargeTaxCalc_SecDomicile` | TField |  | Country code - domicile of the security. Validation Rules: NOINPUT field. Updated from ID. |
| 6 | `SC.CTC.TXN.TYPE` | `ScChargeTaxCalc_TxnType` | TField |  | Transaction Type Validation Rules: NOINPUT field. Updated from ID. |
| 7 | `SC.CTC.CUST.GROUP` | `ScChargeTaxCalc_CustGroup` | TField |  | Customer group Validation Rules: NOINPUT field. Updated from ID . |
| 8 | `SC.CTC.BASE.AMOUNT` | `ScChargeTaxCalc_BaseAmount` |  |  |  |
| 9 | `SC.CTC.CHG.COMM.CODE` | `ScChargeTaxCalc_ChgCommCode` | TField |  | Identifies the commission code , which will be used to calculate the commission amount on sum of BASE.AMOUNT . Validation Rules: A valid FT.COMMISSION.TYPE record ID. |
| 10 | `SC.CTC.TAX.CODE` | `ScChargeTaxCalc_TaxCode` | TField |  | Identifies the TAX code , which will be used to calculate the tax amount on sum of BASE.AMOUNT . Validation Rules: A valid TAx record ID / TAX.TYPE.CONDITION prefixed with * |
| 11 | `SC.CTC.TILL.DATE` | `ScChargeTaxCalc_TillDate` | TField | No | The field is used to specify the date, if any, till which the charge/tax is applicable. For example, if rebate ordiscount is being offered till a specific date (during the promotional period), the end date is specified here. TheTrade Date of the transaction is compared with TILL.DATE, to identify if the charge/discount is applicable. Validation Rules: Standard date format. (Optional input) |
| 12 | `SC.CTC.SOURCE` | `ScChargeTaxCalc_Source` | TField |  | Identifies the source for calculating the Charge Tax amount, specifically for Fund house charges like entry load.If the field has a value SECURITY.MASTER, the system will check for entry/exit load or switch commission defined inSecurity Master (SM) and use the same for calculation Example: If entry load in SM is 2.25%, the system will calculate the load @2.25% and post the entries to thecategory code defined in SCDX.CHARGE.PARAMETER. If there is no rate defined in SM, the amount will be zero. If the field is blank, the system will check for entry/exit load or switch commission defined in Security Master(SM) and use the same for calculation. The entries will be posted to the category code defined inSCDX.CHARGE.PARAMETER. If no entry/exit load or switch commission is defined in SM, the system will check the SC CHARGE TAX CALC and usethe rates defined therein for the calculation. The entry will be posted to the category defined in FT COMMISSIONTYPE linked to the record. Validation Rules: Accepted Values - SECURITY.MASTER or Blank |
| 13 | `SC.CTC.START.DATE` | `ScChargeTaxCalc_StartDate` | TField | No | The field is used to specify the date, if any, from when the charge/tax is applicable. Validation Rules: Standard date format. (Optional input) |
| 14 | `SC.CTC.ADDL.CRITERIA` | `ScChargeTaxCalc_AddlCriteria` |  |  |  |
| 15 | `SC.CTC.ADDL.CRITERIA.VALUE` | `ScChargeTaxCalc_AddlCriteriaValue` |  |  |  |
| 16 | `SC.CTC.SWIFT.QUAL` | `ScChargeTaxCalc_SwiftQual` |  |  |  |
| 17 | `SC.CTC.RESERVED.13` | `ScChargeTaxCalc_Reserved13` | TField |  |  |
| 18 | `SC.CTC.RESERVED.12` | `ScChargeTaxCalc_Reserved12` | TField |  |  |
| 19 | `SC.CTC.RESERVED.11` | `ScChargeTaxCalc_Reserved11` | TField |  |  |
| 20 | `SC.CTC.RESERVED.10` | `ScChargeTaxCalc_Reserved10` | TField |  |  |
| 21 | `SC.CTC.RESERVED.9` | `ScChargeTaxCalc_Reserved9` | TField |  |  |
| 22 | `SC.CTC.RESERVED.8` | `ScChargeTaxCalc_Reserved8` | TField |  |  |
| 23 | `SC.CTC.RESERVED.7` | `ScChargeTaxCalc_Reserved7` | TField |  |  |
| 24 | `SC.CTC.RESERVED.6` | `ScChargeTaxCalc_Reserved6` | TField |  |  |
| 25 | `SC.CTC.RESERVED.5` | `ScChargeTaxCalc_Reserved5` | TField |  |  |
| 26 | `SC.CTC.RESERVED.4` | `ScChargeTaxCalc_Reserved4` | TField |  |  |
| 27 | `SC.CTC.RESERVED.3` | `ScChargeTaxCalc_Reserved3` | TField |  |  |
| 28 | `SC.CTC.RESERVED.2` | `ScChargeTaxCalc_Reserved2` | TField |  |  |
| 29 | `SC.CTC.RESERVED.1` | `ScChargeTaxCalc_Reserved1` | TField |  |  |
| 30 | `SC.CTC.LOCAL.REF` | `ScChargeTaxCalc_LocalRef` |  |  |  |
| 31 | `SC.CTC.OVERRIDE` | `ScChargeTaxCalc_Override` |  |  |  |
| 32 | `SC.CTC.RECORD.STATUS` | `ScChargeTaxCalc_RecordStatus` | String |  |  |
| 33 | `SC.CTC.CURR.NO` | `ScChargeTaxCalc_CurrNo` | String |  |  |
| 34 | `SC.CTC.INPUTTER` | `ScChargeTaxCalc_Inputter` |  |  |  |
| 35 | `SC.CTC.DATE.TIME` | `ScChargeTaxCalc_DateTime` |  |  |  |
| 36 | `SC.CTC.AUTHORISER` | `ScChargeTaxCalc_Authoriser` | String |  |  |
| 37 | `SC.CTC.CO.CODE` | `ScChargeTaxCalc_CoCode` | String |  |  |
| 38 | `SC.CTC.DEPT.CODE` | `ScChargeTaxCalc_DeptCode` | String |  |  |
| 39 | `SC.CTC.AUDITOR.CODE` | `ScChargeTaxCalc_AuditorCode` | String |  |  |
| 40 | `SC.CTC.AUDIT.DATE.TIME` | `ScChargeTaxCalc_AuditDateTime` | String |  |  |
