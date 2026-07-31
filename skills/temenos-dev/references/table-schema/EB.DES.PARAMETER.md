# EB.DES.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.DES.PARAMETER` in `EB_Streaming.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DES.DESCRIPTION` | `EbDesParameter_Description` |  |  |  |
| 2 | `EB.DES.EMIT.APPLICATION` | `EbDesParameter_EmitApplication` |  |  |  |
| 3 | `EB.DES.PRIORITY.APPLICATION` | `EbDesParameter_PriorityApplication` |  |  |  |
| 4 | `EB.DES.DATA.STREAM` | `EbDesParameter_DataStream` | TField |  | Indicates whether the OUTBOX or AVRO events should be emitted for the configured RR.PARAM table By Default, DES event will be emitted for the configured RR.PARAM table All the events should be capable to emit only if the field SPF>DATA.STREAM set to YES. Validation Rules: Possible values are OUTBOX or AVRO |
| 5 | `EB.DES.RESERVED9` | `EbDesParameter_Reserved9` |  |  |  |
| 6 | `EB.DES.RESERVED8` | `EbDesParameter_Reserved8` |  |  |  |
| 7 | `EB.DES.RESERVED7` | `EbDesParameter_Reserved7` |  |  |  |
| 8 | `EB.DES.RESERVED6` | `EbDesParameter_Reserved6` | TField |  |  |
| 9 | `EB.DES.RESERVED5` | `EbDesParameter_Reserved5` | TField |  |  |
| 10 | `EB.DES.RESERVED4` | `EbDesParameter_Reserved4` | TField |  |  |
| 11 | `EB.DES.RESERVED3` | `EbDesParameter_Reserved3` | TField |  |  |
| 12 | `EB.DES.RESERVED2` | `EbDesParameter_Reserved2` | TField |  |  |
| 13 | `EB.DES.RESERVED1` | `EbDesParameter_Reserved1` | TField |  |  |
| 14 | `EB.DES.LOCAL.REF` | `EbDesParameter_LocalRef` |  |  |  |
| 15 | `EB.DES.OVERRIDE` | `EbDesParameter_Override` |  |  |  |
| 16 | `EB.DES.RECORD.STATUS` | `EbDesParameter_RecordStatus` | String |  |  |
| 17 | `EB.DES.CURR.NO` | `EbDesParameter_CurrNo` | String |  |  |
| 18 | `EB.DES.INPUTTER` | `EbDesParameter_Inputter` |  |  |  |
| 19 | `EB.DES.DATE.TIME` | `EbDesParameter_DateTime` |  |  |  |
| 20 | `EB.DES.AUTHORISER` | `EbDesParameter_Authoriser` | String |  |  |
| 21 | `EB.DES.CO.CODE` | `EbDesParameter_CoCode` | String |  |  |
| 22 | `EB.DES.DEPT.CODE` | `EbDesParameter_DeptCode` | String |  |  |
| 23 | `EB.DES.AUDITOR.CODE` | `EbDesParameter_AuditorCode` | String |  |  |
| 24 | `EB.DES.AUDIT.DATE.TIME` | `EbDesParameter_AuditDateTime` | String |  |  |
