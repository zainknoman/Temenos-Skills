# RMA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.RMA.PARAMETER` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.RMAP.DESCRIPTION` | `RmaParameter_Description` | TField | Yes | Description of the Parameter Record Validations: Mandatory text field |
| 2 | `DE.RMAP.ENHANCED.DIRECTORY` | `RmaParameter_EnhancedDirectory` | TField |  | Indicates if the RMA processing is enhanced to handle RMA authorisations per service Validations: Option field with Yes and Null options. By default, it is null. Once set as YES will not be allowed to change back to no or null. |
| 3 | `DE.RMAP.DEFAULT.MT.SERVICE` | `RmaParameter_DefaultMtService` | TField | Yes | Indicates the default swift service for MT messages swift.fin will be suggested Validations: String type field. If ENHANCED.DIRECTORY is set as YES this field is mandatory |
| 4 | `DE.RMAP.DEFAULT.MX.SERVICE` | `RmaParameter_DefaultMxService` | TField | Yes | Indicates the default swift service for MX messages swift.finplus will be suggested Validations: String type field. If ENHANCED.DIRECTORY is set as YES this field is mandatory |
| 5 | `DE.RMAP.RESERVED.10` | `RmaParameter_Reserved10` | TField |  |  |
| 6 | `DE.RMAP.RESERVED.9` | `RmaParameter_Reserved6` | TField |  |  |
| 7 | `DE.RMAP.RESERVED.8` | `RmaParameter_Reserved8` | TField |  |  |
| 8 | `DE.RMAP.RESERVED.7` | `RmaParameter_Reserved7` | TField |  |  |
| 9 | `DE.RMAP.RESERVED.6` | `RmaParameter_Reserved6` | TField |  |  |
| 10 | `DE.RMAP.RESERVED.5` | `RmaParameter_Reserved5` | TField |  |  |
| 11 | `DE.RMAP.RESERVED.4` | `RmaParameter_Reserved4` | TField |  |  |
| 12 | `DE.RMAP.RESERVED.3` | `RmaParameter_Reserved3` | TField |  |  |
| 13 | `DE.RMAP.RESERVED.2` | `RmaParameter_Reserved2` | TField |  |  |
| 14 | `DE.RMAP.RESERVED.1` | `RmaParameter_Reserved1` | TField |  |  |
| 15 | `DE.RMAP.LOCAL.REF` | `RmaParameter_LocalRef` |  |  |  |
| 16 | `DE.RMAP.OVERRIDE` | `RmaParameter_Override` |  |  |  |
| 17 | `DE.RMAP.RECORD.STATUS` | `RmaParameter_RecordStatus` | String |  |  |
| 18 | `DE.RMAP.CURR.NO` | `RmaParameter_CurrNo` | String |  |  |
| 19 | `DE.RMAP.INPUTTER` | `RmaParameter_Inputter` |  |  |  |
| 20 | `DE.RMAP.DATE.TIME` | `RmaParameter_DateTime` |  |  |  |
| 21 | `DE.RMAP.AUTHORISER` | `RmaParameter_Authoriser` | String |  |  |
| 22 | `DE.RMAP.CO.CODE` | `RmaParameter_CoCode` | String |  |  |
| 23 | `DE.RMAP.DEPT.CODE` | `RmaParameter_DeptCode` | String |  |  |
| 24 | `DE.RMAP.AUDITOR.CODE` | `RmaParameter_AuditorCode` | String |  |  |
| 25 | `DE.RMAP.AUDIT.DATE.TIME` | `RmaParameter_AuditDateTime` | String |  |  |
