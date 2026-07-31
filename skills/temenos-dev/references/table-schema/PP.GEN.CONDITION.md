# PP.GEN.CONDITION — Table Schema

> Source: `INSERTS/I_F.PP.GEN.CONDITION` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DEV.HLP.DESCRIPTION` | `PpGenCondition_Description` |  |  |  |
| 2 | `EB.DEV.HLP.ITEM` | `PpGenCondition_Item` |  |  |  |
| 3 | `EB.DEV.HLP.PRIORITY` | `PpGenCondition_Priority` |  |  |  |
| 4 | `EB.DEV.HLP.VALUE` | `PpGenCondition_Value` |  |  |  |
| 5 | `EB.DEV.HLP.MULTIVALUE` | `PpGenCondition_Multivalue` | TField |  | This field is used to expand the associated multivalue set of fields ITEM, PRIORITY and VALUE in PP.GEN.CONDITION. If YES is input, the associated multivalue set is expanded. It is a hot field. Validation Rules: Values can be YES or NO |
| 6 | `EB.DEV.HLP.RECORD.STATUS` | `PpGenCondition_RecordStatus` | String |  |  |
| 7 | `EB.DEV.HLP.CURR.NO` | `PpGenCondition_CurrNo` | String |  |  |
| 8 | `EB.DEV.HLP.INPUTTER` | `PpGenCondition_Inputter` |  |  |  |
| 9 | `EB.DEV.HLP.DATE.TIME` | `PpGenCondition_DateTime` |  |  |  |
| 10 | `EB.DEV.HLP.AUTHORISER` | `PpGenCondition_Authoriser` | String |  |  |
| 11 | `EB.DEV.HLP.CO.CODE` | `PpGenCondition_CoCode` | String |  |  |
| 12 | `EB.DEV.HLP.DEPT.CODE` | `PpGenCondition_DeptCode` | String |  |  |
| 13 | `EB.DEV.HLP.AUDITOR.CODE` | `PpGenCondition_AuditorCode` | String |  |  |
| 14 | `EB.DEV.HLP.AUDIT.DATE.TIME` | `PpGenCondition_AuditDateTime` | String |  |  |
