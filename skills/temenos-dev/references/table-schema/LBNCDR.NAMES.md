# LBNCDR.NAMES — Table Schema

> Source: `INSERTS/I_F.LBNCDR.NAMES` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.NAMES.DESCRIPTION` | `LbncdrNames_Description` | TField |  | This field hold the Description of BDL First Names Validation Rules : Type : A Length :35 |
| 2 | `LBNCDR.NAMES.GENDER` | `LbncdrNames_Gender` | TField |  |  |
| 3 | `LBNCDR.NAMES.AR.NAMES` | `LbncdrNames_ArNames` | TField |  |  |
| 4 | `LBNCDR.NAMES.RESERVED.10` | `LbncdrNames_Reserved10` | TField |  |  |
| 5 | `LBNCDR.NAMES.RESERVED.9` | `LbncdrNames_Reserved9` | TField |  |  |
| 6 | `LBNCDR.NAMES.RESERVED.8` | `LbncdrNames_Reserved8` | TField |  |  |
| 7 | `LBNCDR.NAMES.RESERVED.7` | `LbncdrNames_Reserved7` | TField |  |  |
| 8 | `LBNCDR.NAMES.RESERVED.6` | `LbncdrNames_Reserved6` | TField |  |  |
| 9 | `LBNCDR.NAMES.RESERVED.5` | `LbncdrNames_Reserved5` | TField |  |  |
| 10 | `LBNCDR.NAMES.RESERVED.4` | `LbncdrNames_Reserved4` | TField |  |  |
| 11 | `LBNCDR.NAMES.RESERVED.3` | `LbncdrNames_Reserved3` | TField |  |  |
| 12 | `LBNCDR.NAMES.RESERVED.2` | `LbncdrNames_Reserved2` | TField |  |  |
| 13 | `LBNCDR.NAMES.RESERVED.1` | `LbncdrNames_Reserved1` | TField |  |  |
| 14 | `LBNCDR.NAMES.OVERRIDE` | `LbncdrNames_Override` |  |  |  |
| 15 | `LBNCDR.NAMES.RECORD.STATUS` | `LbncdrNames_RecordStatus` | String |  |  |
| 16 | `LBNCDR.NAMES.CURR.NO` | `LbncdrNames_CurrNo` | String |  |  |
| 17 | `LBNCDR.NAMES.INPUTTER` | `LbncdrNames_Inputter` |  |  |  |
| 18 | `LBNCDR.NAMES.DATE.TIME` | `LbncdrNames_DateTime` |  |  |  |
| 19 | `LBNCDR.NAMES.AUTHORISER` | `LbncdrNames_Authoriser` | String |  |  |
| 20 | `LBNCDR.NAMES.CO.CODE` | `LbncdrNames_CoCode` | String |  |  |
| 21 | `LBNCDR.NAMES.DEPT.CODE` | `LbncdrNames_DeptCode` | String |  |  |
| 22 | `LBNCDR.NAMES.AUDITOR.CODE` | `LbncdrNames_AuditorCode` | String |  |  |
| 23 | `LBNCDR.NAMES.AUDIT.DATE.TIME` | `LbncdrNames_AuditDateTime` | String |  |  |
