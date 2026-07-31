# STO.ACCOUNT.PRIORITY — Table Schema

> Source: `INSERTS/I_F.STO.ACCOUNT.PRIORITY` in `AC_StandingOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STO.PRI.STO.ID` | `StoAccountPriority_StoId` |  |  |  |
| 2 | `STO.PRI.PRIORITY.NUMBER` | `StoAccountPriority_PriorityNumber` |  |  |  |
| 3 | `STO.PRI.RESERVED.10` | `StoAccountPriority_Reserved10` | TField |  |  |
| 4 | `STO.PRI.RESERVED.9` | `StoAccountPriority_Reserved9` | TField |  |  |
| 5 | `STO.PRI.RESERVED.8` | `StoAccountPriority_Reserved8` | TField |  |  |
| 6 | `STO.PRI.RESERVED.7` | `StoAccountPriority_Reserved7` | TField |  |  |
| 7 | `STO.PRI.RESERVED.6` | `StoAccountPriority_Reserved6` | TField |  |  |
| 8 | `STO.PRI.RESERVED.5` | `StoAccountPriority_Reserved5` | TField |  |  |
| 9 | `STO.PRI.RESERVED.4` | `StoAccountPriority_Reserved4` | TField |  |  |
| 10 | `STO.PRI.RESERVED.3` | `StoAccountPriority_Reserved3` | TField |  |  |
| 11 | `STO.PRI.RESERVED.2` | `StoAccountPriority_Reserved2` | TField |  |  |
| 12 | `STO.PRI.RESERVED.1` | `StoAccountPriority_Reserved1` | TField |  |  |
