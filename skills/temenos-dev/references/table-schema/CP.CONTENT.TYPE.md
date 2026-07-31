# CP.CONTENT.TYPE — Table Schema

> Source: `INSERTS/I_F.CP.CONTENT.TYPE` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CT.CONTENT.TYPE.NAME` | `CpContentType_ContentTypeName` | TField |  | This field stores the name of the content type to be defined (E.g. : "Image", "Video", Facebook App", etc.) |
| 2 | `CP.CT.CONTENT.TYPE.DSCR` | `CpContentType_ContentTypeDscr` |  |  |  |
| 3 | `CP.CT.PROJECT.NAME` | `CpContentType_ProjectName` | TField |  | This field stores the name of the UXP project. |
| 4 | `CP.CT.HAS.GLOBAL.OPTIONS` | `CpContentType_HasGlobalOptions` | TField |  | This field stores whether options at content type level are required Y/N. |
| 5 | `CP.CT.GLOBAL.DATA` | `CpContentType_GlobalData` |  |  |  |
| 6 | `CP.CT.HAS.CHNL.OUT.OPT` | `CpContentType_HasChnlOutOpt` | TField |  | This field steores whether options at location level are required Y/N. |
| 7 | `CP.CT.HAS.CPG.OPTIONS` | `CpContentType_HasCpgOptions` | TField |  | This field stores whether options at campaign level (or re-usable resource level) are required Y/N. |
| 8 | `CP.CT.HAS.VIEW.ACTION` | `CpContentType_HasViewAction` | TField |  | This field stores whether an action/callback is required on view Y/N. |
| 9 | `CP.CT.HAS.CLICK.ACTION` | `CpContentType_HasClickAction` | TField |  | This field stores whether an action/callback is required on click Y/N. |
| 10 | `CP.CT.STATUS` | `CpContentType_Status` | TField |  | This field stores the status for the record so we can choose when to make the "Content Type" available in the Campaign Management User Agent Interface. |
| 11 | `CP.CT.ALLOW.CLICK.URL` | `CpContentType_AllowClickUrl` | TField |  | This field stores whether we allow the Inputter to add a click URL (Q gets displayed in UA for Campaigns if flag is Y). |
| 12 | `CP.CT.ORIGINAL.ID` | `CpContentType_OriginalId` | TField |  | The solution allows versioning for ContentType.For every version of a ContentType we need to store the ID of the original one.This field stores the original ID of a ContentType. |
| 13 | `CP.CT.LAST.UPDATE` | `CpContentType_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 14 | `CP.CT.IS.VISIBLE` | `CpContentType_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a ContentType can be used for new campaigns. |
| 15 | `CP.CT.OWNER` | `CpContentType_Owner` | TField |  | The user who defines the ContentType Links to the ID of USER table |
| 16 | `CP.CT.SUSPEND.REASON.ID` | `CpContentType_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 17 | `CP.CT.METADATA.NAME` | `CpContentType_MetadataName` |  |  |  |
| 18 | `CP.CT.METADATA.ID` | `CpContentType_MetadataId` |  |  |  |
| 19 | `CP.CT.WORKFLOW.ID` | `CpContentType_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 20 | `CP.CT.RESERVED.29` | `CpContentType_Reserved29` | TField |  |  |
| 21 | `CP.CT.RESERVED.28` | `CpContentType_Reserved28` | TField |  |  |
| 22 | `CP.CT.RESERVED.27` | `CpContentType_Reserved27` | TField |  |  |
| 23 | `CP.CT.RESERVED.26` | `CpContentType_Reserved26` | TField |  |  |
| 24 | `CP.CT.RESERVED.25` | `CpContentType_Reserved25` | TField |  |  |
| 25 | `CP.CT.RESERVED.24` | `CpContentType_Reserved24` | TField |  |  |
| 26 | `CP.CT.RESERVED.23` | `CpContentType_Reserved23` | TField |  |  |
| 27 | `CP.CT.RESERVED.22` | `CpContentType_Reserved22` | TField |  |  |
| 28 | `CP.CT.RESERVED.21` | `CpContentType_Reserved21` | TField |  |  |
| 29 | `CP.CT.RESERVED.20` | `CpContentType_Reserved20` | TField |  |  |
| 30 | `CP.CT.RESERVED.19` | `CpContentType_Reserved19` | TField |  |  |
| 31 | `CP.CT.RESERVED.18` | `CpContentType_Reserved18` | TField |  |  |
| 32 | `CP.CT.RESERVED.17` | `CpContentType_Reserved17` | TField |  |  |
| 33 | `CP.CT.RESERVED.16` | `CpContentType_Reserved16` | TField |  |  |
| 34 | `CP.CT.RESERVED.15` | `CpContentType_Reserved15` | TField |  |  |
| 35 | `CP.CT.RESERVED.14` | `CpContentType_Reserved14` | TField |  |  |
| 36 | `CP.CT.RESERVED.13` | `CpContentType_Reserved13` | TField |  |  |
| 37 | `CP.CT.RESERVED.12` | `CpContentType_Reserved12` | TField |  |  |
| 38 | `CP.CT.RESERVED.11` | `CpContentType_Reserved11` | TField |  |  |
| 39 | `CP.CT.RESERVED.10` | `CpContentType_Reserved10` | TField |  |  |
| 40 | `CP.CT.RESERVED.9` | `CpContentType_Reserved9` | TField |  |  |
| 41 | `CP.CT.RESERVED.8` | `CpContentType_Reserved8` | TField |  |  |
| 42 | `CP.CT.RESERVED.7` | `CpContentType_Reserved7` | TField |  |  |
| 43 | `CP.CT.RESERVED.6` | `CpContentType_Reserved6` | TField |  |  |
| 44 | `CP.CT.RESERVED.5` | `CpContentType_Reserved5` | TField |  |  |
| 45 | `CP.CT.RESERVED.4` | `CpContentType_Reserved4` | TField |  |  |
| 46 | `CP.CT.RESERVED.3` | `CpContentType_Reserved3` | TField |  |  |
| 47 | `CP.CT.RESERVED.2` | `CpContentType_Reserved2` | TField |  |  |
| 48 | `CP.CT.RESERVED.1` | `CpContentType_Reserved1` | TField |  |  |
| 49 | `CP.CT.LOCAL.REF` | `CpContentType_LocalRef` |  |  |  |
| 50 | `CP.CT.OVERRIDE` | `CpContentType_Override` |  |  |  |
| 51 | `CP.CT.RECORD.STATUS` | `CpContentType_RecordStatus` | String |  |  |
| 52 | `CP.CT.CURR.NO` | `CpContentType_CurrNo` | String |  |  |
| 53 | `CP.CT.INPUTTER` | `CpContentType_Inputter` |  |  |  |
| 54 | `CP.CT.DATE.TIME` | `CpContentType_DateTime` |  |  |  |
| 55 | `CP.CT.AUTHORISER` | `CpContentType_Authoriser` | String |  |  |
| 56 | `CP.CT.CO.CODE` | `CpContentType_CoCode` | String |  |  |
| 57 | `CP.CT.DEPT.CODE` | `CpContentType_DeptCode` | String |  |  |
| 58 | `CP.CT.AUDITOR.CODE` | `CpContentType_AuditorCode` | String |  |  |
| 59 | `CP.CT.AUDIT.DATE.TIME` | `CpContentType_AuditDateTime` | String |  |  |
