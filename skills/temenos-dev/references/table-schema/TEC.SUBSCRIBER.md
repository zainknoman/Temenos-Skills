# TEC.SUBSCRIBER — Table Schema

> Source: `INSERTS/I_F.TEC.SUBSCRIBER` in `EB_Logging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TSU.DESCRIPTION` | `TecSubscriber_Description` |  |  |  |
| 2 | `TSU.PUSH.API` | `TecSubscriber_PushApi` | TField |  | The API AA.PROCESS.EXTERNAL.ACTIVITY is used for creation the activity record for AA facility(Service) request. Its will use the following user data passed into the hand-off details. 1 - System id for the transaction(EB.SYSTEM.ID) 2 - Contract id of the transaction(ID.NEW) 3 - Old record of the transaction(R.OLD) 4 - New record of the transaction(R.NEW) |
| 3 | `TSU.TIME.OUT` | `TecSubscriber_TimeOut` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `TSU.INLINE` | `TecSubscriber_Inline` | TField |  | Its will indicate whether the subscribe is Inline or not. Validation Rules: The Inline subscriber should be released and maintained by Temenos and user only possible to amend the description |
| 5 | `TSU.RESERVED.9` | `TecSubscriber_Reserved9` | TField |  |  |
| 6 | `TSU.RESERVED.8` | `TecSubscriber_Reserved8` | TField |  |  |
| 7 | `TSU.RESERVED.7` | `TecSubscriber_Reserved7` | TField |  |  |
| 8 | `TSU.RESERVED.6` | `TecSubscriber_Reserved6` | TField |  |  |
| 9 | `TSU.RESERVED.5` | `TecSubscriber_Reserved5` | TField |  |  |
| 10 | `TSU.RESERVED.4` | `TecSubscriber_Reserved4` | TField |  |  |
| 11 | `TSU.RESERVED.3` | `TecSubscriber_Reserved3` | TField |  |  |
| 12 | `TSU.RESERVED.2` | `TecSubscriber_Reserved2` | TField |  |  |
| 13 | `TSU.RESERVED.1` | `TecSubscriber_Reserved1` | TField |  |  |
| 14 | `TSU.LOCAL.REF` | `TecSubscriber_LocalRef` |  |  |  |
| 15 | `TSU.OVERRIDE` | `TecSubscriber_Override` |  |  |  |
| 16 | `TSU.RECORD.STATUS` | `TecSubscriber_RecordStatus` | String |  |  |
| 17 | `TSU.CURR.NO` | `TecSubscriber_CurrNo` | String |  |  |
| 18 | `TSU.INPUTTER` | `TecSubscriber_Inputter` |  |  |  |
| 19 | `TSU.DATE.TIME` | `TecSubscriber_DateTime` |  |  |  |
| 20 | `TSU.AUTHORISER` | `TecSubscriber_Authoriser` | String |  |  |
| 21 | `TSU.CO.CODE` | `TecSubscriber_CoCode` | String |  |  |
| 22 | `TSU.DEPT.CODE` | `TecSubscriber_DeptCode` | String |  |  |
| 23 | `TSU.AUDITOR.CODE` | `TecSubscriber_AuditorCode` | String |  |  |
| 24 | `TSU.AUDIT.DATE.TIME` | `TecSubscriber_AuditDateTime` | String |  |  |
