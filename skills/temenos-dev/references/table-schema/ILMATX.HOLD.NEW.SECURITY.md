# ILMATX.HOLD.NEW.SECURITY — Table Schema

> Source: `INSERTS/I_F.ILMATX.HOLD.NEW.SECURITY` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MATX.ENTITLEMENT.TXNS` | `IlmatxHoldNewSecurity_EntitlementTxns` |  |  |  |
| 2 | `MATX.NEW.SEC.NO` | `IlmatxHoldNewSecurity_NewSecNo` |  |  |  |
| 3 | `MATX.RESERVED.5` | `IlmatxHoldNewSecurity_Reserved5` | TField |  | Reserved for future use. |
| 4 | `MATX.RESERVED.4` | `IlmatxHoldNewSecurity_Reserved4` | TField |  | Reserved for future use. |
| 5 | `MATX.RESERVED.3` | `IlmatxHoldNewSecurity_Reserved3` | TField |  | Reserved for future use. |
| 6 | `MATX.RESERVED.2` | `IlmatxHoldNewSecurity_Reserved2` | TField |  | Reserved for future use. |
| 7 | `MATX.RESERVED.1` | `IlmatxHoldNewSecurity_Reserved1` | TField |  | Reserved for future use. |
| 8 | `MATX.LOCAL.REF` | `IlmatxHoldNewSecurity_LocalRef` |  |  |  |
| 9 | `MATX.OVERRIDE` | `IlmatxHoldNewSecurity_Override` |  |  |  |
