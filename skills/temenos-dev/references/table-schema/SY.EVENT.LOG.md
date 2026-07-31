# SY.EVENT.LOG — Table Schema

> Source: `INSERTS/I_F.SY.EVENT.LOG` in `SY_Event.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.EL.EVENT.DEFINITION` | `SyEventLog_EventDefinition` | TField |  | Holds the valid ID of SY.EVENT.DEFINITION record. This is a NOINPUT field. |
| 2 | `SY.EL.TRANSACTION` | `SyEventLog_Transaction` | TField |  | Holds the valid ID of SY.TRANSACTION. This is a NOINPUT field. |
| 3 | `SY.EL.INSTANCE` | `SyEventLog_Instance` | TField |  | This is a NOINPUT field. |
| 4 | `SY.EL.RESERVED.22` | `SyEventLog_Reserved22` | TField |  |  |
| 5 | `SY.EL.SHORT.NAME` | `SyEventLog_ShortName` |  |  |  |
| 6 | `SY.EL.DESCRIPTION` | `SyEventLog_Description` |  |  |  |
| 7 | `SY.EL.RESERVED.21` | `SyEventLog_Reserved21` | TField |  |  |
| 8 | `SY.EL.RESERVED.20` | `SyEventLog_Reserved20` | TField |  |  |
| 9 | `SY.EL.RESERVED.19` | `SyEventLog_Reserved19` | TField |  |  |
| 10 | `SY.EL.TRACKING` | `SyEventLog_Tracking` | TField |  | Defines if this event is tracking or non-tracking. |
| 11 | `SY.EL.EVENT.TYPE` | `SyEventLog_EventType` | TField | Conditional | This classifies the type of event. Some event types relate directly to a T24 function being applied to the Structured Product: Input Authorise Delete Reverse Scheduled - To be actioned on a predetermined date) Rolling - To be repeated at predetermined intervals) Add-Hoc - This will be triggered manually The event type chosen determines which additional fields are required: For Scheduled events, one of DATE or DATE.RULES must be entered with COB.PHASE optional. For Rolling events, FREQUENCY and COB.PHASE are mandatory and DATE.RULES is optional. For the other events these fields must not be used. |
| 12 | `SY.EL.ALLOW.RERUN` | `SyEventLog_AllowRerun` | TField |  | Is the user able to re-run an event after it has been run (successfully) at least once. |
| 13 | `SY.EL.RESERVED.18` | `SyEventLog_Reserved18` | TField |  |  |
| 14 | `SY.EL.RESERVED.17` | `SyEventLog_Reserved17` | TField |  |  |
| 15 | `SY.EL.RESERVED.16` | `SyEventLog_Reserved16` | TField |  |  |
| 16 | `SY.EL.DATE` | `SyEventLog_Date` | TField |  | This is the date on which an event will be processed. |
| 17 | `SY.EL.DATE.RULES` | `SyEventLog_DateRules` | TField |  | This defines the date rules for and event, defining the date in terms of the process date. T24 uses a range of keywords, codes and modifiers to represent the exchange rules when determining the dates. . Keyword Meaning Comments MO Monday TU Tuesday WE Wednesday TH Thursday FR Friday SA Saturday SU Sunday M Month Only valid with multiplier/operator in same field W Week Only valid with multiplier/operator in same field CD Calendar days Only valid with multiplier/operator in same field BD Business days Only valid with multiplier/operator in same field LBD Last business day of the month Not valid with multiplier/operator in same field LCD Last calendar day of the month Not valid with multiplier/operator in same field FBD First business day of the month Not valid with multiplier/operator in same field FCD First calendar day of the month Not valid with multiplier/operator in same field MF* Move forward. If the date obtained is not a business day, the move forward until a business date is found. MB* Move backward If the date obtained is not a business day, then move backwards until a business date is found. CAL* Calendar Date Return the date obtained, . Operators and multipliers can then be applied to any of the above "keywords", subject to the rules shown in the table. For example, +3BD indicates add 3 business days. Some keywords are only valid in the presence of operators or multipliers. It makes no sense to put the keyword 'BD' into a field since it is only useful when describing a date offset, i.e. +3BD or -2BD. Conversely, keywords such as FBD and LCD describe fixed points in a month and are meaningless when combined with operators or multipliers. It is important to note that the scenario the first business day in the month 2 months forward is represented by +2M,FBD and not +2FBD. |
| 18 | `SY.EL.FREQUENCY` | `SyEventLog_Frequency` | TField |  | Defines the frequency of a rolling event. |
| 19 | `SY.EL.INCLUDE.FIRST.DATE` | `SyEventLog_IncludeFirstDate` | TField |  | This flag indicates that a rolling event was first processed on the CREATE.DATE. |
| 20 | `SY.EL.RESERVED.15` | `SyEventLog_Reserved15` | TField |  |  |
| 21 | `SY.EL.RESERVED.14` | `SyEventLog_Reserved14` | TField |  |  |
| 22 | `SY.EL.RESERVED.13` | `SyEventLog_Reserved13` | TField |  |  |
| 23 | `SY.EL.TERMINATOR.CASE` | `SyEventLog_TerminatorCase` | TField |  | Defines if this event is the last event in a products lifecylcle. Once this event is processed no further events can be processed for the deal. |
| 24 | `SY.EL.COB.PHASE` | `SyEventLog_CobPhase` | TField |  | For Scheduled and/or rolling events the Close of buiness processing will be invoked. This defined when during the COB the event will be processed. If set to 'Close of Business', event will be processed before system date change. If set to 'Start of Day', event will be processed after system date change. If set to 'Online', event will be processed after system date change during ONLINE phase. |
| 25 | `SY.EL.NOTES` | `SyEventLog_Notes` |  |  |  |
| 26 | `SY.EL.RESERVED.12` | `SyEventLog_Reserved12` | TField |  |  |
| 27 | `SY.EL.RESERVED.11` | `SyEventLog_Reserved11` | TField |  |  |
| 28 | `SY.EL.RESERVED.10` | `SyEventLog_Reserved10` | TField |  |  |
| 29 | `SY.EL.PROCESS` | `SyEventLog_Process` | TField |  | Used to manually trigger event processing. |
| 30 | `SY.EL.CREATE.DATE` | `SyEventLog_CreateDate` | TField |  | This is the date that the event was created. |
| 31 | `SY.EL.LAST.RUN.DATE` | `SyEventLog_LastRunDate` | TField |  | The last run date for the event. |
| 32 | `SY.EL.LOG.ID` | `SyEventLog_LogId` |  |  |  |
| 33 | `SY.EL.TERMINATED` | `SyEventLog_Terminated` | TField |  | Indicates that the event has been terminated. |
| 34 | `SY.EL.RESERVED.9` | `SyEventLog_Reserved9` | TField |  |  |
| 35 | `SY.EL.RESERVED.8` | `SyEventLog_Reserved8` | TField |  |  |
| 36 | `SY.EL.RESERVED.7` | `SyEventLog_Reserved7` | TField |  |  |
| 37 | `SY.EL.ACTIVITY.CODE` | `SyEventLog_ActivityCode` |  |  |  |
| 38 | `SY.EL.RESERVED.62` | `SyEventLog_Reserved62` |  |  |  |
| 39 | `SY.EL.RESERVED.61` | `SyEventLog_Reserved61` |  |  |  |
| 40 | `SY.EL.MESSAGE.REF` | `SyEventLog_MessageRef` |  |  |  |
| 41 | `SY.EL.RESERVED.6` | `SyEventLog_Reserved6` | TField |  |  |
| 42 | `SY.EL.RESERVED.5` | `SyEventLog_Reserved5` | TField |  |  |
| 43 | `SY.EL.RESERVED.4` | `SyEventLog_Reserved4` | TField |  |  |
| 44 | `SY.EL.CLEAR.UP` | `SyEventLog_ClearUp` | TField |  | For System use only - Not Inputtable by users. Defines if a background cleanup is required. |
| 45 | `SY.EL.CRITICAL` | `SyEventLog_Critical` | TField |  | Defines if this event is critical in the products lifecycle and will prevent the user from reversing the deal. Not used in this application. |
| 46 | `SY.EL.NO.CHANGE` | `SyEventLog_NoChange` | TField |  | Defines if this event should block the ammendment of the deal. Not used in this application. |
| 47 | `SY.EL.RESERVED.3` | `SyEventLog_Reserved3` | TField |  |  |
| 48 | `SY.EL.RESERVED.2` | `SyEventLog_Reserved2` | TField |  |  |
| 49 | `SY.EL.RESERVED.1` | `SyEventLog_Reserved1` | TField |  |  |
| 50 | `SY.EL.INTERNAL.USE` | `SyEventLog_InternalUse` | TField |  | Not used in SY.EVENT.LOG. This field is for internal use only. |
| 51 | `SY.EL.LOCAL.REF` | `SyEventLog_LocalRef` |  |  |  |
| 52 | `SY.EL.OVERRIDE` | `SyEventLog_Override` |  |  |  |
