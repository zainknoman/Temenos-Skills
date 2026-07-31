# LBNCDR.ECO.SECTOR — Table Schema

> Source: `INSERTS/I_F.LBNCDR.ECO.SECTOR` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.ECO.ECO.SECTOR` | `LbncdrEcoSector_EcoSector` | TField |  | Holds the Economic Sector Code value in customer table Validation Rules 4 ANY |
| 2 | `LBNCDR.ECO.RESERVED.10` | `LbncdrEcoSector_Reserved10` | TField |  |  |
| 3 | `LBNCDR.ECO.RESERVED.9` | `LbncdrEcoSector_Reserved9` | TField |  |  |
| 4 | `LBNCDR.ECO.RESERVED.8` | `LbncdrEcoSector_Reserved8` | TField |  |  |
| 5 | `LBNCDR.ECO.RESERVED.7` | `LbncdrEcoSector_Reserved7` | TField |  |  |
| 6 | `LBNCDR.ECO.RESERVED.6` | `LbncdrEcoSector_Reserved6` | TField |  |  |
| 7 | `LBNCDR.ECO.RESERVED.5` | `LbncdrEcoSector_Reserved5` | TField |  |  |
| 8 | `LBNCDR.ECO.RESERVED.4` | `LbncdrEcoSector_Reserved4` | TField |  |  |
| 9 | `LBNCDR.ECO.RESERVED.3` | `LbncdrEcoSector_Reserved3` | TField |  |  |
| 10 | `LBNCDR.ECO.RESERVED.2` | `LbncdrEcoSector_Reserved2` | TField |  |  |
| 11 | `LBNCDR.ECO.RESERVED.1` | `LbncdrEcoSector_Reserved1` | TField |  |  |
| 12 | `LBNCDR.ECO.OVERRIDE` | `LbncdrEcoSector_Override` |  |  |  |
| 13 | `LBNCDR.ECO.RECORD.STATUS` | `LbncdrEcoSector_RecordStatus` | String |  |  |
| 14 | `LBNCDR.ECO.CURR.NO` | `LbncdrEcoSector_CurrNo` | String |  |  |
| 15 | `LBNCDR.ECO.INPUTTER` | `LbncdrEcoSector_Inputter` |  |  |  |
| 16 | `LBNCDR.ECO.DATE.TIME` | `LbncdrEcoSector_DateTime` |  |  |  |
| 17 | `LBNCDR.ECO.AUTHORISER` | `LbncdrEcoSector_Authoriser` | String |  |  |
| 18 | `LBNCDR.ECO.CO.CODE` | `LbncdrEcoSector_CoCode` | String |  |  |
| 19 | `LBNCDR.ECO.DEPT.CODE` | `LbncdrEcoSector_DeptCode` | String |  |  |
| 20 | `LBNCDR.ECO.AUDITOR.CODE` | `LbncdrEcoSector_AuditorCode` | String |  |  |
| 21 | `LBNCDR.ECO.AUDIT.DATE.TIME` | `LbncdrEcoSector_AuditDateTime` | String |  |  |
