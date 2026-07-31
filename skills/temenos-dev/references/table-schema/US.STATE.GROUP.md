# US.STATE.GROUP — Table Schema

> Source: `INSERTS/I_F.US.STATE.GROUP` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STATE.GRP.DESCRIPTION` | `UsStateGroup_Description` |  |  |  |
| 2 | `STATE.GRP.GROUP.CONTEXT` | `UsStateGroup_GroupContext` | TField |  | The group context would be released by Temenos. The group context released for dormancy will be DORMANCY in EB.LOOKUP NACUST.STATE.GROUP.CONTEXT. |
| 3 | `STATE.GRP.US.STATE` | `UsStateGroup_UsState` |  |  |  |
| 4 | `STATE.GRP.RESERVED.10` | `UsStateGroup_Reserved10` | TField |  |  |
| 5 | `STATE.GRP.RESERVED.9` | `UsStateGroup_Reserved9` | TField |  |  |
| 6 | `STATE.GRP.RESERVED.8` | `UsStateGroup_Reserved8` | TField |  |  |
| 7 | `STATE.GRP.RESERVED.7` | `UsStateGroup_Reserved7` | TField |  |  |
| 8 | `STATE.GRP.RESERVED.6` | `UsStateGroup_Reserved6` | TField |  |  |
| 9 | `STATE.GRP.RESERVED.5` | `UsStateGroup_Reserved5` | TField |  |  |
| 10 | `STATE.GRP.RESERVED.4` | `UsStateGroup_Reserved4` | TField |  |  |
| 11 | `STATE.GRP.RESERVED.3` | `UsStateGroup_Reserved3` | TField |  |  |
| 12 | `STATE.GRP.RESERVED.2` | `UsStateGroup_Reserved2` | TField |  |  |
| 13 | `STATE.GRP.RESERVED.1` | `UsStateGroup_Reserved1` | TField |  |  |
| 14 | `STATE.GRP.LOCAL.REF` | `UsStateGroup_LocalRef` |  |  |  |
| 15 | `STATE.GRP.OVERRIDE` | `UsStateGroup_Override` |  |  |  |
| 16 | `STATE.GRP.RECORD.STATUS` | `UsStateGroup_RecordStatus` | String |  |  |
| 17 | `STATE.GRP.CURR.NO` | `UsStateGroup_CurrNo` | String |  |  |
| 18 | `STATE.GRP.INPUTTER` | `UsStateGroup_Inputter` |  |  |  |
| 19 | `STATE.GRP.DATE.TIME` | `UsStateGroup_DateTime` |  |  |  |
| 20 | `STATE.GRP.AUTHORISER` | `UsStateGroup_Authoriser` | String |  |  |
| 21 | `STATE.GRP.CO.CODE` | `UsStateGroup_CoCode` | String |  |  |
| 22 | `STATE.GRP.DEPT.CODE` | `UsStateGroup_DeptCode` | String |  |  |
| 23 | `STATE.GRP.AUDITOR.CODE` | `UsStateGroup_AuditorCode` | String |  |  |
| 24 | `STATE.GRP.AUDIT.DATE.TIME` | `UsStateGroup_AuditDateTime` | String |  |  |
