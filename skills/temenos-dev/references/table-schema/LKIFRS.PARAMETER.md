# LKIFRS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LKIFRS.PARAMETER` in `LKIFRS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKIFRS.PARAM.PRODUCT` | `LkifrsParameter_Product` |  |  |  |
| 2 | `LKIFRS.PARAM.CRITERIA` | `LkifrsParameter_Criteria` |  |  |  |
| 3 | `LKIFRS.PARAM.CRITERIA.APPLICATION` | `LkifrsParameter_CriteriaApplication` |  |  |  |
| 4 | `LKIFRS.PARAM.CRITERIA.APPL.FIELD` | `LkifrsParameter_CriteriaApplField` |  |  |  |
| 5 | `LKIFRS.PARAM.CRITERIA.LOGIC` | `LkifrsParameter_CriteriaLogic` |  |  |  |
| 6 | `LKIFRS.PARAM.SECTOR.START` | `LkifrsParameter_SectorStart` |  |  |  |
| 7 | `LKIFRS.PARAM.SECTOR.END` | `LkifrsParameter_SectorEnd` |  |  |  |
| 8 | `LKIFRS.PARAM.SEGMENT` | `LkifrsParameter_Segment` |  |  |  |
| 9 | `LKIFRS.PARAM.PV.PROFILE` | `LkifrsParameter_PvProfile` |  |  |  |
| 10 | `LKIFRS.PARAM.DEF.PRODUCT` | `LkifrsParameter_DefProduct` |  |  |  |
| 11 | `LKIFRS.PARAM.DEF.CLASS` | `LkifrsParameter_DefClass` | TField |  | Refers to the default classification to be assigned to the LC and MD contracts in case there are no user defined classification. |
| 12 | `LKIFRS.PARAM.LOCAL.REF` | `LkifrsParameter_LocalRef` |  |  |  |
| 13 | `LKIFRS.PARAM.OVERRIDE` | `LkifrsParameter_Override` |  |  |  |
| 14 | `LKIFRS.PARAM.RECORD.STATUS` | `LkifrsParameter_RecordStatus` | String |  |  |
| 15 | `LKIFRS.PARAM.CURR.NO` | `LkifrsParameter_CurrNo` | String |  |  |
| 16 | `LKIFRS.PARAM.INPUTTER` | `LkifrsParameter_Inputter` |  |  |  |
| 17 | `LKIFRS.PARAM.DATE.TIME` | `LkifrsParameter_DateTime` |  |  |  |
| 18 | `LKIFRS.PARAM.AUTHORISER` | `LkifrsParameter_Authoriser` | String |  |  |
| 19 | `LKIFRS.PARAM.CO.CODE` | `LkifrsParameter_CoCode` | String |  |  |
| 20 | `LKIFRS.PARAM.DEPT.CODE` | `LkifrsParameter_DeptCode` | String |  |  |
| 21 | `LKIFRS.PARAM.AUDITOR.CODE` | `LkifrsParameter_AuditorCode` | String |  |  |
| 22 | `LKIFRS.PARAM.AUDIT.DATE.TIME` | `LkifrsParameter_AuditDateTime` | String |  |  |
