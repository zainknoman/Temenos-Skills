# POR.POSTING.AND.CONFIRMATION — Table Schema

> Source: `INSERTS/I_F.POR.POSTING.AND.CONFIRMATION` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PORPD.CHARGE.PARTY.INDICATOR` | `PorPostingAndConfirmation_ChargePartyIndicator` |  |  |  |
| 2 | `PORPD.FEE.TYPE` | `PorPostingAndConfirmation_FeeType` |  |  |  |
| 3 | `PORPD.CHARGE.SIGN` | `PorPostingAndConfirmation_ChargeSign` |  |  |  |
| 4 | `PORPD.TYPE.OF.CHARGE` | `PorPostingAndConfirmation_TypeOfCharge` |  |  |  |
| 5 | `PORPD.FEE.DESCRIPTION` | `PorPostingAndConfirmation_FeeDescription` |  |  |  |
| 6 | `PORPD.CHARGE.AMOUNT` | `PorPostingAndConfirmation_ChargeAmount` |  |  |  |
| 7 | `PORPD.CHARGE.AMOUNT.CURRENCY` | `PorPostingAndConfirmation_ChargeAmountCurrency` |  |  |  |
| 8 | `PORPD.CHARGE.AMOUNT.LOCAL.CCY` | `PorPostingAndConfirmation_ChargeAmountLocalCcy` |  |  |  |
| 9 | `PORPD.LOCAL.CCY.CODE` | `PorPostingAndConfirmation_LocalCcyCode` |  |  |  |
| 10 | `PORPD.CHARGE.AMOUNT.FEE.CURRENCY` | `PorPostingAndConfirmation_ChargeAmountFeeCurrency` |  |  |  |
| 11 | `PORPD.FEE.CURRENCY.CODE` | `PorPostingAndConfirmation_FeeCurrencyCode` |  |  |  |
| 12 | `PORPD.PL.ACCOUNT.COMPANY` | `PorPostingAndConfirmation_PlAccountCompany` |  |  |  |
| 13 | `PORPD.PL.ACCOUNT.NUMBER` | `PorPostingAndConfirmation_PlAccountNumber` |  |  |  |
| 14 | `PORPD.PL.ACCOUNT.CURRENCY` | `PorPostingAndConfirmation_PlAccountCurrency` |  |  |  |
| 15 | `PORPD.PARENT.CHILD.INDICATOR` | `PorPostingAndConfirmation_ParentChildIndicator` |  |  |  |
| 16 | `PORPD.OUTGOING.OUR.CHARGE.IND` | `PorPostingAndConfirmation_OutgoingOurChargeInd` |  |  |  |
| 17 | `PORPD.CLIENT.CHARGES.ID` | `PorPostingAndConfirmation_ClientChargesId` |  |  |  |
| 18 | `PORPD.BANK.CHARGES.ID` | `PorPostingAndConfirmation_BankChargesId` |  |  |  |
| 19 | `PORPD.TAX.INDICATOR` | `PorPostingAndConfirmation_TaxIndicator` |  |  |  |
| 20 | `PORPD.TAX.PERCENTAGE` | `PorPostingAndConfirmation_TaxPercentage` |  |  |  |
| 21 | `PORPD.AMOUNT.FOR.TAX.LOCAL.CCY` | `PorPostingAndConfirmation_AmountForTaxLocalCcy` |  |  |  |
| 22 | `PORPD.AMOUNT.FOR.TAX.FEE.CCY` | `PorPostingAndConfirmation_AmountForTaxFeeCcy` |  |  |  |
| 23 | `PORPD.TAX.AMOUNT` | `PorPostingAndConfirmation_TaxAmount` |  |  |  |
| 24 | `PORPD.TAX.AMOUNT.LOCAL.CCY` | `PorPostingAndConfirmation_TaxAmountLocalCcy` |  |  |  |
| 25 | `PORPD.TAX.ID` | `PorPostingAndConfirmation_TaxId` |  |  |  |
| 26 | `PORPD.RESERVED.2` | `PorPostingAndConfirmation_Reserved2` |  |  |  |
| 27 | `PORPD.RESERVED.3` | `PorPostingAndConfirmation_Reserved3` |  |  |  |
| 28 | `PORPD.RESERVED.4` | `PorPostingAndConfirmation_Reserved4` |  |  |  |
| 29 | `PORPD.RESERVED.5` | `PorPostingAndConfirmation_Reserved5` |  |  |  |
| 30 | `PORPD.BOOKING.DATE` | `PorPostingAndConfirmation_BookingDate` | TField |  | Booking date for this posting entry. Validation Rules: 11 characters of type DATE |
| 31 | `PORPD.OUR.REFERENCE` | `PorPostingAndConfirmation_OurReference` | TField | No | This is an optional output from statement lines and if not defined in statement lines then this must be mapped with FTNumber. This should be mapped to OUR.REFERENCE field by posting interface so that T24 can use it for MT940 reporting (Tag61-subtag7). Validation Rules: 16 alphanumeric characters |
| 32 | `PORPD.LOCAL.CURRENCY.CODE` | `PorPostingAndConfirmation_LocalCurrencyCode` | TField |  | Local currency code for the owning bank. Holds a 3 character unique code which denotes a specific currency used in the system. Validation Rules: Currency should be a valid entry in Currency Table (PPT.CURRENCY). |
| 33 | `PORPD.POSTING.LINE.NUMBER` | `PorPostingAndConfirmation_PostingLineNumber` |  |  |  |
| 34 | `PORPD.STATEMENT.LINE.NUMBER` | `PorPostingAndConfirmation_StatementLineNumber` |  |  |  |
| 35 | `PORPD.STATEMENT.LINE` | `PorPostingAndConfirmation_StatementLine` |  |  |  |
| 36 | `PORPD.LINE.CONTINUITY.FLAG` | `PorPostingAndConfirmation_LineContinuityFlag` |  |  |  |
| 37 | `PORPD.RESERVATION.KEY` | `PorPostingAndConfirmation_ReservationKey` |  |  |  |
| 38 | `PORPD.ACCOUNT.NUMBER.COMPANY.ID` | `PorPostingAndConfirmation_AccountNumberCompanyId` |  |  |  |
| 39 | `PORPD.ACCOUNT.NUMBER` | `PorPostingAndConfirmation_AccountNumber` |  |  |  |
| 40 | `PORPD.ACCOUNT.CURRENCY` | `PorPostingAndConfirmation_AccountCurrency` |  |  |  |
| 41 | `PORPD.POSTING.LINE.DBT.CDT.IND` | `PorPostingAndConfirmation_PostingLineDbtCdtInd` |  |  |  |
| 42 | `PORPD.POSTING.AMOUNT` | `PorPostingAndConfirmation_PostingAmount` |  |  |  |
| 43 | `PORPD.POSTING.AMOUNT.CURRENCY` | `PorPostingAndConfirmation_PostingAmountCurrency` |  |  |  |
| 44 | `PORPD.POSTING.AMOUNT.LOCAL.CCY` | `PorPostingAndConfirmation_PostingAmountLocalCcy` |  |  |  |
| 45 | `PORPD.VALUE.DATE` | `PorPostingAndConfirmation_ValueDate` |  |  |  |
| 46 | `PORPD.EXPOSURE.DATE` | `PorPostingAndConfirmation_ExposureDate` |  |  |  |
| 47 | `PORPD.BOOKING.CODE` | `PorPostingAndConfirmation_BookingCode` |  |  |  |
| 48 | `PORPD.POSTING.TYPE.FLAG` | `PorPostingAndConfirmation_PostingTypeFlag` |  |  |  |
| 49 | `PORPD.ACCOUNT.OWNER.REFERENCE` | `PorPostingAndConfirmation_AccountOwnerReference` |  |  |  |
| 50 | `PORPD.SUPPLEMENTARY.DETAILS` | `PorPostingAndConfirmation_SupplementaryDetails` |  |  |  |
| 51 | `PORPD.DEPARTMENT.CODE` | `PorPostingAndConfirmation_DepartmentCode` |  |  |  |
| 52 | `PORPD.CURRENCY.MARKET` | `PorPostingAndConfirmation_CurrencyMarket` |  |  |  |
| 53 | `PORPD.DEALER.DESK` | `PorPostingAndConfirmation_DealerDesk` |  |  |  |
| 54 | `PORPD.CLIENT.ID` | `PorPostingAndConfirmation_ClientId` |  |  |  |
| 55 | `PORPD.BOOK.CODE` | `PorPostingAndConfirmation_BookCode` |  |  |  |
| 56 | `PORPD.SWIFT.TXN.TYPE.CODE` | `PorPostingAndConfirmation_SwiftTxnTypeCode` |  |  |  |
| 57 | `PORPD.REVERSAL.INDICATOR` | `PorPostingAndConfirmation_ReversalIndicator` |  |  |  |
| 58 | `PORPD.RESERVED.6` | `PorPostingAndConfirmation_Reserved6` |  |  |  |
| 59 | `PORPD.RESERVED.7` | `PorPostingAndConfirmation_Reserved7` |  |  |  |
| 60 | `PORPD.RESERVED.8` | `PorPostingAndConfirmation_Reserved8` |  |  |  |
| 61 | `PORPD.RESERVED.9` | `PorPostingAndConfirmation_Reserved9` |  |  |  |
| 62 | `PORPD.RESERVED.10` | `PorPostingAndConfirmation_Reserved10` |  |  |  |
| 63 | `PORPD.CONFIRMATION.TYPE` | `PorPostingAndConfirmation_ConfirmationType` |  |  |  |
| 64 | `PORPD.ADVICE.NUMBER` | `PorPostingAndConfirmation_AdviceNumber` |  |  |  |
| 65 | `PORPD.SEQUENCE.NUMBER` | `PorPostingAndConfirmation_SequenceNumber` |  |  |  |
| 66 | `PORPD.EMAIL.ID` | `PorPostingAndConfirmation_EmailId` |  |  |  |
| 67 | `PORPD.PHONE.NUMBER` | `PorPostingAndConfirmation_PhoneNumber` |  |  |  |
| 68 | `PORPD.ADVICE.TYPE` | `PorPostingAndConfirmation_AdviceType` |  |  |  |
| 69 | `PORPD.DEBIT.CREDIT.ADVICE` | `PorPostingAndConfirmation_DebitCreditAdvice` |  |  |  |
| 70 | `PORPD.PRODUCT.NAME` | `PorPostingAndConfirmation_ProductName` |  |  |  |
| 71 | `PORPD.PROCESSING.DATE` | `PorPostingAndConfirmation_ProcessingDate` |  |  |  |
| 72 | `PORPD.OTHER.DELIVERY.DETAILS` | `PorPostingAndConfirmation_OtherDeliveryDetails` |  |  |  |
| 73 | `PORPD.OTHER.INFO` | `PorPostingAndConfirmation_OtherInfo` |  |  |  |
| 74 | `PORPD.TRANSACTION.AMOUNT` | `PorPostingAndConfirmation_TransactionAmount` |  |  |  |
| 75 | `PORPD.TRANSACTION.CURRENCY.CODE` | `PorPostingAndConfirmation_TransactionCurrencyCode` |  |  |  |
| 76 | `PORPD.DEBIT.CLIENT.ID` | `PorPostingAndConfirmation_DebitClientId` |  |  |  |
| 77 | `PORPD.DEBIT.MAIN.ACC.COMPANY.ID` | `PorPostingAndConfirmation_DebitMainAccCompanyId` |  |  |  |
| 78 | `PORPD.DEBIT.MAIN.ACCOUNT` | `PorPostingAndConfirmation_DebitMainAccount` |  |  |  |
| 79 | `PORPD.DEBIT.MAIN.ACC.CCY.CODE` | `PorPostingAndConfirmation_DebitMainAccCcyCode` |  |  |  |
| 80 | `PORPD.DEBIT.VALUE.DATE` | `PorPostingAndConfirmation_DebitValueDate` |  |  |  |
| 81 | `PORPD.ORDERING.PARTY.ACC.NUMBER` | `PorPostingAndConfirmation_OrderingPartyAccNumber` |  |  |  |
| 82 | `PORPD.ORDERING.PARTY.NAME` | `PorPostingAndConfirmation_OrderingPartyName` |  |  |  |
| 83 | `PORPD.CREDIT.CLIENT.ID` | `PorPostingAndConfirmation_CreditClientId` |  |  |  |
| 84 | `PORPD.CREDIT.MAIN.ACC.COMPANY.ID` | `PorPostingAndConfirmation_CreditMainAccCompanyId` |  |  |  |
| 85 | `PORPD.CREDIT.MAIN.ACCOUNT` | `PorPostingAndConfirmation_CreditMainAccount` |  |  |  |
| 86 | `PORPD.CREDIT.MAIN.ACC.CCY.CODE` | `PorPostingAndConfirmation_CreditMainAccCcyCode` |  |  |  |
| 87 | `PORPD.CREDIT.VALUE.DATE` | `PorPostingAndConfirmation_CreditValueDate` |  |  |  |
| 88 | `PORPD.BENEFICIARY.ACCOUNT.NUMBER` | `PorPostingAndConfirmation_BeneficiaryAccountNumber` |  |  |  |
| 89 | `PORPD.BENEFICIARY.NAME` | `PorPostingAndConfirmation_BeneficiaryName` |  |  |  |
| 90 | `PORPD.SENDERS.REFERENCE.NUMBER` | `PorPostingAndConfirmation_SendersReferenceNumber` |  |  |  |
| 91 | `PORPD.ALERT.SENT` | `PorPostingAndConfirmation_AlertSent` |  |  |  |
| 92 | `PORPD.CONF.REVERSAL.INDICATOR` | `PorPostingAndConfirmation_ConfReversalIndicator` |  |  |  |
| 93 | `PORPD.ERROR.REASON.CODE.DESC` | `PorPostingAndConfirmation_ErrorReasonCodeDesc` |  |  |  |
| 94 | `PORPD.CONFIRMATION.SENT` | `PorPostingAndConfirmation_ConfirmationSent` |  |  |  |
| 95 | `PORPD.DELIVERY.INFORMATION.LINE` | `PorPostingAndConfirmation_DeliveryInformationLine` |  |  |  |
| 96 | `PORPD.MT.TYPE` | `PorPostingAndConfirmation_MtType` |  |  |  |
| 97 | `PORPD.BIC.CODE` | `PorPostingAndConfirmation_BicCode` |  |  |  |
| 98 | `PORPD.RESERVED.11` | `PorPostingAndConfirmation_Reserved11` |  |  |  |
| 99 | `PORPD.RESERVED.12` | `PorPostingAndConfirmation_Reserved12` |  |  |  |
| 100 | `PORPD.RESERVED.13` | `PorPostingAndConfirmation_Reserved13` |  |  |  |
| 101 | `PORPD.RESERVED.14` | `PorPostingAndConfirmation_Reserved14` |  |  |  |
| 102 | `PORPD.RESERVED.15` | `PorPostingAndConfirmation_Reserved15` |  |  |  |
