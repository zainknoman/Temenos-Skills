# Regulatory & Country Localisations — Reference

> Generated 2026-06-20T03:39:43.046735+00:00 from 306 JARs. Re-run `aggregate.py` to refresh.

---

## Lifecycle Hooks

*No lifecycle hooks detected in this domain.*

---

## Validation & Authorization Hooks

*No validation or authorization hooks detected in this domain.*

---

## Public APIs

| Class | JAR | Method | Returns | Description |
|-------|-----|--------|---------|-------------|
| `Delivery` | `DE_DeliveryApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `mapTagValuesToRecord` | `com.temenos.api.TStructure` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `validateBic` | `com.temenos.t24.api.complex.de.deliveryapi.ValidationResponse` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `validateCustomerBic` | `com.temenos.t24.api.complex.de.deliveryapi.ValidationResponse` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `validateCompanyBic` | `com.temenos.t24.api.complex.de.deliveryapi.ValidationResponse` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `mapMessageRecordsToNameValuePairs` | `java.util.List<com.temenos.t24.api.complex.de.deliveryapi.NameValuePair>` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `getBankRmaStatus` | `com.temenos.t24.api.complex.de.deliveryapi.SwiftRmaStatus` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `getMessageRmaStatus` | `com.temenos.t24.api.complex.de.deliveryapi.SwiftRmaStatus` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryApi.jar` | `getSwiftRmaStatus` | `com.temenos.t24.api.complex.de.deliveryapi.SwiftRmaStatus` | Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Delivery` | `DE_DeliveryHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `translateAmountInSpecificLanguage` | `java.lang.String` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `mapAdditionalDataToMessageType` | `java.util.List<com.temenos.t24.api.complex.de.deliveryhook.Field>` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `processInwardMessage` | `void` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `processOutwardMessage` | `void` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `headerMatchesCondition` | `com.temenos.api.TBoolean` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `convertOutwardValue` | `java.lang.String` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `updateSwiftMessage` | `void` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `createRecords` | `void` | This interface enables the implementer to convert the given value to the required value for the message. |
| `Delivery` | `DE_DeliveryHook.jar` | `getFieldValues` | `java.util.List<com.temenos.t24.api.complex.de.deliveryhook.FieldValue>` | This interface enables the implementer to convert the given value to the required value for the message. |
| `TransactionFee` | `HUTXNF_TransactionFeeHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned. |
| `TransactionFee` | `HUTXNF_TransactionFeeHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned. |
| `TransactionFee` | `HUTXNF_TransactionFeeHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned. |
| `TransactionFee` | `HUTXNF_TransactionFeeHook.jar` | `getPreviousCardNumber` | `java.lang.String` | This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned. |
| `TransactionFee` | `HUTXNF_TransactionFeeHook.jar` | `processEligibleTransaction` | `void` | This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned. |
| `TransactionFee` | `HUTXNF_TransactionFeeHook.jar` | `isHungaryResident` | `com.temenos.api.TBoolean` | This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned. |
| `InitialPublicOffering` | `ILIPOA_InitialPublicOfferingHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer to calculate and return the allocation to be fulfilled for the security order against an Initial public offering. |
| `InitialPublicOffering` | `ILIPOA_InitialPublicOfferingHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer to calculate and return the allocation to be fulfilled for the security order against an Initial public offering. |
| `InitialPublicOffering` | `ILIPOA_InitialPublicOfferingHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer to calculate and return the allocation to be fulfilled for the security order against an Initial public offering. |
| `InitialPublicOffering` | `ILIPOA_InitialPublicOfferingHook.jar` | `getSecurityAllocation` | `com.temenos.t24.api.complex.ilipoa.initialpublicofferinghook.SecurityAllocation` | This Interface enables the implementer to calculate and return the allocation to be fulfilled for the security order against an Initial public offering. |
| `IBAN` | `IN_IbanSystemApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `IBAN` | `IN_IbanSystemApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `IBAN` | `IN_IbanSystemApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `IBAN` | `IN_IbanSystemApi.jar` | `validateIBAN` | `com.temenos.t24.api.complex.in.ibansystemapi.ResponseMessage` | Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `IBAN` | `IN_IbanSystemApi.jar` | `getIbanInformation` | `com.temenos.t24.api.complex.in.ibansystemapi.IbanInformation` | Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `IBAN` | `IN_IbanSystemApi.jar` | `getBic` | `java.lang.String` | Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `RegulatoryReporting` | `ITREGE_TransactionsAPI.jar` | `getVersion` | `java.lang.String` | Create a new RegulatoryReporting using a specific context.. |
| `RegulatoryReporting` | `ITREGE_TransactionsAPI.jar` | `getBuildDate` | `java.lang.String` | Create a new RegulatoryReporting using a specific context.. |
| `RegulatoryReporting` | `ITREGE_TransactionsAPI.jar` | `getComponentVersion` | `java.lang.String` | Create a new RegulatoryReporting using a specific context.. |
| `RegulatoryReporting` | `ITREGE_TransactionsAPI.jar` | `isTransactionEligibleForReporting` | `com.temenos.api.TBoolean` | Create a new RegulatoryReporting using a specific context.. |
| `Loan` | `NOLEND_LoanApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Loan.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Loan` | `NOLEND_LoanApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Loan.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Loan` | `NOLEND_LoanApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Loan.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Loan` | `NOLEND_LoanApi.jar` | `getCharge` | `com.temenos.t24.api.complex.nolend.loanapi.Charge` | Default constructor. Create an empty Loan.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Earlyclosureapi` | `SAREGS_EarlyClosureAPI.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Earlyclosureapi.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Earlyclosureapi` | `SAREGS_EarlyClosureAPI.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Earlyclosureapi.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Earlyclosureapi` | `SAREGS_EarlyClosureAPI.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Earlyclosureapi.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Earlyclosureapi` | `SAREGS_EarlyClosureAPI.jar` | `calculateEarlyClosureChargesMurabaha` | `com.temenos.api.TNumber` | Default constructor. Create an empty Earlyclosureapi.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Earlyclosureapi` | `SAREGS_EarlyClosureAPI.jar` | `calculateEarlyClosureChargesIjara` | `com.temenos.api.TNumber` | Default constructor. Create an empty Earlyclosureapi.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `IslamicLoan` | `SAREGS_IslamicLoanApi.jar` | `getVersion` | `java.lang.String` | Create a new IslamicLoan using a specific context.. |
| `IslamicLoan` | `SAREGS_IslamicLoanApi.jar` | `getBuildDate` | `java.lang.String` | Create a new IslamicLoan using a specific context.. |
| `IslamicLoan` | `SAREGS_IslamicLoanApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new IslamicLoan using a specific context.. |
| `IslamicLoan` | `SAREGS_IslamicLoanApi.jar` | `calculatePartialEarlyPayment` | `com.temenos.t24.api.complex.saregs.islamicloanapi.PartialPaymentResponse` | Create a new IslamicLoan using a specific context.. |
| `Fedwire` | `USRTGS_FedwireHook.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Fedwire` | `USRTGS_FedwireHook.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Fedwire` | `USRTGS_FedwireHook.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Fedwire` | `USRTGS_FedwireHook.jar` | `validateAccountNumber` | `java.lang.String` | Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Fedwire` | `USRTGS_FedwireHook.jar` | `getOutwardFileName` | `java.lang.String` | Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Fedwire` | `USRTGS_FedwireHook.jar` | `getScreeningStatus` | `com.temenos.t24.api.hook.countrymodelbank.usa.Fedwire$ScreeningStatus` | Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |

---

## Enquiry Routines

*No enquiry routines detected in this domain.*

---

## Record Models

*No record models detected in this domain.*

---

## JAR Inventory

| JAR | Class Count | Component Types Present |
|-----|-------------|------------------------|
| `AU_API.jar` | 41 | unknown |
| `AU_Config.jar` | 18 | unknown |
| `AUACCT_AAAccountProducts.jar` | 1 | unknown |
| `AUADRI_Foundation.jar` | 11 | unknown |
| `AUBASE_Foundation.jar` | 9 | unknown |
| `AUBASE_RoleBasedHomePage.jar` | 16 | unknown |
| `AUBPAY_ApiInvocation.jar` | 4 | unknown |
| `AUBPAY_BillerManagement.jar` | 22 | unknown |
| `AUCGTX_Foundation.jar` | 30 | unknown |
| `AUCUST_Foundation.jar` | 7 | unknown |
| `AUDEPO_AADepositProducts.jar` | 1 | unknown |
| `AUIRCN_Foundation.jar` | 6 | unknown |
| `AUIVIC_InvestmentIncomeReport.jar` | 12 | unknown |
| `AULEFS_Foundation.jar` | 18 | unknown |
| `AULEND_AALendingProducts.jar` | 1 | unknown |
| `AULEND_AnnualPackageFee.jar` | 20 | unknown |
| `AULEND_AutoRepayment.jar` | 9 | unknown |
| `AULEND_FlexibleLoanRepayment.jar` | 2 | unknown |
| `AULEND_HomeLoanProductControls.jar` | 15 | unknown |
| `AULMOI_Foundation.jar` | 15 | unknown |
| `AUNPPC_Foundation.jar` | 25 | unknown |
| `AUOBPI_ProductsAPI.jar` | 6 | unknown |
| `AUOBPZ_Foundation.jar` | 100 | unknown |
| `AURLOC_Foundation.jar` | 14 | unknown |
| `AURTLN_Foundation.jar` | 1 | unknown |
| `AUWHTX_Foundation.jar` | 256 | unknown |
| `BR_Create.jar` | 4 | unknown |
| `BR_Foundation.jar` | 21 | unknown |
| `BR_Operations.jar` | 14 | unknown |
| `BRACCT_AccountRegistration.jar` | 1 | unknown |
| `BRBASE_CustomerCreation.jar` | 17 | unknown |
| `BRBASE_InterfaceConnector.jar` | 29 | unknown |
| `BRBASE_PositiveRegister.jar` | 6 | unknown |
| `BRBLOC_BacenLegalReports.jar` | 11 | unknown |
| `BRCRBU_CreditBureau.jar` | 7 | unknown |
| `BRCRED_CreditOperations.jar` | 8 | unknown |
| `BRDEPO_CDBPreAndPostFixado.jar` | 45 | unknown |
| `BRDEPO_CetipInterface.jar` | 5 | unknown |
| `BRPPJD_DOCCreditTransferDocument.jar` | 5 | unknown |
| `BRPPJD_TEDExpressWireTransfer.jar` | 7 | unknown |
| `CNCUST_CustomerInfrastructure.jar` | 16 | unknown |
| `CNCUST_SafeDeclaration.jar` | 5 | unknown |
| `CNDEPO_CorporateDeposit.jar` | 12 | unknown |
| `CNDEPO_RetailDeposit.jar` | 16 | unknown |
| `CNLICO_LimitsAndCollaterals.jar` | 7 | unknown |
| `CNQDII_Limit.jar` | 16 | unknown |
| `CNREVR_MatchingReversal.jar` | 16 | unknown |
| `CNWHTX_WithholdingTax.jar` | 14 | unknown |
| `DE_API.jar` | 70 | unknown |
| `DE_Archiving.jar` | 27 | unknown |
| `DE_Channels.jar` | 4 | unknown |
| `DE_Clearing.jar` | 26 | unknown |
| `DE_Config.jar` | 352 | unknown |
| `DE_DeliveryApi.jar` | 10 | public-api, unknown |
| `DE_DeliveryHook.jar` | 11 | public-api, unknown |
| `DE_Interface.jar` | 19 | unknown |
| `DE_Inward.jar` | 39 | unknown |
| `DE_Messaging.jar` | 32 | unknown |
| `DE_ModelBank.jar` | 81 | unknown |
| `DE_Outward.jar` | 105 | unknown |
| `DE_OutwardMessageService.jar` | 10 | unknown |
| `DE_Reports.jar` | 60 | unknown |
| `DE_ResponseService.jar` | 8 | unknown |
| `DE_Ticklers.jar` | 15 | unknown |
| `DEAWVS_Foundation.jar` | 7 | unknown |
| `DEBA15_Foundation.jar` | 11 | unknown |
| `DEBA18_Foundation.jar` | 30 | unknown |
| `DEBA24_AccountReporting.jar` | 22 | unknown |
| `DEBAIS_AnaCreditExtract.jar` | 16 | unknown |
| `DEBAIS_CommonInterfaceExtract.jar` | 14 | unknown |
| `DEBAIS_PaymentStatistics.jar` | 26 | unknown |
| `DEBAIS_RegulatoryReporting.jar` | 12 | unknown |
| `DEGDPD_AccountReporting.jar` | 21 | unknown |
| `DEMXTR_API.jar` | 2 | unknown |
| `DEMXTR_OutwardService.jar` | 6 | unknown |
| `DESCTX_Taxation.jar` | 189 | unknown |
| `FR_Config.jar` | 5 | unknown |
| `FR_Confirmations.jar` | 13 | unknown |
| `FR_Contract.jar` | 28 | unknown |
| `FR_Delivery.jar` | 2 | unknown |
| `FR_Foundation.jar` | 11 | unknown |
| `FR_PositionAndReval.jar` | 16 | unknown |
| `FR_Reports.jar` | 23 | unknown |
| `FR_TradeAndHedge.jar` | 38 | unknown |
| `FRNPAI_PostalAddressUpdate.jar` | 10 | unknown |
| `FRPFNL_InvestmentIncomeTax.jar` | 13 | unknown |
| `FRPLCL_Foundation.jar` | 59 | unknown |
| `FRPLCL_ManagePel.jar` | 20 | unknown |
| `FRRIBN_Foundation.jar` | 7 | unknown |
| `FRTAEG_Foundation.jar` | 34 | unknown |
| `HKBASE_Foundation.jar` | 29 | unknown |
| `HKCRSR_Foundation.jar` | 11 | unknown |
| `HKDDPR_Foundation.jar` | 85 | unknown |
| `HKDEPO_Foundation.jar` | 28 | unknown |
| `HKECHQ_Foundation.jar` | 8 | unknown |
| `HKLEND_Foundation.jar` | 15 | unknown |
| `HKLEND_IntRateComparison.jar` | 3 | unknown |
| `HKLEND_MortgageInsuranceProgram.jar` | 9 | unknown |
| `HKLEND_PrepaymentPayoff.jar` | 4 | unknown |
| `HKREGS_Foundation.jar` | 23 | unknown |
| `HUASTM_EbkmCalculation.jar` | 2 | unknown |
| `HUGIRO_IG2SettlementReports.jar` | 12 | unknown |
| `HUGIRO_Lookup.jar` | 14 | unknown |
| `HUPYAV_AccountValidation.jar` | 7 | unknown |
| `HUTXNF_Foundation.jar` | 21 | unknown |
| `HUTXNF_TransactionFeeHook.jar` | 5 | public-api, unknown |
| `HUTXNF_TransactionLevy.jar` | 32 | unknown |
| `HUWRNT_Queuing.jar` | 294 | unknown |
| `IL_Config.jar` | 24 | unknown |
| `ILBNKB_AccountValidation.jar` | 6 | unknown |
| `ILBNKB_BankBranchImport.jar` | 6 | unknown |
| `ILCOPM_CollateralPosition.jar` | 18 | unknown |
| `ILDLLI_CpiFcyLinkedInterest.jar` | 13 | unknown |
| `ILDXPR_PremiumStrikeQuoting.jar` | 18 | unknown |
| `ILFEES_FeeOptimisation.jar` | 24 | unknown |
| `ILIPOA_Allocation.jar` | 17 | unknown |
| `ILIPOA_InitialPublicOfferingHook.jar` | 3 | public-api, unknown |
| `ILMATX_MatrixTaxServerInterface.jar` | 85 | unknown |
| `ILSBLF_AgreementConditions.jar` | 12 | unknown |
| `ILSCPR_LimitPrice.jar` | 4 | unknown |
| `ILSCPR_PriceFeed.jar` | 16 | unknown |
| `ILTRCL_TradeCalendarAttributes.jar` | 9 | unknown |
| `IN_Config.jar` | 47 | unknown |
| `IN_IbanSystemApi.jar` | 5 | public-api, unknown |
| `INACCT_Foundation.jar` | 76 | unknown |
| `INBASE_CustomerValidations.jar` | 49 | unknown |
| `INCMMS_Config.jar` | 6 | unknown |
| `INDPMS_Foundation.jar` | 164 | unknown |
| `INFRMA_ANACredit.jar` | 14 | unknown |
| `INFRMA_Reporting.jar` | 12 | unknown |
| `INGAAP_Foundation.jar` | 10 | unknown |
| `INGAAP_LTR.jar` | 2 | unknown |
| `INGAAP_Offbalance.jar` | 10 | unknown |
| `INGAAP_Repo.jar` | 11 | unknown |
| `INGAAP_Securities.jar` | 3 | unknown |
| `INLEND_Foundation.jar` | 113 | unknown |
| `INPYMT_Foundation.jar` | 19 | unknown |
| `INSFMS_Foundation.jar` | 47 | unknown |
| `INTDFN_Foundation.jar` | 17 | unknown |
| `ITACIN_AccountInfrastructure.jar` | 3 | unknown |
| `ITREGE_AccountMovements.jar` | 30 | unknown |
| `ITREGE_AgencyRevenue.jar` | 21 | unknown |
| `ITREGE_BankTransfers.jar` | 11 | unknown |
| `ITREGE_Foundation.jar` | 26 | unknown |
| `ITREGE_PortfolioMovements.jar` | 21 | unknown |
| `ITREGE_Transactions.jar` | 24 | unknown |
| `ITREGE_TransactionsAPI.jar` | 3 | public-api, unknown |
| `ITREGE_TransferOfBalances.jar` | 5 | unknown |
| `ITSDCR_CreditorRegistry.jar` | 2 | unknown |
| `JP_Engine.jar` | 6 | unknown |
| `JP_Foundation.jar` | 19 | unknown |
| `JP_ModelBank.jar` | 5 | unknown |
| `LUCUPI_CardsProcessing.jar` | 22 | unknown |
| `LUCUPI_MultilineExtract.jar` | 15 | unknown |
| `LUCUPI_UnsupportedFileFormat.jar` | 12 | unknown |
| `LUFDRT_FdrTaxation.jar` | 15 | unknown |
| `LUFECH_Foundation.jar` | 16 | unknown |
| `LUINTX_CertificateOfInterest.jar` | 14 | unknown |
| `LUTXRG_Foundation.jar` | 23 | unknown |
| `MXACCT_AccountClabe.jar` | 2 | unknown |
| `MXACCT_GATCalculation.jar` | 5 | unknown |
| `MXACCT_ProductConfiguration.jar` | 4 | unknown |
| `MXACCT_UDILimitAccount.jar` | 5 | unknown |
| `MXBASE_CustomerRegulatory.jar` | 12 | unknown |
| `MXBASE_Foundation.jar` | 1 | unknown |
| `MXBASE_IdValidation.jar` | 8 | unknown |
| `MXCRED_CATCalculation.jar` | 2 | unknown |
| `MXCRED_InflationAdjustedInterest.jar` | 3 | unknown |
| `MXPYMT_BeneficiaryAcTypeValidation.jar` | 2 | unknown |
| `MXPYMT_BeneficiaryLimitValidation.jar` | 2 | unknown |
| `MXPYMT_Foundation.jar` | 2 | unknown |
| `MXPYMT_PaymentInitiationWaiting.jar` | 3 | unknown |
| `NLBASS_BankSwitchingService.jar` | 7 | unknown |
| `NLCEMD_Foundation.jar` | 9 | unknown |
| `NLGSDD_Governmentorder.jar` | 6 | unknown |
| `NLIDIN_CustomerAuthentication.jar` | 11 | unknown |
| `NLIDLP_Foundation.jar` | 10 | unknown |
| `NLNACV_NameNumberCheck.jar` | 2 | unknown |
| `NLPRIV_PaymentReference.jar` | 2 | unknown |
| `NOLEND_Foundation.jar` | 17 | unknown |
| `NOLEND_LoanApi.jar` | 3 | public-api, unknown |
| `NORACC_Foundation.jar` | 14 | unknown |
| `NORACC_JointCustomerProcessing.jar` | 8 | unknown |
| `NORCOL_Foundation.jar` | 4 | unknown |
| `NORNDI_Lending.jar` | 14 | unknown |
| `NORPIC_PenaltyInterestCalculation.jar` | 3 | unknown |
| `NORPIR_PeriodicRateReset.jar` | 7 | unknown |
| `NORSIC_SubsidyInterestCalculation.jar` | 45 | unknown |
| `NORWHT_Foundation.jar` | 4 | unknown |
| `NOTICE_Foundation.jar` | 7 | unknown |
| `NZBASE_CustomerAccountInfrastructure.jar` | 7 | unknown |
| `NZDEPO_ReinvestmentInstructions.jar` | 23 | unknown |
| `NZDEPO_TDBreakCost.jar` | 21 | unknown |
| `NZOBRS_OpenBankResolution.jar` | 24 | unknown |
| `QA_Api.jar` | 9 | unknown |
| `QA_Archiving.jar` | 5 | unknown |
| `QA_Contract.jar` | 18 | unknown |
| `QAACIN_CustomerInfoCapture.jar` | 1 | unknown |
| `QAACIN_DormantAccounts.jar` | 20 | unknown |
| `SA_Foundation.jar` | 40 | unknown |
| `SA_ModelBank.jar` | 9 | unknown |
| `SAACIN_AccountFreezing.jar` | 13 | unknown |
| `SAACIN_AccountStatement.jar` | 15 | unknown |
| `SAAELM_Foundation.jar` | 8 | unknown |
| `SABASE_Foundation.jar` | 14 | unknown |
| `SACUIN_CustomerIdExpiry.jar` | 26 | unknown |
| `SACUIN_NonCustForeignExchange.jar` | 13 | unknown |
| `SACUIN_SpecificAccounts.jar` | 4 | unknown |
| `SAHJRI_Foundation.jar` | 19 | unknown |
| `SALBLK_SalaryBlocking.jar` | 20 | unknown |
| `SAPWPS_WagesProcessing.jar` | 10 | unknown |
| `SAREGS_AutoIjarah.jar` | 4 | unknown |
| `SAREGS_CustomerDeposits.jar` | 2 | unknown |
| `SAREGS_EarlyClosure.jar` | 10 | unknown |
| `SAREGS_EarlyClosureAPI.jar` | 4 | public-api, unknown |
| `SAREGS_IslamicLoanApi.jar` | 3 | public-api, unknown |
| `SASIMA_Foundation.jar` | 63 | unknown |
| `SAWATQ_Foundation.jar` | 35 | unknown |
| `SG_Framework.jar` | 9 | unknown |
| `SG_Service.jar` | 4 | unknown |
| `SGWHTX_Foundation.jar` | 1 | unknown |
| `UKBBSI_Foundation.jar` | 12 | unknown |
| `UKBSFU_Foundation.jar` | 11 | unknown |
| `UKCLGS_BacsDirectCredits.jar` | 7 | unknown |
| `UKCRSR_CRSReporting.jar` | 11 | unknown |
| `UKDDMP_Import.jar` | 11 | unknown |
| `UKDDMP_Lodgements.jar` | 60 | unknown |
| `UKFCOA_Accounting.jar` | 34 | unknown |
| `UKFCOA_Party.jar` | 3 | unknown |
| `UKFSCS_Party.jar` | 5 | unknown |
| `UKFSCS_Reporting.jar` | 33 | unknown |
| `UKISA1_Party.jar` | 4 | unknown |
| `UKISA1_Reporting.jar` | 70 | unknown |
| `UKISAT_Party.jar` | 3 | unknown |
| `UKISAT_Transfer.jar` | 15 | unknown |
| `UKOBPX_Foundation.jar` | 30 | unknown |
| `UKOBPZ_ConditionalApis.jar` | 20 | unknown |
| `UKOBPZ_Foundation.jar` | 21 | unknown |
| `UKOIRT_OtherInterest.jar` | 12 | unknown |
| `UKOIRT_Party.jar` | 3 | unknown |
| `UKSTAT_Foundation.jar` | 12 | unknown |
| `USCK21_Foundation.jar` | 13 | unknown |
| `USCORE_Atmvisadps.jar` | 8 | unknown |
| `USCORE_CDBalReporting.jar` | 12 | unknown |
| `USCORE_CustomerRestriction.jar` | 7 | unknown |
| `USCORE_DocImageMgmt.jar` | 1 | unknown |
| `USCORE_Foundation.jar` | 278 | unknown |
| `USCORE_Holds.jar` | 18 | unknown |
| `USIRAC_IRA.jar` | 78 | unknown |
| `USLEND_CouponBooks.jar` | 11 | unknown |
| `USLEND_EscrowProcessing.jar` | 101 | unknown |
| `USLEND_Foundation.jar` | 12 | unknown |
| `USLEND_LoanParticipation.jar` | 18 | unknown |
| `USLEND_SecondaryMarket.jar` | 7 | unknown |
| `USLREG_FloodInsurance.jar` | 7 | unknown |
| `USLREG_Foundation.jar` | 10 | unknown |
| `USLREG_LegalStatusFlag.jar` | 7 | unknown |
| `USLREG_OverdueEnquiry.jar` | 5 | unknown |
| `USLREG_OverdueNotices.jar` | 8 | unknown |
| `USLREG_PaymentProcessing.jar` | 4 | unknown |
| `USLREG_RateChange.jar` | 17 | unknown |
| `USLREG_RebatableInsurance.jar` | 17 | unknown |
| `USLREG_RegAA.jar` | 6 | unknown |
| `USLREG_RegBB.jar` | 3 | unknown |
| `USLREG_RegO.jar` | 14 | unknown |
| `USLREG_RegZ.jar` | 2 | unknown |
| `USLREG_RestrictedBackdating.jar` | 6 | unknown |
| `USRDCI_Alogent.jar` | 5 | unknown |
| `USREGS_ACH.jar` | 20 | unknown |
| `USREGS_AddressChange.jar` | 22 | unknown |
| `USREGS_BNotice.jar` | 14 | unknown |
| `USREGS_CEDD.jar` | 10 | unknown |
| `USREGS_CTR.jar` | 32 | unknown |
| `USREGS_Escheat.jar` | 48 | unknown |
| `USREGS_FDIC.jar` | 69 | unknown |
| `USREGS_FIDM.jar` | 20 | unknown |
| `USREGS_FinCENBeneficialOwner.jar` | 7 | unknown |
| `USREGS_Foundation.jar` | 27 | unknown |
| `USREGS_RegCC.jar` | 4 | unknown |
| `USREGS_RegD.jar` | 22 | unknown |
| `USREGS_RegDD.jar` | 11 | unknown |
| `USREGS_RegE.jar` | 37 | unknown |
| `USREGS_RegP.jar` | 7 | unknown |
| `USREGS_Reports.jar` | 11 | unknown |
| `USREGS_YearEndTaxReporting.jar` | 87 | unknown |
| `USRETL_AccountAnalysis.jar` | 33 | unknown |
| `USRETL_AccountTitle.jar` | 6 | unknown |
| `USRETL_AuditReport.jar` | 10 | unknown |
| `USRETL_AutoAccountClosure.jar` | 25 | unknown |
| `USRETL_Bonus.jar` | 12 | unknown |
| `USRETL_CheckCollection.jar` | 16 | unknown |
| `USRETL_CheckProduction.jar` | 14 | unknown |
| `USRETL_CombinedStatement.jar` | 73 | unknown |
| `USRETL_EarlyRepaymentFee.jar` | 9 | unknown |
| `USRETL_Ebanking.jar` | 13 | unknown |
| `USRETL_Foundation.jar` | 43 | unknown |
| `USRETL_HistoryMigration.jar` | 28 | unknown |
| `USRETL_InterestpaidInquiry.jar` | 6 | unknown |
| `USRETL_InternalCheckProduction.jar` | 11 | unknown |
| `USRETL_PositivePay.jar` | 33 | unknown |
| `USRETL_SDB.jar` | 18 | unknown |
| `USRETL_TransactionStop.jar` | 15 | unknown |
| `USRSRS_RetailSweepPgm.jar` | 27 | unknown |
| `USRTGS_Fedwire.jar` | 137 | unknown |
| `USRTGS_FedwireHook.jar` | 5 | public-api, unknown |
| `USRTGS_FedwireService.jar` | 6 | unknown |
