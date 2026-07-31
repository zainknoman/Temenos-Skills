# EB.SERVICE.PACK — Table Schema

> Source: `INSERTS/I_F.EB.SERVICE.PACK` in `EB_Upgrade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SRP.DESCRIPTION` | `EbServicePack_Description` | TField |  |  |
| 2 | `EB.SRP.SP.RELEASED` | `EbServicePack_SpReleased` | TField |  |  |
| 3 | `EB.SRP.GA.RELEASE` | `EbServicePack_GaRelease` | TField |  |  |
| 4 | `EB.SRP.RELEASE.DATE` | `EbServicePack_ReleaseDate` | TField |  |  |
| 5 | `EB.SRP.VERSION` | `EbServicePack_Version` | TField |  |  |
| 6 | `EB.SRP.LOCATION` | `EbServicePack_Location` | TField |  |  |
| 7 | `EB.SRP.RESERVED.10` | `EbServicePack_Reserved10` | TField |  |  |
| 8 | `EB.SRP.RESERVED.9` | `EbServicePack_Reserved9` | TField |  |  |
| 9 | `EB.SRP.RESERVED.8` | `EbServicePack_Reserved8` | TField |  |  |
| 10 | `EB.SRP.RESERVED.7` | `EbServicePack_Reserved7` | TField |  |  |
| 11 | `EB.SRP.RESERVED.6` | `EbServicePack_Reserved6` | TField |  |  |
| 12 | `EB.SRP.RESERVED.5` | `EbServicePack_Reserved5` | TField |  |  |
| 13 | `EB.SRP.RESERVED.4` | `EbServicePack_Reserved4` | TField |  |  |
| 14 | `EB.SRP.RESERVED.3` | `EbServicePack_Reserved3` | TField |  |  |
| 15 | `EB.SRP.RESERVED.2` | `EbServicePack_Reserved2` | TField |  |  |
| 16 | `EB.SRP.RESERVED.1` | `EbServicePack_Reserved1` | TField |  |  |
| 17 | `EB.SRP.LOCAL.REF` | `EbServicePack_LocalRef` |  |  |  |
| 18 | `EB.SRP.OVERRIDE` | `EbServicePack_Override` |  |  |  |
| 19 | `EB.SRP.RECORD.STATUS` | `EbServicePack_RecordStatus` | String |  |  |
| 20 | `EB.SRP.CURR.NO` | `EbServicePack_CurrNo` | String |  |  |
| 21 | `EB.SRP.INPUTTER` | `EbServicePack_Inputter` |  |  |  |
| 22 | `EB.SRP.DATE.TIME` | `EbServicePack_DateTime` |  |  |  |
| 23 | `EB.SRP.AUTHORISER` | `EbServicePack_Authoriser` | String |  |  |
| 24 | `EB.SRP.CO.CODE` | `EbServicePack_CoCode` | String |  |  |
| 25 | `EB.SRP.DEPT.CODE` | `EbServicePack_DeptCode` | String |  |  |
| 26 | `EB.SRP.AUDITOR.CODE` | `EbServicePack_AuditorCode` | String |  |  |
| 27 | `EB.SRP.AUDIT.DATE.TIME` | `EbServicePack_AuditDateTime` | String |  |  |
