# DDA.SERVICE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DDA.SERVICE.PARAMETER` in `AC_DDAService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DDA.SVC.DESCRIPTION` | `DdaServiceParameter_Description` | TField |  | Generic description with Alphanumeric characters. |
| 2 | `DDA.SVC.MULTI.CCY.CHECK.API` | `DdaServiceParameter_MultiCcyCheckApi` | TField |  | Hook to attach L3 API to return the Account currency to getFullAccountInfo API. The attached L3 API should be validated against EB.API table. If the MULTI.CCY.CHECK.API is configured, it will be called with the arguments: InArgs , OutArgs, Err,Reserved1,Reserved2. Where, InArgs(AcctNo) - Passed account number InArgs(supPayCcy) - Supplied payment currency InArgs(supAcctComp) - Supplied Account Company InArgs(supDebitAccount) - Supplied Debit Account InArgs(supDebitCurrency) - Supplied Debit currency InArgs(supDebitAccountIBAN) - Supplied Debit Account IBAN InArgs(supCreditAccount) - Supplied Credit Account InArgs(supCreditCurrency) - Supplied Credit Currency InArgs(supCreditAccountIBAN) - Supplied Credit Account IBAN InArgs(supChargeAccount) - Supplied Charge Account InArgs(supChargeCurrency) - Supplied Charge Currency InArgs(supChargeAccountCurrency) - Supplied Charge Account Currency InArgs(supBeneficiaryAccount) - Supplied Beneficiary Account InArgs(supBeneficiaryIBAN) - Supplied Beneficiary IBAN InArgs(supCreditNostroAccount) - Supplied Credit Nostro Account InArgs(supOrderingCustomerAccount) - Supplied Ordering Customer Account InArgs(supPaymentOrderProduct) - Supplied Payment Order Product InArgs(supPaymentSystemId) - Supplied Payment System Id OutArgs(payCcy) - The L3 API logic returned payment currency which will be returned back to calling API. Validations: Routine should have a valid EB.API Entry |
| 3 | `DDA.SVC.RESERVED.13` | `DdaServiceParameter_Reserved13` | TField |  |  |
| 4 | `DDA.SVC.RESERVED.12` | `DdaServiceParameter_Reserved12` | TField |  |  |
| 5 | `DDA.SVC.RESERVED.11` | `DdaServiceParameter_Reserved11` | TField |  |  |
| 6 | `DDA.SVC.RESERVED.10` | `DdaServiceParameter_Reserved10` | TField |  |  |
| 7 | `DDA.SVC.RESERVED.9` | `DdaServiceParameter_Reserved9` | TField |  |  |
| 8 | `DDA.SVC.RESERVED.8` | `DdaServiceParameter_Reserved8` | TField |  |  |
| 9 | `DDA.SVC.RESERVED.7` | `DdaServiceParameter_Reserved7` | TField |  |  |
| 10 | `DDA.SVC.RESERVED.6` | `DdaServiceParameter_Reserved6` | TField |  |  |
| 11 | `DDA.SVC.RESERVED.5` | `DdaServiceParameter_Reserved5` | TField |  |  |
| 12 | `DDA.SVC.RESERVED.4` | `DdaServiceParameter_Reserved4` | TField |  |  |
| 13 | `DDA.SVC.RESERVED.3` | `DdaServiceParameter_Reserved3` | TField |  |  |
| 14 | `DDA.SVC.RESERVED.2` | `DdaServiceParameter_Reserved2` | TField |  |  |
| 15 | `DDA.SVC.RESERVED.1` | `DdaServiceParameter_Reserved1` | TField |  |  |
| 16 | `DDA.SVC.LOCAL.REF` | `DdaServiceParameter_LocalRef` |  |  |  |
| 17 | `DDA.SVC.OVERRIDE` | `DdaServiceParameter_Override` |  |  |  |
| 18 | `DDA.SVC.RECORD.STATUS` | `DdaServiceParameter_RecordStatus` | String |  |  |
| 19 | `DDA.SVC.CURR.NO` | `DdaServiceParameter_CurrNo` | String |  |  |
| 20 | `DDA.SVC.INPUTTER` | `DdaServiceParameter_Inputter` |  |  |  |
| 21 | `DDA.SVC.DATE.TIME` | `DdaServiceParameter_DateTime` |  |  |  |
| 22 | `DDA.SVC.AUTHORISER` | `DdaServiceParameter_Authoriser` | String |  |  |
| 23 | `DDA.SVC.CO.CODE` | `DdaServiceParameter_CoCode` | String |  |  |
| 24 | `DDA.SVC.DEPT.CODE` | `DdaServiceParameter_DeptCode` | String |  |  |
| 25 | `DDA.SVC.AUDITOR.CODE` | `DdaServiceParameter_AuditorCode` | String |  |  |
| 26 | `DDA.SVC.AUDIT.DATE.TIME` | `DdaServiceParameter_AuditDateTime` | String |  |  |
