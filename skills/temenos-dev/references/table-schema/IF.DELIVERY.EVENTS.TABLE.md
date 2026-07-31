# IF.DELIVERY.EVENTS.TABLE — Table Schema

> Source: `INSERTS/I_F.IF.DELIVERY.EVENTS.TABLE` in `IF_IntegrationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.DL.EVENT.DATA` | `IfDlEventData` |  |  |  |
| 2 | `IF.DL.EVENT.TYPE` | `IfDlEventType` |  |  |  |
| 3 | `IF.DL.EVENT.TIMESTAMP` | `IfDlEventTimestamp` |  |  |  |
| 4 | `IF.DL.OLD.EVENT.XML` | `IfDlOldEventXml` |  |  |  |
| 5 | `IF.DL.LOCAL.TRANSFORM` | `IfDlLocalTransform` |  |  |  |
| 6 | `IF.DL.DELIVERY.STATUS` | `IfDlDeliveryStatus` |  |  |  |
| 7 | `IF.DL.STATUS.REASON` | `IfDlStatusReason` |  |  |  |
| 8 | `IF.DL.EVENT.XML.NAME` | `IfDlEventXmlName` |  |  |  |
| 9 | `IF.DL.OLD.FIELD.VALUE` | `IfDlOldFieldValue` |  |  |  |
| 10 | `IF.DL.FIELD.VALUE` | `IfDlFieldValue` |  |  |  |
| 11 | `IF.DL.CREATION.TIME` | `IfDlCreationTime` |  |  |  |
| 12 | `IF.DL.CREATION.DATE` | `IfDlCreationDate` |  |  |  |
| 13 | `IF.DL.EVENT.PRIORITY` | `IfDlEventPriority` |  |  |  |
| 14 | `IF.DL.RESERVED22` | `IfDlReserved22` |  |  |  |
| 15 | `IF.DL.COMMON.XML.NAME` | `IfDlCommonXmlName` |  |  |  |
| 16 | `IF.DL.COMMON.XML.VAL` | `IfDlCommonXmlVal` |  |  |  |
| 17 | `IF.DL.SOURCE` | `IfDlSource` |  |  |  |
| 18 | `IF.DL.CORRELATION.ID` | `IfDlCorrelationId` |  |  |  |
| 19 | `IF.DL.RESERVED.27` | `IfDlReserved27` |  |  |  |
| 20 | `IF.DL.RESERVED.28` | `IfDlReserved28` |  |  |  |
| 21 | `IF.DL.RESERVED.29` | `IfDlReserved29` |  |  |  |
| 22 | `IF.DL.RESERVED.30` | `IfDlReserved30` |  |  |  |
| 23 | `IF.DL.RESERVED.31` | `IfDlReserved31` |  |  |  |
| 24 | `IF.DL.RESERVED.32` | `IfDlReserved32` |  |  |  |
| 25 | `IF.DL.RESERVED.33` | `IfDlReserved33` |  |  |  |
| 26 | `IF.DL.RESERVED.34` | `IfDlReserved34` |  |  |  |
| 27 | `IF.DL.RESERVED.35` | `IfDlReserved35` |  |  |  |
| 28 | `IF.DL.RESERVED.36` | `IfDlReserved36` |  |  |  |
| 29 | `IF.DL.RESERVED.37` | `IfDlReserved37` |  |  |  |
| 30 | `IF.DL.RESERVED.38` | `IfDlReserved38` |  |  |  |
| 31 | `IF.DL.RESERVED.39` | `IfDlReserved39` |  |  |  |
| 32 | `IF.DL.OVERRIDE` | `IfDlOverride` |  |  |  |
| 33 | `IF.DL.RECORD.STATUS` | `IfDlRecordStatus` |  |  |  |
| 34 | `IF.DL.CURR.NO` | `IfDlCurrNo` |  |  |  |
| 35 | `IF.DL.INPUTTER` | `IfDlInputter` |  |  |  |
| 36 | `IF.DL.DATE.TIME` | `IfDlDateTime` |  |  |  |
| 37 | `IF.DL.AUTHORISER` | `IfDlAuthoriser` |  |  |  |
| 38 | `IF.DL.CO.CODE` | `IfDlCoCode` |  |  |  |
| 39 | `IF.DL.DEPT.CODE` | `IfDlDeptCode` |  |  |  |
| 40 | `IF.DL.AUDITOR.CODE` | `IfDlAuditorCode` |  |  |  |
| 41 | `IF.DL.AUDIT.DATE.TIME` | `IfDlAuditDateTime` |  |  |  |
