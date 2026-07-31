# LBNCDR.LIAB.SUB.GROUP — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LIAB.SUB.GROUP` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.LSG.LIAB.GROUP` | `LbncdrLiabSubGroup_LiabGroup` |  |  |  |
| 2 | `LBNCDR.LSG.DESCRIPTION` | `LbncdrLiabSubGroup_Description` |  |  |  |
| 3 | `LBNCDR.LSG.RESERVED.10` | `LbncdrLiabSubGroup_Reserved10` | TField |  |  |
| 4 | `LBNCDR.LSG.RESERVED.9` | `LbncdrLiabSubGroup_Reserved9` | TField |  |  |
| 5 | `LBNCDR.LSG.RESERVED.8` | `LbncdrLiabSubGroup_Reserved8` | TField |  |  |
| 6 | `LBNCDR.LSG.RESERVED.7` | `LbncdrLiabSubGroup_Reserved7` | TField |  |  |
| 7 | `LBNCDR.LSG.RESERVED.6` | `LbncdrLiabSubGroup_Reserved6` | TField |  |  |
| 8 | `LBNCDR.LSG.RESERVED.5` | `LbncdrLiabSubGroup_Reserved5` | TField |  |  |
| 9 | `LBNCDR.LSG.RESERVED.4` | `LbncdrLiabSubGroup_Reserved4` | TField |  |  |
| 10 | `LBNCDR.LSG.RESERVED.3` | `LbncdrLiabSubGroup_Reserved3` | TField |  |  |
| 11 | `LBNCDR.LSG.RESERVED.2` | `LbncdrLiabSubGroup_Reserved2` | TField |  |  |
| 12 | `LBNCDR.LSG.RESERVED.1` | `LbncdrLiabSubGroup_Reserved1` | TField |  |  |
| 13 | `LBNCDR.LSG.LOCAL.REF` | `LbncdrLiabSubGroup_LocalRef` |  |  |  |
| 14 | `LBNCDR.LSG.OVERRIDE` | `LbncdrLiabSubGroup_Override` |  |  |  |
| 15 | `LBNCDR.LSG.RECORD.STATUS` | `LbncdrLiabSubGroup_RecordStatus` | String |  |  |
| 16 | `LBNCDR.LSG.CURR.NO` | `LbncdrLiabSubGroup_CurrNo` | String |  |  |
| 17 | `LBNCDR.LSG.INPUTTER` | `LbncdrLiabSubGroup_Inputter` |  |  |  |
| 18 | `LBNCDR.LSG.DATE.TIME` | `LbncdrLiabSubGroup_DateTime` |  |  |  |
| 19 | `LBNCDR.LSG.AUTHORISER` | `LbncdrLiabSubGroup_Authoriser` | String |  |  |
| 20 | `LBNCDR.LSG.CO.CODE` | `LbncdrLiabSubGroup_CoCode` | String |  |  |
| 21 | `LBNCDR.LSG.DEPT.CODE` | `LbncdrLiabSubGroup_DeptCode` | String |  |  |
| 22 | `LBNCDR.LSG.AUDITOR.CODE` | `LbncdrLiabSubGroup_AuditorCode` | String |  |  |
| 23 | `LBNCDR.LSG.AUDIT.DATE.TIME` | `LbncdrLiabSubGroup_AuditDateTime` | String |  |  |
