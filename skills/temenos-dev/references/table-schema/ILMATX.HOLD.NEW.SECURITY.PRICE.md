# ILMATX.HOLD.NEW.SECURITY.PRICE — Table Schema

> Source: `INSERTS/I_F.ILMATX.HOLD.NEW.SECURITY.PRICE` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MATX.TXN.ENTITLEMENT.TXNS` | `IlmatxHoldNewSecurityPrice_EntitlementTxns` |  |  |  |
| 2 | `MATX.TXN.RESERVED.5` | `IlmatxHoldNewSecurityPrice_Reserved5` | TField |  | Reserved for future use. |
| 3 | `MATX.TXN.RESERVED.4` | `IlmatxHoldNewSecurityPrice_Reserved4` | TField |  | Reserved for future use. |
| 4 | `MATX.TXN.RESERVED.3` | `IlmatxHoldNewSecurityPrice_Reserved3` | TField |  | Reserved for future use. |
| 5 | `MATX.TXN.RESERVED.2` | `IlmatxHoldNewSecurityPrice_Reserved2` | TField |  | Reserved for future use. |
| 6 | `MATX.TXN.RESERVED.1` | `IlmatxHoldNewSecurityPrice_Reserved1` | TField |  | Reserved for future use. |
| 7 | `MATX.TXN.LOCAL.REF` | `IlmatxHoldNewSecurityPrice_LocalRef` |  |  |  |
| 8 | `MATX.TXN.OVERRIDE` | `IlmatxHoldNewSecurityPrice_Override` |  |  |  |
