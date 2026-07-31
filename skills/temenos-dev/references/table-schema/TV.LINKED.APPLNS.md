# TV.LINKED.APPLNS — Table Schema

> Source: `INSERTS/I_F.TV.LINKED.APPLNS` in `TV_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TLA.BASE.APPLICATION` | `TvLinkedApplns_BaseApplication` |  |  |  |
| 2 | `EB.TLA.LINKED.APPLN` | `TvLinkedApplns_LinkedAppln` |  |  |  |
| 3 | `EB.TLA.PARENT.APPLN` | `TvLinkedApplns_ParentAppln` |  |  |  |
| 4 | `EB.TLA.TRACE.FLD` | `TvLinkedApplns_TraceFld` |  |  |  |
| 5 | `EB.TLA.RESERVED.6` | `TvLinkedApplns_Reserved6` | TField |  |  |
| 6 | `EB.TLA.RESERVED.5` | `TvLinkedApplns_Reserved5` | TField |  |  |
| 7 | `EB.TLA.RESERVED.4` | `TvLinkedApplns_Reserved4` | TField |  |  |
| 8 | `EB.TLA.RESERVED.3` | `TvLinkedApplns_Reserved3` | TField |  |  |
| 9 | `EB.TLA.RESERVED.2` | `TvLinkedApplns_Reserved2` | TField |  |  |
| 10 | `EB.TLA.RESERVED.1` | `TvLinkedApplns_Reserved1` | TField |  |  |
| 11 | `EB.TLA.RECORD.STATUS` | `TvLinkedApplns_RecordStatus` | String |  |  |
| 12 | `EB.TLA.CURR.NO` | `TvLinkedApplns_CurrNo` | String |  |  |
| 13 | `EB.TLA.INPUTTER` | `TvLinkedApplns_Inputter` |  |  |  |
| 14 | `EB.TLA.DATE.TIME` | `TvLinkedApplns_DateTime` |  |  |  |
| 15 | `EB.TLA.AUTHORISER` | `TvLinkedApplns_Authoriser` | String |  |  |
| 16 | `EB.TLA.CO.CODE` | `TvLinkedApplns_CoCode` | String |  |  |
| 17 | `EB.TLA.DEPT.CODE` | `TvLinkedApplns_DeptCode` | String |  |  |
| 18 | `EB.TLA.AUDITOR.CODE` | `TvLinkedApplns_AuditorCode` | String |  |  |
| 19 | `EB.TLA.AUDIT.DATE.TIME` | `TvLinkedApplns_AuditDateTime` | String |  |  |
