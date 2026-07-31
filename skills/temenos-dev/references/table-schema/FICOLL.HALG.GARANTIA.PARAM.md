# FICOLL.HALG.GARANTIA.PARAM — Table Schema

> Source: `INSERTS/I_F.FICOLL.HALG.GARANTIA.PARAM` in `FICOLL_GuarantiaGuarantee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.HALGGARANTIAPARAM.PURPOSE.MAX.AMT.LIVING` | `FicollHalgGarantiaParam_PurposeMaxAmtLiving` | TField |  | Maximum guarantee amount for Living purpose. |
| 2 | `FICOLL.HALGGARANTIAPARAM.PURPOSE.MAX.AMT.INVEST` | `FicollHalgGarantiaParam_PurposeMaxAmtInvest` | TField |  | Maximum guarantee amount for Investment purpose. |
| 3 | `FICOLL.HALGGARANTIAPARAM.PURPOSE.MAX.PCT.INVEST` | `FicollHalgGarantiaParam_PurposeMaxPctInvest` | TField |  | Maximum guarantee percentage for Investment purpose. |
| 4 | `FICOLL.HALGGARANTIAPARAM.PURPOSE.MAX.PCT.LIVING` | `FicollHalgGarantiaParam_PurposeMaxPctLiving` | TField |  | Maximum guarantee percentage for Living purpose. |
| 5 | `FICOLL.HALGGARANTIAPARAM.PURPOSE.MAX.LOAN.PCT.LIVING` | `FicollHalgGarantiaParam_PurposeMaxLoanPctLiving` | TField |  | Maximum loan percentage for Living purpose. |
| 6 | `FICOLL.HALGGARANTIAPARAM.PURPOSE.MAX.LOAN.PCT.INVEST` | `FicollHalgGarantiaParam_PurposeMaxLoanPctInvest` | TField |  | Maximum loan percentage for Investment purpose. |
| 7 | `FICOLL.HALGGARANTIAPARAM.GARANTIA.EXE.VALUE.PCT` | `FicollHalgGarantiaParam_GarantiaExeValuePct` | TField |  | Reserved for future use. |
| 8 | `FICOLL.HALGGARANTIAPARAM.LOCAL.REF` | `FicollHalgGarantiaParam_LocalRef` |  |  |  |
| 9 | `FICOLL.HALGGARANTIAPARAM.OVERRIDE` | `FicollHalgGarantiaParam_Override` |  |  |  |
| 10 | `FICOLL.HALGGARANTIAPARAM.RECORD.STATUS` | `FicollHalgGarantiaParam_RecordStatus` | String |  |  |
| 11 | `FICOLL.HALGGARANTIAPARAM.CURR.NO` | `FicollHalgGarantiaParam_CurrNo` | String |  |  |
| 12 | `FICOLL.HALGGARANTIAPARAM.INPUTTER` | `FicollHalgGarantiaParam_Inputter` |  |  |  |
| 13 | `FICOLL.HALGGARANTIAPARAM.DATE.TIME` | `FicollHalgGarantiaParam_DateTime` |  |  |  |
| 14 | `FICOLL.HALGGARANTIAPARAM.AUTHORISER` | `FicollHalgGarantiaParam_Authoriser` | String |  |  |
| 15 | `FICOLL.HALGGARANTIAPARAM.CO.CODE` | `FicollHalgGarantiaParam_CoCode` | String |  |  |
| 16 | `FICOLL.HALGGARANTIAPARAM.DEPT.CODE` | `FicollHalgGarantiaParam_DeptCode` | String |  |  |
| 17 | `FICOLL.HALGGARANTIAPARAM.AUDITOR.CODE` | `FicollHalgGarantiaParam_AuditorCode` | String |  |  |
| 18 | `FICOLL.HALGGARANTIAPARAM.AUDIT.DATE.TIME` | `FicollHalgGarantiaParam_AuditDateTime` | String |  |  |
