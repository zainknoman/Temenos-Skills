# OA.POLICY.GROUP — Table Schema

> Source: `INSERTS/I_F.OA.POLICY.GROUP` in `OA_PolicyRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.PG.DESCRIPTION` | `OaPolicyGroup_Description` |  |  |  |
| 2 | `OA.PG.FULL.DESCRIPTION` | `OaPolicyGroup_FullDescription` |  |  |  |
| 3 | `OA.PG.POLICY.ITEM` | `OaPolicyGroup_PolicyItem` |  |  |  |
| 4 | `OA.PG.RESERVED.5` | `OaPolicyGroup_Reserved5` | TField |  |  |
| 5 | `OA.PG.RESERVED.4` | `OaPolicyGroup_Reserved4` | TField |  |  |
| 6 | `OA.PG.RESERVED.3` | `OaPolicyGroup_Reserved3` | TField |  |  |
| 7 | `OA.PG.RESERVED.2` | `OaPolicyGroup_Reserved2` | TField |  |  |
| 8 | `OA.PG.RESERVED.1` | `OaPolicyGroup_Reserved1` | TField |  |  |
| 9 | `OA.PG.LOCAL.REF` | `OaPolicyGroup_LocalRef` |  |  |  |
| 10 | `OA.PG.OVERRIDE` | `OaPolicyGroup_Override` |  |  |  |
| 11 | `OA.PG.RECORD.STATUS` | `OaPolicyGroup_RecordStatus` | String |  |  |
| 12 | `OA.PG.CURR.NO` | `OaPolicyGroup_CurrNo` | String |  |  |
| 13 | `OA.PG.INPUTTER` | `OaPolicyGroup_Inputter` |  |  |  |
| 14 | `OA.PG.DATE.TIME` | `OaPolicyGroup_DateTime` |  |  |  |
| 15 | `OA.PG.AUTHORISER` | `OaPolicyGroup_Authoriser` | String |  |  |
| 16 | `OA.PG.CO.CODE` | `OaPolicyGroup_CoCode` | String |  |  |
| 17 | `OA.PG.DEPT.CODE` | `OaPolicyGroup_DeptCode` | String |  |  |
| 18 | `OA.PG.AUDITOR.CODE` | `OaPolicyGroup_AuditorCode` | String |  |  |
| 19 | `OA.PG.AUDIT.DATE.TIME` | `OaPolicyGroup_AuditDateTime` | String |  |  |
