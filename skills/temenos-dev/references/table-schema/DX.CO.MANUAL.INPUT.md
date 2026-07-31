# DX.CO.MANUAL.INPUT — Table Schema

> Source: `INSERTS/I_F.DX.CO.MANUAL.INPUT` in `DX_CloseoutSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COMN.TRANS.ID` | `DxCoManualInput_TransId` |  |  |  |
| 2 | `DX.COMN.CO.LOTS` | `DxCoManualInput_CoLots` |  |  |  |
| 3 | `DX.COMN.RESERVED10` | `DxCoManualInput_Reserved10` |  |  |  |
| 4 | `DX.COMN.RESERVED09` | `DxCoManualInput_Reserved09` |  |  |  |
| 5 | `DX.COMN.COST.DIFF.AMT` | `DxCoManualInput_CostDiffAmt` | TField |  | Holds the difference of trade cost between the matched sell and buy trades of CHG.CUSTOMER. Validation Rules: NOINPUT field |
| 6 | `DX.COMN.CHG.CUSTOMER` | `DxCoManualInput_ChgCustomer` |  |  |  |
| 7 | `DX.COMN.FEE.TAX.TYPE` | `DxCoManualInput_FeeTaxType` |  |  |  |
| 8 | `DX.COMN.UNAUTH.AUTH` | `DxCoManualInput_UnauthAuth` | TField |  | If set as authorised this field with ensure that any closeout fed from the application with automatically beauthorised. Validation Rules: One of AUTHORISED or UNAUTHORISED |
| 9 | `DX.COMN.CLOSEOUT.ID` | `DxCoManualInput_CloseoutId` |  |  |  |
| 10 | `DX.COMN.RESERVED11` | `DxCoManualInput_Reserved11` | TField |  |  |
| 11 | `DX.COMN.RESERVED12` | `DxCoManualInput_Reserved12` | TField |  |  |
| 12 | `DX.COMN.RESERVED13` | `DxCoManualInput_Reserved13` | TField |  |  |
| 13 | `DX.COMN.OVERRIDE` | `DxCoManualInput_Override` |  |  |  |
| 14 | `DX.COMN.RECORD.STATUS` | `DxCoManualInput_RecordStatus` | String |  |  |
| 15 | `DX.COMN.CURR.NO` | `DxCoManualInput_CurrNo` | String |  |  |
| 16 | `DX.COMN.INPUTTER` | `DxCoManualInput_Inputter` |  |  |  |
| 17 | `DX.COMN.DATE.TIME` | `DxCoManualInput_DateTime` |  |  |  |
| 18 | `DX.COMN.AUTHORISER` | `DxCoManualInput_Authoriser` | String |  |  |
| 19 | `DX.COMN.CO.CODE` | `DxCoManualInput_CoCode` | String |  |  |
| 20 | `DX.COMN.DEPT.CODE` | `DxCoManualInput_DeptCode` | String |  |  |
| 21 | `DX.COMN.AUDITOR.CODE` | `DxCoManualInput_AuditorCode` | String |  |  |
| 22 | `DX.COMN.AUDIT.DATE.TIME` | `DxCoManualInput_AuditDateTime` | String |  |  |
| 23 | `DX.COMN.FEE.TAX.CCY` | `DxCoManualInput_FeeTaxCcy` |  |  |  |
| 24 | `DX.COMN.FEE.TAX.AMT` | `DxCoManualInput_FeeTaxAmt` |  |  |  |
| 25 | `DX.COMN.SYS.FEE.TAX.AMT` | `DxCoManualInput_SysFeeTaxAmt` |  |  |  |
| 26 | `DX.COMN.FEE.TAX.CODE` | `DxCoManualInput_FeeTaxCode` |  |  |  |
| 27 | `DX.COMN.RESERVED06` | `DxCoManualInput_Reserved06` | TField |  |  |
| 28 | `DX.COMN.RESERVED05` | `DxCoManualInput_Reserved05` | TField |  |  |
| 29 | `DX.COMN.RESERVED04` | `DxCoManualInput_Reserved04` | TField |  |  |
| 30 | `DX.COMN.RESERVED03` | `DxCoManualInput_Reserved03` | TField |  |  |
| 31 | `DX.COMN.RESERVED02` | `DxCoManualInput_Reserved02` | TField |  |  |
| 32 | `DX.COMN.RESERVED01` | `DxCoManualInput_Reserved01` | TField |  |  |
