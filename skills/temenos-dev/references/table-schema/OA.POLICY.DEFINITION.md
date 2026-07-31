# OA.POLICY.DEFINITION — Table Schema

> Source: `INSERTS/I_F.OA.POLICY.DEFINITION` in `OA_PolicyRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.PD.DESCRIPTION` | `OaPolicyDefinition_Description` |  |  |  |
| 2 | `OA.PD.FULL.DESCRIPTION` | `OaPolicyDefinition_FullDescription` |  |  |  |
| 3 | `OA.PD.POLICY.GROUP` | `OaPolicyDefinition_PolicyGroup` |  |  |  |
| 4 | `OA.PD.RESERVED.9` | `OaPolicyDefinition_Reserved9` |  |  |  |
| 5 | `OA.PD.RESERVED.8` | `OaPolicyDefinition_Reserved8` |  |  |  |
| 6 | `OA.PD.POLICY.ITEM` | `OaPolicyDefinition_PolicyItem` |  |  |  |
| 7 | `OA.PD.VALUE` | `OaPolicyDefinition_Value` |  |  |  |
| 8 | `OA.PD.THRESHOLD` | `OaPolicyDefinition_Threshold` |  |  |  |
| 9 | `OA.PD.RULE` | `OaPolicyDefinition_Rule` |  |  |  |
| 10 | `OA.PD.RESERVED.7` | `OaPolicyDefinition_Reserved7` |  |  |  |
| 11 | `OA.PD.RESERVED.6` | `OaPolicyDefinition_Reserved6` |  |  |  |
| 12 | `OA.PD.DOMAIN` | `OaPolicyDefinition_Domain` |  |  |  |
| 13 | `OA.PD.RESERVED.5` | `OaPolicyDefinition_Reserved5` | TField |  |  |
| 14 | `OA.PD.RESERVED.4` | `OaPolicyDefinition_Reserved4` | TField |  |  |
| 15 | `OA.PD.RESERVED.3` | `OaPolicyDefinition_Reserved3` | TField |  |  |
| 16 | `OA.PD.RESERVED.2` | `OaPolicyDefinition_Reserved2` | TField |  |  |
| 17 | `OA.PD.RESERVED.1` | `OaPolicyDefinition_Reserved1` | TField |  |  |
| 18 | `OA.PD.LOCAL.REF` | `OaPolicyDefinition_LocalRef` |  |  |  |
| 19 | `OA.PD.OVERRIDE` | `OaPolicyDefinition_Override` |  |  |  |
| 20 | `OA.PD.RECORD.STATUS` | `OaPolicyDefinition_RecordStatus` | String |  |  |
| 21 | `OA.PD.CURR.NO` | `OaPolicyDefinition_CurrNo` | String |  |  |
| 22 | `OA.PD.INPUTTER` | `OaPolicyDefinition_Inputter` |  |  |  |
| 23 | `OA.PD.DATE.TIME` | `OaPolicyDefinition_DateTime` |  |  |  |
| 24 | `OA.PD.AUTHORISER` | `OaPolicyDefinition_Authoriser` | String |  |  |
| 25 | `OA.PD.CO.CODE` | `OaPolicyDefinition_CoCode` | String |  |  |
| 26 | `OA.PD.DEPT.CODE` | `OaPolicyDefinition_DeptCode` | String |  |  |
| 27 | `OA.PD.AUDITOR.CODE` | `OaPolicyDefinition_AuditorCode` | String |  |  |
| 28 | `OA.PD.AUDIT.DATE.TIME` | `OaPolicyDefinition_AuditDateTime` | String |  |  |
