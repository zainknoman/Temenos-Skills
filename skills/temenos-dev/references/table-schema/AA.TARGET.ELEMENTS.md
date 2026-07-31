# AA.TARGET.ELEMENTS — Table Schema

> Source: `INSERTS/I_F.AA.TARGET.ELEMENTS` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DESCRIPTION` | `AaTargetElements_Description` |  |  |  |
| 2 | `AA.TYPE` | `AaTargetElements_Type` | TField | Yes | Mandatory field. Allows a valid type. User to choose one of the available TYPE from dropdown. Currently, this is restricted to 2 values &apos;Margin&apos; and &apos;Fixed Rate&apos;. |
| 3 | `AA.FIELD` | `AaTargetElements_Field` |  |  |  |
| 4 | `AA.DATATYPE` | `AaTargetElements_Datatype` |  |  |  |
| 5 | `AA.VALUE.TYPE` | `AaTargetElements_ValueType` |  |  |  |
| 6 | `AA.VALUE` | `AaTargetElements_Value` |  |  |  |
| 7 | `AA.OVERRIDE` | `AaTargetElements_Override` |  |  |  |
| 8 | `AA.RECORD.STATUS` | `AaTargetElements_RecordStatus` | String |  |  |
| 9 | `AA.CURR.NO` | `AaTargetElements_CurrNo` | String |  |  |
| 10 | `AA.INPUTTER` | `AaTargetElements_Inputter` |  |  |  |
| 11 | `AA.DATE.TIME` | `AaTargetElements_DateTime` |  |  |  |
| 12 | `AA.AUTHORISER` | `AaTargetElements_Authoriser` | String |  |  |
| 13 | `AA.CO.CODE` | `AaTargetElements_CoCode` | String |  |  |
| 14 | `AA.DEPT.CODE` | `AaTargetElements_DeptCode` | String |  |  |
| 15 | `AA.AUDITOR.CODE` | `AaTargetElements_AuditorCode` | String |  |  |
| 16 | `AA.AUDIT.DATE.TIME` | `AaTargetElements_AuditDateTime` | String |  |  |
