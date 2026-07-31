# CAMB.SHARE.ACCT — Table Schema

> Source: `INSERTS/I_F.CAMB.SHARE.ACCT` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.SHARE.ARR.ID` | `CambShareAcct_ArrId` |  |  |  |
| 2 | `CAMB.SHARE.ARR.STATUS` | `CambShareAcct_ArrStatus` |  |  |  |
| 3 | `CAMB.SHARE.ERROR` | `CambShareAcct_Error` |  |  |  |
| 4 | `CAMB.SHARE.ACCT.TITLE` | `CambShareAcct_AcctTitle` |  |  |  |
| 5 | `CAMB.SHARE.PROD.ID` | `CambShareAcct_ProdId` |  |  |  |
| 6 | `CAMB.SHARE.ARR.CCY` | `CambShareAcct_ArrCcy` |  |  |  |
| 7 | `CAMB.SHARE.RESERVED.3` | `CambShareAcct_Reserved3` | TField |  |  |
| 8 | `CAMB.SHARE.RESERVED.2` | `CambShareAcct_Reserved2` | TField |  |  |
| 9 | `CAMB.SHARE.RESERVED.1` | `CambShareAcct_Reserved1` | TField |  |  |
