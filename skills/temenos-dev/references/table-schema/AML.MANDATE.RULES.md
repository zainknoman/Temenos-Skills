# AML.MANDATE.RULES — Table Schema

> Source: `INSERTS/I_F.AML.MANDATE.RULES` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AML.MAND.RULE.DESCRIPTION` | `AmlMandateRules_Description` |  |  |  |
| 2 | `AML.MAND.RULE.FIELD.NAME` | `AmlMandateRules_FieldName` |  |  |  |
| 3 | `AML.MAND.RULE.OPERAND` | `AmlMandateRules_Operand` |  |  |  |
| 4 | `AML.MAND.RULE.FIELD.VALUE` | `AmlMandateRules_FieldValue` |  |  |  |
| 5 | `AML.MAND.RULE.RESERVED.1` | `AmlMandateRules_Reserved1` |  |  |  |
| 6 | `AML.MAND.RULE.RESERVED.2` | `AmlMandateRules_Reserved2` |  |  |  |
| 7 | `AML.MAND.RULE.CONNECTOR` | `AmlMandateRules_Connector` |  |  |  |
| 8 | `AML.MAND.RULE.MANDATE.RECORD` | `AmlMandateRules_MandateRecord` |  |  |  |
| 9 | `AML.MAND.RULE.RESERVED.3` | `AmlMandateRules_Reserved3` |  |  |  |
| 10 | `AML.MAND.RULE.RESERVED.4` | `AmlMandateRules_Reserved4` |  |  |  |
| 11 | `AML.MAND.RULE.RESERVED.5` | `AmlMandateRules_Reserved5` | TField |  |  |
| 12 | `AML.MAND.RULE.RESERVED.6` | `AmlMandateRules_Reserved6` | TField |  |  |
| 13 | `AML.MAND.RULE.RESERVED.7` | `AmlMandateRules_Reserved7` | TField |  |  |
| 14 | `AML.MAND.RULE.RESERVED.8` | `AmlMandateRules_Reserved8` | TField |  |  |
| 15 | `AML.MAND.RULE.RESERVED.9` | `AmlMandateRules_Reserved9` | TField |  |  |
| 16 | `AML.MAND.RULE.RESERVED.10` | `AmlMandateRules_Reserved10` | TField |  |  |
| 17 | `AML.MAND.RULE.LOCAL.REF` | `AmlMandateRules_LocalRef` |  |  |  |
| 18 | `AML.MAND.RULE.RECORD.STATUS` | `AmlMandateRules_RecordStatus` | String |  |  |
| 19 | `AML.MAND.RULE.CURR.NO` | `AmlMandateRules_CurrNo` | String |  |  |
| 20 | `AML.MAND.RULE.INPUTTER` | `AmlMandateRules_Inputter` |  |  |  |
| 21 | `AML.MAND.RULE.DATE.TIME` | `AmlMandateRules_DateTime` |  |  |  |
| 22 | `AML.MAND.RULE.AUTHORISER` | `AmlMandateRules_Authoriser` | String |  |  |
| 23 | `AML.MAND.RULE.CO.CODE` | `AmlMandateRules_CoCode` | String |  |  |
| 24 | `AML.MAND.RULE.DEPT.CODE` | `AmlMandateRules_DeptCode` | String |  |  |
| 25 | `AML.MAND.RULE.AUDITOR.CODE` | `AmlMandateRules_AuditorCode` | String |  |  |
| 26 | `AML.MAND.RULE.AUDIT.DATE.TIME` | `AmlMandateRules_AuditDateTime` | String |  |  |
