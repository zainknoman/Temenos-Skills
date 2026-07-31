# SIGNATURE.PF.VALUATION.PARAM — Table Schema

> Source: `INSERTS/I_F.SIGNATURE.PF.VALUATION.PARAM` in `FNDINV_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SIGN.PF.VAL.VALUATION.CCY` | `SignaturePfValuationParam_ValuationCcy` | TField |  | The currency in which the valuation amount is updated.This can be same or different from the security currency. Vetted to CURRENCY |
| 2 | `SIGN.PF.VAL.VALUATION.AMOUNT` | `SignaturePfValuationParam_ValuationAmount` | TField |  | The valuation amount in the Valuation currency as on today. |
| 3 | `SIGN.PF.VAL.LOCAL.REF` | `SignaturePfValuationParam_LocalRef` |  |  |  |
| 4 | `SIGN.PF.VAL.ACTION.INDICATOR` | `SignaturePfValuationParam_ActionIndicator` | TField |  | Whenever there is a change in the VALUATION.AMOUNT, ACTION.INDICATOR will be set. |
| 5 | `SIGN.PF.VAL.SECURITY.MASTER.REFERENCE` | `SignaturePfValuationParam_SecurityMasterReference` | TField |  | This field will be updated with SECURITY.MASTER ID which is present in @ID of this parameter table. Field used for internal system calculation NOINPUT field |
| 6 | `SIGN.PF.VAL.PORTFOLIO.REFERENCE` | `SignaturePfValuationParam_PortfolioReference` | TField |  | This field will be updated with SEC.ACC.MASTER ID which is present in @ID of this parameter table. Field used for internal system calculation NOINPUT field |
| 7 | `SIGN.PF.VAL.RESERVED.4` | `SignaturePfValuationParam_Reserved4` | TField |  |  |
| 8 | `SIGN.PF.VAL.RESERVED.5` | `SignaturePfValuationParam_Reserved5` | TField |  |  |
| 9 | `SIGN.PF.VAL.RESERVED.6` | `SignaturePfValuationParam_Reserved6` | TField |  |  |
| 10 | `SIGN.PF.VAL.RESERVED.7` | `SignaturePfValuationParam_Reserved7` | TField |  |  |
| 11 | `SIGN.PF.VAL.RESERVED.8` | `SignaturePfValuationParam_Reserved8` | TField |  |  |
| 12 | `SIGN.PF.VAL.RESERVED.9` | `SignaturePfValuationParam_Reserved9` | TField |  |  |
| 13 | `SIGN.PF.VAL.RESERVED.10` | `SignaturePfValuationParam_Reserved10` | TField |  |  |
| 14 | `SIGN.PF.VAL.OVERRIDE` | `SignaturePfValuationParam_Override` |  |  |  |
| 15 | `SIGN.PF.VAL.RECORD.STATUS` | `SignaturePfValuationParam_RecordStatus` | String |  |  |
| 16 | `SIGN.PF.VAL.CURR.NO` | `SignaturePfValuationParam_CurrNo` | String |  |  |
| 17 | `SIGN.PF.VAL.INPUTTER` | `SignaturePfValuationParam_Inputter` |  |  |  |
| 18 | `SIGN.PF.VAL.DATE.TIME` | `SignaturePfValuationParam_DateTime` |  |  |  |
| 19 | `SIGN.PF.VAL.AUTHORISER` | `SignaturePfValuationParam_Authoriser` | String |  |  |
| 20 | `SIGN.PF.VAL.CO.CODE` | `SignaturePfValuationParam_CoCode` | String |  |  |
| 21 | `SIGN.PF.VAL.DEPT.CODE` | `SignaturePfValuationParam_DeptCode` | String |  |  |
| 22 | `SIGN.PF.VAL.AUDITOR.CODE` | `SignaturePfValuationParam_AuditorCode` | String |  |  |
| 23 | `SIGN.PF.VAL.AUDIT.DATE.TIME` | `SignaturePfValuationParam_AuditDateTime` | String |  |  |
