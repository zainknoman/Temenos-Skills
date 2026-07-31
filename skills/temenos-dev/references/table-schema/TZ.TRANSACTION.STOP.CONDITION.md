# TZ.TRANSACTION.STOP.CONDITION — Table Schema

> Source: `INSERTS/I_F.TZ.TRANSACTION.STOP.CONDITION` in `TZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TZ.TSC.DESCRIPTION` | `TzTransactionStopCondition_Description` |  |  |  |
| 2 | `TZ.TSC.ATTRIBUTE.NAME` | `TzTransactionStopCondition_AttributeName` |  |  |  |
| 3 | `TZ.TSC.ALLOWED.OPERAND` | `TzTransactionStopCondition_AllowedOperand` |  |  |  |
| 4 | `TZ.TSC.ATTRIB.FMT.API` | `TzTransactionStopCondition_AttribFmtApi` | TField |  | Field to attach any API routines for processing/modifications of Stop Instruction Attributes and Values defined as required Arguments: StopInstructionAttributes - Input - Contains the Attributes defined StopInstructionAttributeValues - Input - Contains Attributes values - Output - Contains Processed Attributes values ReturnInfo Spare1 Spare2 Spare3 Validation Rule: Should have an Entry in EB.API |
| 5 | `TZ.TSC.RESERVED.4` | `TzTransactionStopCondition_Reserved4` | TField |  |  |
| 6 | `TZ.TSC.RESERVED.3` | `TzTransactionStopCondition_Reserved3` | TField |  |  |
| 7 | `TZ.TSC.RESERVED.2` | `TzTransactionStopCondition_Reserved2` | TField |  |  |
| 8 | `TZ.TSC.RESERVED.1` | `TzTransactionStopCondition_Reserved1` | TField |  |  |
| 9 | `TZ.TSC.LOCAL.REF` | `TzTransactionStopCondition_LocalRef` |  |  |  |
| 10 | `TZ.TSC.OVERRIDE` | `TzTransactionStopCondition_Override` |  |  |  |
| 11 | `TZ.TSC.RECORD.STATUS` | `TzTransactionStopCondition_RecordStatus` | String |  |  |
| 12 | `TZ.TSC.CURR.NO` | `TzTransactionStopCondition_CurrNo` | String |  |  |
| 13 | `TZ.TSC.INPUTTER` | `TzTransactionStopCondition_Inputter` |  |  |  |
| 14 | `TZ.TSC.DATE.TIME` | `TzTransactionStopCondition_DateTime` |  |  |  |
| 15 | `TZ.TSC.AUTHORISER` | `TzTransactionStopCondition_Authoriser` | String |  |  |
| 16 | `TZ.TSC.CO.CODE` | `TzTransactionStopCondition_CoCode` | String |  |  |
| 17 | `TZ.TSC.DEPT.CODE` | `TzTransactionStopCondition_DeptCode` | String |  |  |
| 18 | `TZ.TSC.AUDITOR.CODE` | `TzTransactionStopCondition_AuditorCode` | String |  |  |
| 19 | `TZ.TSC.AUDIT.DATE.TIME` | `TzTransactionStopCondition_AuditDateTime` | String |  |  |
