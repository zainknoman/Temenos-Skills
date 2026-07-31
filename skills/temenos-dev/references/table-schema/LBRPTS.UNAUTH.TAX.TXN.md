# LBRPTS.UNAUTH.TAX.TXN — Table Schema

> Source: `INSERTS/I_F.LBRPTS.UNAUTH.TAX.TXN` in `LBRPTS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBRPTS.TRANSACTION.ID` | `LbrptsUnauthTaxTxn_TransactionId` |  |  |  |
| 2 | `LBRPTS.TAX.TYPE` | `LbrptsUnauthTaxTxn_TaxType` |  |  |  |
| 3 | `LBRPTS.NEXT.NUMBER` | `LbrptsUnauthTaxTxn_NextNumber` |  |  |  |
| 4 | `LBRPTS.RESERVED5` | `LbrptsUnauthTaxTxn_Reserved5` | TField |  |  |
| 5 | `LBRPTS.RESERVED4` | `LbrptsUnauthTaxTxn_Reserved4` | TField |  |  |
| 6 | `LBRPTS.RESERVED3` | `LbrptsUnauthTaxTxn_Reserved3` | TField |  |  |
| 7 | `LBRPTS.RESERVED2` | `LbrptsUnauthTaxTxn_Reserved2` | TField |  |  |
| 8 | `LBRPTS.OVERRIDE` | `LbrptsUnauthTaxTxn_Override` |  |  |  |
