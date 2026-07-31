# SY.EVENT — Table Schema

> Source: `INSERTS/I_F.SY.EVENT` in `SY_Event.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.EV.EVENT.DEFINITION` | `SyEvent_EventDefinition` | TField |  | Holds the valid ID of SY.EVENT.DEFINITION record. This is a NOINPUT field. |
| 2 | `SY.EV.TRANSACTION` | `SyEvent_Transaction` | TField |  | Holds the valid ID of SY.TRANSACTION. This is a NOINPUT field. |
| 3 | `SY.EV.INSTANCE` | `SyEvent_Instance` | TField |  | This is a NOINPUT field. This field is used in SY.EVENT.LOG only. |
| 4 | `SY.EV.RESERVED.22` | `SyEvent_Reserved22` | TField |  |  |
| 5 | `SY.EV.SHORT.NAME` | `SyEvent_ShortName` |  |  |  |
| 6 | `SY.EV.DESCRIPTION` | `SyEvent_Description` |  |  |  |
| 7 | `SY.EV.RESERVED.21` | `SyEvent_Reserved21` | TField |  |  |
| 8 | `SY.EV.RESERVED.20` | `SyEvent_Reserved20` | TField |  |  |
| 9 | `SY.EV.RESERVED.19` | `SyEvent_Reserved19` | TField |  |  |
| 10 | `SY.EV.TRACKING` | `SyEvent_Tracking` | TField |  | Defines if this event is tracking or non-tracking. |
| 11 | `SY.EV.EVENT.TYPE` | `SyEvent_EventType` | TField | Conditional | This classifies the type of event. Some event types relate directly to a T24 function being applied to the Structured Product: Input Authorise Delete Reverse Scheduled - To be actioned on a predetermined date) Rolling - To be repeated at predetermined intervals) Add-Hoc - This will be triggered manually The event type chosen determines which additional fields are required: For Scheduled events, one of DATE or DATE.RULES must be entered with COB.PHASE optional. For Rolling events, FREQUENCY and COB.PHASE are mandatory and DATE.RULES is optional. For the other events these fields must not be used. |
| 12 | `SY.EV.ALLOW.RERUN` | `SyEvent_AllowRerun` | TField |  | Is the user able to re-run an event after it has been run (successfully) at least once. |
| 13 | `SY.EV.RESERVED.18` | `SyEvent_Reserved18` | TField |  |  |
| 14 | `SY.EV.RESERVED.17` | `SyEvent_Reserved17` | TField |  |  |
| 15 | `SY.EV.RESERVED.16` | `SyEvent_Reserved16` | TField |  |  |
| 16 | `SY.EV.DATE` | `SyEvent_Date` | TField |  | This is the date on which an event will be processed. |
| 17 | `SY.EV.DATE.RULES` | `SyEvent_DateRules` | TField |  | This defines the date rules for and event, defining the date in terms of the process date. T24 uses a range of keywords, codes and modifiers to represent the exchange rules when determining the dates. Keyword Meaning Comments MO Monday TU Tuesday WE Wednesday TH Thursday FR Friday SA Saturday SU Sunday M Month Only valid with multiplier/operator in same field W Week Only valid with multiplier/operator in same field CD Calendar days Only valid with multiplier/operator in same field BD Business days Only valid with multiplier/operator in same field LBD Last business day of the month Not valid with multiplier/operator in same field LCD Last calendar day of the month Not valid with multiplier/operator in same field FBD First business day of the month Not valid with multiplier/operator in same field FCD First calendar day of the month Not valid with multiplier/operator in same field MF* Move forward. If the date obtained is not a business day, the move forward until a business date is found. MB* Move backward If the date obtained is not a business day, then move backwards until a business date is found. CAL* Calendar Date Return the date obtained, . Operators and multipliers can then be applied to any of the above "keywords", subject to the rules shown in the table. For example, +3BD indicates add 3 business days. Some keywords are only valid in the presence of operators or multipliers. It makes no sense to put the keyword 'BD' into a field since it is only useful when describing a date offset, i.e. +3BD or -2BD. Conversely, keywords such as FBD and LCD describe fixed points in a month and are meaningless when combined with operators or multipliers. It is important to note that the scenario the first business day in the month 2 months forward is represented by +2M,FBD and not +2FBD. |
| 18 | `SY.EV.FREQUENCY` | `SyEvent_Frequency` | TField |  | Defines the frequency of a rolling event. |
| 19 | `SY.EV.INCLUDE.FIRST.DATE` | `SyEvent_IncludeFirstDate` | TField |  | If set, for rolling events, the first instance of the event being triggered is on the day that it is created (CREATE.DATE) or the start date (calculated from DATE and DATE.RULES) if specified; otherwise, the first instance of the event being triggered is the next date after that, according to the rolling interval chosen (FREQUENCY). |
| 20 | `SY.EV.RESERVED.15` | `SyEvent_Reserved15` | TField |  |  |
| 21 | `SY.EV.RESERVED.14` | `SyEvent_Reserved14` | TField |  |  |
| 22 | `SY.EV.RESERVED.13` | `SyEvent_Reserved13` | TField |  |  |
| 23 | `SY.EV.TERMINATOR.CASE` | `SyEvent_TerminatorCase` | TField |  | Defines if this event is the last event in a products lifecylcle. Once this event is processed no further events can be processed for the deal. |
| 24 | `SY.EV.COB.PHASE` | `SyEvent_CobPhase` | TField |  | For Scheduled and/or rolling events the Close of buiness processing will be invoked. This defined when during the COB the event will be processed. If set to 'Close of Business', event will be processed before system date change. If set to 'Start of Day', event will be processed after system date change. If set to 'Online', event will be processed after system date change during ONLINE phase. |
| 25 | `SY.EV.NOTES` | `SyEvent_Notes` |  |  |  |
| 26 | `SY.EV.RESERVED.12` | `SyEvent_Reserved12` | TField |  |  |
| 27 | `SY.EV.RESERVED.11` | `SyEvent_Reserved11` | TField |  |  |
| 28 | `SY.EV.RESERVED.10` | `SyEvent_Reserved10` | TField |  |  |
| 29 | `SY.EV.PROCESS` | `SyEvent_Process` | TField |  | This field is used to manually trigger the processing of an event. |
| 30 | `SY.EV.CREATE.DATE` | `SyEvent_CreateDate` | TField |  | The date on which this event was created. System-generated field only. |
| 31 | `SY.EV.LAST.RUN.DATE` | `SyEvent_LastRunDate` | TField |  | The last run date for the event. |
| 32 | `SY.EV.LOG.ID` | `SyEvent_LogId` |  |  |  |
| 33 | `SY.EV.TERMINATED` | `SyEvent_Terminated` | TField |  | This is a system-generated field only - shows whether this event has been terminated. |
| 34 | `SY.EV.RESERVED.9` | `SyEvent_Reserved9` | TField |  |  |
| 35 | `SY.EV.RESERVED.8` | `SyEvent_Reserved8` | TField |  |  |
| 36 | `SY.EV.RESERVED.7` | `SyEvent_Reserved7` | TField |  |  |
| 37 | `SY.EV.ACTIVITY.CODE` | `SyEvent_ActivityCode` |  |  |  |
| 38 | `SY.EV.RESERVED.62` | `SyEvent_Reserved62` |  |  |  |
| 39 | `SY.EV.RESERVED.61` | `SyEvent_Reserved61` |  |  |  |
| 40 | `SY.EV.MESSAGE.REF` | `SyEvent_MessageRef` |  |  |  |
| 41 | `SY.EV.RESERVED.6` | `SyEvent_Reserved6` | TField |  |  |
| 42 | `SY.EV.RESERVED.5` | `SyEvent_Reserved5` | TField |  |  |
| 43 | `SY.EV.RESERVED.4` | `SyEvent_Reserved4` | TField |  |  |
| 44 | `SY.EV.CLEAR.UP` | `SyEvent_ClearUp` | TField |  | For System use only - Not Inputtable by users. Defines if a background cleanup is required. |
| 45 | `SY.EV.CRITICAL` | `SyEvent_Critical` | TField |  | Defines if this event is critical in the products lifecycle and will prevent the user from reversing the deal. |
| 46 | `SY.EV.NO.CHANGE` | `SyEvent_NoChange` | TField |  | Defines if this event should block the amendment of the deal. |
| 47 | `SY.EV.RESERVED.3` | `SyEvent_Reserved3` | TField |  |  |
| 48 | `SY.EV.RESERVED.2` | `SyEvent_Reserved2` | TField |  |  |
| 49 | `SY.EV.RESERVED.1` | `SyEvent_Reserved1` | TField |  |  |
| 50 | `SY.EV.INTERNAL.USE` | `SyEvent_InternalUse` | TField |  | This is a NOINPUT field. This field is only for internal system use. |
| 51 | `SY.EV.LOCAL.REF` | `SyEvent_LocalRef` |  |  |  |
| 52 | `SY.EV.OVERRIDE` | `SyEvent_Override` |  |  |  |
| 53 | `SY.EV.RECORD.STATUS` | `SyEvent_RecordStatus` | String |  |  |
| 54 | `SY.EV.CURR.NO` | `SyEvent_CurrNo` | String |  |  |
| 55 | `SY.EV.INPUTTER` | `SyEvent_Inputter` |  |  |  |
| 56 | `SY.EV.DATE.TIME` | `SyEvent_DateTime` |  |  |  |
| 57 | `SY.EV.AUTHORISER` | `SyEvent_Authoriser` | String |  |  |
| 58 | `SY.EV.CO.CODE` | `SyEvent_CoCode` | String |  |  |
| 59 | `SY.EV.DEPT.CODE` | `SyEvent_DeptCode` | String |  |  |
| 60 | `SY.EV.AUDITOR.CODE` | `SyEvent_AuditorCode` | String |  |  |
| 61 | `SY.EV.AUDIT.DATE.TIME` | `SyEvent_AuditDateTime` | String |  |  |
