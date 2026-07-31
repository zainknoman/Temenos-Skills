# OA.POLICY.ITEM — Table Schema

> Source: `INSERTS/I_F.OA.POLICY.ITEM` in `OA_PolicyRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.PI.DESCRIPTION` | `OaPolicyItem_Description` |  |  |  |
| 2 | `OA.PI.RESERVED.4` | `OaPolicyItem_Reserved4` | TField |  |  |
| 3 | `OA.PI.RESERVED.3` | `OaPolicyItem_Reserved3` | TField |  |  |
| 4 | `OA.PI.RESERVED.2` | `OaPolicyItem_Reserved2` | TField |  |  |
| 5 | `OA.PI.RESERVED.1` | `OaPolicyItem_Reserved1` | TField |  |  |
| 6 | `OA.PI.LOCAL.REF` | `OaPolicyItem_LocalRef` |  |  |  |
| 7 | `OA.PI.OVERRIDE` | `OaPolicyItem_Override` |  |  |  |
| 8 | `OA.PI.RECORD.STATUS` | `OaPolicyItem_RecordStatus` | String |  |  |
| 9 | `OA.PI.CURR.NO` | `OaPolicyItem_CurrNo` | String |  |  |
| 10 | `OA.PI.INPUTTER` | `OaPolicyItem_Inputter` |  |  |  |
| 11 | `OA.PI.DATE.TIME` | `OaPolicyItem_DateTime` |  |  |  |
| 12 | `OA.PI.AUTHORISER` | `OaPolicyItem_Authoriser` | String |  |  |
| 13 | `OA.PI.CO.CODE` | `OaPolicyItem_CoCode` | String |  |  |
| 14 | `OA.PI.DEPT.CODE` | `OaPolicyItem_DeptCode` | String |  |  |
| 15 | `OA.PI.AUDITOR.CODE` | `OaPolicyItem_AuditorCode` | String |  |  |
| 16 | `OA.PI.AUDIT.DATE.TIME` | `OaPolicyItem_AuditDateTime` | String |  |  |
