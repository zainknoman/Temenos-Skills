# CP.CHANNEL.TRIGGER — Table Schema

> Source: `INSERTS/I_F.CP.CHANNEL.TRIGGER` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CH.TG.NAME` | `CpChannelTrigger_Name` | TField |  | This field stores the name of the channel trigger. |
| 2 | `CP.CH.TG.DESCRIPTION` | `CpChannelTrigger_Description` |  |  |  |
| 3 | `CP.CH.TG.CHANNEL.ID` | `CpChannelTrigger_ChannelId` | TField |  | This field stores the ID of the channel where the event associated with the channel trigger might occur. This field links CP.CHANNEL.TRGGER table to the CP.CHANNEL one. |
| 4 | `CP.CH.TG.TRIGGER.TYPE` | `CpChannelTrigger_TriggerType` | TField |  | This field stores the event associated with the trigger. The event is an action taken by the customer in the given channel which triggers the Campaign which contains the given trigger in its� definition. |
| 5 | `CP.CH.TG.PROJECT.IDENTIFIER` | `CpChannelTrigger_ProjectIdentifier` | TField |  | This field stores the ID of the component from an UXP project, entered manually by the admin user in Campaign Administration User Agent Interface. (e.g. the Log in button ID) Apply for online channels only. |
| 6 | `CP.CH.TG.EVENT.DATA` | `CpChannelTrigger_EventData` |  |  |  |
| 7 | `CP.CH.TG.STATUS.CODE` | `CpChannelTrigger_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 8 | `CP.CH.TG.ORIGINAL.ID` | `CpChannelTrigger_OriginalId` | TField |  | The solution allows versioning for channel trigger.For every version of a channel trigger we need to store the ID of the original one.This field stores the original ID of a channel trigger. |
| 9 | `CP.CH.TG.LAST.UPDATE` | `CpChannelTrigger_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 10 | `CP.CH.TG.IS.VISIBLE` | `CpChannelTrigger_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a channel trigger can be used for new campaigns. |
| 11 | `CP.CH.TG.OWNER` | `CpChannelTrigger_Owner` | TField |  | The user who defines the channel trigger Links to the ID of USER table |
| 12 | `CP.CH.TG.SUSPEND.REASON.ID` | `CpChannelTrigger_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 13 | `CP.CH.TG.WORKFLOW.ID` | `CpChannelTrigger_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 14 | `CP.CH.TG.CUSTOMER.SOURCE` | `CpChannelTrigger_CustomerSource` | TField |  | This field stores the source where a customer is registered: Internal (T24) or External (other core banking system) |
| 15 | `CP.CH.TG.RESERVED.28` | `CpChannelTrigger_Reserved28` | TField |  |  |
| 16 | `CP.CH.TG.RESERVED.27` | `CpChannelTrigger_Reserved27` | TField |  |  |
| 17 | `CP.CH.TG.RESERVED.26` | `CpChannelTrigger_Reserved26` | TField |  |  |
| 18 | `CP.CH.TG.RESERVED.25` | `CpChannelTrigger_Reserved25` | TField |  |  |
| 19 | `CP.CH.TG.RESERVED.24` | `CpChannelTrigger_Reserved24` | TField |  |  |
| 20 | `CP.CH.TG.RESERVED.23` | `CpChannelTrigger_Reserved23` | TField |  |  |
| 21 | `CP.CH.TG.RESERVED.22` | `CpChannelTrigger_Reserved22` | TField |  |  |
| 22 | `CP.CH.TG.RESERVED.21` | `CpChannelTrigger_Reserved21` | TField |  |  |
| 23 | `CP.CH.TG.RESERVED.20` | `CpChannelTrigger_Reserved20` | TField |  |  |
| 24 | `CP.CH.TG.RESERVED.19` | `CpChannelTrigger_Reserved19` | TField |  |  |
| 25 | `CP.CH.TG.RESERVED.18` | `CpChannelTrigger_Reserved18` | TField |  |  |
| 26 | `CP.CH.TG.RESERVED.17` | `CpChannelTrigger_Reserved17` | TField |  |  |
| 27 | `CP.CH.TG.RESERVED.16` | `CpChannelTrigger_Reserved16` | TField |  |  |
| 28 | `CP.CH.TG.RESERVED.15` | `CpChannelTrigger_Reserved15` | TField |  |  |
| 29 | `CP.CH.TG.RESERVED.14` | `CpChannelTrigger_Reserved14` | TField |  |  |
| 30 | `CP.CH.TG.RESERVED.13` | `CpChannelTrigger_Reserved13` | TField |  |  |
| 31 | `CP.CH.TG.RESERVED.12` | `CpChannelTrigger_Reserved12` | TField |  |  |
| 32 | `CP.CH.TG.RESERVED.11` | `CpChannelTrigger_Reserved11` | TField |  |  |
| 33 | `CP.CH.TG.RESERVED.10` | `CpChannelTrigger_Reserved10` | TField |  |  |
| 34 | `CP.CH.TG.RESERVED.9` | `CpChannelTrigger_Reserved9` | TField |  |  |
| 35 | `CP.CH.TG.RESERVED.8` | `CpChannelTrigger_Reserved8` | TField |  |  |
| 36 | `CP.CH.TG.RESERVED.7` | `CpChannelTrigger_Reserved7` | TField |  |  |
| 37 | `CP.CH.TG.RESERVED.6` | `CpChannelTrigger_Reserved6` | TField |  |  |
| 38 | `CP.CH.TG.RESERVED.5` | `CpChannelTrigger_Reserved5` | TField |  |  |
| 39 | `CP.CH.TG.RESERVED.4` | `CpChannelTrigger_Reserved4` | TField |  |  |
| 40 | `CP.CH.TG.RESERVED.3` | `CpChannelTrigger_Reserved3` | TField |  |  |
| 41 | `CP.CH.TG.RESERVED.2` | `CpChannelTrigger_Reserved2` | TField |  |  |
| 42 | `CP.CH.TG.RESERVED.1` | `CpChannelTrigger_Reserved1` | TField |  |  |
| 43 | `CP.CH.TG.LOCAL.REF` | `CpChannelTrigger_LocalRef` |  |  |  |
| 44 | `CP.CH.TG.OVERRIDE` | `CpChannelTrigger_Override` |  |  |  |
| 45 | `CP.CH.TG.RECORD.STATUS` | `CpChannelTrigger_RecordStatus` | String |  |  |
| 46 | `CP.CH.TG.CURR.NO` | `CpChannelTrigger_CurrNo` | String |  |  |
| 47 | `CP.CH.TG.INPUTTER` | `CpChannelTrigger_Inputter` |  |  |  |
| 48 | `CP.CH.TG.DATE.TIME` | `CpChannelTrigger_DateTime` |  |  |  |
| 49 | `CP.CH.TG.AUTHORISER` | `CpChannelTrigger_Authoriser` | String |  |  |
| 50 | `CP.CH.TG.CO.CODE` | `CpChannelTrigger_CoCode` | String |  |  |
| 51 | `CP.CH.TG.DEPT.CODE` | `CpChannelTrigger_DeptCode` | String |  |  |
| 52 | `CP.CH.TG.AUDITOR.CODE` | `CpChannelTrigger_AuditorCode` | String |  |  |
| 53 | `CP.CH.TG.AUDIT.DATE.TIME` | `CpChannelTrigger_AuditDateTime` | String |  |  |
