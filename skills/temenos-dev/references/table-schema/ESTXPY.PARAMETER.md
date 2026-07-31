# ESTXPY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ESTXPY.PARAMETER` in `ESTXPY_SocialSecurityTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.PARAM.HOOK.ROUTINE` | `EstxpyParameter_HookRoutine` | TField |  | It holds the hook routine for NRC generation |
| 2 | `ES.PARAM.LIQ.RESTRICT.ACCOUNT` | `EstxpyParameter_LiqRestrictAccount` | TField |  | It holds the LIQUIDATION's Internal Account |
| 3 | `ES.PARAM.SPCL.AUTO.LIQ.RESTRICT.ACCOUNT` | `EstxpyParameter_SpclAutoLiqRestrictAccount` | TField |  | It holds the SPECIAL AUTO LIQUIDATION's Internal Account |
| 4 | `ES.PARAM.AUTO.LIQ.RESTRICT.ACCOUNT` | `EstxpyParameter_AutoLiqRestrictAccount` | TField |  | It holds the AUTO LIQUIDATION's Internal Account |
| 5 | `ES.PARAM.LOCAL.REF` | `EstxpyParameter_LocalRef` |  |  |  |
| 6 | `ES.PARAM.PAYMENT.ORDER.PRODUCT` | `EstxpyParameter_PaymentOrderProduct` | TField |  | It holds the Payment Order Product |
| 7 | `ES.PARAM.STATE.TAX.ACCOUNT` | `EstxpyParameter_StateTaxAccount` | TField |  | It holds the STATE.TAX's Internal Account |
| 8 | `ES.PARAM.LIQ.TREASURY.ACCOUNT` | `EstxpyParameter_LiqTreasuryAccount` | TField |  | It holds the LIQUIDATION's Internal Treasury Account |
| 9 | `ES.PARAM.SPCL.AUTO.LIQ.TREASURY.ACCOUNT` | `EstxpyParameter_SpclAutoLiqTreasuryAccount` | TField |  | It holds the SPECIAL AUTO LIQUIDATION's Internal Treasury Account |
| 10 | `ES.PARAM.AUTO.LIQ.TREASURY.ACCOUNT` | `EstxpyParameter_AutoLiqTreasuryAccount` | TField |  | It holds the AUTO LIQUIDATION's Internal Treasury Account |
| 11 | `ES.PARAM.STATE.TAX.TREASURY.ACCOUNT` | `EstxpyParameter_StateTaxTreasuryAccount` | TField |  | It holds the STATE TAX's Internal Treasury Account |
| 12 | `ES.PARAM.ERROR.TYPE` | `EstxpyParameter_ErrorType` |  |  |  |
| 13 | `ES.PARAM.PP.ERROR.CODES` | `EstxpyParameter_PpErrorCodes` |  |  |  |
| 14 | `ES.PARAM.AUTONOMIC.TAX.RESTRICT.ACCOUNT` | `EstxpyParameter_AutonomicTaxRestrictAccount` | TField |  | It holds the AUTONOMIC TAX's Internal Account |
| 15 | `ES.PARAM.AUTONOMIC.TAX.TREASURY.ACCOUNT` | `EstxpyParameter_AutonomicTaxTreasuryAccount` | TField |  | It holds the AUTONOMIC TAX's Internal Treasury Account |
| 16 | `ES.PARAM.CHARACTER.STRING` | `EstxpyParameter_CharacterString` | TField |  | It holds the Character String for NRC generation |
| 17 | `ES.PARAM.RESERVED.12` | `EstxpyParameter_Reserved12` | TField |  | Reserved field for future use |
| 18 | `ES.PARAM.RESERVED.13` | `EstxpyParameter_Reserved13` | TField |  | Reserved field for future use |
| 19 | `ES.PARAM.RESERVED.14` | `EstxpyParameter_Reserved14` | TField |  | Reserved field for future use |
| 20 | `ES.PARAM.RESERVED.15` | `EstxpyParameter_Reserved15` | TField |  | Reserved field for future use |
| 21 | `ES.PARAM.OVERRIDE` | `EstxpyParameter_Override` |  |  |  |
| 22 | `ES.PARAM.RECORD.STATUS` | `EstxpyParameter_RecordStatus` | String |  |  |
| 23 | `ES.PARAM.CURR.NO` | `EstxpyParameter_CurrNo` | String |  |  |
| 24 | `ES.PARAM.INPUTTER` | `EstxpyParameter_Inputter` |  |  |  |
| 25 | `ES.PARAM.DATE.TIME` | `EstxpyParameter_DateTime` |  |  |  |
| 26 | `ES.PARAM.AUTHORISER` | `EstxpyParameter_Authoriser` | String |  |  |
| 27 | `ES.PARAM.CO.CODE` | `EstxpyParameter_CoCode` | String |  |  |
| 28 | `ES.PARAM.DEPT.CODE` | `EstxpyParameter_DeptCode` | String |  |  |
| 29 | `ES.PARAM.AUDITOR.CODE` | `EstxpyParameter_AuditorCode` | String |  |  |
| 30 | `ES.PARAM.AUDIT.DATE.TIME` | `EstxpyParameter_AuditDateTime` | String |  |  |
