# SC.INDUSTRY — Table Schema

> Source: `INSERTS/I_F.SC.INDUSTRY` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.IND.DESCRIPTION` | `ScIndustry_Description` |  |  |  |
| 2 | `SC.IND.GROUP.SECTOR` | `ScIndustry_GroupSector` | TField |  | Validation Rules: Up to 20 Alphanumeric (type A) characters. |
| 3 | `SC.IND.SECTOR.SPLIT.NO` | `ScIndustry_SectorSplitNo` | TField |  | Validation Rules: Up to 1 Numeric character. |
| 4 | `SC.IND.GICS.CODE` | `ScIndustry_GicsCode` | TField |  | Field identifies whether ID is GICS Complaint Validation Rules: Options allowed is YES,NO Default value is Blank If the value is YES ,then system will auto populate GICS structure hierarchy levels(SECTOR,INDUSTRY.GROUP,INDUSTRY,SUB.INDUSTRY) |
| 5 | `SC.IND.SECTOR` | `ScIndustry_Sector` | TField |  | Field identifies First level of GICS structure hierarchy Validation Rules: If field GICS code is set to YES, system will automatically update the first 2 digits of the ID in this field It will be a no-input field The enrichment for this field will be shown from EB.LOOKUP record GICS.INDUSTRY |
| 6 | `SC.IND.INDUSTRY.GROUP` | `ScIndustry_IndustryGroup` | TField |  |  |
| 7 | `SC.IND.INDUSTRY` | `ScIndustry_Industry` | TField |  | Field identifies Third level of GICS structure hierarchy Validation Rules: If field GICS code is set to YES, system will automatically update the first 6 digits of the ID in this field if length greater than 4 It will be a no-input field The enrichment for this field will be shown from EB.LOOKUP record GICS.INDUSTRY |
| 8 | `SC.IND.SUB.INDUSTRY` | `ScIndustry_SubIndustry` | TField |  | Field identifies Fourth level of GICS structure hierarchy Validation Rules: If field GICS code is set to YES, system will automatically update the the ID to this field if length greater than 6 It will be a no-input field The enrichment for this field will be shown from EB.LOOKUP record GICS.INDUSTRY |
| 9 | `SC.IND.LOCAL.REF` | `ScIndustry_LocalRef` |  |  |  |
| 10 | `SC.IND.RECORD.STATUS` | `ScIndustry_RecordStatus` | String |  |  |
| 11 | `SC.IND.CURR.NO` | `ScIndustry_CurrNo` | String |  |  |
| 12 | `SC.IND.INPUTTER` | `ScIndustry_Inputter` |  |  |  |
| 13 | `SC.IND.DATE.TIME` | `ScIndustry_DateTime` |  |  |  |
| 14 | `SC.IND.AUTHORISER` | `ScIndustry_Authoriser` | String |  |  |
| 15 | `SC.IND.CO.CODE` | `ScIndustry_CoCode` | String |  |  |
| 16 | `SC.IND.DEPT.CODE` | `ScIndustry_DeptCode` | String |  |  |
| 17 | `SC.IND.AUDITOR.CODE` | `ScIndustry_AuditorCode` | String |  |  |
| 18 | `SC.IND.AUDIT.DATE.TIME` | `ScIndustry_AuditDateTime` | String |  |  |
