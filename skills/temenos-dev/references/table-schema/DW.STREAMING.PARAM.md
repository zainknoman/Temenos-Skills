# DW.STREAMING.PARAM — Table Schema

> Source: `INSERTS/I_F.DW.STREAMING.PARAM` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.SP.UTILS.PROPERTIES` | `DwStreamingParam_UtilsProperties` | TField |  | This field stores the Utils properties as json |
| 2 | `DW.SP.RESERVED.6` | `DwStreamingParam_Reserved6` | TField |  |  |
| 3 | `DW.SP.RESERVED.5` | `DwStreamingParam_Reserved5` | TField |  |  |
| 4 | `DW.SP.RESERVED.4` | `DwStreamingParam_Reserved4` | TField |  |  |
| 5 | `DW.SP.RESERVED.3` | `DwStreamingParam_Reserved3` | TField |  |  |
| 6 | `DW.SP.RESERVED.2` | `DwStreamingParam_Reserved2` | TField |  |  |
| 7 | `DW.SP.RESERVED.1` | `DwStreamingParam_Reserved1` | TField |  |  |
| 8 | `DW.SP.RECORD.STATUS` | `DwStreamingParam_RecordStatus` | String |  |  |
| 9 | `DW.SP.CURR.NO` | `DwStreamingParam_CurrNo` | String |  |  |
| 10 | `DW.SP.INPUTTER` | `DwStreamingParam_Inputter` |  |  |  |
| 11 | `DW.SP.DATE.TIME` | `DwStreamingParam_DateTime` |  |  |  |
| 12 | `DW.SP.AUTHORISER` | `DwStreamingParam_Authoriser` | String |  |  |
| 13 | `DW.SP.CO.CODE` | `DwStreamingParam_CoCode` | String |  |  |
| 14 | `DW.SP.DEPT.CODE` | `DwStreamingParam_DeptCode` | String |  |  |
| 15 | `DW.SP.AUDITOR.CODE` | `DwStreamingParam_AuditorCode` | String |  |  |
| 16 | `DW.SP.AUDIT.DATE.TIME` | `DwStreamingParam_AuditDateTime` | String |  |  |
