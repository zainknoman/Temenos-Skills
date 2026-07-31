# EB.COB.MONITOR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.COB.MONITOR.PARAMETER` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.COB.DESCRIPTION` | `EbCobMonitorParameter_Description` |  |  |  |
| 2 | `EB.COB.COB.STAGE` | `EbCobMonitorParameter_CobStage` |  |  |  |
| 3 | `EB.COB.STAGE.EXP.RUNTIME` | `EbCobMonitorParameter_StageExpRuntime` |  |  |  |
| 4 | `EB.COB.STAGE.THRESHOLD` | `EbCobMonitorParameter_StageThreshold` |  |  |  |
| 5 | `EB.COB.STAGE.TEC.ITEM.ID` | `EbCobMonitorParameter_StageTecItemId` |  |  |  |
| 6 | `EB.COB.COMPANY` | `EbCobMonitorParameter_Company` |  |  |  |
| 7 | `EB.COB.COMPANY.GROUP` | `EbCobMonitorParameter_CompanyGroup` |  |  |  |
| 8 | `EB.COB.EXP.RUNTIME` | `EbCobMonitorParameter_ExpRuntime` |  |  |  |
| 9 | `EB.COB.THRESHOLD` | `EbCobMonitorParameter_Threshold` |  |  |  |
| 10 | `EB.COB.TEC.ITEM.ID` | `EbCobMonitorParameter_TecItemId` |  |  |  |
| 11 | `EB.COB.RESERVED.6` | `EbCobMonitorParameter_Reserved6` | TField |  | Reserved Field |
| 12 | `EB.COB.RESERVED.7` | `EbCobMonitorParameter_Reserved7` | TField |  | Reserved Field |
| 13 | `EB.COB.RESERVED.8` | `EbCobMonitorParameter_Reserved8` | TField |  | Reserved Field |
| 14 | `EB.COB.RESERVED.9` | `EbCobMonitorParameter_Reserved9` | TField |  | Reserved Field |
| 15 | `EB.COB.RESERVED.10` | `EbCobMonitorParameter_Reserved10` | TField |  | Reserved Field |
| 16 | `EB.COB.COB.EXP.RUNTIME` | `EbCobMonitorParameter_CobExpRuntime` | TField |  | Respective COB expected runtime i.e in how much time we are expecting COB to complete. Validation Rules: Time Should of HH:MM format Minutes cannot to be greater that 59 Hours can be defined up to 999 Minutes to be give of MM format but not MMM or so |
| 17 | `EB.COB.COB.THRESHOLD` | `EbCobMonitorParameter_CobThreshold` | TField |  | Percentage threshold for whole COB. Validation Rules: Decimal percentage is allowed Is only input able when COB.TEC.ITEM.ID is not given that is both fields cannot have hold together |
| 18 | `EB.COB.COB.TEC.ITEM.ID` | `EbCobMonitorParameter_CobTecItemId` | TField |  | Valid Tec item id defined in table TEC.ITEMS. Validation rules: Is only input able when COB.THRESHOLD is not given that is both fields cannot have hold together |
| 19 | `EB.COB.COMPANY.FOR.TREND` | `EbCobMonitorParameter_CompanyForTrend` |  |  |  |
| 20 | `EB.COB.JOB.NAME` | `EbCobMonitorParameter_JobName` |  |  |  |
| 21 | `EB.COB.RESERVED.13` | `EbCobMonitorParameter_Reserved13` | TField |  | Reserved Field |
| 22 | `EB.COB.RESERVED.14` | `EbCobMonitorParameter_Reserved14` | TField |  | Reserved Field |
| 23 | `EB.COB.RESERVED.15` | `EbCobMonitorParameter_Reserved15` | TField |  | Reserved Field |
| 24 | `EB.COB.RESERVED.16` | `EbCobMonitorParameter_Reserved16` | TField |  | Reserved Field |
| 25 | `EB.COB.RESERVED.17` | `EbCobMonitorParameter_Reserved17` | TField |  | Reserved Field |
| 26 | `EB.COB.RESERVED.18` | `EbCobMonitorParameter_Reserved18` | TField |  | Reserved Field |
| 27 | `EB.COB.RESERVED.19` | `EbCobMonitorParameter_Reserved19` | TField |  | Reserved Field |
| 28 | `EB.COB.RESERVED.20` | `EbCobMonitorParameter_Reserved20` | TField |  | Reserved Field |
| 29 | `EB.COB.LOCAL.REF` | `EbCobMonitorParameter_LocalRef` |  |  |  |
| 30 | `EB.COB.OVERRIDE` | `EbCobMonitorParameter_Override` |  |  |  |
| 31 | `EB.COB.RECORD.STATUS` | `EbCobMonitorParameter_RecordStatus` | String |  |  |
| 32 | `EB.COB.CURR.NO` | `EbCobMonitorParameter_CurrNo` | String |  |  |
| 33 | `EB.COB.INPUTTER` | `EbCobMonitorParameter_Inputter` |  |  |  |
| 34 | `EB.COB.DATE.TIME` | `EbCobMonitorParameter_DateTime` |  |  |  |
| 35 | `EB.COB.AUTHORISER` | `EbCobMonitorParameter_Authoriser` | String |  |  |
| 36 | `EB.COB.CO.CODE` | `EbCobMonitorParameter_CoCode` | String |  |  |
| 37 | `EB.COB.DEPT.CODE` | `EbCobMonitorParameter_DeptCode` | String |  |  |
| 38 | `EB.COB.AUDITOR.CODE` | `EbCobMonitorParameter_AuditorCode` | String |  |  |
| 39 | `EB.COB.AUDIT.DATE.TIME` | `EbCobMonitorParameter_AuditDateTime` | String |  |  |
