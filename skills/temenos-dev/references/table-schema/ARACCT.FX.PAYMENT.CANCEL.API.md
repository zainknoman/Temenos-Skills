# ARACCT.FX.PAYMENT.CANCEL.API — Table Schema

> Source: `INSERTS/I_F.ARACCT.FX.PAYMENT.CANCEL.API` in `ARACCT_FXBlacklistLimitValidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.CANCEL.API.CUSTOMER.ID` | `AracctFxPaymentCancelApi_CustomerId` | TField |  | Customer Id who is the owner of the debit account in FX transaction. |
| 2 | `ARACCT.CANCEL.API.CUSTOMER.LEGAL.ID` | `AracctFxPaymentCancelApi_CustomerLegalId` | TField |  | Customer legal ID that is used in cancellation API call. |
| 3 | `ARACCT.CANCEL.API.DEBIT.ACCOUNT` | `AracctFxPaymentCancelApi_DebitAccount` | TField |  | Debit Account in Transaction. |
| 4 | `ARACCT.CANCEL.API.CREDIT.ACCOUNT` | `AracctFxPaymentCancelApi_CreditAccount` | TField |  | Credit Account in Transaction. |
| 5 | `ARACCT.CANCEL.API.TRANSACTION.AMOUNT` | `AracctFxPaymentCancelApi_TransactionAmount` | TField |  | Transaction Amount. |
| 6 | `ARACCT.CANCEL.API.TRANSACTION.CURRENCY` | `AracctFxPaymentCancelApi_TransactionCurrency` | TField |  | Transaction Currency. |
| 7 | `ARACCT.CANCEL.API.ID.OPERATION` | `AracctFxPaymentCancelApi_IdOperation` | TField |  | ID from the operation responded by BCRA in the FX validation API call. |
| 8 | `ARACCT.CANCEL.API.API.SYSTEM.DATE` | `AracctFxPaymentCancelApi_ApiSystemDate` | TField |  | System date used in cancellation API call. |
| 9 | `ARACCT.CANCEL.API.API.RESPONSE` | `AracctFxPaymentCancelApi_ApiResponse` |  |  |  |
| 10 | `ARACCT.CANCEL.API.RESERVED.1` | `AracctFxPaymentCancelApi_Reserved1` | TField |  | Reserved for Future use. |
| 11 | `ARACCT.CANCEL.API.RESERVED.2` | `AracctFxPaymentCancelApi_Reserved2` | TField |  | Reserved for Future use. |
| 12 | `ARACCT.CANCEL.API.RESERVED.3` | `AracctFxPaymentCancelApi_Reserved3` | TField |  | Reserved for Future use. |
| 13 | `ARACCT.CANCEL.API.RESERVED.4` | `AracctFxPaymentCancelApi_Reserved4` | TField |  | Reserved for Future use. |
| 14 | `ARACCT.CANCEL.API.RESERVED.5` | `AracctFxPaymentCancelApi_Reserved5` | TField |  | Reserved for Future use. |
| 15 | `ARACCT.CANCEL.API.RESERVED.6` | `AracctFxPaymentCancelApi_Reserved6` | TField |  | Reserved for Future use. |
| 16 | `ARACCT.CANCEL.API.RESERVED.7` | `AracctFxPaymentCancelApi_Reserved7` | TField |  | Reserved for Future use. |
| 17 | `ARACCT.CANCEL.API.RESERVED.8` | `AracctFxPaymentCancelApi_Reserved8` | TField |  | Reserved for Future use. |
| 18 | `ARACCT.CANCEL.API.RESERVED.9` | `AracctFxPaymentCancelApi_Reserved9` | TField |  | Reserved for Future use. |
| 19 | `ARACCT.CANCEL.API.RESERVED.10` | `AracctFxPaymentCancelApi_Reserved10` | TField |  | Reserved for Future use. |
| 20 | `ARACCT.CANCEL.API.LOCAL.REF` | `AracctFxPaymentCancelApi_LocalRef` |  |  |  |
| 21 | `ARACCT.CANCEL.API.OVERRIDE` | `AracctFxPaymentCancelApi_Override` |  |  |  |
| 22 | `ARACCT.CANCEL.API.RECORD.STATUS` | `AracctFxPaymentCancelApi_RecordStatus` | String |  |  |
| 23 | `ARACCT.CANCEL.API.CURR.NO` | `AracctFxPaymentCancelApi_CurrNo` | String |  |  |
| 24 | `ARACCT.CANCEL.API.INPUTTER` | `AracctFxPaymentCancelApi_Inputter` |  |  |  |
| 25 | `ARACCT.CANCEL.API.DATE.TIME` | `AracctFxPaymentCancelApi_DateTime` |  |  |  |
| 26 | `ARACCT.CANCEL.API.AUTHORISER` | `AracctFxPaymentCancelApi_Authoriser` | String |  |  |
| 27 | `ARACCT.CANCEL.API.CO.CODE` | `AracctFxPaymentCancelApi_CoCode` | String |  |  |
| 28 | `ARACCT.CANCEL.API.DEPT.CODE` | `AracctFxPaymentCancelApi_DeptCode` | String |  |  |
| 29 | `ARACCT.CANCEL.API.AUDITOR.CODE` | `AracctFxPaymentCancelApi_AuditorCode` | String |  |  |
| 30 | `ARACCT.CANCEL.API.AUDIT.DATE.TIME` | `AracctFxPaymentCancelApi_AuditDateTime` | String |  |  |
