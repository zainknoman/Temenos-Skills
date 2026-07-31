# AU.APP.RULE — Table Schema

> Source: `INSERTS/I_F.AU.APP.RULE` in `AU_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AU.APP.BUSINESS.UNIT` | `AuAppRule_BusinessUnit` | TField |  |  |
| 2 | `AU.APP.APPLICATION` | `AuAppRule_Application` | TField |  |  |
| 3 | `AU.APP.RULE.ID` | `AuAppRule_RuleId` |  |  |  |
| 4 | `AU.APP.ACCT.CO` | `AuAppRule_AcctCo` |  |  |  |
| 5 | `AU.APP.LOCAL.ROUTINE` | `AuAppRule_LocalRoutine` | TField |  |  |
| 6 | `AU.APP.DEFAULT.ACCT.CO` | `AuAppRule_DefaultAcctCo` | TField |  |  |
| 7 | `AU.APP.RESERVED.8` | `AuAppRule_Reserved8` | TField |  |  |
| 8 | `AU.APP.RESERVED.7` | `AuAppRule_Reserved7` | TField |  |  |
| 9 | `AU.APP.RESERVED.6` | `AuAppRule_Reserved6` | TField |  |  |
| 10 | `AU.APP.RESERVED.5` | `AuAppRule_Reserved5` | TField |  |  |
| 11 | `AU.APP.RESERVED.4` | `AuAppRule_Reserved4` | TField |  |  |
| 12 | `AU.APP.RESERVED.3` | `AuAppRule_Reserved3` | TField |  |  |
| 13 | `AU.APP.LOCAL.REF` | `AuAppRule_LocalRef` |  |  |  |
| 14 | `AU.APP.OVERRIDE` | `AuAppRule_Override` |  |  |  |
| 15 | `AU.APP.RECORD.STATUS` | `AuAppRule_RecordStatus` | String |  |  |
| 16 | `AU.APP.CURR.NO` | `AuAppRule_CurrNo` | String |  |  |
| 17 | `AU.APP.INPUTTER` | `AuAppRule_Inputter` |  |  |  |
| 18 | `AU.APP.DATE.TIME` | `AuAppRule_DateTime` |  |  |  |
| 19 | `AU.APP.AUTHORISER` | `AuAppRule_Authoriser` | String |  |  |
| 20 | `AU.APP.CO.CODE` | `AuAppRule_CoCode` | String |  |  |
| 21 | `AU.APP.DEPT.CODE` | `AuAppRule_DeptCode` | String |  |  |
| 22 | `AU.APP.AUDITOR.CODE` | `AuAppRule_AuditorCode` | String |  |  |
| 23 | `AU.APP.AUDIT.DATE.TIME` | `AuAppRule_AuditDateTime` | String |  |  |
