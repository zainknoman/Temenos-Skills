# FS.GA.DESCRIPTION.LANGUAGE — Table Schema

> Source: `INSERTS/I_F.FS.GA.DESCRIPTION.LANGUAGE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DESC.LANG.S.F.O` | `FsGaDescriptionLanguage_SFO` | TField |  | S F O Multifonds DB Column is ID_TYPE. |
| 2 | `DESC.LANG.INTERNAL.SECURITY.ID` | `FsGaDescriptionLanguage_SecurityId` |  |  |  |
| 3 | `DESC.LANG.LANGUAGE.CODE` | `FsGaDescriptionLanguage_LanguageCode` | TField |  | Language code Multifonds DB Column is CLANGUE. |
| 4 | `DESC.LANG.SECURITY.DESCRIPTION` | `FsGaDescriptionLanguage_SecurityDescription` | TField |  | Security description Multifonds DB Column is DESCR. |
| 5 | `DESC.LANG.LONG.DESC` | `FsGaDescriptionLanguage_LongDescription` |  |  |  |
| 6 | `DESC.LANG.DWH.EXPORT` | `FsGaDescriptionLanguage_DwhExport` | TField |  | Dwh Export Multifonds DB Column is DWH_EXPORT. |
| 7 | `DESC.LANG.SPECIFIC.DESCRIPTION` | `FsGaDescriptionLanguage_SpecificDescription` | TField |  | Specific description Multifonds DB Column is DESCR_SPEC. |
| 8 | `DESC.LANG.RECORD.STATUS` | `FsGaDescriptionLanguage_RecordStatus` | String |  |  |
| 9 | `DESC.LANG.CURR.NO` | `FsGaDescriptionLanguage_CurrNo` | String |  |  |
| 10 | `DESC.LANG.INPUTTER` | `FsGaDescriptionLanguage_Inputter` |  |  |  |
| 11 | `DESC.LANG.DATE.TIME` | `FsGaDescriptionLanguage_DateTime` |  |  |  |
| 12 | `DESC.LANG.AUTHORISER` | `FsGaDescriptionLanguage_Authoriser` | String |  |  |
| 13 | `DESC.LANG.CO.CODE` | `FsGaDescriptionLanguage_CoCode` | String |  |  |
| 14 | `DESC.LANG.DEPT.CODE` | `FsGaDescriptionLanguage_DeptCode` | String |  |  |
| 15 | `DESC.LANG.AUDITOR.CODE` | `FsGaDescriptionLanguage_AuditorCode` | String |  |  |
| 16 | `DESC.LANG.AUDIT.DATE.TIME` | `FsGaDescriptionLanguage_AuditDateTime` | String |  |  |
