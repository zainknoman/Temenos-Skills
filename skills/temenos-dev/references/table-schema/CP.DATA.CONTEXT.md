# CP.DATA.CONTEXT — Table Schema

> Source: `INSERTS/I_F.CP.DATA.CONTEXT` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.DC.NAME` | `CpDataContext_Name` | TField | Yes | This field stores the name of the data context. Validation Rules :Mandatory field, any 35 characters. |
| 2 | `CP.DC.DESCRIPTION` | `CpDataContext_Description` |  |  |  |
| 3 | `CP.DC.PROJECT.NAME` | `CpDataContext_ProjectName` | TField |  | Each data context has a correspondent .ifp UXP project. This field stores the name of the corresponding UXP project for the given Data Context. Validation Rules :Any 100 characters. |
| 4 | `CP.DC.REQ.CAMPAIGN.DATA` | `CpDataContext_ReqCampaignData` | TField |  | The Campaign Options allows you to specify the data that needs to be added by the Business User. If it is set to yes then the Data Contexts will also be processed based on the data added by the Business User in the Campaign Management User Agent Interface. |
| 5 | `CP.DC.CACHE.POLICY` | `CpDataContext_CachePolicy` | TField |  | This option stores what period of time the data context information should be stored in memory.The drop down list contain the following Data Cache Policies:Cache from the life of the User�s Session: The Data Context is not reset but it would be cleared when the user session ends. Cache during the Campaign Matching: The Data Context is reset after all Campaigns are matched. Cache for just a single Campaign Match: The Data Context is reset after one or more data items are added in one Campaign. |
| 6 | `CP.DC.HAS.GLOBAL.OPTIONS` | `CpDataContext_HasGlobalOptions` | TField |  |  |
| 7 | `CP.DC.GLOBAL.DATA` | `CpDataContext_GlobalData` |  |  |  |
| 8 | `CP.DC.STATUS.CODE` | `CpDataContext_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 9 | `CP.DC.ORIGINAL.ID` | `CpDataContext_OriginalId` | TField |  | The solution allows versioning for DataContextFor every version of a DataContext we need to store the ID of the original one.This field stores the original ID of a DataContext. |
| 10 | `CP.DC.LAST.UPDATE` | `CpDataContext_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 11 | `CP.DC.IS.VISIBLE` | `CpDataContext_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a data context can be used for new campaigns. |
| 12 | `CP.DC.OWNER` | `CpDataContext_Owner` | TField |  | The user who defines the data context. Links to the ID of USER table |
| 13 | `CP.DC.SUSPEND.REASON.ID` | `CpDataContext_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 14 | `CP.DC.METADATA.NAME` | `CpDataContext_MetadataName` |  |  |  |
| 15 | `CP.DC.METADATA.ID` | `CpDataContext_MetadataId` |  |  |  |
| 16 | `CP.DC.WORKFLOW.ID` | `CpDataContext_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 17 | `CP.DC.RESERVED.29` | `CpDataContext_Reserved29` | TField |  |  |
| 18 | `CP.DC.RESERVED.28` | `CpDataContext_Reserved28` | TField |  |  |
| 19 | `CP.DC.RESERVED.27` | `CpDataContext_Reserved27` | TField |  |  |
| 20 | `CP.DC.RESERVED.26` | `CpDataContext_Reserved26` | TField |  |  |
| 21 | `CP.DC.RESERVED.25` | `CpDataContext_Reserved25` | TField |  |  |
| 22 | `CP.DC.RESERVED.24` | `CpDataContext_Reserved24` | TField |  |  |
| 23 | `CP.DC.RESERVED.23` | `CpDataContext_Reserved23` | TField |  |  |
| 24 | `CP.DC.RESERVED.22` | `CpDataContext_Reserved22` | TField |  |  |
| 25 | `CP.DC.RESERVED.21` | `CpDataContext_Reserved21` | TField |  |  |
| 26 | `CP.DC.RESERVED.20` | `CpDataContext_Reserved20` | TField |  |  |
| 27 | `CP.DC.RESERVED.19` | `CpDataContext_Reserved19` | TField |  |  |
| 28 | `CP.DC.RESERVED.18` | `CpDataContext_Reserved18` | TField |  |  |
| 29 | `CP.DC.RESERVED.17` | `CpDataContext_Reserved17` | TField |  |  |
| 30 | `CP.DC.RESERVED.16` | `CpDataContext_Reserved16` | TField |  |  |
| 31 | `CP.DC.RESERVED.15` | `CpDataContext_Reserved15` | TField |  |  |
| 32 | `CP.DC.RESERVED.14` | `CpDataContext_Reserved14` | TField |  |  |
| 33 | `CP.DC.RESERVED.13` | `CpDataContext_Reserved13` | TField |  |  |
| 34 | `CP.DC.RESERVED.12` | `CpDataContext_Reserved12` | TField |  |  |
| 35 | `CP.DC.RESERVED.11` | `CpDataContext_Reserved11` | TField |  |  |
| 36 | `CP.DC.RESERVED.10` | `CpDataContext_Reserved10` | TField |  |  |
| 37 | `CP.DC.RESERVED.9` | `CpDataContext_Reserved9` | TField |  |  |
| 38 | `CP.DC.RESERVED.8` | `CpDataContext_Reserved8` | TField |  |  |
| 39 | `CP.DC.RESERVED.7` | `CpDataContext_Reserved7` | TField |  |  |
| 40 | `CP.DC.RESERVED.6` | `CpDataContext_Reserved6` | TField |  |  |
| 41 | `CP.DC.RESERVED.5` | `CpDataContext_Reserved5` | TField |  |  |
| 42 | `CP.DC.RESERVED.4` | `CpDataContext_Reserved4` | TField |  |  |
| 43 | `CP.DC.RESERVED.3` | `CpDataContext_Reserved3` | TField |  |  |
| 44 | `CP.DC.RESERVED.2` | `CpDataContext_Reserved2` | TField |  |  |
| 45 | `CP.DC.RESERVED.1` | `CpDataContext_Reserved1` | TField |  |  |
| 46 | `CP.DC.LOCAL.REF` | `CpDataContext_LocalRef` |  |  |  |
| 47 | `CP.DC.OVERRIDE` | `CpDataContext_Override` |  |  |  |
| 48 | `CP.DC.RECORD.STATUS` | `CpDataContext_RecordStatus` | String |  |  |
| 49 | `CP.DC.CURR.NO` | `CpDataContext_CurrNo` | String |  |  |
| 50 | `CP.DC.INPUTTER` | `CpDataContext_Inputter` |  |  |  |
| 51 | `CP.DC.DATE.TIME` | `CpDataContext_DateTime` |  |  |  |
| 52 | `CP.DC.AUTHORISER` | `CpDataContext_Authoriser` | String |  |  |
| 53 | `CP.DC.CO.CODE` | `CpDataContext_CoCode` | String |  |  |
| 54 | `CP.DC.DEPT.CODE` | `CpDataContext_DeptCode` | String |  |  |
| 55 | `CP.DC.AUDITOR.CODE` | `CpDataContext_AuditorCode` | String |  |  |
| 56 | `CP.DC.AUDIT.DATE.TIME` | `CpDataContext_AuditDateTime` | String |  |  |
