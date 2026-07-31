# INLEND.AA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.INLEND.AA.PARAMETER` in `INLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.AA.AA.PRODUCT` | `InlendAaParameter_AaProduct` |  |  |  |
| 2 | `INLEND.AA.ROLLOVER.SUSP.CATEG` | `InlendAaParameter_RolloverSuspCateg` |  |  |  |
| 3 | `INLEND.AA.FCY.ADV.HEDGED.PROP.CLS` | `InlendAaParameter_FcyAdvHedgedPropCls` |  |  |  |
| 4 | `INLEND.AA.FCY.ADV.HEDGED.PROP.FLD` | `InlendAaParameter_FcyAdvHedgedPropFld` |  |  |  |
| 5 | `INLEND.AA.LOCAL.REF` | `InlendAaParameter_LocalRef` |  |  |  |
| 6 | `INLEND.AA.OVERRIDE` | `InlendAaParameter_Override` |  |  |  |
| 7 | `INLEND.AA.RECORD.STATUS` | `InlendAaParameter_RecordStatus` | String |  |  |
| 8 | `INLEND.AA.CURR.NO` | `InlendAaParameter_CurrNo` | String |  |  |
| 9 | `INLEND.AA.INPUTTER` | `InlendAaParameter_Inputter` |  |  |  |
| 10 | `INLEND.AA.DATE.TIME` | `InlendAaParameter_DateTime` |  |  |  |
| 11 | `INLEND.AA.AUTHORISER` | `InlendAaParameter_Authoriser` | String |  |  |
| 12 | `INLEND.AA.CO.CODE` | `InlendAaParameter_CoCode` | String |  |  |
| 13 | `INLEND.AA.DEPT.CODE` | `InlendAaParameter_DeptCode` | String |  |  |
| 14 | `INLEND.AA.AUDITOR.CODE` | `InlendAaParameter_AuditorCode` | String |  |  |
| 15 | `INLEND.AA.AUDIT.DATE.TIME` | `InlendAaParameter_AuditDateTime` | String |  |  |
| 16 | `INLEND.AA.RESTRUCTURE.AA.PRODUCT` | `InlendAaParameter_RestructureAaProduct` | TField |  | This will be the field that will contain the AA Product which will be used for Restructuring. |
| 17 | `INLEND.AA.ARRANGEMENT.STATUS` | `InlendAaParameter_ArrangementStatus` | TField |  | Drop down from the table PV.LOAN.CLASSIFICATION. |
| 18 | `INLEND.AA.NPA.STATUS` | `InlendAaParameter_NpaStatus` | TField |  | Drop down from the table PV.LOAN.CLASSIFICATION. |
| 19 | `INLEND.AA.REVIEW.PERIOD` | `InlendAaParameter_ReviewPeriod` | TField |  | This field will contain the value of the review time to be considered for a restructured loan to be upgraded based on the health of the loan. |
| 20 | `INLEND.AA.CURR.NPA.STATUS` | `InlendAaParameter_CurrNpaStatus` | TField |  | Drop down from the table PV.LOAN.CLASSIFICATION. |
| 21 | `INLEND.AA.NEW.NPA.STATUS` | `InlendAaParameter_NewNpaStatus` | TField |  | Drop down from the table PV.LOAN.CLASSIFICATION. |
| 22 | `INLEND.AA.INT.ACCR.ACC` | `InlendAaParameter_IntAccrAcc` | TField |  | This field will configure the internal account, which will hold the interest accrual. |
| 23 | `INLEND.AA.INT.REV.ACC` | `InlendAaParameter_IntRevAcc` | TField |  | Will configure the internal account, which will hold the interest income reversal. |
| 24 | `INLEND.AA.AC.ENT.PARAM.ACCR` | `InlendAaParameter_AcEntParamAccr` | TField |  | Will configure the record, which will post the interest accrual from internal account to income on daily basis. |
| 25 | `INLEND.AA.AC.ENT.PARAM.REV` | `InlendAaParameter_AcEntParamRev` | TField |  | Will configure the record, which will post the un-recognized income from internal account to income. |
| 26 | `INLEND.AA.PROPERTY` | `InlendAaParameter_Property` |  |  |  |
| 27 | `INLEND.AA.CATEGORY` | `InlendAaParameter_Category` |  |  |  |
| 28 | `INLEND.AA.INT.DEFER.PERIOD` | `InlendAaParameter_IntDeferPeriod` | TField |  | This field is no longer in use. |
| 29 | `INLEND.AA.NEW.OD.NPA.VERSION` | `InlendAaParameter_NewOdNpaVersion` | TField |  | If the Value is set as Y, then the asset classification will be based on Ageing or No Cr Ageing Days. |
| 30 | `INLEND.AA.NPA.HOL.INCLUSIVE` | `InlendAaParameter_NpaHolInclusive` | TField |  | During any holiday, system should calculate the ageing days inclusive of the holiday days in the previous working day COB or not. |
| 31 | `INLEND.AA.SUSPEND.CHARGE.ACCOUNT` | `InlendAaParameter_SuspendChargeAccount` | TField |  | This field is no longer in use. |
| 32 | `INLEND.AA.AC.ENT.PARAM.CHARGE` | `InlendAaParameter_AcEntParamCharge` | TField |  | This field is no longer in use. |
