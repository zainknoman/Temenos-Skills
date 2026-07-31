# FIIPMT.INCOMING.PAYMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.FIIPMT.INCOMING.PAYMENT.PARAM` in `FIIPMT_IncomingPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INCOMING.PAYMENT.PARAM.BANK.IBAN.NUMBER` | `FiipmtIncomingPaymentParam_BankIbanNumber` |  |  |  |
| 2 | `INCOMING.PAYMENT.PARAM.LOAN.DR.ACCOUNT` | `FiipmtIncomingPaymentParam_LoanDrAccount` |  |  |  |
| 3 | `INCOMING.PAYMENT.PARAM.PAYMENT.TYPE.START` | `FiipmtIncomingPaymentParam_PaymentTypeStart` | TField |  | Starting Position of the Payment Type (This has to be provided without considering the RF and check digit) |
| 4 | `INCOMING.PAYMENT.PARAM.PAYMENT.TYPE.LENGTH` | `FiipmtIncomingPaymentParam_PaymentTypeLength` | TField |  | Length of the Payment Type |
| 5 | `INCOMING.PAYMENT.PARAM.REPAYMENT.TYPE` | `FiipmtIncomingPaymentParam_RepaymentType` |  |  |  |
| 6 | `INCOMING.PAYMENT.PARAM.INITIATION.TYPE` | `FiipmtIncomingPaymentParam_InitiationType` |  |  |  |
| 7 | `INCOMING.PAYMENT.PARAM.ACCOUNT.NO.POSITION` | `FiipmtIncomingPaymentParam_AccountNoPosition` | TField |  | The Account Number will also be a Part of the Finnish Creditor Reference Number.( The Start Position and Length of the Account Number should be configured here.This has to be provided without considering the RF and check digit) |
| 8 | `INCOMING.PAYMENT.PARAM.ACCOUNT.NO.LENGTH` | `FiipmtIncomingPaymentParam_AccountNoLength` | TField |  | The length of the account number |
| 9 | `INCOMING.PAYMENT.PARAM.SUBSIDY.PROVIDER` | `FiipmtIncomingPaymentParam_SubsidyProvider` |  |  |  |
| 10 | `INCOMING.PAYMENT.PARAM.EXCESS.INT.ACCOUNT` | `FiipmtIncomingPaymentParam_ExcessIntAccount` |  |  |  |
| 11 | `INCOMING.PAYMENT.PARAM.RESERVED.5` | `FiipmtIncomingPaymentParam_Reserved5` | TField |  |  |
| 12 | `INCOMING.PAYMENT.PARAM.RESERVED.4` | `FiipmtIncomingPaymentParam_Reserved4` | TField |  |  |
| 13 | `INCOMING.PAYMENT.PARAM.RESERVED.3` | `FiipmtIncomingPaymentParam_Reserved3` | TField |  |  |
| 14 | `INCOMING.PAYMENT.PARAM.RESERVED.2` | `FiipmtIncomingPaymentParam_Reserved2` | TField |  |  |
| 15 | `INCOMING.PAYMENT.PARAM.RESERVED.1` | `FiipmtIncomingPaymentParam_Reserved1` | TField |  |  |
| 16 | `INCOMING.PAYMENT.PARAM.LOCAL.REF` | `FiipmtIncomingPaymentParam_LocalRef` |  |  |  |
| 17 | `INCOMING.PAYMENT.PARAM.OVERRIDE` | `FiipmtIncomingPaymentParam_Override` |  |  |  |
| 18 | `INCOMING.PAYMENT.PARAM.RECORD.STATUS` | `FiipmtIncomingPaymentParam_RecordStatus` | String |  |  |
| 19 | `INCOMING.PAYMENT.PARAM.CURR.NO` | `FiipmtIncomingPaymentParam_CurrNo` | String |  |  |
| 20 | `INCOMING.PAYMENT.PARAM.INPUTTER` | `FiipmtIncomingPaymentParam_Inputter` |  |  |  |
| 21 | `INCOMING.PAYMENT.PARAM.DATE.TIME` | `FiipmtIncomingPaymentParam_DateTime` |  |  |  |
| 22 | `INCOMING.PAYMENT.PARAM.AUTHORISER` | `FiipmtIncomingPaymentParam_Authoriser` | String |  |  |
| 23 | `INCOMING.PAYMENT.PARAM.CO.CODE` | `FiipmtIncomingPaymentParam_CoCode` | String |  |  |
| 24 | `INCOMING.PAYMENT.PARAM.DEPT.CODE` | `FiipmtIncomingPaymentParam_DeptCode` | String |  |  |
| 25 | `INCOMING.PAYMENT.PARAM.AUDITOR.CODE` | `FiipmtIncomingPaymentParam_AuditorCode` | String |  |  |
| 26 | `INCOMING.PAYMENT.PARAM.AUDIT.DATE.TIME` | `FiipmtIncomingPaymentParam_AuditDateTime` | String |  |  |
