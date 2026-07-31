# DX.CO.EXPIRE.AUTO — Table Schema

> Source: `INSERTS/I_F.DX.CO.EXPIRE.AUTO` in `DX_CloseoutExpiry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COAXP.CUST.OR.PORT` | `DxCoExpireAuto_CustOrPort` | TField |  | Selection field which controls choice of customer or portfolio trades to be expired. Default is ALL to expire alltrades involving the chosen option series. Validation Rules: Must be one of ALL or CUSTOMER or PORTFOLIO |
| 2 | `DX.COAXP.CUSTOMER` | `DxCoExpireAuto_Customer` | TField |  | The customer for whom option expiry will be performed. Validation Rules: Must be a valid DX.CUSTOMER |
| 3 | `DX.COAXP.PORTFOLIO` | `DxCoExpireAuto_Portfolio` | TField |  | The customer portfolio on which option expiry will be performed. Validation Rules: Must be valid for SEC.ACC.MASTER Customer must be valid for DX.CUSTOMER |
| 4 | `DX.COAXP.CONTRACT.CODE` | `DxCoExpireAuto_ContractCode` | TField |  | The contract code of the option to be expired Validation Rules: Should be valid for DX.CONTRACT.MASTER |
| 5 | `DX.COAXP.OPTION.STYLE` | `DxCoExpireAuto_OptionStyle` | TField |  | Option style defaulted from DX.CONTRACT.MASTER. Validation Rules: NOINPUT One of EUROPEAN or AMERICAN |
| 6 | `DX.COAXP.MATURITY.DATE` | `DxCoExpireAuto_MaturityDate` | TField | Yes | The maturity / delivery month of the option to be expired. Validation Rules: Up to 11 characters in DATE format The field CONTRACT.CODE must be populated prior to this field Must be in the format: MONTHLY TRADES = Month/Year e.g. SEP00 DAILY TRADES = Day/Month/Year e.g. 15SEP00 Mandatory field |
| 7 | `DX.COAXP.DECLARATION.DATE` | `DxCoExpireAuto_DeclarationDate` | TField |  | The declaration date calculated from DX.CONTRACT.MASTER date formula. Validation Rules: NOINPUT field. Display date format, e.g 24 JAN 2000 |
| 8 | `DX.COAXP.STRIKE` | `DxCoExpireAuto_Strike` | TField | Yes | Strike price for option to be expired Validation Rules: Strike must be valid for strike scale and interval on DX.CONTRACT.MASTER Mandatory field |
| 9 | `DX.COAXP.INT.STRIKE` | `DxCoExpireAuto_IntStrike` | TField |  | Intenal strike price defaulted from STRIKE field Validation Rules: NOINPUT |
| 10 | `DX.COAXP.CALL.PUT` | `DxCoExpireAuto_CallPut` | TField | Yes | Select CALL or PUT for option series. Validation Rules: Should be one of CALL or PUT Mandatory field |
| 11 | `DX.COAXP.UNAUTH.AUTH` | `DxCoExpireAuto_UnauthAuth` | TField |  | If set as AUTHORISED this field will create all close out records with status of authorised. Validation Rules: One of AUTHORISED or UNAUTHORISED or blank |
| 12 | `DX.COAXP.CLOSEOUT.ID` | `DxCoExpireAuto_CloseoutId` |  |  |  |
| 13 | `DX.COAXP.CONTRACT.CCY` | `DxCoExpireAuto_ContractCcy` | TField | Yes | Specifies the contract currency of option to be expired. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 14 | `DX.COAXP.DELIVERY.CCY` | `DxCoExpireAuto_DeliveryCcy` | TField | Yes | Specifies the delivery currency of option to be expired. Validation Rule: Must be a valid currency in CURRENCY table and is a mandatory field for FX-OTC options. |
| 15 | `DX.COAXP.TRANS.ID` | `DxCoExpireAuto_TransId` |  |  |  |
| 16 | `DX.COAXP.RESERVED01` | `DxCoExpireAuto_Reserved01` |  |  |  |
| 17 | `DX.COAXP.BUYER` | `DxCoExpireAuto_Buyer` |  |  |  |
| 18 | `DX.COAXP.B.FEE.TAX.TYPE` | `DxCoExpireAuto_BFeeTaxType` |  |  |  |
| 19 | `DX.COAXP.B.FEE.TAX.CCY` | `DxCoExpireAuto_BFeeTaxCcy` |  |  |  |
| 20 | `DX.COAXP.B.FEE.TAX.AMT` | `DxCoExpireAuto_BFeeTaxAmt` |  |  |  |
| 21 | `DX.COAXP.B.SYS.FEE.TAX.AMT` | `DxCoExpireAuto_BSysFeeTaxAmt` |  |  |  |
| 22 | `DX.COAXP.LOCAL.REF` | `DxCoExpireAuto_LocalRef` |  |  |  |
| 23 | `DX.COAXP.OVERRIDE` | `DxCoExpireAuto_Override` |  |  |  |
| 24 | `DX.COAXP.RECORD.STATUS` | `DxCoExpireAuto_RecordStatus` | String |  |  |
| 25 | `DX.COAXP.CURR.NO` | `DxCoExpireAuto_CurrNo` | String |  |  |
| 26 | `DX.COAXP.INPUTTER` | `DxCoExpireAuto_Inputter` |  |  |  |
| 27 | `DX.COAXP.DATE.TIME` | `DxCoExpireAuto_DateTime` |  |  |  |
| 28 | `DX.COAXP.AUTHORISER` | `DxCoExpireAuto_Authoriser` | String |  |  |
| 29 | `DX.COAXP.CO.CODE` | `DxCoExpireAuto_CoCode` | String |  |  |
| 30 | `DX.COAXP.DEPT.CODE` | `DxCoExpireAuto_DeptCode` | String |  |  |
| 31 | `DX.COAXP.AUDITOR.CODE` | `DxCoExpireAuto_AuditorCode` | String |  |  |
| 32 | `DX.COAXP.AUDIT.DATE.TIME` | `DxCoExpireAuto_AuditDateTime` | String |  |  |
| 33 | `DX.COAXP.B.FEE.TAX.CODE` | `DxCoExpireAuto_BFeeTaxCode` |  |  |  |
| 34 | `DX.COAXP.SELLER` | `DxCoExpireAuto_Seller` |  |  |  |
| 35 | `DX.COAXP.S.FEE.TAX.TYPE` | `DxCoExpireAuto_SFeeTaxType` |  |  |  |
| 36 | `DX.COAXP.S.FEE.TAX.CCY` | `DxCoExpireAuto_SFeeTaxCcy` |  |  |  |
| 37 | `DX.COAXP.S.FEE.TAX.AMT` | `DxCoExpireAuto_SFeeTaxAmt` |  |  |  |
| 38 | `DX.COAXP.S.SYS.FEE.TAX.AMT` | `DxCoExpireAuto_SSysFeeTaxAmt` |  |  |  |
| 39 | `DX.COAXP.S.FEE.TAX.CODE` | `DxCoExpireAuto_SFeeTaxCode` |  |  |  |
| 40 | `DX.COAXP.SAFEKEEP.ACCT.NO` | `DxCoExpireAuto_SafekeepAcctNo` |  |  |  |
| 41 | `DX.COAXP.SAFEKEEP.FEE.LCY` | `DxCoExpireAuto_SafekeepFeeLcy` |  |  |  |
| 42 | `DX.COAXP.SK.ACY.LCY.RATE` | `DxCoExpireAuto_SkAcyLcyRate` |  |  |  |
| 43 | `DX.COAXP.SAFEKEEP.FEE.ACY` | `DxCoExpireAuto_SafekeepFeeAcy` |  |  |  |
| 44 | `DX.COAXP.UNDERLYING.MAT.DATE` | `DxCoExpireAuto_UnderlyingMatDate` | TField |  |  |
| 45 | `DX.COAXP.EX.RATE.AC.CCY` | `DxCoExpireAuto_ExRateAcCcy` |  |  |  |
| 46 | `DX.COAXP.B.FEE.TAX.AC.CCY` | `DxCoExpireAuto_BFeeTaxAcCcy` |  |  |  |
| 47 | `DX.COAXP.S.FEE.TAX.AC.CCY` | `DxCoExpireAuto_SFeeTaxAcCcy` |  |  |  |
