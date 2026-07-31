# LKPVCO.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LKPVCO.PARAMETER` in `LKPVCO_ProvisioningandCollateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKPVCO.PARAM.COLLATERAL.TYPE` | `LkpvcoParameter_CollateralType` |  |  |  |
| 2 | `LKPVCO.PARAM.VERSION` | `LkpvcoParameter_Version` |  |  |  |
| 3 | `LKPVCO.PARAM.SECURITY.PERCENTAGE` | `LkpvcoParameter_SecurityPercentage` |  |  |  |
| 4 | `LKPVCO.PARAM.LOAN.CLASSIFICATION` | `LkpvcoParameter_LoanClassification` |  |  |  |
| 5 | `LKPVCO.PARAM.AGEING.CRITERIA` | `LkpvcoParameter_AgeingCriteria` |  |  |  |
| 6 | `LKPVCO.PARAM.EXT.PROD.GRP` | `LkpvcoParameter_ExtProdGrp` |  |  |  |
| 7 | `LKPVCO.PARAM.CLASS.PERCENTAGE` | `LkpvcoParameter_ClassPercentage` | TField |  | The percentage value provide this field we will check against with the percentage calculated as part of 30:70 classification. |
| 8 | `LKPVCO.PARAM.LOC` | `LkpvcoParameter_Loc` | TField |  | Yes or NO field to indicate if the LC exposures of clients need to be included |
| 9 | `LKPVCO.PARAM.LC.TYPE` | `LkpvcoParameter_LcType` |  |  |  |
| 10 | `LKPVCO.PARAM.MD.DEAL` | `LkpvcoParameter_MdDeal` | TField |  | Yes or NO field to indicate if the LC exposures of clients need to be included |
| 11 | `LKPVCO.PARAM.MD.DEAL.TYPE` | `LkpvcoParameter_MdDealType` |  |  |  |
| 12 | `LKPVCO.PARAM.GRACE.DAYS` | `LkpvcoParameter_GraceDays` | TField |  | Refers to the number of days to be considered for the declassification to be applied for the 30:70 rule |
| 13 | `LKPVCO.PARAM.PRODUCT` | `LkpvcoParameter_Product` |  |  |  |
| 14 | `LKPVCO.PARAM.LOCAL.REF` | `LkpvcoParameter_LocalRef` |  |  |  |
| 15 | `LKPVCO.PARAM.OVERRIDE` | `LkpvcoParameter_Override` |  |  |  |
| 16 | `LKPVCO.PARAM.RECORD.STATUS` | `LkpvcoParameter_RecordStatus` | String |  |  |
| 17 | `LKPVCO.PARAM.CURR.NO` | `LkpvcoParameter_CurrNo` | String |  |  |
| 18 | `LKPVCO.PARAM.INPUTTER` | `LkpvcoParameter_Inputter` |  |  |  |
| 19 | `LKPVCO.PARAM.DATE.TIME` | `LkpvcoParameter_DateTime` |  |  |  |
| 20 | `LKPVCO.PARAM.AUTHORISER` | `LkpvcoParameter_Authoriser` | String |  |  |
| 21 | `LKPVCO.PARAM.CO.CODE` | `LkpvcoParameter_CoCode` | String |  |  |
| 22 | `LKPVCO.PARAM.DEPT.CODE` | `LkpvcoParameter_DeptCode` | String |  |  |
| 23 | `LKPVCO.PARAM.AUDITOR.CODE` | `LkpvcoParameter_AuditorCode` | String |  |  |
| 24 | `LKPVCO.PARAM.AUDIT.DATE.TIME` | `LkpvcoParameter_AuditDateTime` | String |  |  |
| 25 | `LKPVCO.PARAM.SUB.PRODUCT` | `LkpvcoParameter_SubProduct` |  |  |  |
| 26 | `LKPVCO.PARAM.RANKING` | `LkpvcoParameter_Ranking` |  |  |  |
| 27 | `LKPVCO.PARAM.HAIRCUT.RATE` | `LkpvcoParameter_HaircutRate` |  |  |  |
| 28 | `LKPVCO.PARAM.PERF.CLASS` | `LkpvcoParameter_PerfClass` | TField |  | Classification to be considered as performing class |
| 29 | `LKPVCO.PARAM.NPL.CLASS` | `LkpvcoParameter_NplClass` |  |  |  |
| 30 | `LKPVCO.PARAM.CLASS.FREQUENCY` | `LkpvcoParameter_ClassFrequency` | TField |  | If the field CLASS FREQUENCY is set as Monthly then 30:70 classification happen on monthly basis.If not it will happen on Daily basis. |
