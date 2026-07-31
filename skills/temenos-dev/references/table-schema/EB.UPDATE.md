# EB.UPDATE — Table Schema

> Source: `INSERTS/I_F.EB.UPDATE` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UPD.DESCRIPTION` | `EbUpdate_Description` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `EB.UPD.UPDATE.RELEASED` | `EbUpdate_UpdateReleased` | TField |  | If an update has been marked as released, then it is available to download. |
| 3 | `EB.UPD.UPDATE.VERSION` | `EbUpdate_UpdateVersion` | TField |  | The version number of the update. This should be used to compare to installed Update on the customer environment. |
| 4 | `EB.UPD.RELEASE.DATE` | `EbUpdate_ReleaseDate` | TField |  | The date that this Update should be released. |
| 5 | `EB.UPD.PRODUCT` | `EbUpdate_Product` | TField |  | The Product that this Update belongs to. |
| 6 | `EB.UPD.COMPONENT` | `EbUpdate_Component` | TField |  | The Component that this Update belongs to. |
| 7 | `EB.UPD.GA.RELEASE` | `EbUpdate_GaRelease` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `EB.UPD.DEPENDENT.UPDATE` | `EbUpdate_DependentUpdate` |  |  |  |
| 9 | `EB.UPD.NO.OF.DOWNLOADS` | `EbUpdate_NoOfDownloads` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `EB.UPD.IMPACT` | `EbUpdate_Impact` | TField |  | The GA release number |
| 11 | `EB.UPD.NOTIFICATION.SENT` | `EbUpdate_NotificationSent` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `EB.UPD.SUPERCEDED` | `EbUpdate_Superceded` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `EB.UPD.RESERVED.9` | `EbUpdate_Reserved9` | TField |  |  |
| 14 | `EB.UPD.RESERVED.8` | `EbUpdate_Reserved8` | TField |  |  |
| 15 | `EB.UPD.RESERVED.7` | `EbUpdate_Reserved7` | TField |  |  |
| 16 | `EB.UPD.RESERVED.6` | `EbUpdate_Reserved6` | TField |  |  |
| 17 | `EB.UPD.RESERVED.5` | `EbUpdate_Reserved5` | TField |  |  |
| 18 | `EB.UPD.RESERVED.4` | `EbUpdate_Reserved4` | TField |  |  |
| 19 | `EB.UPD.RESERVED.3` | `EbUpdate_Reserved3` | TField |  |  |
| 20 | `EB.UPD.RESERVED.2` | `EbUpdate_Reserved2` | TField |  |  |
| 21 | `EB.UPD.RESERVED.1` | `EbUpdate_Reserved1` | TField |  |  |
| 22 | `EB.UPD.LOCAL.REF` | `EbUpdate_LocalRef` |  |  |  |
| 23 | `EB.UPD.OVERRIDE` | `EbUpdate_Override` |  |  |  |
| 24 | `EB.UPD.RECORD.STATUS` | `EbUpdate_RecordStatus` | String |  |  |
| 25 | `EB.UPD.CURR.NO` | `EbUpdate_CurrNo` | String |  |  |
| 26 | `EB.UPD.INPUTTER` | `EbUpdate_Inputter` |  |  |  |
| 27 | `EB.UPD.DATE.TIME` | `EbUpdate_DateTime` |  |  |  |
| 28 | `EB.UPD.AUTHORISER` | `EbUpdate_Authoriser` | String |  |  |
| 29 | `EB.UPD.CO.CODE` | `EbUpdate_CoCode` | String |  |  |
| 30 | `EB.UPD.DEPT.CODE` | `EbUpdate_DeptCode` | String |  |  |
| 31 | `EB.UPD.AUDITOR.CODE` | `EbUpdate_AuditorCode` | String |  |  |
| 32 | `EB.UPD.AUDIT.DATE.TIME` | `EbUpdate_AuditDateTime` | String |  |  |
