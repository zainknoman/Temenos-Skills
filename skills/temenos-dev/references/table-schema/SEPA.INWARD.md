# SEPA.INWARD — Table Schema

> Source: `INSERTS/I_F.SEPA.INWARD` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.IC.INWARD.RECORD` | `SepaInward_InwardRecord` | TField |  | This field defines the Transaction Information stored in such a way that it can be shown easily as it was in its original XML presentation by a delivered T24 drill down enquiry. Validation Rules Value upto 35 type ANY(Any Character) |
| 2 | `SEP.IC.HIST.OPE.ID` | `SepaInward_HistOpeId` |  |  |  |
| 3 | `SEP.IC.HIST.TXN.ID` | `SepaInward_HistTxnId` |  |  |  |
| 4 | `SEP.IC.HIST.MSG.ID` | `SepaInward_HistMsgId` |  |  |  |
| 5 | `SEP.IC.PEACH.ID` | `SepaInward_PeachId` | TField |  | This field contains the ID of the Issuing PE-ACH. Validation Rules Value upto 10 type ANY(Any Character) Value should exist in SEPA.PEACH Application |
| 6 | `SEP.IC.CUSTOMER.ID` | `SepaInward_CustomerId` | TField |  | This field contains the ID of the Handing over customer Validation Rules Value upto 10 type ANY(Any Character) Value should exist in CUSTOMER Application |
| 7 | `SEP.IC.FOLLOW.UP.ID` | `SepaInward_FollowUpId` | TField |  | This field holds the Key to SEPA.FOLLOW.UP. If Inward message is not processed straight through due to technical or validation failures, a SEPA.FOLLOW.UP and FT will be created either to accept the Inward Transaction by authorizing the FT or to reject it by authorizing SEPA.FOLLOW.UP Validation Rules Value upto 27 type ANY(Any Character) |
| 8 | `SEP.IC.LINKED.FT.ID` | `SepaInward_LinkedFtId` | TField |  | This field holds the Key to any postpone acceptance FT. Validation Rules Value upto 25 type ANY(Any Character) |
| 9 | `SEP.IC.OPERATION.CODE` | `SepaInward_OperationCode` | A (Alphanumeric) |  | This field defines the Operation code as defined in the key. Validation Rules Value upto 3 type A(Alphanumeric) with 2 preceeding Zero&apos;s |
| 10 | `SEP.IC.REASON.CODE` | `SepaInward_ReasonCode` | TField |  | This field denotes the Reason for initial transaction failure. Validation Rules Value upto 10 type CUS(CUSTOMER) Value should exist in CUSTOMER Application |
| 11 | `SEP.IC.TRANSACTION.TYPE` | `SepaInward_TransactionType` | A (Alphanumeric) |  | This field holds the Key to FT.TXN.TYPE.CONDITION giving the payment conditions for the customer. Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in FT.TXN.TYPE.CONDITION Application |
| 12 | `SEP.IC.DEBIT.ACCT.NO` | `SepaInward_DebitAcctNo` | TField |  | This field contains the Debited account Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 13 | `SEP.IC.DEBIT.CURRENCY` | `SepaInward_DebitCurrency` | TField |  | This field contains the Debit currency Validation Rules Value upto 3 type CCY(CURRENCY) Value should exist in CURRENCY Application |
| 14 | `SEP.IC.DEBIT.AMOUNT` | `SepaInward_DebitAmount` | TField |  | This field contains the Gross Debit Amount Validation Rules Value upto 18 type AMT (AMOUNT) |
| 15 | `SEP.IC.DEBIT.VALUE.DATE` | `SepaInward_DebitValueDate` | D (DATE) |  | This field specifies the Debit Value Date Validation Rules Value upto 11 type D(DATE) |
| 16 | `SEP.IC.DEBIT.THEIR.REF` | `SepaInward_DebitTheirRef` | TField |  | This field specifies the Debit reference Validation Rules Value upto 16 type S(SWIFT Characters) |
| 17 | `SEP.IC.AMOUNT.DEBITED` | `SepaInward_AmountDebited` | TField |  | This field should contain the Net debit amount Validation Rules Value upto 18 type AMT (AMOUNT) |
| 18 | `SEP.IC.CREDIT.ACCT.NO` | `SepaInward_CreditAcctNo` | TField |  | This field contains the Credited account Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 19 | `SEP.IC.CREDIT.CURRENCY` | `SepaInward_CreditCurrency` | TField |  | This field contains the Credit currency Validation Rules Value upto 3 type CCY(CURRENCY) Value should exist in CURRENCY Application |
| 20 | `SEP.IC.CREDIT.AMOUNT` | `SepaInward_CreditAmount` | TField |  | This field contains the Gross credit amount Validation Rules Value upto 18 type AMT (AMOUNT) |
| 21 | `SEP.IC.CREDIT.VALUE.DATE` | `SepaInward_CreditValueDate` | D (DATE) |  | This field contains the Credit Value Date Validation Rules Value upto 11 type D(DATE) |
| 22 | `SEP.IC.CREDIT.THEIR.REF` | `SepaInward_CreditTheirRef` | TField |  | This field contains the Credit reference Validation Rules Value upto 27 type S(SWIFT Characters) |
| 23 | `SEP.IC.AMOUNT.CREDITED` | `SepaInward_AmountCredited` | TField |  | This field should contain the Net credit amount Validation Rules Value upto 18 type AMT (AMOUNT) |
| 24 | `SEP.IC.EXCHANGE.RATE` | `SepaInward_ExchangeRate` | R (RATE) |  | This field contains the Exchange rate between the customer account and the counterparty in EUR. Validation Rules Value upto 16 type R(RATE) |
| 25 | `SEP.IC.PROCESSING.DATE` | `SepaInward_ProcessingDate` | D (DATE) |  | This field Specifies on which working day this transaction is to be processed. Today or &gt;today. Validation Rules Value upto 11 type D(DATE) |
| 26 | `SEP.IC.CHARGE.ACCT.NO` | `SepaInward_ChargeAcctNo` | TField | No | This field denotes the Optional account to book separately the charges and commissions if foreseen in the T24 customer convention or to take fees for a non financial operation initiated by the customer. Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 27 | `SEP.IC.AMOUNT.CHARGED` | `SepaInward_AmountCharged` | TField |  | This field specifies the amount that is charged which is generally Total amount of charges + commissions. Validation Rules Value upto 18 type AMT (AMOUNT) |
| 28 | `SEP.IC.COMMISSION.CODE` | `SepaInward_CommissionCode` | TField |  | This field defines the Type of calculation for the commissions: - CREDIT LESS CHARGES - DEBIT PLUS CHARGES or - WAIVE Validation Rules Value upto 20 and User can Input only values &apos;CREDIT LESS CHARGES&apos; or &apos;DEBIT PLUS CHARGES&apos; or &apos;WAIVE&apos; |
| 29 | `SEP.IC.COMMISSION.TYPE` | `SepaInward_CommissionType` |  |  |  |
| 30 | `SEP.IC.COMMISSION.AMT` | `SepaInward_CommissionAmt` |  |  |  |
| 31 | `SEP.IC.CHARGE.CODE` | `SepaInward_ChargeCode` | TField |  | This field define the Type of calculation for the charges: - CREDIT LESS CHARGES - DEBIT PLUS CHARGES or - WAIVE Validation Rules Value upto 20 and User can Input only values &apos;CREDIT LESS CHARGES&apos; or &apos;DEBIT PLUS CHARGES&apos; or &apos;WAIVE&apos; |
| 32 | `SEP.IC.CHARGE.TYPE` | `SepaInward_ChargeType` |  |  |  |
| 33 | `SEP.IC.CHARGE.AMT` | `SepaInward_ChargeAmt` |  |  |  |
| 34 | `SEP.IC.TAX.TYPE` | `SepaInward_TaxType` |  |  |  |
| 35 | `SEP.IC.TAX.AMT` | `SepaInward_TaxAmt` |  |  |  |
| 36 | `SEP.IC.THEIR.NAME` | `SepaInward_TheirName` | A (Alphanumeric) |  | This field contains the Name of the sender Validation Rules Value upto 24 type A(Alphanumeric) |
| 37 | `SEP.IC.THEIR.ADDRESS` | `SepaInward_TheirAddress` |  |  |  |
| 38 | `SEP.IC.THEIR.BANK` | `SepaInward_TheirBank` | A (Alphanumeric) |  | This field contains the BIC code of the sender�s bank Validation Rules Value upto 11 type A(Alphanumeric) |
| 39 | `SEP.IC.THEIR.BRANCH` | `SepaInward_TheirBranch` | A (Alphanumeric) |  | This field contains the Branch code of the sender�s bank Validation Rules Value upto 35 type A(Alphanumeric) |
| 40 | `SEP.IC.THEIR.IBAN` | `SepaInward_TheirIban` | A (Alphanumeric) |  | This field contains the IBAN account of the sender Validation Rules Value upto 34 type A(Alphanumeric) |
| 41 | `SEP.IC.THEIR.REFERENCE` | `SepaInward_TheirReference` | A (Alphanumeric) |  | This field specifies the Reference of the sender Validation Rules Value upto 35 type A(Alphanumeric) |
| 42 | `SEP.IC.OPERATION.REF` | `SepaInward_OperationRef` | A (Alphanumeric) |  | This field specifies the Reference of the sender�s bank Validation Rules Value upto 24 type A(Alphanumeric) |
| 43 | `SEP.IC.PAYMENT.DETAILS` | `SepaInward_PaymentDetails` |  |  |  |
| 44 | `SEP.IC.IN.REASON.OVE` | `SepaInward_InReasonOve` |  |  |  |
| 45 | `SEP.IC.INITIAL.BRANCH` | `SepaInward_InitialBranch` | A (Alphanumeric) |  | This field contains the Branch of the bank�s customer Validation Rules Value upto 35 type A(Alphanumeric) |
| 46 | `SEP.IC.INITIAL.ACCOUNT` | `SepaInward_InitialAccount` | TField |  | This field contains the T24 ACCOUNT of the bank�s customer Validation Rules Value upto 16 type ANT(Account Number) Value should exist in ACCOUNT Application |
| 47 | `SEP.IC.INITIAL.IBAN` | `SepaInward_InitialIban` | A (Alphanumeric) |  | This field contain the IBAN account of the bank�s customer. Validation Rules Value upto 34 type A(Alphanumeric) |
| 48 | `SEP.IC.INITIAL.CUSTOMER` | `SepaInward_InitialCustomer` | TField |  | This field specifies the Identification of the bank�s customer. Validation Rules Value upto 10 type CUS(CUSTOMER) Value should exist in CUSTOMER Application |
| 49 | `SEP.IC.INITIAL.NAME` | `SepaInward_InitialName` | A (Alphanumeric) |  | This field contains the Name of the bank�s customer. Validation Rules Value upto 35 type A(Alphanumeric) |
| 50 | `SEP.IC.INITIAL.ADDRESS` | `SepaInward_InitialAddress` |  |  |  |
| 51 | `SEP.IC.INITIAL.AMOUNT` | `SepaInward_InitialAmount` | TField |  | This field specifies the Initial amount of the transaction Validation Rules Value upto 18 type AMT (AMOUNT) |
| 52 | `SEP.IC.INITIAL.CURRENCY` | `SepaInward_InitialCurrency` | TField |  | This field contains the Initial currency of the transaction Validation Rules Value upto 3 type CCY(CURRENCY) Value should exist in CURRENCY Application |
| 53 | `SEP.IC.PROFIT.CENTRE.CUST` | `SepaInward_ProfitCentreCust` | TField |  | This field denotes the Customer Id to be used to identify the booking profit center. Validation Rules Value upto 10 type ANY(Any Character) Value should exist in CUSTOMER Application |
| 54 | `SEP.IC.PROFIT.CENTRE.DEPT` | `SepaInward_ProfitCentreDept` | TField |  | This field holds the Key to DEPT.ACCT.OFFICER to identify an account officer as profit center. These 2 last fields are mutually exclusive. Validation Rules Value upto 4 type DAO(DEPT Accounting Officer) Value should exist in DEPT.ACCT.OFFICER Application |
| 55 | `SEP.IC.MANDATE.ID` | `SepaInward_MandateId` | A (Alphanumeric) |  | This field specifies the Mandate identification for direct debit. Validation Rules Value upto 35 type A(Alphanumeric) |
| 56 | `SEP.IC.CREDITOR.ID` | `SepaInward_CreditorId` | A (Alphanumeric) |  | This field contains the Creditor Identification. Used for SEPA Direct Debits. Validation Rules Value upto 35 type A(Alphanumeric) |
| 57 | `SEP.IC.CUST.DETAIL.ID` | `SepaInward_CustDetailId` | A (Alphanumeric) |  | This field holds the Key to the SEPA.INWARD.DETAIL:�,�:rank of related transaction in the CB message. Validation Rules Value upto 24 type A(Alphanumeric) |
| 58 | `SEP.IC.STATUS` | `SepaInward_Status` | TField |  | This field specifies the Status of the transaction posted. ACP - Accepted CXL � Cancelled PND � Pending PRC � Processed RCV � Received RDY � Ready for transfer REJ � Rejected RET � Returned SND � Sent TRF - Transferred Validation Rules Value upto 3 and User can input only &apos;ACP&apos; or &apos;CXL&apos; or &apos;PND &apos; or &apos;PRC &apos; or &apos;RCV&apos; or &apos;RDY&apos; or &apos;REJ&apos; or &apos;RET&apos; or &apos;SND&apos; or &apos;TRF&apos; |
| 59 | `SEP.IC.SDD.TYPE` | `SepaInward_SddType` | TField |  | This field specifies the Type of Direct debit as described by EPC - CORE / B2B Validation Rules Value upto 5 and User can input only &apos;B2B&apos; or &apos;CORE&apos; Values can be added or modified using VIRTUAL Table with key SDD.TYPE |
| 60 | `SEP.IC.SDD.STATUS` | `SepaInward_SddStatus` | TField |  | This field specifies the Status of Direct debit Value populated by validation routine attached to SEPA.LAYOUT Possible values are AUTH / NOTAUTH Auth - Direct Debit processed on back of a valid Mandate Not Auth - Direct Debit processed with out valid Mandate Validation Rules Value upto 10 and User can input only &apos;AUTH&apos; or &apos;NOTAUTH&apos; Values can be added or modified using VIRTUAL Table with key SDD.STATUS |
| 61 | `SEP.IC.SDD.SEQUENCE` | `SepaInward_SddSequence` | TField |  | This field specifies the Sequence value for Direct debit Possible value are FRST - First / RCUR - Recurrent / FNAL - Final / OOFF - One Off Validation Rules Value upto 5 and User can input only &apos;FRST&apos; or &apos;RCUR&apos; or &apos;FNAL&apos; or &apos;Final&apos; or &apos;OOFF&apos; Values can be added or modified using VIRTUAL Table with key SDD.SEQUENCE |
| 62 | `SEP.IC.SDD.DATE.OF.SIGN` | `SepaInward_SddDateOfSign` | D (DATE) |  | This field specifies the Date on which the Direct Debit Mandate is signed Validation Rules Value upto 11 type D(DATE) |
| 63 | `SEP.IC.STP.STATUS` | `SepaInward_StpStatus` | TField |  | This field specifies the Updates status of the inward transaction, when failed due to failed validations attached at the SEPA.LAYOUT level. Identifies the reason why the transaction is failed. Possible value are MANDATE / REFUSAL / TIME-FRAME / AC-SDD-TYPE .. etc. Validation Rules Value upto 25 and User can input only &apos;AC-SDD-TYPE&apos; or &apos;BLK-AMOUNT&apos; or &apos;BLK-BIC&apos; or &apos;BLK-IBAN&apos; or &apos;BLK-LIMIT&apos; or &apos;BLK-NBOFTXN&apos; or &apos;BLK-SERVICE&apos; or &apos;INTXN&apos; or &apos;MANDATE&apos; or &apos;RCVNTFND&apos; or &apos;REFUSAL&apos; or &apos;TIME-FRAME&apos; Values can be added or modified using VIRTUAL Table with key STP.STATUS |
| 64 | `SEP.IC.CHANNEL` | `SepaInward_Channel` |  |  |  |
| 65 | `SEP.IC.C2B.FWD.MESSAGE` | `SepaInward_C2bFwdMessage` | A (Alphanumeric) |  | This field contains the SEPA.LAYOUT Id of the forward B2B pacs message for processed Inward C2B Pain message Validation Rules Value upto 30 type A(Alphanumeric) Value should exist in SEPA.LAYOUT Application |
| 66 | `SEP.IC.TRANSACTION.ID` | `SepaInward_TransactionId` | TField |  | This field holds the transaction id extracted from transaction Validation Rules Value upto 35 type ANY |
| 67 | `SEP.IC.INSTRUCTION.ID` | `SepaInward_InstructionId` | TField |  | This field holds the instruction id extracted from transaction Validation Rules Value upto 35 type ANY |
| 68 | `SEP.IC.END.TO.END.ID` | `SepaInward_EndToEndId` | TField |  | This field holds the end to end id extracted from transaction Validation Rules Value upto 35 type ANY |
| 69 | `SEP.IC.INWARD.DATA` | `SepaInward_InwardData` |  |  |  |
| 70 | `SEP.IC.CATEG.PURPOSE` | `SepaInward_CategPurpose` | A (Alphanumeric) |  | Specifies the category purpose as published in an external category purpose code list from SEPA.CATEG.PURPOSE or specifies the Category purpose in a proprietary form. Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT field |
| 71 | `SEP.IC.PURPOSE` | `SepaInward_Purpose` | A (Alphanumeric) |  | Specifies the purpose as published in an external purpose code list from SEPA.PURPOSE.CODE or specifies the purpose in a proprietary form. Validation Rules Value upto 35 type A(Alphanumeric) NOINPUT field |
| 72 | `SEP.IC.PAYMENT.REF` | `SepaInward_PaymentRef` |  |  |  |
| 73 | `SEP.IC.PMTINF.ID` | `SepaInward_PmtinfId` | A (Alphanumeric) |  | This field holds the payment information id extracted from transaction Validation Rules Value upto 35 type A(Alphanumeric) |
| 74 | `SEP.IC.ADDITIONAL.INFO` | `SepaInward_AdditionalInfo` |  |  |  |
| 75 | `SEP.IC.CREATION.DATE` | `SepaInward_CreationDate` | D (DATE) |  | This field holds date extracted from xml file which denoteS creation date of the xml file Validation Rules Value upto 8 type D(DATE) |
| 76 | `SEP.IC.STP.CHECK.PROCESS` | `SepaInward_StpCheckProcess` | A (Alphanumeric) |  | This field holds the value "LIMIT" if a SEPA.LIMIT record is available for this transaction Validation Rules Value upto 65 type A(Alphanumeric) |
| 77 | `SEP.IC.SETTLEMENT.DATE` | `SepaInward_SettlementDate` | D (DATE) |  | This field holds actual settlement date taken from xml file Validation Rules Value upto 8 type D(DATE) |
| 78 | `SEP.IC.INWARD.FILES.ID` | `SepaInward_InwardFilesId` | A (Alphanumeric) |  | This field holds the Key for the corresponding inward files record in SEPA.INWARD.FILES application Validation Rules Value upto 60 type A(Alphanumeric) |
| 79 | `SEP.IC.ACCEPTANCE.DATE` | `SepaInward_AcceptanceDate` | D (DATE) |  | This field holds the value of Processing Date when the payment is initiated. The value is from the AccptncDtTm tag Validation Rules Value upto 11 type D(DATE) |
| 80 | `SEP.IC.OUR.AGT.GEN.FIN.ID` | `SepaInward_OurAgtGenFinId` | A (Alphanumeric) |  | This field holds the value from Id tag(NOTPROVIDED) from Inward XML file if Our BIC is not provided. Validation Rules Value upto 15 type A(Alphanumeric) |
| 81 | `SEP.IC.BEN.AGT.GEN.FIN.ID` | `SepaInward_BenAgtGenFinId` | A (Alphanumeric) |  | This field holds the value from Id tag(NOTPROVIDED) from Inward XML file if the Beneficiary BIC is not provided. Validation Rules Value upto 15 type A(Alphanumeric) |
| 82 | `SEP.IC.TXN.NETTING.ID` | `SepaInward_TxnNettingId` | TField |  | This field holds the value of EP.SEPA.TXN.NETTING record ID corresponding to the bulk processed from Inward xml message when customer Netting setup is done in SEPA.PARAMETER. Validation Rules Value upto 70 type ANY(Any Character) |
| 83 | `SEP.IC.ON.US.TRANS` | `SepaInward_OnUsTrans` | A (Alphanumeric) |  | If this field is set to Y, then corresponding PACS message status will be updated accordingly for InHouse Transactions Validation rule Value upto 1 type A (Alphanumeric) and Value allowed 'Y' or null |
| 84 | `SEP.IC.MOD.SETTLEMENT.DATE` | `SepaInward_ModSettlementDate` | D (DATE) |  | This field tell whether the MODIFIED interbank settlement date is received. This field only allowed for CAMT087 message Validation Rules Value upto 11 type D(DATE) NOINPUT field |
| 85 | `SEP.IC.RESERVED.7` | `SepaInward_Reserved7` |  |  |  |
| 86 | `SEP.IC.RESERVED.6` | `SepaInward_Reserved6` |  |  |  |
| 87 | `SEP.IC.RESERVED.5` | `SepaInward_Reserved5` | TField |  |  |
| 88 | `SEP.IC.RESERVED.4` | `SepaInward_Reserved4` | TField |  |  |
| 89 | `SEP.IC.RESERVED.3` | `SepaInward_Reserved3` | TField |  |  |
| 90 | `SEP.IC.RESERVED.2` | `SepaInward_Reserved2` | TField |  |  |
| 91 | `SEP.IC.RESERVED.1` | `SepaInward_Reserved1` | TField |  |  |
| 92 | `SEP.IC.LOCAL.REF` | `SepaInward_LocalRef` |  |  |  |
| 93 | `SEP.IC.DELIVERY.REF` | `SepaInward_DeliveryRef` |  |  |  |
| 94 | `SEP.IC.STATEMENT.NOS` | `SepaInward_StatementNos` |  |  |  |
| 95 | `SEP.IC.OVERRIDE` | `SepaInward_Override` |  |  |  |
| 96 | `SEP.IC.RECORD.STATUS` | `SepaInward_RecordStatus` | A (Alphanumeric) |  | This field contains the Status of the record � always empty. Validation Rules Value upto 4 type A(Alphanumeric) |
| 97 | `SEP.IC.CURR.NO` | `SepaInward_CurrNo` | String |  | This field specifies the Current version of the record � always 1. Validation Rules Value upto 3 |
| 98 | `SEP.IC.INPUTTER` | `SepaInward_Inputter` |  |  |  |
| 99 | `SEP.IC.DATE.TIME` | `SepaInward_DateTime` |  |  |  |
| 100 | `SEP.IC.AUTHORISER` | `SepaInward_Authoriser` | A (Alphanumeric) |  | This field contains the Identification of the authoriser. Validation Rules Value upto 35 type A(Alphanumeric) |
| 101 | `SEP.IC.CO.CODE` | `SepaInward_CoCode` | A (Alphanumeric) |  | This field contains the Company code. Validation Rules Value upto 11 type A(Alphanumeric) |
| 102 | `SEP.IC.DEPT.CODE` | `SepaInward_DeptCode` | A (Alphanumeric) |  | This field specified the Department code of the operator. Validation Rules Value upto 4 type A(Alphanumeric) |
| 103 | `SEP.IC.AUDITOR.CODE` | `SepaInward_AuditorCode` | A (Alphanumeric) |  | This field is used In case of reverse � not used. Validation Rules Value upto 4 type A(Alphanumeric) |
| 104 | `SEP.IC.AUDIT.DATE.TIME` | `SepaInward_AuditDateTime` | A (Alphanumeric) |  | This field is used In case of reverse � not used. Validation Rules Value upto 15 type A(Alphanumeric) |
