# TEC.DISPLAY — Table Schema

> Source: `INSERTS/I_F.TEC.DISPLAY` in `EB_Logging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TEC.DS.ITEM.TYPE` | `TecDisplay_ItemType` | TField |  | Key of the TEC.ITEMS record which is used to identify the TEC event initialization. |
| 2 | `TEC.DS.ITEM.DETAIL` | `TecDisplay_ItemDetail` | TField |  | This field holds the file name on which the event is triggered. |
| 3 | `TEC.DS.THRESHOLD` | `TecDisplay_Threshold` |  |  |  |
| 4 | `TEC.DS.THRESH.COUNT` | `TecDisplay_ThreshCount` |  |  |  |
| 5 | `TEC.DS.THRESH.TOTAL` | `TecDisplay_ThreshTotal` |  |  |  |
| 6 | `TEC.DS.METRIC.COUNT` | `TecDisplay_MetricCount` | TField |  | Number of times this event got triggered. |
| 7 | `TEC.DS.METRIC.TOTAL` | `TecDisplay_MetricTotal` | TField |  | If the same event has triggered more than one time then it just add the metric value with previous one(updated in METRIC.HIGH) and also the old values of time and date would be replaced with latest values in respective fields like SERVER.DATE,SERVER.TIME,START.TIME and END.TIME. |
| 8 | `TEC.DS.METRIC.AVG` | `TecDisplay_MetricAvg` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `TEC.DS.METRIC.HIGH` | `TecDisplay_MetricHigh` | TField |  | THRESHOLD value of the TEC metric. E.g) Value updated here is 500 and If "READ.SIZE" got updated in ITEM.TYPE field then we could say my record size exceeds 500 when I try to read the record (DS.TOP.KEY) on the file (ITEM.DETAIL) during the transaction of the APPLICATION(ID is DS.TXN.REF). |
| 10 | `TEC.DS.TOP.KEY` | `TecDisplay_TopKey` | TField |  | ID of the file mentioned in ITEM.DETAIL. |
| 11 | `TEC.DS.TXN.REF` | `TecDisplay_TxnRef` | TField |  | if the TEC event is triggered during the transaction then the corresponding transaction reference would be logged here. |
| 12 | `TEC.DS.APPLICATION` | `TecDisplay_Application` | TField |  | If TEC event is triggered during the transaction then the corresponding application name of the transaction would be logged here. |
| 13 | `TEC.DS.SERVER.NAME` | `TecDisplay_ServerName` | TField |  | Server name on which the TEC activity got generated |
| 14 | `TEC.DS.SERVER.DATE` | `TecDisplay_ServerDate` | TField |  | Date on which the TEC activity got generated |
| 15 | `TEC.DS.SERVER.TIME` | `TecDisplay_ServerTime` | TField |  | Time on which the TEC activity got generated |
| 16 | `TEC.DS.START.TIME` | `TecDisplay_StartTime` | TField |  | Start time of the event trace. |
| 17 | `TEC.DS.END.TIME` | `TecDisplay_EndTime` | TField |  | End time of the Event trace |
| 18 | `TEC.DS.ITEM.ID` | `TecDisplay_ItemId` | TField |  | This field also holds the ID of the TEC.ITEMS records to identify the THRESHOLD and THRESHOLD.TYPE defined in TEC.ITEMS records |
| 19 | `TEC.DS.CHANNEL` | `TecDisplay_Channel` | TField |  | To identify the OFS.SOURCE Channel used for the communication with T24.If there is no channel specified in OFS.SOURCE record then this field holds the value of OFS.SOURCE id.During the service if any event is triggred then this field holds the value "SERVICE" |
| 20 | `TEC.DS.LAST.UPDATED.TIME` | `TecDisplay_LastUpdatedTime` | TField |  | If the same event has been triggered more than once, this field contains the maximum value of SERVER.TIME of all TEC.DISPLAY items belonging to the same TEC.OUTPUT record. If not, this contains the SERVER.TIME of that metric. |
| 21 | `TEC.DS.FIRST.UPDATED.TIME` | `TecDisplay_FirstUpdatedTime` | TField |  | If the same event has been triggered more than once, this field contains the minimum value of SERVER.TIMEs of all TEC.DISPLAY items belonging to the same TEC.OUTPUT record. If not, this contains the SERVER.TIME of that metric. |
| 22 | `TEC.DS.JAVA.API` | `TecDisplay_JavaApi` | TField |  | This field holds the name of the java api which is triggered from any of the user exit points. |
