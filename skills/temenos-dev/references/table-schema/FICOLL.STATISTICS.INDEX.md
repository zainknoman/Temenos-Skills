# FICOLL.STATISTICS.INDEX — Table Schema

> Source: `INSERTS/I_F.FICOLL.STATISTICS.INDEX` in `FICOLL_StatisticsProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.IND.HC.BUILDING.TYPE` | `FicollStatisticsIndex_HcBuildingType` |  |  |  |
| 2 | `FICOLL.IND.HC.BUILDING.CATEG` | `FicollStatisticsIndex_HcBuildingCateg` |  |  |  |
| 3 | `FICOLL.IND.HC.INDEX.PRICE` | `FicollStatisticsIndex_HcIndexPrice` |  |  |  |
| 4 | `FICOLL.IND.DC.INDEX.PRICE` | `FicollStatisticsIndex_DcIndexPrice` | TField |  | Detached house type statistical Index price to be defined here. |
| 5 | `FICOLL.IND.LOCAL.REF` | `FicollStatisticsIndex_LocalRef` |  |  |  |
| 6 | `FICOLL.IND.OVERRIDE` | `FicollStatisticsIndex_Override` |  |  |  |
| 7 | `FICOLL.IND.RECORD.STATUS` | `FicollStatisticsIndex_RecordStatus` | String |  |  |
| 8 | `FICOLL.IND.CURR.NO` | `FicollStatisticsIndex_CurrNo` | String |  |  |
| 9 | `FICOLL.IND.INPUTTER` | `FicollStatisticsIndex_Inputter` |  |  |  |
| 10 | `FICOLL.IND.DATE.TIME` | `FicollStatisticsIndex_DateTime` |  |  |  |
| 11 | `FICOLL.IND.AUTHORISER` | `FicollStatisticsIndex_Authoriser` | String |  |  |
| 12 | `FICOLL.IND.CO.CODE` | `FicollStatisticsIndex_CoCode` | String |  |  |
| 13 | `FICOLL.IND.DEPT.CODE` | `FicollStatisticsIndex_DeptCode` | String |  |  |
| 14 | `FICOLL.IND.AUDITOR.CODE` | `FicollStatisticsIndex_AuditorCode` | String |  |  |
| 15 | `FICOLL.IND.AUDIT.DATE.TIME` | `FicollStatisticsIndex_AuditDateTime` | String |  |  |
