# PP.AUTH.REPAIR — Table Schema

> Source: `INSERTS/I_F.PP.AUTH.REPAIR` in `PP_OrderEntryRepairService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.AUTR.Status` | `PpAuthRepair_Status` | TField |  | Indicates the Status Code (a Numeric number between 0 - 999) of the payment that is currently being processed. For Order Entry, The initial value of Status is 135. (Pending Submit) After successful Submit Action, the Status is changed to 315.(Pending Authorize) After successful First Authorize Action, the Status is changed to 316. After successful Final Authorize Action, the Status is changed to 600. No Input Field. |
| 2 | `PP.AUTR.TransactionReferenceNumber` | `PpAuthRepair_Transactionreferencenumber` | TField |  | Will hold a system generated unique number (FT Number) to identify the payment throughout its processing. Operator upon entering processing company and click the TRN button, the Transaction Reference Number is generated based on Company ID Date and Sequence number. No Input Field. |
| 3 | `PP.AUTR.SendersReferenceNumber` | `PpAuthRepair_Sendersreferencenumber` | TField |  | Tag 20. Free Text Field. |
| 4 | `PP.AUTR.RelatedReference` | `PpAuthRepair_Relatedreference` | TField |  | Free Text Field. Tag 21 |
| 5 | `PP.AUTR.Source` | `PpAuthRepair_Source` | TField |  | Will contain the actual source through which the payment was originated. No Input Field. Defaulted with a value 'OE' for Order Entry. |
| 6 | `PP.AUTR.Direction` | `PpAuthRepair_Direction` | TField |  | Indicates the direction of the payment. Drop Down Field. No Input Field. Possible values: 1. I - Incoming 2. O - Outgoing 3. B - Book transfer 4. R - Redirect (Future Use) |
| 7 | `PP.AUTR.TransferType` | `PpAuthRepair_Transfertype` | TField |  | CTR BTR Indicator Field. Possible Values: 1. "C" for CTR (Customer Transfer) 2. "B" For BTR (Bank Transfer) |
| 8 | `PP.AUTR.IncomingMessageType` | `PpAuthRepair_Incomingmessagetype` | TField |  | Default value is "RFCT" for Order Entry. No Input Field. |
| 9 | `PP.AUTR.PreAuthorizationNumber` | `PpAuthRepair_Preauthorizationnumber` | TField |  | Operator can key in the ID of AC.FUNDS.AUTHORISATION table, if the funds were pre-authorized. (Pre Authorization Key) Free Text Field. |
| 10 | `PP.AUTR.ProcessCompany` | `PpAuthRepair_Processcompany` | TField |  | Indicates the company code of the company where the payment is processed. Possible values are fetched from the the PPT.COMPANY Table. Drop Down Field. |
| 11 | `PP.AUTR.ProcessingDate` | `PpAuthRepair_Processingdate` | TField |  | Indicates the date on which the processing is supposed to happen. Date Field. |
| 12 | `PP.AUTR.Priority` | `PpAuthRepair_Priority` | TField |  | Identifies the Payment Message Priority and based on this value priority code is set in the payment engine. IF MessagePriority is empty or between 1 and 5, then PriorityCode is 'N' IF MessagePriority is between 6 and 9, then PriorityCode is 'U' Possible values: 1 to 9 Drop Down Value. |
| 13 | `PP.AUTR.Product` | `PpAuthRepair_Product` | TField |  | Must contain a valid Clearing ID from PPT.CLEARINGNATURECODE table Free Text Field. |
| 14 | `PP.AUTR.OutputChannel` | `PpAuthRepair_Outputchannel` | TField |  | Indicates the output channel for the payment. Default Possible values: LORO, NOSTRO, LEDGER Validation Rules: Other Possible values Values are populated based on field 'Clearing' in PPT.CLEARINGSETTING Drop Down Field. |
| 15 | `PP.AUTR.OutputChannelImposedFlag` | `PpAuthRepair_Outputchannelimposedflag` | TField |  | If imposed the corresponding channel entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 16 | `PP.AUTR.TransactionCurrency` | `PpAuthRepair_Transactioncurrency` | TField | Yes | Indicates the currency in which the payment is processed. Will hold valid currency code values from PPT.CURRENCY table. Drop Down Field. Mandatory Field. |
| 17 | `PP.AUTR.TransactionAmount` | `PpAuthRepair_Transactionamount` | TField | Yes | Indicates the amount for which the payment needs to be processed. Mandatory Field. |
| 18 | `PP.AUTR.ChargeOption` | `PpAuthRepair_Chargeoption` | TField |  | Contains the Details of Charge (Tag 71 A) Possible Values: 1. "BEN" 2. "SHA" 3. "OUR" Drop Down Field. |
| 19 | `PP.AUTR.SenderInstitutionBIC` | `PpAuthRepair_Senderinstitutionbic` | TField |  | Bank Identification Code of the Sender Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. Free Text Field. |
| 20 | `PP.AUTR.SenderInstitutionNCC` | `PpAuthRepair_Senderinstitutionncc` | TField |  | National Clearing Code of the Sender Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Free Text Field. |
| 21 | `PP.AUTR.ReceiverInstitutionBIC` | `PpAuthRepair_Receiverinstitutionbic` | TField |  | Bank Identification Code of the Receiver Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. Free Text Field. |
| 22 | `PP.AUTR.ReceiverInstitutionNCC` | `PpAuthRepair_Receiverinstitutionncc` | TField |  | National Clearing Code of the Receiver Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODEtable. Free Text Field. |
| 23 | `PP.AUTR.DebitAccountCompany` | `PpAuthRepair_Debitaccountcompany` | TField |  | Indicates the Company ID of the Debit Party. Accepts valid value as defined in the PPT.COMPANY table. |
| 24 | `PP.AUTR.OrderPartyTagOption` | `PpAuthRepair_Orderpartytagoption` | TField |  | The field can contain the following values: F, K (future phases), or "blank". The field can be used for Order Entry mode in case of Outgoing CTR payments. If the operator wants to impose the tag option 50F or 50K he can do so by setting this field. The data inputted by the operator will then take precedence over the account details from the ledger. |
| 25 | `PP.AUTR.DebitAccountNumber` | `PpAuthRepair_Debitaccountnumber` | TField |  | Indicates the Account Number of the Debit Party Accepts value as defined in ACCOUNT table. |
| 26 | `PP.AUTR.DebitAccountNumberBIC` | `PpAuthRepair_Debitaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Debit Party. |
| 27 | `PP.AUTR.DebitAccountNumberImposedFlag` | `PpAuthRepair_Debitaccountnumberimposedflag` | TField |  | When imposed the corresponding Debit Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 28 | `PP.AUTR.DebitAccountCurrency` | `PpAuthRepair_Debitaccountcurrency` | TField |  | Indicates the Currency Code of the Debit Party. Accepts valid value as defined in the PPT.CURRENCY table. |
| 29 | `PP.AUTR.DebitAmount` | `PpAuthRepair_Debitamount` | TField |  | Indicates the Debit amount which is to be debited from sender. Calculated based on transaction amount involving any FX if applicable. |
| 30 | `PP.AUTR.DebitExchangeRate` | `PpAuthRepair_Debitexchangerate` | TField |  | The exchange rate that is used to convert the debit amount into the transaction amount (or transaction amount into debit amount) in case the debit account currency is different from the transaction currency. |
| 31 | `PP.AUTR.DebitExchangeRateImposedFlag` | `PpAuthRepair_Debitexchangerateimposedflag` | TField |  | If debit exchange rate is imposed by the operator and the entered value will not be overridden by the payment engine. Check Box Field. |
| 32 | `PP.AUTR.DebitExchangeRateReference` | `PpAuthRepair_Debitexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of a foreign currency by the dealer. This is only for transactions that exceed the threshold. The payment operator contacts treasury for a deal. |
| 33 | `PP.AUTR.DebitValueDate` | `PpAuthRepair_Debitvaluedate` | TField |  | Indicates the date on which the actual debit will happen. If left empty, Payment Engine will calculate this date based on Processing Date |
| 34 | `PP.AUTR.DebitValueDateImposedFlag` | `PpAuthRepair_Debitvaluedateimposedflag` | TField |  | This field specifies whether the debit value date is imposed or can still be overwritten by the date component. In case the impose flag is lacking but the debit value date is specified, the manual input is more a suggestion towards the system. In case the impose flag is present and the debit value date is specified, the manual input is a hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. Possible values: "Y" " " |
| 35 | `PP.AUTR.OrderingAccount` | `PpAuthRepair_Orderingaccount` | TField |  | National Clearing Code or Account Number of the Ordering Party can be entered. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 36 | `PP.AUTR.OrderingName` | `PpAuthRepair_Orderingname` | TField |  | Free Text Field. Free Text Field, wherein Additional Address details(Usually Name) of the Ordering Party can be entered. |
| 37 | `PP.AUTR.OrderingAddress1` | `PpAuthRepair_Orderingaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 38 | `PP.AUTR.OrderingAddress2` | `PpAuthRepair_Orderingaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 39 | `PP.AUTR.OrderingAddress3` | `PpAuthRepair_Orderingaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 40 | `PP.AUTR.OrderingCountry` | `PpAuthRepair_Orderingcountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from PPT.COUNTRYIBANSTRUCTURE. Drop Down Field. |
| 41 | `PP.AUTR.VATDebitMainAmountIndicator` | `PpAuthRepair_Vatdebitmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Main Amount % (VATDebitMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 42 | `PP.AUTR.VATDebitMainAmountPercentage` | `PpAuthRepair_Vatdebitmainamountpercentage` | TField |  | Indicates the percentage on Debit Main Amount. |
| 43 | `PP.AUTR.CreditAccountCompany` | `PpAuthRepair_Creditaccountcompany` | TField |  | Indicates the Company ID of the Credit Party. Accepts valid value as defined in the PPT.COMPANY table. |
| 44 | `PP.AUTR.CreditAccountNumber` | `PpAuthRepair_Creditaccountnumber` | TField |  | Indicates the Account Number of the Credit Party Accepts value as defined in ACCOUNT table. |
| 45 | `PP.AUTR.CreditAccountNumberBIC` | `PpAuthRepair_Creditaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Credit Party. |
| 46 | `PP.AUTR.CreditAccountNumberImposedFlag` | `PpAuthRepair_Creditaccountnumberimposedflag` | TField |  | When imposed the corresponding Credit Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 47 | `PP.AUTR.CreditAccountCurrency` | `PpAuthRepair_Creditaccountcurrency` | TField |  | Indicates the Currency Code of the Credit Party. Accepts valid value as defined in the PPT.CURRENCY table. |
| 48 | `PP.AUTR.CreditAmount` | `PpAuthRepair_Creditamount` | TField |  | Indicates the credit amount which is to be credited to the beneficiary. Calculated based on transaction amount involving any FX if present. |
| 49 | `PP.AUTR.CreditExchangeRate` | `PpAuthRepair_Creditexchangerate` | TField |  | The exchange rate that is used to convert the credit amount into the transaction amount (or transaction amount into debit amount) in case the credit account currency is different from the transaction currency. |
| 50 | `PP.AUTR.CreditExchangeRateImposedFlag` | `PpAuthRepair_Creditexchangerateimposedflag` | TField |  | If credit exchange rate is imposed by the operator and the entered value will not be overridden by the payment engine. Check Box Field. |
| 51 | `PP.AUTR.CreditExchangeRateReference` | `PpAuthRepair_Creditexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of a foreign currency by the dealer. This is only for transactions that exceed the threshold. The payment operator contacts treasury for a deal. |
| 52 | `PP.AUTR.CreditValueDate` | `PpAuthRepair_Creditvaluedate` | TField |  | Indicates the date on which the actual credit will happen. If left empty, Payment Engine will calculate this date based on Processing Date. |
| 53 | `PP.AUTR.CreditValueDateImposedFlag` | `PpAuthRepair_Creditvaluedateimposedflag` | TField |  | This field specifies whether the credit value date is imposed or can still be overwritten by the date component. In case the impose flag is lacking but the credit value date is specified, the manual input is more a suggestion towards the system. In case the impose flag is present and the credit value date is specified, the manual input is a hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. |
| 54 | `PP.AUTR.BeneficiaryAccount` | `PpAuthRepair_Beneficiaryaccount` | TField |  | Specifies National Clearing Code or Account Number of the Beneficiary Institution(BENINS for BTR) or Beneficiary(BENFCY for CTR). National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 55 | `PP.AUTR.BeneficiaryName` | `PpAuthRepair_Beneficiaryname` | TField |  | Free Text Field, wherein Additional Address details(Usually Name) of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Free Text Field. |
| 56 | `PP.AUTR.BeneficiaryAddress1` | `PpAuthRepair_Beneficiaryaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 57 | `PP.AUTR.BeneficiaryAddress2` | `PpAuthRepair_Beneficiaryaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 58 | `PP.AUTR.BeneficiaryAddress3` | `PpAuthRepair_Beneficiaryaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 59 | `PP.AUTR.BeneficiaryCountry` | `PpAuthRepair_Beneficiarycountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from CountryIBANStructure table. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Drop Down Field. |
| 60 | `PP.AUTR.VATCreditMainAmountIndicator` | `PpAuthRepair_Vatcreditmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Main Amount % (VATCreditMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 61 | `PP.AUTR.VATCreditMainAmountPercentage` | `PpAuthRepair_Vatcreditmainamountpercentage` | TField |  | Indicates the percentage on Credit Main Amount. |
| 62 | `PP.AUTR.WaiveDebitCharges` | `PpAuthRepair_Waivedebitcharges` | TField |  | Indicates whether the debit side charges/fees can be skipped/waived or not. Check Box Field. |
| 63 | `PP.AUTR.DebitChargeAccountCompany` | `PpAuthRepair_Debitchargeaccountcompany` | TField |  | Indicates the company code where the debit charge account is maintained. Drop Down Field. |
| 64 | `PP.AUTR.DebitChargeAccount` | `PpAuthRepair_Debitchargeaccount` | TField |  | Indicates the account number to where the charges will be debited. |
| 65 | `PP.AUTR.DebitChargeAccountImposeFlag` | `PpAuthRepair_Debitchargeaccountimposeflag` | TField |  | When imposed the corresponding Debit Charge Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 66 | `PP.AUTR.DebitChargeAccountCurrency` | `PpAuthRepair_Debitchargeaccountcurrency` | TField |  | Indicates the currency code of the debit charge account. Drop Down Field. |
| 67 | `PP.AUTR.DebitChargeImposedFlag` | `PpAuthRepair_Debitchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee component that the default charges are not to be calculated. Check Box Field. |
| 68 | `PP.AUTR.DebitChargeComponent` | `PpAuthRepair_Debitchargecomponent` |  |  |  |
| 69 | `PP.AUTR.DebitChargeCurrency` | `PpAuthRepair_Debitchargecurrency` |  |  |  |
| 70 | `PP.AUTR.DebitChargeAmount` | `PpAuthRepair_Debitchargeamount` |  |  |  |
| 71 | `PP.AUTR.DebitReceiverCharge` | `PpAuthRepair_Debitreceivercharge` | TField |  | Outgoing OUR charge amount which can be used by posting and also swift component to determine the outgoing 71G mapping. |
| 72 | `PP.AUTR.DebitReceiverChargeImposedFlag` | `PpAuthRepair_Debitreceiverchargeimposedflag` | TField |  | If imposed the operator entered value in the Outgoing Receiver Charge (DebitReceiverCharge) field will not be overridden by the payment engine. Check Box Field. |
| 73 | `PP.AUTR.VATDebitMainChargeIndicator` | `PpAuthRepair_Vatdebitmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Charge Amount % (VATDebitMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 74 | `PP.AUTR.VATDebitMainChargePercentage` | `PpAuthRepair_Vatdebitmainchargepercentage` | TField |  | Indicates the percentage of VAT which needs to be calculated over the debit charge amount of the transaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specified percentage will override the percentage present in the client conditions component. |
| 75 | `PP.AUTR.WaiveCreditCharges` | `PpAuthRepair_Waivecreditcharges` | TField |  | Indicates whether the credit side charges/fees can be skipped/waived or not. Check Box Field. |
| 76 | `PP.AUTR.CreditChargeAccountCompany` | `PpAuthRepair_Creditchargeaccountcompany` | TField |  | Indicates the company code where the charge account is maintained. Drop Down Field. |
| 77 | `PP.AUTR.CreditChargeAccount` | `PpAuthRepair_Creditchargeaccount` | TField |  | Indicates the account number, to where the charges will be credited |
| 78 | `PP.AUTR.CreditChargeAccountImposeFlag` | `PpAuthRepair_Creditchargeaccountimposeflag` | TField |  | When imposed the corresponding Credit Charge Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 79 | `PP.AUTR.CreditChargeAccountCurrency` | `PpAuthRepair_Creditchargeaccountcurrency` | TField |  | Indicates the currency code of the charge account. Drop Down Field. |
| 80 | `PP.AUTR.CreditChargeImposedFlag` | `PpAuthRepair_Creditchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee component that the default charges are not to be calculated. Check Box Field. |
| 81 | `PP.AUTR.CreditChargeComponent` | `PpAuthRepair_Creditchargecomponent` |  |  |  |
| 82 | `PP.AUTR.CreditChargeCurrency` | `PpAuthRepair_Creditchargecurrency` |  |  |  |
| 83 | `PP.AUTR.CreditChargeAmount` | `PpAuthRepair_Creditchargeamount` |  |  |  |
| 84 | `PP.AUTR.CreditReceiverCharge` | `PpAuthRepair_Creditreceivercharge` | TField |  | Incoming our Charge amount. |
| 85 | `PP.AUTR.VATCreditMainChargeIndicator` | `PpAuthRepair_Vatcreditmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Charge Amount % (VATCreditMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 86 | `PP.AUTR.VATCreditMainChargePercentage` | `PpAuthRepair_Vatcreditmainchargepercentage` | TField |  | This field specifies the percentage of VAT which needs to be calculated over the credit charge amount of the transaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specified percentage will override the percentage present in the client conditions component. |
| 87 | `PP.AUTR.OrderingInstAccount` | `PpAuthRepair_Orderinginstaccount` | TField |  | National Clearing Code or Account Number of the Ordering Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 88 | `PP.AUTR.OrderingInstIdentifierCode` | `PpAuthRepair_Orderinginstidentifiercode` | TField |  | Bank Identification Code of the Ordering Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 89 | `PP.AUTR.OrderingInstAddress` | `PpAuthRepair_Orderinginstaddress` |  |  |  |
| 90 | `PP.AUTR.SendersCorresAccount` | `PpAuthRepair_Senderscorresaccount` | TField |  | National Clearing Code or Account Number of the Sender Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 91 | `PP.AUTR.SendersCorresIdentifierCode` | `PpAuthRepair_Senderscorresidentifiercode` | TField |  | Bank Identification Code of the Sender Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 92 | `PP.AUTR.SendersCorresAddress` | `PpAuthRepair_Senderscorresaddress` |  |  |  |
| 93 | `PP.AUTR.ReceiversCorresAccount` | `PpAuthRepair_Receiverscorresaccount` | TField |  | National Clearing Code or Account Number of the Receiver Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 94 | `PP.AUTR.ReceiversCorresIdentifierCode` | `PpAuthRepair_Receiverscorresidentifiercode` | TField |  | Bank Identification Code of the Receiver Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 95 | `PP.AUTR.ReceiversCorresAddress` | `PpAuthRepair_Receiverscorresaddress` |  |  |  |
| 96 | `PP.AUTR.ThirdReimburseInstAccount` | `PpAuthRepair_Thirdreimburseinstaccount` | TField |  | National Clearing Code or Account Number of the Third Reimbursement Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 97 | `PP.AUTR.ThirdReimburseInstIdentifierCd` | `PpAuthRepair_Thirdreimburseinstidentifiercd` | TField |  | Bank Identification Code of the Third Reimbursement Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 98 | `PP.AUTR.ThirdReimburseInstAddress` | `PpAuthRepair_Thirdreimburseinstaddress` |  |  |  |
| 99 | `PP.AUTR.IntermediaryInstAccount` | `PpAuthRepair_Intermediaryinstaccount` | TField |  | National Clearing Code or Account Number of the Intermediary Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 100 | `PP.AUTR.IntermediaryInstIdentifierCode` | `PpAuthRepair_Intermediaryinstidentifiercode` | TField |  | Bank Identification Code of the Intermediary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 101 | `PP.AUTR.IntermediaryInstAddress` | `PpAuthRepair_Intermediaryinstaddress` |  |  |  |
| 102 | `PP.AUTR.AccountWithInstAccount` | `PpAuthRepair_Accountwithinstaccount` | TField |  | Specifies the National Clearing Code or Account Number of the Account with Institution. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. Account with Institution Tag 57 A, B, C or D {ACWINS} |
| 103 | `PP.AUTR.AccountWithInstIdentifierCode` | `PpAuthRepair_Accountwithinstidentifiercode` | TField |  | Specifies the Bank Identification Code of the Account with Institution. Account with Institution Tag 57 A, B, C or D {ACWINS} Validation Rules: Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 104 | `PP.AUTR.AccountWithInstAddress` | `PpAuthRepair_Accountwithinstaddress` |  |  |  |
| 105 | `PP.AUTR.InstructionCode` | `PpAuthRepair_Instructioncode` |  |  |  |
| 106 | `PP.AUTR.PaymentDetails` | `PpAuthRepair_Paymentdetails` |  |  |  |
| 107 | `PP.AUTR.AdditionalText` | `PpAuthRepair_Additionaltext` | TField |  | Free Text Field wherein the operator can specify additional information relating to the payment instruction. |
| 108 | `PP.AUTR.AuditTrail` | `PpAuthRepair_Audittrail` | TField |  | Used for internal purpose. Context Enquiry attached to this field will launch the Audit Trail Details (POR.HISTORYLOG) of the corresponding payment in a separate screen. |
| 109 | `PP.AUTR.Information` | `PpAuthRepair_Information` |  |  |  |
| 110 | `PP.AUTR.AcceptWarning` | `PpAuthRepair_Acceptwarning` | TField | Yes | Whenever an Warning Type of error is encountered by the payment, the operator must accept the warning (Mandatory) to proceed with further payment processing. Check Box Field. |
| 111 | `PP.AUTR.Warning` | `PpAuthRepair_Warning` |  |  |  |
| 112 | `PP.AUTR.FunctionalError` | `PpAuthRepair_Functionalerror` |  |  |  |
| 113 | `PP.AUTR.FatalError` | `PpAuthRepair_Fatalerror` | TField |  | Highlights the text "Error Information Present" on the main screen, if there are any errors present in Error Information Tab. No Input Field. |
| 114 | `PP.AUTR.ValidationFlag` | `PpAuthRepair_Validationflag` | TField |  | Validation Flag (field 119) from "User Header Block" (Block 3). Triggers diffent type of validations for MT messages in the payments hub. Example: Duplicate check processing uses this field to identify 202COV payments. Validation Rules: 8 alphanumeric characters. No Input. |
| 115 | `PP.AUTR.BalanceReservation` | `PpAuthRepair_Balancereservation` | TField |  | This field gives the status of Balance Check for a payment. Possible values: A - Approved P - Pending R - Rejected S - Skipped. Balance check not required for the payment. E - Error Received from Balance Check Interface Validation Rules: 1 alphanumeric character. No Input. |
| 116 | `PP.AUTR.BalanceReservationNumber` | `PpAuthRepair_Balancereservationnumber` | TField |  | Indicates the unique reservation reference number which is returned by T24 when funds are reserved as part of balance check component. This may not be present if account being debited is a nostro account. Format ACFAjjjjjxxxxxxx. Validation Rules: 16 alphanumeric characters. No Input. |
| 117 | `PP.AUTR.ProcessingDateImposedFlag` | `PpAuthRepair_Processingdateimposedflag` | TField |  | If imposed the corresponding Processing date entered by the operator is not overridden by the payment engine. Check Box Field. |
| 118 | `PP.AUTR.DebitRepairFee` | `PpAuthRepair_Debitrepairfee` | TField |  | Specifies the fee to be charged from the customer for debit side repair operations. Validation Rules: No Input. |
| 119 | `PP.AUTR.CreditRepairFee` | `PpAuthRepair_Creditrepairfee` | TField |  | Specifies the fee to be charged from the customer for credit side repair operations. Validation Rules: No Input. |
| 120 | `PP.AUTR.Action` | `PpAuthRepair_Action` | TField |  | Used for internal purpose. This field can hold upto 1 alphanumeric character and the value is not editable by the user. Possible Values will be G, V, S, C, R and A |
| 121 | `PP.AUTR.CancelDescription` | `PpAuthRepair_Canceldescription` | TField |  | Describes the reason for cancellation of a payment. Operator uses this field to let authoriser know the justification for such an action. Free Text Field. |
| 122 | `PP.AUTR.RejectDescription` | `PpAuthRepair_Rejectdescription` | TField |  | Free Text Field, wherein the operator can specify the reason for rejecting the payment. |
| 123 | `PP.AUTR.DebitInstruction` | `PpAuthRepair_Debitinstruction` | TField |  | Enriches value from POR.DEBITBANKCONDITIONS table after the payment is validated. Contains any credit instructions if present for a bank, which will be useful for the operator how to process the payment. No Input Field. |
| 124 | `PP.AUTR.CreditInstruction` | `PpAuthRepair_Creditinstruction` | TField |  | Enriches value from POR.DEBITBANKCONDITIONS after the payment is validated. Contains any credit instructions if present for a bank, which will be useful for the operator how to process the payment. No input field. |
| 125 | `PP.AUTR.ShowOriginalRoutingInfo` | `PpAuthRepair_Showoriginalroutinginfo` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 126 | `PP.AUTR.OrderingIdentifierCode` | `PpAuthRepair_Orderingidentifiercode` | TField |  | Bank Identification Code of the Ordering Party can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 127 | `PP.AUTR.BeneficiaryIdentifierCode` | `PpAuthRepair_Beneficiaryidentifiercode` | TField |  | Bank Identification Code of the Beneficiary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 128 | `PP.AUTR.DebitTreasuryRate` | `PpAuthRepair_Debittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. The Final exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of the appropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 129 | `PP.AUTR.DebitTreasuryRateImposedFlag` | `PpAuthRepair_Debittreasuryrateimposedflag` | TField |  | If Debit Treasury Rate is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 130 | `PP.AUTR.DebitCustomerSpread` | `PpAuthRepair_Debitcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generate the final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 131 | `PP.AUTR.DebitCustSpreadImposedFlag` | `PpAuthRepair_Debitcustspreadimposedflag` | TField |  | If Debit Customer Spread is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 132 | `PP.AUTR.CreditTreasuryRate` | `PpAuthRepair_Credittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. The Final exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of the appropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 133 | `PP.AUTR.CreditTreasuryRateImposedFlag` | `PpAuthRepair_Credittreasuryrateimposedflag` | TField |  | If Credit Treasury Rate is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 134 | `PP.AUTR.CreditCustomerSpread` | `PpAuthRepair_Creditcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generate the final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 135 | `PP.AUTR.CreditCustSpreadImposedFlag` | `PpAuthRepair_Creditcustspreadimposedflag` | TField |  | If Credit Customer Spread is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 136 | `PP.AUTR.FieldPrompt` | `PpAuthRepair_Fieldprompt` |  |  |  |
| 137 | `PP.AUTR.OldValue` | `PpAuthRepair_Oldvalue` |  |  |  |
| 138 | `PP.AUTR.NewValue` | `PpAuthRepair_Newvalue` |  |  |  |
| 139 | `PP.AUTR.IntraCompanyPayment` | `PpAuthRepair_Intracompanypayment` | TField |  |  |
| 140 | `PP.AUTR.SelectTemplate` | `PpAuthRepair_Selecttemplate` | TField |  |  |
| 141 | `PP.AUTR.SaveAsTemplate` | `PpAuthRepair_Saveastemplate` | TField |  |  |
| 142 | `PP.AUTR.NickName` | `PpAuthRepair_Nickname` | TField |  |  |
| 143 | `PP.AUTR.StoreTemplateValues` | `PpAuthRepair_Storetemplatevalues` | TField |  |  |
| 144 | `PP.AUTR.ReturnPayment` | `PpAuthRepair_Returnpayment` | TField |  | This flag will be set to "Y" or "N" . Check Box Field. |
| 145 | `PP.AUTR.ReturnCode` | `PpAuthRepair_Returncode` | TField |  | Return Code. Validation Rules: 2 alphanumeric characters. No Input. |
| 146 | `PP.AUTR.ReturnDescription` | `PpAuthRepair_Returndescription` | TField |  | Free Text Field. Validation Rules: 256 alphanumeric characters. No Input. |
| 147 | `PP.AUTR.UltDbtNm` | `PpAuthRepair_Ultdbtnm` | TField |  |  |
| 148 | `PP.AUTR.UltDbtBIC` | `PpAuthRepair_Ultdbtbic` | TField |  |  |
| 149 | `PP.AUTR.UltDbtOrgIdOthId` | `PpAuthRepair_Ultdbtorgidothid` | TField |  |  |
| 150 | `PP.AUTR.UltDbtOrgIdOthSchCd` | `PpAuthRepair_Ultdbtorgidothschcd` | TField |  |  |
| 151 | `PP.AUTR.UltDbtOrgIdOthSchProp` | `PpAuthRepair_Ultdbtorgidothschprop` | TField |  |  |
| 152 | `PP.AUTR.UltDbtOrgIdOthIssuer` | `PpAuthRepair_Ultdbtorgidothissuer` | TField |  |  |
| 153 | `PP.AUTR.UltDbtBrDt` | `PpAuthRepair_Ultdbtbrdt` | TField |  |  |
| 154 | `PP.AUTR.UltDbtPvOfBr` | `PpAuthRepair_Ultdbtpvofbr` | TField |  |  |
| 155 | `PP.AUTR.UltDbtCityOfBr` | `PpAuthRepair_Ultdbtcityofbr` | TField |  |  |
| 156 | `PP.AUTR.UltDbtCtryOfBr` | `PpAuthRepair_Ultdbtctryofbr` | TField |  |  |
| 157 | `PP.AUTR.UltDbtPrvIdOthId` | `PpAuthRepair_Ultdbtprvidothid` | TField |  |  |
| 158 | `PP.AUTR.UltDbtPrvIdOthSchCd` | `PpAuthRepair_Ultdbtprvidothschcd` | TField |  |  |
| 159 | `PP.AUTR.UltDbtPrvIdOthSchProp` | `PpAuthRepair_Ultdbtprvidothschprop` | TField |  |  |
| 160 | `PP.AUTR.UltDbtPrvIdOthIssuer` | `PpAuthRepair_Ultdbtprvidothissuer` | TField |  |  |
| 161 | `PP.AUTR.DbtOrgIdOthId` | `PpAuthRepair_Dbtorgidothid` | TField |  |  |
| 162 | `PP.AUTR.DbtOrgIdOthSchCd` | `PpAuthRepair_Dbtorgidothschcd` | TField |  |  |
| 163 | `PP.AUTR.DbtOrgIdOthSchProp` | `PpAuthRepair_Dbtorgidothschprop` | TField |  |  |
| 164 | `PP.AUTR.DbtOrgIdOthIssuer` | `PpAuthRepair_Dbtorgidothissuer` | TField |  |  |
| 165 | `PP.AUTR.DbtBrDt` | `PpAuthRepair_Dbtbrdt` | TField |  |  |
| 166 | `PP.AUTR.DbtPvOfBr` | `PpAuthRepair_Dbtpvofbr` | TField |  |  |
| 167 | `PP.AUTR.DbtCityOfBr` | `PpAuthRepair_Dbtcityofbr` | TField |  |  |
| 168 | `PP.AUTR.DbtCtryOfBr` | `PpAuthRepair_Dbtctryofbr` | TField |  |  |
| 169 | `PP.AUTR.DbtPrvIdOthId` | `PpAuthRepair_Dbtprvidothid` | TField |  |  |
| 170 | `PP.AUTR.DbtPrvIdOthSchCd` | `PpAuthRepair_Dbtprvidothschcd` | TField |  |  |
| 171 | `PP.AUTR.DbtPrvIdOthSchProp` | `PpAuthRepair_Dbtprvidothschprop` | TField |  |  |
| 172 | `PP.AUTR.DbtPrvIdOthIssuer` | `PpAuthRepair_Dbtprvidothissuer` | TField |  |  |
| 173 | `PP.AUTR.CrdOrgIdOthId` | `PpAuthRepair_Crdorgidothid` | TField |  |  |
| 174 | `PP.AUTR.CrdOrgIdOthSchCd` | `PpAuthRepair_Crdorgidothschcd` | TField |  |  |
| 175 | `PP.AUTR.CrdOrgIdOthSchProp` | `PpAuthRepair_Crdorgidothschprop` | TField |  |  |
| 176 | `PP.AUTR.CrdOrgIdOthIssuer` | `PpAuthRepair_Crdorgidothissuer` | TField |  |  |
| 177 | `PP.AUTR.CrdBrDt` | `PpAuthRepair_Crdbrdt` | TField |  |  |
| 178 | `PP.AUTR.CrdPvOfBr` | `PpAuthRepair_Crdpvofbr` | TField |  |  |
| 179 | `PP.AUTR.CrdCityOfBr` | `PpAuthRepair_Crdcityofbr` | TField |  |  |
| 180 | `PP.AUTR.CrdCtryOfBr` | `PpAuthRepair_Crdctryofbr` | TField |  |  |
| 181 | `PP.AUTR.CrdPrvIdOthId` | `PpAuthRepair_Crdprvidothid` | TField |  |  |
| 182 | `PP.AUTR.CrdPrvIdOthSchCd` | `PpAuthRepair_Crdprvidothschcd` | TField |  |  |
| 183 | `PP.AUTR.CrdPrvIdOthSchProp` | `PpAuthRepair_Crdprvidothschprop` | TField |  |  |
| 184 | `PP.AUTR.CrdPrvIdOthIssuer` | `PpAuthRepair_Crdprvidothissuer` | TField |  |  |
| 185 | `PP.AUTR.UltCrdNm` | `PpAuthRepair_Ultcrdnm` | TField |  |  |
| 186 | `PP.AUTR.UltCrdBIC` | `PpAuthRepair_Ultcrdbic` | TField |  |  |
| 187 | `PP.AUTR.UltCrdOrgIdOthId` | `PpAuthRepair_Ultcrdorgidothid` | TField |  |  |
| 188 | `PP.AUTR.UltCrdOrgIdOthSchCd` | `PpAuthRepair_Ultcrdorgidothschcd` | TField |  |  |
| 189 | `PP.AUTR.UltCrdOrgIdOthSchProp` | `PpAuthRepair_Ultcrdorgidothschprop` | TField |  |  |
| 190 | `PP.AUTR.UltCrdOrgIdOthIssuer` | `PpAuthRepair_Ultcrdorgidothissuer` | TField |  |  |
| 191 | `PP.AUTR.UltCrdBrDt` | `PpAuthRepair_Ultcrdbrdt` | TField |  |  |
| 192 | `PP.AUTR.UltCrdPvOfBr` | `PpAuthRepair_Ultcrdpvofbr` | TField |  |  |
| 193 | `PP.AUTR.UltCrdCityOfBr` | `PpAuthRepair_Ultcrdcityofbr` | TField |  |  |
| 194 | `PP.AUTR.UltCrdCtryOfBr` | `PpAuthRepair_Ultcrdctryofbr` | TField |  |  |
| 195 | `PP.AUTR.UltCrdPrvIdOthId` | `PpAuthRepair_Ultcrdprvidothid` | TField |  |  |
| 196 | `PP.AUTR.UltCrdPrvIdOthSchCd` | `PpAuthRepair_Ultcrdprvidothschcd` | TField |  |  |
| 197 | `PP.AUTR.UltCrdPrvIdOthSchProp` | `PpAuthRepair_Ultcrdprvidothschprop` | TField |  |  |
| 198 | `PP.AUTR.UltCrdPrvIdOthIssuer` | `PpAuthRepair_Ultcrdprvidothissuer` | TField |  |  |
| 199 | `PP.AUTR.CrdRefInfTpCd` | `PpAuthRepair_Crdrefinftpcd` |  |  |  |
| 200 | `PP.AUTR.CrdRefInfTpIssuer` | `PpAuthRepair_Crdrefinftpissuer` |  |  |  |
| 201 | `PP.AUTR.CrdRefInfRef` | `PpAuthRepair_Crdrefinfref` |  |  |  |
| 202 | `PP.AUTR.CatPurpCd` | `PpAuthRepair_Catpurpcd` |  |  |  |
| 203 | `PP.AUTR.CatPurpProp` | `PpAuthRepair_Catpurpprop` |  |  |  |
| 204 | `PP.AUTR.TrxPurpCd` | `PpAuthRepair_Trxpurpcd` |  |  |  |
| 205 | `PP.AUTR.ExtendedFields` | `PpAuthRepair_Extendedfields` | TField |  |  |
| 206 | `PP.AUTR.MndtId` | `PpAuthRepair_Mndtid` | TField |  | Indicates the unique mandate identification. The value of this field is updated to the field "MandateReference" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. |
| 207 | `PP.AUTR.MndtDtOfSgn` | `PpAuthRepair_Mndtdtofsgn` | TField |  | Indicates the date of signature of the mandate. The value of this field is updated to the field "SignatureDate" in POR.DEBITAUTHINFO table. Validation Rules: 11 characters of type Date. |
| 208 | `PP.AUTR.MndtAmdtInd` | `PpAuthRepair_Mndtamdtind` | TField |  | Indicates the Amendment indicator of the mandate. The value of this field is updated to the field "AmendmentIndicator" in POR.DEBITAUTHINFO table. Possible values: 'N' - this means that none of the fields should be filled. 'Y' - this means that at least one of the fields should be filled. Note: The mentioned fields here are: OriginalMandateReference, OriginalCreditorName, OriginalCreditorId, OriginalCreditorSchProp, OriginalDebtorAccount, OriginalDebtorAgtOtherID Default value is "N". Validation Rules: 1 alphabetic characters. |
| 209 | `PP.AUTR.MndtOrglMndtId` | `PpAuthRepair_Mndtorglmndtid` | TField | Yes | Indicates the Reference of the original MandateID as received in Incoming Direct Debit message. The value of this field is updated to the field "OriginalMandateReference" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Mandatory only if OriginalMandateReference is different from MandateReference. |
| 210 | `PP.AUTR.MndtOrglCrdSchNm` | `PpAuthRepair_Mndtorglcrdschnm` | TField |  | Indicates the original name of the Creditor who issued the mandate. The value of this field is updated to the field "OriginalCreditorName" in POR.DEBITAUTHINFO table. Validation Rules: 70 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 211 | `PP.AUTR.MndtOrglCrdSchPrvOthId` | `PpAuthRepair_Mndtorglcrdschprvothid` | TField |  | Indicates the Original Creditor ID as it is mapped from Incoming Direct Debit message. The value of this field is updated to the field "OriginalCreditorID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 212 | `PP.AUTR.MndtOrglCrdSchPrvOthSchNmProp` | `PpAuthRepair_Mndtorglcrdschprvothschnmprop` | TField |  | Indicates the scheme name of the original Creditor. The value of this field is updated to the field "OriginalCreditorSchProp" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Only "SEPA" value is allowed. |
| 213 | `PP.AUTR.MndtOrglDbtAccIdIBAN` | `PpAuthRepair_Mndtorgldbtaccidiban` | TField |  |  |
| 214 | `PP.AUTR.MndtOrglDbtAgFinInstIdBIC` | `PpAuthRepair_Mndtorgldbtagfininstidbic` | TField |  | Indicates the Original Debtor Agent Financial Institution Identification BIC. The value of this field is updated to the field "OriginalDebtorAgtBIC" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 215 | `PP.AUTR.MndtElectronicSgn` | `PpAuthRepair_Mndtelectronicsgn` | TField |  | Indicates the placeholder of Electronic Signature of the Mandate provided in the incoming Direct Debit. This data element is not to be used if the mandate is a paper mandate. The value of this field is updated to the field "ElectronicSignature" in POR.DEBITAUTHINFO table. Validation Rules: 1025 alphabetic characters. |
| 216 | `PP.AUTR.CrdSchIdPrvIdOthId` | `PpAuthRepair_Crdschidprvidothid` | TField |  | Indicates the creditor business code. The value of this field is updated to the field "CreditorID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It cannot contains spaces. |
| 217 | `PP.AUTR.MndtOrglDbtAccIdOthId` | `PpAuthRepair_Mndtorgldbtaccidothid` | TField |  | Indicates the Original Debtor Account Identifier. Use account other identification with code 'SMNDA' to indicate same mandate with new Debtor Account or in case of an account change within same bank. The value of this field is updated to the field "OriginalDebtorAcctOtherID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Only "SMNDA" value is allowed. |
| 218 | `PP.AUTR.BalanceReservationKeyForChgAct` | `PpAuthRepair_Balancereservationkeyforchgact` | TField |  | Holds the reservation key of the debit charge account. |
| 219 | `PP.AUTR.RequestedCollectionDate` | `PpAuthRepair_Requestedcollectiondate` | TField |  |  |
| 220 | `PP.AUTR.Scheme` | `PpAuthRepair_Scheme` | TField |  |  |
| 221 | `PP.AUTR.ClearingTransactionType` | `PpAuthRepair_Clearingtransactiontype` | TField |  |  |
| 222 | `PP.AUTR.InstructedCurrency` | `PpAuthRepair_Instructedcurrency` | TField | Yes | Indicates the Instructed currency in which the payment to be processed. Will hold valid currency code values from PPT.CURRENCY table. Drop Down Field. Validation Rules: Mandatory when InstructedAmount is present. |
| 223 | `PP.AUTR.InstructedAmount` | `PpAuthRepair_Instructedamount` | TField | Yes | Indicates the Instructed amount for which the payment needs to be processed. Validation Rules: Mandatory when InstructedCurrency is present. |
| 224 | `PP.AUTR.RESERVED.28` | `PpAuthRepair_Reserved28` | TField |  |  |
| 225 | `PP.AUTR.RESERVED.27` | `PpAuthRepair_Reserved27` | TField |  |  |
| 226 | `PP.AUTR.RESERVED.26` | `PpAuthRepair_Reserved26` | TField |  |  |
| 227 | `PP.AUTR.RESERVED.25` | `PpAuthRepair_Reserved25` | TField |  |  |
| 228 | `PP.AUTR.RESERVED.24` | `PpAuthRepair_Reserved24` | TField |  |  |
| 229 | `PP.AUTR.RESERVED.23` | `PpAuthRepair_Reserved23` | TField |  |  |
| 230 | `PP.AUTR.RESERVED.22` | `PpAuthRepair_Reserved22` | TField |  |  |
| 231 | `PP.AUTR.RESERVED.21` | `PpAuthRepair_Reserved21` | TField |  |  |
| 232 | `PP.AUTR.RESERVED.20` | `PpAuthRepair_Reserved20` | TField |  |  |
| 233 | `PP.AUTR.RESERVED.19` | `PpAuthRepair_Reserved19` | TField |  |  |
| 234 | `PP.AUTR.RESERVED.18` | `PpAuthRepair_Reserved18` | TField |  |  |
| 235 | `PP.AUTR.RESERVED.17` | `PpAuthRepair_Reserved17` | TField |  |  |
| 236 | `PP.AUTR.RESERVED.16` | `PpAuthRepair_Reserved16` | TField |  |  |
| 237 | `PP.AUTR.RESERVED.15` | `PpAuthRepair_Reserved15` | TField |  |  |
| 238 | `PP.AUTR.RESERVED.14` | `PpAuthRepair_Reserved14` | TField |  |  |
| 239 | `PP.AUTR.RESERVED.13` | `PpAuthRepair_Reserved13` | TField |  |  |
| 240 | `PP.AUTR.RESERVED.12` | `PpAuthRepair_Reserved12` | TField |  |  |
| 241 | `PP.AUTR.RESERVED.11` | `PpAuthRepair_Reserved11` | TField |  |  |
| 242 | `PP.AUTR.RESERVED.10` | `PpAuthRepair_Reserved10` | TField |  |  |
| 243 | `PP.AUTR.RESERVED.9` | `PpAuthRepair_Reserved9` | TField |  |  |
| 244 | `PP.AUTR.RESERVED.8` | `PpAuthRepair_Reserved8` | TField |  |  |
| 245 | `PP.AUTR.RESERVED.7` | `PpAuthRepair_Reserved7` | TField |  |  |
| 246 | `PP.AUTR.RESERVED.6` | `PpAuthRepair_Reserved6` | TField |  |  |
| 247 | `PP.AUTR.RESERVED.5` | `PpAuthRepair_Reserved5` | TField |  |  |
| 248 | `PP.AUTR.RESERVED.4` | `PpAuthRepair_Reserved4` | TField |  |  |
| 249 | `PP.AUTR.RESERVED.3` | `PpAuthRepair_Reserved3` | TField |  |  |
| 250 | `PP.AUTR.RESERVED.2` | `PpAuthRepair_Reserved2` | TField |  |  |
| 251 | `PP.AUTR.RESERVED.1` | `PpAuthRepair_Reserved1` | TField |  |  |
| 252 | `PP.AUTR.LOCAL.REF` | `PpAuthRepair_LocalRef` |  |  |  |
| 253 | `PP.AUTR.OVERRIDE` | `PpAuthRepair_Override` |  |  |  |
| 254 | `PP.AUTR.RECORD.STATUS` | `PpAuthRepair_RecordStatus` | String |  |  |
| 255 | `PP.AUTR.CURR.NO` | `PpAuthRepair_CurrNo` | String |  |  |
| 256 | `PP.AUTR.INPUTTER` | `PpAuthRepair_Inputter` |  |  |  |
| 257 | `PP.AUTR.DATE.TIME` | `PpAuthRepair_DateTime` |  |  |  |
| 258 | `PP.AUTR.AUTHORISER` | `PpAuthRepair_Authoriser` | String |  |  |
| 259 | `PP.AUTR.CO.CODE` | `PpAuthRepair_CoCode` | String |  |  |
| 260 | `PP.AUTR.DEPT.CODE` | `PpAuthRepair_DeptCode` | String |  |  |
| 261 | `PP.AUTR.AUDITOR.CODE` | `PpAuthRepair_AuditorCode` | String |  |  |
| 262 | `PP.AUTR.AUDIT.DATE.TIME` | `PpAuthRepair_AuditDateTime` | String |  |  |
