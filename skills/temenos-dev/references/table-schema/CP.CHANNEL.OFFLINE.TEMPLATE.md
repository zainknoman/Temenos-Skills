# CP.CHANNEL.OFFLINE.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.CP.CHANNEL.OFFLINE.TEMPLATE` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CH.OF.NAME` | `CpChannelOfflineTemplate_Name` | TField |  | This field stores the name of the defined offline template. |
| 2 | `CP.CH.OF.DESCRIPTION` | `CpChannelOfflineTemplate_Description` |  |  |  |
| 3 | `CP.CH.OF.CHANNEL.TYPE` | `CpChannelOfflineTemplate_ChannelType` | TField |  | This field stores the ID of the type of the channel on which the message created using the template will be communicated to the customers as part of a marketing campaign. This field links the CP.CHANNEL.OFFLINE.TEMPLATE table to the CP.CHANNEL one. |
| 4 | `CP.CH.OF.CONTEXT` | `CpChannelOfflineTemplate_Context` |  |  |  |
| 5 | `CP.CH.OF.TEMPLATE.DATA` | `CpChannelOfflineTemplate_TemplateData` |  |  |  |
| 6 | `CP.CH.OF.ORIGINAL.ID` | `CpChannelOfflineTemplate_OriginalId` | TField |  | The solution allows versioning of templates. For every version of a template we need to store the ID of the original one. This field stores the original ID of a template. |
| 7 | `CP.CH.OF.EDITABLE` | `CpChannelOfflineTemplate_Editable` | TField |  | Y/N This field indicates whether or not a template can be edited. The versioned templates cannot be edited anymore. |
| 8 | `CP.CH.OF.VERSION` | `CpChannelOfflineTemplate_Version` | TField |  | The solution allows versioning of templates. This field stores the number of the version for a given template. |
| 9 | `CP.CH.OF.VERSION.FLAG` | `CpChannelOfflineTemplate_VersionFlag` | TField |  | [NULL, NWITEM, NWCP] This field store s the 3 values mentioned. NULL- this value is assigned to a template at creation. NWITEM � this value is used when the template is versioned without conditioning the versioning of the campaigns which use the template NWCP - this value is used when the template is versioned and we condition the versioning of the campaigns which use the template |
| 10 | `CP.CH.OF.SUSPEND.REASON.ID` | `CpChannelOfflineTemplate_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 11 | `CP.CH.OF.METADATA.NAME` | `CpChannelOfflineTemplate_MetadataName` |  |  |  |
| 12 | `CP.CH.OF.METADATA.ID` | `CpChannelOfflineTemplate_MetadataId` |  |  |  |
| 13 | `CP.CH.OF.CLICK.URL` | `CpChannelOfflineTemplate_ClickUrl` | TField |  | This field stores the URL a customer is redirected in case s/he decides to click on the content attached to the message which was communicated by the bank as part of marketing campaign |
| 14 | `CP.CH.OF.RESERVED.29` | `CpChannelOfflineTemplate_Reserved29` | TField |  |  |
| 15 | `CP.CH.OF.RESERVED.28` | `CpChannelOfflineTemplate_Reserved28` | TField |  |  |
| 16 | `CP.CH.OF.RESERVED.27` | `CpChannelOfflineTemplate_Reserved27` | TField |  |  |
| 17 | `CP.CH.OF.RESERVED.26` | `CpChannelOfflineTemplate_Reserved26` | TField |  |  |
| 18 | `CP.CH.OF.RESERVED.25` | `CpChannelOfflineTemplate_Reserved25` | TField |  |  |
| 19 | `CP.CH.OF.RESERVED.24` | `CpChannelOfflineTemplate_Reserved24` | TField |  |  |
| 20 | `CP.CH.OF.RESERVED.23` | `CpChannelOfflineTemplate_Reserved23` | TField |  |  |
| 21 | `CP.CH.OF.RESERVED.22` | `CpChannelOfflineTemplate_Reserved22` | TField |  |  |
| 22 | `CP.CH.OF.RESERVED.21` | `CpChannelOfflineTemplate_Reserved21` | TField |  |  |
| 23 | `CP.CH.OF.RESERVED.20` | `CpChannelOfflineTemplate_Reserved20` | TField |  |  |
| 24 | `CP.CH.OF.RESERVED.19` | `CpChannelOfflineTemplate_Reserved19` | TField |  |  |
| 25 | `CP.CH.OF.RESERVED.18` | `CpChannelOfflineTemplate_Reserved18` | TField |  |  |
| 26 | `CP.CH.OF.RESERVED.17` | `CpChannelOfflineTemplate_Reserved17` | TField |  |  |
| 27 | `CP.CH.OF.RESERVED.16` | `CpChannelOfflineTemplate_Reserved16` | TField |  |  |
| 28 | `CP.CH.OF.RESERVED.15` | `CpChannelOfflineTemplate_Reserved15` | TField |  |  |
| 29 | `CP.CH.OF.RESERVED.14` | `CpChannelOfflineTemplate_Reserved14` | TField |  |  |
| 30 | `CP.CH.OF.RESERVED.13` | `CpChannelOfflineTemplate_Reserved13` | TField |  |  |
| 31 | `CP.CH.OF.RESERVED.12` | `CpChannelOfflineTemplate_Reserved12` | TField |  |  |
| 32 | `CP.CH.OF.RESERVED.11` | `CpChannelOfflineTemplate_Reserved11` | TField |  |  |
| 33 | `CP.CH.OF.RESERVED.10` | `CpChannelOfflineTemplate_Reserved10` | TField |  |  |
| 34 | `CP.CH.OF.RESERVED.9` | `CpChannelOfflineTemplate_Reserved9` | TField |  |  |
| 35 | `CP.CH.OF.RESERVED.8` | `CpChannelOfflineTemplate_Reserved8` | TField |  |  |
| 36 | `CP.CH.OF.RESERVED.7` | `CpChannelOfflineTemplate_Reserved7` | TField |  |  |
| 37 | `CP.CH.OF.RESERVED.6` | `CpChannelOfflineTemplate_Reserved6` | TField |  |  |
| 38 | `CP.CH.OF.RESERVED.5` | `CpChannelOfflineTemplate_Reserved5` | TField |  |  |
| 39 | `CP.CH.OF.RESERVED.4` | `CpChannelOfflineTemplate_Reserved4` | TField |  |  |
| 40 | `CP.CH.OF.RESERVED.3` | `CpChannelOfflineTemplate_Reserved3` | TField |  |  |
| 41 | `CP.CH.OF.RESERVED.2` | `CpChannelOfflineTemplate_Reserved2` | TField |  |  |
| 42 | `CP.CH.OF.RESERVED.1` | `CpChannelOfflineTemplate_Reserved1` | TField |  |  |
| 43 | `CP.CH.OF.LOCAL.REF` | `CpChannelOfflineTemplate_LocalRef` |  |  |  |
| 44 | `CP.CH.OF.OVERRIDE` | `CpChannelOfflineTemplate_Override` |  |  |  |
| 45 | `CP.CH.OF.RECORD.STATUS` | `CpChannelOfflineTemplate_RecordStatus` | String |  |  |
| 46 | `CP.CH.OF.CURR.NO` | `CpChannelOfflineTemplate_CurrNo` | String |  |  |
| 47 | `CP.CH.OF.INPUTTER` | `CpChannelOfflineTemplate_Inputter` |  |  |  |
| 48 | `CP.CH.OF.DATE.TIME` | `CpChannelOfflineTemplate_DateTime` |  |  |  |
| 49 | `CP.CH.OF.AUTHORISER` | `CpChannelOfflineTemplate_Authoriser` | String |  |  |
| 50 | `CP.CH.OF.CO.CODE` | `CpChannelOfflineTemplate_CoCode` | String |  |  |
| 51 | `CP.CH.OF.DEPT.CODE` | `CpChannelOfflineTemplate_DeptCode` | String |  |  |
| 52 | `CP.CH.OF.AUDITOR.CODE` | `CpChannelOfflineTemplate_AuditorCode` | String |  |  |
| 53 | `CP.CH.OF.AUDIT.DATE.TIME` | `CpChannelOfflineTemplate_AuditDateTime` | String |  |  |
