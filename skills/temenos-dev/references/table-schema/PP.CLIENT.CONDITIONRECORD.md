# PP.CLIENT.CONDITIONRECORD — Table Schema

> Source: `INSERTS/I_F.PP.CLIENT.CONDITIONRECORD` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CCR.CompanyID` | `PpClientConditionrecord_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 1. 3 alphanumeric characters. 2. The value links to the ID of PP.COMPANY.PROPERTIES.CONCAT |
| 2 | `PP.CCR.ClientConditionProduct` | `PpClientConditionrecord_Clientconditionproduct` | TField |  | This would indicate the source group from where payment has been originated. Valid/Allowed values can only be a valid ClientConditionProduct for the company as per PP.ClientConditionProduct table. If left blank then this should be wildcarded |
| 3 | `PP.CCR.SourceProduct` | `PpClientConditionrecord_Sourceproduct` | TField |  | Indicate the source group from where payment has been originated. Valid/allowed values can only be a valid SourceProduct as per Product table. Validation Rules: 1. If left blank then this should be wild carded as *. 2. DropDown from the Table PP_SourceProductGroup |
| 4 | `PP.CCR.BusinessLine` | `PpClientConditionrecord_Businessline` | TField |  | This is the business line or the customer group to which the customer belongs. When EnableCustGrouping in PP.COMPANY.PROPERTIES is set as "Yes", this holds the Customer Group ID from PP.GEN.CONDITION. When PP.COMPANY.PROPERTIES is blank, this field holds the Customer Target. Validation Rules: 1. Up to 3 A(Alphanumeric) characters. 2. If left blank then this should be wild carded as *. 3. When EnableCustGrouping in PP.COMPANY.PROPERTIES is set as "Yes", this field can only be input with valid records from PP.GEN.CONDITION. |
| 5 | `PP.CCR.ClientID` | `PpClientConditionrecord_Clientid` | TField | Yes | This is the Client ID for whom the condition is being set up for. Validation Rules: 1. Input mandatory when AccountNumber exists 2. If left blank then this will be wild carded. |
| 6 | `PP.CCR.AccountNumber` | `PpClientConditionrecord_Accountnumber` | TField | Yes | Indicates account number to the Client Conditions. Validation Rules: 1. Up to 35 A (Alphanumeric) characters. 2. If left blank then this should be wild carded as *. 2. Input mandatory when Account CompanyID exist. |
| 7 | `PP.CCR.AccountCurrency` | `PpClientConditionrecord_Accountcurrency` | TField |  | Three character currency code of the Account Number. Validation Rules: 1. If left blank then this should be wild carded as *. 2. Valid entry in PP_Currency table |
| 8 | `PP.CCR.AccountCompanyID` | `PpClientConditionrecord_Accountcompanyid` | TField |  | Indicates company code of the Account defined. Shuold be valid T24 Company. Validation Rules: 1. If left blank then this should be wild carded 2. If entered should be same as CompanyID field |
| 9 | `PP.CCR.StartDate` | `PpClientConditionrecord_Startdate` | TField |  | This is the date from which respective record will be active Validation Rules: 1. 11 characters Date format which is non inputtable. 2. It is Defaulted from the ID |
| 10 | `PP.CCR.EndDate` | `PpClientConditionrecord_Enddate` | TField |  | This is the date till which respective record will be active. Validation Rules: 1. End Date must be greater than Start Date |
| 11 | `PP.CCR.LanguageID` | `PpClientConditionrecord_Languageid` | TField |  | Valid Entry in T24 Language table (LANGUAGE). Can be blank. |
| 12 | `PP.CCR.DrStatementFormat` | `PpClientConditionrecord_Drstatementformat` | TField |  | Should be valid from Table PP_StatementFormat table if PH is installed. Value is null and non-inputtable if PH product is not installed. Validation Rules 30 ANY(AlphaNumeric or Special) characters |
| 13 | `PP.CCR.CRStatementFormat` | `PpClientConditionrecord_Crstatementformat` | TField |  | Should be valid from Table PP_StatementFormat table if PH product is installed. Value is null and non-inputtable when PH product is not installed. Validation Rules 30 ANY(AlphaNumeric or Special) characters |
| 14 | `PP.CCR.BillingIndicator` | `PpClientConditionrecord_Billingindicator` | TField |  |  |
| 15 | `PP.CCR.ChargePostingSeparately` | `PpClientConditionrecord_Chargepostingseparately` | TField |  | This field indicates whether the charges for the payment are to be posted separately or not. PSD product will always have Y as an option Y - Charge separate N - Do not charge separate. Validation Rules: 1. If left blank then this will be defaulted to Y |
| 16 | `PP.CCR.ChargePostingDetail` | `PpClientConditionrecord_Chargepostingdetail` | TField |  | This field indicates whether the charges are to be posted in detail and accordingly additional PostingLines for each change should be configured or not.This will take the following values Y=post in detail; N= post detail. If left blank, it will be defaulted to Y. PSD product will always have Y as an option Validation Rules: Not Allowed to input field when ChargePostingSeparately is set to No or Null |
| 17 | `PP.CCR.VatPrincipal` | `PpClientConditionrecord_Vatprincipal` | TField |  | This would be the percentage indicated in nn.nnnn (up to 4 decimal places). Default value defined as zero. |
| 18 | `PP.CCR.VATOnCharge` | `PpClientConditionrecord_Vatoncharge` | TField |  | Dropdown field having values Y (Yes) and N (No). Y - Apply VAT on Charges N - Don't apply VAT on Charges |
| 19 | `PP.CCR.NonSTPIndicator` | `PpClientConditionrecord_Nonstpindicator` | TField |  | It is Dropdown field having values Y, N, C &amp; D Y - Non STP for all transactions; N - STP for all transactions; C - Non STP for all credit transactions D - Non STP for all debit transactions. |
| 20 | `PP.CCR.AdviceIndicator` | `PpClientConditionrecord_Adviceindicator` | TField |  | Dropdown field having values Y (Yes) and N (No). Default Value is N (No). |
| 21 | `PP.CCR.DebitCreditAdvice` | `PpClientConditionrecord_Debitcreditadvice` |  |  |  |
| 22 | `PP.CCR.SequenceNumber` | `PpClientConditionrecord_Sequencenumber` |  |  |  |
| 23 | `PP.CCR.DeliveryMethod` | `PpClientConditionrecord_Deliverymethod` |  |  |  |
| 24 | `PP.CCR.PhoneConfirmation` | `PpClientConditionrecord_Phoneconfirmation` |  |  |  |
| 25 | `PP.CCR.SMS` | `PpClientConditionrecord_Sms` |  |  |  |
| 26 | `PP.CCR.FAX` | `PpClientConditionrecord_Fax` |  |  |  |
| 27 | `PP.CCR.EmailID` | `PpClientConditionrecord_Emailid` |  |  |  |
| 28 | `PP.CCR.MailLine1` | `PpClientConditionrecord_Mailline1` |  |  |  |
| 29 | `PP.CCR.MailLine2` | `PpClientConditionrecord_Mailline2` |  |  |  |
| 30 | `PP.CCR.MailLine3` | `PpClientConditionrecord_Mailline3` |  |  |  |
| 31 | `PP.CCR.MailLine4` | `PpClientConditionrecord_Mailline4` |  |  |  |
| 32 | `PP.CCR.Swift` | `PpClientConditionrecord_Swift` |  |  |  |
| 33 | `PP.CCR.Attention` | `PpClientConditionrecord_Attention` |  |  |  |
| 34 | `PP.CCR.AdviceType` | `PpClientConditionrecord_Advicetype` |  |  |  |
| 35 | `PP.CCR.AdviceTxnLowerLimit` | `PpClientConditionrecord_Advicetxnlowerlimit` |  |  |  |
| 36 | `PP.CCR.FXDiscountIndicator` | `PpClientConditionrecord_Fxdiscountindicator` | TField |  | Dropdown field having values Y (Yes) and N (No). Default Value is N (No). Validation Rules: A new Client FX discount should be created only if FXDiscountIndicator is set to Yes. |
| 37 | `PP.CCR.TransactionCurrency` | `PpClientConditionrecord_Transactioncurrency` |  |  |  |
| 38 | `PP.CCR.Discount` | `PpClientConditionrecord_Discount` |  |  |  |
| 39 | `PP.CCR.SeparatechargeAccountIndicator` | `PpClientConditionrecord_Separatechargeaccountindicator` | TField |  | Dropdown field having values Y (Yes) and N (No). Default Value is N(No). Validation Rules: 1. If SeparatechargeAccountIndicator is set to YES, then at least one charge Account Record needs to be created. 2. A new Client Conditions Charge Account should be created only if SeparatechargeAccountIndicator is set to Yes |
| 40 | `PP.CCR.DebitCreditIndicator` | `PpClientConditionrecord_Debitcreditindicator` |  |  |  |
| 41 | `PP.CCR.ChargeAccTransactionCCY` | `PpClientConditionrecord_Chargeacctransactionccy` |  |  |  |
| 42 | `PP.CCR.ChargeAccountCompanyID` | `PpClientConditionrecord_Chargeaccountcompanyid` |  |  |  |
| 43 | `PP.CCR.ChargeAccountCurrency` | `PpClientConditionrecord_Chargeaccountcurrency` |  |  |  |
| 44 | `PP.CCR.ChargeAccountNumber` | `PpClientConditionrecord_Chargeaccountnumber` |  |  |  |
| 45 | `PP.CCR.FXNonSTPIndicator` | `PpClientConditionrecord_Fxnonstpindicator` | TField |  | Indicates Payment on behalf of customer is STP or NON STP. 1 character (alphanumeric). Possible Values - C / D / Y / N |
| 46 | `PP.CCR.FXNonSTPAmount` | `PpClientConditionrecord_Fxnonstpamount` | TField | Yes | 20 Digit numeric amount field. Validation Rules: Field mandatory when FXNonSTPIndicator exist |
| 47 | `PP.CCR.DebitSpecialInstructions` | `PpClientConditionrecord_Debitspecialinstructions` | TField |  | Possible to give special Debit instructions for the operator. 128 Characters (Alpha Numeric and special characters) |
| 48 | `PP.CCR.CreditSpecialInstructions` | `PpClientConditionrecord_Creditspecialinstructions` | TField |  | This field is used to specify special Credit instructions 128 Characters (Alpha Numeric and special characters) |
| 49 | `PP.CCR.CurrencyCode` | `PpClientConditionrecord_Currencycode` |  |  |  |
| 50 | `PP.CCR.IncomingCutOffLeadTime` | `PpClientConditionrecord_Incomingcutoffleadtime` |  |  |  |
| 51 | `PP.CCR.OutgoingCutOffLeadTime` | `PpClientConditionrecord_Outgoingcutoffleadtime` |  |  |  |
| 52 | `PP.CCR.AccountSubstitution` | `PpClientConditionrecord_Accountsubstitution` | TField |  | Possible values: Y (Yes) or N (No) |
| 53 | `PP.CCR.ReleaseTime` | `PpClientConditionrecord_Releasetime` | TField |  | Holds the TIMESTAMP value. |
| 54 | `PP.CCR.DebitFloat` | `PpClientConditionrecord_Debitfloat` | TField |  | Number of days the bank can take debit float on the payment. |
| 55 | `PP.CCR.CreditFloat` | `PpClientConditionrecord_Creditfloat` | TField |  | This field defines the number of business days to adjust the Credit Value Date (CVD) into the future, potentially adding float to the transaction. This is applicable to the credit client. Validation Rules: 3 Numeric characters, representing the number of days. |
| 56 | `PP.CCR.AuthoriserDateTime` | `PpClientConditionrecord_Authoriserdatetime` | TField |  | Dropdown field having values Y (Yes) and N (No) if PH product is installed. Value is N (No) and is non-inputtable when PH is not installed. Possible Values: Y= Yes, Billing is preferred N= No, Billing is not preferred Default Value is N(No) |
| 57 | `PP.CCR.ThresholdAmount` | `PpClientConditionrecord_Thresholdamount` | TField |  | This field is an output value of the client condition record. The amount specified here is the amount in Home currency of the company. If the transaction amount is greater than this amount specified in this field, then the payment will be moved to manual repair queue with a due to exceeding the transaction amount threshold specified> |
| 58 | `PP.CCR.BatchACKNACKIndicator` | `PpClientConditionrecord_Batchacknackindicator` | TField |  | Indicates Acknowledgement and Non Acknowledgement for customer statusreport at bulk leval. |
| 59 | `PP.CCR.TranNACKIndicator` | `PpClientConditionrecord_Trannackindicator` | TField |  | To hold if the correspondent wishes to receive Ack, Nack, Both or None when processing clearing payments. Valid values : ACK, NACK, BOTH or Blank. |
| 60 | `PP.CCR.BalanceCheckOnChgAct` | `PpClientConditionrecord_Balancecheckonchgact` | TField |  | Specifies whether balance check needs to be done on a charge account for the debit charges |
| 61 | `PP.CCR.InterimStatusIndicator` | `PpClientConditionrecord_Interimstatusindicator` | TField |  | Specifies if the customer requires an interim status confirmation when processing a payment. Applicable for INST and NRINST payments. Valid values : Y, N or Blank |
| 62 | `PP.CCR.CustomerStatusMessageType` | `PpClientConditionrecord_Customerstatusmessagetype` | TField |  | Indicates the message type to be used when sending a payment confirmation to the ordering customer. Should be a valid value from PP.MSGPAYMENTTYPE table |
| 63 | `PP.CCR.TaxId` | `PpClientConditionrecord_Taxid` | TField |  | It holds TAX table record Ids as a drop down |
| 64 | `PP.CCR.TaxTypeId` | `PpClientConditionrecord_Taxtypeid` | TField |  | It holds TAX.TYPE.CONDITION record Ids as a drop down |
| 65 | `PP.CCR.CustomerStatusReportRejects` | `PpClientConditionrecord_Customerstatusreportrejects` | TField |  |  |
| 66 | `PP.CCR.RESERVED.9` | `PpClientConditionrecord_Reserved9` | TField |  | Standard T24 String. No Input Field |
| 67 | `PP.CCR.RESERVED.8` | `PpClientConditionrecord_Reserved8` | TField |  | Standard T24 String. No Input Field |
| 68 | `PP.CCR.RESERVED.7` | `PpClientConditionrecord_Reserved7` | TField |  | Standard T24 String. No Input Field |
| 69 | `PP.CCR.RESERVED.6` | `PpClientConditionrecord_Reserved6` | TField |  | Standard T24 String. No Input Field |
| 70 | `PP.CCR.RESERVED.5` | `PpClientConditionrecord_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 71 | `PP.CCR.RESERVED.4` | `PpClientConditionrecord_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 72 | `PP.CCR.RESERVED.3` | `PpClientConditionrecord_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 73 | `PP.CCR.RESERVED.2` | `PpClientConditionrecord_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 74 | `PP.CCR.RESERVED.1` | `PpClientConditionrecord_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 75 | `PP.CCR.LOCAL.REF` | `PpClientConditionrecord_LocalRef` |  |  |  |
| 76 | `PP.CCR.LinkID` | `PpClientConditionrecord_Linkid` | TField |  | Standard T24 String. No Input Field This field gets updated after authorisation of the record. This field contains the ID of the .PDS table. It contains ConcatID-BusinessDate. |
| 77 | `PP.CCR.OVERRIDE` | `PpClientConditionrecord_Override` |  |  |  |
| 78 | `PP.CCR.RECORD.STATUS` | `PpClientConditionrecord_RecordStatus` | String |  |  |
| 79 | `PP.CCR.CURR.NO` | `PpClientConditionrecord_CurrNo` | String |  |  |
| 80 | `PP.CCR.INPUTTER` | `PpClientConditionrecord_Inputter` |  |  |  |
| 81 | `PP.CCR.DATE.TIME` | `PpClientConditionrecord_DateTime` |  |  |  |
| 82 | `PP.CCR.AUTHORISER` | `PpClientConditionrecord_Authoriser` | String |  |  |
| 83 | `PP.CCR.CO.CODE` | `PpClientConditionrecord_CoCode` | String |  |  |
| 84 | `PP.CCR.DEPT.CODE` | `PpClientConditionrecord_DeptCode` | String |  |  |
| 85 | `PP.CCR.AUDITOR.CODE` | `PpClientConditionrecord_AuditorCode` | String |  |  |
| 86 | `PP.CCR.AUDIT.DATE.TIME` | `PpClientConditionrecord_AuditDateTime` | String |  |  |
