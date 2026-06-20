# Securities — Reference

> Generated 2026-06-20T03:39:43.046735+00:00 from 106 JARs. Re-run `aggregate.py` to refresh.

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
| `Delivery` | `SC_DeliveryHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to define one or more records to be input using the specified transaction data. |
| `Delivery` | `SC_DeliveryHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to define one or more records to be input using the specified transaction data. |
| `Delivery` | `SC_DeliveryHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to define one or more records to be input using the specified transaction data. |
| `Delivery` | `SC_DeliveryHook.jar` | `updateSecuritiesRecords` | `void` | This interface enables the implementer to define one or more records to be input using the specified transaction data. |
| `Security` | `SC_SecuritiesApi.jar` | `getVersion` | `java.lang.String` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getSecurityMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `getSecurityMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `map513MessageToExecuteSecurityOrdersRecord` | `void` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `map515MessageToRecord` | `void` | Create a new Security using a specific context.. |
| `Security` | `SC_SecuritiesApi.jar` | `map540ToSecurityTransferRecord` | `void` | Create a new Security using a specific context.. |
| `Transaction` | `SC_TransactionHook.jar` | `getVersion` | `java.lang.String` | This interface allows the developer to allocate the executed nominal for a single security order in a bulk order group. |
| `Transaction` | `SC_TransactionHook.jar` | `getBuildDate` | `java.lang.String` | This interface allows the developer to allocate the executed nominal for a single security order in a bulk order group. |
| `Transaction` | `SC_TransactionHook.jar` | `getComponentVersion` | `java.lang.String` | This interface allows the developer to allocate the executed nominal for a single security order in a bulk order group. |
| `Transaction` | `SC_TransactionHook.jar` | `allocateOrderNominals` | `void` | This interface allows the developer to allocate the executed nominal for a single security order in a bulk order group. |
| `Transaction` | `SC_TransactionHook.jar` | `isGroupSecurityOrder` | `com.temenos.api.TBoolean` | This interface allows the developer to allocate the executed nominal for a single security order in a bulk order group. |
| `Valuation` | `SC_ValuationHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `calculateStampTaxAndEbvFees` | `void` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `setSecurityPortfolioAssetPositions` | `void` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `updatePortfolioAssetPositions` | `void` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `getSecurityPortfolioContracts` | `java.util.List<java.lang.String>` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `sortTransactionPositionHistory` | `void` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `sortSecurityTradePosition` | `void` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `Valuation` | `SC_ValuationHook.jar` | `setStructuredProductsAssetPositions` | `void` | This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc. |
| `BIC` | `ST_BicApi.jar` | `getVersion` | `java.lang.String` | Create a new BIC using a specific context.. |
| `BIC` | `ST_BicApi.jar` | `getBuildDate` | `java.lang.String` | Create a new BIC using a specific context.. |
| `BIC` | `ST_BicApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new BIC using a specific context.. |
| `BIC` | `ST_BicApi.jar` | `getBicInformation` | `com.temenos.t24.api.complex.st.bicapi.BicInformation` | Create a new BIC using a specific context.. |
| `Calculation` | `ST_CalculationHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateBaseAmount` | `void` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateTaxAmount` | `com.temenos.t24.api.complex.st.calculationhook.ChargeAmount` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `getTaxAmount` | `com.temenos.t24.api.complex.st.calculationhook.ChargeAmount` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateCharge` | `com.temenos.t24.api.complex.st.calculationhook.ChargeAmount` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateRate` | `void` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateSweepAmount` | `com.temenos.api.TNumber` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateTwoWaySweepAmount` | `com.temenos.api.TNumber` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `calculateEodSweepAmount` | `com.temenos.api.TNumber` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `updatePrincipal` | `void` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Calculation` | `ST_CalculationHook.jar` | `getAmortizationAmount` | `com.temenos.api.TNumber` | This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc. |
| `Currency` | `ST_CurrencyApi.jar` | `getVersion` | `java.lang.String` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `setCurrencyId` | `void` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateExchangeRate` | `com.temenos.api.TNumber` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `getRoundAmount` | `com.temenos.api.TNumber` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateForwardBidValueRate` | `com.temenos.t24.api.complex.st.currencyapi.ForwardRate` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateForwardMidValueRate` | `com.temenos.t24.api.complex.st.currencyapi.ForwardRate` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateForwardOfferValueRate` | `com.temenos.t24.api.complex.st.currencyapi.ForwardRate` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `getCurrencyRates` | `java.util.List<com.temenos.t24.api.complex.st.currencyapi.CurrencyRate>` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `getForwardRate` | `com.temenos.t24.api.records.forwardrates.ForwardRatesRecord` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateRate` | `com.temenos.api.TNumber` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateBuyAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeAmount` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateSellAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeAmount` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateBuyExchangeRateAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeRateAmount` | Create a new Currency using a specific context.. |
| `Currency` | `ST_CurrencyApi.jar` | `calculateSellExchangeRateAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeRateAmount` | Create a new Currency using a specific context.. |
| `Customer` | `ST_CustomerApi.jar` | `getVersion` | `java.lang.String` |  |
| `Customer` | `ST_CustomerApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Customer` | `ST_CustomerApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Customer` | `ST_CustomerApi.jar` | `setCustomerId` | `void` |  |
| `Customer` | `ST_CustomerApi.jar` | `customerExists` | `com.temenos.api.TBoolean` |  |
| `Customer` | `ST_CustomerApi.jar` | `getPersonalInfo` | `com.temenos.t24.api.complex.st.customerapi.PersonalInfo` |  |
| `Customer` | `ST_CustomerApi.jar` | `getProfile` | `com.temenos.t24.api.complex.st.customerapi.Profile` |  |
| `Customer` | `ST_CustomerApi.jar` | `getOfficer` | `com.temenos.t24.api.complex.st.customerapi.Officer` |  |
| `Customer` | `ST_CustomerApi.jar` | `getName` | `com.temenos.t24.api.complex.st.customerapi.Name` |  |
| `Customer` | `ST_CustomerApi.jar` | `getContactInfo` | `com.temenos.t24.api.complex.st.customerapi.ContactInfo` |  |
| `Customer` | `ST_CustomerApi.jar` | `getLanguage` | `java.lang.String` |  |
| `Customer` | `ST_CustomerApi.jar` | `getIdForMnemonic` | `java.lang.String` |  |
| `Customer` | `ST_CustomerApi.jar` | `getAccountNumbers` | `java.util.List<java.lang.String>` |  |
| `Customer` | `ST_CustomerApi.jar` | `getParentId` | `java.lang.String` |  |
| `Customer` | `ST_CustomerApi.jar` | `getRelationDetail` | `java.util.List<com.temenos.t24.api.complex.st.customerapi.Relationship>` |  |
| `Customer` | `ST_CustomerApi.jar` | `getPostingRestriction` | `com.temenos.t24.api.complex.st.customerapi.Restriction` |  |
| `Customer` | `ST_CustomerApi.jar` | `getMandateItems` | `java.util.List<com.temenos.t24.api.complex.st.customerapi.Mandates>` |  |
| `Customer` | `ST_CustomerApi.jar` | `getIdentificationDocuments` | `java.util.List<com.temenos.t24.api.complex.st.customerapi.Document>` |  |
| `Customer` | `ST_CustomerApi.jar` | `getSwiftAddress` | `com.temenos.t24.api.complex.st.customerapi.SwiftAddress` |  |
| `Customer` | `ST_CustomerApi.jar` | `getDeliverySecureMessageAddress` | `com.temenos.t24.api.complex.st.customerapi.SecureMessageAddress` |  |
| `Customer` | `ST_CustomerApi.jar` | `getEmailAddress` | `com.temenos.t24.api.complex.st.customerapi.EmailAddress` |  |
| `Customer` | `ST_CustomerApi.jar` | `getAgency` | `com.temenos.t24.api.complex.st.customerapi.Agency` |  |
| `Customer` | `ST_CustomerApi.jar` | `getLimit` | `com.temenos.t24.api.complex.st.customerapi.LimitAmount` |  |
| `Customer` | `ST_CustomerApi.jar` | `getLiableLimit` | `com.temenos.t24.api.complex.st.customerapi.LimitAmount` |  |
| `Customer` | `ST_CustomerApi.jar` | `getSettlementAccountId` | `com.temenos.t24.api.complex.st.customerapi.Settlement` |  |
| `CustomerPosition` | `ST_EnquiryHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the list of contract id's which will be taken forward by CUSTOMER.POSITION enquiry. |
| `CustomerPosition` | `ST_EnquiryHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the list of contract id's which will be taken forward by CUSTOMER.POSITION enquiry. |
| `CustomerPosition` | `ST_EnquiryHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the list of contract id's which will be taken forward by CUSTOMER.POSITION enquiry. |
| `CustomerPosition` | `ST_EnquiryHook.jar` | `getContractIds` | `java.util.List<com.temenos.t24.api.complex.st.enquiryhook.CustomerPositionId>` | This interface enables the implementer to return the list of contract id's which will be taken forward by CUSTOMER.POSITION enquiry. |
| `CustomerPosition` | `ST_EnquiryHook.jar` | `inputCustomerPositionRecord` | `void` | This interface enables the implementer to return the list of contract id's which will be taken forward by CUSTOMER.POSITION enquiry. |
| `Interest` | `ST_InterestApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `setInterestId` | `void` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `calculateAccrualDays` | `com.temenos.api.TNumber` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getBasicRate` | `com.temenos.api.TNumber` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getTermRate` | `com.temenos.t24.api.complex.st.interestapi.TermRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getTermMarginRate` | `com.temenos.t24.api.complex.st.interestapi.TermRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getTermMisRate` | `com.temenos.t24.api.complex.st.interestapi.TermRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Interest` | `ST_InterestApi.jar` | `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `StatementEntry` | `ST_StatementHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the transaction Id of the application. |
| `StatementEntry` | `ST_StatementHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the transaction Id of the application. |
| `StatementEntry` | `ST_StatementHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the transaction Id of the application. |
| `StatementEntry` | `ST_StatementHook.jar` | `getTransactionType` | `java.lang.String` | This interface enables the implementer to return the transaction Id of the application. |
| `StatementEntry` | `ST_StatementHook.jar` | `getTransactionId` | `java.lang.String` | This interface enables the implementer to return the transaction Id of the application. |

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
| `SC_CapitalGainsService.jar` | 7 | unknown |
| `SC_Config.jar` | 225 | unknown |
| `SC_Delivery.jar` | 2 | unknown |
| `SC_DeliveryHook.jar` | 3 | public-api, unknown |
| `SC_Mifid.jar` | 25 | unknown |
| `SC_ModelBank.jar` | 161 | unknown |
| `SC_ReposInterface.jar` | 14 | unknown |
| `SC_SccClassicCA.jar` | 128 | unknown |
| `SC_SccConfig.jar` | 35 | unknown |
| `SC_SccEntitlements.jar` | 318 | unknown |
| `SC_SccEventCapture.jar` | 107 | unknown |
| `SC_SccEventNotification.jar` | 112 | unknown |
| `SC_SccReports.jar` | 31 | unknown |
| `SC_ScfAdvisoryFees.jar` | 85 | unknown |
| `SC_ScfConfig.jar` | 58 | unknown |
| `SC_ScfSafeAdvDailyAccr.jar` | 46 | unknown |
| `SC_ScfSafekeepingFees.jar` | 86 | unknown |
| `SC_ScfTrailerFees.jar` | 77 | unknown |
| `SC_ScoFoundation.jar` | 60 | unknown |
| `SC_ScoPortfolioMaintenance.jar` | 91 | unknown |
| `SC_ScoReports.jar` | 54 | unknown |
| `SC_ScoSecurityMasterMaintenance.jar` | 185 | unknown |
| `SC_ScoSecurityPositionUpdate.jar` | 160 | unknown |
| `SC_ScPeFunds.jar` | 64 | unknown |
| `SC_ScSrdEventCapture.jar` | 39 | unknown |
| `SC_SctBlocking.jar` | 28 | unknown |
| `SC_SctBonds.jar` | 25 | unknown |
| `SC_SctCapitalGains.jar` | 306 | unknown |
| `SC_SctConstraints.jar` | 28 | unknown |
| `SC_SctDealerBook.jar` | 68 | unknown |
| `SC_SctDealerBookPosition.jar` | 39 | unknown |
| `SC_SctDepoSubAccount.jar` | 20 | unknown |
| `SC_SctFees.jar` | 69 | unknown |
| `SC_SctModelling.jar` | 68 | unknown |
| `SC_SctNonStop.jar` | 7 | unknown |
| `SC_SctOffMarketTrades.jar` | 68 | unknown |
| `SC_SctOrderCapture.jar` | 103 | unknown |
| `SC_SctOrderExecution.jar` | 33 | unknown |
| `SC_SctOrderGrouping.jar` | 23 | unknown |
| `SC_SctOtherAssets.jar` | 22 | unknown |
| `SC_SctPositionTransfer.jar` | 43 | unknown |
| `SC_SctPriceTypeUpdateAndProcessing.jar` | 78 | unknown |
| `SC_SctSecurityLending.jar` | 20 | unknown |
| `SC_SctServiceBasedOrders.jar` | 218 | unknown |
| `SC_SctSettlement.jar` | 188 | unknown |
| `SC_SctStockReconciliation.jar` | 55 | unknown |
| `SC_SctStockRecord.jar` | 21 | unknown |
| `SC_SctTaxes.jar` | 20 | unknown |
| `SC_SctTrading.jar` | 194 | unknown |
| `SC_SctTransactionStatement.jar` | 24 | unknown |
| `SC_SctVault.jar` | 28 | unknown |
| `SC_ScvCashAndFundFlow.jar` | 90 | unknown |
| `SC_ScvConfig.jar` | 33 | unknown |
| `SC_ScvReports.jar` | 86 | unknown |
| `SC_ScvValuationUpdates.jar` | 282 | unknown |
| `SC_SecuritiesApi.jar` | 6 | public-api, unknown |
| `SC_SecuritiesEventsService.jar` | 13 | unknown |
| `SC_STP.jar` | 72 | unknown |
| `SC_TransactionHook.jar` | 4 | public-api, unknown |
| `SC_ValuationHook.jar` | 9 | public-api, unknown |
| `SE_Foundation.jar` | 57 | unknown |
| `SE_JavaHooks.jar` | 2 | unknown |
| `SE_MDACustomer.jar` | 13 | unknown |
| `SE_MDAMarketData.jar` | 14 | unknown |
| `SE_MDAReferenceData.jar` | 27 | unknown |
| `SE_MDAReferenceDirectory.jar` | 11 | unknown |
| `SE_MDARegistry.jar` | 4 | unknown |
| `SE_ModelBank.jar` | 33 | unknown |
| `SE_MSBalActApi.jar` | 7 | unknown |
| `SE_SeatHeatMap.jar` | 19 | unknown |
| `SE_TestBankingFramework.jar` | 302 | unknown |
| `SE_TestFramework.jar` | 475 | unknown |
| `SE_TestOtherApplication.jar` | 405 | unknown |
| `SE_TestRetail.jar` | 330 | unknown |
| `SE_TestToolsFramework.jar` | 16 | unknown |
| `SE_UKPTYCustomer.jar` | 5 | unknown |
| `ST_AliasManagement.jar` | 42 | unknown |
| `ST_AssetProcessing.jar` | 42 | unknown |
| `ST_BicApi.jar` | 3 | public-api, unknown |
| `ST_CalculationHook.jar` | 12 | public-api, unknown |
| `ST_Calendar.jar` | 6 | unknown |
| `ST_Channels.jar` | 9 | unknown |
| `ST_ChargeConfig.jar` | 62 | unknown |
| `ST_CompanyCreation.jar` | 59 | unknown |
| `ST_Config.jar` | 204 | unknown |
| `ST_CurrencyApi.jar` | 9 | public-api, unknown |
| `ST_CurrencyConfig.jar` | 48 | unknown |
| `ST_CurrencyExchangeService.jar` | 10 | unknown |
| `ST_Customer.jar` | 292 | unknown |
| `ST_CustomerActivity.jar` | 78 | unknown |
| `ST_CustomerApi.jar` | 23 | public-api, unknown |
| `ST_CustomerService.jar` | 80 | unknown |
| `ST_DormancyMonitor.jar` | 44 | unknown |
| `ST_EnquiryHook.jar` | 4 | public-api, unknown |
| `ST_ExchangeRate.jar` | 23 | unknown |
| `ST_IbanAPI.jar` | 19 | unknown |
| `ST_InterestApi.jar` | 6 | public-api, unknown |
| `ST_ModelBank.jar` | 78 | unknown |
| `ST_OrganizationStructure.jar` | 30 | unknown |
| `ST_Payments.jar` | 5 | unknown |
| `ST_RateParameters.jar` | 105 | unknown |
| `ST_ReferenceAPI.jar` | 12 | unknown |
| `ST_StatementHook.jar` | 4 | public-api, unknown |
| `ST_Sweeping.jar` | 18 | unknown |
| `ST_TreGroupRateFixing.jar` | 14 | unknown |
| `ST_Valuation.jar` | 39 | unknown |
