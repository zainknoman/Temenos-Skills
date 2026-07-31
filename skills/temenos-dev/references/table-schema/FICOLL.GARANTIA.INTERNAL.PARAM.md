# FICOLL.GARANTIA.INTERNAL.PARAM — Table Schema

> Source: `INSERTS/I_F.FICOLL.GARANTIA.INTERNAL.PARAM` in `FICOLL_GuarantiaGuarantee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.GARANTIAINTPARAM.PROPERTY.PURPOSE` | `FicollGarantiaInternalParam_PropertyPurpose` |  |  |  |
| 2 | `FICOLL.GARANTIAINTPARAM.RISK.AREA.BAND` | `FicollGarantiaInternalParam_RiskAreaBand` |  |  |  |
| 3 | `FICOLL.GARANTIAINTPARAM.COST.PCT.GARANTIA` | `FicollGarantiaInternalParam_CostPctGarantia` |  |  |  |
| 4 | `FICOLL.GARANTIAINTPARAM.COST.PCT.BANK.SHARE` | `FicollGarantiaInternalParam_CostPctBankShare` |  |  |  |
| 5 | `FICOLL.GARANTIAINTPARAM.INT.AREA.CODE` | `FicollGarantiaInternalParam_IntAreaCode` |  |  |  |
| 6 | `FICOLL.GARANTIAINTPARAM.RISK.AREA.PCT` | `FicollGarantiaInternalParam_RiskAreaPct` |  |  |  |
| 7 | `FICOLL.GARANTIAINTPARAM.MINIM.RISK.AREA.PCT` | `FicollGarantiaInternalParam_MinimRiskAreaPct` | TField |  | The minium risk percentage to be defined. |
| 8 | `FICOLL.GARANTIAINTPARAM.RISK.AREA.CODE` | `FicollGarantiaInternalParam_RiskAreaCode` |  |  |  |
| 9 | `FICOLL.GARANTIAINTPARAM.INT.PURPOSE.AMT.LIVING` | `FicollGarantiaInternalParam_IntPurposeAmtLiving` |  |  |  |
| 10 | `FICOLL.GARANTIAINTPARAM.INT.PURPOSE.AMT.INVEST` | `FicollGarantiaInternalParam_IntPurposeAmtInvest` |  |  |  |
| 11 | `FICOLL.GARANTIAINTPARAM.LOCAL.REF` | `FicollGarantiaInternalParam_LocalRef` |  |  |  |
| 12 | `FICOLL.GARANTIAINTPARAM.OVERRIDE` | `FicollGarantiaInternalParam_Override` |  |  |  |
| 13 | `FICOLL.GARANTIAINTPARAM.RECORD.STATUS` | `FicollGarantiaInternalParam_RecordStatus` | String |  |  |
| 14 | `FICOLL.GARANTIAINTPARAM.CURR.NO` | `FicollGarantiaInternalParam_CurrNo` | String |  |  |
| 15 | `FICOLL.GARANTIAINTPARAM.INPUTTER` | `FicollGarantiaInternalParam_Inputter` |  |  |  |
| 16 | `FICOLL.GARANTIAINTPARAM.DATE.TIME` | `FicollGarantiaInternalParam_DateTime` |  |  |  |
| 17 | `FICOLL.GARANTIAINTPARAM.AUTHORISER` | `FicollGarantiaInternalParam_Authoriser` | String |  |  |
| 18 | `FICOLL.GARANTIAINTPARAM.CO.CODE` | `FicollGarantiaInternalParam_CoCode` | String |  |  |
| 19 | `FICOLL.GARANTIAINTPARAM.DEPT.CODE` | `FicollGarantiaInternalParam_DeptCode` | String |  |  |
| 20 | `FICOLL.GARANTIAINTPARAM.AUDITOR.CODE` | `FicollGarantiaInternalParam_AuditorCode` | String |  |  |
| 21 | `FICOLL.GARANTIAINTPARAM.AUDIT.DATE.TIME` | `FicollGarantiaInternalParam_AuditDateTime` | String |  |  |
