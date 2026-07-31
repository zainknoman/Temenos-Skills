# EB.WARMUP.SESSIONS — Table Schema

> Source: `INSERTS/I_F.EB.WARMUP.SESSIONS` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.WPS.WARMUP.GROUP` | `EbWarmupSessions_WarmupGroup` |  |  |  |
| 2 | `EB.WPS.RESERVED.5` | `EbWarmupSessions_Reserved5` |  |  |  |
| 3 | `EB.WPS.RESERVED.4` | `EbWarmupSessions_Reserved4` |  |  |  |
| 4 | `EB.WPS.RESERVED.3` | `EbWarmupSessions_Reserved3` | TField |  |  |
| 5 | `EB.WPS.RESERVED.2` | `EbWarmupSessions_Reserved2` | TField |  |  |
| 6 | `EB.WPS.RESERVED.1` | `EbWarmupSessions_Reserved1` | TField |  |  |
| 7 | `EB.WPS.RECORD.STATUS` | `EbWarmupSessions_RecordStatus` | String |  |  |
| 8 | `EB.WPS.CURR.NO` | `EbWarmupSessions_CurrNo` | String |  |  |
| 9 | `EB.WPS.INPUTTER` | `EbWarmupSessions_Inputter` |  |  |  |
| 10 | `EB.WPS.DATE.TIME` | `EbWarmupSessions_DateTime` |  |  |  |
| 11 | `EB.WPS.AUTHORISER` | `EbWarmupSessions_Authoriser` | String |  |  |
| 12 | `EB.WPS.CO.CODE` | `EbWarmupSessions_CoCode` | String |  |  |
| 13 | `EB.WPS.DEPT.CODE` | `EbWarmupSessions_DeptCode` | String |  |  |
| 14 | `EB.WPS.AUDITOR.CODE` | `EbWarmupSessions_AuditorCode` | String |  |  |
| 15 | `EB.WPS.AUDIT.DATE.TIME` | `EbWarmupSessions_AuditDateTime` | String |  |  |
