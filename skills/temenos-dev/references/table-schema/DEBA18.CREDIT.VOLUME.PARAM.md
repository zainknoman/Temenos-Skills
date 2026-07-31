# DEBA18.CREDIT.VOLUME.PARAM — Table Schema

> Source: `INSERTS/I_F.DEBA18.CREDIT.VOLUME.PARAM` in `DEBA18_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBA18.INCL.START.CATEGORY` | `Deba18CreditVolumeParam_InclStartCategory` |  |  |  |
| 2 | `DEBA18.INCL.END.CATEGORY` | `Deba18CreditVolumeParam_InclEndCategory` |  |  |  |
| 3 | `DEBA18.EXCL.START.SECTOR` | `Deba18CreditVolumeParam_ExclStartSector` |  |  |  |
| 4 | `DEBA18.EXCL.END.SECTOR` | `Deba18CreditVolumeParam_ExclEndSector` |  |  |  |
| 5 | `DEBA18.RESERVED.10` | `Deba18CreditVolumeParam_Reserved10` | TField |  | Reserved for Future Use. |
| 6 | `DEBA18.RESERVED.9` | `Deba18CreditVolumeParam_Reserved9` | TField |  | Reserved for Future Use. |
| 7 | `DEBA18.RESERVED.8` | `Deba18CreditVolumeParam_Reserved8` | TField |  | Reserved for Future Use. |
| 8 | `DEBA18.RESERVED.7` | `Deba18CreditVolumeParam_Reserved7` | TField |  | Reserved for Future Use. |
| 9 | `DEBA18.RESERVED.6` | `Deba18CreditVolumeParam_Reserved6` | TField |  | Reserved for Future Use. |
| 10 | `DEBA18.RESERVED.5` | `Deba18CreditVolumeParam_Reserved5` | TField |  | Reserved for Future Use. |
| 11 | `DEBA18.RESERVED.4` | `Deba18CreditVolumeParam_Reserved4` | TField |  | Reserved for Future Use. |
| 12 | `DEBA18.RESERVED.3` | `Deba18CreditVolumeParam_Reserved3` | TField |  | Reserved for Future Use. |
| 13 | `DEBA18.RESERVED.2` | `Deba18CreditVolumeParam_Reserved2` | TField |  | Reserved for Future Use. |
| 14 | `DEBA18.RESERVED.1` | `Deba18CreditVolumeParam_Reserved1` | TField |  | Reserved for Future Use. |
| 15 | `DEBA18.LOCAL.REF` | `Deba18CreditVolumeParam_LocalRef` |  |  |  |
| 16 | `DEBA18.OVERRIDE` | `Deba18CreditVolumeParam_Override` |  |  |  |
| 17 | `DEBA18.RECORD.STATUS` | `Deba18CreditVolumeParam_RecordStatus` | String |  |  |
| 18 | `DEBA18.CURR.NO` | `Deba18CreditVolumeParam_CurrNo` | String |  |  |
| 19 | `DEBA18.INPUTTER` | `Deba18CreditVolumeParam_Inputter` |  |  |  |
| 20 | `DEBA18.DATE.TIME` | `Deba18CreditVolumeParam_DateTime` |  |  |  |
| 21 | `DEBA18.AUTHORISER` | `Deba18CreditVolumeParam_Authoriser` | String |  |  |
| 22 | `DEBA18.CO.CODE` | `Deba18CreditVolumeParam_CoCode` | String |  |  |
| 23 | `DEBA18.DEPT.CODE` | `Deba18CreditVolumeParam_DeptCode` | String |  |  |
| 24 | `DEBA18.AUDITOR.CODE` | `Deba18CreditVolumeParam_AuditorCode` | String |  |  |
| 25 | `DEBA18.AUDIT.DATE.TIME` | `Deba18CreditVolumeParam_AuditDateTime` | String |  |  |
