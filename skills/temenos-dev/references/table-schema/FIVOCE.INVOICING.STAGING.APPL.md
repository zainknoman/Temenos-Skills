# FIVOCE.INVOICING.STAGING.APPL — Table Schema

> Source: `INSERTS/I_F.FIVOCE.INVOICING.STAGING.APPL` in `FIVOCE_InvoicingCreditNote.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIVOCE.INVSTAGING.CREDITOR.REFERENCE.NUMBER` | `FivoceInvoicingStagingAppl_CreditorReferenceNumber` | TField |  | This reference number will be part of every invoice that is generated. The buyer will make the payments using this creditor reference number. |
| 2 | `FIVOCE.INVSTAGING.RECEIVER.ID` | `FivoceInvoicingStagingAppl_ReceiverId` | TField |  | ID of the buyer. Buyer can be customer, state treasury and any other subsidy provider. |
| 3 | `FIVOCE.INVSTAGING.ACCOUNT` | `FivoceInvoicingStagingAppl_Account` |  |  |  |
| 4 | `FIVOCE.INVSTAGING.ACCOUNT.PROPERTY` | `FivoceInvoicingStagingAppl_AccountProperty` |  |  |  |
| 5 | `FIVOCE.INVSTAGING.ACCOUNT.AMOUNT` | `FivoceInvoicingStagingAppl_AccountAmount` |  |  |  |
| 6 | `FIVOCE.INVSTAGING.ACCOUNT.CURRENCY` | `FivoceInvoicingStagingAppl_AccountCurrency` |  |  |  |
| 7 | `FIVOCE.INVSTAGING.INTEREST` | `FivoceInvoicingStagingAppl_Interest` |  |  |  |
| 8 | `FIVOCE.INVSTAGING.INTEREST.PROPERTY` | `FivoceInvoicingStagingAppl_InterestProperty` |  |  |  |
| 9 | `FIVOCE.INVSTAGING.INTEREST.AMOUNT` | `FivoceInvoicingStagingAppl_InterestAmount` |  |  |  |
| 10 | `FIVOCE.INVSTAGING.INTEREST.CURRENCY` | `FivoceInvoicingStagingAppl_InterestCurrency` |  |  |  |
| 11 | `FIVOCE.INVSTAGING.SUBSIDY.INTEREST` | `FivoceInvoicingStagingAppl_SubsidyInterest` |  |  |  |
| 12 | `FIVOCE.INVSTAGING.SUBSIDY.INTEREST.PROPERTY` | `FivoceInvoicingStagingAppl_SubsidyInterestProperty` |  |  |  |
| 13 | `FIVOCE.INVSTAGING.SUBSIDY.INTEREST.AMOUNT` | `FivoceInvoicingStagingAppl_SubsidyInterestAmount` |  |  |  |
| 14 | `FIVOCE.INVSTAGING.SUBSIDY.INTEREST.CURRENCY` | `FivoceInvoicingStagingAppl_SubsidyInterestCurrency` |  |  |  |
| 15 | `FIVOCE.INVSTAGING.PENALTY.INTEREST` | `FivoceInvoicingStagingAppl_PenaltyInterest` |  |  |  |
| 16 | `FIVOCE.INVSTAGING.PENALTY.INTEREST.PROPERTY` | `FivoceInvoicingStagingAppl_PenaltyInterestProperty` |  |  |  |
| 17 | `FIVOCE.INVSTAGING.PENALTY.INTEREST.AMOUNT` | `FivoceInvoicingStagingAppl_PenaltyInterestAmount` |  |  |  |
| 18 | `FIVOCE.INVSTAGING.PENALTY.INTEREST.CURRENCY` | `FivoceInvoicingStagingAppl_PenaltyInterestCurrency` |  |  |  |
| 19 | `FIVOCE.INVSTAGING.CHARGE` | `FivoceInvoicingStagingAppl_Charge` |  |  |  |
| 20 | `FIVOCE.INVSTAGING.CHARGE.PROPERTY` | `FivoceInvoicingStagingAppl_ChargeProperty` |  |  |  |
| 21 | `FIVOCE.INVSTAGING.CHARGE.AMOUNT` | `FivoceInvoicingStagingAppl_ChargeAmount` |  |  |  |
| 22 | `FIVOCE.INVSTAGING.CHARGE.CURRENCY` | `FivoceInvoicingStagingAppl_ChargeCurrency` |  |  |  |
| 23 | `FIVOCE.INVSTAGING.TAX` | `FivoceInvoicingStagingAppl_Tax` |  |  |  |
| 24 | `FIVOCE.INVSTAGING.TAX.PROPERTY` | `FivoceInvoicingStagingAppl_TaxProperty` |  |  |  |
| 25 | `FIVOCE.INVSTAGING.TAX.AMOUNT` | `FivoceInvoicingStagingAppl_TaxAmount` |  |  |  |
| 26 | `FIVOCE.INVSTAGING.TAX.CURRENCY` | `FivoceInvoicingStagingAppl_TaxCurrency` |  |  |  |
| 27 | `FIVOCE.INVSTAGING.CURRENT.INVOICE.TYPE` | `FivoceInvoicingStagingAppl_CurrentInvoiceType` | TField |  | The type of invoice that is currently generated in T24 is updated in this field. |
| 28 | `FIVOCE.INVSTAGING.CURRENT.INVOICE.NO` | `FivoceInvoicingStagingAppl_CurrentInvoiceNo` | TField |  | The Invoice number will be formed with Invoice type, issue date, and sequence number. |
| 29 | `FIVOCE.INVSTAGING.CURRENT.INVOICE.DATE` | `FivoceInvoicingStagingAppl_CurrentInvoiceDate` | TField |  | The date on which the invoice is created in T24 is updated in this field. |
| 30 | `FIVOCE.INVSTAGING.CURRENT.INVOICE.GEN.DATE` | `FivoceInvoicingStagingAppl_CurrentInvoiceGenDate` | TField |  | The date on which the XML is created by T24. |
| 31 | `FIVOCE.INVSTAGING.CURRENT.INVOICE.STATUS` | `FivoceInvoicingStagingAppl_CurrentInvoiceStatus` | TField |  | The current status of the invoice will be updated in this field. |
| 32 | `FIVOCE.INVSTAGING.PREVIOUS.INVOICE.TYPE` | `FivoceInvoicingStagingAppl_PreviousInvoiceType` |  |  |  |
| 33 | `FIVOCE.INVSTAGING.PREVIOUS.INVOICE.NO` | `FivoceInvoicingStagingAppl_PreviousInvoiceNo` |  |  |  |
| 34 | `FIVOCE.INVSTAGING.PREVIOUS.INVOICE.DATE` | `FivoceInvoicingStagingAppl_PreviousInvoiceDate` |  |  |  |
| 35 | `FIVOCE.INVSTAGING.PREVIOUS.INVOICE.GEN.DATE` | `FivoceInvoicingStagingAppl_PreviousInvoiceGenDate` |  |  |  |
| 36 | `FIVOCE.INVSTAGING.PREVIOUS.INVOICE.STATUS` | `FivoceInvoicingStagingAppl_PreviousInvoiceStatus` |  |  |  |
| 37 | `FIVOCE.INVSTAGING.T24.BILL.ID` | `FivoceInvoicingStagingAppl_T24BillId` |  |  |  |
| 38 | `FIVOCE.INVSTAGING.T24.REVERSED.BILL.ID` | `FivoceInvoicingStagingAppl_T24ReversedBillId` | TField |  | When a bill is reversed in T24 the corresponding new bill id will be stored in this field. |
| 39 | `FIVOCE.INVSTAGING.BATCH.NO` | `FivoceInvoicingStagingAppl_BatchNo` | TField |  | The bank can send the invoices in batches if required. So when the XML is created for each invoice this value will be updated with the batch number for the day. |
| 40 | `FIVOCE.INVSTAGING.SUBSIDY.FILE.COUNTER` | `FivoceInvoicingStagingAppl_SubsidyFileCounter` | TField |  | This field is for subsidy invoice only. When event file is generated this counter is updated. |
| 41 | `FIVOCE.INVSTAGING.ERROR.CODE` | `FivoceInvoicingStagingAppl_ErrorCode` | TField |  | When an invoice is rejected the appropriate error code can be updated in this field. |
| 42 | `FIVOCE.INVSTAGING.ERROR.DESC` | `FivoceInvoicingStagingAppl_ErrorDesc` |  |  |  |
| 43 | `FIVOCE.INVSTAGING.RESERVED.13` | `FivoceInvoicingStagingAppl_Reserved13` |  |  |  |
| 44 | `FIVOCE.INVSTAGING.RESERVED.12` | `FivoceInvoicingStagingAppl_Reserved12` |  |  |  |
| 45 | `FIVOCE.INVSTAGING.RESERVED.11` | `FivoceInvoicingStagingAppl_Reserved11` | TField |  | Reserved for future use. |
| 46 | `FIVOCE.INVSTAGING.RESERVED.10` | `FivoceInvoicingStagingAppl_Reserved10` | TField |  | Reserved for future use. |
| 47 | `FIVOCE.INVSTAGING.RESERVED.9` | `FivoceInvoicingStagingAppl_Reserved9` | TField |  | Reserved for future use. |
| 48 | `FIVOCE.INVSTAGING.RESERVED.8` | `FivoceInvoicingStagingAppl_Reserved8` | TField |  | Reserved for future use. |
| 49 | `FIVOCE.INVSTAGING.RESERVED.7` | `FivoceInvoicingStagingAppl_Reserved7` | TField |  | Reserved for future use. |
| 50 | `FIVOCE.INVSTAGING.RESERVED.6` | `FivoceInvoicingStagingAppl_Reserved6` | TField |  | Reserved for future use. |
| 51 | `FIVOCE.INVSTAGING.RESERVED.5` | `FivoceInvoicingStagingAppl_Reserved5` | TField |  | Reserved for future use. |
| 52 | `FIVOCE.INVSTAGING.RESERVED.4` | `FivoceInvoicingStagingAppl_Reserved4` | TField |  | Reserved for future use. |
| 53 | `FIVOCE.INVSTAGING.RESERVED.3` | `FivoceInvoicingStagingAppl_Reserved3` | TField |  | Reserved for future use. |
| 54 | `FIVOCE.INVSTAGING.RESERVED.2` | `FivoceInvoicingStagingAppl_Reserved2` | TField |  | Reserved for future use. |
| 55 | `FIVOCE.INVSTAGING.RESERVED.1` | `FivoceInvoicingStagingAppl_Reserved1` | TField |  | Reserved for future use. |
