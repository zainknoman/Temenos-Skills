# PO.ERROR.DETAIL — Table Schema

> Source: `INSERTS/I_F.PO.ERROR.DETAIL` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PO.ERR.OFS.REQUEST` | `PoErrorDetail_OfsRequest` |  |  |  |
| 2 | `PO.ERR.OFS.RESPONSE` | `PoErrorDetail_OfsResponse` |  |  |  |
| 3 | `PO.ERR.OFS.ERROR` | `PoErrorDetail_OfsError` |  |  |  |
| 4 | `PO.ERR.RESERVED.1` | `PoErrorDetail_Reserved1` |  |  |  |
| 5 | `PO.ERR.RESERVED.2` | `PoErrorDetail_Reserved2` |  |  |  |
| 6 | `PO.ERR.RESERVED.3` | `PoErrorDetail_Reserved3` |  |  |  |
| 7 | `PO.ERR.RESERVED.4` | `PoErrorDetail_Reserved4` |  |  |  |
| 8 | `PO.ERR.RESERVED.5` | `PoErrorDetail_Reserved5` |  |  |  |
| 9 | `PO.ERR.RESERVED.6` | `PoErrorDetail_Reserved6` |  |  |  |
| 10 | `PO.ERR.RESERVED.7` | `PoErrorDetail_Reserved7` |  |  |  |
| 11 | `PO.ERR.RESERVED.8` | `PoErrorDetail_Reserved8` |  |  |  |
| 12 | `PO.ERR.RESERVED.9` | `PoErrorDetail_Reserved9` |  |  |  |
| 13 | `PO.ERR.RESERVED.10` | `PoErrorDetail_Reserved10` |  |  |  |
| 14 | `PO.ERR.LOCAL.REF` | `PoErrorDetail_LocalRef` |  |  |  |
| 15 | `PO.ERR.OVERRIDE` | `PoErrorDetail_Override` |  |  |  |
