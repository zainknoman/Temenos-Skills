# SEAT.TECHNICAL.MAP — Table Schema

> Source: `INSERTS/I_F.SEAT.TECHNICAL.MAP` in `SE_SeatHeatMap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.TM.PRODUCT` | `SeatTechnicalMap_Product` | TField |  |  |
| 2 | `SE.TM.APPLICATION` | `SeatTechnicalMap_Application` | TField |  |  |
| 3 | `SE.TM.COMPONENT` | `SeatTechnicalMap_Component` |  |  |  |
| 4 | `SE.TM.SUBROUTINE` | `SeatTechnicalMap_Subroutine` |  |  |  |
| 5 | `SE.TM.READ.FILE.NAME` | `SeatTechnicalMap_ReadFileName` |  |  |  |
| 6 | `SE.TM.UPDATE.FILE` | `SeatTechnicalMap_UpdateFile` |  |  |  |
| 7 | `SE.TM.CACHE.IO` | `SeatTechnicalMap_CacheIo` |  |  |  |
| 8 | `SE.TM.RESERVED.10` | `SeatTechnicalMap_Reserved10` | TField |  |  |
| 9 | `SE.TM.RESERVED.9` | `SeatTechnicalMap_Reserved9` | TField |  |  |
| 10 | `SE.TM.RESERVED.8` | `SeatTechnicalMap_Reserved8` | TField |  |  |
| 11 | `SE.TM.RESERVED.7` | `SeatTechnicalMap_Reserved7` | TField |  |  |
| 12 | `SE.TM.RESERVED.6` | `SeatTechnicalMap_Reserved6` | TField |  |  |
| 13 | `SE.TM.RESERVED.5` | `SeatTechnicalMap_Reserved5` | TField |  |  |
| 14 | `SE.TM.RESERVED.4` | `SeatTechnicalMap_Reserved4` | TField |  |  |
| 15 | `SE.TM.RESERVED.3` | `SeatTechnicalMap_Reserved3` | TField |  |  |
| 16 | `SE.TM.RESERVED.2` | `SeatTechnicalMap_Reserved2` | TField |  |  |
| 17 | `SE.TM.RESERVED.1` | `SeatTechnicalMap_Reserved1` | TField |  |  |
