# CAMB.L.UPD.CBR.ARR.STATS — Table Schema

> Source: `INSERTS/I_F.CAMB.L.UPD.CBR.ARR.STATS` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.L.UPD.CBR.ARRANGEMENT.ID` | `CambLUpdCbrArrStats_ArrangementId` | TField |  | The purpose of this field is to store the Arrangement ID for which the Limit is closed. |
| 2 | `CAMB.L.UPD.CBR.CLOSE.DATE` | `CambLUpdCbrArrStats_CloseDate` |  |  |  |
| 3 | `CAMB.L.UPD.CBR.LIMIT.REF` | `CambLUpdCbrArrStats_LimitRef` |  |  |  |
| 4 | `CAMB.L.UPD.CBR.SPCL.CMTS` | `CambLUpdCbrArrStats_SpclCmts` |  |  |  |
| 5 | `CAMB.L.UPD.CBR.RESERVED.9` | `CambLUpdCbrArrStats_Reserved9` | TField |  |  |
| 6 | `CAMB.L.UPD.CBR.RESERVED.8` | `CambLUpdCbrArrStats_Reserved8` | TField |  |  |
| 7 | `CAMB.L.UPD.CBR.RESERVED.7` | `CambLUpdCbrArrStats_Reserved7` | TField |  |  |
| 8 | `CAMB.L.UPD.CBR.RESERVED.6` | `CambLUpdCbrArrStats_Reserved6` | TField |  |  |
| 9 | `CAMB.L.UPD.CBR.RESERVED.5` | `CambLUpdCbrArrStats_Reserved5` | TField |  |  |
| 10 | `CAMB.L.UPD.CBR.RESERVED.4` | `CambLUpdCbrArrStats_Reserved4` | TField |  |  |
| 11 | `CAMB.L.UPD.CBR.RESERVED.3` | `CambLUpdCbrArrStats_Reserved3` | TField |  |  |
| 12 | `CAMB.L.UPD.CBR.RESERVED.2` | `CambLUpdCbrArrStats_Reserved2` | TField |  |  |
| 13 | `CAMB.L.UPD.CBR.RESERVED.1` | `CambLUpdCbrArrStats_Reserved1` | TField |  |  |
