# CP.CHANNEL.OUTPUT — Table Schema

> Source: `INSERTS/I_F.CP.CHANNEL.OUTPUT` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CH.OUT.NAME` | `CpChannelOutput_Name` | TField |  | This field stores the name of the channel output. |
| 2 | `CP.CH.OUT.DESCRIPTION` | `CpChannelOutput_Description` |  |  |  |
| 3 | `CP.CH.OUT.CHANNEL.ID` | `CpChannelOutput_ChannelId` | TField |  | This field stores the ID of the channel through which the message will be communicated to the customer as part of a marketing campaign. This field links CP.CHANNEL.OUTPUT table to the CP.CHANNEL one. |
| 4 | `CP.CH.OUT.CONTENT.TYPE` | `CpChannelOutput_ContentType` | TField |  | This field stores the type of the content used for the definition of the online template. (E.g. Image, Video, Text, Image with Text, Article, Blog Entry etc). |
| 5 | `CP.CH.OUT.CONTENT.MODE` | `CpChannelOutput_ContentMode` | TField |  | This field stores the value associated with the mode content is displayed to the customer on a channel. E.g. of values stored in this list are: Inject Content into Placeholder, Replace Existing Content, and Display in a Popup. Apply for online channels only. |
| 6 | `CP.CH.OUT.CONTENT.ATTRIBUTES` | `CpChannelOutput_ContentAttributes` | TField |  | This field will store characteristics related to content style. Apply for online channels only. |
| 7 | `CP.CH.OUT.PROJECT.IDENTIFIER` | `CpChannelOutput_ProjectIdentifier` | TField |  | This field stores the name of the component from UXP, entered manually by the admin user in Campaign Administration User Agent Interface. Apply for online channels only. |
| 8 | `CP.CH.OUT.CONTENT.TYPES` | `CpChannelOutput_ContentTypes` |  |  |  |
| 9 | `CP.CH.OUT.CONTENT.TYPE.DATA` | `CpChannelOutput_ContentTypeData` |  |  |  |
| 10 | `CP.CH.OUT.STATUS.CODE` | `CpChannelOutput_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 11 | `CP.CH.OUT.ORIGINAL.ID` | `CpChannelOutput_OriginalId` | TField |  | The solution allows versioning for Channel Output.For every version of a Channel Output we need to store the ID of the original one.This field stores the original ID of a Channel Output. |
| 12 | `CP.CH.OUT.LAST.UPDATE` | `CpChannelOutput_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 13 | `CP.CH.OUT.IS.VISIBLE` | `CpChannelOutput_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a channel output can be used for new campaigns. |
| 14 | `CP.CH.OUT.OWNER` | `CpChannelOutput_Owner` | TField |  | The user who defines the channel output. Links to the ID of USER table. |
| 15 | `CP.CH.OUT.SUSPEND.REASON.ID` | `CpChannelOutput_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 16 | `CP.CH.OUT.METADATA.NAME` | `CpChannelOutput_MetadataName` |  |  |  |
| 17 | `CP.CH.OUT.METADATA.ID` | `CpChannelOutput_MetadataId` |  |  |  |
| 18 | `CP.CH.OUT.ENTITY.BEHIND.METADATA` | `CpChannelOutput_EntityBehindMetadata` |  |  |  |
| 19 | `CP.CH.OUT.ENTITY.ID.BEHIND.METADATA` | `CpChannelOutput_EntityIdBehindMetadata` |  |  |  |
| 20 | `CP.CH.OUT.METADATA.SUSPENDED` | `CpChannelOutput_MetadataSuspended` |  |  |  |
| 21 | `CP.CH.OUT.WORKFLOW.ID` | `CpChannelOutput_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 22 | `CP.CH.OUT.RESERVED.26` | `CpChannelOutput_Reserved26` | TField |  |  |
| 23 | `CP.CH.OUT.RESERVED.25` | `CpChannelOutput_Reserved25` | TField |  |  |
| 24 | `CP.CH.OUT.RESERVED.24` | `CpChannelOutput_Reserved24` | TField |  |  |
| 25 | `CP.CH.OUT.RESERVED.23` | `CpChannelOutput_Reserved23` | TField |  |  |
| 26 | `CP.CH.OUT.RESERVED.22` | `CpChannelOutput_Reserved22` | TField |  |  |
| 27 | `CP.CH.OUT.RESERVED.21` | `CpChannelOutput_Reserved21` | TField |  |  |
| 28 | `CP.CH.OUT.RESERVED.20` | `CpChannelOutput_Reserved20` | TField |  |  |
| 29 | `CP.CH.OUT.RESERVED.19` | `CpChannelOutput_Reserved19` | TField |  |  |
| 30 | `CP.CH.OUT.RESERVED.18` | `CpChannelOutput_Reserved18` | TField |  |  |
| 31 | `CP.CH.OUT.RESERVED.17` | `CpChannelOutput_Reserved17` | TField |  |  |
| 32 | `CP.CH.OUT.RESERVED.16` | `CpChannelOutput_Reserved16` | TField |  |  |
| 33 | `CP.CH.OUT.RESERVED.15` | `CpChannelOutput_Reserved15` | TField |  |  |
| 34 | `CP.CH.OUT.RESERVED.14` | `CpChannelOutput_Reserved14` | TField |  |  |
| 35 | `CP.CH.OUT.RESERVED.13` | `CpChannelOutput_Reserved13` | TField |  |  |
| 36 | `CP.CH.OUT.RESERVED.12` | `CpChannelOutput_Reserved12` | TField |  |  |
| 37 | `CP.CH.OUT.RESERVED.11` | `CpChannelOutput_Reserved11` | TField |  |  |
| 38 | `CP.CH.OUT.RESERVED.10` | `CpChannelOutput_Reserved10` | TField |  |  |
| 39 | `CP.CH.OUT.RESERVED.9` | `CpChannelOutput_Reserved9` | TField |  |  |
| 40 | `CP.CH.OUT.RESERVED.8` | `CpChannelOutput_Reserved8` | TField |  |  |
| 41 | `CP.CH.OUT.RESERVED.7` | `CpChannelOutput_Reserved7` | TField |  |  |
| 42 | `CP.CH.OUT.RESERVED.6` | `CpChannelOutput_Reserved6` | TField |  |  |
| 43 | `CP.CH.OUT.RESERVED.5` | `CpChannelOutput_Reserved5` | TField |  |  |
| 44 | `CP.CH.OUT.RESERVED.4` | `CpChannelOutput_Reserved4` | TField |  |  |
| 45 | `CP.CH.OUT.RESERVED.3` | `CpChannelOutput_Reserved3` | TField |  |  |
| 46 | `CP.CH.OUT.RESERVED.2` | `CpChannelOutput_Reserved2` | TField |  |  |
| 47 | `CP.CH.OUT.RESERVED.1` | `CpChannelOutput_Reserved1` | TField |  |  |
| 48 | `CP.CH.OUT.LOCAL.REF` | `CpChannelOutput_LocalRef` |  |  |  |
| 49 | `CP.CH.OUT.OVERRIDE` | `CpChannelOutput_Override` |  |  |  |
| 50 | `CP.CH.OUT.RECORD.STATUS` | `CpChannelOutput_RecordStatus` | String |  |  |
| 51 | `CP.CH.OUT.CURR.NO` | `CpChannelOutput_CurrNo` | String |  |  |
| 52 | `CP.CH.OUT.INPUTTER` | `CpChannelOutput_Inputter` |  |  |  |
| 53 | `CP.CH.OUT.DATE.TIME` | `CpChannelOutput_DateTime` |  |  |  |
| 54 | `CP.CH.OUT.AUTHORISER` | `CpChannelOutput_Authoriser` | String |  |  |
| 55 | `CP.CH.OUT.CO.CODE` | `CpChannelOutput_CoCode` | String |  |  |
| 56 | `CP.CH.OUT.DEPT.CODE` | `CpChannelOutput_DeptCode` | String |  |  |
| 57 | `CP.CH.OUT.AUDITOR.CODE` | `CpChannelOutput_AuditorCode` | String |  |  |
| 58 | `CP.CH.OUT.AUDIT.DATE.TIME` | `CpChannelOutput_AuditDateTime` | String |  |  |
