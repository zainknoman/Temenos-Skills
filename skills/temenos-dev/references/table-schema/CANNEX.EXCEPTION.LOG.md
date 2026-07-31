# CANNEX.EXCEPTION.LOG — Table Schema

> Source: `INSERTS/I_F.CANNEX.EXCEPTION.LOG` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.EXCEP.LOG.ERROR.MESSAGE` | `CannexExceptionLog_ErrorMessage` |  |  |  |
| 2 | `CANNEX.EXCEP.LOG.DATE` | `CannexExceptionLog_Date` | TField |  | Date when the error occurs |
| 3 | `CANNEX.EXCEP.LOG.CANNEX.ORDER.ID` | `CannexExceptionLog_CannexOrderId` | TField |  | Store the CFN.ORDER.NO from the incoming PO file |
| 4 | `CANNEX.EXCEP.LOG.COMPANY.PROCESSED` | `CannexExceptionLog_CompanyProcessed` | TField |  | Company where the GIC gets processed |
| 5 | `CANNEX.EXCEP.LOG.AGENT.ID` | `CannexExceptionLog_AgentId` | TField |  | Agent for the GIC processed |
| 6 | `CANNEX.EXCEP.LOG.AGENT.ARR.ID` | `CannexExceptionLog_AgentArrId` | TField |  | Agent Arrangement for the GIC Processed |
| 7 | `CANNEX.EXCEP.LOG.CUSTOMER.NO` | `CannexExceptionLog_CustomerNo` | TField |  | Customer Number for the GIC Processed |
| 8 | `CANNEX.EXCEP.LOG.RESERVED.1` | `CannexExceptionLog_Reserved1` | TField |  |  |
| 9 | `CANNEX.EXCEP.LOG.RESERVED.2` | `CannexExceptionLog_Reserved2` | TField |  |  |
| 10 | `CANNEX.EXCEP.LOG.RESERVED.3` | `CannexExceptionLog_Reserved3` | TField |  |  |
| 11 | `CANNEX.EXCEP.LOG.RESERVED.4` | `CannexExceptionLog_Reserved4` | TField |  |  |
| 12 | `CANNEX.EXCEP.LOG.RESERVED.5` | `CannexExceptionLog_Reserved5` | TField |  |  |
| 13 | `CANNEX.EXCEP.LOG.RESERVED.6` | `CannexExceptionLog_Reserved6` | TField |  |  |
| 14 | `CANNEX.EXCEP.LOG.RESERVED.7` | `CannexExceptionLog_Reserved7` | TField |  |  |
| 15 | `CANNEX.EXCEP.LOG.RESERVED.8` | `CannexExceptionLog_Reserved8` | TField |  |  |
| 16 | `CANNEX.EXCEP.LOG.RESERVED.9` | `CannexExceptionLog_Reserved9` | TField |  |  |
| 17 | `CANNEX.EXCEP.LOG.RESERVED.10` | `CannexExceptionLog_Reserved10` | TField |  |  |
| 18 | `CANNEX.EXCEP.LOG.LOCAL.REF` | `CannexExceptionLog_LocalRef` |  |  |  |
| 19 | `CANNEX.EXCEP.LOG.OVERRIDE` | `CannexExceptionLog_Override` |  |  |  |
| 20 | `CANNEX.EXCEP.LOG.RECORD.STATUS` | `CannexExceptionLog_RecordStatus` | String |  |  |
| 21 | `CANNEX.EXCEP.LOG.CURR.NO` | `CannexExceptionLog_CurrNo` | String |  |  |
| 22 | `CANNEX.EXCEP.LOG.INPUTTER` | `CannexExceptionLog_Inputter` |  |  |  |
| 23 | `CANNEX.EXCEP.LOG.DATE.TIME` | `CannexExceptionLog_DateTime` |  |  |  |
| 24 | `CANNEX.EXCEP.LOG.AUTHORISER` | `CannexExceptionLog_Authoriser` | String |  |  |
| 25 | `CANNEX.EXCEP.LOG.CO.CODE` | `CannexExceptionLog_CoCode` | String |  |  |
| 26 | `CANNEX.EXCEP.LOG.DEPT.CODE` | `CannexExceptionLog_DeptCode` | String |  |  |
| 27 | `CANNEX.EXCEP.LOG.AUDITOR.CODE` | `CannexExceptionLog_AuditorCode` | String |  |  |
| 28 | `CANNEX.EXCEP.LOG.AUDIT.DATE.TIME` | `CannexExceptionLog_AuditDateTime` | String |  |  |
