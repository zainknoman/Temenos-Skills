# CANNEX.REREG.RULE.CHECK — Table Schema

> Source: `INSERTS/I_F.CANNEX.REREG.RULE.CHECK` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REREG.RULE.DESCRIPTION` | `CannexReregRuleCheck_Description` | TField |  | The Purpose of this field is used to define the description for the record.Alphanumeric with 20 characters. |
| 2 | `REREG.RULE.APPLICATION` | `CannexReregRuleCheck_Application` |  |  |  |
| 3 | `REREG.RULE.APPLICATION.ID` | `CannexReregRuleCheck_ApplicationId` |  |  |  |
| 4 | `REREG.RULE.AA.CONDITION` | `CannexReregRuleCheck_AaCondition` |  |  |  |
| 5 | `REREG.RULE.FIELD.NAME` | `CannexReregRuleCheck_FieldName` |  |  |  |
| 6 | `REREG.RULE.FIELD.OPERAND` | `CannexReregRuleCheck_FieldOperand` |  |  |  |
| 7 | `REREG.RULE.FIELD.VALUE` | `CannexReregRuleCheck_FieldValue` |  |  |  |
| 8 | `REREG.RULE.RESERVED.15` | `CannexReregRuleCheck_Reserved15` |  |  |  |
| 9 | `REREG.RULE.RESERVED.14` | `CannexReregRuleCheck_Reserved14` |  |  |  |
| 10 | `REREG.RULE.RESERVED.13` | `CannexReregRuleCheck_Reserved13` |  |  |  |
| 11 | `REREG.RULE.RESERVED.12` | `CannexReregRuleCheck_Reserved12` |  |  |  |
| 12 | `REREG.RULE.RESERVED.11` | `CannexReregRuleCheck_Reserved11` |  |  |  |
| 13 | `REREG.RULE.CONNECTOR` | `CannexReregRuleCheck_Connector` |  |  |  |
| 14 | `REREG.RULE.ERROR` | `CannexReregRuleCheck_Error` |  |  |  |
| 15 | `REREG.RULE.OVERRIDE.DISPLAY` | `CannexReregRuleCheck_OverrideDisplay` |  |  |  |
| 16 | `REREG.RULE.VERSION` | `CannexReregRuleCheck_Version` |  |  |  |
| 17 | `REREG.RULE.CONV.ROUTINE` | `CannexReregRuleCheck_ConvRoutine` | TField |  | This field is used to define the conversion routine to derive the value using routine Valid record from EB.API. |
| 18 | `REREG.RULE.RESERVED.10` | `CannexReregRuleCheck_Reserved10` | TField |  |  |
| 19 | `REREG.RULE.RESERVED.9` | `CannexReregRuleCheck_Reserved9` | TField |  |  |
| 20 | `REREG.RULE.RESERVED.8` | `CannexReregRuleCheck_Reserved8` | TField |  |  |
| 21 | `REREG.RULE.RESERVED.7` | `CannexReregRuleCheck_Reserved7` | TField |  |  |
| 22 | `REREG.RULE.RESERVED.6` | `CannexReregRuleCheck_Reserved6` | TField |  |  |
| 23 | `REREG.RULE.RESERVED.5` | `CannexReregRuleCheck_Reserved5` | TField |  |  |
| 24 | `REREG.RULE.RESERVED.4` | `CannexReregRuleCheck_Reserved4` | TField |  |  |
| 25 | `REREG.RULE.RESERVED.3` | `CannexReregRuleCheck_Reserved3` | TField |  |  |
| 26 | `REREG.RULE.RESERVED.2` | `CannexReregRuleCheck_Reserved2` | TField |  |  |
| 27 | `REREG.RULE.RESERVED.1` | `CannexReregRuleCheck_Reserved1` | TField |  |  |
| 28 | `REREG.RULE.LOCAL.REF` | `CannexReregRuleCheck_LocalRef` |  |  |  |
| 29 | `REREG.RULE.OVERRIDE` | `CannexReregRuleCheck_Override` |  |  |  |
| 30 | `REREG.RULE.RECORD.STATUS` | `CannexReregRuleCheck_RecordStatus` | String |  |  |
| 31 | `REREG.RULE.CURR.NO` | `CannexReregRuleCheck_CurrNo` | String |  |  |
| 32 | `REREG.RULE.INPUTTER` | `CannexReregRuleCheck_Inputter` |  |  |  |
| 33 | `REREG.RULE.DATE.TIME` | `CannexReregRuleCheck_DateTime` |  |  |  |
| 34 | `REREG.RULE.AUTHORISER` | `CannexReregRuleCheck_Authoriser` | String |  |  |
| 35 | `REREG.RULE.CO.CODE` | `CannexReregRuleCheck_CoCode` | String |  |  |
| 36 | `REREG.RULE.DEPT.CODE` | `CannexReregRuleCheck_DeptCode` | String |  |  |
| 37 | `REREG.RULE.AUDITOR.CODE` | `CannexReregRuleCheck_AuditorCode` | String |  |  |
| 38 | `REREG.RULE.AUDIT.DATE.TIME` | `CannexReregRuleCheck_AuditDateTime` | String |  |  |
