# DD.CREDITOR.REGISTRY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DD.CREDITOR.REGISTRY.PARAMETER` in `DD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.CRP.LAST.FULL.UPLD.DATE` | `DdCreditorRegistryParameter_LastFullUpldDate` | TField |  | The date of the latest full upload. |
| 2 | `DD.CRP.LASTFULL.UPD.FILE.NAME` | `DdCreditorRegistryParameter_LastfullUpdFileName` | TField |  | The name of the latest full file uploaded. |
| 3 | `DD.CRP.RESERVED.15` | `DdCreditorRegistryParameter_Reserved15` | TField |  |  |
| 4 | `DD.CRP.RESERVED.14` | `DdCreditorRegistryParameter_Reserved14` | TField |  |  |
| 5 | `DD.CRP.RESERVED.13` | `DdCreditorRegistryParameter_Reserved13` | TField |  |  |
| 6 | `DD.CRP.RESERVED.12` | `DdCreditorRegistryParameter_Reserved12` | TField |  |  |
| 7 | `DD.CRP.RESERVED.11` | `DdCreditorRegistryParameter_Reserved11` | TField |  |  |
| 8 | `DD.CRP.RESERVED.10` | `DdCreditorRegistryParameter_Reserved10` | TField |  |  |
| 9 | `DD.CRP.RESERVED.9` | `DdCreditorRegistryParameter_Reserved9` | TField |  |  |
| 10 | `DD.CRP.RESERVED.8` | `DdCreditorRegistryParameter_Reserved8` | TField |  |  |
| 11 | `DD.CRP.RESERVED.7` | `DdCreditorRegistryParameter_Reserved7` | TField |  |  |
| 12 | `DD.CRP.RESERVED.6` | `DdCreditorRegistryParameter_Reserved6` | TField |  |  |
| 13 | `DD.CRP.RESERVED.5` | `DdCreditorRegistryParameter_Reserved5` | TField |  |  |
| 14 | `DD.CRP.RESERVED.4` | `DdCreditorRegistryParameter_Reserved4` | TField |  |  |
| 15 | `DD.CRP.RESERVED.3` | `DdCreditorRegistryParameter_Reserved3` | TField |  |  |
| 16 | `DD.CRP.RESERVED.2` | `DdCreditorRegistryParameter_Reserved2` | TField |  |  |
| 17 | `DD.CRP.RESERVED.1` | `DdCreditorRegistryParameter_Reserved1` | TField |  |  |
| 18 | `DD.CRP.LOCAL.REF` | `DdCreditorRegistryParameter_LocalRef` |  |  |  |
| 19 | `DD.CRP.OVERRIDE` | `DdCreditorRegistryParameter_Override` |  |  |  |
| 20 | `DD.CRP.RECORD.STATUS` | `DdCreditorRegistryParameter_RecordStatus` | String |  |  |
| 21 | `DD.CRP.CURR.NO` | `DdCreditorRegistryParameter_CurrNo` | String |  |  |
| 22 | `DD.CRP.INPUTTER` | `DdCreditorRegistryParameter_Inputter` |  |  |  |
| 23 | `DD.CRP.DATE.TIME` | `DdCreditorRegistryParameter_DateTime` |  |  |  |
| 24 | `DD.CRP.AUTHORISER` | `DdCreditorRegistryParameter_Authoriser` | String |  |  |
| 25 | `DD.CRP.CO.CODE` | `DdCreditorRegistryParameter_CoCode` | String |  |  |
| 26 | `DD.CRP.DEPT.CODE` | `DdCreditorRegistryParameter_DeptCode` | String |  |  |
| 27 | `DD.CRP.AUDITOR.CODE` | `DdCreditorRegistryParameter_AuditorCode` | String |  |  |
| 28 | `DD.CRP.AUDIT.DATE.TIME` | `DdCreditorRegistryParameter_AuditDateTime` | String |  |  |
