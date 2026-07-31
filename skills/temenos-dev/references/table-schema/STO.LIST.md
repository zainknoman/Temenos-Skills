# STO.LIST — Table Schema

> Source: `INSERTS/I_F.STO.LIST` in `AC_StandingOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STO.LIST.STO.ID` | `StoList_StoId` |  |  |  |
| 2 | `STO.LIST.RESERVED.10` | `StoList_Reserved10` | TField |  |  |
| 3 | `STO.LIST.RESERVED.9` | `StoList_Reserved9` | TField |  |  |
| 4 | `STO.LIST.RESERVED.8` | `StoList_Reserved8` | TField |  |  |
| 5 | `STO.LIST.RESERVED.7` | `StoList_Reserved7` | TField |  |  |
| 6 | `STO.LIST.RESERVED.6` | `StoList_Reserved6` | TField |  |  |
| 7 | `STO.LIST.RESERVED.5` | `StoList_Reserved5` | TField |  |  |
| 8 | `STO.LIST.RESERVED.4` | `StoList_Reserved4` | TField |  |  |
| 9 | `STO.LIST.RESERVED.3` | `StoList_Reserved3` | TField |  |  |
| 10 | `STO.LIST.RESERVED.2` | `StoList_Reserved2` | TField |  |  |
| 11 | `STO.LIST.RESERVED.1` | `StoList_Reserved1` | TField |  |  |
