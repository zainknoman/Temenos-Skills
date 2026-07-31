# PP.SOURCEPRODUCTGROUP — Table Schema

> Source: `INSERTS/I_F.PP.SOURCEPRODUCTGROUP` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SPG.SourceDescription` | `PpSourceproductgroup_Sourcedescription` |  |  |  |
| 2 | `PP.SPG.RESERVED.5` | `PpSourceproductgroup_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 3 | `PP.SPG.RESERVED.4` | `PpSourceproductgroup_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.SPG.RESERVED.3` | `PpSourceproductgroup_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.SPG.RESERVED.2` | `PpSourceproductgroup_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.SPG.RESERVED.1` | `PpSourceproductgroup_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.SPG.LOCAL.REF` | `PpSourceproductgroup_LocalRef` |  |  |  |
| 8 | `PP.SPG.OVERRIDE` | `PpSourceproductgroup_Override` |  |  |  |
| 9 | `PP.SPG.RECORD.STATUS` | `PpSourceproductgroup_RecordStatus` | String |  |  |
| 10 | `PP.SPG.CURR.NO` | `PpSourceproductgroup_CurrNo` | String |  |  |
| 11 | `PP.SPG.INPUTTER` | `PpSourceproductgroup_Inputter` |  |  |  |
| 12 | `PP.SPG.DATE.TIME` | `PpSourceproductgroup_DateTime` |  |  |  |
| 13 | `PP.SPG.AUTHORISER` | `PpSourceproductgroup_Authoriser` | String |  |  |
| 14 | `PP.SPG.CO.CODE` | `PpSourceproductgroup_CoCode` | String |  |  |
| 15 | `PP.SPG.DEPT.CODE` | `PpSourceproductgroup_DeptCode` | String |  |  |
| 16 | `PP.SPG.AUDITOR.CODE` | `PpSourceproductgroup_AuditorCode` | String |  |  |
| 17 | `PP.SPG.AUDIT.DATE.TIME` | `PpSourceproductgroup_AuditDateTime` | String |  |  |
