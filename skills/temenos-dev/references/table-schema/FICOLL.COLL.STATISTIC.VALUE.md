# FICOLL.COLL.STATISTIC.VALUE — Table Schema

> Source: `INSERTS/I_F.FICOLL.COLL.STATISTIC.VALUE` in `FICOLL_StatisticsProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.STAT.SV.INDEX.VALUE` | `FicollCollStatisticValue_SvIndexValue` | TField |  | Latest Statistical index value to be defined here. |
| 2 | `FICOLL.STAT.SV.INDEX.UPDATE.DATE` | `FicollCollStatisticValue_SvIndexUpdateDate` | TField |  | Statistical index value update date in T24. |
| 3 | `FICOLL.STAT.STATISTICS.VALUE` | `FicollCollStatisticValue_StatisticsValue` | TField |  | System calculates the statistical value once latest index value is fed into T24. |
| 4 | `FICOLL.STAT.NOMINAL.INDEX.VALUE` | `FicollCollStatisticValue_NominalIndexValue` | TField |  | Index value used for calculating the nominal value. |
| 5 | `FICOLL.STAT.NOM.INDEX.REVIEW.DATE` | `FicollCollStatisticValue_NomIndexReviewDate` | TField |  | Review date of Nominal index value. |
| 6 | `FICOLL.STAT.POSTAL.CODE` | `FicollCollStatisticValue_PostalCode` | TField |  | Customer postal code as part of address detail to be defined here. |
| 7 | `FICOLL.STAT.HC.BUILDING.CATEG` | `FicollCollStatisticValue_HcBuildingCateg` | TField |  | Housing Collateral building category to be defined here. |
| 8 | `FICOLL.STAT.LOCAL.REF` | `FicollCollStatisticValue_LocalRef` |  |  |  |
| 9 | `FICOLL.STAT.OVERRIDE` | `FicollCollStatisticValue_Override` |  |  |  |
| 10 | `FICOLL.STAT.RECORD.STATUS` | `FicollCollStatisticValue_RecordStatus` | String |  |  |
| 11 | `FICOLL.STAT.CURR.NO` | `FicollCollStatisticValue_CurrNo` | String |  |  |
| 12 | `FICOLL.STAT.INPUTTER` | `FicollCollStatisticValue_Inputter` |  |  |  |
| 13 | `FICOLL.STAT.DATE.TIME` | `FicollCollStatisticValue_DateTime` |  |  |  |
| 14 | `FICOLL.STAT.AUTHORISER` | `FicollCollStatisticValue_Authoriser` | String |  |  |
| 15 | `FICOLL.STAT.CO.CODE` | `FicollCollStatisticValue_CoCode` | String |  |  |
| 16 | `FICOLL.STAT.DEPT.CODE` | `FicollCollStatisticValue_DeptCode` | String |  |  |
| 17 | `FICOLL.STAT.AUDITOR.CODE` | `FicollCollStatisticValue_AuditorCode` | String |  |  |
| 18 | `FICOLL.STAT.AUDIT.DATE.TIME` | `FicollCollStatisticValue_AuditDateTime` | String |  |  |
