# SAWATQ.SERVICE.LOG — Table Schema

> Source: `INSERTS/I_F.SAWATQ.SERVICE.LOG` in `SAWATQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.LOG.SERVICE.NAME` | `SawatqServiceLog_ServiceName` | TField |  | This indicates the Service Name |
| 2 | `SA.LOG.REQUEST.ATTRIBUTE` | `SawatqServiceLog_RequestAttribute` |  |  |  |
| 3 | `SA.LOG.REQUEST.VALUE` | `SawatqServiceLog_RequestValue` |  |  |  |
| 4 | `SA.LOG.REPLY.CODE` | `SawatqServiceLog_ReplyCode` | TField |  | This indicates the Response Code for the Incoming Request from T24 |
| 5 | `SA.LOG.REPLY.DESCRIPTION` | `SawatqServiceLog_ReplyDescription` | TField |  | This indicates the Description of the Response Code |
| 6 | `SA.LOG.ERROR.CODE` | `SawatqServiceLog_ErrorCode` | TField |  | If the Incoming Request is successfully validated against any of the Error Scenarios, then the Error Code is captured in this Field |
| 7 | `SA.LOG.ERROR.DESCRIPTION` | `SawatqServiceLog_ErrorDescription` | TField |  | This indicates the Description of the Error Code |
| 8 | `SA.LOG.RESPONSE.FIELD.NAME` | `SawatqServiceLog_ResponseFieldName` |  |  |  |
| 9 | `SA.LOG.RESPONSE.FIELD.VALUE` | `SawatqServiceLog_ResponseFieldValue` |  |  |  |
| 10 | `SA.LOG.STATUS` | `SawatqServiceLog_Status` | TField |  | This field indicates the status of the Web Service Request Cleared - Successfully processed Error - Error scenario faced On-hold - Request is On-Hold |
| 11 | `SA.LOG.LOCAL.REF` | `SawatqServiceLog_LocalRef` |  |  |  |
| 12 | `SA.LOG.OVERRIDE` | `SawatqServiceLog_Override` |  |  |  |
| 13 | `SA.LOG.RESERVED.1` | `SawatqServiceLog_Reserved1` | TField |  |  |
| 14 | `SA.LOG.RESERVED.2` | `SawatqServiceLog_Reserved2` | TField |  |  |
| 15 | `SA.LOG.RESERVED.3` | `SawatqServiceLog_Reserved3` | TField |  |  |
| 16 | `SA.LOG.RESERVED.4` | `SawatqServiceLog_Reserved4` | TField |  |  |
| 17 | `SA.LOG.RESERVED.5` | `SawatqServiceLog_Reserved5` | TField |  |  |
| 18 | `SA.LOG.RESERVED.6` | `SawatqServiceLog_Reserved6` | TField |  |  |
| 19 | `SA.LOG.RESERVED.7` | `SawatqServiceLog_Reserved7` | TField |  |  |
| 20 | `SA.LOG.RESERVED.8` | `SawatqServiceLog_Reserved8` | TField |  |  |
| 21 | `SA.LOG.RESERVED.9` | `SawatqServiceLog_Reserved9` | TField |  |  |
| 22 | `SA.LOG.RESERVED.10` | `SawatqServiceLog_Reserved10` | TField |  |  |
| 23 | `SA.LOG.RECORD.STATUS` | `SawatqServiceLog_RecordStatus` | String |  |  |
| 24 | `SA.LOG.CURR.NO` | `SawatqServiceLog_CurrNo` | String |  |  |
| 25 | `SA.LOG.INPUTTER` | `SawatqServiceLog_Inputter` |  |  |  |
| 26 | `SA.LOG.DATE.TIME` | `SawatqServiceLog_DateTime` |  |  |  |
| 27 | `SA.LOG.AUTHORISER` | `SawatqServiceLog_Authoriser` | String |  |  |
| 28 | `SA.LOG.CO.CODE` | `SawatqServiceLog_CoCode` | String |  |  |
| 29 | `SA.LOG.DEPT.CODE` | `SawatqServiceLog_DeptCode` | String |  |  |
| 30 | `SA.LOG.AUDITOR.CODE` | `SawatqServiceLog_AuditorCode` | String |  |  |
| 31 | `SA.LOG.AUDIT.DATE.TIME` | `SawatqServiceLog_AuditDateTime` | String |  |  |
