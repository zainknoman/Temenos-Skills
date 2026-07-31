# LBNCDR.LIAB.GROUP — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LIAB.GROUP` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.LG.DESCRIPTION` | `LbncdrLiabGroup_Description` | TField |  | Holds the Liability Group Description Validation Rules 50 ANY |
| 2 | `LBNCDR.LG.RESERVED.10` | `LbncdrLiabGroup_Reserved10` | TField |  |  |
| 3 | `LBNCDR.LG.RESERVED.9` | `LbncdrLiabGroup_Reserved9` | TField |  |  |
| 4 | `LBNCDR.LG.RESERVED.8` | `LbncdrLiabGroup_Reserved8` | TField |  |  |
| 5 | `LBNCDR.LG.RESERVED.7` | `LbncdrLiabGroup_Reserved7` | TField |  |  |
| 6 | `LBNCDR.LG.RESERVED.6` | `LbncdrLiabGroup_Reserved6` | TField |  |  |
| 7 | `LBNCDR.LG.RESERVED.5` | `LbncdrLiabGroup_Reserved5` | TField |  |  |
| 8 | `LBNCDR.LG.RESERVED.4` | `LbncdrLiabGroup_Reserved4` | TField |  |  |
| 9 | `LBNCDR.LG.RESERVED.3` | `LbncdrLiabGroup_Reserved3` | TField |  |  |
| 10 | `LBNCDR.LG.RESERVED.2` | `LbncdrLiabGroup_Reserved2` | TField |  |  |
| 11 | `LBNCDR.LG.RESERVED.1` | `LbncdrLiabGroup_Reserved1` | TField |  |  |
| 12 | `LBNCDR.LG.LOCAL.REF` | `LbncdrLiabGroup_LocalRef` |  |  |  |
| 13 | `LBNCDR.LG.OVERRIDE` | `LbncdrLiabGroup_Override` |  |  |  |
| 14 | `LBNCDR.LG.RECORD.STATUS` | `LbncdrLiabGroup_RecordStatus` | String |  |  |
| 15 | `LBNCDR.LG.CURR.NO` | `LbncdrLiabGroup_CurrNo` | String |  |  |
| 16 | `LBNCDR.LG.INPUTTER` | `LbncdrLiabGroup_Inputter` |  |  |  |
| 17 | `LBNCDR.LG.DATE.TIME` | `LbncdrLiabGroup_DateTime` |  |  |  |
| 18 | `LBNCDR.LG.AUTHORISER` | `LbncdrLiabGroup_Authoriser` | String |  |  |
| 19 | `LBNCDR.LG.CO.CODE` | `LbncdrLiabGroup_CoCode` | String |  |  |
| 20 | `LBNCDR.LG.DEPT.CODE` | `LbncdrLiabGroup_DeptCode` | String |  |  |
| 21 | `LBNCDR.LG.AUDITOR.CODE` | `LbncdrLiabGroup_AuditorCode` | String |  |  |
| 22 | `LBNCDR.LG.AUDIT.DATE.TIME` | `LbncdrLiabGroup_AuditDateTime` | String |  |  |
