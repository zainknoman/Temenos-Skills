# CP.CHANNEL.ONLINE.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.CP.CHANNEL.ONLINE.TEMPLATE` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CH.ON.NAME` | `CpChannelOnlineTemplate_Name` | TField |  | This field stores the name of the reusable resource. |
| 2 | `CP.CH.ON.DESCRIPTION` | `CpChannelOnlineTemplate_Description` |  |  |  |
| 3 | `CP.CH.ON.PRODUCT.ID` | `CpChannelOnlineTemplate_ProductId` | TField |  | This field stores the ID of the product associated with the new defined reusable resource. This field links CP.CHANNEL.ONLINE.TEMPLATE table to the AA.PRODUCT one. |
| 4 | `CP.CH.ON.PRODUCT.GROUP.ID` | `CpChannelOnlineTemplate_ProductGroupId` | TField |  | This field stores the ID of the product group associated with the new defined reusable resource. This field links CP.CHANNEL.ONLINE.TEMPLATE table to the AA.PRODUCT.GROUP one. |
| 5 | `CP.CH.ON.CONTENT.TYPE` | `CpChannelOnlineTemplate_ContentType` | TField |  | This field stores the type of the content used for the definition of the reusable resource. (E.g. Image, Video, Text, Image with Text, Article, Blog Entry etc). |
| 6 | `CP.CH.ON.CONTENT.URL` | `CpChannelOnlineTemplate_ContentUrl` | TField |  | The URL where the given resource exists. |
| 7 | `CP.CH.ON.EXTRA` | `CpChannelOnlineTemplate_Extra` | TField |  | Phase 2 Enhancement |
| 8 | `CP.CH.ON.TITLE` | `CpChannelOnlineTemplate_Title` | TField |  | This field stores the values which are used as tooltips in the Campaign Management User Agent Interface for the given reusable resource. |
| 9 | `CP.CH.ON.CLICK.URL` | `CpChannelOnlineTemplate_ClickUrl` | TField |  | This field stores the URL a customer is redirected in case s/he decides to click on the content attached to the message which was communicated by the bank as part of marketing campaign. |
| 10 | `CP.CH.ON.REUSE.TYPE` | `CpChannelOnlineTemplate_ReuseType` | TField |  | This field stores two values "For All" or "For Products". The value in this field conditions whether the resource is reusable for All cases or only for product campaigns. |
| 11 | `CP.CH.ON.CONTENT.TYPE.DATA` | `CpChannelOnlineTemplate_ContentTypeData` |  |  |  |
| 12 | `CP.CH.ON.REQ.DATA.CONTEXT` | `CpChannelOnlineTemplate_ReqDataContext` |  |  |  |
| 13 | `CP.CH.ON.SUSPEND.REASON.ID` | `CpChannelOnlineTemplate_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 14 | `CP.CH.ON.METADATA.NAME` | `CpChannelOnlineTemplate_MetadataName` |  |  |  |
| 15 | `CP.CH.ON.METADATA.ID` | `CpChannelOnlineTemplate_MetadataId` |  |  |  |
| 16 | `CP.CH.ON.RESERVED.30` | `CpChannelOnlineTemplate_Reserved30` | TField |  |  |
| 17 | `CP.CH.ON.RESERVED.29` | `CpChannelOnlineTemplate_Reserved29` | TField |  |  |
| 18 | `CP.CH.ON.RESERVED.28` | `CpChannelOnlineTemplate_Reserved28` | TField |  |  |
| 19 | `CP.CH.ON.RESERVED.27` | `CpChannelOnlineTemplate_Reserved27` | TField |  |  |
| 20 | `CP.CH.ON.RESERVED.26` | `CpChannelOnlineTemplate_Reserved26` | TField |  |  |
| 21 | `CP.CH.ON.RESERVED.25` | `CpChannelOnlineTemplate_Reserved25` | TField |  |  |
| 22 | `CP.CH.ON.RESERVED.24` | `CpChannelOnlineTemplate_Reserved24` | TField |  |  |
| 23 | `CP.CH.ON.RESERVED.23` | `CpChannelOnlineTemplate_Reserved23` | TField |  |  |
| 24 | `CP.CH.ON.RESERVED.22` | `CpChannelOnlineTemplate_Reserved22` | TField |  |  |
| 25 | `CP.CH.ON.RESERVED.21` | `CpChannelOnlineTemplate_Reserved21` | TField |  |  |
| 26 | `CP.CH.ON.RESERVED.20` | `CpChannelOnlineTemplate_Reserved20` | TField |  |  |
| 27 | `CP.CH.ON.RESERVED.19` | `CpChannelOnlineTemplate_Reserved19` | TField |  |  |
| 28 | `CP.CH.ON.RESERVED.18` | `CpChannelOnlineTemplate_Reserved18` | TField |  |  |
| 29 | `CP.CH.ON.RESERVED.17` | `CpChannelOnlineTemplate_Reserved17` | TField |  |  |
| 30 | `CP.CH.ON.RESERVED.16` | `CpChannelOnlineTemplate_Reserved16` | TField |  |  |
| 31 | `CP.CH.ON.RESERVED.15` | `CpChannelOnlineTemplate_Reserved15` | TField |  |  |
| 32 | `CP.CH.ON.RESERVED.14` | `CpChannelOnlineTemplate_Reserved14` | TField |  |  |
| 33 | `CP.CH.ON.RESERVED.13` | `CpChannelOnlineTemplate_Reserved13` | TField |  |  |
| 34 | `CP.CH.ON.RESERVED.12` | `CpChannelOnlineTemplate_Reserved12` | TField |  |  |
| 35 | `CP.CH.ON.RESERVED.11` | `CpChannelOnlineTemplate_Reserved11` | TField |  |  |
| 36 | `CP.CH.ON.RESERVED.10` | `CpChannelOnlineTemplate_Reserved10` | TField |  |  |
| 37 | `CP.CH.ON.RESERVED.9` | `CpChannelOnlineTemplate_Reserved9` | TField |  |  |
| 38 | `CP.CH.ON.RESERVED.8` | `CpChannelOnlineTemplate_Reserved8` | TField |  |  |
| 39 | `CP.CH.ON.RESERVED.7` | `CpChannelOnlineTemplate_Reserved7` | TField |  |  |
| 40 | `CP.CH.ON.RESERVED.6` | `CpChannelOnlineTemplate_Reserved6` | TField |  |  |
| 41 | `CP.CH.ON.RESERVED.5` | `CpChannelOnlineTemplate_Reserved5` | TField |  |  |
| 42 | `CP.CH.ON.RESERVED.4` | `CpChannelOnlineTemplate_Reserved4` | TField |  |  |
| 43 | `CP.CH.ON.RESERVED.3` | `CpChannelOnlineTemplate_Reserved3` | TField |  |  |
| 44 | `CP.CH.ON.RESERVED.2` | `CpChannelOnlineTemplate_Reserved2` | TField |  |  |
| 45 | `CP.CH.ON.RESERVED.1` | `CpChannelOnlineTemplate_Reserved1` | TField |  |  |
| 46 | `CP.CH.ON.LOCAL.REF` | `CpChannelOnlineTemplate_LocalRef` |  |  |  |
| 47 | `CP.CH.ON.OVERRIDE` | `CpChannelOnlineTemplate_Override` |  |  |  |
| 48 | `CP.CH.ON.RECORD.STATUS` | `CpChannelOnlineTemplate_RecordStatus` | String |  |  |
| 49 | `CP.CH.ON.CURR.NO` | `CpChannelOnlineTemplate_CurrNo` | String |  |  |
| 50 | `CP.CH.ON.INPUTTER` | `CpChannelOnlineTemplate_Inputter` |  |  |  |
| 51 | `CP.CH.ON.DATE.TIME` | `CpChannelOnlineTemplate_DateTime` |  |  |  |
| 52 | `CP.CH.ON.AUTHORISER` | `CpChannelOnlineTemplate_Authoriser` | String |  |  |
| 53 | `CP.CH.ON.CO.CODE` | `CpChannelOnlineTemplate_CoCode` | String |  |  |
| 54 | `CP.CH.ON.DEPT.CODE` | `CpChannelOnlineTemplate_DeptCode` | String |  |  |
| 55 | `CP.CH.ON.AUDITOR.CODE` | `CpChannelOnlineTemplate_AuditorCode` | String |  |  |
| 56 | `CP.CH.ON.AUDIT.DATE.TIME` | `CpChannelOnlineTemplate_AuditDateTime` | String |  |  |
