# CP.PROFILE — Table Schema

> Source: `INSERTS/I_F.CP.PROFILE` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.PRF.NAME` | `CpProfile_Name` | TField | Yes | This field stores the name of a given profile. Validation Rules: Mandatory field, any 50 characters. |
| 2 | `CP.PRF.DESCRIPTION` | `CpProfile_Description` |  |  |  |
| 3 | `CP.PRF.TYPE` | `CpProfile_Type` | TField | Yes | This field stores whether the given profile is an evaluation one. Validation Rules: Mandatory field, 35 text characters. |
| 4 | `CP.PRF.CONTEXT` | `CpProfile_Context` |  |  |  |
| 5 | `CP.PRF.VALUE` | `CpProfile_Value` |  |  |  |
| 6 | `CP.PRF.VERSION` | `CpProfile_Version` | TField | Yes | The solution allows versioning of templates.This field stores the number of the version for a given profile. Validation Rules: Mandatory numeric field, maximum 3 digits. |
| 7 | `CP.PRF.ORIGINAL.ID` | `CpProfile_OriginalId` | TField | Yes | The solution allows versioning of profiles.For every version of a profile we need to store the ID of the original one.This field stores the original ID of a profile. Validation Rules: Mandatory field, 12 text characters. |
| 8 | `CP.PRF.EDITABLE` | `CpProfile_Editable` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a profile can be edited.The versioned profiles cannot be edited anymore. |
| 9 | `CP.PRF.VERSION.FLAG` | `CpProfile_VersionFlag` | TField |  | This field stores "NULL", "NWITEM" or "NWCP" values .NULL - this value is assigned to a profile at creation.NWITEM - this value is used when the profile is versioned without conditioning the versioning of the campaigns which use the templateNWCP - this value is used when the profile is versioned and we condition the versioning of the campaigns which use the profile |
| 10 | `CP.PRF.FOR.USE.BY` | `CpProfile_ForUseBy` | TField |  | This field stores values set on EB.LOOKUP - CP.PROFILE.FORUSEBY for : GCP, GEP, GPP, FWP, Empty Field (Normal Profiles)These values condition whether the defined profile is one that will be applied at a global level (to all campaign without it being selected as part of one). |
| 11 | `CP.PRF.STATUS.CODE` | `CpProfile_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 12 | `CP.PRF.LAST.UPDATE` | `CpProfile_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 13 | `CP.PRF.SUSPEND.REASON.ID` | `CpProfile_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 14 | `CP.PRF.METADATA.NAME` | `CpProfile_MetadataName` |  |  |  |
| 15 | `CP.PRF.METADATA.ID` | `CpProfile_MetadataId` |  |  |  |
| 16 | `CP.PRF.WORKFLOW.ID` | `CpProfile_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 17 | `CP.PRF.RESERVED.29` | `CpProfile_Reserved29` | TField |  |  |
| 18 | `CP.PRF.RESERVED.28` | `CpProfile_Reserved28` | TField |  |  |
| 19 | `CP.PRF.RESERVED.27` | `CpProfile_Reserved27` | TField |  |  |
| 20 | `CP.PRF.RESERVED.26` | `CpProfile_Reserved26` | TField |  |  |
| 21 | `CP.PRF.RESERVED.25` | `CpProfile_Reserved25` | TField |  |  |
| 22 | `CP.PRF.RESERVED.24` | `CpProfile_Reserved24` | TField |  |  |
| 23 | `CP.PRF.RESERVED.23` | `CpProfile_Reserved23` | TField |  |  |
| 24 | `CP.PRF.RESERVED.22` | `CpProfile_Reserved22` | TField |  |  |
| 25 | `CP.PRF.RESERVED.21` | `CpProfile_Reserved21` | TField |  |  |
| 26 | `CP.PRF.RESERVED.20` | `CpProfile_Reserved20` | TField |  |  |
| 27 | `CP.PRF.RESERVED.19` | `CpProfile_Reserved19` | TField |  |  |
| 28 | `CP.PRF.RESERVED.18` | `CpProfile_Reserved18` | TField |  |  |
| 29 | `CP.PRF.RESERVED.17` | `CpProfile_Reserved17` | TField |  |  |
| 30 | `CP.PRF.RESERVED.16` | `CpProfile_Reserved16` | TField |  |  |
| 31 | `CP.PRF.RESERVED.15` | `CpProfile_Reserved15` | TField |  |  |
| 32 | `CP.PRF.RESERVED.14` | `CpProfile_Reserved14` | TField |  |  |
| 33 | `CP.PRF.RESERVED.13` | `CpProfile_Reserved13` | TField |  |  |
| 34 | `CP.PRF.RESERVED.12` | `CpProfile_Reserved12` | TField |  |  |
| 35 | `CP.PRF.RESERVED.11` | `CpProfile_Reserved11` | TField |  |  |
| 36 | `CP.PRF.RESERVED.10` | `CpProfile_Reserved10` | TField |  |  |
| 37 | `CP.PRF.RESERVED.9` | `CpProfile_Reserved9` | TField |  |  |
| 38 | `CP.PRF.RESERVED.8` | `CpProfile_Reserved8` | TField |  |  |
| 39 | `CP.PRF.RESERVED.7` | `CpProfile_Reserved7` | TField |  |  |
| 40 | `CP.PRF.RESERVED.6` | `CpProfile_Reserved6` | TField |  |  |
| 41 | `CP.PRF.RESERVED.5` | `CpProfile_Reserved5` | TField |  |  |
| 42 | `CP.PRF.RESERVED.4` | `CpProfile_Reserved4` | TField |  |  |
| 43 | `CP.PRF.RESERVED.3` | `CpProfile_Reserved3` | TField |  |  |
| 44 | `CP.PRF.RESERVED.2` | `CpProfile_Reserved2` | TField |  |  |
| 45 | `CP.PRF.RESERVED.1` | `CpProfile_Reserved1` | TField |  |  |
| 46 | `CP.PRF.LOCAL.REF` | `CpProfile_LocalRef` |  |  |  |
| 47 | `CP.PRF.OVERRIDE` | `CpProfile_Override` |  |  |  |
| 48 | `CP.PRF.RECORD.STATUS` | `CpProfile_RecordStatus` | String |  |  |
| 49 | `CP.PRF.CURR.NO` | `CpProfile_CurrNo` | String |  |  |
| 50 | `CP.PRF.INPUTTER` | `CpProfile_Inputter` |  |  |  |
| 51 | `CP.PRF.DATE.TIME` | `CpProfile_DateTime` |  |  |  |
| 52 | `CP.PRF.AUTHORISER` | `CpProfile_Authoriser` | String |  |  |
| 53 | `CP.PRF.CO.CODE` | `CpProfile_CoCode` | String |  |  |
| 54 | `CP.PRF.DEPT.CODE` | `CpProfile_DeptCode` | String |  |  |
| 55 | `CP.PRF.AUDITOR.CODE` | `CpProfile_AuditorCode` | String |  |  |
| 56 | `CP.PRF.AUDIT.DATE.TIME` | `CpProfile_AuditDateTime` | String |  |  |
