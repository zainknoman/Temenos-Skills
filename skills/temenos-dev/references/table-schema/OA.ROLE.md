# OA.ROLE — Table Schema

> Source: `INSERTS/I_F.OA.ROLE` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.RL.DESCRIPTION` | `OaRole_Description` |  |  |  |
| 2 | `OA.RL.FULL.DESCRIPTION` | `OaRole_FullDescription` | TField | Yes | Full description of the origination role. 1) 1 to 100 alphanumeric characters. 2) Mandatory input. |
| 3 | `OA.RL.SYSTEM.CREATED` | `OaRole_SystemCreated` | TField |  | Options field - with options as YES and NULL. This field will be set for System created origination roles. |
| 4 | `OA.RL.RESERVED.5` | `OaRole_Reserved5` | TField |  | System field - reserved for future use |
| 5 | `OA.RL.RESERVED.4` | `OaRole_Reserved4` | TField |  | System field - reserved for future use |
| 6 | `OA.RL.RESERVED.3` | `OaRole_Reserved3` | TField |  | System field - reserved for future use |
| 7 | `OA.RL.RESERVED.2` | `OaRole_Reserved2` | TField |  | System field - reserved for future use |
| 8 | `OA.RL.RESERVED.1` | `OaRole_Reserved1` | TField |  | System field - reserved for future use |
| 9 | `OA.RL.RECORD.STATUS` | `OaRole_RecordStatus` | String |  |  |
| 10 | `OA.RL.CURR.NO` | `OaRole_CurrNo` | String |  |  |
| 11 | `OA.RL.INPUTTER` | `OaRole_Inputter` |  |  |  |
| 12 | `OA.RL.DATE.TIME` | `OaRole_DateTime` |  |  |  |
| 13 | `OA.RL.AUTHORISER` | `OaRole_Authoriser` | String |  |  |
| 14 | `OA.RL.CO.CODE` | `OaRole_CoCode` | String |  |  |
| 15 | `OA.RL.DEPT.CODE` | `OaRole_DeptCode` | String |  |  |
| 16 | `OA.RL.AUDITOR.CODE` | `OaRole_AuditorCode` | String |  |  |
| 17 | `OA.RL.AUDIT.DATE.TIME` | `OaRole_AuditDateTime` | String |  |  |
