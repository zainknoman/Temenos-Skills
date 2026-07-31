# OA.OWNERSHIP.DEFINITION — Table Schema

> Source: `INSERTS/I_F.OA.OWNERSHIP.DEFINITION` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.OWD.DESCRIPTION` | `OaOwnershipDefinition_Description` |  |  |  |
| 2 | `OA.OWD.FULL.DESCRIPTION` | `OaOwnershipDefinition_FullDescription` |  |  |  |
| 3 | `OA.OWD.RULE` | `OaOwnershipDefinition_Rule` |  |  |  |
| 4 | `OA.OWD.OWNER` | `OaOwnershipDefinition_Owner` |  |  |  |
| 5 | `OA.OWD.DEFAULT.OWNER` | `OaOwnershipDefinition_DefaultOwner` | TField |  | This field will specify the default dossier owner, when none of the rules are successful. |
| 6 | `OA.OWD.RESERVED.FIELD.5` | `OaOwnershipDefinition_ReservedField5` | TField |  |  |
| 7 | `OA.OWD.RESERVED.FIELD.4` | `OaOwnershipDefinition_ReservedField4` | TField |  |  |
| 8 | `OA.OWD.RESERVED.FIELD.3` | `OaOwnershipDefinition_ReservedField3` | TField |  |  |
| 9 | `OA.OWD.RESERVED.FIELD.2` | `OaOwnershipDefinition_ReservedField2` | TField |  |  |
| 10 | `OA.OWD.RESERVED.FIELD.1` | `OaOwnershipDefinition_ReservedField1` | TField |  |  |
| 11 | `OA.OWD.LOCAL.REF` | `OaOwnershipDefinition_LocalRef` |  |  |  |
| 12 | `OA.OWD.OVERRIDE` | `OaOwnershipDefinition_Override` |  |  |  |
| 13 | `OA.OWD.RECORD.STATUS` | `OaOwnershipDefinition_RecordStatus` | String |  |  |
| 14 | `OA.OWD.CURR.NO` | `OaOwnershipDefinition_CurrNo` | String |  |  |
| 15 | `OA.OWD.INPUTTER` | `OaOwnershipDefinition_Inputter` |  |  |  |
| 16 | `OA.OWD.DATE.TIME` | `OaOwnershipDefinition_DateTime` |  |  |  |
| 17 | `OA.OWD.AUTHORISER` | `OaOwnershipDefinition_Authoriser` | String |  |  |
| 18 | `OA.OWD.CO.CODE` | `OaOwnershipDefinition_CoCode` | String |  |  |
| 19 | `OA.OWD.DEPT.CODE` | `OaOwnershipDefinition_DeptCode` | String |  |  |
| 20 | `OA.OWD.AUDITOR.CODE` | `OaOwnershipDefinition_AuditorCode` | String |  |  |
| 21 | `OA.OWD.AUDIT.DATE.TIME` | `OaOwnershipDefinition_AuditDateTime` | String |  |  |
