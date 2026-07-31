# LBNCDR.LIAB.CODE — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LIAB.CODE` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDR.LIAB.LIAB.TYPE` | `LbncdrLiabCode_LiabType` | TField |  | Holds Liability Type Validation Rules 12 |
| 2 | `CDR.LIAB.RESERVED.1` | `LbncdrLiabCode_Reserved1` | TField |  | Validation Rules |
| 3 | `CDR.LIAB.RESERVED.2` | `LbncdrLiabCode_Reserved2` | TField |  | Validation Rules |
| 4 | `CDR.LIAB.RESERVED.3` | `LbncdrLiabCode_Reserved3` | TField |  | Validation Rules |
| 5 | `CDR.LIAB.RESERVED.4` | `LbncdrLiabCode_Reserved4` | TField |  | Validation Rules |
| 6 | `CDR.LIAB.RESERVED.5` | `LbncdrLiabCode_Reserved5` | TField |  | Validation Rules |
| 7 | `CDR.LIAB.RESERVED.6` | `LbncdrLiabCode_Reserved6` | TField |  | Validation Rules |
| 8 | `CDR.LIAB.RESERVED.7` | `LbncdrLiabCode_Reserved7` | TField |  | Validation Rules |
| 9 | `CDR.LIAB.RESERVED.8` | `LbncdrLiabCode_Reserved8` | TField |  | Validation Rules |
| 10 | `CDR.LIAB.LOCAL.REF` | `LbncdrLiabCode_LocalRef` |  |  |  |
| 11 | `CDR.LIAB.OVERRIDE` | `LbncdrLiabCode_Override` |  |  |  |
| 12 | `CDR.LIAB.RECORD.STATUS` | `LbncdrLiabCode_RecordStatus` | String |  |  |
| 13 | `CDR.LIAB.CURR.NO` | `LbncdrLiabCode_CurrNo` | String |  |  |
| 14 | `CDR.LIAB.INPUTTER` | `LbncdrLiabCode_Inputter` |  |  |  |
| 15 | `CDR.LIAB.DATE.TIME` | `LbncdrLiabCode_DateTime` |  |  |  |
| 16 | `CDR.LIAB.AUTHORISER` | `LbncdrLiabCode_Authoriser` | String |  |  |
| 17 | `CDR.LIAB.CO.CODE` | `LbncdrLiabCode_CoCode` | String |  |  |
| 18 | `CDR.LIAB.DEPT.CODE` | `LbncdrLiabCode_DeptCode` | String |  |  |
| 19 | `CDR.LIAB.AUDITOR.CODE` | `LbncdrLiabCode_AuditorCode` | String |  |  |
| 20 | `CDR.LIAB.AUDIT.DATE.TIME` | `LbncdrLiabCode_AuditDateTime` | String |  |  |
