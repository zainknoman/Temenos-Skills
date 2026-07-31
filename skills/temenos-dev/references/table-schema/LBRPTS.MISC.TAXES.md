# LBRPTS.MISC.TAXES — Table Schema

> Source: `INSERTS/I_F.LBRPTS.MISC.TAXES` in `LBRPTS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBRPTS.MISC.COMPANY` | `LbrptsMiscTaxes_Company` | TField |  | Id of the company from which the transaction is made |
| 2 | `LBRPTS.MISC.TAX.TYPE` | `LbrptsMiscTaxes_TaxType` | TField |  | Type of tax for which the transaction is made |
| 3 | `LBRPTS.MISC.DEBIT.ACCOUNT` | `LbrptsMiscTaxes_DebitAccount` | TField |  | Debit account of the branch from which the transaction is made |
| 4 | `LBRPTS.MISC.CREDIT.ACCOUNT` | `LbrptsMiscTaxes_CreditAccount` | TField |  | Crdeit account of the head office to which the transaction is made |
| 5 | `LBRPTS.MISC.CURRENCY` | `LbrptsMiscTaxes_Currency` | TField |  | Currency in which the transaction is made |
| 6 | `LBRPTS.MISC.AMOUNT` | `LbrptsMiscTaxes_Amount` | TField |  | Amount of transaction |
| 7 | `LBRPTS.MISC.DATE` | `LbrptsMiscTaxes_Date` | TField |  | DATE in which the transaction is made |
| 8 | `LBRPTS.MISC.REF.NO` | `LbrptsMiscTaxes_RefNo` | TField |  | Reference number for each transaction by the branch. Format is YYYY.sequence.no |
| 9 | `LBRPTS.MISC.RESERVED5` | `LbrptsMiscTaxes_Reserved5` | TField |  |  |
| 10 | `LBRPTS.MISC.RESERVED4` | `LbrptsMiscTaxes_Reserved4` | TField |  |  |
| 11 | `LBRPTS.MISC.RESERVED3` | `LbrptsMiscTaxes_Reserved3` | TField |  |  |
| 12 | `LBRPTS.MISC.RESERVED2` | `LbrptsMiscTaxes_Reserved2` | TField |  |  |
| 13 | `LBRPTS.MISC.LOCAL.REF` | `LbrptsMiscTaxes_LocalRef` |  |  |  |
