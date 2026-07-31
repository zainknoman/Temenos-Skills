# IF.FLOW.OVERRIDE — Table Schema

> Source: `INSERTS/I_F.IF.FLOW.OVERRIDE` in `IF_FlowCatalog.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.FO.DESCRIPTION` | `IfFlowOverride_Description` |  |  |  |
| 2 | `IF.FO.MERGE.TO.FLOW` | `IfFlowOverride_MergeToFlow` | TField |  | Overview This field in this table says the value of the next set of fields need to be merged to IF.INTEGRATION.FLOW.CATALOG or not. Validation Rules Yes or No or None Yes or None merges the flow attributes to the flow when the record is authorised. If set to No, then the record is authorised but the Flow is not updated with the flow attributes defined |
| 3 | `IF.FO.EVENT.PRIORITY` | `IfFlowOverride_EventPriority` | TField |  |  |
| 4 | `IF.FO.DELIVERY.MODE` | `IfFlowOverride_DeliveryMode` | TField |  | Overview This is a single value field that specifies the mode of delivery to be applied. Validation Rules Following are allowed values with its description: None - In this case the default delivery mode set via event designer is retained for the flow record in IF.INTEGRATION.FLOW.CATALOG table with no changes. CLASSIC - When this option is selected, the mode of delivery is switched to integration service or adapter based on the IF.INTEGRATION.SERVICE.PARAM configuration or adapter. This removes the raw-xml attribute if chosen. CLASSIC.RAW.XML - When this option is selected, the flow attribute RAW-XML is added in the IF.INTEGRATION.FLOW.CATALOG record. Also the mode of delivery is switched to integration service or adapter based on the IF.INTEGRATION.SERVICE.PARAM configuration or adapter WRITE.TO.QUEUE - When this option is selected, the RAW-XML attribute is added as well the delivery mode is to post the message to the queue mentioned in the QUEUE.NAME field. |
| 5 | `IF.FO.QUEUE.NAME` | `IfFlowOverride_QueueName` | TField |  | Overview This field allows events to be delivered to a specific queue.This field holds the destination to deliver the events. Validation Rules If the delivery mode is WRITE.TO.QUEUE, then the queue name must be provided. This represents the queue to which the Raw IF Event would be posted when using direct posting. |
| 6 | `IF.FO.WRITE.TO.ARCHIVE` | `IfFlowOverride_WriteToArchive` | TField |  | Overview When this option is selected, then the flow attribute RAW-XML and WRITE.TO.ARC are added in the IF.INTEGRATION.FLOW.CATALOG record and this option can be enabled to Y only when the DELIVERY.MODE is set to WRITE.TO.QUEUE. This option writes to $ARC file if the direct posting had posted the message to queue successfully Validation Rules Yes or No |
| 7 | `IF.FO.COMPANIES` | `IfFlowOverride_Companies` |  |  |  |
| 8 | `IF.FO.DISABLE.FLOW` | `IfFlowOverride_disableflow` |  |  |  |
| 9 | `IF.FO.CORRELATION.ID.FIELD` | `IfFlowOverride_CorrelationIdField` | TField |  |  |
| 10 | `IF.FO.RESERVED.3` | `IfFlowOverride_Reserved3` | TField |  |  |
| 11 | `IF.FO.RESERVED.4` | `IfFlowOverride_Reserved4` | TField |  |  |
| 12 | `IF.FO.RESERVED.5` | `IfFlowOverride_Reserved5` | TField |  |  |
| 13 | `IF.FO.RESERVED.6` | `IfFlowOverride_Reserved6` | TField |  |  |
| 14 | `IF.FO.RESERVED.7` | `IfFlowOverride_Reserved7` | TField |  |  |
| 15 | `IF.FO.RESERVED.8` | `IfFlowOverride_Reserved8` | TField |  |  |
| 16 | `IF.FO.RESERVED.9` | `IfFlowOverride_Reserved9` | TField |  |  |
| 17 | `IF.FO.RESERVED.10` | `IfFlowOverride_Reserved10` | TField |  |  |
| 18 | `IF.FO.RESERVED.11` | `IfFlowOverride_Reserved11` | TField |  |  |
| 19 | `IF.FO.RESERVED.12` | `IfFlowOverride_Reserved12` | TField |  |  |
| 20 | `IF.FO.RESERVED.13` | `IfFlowOverride_Reserved13` | TField |  |  |
| 21 | `IF.FO.RESERVED.14` | `IfFlowOverride_Reserved14` | TField |  |  |
| 22 | `IF.FO.RESERVED.15` | `IfFlowOverride_Reserved15` | TField |  |  |
| 23 | `IF.FO.OVERRIDE` | `IfFlowOverride_Override` |  |  |  |
| 24 | `IF.FO.RECORD.STATUS` | `IfFlowOverride_RecordStatus` | String |  |  |
| 25 | `IF.FO.CURR.NO` | `IfFlowOverride_CurrNo` | String |  |  |
| 26 | `IF.FO.INPUTTER` | `IfFlowOverride_Inputter` |  |  |  |
| 27 | `IF.FO.DATE.TIME` | `IfFlowOverride_DateTime` |  |  |  |
| 28 | `IF.FO.AUTHORISER` | `IfFlowOverride_Authoriser` | String |  |  |
| 29 | `IF.FO.CO.CODE` | `IfFlowOverride_CoCode` | String |  |  |
| 30 | `IF.FO.DEPT.CODE` | `IfFlowOverride_DeptCode` | String |  |  |
| 31 | `IF.FO.AUDITOR.CODE` | `IfFlowOverride_AuditorCode` | String |  |  |
| 32 | `IF.FO.AUDIT.DATE.TIME` | `IfFlowOverride_AuditDateTime` | String |  |  |
