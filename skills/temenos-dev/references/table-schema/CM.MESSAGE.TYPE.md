# CM.MESSAGE.TYPE — Table Schema

> Source: `INSERTS/I_F.CM.MESSAGE.TYPE` in `CM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CM.ME.T.OUT.MATCH.TAG` | `CmMessageType_OutMatchTag` |  |  |  |
| 2 | `CM.ME.T.IN.MATCH.TAG` | `CmMessageType_InMatchTag` |  |  |  |
| 3 | `CM.ME.T.OUT.OPTION.TAG` | `CmMessageType_OutOptionTag` |  |  |  |
| 4 | `CM.ME.T.IN.OPTION.TAG` | `CmMessageType_InOptionTag` |  |  |  |
| 5 | `CM.ME.T.LOCAL.REF` | `CmMessageType_LocalRef` |  |  |  |
| 6 | `CM.ME.T.HOOK.RTN` | `CmMessageType_HookRtn` | TField |  | Name of the hook routine used is specified in this field. It takes DE.O.HEADER ID and DE.O.HEADER record as incoming arguments. Error variable is outgoing argument which needs to be set for preventing writing of messages to CM.HOLDING.QUEUE Sample routine has been released under the name "DE.UPD.CM.HOLDING.QUEUE". |
| 7 | `CM.ME.T.RESERVED9` | `CmMessageType_Reserved9` | TField |  |  |
| 8 | `CM.ME.T.RESERVED8` | `CmMessageType_Reserved8` | TField |  |  |
| 9 | `CM.ME.T.RESERVED7` | `CmMessageType_Reserved7` | TField |  |  |
| 10 | `CM.ME.T.RESERVED6` | `CmMessageType_Reserved6` | TField |  |  |
| 11 | `CM.ME.T.RESERVED5` | `CmMessageType_Reserved5` | TField |  |  |
| 12 | `CM.ME.T.RESERVED4` | `CmMessageType_Reserved4` | TField |  |  |
| 13 | `CM.ME.T.RESERVED3` | `CmMessageType_Reserved3` | TField |  |  |
| 14 | `CM.ME.T.RESERVED2` | `CmMessageType_Reserved2` | TField |  |  |
| 15 | `CM.ME.T.OVERRIDE` | `CmMessageType_Override` |  |  |  |
| 16 | `CM.ME.T.RECORD.STATUS` | `CmMessageType_RecordStatus` | String |  |  |
| 17 | `CM.ME.T.CURR.NO` | `CmMessageType_CurrNo` | String |  |  |
| 18 | `CM.ME.T.INPUTTER` | `CmMessageType_Inputter` |  |  |  |
| 19 | `CM.ME.T.DATE.TIME` | `CmMessageType_DateTime` |  |  |  |
| 20 | `CM.ME.T.AUTHORISER` | `CmMessageType_Authoriser` | String |  |  |
| 21 | `CM.ME.T.CO.CODE` | `CmMessageType_CoCode` | String |  |  |
| 22 | `CM.ME.T.DEPT.CODE` | `CmMessageType_DeptCode` | String |  |  |
| 23 | `CM.ME.T.AUDITOR.CODE` | `CmMessageType_AuditorCode` | String |  |  |
| 24 | `CM.ME.T.AUDIT.DATE.TIME` | `CmMessageType_AuditDateTime` | String |  |  |
