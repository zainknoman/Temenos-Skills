# SC.AGENT.PLACE — Table Schema

> Source: `INSERTS/I_F.SC.AGENT.PLACE` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.AGPL.ADDRESS` | `ScAgentPlace_Address` |  |  |  |
| 2 | `SC.AGPL.RESERVED.1` | `ScAgentPlace_Reserved1` |  |  |  |
| 3 | `SC.AGPL.RESERVED.2` | `ScAgentPlace_Reserved2` | TField |  |  |
| 4 | `SC.AGPL.RESERVED.3` | `ScAgentPlace_Reserved3` | TField |  |  |
| 5 | `SC.AGPL.RESERVED.4` | `ScAgentPlace_Reserved4` | TField |  |  |
| 6 | `SC.AGPL.RESERVED.5` | `ScAgentPlace_Reserved5` | TField |  |  |
| 7 | `SC.AGPL.RESERVED.6` | `ScAgentPlace_Reserved6` | TField |  |  |
| 8 | `SC.AGPL.RESERVED.7` | `ScAgentPlace_Reserved7` | TField |  |  |
| 9 | `SC.AGPL.RESERVED.8` | `ScAgentPlace_Reserved8` | TField |  |  |
| 10 | `SC.AGPL.RESERVED.9` | `ScAgentPlace_Reserved9` | TField |  |  |
| 11 | `SC.AGPL.RESERVED.10` | `ScAgentPlace_Reserved10` | TField |  |  |
| 12 | `SC.AGPL.LOCAL.REF` | `ScAgentPlace_LocalRef` |  |  |  |
| 13 | `SC.AGPL.RECORD.STATUS` | `ScAgentPlace_RecordStatus` | String |  |  |
| 14 | `SC.AGPL.CURR.NO` | `ScAgentPlace_CurrNo` | String |  |  |
| 15 | `SC.AGPL.INPUTTER` | `ScAgentPlace_Inputter` |  |  |  |
| 16 | `SC.AGPL.DATE.TIME` | `ScAgentPlace_DateTime` |  |  |  |
| 17 | `SC.AGPL.AUTHORISER` | `ScAgentPlace_Authoriser` | String |  |  |
| 18 | `SC.AGPL.CO.CODE` | `ScAgentPlace_CoCode` | String |  |  |
| 19 | `SC.AGPL.DEPT.CODE` | `ScAgentPlace_DeptCode` | String |  |  |
| 20 | `SC.AGPL.AUDITOR.CODE` | `ScAgentPlace_AuditorCode` | String |  |  |
| 21 | `SC.AGPL.AUDIT.DATE.TIME` | `ScAgentPlace_AuditDateTime` | String |  |  |
