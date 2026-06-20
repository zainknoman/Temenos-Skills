# Arrangement Architecture (AA) — Reference

> Generated 2026-06-20T03:17:58.699072+00:00 from 99 JARs. Re-run `aggregate.py` to refresh.

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
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `getVersion` | `java.lang.String` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `defaultFieldValues` | `void` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `generateSecondaryActivity` | `void` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `postCoreTableUpdate` | `void` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `validateRecord` | `com.temenos.api.TValidationResponse` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `updateLookupTable` | `com.temenos.api.TBoolean` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `setElementData` | `void` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `filterElements` | `java.util.List<java.lang.String>` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `filterAccrualProperties` | `void` |  |
| `Bill` | `AA_BillApi.jar` | `getVersion` | `java.lang.String` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `setContractId` | `void` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `getContractId` | `java.lang.String` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `setBillId` | `void` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `getBillId` | `java.lang.String` | Create a new Bill using a specific context.. |
| `Bill` | `AA_BillApi.jar` | `getBillRecord` | `com.temenos.t24.api.records.aabilldetails.AaBillDetailsRecord` | Create a new Bill using a specific context.. |
| `Calculation` | `AA_CalculationHook.jar` | `getVersion` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `calculateSourceBalance` | `void` |  |
| `Calculation` | `AA_CalculationHook.jar` | `calculatePayment` | `com.temenos.api.TNumber` |  |
| `Calculation` | `AA_CalculationHook.jar` | `calculateUncSettledAmount` | `com.temenos.api.TNumber` |  |
| `Calculation` | `AA_CalculationHook.jar` | `calculateCharge` | `void` |  |
| `Calculation` | `AA_CalculationHook.jar` | `calculateAdjustedCharge` | `void` |  |
| `Calculation` | `AA_CalculationHook.jar` | `SortDrawingsArrangements` | `void` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getChargeAmount` | `com.temenos.api.TNumber` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getAdjustedChargeAmount` | `com.temenos.t24.api.complex.aa.calculationhook.ChargeAdjustment` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getDataElementValue` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getBreakCostFeeInterestRates` | `com.temenos.t24.api.complex.aa.calculationhook.AdjustedInterest` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getInterestCustomRate` | `void` |  |
| `Contract` | `AA_ContractApi.jar` | `getVersion` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `setContractId` | `void` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractId` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBalanceMovementsForPeriod` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getForwardCreditBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getForwardDebitBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getAllBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractBalanceMovementsForPeriod` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractForwardCreditBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractForwardDebitBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getAllContractBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` |  |
| `Contract` | `AA_ContractApi.jar` | `getInterestAmounts` | `com.temenos.t24.api.complex.aa.contractapi.InterestAmount` |  |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepayment` | `com.temenos.api.TNumber` |  |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepaymentForProperty` | `com.temenos.api.TNumber` |  |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepaymentForPeriod` | `com.temenos.api.TNumber` |  |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepaymentForMonth` | `com.temenos.api.TNumber` |  |
| `Contract` | `AA_ContractApi.jar` | `getLastRepayment` | `com.temenos.t24.api.complex.aa.contractapi.Payment` |  |
| `Contract` | `AA_ContractApi.jar` | `getNextPayment` | `com.temenos.t24.api.complex.aa.contractapi.Payment` |  |
| `Contract` | `AA_ContractApi.jar` | `getAccountDetailsRecord` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getInterestAccrualsRecord` | `com.temenos.t24.api.records.aainterestaccruals.AaInterestAccrualsRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForPayMethod` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForDate` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForPaymentDate` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForBillType` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForBillStatus` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForSettlementStatus` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForAgingStatus` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForNextAgeDate` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForRepaymentReference` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getBillIds` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getContract` | `com.temenos.t24.api.records.aaarrangement.AaArrangementRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getCustomerRole` | `com.temenos.t24.api.complex.aa.contractapi.CustomerRole` |  |
| `Contract` | `AA_ContractApi.jar` | `getNextDueDate` | `com.temenos.api.TDate` |  |
| `Contract` | `AA_ContractApi.jar` | `getFirstOverdueDate` | `com.temenos.api.TDate` |  |
| `Contract` | `AA_ContractApi.jar` | `getLastOverDueDate` | `com.temenos.api.TDate` |  |
| `Contract` | `AA_ContractApi.jar` | `getNumberOfOverDueBills` | `com.temenos.api.TNumber` |  |
| `Contract` | `AA_ContractApi.jar` | `getMaturityDate` | `com.temenos.api.TDate` |  |
| `Contract` | `AA_ContractApi.jar` | `getPropertyIds` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getPropertyIdsForPropertyClass` | `java.util.List<java.lang.String>` |  |
| `Contract` | `AA_ContractApi.jar` | `getTerm` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getTermAmount` | `com.temenos.api.TNumber` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractAgeStatus` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getProductId` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getProductIdForEffectiveDate` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getSimulationId` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getAccountCondition` | `com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getAccountConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getCustomerCondition` | `com.temenos.t24.api.records.aaprddescustomer.AaPrdDesCustomerRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getCustomerConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddescustomer.AaPrdDesCustomerRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getInterestCondition` | `java.util.List<com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord>` |  |
| `Contract` | `AA_ContractApi.jar` | `getInterestConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord>` |  |
| `Contract` | `AA_ContractApi.jar` | `getLimitCondition` | `com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getLimitConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getOfficersCondition` | `com.temenos.t24.api.records.aaprddesofficers.AaPrdDesOfficersRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getOfficersConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddesofficers.AaPrdDesOfficersRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getCommitmentCondition` | `com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getCommitmentConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord` |  |
| `Contract` | `AA_ContractApi.jar` | `getChargeCondition` | `java.util.List<com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord>` |  |
| `Contract` | `AA_ContractApi.jar` | `getChargeConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord>` |  |
| `Contract` | `AA_ContractApi.jar` | `getRepaymentCondition` | `java.util.List<com.temenos.t24.api.records.aaprddespaymentrules.AaPrdDesPaymentRulesRecord>` |  |
| `Contract` | `AA_ContractApi.jar` | `getRepaymentConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddespaymentrules.AaPrdDesPaymentRulesRecord>` |  |
| `Contract` | `AA_ContractApi.jar` | `getConditionForProperty` | `com.temenos.api.TStructure` |  |
| `Contract` | `AA_ContractApi.jar` | `getConditionForPropertyEffectiveDate` | `com.temenos.api.TStructure` |  |
| `Contract` | `AA_ContractApi.jar` | `getSimulationConditionForProperty` | `com.temenos.api.TStructure` |  |
| `Contract` | `AA_ContractApi.jar` | `getFirstVersionOfProperty` | `com.temenos.api.TStructure` |  |
| `Contract` | `AA_ContractApi.jar` | `getPreviousDatedProperty` | `com.temenos.api.TStructure` |  |
| `Contract` | `AA_ContractApi.jar` | `getPreviousProperty` | `com.temenos.api.TStructure` |  |
| `Contract` | `AA_ContractApi.jar` | `buildPaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.PaymentSchedule>` |  |
| `Contract` | `AA_ContractApi.jar` | `buildPaymentScheduleForProperty` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.PaymentSchedule>` |  |
| `Contract` | `AA_ContractApi.jar` | `getFutureRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` |  |
| `Contract` | `AA_ContractApi.jar` | `getRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` |  |
| `Contract` | `AA_ContractApi.jar` | `getContractBeneficialOwner` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getOutstandingBalance` | `com.temenos.t24.api.complex.aa.contractapi.OutstandingBalances` |  |
| `Contract` | `AA_ContractApi.jar` | `getEffectiveInterestRate` | `com.temenos.t24.api.complex.aa.contractapi.EffectiveInterestRate` |  |
| `Contract` | `AA_ContractApi.jar` | `getEffectiveInterestRate` | `com.temenos.t24.api.complex.aa.contractapi.EffectiveInterestRate` |  |
| `Contract` | `AA_ContractApi.jar` | `getInterestProfitAmount` | `com.temenos.t24.api.complex.aa.contractapi.ProfitAmount` |  |
| `Contract` | `AA_ContractApi.jar` | `getActualDate` | `com.temenos.t24.api.complex.aa.contractapi.DateConversion` |  |
| `Contract` | `AA_ContractApi.jar` | `getFutureSimulationRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` |  |
| `Contract` | `AA_ContractApi.jar` | `getSimulationRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` |  |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getAvailableBalance` | `void` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `Product` | `AA_ProductApi.jar` | `getVersion` | `java.lang.String` | Create a new Product using a specific context.. |
| `Product` | `AA_ProductApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Product using a specific context.. |
| `Product` | `AA_ProductApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Product using a specific context.. |
| `Product` | `AA_ProductApi.jar` | `setProductId` | `void` | Create a new Product using a specific context.. |
| `Product` | `AA_ProductApi.jar` | `getProductId` | `java.lang.String` | Create a new Product using a specific context.. |
| `Product` | `AA_ProductApi.jar` | `getProduct` | `com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord` | Create a new Product using a specific context.. |
| `Property` | `AA_PropertyApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Property` | `AA_PropertyApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Property` | `AA_PropertyApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Property` | `AA_PropertyApi.jar` | `setPropertyId` | `void` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Property` | `AA_PropertyApi.jar` | `getPropertyId` | `java.lang.String` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Property` | `AA_PropertyApi.jar` | `getPropertyClassId` | `java.lang.String` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Property` | `AA_PropertyApi.jar` | `getPropertiesForProduct` | `com.temenos.api.TStructure` | Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getVersion` | `java.lang.String` | Create a new PropertyClass using a specific context.. |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getBuildDate` | `java.lang.String` | Create a new PropertyClass using a specific context.. |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new PropertyClass using a specific context.. |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `setPropertyClassId` | `void` | Create a new PropertyClass using a specific context.. |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getPropertyClassId` | `java.lang.String` | Create a new PropertyClass using a specific context.. |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getPropertyIdsForProduct` | `java.util.List<java.lang.String>` | Create a new PropertyClass using a specific context.. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getComparableValues` | `void` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `compareNegotiatedValue` | `void` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `validateNegotiableField` | `void` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getRelatedArrangements` | `void` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getDormancyException` | `com.temenos.t24.api.complex.aa.rulecomparisonhook.DormancyResponse` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getComparableStringValues` | `void` | This interface enables the implementer to compare arrangement values against default
value in the product property definition. |
| `Settlement` | `AA_SettlementHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `Settlement` | `AA_SettlementHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `Settlement` | `AA_SettlementHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |
| `Settlement` | `AA_SettlementHook.jar` | `validateUserRoutine` | `void` | This interface enables the implementer to return exceptions if any after execution of the User defined logic routine. |

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
| `AA_AaActivityExtractorService.jar` | 7 | unknown |
| `AA_Account.jar` | 165 | unknown |
| `AA_Accounting.jar` | 55 | unknown |
| `AA_ActivityAPI.jar` | 18 | unknown |
| `AA_ActivityCharges.jar` | 39 | unknown |
| `AA_ActivityControl.jar` | 6 | unknown |
| `AA_ActivityHook.jar` | 11 | public-api, unknown |
| `AA_ActivityMapping.jar` | 11 | unknown |
| `AA_ActivityMessaging.jar` | 49 | unknown |
| `AA_ActivityPresentation.jar` | 12 | unknown |
| `AA_ActivityRestriction.jar` | 31 | unknown |
| `AA_AgentCommission.jar` | 52 | unknown |
| `AA_Alerts.jar` | 18 | unknown |
| `AA_ARAccountsData.jar` | 4 | unknown |
| `AA_ARC.jar` | 43 | unknown |
| `AA_BalanceAvailability.jar` | 15 | unknown |
| `AA_BalanceMaintenance.jar` | 28 | unknown |
| `AA_BillApi.jar` | 3 | public-api, unknown |
| `AA_BundleHierarchy.jar` | 48 | unknown |
| `AA_CalculationHook.jar` | 14 | public-api, unknown |
| `AA_ChangeProduct.jar` | 17 | unknown |
| `AA_ChannelAccess.jar` | 11 | unknown |
| `AA_Channels.jar` | 13 | unknown |
| `AA_ChargeOff.jar` | 32 | unknown |
| `AA_ChargeOverride.jar` | 14 | unknown |
| `AA_ClassicProducts.jar` | 102 | unknown |
| `AA_Closure.jar` | 26 | unknown |
| `AA_Constraint.jar` | 21 | unknown |
| `AA_ContractApi.jar` | 59 | public-api, unknown |
| `AA_Customer.jar` | 68 | unknown |
| `AA_DepositData.jar` | 4 | unknown |
| `AA_Dormancy.jar` | 50 | unknown |
| `AA_Eligibility.jar` | 24 | unknown |
| `AA_EventStructures.jar` | 63 | unknown |
| `AA_Evidence.jar` | 21 | unknown |
| `AA_ExchangeRate.jar` | 14 | unknown |
| `AA_Facility.jar` | 27 | unknown |
| `AA_Feature.jar` | 42 | unknown |
| `AA_Fees.jar` | 127 | unknown |
| `AA_Framework.jar` | 837 | unknown |
| `AA_Inheritance.jar` | 11 | unknown |
| `AA_IntegrationFramework.jar` | 39 | unknown |
| `AA_Interest.jar` | 258 | unknown |
| `AA_InterestCompensation.jar` | 17 | unknown |
| `AA_Interfaces.jar` | 13 | unknown |
| `AA_LendingData.jar` | 3 | unknown |
| `AA_Limit.jar` | 62 | unknown |
| `AA_MarketingCatalogue.jar` | 86 | unknown |
| `AA_ModelBank.jar` | 437 | unknown |
| `AA_ModelBankBb.jar` | 5 | unknown |
| `AA_NoticeWithdrawal.jar` | 21 | unknown |
| `AA_Officers.jar` | 11 | unknown |
| `AA_Overdue.jar` | 49 | unknown |
| `AA_Participant.jar` | 54 | unknown |
| `AA_PaymentHoliday.jar` | 15 | unknown |
| `AA_PaymentPriority.jar` | 28 | unknown |
| `AA_PaymentRules.jar` | 47 | unknown |
| `AA_PaymentSchedule.jar` | 332 | unknown |
| `AA_PaymentScheduleHook.jar` | 3 | public-api, unknown |
| `AA_Payoff.jar` | 36 | unknown |
| `AA_PayoutRules.jar` | 17 | unknown |
| `AA_PeriodicCharges.jar` | 65 | unknown |
| `AA_PreferentialPricing.jar` | 12 | unknown |
| `AA_PreferentialPricingFx.jar` | 8 | unknown |
| `AA_PricingAdjustments.jar` | 11 | unknown |
| `AA_PricingGrid.jar` | 30 | unknown |
| `AA_PricingRules.jar` | 53 | unknown |
| `AA_ProductApi.jar` | 3 | public-api, unknown |
| `AA_ProductAttribute.jar` | 42 | unknown |
| `AA_ProductBundle.jar` | 40 | unknown |
| `AA_ProductCommission.jar` | 14 | unknown |
| `AA_ProductFramework.jar` | 117 | unknown |
| `AA_ProductImporter.jar` | 32 | unknown |
| `AA_ProductManagement.jar` | 125 | unknown |
| `AA_PromotionRules.jar` | 21 | unknown |
| `AA_PropertyApi.jar` | 4 | public-api, unknown |
| `AA_PropertyClassApi.jar` | 3 | public-api, unknown |
| `AA_PropertyControl.jar` | 12 | unknown |
| `AA_Quotation.jar` | 58 | unknown |
| `AA_Reporting.jar` | 59 | unknown |
| `AA_RestructureRules.jar` | 24 | unknown |
| `AA_RuleComparisonHook.jar` | 8 | public-api, unknown |
| `AA_Rules.jar` | 99 | unknown |
| `AA_SafeDepositBox.jar` | 12 | unknown |
| `AA_SeatInfra.jar` | 7 | unknown |
| `AA_Services.jar` | 31 | unknown |
| `AA_Settlement.jar` | 112 | unknown |
| `AA_SettlementHook.jar` | 3 | public-api, unknown |
| `AA_ShareTransfer.jar` | 15 | unknown |
| `AA_SplitsMerges.jar` | 27 | unknown |
| `AA_Statement.jar` | 26 | unknown |
| `AA_SubArrangementCondition.jar` | 12 | unknown |
| `AA_SubArrangementRules.jar` | 13 | unknown |
| `AA_SubLimits.jar` | 13 | unknown |
| `AA_Swift.jar` | 9 | unknown |
| `AA_Tax.jar` | 42 | unknown |
| `AA_TermAmount.jar` | 124 | unknown |
| `AA_TransactionRules.jar` | 5 | unknown |
| `AA_Util.jar` | 69 | unknown |
