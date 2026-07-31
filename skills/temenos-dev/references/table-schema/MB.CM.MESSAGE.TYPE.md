# MB.CM.MESSAGE.TYPE — Table Schema

> Source: `INSERTS/I_F.MB.CM.MESSAGE.TYPE` in `CM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMM.OUT.TAG` | `MbCmMessageType_OutTag` |  |  |  |
| 2 | `CMM.OUT.SEQUENCE` | `MbCmMessageType_OutSequence` |  |  |  |
| 3 | `CMM.IN.TAG` | `MbCmMessageType_InTag` |  |  |  |
| 4 | `CMM.IN.SEQUENCE` | `MbCmMessageType_InSequence` |  |  |  |
| 5 | `CMM.MATCH.CRITERIA` | `MbCmMessageType_MatchCriteria` |  |  |  |
| 6 | `CMM.LIKE.CRITERIA` | `MbCmMessageType_LikeCriteria` |  |  |  |
| 7 | `CMM.OUT.VALUE` | `MbCmMessageType_OutValue` |  |  |  |
| 8 | `CMM.IN.VALUE` | `MbCmMessageType_InValue` |  |  |  |
| 9 | `CMM.OFS.SOURCE` | `MbCmMessageType_OfsSource` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `CMM.OFS.VERSION` | `MbCmMessageType_OfsVersion` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 11 | `CMM.RESERVED.3` | `MbCmMessageType_Reserved3` | TField |  |  |
| 12 | `CMM.RESERVED.4` | `MbCmMessageType_Reserved4` | TField |  |  |
| 13 | `CMM.RESERVED.5` | `MbCmMessageType_Reserved5` | TField |  |  |
| 14 | `CMM.RESERVED.6` | `MbCmMessageType_Reserved6` | TField |  |  |
| 15 | `CMM.LOCAL.REF` | `MbCmMessageType_LocalRef` |  |  |  |
| 16 | `CMM.OVERRIDE` | `MbCmMessageType_Override` |  |  |  |
| 17 | `CMM.RECORD.STATUS` | `MbCmMessageType_RecordStatus` | String |  |  |
| 18 | `CMM.CURR.NO` | `MbCmMessageType_CurrNo` | String |  |  |
| 19 | `CMM.INPUTTER` | `MbCmMessageType_Inputter` |  |  |  |
| 20 | `CMM.DATE.TIME` | `MbCmMessageType_DateTime` |  |  |  |
| 21 | `CMM.AUTHORISER` | `MbCmMessageType_Authoriser` | String |  |  |
| 22 | `CMM.CO.CODE` | `MbCmMessageType_CoCode` | String |  |  |
| 23 | `CMM.DEPT.CODE` | `MbCmMessageType_DeptCode` | String |  |  |
| 24 | `CMM.AUDITOR.CODE` | `MbCmMessageType_AuditorCode` | String |  |  |
| 25 | `CMM.AUDIT.DATE.TIME` | `MbCmMessageType_AuditDateTime` | String |  |  |
