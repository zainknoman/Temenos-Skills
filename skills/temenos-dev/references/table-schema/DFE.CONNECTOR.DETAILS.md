# DFE.CONNECTOR.DETAILS — Table Schema

> Source: `INSERTS/I_F.DFE.CONNECTOR.DETAILS` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DFE.CONN.DESCRIPTION` | `DfeConnectorDetails_Description` |  |  |  |
| 2 | `DFE.CONN.CONNECTION.METHOD` | `DfeConnectorDetails_ConnectionMethod` | TField |  |  |
| 3 | `DFE.CONN.CUSTOM.ROUTINE` | `DfeConnectorDetails_CustomRoutine` | TField |  |  |
| 4 | `DFE.CONN.CONNECTION.HANDLER` | `DfeConnectorDetails_ConnectionHandler` | TField |  |  |
| 5 | `DFE.CONN.WEBSERVER` | `DfeConnectorDetails_Webserver` | TField |  |  |
| 6 | `DFE.CONN.USERNAME` | `DfeConnectorDetails_Username` | TField |  |  |
| 7 | `DFE.CONN.PASSWORD` | `DfeConnectorDetails_Password` | TField |  |  |
| 8 | `DFE.CONN.JEE.HOSTS` | `DfeConnectorDetails_JeeHosts` |  |  |  |
| 9 | `DFE.CONN.JEE.PORTS` | `DfeConnectorDetails_JeePorts` |  |  |  |
| 10 | `DFE.CONN.RESERVED.20` | `DfeConnectorDetails_Reserved20` |  |  |  |
| 11 | `DFE.CONN.RESERVED.19` | `DfeConnectorDetails_Reserved19` |  |  |  |
| 12 | `DFE.CONN.RESERVED.18` | `DfeConnectorDetails_Reserved18` |  |  |  |
| 13 | `DFE.CONN.RESERVED.17` | `DfeConnectorDetails_Reserved17` |  |  |  |
| 14 | `DFE.CONN.RESERVED.16` | `DfeConnectorDetails_Reserved16` |  |  |  |
| 15 | `DFE.CONN.HOSTNAME` | `DfeConnectorDetails_Hostname` | TField |  |  |
| 16 | `DFE.CONN.PORT.ID` | `DfeConnectorDetails_PortId` | TField |  |  |
| 17 | `DFE.CONN.MQ.MANAGER` | `DfeConnectorDetails_MqManager` | TField |  |  |
| 18 | `DFE.CONN.MQ.CHANNEL` | `DfeConnectorDetails_MqChannel` | TField |  |  |
| 19 | `DFE.CONN.HTTP.VERSION` | `DfeConnectorDetails_HttpVersion` | TField |  |  |
| 20 | `DFE.CONN.MSG.TIMEOUT` | `DfeConnectorDetails_MsgTimeout` | TField |  |  |
| 21 | `DFE.CONN.JMS.CONTEXTFACTORY` | `DfeConnectorDetails_JmsContextfactory` | TField |  |  |
| 22 | `DFE.CONN.PROCESS.VIA.EJB` | `DfeConnectorDetails_ProcessViaEjb` | TField |  |  |
| 23 | `DFE.CONN.JAVA.API.DETAILS` | `DfeConnectorDetails_JavaApiDetails` | TField |  |  |
| 24 | `DFE.CONN.RESERVED.12` | `DfeConnectorDetails_Reserved12` | TField |  |  |
| 25 | `DFE.CONN.RESERVED.11` | `DfeConnectorDetails_Reserved11` | TField |  |  |
| 26 | `DFE.CONN.RESERVED.10` | `DfeConnectorDetails_Reserved10` | TField |  |  |
| 27 | `DFE.CONN.RESERVED.9` | `DfeConnectorDetails_Reserved9` | TField |  |  |
| 28 | `DFE.CONN.RESERVED.8` | `DfeConnectorDetails_Reserved8` | TField |  |  |
| 29 | `DFE.CONN.RESERVED.7` | `DfeConnectorDetails_Reserved7` | TField |  |  |
| 30 | `DFE.CONN.RESERVED.6` | `DfeConnectorDetails_Reserved6` | TField |  |  |
| 31 | `DFE.CONN.RESERVED.5` | `DfeConnectorDetails_Reserved5` | TField |  |  |
| 32 | `DFE.CONN.RESERVED.4` | `DfeConnectorDetails_Reserved4` | TField |  |  |
| 33 | `DFE.CONN.RESERVED.3` | `DfeConnectorDetails_Reserved3` | TField |  |  |
| 34 | `DFE.CONN.RESERVED.2` | `DfeConnectorDetails_Reserved2` | TField |  |  |
| 35 | `DFE.CONN.RESERVED.1` | `DfeConnectorDetails_Reserved1` | TField |  |  |
| 36 | `DFE.CONN.RECORD.STATUS` | `DfeConnectorDetails_RecordStatus` | String |  |  |
| 37 | `DFE.CONN.CURR.NO` | `DfeConnectorDetails_CurrNo` | String |  |  |
| 38 | `DFE.CONN.INPUTTER` | `DfeConnectorDetails_Inputter` |  |  |  |
| 39 | `DFE.CONN.DATE.TIME` | `DfeConnectorDetails_DateTime` |  |  |  |
| 40 | `DFE.CONN.AUTHORISER` | `DfeConnectorDetails_Authoriser` | String |  |  |
| 41 | `DFE.CONN.CO.CODE` | `DfeConnectorDetails_CoCode` | String |  |  |
| 42 | `DFE.CONN.DEPT.CODE` | `DfeConnectorDetails_DeptCode` | String |  |  |
| 43 | `DFE.CONN.AUDITOR.CODE` | `DfeConnectorDetails_AuditorCode` | String |  |  |
| 44 | `DFE.CONN.AUDIT.DATE.TIME` | `DfeConnectorDetails_AuditDateTime` | String |  |  |
