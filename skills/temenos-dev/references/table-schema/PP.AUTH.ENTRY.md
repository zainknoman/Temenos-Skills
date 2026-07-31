# PP.AUTH.ENTRY — Table Schema

> Source: `INSERTS/I_F.PP.AUTH.ENTRY` in `PP_OrderEntryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.AUTE.Status` | `PpAuthEntry_Status` | TField |  | Indicates the Status Code (a Numeric number between 0 - 999) of the payment that is currently being processed. For Order Entry, The initial value of Status is 135. (Pending Submit) After successful Submit Action, the Status is changed to 315.(Pending Authorize) After successful First Authorize Action, the Status is changed to 316. After successful Final Authorize Action, the Status is changed to 600. No Input Field. |
| 2 | `PP.AUTE.TransactionReferenceNumber` | `PpAuthEntry_Transactionreferencenumber` | TField |  | Will hold a system generated unique number (FT Number) to identify the payment throughout its processing. Operator upon entering processing company and click the TRN button, the Transaction Reference Number is generated based on Company ID Date and Sequence number. No Input Field. |
| 3 | `PP.AUTE.SendersReferenceNumber` | `PpAuthEntry_Sendersreferencenumber` | TField |  | Tag 20. Free Text Field. No Input Field. |
| 4 | `PP.AUTE.RelatedReference` | `PpAuthEntry_Relatedreference` | TField |  | Free Text Field. Tag 21. No Input Field. |
| 5 | `PP.AUTE.Source` | `PpAuthEntry_Source` | TField |  | Will contain the actual source through which the payment was originated. No Input Field. Defaulted with a value 'OE' for Order Entry. |
| 6 | `PP.AUTE.Direction` | `PpAuthEntry_Direction` | TField |  | Indicates the direction of the payment. Drop Down Field. No Input Field. Possible values: 1. I - Incoming 2. O - Outgoing 3. B - Book transfer 4. R - Redirect (Future Use) |
| 7 | `PP.AUTE.TransferType` | `PpAuthEntry_Transfertype` | TField |  | CTR BTR Indicator Field. Possible Values: 1. "C" for CTR (Customer Transfer) 2. "B" For BTR (Bank Transfer) No Input Field. |
| 8 | `PP.AUTE.IncomingMessageType` | `PpAuthEntry_Incomingmessagetype` | TField |  | Default value is "RFCT" for Order Entry. No Input Field. |
| 9 | `PP.AUTE.PreAuthorizationNumber` | `PpAuthEntry_Preauthorizationnumber` | TField |  | Operator can key in the ID of AC.FUNDS.AUTHORISATION table, if the funds were pre-authorized. (Pre Authorization Key) Free Text Field. No Input Field. |
| 10 | `PP.AUTE.ProcessCompany` | `PpAuthEntry_Processcompany` | TField |  | Indicates the company code of the company where the payment is processed. Possible values are fetched from the the PPT.COMPANY Table. Drop Down Field. No Input Field. |
| 11 | `PP.AUTE.ProcessingDate` | `PpAuthEntry_Processingdate` | TField |  | Indicates the date on which the processing is supposed to happen. Date Field. No Input Field. |
| 12 | `PP.AUTE.Priority` | `PpAuthEntry_Priority` | TField |  | Identifies the Payment Message Priority and based on this value priority code is set in the payment engine. IF MessagePriority is empty or between 1 and 5, then PriorityCode is 'N' IF MessagePriority is between 6 and 9, then PriorityCode is 'U' Possible values: 1 to 9 Drop Down Value. No Input Field. |
| 13 | `PP.AUTE.Product` | `PpAuthEntry_Product` | TField |  | Must contain a valid Clearing ID from PPT.CLEARINGNATURECODE table Free Text Field. No Input Field. |
| 14 | `PP.AUTE.OutputChannel` | `PpAuthEntry_Outputchannel` | TField |  | Indicates the output channel for the payment. Default Possible values: LORO, NOSTRO, LEDGER Validation Rules: Other Possible values Values are populated based on field 'Clearing' in PPT.CLEARINGSETTING Drop Down Field. No Input Field. |
| 15 | `PP.AUTE.OutputChannelImposedFlag` | `PpAuthEntry_Outputchannelimposedflag` | TField |  | If imposed the corresponding channel entered by the operator will not be overridden by the payment engine. Check Box Field. No Input Field. |
| 16 | `PP.AUTE.TransactionCurrency` | `PpAuthEntry_Transactioncurrency` | TField | Yes | Indicates the currency in which the payment is processed. Will hold valid currency code values from PPT.CURRENCY table. Drop Down Field. Mandatory Field. No Input Field. |
| 17 | `PP.AUTE.TransactionAmount` | `PpAuthEntry_Transactionamount` | TField | Yes | Indicates the amount for which the payment needs to be processed. Mandatory Field. No Input Field. |
| 18 | `PP.AUTE.ChargeOption` | `PpAuthEntry_Chargeoption` | TField |  | Contains the Details of Charge (Tag 71 A) Possible Values: 1. "BEN" 2. "SHA" 3. "OUR" Drop Down Field. No Input Field. |
| 19 | `PP.AUTE.SenderInstitutionBIC` | `PpAuthEntry_Senderinstitutionbic` | TField |  | Bank Identification Code of the Sender Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. Free Text Field. No Input Field. |
| 20 | `PP.AUTE.SenderInstitutionNCC` | `PpAuthEntry_Senderinstitutionncc` | TField |  | National Clearing Code of the Sender Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Free Text Field. No Input Field. |
| 21 | `PP.AUTE.ReceiverInstitutionBIC` | `PpAuthEntry_Receiverinstitutionbic` | TField |  | Bank Identification Code of the Receiver Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. Free Text Field. No Input Field. |
| 22 | `PP.AUTE.ReceiverInstitutionNCC` | `PpAuthEntry_Receiverinstitutionncc` | TField |  | National Clearing Code of the Receiver Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODEtable. Free Text Field. No Input Field. |
| 23 | `PP.AUTE.DebitAccountCompany` | `PpAuthEntry_Debitaccountcompany` | TField |  | Indicates the Company ID of the Debit Party. Accepts valid value as defined in the PPT.COMPANY table. No Input Field. |
| 24 | `PP.AUTE.OrderPartyTagOption` | `PpAuthEntry_Orderpartytagoption` | TField |  | The field can contain the following values: F, K (future phases), or "blank". The field can be used for Order Entry mode in case of Outgoing CTR payments. If the operator wants to impose the tag option 50F or 50K he can do so by setting this field. The data inputted by the operator will then take precedence over the account details from the ledger. No Input Field. |
| 25 | `PP.AUTE.DebitAccountNumber` | `PpAuthEntry_Debitaccountnumber` | TField |  | Indicates the Account Number of the Debit Party Accepts value as defined in ACCOUNT table. No Input Field. |
| 26 | `PP.AUTE.DebitAccountNumberBIC` | `PpAuthEntry_Debitaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Debit Party. No Input Field. |
| 27 | `PP.AUTE.DebitAccountNumberImposedFlag` | `PpAuthEntry_Debitaccountnumberimposedflag` | TField |  | When imposed the corresponding Debit Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. No Input Field. |
| 28 | `PP.AUTE.DebitAccountCurrency` | `PpAuthEntry_Debitaccountcurrency` | TField |  | Indicates the Currency Code of the Debit Party. Accepts valid value as defined in the PPT.CURRENCY table. No Input Field. |
| 29 | `PP.AUTE.DebitAmount` | `PpAuthEntry_Debitamount` | TField |  | Indicates the Debit amount which is to be debited from sender. Calculated based on transaction amount involving any FX if applicable. No Input Field. |
| 30 | `PP.AUTE.DebitExchangeRate` | `PpAuthEntry_Debitexchangerate` | TField |  | The exchange rate that is used to convert the debit amount into the transaction amount (or transaction amount into debit amount) in case the debit account currency is different from the transaction currency. If a rate is keyed in then the impose flag must also be set, else the rate keyed in will be ignored. See also the description with field DebitExchangeRateImposedFlag. No Input Field. |
| 31 | `PP.AUTE.DebitExchangeRateImposedFlag` | `PpAuthEntry_Debitexchangerateimposedflag` | TField |  | If debit exchange rate is imposed by the operator and the entered value will not be overridden by the payment engine. Check Box Field. No Input Field. |
| 32 | `PP.AUTE.DebitExchangeRateReference` | `PpAuthEntry_Debitexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of a foreign currency by the dealer. This is only for transactions that exceed the threshold. The payment operator contacts treasury for a deal. No Input Field. |
| 33 | `PP.AUTE.DebitValueDate` | `PpAuthEntry_Debitvaluedate` | TField |  | Indicates the date on which the actual debit will happen. If left empty, Payment Engine will calculate this date based on Processing Date No Input Field. |
| 34 | `PP.AUTE.DebitValueDateImposedFlag` | `PpAuthEntry_Debitvaluedateimposedflag` | TField |  | This field specifies whether the debit value date is imposed or can still be overwritten by the date component. In case the impose flag is lacking but the debit value date is specified, the manual input is more a suggestion towards the system. In case the impose flag is present and the debit value date is specified, the manual input is a hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. No Input Field. Possible values: "Y" " " |
| 35 | `PP.AUTE.OrderingAccount` | `PpAuthEntry_Orderingaccount` | TField |  | National Clearing Code or Account Number of the Ordering Party can be entered. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. No Input Field. |
| 36 | `PP.AUTE.OrderingName` | `PpAuthEntry_Orderingname` | TField |  | Free Text Field, wherein Additional Address details(Usually Name) of the Ordering Party can be entered. Free Text Field. No Input Field. |
| 37 | `PP.AUTE.OrderingAddress1` | `PpAuthEntry_Orderingaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. No Input Field. |
| 38 | `PP.AUTE.OrderingAddress2` | `PpAuthEntry_Orderingaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. No Input Field. |
| 39 | `PP.AUTE.OrderingAddress3` | `PpAuthEntry_Orderingaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. No Input Field. |
| 40 | `PP.AUTE.OrderingCountry` | `PpAuthEntry_Orderingcountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from PPT.COUNTRYIBANSTRUCTURE. Drop Down Field. No Input Field. |
| 41 | `PP.AUTE.VATDebitMainAmountIndicator` | `PpAuthEntry_Vatdebitmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Main Amount % (VATDebitMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. No Input Field. |
| 42 | `PP.AUTE.VATDebitMainAmountPercentage` | `PpAuthEntry_Vatdebitmainamountpercentage` | TField |  | Indicates the percentage on Debit Main Amount. No Input Field. |
| 43 | `PP.AUTE.CreditAccountCompany` | `PpAuthEntry_Creditaccountcompany` | TField |  | Indicates the Company ID of the Credit Party. Accepts valid value as defined in the PPT.COMPANY table. No Input Field. |
| 44 | `PP.AUTE.CreditAccountNumber` | `PpAuthEntry_Creditaccountnumber` | TField |  | Indicates the Account Number of the Credit Party Accepts value as defined in ACCOUNT table. No Input Field. |
| 45 | `PP.AUTE.CreditAccountNumberBIC` | `PpAuthEntry_Creditaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Credit Party. No Input Field. |
| 46 | `PP.AUTE.CreditAccountNumberImposedFlag` | `PpAuthEntry_Creditaccountnumberimposedflag` | TField |  | When imposed the corresponding Credit Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. No Input Field. |
| 47 | `PP.AUTE.CreditAccountCurrency` | `PpAuthEntry_Creditaccountcurrency` | TField |  | Indicates the Currency Code of the Credit Party. Accepts valid value as defined in the PPT.CURRENCY table. No Input Field. |
| 48 | `PP.AUTE.CreditAmount` | `PpAuthEntry_Creditamount` | TField |  | Indicates the credit amount which is to be credited to the beneficiary. Calculated based on transaction amount involving any FX if present. No Input Field. |
| 49 | `PP.AUTE.CreditExchangeRate` | `PpAuthEntry_Creditexchangerate` | TField |  | The exchange rate that is used to convert the credit amount into the transaction amount (or transaction amount into debit amount) in case the credit account currency is different from the transaction currency. No Input Field. |
| 50 | `PP.AUTE.CreditExchangeRateImposedFlag` | `PpAuthEntry_Creditexchangerateimposedflag` | TField |  | If credit exchange rate is imposed by the operator and the entered value will not be overridden by the payment engine. Check Box Field. No Input Field. |
| 51 | `PP.AUTE.CreditExchangeRateReference` | `PpAuthEntry_Creditexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of a foreign currency by the dealer. This is only for transactions that exceed the threshold. The payment operator contacts treasury for a deal. No Input Field. |
| 52 | `PP.AUTE.CreditValueDate` | `PpAuthEntry_Creditvaluedate` | TField |  | Indicates the date on which the actual credit will happen. If left empty, Payment Engine will calculate this date based on Processing Date. No Input Field. |
| 53 | `PP.AUTE.CreditValueDateImposedFlag` | `PpAuthEntry_Creditvaluedateimposedflag` | TField |  | This field specifies whether the credit value date is imposed or can still be overwritten by the date component. In case the impose flag is lacking but the credit value date is specified, the manual input is more a suggestion towards the system. In case the impose flag is present and the credit value date is specified, the manual input is a hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. No Input Field. |
| 54 | `PP.AUTE.BeneficiaryAccount` | `PpAuthEntry_Beneficiaryaccount` | TField |  | Specifies National Clearing Code or Account Number of the Beneficiary Institution(BENINS for BTR) or Beneficiary(BENFCY for CTR). National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} No Input Field. |
| 55 | `PP.AUTE.BeneficiaryName` | `PpAuthEntry_Beneficiaryname` | TField |  | Free Text Field, wherein Additional Address details(Usually Name) of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Free Text Field. No Input Field. |
| 56 | `PP.AUTE.BeneficiaryAddress1` | `PpAuthEntry_Beneficiaryaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} No Input Field. |
| 57 | `PP.AUTE.BeneficiaryAddress2` | `PpAuthEntry_Beneficiaryaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} No Input Field. |
| 58 | `PP.AUTE.BeneficiaryAddress3` | `PpAuthEntry_Beneficiaryaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} No Input Field. |
| 59 | `PP.AUTE.BeneficiaryCountry` | `PpAuthEntry_Beneficiarycountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from CountryIBANStructure table. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} No Input Field. Drop Down Field. |
| 60 | `PP.AUTE.VATCreditMainAmountIndicator` | `PpAuthEntry_Vatcreditmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Main Amount % (VATCreditMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. No Input Field. |
| 61 | `PP.AUTE.VATCreditMainAmountPercentage` | `PpAuthEntry_Vatcreditmainamountpercentage` | TField |  | Indicates the percentage on Credit Main Amount. No Input Field. |
| 62 | `PP.AUTE.WaiveDebitCharges` | `PpAuthEntry_Waivedebitcharges` | TField |  | Indicates whether the debit side charges/fees can be skipped/waived or not. Check Box Field. No Input Field. |
| 63 | `PP.AUTE.DebitChargeAccountCompany` | `PpAuthEntry_Debitchargeaccountcompany` | TField |  | Indicates the company code where the debit charge account is maintained. Drop Down Field. No Input Field. |
| 64 | `PP.AUTE.DebitChargeAccount` | `PpAuthEntry_Debitchargeaccount` | TField |  | Indicates the account number to where the charges will be debited. No Input Field. |
| 65 | `PP.AUTE.DebitChargeAccountImposeFlag` | `PpAuthEntry_Debitchargeaccountimposeflag` | TField |  | When imposed the corresponding Debit Charge Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 66 | `PP.AUTE.DebitChargeAccountCurrency` | `PpAuthEntry_Debitchargeaccountcurrency` | TField |  | Indicates the currency code of the debit charge account. Drop Down Field. No Input Field. |
| 67 | `PP.AUTE.DebitChargeImposedFlag` | `PpAuthEntry_Debitchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee component that the default charges are not to be calculated. Check Box Field. No Input Field. |
| 68 | `PP.AUTE.DebitChargeComponent` | `PpAuthEntry_Debitchargecomponent` |  |  |  |
| 69 | `PP.AUTE.DebitChargeCurrency` | `PpAuthEntry_Debitchargecurrency` |  |  |  |
| 70 | `PP.AUTE.DebitChargeAmount` | `PpAuthEntry_Debitchargeamount` |  |  |  |
| 71 | `PP.AUTE.DebitReceiverCharge` | `PpAuthEntry_Debitreceivercharge` | TField |  | Outgoing OUR charge amount which can be used by posting and also swift component to determine the outgoing 71G mapping. No Input Field. |
| 72 | `PP.AUTE.DebitReceiverChargeImposedFlag` | `PpAuthEntry_Debitreceiverchargeimposedflag` | TField |  | If imposed the operator entered value in the Outgoing Receiver Charge (DebitReceiverCharge) field will not be overridden by the payment engine. Check Box Field. No Input Field. |
| 73 | `PP.AUTE.VATDebitMainChargeIndicator` | `PpAuthEntry_Vatdebitmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Charge Amount % (VATDebitMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. No Input Field. |
| 74 | `PP.AUTE.VATDebitMainChargePercentage` | `PpAuthEntry_Vatdebitmainchargepercentage` | TField |  | Indicates the percentage of VAT which needs to be calculated over the debit charge amount of the transaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specified percentage will override the percentage present in the client conditions component. No Input Field. |
| 75 | `PP.AUTE.WaiveCreditCharges` | `PpAuthEntry_Waivecreditcharges` | TField |  | Indicates whether the credit side charges/fees can be skipped/waived or not. Check Box Field. No Input Field. |
| 76 | `PP.AUTE.CreditChargeAccountCompany` | `PpAuthEntry_Creditchargeaccountcompany` | TField |  | Indicates the company code where the charge account is maintained. Drop Down Field. No Input Field. |
| 77 | `PP.AUTE.CreditChargeAccount` | `PpAuthEntry_Creditchargeaccount` | TField |  | Indicates the account number, to where the charges will be credited No Input Field. |
| 78 | `PP.AUTE.CreditChargeAccountImposeFlag` | `PpAuthEntry_Creditchargeaccountimposeflag` | TField |  | When imposed the corresponding Credit Charge Account Number entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 79 | `PP.AUTE.CreditChargeAccountCurrency` | `PpAuthEntry_Creditchargeaccountcurrency` | TField |  | Indicates the currency code of the charge account. Drop Down Field. No Input Field. |
| 80 | `PP.AUTE.CreditChargeImposedFlag` | `PpAuthEntry_Creditchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee component that the default charges are not to be calculated. Check Box Field. No Input Field. |
| 81 | `PP.AUTE.CreditChargeComponent` | `PpAuthEntry_Creditchargecomponent` |  |  |  |
| 82 | `PP.AUTE.CreditChargeCurrency` | `PpAuthEntry_Creditchargecurrency` |  |  |  |
| 83 | `PP.AUTE.CreditChargeAmount` | `PpAuthEntry_Creditchargeamount` |  |  |  |
| 84 | `PP.AUTE.CreditReceiverCharge` | `PpAuthEntry_Creditreceivercharge` | TField |  | Incoming our Charge amount. No Input Field. |
| 85 | `PP.AUTE.VATCreditMainChargeIndicator` | `PpAuthEntry_Vatcreditmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Charge Amount % (VATCreditMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. No Input Field. Check Box Field. |
| 86 | `PP.AUTE.VATCreditMainChargePercentage` | `PpAuthEntry_Vatcreditmainchargepercentage` | TField |  | This field specifies the percentage of VAT which needs to be calculated over the credit charge amount of the transaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specified percentage will override the percentage present in the client conditions component. No Input Field. |
| 87 | `PP.AUTE.OrderingInstAccount` | `PpAuthEntry_Orderinginstaccount` | TField |  | National Clearing Code or Account Number of the Ordering Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. No Input Field. |
| 88 | `PP.AUTE.OrderingInstIdentifierCode` | `PpAuthEntry_Orderinginstidentifiercode` | TField |  | Bank Identification Code of the Ordering Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. No Input Field. |
| 89 | `PP.AUTE.OrderingInstAddress` | `PpAuthEntry_Orderinginstaddress` |  |  |  |
| 90 | `PP.AUTE.SendersCorresAccount` | `PpAuthEntry_Senderscorresaccount` | TField |  | National Clearing Code or Account Number of the Sender Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. No Input Field. |
| 91 | `PP.AUTE.SendersCorresIdentifierCode` | `PpAuthEntry_Senderscorresidentifiercode` | TField |  | Bank Identification Code of the Sender Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE No Input Field. |
| 92 | `PP.AUTE.SendersCorresAddress` | `PpAuthEntry_Senderscorresaddress` |  |  |  |
| 93 | `PP.AUTE.ReceiversCorresAccount` | `PpAuthEntry_Receiverscorresaccount` | TField |  | National Clearing Code or Account Number of the Receiver Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. No Input Field. |
| 94 | `PP.AUTE.ReceiversCorresIdentifierCode` | `PpAuthEntry_Receiverscorresidentifiercode` | TField |  | Bank Identification Code of the Receiver Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. No Input Field. |
| 95 | `PP.AUTE.ReceiversCorresAddress` | `PpAuthEntry_Receiverscorresaddress` |  |  |  |
| 96 | `PP.AUTE.ThirdReimburseInstAccount` | `PpAuthEntry_Thirdreimburseinstaccount` | TField |  | National Clearing Code or Account Number of the Third Reimbursement Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. No Input Field. |
| 97 | `PP.AUTE.ThirdReimburseInstIdentifierCd` | `PpAuthEntry_Thirdreimburseinstidentifiercd` | TField |  | Bank Identification Code of the Third Reimbursement Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. No Input Field. |
| 98 | `PP.AUTE.ThirdReimburseInstAddress` | `PpAuthEntry_Thirdreimburseinstaddress` |  |  |  |
| 99 | `PP.AUTE.IntermediaryInstAccount` | `PpAuthEntry_Intermediaryinstaccount` | TField |  | National Clearing Code or Account Number of the Intermediary Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT_BankCode table. Account Number can be entered by prefixing '/'. No Input Field. |
| 100 | `PP.AUTE.IntermediaryInstIdentifierCode` | `PpAuthEntry_Intermediaryinstidentifiercode` | TField |  | Bank Identification Code of the Intermediary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE No Input Field. |
| 101 | `PP.AUTE.IntermediaryInstAddress` | `PpAuthEntry_Intermediaryinstaddress` |  |  |  |
| 102 | `PP.AUTE.AccountWithInstAccount` | `PpAuthEntry_Accountwithinstaccount` | TField |  | Specifies the National Clearing Code or Account Number of the Account with Institution. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value from PPT.BANKCODE table. Account Number can be entered by prefixing '/'. Account with Institution Tag 57 A, B, C or D {ACWINS} No Input Field. |
| 103 | `PP.AUTE.AccountWithInstIdentifierCode` | `PpAuthEntry_Accountwithinstidentifiercode` | TField |  | Specifies the Bank Identification Code of the Account with Institution. Account with Institution Tag 57 A, B, C or D {ACWINS} Validation Rules: Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE No Input Field. |
| 104 | `PP.AUTE.AccountWithInstAddress` | `PpAuthEntry_Accountwithinstaddress` |  |  |  |
| 105 | `PP.AUTE.InstructionCode` | `PpAuthEntry_Instructioncode` |  |  |  |
| 106 | `PP.AUTE.PaymentDetails` | `PpAuthEntry_Paymentdetails` |  |  |  |
| 107 | `PP.AUTE.AdditionalText` | `PpAuthEntry_Additionaltext` | TField |  | Free Text Field wherein the operator can specify additional information relating to the payment instruction. No Input Field. |
| 108 | `PP.AUTE.AuditTrail` | `PpAuthEntry_Audittrail` |  |  |  |
| 109 | `PP.AUTE.Information` | `PpAuthEntry_Information` |  |  |  |
| 110 | `PP.AUTE.AcceptWarning` | `PpAuthEntry_Acceptwarning` | TField | Yes | Whenever an Warning Type of error is encountered by the payment, the operator must accept the warning (Mandatory) to proceed with further payment processing. Check Box Field. No Input Field. |
| 111 | `PP.AUTE.Warning` | `PpAuthEntry_Warning` |  |  |  |
| 112 | `PP.AUTE.FunctionalError` | `PpAuthEntry_Functionalerror` |  |  |  |
| 113 | `PP.AUTE.FatalError` | `PpAuthEntry_Fatalerror` | TField |  | Highlights the text "Error Information Present" on the main screen, if there are any errors present in Error Information Tab. No Input Field. |
| 114 | `PP.AUTE.ValidationFlag` | `PpAuthEntry_Validationflag` | TField |  | Not Applicable for Order Entry. (Used in Repair application) Will be populated/enriched by payment engine. Validation Flag (field 119) from "User Header Block" (Block 3). |
| 115 | `PP.AUTE.BalanceReservation` | `PpAuthEntry_Balancereservation` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 116 | `PP.AUTE.BalanceReservationNumber` | `PpAuthEntry_Balancereservationnumber` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 117 | `PP.AUTE.ProcessingDateImposedFlag` | `PpAuthEntry_Processingdateimposedflag` | TField |  | If imposed the corresponding Processing date entered by the operator is not overridden by the payment engine. Check Box Field. No Input Field. |
| 118 | `PP.AUTE.DebitRepairFee` | `PpAuthEntry_Debitrepairfee` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 119 | `PP.AUTE.CreditRepairFee` | `PpAuthEntry_Creditrepairfee` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 120 | `PP.AUTE.Action` | `PpAuthEntry_Action` | TField |  | Used for internal purpose. No Input Field. This field can hold upto 1 alphanumeric character and the value is not editable by the user. Possible Values will be G, V, S, C, R and A |
| 121 | `PP.AUTE.CancelDescription` | `PpAuthEntry_Canceldescription` | TField |  | Describes the reason for cancellation of a payment. Operator uses this field to let authoriser know the justification for such an action. Free Text Field. No Input Field. |
| 122 | `PP.AUTE.RejectDescription` | `PpAuthEntry_Rejectdescription` | TField |  | Free Text Field, wherein the operator can specify the reason for rejecting the payment. Input Field. |
| 123 | `PP.AUTE.DebitInstruction` | `PpAuthEntry_Debitinstruction` | TField |  | Enriches value from POR.DEBITBANKCONDITIONS table after the payment is validated. Contains any credit instructions if present for a bank, which will be useful for the operator how to process the payment. No Input Field. |
| 124 | `PP.AUTE.CreditInstruction` | `PpAuthEntry_Creditinstruction` | TField |  | Enriches value from POR.DEBITBANKCONDITIONS after the payment is validated. Contains any credit instructions if present for a bank, which will be useful for the operator how to process the payment. No input field. |
| 125 | `PP.AUTE.ShowOriginalRoutingInfo` | `PpAuthEntry_Showoriginalroutinginfo` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 126 | `PP.AUTE.OrderingIdentifierCode` | `PpAuthEntry_Orderingidentifiercode` | TField |  | Bank Identification Code of the Ordering Party can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value. |
| 127 | `PP.AUTE.BeneficiaryIdentifierCode` | `PpAuthEntry_Beneficiaryidentifiercode` | TField |  | Bank Identification Code of the Beneficiary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 128 | `PP.AUTE.DebitTreasuryRate` | `PpAuthEntry_Debittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. The Final exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of the appropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 129 | `PP.AUTE.DebitTreasuryRateImposedFlag` | `PpAuthEntry_Debittreasuryrateimposedflag` | TField |  | If Debit Treasury Rate is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 130 | `PP.AUTE.DebitCustomerSpread` | `PpAuthEntry_Debitcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generate the final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 131 | `PP.AUTE.DebitCustSpreadImposedFlag` | `PpAuthEntry_Debitcustspreadimposedflag` | TField |  | If Debit Customer Spread is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 132 | `PP.AUTE.CreditTreasuryRate` | `PpAuthEntry_Credittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. The Final exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of the appropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 133 | `PP.AUTE.CreditTreasuryRateImposedFlag` | `PpAuthEntry_Credittreasuryrateimposedflag` | TField |  | If Credit Treasury Rate is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 134 | `PP.AUTE.CreditCustomerSpread` | `PpAuthEntry_Creditcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generate the final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value can only be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24 Currency table. |
| 135 | `PP.AUTE.CreditCustSpreadImposedFlag` | `PpAuthEntry_Creditcustspreadimposedflag` | TField |  | If Credit Customer Spread is imposed by the operator then the entered value will not be overridden by the payment engine. Check Box Field. |
| 136 | `PP.AUTE.FieldPrompt` | `PpAuthEntry_Fieldprompt` |  |  |  |
| 137 | `PP.AUTE.OldValue` | `PpAuthEntry_Oldvalue` |  |  |  |
| 138 | `PP.AUTE.NewValue` | `PpAuthEntry_Newvalue` |  |  |  |
| 139 | `PP.AUTE.IntraCompanyPayment` | `PpAuthEntry_Intracompanypayment` | TField |  |  |
| 140 | `PP.AUTE.SelectTemplate` | `PpAuthEntry_Selecttemplate` | TField |  |  |
| 141 | `PP.AUTE.SaveAsTemplate` | `PpAuthEntry_Saveastemplate` | TField |  |  |
| 142 | `PP.AUTE.NickName` | `PpAuthEntry_Nickname` | TField |  |  |
| 143 | `PP.AUTE.StoreTemplateValues` | `PpAuthEntry_Storetemplatevalues` | TField |  |  |
| 144 | `PP.AUTE.ReturnPayment` | `PpAuthEntry_Returnpayment` | TField |  |  |
| 145 | `PP.AUTE.ReturnCode` | `PpAuthEntry_Returncode` | TField |  |  |
| 146 | `PP.AUTE.ReturnDescription` | `PpAuthEntry_Returndescription` | TField |  |  |
| 147 | `PP.AUTE.UltDbtNm` | `PpAuthEntry_Ultdbtnm` | TField |  |  |
| 148 | `PP.AUTE.UltDbtBIC` | `PpAuthEntry_Ultdbtbic` | TField |  |  |
| 149 | `PP.AUTE.UltDbtOrgIdOthId` | `PpAuthEntry_Ultdbtorgidothid` | TField |  |  |
| 150 | `PP.AUTE.UltDbtOrgIdOthSchCd` | `PpAuthEntry_Ultdbtorgidothschcd` | TField |  |  |
| 151 | `PP.AUTE.UltDbtOrgIdOthSchProp` | `PpAuthEntry_Ultdbtorgidothschprop` | TField |  |  |
| 152 | `PP.AUTE.UltDbtOrgIdOthIssuer` | `PpAuthEntry_Ultdbtorgidothissuer` | TField |  |  |
| 153 | `PP.AUTE.UltDbtBrDt` | `PpAuthEntry_Ultdbtbrdt` | TField |  |  |
| 154 | `PP.AUTE.UltDbtPvOfBr` | `PpAuthEntry_Ultdbtpvofbr` | TField |  |  |
| 155 | `PP.AUTE.UltDbtCityOfBr` | `PpAuthEntry_Ultdbtcityofbr` | TField |  |  |
| 156 | `PP.AUTE.UltDbtCtryOfBr` | `PpAuthEntry_Ultdbtctryofbr` | TField |  |  |
| 157 | `PP.AUTE.UltDbtPrvIdOthId` | `PpAuthEntry_Ultdbtprvidothid` | TField |  |  |
| 158 | `PP.AUTE.UltDbtPrvIdOthSchCd` | `PpAuthEntry_Ultdbtprvidothschcd` | TField |  |  |
| 159 | `PP.AUTE.UltDbtPrvIdOthSchProp` | `PpAuthEntry_Ultdbtprvidothschprop` | TField |  |  |
| 160 | `PP.AUTE.UltDbtPrvIdOthIssuer` | `PpAuthEntry_Ultdbtprvidothissuer` | TField |  |  |
| 161 | `PP.AUTE.DbtOrgIdOthId` | `PpAuthEntry_Dbtorgidothid` | TField |  |  |
| 162 | `PP.AUTE.DbtOrgIdOthSchCd` | `PpAuthEntry_Dbtorgidothschcd` | TField |  |  |
| 163 | `PP.AUTE.DbtOrgIdOthSchProp` | `PpAuthEntry_Dbtorgidothschprop` | TField |  |  |
| 164 | `PP.AUTE.DbtOrgIdOthIssuer` | `PpAuthEntry_Dbtorgidothissuer` | TField |  |  |
| 165 | `PP.AUTE.DbtBrDt` | `PpAuthEntry_Dbtbrdt` | TField |  |  |
| 166 | `PP.AUTE.DbtPvOfBr` | `PpAuthEntry_Dbtpvofbr` | TField |  |  |
| 167 | `PP.AUTE.DbtCityOfBr` | `PpAuthEntry_Dbtcityofbr` | TField |  |  |
| 168 | `PP.AUTE.DbtCtryOfBr` | `PpAuthEntry_Dbtctryofbr` | TField |  |  |
| 169 | `PP.AUTE.DbtPrvIdOthId` | `PpAuthEntry_Dbtprvidothid` | TField |  |  |
| 170 | `PP.AUTE.DbtPrvIdOthSchCd` | `PpAuthEntry_Dbtprvidothschcd` | TField |  |  |
| 171 | `PP.AUTE.DbtPrvIdOthSchProp` | `PpAuthEntry_Dbtprvidothschprop` | TField |  |  |
| 172 | `PP.AUTE.DbtPrvIdOthIssuer` | `PpAuthEntry_Dbtprvidothissuer` | TField |  |  |
| 173 | `PP.AUTE.CrdOrgIdOthId` | `PpAuthEntry_Crdorgidothid` | TField |  |  |
| 174 | `PP.AUTE.CrdOrgIdOthSchCd` | `PpAuthEntry_Crdorgidothschcd` | TField |  |  |
| 175 | `PP.AUTE.CrdOrgIdOthSchProp` | `PpAuthEntry_Crdorgidothschprop` | TField |  |  |
| 176 | `PP.AUTE.CrdOrgIdOthIssuer` | `PpAuthEntry_Crdorgidothissuer` | TField |  |  |
| 177 | `PP.AUTE.CrdBrDt` | `PpAuthEntry_Crdbrdt` | TField |  |  |
| 178 | `PP.AUTE.CrdPvOfBr` | `PpAuthEntry_Crdpvofbr` | TField |  |  |
| 179 | `PP.AUTE.CrdCityOfBr` | `PpAuthEntry_Crdcityofbr` | TField |  |  |
| 180 | `PP.AUTE.CrdCtryOfBr` | `PpAuthEntry_Crdctryofbr` | TField |  |  |
| 181 | `PP.AUTE.CrdPrvIdOthId` | `PpAuthEntry_Crdprvidothid` | TField |  |  |
| 182 | `PP.AUTE.CrdPrvIdOthSchCd` | `PpAuthEntry_Crdprvidothschcd` | TField |  |  |
| 183 | `PP.AUTE.CrdPrvIdOthSchProp` | `PpAuthEntry_Crdprvidothschprop` | TField |  |  |
| 184 | `PP.AUTE.CrdPrvIdOthIssuer` | `PpAuthEntry_Crdprvidothissuer` | TField |  |  |
| 185 | `PP.AUTE.UltCrdNm` | `PpAuthEntry_Ultcrdnm` | TField |  |  |
| 186 | `PP.AUTE.UltCrdBIC` | `PpAuthEntry_Ultcrdbic` | TField |  |  |
| 187 | `PP.AUTE.UltCrdOrgIdOthId` | `PpAuthEntry_Ultcrdorgidothid` | TField |  |  |
| 188 | `PP.AUTE.UltCrdOrgIdOthSchCd` | `PpAuthEntry_Ultcrdorgidothschcd` | TField |  |  |
| 189 | `PP.AUTE.UltCrdOrgIdOthSchProp` | `PpAuthEntry_Ultcrdorgidothschprop` | TField |  |  |
| 190 | `PP.AUTE.UltCrdOrgIdOthIssuer` | `PpAuthEntry_Ultcrdorgidothissuer` | TField |  |  |
| 191 | `PP.AUTE.UltCrdBrDt` | `PpAuthEntry_Ultcrdbrdt` | TField |  |  |
| 192 | `PP.AUTE.UltCrdPvOfBr` | `PpAuthEntry_Ultcrdpvofbr` | TField |  |  |
| 193 | `PP.AUTE.UltCrdCityOfBr` | `PpAuthEntry_Ultcrdcityofbr` | TField |  |  |
| 194 | `PP.AUTE.UltCrdCtryOfBr` | `PpAuthEntry_Ultcrdctryofbr` | TField |  |  |
| 195 | `PP.AUTE.UltCrdPrvIdOthId` | `PpAuthEntry_Ultcrdprvidothid` | TField |  |  |
| 196 | `PP.AUTE.UltCrdPrvIdOthSchCd` | `PpAuthEntry_Ultcrdprvidothschcd` | TField |  |  |
| 197 | `PP.AUTE.UltCrdPrvIdOthSchProp` | `PpAuthEntry_Ultcrdprvidothschprop` | TField |  |  |
| 198 | `PP.AUTE.UltCrdPrvIdOthIssuer` | `PpAuthEntry_Ultcrdprvidothissuer` | TField |  |  |
| 199 | `PP.AUTE.CrdRefInfTpCd` | `PpAuthEntry_Crdrefinftpcd` |  |  |  |
| 200 | `PP.AUTE.CrdRefInfTpIssuer` | `PpAuthEntry_Crdrefinftpissuer` |  |  |  |
| 201 | `PP.AUTE.CrdRefInfRef` | `PpAuthEntry_Crdrefinfref` |  |  |  |
| 202 | `PP.AUTE.CatPurpCd` | `PpAuthEntry_Catpurpcd` |  |  |  |
| 203 | `PP.AUTE.CatPurpProp` | `PpAuthEntry_Catpurpprop` |  |  |  |
| 204 | `PP.AUTE.TrxPurpCd` | `PpAuthEntry_Trxpurpcd` |  |  |  |
| 205 | `PP.AUTE.ExtendedFields` | `PpAuthEntry_Extendedfields` | TField |  |  |
| 206 | `PP.AUTE.MndtId` | `PpAuthEntry_Mndtid` | TField |  | Indicates the unique mandate identification. The value of this field is updated to the field "MandateReference" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. |
| 207 | `PP.AUTE.MndtDtOfSgn` | `PpAuthEntry_Mndtdtofsgn` | TField |  | Indicates the date of signature of the mandate. The value of this field is updated to the field "SignatureDate" in POR.DEBITAUTHINFO table. Validation Rules: 11 characters of type Date. |
| 208 | `PP.AUTE.MndtAmdtInd` | `PpAuthEntry_Mndtamdtind` | TField |  | Indicates the Amendment indicator of the mandate. The value of this field is updated to the field "AmendmentIndicator" in POR.DEBITAUTHINFO table. Possible values: 'N' - this means that none of the fields should be filled. 'Y' - this means that at least one of the fields should be filled. Note: The mentioned fields here are: OriginalMandateReference, OriginalCreditorName, OriginalCreditorId, OriginalCreditorSchProp, OriginalDebtorAccount, OriginalDebtorAgtOtherID Default value is "N". Validation Rules: 1 alphabetic characters. |
| 209 | `PP.AUTE.MndtOrglMndtId` | `PpAuthEntry_Mndtorglmndtid` | TField | Yes | Indicates the Reference of the original MandateID as received in Incoming Direct Debit message. The value of this field is updated to the field "OriginalMandateReference" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Mandatory only if OriginalMandateReference is different from MandateReference. |
| 210 | `PP.AUTE.MndtOrglCrdSchNm` | `PpAuthEntry_Mndtorglcrdschnm` | TField |  | Indicates the original name of the Creditor who issued the mandate. The value of this field is updated to the field "OriginalCreditorName" in POR.DEBITAUTHINFO table. Validation Rules: 70 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 211 | `PP.AUTE.MndtOrglCrdSchPrvOthId` | `PpAuthEntry_Mndtorglcrdschprvothid` | TField |  | Indicates the Original Creditor ID as it is mapped from Incoming Direct Debit message. The value of this field is updated to the field "OriginalCreditorID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 212 | `PP.AUTE.MndtOrglCrdSchPrvOthSchNmProp` | `PpAuthEntry_Mndtorglcrdschprvothschnmprop` | TField |  | Indicates the scheme name of the original Creditor. The value of this field is updated to the field "OriginalCreditorSchProp" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Only "SEPA" value is allowed. |
| 213 | `PP.AUTE.MndtOrglDbtAccIdIBAN` | `PpAuthEntry_Mndtorgldbtaccidiban` | TField |  | Indicates the original Debtor account IBAN. The value of this field is updated to the field "OriginalDebtorAccount" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". If present only IBAN is allowed. Only present if changes occur in "Debtor Account" received from Incoming Direct Debit message. |
| 214 | `PP.AUTE.MndtOrglDbtAgFinInstIdBIC` | `PpAuthEntry_Mndtorgldbtagfininstidbic` | TField |  | Indicates the Original Debtor Agent Financial Institution Identification BIC. The value of this field is updated to the field "OriginalDebtorAgtBIC" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". |
| 215 | `PP.AUTE.MndtElectronicSgn` | `PpAuthEntry_Mndtelectronicsgn` | TField |  | Indicates the placeholder of Electronic Signature of the Mandate provided in the incoming Direct Debit. This data element is not to be used if the mandate is a paper mandate. The value of this field is updated to the field "ElectronicSignature" in POR.DEBITAUTHINFO table. Validation Rules: 1025 alphabetic characters. |
| 216 | `PP.AUTE.CrdSchIdPrvIdOthId` | `PpAuthEntry_Crdschidprvidothid` | TField |  | Indicates the creditor business code. The value of this field is updated to the field "CreditorID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It cannot contains spaces. |
| 217 | `PP.AUTE.MndtOrglDbtAccIdOthId` | `PpAuthEntry_Mndtorgldbtaccidothid` | TField |  | Indicates the Original Debtor Account Identifier. Use account other identification with code 'SMNDA' to indicate same mandate with new Debtor Account or in case of an account change within same bank. The value of this field is updated to the field "OriginalDebtorAcctOtherID" in POR.DEBITAUTHINFO table. Validation Rules: 35 alphabetic characters. It should be filled only if AmendmentIndicator is "Y". Only "SMNDA" value is allowed. |
| 218 | `PP.AUTE.BalanceReservationKeyForChgAct` | `PpAuthEntry_Balancereservationkeyforchgact` | TField |  | Holds the reservation key of the debit charge account. |
| 219 | `PP.AUTE.RequestedCollectionDate` | `PpAuthEntry_Requestedcollectiondate` | TField |  |  |
| 220 | `PP.AUTE.Scheme` | `PpAuthEntry_Scheme` | TField |  |  |
| 221 | `PP.AUTE.ClearingTransactionType` | `PpAuthEntry_Clearingtransactiontype` | TField |  |  |
| 222 | `PP.AUTE.InstructedCurrency` | `PpAuthEntry_Instructedcurrency` | TField | Yes | Indicates the Instructed currency in which the payment to be processed. Will hold valid currency code values from PPT.CURRENCY table. Drop Down Field. Validation Rules: Mandatory when InstructedAmount is present. |
| 223 | `PP.AUTE.InstructedAmount` | `PpAuthEntry_Instructedamount` | TField | Yes | Indicates the Instructed amount for which the payment needs to be processed. Validation Rules: Mandatory when InstructedCurrency is present. |
| 224 | `PP.AUTE.RESERVED.28` | `PpAuthEntry_Reserved28` | TField |  |  |
| 225 | `PP.AUTE.RESERVED.27` | `PpAuthEntry_Reserved27` | TField |  |  |
| 226 | `PP.AUTE.RESERVED.26` | `PpAuthEntry_Reserved26` | TField |  |  |
| 227 | `PP.AUTE.RESERVED.25` | `PpAuthEntry_Reserved25` | TField |  |  |
| 228 | `PP.AUTE.RESERVED.24` | `PpAuthEntry_Reserved24` | TField |  |  |
| 229 | `PP.AUTE.RESERVED.23` | `PpAuthEntry_Reserved23` | TField |  |  |
| 230 | `PP.AUTE.RESERVED.22` | `PpAuthEntry_Reserved22` | TField |  |  |
| 231 | `PP.AUTE.RESERVED.21` | `PpAuthEntry_Reserved21` | TField |  |  |
| 232 | `PP.AUTE.RESERVED.20` | `PpAuthEntry_Reserved20` | TField |  |  |
| 233 | `PP.AUTE.RESERVED.19` | `PpAuthEntry_Reserved19` | TField |  |  |
| 234 | `PP.AUTE.RESERVED.18` | `PpAuthEntry_Reserved18` | TField |  |  |
| 235 | `PP.AUTE.RESERVED.17` | `PpAuthEntry_Reserved17` | TField |  |  |
| 236 | `PP.AUTE.RESERVED.16` | `PpAuthEntry_Reserved16` | TField |  |  |
| 237 | `PP.AUTE.RESERVED.15` | `PpAuthEntry_Reserved15` | TField |  |  |
| 238 | `PP.AUTE.RESERVED.14` | `PpAuthEntry_Reserved14` | TField |  |  |
| 239 | `PP.AUTE.RESERVED.13` | `PpAuthEntry_Reserved13` | TField |  |  |
| 240 | `PP.AUTE.RESERVED.12` | `PpAuthEntry_Reserved12` | TField |  |  |
| 241 | `PP.AUTE.RESERVED.11` | `PpAuthEntry_Reserved11` | TField |  |  |
| 242 | `PP.AUTE.RESERVED.10` | `PpAuthEntry_Reserved10` | TField |  |  |
| 243 | `PP.AUTE.RESERVED.9` | `PpAuthEntry_Reserved9` | TField |  |  |
| 244 | `PP.AUTE.RESERVED.8` | `PpAuthEntry_Reserved8` | TField |  |  |
| 245 | `PP.AUTE.RESERVED.7` | `PpAuthEntry_Reserved7` | TField |  |  |
| 246 | `PP.AUTE.RESERVED.6` | `PpAuthEntry_Reserved6` | TField |  |  |
| 247 | `PP.AUTE.RESERVED.5` | `PpAuthEntry_Reserved5` | TField |  |  |
| 248 | `PP.AUTE.RESERVED.4` | `PpAuthEntry_Reserved4` | TField |  |  |
| 249 | `PP.AUTE.RESERVED.3` | `PpAuthEntry_Reserved3` | TField |  |  |
| 250 | `PP.AUTE.RESERVED.2` | `PpAuthEntry_Reserved2` | TField |  |  |
| 251 | `PP.AUTE.RESERVED.1` | `PpAuthEntry_Reserved1` | TField |  |  |
| 252 | `PP.AUTE.LOCAL.REF` | `PpAuthEntry_LocalRef` |  |  |  |
| 253 | `PP.AUTE.OVERRIDE` | `PpAuthEntry_Override` |  |  |  |
| 254 | `PP.AUTE.RECORD.STATUS` | `PpAuthEntry_RecordStatus` | String |  |  |
| 255 | `PP.AUTE.CURR.NO` | `PpAuthEntry_CurrNo` | String |  |  |
| 256 | `PP.AUTE.INPUTTER` | `PpAuthEntry_Inputter` |  |  |  |
| 257 | `PP.AUTE.DATE.TIME` | `PpAuthEntry_DateTime` |  |  |  |
| 258 | `PP.AUTE.AUTHORISER` | `PpAuthEntry_Authoriser` | String |  |  |
| 259 | `PP.AUTE.CO.CODE` | `PpAuthEntry_CoCode` | String |  |  |
| 260 | `PP.AUTE.DEPT.CODE` | `PpAuthEntry_DeptCode` | String |  |  |
| 261 | `PP.AUTE.AUDITOR.CODE` | `PpAuthEntry_AuditorCode` | String |  |  |
| 262 | `PP.AUTE.AUDIT.DATE.TIME` | `PpAuthEntry_AuditDateTime` | String |  |  |
