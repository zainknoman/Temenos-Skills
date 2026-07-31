# CHEQUE.ADVICE — Table Schema

> Source: `INSERTS/I_F.CHEQUE.ADVICE` in `CQ_ChqConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHAD.DIRECTION` | `ChequeAdvice_Direction` | TField |  | The field will indicate if record is created from incoming MT110 or outgoing MT110. Validation Rules: Allowed values are OUTWARD/INWARD. Default value is INWARD |
| 2 | `CHAD.DRAWER.BANK.ACCOUNT` | `ChequeAdvice_DrawerBankAccount` | TField |  | The field indicates account of drawer bank Validation rules: Valid T24 Account |
| 3 | `CHAD.CHEQUE.NUMBER` | `ChequeAdvice_ChequeNumber` | TField |  | The field indicates number of the cheque to which the message refers |
| 4 | `CHAD.CHEQUE.TYPE` | `ChequeAdvice_ChequeType` | TField |  |  |
| 5 | `CHAD.DATE.OF.ISSUE` | `ChequeAdvice_DateOfIssue` | TField |  | This field contains the date on which the cheque was issued (drawn) |
| 6 | `CHAD.VALUE.DATE` | `ChequeAdvice_ValueDate` | TField |  | This field is used when the Drawer Bank has previously credited the Drawee Bank with the cheque amount. |
| 7 | `CHAD.CHEQUE.CCY` | `ChequeAdvice_ChequeCcy` | TField |  | This field identifies the currency of the cheque Validation Rules: Valid currency record |
| 8 | `CHAD.CHEQUE.AMOUNT` | `ChequeAdvice_ChequeAmount` | TField |  | This field identifies the amount of the cheque |
| 9 | `CHAD.REFERENCE` | `ChequeAdvice_Reference` | TField |  | The field identifies the Transaction Reference Number assigned by the Sender to unambiguously identify the message Validation Rules: Free text of length 35 accepting alphanumeric characters |
| 10 | `CHAD.PAYER` | `ChequeAdvice_Payer` |  |  |  |
| 11 | `CHAD.IN.DRAWER.BANK` | `ChequeAdvice_InDrawerBank` |  |  |  |
| 12 | `CHAD.DRAWER.BANK.BIC` | `ChequeAdvice_DrawerBankBic` | TField |  | Field indicates the BIC of sender of 110 message |
| 13 | `CHAD.PAYEE` | `ChequeAdvice_Payee` |  |  |  |
| 14 | `CHAD.PAYEE.ACCOUNT.NO` | `ChequeAdvice_PayeeAccountNo` | TField |  | The field indicates account number of Payee. |
| 15 | `CHAD.PAYEE.NAME.ADDRESS` | `ChequeAdvice_PayeeNameAddress` |  |  |  |
| 16 | `CHAD.SENDER.CORR.BANK` | `ChequeAdvice_SenderCorrBank` |  |  |  |
| 17 | `CHAD.RECEIVER.CORR.BANK` | `ChequeAdvice_ReceiverCorrBank` |  |  |  |
| 18 | `CHAD.SENDER.RECEIVER.INFO` | `ChequeAdvice_SenderReceiverInfo` |  |  |  |
| 19 | `CHAD.IN.DELIVERY.REF` | `ChequeAdvice_InDeliveryRef` | TField |  | The field indicates the inward delivery reference created when MT110 message is received. Validation Rules: NOINPUT field. System updated |
| 20 | `CHAD.IN.PROCESS.ERR` | `ChequeAdvice_InProcessErr` |  |  |  |
| 21 | `CHAD.RESERVED.5` | `ChequeAdvice_Reserved5` | TField |  |  |
| 22 | `CHAD.RESERVED.4` | `ChequeAdvice_Reserved4` | TField |  |  |
| 23 | `CHAD.RESERVED.3` | `ChequeAdvice_Reserved3` | TField |  |  |
| 24 | `CHAD.RESERVED.2` | `ChequeAdvice_Reserved2` | TField |  |  |
| 25 | `CHAD.RESERVED.1` | `ChequeAdvice_Reserved1` | TField |  |  |
| 26 | `CHAD.LOCAL.REF` | `ChequeAdvice_LocalRef` |  |  |  |
| 27 | `CHAD.OVERRIDE` | `ChequeAdvice_Override` |  |  |  |
| 28 | `CHAD.RECORD.STATUS` | `ChequeAdvice_RecordStatus` | String |  |  |
| 29 | `CHAD.CURR.NO` | `ChequeAdvice_CurrNo` | String |  |  |
| 30 | `CHAD.INPUTTER` | `ChequeAdvice_Inputter` |  |  |  |
| 31 | `CHAD.DATE.TIME` | `ChequeAdvice_DateTime` |  |  |  |
| 32 | `CHAD.AUTHORISER` | `ChequeAdvice_Authoriser` | String |  |  |
| 33 | `CHAD.CO.CODE` | `ChequeAdvice_CoCode` | String |  |  |
| 34 | `CHAD.DEPT.CODE` | `ChequeAdvice_DeptCode` | String |  |  |
| 35 | `CHAD.AUDITOR.CODE` | `ChequeAdvice_AuditorCode` | String |  |  |
| 36 | `CHAD.AUDIT.DATE.TIME` | `ChequeAdvice_AuditDateTime` | String |  |  |
