# SWIFT.ALLIANCE.PARAM — Table Schema

> Source: `INSERTS/I_F.SWIFT.ALLIANCE.PARAM` in `SWFTAL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SWIFT.AL.PARA.MSG.TYPE` | `SwiftAllianceParam_MsgType` | TField |  | It defines message prefix or suffix as 'MSG' by default. Default value can be altered by defining new message type in Data Value field of EB.LOOKUP>SWFTAL.MSG.TYPE*FIN |
| 2 | `SWIFT.AL.PARA.IN.MSG.FORMAT` | `SwiftAllianceParam_InMsgFormat` | TField |  | It defines incoming format for the Alliance message. Possible values are DOS-PCC/RJE. |
| 3 | `SWIFT.AL.PARA.OUT.MSG.FORMAT` | `SwiftAllianceParam_OutMsgFormat` | TField |  | It defines the Outgoing format for the Alliance message � Possible values are DOS-PCC/RJE. |
| 4 | `SWIFT.AL.PARA.MQ.ENABLE` | `SwiftAllianceParam_MqEnable` | TField | Yes | It defines to enable whether MQ is used for the Alliance�s outgoing processing or not.If MQ_ENABLE is set as OUTWARD then the fields MQ.CONN.FACTORY andMQ.OUT.QUEUE.NAME are mandatory for the TAFJ runtime and field HANDLER is mandatory for the TAFC runtime. |
| 5 | `SWIFT.AL.PARA.MQ.CONN.FACTORY` | `SwiftAllianceParam_MqConnFactory` |  |  |  |
| 6 | `SWIFT.AL.PARA.MQ.OUT.QUEUE.NAME` | `SwiftAllianceParam_MqOutQueueName` |  |  |  |
| 7 | `SWIFT.AL.PARA.GUARD.QUEUE.NAME` | `SwiftAllianceParam_GuardQueueName` |  |  |  |
| 8 | `SWIFT.AL.PARA.TIME.TO.LIVE` | `SwiftAllianceParam_TimeToLive` |  |  |  |
| 9 | `SWIFT.AL.PARA.ALLIANCE.FILEPATH` | `SwiftAllianceParam_AllianceFilepath` | TField |  |  |
| 10 | `SWIFT.AL.PARA.HANDLER` | `SwiftAllianceParam_Handler` | TField | Yes | It holds the activation string which has to be passed as a parameter to the CALLJEE and used in TAFC runtime. Validation Rule: Input mandatory when MQ.ENABLE is OUTWARD and running in TAFC runtime. |
| 11 | `SWIFT.AL.PARA.TPH.DELIVERY.MODE` | `SwiftAllianceParam_TphDeliveryMode` | TField |  |  |
| 12 | `SWIFT.AL.PARA.RESERVED.4` | `SwiftAllianceParam_Reserved4` | TField |  |  |
| 13 | `SWIFT.AL.PARA.RESERVED.3` | `SwiftAllianceParam_Reserved3` | TField |  |  |
| 14 | `SWIFT.AL.PARA.RESERVED.2` | `SwiftAllianceParam_Reserved2` | TField |  |  |
| 15 | `SWIFT.AL.PARA.RESERVED.1` | `SwiftAllianceParam_Reserved1` | TField |  |  |
| 16 | `SWIFT.AL.PARA.LOCAL.REF` | `SwiftAllianceParam_LocalRef` |  |  |  |
| 17 | `SWIFT.AL.PARA.RECORD.STATUS` | `SwiftAllianceParam_RecordStatus` | String |  |  |
| 18 | `SWIFT.AL.PARA.CURR.NO` | `SwiftAllianceParam_CurrNo` | String |  |  |
| 19 | `SWIFT.AL.PARA.INPUTTER` | `SwiftAllianceParam_Inputter` |  |  |  |
| 20 | `SWIFT.AL.PARA.DATE.TIME` | `SwiftAllianceParam_DateTime` |  |  |  |
| 21 | `SWIFT.AL.PARA.AUTHORISER` | `SwiftAllianceParam_Authoriser` | String |  |  |
| 22 | `SWIFT.AL.PARA.CO.CODE` | `SwiftAllianceParam_CoCode` | String |  |  |
| 23 | `SWIFT.AL.PARA.DEPT.CODE` | `SwiftAllianceParam_DeptCode` | String |  |  |
| 24 | `SWIFT.AL.PARA.AUDITOR.CODE` | `SwiftAllianceParam_AuditorCode` | String |  |  |
| 25 | `SWIFT.AL.PARA.AUDIT.DATE.TIME` | `SwiftAllianceParam_AuditDateTime` | String |  |  |
| 26 | `SWIFT.AL.PARA.COMPANY` | `SwiftAllianceParam_Company` |  |  |  |
