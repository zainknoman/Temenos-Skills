# CBVTMS.CURRENCY.PRINTING.COST — Table Schema

> Source: `INSERTS/I_F.CBVTMS.CURRENCY.PRINTING.COST` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.REQUESTED.BY.TO` | `CbvtmsCurrencyPrintingCost_RequestedByTo` | TField |  |  |
| 2 | `VTMS.CURRENCY` | `CbvtmsCurrencyPrintingCost_Currency` | TField |  | The currency in which the total value and the cost is calculated |
| 3 | `VTMS.TOTAL.VALUE` | `CbvtmsCurrencyPrintingCost_TotalValue` | TField |  | The total value of the currency received from the printer/minter |
| 4 | `VTMS.COST.CURRENCY` | `CbvtmsCurrencyPrintingCost_CostCurrency` | TField |  | The cost of the currency for printing the currency |
| 5 | `VTMS.TOTAL.COST` | `CbvtmsCurrencyPrintingCost_TotalCost` | TField |  | The total cost of currency printing |
| 6 | `VTMS.DENOMINATION` | `CbvtmsCurrencyPrintingCost_Denomination` |  |  |  |
| 7 | `VTMS.UNITS` | `CbvtmsCurrencyPrintingCost_Units` |  |  |  |
| 8 | `VTMS.COST.PER.UNIT` | `CbvtmsCurrencyPrintingCost_CostPerUnit` |  |  |  |
| 9 | `VTMS.PAYMENT.STATUS` | `CbvtmsCurrencyPrintingCost_PaymentStatus` | TField |  | The payment status of the cost incurred for printing the currency |
| 10 | `VTMS.PAYMENT.REFERENCE` | `CbvtmsCurrencyPrintingCost_PaymentReference` | TField |  | The payment reference of the cost incurred for printing the currency |
| 11 | `VTMS.LOCAL.REF` | `CbvtmsCurrencyPrintingCost_LocalRef` |  |  |  |
| 12 | `VTMS.RESERVED.1` | `CbvtmsCurrencyPrintingCost_Reserved1` | TField |  | Reserved field for future use |
| 13 | `VTMS.RESERVED.2` | `CbvtmsCurrencyPrintingCost_Reserved2` | TField |  | Reserved field for future use |
| 14 | `VTMS.RESERVED.3` | `CbvtmsCurrencyPrintingCost_Reserved3` | TField |  | Reserved field for future use |
| 15 | `VTMS.RESERVED.4` | `CbvtmsCurrencyPrintingCost_Reserved4` | TField |  | Reserved field for future use |
| 16 | `VTMS.RESERVED.5` | `CbvtmsCurrencyPrintingCost_Reserved5` | TField |  | Reserved field for future use |
| 17 | `VTMS.RESERVED.6` | `CbvtmsCurrencyPrintingCost_Reserved6` | TField |  | Reserved field for future use |
| 18 | `VTMS.RESERVED.7` | `CbvtmsCurrencyPrintingCost_Reserved7` | TField |  | Reserved field for future use |
| 19 | `VTMS.RESERVED.8` | `CbvtmsCurrencyPrintingCost_Reserved8` | TField |  | Reserved field for future use |
| 20 | `VTMS.RESERVED.9` | `CbvtmsCurrencyPrintingCost_Reserved9` | TField |  | Reserved field for future use |
| 21 | `VTMS.RESERVED.10` | `CbvtmsCurrencyPrintingCost_Reserved10` | TField |  | Reserved field for future use |
| 22 | `VTMS.OVERRIDE` | `CbvtmsCurrencyPrintingCost_Override` |  |  |  |
| 23 | `VTMS.RECORD.STATUS` | `CbvtmsCurrencyPrintingCost_RecordStatus` | String |  |  |
| 24 | `VTMS.CURR.NO` | `CbvtmsCurrencyPrintingCost_CurrNo` | String |  |  |
| 25 | `VTMS.INPUTTER` | `CbvtmsCurrencyPrintingCost_Inputter` |  |  |  |
| 26 | `VTMS.DATE.TIME` | `CbvtmsCurrencyPrintingCost_DateTime` |  |  |  |
| 27 | `VTMS.AUTHORISER` | `CbvtmsCurrencyPrintingCost_Authoriser` | String |  |  |
| 28 | `VTMS.CO.CODE` | `CbvtmsCurrencyPrintingCost_CoCode` | String |  |  |
| 29 | `VTMS.DEPT.CODE` | `CbvtmsCurrencyPrintingCost_DeptCode` | String |  |  |
| 30 | `VTMS.AUDITOR.CODE` | `CbvtmsCurrencyPrintingCost_AuditorCode` | String |  |  |
| 31 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsCurrencyPrintingCost_AuditDateTime` | String |  |  |
