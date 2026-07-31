# EB.EXTERNAL.EVENTS.DEFINITION — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.EVENTS.DEFINITION` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DESCRIPTION` | `EbExternalEventsDefinition_Description` |  |  |  |
| 2 | `EB.SYS.TAG.NAME` | `EbExternalEventsDefinition_SysTagName` |  |  |  |
| 3 | `EB.SYS.TAG.POSITION` | `EbExternalEventsDefinition_SysTagPosition` |  |  |  |
| 4 | `EB.SYS.IGNORE.EMPTY.TAG` | `EbExternalEventsDefinition_SysIgnoreEmptyTag` |  |  |  |
| 5 | `EB.SYS.TAG.DATATYPE` | `EbExternalEventsDefinition_SysTagDatatype` |  |  |  |
| 6 | `EB.RESERVED.1` | `EbExternalEventsDefinition_Reserved1` |  |  |  |
| 7 | `EB.RESERVED.2` | `EbExternalEventsDefinition_Reserved2` |  |  |  |
| 8 | `EB.RESERVED.3` | `EbExternalEventsDefinition_Reserved3` |  |  |  |
| 9 | `EB.RESERVED.4` | `EbExternalEventsDefinition_Reserved4` |  |  |  |
| 10 | `EB.RESERVED.5` | `EbExternalEventsDefinition_Reserved5` |  |  |  |
| 11 | `EB.USR.TAG.NAME` | `EbExternalEventsDefinition_UsrTagName` |  |  |  |
| 12 | `EB.USR.TAG.POSITION` | `EbExternalEventsDefinition_UsrTagPosition` |  |  |  |
| 13 | `EB.USR.IGNORE.EMPTY.TAG` | `EbExternalEventsDefinition_UsrIgnoreEmptyTag` |  |  |  |
| 14 | `EB.USR.TAG.DATATYPE` | `EbExternalEventsDefinition_UsrTagDatatype` |  |  |  |
| 15 | `EB.RESERVED.6` | `EbExternalEventsDefinition_Reserved6` |  |  |  |
| 16 | `EB.RESERVED.7` | `EbExternalEventsDefinition_Reserved7` |  |  |  |
| 17 | `EB.RESERVED.8` | `EbExternalEventsDefinition_Reserved8` |  |  |  |
| 18 | `EB.RESERVED.9` | `EbExternalEventsDefinition_Reserved9` |  |  |  |
| 19 | `EB.RESERVED.10` | `EbExternalEventsDefinition_Reserved10` |  |  |  |
| 20 | `EB.METRIC.TYPE` | `EbExternalEventsDefinition_MetricType` | TField |  | configure the metrics for monitoring Metric type like gauge,log,counter |
| 21 | `EB.METRIC.VALUE` | `EbExternalEventsDefinition_MetricValue` | TField |  | Define the tag name as a part of value Validation Rules: The value should be part of tag Name The value is set for gauge only |
| 22 | `EB.RESERVED.13` | `EbExternalEventsDefinition_Reserved13` |  |  |  |
| 23 | `EB.RESERVED.14` | `EbExternalEventsDefinition_Reserved14` | TField |  | Reserved Field |
| 24 | `EB.RESERVED.15` | `EbExternalEventsDefinition_Reserved15` | TField |  | Reserved Field |
| 25 | `EB.RESERVED.16` | `EbExternalEventsDefinition_Reserved16` | TField |  | Reserved Field |
| 26 | `EB.RESERVED.17` | `EbExternalEventsDefinition_Reserved17` | TField |  | Reserved Field |
| 27 | `EB.RESERVED.18` | `EbExternalEventsDefinition_Reserved18` | TField |  | Reserved Field |
| 28 | `EB.RESERVED.19` | `EbExternalEventsDefinition_Reserved19` | TField |  | Reserved Field |
| 29 | `EB.RESERVED.20` | `EbExternalEventsDefinition_Reserved20` | TField |  | Reserved Field |
| 30 | `EB.LOCAL.REF` | `EbExternalEventsDefinition_LocalRef` |  |  |  |
| 31 | `EB.OVERRIDE` | `EbExternalEventsDefinition_Override` |  |  |  |
| 32 | `EB.RECORD.STATUS` | `EbExternalEventsDefinition_RecordStatus` | String |  |  |
| 33 | `EB.CURR.NO` | `EbExternalEventsDefinition_CurrNo` | String |  |  |
| 34 | `EB.INPUTTER` | `EbExternalEventsDefinition_Inputter` |  |  |  |
| 35 | `EB.DATE.TIME` | `EbExternalEventsDefinition_DateTime` |  |  |  |
| 36 | `EB.AUTHORISER` | `EbExternalEventsDefinition_Authoriser` | String |  |  |
| 37 | `EB.CO.CODE` | `EbExternalEventsDefinition_CoCode` | String |  |  |
| 38 | `EB.DEPT.CODE` | `EbExternalEventsDefinition_DeptCode` | String |  |  |
| 39 | `EB.AUDITOR.CODE` | `EbExternalEventsDefinition_AuditorCode` | String |  |  |
| 40 | `EB.AUDIT.DATE.TIME` | `EbExternalEventsDefinition_AuditDateTime` | String |  |  |
