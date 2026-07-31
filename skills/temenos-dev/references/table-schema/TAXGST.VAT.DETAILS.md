# TAXGST.VAT.DETAILS — Table Schema

> Source: `INSERTS/I_F.TAXGST.VAT.DETAILS` in `TAXGST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VAT.DETAILS.CUSTOMER.NO` | `TaxgstVatDetails_CustomerNo` | TField |  | Identifies the customer number of the income transaction. |
| 2 | `VAT.DETAILS.VAT.TYPE` | `TaxgstVatDetails_VatType` | TField |  | Identifies the income type. Can be interest accruals or charges. |
| 3 | `VAT.DETAILS.TAX.CODE` | `TaxgstVatDetails_TaxCode` | TField |  | Identifies the tax code applied on this income. |
| 4 | `VAT.DETAILS.VAT.RATE` | `TaxgstVatDetails_VatRate` | TField |  | Identifies the tax rate applied on the income. |
| 5 | `VAT.DETAILS.PL.CATEGORY` | `TaxgstVatDetails_PlCategory` | TField |  | Identifies the PL category of the income. |
| 6 | `VAT.DETAILS.DR.ACCOUNT` | `TaxgstVatDetails_DrAccount` | TField |  | Identifies the debit end for the tax entry. |
| 7 | `VAT.DETAILS.CR.ACCOUNT` | `TaxgstVatDetails_CrAccount` | TField |  | Identifies the crebit end for the tax entry. |
| 8 | `VAT.DETAILS.VAT.LCY` | `TaxgstVatDetails_VatLcy` | TField |  | Identifies the tax amount in local currency. |
| 9 | `VAT.DETAILS.VAT.FCY` | `TaxgstVatDetails_VatFcy` | TField |  | Identifies the tax amount in income currency. |
| 10 | `VAT.DETAILS.VAT.CCY` | `TaxgstVatDetails_VatCcy` | TField |  | Identifies the tax currency. |
| 11 | `VAT.DETAILS.EXCH.RATE` | `TaxgstVatDetails_ExchRate` | TField |  | Identifies the exchange rate used for tax collection when income currency is different from the tax currency. |
| 12 | `VAT.DETAILS.VALUE.DATE` | `TaxgstVatDetails_ValueDate` | TField |  | Identifies the value date of the tax entry. |
| 13 | `VAT.DETAILS.COMM.AMT` | `TaxgstVatDetails_CommAmt` | TField |  | Identifies the income amount. |
| 14 | `VAT.DETAILS.CONTRACT.ID` | `TaxgstVatDetails_ContractId` | TField |  | Identifies the contract id for the income. |
| 15 | `VAT.DETAILS.NEW.TAX.CODE` | `TaxgstVatDetails_NewTaxCode` |  |  |  |
| 16 | `VAT.DETAILS.ADJUST.DATE` | `TaxgstVatDetails_AdjustDate` |  |  |  |
| 17 | `VAT.DETAILS.ADJUST.AMT` | `TaxgstVatDetails_AdjustAmt` |  |  |  |
| 18 | `VAT.DETAILS.LOCAL.REF` | `TaxgstVatDetails_LocalRef` |  |  |  |
| 19 | `VAT.DETAILS.RESERVED.10` | `TaxgstVatDetails_Reserved10` | TField |  |  |
| 20 | `VAT.DETAILS.RESERVED.9` | `TaxgstVatDetails_Reserved9` | TField |  |  |
| 21 | `VAT.DETAILS.RESERVED.8` | `TaxgstVatDetails_Reserved8` | TField |  |  |
| 22 | `VAT.DETAILS.RESERVED.7` | `TaxgstVatDetails_Reserved7` | TField |  |  |
| 23 | `VAT.DETAILS.RESERVED.6` | `TaxgstVatDetails_Reserved6` | TField |  |  |
| 24 | `VAT.DETAILS.RESERVED.5` | `TaxgstVatDetails_Reserved5` | TField |  |  |
| 25 | `VAT.DETAILS.RESERVED.4` | `TaxgstVatDetails_Reserved4` | TField |  |  |
| 26 | `VAT.DETAILS.RESERVED.3` | `TaxgstVatDetails_Reserved3` | TField |  |  |
| 27 | `VAT.DETAILS.RESERVED.2` | `TaxgstVatDetails_Reserved2` | TField |  |  |
| 28 | `VAT.DETAILS.RESERVED.1` | `TaxgstVatDetails_Reserved1` | TField |  |  |
