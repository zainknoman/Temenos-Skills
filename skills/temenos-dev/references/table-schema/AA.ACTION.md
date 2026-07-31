# AA.ACTION — Table Schema

> Source: `INSERTS/I_F.AA.ACTION` in `AA_ActivityControl.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACTION.DESCRIPTION` | `AaAction_Description` |  |  |  |
| 2 | `AA.ACTION.ACTIVITY` | `AaAction_Activity` |  |  |  |
| 3 | `AA.ACTION.PRODUCT` | `AaAction_Product` | TField |  |  |
| 4 | `AA.ACTION.ARRANGEMENT.LEVEL` | `AaAction_ArrangementLevel` | TField |  | Field to specify if the activities are defined for Facility or Deal. Allowed values are FACILITY, DEAL Validation Rules: Default value is Facility when activities of FACILITY product line is defined in the field ACTIVITY. Applicable only for FACILITY product line. |
| 5 | `AA.ACTION.RESERVED.3` | `AaAction_Reserved3` | TField |  |  |
| 6 | `AA.ACTION.RESERVED.2` | `AaAction_Reserved2` | TField |  |  |
| 7 | `AA.ACTION.RESERVED.1` | `AaAction_Reserved1` | TField |  |  |
| 8 | `AA.ACTION.LOCAL.REF` | `AaAction_LocalRef` |  |  |  |
| 9 | `AA.ACTION.OVERRIDE` | `AaAction_Override` |  |  |  |
| 10 | `AA.ACTION.RECORD.STATUS` | `AaAction_RecordStatus` | String |  |  |
| 11 | `AA.ACTION.CURR.NO` | `AaAction_CurrNo` | String |  |  |
| 12 | `AA.ACTION.INPUTTER` | `AaAction_Inputter` |  |  |  |
| 13 | `AA.ACTION.DATE.TIME` | `AaAction_DateTime` |  |  |  |
| 14 | `AA.ACTION.AUTHORISER` | `AaAction_Authoriser` | String |  |  |
| 15 | `AA.ACTION.CO.CODE` | `AaAction_CoCode` | String |  |  |
| 16 | `AA.ACTION.DEPT.CODE` | `AaAction_DeptCode` | String |  |  |
| 17 | `AA.ACTION.AUDITOR.CODE` | `AaAction_AuditorCode` | String |  |  |
| 18 | `AA.ACTION.AUDIT.DATE.TIME` | `AaAction_AuditDateTime` | String |  |  |
| 19 | `AA.ACTION.ACTION` | `AaAction_Action` | TField |  |  |
