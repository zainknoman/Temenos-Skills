# DX.CO.EXPIRE.MANUAL — Table Schema

> Source: `INSERTS/I_F.DX.CO.EXPIRE.MANUAL` in `DX_CloseoutExpiry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COEXP.TRANS.ID` | `DxCoExpireManual_TransId` |  |  |  |
| 2 | `DX.COEXP.CO.LOTS` | `DxCoExpireManual_CoLots` |  |  |  |
| 3 | `DX.COEXP.RESERVED10` | `DxCoExpireManual_Reserved10` |  |  |  |
| 4 | `DX.COEXP.BUYER` | `DxCoExpireManual_Buyer` |  |  |  |
| 5 | `DX.COEXP.B.FEE.TAX.TYPE` | `DxCoExpireManual_BFeeTaxType` |  |  |  |
| 6 | `DX.COEXP.B.FEE.TAX.CCY` | `DxCoExpireManual_BFeeTaxCcy` |  |  |  |
| 7 | `DX.COEXP.B.FEE.TAX.AMT` | `DxCoExpireManual_BFeeTaxAmt` |  |  |  |
| 8 | `DX.COEXP.UNAUTH.AUTH` | `DxCoExpireManual_UnauthAuth` | TField |  | If set as AUTHORISED this field will create all close out records with status of authorised Validation Rules: One of AUTHORISED or UNAUTHORISED or blank |
| 9 | `DX.COEXP.CLOSEOUT.ID` | `DxCoExpireManual_CloseoutId` |  |  |  |
| 10 | `DX.COEXP.RESERVED03` | `DxCoExpireManual_Reserved03` | TField |  |  |
| 11 | `DX.COEXP.RESERVED02` | `DxCoExpireManual_Reserved02` | TField |  |  |
| 12 | `DX.COEXP.LOCAL.REF` | `DxCoExpireManual_LocalRef` |  |  |  |
| 13 | `DX.COEXP.OVERRIDE` | `DxCoExpireManual_Override` |  |  |  |
| 14 | `DX.COEXP.RECORD.STATUS` | `DxCoExpireManual_RecordStatus` | String |  |  |
| 15 | `DX.COEXP.CURR.NO` | `DxCoExpireManual_CurrNo` | String |  |  |
| 16 | `DX.COEXP.INPUTTER` | `DxCoExpireManual_Inputter` |  |  |  |
| 17 | `DX.COEXP.DATE.TIME` | `DxCoExpireManual_DateTime` |  |  |  |
| 18 | `DX.COEXP.AUTHORISER` | `DxCoExpireManual_Authoriser` | String |  |  |
| 19 | `DX.COEXP.CO.CODE` | `DxCoExpireManual_CoCode` | String |  |  |
| 20 | `DX.COEXP.DEPT.CODE` | `DxCoExpireManual_DeptCode` | String |  |  |
| 21 | `DX.COEXP.AUDITOR.CODE` | `DxCoExpireManual_AuditorCode` | String |  |  |
| 22 | `DX.COEXP.AUDIT.DATE.TIME` | `DxCoExpireManual_AuditDateTime` | String |  |  |
| 23 | `DX.COEXP.B.SYS.FEE.TAX.AMT` | `DxCoExpireManual_BSysFeeTaxAmt` |  |  |  |
| 24 | `DX.COEXP.B.FEE.TAX.CODE` | `DxCoExpireManual_BFeeTaxCode` |  |  |  |
| 25 | `DX.COEXP.SELLER` | `DxCoExpireManual_Seller` |  |  |  |
| 26 | `DX.COEXP.S.FEE.TAX.TYPE` | `DxCoExpireManual_SFeeTaxType` |  |  |  |
| 27 | `DX.COEXP.S.FEE.TAX.CCY` | `DxCoExpireManual_SFeeTaxCcy` |  |  |  |
| 28 | `DX.COEXP.S.FEE.TAX.AMT` | `DxCoExpireManual_SFeeTaxAmt` |  |  |  |
| 29 | `DX.COEXP.S.SYS.FEE.TAX.AMT` | `DxCoExpireManual_SSysFeeTaxAmt` |  |  |  |
| 30 | `DX.COEXP.S.FEE.TAX.CODE` | `DxCoExpireManual_SFeeTaxCode` |  |  |  |
| 31 | `DX.COEXP.CREATION` | `DxCoExpireManual_Creation` | TField |  | This field determines if the record is being generated during the COB as result of Autoexpire of Cash settledoptions Validation Rules: NOINPUT field, updated by System |
| 32 | `DX.COEXP.SAFEKEEP.ACCT.NO` | `DxCoExpireManual_SafekeepAcctNo` |  |  |  |
| 33 | `DX.COEXP.SAFEKEEP.FEE.LCY` | `DxCoExpireManual_SafekeepFeeLcy` |  |  |  |
| 34 | `DX.COEXP.SK.ACY.LCY.RATE` | `DxCoExpireManual_SkAcyLcyRate` |  |  |  |
| 35 | `DX.COEXP.SAFEKEEP.FEE.ACY` | `DxCoExpireManual_SafekeepFeeAcy` |  |  |  |
| 36 | `DX.COEXP.EX.RATE.AC.CCY` | `DxCoExpireManual_ExRateAcCcy` |  |  |  |
| 37 | `DX.COEXP.B.FEE.TAX.AC.CCY` | `DxCoExpireManual_BFeeTaxAcCcy` |  |  |  |
| 38 | `DX.COEXP.S.FEE.TAX.AC.CCY` | `DxCoExpireManual_SFeeTaxAcCcy` |  |  |  |
| 39 | `DX.COEXP.PARENT.CHILD.REF` | `DxCoExpireManual_ParentChildRef` | TField |  |  |
