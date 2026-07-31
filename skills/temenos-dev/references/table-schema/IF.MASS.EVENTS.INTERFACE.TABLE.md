# IF.MASS.EVENTS.INTERFACE.TABLE — Table Schema

> Source: `INSERTS/I_F.IF.MASS.EVENTS.INTERFACE.TABLE` in `IF_IntegrationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.MASS.EV.EVENT.DATA` | `IfMassEventsInterfaceTable_EventData` | TField |  | Overview This field holds the Integration Framework generated event data in XML format. Validation Rules Input not allowed. |
| 2 | `IF.MASS.EV.EVENT.TYPE` | `IfMassEventsInterfaceTable_EventType` | TField |  | Overview This field holds the type of the event represented by this record. Validation Rules Input not allowed. |
| 3 | `IF.MASS.EV.EVENT.TIMESTAMP` | `IfMassEventsInterfaceTable_EventTimestamp` | TField |  | Overview This field holds the timestamp at which the event was delivered through any of the available delivery mechanisms. An event record with this field having a non empty value indicates that the event is already delivered and the record is ready for archival. Validation Rules Input not allowed. |
| 4 | `IF.MASS.EV.OLD.EVENT.XML` | `IfMassEventsInterfaceTable_OldEventXml` | TField |  | Overview This field holds the Integration Framework generated previous image event data in XML format. This XML would be generated if and only the option "Include Previous Image" is selected during flow creation. Validation Rules Input not allowed. |
| 5 | `IF.MASS.EV.LOCAL.TRANSFORM` | `IfMassEventsInterfaceTable_LocalTransform` | TField |  | Overview This field records whether the outbound message was transformed using XSL and if so was the transformation successful. Validation Rules This field can have the below values: NO_XSLT_TRANSFORMATION - Indicates that there is no custom stylesheet applied and the IF generic transformation is used. XSLT_TRANSFORMATION_SUCCESS - Indicates that there is custom stylesheet applied and the transformation is success. XSLT_TRANSFORMATION_FAILURE - Indicates that there is custom stylesheet applied and the transformation failed. Input not allowed. |
| 6 | `IF.MASS.EV.DELIVERY.STATUS` | `IfMassEventsInterfaceTable_DeliveryStatus` | TField |  | Overview This indicates the status of the event after the execution of Integration Service. Validation Rules This field can have the below values: DELIVERY_SUCCESS - Event Delivered to queue successfully. TRANSFORM_ERROR_CUSTOM - Custom Style Sheet got applied and the transformation failed TRANSFORM_ERROR - IF default transform failed EVENT_FILTERED - The IF event is filtered and will not be delivered to queue TRANSMIT_ERROR - Issue in delivering the event XML to the JMS Queue Input not allowed. |
| 7 | `IF.MASS.EV.STATUS.REASON` | `IfMassEventsInterfaceTable_StatusReason` | TField |  | Overview This field provides more information about the DELVIERY.STATUS of and event Validation Rules Input not allowed. |
| 8 | `IF.MASS.EV.EVENT.XML.NAME` | `IfMassEventsInterfaceTable_EventXmlName` |  |  |  |
| 9 | `IF.MASS.EV.OLD.FIELD.VALUE` | `IfMassEventsInterfaceTable_OldFieldValue` |  |  |  |
| 10 | `IF.MASS.EV.FIELD.VALUE` | `IfMassEventsInterfaceTable_FieldValue` |  |  |  |
| 11 | `IF.MASS.EV.CREATION.TIME` | `IfMassEventsInterfaceTable_CreationTime` | TField |  | Overview This field holds the timestamp at which the event was created by Integration Framework. Validation Rules Input not allowed. |
| 12 | `IF.MASS.EV.CREATION.DATE` | `IfMassEventsInterfaceTable_CreationDate` | TField |  | Overview This field hold the event creation date in T24 date format. Validation Rules Input not allowed. |
| 13 | `IF.MASS.EV.EVENT.PRIORITY` | `IfMassEventsInterfaceTable_EventPriority` | TField |  | Overview The field holds the event priority of the event record. This value is taken from the EVENT.PRIORITY field ofIF.INTEGRATION.FLOW.CATALOG. Validation Rules Input not allowed. |
| 14 | `IF.MASS.EV.RESERVED22` | `IfMassEventsInterfaceTable_Reserved22` | TField |  |  |
| 15 | `IF.MASS.EV.COMMON.XML.NAME` | `IfMassEventsInterfaceTable_CommonXmlName` |  |  |  |
| 16 | `IF.MASS.EV.COMMON.XML.VAL` | `IfMassEventsInterfaceTable_CommonXmlVal` |  |  |  |
| 17 | `IF.MASS.EV.SOURCE` | `IfMassEventsInterfaceTable_Source` | TField |  |  |
| 18 | `IF.MASS.EV.CORRELATION.ID` | `IfMassEventsInterfaceTable_CorrelationId` | TField |  |  |
| 19 | `IF.MASS.EV.RESERVED.27` | `IfMassEventsInterfaceTable_Reserved27` | TField |  |  |
| 20 | `IF.MASS.EV.RESERVED.28` | `IfMassEventsInterfaceTable_Reserved28` | TField |  |  |
| 21 | `IF.MASS.EV.RESERVED.29` | `IfMassEventsInterfaceTable_Reserved29` | TField |  |  |
| 22 | `IF.MASS.EV.RESERVED.30` | `IfMassEventsInterfaceTable_Reserved30` | TField |  |  |
| 23 | `IF.MASS.EV.RESERVED.31` | `IfMassEventsInterfaceTable_Reserved31` | TField |  |  |
| 24 | `IF.MASS.EV.RESERVED.32` | `IfMassEventsInterfaceTable_Reserved32` | TField |  |  |
| 25 | `IF.MASS.EV.RESERVED.33` | `IfMassEventsInterfaceTable_Reserved33` | TField |  |  |
| 26 | `IF.MASS.EV.RESERVED.34` | `IfMassEventsInterfaceTable_Reserved34` | TField |  |  |
| 27 | `IF.MASS.EV.RESERVED.35` | `IfMassEventsInterfaceTable_Reserved35` | TField |  |  |
| 28 | `IF.MASS.EV.RESERVED.36` | `IfMassEventsInterfaceTable_Reserved36` | TField |  |  |
| 29 | `IF.MASS.EV.RESERVED.37` | `IfMassEventsInterfaceTable_Reserved37` | TField |  |  |
| 30 | `IF.MASS.EV.RESERVED.38` | `IfMassEventsInterfaceTable_Reserved38` | TField |  |  |
| 31 | `IF.MASS.EV.RESERVED.39` | `IfMassEventsInterfaceTable_Reserved39` | TField |  |  |
| 32 | `IF.MASS.EV.OVERRIDE` | `IfMassEventsInterfaceTable_Override` |  |  |  |
| 33 | `IF.MASS.EV.RECORD.STATUS` | `IfMassEventsInterfaceTable_RecordStatus` | String |  |  |
| 34 | `IF.MASS.EV.CURR.NO` | `IfMassEventsInterfaceTable_CurrNo` | String |  |  |
| 35 | `IF.MASS.EV.INPUTTER` | `IfMassEventsInterfaceTable_Inputter` |  |  |  |
| 36 | `IF.MASS.EV.DATE.TIME` | `IfMassEventsInterfaceTable_DateTime` |  |  |  |
| 37 | `IF.MASS.EV.AUTHORISER` | `IfMassEventsInterfaceTable_Authoriser` | String |  |  |
| 38 | `IF.MASS.EV.CO.CODE` | `IfMassEventsInterfaceTable_CoCode` | String |  |  |
| 39 | `IF.MASS.EV.DEPT.CODE` | `IfMassEventsInterfaceTable_DeptCode` | String |  |  |
| 40 | `IF.MASS.EV.AUDITOR.CODE` | `IfMassEventsInterfaceTable_AuditorCode` | String |  |  |
| 41 | `IF.MASS.EV.AUDIT.DATE.TIME` | `IfMassEventsInterfaceTable_AuditDateTime` | String |  |  |
