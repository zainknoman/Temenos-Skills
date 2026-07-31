# EB.COMPONENT — Table Schema

> Source: `INSERTS/I_F.EB.COMPONENT` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.COMPT.DESCRIPTION` | `EbComponent_Description` |  |  |  |
| 2 | `EB.COMPT.PRODUCT` | `EbComponent_Product` | TField |  | This field represents the T24 product the component belongs to. Should be a valid T24 product |
| 3 | `EB.COMPT.NO.PLATFORMS` | `EbComponent_NoPlatforms` | TField |  | Whether or not this component is platform specific or not. For example T24 server code must be compile on different platforms (i.e. types of Unix operating systems) whereas other components are Java based so are platform independent (e.g. Browser). |
| 4 | `EB.COMPT.T24.SERVER` | `EbComponent_T24Server` | TField |  | Whether this component is a T24 server component or not (as opposed to a front-end UI component such as Browser, etc). |
| 5 | `EB.COMPT.RESERVED.7` | `EbComponent_Reserved7` | TField |  |  |
| 6 | `EB.COMPT.RESERVED.6` | `EbComponent_Reserved6` | TField |  |  |
| 7 | `EB.COMPT.RESERVED.5` | `EbComponent_Reserved5` | TField |  |  |
| 8 | `EB.COMPT.RESERVED.4` | `EbComponent_Reserved4` | TField |  |  |
| 9 | `EB.COMPT.RESERVED.3` | `EbComponent_Reserved3` | TField |  |  |
| 10 | `EB.COMPT.RESERVED.2` | `EbComponent_Reserved2` | TField |  |  |
| 11 | `EB.COMPT.RESERVED.1` | `EbComponent_Reserved1` | TField |  |  |
| 12 | `EB.COMPT.LOCAL.REF` | `EbComponent_LocalRef` |  |  |  |
| 13 | `EB.COMPT.RECORD.STATUS` | `EbComponent_RecordStatus` | String |  |  |
| 14 | `EB.COMPT.CURR.NO` | `EbComponent_CurrNo` | String |  |  |
| 15 | `EB.COMPT.INPUTTER` | `EbComponent_Inputter` |  |  |  |
| 16 | `EB.COMPT.DATE.TIME` | `EbComponent_DateTime` |  |  |  |
| 17 | `EB.COMPT.AUTHORISER` | `EbComponent_Authoriser` | String |  |  |
| 18 | `EB.COMPT.CO.CODE` | `EbComponent_CoCode` | String |  |  |
| 19 | `EB.COMPT.DEPT.CODE` | `EbComponent_DeptCode` | String |  |  |
| 20 | `EB.COMPT.AUDITOR.CODE` | `EbComponent_AuditorCode` | String |  |  |
| 21 | `EB.COMPT.AUDIT.DATE.TIME` | `EbComponent_AuditDateTime` | String |  |  |
