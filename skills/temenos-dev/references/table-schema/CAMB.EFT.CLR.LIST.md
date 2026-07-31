# CAMB.EFT.CLR.LIST — Table Schema

> Source: `INSERTS/I_F.CAMB.EFT.CLR.LIST` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.EFT.LST.ORIG.DATA` | `CambEftClrList_OrigData` |  |  |  |
| 2 | `CAMB.EFT.LST.UPDT.DATA` | `CambEftClrList_UpdtData` |  |  |  |
| 3 | `CAMB.EFT.LST.RESERVED.3` | `CambEftClrList_Reserved3` |  |  |  |
| 4 | `CAMB.EFT.LST.RESERVED.2` | `CambEftClrList_Reserved2` |  |  |  |
| 5 | `CAMB.EFT.LST.RESERVED.1` | `CambEftClrList_Reserved1` |  |  |  |
