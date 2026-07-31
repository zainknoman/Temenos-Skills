# PW.DEF.PUBLISHER — Table Schema

> Source: `INSERTS/I_F.PW.DEF.PUBLISHER` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.DEF.PUBLISH.PWD.ID` | `PwDefPublisher_PwdId` |  |  |  |
| 2 | `PW.DEF.PUBLISH.RESERVED.8` | `PwDefPublisher_Reserved8` | TField |  |  |
| 3 | `PW.DEF.PUBLISH.RESERVED.7` | `PwDefPublisher_Reserved7` | TField |  |  |
| 4 | `PW.DEF.PUBLISH.RESERVED.6` | `PwDefPublisher_Reserved6` | TField |  |  |
| 5 | `PW.DEF.PUBLISH.RESERVED.5` | `PwDefPublisher_Reserved5` | TField |  |  |
| 6 | `PW.DEF.PUBLISH.RESERVED.4` | `PwDefPublisher_Reserved4` | TField |  |  |
| 7 | `PW.DEF.PUBLISH.RESERVED.3` | `PwDefPublisher_Reserved3` | TField |  |  |
| 8 | `PW.DEF.PUBLISH.RESERVED.2` | `PwDefPublisher_Reserved2` | TField |  |  |
| 9 | `PW.DEF.PUBLISH.VERSION` | `PwDefPublisher_Version` | TField |  | PW.DEF.PUBLISHER VERSION This field handles the LIVE RECORD NOT CHANGED problem Validation Rules: This is a non input numeric field. The value in this field auto increments every time the record is committed |
| 10 | `PW.DEF.PUBLISH.RECORD.STATUS` | `PwDefPublisher_RecordStatus` | String |  |  |
| 11 | `PW.DEF.PUBLISH.CURR.NO` | `PwDefPublisher_CurrNo` | String |  |  |
| 12 | `PW.DEF.PUBLISH.INPUTTER` | `PwDefPublisher_Inputter` |  |  |  |
| 13 | `PW.DEF.PUBLISH.DATE.TIME` | `PwDefPublisher_DateTime` |  |  |  |
| 14 | `PW.DEF.PUBLISH.AUTHORISER` | `PwDefPublisher_Authoriser` | String |  |  |
| 15 | `PW.DEF.PUBLISH.CO.CODE` | `PwDefPublisher_CoCode` | String |  |  |
| 16 | `PW.DEF.PUBLISH.DEPT.CODE` | `PwDefPublisher_DeptCode` | String |  |  |
| 17 | `PW.DEF.PUBLISH.AUDITOR.CODE` | `PwDefPublisher_AuditorCode` | String |  |  |
| 18 | `PW.DEF.PUBLISH.AUDIT.DATE.TIME` | `PwDefPublisher_AuditDateTime` | String |  |  |
