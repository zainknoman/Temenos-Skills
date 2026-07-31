# CHANNEL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CHANNEL.PARAMETER` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CPR.EXT.CACHE.EXPIRY` | `ChannelParameter_ExtCacheExpiry` | TField |  | This field specifies the time interval (in number of seconds) between the cache file refreshes. |
| 2 | `CPR.OFS.SOURCE` | `ChannelParameter_OfsSource` |  |  |  |
| 3 | `CPR.ENABLE.CACHE` | `ChannelParameter_EnableCache` |  |  |  |
| 4 | `CPR.APP.NAME` | `ChannelParameter_AppName` |  |  |  |
| 5 | `CPR.VERSION.NAME` | `ChannelParameter_VersionName` |  |  |  |
| 6 | `CPR.FUNCTION` | `ChannelParameter_Function` |  |  |  |
| 7 | `CPR.RESERVED.08` | `ChannelParameter_Reserved08` |  |  |  |
| 8 | `CPR.RESERVED.07` | `ChannelParameter_Reserved07` |  |  |  |
| 9 | `CPR.ENQUIRY.CACHE` | `ChannelParameter_EnquiryCache` |  |  |  |
| 10 | `CPR.DELETE.EEU.RECORD` | `ChannelParameter_DeleteEeuRecord` | TField |  | YES - Delete external user record from third party server. |
| 11 | `CPR.RELATION.TYPE` | `ChannelParameter_RelationType` |  |  |  |
| 12 | `CPR.RELATION.CODE` | `ChannelParameter_RelationCode` |  |  |  |
| 13 | `CPR.RELATION.PERMISSION` | `ChannelParameter_RelationPermission` |  |  |  |
| 14 | `CPR.PRIVILEGES.CHECK` | `ChannelParameter_PrivilegesCheck` | TField |  |  |
| 15 | `CPR.GENERIC.USER.SMS.GROUP` | `ChannelParameter_GenericUserSmsGroup` | TField |  |  |
| 16 | `CPR.EXT.USER.SECTOR` | `ChannelParameter_GenericUserSmsGroup` | TField |  |  |
| 17 | `CPR.EEU.PURGE.DAYS` | `ChannelParameter_GenericUserSmsGroup` | TField |  |  |
| 18 | `CPR.RECORD.STATUS` | `ChannelParameter_RecordStatus` | String |  |  |
| 19 | `CPR.CURR.NO` | `ChannelParameter_CurrNo` | String |  |  |
| 20 | `CPR.INPUTTER` | `ChannelParameter_Inputter` |  |  |  |
| 21 | `CPR.DATE.TIME` | `ChannelParameter_DateTime` |  |  |  |
| 22 | `CPR.AUTHORISER` | `ChannelParameter_Authoriser` | String |  |  |
| 23 | `CPR.CO.CODE` | `ChannelParameter_CoCode` | String |  |  |
| 24 | `CPR.DEPT.CODE` | `ChannelParameter_DeptCode` | String |  |  |
| 25 | `CPR.AUDITOR.CODE` | `ChannelParameter_AuditorCode` | String |  |  |
| 26 | `CPR.AUDIT.DATE.TIME` | `ChannelParameter_AuditDateTime` | String |  |  |
