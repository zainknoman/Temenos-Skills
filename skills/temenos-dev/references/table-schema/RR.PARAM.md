# RR.PARAM — Table Schema

> Source: `INSERTS/I_F.RR.PARAM` in `EB_Streaming.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RR.ILP.REQUIRED` | `RrParam_IlpRequired` | TField |  | Indicates whether the table requires initial load processing (ILP) or not. If it is not set during the first time then the user cannot set it back to "YES" later. Also it will be set to "" once the ILP is completed for this table. |
| 2 | `RR.APPLICATION` | `RrParam_Application` | TField |  | Its a no input field and indicates the application name of the configured table. |
| 3 | `RR.DEFAULT.SIZE` | `RrParam_DefaultSize` | TField | No | It's an optional field indicates the maximum character length that any field can hold in the configured table. If this value entered it is set as COLWIDTH in $RR TAFC VOC record. |
| 4 | `RR.RESERVED.9` | `RrParam_Reserved9` |  |  |  |
| 5 | `RR.RESERVED.8` | `RrParam_Reserved8` |  |  |  |
| 6 | `RR.RESERVED.7` | `RrParam_Reserved7` | TField |  |  |
| 7 | `RR.RESERVED.6` | `RrParam_Reserved6` | TField |  |  |
| 8 | `RR.RESERVED.5` | `RrParam_Reserved5` | TField |  |  |
| 9 | `RR.RESERVED.4` | `RrParam_Reserved4` | TField |  |  |
| 10 | `RR.RESERVED.3` | `RrParam_Reserved3` | TField |  |  |
| 11 | `RR.RESERVED.2` | `RrParam_Reserved2` | TField |  |  |
| 12 | `RR.RESERVED.1` | `RrParam_Reserved1` | TField |  |  |
| 13 | `RR.OVERRIDE` | `RrParam_Override` |  |  |  |
| 14 | `RR.RECORD.STATUS` | `RrParam_RecordStatus` | String |  |  |
| 15 | `RR.CURR.NO` | `RrParam_CurrNo` | String |  |  |
| 16 | `RR.INPUTTER` | `RrParam_Inputter` |  |  |  |
| 17 | `RR.DATE.TIME` | `RrParam_DateTime` |  |  |  |
| 18 | `RR.AUTHORISER` | `RrParam_Authoriser` | String |  |  |
| 19 | `RR.CO.CODE` | `RrParam_CoCode` | String |  |  |
| 20 | `RR.DEPT.CODE` | `RrParam_DeptCode` | String |  |  |
| 21 | `RR.AUDITOR.CODE` | `RrParam_AuditorCode` | String |  |  |
| 22 | `RR.AUDIT.DATE.TIME` | `RrParam_AuditDateTime` | String |  |  |
