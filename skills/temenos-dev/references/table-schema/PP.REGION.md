# PP.REGION — Table Schema

> Source: `INSERTS/I_F.PP.REGION` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.TRG.Region` | `PpRegion_Region` |  |  |  |
| 2 | `PP.TRG.RESERVED.5` | `PpRegion_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 3 | `PP.TRG.RESERVED.4` | `PpRegion_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.TRG.RESERVED.3` | `PpRegion_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.TRG.RESERVED.2` | `PpRegion_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.TRG.RESERVED.1` | `PpRegion_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.TRG.LOCAL.REF` | `PpRegion_LocalRef` |  |  |  |
| 8 | `PP.TRG.OVERRIDE` | `PpRegion_Override` |  |  |  |
| 9 | `PP.TRG.RECORD.STATUS` | `PpRegion_RecordStatus` | String |  |  |
| 10 | `PP.TRG.CURR.NO` | `PpRegion_CurrNo` | String |  |  |
| 11 | `PP.TRG.INPUTTER` | `PpRegion_Inputter` |  |  |  |
| 12 | `PP.TRG.DATE.TIME` | `PpRegion_DateTime` |  |  |  |
| 13 | `PP.TRG.AUTHORISER` | `PpRegion_Authoriser` | String |  |  |
| 14 | `PP.TRG.CO.CODE` | `PpRegion_CoCode` | String |  |  |
| 15 | `PP.TRG.DEPT.CODE` | `PpRegion_DeptCode` | String |  |  |
| 16 | `PP.TRG.AUDITOR.CODE` | `PpRegion_AuditorCode` | String |  |  |
| 17 | `PP.TRG.AUDIT.DATE.TIME` | `PpRegion_AuditDateTime` | String |  |  |
