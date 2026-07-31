# DX.CO.AUTO.INPUT — Table Schema

> Source: `INSERTS/I_F.DX.CO.AUTO.INPUT` in `DX_CloseoutSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COAT.CUSTOMER` | `DxCoAutoInput_Customer` | TField | No | Allows the user to select a customer to perform an automatic settlement of trades on. Validation Rules: Optional Must be a valid customer on the CUSTOMER application. Must be a valid customer on the DX.CUSTOMER application. |
| 2 | `DX.COAT.PORTFOLIO` | `DxCoAutoInput_Portfolio` | TField |  | Allows the user to select a customer portfolio to perform an automatic settlement of trades on. Validation Rules: Must be a valid portfolio in the SEC.ACC.MASTER application. Must be a valid portfolio for a DX.CUSTOMER Must be a valid portfolio for the CUSTOMER specified in the CUSTOMER field if it has been specified. |
| 3 | `DX.COAT.EXCHANGE.CODE` | `DxCoAutoInput_ExchangeCode` | TField |  | Allows the user to select an exchange on which to perform an automatic settlement of trades on. Validation Rules: Must be a valid exchange on the DX.EXCHANGE.MASTER application. |
| 4 | `DX.COAT.MATURITY.DATE` | `DxCoAutoInput_MaturityDate` | TField |  | Allows the user to select a valid maturity period for which to auto settle trades. Validation Rules: Must be a valid maturity period. MMYY or DDMMYY |
| 5 | `DX.COAT.CONTRACT.CODE` | `DxCoAutoInput_ContractCode` | TField |  | Allows the user to select a specific contract on which to process and automatic settlement. Validation Rules: Must exist as a valid contract on the DX.CONTRACT.MASTER application. If a EXCHANGE.CODE has been specified then the CONTRACT.CODE must exisit for this exchange. |
| 6 | `DX.COAT.STRIKE` | `DxCoAutoInput_Strike` | TField |  | For options contracts only, allows the user to specify a STRIKE price to select trades which are to beautomatically settled. Validation Rules: Must be a valid strike price. This field is no available for input if a futures contract code has been entered in the CONTRACT.CODE |
| 7 | `DX.COAT.CALL.PUT` | `DxCoAutoInput_CallPut` | TField |  | Allows the user to select either CALL options or PUT options to be auto settled. Validation Rules: CALL or PUT This field is no available for input if a futures contract code has been entered in the CONTRACT.CODE |
| 8 | `DX.COAT.CLOSEOUT.ID` | `DxCoAutoInput_CloseoutId` |  |  |  |
| 9 | `DX.COAT.CONTRACT.CCY` | `DxCoAutoInput_ContractCcy` | TField | Yes | Select the option trades with the mentioned contract currency to be auto settled. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 10 | `DX.COAT.DELIVERY.CCY` | `DxCoAutoInput_DeliveryCcy` | TField | Yes | Select the option trades with the mentioned delivery currency to be auto settled. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 11 | `DX.COAT.TRANS.ID` | `DxCoAutoInput_TransId` |  |  |  |
| 12 | `DX.COAT.RESERVED6` | `DxCoAutoInput_Reserved6` |  |  |  |
| 13 | `DX.COAT.RESERVED5` | `DxCoAutoInput_Reserved5` |  |  |  |
| 14 | `DX.COAT.COST.DIFF.AMT` | `DxCoAutoInput_CostDiffAmt` | TField |  | Holds the difference of trade cost between the matched sell and buy trades of CHG.CUSTOMER. Validation Rules: NOINPUT field |
| 15 | `DX.COAT.CHG.CUSTOMER` | `DxCoAutoInput_ChgCustomer` |  |  |  |
| 16 | `DX.COAT.FEE.TAX.TYPE` | `DxCoAutoInput_FeeTaxType` |  |  |  |
| 17 | `DX.COAT.FEE.TAX.CCY` | `DxCoAutoInput_FeeTaxCcy` |  |  |  |
| 18 | `DX.COAT.LOCAL.REF` | `DxCoAutoInput_LocalRef` |  |  |  |
| 19 | `DX.COAT.OVERRIDE` | `DxCoAutoInput_Override` |  |  |  |
| 20 | `DX.COAT.RECORD.STATUS` | `DxCoAutoInput_RecordStatus` | String |  |  |
| 21 | `DX.COAT.CURR.NO` | `DxCoAutoInput_CurrNo` | String |  |  |
| 22 | `DX.COAT.INPUTTER` | `DxCoAutoInput_Inputter` |  |  |  |
| 23 | `DX.COAT.DATE.TIME` | `DxCoAutoInput_DateTime` |  |  |  |
| 24 | `DX.COAT.AUTHORISER` | `DxCoAutoInput_Authoriser` | String |  |  |
| 25 | `DX.COAT.CO.CODE` | `DxCoAutoInput_CoCode` | String |  |  |
| 26 | `DX.COAT.DEPT.CODE` | `DxCoAutoInput_DeptCode` | String |  |  |
| 27 | `DX.COAT.AUDITOR.CODE` | `DxCoAutoInput_AuditorCode` | String |  |  |
| 28 | `DX.COAT.AUDIT.DATE.TIME` | `DxCoAutoInput_AuditDateTime` | String |  |  |
| 29 | `DX.COAT.FEE.TAX.AMT` | `DxCoAutoInput_FeeTaxAmt` |  |  |  |
| 30 | `DX.COAT.SYS.FEE.TAX.AMT` | `DxCoAutoInput_SysFeeTaxAmt` |  |  |  |
| 31 | `DX.COAT.FEE.TAX.CODE` | `DxCoAutoInput_FeeTaxCode` |  |  |  |
| 32 | `DX.COAT.RESERVED06` | `DxCoAutoInput_Reserved06` |  |  |  |
| 33 | `DX.COAT.RESERVED05` | `DxCoAutoInput_Reserved05` | TField |  |  |
| 34 | `DX.COAT.RESERVED04` | `DxCoAutoInput_Reserved04` | TField |  |  |
| 35 | `DX.COAT.RESERVED03` | `DxCoAutoInput_Reserved03` | TField |  |  |
| 36 | `DX.COAT.RESERVED02` | `DxCoAutoInput_Reserved02` | TField |  |  |
| 37 | `DX.COAT.RESERVED01` | `DxCoAutoInput_Reserved01` | TField |  |  |
