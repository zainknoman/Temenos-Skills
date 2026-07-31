# CP.CHANNEL — Table Schema

> Source: `INSERTS/I_F.CP.CHANNEL` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CH.NAME` | `CpChannel_Name` | TField |  | This field stores the name of the defined channel |
| 2 | `CP.CH.DESCRIPTION` | `CpChannel_Description` |  |  |  |
| 3 | `CP.CH.PROJECT.NAME` | `CpChannel_ProjectName` | TField |  | This field stores the name of the corresponding project from UXP for the respective channel. Each channel will have a correspondent project in UXP. Channel Project Name represents the name of the project from UXP, entered manually by the admin user in the Campaign Administration User Agent Interface. Apply for both online and offline channels. |
| 4 | `CP.CH.TYPE` | `CpChannel_Type` | TField |  | This stores the type of the defined channel. This will be a predefined list of channel types. The Admin role will create the list and be able to pick one of the values from the list to define the type of the Channel. The values contained by the list are: ONLINE, OFFLINE |
| 5 | `CP.CH.HAS.CAMPAIGN.OPT` | `CpChannel_HasCampaignOpt` | TField |  | This field stores if the channel should display to the Marketing User Role the channel Configurable Options when defining a campaign. This will be a predefined yes/no list. The Admin role will be able to pick one of the values from the list to further display the channel options. If value "yes" is chosen, the Marketing User will have displayed, in Channel tab, the fields he must fill in as configurable Options. Apply for offline channels only. |
| 6 | `CP.CH.HAS.GLOBAL.OPTIONS` | `CpChannel_HasGlobalOptions` | TField |  | This field stores if the channel has global option defined. This will be a predefined yes/no list. The Admin role will be able to pick one of the values from the list to further display the channel options in the Campaign Administration User Agent Interface. Option "yes" will display the section "Channel Options". Apply for offline channels only. |
| 7 | `CP.CH.HAS.TEMPLATE.OPT` | `CpChannel_HasTemplateOpt` | TField |  | This field is a Yes/No field which is set by the Admin User and allows the Marketing User to use templates for a given channel, when defining a marketing campaign. |
| 8 | `CP.CH.GLOBAL.DATA` | `CpChannel_GlobalData` |  |  |  |
| 9 | `CP.CH.FRONT.TRIGGER` | `CpChannel_FrontTrigger` |  |  |  |
| 10 | `CP.CH.OUTPUT.CONTENT` | `CpChannel_OutputContent` |  |  |  |
| 11 | `CP.CH.STATUS.CODE` | `CpChannel_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 12 | `CP.CH.ORIGINAL.ID` | `CpChannel_OriginalId` | TField |  | The solution allows versioning for Channel.For every version of a Channel we need to store the ID of the original one.This field stores the original ID of a Channel. |
| 13 | `CP.CH.LAST.UPDATE` | `CpChannel_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 14 | `CP.CH.IS.VISIBLE` | `CpChannel_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a channel can be used for new campaigns. |
| 15 | `CP.CH.OWNER` | `CpChannel_Owner` | TField |  | The user who defines the channel Links to the ID of USER table |
| 16 | `CP.CH.SUSPEND.REASON.ID` | `CpChannel_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 17 | `CP.CH.METADATA.NAME` | `CpChannel_MetadataName` |  |  |  |
| 18 | `CP.CH.METADATA.ID` | `CpChannel_MetadataId` |  |  |  |
| 19 | `CP.CH.WORKFLOW.ID` | `CpChannel_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 20 | `CP.CH.ALLOW.CLICK.URL` | `CpChannel_AllowClickUrl` | TField |  | Allow URL |
| 21 | `CP.CH.LOG.CR.CONTACT` | `CpChannel_LogCrContact` | TField |  | Y - the opportunities triggered for customers thru this channel, will be also logged in CR.CONTACT.LOGotherwise - there will be no logging in CR.CONTACT.LOG |
| 22 | `CP.CH.EB.CHANNEL.ID` | `CpChannel_EbChannelId` | TField |  | The corresponding id from EB.CHANNEL |
| 23 | `CP.CH.RESERVED.26` | `CpChannel_Reserved26` | TField |  |  |
| 24 | `CP.CH.RESERVED.25` | `CpChannel_Reserved25` | TField |  |  |
| 25 | `CP.CH.RESERVED.24` | `CpChannel_Reserved24` | TField |  |  |
| 26 | `CP.CH.RESERVED.23` | `CpChannel_Reserved23` | TField |  |  |
| 27 | `CP.CH.RESERVED.22` | `CpChannel_Reserved22` | TField |  |  |
| 28 | `CP.CH.RESERVED.21` | `CpChannel_Reserved21` | TField |  |  |
| 29 | `CP.CH.RESERVED.20` | `CpChannel_Reserved20` | TField |  |  |
| 30 | `CP.CH.RESERVED.19` | `CpChannel_Reserved19` | TField |  |  |
| 31 | `CP.CH.RESERVED.18` | `CpChannel_Reserved18` | TField |  |  |
| 32 | `CP.CH.RESERVED.17` | `CpChannel_Reserved17` | TField |  |  |
| 33 | `CP.CH.RESERVED.16` | `CpChannel_Reserved16` | TField |  |  |
| 34 | `CP.CH.RESERVED.15` | `CpChannel_Reserved15` | TField |  |  |
| 35 | `CP.CH.RESERVED.14` | `CpChannel_Reserved14` | TField |  |  |
| 36 | `CP.CH.RESERVED.13` | `CpChannel_Reserved13` | TField |  |  |
| 37 | `CP.CH.RESERVED.12` | `CpChannel_Reserved12` | TField |  |  |
| 38 | `CP.CH.RESERVED.11` | `CpChannel_Reserved11` | TField |  |  |
| 39 | `CP.CH.RESERVED.10` | `CpChannel_Reserved10` | TField |  |  |
| 40 | `CP.CH.RESERVED.9` | `CpChannel_Reserved9` | TField |  |  |
| 41 | `CP.CH.RESERVED.8` | `CpChannel_Reserved8` | TField |  |  |
| 42 | `CP.CH.RESERVED.7` | `CpChannel_Reserved7` | TField |  |  |
| 43 | `CP.CH.RESERVED.6` | `CpChannel_Reserved6` | TField |  |  |
| 44 | `CP.CH.RESERVED.5` | `CpChannel_Reserved5` | TField |  |  |
| 45 | `CP.CH.RESERVED.4` | `CpChannel_Reserved4` | TField |  |  |
| 46 | `CP.CH.RESERVED.3` | `CpChannel_Reserved3` | TField |  |  |
| 47 | `CP.CH.RESERVED.2` | `CpChannel_Reserved2` | TField |  |  |
| 48 | `CP.CH.RESERVED.1` | `CpChannel_Reserved1` | TField |  |  |
| 49 | `CP.CH.LOCAL.REF` | `CpChannel_LocalRef` |  |  |  |
| 50 | `CP.CH.OVERRIDE` | `CpChannel_Override` |  |  |  |
| 51 | `CP.CH.RECORD.STATUS` | `CpChannel_RecordStatus` | String |  |  |
| 52 | `CP.CH.CURR.NO` | `CpChannel_CurrNo` | String |  |  |
| 53 | `CP.CH.INPUTTER` | `CpChannel_Inputter` |  |  |  |
| 54 | `CP.CH.DATE.TIME` | `CpChannel_DateTime` |  |  |  |
| 55 | `CP.CH.AUTHORISER` | `CpChannel_Authoriser` | String |  |  |
| 56 | `CP.CH.CO.CODE` | `CpChannel_CoCode` | String |  |  |
| 57 | `CP.CH.DEPT.CODE` | `CpChannel_DeptCode` | String |  |  |
| 58 | `CP.CH.AUDITOR.CODE` | `CpChannel_AuditorCode` | String |  |  |
| 59 | `CP.CH.AUDIT.DATE.TIME` | `CpChannel_AuditDateTime` | String |  |  |
