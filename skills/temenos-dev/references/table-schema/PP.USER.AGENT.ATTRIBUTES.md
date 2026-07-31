# PP.USER.AGENT.ATTRIBUTES — Table Schema

> Source: `INSERTS/I_F.PP.USER.AGENT.ATTRIBUTES` in `PP_InquiryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.UA.DESCRIPTION` | `PpUserAgentAttributes_Description` | TField |  | Description of the application Validation Rules:Nil 65 alphanumeric characters. |
| 2 | `PP.UA.FILTER.NAME` | `PpUserAgentAttributes_FilterName` |  |  |  |
| 3 | `PP.UA.FILTER.FIELD` | `PpUserAgentAttributes_FilterField` |  |  |  |
| 4 | `PP.UA.FILTER.VALUE` | `PpUserAgentAttributes_FilterValue` |  |  |  |
| 5 | `PP.UA.RESERVED9` | `PpUserAgentAttributes_Reserved9` |  |  |  |
| 6 | `PP.UA.TAB.NAME` | `PpUserAgentAttributes_TabName` |  |  |  |
| 7 | `PP.UA.TAB.LINE` | `PpUserAgentAttributes_TabLine` |  |  |  |
| 8 | `PP.UA.TAB.FILTER.FIELD` | `PpUserAgentAttributes_TabFilterField` |  |  |  |
| 9 | `PP.UA.TAB.FILTER.OPERAND` | `PpUserAgentAttributes_TabFilterOperand` |  |  |  |
| 10 | `PP.UA.TAB.FILTER.VALUE` | `PpUserAgentAttributes_TabFilterValue` |  |  |  |
| 11 | `PP.UA.TAB.IGNORE.FIELD` | `PpUserAgentAttributes_TabIgnoreField` |  |  |  |
| 12 | `PP.UA.RESERVED8` | `PpUserAgentAttributes_Reserved8` | TField |  |  |
| 13 | `PP.UA.RESERVED7` | `PpUserAgentAttributes_Reserved7` | TField |  |  |
| 14 | `PP.UA.RESERVED6` | `PpUserAgentAttributes_Reserved6` | TField |  |  |
| 15 | `PP.UA.RESERVED5` | `PpUserAgentAttributes_Reserved5` | TField |  |  |
| 16 | `PP.UA.RESERVED4` | `PpUserAgentAttributes_Reserved4` | TField |  |  |
| 17 | `PP.UA.RESERVED3` | `PpUserAgentAttributes_Reserved3` | TField |  |  |
| 18 | `PP.UA.RESERVED2` | `PpUserAgentAttributes_Reserved2` | TField |  |  |
| 19 | `PP.UA.RESERVED1` | `PpUserAgentAttributes_Reserved1` | TField |  |  |
| 20 | `PP.UA.OVERRIDE` | `PpUserAgentAttributes_Override` |  |  |  |
| 21 | `PP.UA.RECORD.STATUS` | `PpUserAgentAttributes_RecordStatus` | String |  |  |
| 22 | `PP.UA.CURR.NO` | `PpUserAgentAttributes_CurrNo` | String |  |  |
| 23 | `PP.UA.INPUTTER` | `PpUserAgentAttributes_Inputter` |  |  |  |
| 24 | `PP.UA.DATE.TIME` | `PpUserAgentAttributes_DateTime` |  |  |  |
| 25 | `PP.UA.AUTHORISER` | `PpUserAgentAttributes_Authoriser` | String |  |  |
| 26 | `PP.UA.CO.CODE` | `PpUserAgentAttributes_CoCode` | String |  |  |
| 27 | `PP.UA.DEPT.CODE` | `PpUserAgentAttributes_DeptCode` | String |  |  |
| 28 | `PP.UA.AUDITOR.CODE` | `PpUserAgentAttributes_AuditorCode` | String |  |  |
| 29 | `PP.UA.AUDIT.DATE.TIME` | `PpUserAgentAttributes_AuditDateTime` | String |  |  |
| 30 | `PP.UA.COMPANY.ID` | `PpUserAgentAttributes_CompanyId` |  |  |  |
| 31 | `PP.UA.CRITICAL.DEADLINE.THRESHOLD` | `PpUserAgentAttributes_CriticalDeadlineThreshold` |  |  |  |
| 32 | `PP.UA.NEAR.CUT.OFF.THRESHOLD` | `PpUserAgentAttributes_NearCutOffThreshold` |  |  |  |
| 33 | `PP.UA.SHOW.FAR.CUT.OFF` | `PpUserAgentAttributes_ShowFarCutOff` |  |  |  |
| 34 | `PP.UA.TIME.DURATION` | `PpUserAgentAttributes_TimeDuration` | TField |  | Specifies the time duration of the records fetched in the case management dashboard. It is represented in calendar days. The default value is 90 days and signifies the last 90 days data to be fetched. |
