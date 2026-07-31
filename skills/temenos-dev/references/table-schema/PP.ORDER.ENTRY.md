# PP.ORDER.ENTRY — Table Schema

> Source: `INSERTS/I_F.PP.ORDER.ENTRY` in `PP_OrderEntryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.OEYG.Status` | `PpOrderEntry_Status` | TField |  | Indicates the Status Code (a Numeric number between 0 - 999) of the payment that is currently being processed. For Order Entry, The initial value of Status is 135. (Pending Submit) After successful Submit Action, the Status is changed to 315.(Pending Authorize) After successful First Authorize Action, the Status is changed to 316. After successful Final Authorize Action, the Status is changed to 600. No Input Field. |
| 2 | `PP.OEYG.TransactionReferenceNumber` | `PpOrderEntry_Transactionreferencenumber` | TField |  | Will hold a system generated unique number (FT Number) to identify the payment throughout its processing.Operator upon entering processing company and click the TRN button, the Transaction Reference Number is generatedbased on Company ID Date and Sequence number. No Input Field. |
| 3 | `PP.OEYG.SendersReferenceNumber` | `PpOrderEntry_Sendersreferencenumber` | TField |  | Tag 20. Free Text Field. |
| 4 | `PP.OEYG.RelatedReference` | `PpOrderEntry_Relatedreference` | TField |  | Free Text Field. Tag 21 |
| 5 | `PP.OEYG.Source` | `PpOrderEntry_Source` | TField |  | Will contain the actual source through which the payment was originated. No Input Field. Defaulted with a value 'OE' for Order Entry. |
| 6 | `PP.OEYG.Direction` | `PpOrderEntry_Direction` | TField |  | Indicates the direction of the payment. Drop Down Field. No Input Field. Possible values: 1. I - Incoming 2. O - Outgoing 3. B - Book transfer 4. R - Redirect (Future Use) |
| 7 | `PP.OEYG.TransferType` | `PpOrderEntry_Transfertype` | TField |  | CTR BTR Indicator Field. Possible Values: 1. "C" for CTR (Customer Transfer) 2. "B" For BTR (Bank Transfer) |
| 8 | `PP.OEYG.IncomingMessageType` | `PpOrderEntry_Incomingmessagetype` | TField |  | Default value is "RFCT" for Order Entry. Default value is "MXCT" for Customer ISO Outgoing screens Default value is "MXBT" for Bank ISO Outgoing screens No Input Field. |
| 9 | `PP.OEYG.PreAuthorizationNumber` | `PpOrderEntry_Preauthorizationnumber` | TField |  | Operator can key in the ID of AC.FUNDS.AUTHORISATION table, if the funds were pre-authorized. (Pre AuthorizationKey) Free Text Field. |
| 10 | `PP.OEYG.ProcessCompany` | `PpOrderEntry_Processcompany` | TField |  | Indicates the company code of the company where the payment is processed. Possible values are fetched from the the T24 COMPANY Table. Drop Down Field. |
| 11 | `PP.OEYG.ProcessingDate` | `PpOrderEntry_Processingdate` | TField |  | Indicates the date on which the processing is supposed to happen. Date Field. |
| 12 | `PP.OEYG.Priority` | `PpOrderEntry_Priority` | TField |  | Identifies the Payment Message Priority and based on this value priority code is set in the payment engine. IF MessagePriority is empty or between 1 and 5, then PriorityCode is 'N' IF MessagePriority is between 6 and 9, then PriorityCode is 'U' Possible values: 1 to 9 Drop Down Value. |
| 13 | `PP.OEYG.Product` | `PpOrderEntry_Product` | TField |  | Must contain a valid Clearing ID from PP.CLEARING.NATURE.CODE table Free Text Field. For DD Initiation Payments, User can input product with three words separated by hyphen as delimiter. First word should be valid bank operation code , Second one should be valid clearing nature code and Third can be user defined. Example: B2B-FNAL-OUTGOING |
| 14 | `PP.OEYG.OutputChannel` | `PpOrderEntry_Outputchannel` | TField |  | Indicates the output channel for the payment. Default Possible values: LORO, NOSTRO, LEDGER Validation Rules: Other Possible values Values are populated based on field 'ClearingID' in PP.CLEARING.SETTING Drop Down Field. |
| 15 | `PP.OEYG.OutputChannelImposedFlag` | `PpOrderEntry_Outputchannelimposedflag` | TField |  | If imposed the corresponding channel entered by the operator will not be overridden by the payment engine. Check Box Field. |
| 16 | `PP.OEYG.TransactionCurrency` | `PpOrderEntry_Transactioncurrency` | TField | Yes | Indicates the currency in which the payment is processed. Will hold valid currency code values from PP.CURRENCY table. Drop Down Field. Mandatory Field. |
| 17 | `PP.OEYG.TransactionAmount` | `PpOrderEntry_Transactionamount` | TField | Yes | Indicates the amount for which the payment needs to be processed. Mandatory Field. |
| 18 | `PP.OEYG.ChargeOption` | `PpOrderEntry_Chargeoption` | TField |  | Contains the Details of Charge (Tag 71 A) Possible Values: 1. "BEN" 2. "SHA" 3. "OUR" Drop Down Field. |
| 19 | `PP.OEYG.SenderInstitutionBIC` | `PpOrderEntry_Senderinstitutionbic` | TField |  | Bank Identification Code of the Sender Institution can be keyed in. Bank Identification Code (BIC) should containa valid BIC value from PPT.BICTABLE. Free Text Field. |
| 20 | `PP.OEYG.SenderInstitutionNCC` | `PpOrderEntry_Senderinstitutionncc` | TField |  | National Clearing Code of the Sender Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODE table. Free Text Field. |
| 21 | `PP.OEYG.ReceiverInstitutionBIC` | `PpOrderEntry_Receiverinstitutionbic` | TField |  | Bank Identification Code of the Receiver Institution can be keyed in. Bank Identification Code (BIC) shouldcontain a valid BIC value from PPT.BICTABLE. Free Text Field. |
| 22 | `PP.OEYG.ReceiverInstitutionNCC` | `PpOrderEntry_Receiverinstitutionncc` | TField |  | National Clearing Code of the Receiver Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODEtable. Free Text Field. |
| 23 | `PP.OEYG.DebitAccountCompany` | `PpOrderEntry_Debitaccountcompany` | TField |  | Indicates the Company ID of the Debit Party. Accepts valid value as defined in the T24 COMPANY table. |
| 24 | `PP.OEYG.OrderPartyTagOption` | `PpOrderEntry_Orderpartytagoption` | TField |  | The field can contain the following values: F, K , or "blank". The field can be used for Order Entry mode in case of Outgoing CTR payments. If the operator wants to impose thetag option 50F or 50K he can do so by setting this field. The data inputted by the operator will then takeprecedence over the account details from the ledger. |
| 25 | `PP.OEYG.DebitAccountNumber` | `PpOrderEntry_Debitaccountnumber` | TField |  | Indicates the Account Number of the Debit Party Accepts value as defined in ACCOUNT table. |
| 26 | `PP.OEYG.DebitAccountNumberBIC` | `PpOrderEntry_Debitaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Debit Party. |
| 27 | `PP.OEYG.DebitAccountNumberImposedFlag` | `PpOrderEntry_Debitaccountnumberimposedflag` | TField |  | When imposed the corresponding Debit Account Number entered by the operator will not be overridden by the paymentengine. Check Box Field. |
| 28 | `PP.OEYG.DebitAccountCurrency` | `PpOrderEntry_Debitaccountcurrency` | TField |  | Indicates the Currency Code of the Debit Party. Accepts valid value as defined in the PP.CURRENCY table. |
| 29 | `PP.OEYG.DebitAmount` | `PpOrderEntry_Debitamount` | TField |  | Indicates the Debit amount which is to be debited from sender. Calculated based on transaction amount involvingany FX if applicable. |
| 30 | `PP.OEYG.DebitExchangeRate` | `PpOrderEntry_Debitexchangerate` | TField |  | The exchange rate that is used to convert the debit amount into the transaction amount (or transaction amountinto debit amount) in case the debit account currency is different from the transaction currency. If a rate iskeyed in then the impose flag must also be set, else the rate keyed in will be ignored. See also the descriptionwith field DebitExchangeRateImposedFlag. |
| 31 | `PP.OEYG.DebitExchangeRateImposedFlag` | `PpOrderEntry_Debitexchangerateimposedflag` | TField |  | If debit exchange rate is imposed by the operator and the entered value will not be overridden by the paymentengine. Check Box Field. |
| 32 | `PP.OEYG.DebitExchangeRateReference` | `PpOrderEntry_Debitexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of aforeign currency by the dealer. This is only for transactions that exceed the threshold. The payment operatorcontacts treasury for a deal. |
| 33 | `PP.OEYG.DebitValueDate` | `PpOrderEntry_Debitvaluedate` | TField |  | Indicates the date on which the actual debit will happen. If left empty, Payment Engine will calculate this datebased on Processing Date |
| 34 | `PP.OEYG.DebitValueDateImposedFlag` | `PpOrderEntry_Debitvaluedateimposedflag` | TField |  | This field specifies whether the debit value date is imposed or can still be overwritten by the date component.In case the impose flag is lacking but the debit value date is specified, the manual input is more a suggestiontowards the system. In case the impose flag is present and the debit value date is specified, the manual input is ahard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. Possible values: "Y" " " |
| 35 | `PP.OEYG.OrderingAccount` | `PpOrderEntry_Orderingaccount` | TField |  | National Clearing Code or Account Number of the Ordering Party can be entered. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 36 | `PP.OEYG.OrderingName` | `PpOrderEntry_Orderingname` | TField |  | Free Text Field, wherein Additional Address details(Usually Name) of the Ordering Party can be entered. |
| 37 | `PP.OEYG.OrderingAddress1` | `PpOrderEntry_Orderingaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 38 | `PP.OEYG.OrderingAddress2` | `PpOrderEntry_Orderingaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 39 | `PP.OEYG.OrderingAddress3` | `PpOrderEntry_Orderingaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Ordering Party can be entered. |
| 40 | `PP.OEYG.OrderingCountry` | `PpOrderEntry_Orderingcountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from PPT.COUNTRYIBANSTRUCTURE. Drop Down Field. |
| 41 | `PP.OEYG.VATDebitMainAmountIndicator` | `PpOrderEntry_Vatdebitmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Main Amount %(VATDebitMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 42 | `PP.OEYG.VATDebitMainAmountPercentage` | `PpOrderEntry_Vatdebitmainamountpercentage` | TField |  | Indicates the percentage on Debit Main Amount. |
| 43 | `PP.OEYG.CreditAccountCompany` | `PpOrderEntry_Creditaccountcompany` | TField |  | Indicates the Company ID of the Credit Party. Accepts valid value as defined in the T24 COMPANY table. |
| 44 | `PP.OEYG.CreditAccountNumber` | `PpOrderEntry_Creditaccountnumber` | TField |  | Indicates the Account Number of the Credit Party Accepts value as defined in ACCOUNT table. |
| 45 | `PP.OEYG.CreditAccountNumberBIC` | `PpOrderEntry_Creditaccountnumberbic` | TField |  | Indicates the Bank Identification Code of the Credit Party. |
| 46 | `PP.OEYG.CreditAccountNumberImposedFlag` | `PpOrderEntry_Creditaccountnumberimposedflag` | TField |  | When imposed the corresponding Credit Account Number entered by the operator will not be overridden by thepayment engine. Check Box Field. |
| 47 | `PP.OEYG.CreditAccountCurrency` | `PpOrderEntry_Creditaccountcurrency` | TField |  | Indicates the Currency Code of the Credit Party. Accepts valid value as defined in the PP.CURRENCY table. |
| 48 | `PP.OEYG.CreditAmount` | `PpOrderEntry_Creditamount` | TField |  | Indicates the credit amount which is to be credited to the beneficiary. Calculated based on transaction amountinvolving any FX if present. |
| 49 | `PP.OEYG.CreditExchangeRate` | `PpOrderEntry_Creditexchangerate` | TField |  | The exchange rate that is used to convert the credit amount into the transaction amount (or transaction amountinto debit amount) in case the credit account currency is different from the transaction currency. |
| 50 | `PP.OEYG.CreditExchangeRateImposedFlag` | `PpOrderEntry_Creditexchangerateimposedflag` | TField |  | If credit exchange rate is imposed by the operator and the entered value will not be overridden by the paymentengine. Check Box Field. |
| 51 | `PP.OEYG.CreditExchangeRateReference` | `PpOrderEntry_Creditexchangeratereference` | TField |  | The exchange rate reference field is used to specify the treasury contract number which goes with the buy of aforeign currency by the dealer. This is only for transactions that exceed the threshold. The payment operatorcontacts treasury for a deal. |
| 52 | `PP.OEYG.CreditValueDate` | `PpOrderEntry_Creditvaluedate` | TField |  | Indicates the date on which the actual credit will happen. If left empty, Payment Engine will calculate this datebased on Processing Date. |
| 53 | `PP.OEYG.CreditValueDateImposedFlag` | `PpOrderEntry_Creditvaluedateimposedflag` | TField |  | This field specifies whether the credit value date is imposed or can still be overwritten by the date component.In case the impose flag is lacking but the credit value date is specified, the manual input is more a suggestiontowards the system. In case the impose flag is present and the credit value date is specified, the manual input isa hard requirement to be taken into account by the date component, even though the given date is a non-working day. Check Box Field. |
| 54 | `PP.OEYG.BeneficiaryAccount` | `PpOrderEntry_Beneficiaryaccount` | TField |  | Specifies National Clearing Code or Account Number of the Beneficiary Institution(BENINS for BTR) orBeneficiary(BENFCY for CTR). National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODE table. Account Number can be entered by prefixing '/'. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 55 | `PP.OEYG.BeneficiaryName` | `PpOrderEntry_Beneficiaryname` | TField |  | Free Text Field, wherein Additional Address details(Usually Name) of the Beneficiary or beneficiary Institutioncan be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Free Text Field. |
| 56 | `PP.OEYG.BeneficiaryAddress1` | `PpOrderEntry_Beneficiaryaddress1` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 57 | `PP.OEYG.BeneficiaryAddress2` | `PpOrderEntry_Beneficiaryaddress2` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 58 | `PP.OEYG.BeneficiaryAddress3` | `PpOrderEntry_Beneficiaryaddress3` | TField |  | Free Text Field, wherein Additional Address details of the Beneficiary or beneficiary Institution can be entered. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} |
| 59 | `PP.OEYG.BeneficiaryCountry` | `PpOrderEntry_Beneficiarycountry` | TField |  | Beneficiary Country can be entered. Valid values are taken from CountryIBANStructure table. Beneficiary 59A or no letter option {BENFCY} or Beneficiary Institution 58 A or D {BENINS} Drop Down Field. |
| 60 | `PP.OEYG.VATCreditMainAmountIndicator` | `PpOrderEntry_Vatcreditmainamountindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Main Amount %(VATCreditMainAmountPercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 61 | `PP.OEYG.VATCreditMainAmountPercentage` | `PpOrderEntry_Vatcreditmainamountpercentage` | TField |  | Indicates the percentage on Credit Main Amount. |
| 62 | `PP.OEYG.WaiveDebitCharges` | `PpOrderEntry_Waivedebitcharges` | TField |  | Indicates whether the debit side charges/fees can be skipped/waived or not. Check Box Field. |
| 63 | `PP.OEYG.DebitChargeAccountCompany` | `PpOrderEntry_Debitchargeaccountcompany` | TField |  | Indicates the company code where the debit charge account is maintained. Drop Down Field. |
| 64 | `PP.OEYG.DebitChargeAccount` | `PpOrderEntry_Debitchargeaccount` | TField |  | Indicates the account number to where the charges will be debited. |
| 65 | `PP.OEYG.DebitChargeAccountImposedFlag` | `PpOrderEntry_Debitchargeaccountimposedflag` | TField |  | When imposed the corresponding Debit Charge Account Number entered by the operator will not be overridden by thepayment engine. Check Box Field. |
| 66 | `PP.OEYG.DebitChargeAccountCurrency` | `PpOrderEntry_Debitchargeaccountcurrency` | TField |  | Indicates the currency code of the debit charge account. Drop Down Field. |
| 67 | `PP.OEYG.DebitChargeImposedFlag` | `PpOrderEntry_Debitchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee componentthat the default charges are not to be calculated. Check Box Field. |
| 68 | `PP.OEYG.DebitChargeComponent` | `PpOrderEntry_Debitchargecomponent` |  |  |  |
| 69 | `PP.OEYG.DebitChargeCurrency` | `PpOrderEntry_Debitchargecurrency` |  |  |  |
| 70 | `PP.OEYG.DebitChargeAmount` | `PpOrderEntry_Debitchargeamount` |  |  |  |
| 71 | `PP.OEYG.DebitReceiverCharge` | `PpOrderEntry_Debitreceivercharge` | TField |  | Outgoing OUR charge amount which can be used by posting and also swift component to determine the outgoing 71G mapping. |
| 72 | `PP.OEYG.DebitReceiverChargeImposedFlag` | `PpOrderEntry_Debitreceiverchargeimposedflag` | TField |  | If imposed the operator entered value in the Outgoing Receiver Charge (DebitReceiverCharge) field will not beoverridden by the payment engine. Check Box Field. |
| 73 | `PP.OEYG.VATDebitMainChargeIndicator` | `PpOrderEntry_Vatdebitmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Debit Charge Amount %(VATDebitMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 74 | `PP.OEYG.VATDebitMainChargePercentage` | `PpOrderEntry_Vatdebitmainchargepercentage` | TField |  | Indicates the percentage of VAT which needs to be calculated over the debit charge amount of the transaction incase VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator, the specifiedpercentage will override the percentage present in the client conditions component. |
| 75 | `PP.OEYG.WaiveCreditCharges` | `PpOrderEntry_Waivecreditcharges` | TField |  | Indicates whether the credit side charges/fees can be skipped/waived or not. Check Box Field. |
| 76 | `PP.OEYG.CreditChargeAccountCompany` | `PpOrderEntry_Creditchargeaccountcompany` | TField |  | Indicates the company code where the charge account is maintained. Drop Down Field. |
| 77 | `PP.OEYG.CreditChargeAccount` | `PpOrderEntry_Creditchargeaccount` | TField |  | Indicates the account number, to where the charges will be credited |
| 78 | `PP.OEYG.CreditChargeAccountImposedFlag` | `PpOrderEntry_Creditchargeaccountimposedflag` | TField |  | When imposed the corresponding Credit Charge Account Number entered by the operator will not be overridden by thepayment engine. Check Box Field. |
| 79 | `PP.OEYG.CreditChargeAccountCurrency` | `PpOrderEntry_Creditchargeaccountcurrency` | TField |  | Indicates the currency code of the charge account. Drop Down Field. |
| 80 | `PP.OEYG.CreditChargeImposedFlag` | `PpOrderEntry_Creditchargeimposedflag` | TField |  | If operator enters a charge manually (via OE screen), this flag will be set to "Y" to inform the fee componentthat the default charges are not to be calculated. Check Box Field. |
| 81 | `PP.OEYG.CreditChargeComponent` | `PpOrderEntry_Creditchargecomponent` |  |  |  |
| 82 | `PP.OEYG.CreditChargeCurrency` | `PpOrderEntry_Creditchargecurrency` |  |  |  |
| 83 | `PP.OEYG.CreditChargeAmount` | `PpOrderEntry_Creditchargeamount` |  |  |  |
| 84 | `PP.OEYG.CreditReceiverCharge` | `PpOrderEntry_Creditreceivercharge` | TField |  | Incoming our Charge amount. |
| 85 | `PP.OEYG.VATCreditMainChargeIndicator` | `PpOrderEntry_Vatcreditmainchargeindicator` | TField |  | If the field is set (checked), the value entered by the operator for the field VAT Credit Charge Amount %(VATCreditMainChargePercentage) will overwrite the VAT value which is defined/derived from Client Conditions. Check Box Field. |
| 86 | `PP.OEYG.VATCreditMainChargePercentage` | `PpOrderEntry_Vatcreditmainchargepercentage` | TField |  | This field specifies the percentage of VAT which needs to be calculated over the credit charge amount of thetransaction in case VAT is imposed by the payments operator. In case VAT is not imposed by the payments operator,the specified percentage will override the percentage present in the client conditions component. |
| 87 | `PP.OEYG.OrderingInstAccount` | `PpOrderEntry_Orderinginstaccount` | TField |  | National Clearing Code or Account Number of the Ordering Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 88 | `PP.OEYG.OrderingInstIdentifierCode` | `PpOrderEntry_Orderinginstidentifiercode` | TField |  | Bank Identification Code of the Ordering Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 89 | `PP.OEYG.OrderingInstAddress` | `PpOrderEntry_Orderinginstaddress` |  |  |  |
| 90 | `PP.OEYG.SendersCorresAccount` | `PpOrderEntry_Senderscorresaccount` | TField |  | National Clearing Code or Account Number of the Sender Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 91 | `PP.OEYG.SendersCorresIdentifierCode` | `PpOrderEntry_Senderscorresidentifiercode` | TField |  | Bank Identification Code of the Sender Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 92 | `PP.OEYG.SendersCorresAddress` | `PpOrderEntry_Senderscorresaddress` |  |  |  |
| 93 | `PP.OEYG.ReceiversCorresAccount` | `PpOrderEntry_Receiverscorresaccount` | TField |  | National Clearing Code or Account Number of the Receiver Correspondent Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 94 | `PP.OEYG.ReceiversCorresIdentifierCode` | `PpOrderEntry_Receiverscorresidentifiercode` | TField |  | Bank Identification Code of the Receiver Correspondent Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 95 | `PP.OEYG.ReceiversCorresAddress` | `PpOrderEntry_Receiverscorresaddress` |  |  |  |
| 96 | `PP.OEYG.ThirdReimburseInstAccount` | `PpOrderEntry_Thirdreimburseinstaccount` | TField |  | National Clearing Code or Account Number of the Third Reimbursement Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODE table. Account Number can be entered by prefixing '/'. |
| 97 | `PP.OEYG.ThirdReimburseInstIdentifierCd` | `PpOrderEntry_Thirdreimburseinstidentifiercd` | TField |  | Bank Identification Code of the Third Reimbursement Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE. |
| 98 | `PP.OEYG.ThirdReimburseInstAddress` | `PpOrderEntry_Thirdreimburseinstaddress` |  |  |  |
| 99 | `PP.OEYG.IntermediaryInstAccount` | `PpOrderEntry_Intermediaryinstaccount` | TField |  | National Clearing Code or Account Number of the Intermediary Institution can be keyed in. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT_BankCode table. Account Number can be entered by prefixing '/'. |
| 100 | `PP.OEYG.IntermediaryInstIdentifierCode` | `PpOrderEntry_Intermediaryinstidentifiercode` | TField |  | Bank Identification Code of the Intermediary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 101 | `PP.OEYG.IntermediaryInstAddress` | `PpOrderEntry_Intermediaryinstaddress` |  |  |  |
| 102 | `PP.OEYG.AccountWithInstAccount` | `PpOrderEntry_Accountwithinstaccount` | TField |  | Specifies the National Clearing Code or Account Number of the Account with Institution. National Clearing Code (NCC) should be entered by prefixing double slash '//'. It should be valid value fromPPT.BANKCODE table. Account Number can be entered by prefixing '/'. Account with Institution Tag 57 A, B, C or D {ACWINS} |
| 103 | `PP.OEYG.AccountWithInstIdentifierCode` | `PpOrderEntry_Accountwithinstidentifiercode` | TField |  | Specifies the Bank Identification Code of the Account with Institution. Account with Institution Tag 57 A, B, C or D {ACWINS} Validation Rules: Bank Identification Code (BIC) should contain a valid BIC value from PPT.BICTABLE |
| 104 | `PP.OEYG.AccountWithInstAddress` | `PpOrderEntry_Accountwithinstaddress` |  |  |  |
| 105 | `PP.OEYG.InstructionCode` | `PpOrderEntry_Instructioncode` |  |  |  |
| 106 | `PP.OEYG.PaymentDetails` | `PpOrderEntry_Paymentdetails` |  |  |  |
| 107 | `PP.OEYG.AdditionalText` | `PpOrderEntry_Additionaltext` |  |  |  |
| 108 | `PP.OEYG.AuditTrail` | `PpOrderEntry_Audittrail` |  |  |  |
| 109 | `PP.OEYG.Information` | `PpOrderEntry_Information` |  |  |  |
| 110 | `PP.OEYG.AcceptWarning` | `PpOrderEntry_Acceptwarning` | TField | Yes | Whenever an Warning Type of error is encountered by the payment, the operator must accept the warning (Mandatory)to proceed with further payment processing. Check Box Field. |
| 111 | `PP.OEYG.Warning` | `PpOrderEntry_Warning` |  |  |  |
| 112 | `PP.OEYG.FunctionalError` | `PpOrderEntry_Functionalerror` |  |  |  |
| 113 | `PP.OEYG.FatalError` | `PpOrderEntry_Fatalerror` | TField |  | Highlights the text "Error Information Present" on the main screen, if there are any errors present in ErrorInformation Tab. No Input Field. |
| 114 | `PP.OEYG.ValidationFlag` | `PpOrderEntry_Validationflag` | TField |  | Not Applicable for Order Entry. (Used in Repair application) Will be populated/enriched by payment engine. Validation Flag (field 119) from "User Header Block" (Block 3). |
| 115 | `PP.OEYG.BalanceReservation` | `PpOrderEntry_Balancereservation` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 116 | `PP.OEYG.BalanceReservationNumber` | `PpOrderEntry_Balancereservationnumber` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 117 | `PP.OEYG.ProcessingDateImposedFlag` | `PpOrderEntry_Processingdateimposedflag` | TField |  | If imposed the corresponding Processing date entered by the operator is not overridden by the payment engine. Check Box Field. |
| 118 | `PP.OEYG.DebitRepairFee` | `PpOrderEntry_Debitrepairfee` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 119 | `PP.OEYG.CreditRepairFee` | `PpOrderEntry_Creditrepairfee` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 120 | `PP.OEYG.Action` | `PpOrderEntry_Action` | TField |  | Used for internal purpose. This field can hold upto 2 alphanumeric character and the value is not editable by the user. Possible Values will be G, V, S, C, R, T, J , A, Z, RR, SR and MO |
| 121 | `PP.OEYG.CancelDescription` | `PpOrderEntry_Canceldescription` | TField |  | Describes the reason for cancellation of a payment. Operator uses this field to let authoriser know thejustification for such an action. Free Text Field. |
| 122 | `PP.OEYG.RejectDescription` | `PpOrderEntry_Rejectdescription` | TField |  | Free Text Field, wherein the operator can specify the reason for rejecting the payment. |
| 123 | `PP.OEYG.DebitInstruction` | `PpOrderEntry_Debitinstruction` | TField |  | Enriches value from POR.AGREEMENT.AND.ADVICE table after the payment is validated. Contains any Debitinstructions if present for a bank, which will be useful for the operator how to process the payment. No Input Field. |
| 124 | `PP.OEYG.CreditInstruction` | `PpOrderEntry_Creditinstruction` | TField |  | Enriches value from POR.AGREEMENT.AND.ADVICE after the payment is validated. Contains any credit instructions ifpresent for a bank, which will be useful for the operator how to process the payment. No input field. |
| 125 | `PP.OEYG.ShowOriginalRoutingInfo` | `PpOrderEntry_Showoriginalroutinginfo` | TField |  | Not Applicable for Order Entry. (Used in Repair application) |
| 126 | `PP.OEYG.OrderingIdentifierCode` | `PpOrderEntry_Orderingidentifiercode` | TField |  | Bank Identification Code of the Ordering Party can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 127 | `PP.OEYG.BeneficiaryIdentifierCode` | `PpOrderEntry_Beneficiaryidentifiercode` | TField |  | Bank Identification Code of the Beneficiary Institution can be keyed in. Bank Identification Code (BIC) should contain a valid BIC value |
| 128 | `PP.OEYG.DebitTreasuryRate` | `PpOrderEntry_Debittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. TheFinal exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of theappropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if theExchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24Currency table. |
| 129 | `PP.OEYG.DebitTreasuryRateImposedFlag` | `PpOrderEntry_Debittreasuryrateimposedflag` | TField |  | If Debit Treasury Rate is imposed by the operator then the entered value will not be overridden by the paymentengine. Check Box Field. |
| 130 | `PP.OEYG.DebitCustomerSpread` | `PpOrderEntry_Debitcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. Holds a negative value when spreadis negative. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generatethe final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value canonly be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will beignored and taken from T24 Currency table. |
| 131 | `PP.OEYG.DebitCustSpreadImposedFlag` | `PpOrderEntry_Debitcustspreadimposedflag` | TField |  | If Debit Customer Spread is imposed by the operator then the entered value will not be overridden by the paymentengine. Check Box Field. |
| 132 | `PP.OEYG.CreditTreasuryRate` | `PpOrderEntry_Credittreasuryrate` | TField |  | Defines the rate at which the Treasury unit will buy or sell foreign Currency from/to the marketing units. TheFinal exchange rate quoted to Customers (Customer Rate) will be determined by the addition or subtraction of theappropriate Customer Spread to/from the Treasury Buy/Sell Rate. This value can only be imposed if theExchange/Customer Rate is not imposed. If not imposed the value that is entered will be ignored and taken from T24Currency table. |
| 133 | `PP.OEYG.CreditTreasuryRateImposedFlag` | `PpOrderEntry_Credittreasuryrateimposedflag` | TField |  | If Credit Treasury Rate is imposed by the operator then the entered value will not be overridden by the paymentengine. Check Box Field. |
| 134 | `PP.OEYG.CreditCustomerSpread` | `PpOrderEntry_Creditcustomerspread` | TField |  | Identifies the Customer's Exchange Spread to be applied for this transaction. Holds a negative value when spreadis negative. The Customer Spread defined in this field will be applied to the Treasury (buy/sell) Rate to generatethe final Rate of the transaction, i.e. the exchange rate which is applicable to the Transaction. This value canonly be imposed if the Exchange/Customer Rate is not imposed. If not imposed the value that is entered will beignored and taken from T24 Currency table. |
| 135 | `PP.OEYG.CreditCustSpreadImposedFlag` | `PpOrderEntry_Creditcustspreadimposedflag` | TField |  | If Credit Customer Spread is imposed by the operator then the entered value will not be overridden by the paymentengine. Check Box Field. |
| 136 | `PP.OEYG.FieldPrompt` | `PpOrderEntry_Fieldprompt` |  |  |  |
| 137 | `PP.OEYG.OldValue` | `PpOrderEntry_Oldvalue` |  |  |  |
| 138 | `PP.OEYG.NewValue` | `PpOrderEntry_Newvalue` |  |  |  |
| 139 | `PP.OEYG.IntraCompanyPayment` | `PpOrderEntry_Intracompanypayment` | TField |  | Intra company flag can be used in the determination of the product for Order-Entry and Repair payments andaccordingly payment product and fee product should be retrieved by the system during processing of the payment. For first party payment, Operator will manually set this flag on Order Entry screen as 'Y' |
| 140 | `PP.OEYG.SelectTemplate` | `PpOrderEntry_Selecttemplate` | TField |  | This field will display the list of existing templates which user can use to populate payment data. User will be able to select from templates which are stored against User or the group to which user is associatedor templates which are available for all bank users. |
| 141 | `PP.OEYG.SaveAsTemplate` | `PpOrderEntry_Saveastemplate` | TField | Yes | Operator can save the details of the order entry screen in template application PPT.OE.TEMPLATE. Validation: In case user has provided nickname but not selected this checkbox, user should be prompted to select this to saveas template In case user has selected this checkbox, nick name is mandatory |
| 142 | `PP.OEYG.NickName` | `PpOrderEntry_Nickname` | TField | Yes | User can provide a nickname against which payment data should be stored in Template application Validation: In case user has provided nickname but not selected this checkbox, user should be prompted to select this to saveas template In case user has selected this checkbox, nick name is mandatory |
| 143 | `PP.OEYG.StoreTemplateValues` | `PpOrderEntry_Storetemplatevalues` | TField |  | Technical field - for internal purpose. This field will not be available to the user. |
| 144 | `PP.OEYG.ReturnPayment` | `PpOrderEntry_Returnpayment` | TField |  | This field indicates if the operator wants to return or reject a payment from Repair screen or from newReturn/Reject screen. Dropdown Field. Values for the field: 'Return' 'Reject' empty |
| 145 | `PP.OEYG.ReturnCode` | `PpOrderEntry_Returncode` | TField |  | This field indicates the clearing return code that is used for returning or rejecting a payment. Validation Rules: 4 alphanumeric characters. A valid return code in PP.CLEARING.RETURN.CODE table. |
| 146 | `PP.OEYG.ReturnDescription` | `PpOrderEntry_Returndescription` | TField |  | This field indicates a short additional information on the reason why the payment was returned/refunded/rejected. Free Text Field. Validation Rules: 256 alphanumeric characters. |
| 147 | `PP.OEYG.UltDbtNm` | `PpOrderEntry_Ultdbtnm` | TField |  |  |
| 148 | `PP.OEYG.UltDbtBIC` | `PpOrderEntry_Ultdbtbic` | TField |  |  |
| 149 | `PP.OEYG.UltDbtOrgIdOthId` | `PpOrderEntry_Ultdbtorgidothid` |  |  |  |
| 150 | `PP.OEYG.UltDbtOrgIdOthSchCd` | `PpOrderEntry_Ultdbtorgidothschcd` |  |  |  |
| 151 | `PP.OEYG.UltDbtOrgIdOthSchProp` | `PpOrderEntry_Ultdbtorgidothschprop` |  |  |  |
| 152 | `PP.OEYG.UltDbtOrgIdOthIssuer` | `PpOrderEntry_Ultdbtorgidothissuer` |  |  |  |
| 153 | `PP.OEYG.UltDbtBrDt` | `PpOrderEntry_Ultdbtbrdt` | TField |  |  |
| 154 | `PP.OEYG.UltDbtPvOfBr` | `PpOrderEntry_Ultdbtpvofbr` | TField |  |  |
| 155 | `PP.OEYG.UltDbtCityOfBr` | `PpOrderEntry_Ultdbtcityofbr` | TField |  |  |
| 156 | `PP.OEYG.UltDbtCtryOfBr` | `PpOrderEntry_Ultdbtctryofbr` | TField |  |  |
| 157 | `PP.OEYG.UltDbtPrvIdOthId` | `PpOrderEntry_Ultdbtprvidothid` |  |  |  |
| 158 | `PP.OEYG.UltDbtPrvIdOthSchCd` | `PpOrderEntry_Ultdbtprvidothschcd` |  |  |  |
| 159 | `PP.OEYG.UltDbtPrvIdOthSchProp` | `PpOrderEntry_Ultdbtprvidothschprop` |  |  |  |
| 160 | `PP.OEYG.UltDbtPrvIdOthIssuer` | `PpOrderEntry_Ultdbtprvidothissuer` |  |  |  |
| 161 | `PP.OEYG.DbtOrgIdOthId` | `PpOrderEntry_Dbtorgidothid` |  |  |  |
| 162 | `PP.OEYG.DbtOrgIdOthSchCd` | `PpOrderEntry_Dbtorgidothschcd` |  |  |  |
| 163 | `PP.OEYG.DbtOrgIdOthSchProp` | `PpOrderEntry_Dbtorgidothschprop` |  |  |  |
| 164 | `PP.OEYG.DbtOrgIdOthIssuer` | `PpOrderEntry_Dbtorgidothissuer` |  |  |  |
| 165 | `PP.OEYG.DbtBrDt` | `PpOrderEntry_Dbtbrdt` | TField |  |  |
| 166 | `PP.OEYG.DbtPvOfBr` | `PpOrderEntry_Dbtpvofbr` | TField |  |  |
| 167 | `PP.OEYG.DbtCityOfBr` | `PpOrderEntry_Dbtcityofbr` | TField |  |  |
| 168 | `PP.OEYG.DbtCtryOfBr` | `PpOrderEntry_Dbtctryofbr` | TField |  |  |
| 169 | `PP.OEYG.DbtPrvIdOthId` | `PpOrderEntry_Dbtprvidothid` |  |  |  |
| 170 | `PP.OEYG.DbtPrvIdOthSchCd` | `PpOrderEntry_Dbtprvidothschcd` |  |  |  |
| 171 | `PP.OEYG.DbtPrvIdOthSchProp` | `PpOrderEntry_Dbtprvidothschprop` |  |  |  |
| 172 | `PP.OEYG.DbtPrvIdOthIssuer` | `PpOrderEntry_Dbtprvidothissuer` |  |  |  |
| 173 | `PP.OEYG.CrdOrgIdOthId` | `PpOrderEntry_Crdorgidothid` |  |  |  |
| 174 | `PP.OEYG.CrdOrgIdOthSchCd` | `PpOrderEntry_Crdorgidothschcd` |  |  |  |
| 175 | `PP.OEYG.CrdOrgIdOthSchProp` | `PpOrderEntry_Crdorgidothschprop` |  |  |  |
| 176 | `PP.OEYG.CrdOrgIdOthIssuer` | `PpOrderEntry_Crdorgidothissuer` |  |  |  |
| 177 | `PP.OEYG.CrdBrDt` | `PpOrderEntry_Crdbrdt` | TField |  |  |
| 178 | `PP.OEYG.CrdPvOfBr` | `PpOrderEntry_Crdpvofbr` | TField |  |  |
| 179 | `PP.OEYG.CrdCityOfBr` | `PpOrderEntry_Crdcityofbr` | TField |  |  |
| 180 | `PP.OEYG.CrdCtryOfBr` | `PpOrderEntry_Crdctryofbr` | TField |  |  |
| 181 | `PP.OEYG.CrdPrvIdOthId` | `PpOrderEntry_Crdprvidothid` |  |  |  |
| 182 | `PP.OEYG.CrdPrvIdOthSchCd` | `PpOrderEntry_Crdprvidothschcd` |  |  |  |
| 183 | `PP.OEYG.CrdPrvIdOthSchProp` | `PpOrderEntry_Crdprvidothschprop` |  |  |  |
| 184 | `PP.OEYG.CrdPrvIdOthIssuer` | `PpOrderEntry_Crdprvidothissuer` |  |  |  |
| 185 | `PP.OEYG.UltCrdNm` | `PpOrderEntry_Ultcrdnm` | TField |  |  |
| 186 | `PP.OEYG.UltCrdBIC` | `PpOrderEntry_Ultcrdbic` | TField |  |  |
| 187 | `PP.OEYG.UltCrdOrgIdOthId` | `PpOrderEntry_Ultcrdorgidothid` |  |  |  |
| 188 | `PP.OEYG.UltCrdOrgIdOthSchCd` | `PpOrderEntry_Ultcrdorgidothschcd` |  |  |  |
| 189 | `PP.OEYG.UltCrdOrgIdOthSchProp` | `PpOrderEntry_Ultcrdorgidothschprop` |  |  |  |
| 190 | `PP.OEYG.UltCrdOrgIdOthIssuer` | `PpOrderEntry_Ultcrdorgidothissuer` |  |  |  |
| 191 | `PP.OEYG.UltCrdBrDt` | `PpOrderEntry_Ultcrdbrdt` | TField |  |  |
| 192 | `PP.OEYG.UltCrdPvOfBr` | `PpOrderEntry_Ultcrdpvofbr` | TField |  |  |
| 193 | `PP.OEYG.UltCrdCityOfBr` | `PpOrderEntry_Ultcrdcityofbr` | TField |  |  |
| 194 | `PP.OEYG.UltCrdCtryOfBr` | `PpOrderEntry_Ultcrdctryofbr` | TField |  |  |
| 195 | `PP.OEYG.UltCrdPrvIdOthId` | `PpOrderEntry_Ultcrdprvidothid` |  |  |  |
| 196 | `PP.OEYG.UltCrdPrvIdOthSchCd` | `PpOrderEntry_Ultcrdprvidothschcd` |  |  |  |
| 197 | `PP.OEYG.UltCrdPrvIdOthSchProp` | `PpOrderEntry_Ultcrdprvidothschprop` |  |  |  |
| 198 | `PP.OEYG.UltCrdPrvIdOthIssuer` | `PpOrderEntry_Ultcrdprvidothissuer` |  |  |  |
| 199 | `PP.OEYG.CrdRefInfTpCd` | `PpOrderEntry_Crdrefinftpcd` |  |  |  |
| 200 | `PP.OEYG.CrdRefInfTpIssuer` | `PpOrderEntry_Crdrefinftpissuer` |  |  |  |
| 201 | `PP.OEYG.CrdRefInfRef` | `PpOrderEntry_Crdrefinfref` |  |  |  |
| 202 | `PP.OEYG.CatPurpCd` | `PpOrderEntry_Catpurpcd` |  |  |  |
| 203 | `PP.OEYG.CatPurpProp` | `PpOrderEntry_Catpurpprop` |  |  |  |
| 204 | `PP.OEYG.TrxPurpCd` | `PpOrderEntry_Trxpurpcd` |  |  |  |
| 205 | `PP.OEYG.ExtendedFields` | `PpOrderEntry_Extendedfields` | TField |  |  |
| 206 | `PP.OEYG.MndtId` | `PpOrderEntry_Mndtid` | TField |  | Indicates the unique mandate identification. The value of this field is updated to the field "MANDATE.REFERENCE" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. |
| 207 | `PP.OEYG.MndtDtOfSgn` | `PpOrderEntry_Mndtdtofsgn` | TField |  | Indicates the date of signature of the mandate. The value of this field is updated to the field "SIGNATURE.DATE" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 11 characters of type Date. |
| 208 | `PP.OEYG.MndtAmdtInd` | `PpOrderEntry_Mndtamdtind` | TField |  | Indicates the Amendment indicator of the mandate. The value of this field is updated to the field "AMENDMENT.INDICATOR" in POR.AGREEMENT.AND.ADVICE table. Possible values: 'N' - this means that none of the fields should be filled. 'Y' - this means that at least one of the fields should be filled. Note: The mentioned fields here are: ORIGINAL.MANDATE.REFERENCE, ORIGINAL.CREDITOR.NAME, ORIGINAL.CREDITOR.ID,ORIGINAL.CREDITOR.SCH.PROP, ORIGINAL.DEBTOR.ACCOUNT, ORG.DEBTOR.ACCT.OTHER.ID Default value is "N". Validation Rules: 1 alphabetic characters. |
| 209 | `PP.OEYG.MndtOrglMndtId` | `PpOrderEntry_Mndtorglmndtid` | TField | Yes | Indicates the Reference of the original MandateID as received in Incoming Direct Debit message. The value of this field is updated to the field "ORIGINAL.MANDATE.REFERENCE" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". Mandatory only if ORIGINAL.MANDATE.REFERENCE is different from MANDATE.REFERENCE. |
| 210 | `PP.OEYG.MndtOrglCrdSchNm` | `PpOrderEntry_Mndtorglcrdschnm` | TField |  | Indicates the original name of the Creditor who issued the mandate. The value of this field is updated to the field "ORIGINAL.CREDITOR.NAME" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 70 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". |
| 211 | `PP.OEYG.MndtOrglCrdSchPrvOthId` | `PpOrderEntry_Mndtorglcrdschprvothid` | TField |  | Indicates the Original Creditor ID as it is mapped from Incoming Direct Debit message. The value of this field is updated to the field "ORIGINAL.CREDITOR.ID" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". |
| 212 | `PP.OEYG.MndtOrglCrdSchPrvOthSchNmProp` | `PpOrderEntry_Mndtorglcrdschprvothschnmprop` | TField |  | Indicates the scheme name of the original Creditor. The value of this field is updated to the field "ORIGINAL.CREDITOR.SCH.PROP" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". Only "SEPA" value is allowed. |
| 213 | `PP.OEYG.MndtOrglDbtAccIdIBAN` | `PpOrderEntry_Mndtorgldbtaccidiban` | TField |  | Indicates the original Debtor account IBAN. The value of this field is updated to the field "ORIGINAL.DEBTOR.ACCOUNT" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". If present only IBAN is allowed. Only present if changes occur in "Debtor Account" received from Incoming Direct Debit message. |
| 214 | `PP.OEYG.MndtOrglDbtAgFinInstIdBIC` | `PpOrderEntry_Mndtorgldbtagfininstidbic` | TField |  | Indicates the Original Debtor Agent Financial Institution Identification BIC. The value of this field is updated to the field "OriginalDebtorAgtBIC" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". |
| 215 | `PP.OEYG.MndtElectronicSgn` | `PpOrderEntry_Mndtelectronicsgn` | TField |  | Indicates the placeholder of Electronic Signature of the Mandate provided in the incoming Direct Debit. This data element is not to be used if the mandate is a paper mandate. The value of this field is updated to the field "ELECTRONIC.SIGNATURE" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 1025 alphabetic characters. |
| 216 | `PP.OEYG.CrdSchIdPrvIdOthId` | `PpOrderEntry_Crdschidprvidothid` | TField |  | Indicates the creditor business code. The value of this field is updated to the field "CREDITOR.ID" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It cannot contains spaces. |
| 217 | `PP.OEYG.MndtOrglDbtAccIdOthId` | `PpOrderEntry_Mndtorgldbtaccidothid` | TField |  | Indicates the Original Debtor Account Identifier. Use account other identification with code 'SMNDA' to indicate same mandate with new Debtor Account or in case ofan account change within same bank. The value of this field is updated to the field "ORG.DEBTOR.ACCT.OTHER.ID" in POR.AGREEMENT.AND.ADVICE table. Validation Rules: 35 alphabetic characters. It should be filled only if AMENDMENT.INDICATOR is "Y". Only "SMNDA" value is allowed. |
| 218 | `PP.OEYG.BalanceReservationKeyForChgAct` | `PpOrderEntry_Balancereservationkeyforchgact` | TField |  | Holds the reservation key of the debit charge account. |
| 219 | `PP.OEYG.RequestedCollectionDate` | `PpOrderEntry_Requestedcollectiondate` | TField |  |  |
| 220 | `PP.OEYG.Scheme` | `PpOrderEntry_Scheme` | TField |  |  |
| 221 | `PP.OEYG.ClearingTransactionType` | `PpOrderEntry_Clearingtransactiontype` | TField |  |  |
| 222 | `PP.OEYG.InstructedCurrency` | `PpOrderEntry_Instructedcurrency` | TField | Yes | Indicates the Instructed currency in which the payment to be processed. Will hold valid currency code values from PP.CURRENCY table. Drop Down Field. Validation Rules: Mandatory when InstructedAmount is present. |
| 223 | `PP.OEYG.InstructedAmount` | `PpOrderEntry_Instructedamount` | TField | Yes | Indicates the Instructed amount for which the payment needs to be processed. Validation Rules: Mandatory when InstructedCurrency is present. |
| 224 | `PP.OEYG.ReversalCode` | `PpOrderEntry_Reversalcode` | TField |  | ISO Reason Code for SEPA Reversal transaction. Validation Rules: 4 alphabetic characters. Defaulted value is "AM05" . |
| 225 | `PP.OEYG.ReversalOriginator` | `PpOrderEntry_Reversaloriginator` | TField |  | Originator for the Reversal transaction. Validation Rules: 35 alphabetic characters. Possible values: 'Bank' - Reversal originated by the Bank. 'Customer' - Reversal originated by the Customer/Creditor. |
| 226 | `PP.OEYG.RetRejOriginatedBy` | `PpOrderEntry_Retrejoriginatedby` | TField |  | Indicates if the Return or Reject was Originated by the Bank or by the Customer. Possible values: "Bank" - Return/Reject originated by the Bank, "Customer" - Return/Reject originated by the Customerand empty value. Default value will be "Bank" into the new ReturnReject Screen. Default value will be empty into the Repair screen, because when a payment is in Repair it is not always returnedor rejected. Validation Rules: 6 alphabetic characters. Allowed values: "Bank", "Customer", empty. |
| 227 | `PP.OEYG.AuthorisedMandate` | `PpOrderEntry_Authorisedmandate` | TField |  | Indicates if the Mandate is authorised or not. Possible values: "Y" - Mandate was authorized, "N" - Mandate was unauthorized, "" - empty (mandate is notrequired for current payment). Validation Rules: 1 alphabetic character. Allowed values: "Y", "N", empty value. |
| 228 | `PP.OEYG.TransactionReferenceIncoming` | `PpOrderEntry_Transactionreferenceincoming` | TField |  | Indicates the related reference of a payment. For a clearing payment will represent the value of the original transaction that was returned/refunded.. Validation Rules: 35 alphabetic characters. Allowed values: any string. |
| 229 | `PP.OEYG.OrgSetlDate` | `PpOrderEntry_Orgsetldate` | TField |  | Indicates the original settlement date meaning the credit/debit value date of the original payment. Validation Rules: Standard DATE format of length 11 characters. NOINPUT field. |
| 230 | `PP.OEYG.OrgCollectionDate` | `PpOrderEntry_Orgcollectiondate` | TField |  | Indicates the original settlement date meaning the requested collection date of the original payment. Validation Rules: Standard DATE format of length 11 characters. NOINPUT field. |
| 231 | `PP.OEYG.BeneficiaryID` | `PpOrderEntry_Beneficiaryid` | TField |  | When the ID of the BENEFICIARY table is input, the details defined in the BENEFICIARY table get defaulted.Accepts ID of the BENEFICIARY table. |
| 232 | `PP.OEYG.LocInstProp` | `PpOrderEntry_Locinstprop` | TField |  | Local Instrument Proprietary This field specifies Proprietaries specified by the Local Authorities. This field will be updated in"PI.INFORMATION.LINE" in the table POR.SUPPLEMENTARY.INFO. The "PI.INFORMATIONCODE" will be updated as "INSBNK" and the "PI.INSTRUCTION.CODE" will be "LCLINSPY". |
| 233 | `PP.OEYG.TransPurpProp` | `PpOrderEntry_Transpurpprop` | TField |  | Transaction Purpose Proprietary This field specifies the underlying reason for the transaction in Proprietary form. This field will be updated in"PI.INFORMATION.LINE" in the table POR.SUPPLEMENTARY.INFO. The "PI.INFORMATIONCODE" will be updated as "INSSDR" and the "PI.INSTRUCTION.CODE" will be "TXPURPPY". |
| 234 | `PP.OEYG.ChequeNumber` | `PpOrderEntry_Chequenumber` | TField |  |  |
| 235 | `PP.OEYG.BeneficiaryPartyTagOption` | `PpOrderEntry_Beneficiarypartytagoption` | TField |  | The field can contain the following values: F or "blank". The field can be used for Order Entry mode in case of Outgoing/Redirect CTR payments. If the operator wants toimpose the tag option 59F or 59 he can do so by setting this field. The data inputted by the operator will bepresent in the respective tags of the outgoing message. |
| 236 | `PP.OEYG.ChequeStatus` | `PpOrderEntry_Chequestatus` | TField |  | This field will hold the status of cheque. Possible Values: DEPOSITED CLEARED RETURNED |
| 237 | `PP.OEYG.SenderClearingSystemIdCode` | `PpOrderEntry_Senderclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Sender Financial Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 238 | `PP.OEYG.ReceiverClearingSystemIdCode` | `PpOrderEntry_Receiverclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Receiver Financial Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 239 | `PP.OEYG.OrdInstClearingSystemIdCode` | `PpOrderEntry_Ordinstclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Ordering Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 240 | `PP.OEYG.SenderCorrClearingSystemIdCode` | `PpOrderEntry_Sendercorrclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Sender Corresponding Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 241 | `PP.OEYG.ReceivCorrClearingSystemIdCode` | `PpOrderEntry_Receivcorrclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Receiver Corresponding Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 242 | `PP.OEYG.ThirdReimClearingSystemIdCode` | `PpOrderEntry_Thirdreimclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Third Reimbursement Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 243 | `PP.OEYG.InterClearingSystemIdCode` | `PpOrderEntry_Interclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Intermediary Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 244 | `PP.OEYG.AcntWithClearingSystemIdCode` | `PpOrderEntry_Acntwithclearingsystemidcode` | TField | Yes | This field is used to edit/view the ISO Clearing System Code of Account with Institution. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 245 | `PP.OEYG.UltCrdAddrLine` | `PpOrderEntry_Ultcrdaddrline` |  |  |  |
| 246 | `PP.OEYG.UltCrdCtry` | `PpOrderEntry_Ultcrdctry` | TField |  | Holds the country of ultimate creditor |
| 247 | `PP.OEYG.UltDbtAddrLine` | `PpOrderEntry_Ultdbtaddrline` |  |  |  |
| 248 | `PP.OEYG.UltDbtCtry` | `PpOrderEntry_Ultdbtctry` | TField |  | Holds the country of ultimate Debtor |
| 249 | `PP.OEYG.UniqueEndToEndRef` | `PpOrderEntry_Uniqueendtoendref` | TField | Yes | This field must be filled with the received UETR from the incoming SWIFT message Validation Rules: Non mandatory field This field hold 36 char length of reference |
| 250 | `PP.OEYG.PreviewReference` | `PpOrderEntry_Previewreference` |  |  |  |
| 251 | `PP.OEYG.ReverseMapFlag` | `PpOrderEntry_Reversemapflag` | TField |  |  |
| 252 | `PP.OEYG.LOCAL.REF` | `PpOrderEntry_LocalRef` |  |  |  |
| 253 | `PP.OEYG.OVERRIDE` | `PpOrderEntry_Override` |  |  |  |
| 254 | `PP.OEYG.RECORD.STATUS` | `PpOrderEntry_RecordStatus` | String |  |  |
| 255 | `PP.OEYG.CURR.NO` | `PpOrderEntry_CurrNo` | String |  |  |
| 256 | `PP.OEYG.INPUTTER` | `PpOrderEntry_Inputter` |  |  |  |
| 257 | `PP.OEYG.DATE.TIME` | `PpOrderEntry_DateTime` |  |  |  |
| 258 | `PP.OEYG.AUTHORISER` | `PpOrderEntry_Authoriser` | String |  |  |
| 259 | `PP.OEYG.CO.CODE` | `PpOrderEntry_CoCode` | String |  |  |
| 260 | `PP.OEYG.DEPT.CODE` | `PpOrderEntry_DeptCode` | String |  |  |
| 261 | `PP.OEYG.AUDITOR.CODE` | `PpOrderEntry_AuditorCode` | String |  |  |
| 262 | `PP.OEYG.AUDIT.DATE.TIME` | `PpOrderEntry_AuditDateTime` | String |  |  |
| 263 | `PP.OEYG.PaymentServiceLevelCode` | `PpOrderEntry_Paymentservicelevelcode` | TField |  |  |
| 264 | `PP.OEYG.ExposureDate` | `PpOrderEntry_Exposuredate` | TField |  | This is the date from which funds are available to the party for withdrawal. |
| 265 | `PP.OEYG.FileReferenceOutgoing` | `PpOrderEntry_Filereferenceoutgoing` | TField |  | The reference of the file in which this transaction has been incorporated. |
| 266 | `PP.OEYG.OriginalTransactionRef` | `PpOrderEntry_Originaltransactionref` | TField |  | It is the Original Transaction Reference which is considered to be already present in the Database. |
| 267 | `PP.OEYG.OriginalMsgId` | `PpOrderEntry_Originalmsgid` | TField |  | Point to point reference of the underlying message for which the return is initiated, as assigned by the instructing party, and sent to the next party in the chain to unambiguously identify the message. |
| 268 | `PP.OEYG.SendersReferenceOutgoing` | `PpOrderEntry_Sendersreferenceoutgoing` | TField |  |  |
| 269 | `PP.OEYG.LocalFieldName` | `PpOrderEntry_Localfieldname` |  |  |  |
| 270 | `PP.OEYG.LocalFieldValue` | `PpOrderEntry_Localfieldvalue` |  |  |  |
| 271 | `PP.OEYG.OrderingCtryResidence` | `PpOrderEntry_Orderingctryresidence` | TField |  | Nation with its own government |
| 272 | `PP.OEYG.OrderingTownName` | `PpOrderEntry_Orderingtownname` | TField |  | Name of a built-up area, with defined boundaries, and a local government |
| 273 | `PP.OEYG.DebtorLEI` | `PpOrderEntry_Debtorlei` | TField |  | Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)". |
| 274 | `PP.OEYG.BeneficiaryCtryResidence` | `PpOrderEntry_Beneficiaryctryresidence` | TField |  | country residing in beneficiary side |
| 275 | `PP.OEYG.BeneficiaryTownName` | `PpOrderEntry_Beneficiarytownname` | TField |  | Name of a built-up area, with defined boundaries, and a local government for beneficiary side. |
| 276 | `PP.OEYG.CreditorLEI` | `PpOrderEntry_Creditorlei` | TField |  | Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)". |
| 277 | `PP.OEYG.UltDbtTownName` | `PpOrderEntry_Ultdbttownname` | TField |  | Name of the built-up area, with defined boundaries for the ulimate debtor side. |
| 278 | `PP.OEYG.UltDbtLEI` | `PpOrderEntry_Ultdbtlei` | TField |  | Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)". |
| 279 | `PP.OEYG.UltCrdTownName` | `PpOrderEntry_Ultcrdtownname` | TField |  | Name of the built up area, with defined boundaries for ultimate creditor side. |
| 280 | `PP.OEYG.UltCrdLEI` | `PpOrderEntry_Ultcrdlei` | TField |  | Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)". |
| 281 | `PP.OEYG.PrvInstAgt1BIC` | `PpOrderEntry_Prvinstagt1bic` | TField |  | BIC value for Previous instructing institution. the value should be present in BIC table |
| 282 | `PP.OEYG.PrvInstAgt2BIC` | `PpOrderEntry_Prvinstagt2bic` | TField |  | BIC value for the second Previous instructing institution. The BIC should present in BIC table. If Previous instructing Institution 2 - BIC is present, then Previous instructing Institution 1 - BIC must bepresent |
| 283 | `PP.OEYG.PrvInstAgt3BIC` | `PpOrderEntry_Prvinstagt3bic` | TField |  | BIC value for the second Previous instructing institution. The BIC should present in BIC table. If Previous instructing Institution 3 - BIC is present, then Previous instructing Institution 2 - BIC must bepresent |
| 284 | `PP.OEYG.RegDebtorCreditorRpt` | `PpOrderEntry_Regdebtorcreditorrpt` |  |  |  |
| 285 | `PP.OEYG.RegRepCountryCd` | `PpOrderEntry_Regrepcountrycd` |  |  |  |
| 286 | `PP.OEYG.RegRepInformation` | `PpOrderEntry_Regrepinformation` |  |  |  |
| 287 | `PP.OEYG.ClearingSystemRef` | `PpOrderEntry_Clearingsystemref` | TField |  |  |
| 288 | `PP.OEYG.ServiceLevelCode` | `PpOrderEntry_Servicelevelcode` |  |  |  |
| 289 | `PP.OEYG.ServiceLevelProp` | `PpOrderEntry_Servicelevelprop` |  |  |  |
| 290 | `PP.OEYG.LocalInstCode` | `PpOrderEntry_Localinstcode` | TField |  | Indicates the local instrument of the instruction. This field is a code as published in an external list. |
| 291 | `PP.OEYG.OriginatingChannel` | `PpOrderEntry_Originatingchannel` | TField |  | If Originating Channel is selected not as SWIFT (so a SWIFT based clearing), then DebitMainAccount should bedetermined from ClearingSetting (see Debit Credit Info screen:DebitMainAccount) If Originating Channel is selected as SWIFT, then DebitMainAccount should be determined from LoroNostro Table asper existing logic based on the Sender Institution, see next field). SWIFT will be supported during CBPR SWIFT migration |
| 292 | `PP.OEYG.CrAgtInstructionCode` | `PpOrderEntry_Cragtinstructioncode` |  |  |  |
| 293 | `PP.OEYG.CrAgtInstructionInformation` | `PpOrderEntry_Cragtinstructioninformation` |  |  |  |
| 294 | `PP.OEYG.NxtAgtInstructionInformation` | `PpOrderEntry_Nxtagtinstructioninformation` |  |  |  |
| 295 | `PP.OEYG.InstructionIdentification` | `PpOrderEntry_Instructionidentification` | TField |  | To Input the Message reference. |
| 296 | `PP.OEYG.RemittanceInformation` | `PpOrderEntry_Remittanceinformation` | TField |  | To Input the Remittance Information(Unstructured). |
| 297 | `PP.OEYG.OrderingCustomerId` | `PpOrderEntry_Orderingcustomerid` | TField |  | Indicates the Id or reference of the ordering customer. |
| 298 | `PP.OEYG.Structured` | `PpOrderEntry_Structured` |  |  |  |
| 299 | `PP.OEYG.RefDocInfTpCdOrPropCd` | `PpOrderEntry_Refdocinftpcdorpropcd` |  |  |  |
| 300 | `PP.OEYG.RefDocInfNr` | `PpOrderEntry_Refdocinfnr` |  |  |  |
| 301 | `PP.OEYG.RefDocAmRemittedAm` | `PpOrderEntry_Refdocamremittedam` |  |  |  |
| 302 | `PP.OEYG.RefDocAmRemittedAmCcy` | `PpOrderEntry_Refdocamremittedamccy` |  |  |  |
| 303 | `PP.OEYG.RefDocAmCrNoteAm` | `PpOrderEntry_Refdocamcrnoteam` |  |  |  |
| 304 | `PP.OEYG.RefDocAmCrNoteAmCcy` | `PpOrderEntry_Refdocamcrnoteamccy` |  |  |  |
| 305 | `PP.OEYG.CrdRefInfTpProp` | `PpOrderEntry_Crdrefinftpprop` |  |  |  |
| 306 | `PP.OEYG.AdRemittanceInf1` | `PpOrderEntry_Adremittanceinf1` |  |  |  |
| 307 | `PP.OEYG.ChequeType` | `PpOrderEntry_Chequetype` | TField |  |  |
| 308 | `PP.OEYG.SettlementPriority` | `PpOrderEntry_Settlementpriority` | TField |  | Identifies the settlement priority of the message. Allowed values are NORM,HIGH,URGT |
| 309 | `PP.OEYG.DebtorStreetName` | `PpOrderEntry_Debtorstreetname` | TField |  | Identifies the street name of the debtor or Ordering customer |
| 310 | `PP.OEYG.DebtorBuildingNumber` | `PpOrderEntry_Debtorbuildingnumber` | TField |  | Identifies the Building number of the debtor or Ordering customer |
| 311 | `PP.OEYG.DebtorBuildingName` | `PpOrderEntry_Debtorbuildingname` | TField |  | Identifies the Building Name of the debtor or Ordering customer |
| 312 | `PP.OEYG.DebtorDepartment` | `PpOrderEntry_Debtordepartment` | TField |  | Identifies the Department Name of the debtor or Ordering customer |
| 313 | `PP.OEYG.DebtorSubDepartment` | `PpOrderEntry_Debtorsubdepartment` | TField |  | Identifies the Sub Department Name of the debtor or Ordering customer |
| 314 | `PP.OEYG.DebtorFloor` | `PpOrderEntry_Debtorfloor` | TField |  | Identifies the Sub Floor Name of the debtor or Ordering customer |
| 315 | `PP.OEYG.DebtorRoom` | `PpOrderEntry_Debtorroom` | TField |  | Identifies the Sub Room Number/Name of the debtor or Ordering customer |
| 316 | `PP.OEYG.DebtorPostBox` | `PpOrderEntry_Debtorpostbox` | TField |  | Identifies the Post Box Number of the debtor or Ordering customer |
| 317 | `PP.OEYG.DebtorPostCode` | `PpOrderEntry_Debtorpostcode` | TField |  | Identifies the Postal Code of the debtor or Ordering customer |
| 318 | `PP.OEYG.DebtorTownLocationName` | `PpOrderEntry_Debtortownlocationname` | TField |  | Identifies the Town Location Name of the debtor or Ordering customer |
| 319 | `PP.OEYG.DebtorDistrictName` | `PpOrderEntry_Debtordistrictname` | TField |  | Identifies the District Name of the debtor or Ordering customer |
| 320 | `PP.OEYG.DebtorCountrySubDivision` | `PpOrderEntry_Debtorcountrysubdivision` | TField |  | Identifies the Country Sub Division of the debtor or Ordering customer |
| 321 | `PP.OEYG.CreditorStreetName` | `PpOrderEntry_Creditorstreetname` | TField |  | Identifies the street name of the Creditor or Beneficiary customer |
| 322 | `PP.OEYG.CreditorBuildingNumber` | `PpOrderEntry_Creditorbuildingnumber` | TField |  | Identifies the Building number of the Creditor or Beneficiary customer |
| 323 | `PP.OEYG.CreditorBuildingName` | `PpOrderEntry_Creditorbuildingname` | TField |  | Identifies the Building Name of the Creditor or Beneficiary customer |
| 324 | `PP.OEYG.CreditorDepartment` | `PpOrderEntry_Creditordepartment` | TField |  | Identifies the Department Name of the Creditor or Beneficiary customer |
| 325 | `PP.OEYG.CreditorSubDepartment` | `PpOrderEntry_Creditorsubdepartment` | TField |  | Identifies the Sub Department Name of the Creditor or Beneficiary customer |
| 326 | `PP.OEYG.CreditorFloor` | `PpOrderEntry_Creditorfloor` | TField |  | Identifies the Sub Floor Name of the Creditor or Beneficiary customer |
| 327 | `PP.OEYG.CreditorRoom` | `PpOrderEntry_Creditorroom` | TField |  | Identifies the Sub Room Number/Name of the Creditor or Beneficiary customer |
| 328 | `PP.OEYG.CreditorPostBox` | `PpOrderEntry_Creditorpostbox` | TField |  | Identifies the Post Box Number of the Creditor or Beneficiary customer |
| 329 | `PP.OEYG.CreditorPostCode` | `PpOrderEntry_Creditorpostcode` | TField |  | Identifies the Postal Code of the Creditor or Beneficiary customer |
| 330 | `PP.OEYG.CreditorTownLocationName` | `PpOrderEntry_Creditortownlocationname` | TField |  | Identifies the Town Location Name of the Creditor or Beneficiary customer |
| 331 | `PP.OEYG.CreditorDistrictName` | `PpOrderEntry_Creditordistrictname` | TField |  | Identifies the District Name of the Creditor or Beneficiary customer |
| 332 | `PP.OEYG.CreditorCountrySubDivision` | `PpOrderEntry_Creditorcountrysubdivision` | TField |  | Identifies the Country Sub Division of the Creditor or Beneficiary customer |
| 333 | `PP.OEYG.AccountWithInstClrsysMmbid` | `PpOrderEntry_Accountwithinstclrsysmmbid` | TField |  | Creditor Agent clearing system member id. |
| 334 | `PP.OEYG.AccountWithInstLEI` | `PpOrderEntry_Accountwithinstlei` | TField |  | Legal Entity identifier of creditor agent |
| 335 | `PP.OEYG.AccountWithInstName` | `PpOrderEntry_Accountwithinstname` | TField |  | Name of the creditor Agent |
| 336 | `PP.OEYG.AccountWithInstPostCode` | `PpOrderEntry_Accountwithinstpostcode` | TField |  | Postal code of the creditor Agent |
| 337 | `PP.OEYG.AccountWithInstTownName` | `PpOrderEntry_Accountwithinsttownname` | TField |  | Town Name of the creditor Agent |
| 338 | `PP.OEYG.AccountWithInstCountry` | `PpOrderEntry_Accountwithinstcountry` | TField |  | Country Code of the creditor Agent |
| 339 | `PP.OEYG.OrderingInstClrsysMmbid` | `PpOrderEntry_Orderinginstclrsysmmbid` | TField |  | Debtor Agent clearing system member id. |
| 340 | `PP.OEYG.OrderingInstLEI` | `PpOrderEntry_Orderinginstlei` | TField |  | Legal Entity identifier of the Debtor agent |
| 341 | `PP.OEYG.OrderingInstName` | `PpOrderEntry_Orderinginstname` | TField |  | Name of the Debtor Agent |
| 342 | `PP.OEYG.OrderingInstPostCode` | `PpOrderEntry_Orderinginstpostcode` | TField |  | Postal code of the creditor Agent |
| 343 | `PP.OEYG.OrderingInstTownName` | `PpOrderEntry_Orderinginsttownname` | TField |  | Town Name of the creditor Agent |
| 344 | `PP.OEYG.OrderingInstCountry` | `PpOrderEntry_Orderinginstcountry` | TField |  | Country Code of the creditor Agent |
| 345 | `PP.OEYG.IntermediaryClrsysMmbid` | `PpOrderEntry_Intermediaryclrsysmmbid` | TField |  | Intermediary Agent1 clearing system member id. |
| 346 | `PP.OEYG.IntermediaryLEI` | `PpOrderEntry_Intermediarylei` | TField |  | Legal Entity identifier of the Intermediary Agent1 |
| 347 | `PP.OEYG.IntermediaryName` | `PpOrderEntry_Intermediaryname` | TField |  | Name of the Intermediary Agent1 |
| 348 | `PP.OEYG.IntermediaryPostCode` | `PpOrderEntry_Intermediarypostcode` | TField |  | Postal code of the Intermediary Agent1 |
| 349 | `PP.OEYG.IntermediaryTownName` | `PpOrderEntry_Intermediarytownname` | TField |  | Town Name of the Intermediary Agent1 |
| 350 | `PP.OEYG.IntermediaryCountry` | `PpOrderEntry_Intermediarycountry` | TField |  | Country Code of the Intermediary Agent1 |
| 351 | `PP.OEYG.Intermediary2IdentifierCode` | `PpOrderEntry_Intermediary2identifiercode` | TField |  | BIC of Intermediary Agent2 |
| 352 | `PP.OEYG.Intermediary2ClrsysMmbid` | `PpOrderEntry_Intermediary2clrsysmmbid` | TField |  | Intermediary Agent2 clearing system member id. |
| 353 | `PP.OEYG.Intermediary2ClrgsystemidCode` | `PpOrderEntry_Intermediary2clrgsystemidcode` | TField |  |  |
| 354 | `PP.OEYG.Intermediary2LEI` | `PpOrderEntry_Intermediary2lei` | TField |  | Legal Entity identifier of the Intermediary Agent2 |
| 355 | `PP.OEYG.Intermediary2Name` | `PpOrderEntry_Intermediary2name` | TField |  | Name of the Intermediary Agent2 |
| 356 | `PP.OEYG.Intermediary2PostCode` | `PpOrderEntry_Intermediary2postcode` | TField |  |  |
| 357 | `PP.OEYG.Intermediary2TownName` | `PpOrderEntry_Intermediary2townname` | TField |  | Town Name of the Intermediary Agent2 |
| 358 | `PP.OEYG.Intermediary2Country` | `PpOrderEntry_Intermediary2country` | TField |  | Country Code of the Intermediary Agent2 |
| 359 | `PP.OEYG.Intermediary2Address` | `PpOrderEntry_Intermediary2address` |  |  |  |
| 360 | `PP.OEYG.Intermediary2Account` | `PpOrderEntry_Intermediary2account` | TField |  | Account number of Intermediary Agent2 |
| 361 | `PP.OEYG.Intermediary3IdentifierCode` | `PpOrderEntry_Intermediary3identifiercode` | TField |  | BIC of Intermediary Agent3 |
| 362 | `PP.OEYG.Intermediary3ClrsysMmbid` | `PpOrderEntry_Intermediary3clrsysmmbid` | TField |  | Intermediary Agent3 clearing system member id. |
| 363 | `PP.OEYG.Intermediary3ClrgsystemidCode` | `PpOrderEntry_Intermediary3clrgsystemidcode` | TField |  |  |
| 364 | `PP.OEYG.Intermediary3LEI` | `PpOrderEntry_Intermediary3lei` | TField |  | Legal Entity identifier of the Intermediary Agent3 |
| 365 | `PP.OEYG.Intermediary3Name` | `PpOrderEntry_Intermediary3name` | TField |  | Name of the Intermediary Agent3 |
| 366 | `PP.OEYG.Intermediary3PostCode` | `PpOrderEntry_Intermediary3postcode` | TField |  | Postal code of the Intermediary Agent3 |
| 367 | `PP.OEYG.Intermediary3TownName` | `PpOrderEntry_Intermediary3townname` | TField |  | Town Name of the Intermediary Agent3 |
| 368 | `PP.OEYG.Intermediary3Country` | `PpOrderEntry_Intermediary3country` | TField |  | Country Code of the Intermediary Agent3 |
| 369 | `PP.OEYG.Intermediary3Address` | `PpOrderEntry_Intermediary3address` |  |  |  |
| 370 | `PP.OEYG.Intermediary3Account` | `PpOrderEntry_Intermediary3account` | TField |  | Account number of Intermediary Agent3 |
| 371 | `PP.OEYG.SenderCorClrsysMmbid` | `PpOrderEntry_Sendercorclrsysmmbid` | TField |  | Senders Correspondent/Instructing Reimbursement Agent clearing system member id. |
| 372 | `PP.OEYG.SenderCorLEI` | `PpOrderEntry_Sendercorlei` | TField |  | Legal Entity identifier of the Senders Correspondent/Instructing Reimbursement Agent |
| 373 | `PP.OEYG.SenderCorName` | `PpOrderEntry_Sendercorname` | TField |  | Name of the Senders correspondent/ Instructing Reimbursement Agent |
| 374 | `PP.OEYG.SenderCorPostCode` | `PpOrderEntry_Sendercorpostcode` | TField |  | Postal code of the Senders correspondent/ Instructing Reimbursement Agent |
| 375 | `PP.OEYG.SenderCorTownName` | `PpOrderEntry_Sendercortownname` | TField |  | Town Name of the Senders correspondent/ Instructing Reimbursement Agent |
| 376 | `PP.OEYG.SenderCorCountry` | `PpOrderEntry_Sendercorcountry` | TField |  | Country Name of the Senders correspondent/ Instructing Reimbursement Agent |
| 377 | `PP.OEYG.ReceiverCorClrsysMmbid` | `PpOrderEntry_Receivercorclrsysmmbid` | TField |  | Receivers Correspondent/Instructed Reimbursement Agent clearing system member id. |
| 378 | `PP.OEYG.ReceiverCorLEI` | `PpOrderEntry_Receivercorlei` | TField |  | Legal Entity identifier of the Receivers Correspondent/Instructed Reimbursement Agent |
| 379 | `PP.OEYG.ReceiverCorName` | `PpOrderEntry_Receivercorname` | TField |  | Name of the Receivers Correspondent/Instructed Reimbursement Agent |
| 380 | `PP.OEYG.ReceiverCorPostCode` | `PpOrderEntry_Receivercorpostcode` | TField |  | Postal code of the Receivers Correspondent/Instructed Reimbursement Agent |
| 381 | `PP.OEYG.ReceiverCorTownName` | `PpOrderEntry_Receivercortownname` | TField |  | Town Name of the Receivers Correspondent/Instructed Reimbursement Agent |
| 382 | `PP.OEYG.ReceiverCorCountry` | `PpOrderEntry_Receivercorcountry` | TField |  | Country Code of the Receivers Correspondent/Instructed Reimbursement Agent |
| 383 | `PP.OEYG.ThirdReimClrsysMmbid` | `PpOrderEntry_Thirdreimclrsysmmbid` | TField |  | Third Reimbursement Agent clearing system member id. |
| 384 | `PP.OEYG.ThirdReimLEI` | `PpOrderEntry_Thirdreimlei` | TField |  | Legal Entity identifier of the Third Reimbursement Agent |
| 385 | `PP.OEYG.ThirdReimName` | `PpOrderEntry_Thirdreimname` | TField |  | Name of the Third Reimbursement Agent |
| 386 | `PP.OEYG.ThirdReimPostCode` | `PpOrderEntry_Thirdreimpostcode` | TField |  | Postal code of the Third Reimbursement Agent |
| 387 | `PP.OEYG.ThirdReimTownName` | `PpOrderEntry_Thirdreimtownname` | TField |  | Town Name of the Third Reimbursement Agent |
| 388 | `PP.OEYG.ThirdReimCountry` | `PpOrderEntry_Thirdreimcountry` | TField |  | Country Code of the Third Reimbursement Agent |
| 389 | `PP.OEYG.UltdbtDepartment` | `PpOrderEntry_Ultdbtdepartment` | TField |  | Department Name of Ultimate Debtor |
| 390 | `PP.OEYG.UltdbtSubDepartment` | `PpOrderEntry_Ultdbtsubdepartment` | TField |  | Sub Department Name of Ultimate Debtor |
| 391 | `PP.OEYG.UltdbtStreetName` | `PpOrderEntry_Ultdbtstreetname` | TField |  | Street Name of Ultimate Debtor |
| 392 | `PP.OEYG.UltdbtBuildingNumber` | `PpOrderEntry_Ultdbtbuildingnumber` | TField |  | Building Number of Ultimate Debtor |
| 393 | `PP.OEYG.UltdbtBuildingName` | `PpOrderEntry_Ultdbtbuildingname` | TField |  | Building Name of Ultimate Debtor |
| 394 | `PP.OEYG.UltdbtFloor` | `PpOrderEntry_Ultdbtfloor` | TField |  | Floor Number of Ultimate Debtor |
| 395 | `PP.OEYG.UltdbtPostBox` | `PpOrderEntry_Ultdbtpostbox` | TField |  | Post Box Number of Ultimate Debtor |
| 396 | `PP.OEYG.UltdbtRoom` | `PpOrderEntry_Ultdbtroom` | TField |  | Room Number of Ultimate Debtor |
| 397 | `PP.OEYG.UltdbtPostCode` | `PpOrderEntry_Ultdbtpostcode` | TField |  | Postal Code of Ultimate Debtor |
| 398 | `PP.OEYG.UltdbtTownLocationName` | `PpOrderEntry_Ultdbttownlocationname` | TField |  | Town Location Name of Ultimate Debtor |
| 399 | `PP.OEYG.UltdbtDistrictName` | `PpOrderEntry_Ultdbtdistrictname` | TField |  | District Name of Ultimate Debtor |
| 400 | `PP.OEYG.UltdbtCountrySubDivision` | `PpOrderEntry_Ultdbtcountrysubdivision` | TField |  | Country Subdivision of Ultimate Debtor |
| 401 | `PP.OEYG.UltdbtCountryofResidence` | `PpOrderEntry_Ultdbtcountryofresidence` | TField |  | Residence Country Code of Ultimate Debtor |
| 402 | `PP.OEYG.UltCrdDepartment` | `PpOrderEntry_Ultcrddepartment` | TField |  | Department Name of Ultimate Creditor |
| 403 | `PP.OEYG.UltCrdSubDepartment` | `PpOrderEntry_Ultcrdsubdepartment` | TField |  | Sub Department Name of Ultimate Creditor |
| 404 | `PP.OEYG.UltCrdStreetName` | `PpOrderEntry_Ultcrdstreetname` | TField |  | Street Name of Ultimate Creditor |
| 405 | `PP.OEYG.UltCrdBuildingNumber` | `PpOrderEntry_Ultcrdbuildingnumber` | TField |  | Building Number of Ultimate Creditor |
| 406 | `PP.OEYG.UltCrdBuildingName` | `PpOrderEntry_Ultcrdbuildingname` | TField |  | Building Name of Ultimate Creditor |
| 407 | `PP.OEYG.UltCrdFloor` | `PpOrderEntry_Ultcrdfloor` | TField |  | Floor Number of Ultimate Creditor |
| 408 | `PP.OEYG.UltCrdPostBox` | `PpOrderEntry_Ultcrdpostbox` | TField |  | Post Box Number of Ultimate Creditor |
| 409 | `PP.OEYG.UltCrdRoom` | `PpOrderEntry_Ultcrdroom` | TField |  | Room Number of Ultimate Creditor |
| 410 | `PP.OEYG.UltCrdPostCode` | `PpOrderEntry_Ultcrdpostcode` | TField |  | Postal Code of Ultimate Creditor |
| 411 | `PP.OEYG.UltCrdTownLocationName` | `PpOrderEntry_Ultcrdtownlocationname` | TField |  | Town Location Name of Ultimate Creditor |
| 412 | `PP.OEYG.UltCrdDistrictName` | `PpOrderEntry_Ultcrddistrictname` | TField |  | District Name of Ultimate Creditor |
| 413 | `PP.OEYG.UltCrdCountrySubDivision` | `PpOrderEntry_Ultcrdcountrysubdivision` | TField |  | Country Subdivision of Ultimate Creditor |
| 414 | `PP.OEYG.UltCrdCountryofResidence` | `PpOrderEntry_Ultcrdcountryofresidence` | TField |  | Residence Country Code of Ultimate Creditor |
| 415 | `PP.OEYG.RegrepAuthorityName` | `PpOrderEntry_Regrepauthorityname` |  |  |  |
| 416 | `PP.OEYG.RegrepAuthorityCountry` | `PpOrderEntry_Regrepauthoritycountry` |  |  |  |
| 417 | `PP.OEYG.Regreptype` | `PpOrderEntry_Regreptype` |  |  |  |
| 418 | `PP.OEYG.RegrepDate` | `PpOrderEntry_Regrepdate` |  |  |  |
| 419 | `PP.OEYG.RegrepCode` | `PpOrderEntry_Regrepcode` |  |  |  |
| 420 | `PP.OEYG.RegrepAmount` | `PpOrderEntry_Regrepamount` |  |  |  |
| 421 | `PP.OEYG.RegrepAmountCurrency` | `PpOrderEntry_Regrepamountcurrency` |  |  |  |
| 422 | `PP.OEYG.Prvinstagt1clrgsystemIdCode` | `PpOrderEntry_Prvinstagt1clrgsystemidcode` | TField |  |  |
| 423 | `PP.OEYG.Prvinstagt1ClrsysMmbid` | `PpOrderEntry_Prvinstagt1clrsysmmbid` | TField |  | Previous Instructing Agent1 clearing system member id. |
| 424 | `PP.OEYG.Prvinstagt1LEI` | `PpOrderEntry_Prvinstagt1lei` | TField |  | Legal Entity identifier of Previous Instructing Agent1 |
| 425 | `PP.OEYG.Prvinstagt1Name` | `PpOrderEntry_Prvinstagt1name` | TField |  | Name of the Previous Instructing Agent1 |
| 426 | `PP.OEYG.Prvinstagt1PostCode` | `PpOrderEntry_Prvinstagt1postcode` | TField |  | Postal code of the Previous Instructing Agent1 |
| 427 | `PP.OEYG.Prvinstagt1TownName` | `PpOrderEntry_Prvinstagt1townname` | TField |  | Town Name of the Previous Instructing Agent1 |
| 428 | `PP.OEYG.Prvinstagt1Country` | `PpOrderEntry_Prvinstagt1country` | TField |  | Country Code of the Previous Instructing Agent1 |
| 429 | `PP.OEYG.Prvinstagt1Address` | `PpOrderEntry_Prvinstagt1address` |  |  |  |
| 430 | `PP.OEYG.Prvinstagt1AccountNumber` | `PpOrderEntry_Prvinstagt1accountnumber` | TField |  | Account number of Previous Instructing Agent1 |
| 431 | `PP.OEYG.Prvinstagt2clrgsystemIdCode` | `PpOrderEntry_Prvinstagt2clrgsystemidcode` | TField |  |  |
| 432 | `PP.OEYG.Prvinstagt2ClrsysMmbid` | `PpOrderEntry_Prvinstagt2clrsysmmbid` | TField |  | Previous Instructing Agent2 clearing system member id. |
| 433 | `PP.OEYG.Prvinstagt2LEI` | `PpOrderEntry_Prvinstagt2lei` | TField |  | Legal Entity identifier of Previous Instructing Agent2 |
| 434 | `PP.OEYG.Prvinstagt2Name` | `PpOrderEntry_Prvinstagt2name` | TField |  | Name of the Previous Instructing Agent2 |
| 435 | `PP.OEYG.Prvinstagt2PostCode` | `PpOrderEntry_Prvinstagt2postcode` | TField |  | Postal code of the Previous Instructing Agent2 |
| 436 | `PP.OEYG.Prvinstagt2TownName` | `PpOrderEntry_Prvinstagt2townname` | TField |  | Town Name of the Previous Instructing Agent2 |
| 437 | `PP.OEYG.Prvinstagt2Country` | `PpOrderEntry_Prvinstagt2country` | TField |  | Country Code of the Previous Instructing Agent2 |
| 438 | `PP.OEYG.Prvinstagt2Address` | `PpOrderEntry_Prvinstagt2address` |  |  |  |
| 439 | `PP.OEYG.Prvinstagt2AccountNumber` | `PpOrderEntry_Prvinstagt2accountnumber` | TField |  | Account number of Previous Instructing Agent2 |
| 440 | `PP.OEYG.Prvinstagt3clrgsystemIdCode` | `PpOrderEntry_Prvinstagt3clrgsystemidcode` | TField |  |  |
| 441 | `PP.OEYG.Prvinstagt3ClrsysMmbid` | `PpOrderEntry_Prvinstagt3clrsysmmbid` | TField |  | Previous Instructing Agent3 clearing system member id. |
| 442 | `PP.OEYG.Prvinstagt3LEI` | `PpOrderEntry_Prvinstagt3lei` | TField |  | Legal Entity identifier of Previous Instructing Agent3 |
| 443 | `PP.OEYG.Prvinstagt3Name` | `PpOrderEntry_Prvinstagt3name` | TField |  | Name of the Previous Instructing Agent3 |
| 444 | `PP.OEYG.Prvinstagt3PostCode` | `PpOrderEntry_Prvinstagt3postcode` | TField |  | Postal code of the Previous Instructing Agent3 |
| 445 | `PP.OEYG.Prvinstagt3TownName` | `PpOrderEntry_Prvinstagt3townname` | TField |  | Town Name of the Previous Instructing Agent3 |
| 446 | `PP.OEYG.Prvinstagt3Country` | `PpOrderEntry_Prvinstagt3country` | TField |  | Country Code of the Previous Instructing Agent3 |
| 447 | `PP.OEYG.Prvinstagt3Address` | `PpOrderEntry_Prvinstagt3address` |  |  |  |
| 448 | `PP.OEYG.Prvinstagt3AccountNumber` | `PpOrderEntry_Prvinstagt3accountnumber` | TField |  | Account number of Previous Instructing Agent3 |
| 449 | `PP.OEYG.FromTime` | `PpOrderEntry_Fromtime` | TField |  | The time from which the settlement happens in clearing |
| 450 | `PP.OEYG.TillTime` | `PpOrderEntry_Tilltime` | TField |  | The time until which the payment can be settled in clearing |
| 451 | `PP.OEYG.RejectTime` | `PpOrderEntry_Rejecttime` | TField |  | If the payment is not settled within this time, clearing should reject the payment |
| 452 | `PP.OEYG.CLSTime` | `PpOrderEntry_Clstime` | TField |  | This is the clearing and settlement time. |
| 453 | `PP.OEYG.AdRemittanceInf2` | `PpOrderEntry_Adremittanceinf2` |  |  |  |
| 454 | `PP.OEYG.AdRemittanceInf3` | `PpOrderEntry_Adremittanceinf3` |  |  |  |
| 455 | `PP.OEYG.ReceiverMmbid` | `PpOrderEntry_Receivermmbid` | TField |  | Receiver member id. |
| 456 | `PP.OEYG.MessageData` | `PpOrderEntry_Messagedata` |  |  |  |
| 457 | `PP.OEYG.BeneficiaryClrsysIdCode` | `PpOrderEntry_Beneficiaryclrsysidcode` | TField |  | Identifies the Beneficiary Clearing system identification code |
| 458 | `PP.OEYG.BeneficiaryClrsysMmbid` | `PpOrderEntry_Beneficiaryclrsysmmbid` | TField |  | Identifies the Beneficiary Clearing system Member Id |
| 459 | `PP.OEYG.RegRepTypeRelation` | `PpOrderEntry_Regreptyperelation` |  |  |  |
| 460 | `PP.OEYG.SenderClearingMemberId` | `PpOrderEntry_Senderclearingmemberid` | TField |  | Identifies the Sender Clearing Member Id |
| 461 | `PP.OEYG.TaxType` | `PpOrderEntry_Taxtype` |  |  |  |
| 462 | `PP.OEYG.TaxIndicator` | `PpOrderEntry_Taxindicator` |  |  |  |
| 463 | `PP.OEYG.TaxAmount` | `PpOrderEntry_Taxamount` |  |  |  |
| 464 | `PP.OEYG.TaxCurrency` | `PpOrderEntry_Taxcurrency` |  |  |  |
| 465 | `PP.OEYG.TaxPartyIndicator` | `PpOrderEntry_Taxpartyindicator` |  |  |  |
| 466 | `PP.OEYG.AAChargeAccountType` | `PpOrderEntry_Aachargeaccounttype` |  |  |  |
| 467 | `PP.OEYG.AAChargeAmount` | `PpOrderEntry_Aachargeamount` |  |  |  |
| 468 | `PP.OEYG.Originalmsgnameid` | `PpOrderEntry_Originalmsgnameid` | TField |  | Originalmsgnameid(Existing Field - Needs to be modified to Dropdown with EB.LOOKUP values. Allowed values are pacs.009.001.08,camt.054.001.08,camt.053.001.08,MT910,MT940,MT950 |
| 469 | `PP.OEYG.ReturnOrgBIC` | `PpOrderEntry_Returnorgbic` | TField |  | Indicates BIC of the Originator of return payment |
| 470 | `PP.OEYG.ReturnOrgLEI` | `PpOrderEntry_Returnorglei` | TField |  | Indicates LEI of the Originator of return payment |
| 471 | `PP.OEYG.ReturnOrgName` | `PpOrderEntry_Returnorgname` | TField |  | Indicates Name of the Originator of return payment |
| 472 | `PP.OEYG.ReturnOrgPostCode` | `PpOrderEntry_Returnorgpostcode` | TField |  | Indicates PostCode of the Originator of return payment |
| 473 | `PP.OEYG.ReturnOrgTownName` | `PpOrderEntry_Returnorgtownname` | TField |  | Indicates TownName of the Originator of return payment |
| 474 | `PP.OEYG.ReturnOrgCountry` | `PpOrderEntry_Returnorgcountry` | TField |  | Indicates Country of the Originator of return payment |
| 475 | `PP.OEYG.ReturnOrgAddress` | `PpOrderEntry_Returnorgaddress` |  |  |  |
| 476 | `PP.OEYG.EXTERNAL.DEBIT.ACCOUNT` | `PpOrderEntry_ExternalDebitAccount` | TField |  | This field is to capture the corresponding account number of the Debit Account as maintained in an externalentity's system. Examples of external entity: A bank that holds a Vostro of a TPH bank, a Clearing System thatholds an account of a participant bank. |
| 477 | `PP.OEYG.EXTERNAL.CREDIT.ACCOUNT` | `PpOrderEntry_ExternalCreditAccount` | TField |  | This field is to capture the corresponding account number of the Credit Account as maintained in an externalentity's system. Examples of external entity: A bank that holds a Vostro of a TPH bank, a Clearing System thatholds an account of a participant bank. |
| 478 | `PP.OEYG.ReturnDescription2` | `PpOrderEntry_Returndescription2` |  |  |  |
| 479 | `PP.OEYG.ReservationType` | `PpOrderEntry_Reservationtype` | TField |  | This is used to store whether partial Funds have been reserved for the cheque payment or represented partial cheque Allowed values are None, Partial, Represented |
| 480 | `PP.OEYG.ReturnType` | `PpOrderEntry_Returntype` | TField |  | This field indicates the type of return Applicable values: Partial, Incomplete |
| 481 | `PP.OEYG.AAChargeType` | `PpOrderEntry_Aachargetype` |  |  |  |
| 482 | `PP.OEYG.CdtrAcctOthrIdSchmeCd` | `PpOrderEntry_Cdtracctothridschmecd` | TField |  | Code for the creditor / beneficiary account identification scheme The dropdown values are displayed from PI.ISO.EXTERNALCODE against id AcctSchemeNameCode |
| 483 | `PP.OEYG.CdtrAcctOthrIdSchemePrtry` | `PpOrderEntry_Cdtracctothridschemeprtry` | TField |  | Proprietary textual description for the creditor / beneficiary account identification scheme. |
| 484 | `PP.OEYG.CdtrAcctOthrIdIssr` | `PpOrderEntry_Cdtracctothridissr` | TField |  | Textual description of the entity that assigned the identification |
| 485 | `PP.OEYG.MobileNumber` | `PpOrderEntry_Mobilenumber` | TField |  | Collection of information that identifies a mobile number, as defined by telecom services. |
| 486 | `PP.OEYG.EmailAddress` | `PpOrderEntry_Emailaddress` | TField |  | Address for electronic mail. |
| 487 | `PP.OEYG.FxContractId` | `PpOrderEntry_Fxcontractid` | TField |  | Contains the reference to the foreign exchange contract utilized for the payment. Must allow input only for cross currency payments If valid FX contract ID is input, API calls will be made to Treasury module to validate/update FX utilisation and to default the customer rate Currently supported only when TPH is embedded with TRANSACT |
| 488 | `PP.OEYG.Reserved1` | `PpOrderEntry_Reserved1` | TField |  |  |
