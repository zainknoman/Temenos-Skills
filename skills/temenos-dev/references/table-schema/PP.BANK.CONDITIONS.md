# PP.BANK.CONDITIONS — Table Schema

> Source: `INSERTS/I_F.PP.BANK.CONDITIONS` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BC.CompanyID` | `PpBankConditions_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field 3 alphanumeric characters. NoInput Field The value gets autopopulated based on the company that you login |
| 2 | `PP.BC.CorrespondentBIC` | `PpBankConditions_Correspondentbic` | TField | Yes | 35 characters (alphanumeric). Holds both BIC as well as NCC as some clearings do not support usage of BIC (Example FPS in UK) BIC can be defined at different levels (BIC 11, 8 , 6, 4 , 2). Default value defined as "*". Example CITIUS33CH1 ( BIC11) CITIUS33 ( BIC8) CITIUS CITI US * (default Value) No BIC should start with * (Eg. ****US33) Validation Rules: 1. Mandatory field 2. Valid BIC from PPT_BICTable of the selected company 3. Only the 11/ 8/ 6/ 4 and 2 BIC values are permissible along with the default value '*' 4. Valid NCC from PPT_BANKCODE of the selected company |
| 3 | `PP.BC.SLAID` | `PpBankConditions_Slaid` | TField | Yes | Indicates Service level agreement with the other bank. 10 characters allowed to input. Validation Rules: 1. Mandatory field. 2. Valid value for this comes from the SLA table or wildcarded * ( Default Value) 3. If SLA is * then currency has to be *. 4. Currency code can only be entered if SLA is entered. |
| 4 | `PP.BC.CurrencyCode` | `PpBankConditions_Currencycode` | TField | Yes | Holds a 3 character unique code which denotes a specific currency used in the system. It can also be a "*". Validation Rules: 1. Mandatory field 2. If SLA is * then currency has to be *. 3. Currency code can only be entered if SLA is entered. 4. Currency should be a valid entry in Currency Table (PP.CURRENCY). |
| 5 | `PP.BC.StartDate` | `PpBankConditions_Startdate` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. Validation Rules: 1. Start Date should be &gt; Today and &lt;= End Date |
| 6 | `PP.BC.CTRNonSTPIndicator` | `PpBankConditions_Ctrnonstpindicator` | TField | Yes | Indicates Payment on behalf of customer is STP or NON STP if PH is installed. Value is NON STP and the field is non-inputtable if PH is not installed. 1 character (alphanumeric). Possible Values � Y (Yes) or N (No). Default Value is No Validation Rules: 1. Mandatory Input 2. If CTRBTRIndicator is 'Yes' then CreditInstruction should be input. |
| 7 | `PP.BC.CreditInstruction` | `PpBankConditions_Creditinstruction` | TField |  | Credit instructions are allowed only if Non STP for CTR is Yes.This field can hold upto 128 alphanumeric characters |
| 8 | `PP.BC.BTRNonSTPIndicator` | `PpBankConditions_Btrnonstpindicator` | TField | Yes | Indicates Payment on behalf of bank (BTR) is STP or NON STP if PH is installed. Value is NON STP and the field is non-inputtable if PH is not installed. 1 character (alphanumeric). Possible Values � Y (Yes) or N (No). Default Value is No. Validation Rules: 1. Mandatory field |
| 9 | `PP.BC.DebitInstruction` | `PpBankConditions_Debitinstruction` | TField |  | Debit instructions are allowed only if Non STP for BTR is Yes. This field can hold upto 128 alphanumeric characters |
| 10 | `PP.BC.WareHouseFlag` | `PpBankConditions_Warehouseflag` | TField |  | Indicates Payment can be moved to Warehouse or not if PH is installed. The field is non-inputtable and the value is 'N' (No) if PH is not installed. Possible Values: Y - Yes J - Just in Time (JIT) N - No Default Value is J (JIT) |
| 11 | `PP.BC.WareHouseReleaseTime` | `PpBankConditions_Warehousereleasetime` | TField |  | Indicates at what time payment to be released from Warehouse if PH is installed. The field is non-inputtable since Warehouse functionality is not available when PH is not installed. Time in HH:MM format. Default value is blank. Validation Rules: 1.Warehouse release time is allowed only when Warehouse Indicator is set Yes/JIT NOTE: Currently it is not in use reserved for future use. |
| 12 | `PP.BC.PSDECChargeCompliant` | `PpBankConditions_Psdecchargecompliant` | TField |  | 1 character (alphanumeric). It is Dropdown field having values Y(Yes) and N(No). Default Value is No. NOTE: Currently it is not in use reserved for future use. |
| 13 | `PP.BC.LanguageID` | `PpBankConditions_Languageid` | TField |  | 2 characters (alphanumeric). Valid Entry in T24 Language table (LANGUAGE). Can be blank. |
| 14 | `PP.BC.CreditStmtFormatName` | `PpBankConditions_Creditstmtformatname` | TField | No | 15 characters (alphanumeric). Optional field. Validation Rules: 1. Value should be valid entry in Statement Format table(PPT.STATEMENTFORMAT). |
| 15 | `PP.BC.DebitStmtFormatName` | `PpBankConditions_Debitstmtformatname` | TField |  | 15 characters (alphanumeric). Value should be valid entry in Statement Format table. It can also be blank |
| 16 | `PP.BC.FXSpread` | `PpBankConditions_Fxspread` | TField |  | Providing preferential exchange rate spread when debit / credit accounts are different from to the payment currency. NOTE: Currently it is not in use reserved for future use. |
| 17 | `PP.BC.EndDate` | `PpBankConditions_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. Validation Rules: 1. End Date &gt;= Start Date |
| 18 | `PP.BC.ChargeAccountIndicator` | `PpBankConditions_Chargeaccountindicator` | TField | Yes | 1 character (alphanumeric). Possible Values - Y (Yes) or N (No). Default Value is No. This is to indicate that Bank requires separate charge account or charge accounts for different transaction currency. This field is only required for GUI validation. It is not stored in database. Validation Rules: 1. Mandatory field 2. If charge Account Indicator is set to YES, then at least one charge acount details should be entered. 3. In Edit mode, if there is at least one Charge Account Record, Charge Account Indicator must be set to YES. |
| 19 | `PP.BC.TransactionCurrency` | `PpBankConditions_Transactioncurrency` |  |  |  |
| 20 | `PP.BC.ChargeAccountCompanyID` | `PpBankConditions_Chargeaccountcompanyid` |  |  |  |
| 21 | `PP.BC.ChargeAccountNumber` | `PpBankConditions_Chargeaccountnumber` |  |  |  |
| 22 | `PP.BC.ChargeAccountCurrency` | `PpBankConditions_Chargeaccountcurrency` |  |  |  |
| 23 | `PP.BC.AdviceIndicator` | `PpBankConditions_Adviceindicator` | TField | Yes | 1 character allowed to input(alphanumeric). Dropdown field having values Y (Yes) and N (No) default Value is N (No). This field is only required for GUI validation. It is not stored in database. Validation Rules: 1. Mandatory field 2. If Advice Indicator is set to YES, then at least one Advice detail should be entered. 3. In Edit mode, if there is at least one Advice Record, Advice Indicator must be set to YES |
| 24 | `PP.BC.SequenceNumber` | `PpBankConditions_Sequencenumber` |  |  |  |
| 25 | `PP.BC.DebitCreditAdvice` | `PpBankConditions_Debitcreditadvice` |  |  |  |
| 26 | `PP.BC.CTRBTRIndicator` | `PpBankConditions_Ctrbtrindicator` |  |  |  |
| 27 | `PP.BC.InitiatedByOthers` | `PpBankConditions_Initiatedbyothers` |  |  |  |
| 28 | `PP.BC.AmountCurreny` | `PpBankConditions_Amountcurreny` |  |  |  |
| 29 | `PP.BC.FromAmount` | `PpBankConditions_Fromamount` |  |  |  |
| 30 | `PP.BC.ToAmount` | `PpBankConditions_Toamount` |  |  |  |
| 31 | `PP.BC.DeliveryMethod` | `PpBankConditions_Deliverymethod` |  |  |  |
| 32 | `PP.BC.Telephonenumber` | `PpBankConditions_Telephonenumber` |  |  |  |
| 33 | `PP.BC.EmailID` | `PpBankConditions_Emailid` |  |  |  |
| 34 | `PP.BC.BICAddress` | `PpBankConditions_Bicaddress` |  |  |  |
| 35 | `PP.BC.SMSNumber` | `PpBankConditions_Smsnumber` |  |  |  |
| 36 | `PP.BC.FaxNumber` | `PpBankConditions_Faxnumber` |  |  |  |
| 37 | `PP.BC.PostName` | `PpBankConditions_Postname` |  |  |  |
| 38 | `PP.BC.PostAddress1` | `PpBankConditions_Postaddress1` |  |  |  |
| 39 | `PP.BC.PostAddress2` | `PpBankConditions_Postaddress2` |  |  |  |
| 40 | `PP.BC.PostAddress3` | `PpBankConditions_Postaddress3` |  |  |  |
| 41 | `PP.BC.Attention` | `PpBankConditions_Attention` |  |  |  |
| 42 | `PP.BC.AllowSpecialCharacterSet` | `PpBankConditions_Allowspecialcharacterset` | TField |  | This new indicator will take the following values Y or blank. Y indicates the country supports special character set. Blank is default |
| 43 | `PP.BC.CodePageSet` | `PpBankConditions_Codepageset` | TField |  | This field will specify against which code page the special characters have to be validated The value inputted by the user in this field will be validated against the ASCII.VAL.TABLE STANDARD.SW for LATIN or STANDARD.GR for GREEK |
| 44 | `PP.BC.TranAckNackIndicator` | `PpBankConditions_Tranacknackindicator` | TField |  | To hold if the correspondent wishes to receive Ack, Nack, Both or None when processing clearing payments. Possible values: ACK, NACK, BOTH or Blank |
| 45 | `PP.BC.InterimStatusIndicator` | `PpBankConditions_Interimstatusindicator` | TField |  | Specifies if the correspondent requires an interim status confirmation when processing a payment. Applicable for INST and NRINST payments. Valid values : Y, N or Blank |
| 46 | `PP.BC.CustomerStatusMessageType` | `PpBankConditions_Customerstatusmessagetype` | TField |  | Indicates the message type to be used when sending a payment confirmation to the ordering customer. Should be a valid value from PP.MSGPAYMENTTYPE table |
| 47 | `PP.BC.LOCAL.REF` | `PpBankConditions_LocalRef` |  |  |  |
| 48 | `PP.BC.LinkID` | `PpBankConditions_Linkid` | TField |  |  |
| 49 | `PP.BC.OVERRIDE` | `PpBankConditions_Override` |  |  |  |
| 50 | `PP.BC.RECORD.STATUS` | `PpBankConditions_RecordStatus` | String |  |  |
| 51 | `PP.BC.CURR.NO` | `PpBankConditions_CurrNo` | String |  |  |
| 52 | `PP.BC.INPUTTER` | `PpBankConditions_Inputter` |  |  |  |
| 53 | `PP.BC.DATE.TIME` | `PpBankConditions_DateTime` |  |  |  |
| 54 | `PP.BC.AUTHORISER` | `PpBankConditions_Authoriser` | String |  |  |
| 55 | `PP.BC.CO.CODE` | `PpBankConditions_CoCode` | String |  |  |
| 56 | `PP.BC.DEPT.CODE` | `PpBankConditions_DeptCode` | String |  |  |
| 57 | `PP.BC.AUDITOR.CODE` | `PpBankConditions_AuditorCode` | String |  |  |
| 58 | `PP.BC.AUDIT.DATE.TIME` | `PpBankConditions_AuditDateTime` | String |  |  |
| 59 | `PP.BC.MT210MatchRequired` | `PpBankConditions_Mt210matchrequired` | TField |  | Indicates the bank, If respective payment details (MT103 or MT202) should be sent to ER module to check against MT210 message. Possible Values � Y (Yes) or N (No). Default Value is No. |
| 60 | `PP.BC.GPILeadTime` | `PpBankConditions_Gpileadtime` | TField |  | This field is used to determine the soft cut-off time between banks for incoming payments. The cut-off as retrieved from the channel cut-off table is subtracted/added by this lead time . |
