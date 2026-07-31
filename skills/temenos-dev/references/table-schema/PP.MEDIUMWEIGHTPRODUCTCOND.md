# PP.MEDIUMWEIGHTPRODUCTCOND — Table Schema

> Source: `INSERTS/I_F.PP.MEDIUMWEIGHTPRODUCTCOND` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MPC.CompanyID` | `PpMediumweightproductcond_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.MPC.PaymentDirection` | `PpMediumweightproductcond_Paymentdirection` | TField | Yes | Indicates the Direction of the payment. Possible values: "I" � Incoming payment "B" � Book payment "O" � Outgoing payment "R" � Redirect payment It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 3 | `PP.MPC.ClearingTransactionType` | `PpMediumweightproductcond_Clearingtransactiontype` | TField | Yes | Identifies the clearing transaction type of the payment.It will be validated with PP.TRANSACTION.TYPES Example: "CC" - Cheque Credits "CD" - Cheque Debits "CT" - Credit Transfer "DD" - Direct Debits It's a mandatory Field. This field is used as one of the criteria to determine the product of a payment. |
| 4 | `PP.MPC.SingleBatchClearing` | `PpMediumweightproductcond_Singlebatchclearing` | TField | Yes | Indicates payment type based on Single, Batch and Clearing payment. Possible values: "C" - Batch Child payment "N" - Clearing payment "P" - Batch Parent payment "S" - Single payment "Y" - Clearing Settlement Transaction It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 5 | `PP.MPC.ChargeType` | `PpMediumweightproductcond_Chargetype` | TField | Yes | Holds the Charge type of the payment. Possible values: "BEN" - Charges are borne by the Beneficiary "SHA" - Charges are shared by both Ordering Party and Beneficiary "OUR" - Charges are borne by the Ordering Party It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 6 | `PP.MPC.Currency` | `PpMediumweightproductcond_Currency` | TField | Yes | Holds a 3 character unique code which denotes a specific currency used in the system. It's a mandatory field. The value links to the field �CurrencyCode� in PP.CURRENCY. This field is used as one of the criteria to determine the product of a payment. |
| 7 | `PP.MPC.OriginatingSource` | `PpMediumweightproductcond_Originatingsource` | TField | Yes | Identifies the Source Group of the payment. It's a mandatory field. Can have a maximum length of 10 alpha-numeric characters. The value links to the field 'SourcePDGroup' in PP.SOURCE Default value is "*". This field is used as one of the criteria to determine the product of a payment. |
| 8 | `PP.MPC.IncomingMessageType` | `PpMediumweightproductcond_Incomingmessagetype` | TField | Yes | Indicates the message type of the Payment. Default value is "*". It's a mandatory field. Can have a maximum length of 10 alpha-numeric characters. The value links to the field ID in PP.MESSAGEPAYMENTTYPE. This field is used as one of the criteria to determine the product of a payment. |
| 9 | `PP.MPC.ClearingNatureCode` | `PpMediumweightproductcond_Clearingnaturecode` | TField | Yes | Identifies the nature of clearing payment. It is updated from Mapping. Default value is "*". It's a mandatory field. Can have a maximum length of 20 alpha-numeric characters. The value links to the field �ClearingNatureCode� in PP.CLEARING.NATURE.CODE. This field is used as one of the criteria to determine the product of a payment. |
| 10 | `PP.MPC.BeneficiaryPartyIBANCountry` | `PpMediumweightproductcond_Beneficiarypartyibancountry` | TField | Yes | Indicates the country code or country group present in the IBAN of the Beneficiary. It's a mandatory field. Can have a maximum length of 2 alpha-numeric characters. The entry should be an existing record in COUNTRY or COUNTRY.GROUP. Default value is "*". This field is used as one of the criteria to determine the product of a payment. |
| 11 | `PP.MPC.OrderingPartyIBANCountry` | `PpMediumweightproductcond_Orderingpartyibancountry` | TField | Yes | Indicates the country code or country group present in the IBAN of the Ordering Party. It's a mandatory field. Can have a maximum length of 2 alpha-numeric characters. The entry should be an existing record in COUNTRY or COUNTRY.GROUP. Default value is "*". This field is used as one of the criteria to determine the product of a payment. |
| 12 | `PP.MPC.BeneficiaryPartyIBANPresent` | `PpMediumweightproductcond_Beneficiarypartyibanpresent` | TField | Yes | Indicates Presence of Beneficiary IBAN. Possible Values: "Y" - Yes "*" - Applies-to-all Value Default value is "Y". It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 13 | `PP.MPC.OrderingPartyIBANPresent` | `PpMediumweightproductcond_Orderingpartyibanpresent` | TField | Yes | Indicates Presence of Ordering Party IBAN. Possible Values: "Y" - Yes "*" - Applies-to-all Value Default value is "Y". It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 14 | `PP.MPC.BeneficiaryInstitBICPresent` | `PpMediumweightproductcond_Beneficiaryinstitbicpresent` | TField | Yes | Indicates Presence of Beneficiary institution BIC. Possible Values: "Y" - Yes "*" - Applies-to-all Value Default value is "Y". It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 15 | `PP.MPC.OrderingInstitBICPresent` | `PpMediumweightproductcond_Orderinginstitbicpresent` | TField | Yes | Indicates Presence of Ordering institution BIC. Possible Values: "Y" - Yes "*" - Applies-to-all Value Default value is "Y". It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 16 | `PP.MPC.OrderingPartyResidency` | `PpMediumweightproductcond_Orderingpartyresidency` | TField | Yes | Indicates the Resident type of the Ordering party. Possible Values: "R" - Resident "N" - Non Resident "*" - Applies-to-all Value Default value is "*". It's a mandatory field. This field is used as one of the criteria to determine the product of a payment. |
| 17 | `PP.MPC.FinalCodeWord` | `PpMediumweightproductcond_Finalcodeword` | TField | Yes | Holds the bilaterally agreed code words between the banks. Default value is "*". It's a mandatory field. Can have a maximum length of 8 alpha-numeric characters. The value links to the field �CodeWord� in PP.INBOUND.CODEWORD. This field is used as one of the criteria to determine the product of a payment. |
| 18 | `PP.MPC.StartDate` | `PpMediumweightproductcond_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 19 | `PP.MPC.EndDate` | `PpMediumweightproductcond_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 20 | `PP.MPC.FromAmount` | `PpMediumweightproductcond_Fromamount` |  |  |  |
| 21 | `PP.MPC.ToAmount` | `PpMediumweightproductcond_Toamount` |  |  |  |
| 22 | `PP.MPC.ClientConditionProduct` | `PpMediumweightproductcond_Clientconditionproduct` |  |  |  |
| 23 | `PP.MPC.SourceIndicator` | `PpMediumweightproductcond_Sourceindicator` |  |  |  |
| 24 | `PP.MPC.RoutingProduct` | `PpMediumweightproductcond_Routingproduct` |  |  |  |
| 25 | `PP.MPC.ImposeRoutingFlag` | `PpMediumweightproductcond_Imposeroutingflag` |  |  |  |
| 26 | `PP.MPC.FeeProduct` | `PpMediumweightproductcond_Feeproduct` |  |  |  |
| 27 | `PP.MPC.PostingProduct` | `PpMediumweightproductcond_Postingproduct` |  |  |  |
| 28 | `PP.MPC.FilterProduct` | `PpMediumweightproductcond_Filterproduct` |  |  |  |
| 29 | `PP.MPC.LedgerProductCode` | `PpMediumweightproductcond_Ledgerproductcode` |  |  |  |
| 30 | `PP.MPC.DebitBookCode` | `PpMediumweightproductcond_Debitbookcode` |  |  |  |
| 31 | `PP.MPC.CreditBookCode` | `PpMediumweightproductcond_Creditbookcode` |  |  |  |
| 32 | `PP.MPC.DebitChargeBookCode` | `PpMediumweightproductcond_Debitchargebookcode` |  |  |  |
| 33 | `PP.MPC.CreditChargeBookCode` | `PpMediumweightproductcond_Creditchargebookcode` |  |  |  |
| 34 | `PP.MPC.DebitVATBookCode` | `PpMediumweightproductcond_Debitvatbookcode` |  |  |  |
| 35 | `PP.MPC.CreditVATBookCode` | `PpMediumweightproductcond_Creditvatbookcode` |  |  |  |
| 36 | `PP.MPC.RegulatoryReportingIndic` | `PpMediumweightproductcond_Regulatoryreportingindic` |  |  |  |
| 37 | `PP.MPC.NewPriority` | `PpMediumweightproductcond_Newpriority` |  |  |  |
| 38 | `PP.MPC.NonSTPIndicator` | `PpMediumweightproductcond_Nonstpindicator` |  |  |  |
| 39 | `PP.MPC.PSDCompliantIndicator` | `PpMediumweightproductcond_Psdcompliantindicator` |  |  |  |
| 40 | `PP.MPC.ECCompliantIndicator` | `PpMediumweightproductcond_Eccompliantindicator` |  |  |  |
| 41 | `PP.MPC.CurrencyMarket` | `PpMediumweightproductcond_Currencymarket` |  |  |  |
| 42 | `PP.MPC.SettlementType` | `PpMediumweightproductcond_Settlementtype` |  |  |  |
| 43 | `PP.MPC.ClearingHoliday` | `PpMediumweightproductcond_Clearingholiday` |  |  |  |
| 44 | `PP.MPC.DuplicateType` | `PpMediumweightproductcond_Duplicatetype` |  |  |  |
| 45 | `PP.MPC.DomesticInternational` | `PpMediumweightproductcond_Domesticinternational` | TField |  |  |
| 46 | `PP.MPC.RateFixing` | `PpMediumweightproductcond_Ratefixing` | TField | No | This field is used to Enable the Rate Fixing Functionality. If this flag is selected as 'Y', system will park the transaction in a new Status code for Awaiting rate fixing. If this flag is selected as 'YesWithReservation', balance check and fund reservation will happen and then system will park the transaction in a new Status code for Awaiting rate fixing. Applicable only if Balance Check Required flag is 'Y' in Fund Reservation required config Validation: Optional Field. Defaulted to Blank. If Blank is selected, then the Rate Fixing definition at the Company Properties table will prevail. The definition of Rate Fixing of 'Y' or 'N' here take precedence over the PP.COMPANY.PROPERTIES table. |
| 47 | `PP.MPC.LOCAL.REF` | `PpMediumweightproductcond_LocalRef` |  |  |  |
| 48 | `PP.MPC.LinkID` | `PpMediumweightproductcond_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 49 | `PP.MPC.OVERRIDE` | `PpMediumweightproductcond_Override` |  |  |  |
| 50 | `PP.MPC.RECORD.STATUS` | `PpMediumweightproductcond_RecordStatus` | String |  |  |
| 51 | `PP.MPC.CURR.NO` | `PpMediumweightproductcond_CurrNo` | String |  |  |
| 52 | `PP.MPC.INPUTTER` | `PpMediumweightproductcond_Inputter` |  |  |  |
| 53 | `PP.MPC.DATE.TIME` | `PpMediumweightproductcond_DateTime` |  |  |  |
| 54 | `PP.MPC.AUTHORISER` | `PpMediumweightproductcond_Authoriser` | String |  |  |
| 55 | `PP.MPC.CO.CODE` | `PpMediumweightproductcond_CoCode` | String |  |  |
| 56 | `PP.MPC.DEPT.CODE` | `PpMediumweightproductcond_DeptCode` | String |  |  |
| 57 | `PP.MPC.AUDITOR.CODE` | `PpMediumweightproductcond_AuditorCode` | String |  |  |
| 58 | `PP.MPC.AUDIT.DATE.TIME` | `PpMediumweightproductcond_AuditDateTime` | String |  |  |
| 59 | `PP.MPC.TxnStopMapRule` | `PpMediumweightproductcond_Txnstopmaprule` | TField | No | This optional field indicates if the TPH must perform Debit Account Validation using Transaction Stop Module. If left blank, Transaction Stop check will not be performed on the Debit Account Validation: Should be a valid record in TZ.TRANSACTION.STOP.MAP.RULES |
| 60 | `PP.MPC.SwitchAccount` | `PpMediumweightproductcond_Switchaccount` | TField |  | This field is used when account switching service is required for a customer. Possible values : Yes/Blank Inputtable only when PH and ACSWIT modules are installed |
| 61 | `PP.MPC.ChangeProductAPI` | `PpMediumweightproductcond_Changeproductapi` | TField |  | Holds the name of the ChangeProductAPI, which can override the routing product or any determined output product based on the clearing requirement Validation Rules:Valid EB.API record of type 'Basic',if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record PP.MEDIUMWEIGHT.CHANGEPRODUCT.HOOK. If a Valid Routing product is returned, it will override the existing value in the field 'RoutingProduct'. If empty string is returned, the payment will be processed based on the exisitng routing product |
| 62 | `PP.MPC.PP.DateProduct` | `PpMediumweightproductcond_PpDateproduct` |  |  |  |
