# SC.STAPLES.REBUILDER — Table Schema

> Source: `INSERTS/I_F.SC.STAPLES.REBUILDER` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SR.STAPLE.PARENT` | `ScStaplesRebuilder_StapleParent` |  |  |  |
| 2 | `SC.SR.NARRATIVE` | `ScStaplesRebuilder_Narrative` |  |  |  |
| 3 | `SC.SR.STATUS` | `ScStaplesRebuilder_Status` | TField |  | Indicates the status of the rebuild process Allowed Values : ACTIVATED , PROCESSED When the record is authorised, the status will be marked as ACTIVATED When the staple rebuild processing is completed, the status will be marked as PROCESSED. |
| 4 | `SC.SR.LOCAL.REF` | `ScStaplesRebuilder_LocalRef` |  |  |  |
| 5 | `SC.SR.OVERRIDE` | `ScStaplesRebuilder_Override` |  |  |  |
| 6 | `SC.SR.RECORD.STATUS` | `ScStaplesRebuilder_RecordStatus` | String |  |  |
| 7 | `SC.SR.CURR.NO` | `ScStaplesRebuilder_CurrNo` | String |  |  |
| 8 | `SC.SR.INPUTTER` | `ScStaplesRebuilder_Inputter` |  |  |  |
| 9 | `SC.SR.DATE.TIME` | `ScStaplesRebuilder_DateTime` |  |  |  |
| 10 | `SC.SR.AUTHORISER` | `ScStaplesRebuilder_Authoriser` | String |  |  |
| 11 | `SC.SR.CO.CODE` | `ScStaplesRebuilder_CoCode` | String |  |  |
| 12 | `SC.SR.DEPT.CODE` | `ScStaplesRebuilder_DeptCode` | String |  |  |
| 13 | `SC.SR.AUDITOR.CODE` | `ScStaplesRebuilder_AuditorCode` | String |  |  |
| 14 | `SC.SR.AUDIT.DATE.TIME` | `ScStaplesRebuilder_AuditDateTime` | String |  |  |
