# LBNCDR.FAMILY.NAMES — Table Schema

> Source: `INSERTS/I_F.LBNCDR.FAMILY.NAMES` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.FAMILY.NAMES.DESCRIPTION` | `LbncdrFamilyNames_Description` | TField |  | This field hold the Description of BDL First Names Validation Rules : Type : A Length :35 |
| 2 | `LBNCDR.FAMILY.NAMES.AR.NAMES` | `LbncdrFamilyNames_ArNames` | TField |  |  |
| 3 | `LBNCDR.FAMILY.NAMES.RESERVED.10` | `LbncdrFamilyNames_Reserved10` | TField |  |  |
| 4 | `LBNCDR.FAMILY.NAMES.RESERVED.9` | `LbncdrFamilyNames_Reserved9` | TField |  |  |
| 5 | `LBNCDR.FAMILY.NAMES.RESERVED.8` | `LbncdrFamilyNames_Reserved8` | TField |  |  |
| 6 | `LBNCDR.FAMILY.NAMES.RESERVED.7` | `LbncdrFamilyNames_Reserved7` | TField |  |  |
| 7 | `LBNCDR.FAMILY.NAMES.RESERVED.6` | `LbncdrFamilyNames_Reserved6` | TField |  |  |
| 8 | `LBNCDR.FAMILY.NAMES.RESERVED.5` | `LbncdrFamilyNames_Reserved5` | TField |  |  |
| 9 | `LBNCDR.FAMILY.NAMES.RESERVED.4` | `LbncdrFamilyNames_Reserved4` | TField |  |  |
| 10 | `LBNCDR.FAMILY.NAMES.RESERVED.3` | `LbncdrFamilyNames_Reserved3` | TField |  |  |
| 11 | `LBNCDR.FAMILY.NAMES.RESERVED.2` | `LbncdrFamilyNames_Reserved2` | TField |  |  |
| 12 | `LBNCDR.FAMILY.NAMES.RESERVED.1` | `LbncdrFamilyNames_Reserved1` | TField |  |  |
| 13 | `LBNCDR.FAMILY.NAMES.OVERRIDE` | `LbncdrFamilyNames_Override` |  |  |  |
| 14 | `LBNCDR.FAMILY.NAMES.RECORD.STATUS` | `LbncdrFamilyNames_RecordStatus` | String |  |  |
| 15 | `LBNCDR.FAMILY.NAMES.CURR.NO` | `LbncdrFamilyNames_CurrNo` | String |  |  |
| 16 | `LBNCDR.FAMILY.NAMES.INPUTTER` | `LbncdrFamilyNames_Inputter` |  |  |  |
| 17 | `LBNCDR.FAMILY.NAMES.DATE.TIME` | `LbncdrFamilyNames_DateTime` |  |  |  |
| 18 | `LBNCDR.FAMILY.NAMES.AUTHORISER` | `LbncdrFamilyNames_Authoriser` | String |  |  |
| 19 | `LBNCDR.FAMILY.NAMES.CO.CODE` | `LbncdrFamilyNames_CoCode` | String |  |  |
| 20 | `LBNCDR.FAMILY.NAMES.DEPT.CODE` | `LbncdrFamilyNames_DeptCode` | String |  |  |
| 21 | `LBNCDR.FAMILY.NAMES.AUDITOR.CODE` | `LbncdrFamilyNames_AuditorCode` | String |  |  |
| 22 | `LBNCDR.FAMILY.NAMES.AUDIT.DATE.TIME` | `LbncdrFamilyNames_AuditDateTime` | String |  |  |
