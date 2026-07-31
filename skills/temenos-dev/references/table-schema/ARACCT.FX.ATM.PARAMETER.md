# ARACCT.FX.ATM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ARACCT.FX.ATM.PARAMETER` in `ARACCT_AtmFxTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.FXATM.BANK.CCY.MKT` | `AracctFxAtmParameter_BankCcyMkt` | TField |  | Bank currency market used for FX conversion of ATM transaction amount |
| 2 | `ARACCT.FXATM.BNA.CCY.MKT` | `AracctFxAtmParameter_BnaCcyMkt` | TField |  | BNA currency market used for FX conversion of ATM transaction amount in Tax calculation |
| 3 | `ARACCT.FXATM.TAX.NAME` | `AracctFxAtmParameter_TaxName` |  |  |  |
| 4 | `ARACCT.FXATM.TAX.TYPE.DIGITAL` | `AracctFxAtmParameter_TaxTypeDigital` |  |  |  |
| 5 | `ARACCT.FXATM.TAX.TYPE.NON.DIGITAL` | `AracctFxAtmParameter_TaxTypeNonDigital` |  |  |  |
| 6 | `ARACCT.FXATM.TAX.TYPE.TIMEOUT` | `AracctFxAtmParameter_TaxTypeTimeout` |  |  |  |
| 7 | `ARACCT.FXATM.TAX.STATUS` | `AracctFxAtmParameter_TaxStatus` |  |  |  |
| 8 | `ARACCT.FXATM.DIGITAL.PROVIDER.VALIDATE.API` | `AracctFxAtmParameter_DigitalProviderValidateApi` | TField |  | This is used for the validation of the Digital provider. AR Feature contains a routine ARACCT.ATM.FCM.API.CALLJ to call FCM webservices to validate the digital providers. Client can attach own routine for validating the digital provider. Valid EB.API record. |
| 9 | `ARACCT.FXATM.RESERVED.3` | `AracctFxAtmParameter_Reserved3` | TField |  |  |
| 10 | `ARACCT.FXATM.RESERVED.2` | `AracctFxAtmParameter_Reserved2` | TField |  |  |
| 11 | `ARACCT.FXATM.RESERVED.1` | `AracctFxAtmParameter_Reserved1` | TField |  |  |
| 12 | `ARACCT.FXATM.RECORD.STATUS` | `AracctFxAtmParameter_RecordStatus` | String |  |  |
| 13 | `ARACCT.FXATM.CURR.NO` | `AracctFxAtmParameter_CurrNo` | String |  |  |
| 14 | `ARACCT.FXATM.INPUTTER` | `AracctFxAtmParameter_Inputter` |  |  |  |
| 15 | `ARACCT.FXATM.DATE.TIME` | `AracctFxAtmParameter_DateTime` |  |  |  |
| 16 | `ARACCT.FXATM.AUTHORISER` | `AracctFxAtmParameter_Authoriser` | String |  |  |
| 17 | `ARACCT.FXATM.CO.CODE` | `AracctFxAtmParameter_CoCode` | String |  |  |
| 18 | `ARACCT.FXATM.DEPT.CODE` | `AracctFxAtmParameter_DeptCode` | String |  |  |
| 19 | `ARACCT.FXATM.AUDITOR.CODE` | `AracctFxAtmParameter_AuditorCode` | String |  |  |
| 20 | `ARACCT.FXATM.AUDIT.DATE.TIME` | `AracctFxAtmParameter_AuditDateTime` | String |  |  |
| 21 | `ARACCT.FXATM.BANK.CCY.RATE.TYPE` | `AracctFxAtmParameter_BankCcyRateType` | TField |  | Bank currency rate type used for FX conversion of ATM transaction amount. The possible values will be:Sell RateBuy RateMid Rate |
