# SC.NCI.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SC.NCI.PARAMETER` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.NCI.FIELD.NAME` | `ScNciParameter_FieldName` |  |  |  |
| 2 | `SC.NCI.FIELD.VALUE` | `ScNciParameter_FieldValue` |  |  |  |
| 3 | `SC.NCI.NO.OF.CHAR` | `ScNciParameter_NoOfChar` |  |  |  |
| 4 | `SC.NCI.PREFIX` | `ScNciParameter_Prefix` |  |  |  |
| 5 | `SC.NCI.OUTPUT` | `ScNciParameter_Output` |  |  |  |
| 6 | `SC.NCI.INPUT` | `ScNciParameter_Input` |  |  |  |
| 7 | `SC.NCI.LOCAL.REF` | `ScNciParameter_LocalRef` |  |  |  |
| 8 | `SC.NCI.OVERRIDE` | `ScNciParameter_Override` |  |  |  |
| 9 | `SC.NCI.RECORD.STATUS` | `ScNciParameter_RecordStatus` | String |  |  |
| 10 | `SC.NCI.CURR.NO` | `ScNciParameter_CurrNo` | String |  |  |
| 11 | `SC.NCI.INPUTTER` | `ScNciParameter_Inputter` |  |  |  |
| 12 | `SC.NCI.DATE.TIME` | `ScNciParameter_DateTime` |  |  |  |
| 13 | `SC.NCI.AUTHORISER` | `ScNciParameter_Authoriser` | String |  |  |
| 14 | `SC.NCI.CO.CODE` | `ScNciParameter_CoCode` | String |  |  |
| 15 | `SC.NCI.DEPT.CODE` | `ScNciParameter_DeptCode` | String |  |  |
| 16 | `SC.NCI.AUDITOR.CODE` | `ScNciParameter_AuditorCode` | String |  |  |
| 17 | `SC.NCI.AUDIT.DATE.TIME` | `ScNciParameter_AuditDateTime` | String |  |  |
