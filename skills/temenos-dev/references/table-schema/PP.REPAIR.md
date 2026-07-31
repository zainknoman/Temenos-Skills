# PP.REPAIR — Table Schema

> Source: `INSERTS/I_F.PP.REPAIR` in `PP_OrderEntryRepairService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RPG.Status` | `PpRepair_Status` | TField |  | Indicates the Status Code (a Numeric number between 0 - 999) of the payment that is currently being processed. For Order Entry, The initial value of Status is 135. (Pending Submit) After successful Submit Action, the Status is changed to 315.(Pending Authorize) After successful First Authorize Action, the Status is changed to 316. After successful Final Authorize Action, the Status is changed to 600. No Input Field. |
| 2 | `PP.RPG.TransactionReferenceNumber` | `PpRepair_Transactionreferencenumber` | TField |  | Will hold a system generated unique number (FT Number) to identify the payment throughout its processing. Operator upon entering processing company and click the TRN button, the Transaction Reference Number is generated based on Company ID Date and Sequence number. No Input Field. |
| 3 | `PP.RPG.SendersReferenceNumber` | `PpRepair_Sendersreferencenumber` | TField |  | Tag 20. Free Text Field. |
| 4 | `PP.RPG.RelatedReference` | `PpRepair_Relatedreference` | TField |  | Free Text Field. Tag 21 |
| 5 | `PP.RPG.Source` | `PpRepair_Source` | TField |  | Will contain the actual source through which the payment was originated. No Input Field. Defaulted with a value 'OE' for Order Entry. |
| 6 | `PP.RPG.Direction` | `PpRepair_Direction` | TField |  | Indicates the direction of the payment. Drop Down Field. No Input Field. Possible values: 1. I - Incoming 2. O - Outgoing 3. B - Book transfer 4. R - Redirect (Future Use) |
| 7 | `PP.RPG.TransferType` | `PpRepair_Transfertype` | TField |  | CTR BTR Indicator Field. Possible Values: 1. "C" for CTR (Customer Transfer) 2. "B" For BTR (Bank Transfer) |
| 8 | `PP.RPG.IncomingMessageType` | `PpRepair_Incomingmessagetype` | TField |  | Default value is "RFCT" for Order Entry. No Input Field. |
| 9 | `PP.RPG.PreAuthorizationNumber` | `PpRepair_Preauthorizationnumber` | TField |  | Operator can key in the ID of AC.FUNDS.AUTHORISATION table, if the funds were pre-authorized. (Pre Authorization Key) Free Text Field. |
| 10 | `PP.RPG.ProcessCompany` | `PpRepair_Processcompany` | TField |  | Indicates the company code of the company where the payment is processed. Possible values are fetched from the the PPT.COMPANY Table. Drop Down Field. |
| 11 | `PP.RPG.ProcessingDate` | `PpRepair_Processingdate` | TField |  | Indicates the date on which the processing is supposed to happen. Date Field. |
| 12 | `PP.RPG.Priority` | `PpRepair_Priority` | TField |  | Identifies the Payment Message Priority and based on this value priority code is set in the payment engine. IF MessagePriority is empty or between 1 and 5, then PriorityCode is 'N' IF MessagePriority is between 6 and 9, then PriorityCode is 'U' Possible values: 1 to 9 Drop Down Value. |
| 13 | `PP.RPG.Product` | `PpRepair_Product` | TField |  | Must contain a valid Clearing ID from PPT.CLEARINGNATURECODE table Free Text Field. |
| 14 | `PP.RPG.OutputChannel` | `PpRepair_Outputchannel` | TField |  | Indicates the output channel for the payment. Default Possible values: LORO, NOSTRO, LEDGER Validation Rules: Other Possible values Values are populated based on field 'Clearing' in PPT.CLEARINGSETTING Drop Down Field. |
| 15 | `PP.RPG.OutputChannelImposedFlag` | `PpRepair_Outputchannelimposedflag` | TField |  | If imposed the corresponding channel entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 16 | `PP.RPG.TransactionCurrency` | `PpRepair_Transactioncurrency` | TField | Yes | Indicates the currency in which the payment is processed. Will hold valid currency code values from PPT.CURRENCY table. Drop Down Field. Mandatory Field. |
| 17 | `PP.RPG.TransactionAmount` | `PpRepair_Transactionamount` | TField | Yes | Indicates the amount for which the payment needs to be processed. Mandatory Field. |
| 18 | `PP.RPG.ChargeOption` | `PpRepair_Chargeoption` | TField |  | Contains the Details of Charge (Tag 71 A) Possible Values: 1. "BEN" 2. "SHA" 3. "OUR" Drop Down Field. |
| 19 | `PP.RPG.SenderInstitutionBIC` | `PpRepair_Senderinstitutionbic` | TField |  | Bank Identification Code of the Sender Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. Free Text Field. |
| 20 | `PP.RPG.SenderInstitutionNCC` | `PpRepair_Senderinstitutionncc` | TField |  | National Clearing Code of the Sender Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Free Text Field. |
| 21 | `PP.RPG.ReceiverInstitutionBIC` | `PpRepair_Receiverinstitutionbic` | TField |  | Bank Identification Code of the Receiver Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. Free Text Field. |
| 22 | `PP.RPG.ReceiverInstitutionNCC` | `PpRepair_Receiverinstitutionncc` | TField |  | National Clearing Code of the Receiver Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODEtable. Free Text Field. |
| 23 | `PP.RPG.DebitAccountCompany` | `PpRepair_Debitaccountcompany` | TField |  | Indicates the Company ID of the Debit Party. Accepts valid value as defined in the PPT.COMPANY table. |
| 24 | `PP.RPG.OrderPartyTagOption` | `PpRepair_Orderpartytagoption` | TField |  | The field can contain the following values: F, K (future phases), or "blank". The field can be used for Order Entry mode in case of Outgoing CTR payments. If the operator wants to impose the tag option 50F or 50K he can do so by setting this field. The data inputted by the operator will then take precedence over the account details from the ledger. |
| 25 | `PP.RPG.DebitAccountNumber` | `PpRepair_Debitaccountnumber` | TField |  | Indicates the Account Number of the Debit Party Accepts value as defined in ACCOUNT table. |
| 26 | `PP.RPG.DebitAccountNumberBIC` | `PpRepair_Debitaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Debit Party. |
| 27 | `PP.RPG.DebitAccountNumberImposedFlag` | `PpRepair_Debitaccountnumberimposedflag` | TField |  | When imposed the corresponding Debit Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 28 | `PP.RPG.DebitAccountCurrency` | `PpRepair_Debitaccountcurrency` | TField |  | Indicates the Currency Code of the Debit Party. Accepts valid value as defined in the PPT.CURRENCY table. |
| 29 | `PP.RPG.DebitAmount` | `PpRepair_Debitamount` | TField |  | Indicates the Debit amount which is to be debited from sender. Calculated based on transaction amount involving any FX if applicable. |
| 30 | `PP.RPG.DebitExchangeRate` | `PpRepair_Debitexchangerate` | TField |  | The exchange rate that is used to convert the debit amount into the transaction amount (or transaction amount into debit amount) in case the debit account currency is different from the transaction currency. |
| 31 | `PP.RPG.DebitExchangeRateImposedFlag` | `PpRepair_Debitexchangerateimposedflag` | TField |  | If debit exchange rate is imposed by the operator and the entered value will not be overridden by the payment engine. Check Box Field. |
| 32 | `PP.RPG.DebitExchangeRateReference` | `PpRepair_Debitexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of a foreign currency by the dealer. This is only for transactions that exceed the threshold. The payment operator contacts treasury for a deal. |
| 33 | `PP.RPG.DebitValueDate` | `PpRepair_Debitvaluedate` | TField |  | Indicates the date on which the actual debit will happen. If left empty, Payment Engine will calculate this date based on Processing Date |
| 34 | `PP.RPG.DebitValueDateImposedFlag` | `PpRepair_Debitvaluedateimposedflag` | TField |  | This field specifies whether the debit value date is imposed or can still be overwritten by the date component. In case the impose flag is lacking but the debit value date is specified, the manual input is more a suggestion towards the system. In case the impose flag is present and the debit value date is specified, the manual input is a hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. Possible values: "Y" " " |
| 35 | `PP.RPG.OrderingAccount` | `PpRepair_Orderingaccount` | TField |  | National Clearing Code or Account Number of the Ordering Party can be entered. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 36 | `PP.RPG.OrderingName` | `PpRepair_Orderingname` | TField |  | Free Text Field. Free Text Field, wherein Additional Address details(Usually Name) of the Ordering Party can be entered. |
| 37 | `PP.RPG.OrderingAddress1` | `PpRepair_Orderingaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 38 | `PP.RPG.OrderingAddress2` | `PpRepair_Orderingaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 39 | `PP.RPG.OrderingAddress3` | `PpRepair_Orderingaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 40 | `PP.RPG.OrderingCountry` | `PpRepair_Orderingcountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from PPT.COUNTRYIBANSTRUCTURE. Drop Down Field. |
| 41 | `PP.RPG.VATDebitMainAmountIndicator` | `PpRepair_Vatdebitmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Main Amount % (VATDebitMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 42 | `PP.RPG.VATDebitMainAmountPercentage` | `PpRepair_Vatdebitmainamountpercentage` | TField |  | Indicates the percentage on Debit Main Amount. |
| 43 | `PP.RPG.CreditAccountCompany` | `PpRepair_Creditaccountcompany` | TField |  | Indicates the Company ID of the Credit Party. Accepts valid value as defined in the PPT.COMPANY table. |
| 44 | `PP.RPG.CreditAccountNumber` | `PpRepair_Creditaccountnumber` | TField |  | Indicates the Account Number of the Credit Party Accepts value as defined in ACCOUNT table. |
| 45 | `PP.RPG.CreditAccountNumberBIC` | `PpRepair_Creditaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Credit Party. |
| 46 | `PP.RPG.CreditAccountNumberImposedFlag` | `PpRepair_Creditaccountnumberimposedflag` | TField |  | When imposed the corresponding Credit Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 47 | `PP.RPG.CreditAccountCurrency` | `PpRepair_Creditaccountcurrency` | TField |  | Indicates the Currency Code of the Credit Party. Accepts valid value as defined in the PPT.CURRENCY table. |
| 48 | `PP.RPG.CreditAmount` | `PpRepair_Creditamount` | TField |  | Indicates the credit amount which is to be credited to the beneficiary. Calculated based on transaction amount involving any FX if present. |
| 49 | `PP.RPG.CreditExchangeRate` | `PpRepair_Creditexchangerate` | TField |  | The exchange rate that is used to convert the credit amount into the transaction amount (or transaction amount into debit amount) in case the credit account currency is different from the transaction currency. |
| 50 | `PP.RPG.CreditExchangeRateImposedFlag` | `PpRepair_Creditexchangerateimposedflag` | TField |  | If credit exchange rate is imposed by the operator and the entered value will not be overridden by the payment engine. Check Box Field. |
| 51 | `PP.RPG.CreditExchangeRateReference` | `PpRepair_Creditexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of a foreign currency by the dealer. This is only for transactions that exceed the threshold. The payment operator contacts treasury for a deal. |
| 52 | `PP.RPG.CreditValueDate` | `PpRepair_Creditvaluedate` | TField |  | Indicates the date on which the actual credit will happen. If left empty, Payment Engine will calculate this date based on Processing Date. |
| 53 | `PP.RPG.CreditValueDateImposedFlag` | `PpRepair_Creditvaluedateimposedflag` | TField |  | This field specifies whether the credit value date is imposed or can still be overwritten by the date component. In case the impose flag is lacking but the credit value date is specified, the manual input is more a suggestion towards the system. In case the impose flag is present and the credit value date is specified, the manual input is a hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. |
| 54 | `PP.RPG.BeneficiaryAccount` | `PpRepair_Beneficiaryaccount` | TField |  | Specifies National Clearing Code or Account Number of the Beneficiary Institution(BENINS for BTR) or Beneficiary(BENFCY for CTR). National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 55 | `PP.RPG.BeneficiaryName` | `PpRepair_Beneficiaryname` | TField |  | Free Text Field, wherein Additional Address details(Usually Name) of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Free Text Field. |
| 56 | `PP.RPG.BeneficiaryAddress1` | `PpRepair_Beneficiaryaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 57 | `PP.RPG.BeneficiaryAddress2` | `PpRepair_Beneficiaryaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 58 | `PP.RPG.BeneficiaryAddress3` | `PpRepair_Beneficiaryaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 59 | `PP.RPG.BeneficiaryCountry` | `PpRepair_Beneficiarycountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from CountryIBANStructure table. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Drop Down Field. |
| 60 | `PP.RPG.VATCreditMainAmountIndicator` | `PpRepair_Vatcreditmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Main Amount % (VATCreditMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 61 | `PP.RPG.VATCreditMainAmountPercentage` | `PpRepair_Vatcreditmainamountpercentage` | TField |  | Indicates the percentage on Credit Main Amount. |
| 62 | `PP.RPG.WaiveDebitCharges` | `PpRepair_Waivedebitcharges` | TField |  | Indicates whether the debit side charges/fees can be skipped/waived or not. Check Box Field. |
| 63 | `PP.RPG.DebitChargeAccountCompany` | `PpRepair_Debitchargeaccountcompany` | TField |  | Indicates the company code where the debit charge account is maintained. Drop Down Field. |
| 64 | `PP.RPG.DebitChargeAccount` | `PpRepair_Debitchargeaccount` | TField |  | Indicates the account number to where the charges will be debited. |
| 65 | `PP.RPG.DebitChargeAccountImposedFlag` | `PpRepair_Debitchargeaccountimposedflag` | TField |  | When imposed the corresponding Debit Charge Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 66 | `PP.RPG.DebitChargeAccountCurrency` | `PpRepair_Debitchargeaccountcurrency` | TField |  | Indicates the currency code of the debit charge account. Drop Down Field. |
| 67 | `PP.RPG.DebitChargeImposedFlag` | `PpRepair_Debitchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee component that the default charges are not to be calculated. Check Box Field. |
| 68 | `PP.RPG.DebitChargeComponent` | `PpRepair_Debitchargecomponent` |  |  |  |
| 69 | `PP.RPG.DebitChargeCurrency` | `PpRepair_Debitchargecurrency` |  |  |  |
| 70 | `PP.RPG.DebitChargeAmount` | `PpRepair_Debitchargeamount` |  |  |  |
| 71 | `PP.RPG.DebitReceiverCharge` | `PpRepair_Debitreceivercharge` | TField |  | Outgoing OUR charge amount which can be used by posting and also swift component to determine the outgoing 71G mapping. |
| 72 | `PP.RPG.DebitReceiverChargeImposedFlag` | `PpRepair_Debitreceiverchargeimposedflag` | TField |  | If imposed the operator entered value in the Outgoing Receiver Charge (DebitReceiverCharge) field will not be overridden by the payment engine. Check Box Field. |
| 73 | `PP.RPG.VATDebitMainChargeIndicator` | `PpRepair_Vatdebitmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Charge Amount % (VATDebitMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 74 | `PP.RPG.VATDebitMainChargePercentage` | `PpRepair_Vatdebitmainchargepercentage` | TField |  | Indicates the percentage of VAT which needs to be calculated over the debit charge amount of the transaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specified percentage will override the percentage present in the client conditions component. |
| 75 | `PP.RPG.WaiveCreditCharges` | `PpRepair_Waivecreditcharges` | TField |  | Indicates whether the credit side charges/fees can be skipped/waived or not. Check Box Field. |
| 76 | `PP.RPG.CreditChargeAccountCompany` | `PpRepair_Creditchargeaccountcompany` | TField |  | Indicates the company code where the charge account is maintained. Drop Down Field. |
| 77 | `PP.RPG.CreditChargeAccount` | `PpRepair_Creditchargeaccount` | TField |  | Indicates the account number, to where the charges will be credited |
| 78 | `PP.RPG.CreditChargeAccountImposedFlag` | `PpRepair_Creditchargeaccountimposedflag` | TField |  | When imposed the corresponding Credit Charge Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 79 | `PP.RPG.CreditChargeAccountCurrency` | `PpRepair_Creditchargeaccountcurrency` | TField |  | Indicates the currency code of the charge account. Drop Down Field. |
| 80 | `PP.RPG.CreditChargeImposedFlag` | `PpRepair_Creditchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee component that the default charges are not to be calculated. Check Box Field. |
| 81 | `PP.RPG.CreditChargeComponent` | `PpRepair_Creditchargecomponent` |  |  |  |
| 82 | `PP.RPG.CreditChargeCurrency` | `PpRepair_Creditchargecurrency` |  |  |  |
| 83 | `PP.RPG.CreditChargeAmount` | `PpRepair_Creditchargeamount` |  |  |  |
| 84 | `PP.RPG.CreditReceiverCharge` | `PpRepair_Creditreceivercharge` | TField |  | Incoming our Charge amount. |
| 85 | `PP.RPG.VATCreditMainChargeIndicator` | `PpRepair_Vatcreditmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Charge Amount % (VATCreditMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 86 | `PP.RPG.VATCreditMainChargePercentage` | `PpRepair_Vatcreditmainchargepercentage` | TField |  | This field specifies the percentage of VAT which needs to be calculated over the credit charge amount of the transaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specified percentage will override the percentage present in the client conditions component. |
| 87 | `PP.RPG.OrderingInstAccount` | `PpRepair_Orderinginstaccount` | TField |  | National Clearing Code or Account Number of the Ordering Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 88 | `PP.RPG.OrderingInstIdentifierCode` | `PpRepair_Orderinginstidentifiercode` | TField |  | Bank Identification Code of the Ordering Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 89 | `PP.RPG.OrderingInstAddress` | `PpRepair_Orderinginstaddress` |  |  |  |
| 90 | `PP.RPG.SendersCorresAccount` | `PpRepair_Senderscorresaccount` | TField |  | National Clearing Code or Account Number of the Sender Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 91 | `PP.RPG.SendersCorresIdentifierCode` | `PpRepair_Senderscorresidentifiercode` | TField |  | Bank Identification Code of the Sender Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 92 | `PP.RPG.SendersCorresAddress` | `PpRepair_Senderscorresaddress` |  |  |  |
| 93 | `PP.RPG.ReceiversCorresAccount` | `PpRepair_Receiverscorresaccount` | TField |  | National Clearing Code or Account Number of the Receiver Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 94 | `PP.RPG.ReceiversCorresIdentifierCode` | `PpRepair_Receiverscorresidentifiercode` | TField |  | Bank Identification Code of the Receiver Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 95 | `PP.RPG.ReceiversCorresAddress` | `PpRepair_Receiverscorresaddress` |  |  |  |
| 96 | `PP.RPG.ThirdReimburseInstAccount` | `PpRepair_Thirdreimburseinstaccount` | TField |  | National Clearing Code or Account Number of the Third Reimbursement Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 97 | `PP.RPG.ThirdReimburseInstIdentifierCd` | `PpRepair_Thirdreimburseinstidentifiercd` | TField |  | Bank Identification Code of the Third Reimbursement Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 98 | `PP.RPG.ThirdReimburseInstAddress` | `PpRepair_Thirdreimburseinstaddress` |  |  |  |
| 99 | `PP.RPG.IntermediaryInstAccount` | `PpRepair_Intermediaryinstaccount` | TField |  | National Clearing Code or Account Number of the Intermediary Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 100 | `PP.RPG.IntermediaryInstIdentifierCode` | `PpRepair_Intermediaryinstidentifiercode` | TField |  | Bank Identification Code of the Intermediary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 101 | `PP.RPG.IntermediaryInstAddress` | `PpRepair_Intermediaryinstaddress` |  |  |  |
| 102 | `PP.RPG.AccountWithInstAccount` | `PpRepair_Accountwithinstaccount` | TField |  | Specifies the National Clearing Code or Account Number of the Account with Institution. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. Account with Institution Tag 57 A, B, C or D {ACWINS} |
| 103 | `PP.RPG.AccountWithInstIdentifierCode` | `PpRepair_Accountwithinstidentifiercode` | TField |  | Specifies the Bank Identification Code of the Account with Institution. Account with Institution Tag 57 A, B, C or D {ACWINS} Validation Rules: Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 104 | `PP.RPG.AccountWithInstAddress` | `PpRepair_Accountwithinstaddress` |  |  |  |
| 105 | `PP.RPG.InstructionCode` | `PpRepair_Instructioncode` |  |  |  |
| 106 | `PP.RPG.PaymentDetails` | `PpRepair_Paymentdetails` |  |  |  |
| 107 | `PP.RPG.AdditionalText` | `PpRepair_Additionaltext` | TField |  | Free Text Field wherein the operator can specify additional information relating to the payment instruction. |
| 108 | `PP.RPG.AuditTrail` | `PpRepair_Audittrail` | TField |  | Used for internal purpose. Context Enquiry attached to this field will launch the Audit Trail Details (POR.HISTORYLOG) of the corresponding payment in a separate screen. |
| 109 | `PP.RPG.Information` | `PpRepair_Information` |  |  |  |
| 110 | `PP.RPG.AcceptWarning` | `PpRepair_Acceptwarning` | TField | Yes | Whenever an Warning Type of error is encountered by the payment, the operator must accept the warning (Mandatory) to proceed with further payment processing. Check Box Field. |
| 111 | `PP.RPG.Warning` | `PpRepair_Warning` |  |  |  |
| 112 | `PP.RPG.FunctionalError` | `PpRepair_Functionalerror` |  |  |  |
| 113 | `PP.RPG.FatalError` | `PpRepair_Fatalerror` | TField |  | Highlights the text "Error Information Present" on the main screen, if there are any errors present in Error Information Tab. No Input Field. |
| 114 | `PP.RPG.ValidationFlag` | `PpRepair_Validationflag` | TField |  | Triggers diffent type of validations for MT messages in the payments hub. Taken from Field 119 from Heading Block 3 Example: Duplicate check processing uses this field to identify 202COV payments. Validation Rules: 8 alphanumeric characters. No Input. |
| 115 | `PP.RPG.BalanceReservation` | `PpRepair_Balancereservation` | TField |  | This field gives the status of Balance Check for a payment. Possible values: A - Approved P - Pending R - Rejected S - Skipped. Balance check not required for the payment. E - Error Received from Balance Check Interface Validation Rules: 1 alphanumeric character. No Input. |
| 116 | `PP.RPG.BalanceReservationNumber` | `PpRepair_Balancereservationnumber` | TField |  | Indicates the unique reservation reference number which is returned by T24 when funds are reserved as part of balance check component. This may not be present if account being debited is a nostro account. Format ACFAjjjjjxxxxxxx. Validation Rules: 16 alphanumeric characters. No Input. |
| 117 | `PP.RPG.ProcessingDateImposedFlag` | `PpRepair_Processingdateimposedflag` | TField |  | If imposed the corresponding Processing date entered by the operator is not overridden by the payment engine. Check Box Field. |
| 118 | `PP.RPG.DebitRepairFee` | `PpRepair_Debitrepairfee` | TField |  | Specifies the fee to be charged from the customer for debit side repair operations. Validation Rules: No Input. |
| 119 | `PP.RPG.CreditRepairFee` | `PpRepair_Creditrepairfee` | TField |  | Specifies the fee to be charged from the customer for credit side repair operations. Validation Rules: No Input. |
| 120 | `PP.RPG.Action` | `PpRepair_Action` | TField |  | Used for internal purpose. This field can hold upto 1 alphanumeric character and the value is not editable by the user. Possible Values will be G, V, S, C, R and A |
| 121 | `PP.RPG.CancelDescription` | `PpRepair_Canceldescription` | TField |  | Describes the reason for cancellation of a payment. Operator uses this field to let authoriser know the justification for such an action. Free Text Field. |
| 122 | `PP.RPG.RejectDescription` | `PpRepair_Rejectdescription` | TField |  | Free Text Field, wherein the operator can specify the reason for rejecting the payment. |
| 123 | `PP.RPG.DebitInstruction` | `PpRepair_Debitinstruction` | TField |  | Enriches value from POR.DEBITBANKCONDITIONS table after the payment is validated. Contains any credit instructions if present for a bank, which will be useful for the operator how to process the payment. No Input Field. |
| 124 | `PP.RPG.CreditInstruction` | `PpRepair_Creditinstruction` | TField |  | Enriches value from POR.DEBITBANKCONDITIONS after the payment is validated. Contains any credit instructions if present for a bank, which will be useful for the operator how to process the payment. No input field. |
| 125 | `PP.RPG.ShowOriginalRoutingInfo` | `PpRepair_Showoriginalroutinginfo` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 126 | `PP.RPG.OrderingIdentifierCode` | `PpRepair_Orderingidentifiercode` | TField |  | Bank Identification Code of the Ordering Party can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 127 | `PP.RPG.BeneficiaryIdentifierCode` | `PpRepair_Beneficiaryidentifiercode` | TField |  | Bank Identification Code of the Beneficiary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 128 | `PP.RPG.DebitTreasuryRate` | `PpRepair_Debittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. The Final exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of the appropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 129 | `PP.RPG.DebitTreasuryRateImposedFlag` | `PpRepair_Debittreasuryrateimposedflag` | TField |  | If Debit Treasury Rate is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 130 | `PP.RPG.DebitCustomerSpread` | `PpRepair_Debitcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generate the final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 131 | `PP.RPG.DebitCustSpreadImposedFlag` | `PpRepair_Debitcustspreadimposedflag` | TField |  | If Debit Customer Spread is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 132 | `PP.RPG.CreditTreasuryRate` | `PpRepair_Credittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. The Final exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of the appropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 133 | `PP.RPG.CreditTreasuryRateImposedFlag` | `PpRepair_Credittreasuryrateimposedflag` | TField |  | If Credit Treasury Rate is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 134 | `PP.RPG.CreditCustomerSpread` | `PpRepair_Creditcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generate the final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 135 | `PP.RPG.CreditCustSpreadImposedFlag` | `PpRepair_Creditcustspreadimposedflag` | TField |  | If Credit Customer Spread is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 136 | `PP.RPG.FieldPrompt` | `PpRepair_Fieldprompt` |  |  |  |
| 137 | `PP.RPG.OldValue` | `PpRepair_Oldvalue` |  |  |  |
| 138 | `PP.RPG.NewValue` | `PpRepair_Newvalue` |  |  |  |
| 139 | `PP.RPG.IntraCompanyPayment` | `PpRepair_Intracompanypayment` | TField |  |  |
| 140 | `PP.RPG.SelectTemplate` | `PpRepair_Selecttemplate` | TField |  |  |
| 141 | `PP.RPG.SaveAsTemplate` | `PpRepair_Saveastemplate` | TField |  |  |
| 142 | `PP.RPG.NickName` | `PpRepair_Nickname` | TField |  |  |
| 143 | `PP.RPG.StoreTemplateValues` | `PpRepair_Storetemplatevalues` | TField |  |  |
| 144 | `PP.RPG.ReturnPayment` | `PpRepair_Returnpayment` | TField |  | This flag will be set to "Y" or "N" . Check Box Field. |
| 145 | `PP.RPG.ReturnCode` | `PpRepair_Returncode` | TField |  | Return Code. Validation Rules: 3 alphanumeric characters. |
| 146 | `PP.RPG.ReturnDescription` | `PpRepair_Returndescription` | TField |  | Free Text Field. Validation Rules: 256 alphanumeric characters. |
| 147 | `PP.RPG.UltDbtNm` | `PpRepair_Ultdbtnm` | TField |  |  |
| 148 | `PP.RPG.UltDbtBIC` | `PpRepair_Ultdbtbic` | TField |  |  |
| 149 | `PP.RPG.UltDbtOrgIdOthId` | `PpRepair_Ultdbtorgidothid` | TField |  |  |
| 150 | `PP.RPG.UltDbtOrgIdOthSchCd` | `PpRepair_Ultdbtorgidothschcd` | TField |  |  |
| 151 | `PP.RPG.UltDbtOrgIdOthSchProp` | `PpRepair_Ultdbtorgidothschprop` | TField |  |  |
| 152 | `PP.RPG.UltDbtOrgIdOthIssuer` | `PpRepair_Ultdbtorgidothissuer` | TField |  |  |
| 153 | `PP.RPG.UltDbtBrDt` | `PpRepair_Ultdbtbrdt` | TField |  |  |
| 154 | `PP.RPG.UltDbtPvOfBr` | `PpRepair_Ultdbtpvofbr` | TField |  |  |
| 155 | `PP.RPG.UltDbtCityOfBr` | `PpRepair_Ultdbtcityofbr` | TField |  |  |
| 156 | `PP.RPG.UltDbtCtryOfBr` | `PpRepair_Ultdbtctryofbr` | TField |  |  |
| 157 | `PP.RPG.UltDbtPrvIdOthId` | `PpRepair_Ultdbtprvidothid` | TField |  |  |
| 158 | `PP.RPG.UltDbtPrvIdOthSchCd` | `PpRepair_Ultdbtprvidothschcd` | TField |  |  |
| 159 | `PP.RPG.UltDbtPrvIdOthSchProp` | `PpRepair_Ultdbtprvidothschprop` | TField |  |  |
| 160 | `PP.RPG.UltDbtPrvIdOthIssuer` | `PpRepair_Ultdbtprvidothissuer` | TField |  |  |
| 161 | `PP.RPG.DbtOrgIdOthId` | `PpRepair_Dbtorgidothid` | TField |  |  |
| 162 | `PP.RPG.DbtOrgIdOthSchCd` | `PpRepair_Dbtorgidothschcd` | TField |  |  |
| 163 | `PP.RPG.DbtOrgIdOthSchProp` | `PpRepair_Dbtorgidothschprop` | TField |  |  |
| 164 | `PP.RPG.DbtOrgIdOthIssuer` | `PpRepair_Dbtorgidothissuer` | TField |  |  |
| 165 | `PP.RPG.DbtBrDt` | `PpRepair_Dbtbrdt` | TField |  |  |
| 166 | `PP.RPG.DbtPvOfBr` | `PpRepair_Dbtpvofbr` | TField |  |  |
| 167 | `PP.RPG.DbtCityOfBr` | `PpRepair_Dbtcityofbr` | TField |  |  |
| 168 | `PP.RPG.DbtCtryOfBr` | `PpRepair_Dbtctryofbr` | TField |  |  |
| 169 | `PP.RPG.DbtPrvIdOthId` | `PpRepair_Dbtprvidothid` | TField |  |  |
| 170 | `PP.RPG.DbtPrvIdOthSchCd` | `PpRepair_Dbtprvidothschcd` | TField |  |  |
| 171 | `PP.RPG.DbtPrvIdOthSchProp` | `PpRepair_Dbtprvidothschprop` | TField |  |  |
| 172 | `PP.RPG.DbtPrvIdOthIssuer` | `PpRepair_Dbtprvidothissuer` | TField |  |  |
| 173 | `PP.RPG.CrdOrgIdOthId` | `PpRepair_Crdorgidothid` | TField |  |  |
| 174 | `PP.RPG.CrdOrgIdOthSchCd` | `PpRepair_Crdorgidothschcd` | TField |  |  |
| 175 | `PP.RPG.CrdOrgIdOthSchProp` | `PpRepair_Crdorgidothschprop` | TField |  |  |
| 176 | `PP.RPG.CrdOrgIdOthIssuer` | `PpRepair_Crdorgidothissuer` | TField |  |  |
| 177 | `PP.RPG.CrdBrDt` | `PpRepair_Crdbrdt` | TField |  |  |
| 178 | `PP.RPG.CrdPvOfBr` | `PpRepair_Crdpvofbr` | TField |  |  |
| 179 | `PP.RPG.CrdCityOfBr` | `PpRepair_Crdcityofbr` | TField |  |  |
| 180 | `PP.RPG.CrdCtryOfBr` | `PpRepair_Crdctryofbr` | TField |  |  |
| 181 | `PP.RPG.CrdPrvIdOthId` | `PpRepair_Crdprvidothid` | TField |  |  |
| 182 | `PP.RPG.CrdPrvIdOthSchCd` | `PpRepair_Crdprvidothschcd` | TField |  |  |
| 183 | `PP.RPG.CrdPrvIdOthSchProp` | `PpRepair_Crdprvidothschprop` | TField |  |  |
| 184 | `PP.RPG.CrdPrvIdOthIssuer` | `PpRepair_Crdprvidothissuer` | TField |  |  |
| 185 | `PP.RPG.UltCrdNm` | `PpRepair_Ultcrdnm` | TField |  |  |
| 186 | `PP.RPG.UltCrdBIC` | `PpRepair_Ultcrdbic` | TField |  |  |
| 187 | `PP.RPG.UltCrdOrgIdOthId` | `PpRepair_Ultcrdorgidothid` | TField |  |  |
| 188 | `PP.RPG.UltCrdOrgIdOthSchCd` | `PpRepair_Ultcrdorgidothschcd` | TField |  |  |
| 189 | `PP.RPG.UltCrdOrgIdOthSchProp` | `PpRepair_Ultcrdorgidothschprop` | TField |  |  |
| 190 | `PP.RPG.UltCrdOrgIdOthIssuer` | `PpRepair_Ultcrdorgidothissuer` | TField |  |  |
| 191 | `PP.RPG.UltCrdBrDt` | `PpRepair_Ultcrdbrdt` | TField |  |  |
| 192 | `PP.RPG.UltCrdPvOfBr` | `PpRepair_Ultcrdpvofbr` | TField |  |  |
| 193 | `PP.RPG.UltCrdCityOfBr` | `PpRepair_Ultcrdcityofbr` | TField |  |  |
| 194 | `PP.RPG.UltCrdCtryOfBr` | `PpRepair_Ultcrdctryofbr` | TField |  |  |
| 195 | `PP.RPG.UltCrdPrvIdOthId` | `PpRepair_Ultcrdprvidothid` | TField |  |  |
| 196 | `PP.RPG.UltCrdPrvIdOthSchCd` | `PpRepair_Ultcrdprvidothschcd` | TField |  |  |
| 197 | `PP.RPG.UltCrdPrvIdOthSchProp` | `PpRepair_Ultcrdprvidothschprop` | TField |  |  |
| 198 | `PP.RPG.UltCrdPrvIdOthIssuer` | `PpRepair_Ultcrdprvidothissuer` | TField |  |  |
| 199 | `PP.RPG.CrdRefInfTpCd` | `PpRepair_Crdrefinftpcd` |  |  |  |
| 200 | `PP.RPG.CrdRefInfTpIssuer` | `PpRepair_Crdrefinftpissuer` |  |  |  |
| 201 | `PP.RPG.CrdRefInfRef` | `PpRepair_Crdrefinfref` |  |  |  |
| 202 | `PP.RPG.CatPurpCd` | `PpRepair_Catpurpcd` |  |  |  |
| 203 | `PP.RPG.CatPurpProp` | `PpRepair_Catpurpprop` |  |  |  |
| 204 | `PP.RPG.TrxPurpCd` | `PpRepair_Trxpurpcd` |  |  |  |
| 205 | `PP.RPG.ExtendedFields` | `PpRepair_Extendedfields` | TField |  |  |
| 206 | `PP.RPG.MndtId` | `PpRepair_Mndtid` | TField |  | Indicates the unique mandate identification. The value of this field is updated to the field "MandateReference" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. |
| 207 | `PP.RPG.MndtDtOfSgn` | `PpRepair_Mndtdtofsgn` | TField |  | Indicates the date of signature of the mandate. The value of this field is updated to the field "SignatureDate" in POR.DEBITAUTHINFO table. Validation Rules: 11 characters of type Date. |
| 208 | `PP.RPG.MndtAmdtInd` | `PpRepair_Mndtamdtind` | TField |  | Indicates the Amendment indicator of the mandate. The value of this field is updated to the field "AmendmentIndicator" in POR.DEBITAUTHINFO table. Possible values: 'N' - this means that none of the fields should be filled. 'Y' - this means that at least one of the fields should be filled. Note: The mentioned fields here are: OriginalMandateReference, OriginalCreditorName, OriginalCreditorId, OriginalCreditorSchProp, OriginalDebtorAccount, OriginalDebtorAgtOtherID Default value is "N". Validation Rules: 1 alphabetic characters. |
| 209 | `PP.RPG.MndtOrglMndtId` | `PpRepair_Mndtorglmndtid` | TField | Yes | Indicates the Reference of the original MandateID as received in Incoming Direct Debit message. The value of this field is updated to the field "OriginalMandateReference" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Mandatory only if OriginalMandateReference is different from MandateReference. |
| 210 | `PP.RPG.MndtOrglCrdSchNm` | `PpRepair_Mndtorglcrdschnm` | TField |  | Indicates the original name of the Creditor who issued the mandate. The value of this field is updated to the field "OriginalCreditorName" in POR.DEBITAUTHINFO table. Validation Rules: 70 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 211 | `PP.RPG.MndtOrglCrdSchPrvOthId` | `PpRepair_Mndtorglcrdschprvothid` | TField |  | Indicates the Original Creditor ID as it is mapped from Incoming Direct Debit message. The value of this field is updated to the field "OriginalCreditorID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 212 | `PP.RPG.MndtOrglCrdSchPrvOthSchNmProp` | `PpRepair_Mndtorglcrdschprvothschnmprop` | TField |  | Indicates the scheme name of the original Creditor. The value of this field is updated to the field "OriginalCreditorSchProp" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Only "SEPA" value is allowed. |
| 213 | `PP.RPG.MndtOrglDbtAccIdIBAN` | `PpRepair_Mndtorgldbtaccidiban` | TField |  | Indicates the original Debtor account IBAN. The value of this field is updated to the field "OriginalDebtorAccount" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". If present only IBAN is allowed. Only present if changes occur in "Debtor Account" received from Incoming Direct Debit message. |
| 214 | `PP.RPG.MndtOrglDbtAgFinInstIdBIC` | `PpRepair_Mndtorgldbtagfininstidbic` | TField |  | Indicates the Original Debtor Agent Financial Institution Identification BIC. The value of this field is updated to the field "OriginalDebtorAgtBIC" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 215 | `PP.RPG.MndtElectronicSgn` | `PpRepair_Mndtelectronicsgn` | TField |  | Indicates the placeholder of Electronic Signature of the Mandate provided in the incoming Direct Debit. This data element is not to be used if the mandate is a paper mandate. The value of this field is updated to the field "ElectronicSignature" in POR.DEBITAUTHINFO table. Validation Rules: 1025 alphabetic characters. |
| 216 | `PP.RPG.CrdSchIdPrvIdOthId` | `PpRepair_Crdschidprvidothid` | TField |  | Indicates the creditor business code. The value of this field is updated to the field "CreditorID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It cannot contains spaces. |
| 217 | `PP.RPG.MndtOrglDbtAccIdOthId` | `PpRepair_Mndtorgldbtaccidothid` | TField |  | Indicates the Original Debtor Account Identifier. Use account other identification with code 'SMNDA' to indicate same mandate with new Debtor Account or in case of an account change within same bank. The value of this field is updated to the field "OriginalDebtorAcctOtherID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Only "SMNDA" value is allowed. |
| 218 | `PP.RPG.BalanceReservationKeyForChgAct` | `PpRepair_Balancereservationkeyforchgact` | TField |  | Holds the reservation key of the debit charge account. |
| 219 | `PP.RPG.RequestedCollectionDate` | `PpRepair_Requestedcollectiondate` | TField |  |  |
| 220 | `PP.RPG.Scheme` | `PpRepair_Scheme` | TField |  |  |
| 221 | `PP.RPG.ClearingTransactionType` | `PpRepair_Clearingtransactiontype` | TField |  |  |
| 222 | `PP.RPG.InstructedCurrency` | `PpRepair_Instructedcurrency` | TField | Yes | Indicates the Instructed currency in which the payment to be processed. Will hold valid currency code values from PPT.CURRENCY table. Drop Down Field. Validation Rules: Mandatory when InstructedAmount is present. |
| 223 | `PP.RPG.InstructedAmount` | `PpRepair_Instructedamount` | TField | Yes | Indicates the Instructed amount for which the payment needs to be processed. Validation Rules: Mandatory when InstructedCurrency is present. |
| 224 | `PP.RPG.RESERVED.28` | `PpRepair_Reserved28` | TField |  |  |
| 225 | `PP.RPG.RESERVED.27` | `PpRepair_Reserved27` | TField |  |  |
| 226 | `PP.RPG.RESERVED.26` | `PpRepair_Reserved26` | TField |  |  |
| 227 | `PP.RPG.RESERVED.25` | `PpRepair_Reserved25` | TField |  |  |
| 228 | `PP.RPG.RESERVED.24` | `PpRepair_Reserved24` | TField |  |  |
| 229 | `PP.RPG.RESERVED.23` | `PpRepair_Reserved23` | TField |  |  |
| 230 | `PP.RPG.RESERVED.22` | `PpRepair_Reserved22` | TField |  |  |
| 231 | `PP.RPG.RESERVED.21` | `PpRepair_Reserved21` | TField |  |  |
| 232 | `PP.RPG.RESERVED.20` | `PpRepair_Reserved20` | TField |  |  |
| 233 | `PP.RPG.RESERVED.19` | `PpRepair_Reserved19` | TField |  |  |
| 234 | `PP.RPG.RESERVED.18` | `PpRepair_Reserved18` | TField |  |  |
| 235 | `PP.RPG.RESERVED.17` | `PpRepair_Reserved17` | TField |  |  |
| 236 | `PP.RPG.RESERVED.16` | `PpRepair_Reserved16` | TField |  |  |
| 237 | `PP.RPG.RESERVED.15` | `PpRepair_Reserved15` | TField |  |  |
| 238 | `PP.RPG.RESERVED.14` | `PpRepair_Reserved14` | TField |  |  |
| 239 | `PP.RPG.RESERVED.13` | `PpRepair_Reserved13` | TField |  |  |
| 240 | `PP.RPG.RESERVED.12` | `PpRepair_Reserved12` | TField |  |  |
| 241 | `PP.RPG.RESERVED.11` | `PpRepair_Reserved11` | TField |  |  |
| 242 | `PP.RPG.RESERVED.10` | `PpRepair_Reserved10` | TField |  |  |
| 243 | `PP.RPG.RESERVED.9` | `PpRepair_Reserved9` | TField |  |  |
| 244 | `PP.RPG.RESERVED.8` | `PpRepair_Reserved8` | TField |  |  |
| 245 | `PP.RPG.RESERVED.7` | `PpRepair_Reserved7` | TField |  |  |
| 246 | `PP.RPG.RESERVED.6` | `PpRepair_Reserved6` | TField |  |  |
| 247 | `PP.RPG.RESERVED.5` | `PpRepair_Reserved5` | TField |  |  |
| 248 | `PP.RPG.RESERVED.4` | `PpRepair_Reserved4` | TField |  |  |
| 249 | `PP.RPG.RESERVED.3` | `PpRepair_Reserved3` | TField |  |  |
| 250 | `PP.RPG.RESERVED.2` | `PpRepair_Reserved2` | TField |  |  |
| 251 | `PP.RPG.RESERVED.1` | `PpRepair_Reserved1` | TField |  |  |
| 252 | `PP.RPG.LOCAL.REF` | `PpRepair_LocalRef` |  |  |  |
| 253 | `PP.RPG.OVERRIDE` | `PpRepair_Override` |  |  |  |
| 254 | `PP.RPG.RECORD.STATUS` | `PpRepair_RecordStatus` | String |  |  |
| 255 | `PP.RPG.CURR.NO` | `PpRepair_CurrNo` | String |  |  |
| 256 | `PP.RPG.INPUTTER` | `PpRepair_Inputter` |  |  |  |
| 257 | `PP.RPG.DATE.TIME` | `PpRepair_DateTime` |  |  |  |
| 258 | `PP.RPG.AUTHORISER` | `PpRepair_Authoriser` | String |  |  |
| 259 | `PP.RPG.CO.CODE` | `PpRepair_CoCode` | String |  |  |
| 260 | `PP.RPG.DEPT.CODE` | `PpRepair_DeptCode` | String |  |  |
| 261 | `PP.RPG.AUDITOR.CODE` | `PpRepair_AuditorCode` | String |  |  |
| 262 | `PP.RPG.AUDIT.DATE.TIME` | `PpRepair_AuditDateTime` | String |  |  |
