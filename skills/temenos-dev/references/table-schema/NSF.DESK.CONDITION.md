# NSF.DESK.CONDITION — Table Schema

> Source: `INSERTS/I_F.NSF.DESK.CONDITION` in `NSFDES_DeskMgmt.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DSK.COND.DESCRIPTION` | `NsfDeskCondition_Description` |  |  |  |
| 2 | `DSK.COND.SOURCE.INFO` | `NsfDeskCondition_SourceInfo` |  |  |  |
| 3 | `DSK.COND.RESERVED.10` | `NsfDeskCondition_Reserved10` | TField |  |  |
| 4 | `DSK.COND.RESERVED.9` | `NsfDeskCondition_Reserved9` | TField |  |  |
| 5 | `DSK.COND.RESERVED.8` | `NsfDeskCondition_Reserved8` | TField |  |  |
| 6 | `DSK.COND.RESERVED.7` | `NsfDeskCondition_Reserved7` | TField |  |  |
| 7 | `DSK.COND.RESERVED.6` | `NsfDeskCondition_Reserved6` | TField |  |  |
| 8 | `DSK.COND.RESERVED.5` | `NsfDeskCondition_Reserved5` | TField |  |  |
| 9 | `DSK.COND.RESERVED.4` | `NsfDeskCondition_Reserved4` | TField |  |  |
| 10 | `DSK.COND.RESERVED.3` | `NsfDeskCondition_Reserved3` | TField |  |  |
| 11 | `DSK.COND.RESERVED.2` | `NsfDeskCondition_Reserved2` | TField |  |  |
| 12 | `DSK.COND.RESERVED.1` | `NsfDeskCondition_Reserved1` | TField |  |  |
| 13 | `DSK.COND.OVERRIDE` | `NsfDeskCondition_Override` |  |  |  |
| 14 | `DSK.COND.RECORD.STATUS` | `NsfDeskCondition_RecordStatus` | String |  |  |
| 15 | `DSK.COND.CURR.NO` | `NsfDeskCondition_CurrNo` | String |  |  |
| 16 | `DSK.COND.INPUTTER` | `NsfDeskCondition_Inputter` |  |  |  |
| 17 | `DSK.COND.DATE.TIME` | `NsfDeskCondition_DateTime` |  |  |  |
| 18 | `DSK.COND.AUTHORISER` | `NsfDeskCondition_Authoriser` | String |  |  |
| 19 | `DSK.COND.CO.CODE` | `NsfDeskCondition_CoCode` | String |  |  |
| 20 | `DSK.COND.DEPT.CODE` | `NsfDeskCondition_DeptCode` | String |  |  |
| 21 | `DSK.COND.AUDITOR.CODE` | `NsfDeskCondition_AuditorCode` | String |  |  |
| 22 | `DSK.COND.AUDIT.DATE.TIME` | `NsfDeskCondition_AuditDateTime` | String |  |  |
