# FIVOCE.INVOICING.PARAM — Table Schema

> Source: `INSERTS/I_F.FIVOCE.INVOICING.PARAM` in `FIVOCE_InvoicingCreditNote.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIVOCE.INVPARAM.PRINCIPAL.INTEREST.PROPERTY` | `FivoceInvoicingParam_PrincipalInterestProperty` |  |  |  |
| 2 | `FIVOCE.INVPARAM.ACCOUNT.PROPERTY` | `FivoceInvoicingParam_AccountProperty` |  |  |  |
| 3 | `FIVOCE.INVPARAM.SUBSIDY.PROPERTY` | `FivoceInvoicingParam_SubsidyProperty` |  |  |  |
| 4 | `FIVOCE.INVPARAM.PENALTY.INTEREST.PROPERTY` | `FivoceInvoicingParam_PenaltyInterestProperty` |  |  |  |
| 5 | `FIVOCE.INVPARAM.CHARGE.PROPERTY` | `FivoceInvoicingParam_ChargeProperty` |  |  |  |
| 6 | `FIVOCE.INVPARAM.TAX.PROPERTY` | `FivoceInvoicingParam_TaxProperty` |  |  |  |
| 7 | `FIVOCE.INVPARAM.SELLER.CUSTOMER.ID` | `FivoceInvoicingParam_SellerCustomerId` | TField |  | Banks customer id can be configured so that the invoices will be filled with the sellers details from configured customer. |
| 8 | `FIVOCE.INVPARAM.SELLER.ACCOUNT` | `FivoceInvoicingParam_SellerAccount` |  |  |  |
| 9 | `FIVOCE.INVPARAM.SELLER.ACCOUNT.BIC` | `FivoceInvoicingParam_SellerAccountBic` |  |  |  |
| 10 | `FIVOCE.INVPARAM.MIN.INVOICE.AMT` | `FivoceInvoicingParam_MinInvoiceAmt` | TField |  | The amount below which the invoice will be sent to the next schedule date for a loan. |
| 11 | `FIVOCE.INVPARAM.ACTIVITY` | `FivoceInvoicingParam_Activity` |  |  |  |
| 12 | `FIVOCE.INVPARAM.START.POSITION` | `FivoceInvoicingParam_StartPosition` |  |  |  |
| 13 | `FIVOCE.INVPARAM.END.POSITION` | `FivoceInvoicingParam_EndPosition` |  |  |  |
| 14 | `FIVOCE.INVPARAM.FIELD.VALUE` | `FivoceInvoicingParam_FieldValue` |  |  |  |
| 15 | `FIVOCE.INVPARAM.CHECKSUM.ROUTINE` | `FivoceInvoicingParam_ChecksumRoutine` | TField |  | The routine which calculates check sum as per finish reference number standards. |
| 16 | `FIVOCE.INVPARAM.REQUEST.QUEUE` | `FivoceInvoicingParam_RequestQueue` | TField |  | Request queue name which is configured to send message. |
| 17 | `FIVOCE.INVPARAM.REPLY.QUEUE` | `FivoceInvoicingParam_ReplyQueue` | TField |  | Reply queue name which is configured to get message. |
| 18 | `FIVOCE.INVPARAM.CONNECTION.FACTORY` | `FivoceInvoicingParam_ConnectionFactory` | TField |  | Connection factory name. |
| 19 | `FIVOCE.INVPARAM.EVENT.FILE.NAME` | `FivoceInvoicingParam_EventFileName` | TField |  | Event file name. |
| 20 | `FIVOCE.INVPARAM.HEADER.TAG` | `FivoceInvoicingParam_HeaderTag` | TField |  | Header Tag of event file. |
| 21 | `FIVOCE.INVPARAM.FOOTER.TAG` | `FivoceInvoicingParam_FooterTag` | TField |  | Footer tag of event file. |
| 22 | `FIVOCE.INVPARAM.RECEIVABLE.TAG` | `FivoceInvoicingParam_ReceivableTag` | TField |  | Receivable tag of event file. |
| 23 | `FIVOCE.INVPARAM.INTEREST.INFO.TAG` | `FivoceInvoicingParam_InterestInfoTag` | TField |  | Interest info tag of event file |
| 24 | `FIVOCE.INVPARAM.INTEREST.BASIS.TAG` | `FivoceInvoicingParam_InterestBasisTag` | TField |  | Interest basis tag of event file. |
| 25 | `FIVOCE.INVPARAM.FINANCIAL.INST.CODE` | `FivoceInvoicingParam_FinancialInstCode` | TField |  | Financial institution code. |
| 26 | `FIVOCE.INVPARAM.STATE.TREASURY.INT.BASIC.CODE` | `FivoceInvoicingParam_StateTreasuryIntBasicCode` |  |  |  |
| 27 | `FIVOCE.INVPARAM.T24.INT.BASIC.CODE` | `FivoceInvoicingParam_T24IntBasicCode` |  |  |  |
| 28 | `FIVOCE.INVPARAM.CHECKSUM.VAL` | `FivoceInvoicingParam_ChecksumVal` | TField |  | This field is used to do checksum validation. |
| 29 | `FIVOCE.INVPARAM.PERFORM.CHECK` | `FivoceInvoicingParam_PerformCheck` | TField |  | This field indicates whether to consider the values of the table FIVOCE.INVOICING.PARAM or not.. YES - Consider the values from the parameter table FIVOCE.INVOICING.PARAM for invoicing . NO - Skip the parameter table . |
| 30 | `FIVOCE.INVPARAM.AGREEMENT.IDENTIFIER` | `FivoceInvoicingParam_AgreementIdentifier` | TField |  | Alternate Account type for ASTA Loan ID to be configured here |
| 31 | `FIVOCE.INVPARAM.PRINCIPAL.NAME` | `FivoceInvoicingParam_PrincipalName` | TField |  | Finnish name for the principal component that needs to be updated in invoice XML |
| 32 | `FIVOCE.INVPARAM.PRINCIPAL.INTEREST.NAME` | `FivoceInvoicingParam_PrincipalInterestName` | TField |  | Finnish name for the principal interest and subsidy interest component that needs to be updated in invoice XML |
| 33 | `FIVOCE.INVPARAM.INTEREST.DAYS.NAME` | `FivoceInvoicingParam_InterestDaysName` | TField |  | Finnish name for the interest days that needs to be updated in invoice XML |
| 34 | `FIVOCE.INVPARAM.PENALTY.INTEREST.NAME` | `FivoceInvoicingParam_PenaltyInterestName` | TField |  | Finnish name for the penalty interest component that needs to be updated in invoice XML |
| 35 | `FIVOCE.INVPARAM.CHARGE.NAME` | `FivoceInvoicingParam_ChargeName` | TField |  | Finnish name for the Charge/Cost / Fee component that needs to be updated in invoice XML |
| 36 | `FIVOCE.INVPARAM.TAX.VAT.NAME` | `FivoceInvoicingParam_TaxVatName` | TField |  | Finnish name for the Tax/Vat component that needs to be updated in invoice XML |
| 37 | `FIVOCE.INVPARAM.RESERVED.11` | `FivoceInvoicingParam_Reserved11` |  |  |  |
| 38 | `FIVOCE.INVPARAM.RESERVED.10` | `FivoceInvoicingParam_Reserved10` |  |  |  |
| 39 | `FIVOCE.INVPARAM.RESERVED.9` | `FivoceInvoicingParam_Reserved9` |  |  |  |
| 40 | `FIVOCE.INVPARAM.RESERVED.8` | `FivoceInvoicingParam_Reserved8` | TField |  | Reserved for future use. |
| 41 | `FIVOCE.INVPARAM.RESERVED.7` | `FivoceInvoicingParam_Reserved7` | TField |  | Reserved for future use. |
| 42 | `FIVOCE.INVPARAM.RESERVED.6` | `FivoceInvoicingParam_Reserved6` | TField |  | Reserved for future use. |
| 43 | `FIVOCE.INVPARAM.RESERVED.5` | `FivoceInvoicingParam_Reserved5` | TField |  | Reserved for future use. |
| 44 | `FIVOCE.INVPARAM.RESERVED.4` | `FivoceInvoicingParam_Reserved4` | TField |  | Reserved for future use. |
| 45 | `FIVOCE.INVPARAM.RESERVED.3` | `FivoceInvoicingParam_Reserved3` | TField |  | Reserved for future use. |
| 46 | `FIVOCE.INVPARAM.RESERVED.2` | `FivoceInvoicingParam_Reserved2` | TField |  | Reserved for future use. |
| 47 | `FIVOCE.INVPARAM.RESERVED.1` | `FivoceInvoicingParam_Reserved1` | TField |  | Reserved for future use. |
| 48 | `FIVOCE.INVPARAM.LOCAL.REF` | `FivoceInvoicingParam_LocalRef` |  |  |  |
| 49 | `FIVOCE.INVPARAM.OVERRIDE` | `FivoceInvoicingParam_Override` |  |  |  |
| 50 | `FIVOCE.INVPARAM.RECORD.STATUS` | `FivoceInvoicingParam_RecordStatus` | String |  |  |
| 51 | `FIVOCE.INVPARAM.CURR.NO` | `FivoceInvoicingParam_CurrNo` | String |  |  |
| 52 | `FIVOCE.INVPARAM.INPUTTER` | `FivoceInvoicingParam_Inputter` |  |  |  |
| 53 | `FIVOCE.INVPARAM.DATE.TIME` | `FivoceInvoicingParam_DateTime` |  |  |  |
| 54 | `FIVOCE.INVPARAM.AUTHORISER` | `FivoceInvoicingParam_Authoriser` | String |  |  |
| 55 | `FIVOCE.INVPARAM.CO.CODE` | `FivoceInvoicingParam_CoCode` | String |  |  |
| 56 | `FIVOCE.INVPARAM.DEPT.CODE` | `FivoceInvoicingParam_DeptCode` | String |  |  |
| 57 | `FIVOCE.INVPARAM.AUDITOR.CODE` | `FivoceInvoicingParam_AuditorCode` | String |  |  |
| 58 | `FIVOCE.INVPARAM.AUDIT.DATE.TIME` | `FivoceInvoicingParam_AuditDateTime` | String |  |  |
