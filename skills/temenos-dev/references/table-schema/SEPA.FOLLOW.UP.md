# SEPA.FOLLOW.UP — Table Schema

> Source: `INSERTS/I_F.SEPA.FOLLOW.UP` in `EP_OutwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.FUP.FIELD.DESCR1` | `SepaFollowUp_FieldDescr1` | TField |  |  |
| 2 | `SEP.FUP.FIELD.CONTENT1` | `SepaFollowUp_FieldContent1` | TField |  | This field contains the Value given to the 1st field to redefine Validation Rules Value upto 35 |
| 3 | `SEP.FUP.FIELD.VET1` | `SepaFollowUp_FieldVet1` |  |  |  |
| 4 | `SEP.FUP.FIELD.DESCR2` | `SepaFollowUp_FieldDescr2` | TField |  |  |
| 5 | `SEP.FUP.FIELD.CONTENT2` | `SepaFollowUp_FieldContent2` | TField |  | This field contains the Net debit amount Validation Rules Value upto 18 type AMT(AMOUNT) NOINPUT field |
| 6 | `SEP.FUP.FIELD.VET2` | `SepaFollowUp_FieldVet2` |  |  |  |
| 7 | `SEP.FUP.FIELD.DESCR3` | `SepaFollowUp_FieldDescr3` | TField |  |  |
| 8 | `SEP.FUP.FIELD.CONTENT3` | `SepaFollowUp_FieldContent3` | TField |  |  |
| 9 | `SEP.FUP.FIELD.VET3` | `SepaFollowUp_FieldVet3` |  |  |  |
| 10 | `SEP.FUP.FIELD.DESCR4` | `SepaFollowUp_FieldDescr4` | TField |  |  |
| 11 | `SEP.FUP.FIELD.CONTENT4` | `SepaFollowUp_FieldContent4` | TField |  |  |
| 12 | `SEP.FUP.FIELD.VET4` | `SepaFollowUp_FieldVet4` |  |  |  |
| 13 | `SEP.FUP.FIELD.DESCR5` | `SepaFollowUp_FieldDescr5` | TField |  |  |
| 14 | `SEP.FUP.FIELD.CONTENT5` | `SepaFollowUp_FieldContent5` | TField |  |  |
| 15 | `SEP.FUP.FIELD.VET5` | `SepaFollowUp_FieldVet5` |  |  |  |
| 16 | `SEP.FUP.FIELD.DESCR6` | `SepaFollowUp_FieldDescr6` | TField |  |  |
| 17 | `SEP.FUP.FIELD.CONTENT6` | `SepaFollowUp_FieldContent6` | A (Alphanumeric) |  | This field provides a Description of the 1st field to redefine (after SEPA.FIELDS DESCRIPTION field or, by default, SEPA.LAYOUT FIELD.NAME field if a vetting list is also foreseen). Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT FIELD |
| 18 | `SEP.FUP.FIELD.VET6` | `SepaFollowUp_FieldVet6` |  |  |  |
| 19 | `SEP.FUP.FIELD.DESCR7` | `SepaFollowUp_FieldDescr7` | TField |  |  |
| 20 | `SEP.FUP.FIELD.CONTENT7` | `SepaFollowUp_FieldContent7` | TField |  |  |
| 21 | `SEP.FUP.FIELD.VET7` | `SepaFollowUp_FieldVet7` |  |  |  |
| 22 | `SEP.FUP.FIELD.DESCR8` | `SepaFollowUp_FieldDescr8` | TField |  |  |
| 23 | `SEP.FUP.FIELD.CONTENT8` | `SepaFollowUp_FieldContent8` | TField |  |  |
| 24 | `SEP.FUP.FIELD.VET8` | `SepaFollowUp_FieldVet8` |  |  |  |
| 25 | `SEP.FUP.FIELD.DESCR9` | `SepaFollowUp_FieldDescr9` | TField |  |  |
| 26 | `SEP.FUP.FIELD.CONTENT9` | `SepaFollowUp_FieldContent9` | TField |  |  |
| 27 | `SEP.FUP.FIELD.VET9` | `SepaFollowUp_FieldVet9` |  |  |  |
| 28 | `SEP.FUP.FIELD.DESCR10` | `SepaFollowUp_FieldDescr10` | A (Alphanumeric) |  | This field specifies the Way of previous application referred to. �INWARD� : reply to a received operation �OUTWARD� : reply to a sent operation Validation Rules Value upto 7 type A(Alphanumeric) User can input only &apos;INWARD&apos; or &apos;OUTWARD&apos; |
| 29 | `SEP.FUP.FIELD.CONTENT10` | `SepaFollowUp_FieldContent10` | TField |  | This field contains the Net credit amount Validation Rules Value upto 18 type AMT(AMOUNT) NOINPUT field |
| 30 | `SEP.FUP.FIELD.VET10` | `SepaFollowUp_FieldVet10` |  |  |  |
| 31 | `SEP.FUP.FIELD.DESCR11` | `SepaFollowUp_FieldDescr11` | TField |  |  |
| 32 | `SEP.FUP.FIELD.CONTENT11` | `SepaFollowUp_FieldContent11` | TField |  |  |
| 33 | `SEP.FUP.FIELD.VET11` | `SepaFollowUp_FieldVet11` |  |  |  |
| 34 | `SEP.FUP.FIELD.DESCR12` | `SepaFollowUp_FieldDescr12` | TField |  |  |
| 35 | `SEP.FUP.FIELD.CONTENT12` | `SepaFollowUp_FieldContent12` | TField |  |  |
| 36 | `SEP.FUP.FIELD.VET12` | `SepaFollowUp_FieldVet12` |  |  |  |
| 37 | `SEP.FUP.FIELD.DESCR13` | `SepaFollowUp_FieldDescr13` | TField |  |  |
| 38 | `SEP.FUP.FIELD.CONTENT13` | `SepaFollowUp_FieldContent13` | TField |  |  |
| 39 | `SEP.FUP.FIELD.VET13` | `SepaFollowUp_FieldVet13` |  |  |  |
| 40 | `SEP.FUP.FIELD.DESCR14` | `SepaFollowUp_FieldDescr14` | TField |  |  |
| 41 | `SEP.FUP.FIELD.CONTENT14` | `SepaFollowUp_FieldContent14` | TField |  |  |
| 42 | `SEP.FUP.FIELD.VET14` | `SepaFollowUp_FieldVet14` |  |  |  |
| 43 | `SEP.FUP.FIELD.DESCR15` | `SepaFollowUp_FieldDescr15` | TField |  | This field specifies the SEPA channel of the Original Transaction for which this Follow Up is generated. B2B - Bank to Bank C2B - Customer to Bank Validation Rules Value upto 3 and Possible Values &apos;B2B or &apos;C2B&apos; |
| 44 | `SEP.FUP.FIELD.CONTENT15` | `SepaFollowUp_FieldContent15` | TField |  |  |
| 45 | `SEP.FUP.FIELD.VET15` | `SepaFollowUp_FieldVet15` |  |  |  |
| 46 | `SEP.FUP.FIELD.DESCR16` | `SepaFollowUp_FieldDescr16` | TField |  |  |
| 47 | `SEP.FUP.FIELD.CONTENT16` | `SepaFollowUp_FieldContent16` | TField |  |  |
| 48 | `SEP.FUP.FIELD.VET16` | `SepaFollowUp_FieldVet16` |  |  |  |
| 49 | `SEP.FUP.FIELD.DESCR17` | `SepaFollowUp_FieldDescr17` | TField |  |  |
| 50 | `SEP.FUP.FIELD.CONTENT17` | `SepaFollowUp_FieldContent17` | TField |  |  |
| 51 | `SEP.FUP.FIELD.VET17` | `SepaFollowUp_FieldVet17` |  |  |  |
| 52 | `SEP.FUP.FIELD.DESCR18` | `SepaFollowUp_FieldDescr18` | TField |  |  |
| 53 | `SEP.FUP.FIELD.CONTENT18` | `SepaFollowUp_FieldContent18` | TField |  |  |
| 54 | `SEP.FUP.FIELD.VET18` | `SepaFollowUp_FieldVet18` |  |  |  |
| 55 | `SEP.FUP.FIELD.DESCR19` | `SepaFollowUp_FieldDescr19` | TField |  |  |
| 56 | `SEP.FUP.FIELD.CONTENT19` | `SepaFollowUp_FieldContent19` | TField |  |  |
| 57 | `SEP.FUP.FIELD.VET19` | `SepaFollowUp_FieldVet19` |  |  |  |
| 58 | `SEP.FUP.FIELD.DESCR20` | `SepaFollowUp_FieldDescr20` | TField |  |  |
| 59 | `SEP.FUP.FIELD.CONTENT20` | `SepaFollowUp_FieldContent20` | TField |  |  |
| 60 | `SEP.FUP.FIELD.VET20` | `SepaFollowUp_FieldVet20` |  |  |  |
| 61 | `SEP.FUP.FIELD.DESCR21` | `SepaFollowUp_FieldDescr21` | TField |  |  |
| 62 | `SEP.FUP.FIELD.CONTENT21` | `SepaFollowUp_FieldContent21` | TField |  |  |
| 63 | `SEP.FUP.FIELD.VET21` | `SepaFollowUp_FieldVet21` |  |  |  |
| 64 | `SEP.FUP.FIELD.DESCR22` | `SepaFollowUp_FieldDescr22` | TField |  |  |
| 65 | `SEP.FUP.FIELD.CONTENT22` | `SepaFollowUp_FieldContent22` | TField |  |  |
| 66 | `SEP.FUP.FIELD.VET22` | `SepaFollowUp_FieldVet22` |  |  |  |
| 67 | `SEP.FUP.FIELD.DESCR23` | `SepaFollowUp_FieldDescr23` | TField |  |  |
| 68 | `SEP.FUP.FIELD.CONTENT23` | `SepaFollowUp_FieldContent23` | TField |  |  |
| 69 | `SEP.FUP.FIELD.VET23` | `SepaFollowUp_FieldVet23` |  |  |  |
| 70 | `SEP.FUP.FIELD.DESCR24` | `SepaFollowUp_FieldDescr24` | A (Alphanumeric) |  | This field denotes the Enrichment or vetting list for the 1st field to redefine. (Given by the SEPA.FIELDS fields ALLOWED.VALUE + ALLOWED.NARR). Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT FIELD and Individual Multi Value field |
| 71 | `SEP.FUP.FIELD.CONTENT24` | `SepaFollowUp_FieldContent24` | TField |  |  |
| 72 | `SEP.FUP.FIELD.VET24` | `SepaFollowUp_FieldVet24` |  |  |  |
| 73 | `SEP.FUP.FIELD.DESCR25` | `SepaFollowUp_FieldDescr25` | TField |  |  |
| 74 | `SEP.FUP.FIELD.CONTENT25` | `SepaFollowUp_FieldContent25` | TField |  |  |
| 75 | `SEP.FUP.FIELD.VET25` | `SepaFollowUp_FieldVet25` |  |  |  |
| 76 | `SEP.FUP.APPLYING.ON` | `SepaFollowUp_ApplyingOn` | TField |  |  |
| 77 | `SEP.FUP.INITIAL.CLEAR.ID` | `SepaFollowUp_InitialClearId` | TField |  | This field holds the Key to the previous operation referred to. (from SEPA.INWARD or SEPA.OUTWARD) Validation Rules value upto 20 type ANY(Any Character) |
| 78 | `SEP.FUP.OUT.CLEAR.ID` | `SepaFollowUp_OutClearId` | TField |  | This field holds the Key to the generated SEPA.OUTWARD record � no input field. Validation Rules value upto 20 type ANY(Any Character) NOINPUT FIELD |
| 79 | `SEP.FUP.LOT.PROCESS.ID` | `SepaFollowUp_LotProcessId` | TField |  | This field holds the Key of the LOT.PROCESS record if this record has been generated from one. Validation Rules value upto 24 type ANY(Any Character) NOINPUT FIELD |
| 80 | `SEP.FUP.LINKED.FT.ID` | `SepaFollowUp_LinkedFtId` | TField |  | This field holds the Key to the acceptance FT simultaneously generated by a MAN inward process type. Validation Rules value upto 25 type ANY(Any Character) NOINPUT FIELD |
| 81 | `SEP.FUP.OPERATION.CODE` | `SepaFollowUp_OperationCode` | TField |  | This field specifies the SEPA operation code (3 digits) Validation Rules Value must be 3 with 2 preceeding Zero&apos;s |
| 82 | `SEP.FUP.REASON.CODE` | `SepaFollowUp_ReasonCode` | A (Alphanumeric) |  | This field denotes the Return, Refund or Reverse reason code. Validation Rules Value upto 4 type A(Alphanumeric) |
| 83 | `SEP.FUP.PEACH.ID` | `SepaFollowUp_PeachId` | TField |  | This field contains the Destination PE-ACH plateform center Validation Rules Value upto 10 type ANY(Any Character) Value should exist in SEPA.PEACH Application |
| 84 | `SEP.FUP.CUSTOMER.ID` | `SepaFollowUp_CustomerId` | TField |  | This field contains the ID of the Handing over customer Validation Rules Value upto 10 type ANY(Any Character) Value should exist in CUSTOMER Application |
| 85 | `SEP.FUP.TRANSACTION.TYPE` | `SepaFollowUp_TransactionType` | A (Alphanumeric) |  | This field holds the Key to FT.TXN.TYPE.CONDITION giving the payment conditions for the customer. Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in FT.TXN.TYPE.CONDITION Application |
| 86 | `SEP.FUP.DEBIT.ACCT.NO` | `SepaFollowUp_DebitAcctNo` | TField |  | This field contains the Debited account number Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 87 | `SEP.FUP.DEBIT.CURRENCY` | `SepaFollowUp_DebitCurrency` | TField |  | This field contains the Debit currency Validation Rules Value upto 3 type CCY(CURRENCY) Value should exist in CURRENCY Application |
| 88 | `SEP.FUP.DEBIT.AMOUNT` | `SepaFollowUp_DebitAmount` | TField |  | This field contains the Gross debit amount number Validation Rules Value upto 18 type AMT(AMOUNT) NOINPUT field |
| 89 | `SEP.FUP.DEBIT.VALUE.DATE` | `SepaFollowUp_DebitValueDate` | D (DATE) |  | This field specifies the Debit value date Validation Rules Value upto 11 type D(DATE) |
| 90 | `SEP.FUP.DEBIT.THEIR.REF` | `SepaFollowUp_DebitTheirRef` | TField |  | This field specifies the Debit reference Validation Rules Value upto 16 type S(SWIFT Character) |
| 91 | `SEP.FUP.AMOUNT.DEBITED` | `SepaFollowUp_AmountDebited` | TField |  |  |
| 92 | `SEP.FUP.CREDIT.ACCT.NO` | `SepaFollowUp_CreditAcctNo` | TField |  | This field contains the Credited account Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 93 | `SEP.FUP.CREDIT.CURRENCY` | `SepaFollowUp_CreditCurrency` | TField |  | This field specifies the Credit currency Validation Rules Value upto 3 type CCY(CURRENCY) Value should exist in CURRENCY Application |
| 94 | `SEP.FUP.CREDIT.AMOUNT` | `SepaFollowUp_CreditAmount` | TField |  | This field contains the Gross credit amount Validation Rules Value upto 18 type AMT(AMOUNT) NOINPUT field |
| 95 | `SEP.FUP.CREDIT.VALUE.DATE` | `SepaFollowUp_CreditValueDate` | D (DATE) |  | This field specifies the Credit value date Validation Rules Value upto 11 type D(DATE) |
| 96 | `SEP.FUP.CREDIT.THEIR.REF` | `SepaFollowUp_CreditTheirRef` | TField |  | This field denotes the Credit reference Validation Rules Value upto 27 type S(SWIFT Character) |
| 97 | `SEP.FUP.AMOUNT.CREDITED` | `SepaFollowUp_AmountCredited` | TField |  |  |
| 98 | `SEP.FUP.EXCHANGE.RATE` | `SepaFollowUp_ExchangeRate` | R (NUMERIC) |  | This field holds the Exchange rate between the customer account and the counterparty in EUR. Validation Rules Value upto 16 type R(NUMERIC) |
| 99 | `SEP.FUP.PROCESSING.DATE` | `SepaFollowUp_ProcessingDate` | D (DATE) |  | This field specifies the Date on which the SEPA.Follow.up is created Validation Rules Value upto 11 type D(DATE) |
| 100 | `SEP.FUP.CHARGE.ACCT.NO` | `SepaFollowUp_ChargeAcctNo` | TField | No | This field contains the Optional account to book separately the charges and commissions if foreseen in the T24 customer convention or to take fees for a non financial operation initiated by the customer. Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 101 | `SEP.FUP.AMOUNT.CHARGED` | `SepaFollowUp_AmountCharged` | TField |  | This field contains the amount to be charged which is equal to Total amount of charges + commissions. Validation Rules Value upto 18 type AMT(AMOUNT) NOINPUT field |
| 102 | `SEP.FUP.COMMISSION.CODE` | `SepaFollowUp_CommissionCode` | TField |  | This field specifies the Calculation method for commissions: CREDIT LESS CHARGES, DEBIT PLUS CHARGES or WAIVE Validation Rules Value upto 20 User can input only &apos;CREDIT LESS CHARGES&apos; or &apos;DEBIT PLUS CHARGES WAIVE&apos; |
| 103 | `SEP.FUP.COMMISSION.TYPE` | `SepaFollowUp_CommissionType` |  |  |  |
| 104 | `SEP.FUP.COMMISSION.AMT` | `SepaFollowUp_CommissionAmt` |  |  |  |
| 105 | `SEP.FUP.CHARGE.CODE` | `SepaFollowUp_ChargeCode` | TField |  |  |
| 106 | `SEP.FUP.CHARGE.TYPE` | `SepaFollowUp_ChargeType` |  |  |  |
| 107 | `SEP.FUP.CHARGE.AMT` | `SepaFollowUp_ChargeAmt` |  |  |  |
| 108 | `SEP.FUP.TAX.TYPE` | `SepaFollowUp_TaxType` |  |  |  |
| 109 | `SEP.FUP.TAX.AMT` | `SepaFollowUp_TaxAmt` |  |  |  |
| 110 | `SEP.FUP.THEIR.NAME` | `SepaFollowUp_TheirName` | A (Alphanumeric) |  | This field contains the Name of the receiver Validation Rules Value upto 24 type A(Alphanumeric) |
| 111 | `SEP.FUP.THEIR.ADDRESS` | `SepaFollowUp_TheirAddress` |  |  |  |
| 112 | `SEP.FUP.THEIR.BANK` | `SepaFollowUp_TheirBank` | A (Alphanumeric) |  | This field contains the BIC code of the receiver�s bank Validation Rules Value upto 11 type A(Alphanumeric) |
| 113 | `SEP.FUP.THEIR.BRANCH` | `SepaFollowUp_TheirBranch` | A (Alphanumeric) |  | This field contains the Branch code of the receiver�s bank Validation Rules Value upto 35 type A(Alphanumeric) |
| 114 | `SEP.FUP.THEIR.IBAN` | `SepaFollowUp_TheirIban` | A (Alphanumeric) |  | This field contains the IBAN account of the receiver Validation Rules Value upto 34 type A(Alphanumeric) |
| 115 | `SEP.FUP.THEIR.REFERENCE` | `SepaFollowUp_TheirReference` | A (Alphanumeric) |  | This field specifies the Reference of the sender Validation Rules Value upto 35 type A(Alphanumeric) |
| 116 | `SEP.FUP.OPERATION.REF` | `SepaFollowUp_OperationRef` | A (Alphanumeric) |  | This field specifies the Reference of the sender�s bank. Validation Rules Value upto 24 type A(Alphanumeric) |
| 117 | `SEP.FUP.PAYMENT.DETAILS` | `SepaFollowUp_PaymentDetails` |  |  |  |
| 118 | `SEP.FUP.IN.REASON.OVE` | `SepaFollowUp_InReasonOve` |  |  |  |
| 119 | `SEP.FUP.INITIAL.BRANCH` | `SepaFollowUp_InitialBranch` | A (Alphanumeric) |  | This field contains the Branch of the bank�s customer Validation Rules Value upto 35 type A(Alphanumeric) |
| 120 | `SEP.FUP.INITIAL.ACCOUNT` | `SepaFollowUp_InitialAccount` | TField |  | This field contains the T24 ACCOUNT of the bank�s customer Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 121 | `SEP.FUP.INITIAL.IBAN` | `SepaFollowUp_InitialIban` | A (Alphanumeric) |  | This field contains the IBAN account of the bank�s customer. Validation Rules Value upto 34 type A(Alphanumeric) NOINPUT field |
| 122 | `SEP.FUP.INITIAL.CUSTOMER` | `SepaFollowUp_InitialCustomer` | TField |  | This field contains the Identification of the bank�s customer. Validation Rules Value upto 10 type CUS(Customer number) NOINPUT field and Value should exist in CUSTOMER Application |
| 123 | `SEP.FUP.INITIAL.NAME` | `SepaFollowUp_InitialName` | A (Alphanumeric) |  | This field contains the Name of the bank�s customer. Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT field |
| 124 | `SEP.FUP.INITIAL.ADDRESS` | `SepaFollowUp_InitialAddress` |  |  |  |
| 125 | `SEP.FUP.INITIAL.AMOUNT` | `SepaFollowUp_InitialAmount` | TField |  | This field contains the Initial amount of the transaction Validation Rules Value upto 18 type AMT(AMOUNT) NOINPUT field |
| 126 | `SEP.FUP.INITIAL.CURRENCY` | `SepaFollowUp_InitialCurrency` | TField |  | This field contains the Initial currency of the transaction Validation Rules Value upto 3 type CCY(CURRENCY) NOINPUT field and Value should exist in CURRENCY Application |
| 127 | `SEP.FUP.PROFIT.CENTRE.CUST` | `SepaFollowUp_ProfitCentreCust` | TField |  | This field contains the Customer Id to be used to identify the booking profit center. Validation Rules Value upto 10 type CUS(Customer number) Value should exist in CUSTOMER Application |
| 128 | `SEP.FUP.PROFIT.CENTRE.DEPT` | `SepaFollowUp_ProfitCentreDept` | TField |  | This field holds the Key to DEPT.ACCT.OFFICER (profit center). These 2 fields are mutually exclusive. Validation Rules Value upto 4 type DAO(Deparment Accounting Officer) Value should exist in DEPT.ACCT.OFFICER Application |
| 129 | `SEP.FUP.MANDATE.ID` | `SepaFollowUp_MandateId` | A (Alphanumeric) |  | This field denotes the Mandate identification for direct debit. Validation Rules Value upto 35 type A(Alphanumeric) |
| 130 | `SEP.FUP.CREDITOR.ID` | `SepaFollowUp_CreditorId` | A (Alphanumeric) |  | This field denotes the Identification of the Direct Debit creditor. Validation Rules Value upto 35 type A(Alphanumeric) |
| 131 | `SEP.FUP.CUST.DETAIL.ID` | `SepaFollowUp_CustDetailId` | A (Alphanumeric) |  | This field holds the Key to the SEPA.INWARD.DETAIL:�,�:rank of related transaction in the CB message. Validation Rules Value upto 24 type A(Alphanumeric) |
| 132 | `SEP.FUP.ADVICE.REQD.Y.N` | `SepaFollowUp_AdviceReqdYN` | TField |  | This field contains a value of �Y�:which denotes Issuing of a customer advice. Validation Rules Value upto 2 and User can input only &apos;Y&apos; or &apos;NO&apos; |
| 133 | `SEP.FUP.SETTLEMENT.DATE` | `SepaFollowUp_SettlementDate` | D (DATE) |  | This field denotes the Date required for the payment. Validation Rules Value upto 11 type D(DATE) |
| 134 | `SEP.FUP.PRESENTATION.DATE` | `SepaFollowUp_PresentationDate` | D (DATE) |  | This field specifies the Generation date of the SEPA outward file. Validation Rules Value upto 11 type D(DATE) |
| 135 | `SEP.FUP.INPUT.REASON.CODE` | `SepaFollowUp_InputReasonCode` | A (Alphanumeric) |  | This field defines the Reason code updated for reversal of transaction made. Must be a valid reason code in SEPA.REASONS template Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in SEPA.REASONS Application |
| 136 | `SEP.FUP.SDD.TYPE` | `SepaFollowUp_SddType` | TField |  | This field denotes the Type of Direct debit CORE / B2B Validation Rules Value upto 5 and User can input only &apos;CORE&apos; or &apos;B2B&apos; |
| 137 | `SEP.FUP.SDD.STATUS` | `SepaFollowUp_SddStatus` | TField |  | This field specifies the Sequence value for Direct debit Possible value are FRST / RCUR / FNAL / OOFF Validation Rules Value upto 5 and User can input only &apos;FRST&apos; or &apos;RCUR&apos; or &apos;FNAL&apos; or &apos;OOFF&apos; |
| 138 | `SEP.FUP.SDD.SEQUENCE` | `SepaFollowUp_SddSequence` | TField |  | This field specifies the Status of Direct debit Value populated by SEPA routines Possible values are AUTH / NOTAUTH Validation Rules Value upto 10 And User can input only &apos;AUTH&apos; or &apos;NOTAUTH&apos; |
| 139 | `SEP.FUP.SDD.DATE.OF.SIGN` | `SepaFollowUp_SddDateOfSign` | D (DATE) |  | This field specifies the Date on which the direct debit is signed Validation Rules Value upto 11 and type D(DATE) |
| 140 | `SEP.FUP.STP.STATUS` | `SepaFollowUp_StpStatus` | TField |  | This field specifies the Updates status of the direct debit when failed due to certain check validated at the SEPA.LAYOUT level Possible value are AC-SDD-TYPE/BLK-AMOUNT/BLK-BIC/BLK-IBAN/BLK-LIMIT/BLK-NBOFTXN/BLK-SERVICE/INTXN/MANDATE/RCVNTFND/REFUSAL/TIME-FRAME Validation Rules Value upto 15 and User can input only &apos;AC-SDD-TYPE&apos; or &apos;BLK-AMOUNT&apos; or &apos;BLK-BIC&apos; or &apos;BLK-IBAN&apos; or &apos;BLK-LIMIT&apos; or &apos;BLK-NBOFTXN&apos; or &apos;BLK-SERVICE&apos; or &apos;INTXN&apos; or &apos;MANDATE&apos; or &apos;RCVNTFND&apos; or &apos;REFUSAL&apos; or &apos;TIME-FRAME&apos; |
| 141 | `SEP.FUP.CHANNEL` | `SepaFollowUp_Channel` | TField |  |  |
| 142 | `SEP.FUP.CATEG.PURPOSE` | `SepaFollowUp_CategPurpose` | A (Alphanumeric) |  | Specifies the category purpose as published in an external category purpose code list from SEPA.CATEG.PURPOSE or specifies the Category purpose in a proprietary form. Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT field |
| 143 | `SEP.FUP.PURPOSE` | `SepaFollowUp_Purpose` | A (Alphanumeric) |  | Specifies the purpose as published in an external purpose code list from SEPA.PURPOSE.CODE or specifies the purpose in a proprietary form. Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT field |
| 144 | `SEP.FUP.PAYMENT.REF` | `SepaFollowUp_PaymentRef` |  |  |  |
| 145 | `SEP.FUP.END.TO.END.ID` | `SepaFollowUp_EndToEndId` | A (Alphanumeric) |  | This field holds the EndToEndId value from the original transaction if present. Validation Rules Value upto 35 type A(Alphanumeric) |
| 146 | `SEP.FUP.PMTINF.ID` | `SepaFollowUp_PmtinfId` | TField |  | This field holds the value of PmtInfID from the original PAIN transaction which will be provided in the XML file Validation Rules Value upto 35 type R NOINPUT field |
| 147 | `SEP.FUP.ADDITIONAL.INFO` | `SepaFollowUp_AdditionalInfo` |  |  |  |
| 148 | `SEP.FUP.EONIA.RATE` | `SepaFollowUp_EoniaRate` | TField |  | Contains the EONIA rate to calculate the compensation amount. Validation Rules Value upto 16 type R |
| 149 | `SEP.FUP.COMPENSATION.AMT` | `SepaFollowUp_CompensationAmt` | TField |  | The amount should be calculated automatically from transaction amount based on the EONIA rate inputted. Validation Rules Value upto 18 type numeric |
| 150 | `SEP.FUP.CUST.INIT.RECALL` | `SepaFollowUp_CustInitRecall` | TField |  | This field tell whether the follow up initiated by customer or not. This field only allowed for CAMT056 message Validation Rules Set to YES if follow up is initiated by customer |
| 151 | `SEP.FUP.TXN.NETTING.ID` | `SepaFollowUp_TxnNettingId` | TField |  | This field holds the value of EP.SEPA.TXN.NETTING record ID corresponding to the original transaction bulk for wich the FollowUp is being generated, when customer Netting setup is done in SEPA.PARAMETER. Validation Rules Value upto 70 type ANY(Any Character) |
| 152 | `SEP.FUP.MOD.SETTLEMENT.DATE` | `SepaFollowUp_ModSettlementDate` | D (DATE) |  | This field tell whether the MODIFIED interbank settlement date is received. This field only allowed for CAMT087 message Validation Rules Value upto 11 type D(DATE) |
| 153 | `SEP.FUP.INQUIRY.CHARGE.AMT` | `SepaFollowUp_InquiryChargeAmt` | TField |  | This field tell whether the inquiry charge amount is received. This field only allowed for CAMT087 message Validation Rules Value upto 18 type AMT(AMOUNT) |
| 154 | `SEP.FUP.ACCEPTANCE.DATE` | `SepaFollowUp_AcceptanceDate` | D (DATE) |  | This field tell whether the acceptance date is received. This field only allowed for CAMT027 message Validation Rules Value upto 11 type D(DATE) NOINPUT field |
| 155 | `SEP.FUP.COMPENSATION.IBAN` | `SepaFollowUp_CompensationIban` | TField |  |  |
| 156 | `SEP.FUP.INQUIRY.CHARGE.IBAN` | `SepaFollowUp_InquiryChargeIban` | TField |  |  |
| 157 | `SEP.FUP.RESERVED4` | `SepaFollowUp_Reserved4` |  |  |  |
| 158 | `SEP.FUP.RESERVED3` | `SepaFollowUp_Reserved3` | TField |  |  |
| 159 | `SEP.FUP.RESERVED2` | `SepaFollowUp_Reserved2` | TField |  |  |
| 160 | `SEP.FUP.RESERVED1` | `SepaFollowUp_Reserved1` | TField |  |  |
| 161 | `SEP.FUP.LOCAL.REF` | `SepaFollowUp_LocalRef` |  |  |  |
| 162 | `SEP.FUP.DELIVERY.REF` | `SepaFollowUp_DeliveryRef` |  |  |  |
| 163 | `SEP.FUP.STATEMENT.NOS` | `SepaFollowUp_StatementNos` |  |  |  |
| 164 | `SEP.FUP.OVERRIDE` | `SepaFollowUp_Override` |  |  |  |
| 165 | `SEP.FUP.RECORD.STATUS` | `SepaFollowUp_RecordStatus` | String |  |  |
| 166 | `SEP.FUP.CURR.NO` | `SepaFollowUp_CurrNo` | String |  |  |
| 167 | `SEP.FUP.INPUTTER` | `SepaFollowUp_Inputter` |  |  |  |
| 168 | `SEP.FUP.DATE.TIME` | `SepaFollowUp_DateTime` |  |  |  |
| 169 | `SEP.FUP.AUTHORISER` | `SepaFollowUp_Authoriser` | String |  |  |
| 170 | `SEP.FUP.CO.CODE` | `SepaFollowUp_CoCode` | String |  |  |
| 171 | `SEP.FUP.DEPT.CODE` | `SepaFollowUp_DeptCode` | String |  |  |
| 172 | `SEP.FUP.AUDITOR.CODE` | `SepaFollowUp_AuditorCode` | String |  |  |
| 173 | `SEP.FUP.AUDIT.DATE.TIME` | `SepaFollowUp_AuditDateTime` | String |  |  |
