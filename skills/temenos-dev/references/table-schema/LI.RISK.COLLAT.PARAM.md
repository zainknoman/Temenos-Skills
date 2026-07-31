# LI.RISK.COLLAT.PARAM — Table Schema

> Source: `INSERTS/I_F.LI.RISK.COLLAT.PARAM` in `LI_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.RCP.RISK.CODE` | `LiRiskCollatParam_RiskCode` |  |  |  |
| 2 | `LI.RCP.RISK.PERCENTAGE` | `LiRiskCollatParam_RiskPercentage` |  |  |  |
| 3 | `LI.RCP.RISK.NARR` | `LiRiskCollatParam_RiskNarr` |  |  |  |
| 4 | `LI.RCP.COLLAT.CODE` | `LiRiskCollatParam_CollatCode` |  |  |  |
| 5 | `LI.RCP.COLLAT.PRCNTG` | `LiRiskCollatParam_CollatPrcntg` |  |  |  |
| 6 | `LI.RCP.COLAT.NAR` | `LiRiskCollatParam_ColatNar` |  |  |  |
| 7 | `LI.RCP.COLLAT.ACCT.CD` | `LiRiskCollatParam_CollatAcctCd` |  |  |  |
| 8 | `LI.RCP.FX.PROD.CD` | `LiRiskCollatParam_FxProdCd` |  |  |  |
| 9 | `LI.RCP.RESERVE.1` | `LiRiskCollatParam_Reserve1` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 10 | `LI.RCP.RESERVE.2` | `LiRiskCollatParam_Reserve2` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 11 | `LI.RCP.RESERVE.3` | `LiRiskCollatParam_Reserve3` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 12 | `LI.RCP.LOCAL.REF` | `LiRiskCollatParam_LocalRef` |  |  |  |
| 13 | `LI.RCP.RESERVE.5` | `LiRiskCollatParam_Reserve5` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 14 | `LI.RCP.RECORD.STATUS` | `LiRiskCollatParam_RecordStatus` | String |  |  |
| 15 | `LI.RCP.CURR.NO` | `LiRiskCollatParam_CurrNo` | String |  |  |
| 16 | `LI.RCP.INPUTTER` | `LiRiskCollatParam_Inputter` |  |  |  |
| 17 | `LI.RCP.DATE.TIME` | `LiRiskCollatParam_DateTime` |  |  |  |
| 18 | `LI.RCP.AUTHORISER` | `LiRiskCollatParam_Authoriser` | String |  |  |
| 19 | `LI.RCP.CO.CODE` | `LiRiskCollatParam_CoCode` | String |  |  |
| 20 | `LI.RCP.DEPT.CODE` | `LiRiskCollatParam_DeptCode` | String |  |  |
| 21 | `LI.RCP.AUDITOR.CODE` | `LiRiskCollatParam_AuditorCode` | String |  |  |
| 22 | `LI.RCP.AUDIT.DATE.TIME` | `LiRiskCollatParam_AuditDateTime` | String |  |  |
