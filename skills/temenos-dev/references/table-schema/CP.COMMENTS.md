# CP.COMMENTS — Table Schema

> Source: `INSERTS/I_F.CP.COMMENTS` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CM.WORKFLOW.ID` | `CpComments_WorkflowId` | TField |  | This field stores the ID of the entity workflow. Validation Rules :50 text characters. |
| 2 | `CP.CM.ID.RECORD` | `CpComments_IdRecord` | TField | Yes | This field stores the ID of the campaign or campaign program for which the comment is added. Validation Rules :Mandatory field, 35 text characters. |
| 3 | `CP.CM.OWNER` | `CpComments_Owner` | TField |  | This field stores the name of the user who ads a comment to a campaign or program.This field links the CP.COMMENTS table to the USER one. Validation Rules :35 string characters. |
| 4 | `CP.CM.COMMENTS` | `CpComments_Comments` |  |  |  |
| 5 | `CP.CM.DATE` | `CpComments_Date` | TField |  | This field stores the date when the comment is added. |
| 6 | `CP.CM.HISTORY.STATUS` | `CpComments_HistoryStatus` | TField |  | This field stores the status of the campaign or program when the user ads a comment. Validation Rules :35 string characters. |
| 7 | `CP.CM.WORKFLOW.TYPE` | `CpComments_WorkflowType` | TField |  | This field stores the values of the field WORKFLOW.TYPE from the table CP.ENTITY.WORKFLOW. Validation Rules :Any 50 characters. |
| 8 | `CP.CM.GENERATED` | `CpComments_Generated` | TField |  | This field marks the fact that this comment was generated automaticaly. If 'Y', then the comment was generated ok. Otherwise a new comment will manualy be created. |
| 9 | `CP.CM.RESERVED.8` | `CpComments_Reserved8` | TField |  |  |
| 10 | `CP.CM.RESERVED.7` | `CpComments_Reserved7` | TField |  |  |
| 11 | `CP.CM.RESERVED.6` | `CpComments_Reserved6` | TField |  |  |
| 12 | `CP.CM.RESERVED.5` | `CpComments_Reserved5` | TField |  |  |
| 13 | `CP.CM.RESERVED.4` | `CpComments_Reserved4` | TField |  |  |
| 14 | `CP.CM.RESERVED.3` | `CpComments_Reserved3` | TField |  |  |
| 15 | `CP.CM.RESERVED.2` | `CpComments_Reserved2` | TField |  |  |
| 16 | `CP.CM.RESERVED.1` | `CpComments_Reserved1` | TField |  |  |
| 17 | `CP.CM.LOCAL.REF` | `CpComments_LocalRef` |  |  |  |
| 18 | `CP.CM.OVERRIDE` | `CpComments_Override` |  |  |  |
| 19 | `CP.CM.RECORD.STATUS` | `CpComments_RecordStatus` | String |  |  |
| 20 | `CP.CM.CURR.NO` | `CpComments_CurrNo` | String |  |  |
| 21 | `CP.CM.INPUTTER` | `CpComments_Inputter` |  |  |  |
| 22 | `CP.CM.DATE.TIME` | `CpComments_DateTime` |  |  |  |
| 23 | `CP.CM.AUTHORISER` | `CpComments_Authoriser` | String |  |  |
| 24 | `CP.CM.CO.CODE` | `CpComments_CoCode` | String |  |  |
| 25 | `CP.CM.DEPT.CODE` | `CpComments_DeptCode` | String |  |  |
| 26 | `CP.CM.AUDITOR.CODE` | `CpComments_AuditorCode` | String |  |  |
| 27 | `CP.CM.AUDIT.DATE.TIME` | `CpComments_AuditDateTime` | String |  |  |
