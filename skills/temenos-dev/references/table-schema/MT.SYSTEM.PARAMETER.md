# MT.SYSTEM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.MT.SYSTEM.PARAMETER` in `MT_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MT.PARAM.DESCRIPTION` | `MtSystemParameter_Description` |  |  |  |
| 2 | `MT.PARAM.MSG.EMIT.TYPE` | `MtSystemParameter_MsgEmitType` | TField | Yes | This field is to define the message emission type, by which the message(xml) formation can be defined as INDIVIDUAL messages(multi emit) during MT console table authorisation. Validation Rules: Accepted value: INDIVIDUAL :- One event emit will happen for each tenant. If the SERVICE.COMP.MNE field in MT.TSA.SERVICE.CONSOLE has more than one value, then several event messages will be created in the single xml emitted. Mandatory field. |
| 3 | `MT.PARAM.MSG.TYPE` | `MtSystemParameter_MsgType` | TField |  | This field contains the style of the message(s) to be generated. Validation Rules: Accepted values are: 1. QUEUE :- Signifies that the message should contain an embedded OFS payload, that can be passed through with minimal intervention from the external tools. A QUEUE based message will have tenant id as the prefix to the OFS payload. The emitted message is still XML format. 2. TOPIC :- Signifies that the message should contain an embedded OFS payload, that can be passed through with minimal intervention from the external tools. A TOPIC based message will have both the topic and the tenant id as the prefix to the OFS payload. The emitted message is still XML format. This TOPIC prefix value will be considered as a target directory/queue in an external system where the messages can be placed for further processing. |
| 4 | `MT.PARAM.TOPIC.PREFIX` | `MtSystemParameter_TopicPrefix` | TField | Yes | This field can have the topic prefix value for the topic message type defined in MSG.TYPE field. This value will be prefixed to the ofs payload (along with tenant id) which will be part of the output xml. Validation Rules: Maximum of 35 characters allowed Value permitted only when MSG.TYPE = TOPIC. This field is mandatory if MSG.TYPE = TOPIC. |
| 5 | `MT.PARAM.OFS.SOURCE` | `MtSystemParameter_OfsSource` | TField | Yes | This field can be used to define the OFS.SOURCE id required to process emitted message(s). Validation Rules: Maximum of 35 characters allowed. Must be a valid entry in OFS.SOURCE table. Mandatory field |
| 6 | `MT.PARAM.RESERVED.10` | `MtSystemParameter_Reserved10` | TField |  |  |
| 7 | `MT.PARAM.RESERVED.9` | `MtSystemParameter_Reserved9` | TField |  |  |
| 8 | `MT.PARAM.RESERVED.8` | `MtSystemParameter_Reserved8` | TField |  |  |
| 9 | `MT.PARAM.RESERVED.7` | `MtSystemParameter_Reserved7` | TField |  |  |
| 10 | `MT.PARAM.RESERVED.6` | `MtSystemParameter_Reserved6` | TField |  |  |
| 11 | `MT.PARAM.RESERVED.5` | `MtSystemParameter_Reserved5` | TField |  |  |
| 12 | `MT.PARAM.RESERVED.4` | `MtSystemParameter_Reserved4` | TField |  |  |
| 13 | `MT.PARAM.RESERVED.3` | `MtSystemParameter_Reserved3` | TField |  |  |
| 14 | `MT.PARAM.RESERVED.2` | `MtSystemParameter_Reserved2` | TField |  |  |
| 15 | `MT.PARAM.RESERVED.1` | `MtSystemParameter_Reserved1` | TField |  |  |
| 16 | `MT.PARAM.RECORD.STATUS` | `MtSystemParameter_RecordStatus` | String |  |  |
| 17 | `MT.PARAM.CURR.NO` | `MtSystemParameter_CurrNo` | String |  |  |
| 18 | `MT.PARAM.INPUTTER` | `MtSystemParameter_Inputter` |  |  |  |
| 19 | `MT.PARAM.DATE.TIME` | `MtSystemParameter_DateTime` |  |  |  |
| 20 | `MT.PARAM.AUTHORISER` | `MtSystemParameter_Authoriser` | String |  |  |
| 21 | `MT.PARAM.CO.CODE` | `MtSystemParameter_CoCode` | String |  |  |
| 22 | `MT.PARAM.DEPT.CODE` | `MtSystemParameter_DeptCode` | String |  |  |
| 23 | `MT.PARAM.AUDITOR.CODE` | `MtSystemParameter_AuditorCode` | String |  |  |
| 24 | `MT.PARAM.AUDIT.DATE.TIME` | `MtSystemParameter_AuditDateTime` | String |  |  |
