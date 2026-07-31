# US.STATE.GROUP.CONCAT — Table Schema

> Source: `INSERTS/I_F.US.STATE.GROUP.CONCAT` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STATE.GRP.CON.GROUP.ID` | `UsStateGroupConcat_GroupId` | TField |  | The group under which this state is defined will be stored here. If any state used for dormancy state level parameter then the string STATE will be updated as group id. If any state used as default state in dormancy parameter then the group id will be blank. |
| 2 | `STATE.GRP.CON.RESERVED.10` | `UsStateGroupConcat_Reserved10` | TField |  |  |
| 3 | `STATE.GRP.CON.RESERVED.9` | `UsStateGroupConcat_Reserved9` | TField |  |  |
| 4 | `STATE.GRP.CON.RESERVED.8` | `UsStateGroupConcat_Reserved8` | TField |  |  |
| 5 | `STATE.GRP.CON.RESERVED.7` | `UsStateGroupConcat_Reserved7` | TField |  |  |
| 6 | `STATE.GRP.CON.RESERVED.6` | `UsStateGroupConcat_Reserved6` | TField |  |  |
| 7 | `STATE.GRP.CON.RESERVED.5` | `UsStateGroupConcat_Reserved5` | TField |  |  |
| 8 | `STATE.GRP.CON.RESERVED.4` | `UsStateGroupConcat_Reserved4` | TField |  |  |
| 9 | `STATE.GRP.CON.RESERVED.3` | `UsStateGroupConcat_Reserved3` | TField |  |  |
| 10 | `STATE.GRP.CON.RESERVED.2` | `UsStateGroupConcat_Reserved2` | TField |  |  |
| 11 | `STATE.GRP.CON.RESERVED.1` | `UsStateGroupConcat_Reserved1` | TField |  |  |
