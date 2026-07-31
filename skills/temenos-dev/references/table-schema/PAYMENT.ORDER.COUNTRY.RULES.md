# PAYMENT.ORDER.COUNTRY.RULES — Table Schema

> Source: `INSERTS/I_F.PAYMENT.ORDER.COUNTRY.RULES` in `PI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `POCR.DESCRIPTION` | `PaymentOrderCountryRules_Description` |  |  |  |
| 2 | `POCR.ALLOW.IBAN` | `PaymentOrderCountryRules_AllowIban` | TField | Yes | The field BENEFICIARY.IBAN in a PAYMENT.ORDER transaction done using pay through beneficiary option, can hold value based on configuration of this field. Allowed options are either 'Allowed' or 'Not Allowed'. If it is 'Not Allowed' and if IBAN is given in payment order or Vice the Versa, then error will be thrown Validation Rules: Inputable and mandatory field only if IN is installed. By Default 'Allowed' will be set if IN is installed and country follows rules as per IN.IBAN.STRUCTURE, otherwise defaulted to value 'Not Allowed' |
| 3 | `POCR.ALLOW.BIC` | `PaymentOrderCountryRules_AllowBic` | TField | Yes | The field BENEFICIARY.BIC in a PAYMENT.ORDER transaction done using pay through beneficiary option, can hold value based on configuration of this field. Allowed options are either 'Allowed' or 'Not Allowed'. If it is 'Not allowed' and if BIC is defined or Vice the Versa, then error will be thrown Validation Rules: Mandatory. By Default 'Not Allowed' will be set |
| 4 | `POCR.ALLOW.SORT.CODE` | `PaymentOrderCountryRules_AllowSortCode` | TField | Yes | The field BEN.BANK.CODE in a PAYMENT.ORDER transaction done using pay through beneficiary option, can hold value based on configuration of this field. Allowed options are either 'Allowed' or 'Not Allowed'. If it is 'Not Allowed' and if bank code is given or Vice the Versa, then error will be thrown Validation Rules: Mandatory. By Default 'Not Allowed' will be set |
| 5 | `POCR.CLEARING.CHANNEL` | `PaymentOrderCountryRules_ClearingChannel` |  |  |  |
| 6 | `POCR.CLEARING.CODE.FORMAT` | `PaymentOrderCountryRules_ClearingCodeFormat` |  |  |  |
| 7 | `POCR.RESERVED.15` | `PaymentOrderCountryRules_Reserved15` |  |  |  |
| 8 | `POCR.RESERVED.14` | `PaymentOrderCountryRules_Reserved14` |  |  |  |
| 9 | `POCR.RESERVED.13` | `PaymentOrderCountryRules_Reserved13` |  |  |  |
| 10 | `POCR.RESERVED.12` | `PaymentOrderCountryRules_Reserved12` |  |  |  |
| 11 | `POCR.RESERVED.11` | `PaymentOrderCountryRules_Reserved11` |  |  |  |
| 12 | `POCR.ALLOW.PAYMENT.CURRENCY` | `PaymentOrderCountryRules_AllowPaymentCurrency` |  |  |  |
| 13 | `POCR.RESERVED.9` | `PaymentOrderCountryRules_Reserved9` | TField |  |  |
| 14 | `POCR.RESERVED.8` | `PaymentOrderCountryRules_Reserved8` | TField |  |  |
| 15 | `POCR.RESERVED.7` | `PaymentOrderCountryRules_Reserved7` | TField |  |  |
| 16 | `POCR.RESERVED.6` | `PaymentOrderCountryRules_Reserved6` | TField |  |  |
| 17 | `POCR.RESERVED.5` | `PaymentOrderCountryRules_Reserved5` | TField |  |  |
| 18 | `POCR.RESERVED.4` | `PaymentOrderCountryRules_Reserved4` | TField |  |  |
| 19 | `POCR.RESERVED.3` | `PaymentOrderCountryRules_Reserved3` | TField |  |  |
| 20 | `POCR.RESERVED.2` | `PaymentOrderCountryRules_Reserved2` | TField |  |  |
| 21 | `POCR.RESERVED.1` | `PaymentOrderCountryRules_Reserved1` | TField |  |  |
| 22 | `POCR.LOCAL.REF` | `PaymentOrderCountryRules_LocalRef` |  |  |  |
| 23 | `POCR.OVERRIDE` | `PaymentOrderCountryRules_Override` |  |  |  |
| 24 | `POCR.RECORD.STATUS` | `PaymentOrderCountryRules_RecordStatus` | String |  |  |
| 25 | `POCR.CURR.NO` | `PaymentOrderCountryRules_CurrNo` | String |  |  |
| 26 | `POCR.INPUTTER` | `PaymentOrderCountryRules_Inputter` |  |  |  |
| 27 | `POCR.DATE.TIME` | `PaymentOrderCountryRules_DateTime` |  |  |  |
| 28 | `POCR.AUTHORISER` | `PaymentOrderCountryRules_Authoriser` | String |  |  |
| 29 | `POCR.CO.CODE` | `PaymentOrderCountryRules_CoCode` | String |  |  |
| 30 | `POCR.DEPT.CODE` | `PaymentOrderCountryRules_DeptCode` | String |  |  |
| 31 | `POCR.AUDITOR.CODE` | `PaymentOrderCountryRules_AuditorCode` | String |  |  |
| 32 | `POCR.AUDIT.DATE.TIME` | `PaymentOrderCountryRules_AuditDateTime` | String |  |  |
