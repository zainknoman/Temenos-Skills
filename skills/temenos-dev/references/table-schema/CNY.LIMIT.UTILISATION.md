# CNY.LIMIT.UTILISATION — Table Schema

> Source: `INSERTS/I_F.CNY.LIMIT.UTILISATION` in `OTREMI_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LIMIT.UTIL.CNY.SELL.LIMIT` | `CnyLimitUtilisation_CnySellLimit` | TField |  | Cumulative transaction amount hitting sell limit for the customer as on date |
| 2 | `LIMIT.UTIL.TXN.DATE` | `CnyLimitUtilisation_TxnDate` |  |  |  |
| 3 | `LIMIT.UTIL.TXN.REFERENCE` | `CnyLimitUtilisation_TxnReference` |  |  |  |
| 4 | `LIMIT.UTIL.TOTAL.TXN.COUNT` | `CnyLimitUtilisation_TotalTxnCount` | TField |  | Transaction count for the customer on respective date |
| 5 | `LIMIT.UTIL.UNAUTH.TXN.COUNT` | `CnyLimitUtilisation_UnauthTxnCount` | TField |  | Number of transaction processed kept in INAU status |
| 6 | `LIMIT.UTIL.AUTH.TXN.COUNT` | `CnyLimitUtilisation_AuthTxnCount` | TField |  | Number of transaction processed and authorised |
| 7 | `LIMIT.UTIL.LAST.REMITTANCE.DATE` | `CnyLimitUtilisation_LastRemittanceDate` | TField |  | Last outward remittance date for the customer |
| 8 | `LIMIT.UTIL.RESERVED.1` | `CnyLimitUtilisation_Reserved1` | TField |  | Reserved for future use |
| 9 | `LIMIT.UTIL.RESERVED.2` | `CnyLimitUtilisation_Reserved2` | TField |  | Reserved for future use |
| 10 | `LIMIT.UTIL.RESERVED.3` | `CnyLimitUtilisation_Reserved3` | TField |  | Reserved for future use |
| 11 | `LIMIT.UTIL.RESERVED.4` | `CnyLimitUtilisation_Reserved4` | TField |  | Reserved for future use |
| 12 | `LIMIT.UTIL.RESERVED.5` | `CnyLimitUtilisation_Reserved5` | TField |  | Reserved for future use |
| 13 | `LIMIT.UTIL.RESERVED.6` | `CnyLimitUtilisation_Reserved6` | TField |  | Reserved for future use |
| 14 | `LIMIT.UTIL.RESERVED.7` | `CnyLimitUtilisation_Reserved7` | TField |  | Reserved for future use |
| 15 | `LIMIT.UTIL.RESERVED.8` | `CnyLimitUtilisation_Reserved8` | TField |  | Reserved for future use |
| 16 | `LIMIT.UTIL.RESERVED.9` | `CnyLimitUtilisation_Reserved9` | TField |  | Reserved for future use |
| 17 | `LIMIT.UTIL.RESERVED.10` | `CnyLimitUtilisation_Reserved10` | TField |  | Reserved for future use |
| 18 | `LIMIT.UTIL.LOCAL.REF` | `CnyLimitUtilisation_LocalRef` |  |  |  |
| 19 | `LIMIT.UTIL.OVERRIDE` | `CnyLimitUtilisation_Override` |  |  |  |
