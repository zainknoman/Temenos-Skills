# REV.GROUP.CP — Table Schema

> Source: `INSERTS/I_F.REV.GROUP.CP` in `PO_Cashpooling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.REV.DESCRIPTION` | `RevGroupCp_Description` | TField |  |  |
| 2 | `AC.REV.RESERVED11` | `RevGroupCp_Reserved11` | TField |  |  |
| 3 | `AC.REV.RESERVED10` | `RevGroupCp_Reserved10` | TField |  |  |
| 4 | `AC.REV.RESERVED09` | `RevGroupCp_Reserved09` | TField |  |  |
| 5 | `AC.REV.RESERVED08` | `RevGroupCp_Reserved08` | TField |  |  |
| 6 | `AC.REV.RESERVED07` | `RevGroupCp_Reserved07` | TField |  |  |
| 7 | `AC.REV.RESERVED06` | `RevGroupCp_Reserved06` | TField |  |  |
| 8 | `AC.REV.RESERVED05` | `RevGroupCp_Reserved05` | TField |  |  |
| 9 | `AC.REV.RESERVED04` | `RevGroupCp_Reserved04` | TField |  |  |
| 10 | `AC.REV.RESERVED03` | `RevGroupCp_Reserved03` | TField |  |  |
| 11 | `AC.REV.RESERVED02` | `RevGroupCp_Reserved02` | TField |  |  |
| 12 | `AC.REV.LOCAL.REF` | `RevGroupCp_LocalRef` |  |  |  |
| 13 | `AC.REV.STMT.NOS` | `RevGroupCp_StmtNos` |  |  |  |
| 14 | `AC.REV.OVERRIDE` | `RevGroupCp_Override` |  |  |  |
| 15 | `AC.REV.RECORD.STATUS` | `RevGroupCp_RecordStatus` | String |  |  |
| 16 | `AC.REV.CURR.NO` | `RevGroupCp_CurrNo` | String |  |  |
| 17 | `AC.REV.INPUTTER` | `RevGroupCp_Inputter` |  |  |  |
| 18 | `AC.REV.DATE.TIME` | `RevGroupCp_DateTime` |  |  |  |
| 19 | `AC.REV.AUTHORISER` | `RevGroupCp_Authoriser` | String |  |  |
| 20 | `AC.REV.CO.CODE` | `RevGroupCp_CoCode` | String |  |  |
| 21 | `AC.REV.DEPT.CODE` | `RevGroupCp_DeptCode` | String |  |  |
| 22 | `AC.REV.AUDITOR.CODE` | `RevGroupCp_AuditorCode` | String |  |  |
| 23 | `AC.REV.AUDIT.DATE.TIME` | `RevGroupCp_AuditDateTime` | String |  |  |
