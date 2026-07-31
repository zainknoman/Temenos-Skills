# SC.ESG.SCORES — Table Schema

> Source: `INSERTS/I_F.SC.ESG.SCORES` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ESGS.SECURITY.NO` | `ScEsgScores_SecurityNo` | TField |  | This field holds the security no. Automatically defaulted based on the ID NOINPUT field. |
| 2 | `SC.ESGS.SC.ISSUER` | `ScEsgScores_ScIssuer` | TField |  | This field holds the SC.ISSUER ID. Automatically defaulted based on the ID NOINPUT field |
| 3 | `SC.ESGS.ISSUER.ID` | `ScEsgScores_IssuerId` | TField |  | This field holds the Issuer record id Automatically defaulted based on the ID NOINPUT field |
| 4 | `SC.ESGS.PROVIDER` | `ScEsgScores_Provider` | TField |  | This field holds the Provider. Automatically defaulted based on the ID NOINPUT field |
| 5 | `SC.ESGS.OVERALL.RATING` | `ScEsgScores_OverallRating` | TField |  | This field holds the overall rating of the instrument or issuer. |
| 6 | `SC.ESGS.RATING.OVERALL.SCORE` | `ScEsgScores_RatingOverallScore` | TField |  | This field holds the overall rating score |
| 7 | `SC.ESGS.RATING.E.PILLAR.SCORE` | `ScEsgScores_RatingEPillarScore` | TField |  | This field holds the environmental pillar rating score. |
| 8 | `SC.ESGS.RATING.E.WEIGHT` | `ScEsgScores_RatingEWeight` | TField |  | This field holds the environmental pillar rating weight. |
| 9 | `SC.ESGS.RATING.S.PILLAR.SCORE` | `ScEsgScores_RatingSPillarScore` | TField |  | This field holds the social pillar rating score. |
| 10 | `SC.ESGS.RATING.S.WEIGHT` | `ScEsgScores_RatingSWeight` | TField |  | This field holds the social pillar rating weight. |
| 11 | `SC.ESGS.RATING.G.PILLAR.SCORE` | `ScEsgScores_RatingGPillarScore` | TField |  | This field holds the governance pillar rating score. |
| 12 | `SC.ESGS.RATING.G.WEIGHT` | `ScEsgScores_RatingGWeight` | TField |  | This field holds the governance pillar rating weight. |
| 13 | `SC.ESGS.CONTROVERSY.OVERALL.SCORE` | `ScEsgScores_ControversyOverallScore` | TField |  | This field holds the overall controversy score |
| 14 | `SC.ESGS.CONTROVERSY.OVERALL.SUMMARY` | `ScEsgScores_ControversyOverallSummary` |  |  |  |
| 15 | `SC.ESGS.CONTROVERSY.OVERALL.FLAG` | `ScEsgScores_ControversyOverallFlag` | TField |  | This field holds the overall controversy flag |
| 16 | `SC.ESGS.CONTROVERSY.E.PILLAR.SCORE` | `ScEsgScores_ControversyEPillarScore` | TField |  | This field holds the environmental pillar controversy score. |
| 17 | `SC.ESGS.CONTROVERSY.E.FLAG` | `ScEsgScores_ControversyEFlag` | TField |  | This field holds the environmental pillar controversy flag. |
| 18 | `SC.ESGS.CONTROVERSY.S.PILLAR.SCORE` | `ScEsgScores_ControversySPillarScore` | TField |  | This field holds the social pillar controversy score. |
| 19 | `SC.ESGS.CONTROVERSY.S.FLAG` | `ScEsgScores_ControversySFlag` | TField |  | This field holds the social pillar controversy flag. |
| 20 | `SC.ESGS.CONTROVERSY.G.PILLAR.SCORE` | `ScEsgScores_ControversyGPillarScore` | TField |  | This field holds the governance pillar controversy score. |
| 21 | `SC.ESGS.CONTROVERSY.G.FLAG` | `ScEsgScores_ControversyGFlag` | TField |  | This field holds the governance pillar controversy flag. |
| 22 | `SC.ESGS.INDICATOR.CATEGORY` | `ScEsgScores_IndicatorCategory` |  |  |  |
| 23 | `SC.ESGS.CATEGORY.UPDATE.DATE` | `ScEsgScores_CategoryUpdateDate` |  |  |  |
| 24 | `SC.ESGS.INDICATOR` | `ScEsgScores_Indicator` |  |  |  |
| 25 | `SC.ESGS.INDICATOR.VALUE` | `ScEsgScores_IndicatorValue` |  |  |  |
| 26 | `SC.ESGS.RESERVED.01` | `ScEsgScores_Reserved01` |  |  |  |
| 27 | `SC.ESGS.RESERVED.02` | `ScEsgScores_Reserved02` |  |  |  |
| 28 | `SC.ESGS.RESERVED.03` | `ScEsgScores_Reserved03` | TField |  |  |
| 29 | `SC.ESGS.RESERVED.04` | `ScEsgScores_Reserved04` | TField |  |  |
| 30 | `SC.ESGS.RESERVED.05` | `ScEsgScores_Reserved05` | TField |  |  |
| 31 | `SC.ESGS.LOCAL.REF` | `ScEsgScores_LocalRef` |  |  |  |
| 32 | `SC.ESGS.OVERRIDE` | `ScEsgScores_Override` |  |  |  |
| 33 | `SC.ESGS.RECORD.STATUS` | `ScEsgScores_RecordStatus` | String |  |  |
| 34 | `SC.ESGS.CURR.NO` | `ScEsgScores_CurrNo` | String |  |  |
| 35 | `SC.ESGS.INPUTTER` | `ScEsgScores_Inputter` |  |  |  |
| 36 | `SC.ESGS.DATE.TIME` | `ScEsgScores_DateTime` |  |  |  |
| 37 | `SC.ESGS.AUTHORISER` | `ScEsgScores_Authoriser` | String |  |  |
| 38 | `SC.ESGS.CO.CODE` | `ScEsgScores_CoCode` | String |  |  |
| 39 | `SC.ESGS.DEPT.CODE` | `ScEsgScores_DeptCode` | String |  |  |
| 40 | `SC.ESGS.AUDITOR.CODE` | `ScEsgScores_AuditorCode` | String |  |  |
| 41 | `SC.ESGS.AUDIT.DATE.TIME` | `ScEsgScores_AuditDateTime` | String |  |  |
