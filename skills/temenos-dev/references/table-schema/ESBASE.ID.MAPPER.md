# ESBASE.ID.MAPPER — Table Schema

> Source: `INSERTS/I_F.ESBASE.ID.MAPPER` in `CMBASE_IdValidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.MAPPER.ALTERNATE.VALUE` | `EsbaseIdMapper_AlternateValue` | TField |  | To replace the @ID with the letter configured and to compare the Check Digit |
| 2 | `ID.MAPPER.RESERVED.16` | `EsbaseIdMapper_Reserved16` | TField |  |  |
| 3 | `ID.MAPPER.LOCAL.REF` | `EsbaseIdMapper_LocalRef` |  |  |  |
| 4 | `ID.MAPPER.RESERVED.1` | `EsbaseIdMapper_Reserved1` | TField |  |  |
| 5 | `ID.MAPPER.RESERVED.2` | `EsbaseIdMapper_Reserved2` | TField |  |  |
| 6 | `ID.MAPPER.RESERVED.3` | `EsbaseIdMapper_Reserved3` | TField |  |  |
| 7 | `ID.MAPPER.RESERVED.4` | `EsbaseIdMapper_Reserved4` | TField |  |  |
| 8 | `ID.MAPPER.RESERVED.5` | `EsbaseIdMapper_Reserved5` | TField |  |  |
| 9 | `ID.MAPPER.RESERVED.6` | `EsbaseIdMapper_Reserved6` | TField |  |  |
| 10 | `ID.MAPPER.RESERVED.7` | `EsbaseIdMapper_Reserved7` | TField |  |  |
| 11 | `ID.MAPPER.RESERVED.8` | `EsbaseIdMapper_Reserved8` | TField |  |  |
| 12 | `ID.MAPPER.RESERVED.9` | `EsbaseIdMapper_Reserved9` | TField |  |  |
| 13 | `ID.MAPPER.RESERVED.10` | `EsbaseIdMapper_Reserved10` | TField |  |  |
| 14 | `ID.MAPPER.RESERVED.11` | `EsbaseIdMapper_Reserved11` | TField |  |  |
| 15 | `ID.MAPPER.RESERVED.12` | `EsbaseIdMapper_Reserved12` | TField |  |  |
| 16 | `ID.MAPPER.RESERVED.13` | `EsbaseIdMapper_Reserved13` | TField |  |  |
| 17 | `ID.MAPPER.RESERVED.14` | `EsbaseIdMapper_Reserved14` | TField |  |  |
| 18 | `ID.MAPPER.RESERVED.15` | `EsbaseIdMapper_Reserved15` | TField |  |  |
| 19 | `ID.MAPPER.OVERRIDE` | `EsbaseIdMapper_Override` |  |  |  |
| 20 | `ID.MAPPER.RECORD.STATUS` | `EsbaseIdMapper_RecordStatus` | String |  | Indicates the record status |
| 21 | `ID.MAPPER.CURR.NO` | `EsbaseIdMapper_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 22 | `ID.MAPPER.INPUTTER` | `EsbaseIdMapper_Inputter` |  |  |  |
| 23 | `ID.MAPPER.DATE.TIME` | `EsbaseIdMapper_DateTime` |  |  |  |
| 24 | `ID.MAPPER.AUTHORISER` | `EsbaseIdMapper_Authoriser` | String |  |  |
| 25 | `ID.MAPPER.CO.CODE` | `EsbaseIdMapper_CoCode` | String |  |  |
| 26 | `ID.MAPPER.DEPT.CODE` | `EsbaseIdMapper_DeptCode` | String |  |  |
| 27 | `ID.MAPPER.AUDITOR.CODE` | `EsbaseIdMapper_AuditorCode` | String |  |  |
| 28 | `ID.MAPPER.AUDIT.DATE.TIME` | `EsbaseIdMapper_AuditDateTime` | String |  |  |
