# TEC.ITEMS — Table Schema

> Source: `INSERTS/I_F.TEC.ITEMS` in `EB_Logging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TEC.IT.DESCRIPTION` | `TecItems_Description` |  |  |  |
| 2 | `TEC.IT.AREA` | `TecItems_Area` | TField | Yes | Used to differentiate the TEC Metric items in TECMonitor. 1.1-10 (Alphanumeric) characters. 2.Non Mandatory field. 3.Allowed values - PERFORMANCE,USAGE and INFO |
| 3 | `TEC.IT.METRIC.TYPE` | `TecItems_MetricType` | A (alpha) | Yes | This field is used to identify the Metric type of the TEC.ITEMS. We have to specify the metric type based on the usability of the TEC ITEMS record. 1.1-35 type A (alpha) characters. 2.Non Mandatory field. 3.Allowed values - SIZE, TIME and COUNT 4.If TIME is specified here then the value entered in THRESHOLD would be treated in mille seconds 5.If SIZE is specified here then the value entered in THRESHOLD would be treated in bytes Examples: READ.SIZE - Size of the record when a READ happening on the record- This TEC ITEM is based on SIZE READ.RESPOSE - Time taken to READ a particular record. This one is based on TIME LOCK.COLLISION - Number of LOCK collision. This one is based on the COUNT |
| 4 | `TEC.IT.THRESHOLD.TYPE` | `TecItems_ThresholdType` |  |  |  |
| 5 | `TEC.IT.THRESHOLD` | `TecItems_Threshold` |  |  |  |
| 6 | `TEC.IT.SUBSCRIBER` | `TecItems_Subscriber` |  |  |  |
| 7 | `TEC.IT.HISTORIC` | `TecItems_Historic` | TField | Yes | When this field holds the value of Y then logged TEC metrics will also be written to TEC.OUTPUT.HISTORY file. 1.1-35 (Alphanumeric) characters. 2.Non Mandatory field. 3.Allowed values - Y or NULL |
| 8 | `TEC.IT.LOG` | `TecItems_Log` | TField | Yes | Field relevant to the EVENT.LIST table and it is no where related to TEC metrics or t24monitor. 1.1-35 (Alphanumeric) characters. 2.Non Mandatory field. |
| 9 | `TEC.IT.METRIC.UNITS` | `TecItems_MetricUnits` | TField | Yes | Field used to identifies the unit measurement of a TEC.ITEMS records. We have to specify the metric unit based on the METRIC.TYPE and the usability of TEC ITEMS record. 1.1-10 (Alphanumeric) characters. 2.Non Mandatory field. |
| 10 | `TEC.IT.METRIC.KEY` | `TecItems_MetricKey` |  |  |  |
| 11 | `TEC.IT.METRIC.CAPTION` | `TecItems_MetricCaption` |  |  |  |
| 12 | `TEC.IT.COL.TYPES` | `TecItems_ColTypes` | TField | Yes | Specify the Metric type of the TEC.ITEMS record to T24Monitor/TECMonitor. If nothing specified then the value would be taken from the field METRIC.TYPE. 1.1-10 (Alphanumeric) characters. 2.Non Mandatory field. |
| 13 | `TEC.IT.ITEM.CLASSIFICATION` | `TecItems_ItemClassification` | TField |  | Field to distinguish between technical and business related activities 1.Possible Values - TECHNICAL, BUSINESS, SERVICE 2. Default Value - TECHNICAL 3. NOCHANGE field |
| 14 | `TEC.IT.EVENT.TYPE` | `TecItems_EventType` | TField | Yes | To specify the type of EVENT 1. This field has a check file validation to EB.EVENT.TYPE application 2. Mandatory if Item classification is BUSINESS and when EVENT.API not defined for the event. 3. NOCHANGE field 4. Event type should be end with - SERVICE for the classification SERVICE |
| 15 | `TEC.IT.SUBSCRIPTION.TYPE` | `TecItems_SubscriptionType` | TField | Yes | To specify whether subscription is done at product/customer level 1. Possible Values - CUSTOMER, PRODUCT 2. Mandatory if Item classification is BUSINESS and when EVENT.API is not defined. 3. Mandatory value Product if Item classification is Service |
| 16 | `TEC.IT.SUBSCRIPTION.LEVEL` | `TecItems_SubscriptionLevel` | TField | Yes | This field is to allow extra filtering and validation at the subscription level to indicate if this event can be subscribed by a customer or DAO or both. If defined as GLOBAL, then the customer cannot subscribe or un-subscribe to this event. 1. Possible Values - INTERNAL, EXTERNAL, BOTH, GLOBAL 2. Mandatory if Item classification is BUSINESS and when EVENT.API is not defined 3. MANDATORY only allowed for SERVICE classification |
| 17 | `TEC.IT.SOURCE.TABLE` | `TecItems_Table` |  |  |  |
| 18 | `TEC.IT.FIELD.TYPE` | `TecItems_FieldType` |  |  |  |
| 19 | `TEC.IT.FIELD` | `TecItems_Field` |  |  |  |
| 20 | `TEC.IT.FIELD.DESC` | `TecItems_FieldDesc` |  |  |  |
| 21 | `TEC.IT.FIELD.NO` | `TecItems_FieldNo` |  |  |  |
| 22 | `TEC.IT.OPERAND` | `TecItems_Operand` |  |  |  |
| 23 | `TEC.IT.VALUE` | `TecItems_Value` |  |  |  |
| 24 | `TEC.IT.INHERIT` | `TecItems_Inherit` |  |  |  |
| 25 | `TEC.IT.SEVERITY` | `TecItems_Severity` | TField |  | This field describes the severity of the event. Validation rules: 1.Allowed values - CRITICAL, HIGH, MEDIUM, LOW. 2.Input allowed only when ITEM.CLASSIFICATION is BUSINESS |
| 26 | `TEC.IT.PRECEDENCE` | `TecItems_Precedence` |  |  |  |
| 27 | `TEC.IT.EVENT.API` | `TecItems_EventApi` | TField |  | This field is used to specify a Local API which is to be invoked before recording the event. Validation rules: 1.The routine entered should have a record on the EB.API application 2. Alphanumeric characters. Length: Maximum of 35 characters. 3. Input allowed only when ITEM.CLASSIFICATION is BUSINESS |
| 28 | `TEC.IT.STATUS` | `TecItems_Status` | TField |  | This field indicates the status of this TEC ITEM. 1.Possible Values - ACTIVE,INACTIVE 2. Input allowed only when ITEM.CLASSIFICATION is BUSINESS 3. Default is INACTIVE |
| 29 | `TEC.IT.ONE.TIME.SUB` | `TecItems_OneTimeSub` | TField |  | To indicate whether the particular event is one-time event or not. If set to YES, it will do automatic unsubscription of event from ACCOUNT/DAO. Automatic unsubscription is not possible during COB when used with DAO. 1. Possible Value - YES 2. NOCHANGE field |
| 30 | `TEC.IT.SEND.ALERTS.TO.ALL` | `TecItems_SendAlertsToAll` | TField | Yes | When this field is enabled,alerts will be sent to all customers belonging to particular account/ arrangement Validation rules: 1.Allowed values - YES, NULL. 2.Input allowed only when SUBSCRIPTION.LEVEL is MANDATORY |
| 31 | `TEC.IT.LOCAL.REF` | `TecItems_LocalRef` |  |  |  |
| 32 | `TEC.IT.RESERVED.7` | `TecItems_Reserved7` | TField |  |  |
| 33 | `TEC.IT.RESERVED.6` | `TecItems_Reserved6` | TField |  |  |
| 34 | `TEC.IT.RESERVED.5` | `TecItems_Reserved5` | TField |  |  |
| 35 | `TEC.IT.RESERVED.4` | `TecItems_Reserved4` | TField |  |  |
| 36 | `TEC.IT.RESERVED.3` | `TecItems_Reserved3` | TField |  |  |
| 37 | `TEC.IT.RESERVED.2` | `TecItems_Reserved2` | TField |  |  |
| 38 | `TEC.IT.RESERVED.1` | `TecItems_Reserved1` | TField |  |  |
| 39 | `TEC.IT.RECORD.STATUS` | `TecItems_RecordStatus` | String |  |  |
| 40 | `TEC.IT.CURR.NO` | `TecItems_CurrNo` | String |  |  |
| 41 | `TEC.IT.INPUTTER` | `TecItems_Inputter` |  |  |  |
| 42 | `TEC.IT.DATE.TIME` | `TecItems_DateTime` |  |  |  |
| 43 | `TEC.IT.AUTHORISER` | `TecItems_Authoriser` | String |  |  |
| 44 | `TEC.IT.CO.CODE` | `TecItems_CoCode` | String |  |  |
| 45 | `TEC.IT.DEPT.CODE` | `TecItems_DeptCode` | String |  |  |
| 46 | `TEC.IT.AUDITOR.CODE` | `TecItems_AuditorCode` | String |  |  |
| 47 | `TEC.IT.AUDIT.DATE.TIME` | `TecItems_AuditDateTime` | String |  |  |
