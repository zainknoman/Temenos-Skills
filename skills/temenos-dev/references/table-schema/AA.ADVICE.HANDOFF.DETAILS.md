# AA.ADVICE.HANDOFF.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.ADVICE.HANDOFF.DETAILS` in `AA_ActivityMessaging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ADV.PROPERTY.CLASS` | `AaAdviceHandoffDetails_PropertyClass` | TField |  | This field indicates whether only the current information or previous and current information needs to be passed to form the message. Allowed values: ALL - Both current and previous property details needs to be passed CHANGE - Only the current property details needs to be passed |
| 2 | `AA.ADV.ADDITIONAL.CONTENT` | `AaAdviceHandoffDetails_AdditionalContent` |  |  |  |
| 3 | `AA.ADV.USER.HANDOFF.ROUTINE` | `AaAdviceHandoffDetails_UserHandoffRoutine` | TField |  | This field contains the Handoff routine name Validation Rules: 1. The routine name should be present in EB.API (CheckFile) |
| 4 | `AA.ADV.RESERVED.2` | `AaAdviceHandoffDetails_Reserved2` | TField |  |  |
| 5 | `AA.ADV.RESERVED.3` | `AaAdviceHandoffDetails_Reserved3` | TField |  |  |
| 6 | `AA.ADV.RESERVED.4` | `AaAdviceHandoffDetails_Reserved4` | TField |  |  |
| 7 | `AA.ADV.RESERVED.5` | `AaAdviceHandoffDetails_Reserved5` | TField |  |  |
| 8 | `AA.ADV.RESERVED.6` | `AaAdviceHandoffDetails_Reserved6` | TField |  |  |
| 9 | `AA.ADV.RESERVED.7` | `AaAdviceHandoffDetails_Reserved7` | TField |  |  |
| 10 | `AA.ADV.RESERVED.8` | `AaAdviceHandoffDetails_Reserved8` | TField |  |  |
| 11 | `AA.ADV.RESERVED.9` | `AaAdviceHandoffDetails_Reserved9` | TField |  |  |
| 12 | `AA.ADV.RESERVED.10` | `AaAdviceHandoffDetails_Reserved10` | TField |  |  |
| 13 | `AA.ADV.LOCAL.REF` | `AaAdviceHandoffDetails_LocalRef` |  |  |  |
| 14 | `AA.ADV.OVERRIDE` | `AaAdviceHandoffDetails_Override` |  |  |  |
| 15 | `AA.ADV.RECORD.STATUS` | `AaAdviceHandoffDetails_RecordStatus` | String |  |  |
| 16 | `AA.ADV.CURR.NO` | `AaAdviceHandoffDetails_CurrNo` | String |  |  |
| 17 | `AA.ADV.INPUTTER` | `AaAdviceHandoffDetails_Inputter` |  |  |  |
| 18 | `AA.ADV.DATE.TIME` | `AaAdviceHandoffDetails_DateTime` |  |  |  |
| 19 | `AA.ADV.AUTHORISER` | `AaAdviceHandoffDetails_Authoriser` | String |  |  |
| 20 | `AA.ADV.CO.CODE` | `AaAdviceHandoffDetails_CoCode` | String |  |  |
| 21 | `AA.ADV.DEPT.CODE` | `AaAdviceHandoffDetails_DeptCode` | String |  |  |
| 22 | `AA.ADV.AUDITOR.CODE` | `AaAdviceHandoffDetails_AuditorCode` | String |  |  |
| 23 | `AA.ADV.AUDIT.DATE.TIME` | `AaAdviceHandoffDetails_AuditDateTime` | String |  |  |
