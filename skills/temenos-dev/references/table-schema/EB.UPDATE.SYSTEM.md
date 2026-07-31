# EB.UPDATE.SYSTEM — Table Schema

> Source: `INSERTS/I_F.EB.UPDATE.SYSTEM` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UPDSYS.CUSTOMER.NO` | `EbUpdateSystem_CustomerNo` | TField |  | Enter an existing customer number. |
| 2 | `EB.UPDSYS.DESCRIPTION` | `EbUpdateSystem_Description` | TField |  | Enter a description of the environment. |
| 3 | `EB.UPDSYS.GA.RELEASE` | `EbUpdateSystem_GaRelease` | TField |  | The GA Release that this customer has installed. |
| 4 | `EB.UPDSYS.INSTALLED.PRODUCT` | `EbUpdateSystem_InstalledProduct` |  |  |  |
| 5 | `EB.UPDSYS.INSTALLED.COMPONENT` | `EbUpdateSystem_InstalledComponent` |  |  |  |
| 6 | `EB.UPDSYS.VERSION` | `EbUpdateSystem_Version` |  |  |  |
| 7 | `EB.UPDSYS.INTERESTED` | `EbUpdateSystem_Interested` |  |  |  |
| 8 | `EB.UPDSYS.OS.PLATFORM` | `EbUpdateSystem_OsPlatform` | A (alphanumeric) | Yes | This field holds the OS.PLATFORM that the system is using. For example:AIX, WIN64,�etc. Should have an entry in EB.OS.PLATFORM application. Validation Rules: .Mandatory Input. Up to 35 type A (alphanumeric) |
| 9 | `EB.UPDSYS.INSTALLED.UPDATE` | `EbUpdateSystem_InstalledUpdate` |  |  |  |
| 10 | `EB.UPDSYS.DELETED` | `EbUpdateSystem_Deleted` | TField |  | If this field contains �YES� the record is deleted. |
| 11 | `EB.UPDSYS.LAST.REGISTRATION` | `EbUpdateSystem_LastRegistration` | TField |  | This field holds the date and time of last registration. |
| 12 | `EB.UPDSYS.LAST.DOWNLOAD` | `EbUpdateSystem_LastDownload` | TField |  | This field holds the date and time of last download. |
| 13 | `EB.UPDSYS.RESERVED.8` | `EbUpdateSystem_Reserved8` | TField |  |  |
| 14 | `EB.UPDSYS.RESERVED.7` | `EbUpdateSystem_Reserved7` | TField |  |  |
| 15 | `EB.UPDSYS.RESERVED.6` | `EbUpdateSystem_Reserved6` | TField |  |  |
| 16 | `EB.UPDSYS.RESERVED.5` | `EbUpdateSystem_Reserved5` | TField |  |  |
| 17 | `EB.UPDSYS.RESERVED.4` | `EbUpdateSystem_Reserved4` | TField |  |  |
| 18 | `EB.UPDSYS.RESERVED.3` | `EbUpdateSystem_Reserved3` | TField |  |  |
| 19 | `EB.UPDSYS.RESERVED.2` | `EbUpdateSystem_Reserved2` | TField |  |  |
| 20 | `EB.UPDSYS.RESERVED.1` | `EbUpdateSystem_Reserved1` | TField |  |  |
| 21 | `EB.UPDSYS.LOCAL.REF` | `EbUpdateSystem_LocalRef` |  |  |  |
| 22 | `EB.UPDSYS.RECORD.STATUS` | `EbUpdateSystem_RecordStatus` | String |  |  |
| 23 | `EB.UPDSYS.CURR.NO` | `EbUpdateSystem_CurrNo` | String |  |  |
| 24 | `EB.UPDSYS.INPUTTER` | `EbUpdateSystem_Inputter` |  |  |  |
| 25 | `EB.UPDSYS.DATE.TIME` | `EbUpdateSystem_DateTime` |  |  |  |
| 26 | `EB.UPDSYS.AUTHORISER` | `EbUpdateSystem_Authoriser` | String |  |  |
| 27 | `EB.UPDSYS.CO.CODE` | `EbUpdateSystem_CoCode` | String |  |  |
| 28 | `EB.UPDSYS.DEPT.CODE` | `EbUpdateSystem_DeptCode` | String |  |  |
| 29 | `EB.UPDSYS.AUDITOR.CODE` | `EbUpdateSystem_AuditorCode` | String |  |  |
| 30 | `EB.UPDSYS.AUDIT.DATE.TIME` | `EbUpdateSystem_AuditDateTime` | String |  |  |
