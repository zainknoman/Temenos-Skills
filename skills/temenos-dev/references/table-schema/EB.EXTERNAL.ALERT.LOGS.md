# EB.EXTERNAL.ALERT.LOGS — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.ALERT.LOGS` in `BE_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.LOG.EVENT.NAME` | `EbExternalAlertLogs_EventName` | TField |  | This field is used to capture the event name from TEC.ITEMS as part of external alert request. |
| 2 | `EXT.LOG.TEC.ITEM.NAME` | `EbExternalAlertLogs_TecItemName` | TField |  | This field is used to capture TEC.ITEMS name as part of transact request to trigger an alert. |
| 3 | `EXT.LOG.SUBSCRIPTION.ID` | `EbExternalAlertLogs_SubscriptionId` | TField |  | To capture subscription id as part of triggered events from the transact. |
| 4 | `EXT.LOG.OFS.SOURCE` | `EbExternalAlertLogs_OfsSource` | TField |  | OFS.SOURCE is used as part of the request. |
| 5 | `EXT.LOG.PAYLOAD.HEADER` | `EbExternalAlertLogs_PayloadHeader` | TField |  | This field is to capture the Payload header mapping details from EB.EXTERNAL.REST.API.HEADER application. |
| 6 | `EXT.LOG.PAYLOAD.BODY` | `EbExternalAlertLogs_PayloadBody` | TField |  | This field is to capture the Payload data from EB.EXTERNAL.ALERT.MAPPING application. |
| 7 | `EXT.LOG.PAYLOAD.REQUEST` | `EbExternalAlertLogs_PayloadRequest` | TField |  | The field is to capture the entire payload data as apart of the request send to the external system. |
| 8 | `EXT.LOG.PAYLOAD.RESPONSE` | `EbExternalAlertLogs_PayloadResponse` | TField |  | This field is used to capture the response of external alerts whether it success or failure. |
| 9 | `EXT.LOG.CALLJ.ERROR` | `EbExternalAlertLogs_CalljError` | TField |  | This field is used to capture the errors from TAFJ only when the payload data is failed to transmit. |
| 10 | `EXT.LOG.STATUS` | `EbExternalAlertLogs_Status` | TField |  | This field is to capture the status of external alert request. SUCCESS: Alerts sent successfully to an external System. FAILURE: Failed to send an alert in external system. |
| 11 | `EXT.LOG.REASON` | `EbExternalAlertLogs_Reason` | TField |  | User define field needs to be enter the reason of failure when we are resubmitting the request. Validation Rules: NOINPUT field for Success Alert and INPUT field for FAILURE alert. |
| 12 | `EXT.LOG.RESUBMIT` | `EbExternalAlertLogs_Resubmit` | TField |  | This field is used for resubmit an alerts again after correcting the necessary details Validation Rules: NOINPUT field for Success Alert and INPUT field for FAILURE alert. |
| 13 | `EXT.LOG.RESERVEDFLD.6` | `EbExternalAlertLogs_Reservedfld6` |  |  |  |
| 14 | `EXT.LOG.RESERVEDFLD.5` | `EbExternalAlertLogs_Reservedfld5` |  |  |  |
| 15 | `EXT.LOG.RESERVEDFLD.4` | `EbExternalAlertLogs_Reservedfld4` |  |  |  |
| 16 | `EXT.LOG.RESERVEDFLD.3` | `EbExternalAlertLogs_Reservedfld3` |  |  |  |
| 17 | `EXT.LOG.RESERVEDFLD.2` | `EbExternalAlertLogs_Reservedfld2` |  |  |  |
| 18 | `EXT.LOG.RESERVEDFLD.1` | `EbExternalAlertLogs_Reservedfld1` |  |  |  |
| 19 | `EXT.LOG.RESERVED.10` | `EbExternalAlertLogs_Reserved10` | TField |  |  |
| 20 | `EXT.LOG.RESERVED.9` | `EbExternalAlertLogs_Reserved9` | TField |  |  |
| 21 | `EXT.LOG.RESERVED.8` | `EbExternalAlertLogs_Reserved8` | TField |  |  |
| 22 | `EXT.LOG.RESERVED.7` | `EbExternalAlertLogs_Reserved7` | TField |  |  |
| 23 | `EXT.LOG.RESERVED.6` | `EbExternalAlertLogs_Reserved6` | TField |  |  |
| 24 | `EXT.LOG.RESERVED.5` | `EbExternalAlertLogs_Reserved5` | TField |  |  |
| 25 | `EXT.LOG.RESERVED.4` | `EbExternalAlertLogs_Reserved4` | TField |  |  |
| 26 | `EXT.LOG.RESERVED.3` | `EbExternalAlertLogs_Reserved3` | TField |  |  |
| 27 | `EXT.LOG.RESERVED.2` | `EbExternalAlertLogs_Reserved2` | TField |  |  |
| 28 | `EXT.LOG.RESERVED.1` | `EbExternalAlertLogs_Reserved1` | TField |  |  |
| 29 | `EXT.LOG.LOCAL.REF` | `EbExternalAlertLogs_LocalRef` |  |  |  |
| 30 | `EXT.LOG.OVERRIDE` | `EbExternalAlertLogs_Override` |  |  |  |
| 31 | `EXT.LOG.RECORD.STATUS` | `EbExternalAlertLogs_RecordStatus` | String |  |  |
| 32 | `EXT.LOG.CURR.NO` | `EbExternalAlertLogs_CurrNo` | String |  |  |
| 33 | `EXT.LOG.INPUTTER` | `EbExternalAlertLogs_Inputter` |  |  |  |
| 34 | `EXT.LOG.DATE.TIME` | `EbExternalAlertLogs_DateTime` |  |  |  |
| 35 | `EXT.LOG.AUTHORISER` | `EbExternalAlertLogs_Authoriser` | String |  |  |
| 36 | `EXT.LOG.CO.CODE` | `EbExternalAlertLogs_CoCode` | String |  |  |
| 37 | `EXT.LOG.DEPT.CODE` | `EbExternalAlertLogs_DeptCode` | String |  |  |
| 38 | `EXT.LOG.AUDITOR.CODE` | `EbExternalAlertLogs_AuditorCode` | String |  |  |
| 39 | `EXT.LOG.AUDIT.DATE.TIME` | `EbExternalAlertLogs_AuditDateTime` | String |  |  |
