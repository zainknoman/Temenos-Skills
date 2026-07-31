# CL.ACTION — Table Schema

> Source: `INSERTS/I_F.CL.ACTION` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.ACT.DESCRIPTION` | `ClAction_Description` |  |  |  |
| 2 | `CL.ACT.ACTION.COST` | `ClAction_ActionCost` |  |  |  |
| 3 | `CL.ACT.LOCAL.REF` | `ClAction_LocalRef` |  |  |  |
| 4 | `CL.ACT.RESERVED.5` | `ClAction_Reserved5` |  |  |  |
| 5 | `CL.ACT.RESERVED.4` | `ClAction_Reserved4` |  |  |  |
| 6 | `CL.ACT.RESERVED.3` | `ClAction_Reserved3` |  |  |  |
| 7 | `CL.ACT.RESERVED.2` | `ClAction_Reserved2` |  |  |  |
| 8 | `CL.ACT.RESERVED.1` | `ClAction_Reserved1` |  |  |  |
| 9 | `CL.ACT.RECORD.STATUS` | `ClAction_RecordStatus` |  |  |  |
| 10 | `CL.ACT.CURR.NO` | `ClAction_CurrNo` |  |  |  |
| 11 | `CL.ACT.INPUTTER` | `ClAction_Inputter` |  |  |  |
| 12 | `CL.ACT.DATE.TIME` | `ClAction_DateTime` |  |  |  |
| 13 | `CL.ACT.AUTHORISER` | `ClAction_Authoriser` |  |  |  |
| 14 | `CL.ACT.CO.CODE` | `ClAction_CoCode` |  |  |  |
| 15 | `CL.ACT.DEPT.CODE` | `ClAction_DeptCode` |  |  |  |
| 16 | `CL.ACT.AUDITOR.CODE` | `ClAction_AuditorCode` |  |  |  |
| 17 | `CL.ACT.AUDIT.DATE.TIME` | `ClAction_AuditDateTime` |  |  |  |
