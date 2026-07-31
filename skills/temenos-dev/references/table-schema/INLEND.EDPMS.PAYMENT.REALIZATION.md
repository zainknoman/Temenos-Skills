# INLEND.EDPMS.PAYMENT.REALIZATION — Table Schema

> Source: `INSERTS/I_F.INLEND.EDPMS.PAYMENT.REALIZATION` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.EDPMS.TRANSACTION.CURRENCY` | `InlendEdpmsPaymentRealization_TransactionCurrency` | TField |  | Transaction Currency. A Valid record from CURRENCY table. |
| 2 | `INLEND.EDPMS.TRANSACTION.AMOUNT` | `InlendEdpmsPaymentRealization_TransactionAmount` | TField |  | Transaction Amount of Credit Transaction. |
| 3 | `INLEND.EDPMS.TRANSACTION.DATE` | `InlendEdpmsPaymentRealization_TransactionDate` | TField |  | Date of Transaction. |
| 4 | `INLEND.EDPMS.SETTLED.AMOUNT` | `InlendEdpmsPaymentRealization_SettledAmount` | TField |  | Settled amount out of transaction amount |
| 5 | `INLEND.EDPMS.IS.SETTLEMENT.FIRC` | `InlendEdpmsPaymentRealization_IsSettlementFirc` | TField |  | Indicates whether payment realization is by way of FIRC. Allowed values are YES or NO |
| 6 | `INLEND.EDPMS.FIRC.NUMBER` | `InlendEdpmsPaymentRealization_FircNumber` | TField |  | A Valid record from INLEND.EDPMS.FIRC. |
| 7 | `INLEND.EDPMS.FIRC.CURRENCY` | `InlendEdpmsPaymentRealization_FircCurrency` | TField |  | Currency of FIRC |
| 8 | `INLEND.EDPMS.FIRC.AMOUNT` | `InlendEdpmsPaymentRealization_FircAmount` | TField |  | Amount of FIRC |
| 9 | `INLEND.EDPMS.FIRC.UNUTILIZED.AMOUNT` | `InlendEdpmsPaymentRealization_FircUnutilizedAmount` | TField |  | Un-utilized amount of FIRC |
| 10 | `INLEND.EDPMS.PAYMENT.PARTY` | `InlendEdpmsPaymentRealization_PaymentParty` | TField |  | Third Party Payment. Drop-down field. Allowed values are Y or N. |
| 11 | `INLEND.EDPMS.SHIPPING.BILL.NUMBER` | `InlendEdpmsPaymentRealization_ShippingBillNumber` |  |  |  |
| 12 | `INLEND.EDPMS.DRAWING.REF.NUMBER` | `InlendEdpmsPaymentRealization_DrawingRefNumber` |  |  |  |
| 13 | `INLEND.EDPMS.INVOICE.NUMBER` | `InlendEdpmsPaymentRealization_InvoiceNumber` |  |  |  |
| 14 | `INLEND.EDPMS.INVOICE.CURRENCY` | `InlendEdpmsPaymentRealization_InvoiceCurrency` |  |  |  |
| 15 | `INLEND.EDPMS.INVOICE.AMOUNT` | `InlendEdpmsPaymentRealization_InvoiceAmount` |  |  |  |
| 16 | `INLEND.EDPMS.ADJ.REMIT.AMOUNT` | `InlendEdpmsPaymentRealization_AdjRemitAmount` |  |  |  |
| 17 | `INLEND.EDPMS.EXCHANGE.RATE` | `InlendEdpmsPaymentRealization_ExchangeRate` |  |  |  |
| 18 | `INLEND.EDPMS.EQUI.INVOICE.AMOUNT` | `InlendEdpmsPaymentRealization_EquiInvoiceAmount` |  |  |  |
| 19 | `INLEND.EDPMS.FREIGHT.AMOUNT` | `InlendEdpmsPaymentRealization_FreightAmount` |  |  |  |
| 20 | `INLEND.EDPMS.FREIGHT.EXCHANGE.RATE` | `InlendEdpmsPaymentRealization_FreightExchangeRate` |  |  |  |
| 21 | `INLEND.EDPMS.EQUI.FREIGHT.AMT.INV.CURR` | `InlendEdpmsPaymentRealization_EquiFreightAmtInvCurr` |  |  |  |
| 22 | `INLEND.EDPMS.INSURANCE.AMOUNT` | `InlendEdpmsPaymentRealization_InsuranceAmount` |  |  |  |
| 23 | `INLEND.EDPMS.INSURANCE.EXCHANGE.RATE` | `InlendEdpmsPaymentRealization_InsuranceExchangeRate` |  |  |  |
| 24 | `INLEND.EDPMS.EQUI.INSURANCE.AMT.INV.CURR` | `InlendEdpmsPaymentRealization_EquiInsuranceAmtInvCurr` |  |  |  |
| 25 | `INLEND.EDPMS.FOREIGN.BANK.CHARGES` | `InlendEdpmsPaymentRealization_ForeignBankCharges` |  |  |  |
| 26 | `INLEND.EDPMS.PAYMENT.SEQ.NUMBER` | `InlendEdpmsPaymentRealization_PaymentSeqNumber` | TField |  | A Unique Payment Sequence Number |
| 27 | `INLEND.EDPMS.REMITTER.NAME` | `InlendEdpmsPaymentRealization_RemitterName` |  |  |  |
| 28 | `INLEND.EDPMS.REMITTER.COUNTRY` | `InlendEdpmsPaymentRealization_RemitterCountry` | TField |  | Remitter Country |
| 29 | `INLEND.EDPMS.RECEIVER.ACCT.NUMBER` | `InlendEdpmsPaymentRealization_ReceiverAcctNumber` | TField |  | Receiver Account Number |
| 30 | `INLEND.EDPMS.RECORD.INDICATOR` | `InlendEdpmsPaymentRealization_RecordIndicator` | TField |  | Record Indicator |
| 31 | `INLEND.EDPMS.PROCESS.DATE` | `InlendEdpmsPaymentRealization_ProcessDate` |  |  |  |
| 32 | `INLEND.EDPMS.ERROR.STATUS` | `InlendEdpmsPaymentRealization_ErrorStatus` |  |  |  |
| 33 | `INLEND.EDPMS.TRANSMIT.INDICATOR` | `InlendEdpmsPaymentRealization_TransmitIndicator` | TField |  | Drop-down field. A Valid record from INLEND.TRANSMIT.INDICATOR. System updated field |
| 34 | `INLEND.EDPMS.CREDIT.COMPANY.CODE` | `InlendEdpmsPaymentRealization_CreditCompanyCode` | TField |  | A Valid company record. Should default to CreditAccountCompany of PP.ORDER.ENTRY. Defaulted based on @ID. System updated field. |
| 35 | `INLEND.EDPMS.CREDIT.CUST.ID` | `InlendEdpmsPaymentRealization_CreditCustId` | TField |  | Customer ID of customer who has received the credit (CreditAccountNumber of PP.ORDER.ENTRY should be used to fetch Customer ID). Defaulted based on @ID. System updated field. |
| 36 | `INLEND.EDPMS.FIRC.AD.CODE` | `InlendEdpmsPaymentRealization_FircAdCode` | TField | Yes | FIRC AD Code. Defaulted from OTHER BANK FIRC based on FIRC.NUMBER. Mandatory, if IS.SETTLEMENT.FIRC = YES. |
| 37 | `INLEND.EDPMS.FIRC.IE.CODE` | `InlendEdpmsPaymentRealization_FircIeCode` | TField | Yes | FIRC IE Code. Defaulted from OTHER BANK FIRC based on FIRC.NUMBER. Mandatory, if IS.SETTLEMENT.FIRC = YES. |
| 38 | `INLEND.EDPMS.FIRC.ISSUE.DATE` | `InlendEdpmsPaymentRealization_FircIssueDate` | TField | Yes | Date of FIRC. Defaulted from OTHER BANK FIRC based on FIRC.NUMBER. Mandatory, if IS.SETTLEMENT.FIRC = YES. |
| 39 | `INLEND.EDPMS.FRGN.BANK.CHARGES` | `InlendEdpmsPaymentRealization_FrgnBankCharges` | TField |  | Foreign Bank Charges paid for realization. User input. Foreign Bank charges will be assumed to be in Transaction currency. |
| 40 | `INLEND.EDPMS.FIRC.UTILIZED.AMOUNT` | `InlendEdpmsPaymentRealization_FircUtilizedAmount` | TField |  | Utilized amount of FIRC. Defaulted from FIRC.UTILIZED.AMOUNT of OTHER BANK FIRC based on FIRC.NUMBER. System updated field. |
| 41 | `INLEND.EDPMS.INTERFACE.ERROR.RESPONSE` | `InlendEdpmsPaymentRealization_InterfaceErrorResponse` | TField |  | Error response updated by EDPMS. |
| 42 | `INLEND.EDPMS.LOCAL.REF` | `InlendEdpmsPaymentRealization_LocalRef` |  |  |  |
| 43 | `INLEND.EDPMS.OVERRIDE` | `InlendEdpmsPaymentRealization_Override` |  |  |  |
| 44 | `INLEND.EDPMS.RECORD.STATUS` | `InlendEdpmsPaymentRealization_RecordStatus` | String |  |  |
| 45 | `INLEND.EDPMS.CURR.NO` | `InlendEdpmsPaymentRealization_CurrNo` | String |  |  |
| 46 | `INLEND.EDPMS.INPUTTER` | `InlendEdpmsPaymentRealization_Inputter` |  |  |  |
| 47 | `INLEND.EDPMS.DATE.TIME` | `InlendEdpmsPaymentRealization_DateTime` |  |  |  |
| 48 | `INLEND.EDPMS.AUTHORISER` | `InlendEdpmsPaymentRealization_Authoriser` | String |  |  |
| 49 | `INLEND.EDPMS.CO.CODE` | `InlendEdpmsPaymentRealization_CoCode` | String |  |  |
| 50 | `INLEND.EDPMS.DEPT.CODE` | `InlendEdpmsPaymentRealization_DeptCode` | String |  |  |
| 51 | `INLEND.EDPMS.AUDITOR.CODE` | `InlendEdpmsPaymentRealization_AuditorCode` | String |  |  |
| 52 | `INLEND.EDPMS.AUDIT.DATE.TIME` | `InlendEdpmsPaymentRealization_AuditDateTime` | String |  |  |
| 53 | `INLEND.EDPMS.SETTLE.INV.FREIGHT.AMOUNT` | `InlendEdpmsPaymentRealization_SettleInvFreightAmount` |  |  |  |
| 54 | `INLEND.EDPMS.SETTLE.INV.INS.AMOUNT` | `InlendEdpmsPaymentRealization_SettleInvInsAmount` |  |  |  |
| 55 | `INLEND.EDPMS.EDPMS.PRN.PROCESS.NAME` | `InlendEdpmsPaymentRealization_EdpmsPrnProcessName` | TField |  | Indicates the Payment realization Process. |
