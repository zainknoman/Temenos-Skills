# SY.EVENT.DEFINITION — Table Schema

> Source: `INSERTS/I_F.SY.EVENT.DEFINITION` in `SY_Event.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.ED.EVENT.DEFINITION` | `SyEventDefinition_EventDefinition` | TField |  | This is a link to event definition for this event. This will be the same as the ID |
| 2 | `SY.ED.TRANSACTION` | `SyEventDefinition_Transaction` | TField |  | Not used in this application. Used in SY.EVENT &amp; SY.EVENT.LOG only. |
| 3 | `SY.ED.INSTANCE` | `SyEventDefinition_Instance` | TField |  | Not used in this application. Used in SY.EVENT.LOG only. |
| 4 | `SY.ED.RESERVED.22` | `SyEventDefinition_Reserved22` | TField |  |  |
| 5 | `SY.ED.SHORT.NAME` | `SyEventDefinition_ShortName` |  |  |  |
| 6 | `SY.ED.DESCRIPTION` | `SyEventDefinition_Description` |  |  |  |
| 7 | `SY.ED.RESERVED.21` | `SyEventDefinition_Reserved21` | TField |  |  |
| 8 | `SY.ED.RESERVED.20` | `SyEventDefinition_Reserved20` | TField |  |  |
| 9 | `SY.ED.RESERVED.19` | `SyEventDefinition_Reserved19` | TField |  |  |
| 10 | `SY.ED.TRACKING` | `SyEventDefinition_Tracking` | TField |  | Defines if this event definition is tracking or non-tracking. Tracking events always refer to the definition on the event definition table. Any changes made to the event definition will affect all deals in the system. |
| 11 | `SY.ED.EVENT.TYPE` | `SyEventDefinition_EventType` | TField | Conditional | This classifies the type of event. Some event types relate directly to a T24 function being applied to the Structured Product: Input Authorise Delete Reverse Scheduled - To be actioned on a predetermined date) Rolling - To be repeated at predetermined intervals) Add-Hoc - This will be triggered manually The event type chosen determines which additional fields are required: For Scheduled events, one of DATE or DATE.RULES must be entered with COB.PHASE optional. For Rolling events, FREQUENCY and COB.PHASE are mandatory and DATE.RULES is optional. For the other events these fields must not be used. |
| 12 | `SY.ED.ALLOW.RERUN` | `SyEventDefinition_AllowRerun` | TField |  | Is the user able to re-run an event after it has been run (succesully) at least once. |
| 13 | `SY.ED.RESERVED.18` | `SyEventDefinition_Reserved18` | TField |  |  |
| 14 | `SY.ED.RESERVED.17` | `SyEventDefinition_Reserved17` | TField |  |  |
| 15 | `SY.ED.RESERVED.16` | `SyEventDefinition_Reserved16` | TField |  |  |
| 16 | `SY.ED.DATE` | `SyEventDefinition_Date` | TField |  | This is the date on which an event will be processed. |
| 17 | `SY.ED.DATE.RULES` | `SyEventDefinition_DateRules` | TField |  | This defines the date rules for and event, defining the date in terms of the process date. T24 uses a range of keywords, codes and modifiers to represent the exchange rules when determining the dates. . Keyword Meaning Comments MO Monday TU Tuesday WE Wednesday TH Thursday FR Friday SA Saturday SU Sunday M Month Only valid with multiplier/operator in same field W Week Only valid with multiplier/operator in same field CD Calendar days Only valid with multiplier/operator in same field BD Business days Only valid with multiplier/operator in same field LBD Last business day of the month Not valid with multiplier/operator in same field LCD Last calendar day of the month Not valid with multiplier/operator in same field FBD First business day of the month Not valid with multiplier/operator in same field FCD First calendar day of the month Not valid with multiplier/operator in same field MF* Move forward. If the date obtained is not a business day, the move forward until a business date is found. MB* Move backward If the date obtained is not a business day, then move backwards until a business date is found. CAL* Calendar Date Return the date obtained, . Operators and multipliers can then be applied to any of the above �keywords�, subject to the rules shown in the table. For example, +3BD indicates add 3 business days. Some keywords are only valid in the presence of operators or multipliers. It makes no sense to put the keyword �BD� into a field since it is only useful when describing a date offset, i.e. +3BD or �2BD. Conversely, keywords such as FBD and LCD describe fixed points in a month and are meaningless when combined with operators or multipliers. It is important to note that the scenario the first business day in the month 2 months forward� is represented by �+2M,FBD� and not �+2FBD�. . Description Formula Last business day of the delivery month LBD Third Wednesday of the month prior to the delivery month -1M, +3WE The Saturday following the third Friday of the delivery month +3FR, +1SA Ninth business day prior to the twentieth of the delivery month +20CD, -9BD |
| 18 | `SY.ED.FREQUENCY` | `SyEventDefinition_Frequency` | TField |  | Defines the frequency of a rolling event. |
| 19 | `SY.ED.INCLUDE.FIRST.DATE` | `SyEventDefinition_IncludeFirstDate` | TField |  | This field is used for rolling events only. If set to YES, the event will be processed on the CREATE.DATE as well as subsequent dates as per the FREQUENCY field, otherwise the event will be processed on the subsequent dates as per FREQUENCY field only. |
| 20 | `SY.ED.RESERVED.15` | `SyEventDefinition_Reserved15` | TField |  |  |
| 21 | `SY.ED.RESERVED.14` | `SyEventDefinition_Reserved14` | TField |  |  |
| 22 | `SY.ED.RESERVED.13` | `SyEventDefinition_Reserved13` | TField |  |  |
| 23 | `SY.ED.TERMINATOR.CASE` | `SyEventDefinition_TerminatorCase` | TField |  | Defines if this event is the last event in a products lifecylcle. Once this event is processed no further events can be processed for the deal. |
| 24 | `SY.ED.COB.PHASE` | `SyEventDefinition_CobPhase` | TField |  | For Scheduled and/or rolling events the Close of buiness processing will be invoked. This defined when during the COB the event will be processed. If set to 'Close of Business', event will be processed before system date change. If set to 'Start of Day', event will be processed after system date change. If set to 'Online', event will be processed after system date change during ONLINE phase. |
| 25 | `SY.ED.NOTES` | `SyEventDefinition_Notes` |  |  |  |
| 26 | `SY.ED.RESERVED.12` | `SyEventDefinition_Reserved12` | TField |  |  |
| 27 | `SY.ED.RESERVED.11` | `SyEventDefinition_Reserved11` | TField |  |  |
| 28 | `SY.ED.RESERVED.10` | `SyEventDefinition_Reserved10` | TField |  |  |
| 29 | `SY.ED.PROCESS` | `SyEventDefinition_Process` | TField |  | Not used in this application. Used in SY.EVENT &amp; SY.EVENT.LOG only. |
| 30 | `SY.ED.CREATE.DATE` | `SyEventDefinition_CreateDate` | TField |  | System-generated field only. Used in SY.EVENT &amp; SY.EVENT.LOG only. |
| 31 | `SY.ED.LAST.RUN.DATE` | `SyEventDefinition_LastRunDate` | TField |  | System-generated field only. Used in SY.EVENT &amp; SY.EVENT.LOG only. |
| 32 | `SY.ED.LOG.ID` | `SyEventDefinition_LogId` |  |  |  |
| 33 | `SY.ED.TERMINATED` | `SyEventDefinition_Terminated` | TField |  | Not used in this application. Used in SY.EVENT &amp; SY.EVENT.LOG only. |
| 34 | `SY.ED.RESERVED.9` | `SyEventDefinition_Reserved9` | TField |  |  |
| 35 | `SY.ED.RESERVED.8` | `SyEventDefinition_Reserved8` | TField |  |  |
| 36 | `SY.ED.RESERVED.7` | `SyEventDefinition_Reserved7` | TField |  |  |
| 37 | `SY.ED.ACTIVITY.CODE` | `SyEventDefinition_ActivityCode` |  |  |  |
| 38 | `SY.ED.RESERVED.62` | `SyEventDefinition_Reserved62` |  |  |  |
| 39 | `SY.ED.RESERVED.61` | `SyEventDefinition_Reserved61` |  |  |  |
| 40 | `SY.ED.MESSAGE.REF` | `SyEventDefinition_MessageRef` |  |  |  |
| 41 | `SY.ED.RESERVED.6` | `SyEventDefinition_Reserved6` | TField |  |  |
| 42 | `SY.ED.RESERVED.5` | `SyEventDefinition_Reserved5` | TField |  |  |
| 43 | `SY.ED.RESERVED.4` | `SyEventDefinition_Reserved4` | TField |  |  |
| 44 | `SY.ED.CLEAR.UP` | `SyEventDefinition_ClearUp` | TField |  | For Internal Use Only. Not Accessible by Users. Triggers a clear-up of the event processing. |
| 45 | `SY.ED.CRITICAL` | `SyEventDefinition_Critical` | TField |  | Reversal of the users deal will not be possible once this event has been triggered. |
| 46 | `SY.ED.NO.CHANGE` | `SyEventDefinition_NoChange` | TField |  | Is input/amendment possible to the users contract once this event has been processed. |
| 47 | `SY.ED.RESERVED.3` | `SyEventDefinition_Reserved3` | TField |  |  |
| 48 | `SY.ED.RESERVED.2` | `SyEventDefinition_Reserved2` | TField |  |  |
| 49 | `SY.ED.RESERVED.1` | `SyEventDefinition_Reserved1` | TField |  |  |
| 50 | `SY.ED.INTERNAL.USE` | `SyEventDefinition_InternalUse` | TField |  | For System use only - Not Inputtable by users. |
| 51 | `SY.ED.LOCAL.REF` | `SyEventDefinition_LocalRef` |  |  |  |
| 52 | `SY.ED.OVERRIDE` | `SyEventDefinition_Override` |  |  |  |
| 53 | `SY.ED.RECORD.STATUS` | `SyEventDefinition_RecordStatus` | String |  |  |
| 54 | `SY.ED.CURR.NO` | `SyEventDefinition_CurrNo` | String |  |  |
| 55 | `SY.ED.INPUTTER` | `SyEventDefinition_Inputter` |  |  |  |
| 56 | `SY.ED.DATE.TIME` | `SyEventDefinition_DateTime` |  |  |  |
| 57 | `SY.ED.AUTHORISER` | `SyEventDefinition_Authoriser` | String |  |  |
| 58 | `SY.ED.CO.CODE` | `SyEventDefinition_CoCode` | String |  |  |
| 59 | `SY.ED.DEPT.CODE` | `SyEventDefinition_DeptCode` | String |  |  |
| 60 | `SY.ED.AUDITOR.CODE` | `SyEventDefinition_AuditorCode` | String |  |  |
| 61 | `SY.ED.AUDIT.DATE.TIME` | `SyEventDefinition_AuditDateTime` | String |  |  |
