# EB.UPDATE.RELEASE — Table Schema

> Source: `INSERTS/I_F.EB.UPDATE.RELEASE` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UPD.DESCRIPTION` | `EbUpdateRelease_Description` |  |  |  |
| 2 | `EB.UPD.COMPONENT` | `EbUpdateRelease_Component` | TField |  | Linked component if available. |
| 3 | `EB.UPD.SUPPORTED.PLATFORMS` | `EbUpdateRelease_SupportedPlatforms` |  |  |  |
| 4 | `EB.UPD.RESERVED.8` | `EbUpdateRelease_Reserved8` | TField |  |  |
| 5 | `EB.UPD.RESERVED.7` | `EbUpdateRelease_Reserved7` | TField |  |  |
| 6 | `EB.UPD.RESERVED.6` | `EbUpdateRelease_Reserved6` | TField |  |  |
| 7 | `EB.UPD.RESERVED.5` | `EbUpdateRelease_Reserved5` | TField |  |  |
| 8 | `EB.UPD.RESERVED.4` | `EbUpdateRelease_Reserved4` | TField |  |  |
| 9 | `EB.UPD.RESERVED.3` | `EbUpdateRelease_Reserved3` | TField |  |  |
| 10 | `EB.UPD.RESERVED.2` | `EbUpdateRelease_Reserved2` | TField |  |  |
| 11 | `EB.UPD.RESERVED.1` | `EbUpdateRelease_Reserved1` | TField |  |  |
| 12 | `EB.UPD.LOCAL.REF` | `EbUpdateRelease_LocalRef` |  |  |  |
| 13 | `EB.UPD.RECORD.STATUS` | `EbUpdateRelease_RecordStatus` | String |  |  |
| 14 | `EB.UPD.CURR.NO` | `EbUpdateRelease_CurrNo` | String |  |  |
| 15 | `EB.UPD.INPUTTER` | `EbUpdateRelease_Inputter` |  |  |  |
| 16 | `EB.UPD.DATE.TIME` | `EbUpdateRelease_DateTime` |  |  |  |
| 17 | `EB.UPD.AUTHORISER` | `EbUpdateRelease_Authoriser` | String |  |  |
| 18 | `EB.UPD.CO.CODE` | `EbUpdateRelease_CoCode` | String |  |  |
| 19 | `EB.UPD.DEPT.CODE` | `EbUpdateRelease_DeptCode` | String |  |  |
| 20 | `EB.UPD.AUDITOR.CODE` | `EbUpdateRelease_AuditorCode` | String |  |  |
| 21 | `EB.UPD.AUDIT.DATE.TIME` | `EbUpdateRelease_AuditDateTime` | String |  |  |
