# CP.VARIANT — Table Schema

> Source: `INSERTS/I_F.CP.VARIANT` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.VR.NAME` | `CpVariant_Name` | TField | Yes | Name of the Variant. Validation Rules :Mandatory field, 35 text characters. |
| 2 | `CP.VR.DESCRIPTION` | `CpVariant_Description` |  |  |  |
| 3 | `CP.VR.SELECTION.DATA` | `CpVariant_SelectionData` | TField |  | Linked to new option in CP.CAMPAIGN and CP.VARIANT.SELECTION HasVariantOptions = Y. Validation Rules :Any 10000 characters. |
| 4 | `CP.VR.VARIANT.TYPE` | `CpVariant_VariantType` | TField |  | If it is blank, the variant is not tested yet. If it is 'TESTED', the variant has been tested and should not be updated. Validation Rules |
| 5 | `CP.VR.CHANNEL` | `CpVariant_Channel` | TField |  | The ID of the communication channel used to manage the customer interactions for a campaign. This field links the CP.VARIANT table to the CP.CHANNEL one. Validation Rules :35 text characters. |
| 6 | `CP.VR.USE.TEMPLATES` | `CpVariant_UseTemplates` | TField |  | A dropdown list containing Yes/No values to indicate if the Marketing Inputter would like to use an already saved template for a communication. |
| 7 | `CP.VR.OFFLINE.TEMPLATE` | `CpVariant_OfflineTemplate` | TField |  | The ID of the communication template used to shape the message sent to the customer through email or secure message, as part of a campaign.This field links the CP.VARIANT table to the CP.CHANNEL.OFFLINE.TEMPLATE one. Validation Rules :35 text characters. |
| 8 | `CP.VR.REQ.DATA.CONTEXT` | `CpVariant_ReqDataContext` |  |  |  |
| 9 | `CP.VR.CHANNEL.DATA` | `CpVariant_ChannelData` |  |  |  |
| 10 | `CP.VR.CONTENT.LOCATION` | `CpVariant_ContentLocation` | TField |  | The ID of the placeholder/section in the edgeConnect project where campaign content can be displayed to the customer as output for the running campaign.This field links the CP.VARIANT table to the CP.CHANNEL.OUTPUT one. Validation Rules :Any 250 characters. |
| 11 | `CP.VR.USE.RESOURCE` | `CpVariant_UseResource` | TField |  | Drop down list containing Yes and No values which allows the Marketing Inputter to choose if s/he will use a Resource. |
| 12 | `CP.VR.RESOURCE` | `CpVariant_Resource` | TField |  | The ID of a reusable set of content attached or not to a product, that can be used across multiple campaigns.This field links the CP.VARIANT table to the CP.CHANNEL.ONLINE.TEMPLATE one. Validation Rules :35 text characters. |
| 13 | `CP.VR.CHOSEN.CONTENT` | `CpVariant_ChosenContent` | TField |  | The content which will be displayed for the customer. Validation Rules :Any 1000 characters. |
| 14 | `CP.VR.CONTENT.EXTRA` | `CpVariant_ContentExtra` | TField |  | The extra content which will be displayed for the customer. Validation Rules :Any 250 characters. |
| 15 | `CP.VR.CONTENT.TITLE` | `CpVariant_ContentTitle` | TField |  | The content which will be displayed for the customer. Validation Rules :Any 250 characters. |
| 16 | `CP.VR.ON.CLICK.URL` | `CpVariant_OnClickUrl` | TField |  | The URL to which the customer will be redirected if he clicks on the content displayed as output for the campaign. Validation Rules :Any 1000 characters. |
| 17 | `CP.VR.CONTENT.TYPE` | `CpVariant_ContentType` | TField |  | This filed stores the type of the content used for the definition of the reusable resource. |
| 18 | `CP.VR.CONTENT.TYPE.DATA` | `CpVariant_ContentTypeData` |  |  |  |
| 19 | `CP.VR.VERSION.FLAG` | `CpVariant_VersionFlag` | TField |  | VERSION.FLAG |
| 20 | `CP.VR.NEW.VERSION.ID` | `CpVariant_NewVersionId` | TField |  | NEW.VERSION.ID |
| 21 | `CP.VR.SUSPEND.REASON.ID` | `CpVariant_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SuspendReasonId -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 22 | `CP.VR.CAMPAIGN.ID` | `CpVariant_CampaignId` | TField |  | This field stores the ID of the campaign that has/had this variant attached for testing. A campaign can have more than one variant attached. A variant is created for only one campaign. |
| 23 | `CP.VR.SEGMENTATION` | `CpVariant_Segmentation` | TField |  | Percentage of clients from the defined target audience who will receive the variant. It is calculated as 100%-Control's segment. |
| 24 | `CP.VR.NO.VARIANT.CUSTOMERS` | `CpVariant_NoVariantCustomers` | TField |  | Specifies the number of clients who triggered the campaign and received the variant. |
| 25 | `CP.VR.ORIGINAL.ID` | `CpVariant_OriginalId` | TField |  | This field is used to save the original id of the Variant record. |
| 26 | `CP.VR.LAST.UPDATE` | `CpVariant_LastUpdate` | TField |  | This field is used to specify the datetime for the last modification done for this record. |
| 27 | `CP.VR.RESERVED.29` | `CpVariant_Reserved29` | TField |  |  |
| 28 | `CP.VR.RESERVED.28` | `CpVariant_Reserved28` | TField |  |  |
| 29 | `CP.VR.RESERVED.27` | `CpVariant_Reserved27` | TField |  |  |
| 30 | `CP.VR.RESERVED.26` | `CpVariant_Reserved26` | TField |  |  |
| 31 | `CP.VR.RESERVED.25` | `CpVariant_Reserved25` | TField |  |  |
| 32 | `CP.VR.RESERVED.24` | `CpVariant_Reserved24` | TField |  |  |
| 33 | `CP.VR.RESERVED.23` | `CpVariant_Reserved23` | TField |  |  |
| 34 | `CP.VR.RESERVED.22` | `CpVariant_Reserved22` | TField |  |  |
| 35 | `CP.VR.RESERVED.21` | `CpVariant_Reserved21` | TField |  |  |
| 36 | `CP.VR.RESERVED.20` | `CpVariant_Reserved20` | TField |  |  |
| 37 | `CP.VR.RESERVED.19` | `CpVariant_Reserved19` | TField |  |  |
| 38 | `CP.VR.RESERVED.18` | `CpVariant_Reserved18` | TField |  |  |
| 39 | `CP.VR.RESERVED.17` | `CpVariant_Reserved17` | TField |  |  |
| 40 | `CP.VR.RESERVED.16` | `CpVariant_Reserved16` | TField |  |  |
| 41 | `CP.VR.RESERVED.15` | `CpVariant_Reserved15` | TField |  |  |
| 42 | `CP.VR.RESERVED.14` | `CpVariant_Reserved14` | TField |  |  |
| 43 | `CP.VR.RESERVED.13` | `CpVariant_Reserved13` | TField |  |  |
| 44 | `CP.VR.RESERVED.12` | `CpVariant_Reserved12` | TField |  |  |
| 45 | `CP.VR.RESERVED.11` | `CpVariant_Reserved11` | TField |  |  |
| 46 | `CP.VR.RESERVED.10` | `CpVariant_Reserved10` | TField |  |  |
| 47 | `CP.VR.RESERVED.9` | `CpVariant_Reserved9` | TField |  |  |
| 48 | `CP.VR.RESERVED.8` | `CpVariant_Reserved8` | TField |  |  |
| 49 | `CP.VR.RESERVED.7` | `CpVariant_Reserved7` | TField |  |  |
| 50 | `CP.VR.RESERVED.6` | `CpVariant_Reserved6` | TField |  |  |
| 51 | `CP.VR.RESERVED.5` | `CpVariant_Reserved5` | TField |  |  |
| 52 | `CP.VR.RESERVED.4` | `CpVariant_Reserved4` | TField |  |  |
| 53 | `CP.VR.RESERVED.3` | `CpVariant_Reserved3` | TField |  |  |
| 54 | `CP.VR.RESERVED.2` | `CpVariant_Reserved2` | TField |  |  |
| 55 | `CP.VR.RESERVED.1` | `CpVariant_Reserved1` | TField |  |  |
| 56 | `CP.VR.LOCAL.REF` | `CpVariant_LocalRef` |  |  |  |
| 57 | `CP.VR.OVERRIDE` | `CpVariant_Override` |  |  |  |
| 58 | `CP.VR.RECORD.STATUS` | `CpVariant_RecordStatus` | String |  |  |
| 59 | `CP.VR.CURR.NO` | `CpVariant_CurrNo` | String |  |  |
| 60 | `CP.VR.INPUTTER` | `CpVariant_Inputter` |  |  |  |
| 61 | `CP.VR.DATE.TIME` | `CpVariant_DateTime` |  |  |  |
| 62 | `CP.VR.AUTHORISER` | `CpVariant_Authoriser` | String |  |  |
| 63 | `CP.VR.CO.CODE` | `CpVariant_CoCode` | String |  |  |
| 64 | `CP.VR.DEPT.CODE` | `CpVariant_DeptCode` | String |  |  |
| 65 | `CP.VR.AUDITOR.CODE` | `CpVariant_AuditorCode` | String |  |  |
| 66 | `CP.VR.AUDIT.DATE.TIME` | `CpVariant_AuditDateTime` | String |  |  |
