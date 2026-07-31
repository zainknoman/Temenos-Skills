# CS.SOCIAL.MEDIA — Table Schema

> Source: `INSERTS/I_F.CS.SOCIAL.MEDIA` in `CS_SocialMedia.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CS.SCM.SOCIAL.MEDIA.TYPE` | `CsSocialMedia_SocialMediaType` | TField | Yes | This field stores the social media type (Facebook, Twitter, etc.) for which the record is being created. Validation Rules: Mandatory numeric field, maximum 100 characters. |
| 2 | `CS.SCM.DESCRIPTION` | `CsSocialMedia_Description` |  |  |  |
| 3 | `CS.SCM.BLOB` | `CsSocialMedia_Blob` |  |  |  |
| 4 | `CS.SCM.IDENTIFIER` | `CsSocialMedia_Identifier` | TField |  | This field contains a key, that will help identify the data stored into the blob field. Validation Rules: Up to any 500 characters. |
| 5 | `CS.SCM.STATUS.CODE` | `CsSocialMedia_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 6 | `CS.SCM.ORIGINAL.ID` | `CsSocialMedia_OriginalId` | TField |  | The solution allows versioning for SocialMedia.For every version of a SocialMedia we need to store the ID of the original one.This field stores the original ID of a SocialMedia. |
| 7 | `CS.SCM.LAST.UPDATE` | `CsSocialMedia_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 8 | `CS.SCM.IS.VISIBLE` | `CsSocialMedia_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a SocialMedia can be used for new campaigns. |
| 9 | `CS.SCM.OWNER` | `CsSocialMedia_Owner` | TField |  | The user who defines the SocialMedia. Links to the ID of USER table. |
| 10 | `CS.SCM.SUSPEND.REASON.ID` | `CsSocialMedia_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 11 | `CS.SCM.METADATA.NAME` | `CsSocialMedia_MetadataName` |  |  |  |
| 12 | `CS.SCM.METADATA.ID` | `CsSocialMedia_MetadataId` |  |  |  |
| 13 | `CS.SCM.WORKFLOW.ID` | `CsSocialMedia_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 14 | `CS.SCM.RESERVED.29` | `CsSocialMedia_Reserved29` | TField |  |  |
| 15 | `CS.SCM.RESERVED.28` | `CsSocialMedia_Reserved28` | TField |  |  |
| 16 | `CS.SCM.RESERVED.27` | `CsSocialMedia_Reserved27` | TField |  |  |
| 17 | `CS.SCM.RESERVED.26` | `CsSocialMedia_Reserved26` | TField |  |  |
| 18 | `CS.SCM.RESERVED.25` | `CsSocialMedia_Reserved25` | TField |  |  |
| 19 | `CS.SCM.RESERVED.24` | `CsSocialMedia_Reserved24` | TField |  |  |
| 20 | `CS.SCM.RESERVED.23` | `CsSocialMedia_Reserved23` | TField |  |  |
| 21 | `CS.SCM.RESERVED.22` | `CsSocialMedia_Reserved22` | TField |  |  |
| 22 | `CS.SCM.RESERVED.21` | `CsSocialMedia_Reserved21` | TField |  |  |
| 23 | `CS.SCM.RESERVED.20` | `CsSocialMedia_Reserved20` | TField |  |  |
| 24 | `CS.SCM.RESERVED.19` | `CsSocialMedia_Reserved19` | TField |  |  |
| 25 | `CS.SCM.RESERVED.18` | `CsSocialMedia_Reserved18` | TField |  |  |
| 26 | `CS.SCM.RESERVED.17` | `CsSocialMedia_Reserved17` | TField |  |  |
| 27 | `CS.SCM.RESERVED.16` | `CsSocialMedia_Reserved16` | TField |  |  |
| 28 | `CS.SCM.RESERVED.15` | `CsSocialMedia_Reserved15` | TField |  |  |
| 29 | `CS.SCM.RESERVED.14` | `CsSocialMedia_Reserved14` | TField |  |  |
| 30 | `CS.SCM.RESERVED.13` | `CsSocialMedia_Reserved13` | TField |  |  |
| 31 | `CS.SCM.RESERVED.12` | `CsSocialMedia_Reserved12` | TField |  |  |
| 32 | `CS.SCM.RESERVED.11` | `CsSocialMedia_Reserved11` | TField |  |  |
| 33 | `CS.SCM.RESERVED.10` | `CsSocialMedia_Reserved10` | TField |  |  |
| 34 | `CS.SCM.RESERVED.9` | `CsSocialMedia_Reserved9` | TField |  |  |
| 35 | `CS.SCM.RESERVED.8` | `CsSocialMedia_Reserved8` | TField |  |  |
| 36 | `CS.SCM.RESERVED.7` | `CsSocialMedia_Reserved7` | TField |  |  |
| 37 | `CS.SCM.RESERVED.6` | `CsSocialMedia_Reserved6` | TField |  |  |
| 38 | `CS.SCM.RESERVED.5` | `CsSocialMedia_Reserved5` | TField |  |  |
| 39 | `CS.SCM.RESERVED.4` | `CsSocialMedia_Reserved4` | TField |  |  |
| 40 | `CS.SCM.RESERVED.3` | `CsSocialMedia_Reserved3` | TField |  |  |
| 41 | `CS.SCM.RESERVED.2` | `CsSocialMedia_Reserved2` | TField |  |  |
| 42 | `CS.SCM.RESERVED.1` | `CsSocialMedia_Reserved1` | TField |  |  |
| 43 | `CS.SCM.LOCAL.REF` | `CsSocialMedia_LocalRef` |  |  |  |
| 44 | `CS.SCM.OVERRIDE` | `CsSocialMedia_Override` |  |  |  |
| 45 | `CS.SCM.RECORD.STATUS` | `CsSocialMedia_RecordStatus` | String |  |  |
| 46 | `CS.SCM.CURR.NO` | `CsSocialMedia_CurrNo` | String |  |  |
| 47 | `CS.SCM.INPUTTER` | `CsSocialMedia_Inputter` |  |  |  |
| 48 | `CS.SCM.DATE.TIME` | `CsSocialMedia_DateTime` |  |  |  |
| 49 | `CS.SCM.AUTHORISER` | `CsSocialMedia_Authoriser` | String |  |  |
| 50 | `CS.SCM.CO.CODE` | `CsSocialMedia_CoCode` | String |  |  |
| 51 | `CS.SCM.DEPT.CODE` | `CsSocialMedia_DeptCode` | String |  |  |
| 52 | `CS.SCM.AUDITOR.CODE` | `CsSocialMedia_AuditorCode` | String |  |  |
| 53 | `CS.SCM.AUDIT.DATE.TIME` | `CsSocialMedia_AuditDateTime` | String |  |  |
