# T24 Java API Catalog

> Generated 2026-06-20T03:39:43.046735+00:00 — 157 public API classes.

## `ActivityLifecycle`

**JAR:** `AA_ActivityHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `defaultFieldValues` | `void` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure` |
| `generateSecondaryActivity` | `void` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.complex.aa.activityhook.SecondaryActivity` |
| `postCoreTableUpdate` | `void` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, java.util.List<com.temenos.t24.api.complex.aa.activityhook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `validateRecord` | `com.temenos.api.TValidationResponse` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure` |
| `updateLookupTable` | `com.temenos.api.TBoolean` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, java.util.List<com.temenos.t24.api.complex.aa.activityhook.LookupData>` |
| `setElementData` | `void` | `java.lang.String, java.lang.String, java.util.List<java.lang.String>, java.util.List<com.temenos.api.TStructure>, java.util.List<com.temenos.api.TStructure>, com.temenos.t24.api.complex.aa.activityhook.ActivityContext, java.util.List<java.lang.String>, java.util.List<com.temenos.api.TStructure>, java.util.List<com.temenos.api.TStructure>` |
| `filterElements` | `java.util.List<java.lang.String>` | `java.util.List<java.lang.String>, java.lang.String, java.lang.String, java.lang.String` |
| `filterAccrualProperties` | `void` | `java.lang.String, com.temenos.t24.api.complex.aa.activityhook.AccrualContext, java.util.List<java.lang.String>, java.util.List<java.lang.String>` |

---
## `Bill`

**JAR:** `AA_BillApi.jar`  **Package:** `com.temenos.t24.api.arrangement`

Create a new Bill using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setContractId` | `void` | `java.lang.String` |
| `getContractId` | `java.lang.String` | `` |
| `setBillId` | `void` | `java.lang.String` |
| `getBillId` | `java.lang.String` | `` |
| `getBillRecord` | `com.temenos.t24.api.records.aabilldetails.AaBillDetailsRecord` | `` |

---
## `Calculation`

**JAR:** `AA_CalculationHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateSourceBalance` | `void` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, java.lang.String, com.temenos.api.TDate, com.temenos.api.TNumber, com.temenos.api.TDate, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord` |
| `calculatePayment` | `com.temenos.api.TNumber` | `java.lang.String, java.lang.String, com.temenos.t24.api.records.aaprddespaymentschedule.AaPrdDesPaymentScheduleRecord, com.temenos.api.TDate, java.lang.String, com.temenos.api.TDate, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord` |
| `calculateUncSettledAmount` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TNumber, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TDate, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord` |
| `calculateCharge` | `void` | `java.lang.String, com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord, com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TNumber, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord` |
| `calculateAdjustedCharge` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TDate, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord, com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TNumber, com.temenos.api.TString, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord` |
| `SortDrawingsArrangements` | `void` | `java.lang.String, com.temenos.api.TNumber, com.temenos.api.TString` |
| `getChargeAmount` | `com.temenos.api.TNumber` | `java.lang.String, com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord, com.temenos.api.TNumber, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.calculationhook.ChargeCalculationContext` |
| `getAdjustedChargeAmount` | `com.temenos.t24.api.complex.aa.calculationhook.ChargeAdjustment` | `com.temenos.api.TDate, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord, com.temenos.api.TNumber, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.calculationhook.ChargeCalculationContext` |
| `getDataElementValue` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, java.lang.String, java.lang.String, com.temenos.t24.api.records.evevidence.EvEvidenceRecord, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.calculationhook.DataElementContext` |
| `getBreakCostFeeInterestRates` | `com.temenos.t24.api.complex.aa.calculationhook.AdjustedInterest` | `com.temenos.t24.api.complex.aa.calculationhook.Arrangement, com.temenos.t24.api.complex.aa.calculationhook.Property, com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord, com.temenos.t24.api.complex.aa.calculationhook.Interest, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.records.aaarrangement.AaArrangementRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.calculationhook.BreakCostFeeContext` |
| `getInterestCustomRate` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TDate, java.lang.String, java.util.List<com.temenos.api.TDate>, com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord, java.lang.String, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.aa.activityhook.ArrangementContext, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.t24.api.complex.aa.calculationhook.InterestCustomRate` |

---
## `Contract`

**JAR:** `AA_ContractApi.jar`  **Package:** `com.temenos.t24.api.arrangement.accounting`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setContractId` | `void` | `java.lang.String` |
| `getContractId` | `java.lang.String` | `` |
| `getBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String` |
| `getBalanceMovementsForPeriod` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getForwardCreditBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getForwardDebitBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getAllBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getContractBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String` |
| `getContractBalanceMovementsForPeriod` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getContractForwardCreditBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getContractForwardDebitBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getAllContractBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getInterestAmounts` | `com.temenos.t24.api.complex.aa.contractapi.InterestAmount` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getTotalReceivedRepayment` | `com.temenos.api.TNumber` | `` |
| `getTotalReceivedRepaymentForProperty` | `com.temenos.api.TNumber` | `java.lang.String` |
| `getTotalReceivedRepaymentForPeriod` | `com.temenos.api.TNumber` | `com.temenos.api.TDate, com.temenos.api.TDate` |
| `getTotalReceivedRepaymentForMonth` | `com.temenos.api.TNumber` | `` |
| `getLastRepayment` | `com.temenos.t24.api.complex.aa.contractapi.Payment` | `java.lang.String` |
| `getNextPayment` | `com.temenos.t24.api.complex.aa.contractapi.Payment` | `java.lang.String` |
| `getAccountDetailsRecord` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord` | `` |
| `getInterestAccrualsRecord` | `com.temenos.t24.api.records.aainterestaccruals.AaInterestAccrualsRecord` | `java.lang.String, com.temenos.api.TDate` |
| `getBillIdsForPayMethod` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getBillIdsForDate` | `java.util.List<java.lang.String>` | `com.temenos.api.TDate` |
| `getBillIdsForPaymentDate` | `java.util.List<java.lang.String>` | `com.temenos.api.TDate, java.lang.String` |
| `getBillIdsForBillType` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getBillIdsForBillStatus` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getBillIdsForSettlementStatus` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getBillIdsForAgingStatus` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getBillIdsForNextAgeDate` | `java.util.List<java.lang.String>` | `com.temenos.api.TDate` |
| `getBillIdsForRepaymentReference` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getBillIds` | `java.util.List<java.lang.String>` | `com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TDate, java.lang.String` |
| `getContract` | `com.temenos.t24.api.records.aaarrangement.AaArrangementRecord` | `` |
| `getCustomerRole` | `com.temenos.t24.api.complex.aa.contractapi.CustomerRole` | `` |
| `getNextDueDate` | `com.temenos.api.TDate` | `` |
| `getFirstOverdueDate` | `com.temenos.api.TDate` | `` |
| `getLastOverDueDate` | `com.temenos.api.TDate` | `` |
| `getNumberOfOverDueBills` | `com.temenos.api.TNumber` | `` |
| `getMaturityDate` | `com.temenos.api.TDate` | `` |
| `getPropertyIds` | `java.util.List<java.lang.String>` | `` |
| `getPropertyIdsForPropertyClass` | `java.util.List<java.lang.String>` | `java.lang.String` |
| `getTerm` | `java.lang.String` | `` |
| `getTermAmount` | `com.temenos.api.TNumber` | `` |
| `getContractAgeStatus` | `java.lang.String` | `` |
| `getProductId` | `java.lang.String` | `` |
| `getProductIdForEffectiveDate` | `java.lang.String` | `com.temenos.api.TDate` |
| `getSimulationId` | `java.lang.String` | `` |
| `getAccountCondition` | `com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord` | `java.lang.String` |
| `getAccountConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord` | `java.lang.String, com.temenos.api.TDate` |
| `getCustomerCondition` | `com.temenos.t24.api.records.aaprddescustomer.AaPrdDesCustomerRecord` | `java.lang.String` |
| `getCustomerConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddescustomer.AaPrdDesCustomerRecord` | `java.lang.String, com.temenos.api.TDate` |
| `getInterestCondition` | `java.util.List<com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord>` | `java.lang.String` |
| `getInterestConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord>` | `java.lang.String, com.temenos.api.TDate` |
| `getLimitCondition` | `com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord` | `java.lang.String` |
| `getLimitConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord` | `java.lang.String, com.temenos.api.TDate` |
| `getOfficersCondition` | `com.temenos.t24.api.records.aaprddesofficers.AaPrdDesOfficersRecord` | `java.lang.String` |
| `getOfficersConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddesofficers.AaPrdDesOfficersRecord` | `java.lang.String, com.temenos.api.TDate` |
| `getCommitmentCondition` | `com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord` | `java.lang.String` |
| `getCommitmentConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord` | `java.lang.String, com.temenos.api.TDate` |
| `getChargeCondition` | `java.util.List<com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord>` | `java.lang.String` |
| `getChargeConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord>` | `java.lang.String, com.temenos.api.TDate` |
| `getRepaymentCondition` | `java.util.List<com.temenos.t24.api.records.aaprddespaymentrules.AaPrdDesPaymentRulesRecord>` | `java.lang.String` |
| `getRepaymentConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddespaymentrules.AaPrdDesPaymentRulesRecord>` | `java.lang.String, com.temenos.api.TDate` |
| `getConditionForProperty` | `com.temenos.api.TStructure` | `java.lang.String` |
| `getConditionForPropertyEffectiveDate` | `com.temenos.api.TStructure` | `java.lang.String, com.temenos.api.TDate` |
| `getSimulationConditionForProperty` | `com.temenos.api.TStructure` | `java.lang.String` |
| `getFirstVersionOfProperty` | `com.temenos.api.TStructure` | `java.lang.String, com.temenos.api.TDate` |
| `getPreviousDatedProperty` | `com.temenos.api.TStructure` | `java.lang.String` |
| `getPreviousProperty` | `com.temenos.api.TStructure` | `java.lang.String` |
| `buildPaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.PaymentSchedule>` | `com.temenos.api.TDate, com.temenos.api.TDate, com.temenos.api.TNumber, java.util.List<java.lang.String>` |
| `buildPaymentScheduleForProperty` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.PaymentSchedule>` | `com.temenos.api.TDate, com.temenos.api.TDate, com.temenos.api.TNumber, java.util.List<java.lang.String>, java.lang.String` |
| `getFutureRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | `com.temenos.api.TDate, com.temenos.api.TDate` |
| `getRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | `com.temenos.api.TDate, com.temenos.api.TDate` |
| `getContractBeneficialOwner` | `java.lang.String` | `` |
| `getOutstandingBalance` | `com.temenos.t24.api.complex.aa.contractapi.OutstandingBalances` | `` |
| `getEffectiveInterestRate` | `com.temenos.t24.api.complex.aa.contractapi.EffectiveInterestRate` | `java.lang.String, com.temenos.api.TDate` |
| `getEffectiveInterestRate` | `com.temenos.t24.api.complex.aa.contractapi.EffectiveInterestRate` | `java.lang.String, com.temenos.api.TDate, java.lang.String` |
| `getInterestProfitAmount` | `com.temenos.t24.api.complex.aa.contractapi.ProfitAmount` | `java.lang.String, com.temenos.api.TDate` |
| `getActualDate` | `com.temenos.t24.api.complex.aa.contractapi.DateConversion` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |
| `getFutureSimulationRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `getSimulationRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |

---
## `PaymentSchedule`

**JAR:** `AA_PaymentScheduleHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`

This interface enables the implementer to return exceptions if any after execution of the User defined logic routine.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getAvailableBalance` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString` |

---
## `Product`

**JAR:** `AA_ProductApi.jar`  **Package:** `com.temenos.t24.api.arrangement`

Create a new Product using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setProductId` | `void` | `java.lang.String` |
| `getProductId` | `java.lang.String` | `` |
| `getProduct` | `com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord` | `` |

---
## `Property`

**JAR:** `AA_PropertyApi.jar`  **Package:** `com.temenos.t24.api.arrangement`

Default constructor. Create an empty Property.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setPropertyId` | `void` | `java.lang.String` |
| `getPropertyId` | `java.lang.String` | `` |
| `getPropertyClassId` | `java.lang.String` | `` |
| `getPropertiesForProduct` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |

---
## `PropertyClass`

**JAR:** `AA_PropertyClassApi.jar`  **Package:** `com.temenos.t24.api.arrangement`

Create a new PropertyClass using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setPropertyClassId` | `void` | `java.lang.String` |
| `getPropertyClassId` | `java.lang.String` | `` |
| `getPropertyIdsForProduct` | `java.util.List<java.lang.String>` | `com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord` |

---
## `RuleComparison`

**JAR:** `AA_RuleComparisonHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`

This interface enables the implementer to compare arrangement values against default
value in the product property definition.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getComparableValues` | `void` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String, java.util.List<java.lang.String>, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TDate, java.lang.String, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TBoolean, com.temenos.api.TNumber, com.temenos.api.TNumber, com.temenos.api.TNumber` |
| `compareNegotiatedValue` | `void` | `com.temenos.api.TNumber, com.temenos.api.TNumber, com.temenos.api.TNumber, java.util.List<com.temenos.api.TNumber>, com.temenos.api.TBoolean` |
| `validateNegotiableField` | `void` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |
| `getRelatedArrangements` | `void` | `java.lang.String, com.temenos.api.TDate, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>` |
| `getDormancyException` | `com.temenos.t24.api.complex.aa.rulecomparisonhook.DormancyResponse` | `java.lang.String, com.temenos.api.TDate, java.lang.String, com.temenos.t24.api.records.aaprddesdormancy.AaPrdDesDormancyRecord, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.t24.api.complex.aa.rulecomparisonhook.DormancyContext` |
| `getComparableStringValues` | `void` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String, java.util.List<java.lang.String>, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord, com.temenos.api.TDate, java.lang.String, com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord, com.temenos.api.TBoolean, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString` |

---
## `Settlement`

**JAR:** `AA_SettlementHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`

This interface enables the implementer to return exceptions if any after execution of the User defined logic routine.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateUserRoutine` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TString` |

---
## `Account`

**JAR:** `AC_AccountApi.jar`  **Package:** `com.temenos.t24.api.party`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setAccountId` | `void` | `java.lang.String` |
| `getAccountId` | `java.lang.String` | `` |
| `getAvailableAmount` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `java.lang.String` |
| `isValidAccountClassForSector` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, java.lang.String` |
| `getOpenAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `` |
| `getOpenActualBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `` |
| `getOpenClearedBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `` |
| `getAccountOverdueDate` | `java.util.List<com.temenos.t24.api.complex.ac.accountapi.Overdue>` | `` |
| `getCapitalisationDate` | `com.temenos.api.TDate` | `java.lang.String, java.lang.String` |
| `getStatementNarrative` | `java.lang.String` | `java.lang.String, java.lang.String` |
| `isValidAccountId` | `com.temenos.api.TBoolean` | `` |
| `isValidInternalAccount` | `com.temenos.api.TBoolean` | `` |
| `getTurnoverCredit` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `java.lang.String, com.temenos.api.TDate` |
| `getTurnoverDebit` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `java.lang.String, com.temenos.api.TDate` |
| `getBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` | `java.lang.String, com.temenos.api.TDate` |
| `getEntries` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate` |
| `isValidNostroAccount` | `com.temenos.api.TBoolean` | `` |
| `isValidNostroAccount` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, com.temenos.api.TDate` |
| `getNostroAccount` | `com.temenos.t24.api.complex.ac.accountapi.NostroAccount` | `java.lang.String, com.temenos.api.TDate, java.lang.String` |
| `getNostroAccountForTransactionType` | `com.temenos.t24.api.complex.ac.accountapi.NostroAccount` | `java.lang.String, com.temenos.api.TDate, java.lang.String` |
| `lockContractBalancesRecord` | `com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord` | `` |
| `getContractBalancesRecord` | `com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord` | `` |
| `getContractBalancesRecord` | `com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord` | `com.temenos.api.TBoolean` |
| `getAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Balance` | `java.lang.String, com.temenos.api.TDate` |
| `getAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Balance` | `` |
| `getAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Balance` | `java.lang.String` |

---
## `AccountingEntry`

**JAR:** `AC_AccountHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This Interface enables the implementer for export accounting entries to local developement.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `raiseOverrides` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord` |
| `exportEntries` | `void` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord` |
| `setAccountId` | `void` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TString` |
| `setAlternateAccountId` | `java.lang.String` | `` |
| `getAlternateAccountId` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.complex.ac.accounthook.AlternateAccountContext` |
| `postUpdateRequest` | `void` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.ac.accounthook.AccountingContext, java.util.List<com.temenos.t24.api.complex.eb.servicehook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `generateStatementEntryEvent` | `void` | `com.temenos.api.TString, java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.ac.accounthook.AccountContext, java.util.List<com.temenos.t24.api.complex.ac.accounthook.NameValuePair>, com.temenos.api.TBoolean` |
| `getAccountingEntryLocalFieldValues` | `void` | `java.lang.String, java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, java.lang.String, com.temenos.t24.api.complex.ac.accounthook.AccountingContext, java.util.List<com.temenos.t24.api.complex.ac.accounthook.LocalFieldDetails>` |

---
## `Account`

**JAR:** `AC_AccountServiceHook.jar`  **Package:** `com.temenos.t24.api.hook.party`

This interface enables the implementer to get the payment currency for the account.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getPaymentCurrency` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.ac.accountservicehook.PaymentCurrencyContext` |

---
## `Category`

**JAR:** `AC_CategoryApi.jar`  **Package:** `com.temenos.t24.api.accounting`

Default constructor. Create an empty Category.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setCategoryId` | `void` | `java.lang.String` |
| `getProfitAndLossEntryIds` | `java.util.List<java.lang.String>` | `com.temenos.api.TDate, com.temenos.api.TDate` |

---
## `Charge`

**JAR:** `AC_ChargeApi.jar`  **Package:** `com.temenos.t24.api.account`

Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setAccrualEndDate` | `void` | `java.lang.String, com.temenos.api.TDate` |
| `setAccrualAmount` | `void` | `java.lang.String, com.temenos.api.TNumber` |

---
## `ClearingService`

**JAR:** `AC_ClearingServiceHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This interface is invoked from a service and enables the implementer to provide clearing entries which will be raised by the system.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `bookEntries` | `void` | `java.lang.String, com.temenos.t24.api.complex.ac.clearingservicehook.ClearingContext, java.lang.String, com.temenos.api.TString, com.temenos.t24.api.complex.ac.clearingservicehook.RequestDetail, java.util.List<com.temenos.t24.api.complex.ac.clearingservicehook.Entry>` |

---
## `StandingOrder`

**JAR:** `AC_ContractHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This Interface enables the implementer to check the status of a
Funds Transfer generated by a standing order during batch processing.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `checkStandingOrderFundsTransfer` | `void` | `java.lang.String, java.lang.String` |
| `modifyPaymentOrderRecord` | `com.temenos.t24.api.records.paymentorder.PaymentOrderRecord` | `com.temenos.t24.api.records.paymentorder.PaymentOrderRecord` |

---
## `Statement`

**JAR:** `AC_StatementHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `printStatement` | `void` | `com.temenos.api.TStructure` |
| `printAccountStatement` | `void` | `java.lang.String, com.temenos.t24.api.records.acstmthandoff.AcStmtHandoffRecord, java.lang.String` |
| `formatStatement` | `void` | `java.lang.String, com.temenos.t24.api.records.acstmthandoff.AcStmtHandoffRecord, com.temenos.t24.api.records.stmtprinted.StmtPrintedRecord` |
| `modifyDataRecord` | `java.util.List<com.temenos.t24.api.complex.ac.statementhook.ModifiedData>` | `java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.ac.statementhook.EntryLine, java.util.List<java.lang.String>, java.util.List<com.temenos.t24.api.complex.ac.statementhook.ProductDetail>, com.temenos.t24.api.records.account.AccountRecord, com.temenos.t24.api.records.accountstatement.AccountStatementRecord` |
| `modifyHandOffRecord` | `java.util.List<com.temenos.t24.api.complex.ac.statementhook.ModifiedHandoffData>` | `java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.ac.statementhook.EntryLine, java.util.List<java.lang.String>, java.util.List<com.temenos.t24.api.complex.ac.statementhook.ProductDetail>, com.temenos.t24.api.records.account.AccountRecord, com.temenos.t24.api.records.accountstatement.AccountStatementRecord` |
| `getExternalSepaId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.ac.statementhook.SepaContext` |
| `getNarrativeText` | `java.util.List<java.lang.String>` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.ac.statementhook.NarrativeContext` |

---
## `Clearing`

**JAR:** `ACHFRM_ClearingHouseHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.usa`

This interface enables the implementor to update information related to transactions in automated clearing house entries.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateEntry` | `com.temenos.t24.api.complex.achfrm.clearinghousehook.EntryData` | `com.temenos.t24.api.records.achentries.AchEntriesRecord, com.temenos.t24.api.complex.achfrm.clearinghousehook.EntryDataContext` |

---
## `SoftClassActivityLifecycle`

**JAR:** `AF_ApiClassHook.jar`  **Package:** `com.temenos.t24.api.hook.arrangement`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `defaultSoftClassFieldValues` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.aadefinitionmanager.AaDefinitionManagerRecord, com.temenos.api.TStructure, com.temenos.t24.api.complex.af.apiclasshook.ArrangementContext` |
| `validateSoftClassRecord` | `com.temenos.api.TValidationResponse` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.aadefinitionmanager.AaDefinitionManagerRecord, com.temenos.api.TStructure, com.temenos.t24.api.complex.af.apiclasshook.ArrangementContext` |
| `processSoftClass` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.aadefinitionmanager.AaDefinitionManagerRecord, com.temenos.api.TStructure, com.temenos.t24.api.complex.af.apiclasshook.ArrangementContext` |
| `processSoftClassActivity` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.records.aadefinitionmanager.AaDefinitionManagerRecord, com.temenos.api.TStructure, com.temenos.t24.api.complex.af.apiclasshook.ArrangementContext` |
| `postUpdateRequest` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.records.aadefinitionmanager.AaDefinitionManagerRecord, com.temenos.api.TStructure, com.temenos.t24.api.complex.af.apiclasshook.ArrangementContext, java.util.List<com.temenos.t24.api.complex.eb.servicehook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |

---
## `SoftClass`

**JAR:** `AF_SoftClassApi.jar`  **Package:** `com.temenos.t24.api.arrangement`

Default constructor. Create an empty SoftClass.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getSoftClassInstance` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TString` |

---
## `InterfaceProcessEngine`

**JAR:** `ALLFND_InterfaceProcessEngineHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.system`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `convertData` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.allfnd.interfaceprocessenginehook.EngineContext` |

---
## `AtmMessageLifecycle`

**JAR:** `ATMFRM_MessageHook.jar`  **Package:** `com.temenos.t24.api.hook.atm`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateRequestMessage` | `void` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.api.TString, com.temenos.t24.api.records.intrfmessage.IntrfMessageRecord, com.temenos.api.TString` |
| `modifyRequestMessage` | `void` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.api.TString, com.temenos.api.TStructure, com.temenos.api.TString` |
| `updateResponseMessage` | `void` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.t24.api.records.intrfmessage.IntrfMessageRecord, com.temenos.t24.api.records.intrfmapping.IntrfMappingRecord, com.temenos.api.TString` |
| `getMappingId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest` |
| `updateAccountNumber` | `void` | `com.temenos.t24.api.records.atmterminalacct.AtmTerminalAcctRecord, com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.api.TString` |
| `calculateCharge` | `void` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.api.TStructure, com.temenos.t24.api.records.atmtransaction.AtmTransactionRecord` |
| `getBalance` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, java.lang.String` |
| `getFieldValue` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, java.lang.String` |
| `updateOfsResponseMessage` | `java.lang.String` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, java.lang.String` |
| `getTransactionData` | `com.temenos.t24.api.complex.atmfrm.messagehook.TransactionData` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader` |
| `getDualTransactionId` | `java.lang.String` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader` |
| `updateRecord` | `void` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.api.TString, com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData, com.temenos.api.TStructure` |
| `getCharge` | `com.temenos.t24.api.complex.atmfrm.messagehook.Charge` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.t24.api.records.atmtransaction.AtmTransactionRecord` |
| `getAtmTransactionId` | `java.lang.String` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader` |
| `getReservationAmount` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext` |
| `getCompanyCode` | `java.lang.String` | `com.temenos.t24.api.complex.atmfrm.messagehook.AtmTransactionContext, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequest, com.temenos.t24.api.complex.atmfrm.messagehook.IsoRequestHeader, com.temenos.t24.api.records.intrfmapping.IntrfMappingRecord, java.lang.String` |

---
## `Charge`

**JAR:** `CG_ChargeApi.jar`  **Package:** `com.temenos.t24.api.rates`

Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateCharges` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | `com.temenos.t24.api.complex.cg.chargeapi.ChargeCode, com.temenos.t24.api.complex.cg.chargeapi.ChargeCustomer, com.temenos.t24.api.complex.cg.chargeapi.DealAmountAndCurrency, com.temenos.t24.api.complex.cg.chargeapi.CrossRate` |
| `calculateCharges` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | `com.temenos.t24.api.complex.cg.chargeapi.ChargeCode, com.temenos.t24.api.complex.cg.chargeapi.ChargeCustomer, com.temenos.t24.api.complex.cg.chargeapi.DealAmountAndCurrency, com.temenos.t24.api.complex.cg.chargeapi.CrossRate, com.temenos.t24.api.complex.cg.chargeapi.Condition` |
| `calculateCommission` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | `com.temenos.t24.api.complex.cg.chargeapi.ChargeCode, com.temenos.t24.api.complex.cg.chargeapi.ChargeCustomer, com.temenos.t24.api.complex.cg.chargeapi.DealAmountAndCurrency, com.temenos.t24.api.complex.cg.chargeapi.CrossRate` |
| `calculateCommission` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | `com.temenos.t24.api.complex.cg.chargeapi.ChargeCode, com.temenos.t24.api.complex.cg.chargeapi.ChargeCustomer, com.temenos.t24.api.complex.cg.chargeapi.DealAmountAndCurrency, com.temenos.t24.api.complex.cg.chargeapi.CrossRate, com.temenos.t24.api.complex.cg.chargeapi.Condition` |
| `calculateTax` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | `com.temenos.t24.api.complex.cg.chargeapi.ChargeCode, com.temenos.t24.api.complex.cg.chargeapi.ChargeCustomer, com.temenos.t24.api.complex.cg.chargeapi.DealAmountAndCurrency, com.temenos.t24.api.complex.cg.chargeapi.CrossRate` |
| `calculateTax` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | `com.temenos.t24.api.complex.cg.chargeapi.ChargeCode, com.temenos.t24.api.complex.cg.chargeapi.ChargeCustomer, com.temenos.t24.api.complex.cg.chargeapi.DealAmountAndCurrency, com.temenos.t24.api.complex.cg.chargeapi.CrossRate, com.temenos.t24.api.complex.cg.chargeapi.Condition` |
| `getCommissionCondition` | `com.temenos.t24.api.complex.cg.chargeapi.Condition` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `getFundsTransferCondition` | `com.temenos.t24.api.complex.cg.chargeapi.Condition` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.fundstransfer.FundsTransferRecord` |
| `getChargeCondition` | `com.temenos.t24.api.complex.cg.chargeapi.Condition` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure` |

---
## `LegalID`

**JAR:** `CMBASE_IdValidationHook.jar`  **Package:** `com.temenos.t24.api.hook.validate`

This interface component allows to attach a validation routine that validates the given LegalID

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateLegalID` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TString` |

---
## `XmlExtractService`

**JAR:** `CMBASE_InterfaceBatchExtractHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.system`

This interface enables the implementer to decide whether to process the current Id.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `processId` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.t24.api.complex.cmbase.interfacebatchextracthook.XmlExtractContext` |

---
## `Collateral`

**JAR:** `CO_CollateralHook.jar`  **Package:** `com.temenos.t24.api.hook.party`

This Interface enables the implementer to resequence the contracts provided in the limitTransactions parameter in the order in which the collateral is to be allocated.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getContractAllocationSequence` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, java.util.List<com.temenos.t24.api.complex.co.collateralhook.LimitTransaction>, com.temenos.t24.api.complex.co.collateralhook.CollateralContext` |

---
## `GeneralDataProtectionRegulation`

**JAR:** `CZ_FrameworkHook.jar`  **Package:** `com.temenos.t24.api.hook.party`

This interface enables the implementer to return the obfuscated version of a party's personal information to replace the original field value in the record to fulfil the customer data protection erasure process.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `isEligible` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.cz.frameworkhook.PartyEligibilityContext` |
| `getObfuscatedFieldValue` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.cz.frameworkhook.ObfuscationContext` |

---
## `DebitCollectionOrderHook`

**JAR:** `DB_DebitCollectionOrderHook.jar`  **Package:** `com.temenos.t24.api.hook`

This interface enables the implementer to validate debit collection Product record.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateRecord` | `void` | `java.lang.String, com.temenos.t24.api.records.dbdebitcollectionorder.DbDebitCollectionOrderRecord, com.temenos.api.TString` |

---
## `DirectDebit`

**JAR:** `DD_ContractHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This Interface enables the implementer to set the clearing reference for the direct debit.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setCreditorReference` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.dd.contracthook.DirectDebitContext` |
| `setClearingReference` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.dd.contracthook.DirectDebitContext, com.temenos.api.TString` |
| `setMandateId` | `java.lang.String` | `com.temenos.t24.api.complex.dd.contracthook.Mandate, com.temenos.t24.api.complex.dd.contracthook.DirectDebitContext, java.lang.String, com.temenos.t24.api.records.ddddi.DdDdiRecord, com.temenos.api.TBoolean` |

---
## `Delivery`

**JAR:** `DE_DeliveryApi.jar`  **Package:** `com.temenos.t24.api.system`

Default constructor. Create an empty Delivery.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `mapTagValuesToRecord` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, java.lang.String` |
| `validateBic` | `com.temenos.t24.api.complex.de.deliveryapi.ValidationResponse` | `java.lang.String` |
| `validateCustomerBic` | `com.temenos.t24.api.complex.de.deliveryapi.ValidationResponse` | `java.lang.String` |
| `validateCompanyBic` | `com.temenos.t24.api.complex.de.deliveryapi.ValidationResponse` | `java.lang.String` |
| `mapMessageRecordsToNameValuePairs` | `java.util.List<com.temenos.t24.api.complex.de.deliveryapi.NameValuePair>` | `java.util.List<com.temenos.api.TStructure>, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.t24.api.records.demapping.DeMappingRecord` |
| `getBankRmaStatus` | `com.temenos.t24.api.complex.de.deliveryapi.SwiftRmaStatus` | `java.lang.String, java.lang.String` |
| `getMessageRmaStatus` | `com.temenos.t24.api.complex.de.deliveryapi.SwiftRmaStatus` | `java.lang.String` |
| `getSwiftRmaStatus` | `com.temenos.t24.api.complex.de.deliveryapi.SwiftRmaStatus` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |

---
## `Delivery`

**JAR:** `DE_DeliveryHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to convert the given value to the required value for the message.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `translateAmountInSpecificLanguage` | `java.lang.String` | `com.temenos.api.TNumber, com.temenos.api.TNumber, com.temenos.api.TNumber` |
| `mapAdditionalDataToMessageType` | `java.util.List<com.temenos.t24.api.complex.de.deliveryhook.Field>` | `com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, java.lang.String, com.temenos.api.TStructure` |
| `processInwardMessage` | `void` | `com.temenos.t24.api.complex.de.deliveryhook.DeliveryDetail, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString` |
| `processOutwardMessage` | `void` | `java.lang.String, com.temenos.t24.api.complex.de.deliveryhook.DeliveryDetail, com.temenos.api.TString, com.temenos.api.TString` |
| `headerMatchesCondition` | `com.temenos.api.TBoolean` | `com.temenos.api.TStructure, com.temenos.t24.api.complex.de.deliveryhook.Condition, com.temenos.api.TStructure, com.temenos.t24.api.complex.de.deliveryhook.DispositionControlContext` |
| `convertOutwardValue` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.records.deoheader.DeOHeaderRecord, com.temenos.api.TNumber, com.temenos.t24.api.complex.de.deliveryhook.OutwardConversionContext` |
| `updateSwiftMessage` | `void` | `com.temenos.t24.api.records.deformatswift.DeFormatSwiftRecord, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.api.TString, com.temenos.api.TString, com.temenos.t24.api.complex.de.deliveryhook.SwiftUpdateContext` |
| `createRecords` | `void` | `com.temenos.t24.api.complex.de.deliveryhook.InwardContext, java.lang.String, com.temenos.t24.api.records.deiheader.DeIHeaderRecord, java.lang.String, java.lang.String, com.temenos.t24.api.records.demessage.DeMessageRecord, java.util.List<com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `getFieldValues` | `java.util.List<com.temenos.t24.api.complex.de.deliveryhook.FieldValue>` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.de.deliveryhook.FieldContext` |

---
## `DataExporter`

**JAR:** `DW_DataExportHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to filter records from the data extract by excluding them.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getIds` | `java.util.List<java.lang.String>` | `java.lang.String, com.temenos.t24.api.records.dwexport.DwExportRecord, com.temenos.t24.api.complex.dw.dataexporthook.SelectionContext, com.temenos.api.TString` |
| `getRows` | `java.util.List<com.temenos.t24.api.complex.dw.dataexporthook.Row>` | `java.lang.String, java.lang.String, com.temenos.t24.api.records.dwexport.DwExportRecord, com.temenos.t24.api.complex.dw.dataexporthook.ProcessContext, com.temenos.api.TBoolean, java.util.List<java.lang.String>` |
| `getCustomFields` | `java.util.List<com.temenos.t24.api.complex.dw.dataexporthook.Field>` | `java.lang.String, java.lang.String, com.temenos.t24.api.records.dwexport.DwExportRecord, com.temenos.t24.api.complex.dw.dataexporthook.TransformContext, java.util.List<java.lang.String>, com.temenos.t24.api.complex.dw.dataexporthook.Row, com.temenos.api.TBoolean, java.util.List<java.lang.String>` |
| `excludeId` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.dw.dataexporthook.FilterContext` |
| `transferDataExtract` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.t24.api.complex.dw.dataexporthook.TransferDataExtractContext` |
| `setCustomFields` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.dwexport.DwExportRecord, com.temenos.t24.api.records.dwexportapi.DwExportApiRecord, java.util.List<com.temenos.t24.api.complex.dw.dataexporthook.CustomField>, com.temenos.t24.api.complex.dw.dataexporthook.RealtimeProcessContext, java.util.List<com.temenos.t24.api.complex.dw.dataexporthook.CustomField>` |
| `getFilterCriteria` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.dw.dataexporthook.RealtimeFilterContext` |

---
## `ContractLifecycle`

**JAR:** `DX_ContractLifecycleHook.jar`  **Package:** `com.temenos.t24.api.hook.derivatives`

This interface enables the implementer to return a list of transaction details for close out processing by the system.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getTransactionDetails` | `java.util.List<com.temenos.t24.api.complex.dx.contractlifecyclehook.TransactionDetail>` | `java.lang.String, com.temenos.api.TBoolean, java.util.List<java.lang.String>, java.util.List<com.temenos.t24.api.records.dxtransaction.DxTransactionRecord>` |

---
## `Valuation`

**JAR:** `DX_ValuationHook.jar`  **Package:** `com.temenos.t24.api.hook.derivatives`

This interface enables the implementer to calculate the credit exposure values, based on the add-on rates.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateCreditExposureValues` | `com.temenos.t24.api.complex.dx.valuationhook.CreditExposure` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.complex.dx.valuationhook.CreditExposureParameters, com.temenos.t24.api.records.dxtransaction.DxTransactionRecord` |
| `calculateNetCost` | `void` | `java.lang.String, com.temenos.t24.api.complex.dx.valuationhook.NetCostParameters, com.temenos.t24.api.complex.dx.valuationhook.CurrencyAmount, com.temenos.api.TNumber` |
| `getRevaluationMarginDetails` | `com.temenos.api.TStructure` | `java.lang.String, com.temenos.api.TBoolean, java.lang.String, com.temenos.t24.api.complex.dx.valuationhook.RevaluationRequest, com.temenos.t24.api.complex.dx.valuationhook.RevaluationDetail` |

---
## `Archive`

**JAR:** `EB_ArchiveHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to archive records from local applications related
to the supplied contract returning the number of records that have been archived.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getDateComparator` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `getSkipDecision` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `getArchiveFilter` | `com.temenos.t24.api.complex.eb.archivehook.ArchiveFilter` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `archiveRelatedRecords` | `com.temenos.api.TNumber` | `com.temenos.t24.api.complex.eb.archivehook.ArchiveContract, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `loadArchiveFiles` | `void` | `com.temenos.t24.api.complex.eb.archivehook.ArchiveLoad, com.temenos.t24.api.records.archive.ArchiveRecord, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `selectArchiveRecords` | `void` | `com.temenos.t24.api.records.archive.ArchiveRecord, java.util.List<java.lang.String>, com.temenos.t24.api.complex.eb.archivehook.ArchiveSelect, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `processArchiveRecords` | `void` | `com.temenos.api.TString, com.temenos.t24.api.records.archive.ArchiveRecord, java.util.List<java.lang.String>, com.temenos.t24.api.complex.eb.archivehook.ArchiveProcess, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `getSelectedRecords` | `com.temenos.t24.api.complex.eb.archivehook.ArchiveSelect` | `com.temenos.t24.api.records.archive.ArchiveRecord, java.util.List<java.lang.String>, java.lang.String, com.temenos.t24.api.complex.eb.archivehook.ArchiveContext` |
| `getRelatedFiles` | `void` | `com.temenos.api.TStructure, com.temenos.t24.api.records.archive.ArchiveRecord, java.util.List<java.lang.String>, java.util.List<com.temenos.t24.api.complex.eb.archivehook.RelatedFiles>, com.temenos.t24.api.complex.eb.archivehook.ArchiveInformation` |

---
## `DataAccess`

**JAR:** `EB_DataAccessApi.jar`  **Package:** `com.temenos.t24.api.system`

Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getRecord` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String` |
| `getRecord` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |
| `getRecord` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean` |
| `getHistoryRecord` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String` |
| `getConcatValues` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String` |
| `selectRecords` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |
| `selectRecords` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean` |
| `updateLocalfields` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `getRequestResponse` | `com.temenos.t24.api.records.ofsrequestdetail.OfsRequestDetailRecord` | `java.lang.String, com.temenos.api.TBoolean` |
| `getFieldValue` | `com.temenos.t24.api.complex.eb.dataaccessapi.FieldValue` | `java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `setFieldValue` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.dataaccessapi.FieldValue` |
| `getCurrentDirectory` | `java.lang.String` | `` |

---
## `DataFormattingEngine`

**JAR:** `EB_DataFormattingEngineHook.jar`  **Package:** `com.temenos.t24.api.hook.system`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getSourceFileName` | `java.lang.String` | `` |
| `getCompanyCode` | `java.lang.String` | `java.lang.String` |
| `validateFile` | `void` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TString` |
| `validateSourceData` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, java.util.List<java.lang.String>` |
| `getHeader` | `java.lang.String` | `java.lang.String` |
| `getHeaderData` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.api.TString` |
| `getTrailerData` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.api.TString` |
| `getTrailer` | `java.lang.String` | `java.lang.String` |
| `convertFieldData` | `java.lang.String` | `java.lang.String, java.lang.String` |
| `updateFieldData` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String` |
| `processOutwardTransactionData` | `void` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |
| `processInwardTransactionResponse` | `void` | `com.temenos.t24.api.complex.eb.dataformattingenginehook.TransactionResponse, java.lang.String, java.lang.String, java.util.List<com.temenos.t24.api.complex.eb.servicehook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `performCustomOperations` | `void` | `java.lang.String` |
| `modifyOutboundRecord` | `void` | `com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.api.TStructure` |
| `modifyInboundMessage` | `void` | `com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.api.TString` |
| `updateOutboundData` | `void` | `com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.api.TString, com.temenos.api.TBoolean` |
| `getIds` | `java.util.List<java.lang.String>` | `com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext` |
| `modifyData` | `java.lang.String` | `java.lang.String, java.lang.String` |
| `getTransactionId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.t24.api.complex.eb.dataformattingenginehook.DelimitedData` |
| `getTargetFileName` | `java.lang.String` | `com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingInitialiseContext` |
| `publishMessage` | `void` | `java.lang.String, com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.api.TStructure` |
| `updateRecord` | `void` | `com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.dataformattingenginehook.DataFormattingContext, com.temenos.t24.api.complex.eb.dataformattingenginehook.DelimitedData, com.temenos.t24.api.complex.eb.servicehook.TransactionControl, java.util.List<com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData>, java.util.List<com.temenos.api.TStructure>` |

---
## `DataMapper`

**JAR:** `EB_DataMappingHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to convert the given value and return the converted value while mapping data from one record to another.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `convertFieldValue` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.eb.datamappinghook.ConversionContext` |

---
## `Date`

**JAR:** `EB_DateApi.jar`  **Package:** `com.temenos.t24.api.system`

Create a new Date using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getDayType` | `java.lang.String` | `com.temenos.api.TDate` |
| `getDayType` | `java.lang.String` | `com.temenos.api.TDate, java.lang.String` |
| `addWorkingDays` | `com.temenos.api.TDate` | `com.temenos.api.TDate, com.temenos.api.TNumber` |
| `addWorkingDays` | `com.temenos.api.TDate` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TNumber` |
| `getDates` | `com.temenos.t24.api.records.dates.DatesRecord` | `` |
| `addFrequency` | `java.lang.String` | `java.lang.String` |
| `addFrequency` | `java.lang.String` | `java.lang.String, com.temenos.api.TNumber` |
| `minusFrequency` | `java.lang.String` | `java.lang.String` |
| `getWorkingDayDifference` | `com.temenos.api.TNumber` | `com.temenos.api.TDate, com.temenos.api.TDate` |
| `getWorkingDayDifference` | `com.temenos.api.TNumber` | `com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String` |
| `gregorianToJulian` | `java.lang.String` | `com.temenos.api.TDate` |
| `julianToGregorian` | `com.temenos.api.TDate` | `java.lang.String` |
| `getRecurrenceText` | `java.lang.String` | `java.lang.String` |
| `getMonthDifference` | `com.temenos.api.TNumber` | `com.temenos.api.TDate, com.temenos.api.TDate` |
| `getHolidaySchedules` | `java.util.List<com.temenos.t24.api.complex.eb.dateapi.HolidaySchedule>` | `` |
| `getBranchHolidaySchedules` | `java.util.List<com.temenos.t24.api.complex.eb.dateapi.HolidaySchedule>` | `` |
| `getSystemDate` | `com.temenos.api.TDate` | `` |

---
## `Date`

**JAR:** `EB_DateHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to return the next frequency in the cycle for the given T24 frequency.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getNextFrequency` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.datehook.FrequencyContext` |

---
## `Encryption`

**JAR:** `EB_EncryptionHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `encryptFieldData` | `java.lang.String` | `java.lang.String` |
| `decryptFieldData` | `java.lang.String` | `java.lang.String` |
| `maskFieldData` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.complex.eb.encryptionhook.DecryptionApplicationContext` |
| `decryptEnquiryFieldData` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.eb.encryptionhook.DecryptionEnquiryContext, com.temenos.api.TString` |
| `decryptEnrichmentFieldData` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.eb.encryptionhook.DecryptionEnrichmentContext, com.temenos.api.TBoolean` |

---
## `Enquiry`

**JAR:** `EB_EnquiryHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to return the attribute class while processing enquiry.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setFilterCriteria` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |
| `setValue` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |
| `setValues` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |
| `setRecord` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |
| `setIds` | `java.util.List<java.lang.String>` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |
| `setDropdownFilterCriteria` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |
| `getAttributeClass` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext` |

---
## `MessageLifecycle`

**JAR:** `EB_MessageHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to perform their own processing after processing the incoming message.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `preProcess` | `void` | `com.temenos.t24.api.records.ofsrequestdetail.OfsRequestDetailRecord, com.temenos.t24.api.complex.eb.messagehook.MessageContext` |
| `postProcess` | `void` | `com.temenos.t24.api.records.ofsrequestdetail.OfsRequestDetailRecord, com.temenos.t24.api.complex.eb.messagehook.MessageContext` |

---
## `Record`

**JAR:** `EB_RecordApi.jar`  **Package:** `com.temenos.t24.api.system`

Default constructor. Create an empty Record.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getGroupName` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure` |

---
## `Security`

**JAR:** `EB_SecurityHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to return a specified attribute value to be used for external security processing.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getAttributeValue` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String` |
| `getAttributeValuePair` | `java.util.List<com.temenos.t24.api.complex.eb.securityhook.AttributeValuePair>` | `java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `isDataAccessRestricted` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.complex.eb.securityhook.SecurityContext` |
| `validateSignOn` | `com.temenos.t24.api.complex.eb.securityhook.SignOnResponse` | `java.lang.String, com.temenos.t24.api.records.ofssource.OfsSourceRecord, com.temenos.t24.api.complex.eb.securityhook.SignOnContext` |

---
## `ServiceLifecycle`

**JAR:** `EB_ServiceHook.jar`  **Package:** `com.temenos.t24.api.hook.system`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `initialise` | `void` | `com.temenos.t24.api.complex.eb.servicehook.ServiceData` |
| `getTableName` | `java.lang.String` | `com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.util.List<java.lang.String>` |
| `getTableCriteria` | `com.temenos.t24.api.complex.eb.servicehook.TableCriteria` | `com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.util.List<java.lang.String>` |
| `getIds` | `java.util.List<java.lang.String>` | `com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.util.List<java.lang.String>` |
| `process` | `void` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String` |
| `inputRecord` | `void` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String, com.temenos.api.TBoolean, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<com.temenos.api.TStructure>` |
| `processSingleThreaded` | `void` | `com.temenos.t24.api.complex.eb.servicehook.ServiceData` |
| `postUpdateRequest` | `void` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String, java.util.List<com.temenos.t24.api.complex.eb.servicehook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `updateRecord` | `void` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String, com.temenos.t24.api.complex.eb.servicehook.TransactionControl, java.util.List<com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `getServiceControlDetail` | `com.temenos.t24.api.complex.eb.servicehook.ServiceControl` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String` |
| `getSwiftRequests` | `java.util.List<com.temenos.t24.api.complex.eb.servicehook.SwiftRequest>` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String` |

---
## `Session`

**JAR:** `EB_SessionApi.jar`  **Package:** `com.temenos.t24.api.system`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `listCurrentVariables` | `java.util.List<com.temenos.t24.api.complex.eb.sessionapi.NameValuePair>` | `` |
| `getCurrentVariable` | `java.lang.String` | `java.lang.String` |
| `setCurrentVariable` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String` |
| `deleteCurrentVariable` | `com.temenos.api.TBoolean` | `java.lang.String` |
| `getCompanyId` | `java.lang.String` | `` |
| `getCompanyRecord` | `com.temenos.t24.api.records.company.CompanyRecord` | `` |
| `getLocalCountry` | `java.lang.String` | `` |
| `getLocalCurrency` | `java.lang.String` | `` |
| `getUserId` | `java.lang.String` | `` |
| `getUserRecord` | `com.temenos.t24.api.records.user.UserRecord` | `` |
| `getUserLanguage` | `com.temenos.api.TNumber` | `` |
| `getMainMenu` | `java.lang.String` | `` |
| `getOnlineStatus` | `java.lang.String` | `` |
| `isService` | `com.temenos.api.TBoolean` | `` |
| `isProductInstalled` | `com.temenos.api.TBoolean` | `java.lang.String` |
| `getUserDispoOfficer` | `java.lang.String` | `` |
| `getUserDispoRights` | `java.util.List<java.lang.String>` | `` |
| `getUserOverrideClass` | `java.util.List<java.lang.String>` | `` |
| `getUserRoles` | `java.util.List<com.temenos.t24.api.complex.eb.sessionapi.UserRole>` | `` |
| `publishMessage` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.api.TStructure, com.temenos.api.TString` |
| `publishMessage` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.api.TStructure, com.temenos.api.TString, com.temenos.api.TString` |
| `getSessionNumber` | `java.lang.String` | `` |
| `getSourceId` | `java.lang.String` | `` |
| `printLine` | `void` | `java.lang.String` |
| `setNextVersion` | `void` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean` |
| `setNextVersion` | `void` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TBoolean` |
| `getCachedRecord` | `com.temenos.api.TStructure` | `java.lang.String, java.lang.String` |
| `getCachedLookupValues` | `java.util.List<com.temenos.t24.api.complex.eb.sessionapi.LookupValue>` | `java.lang.String` |
| `clearLookupCache` | `void` | `` |
| `getExternalUserId` | `java.lang.String` | `` |
| `getClientConnection` | `com.temenos.t24.api.complex.eb.sessionapi.Connection` | `` |
| `addMessageToQueue` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, java.lang.String` |
| `addMessageToQueue` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List<com.temenos.t24.api.complex.eb.sessionapi.NameValuePair>` |
| `getUnauthorisedRecord` | `com.temenos.api.TStructure` | `` |

---
## `Session`

**JAR:** `EB_SessionHook.jar`  **Package:** `com.temenos.t24.api.hook.system`

This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `initialise` | `void` | `com.temenos.t24.api.complex.eb.sessionhook.SessionContext` |
| `loadRecord` | `void` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.eb.sessionhook.SessionContext` |
| `deriveLabelValue` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.sessionhook.LabelContext` |

---
## `RecordLifecycle`

**JAR:** `EB_TemplateHook.jar`  **Package:** `com.temenos.t24.api.hook.system`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `checkId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `validateRecord` | `com.temenos.api.TValidationResponse` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `updateLookupTable` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TBoolean, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `defaultFieldValues` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `defaultFieldValuesOnHotField` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.InputValue, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `formatDealSlip` | `java.lang.String` | `java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `validateField` | `com.temenos.api.TValidationResponse` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `updateCoreRecord` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, java.util.List<java.lang.String>, com.temenos.api.TBoolean, java.util.List<java.lang.String>, java.util.List<com.temenos.api.TStructure>, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `setOverrideComparisonValue` | `void` | `java.lang.String, java.util.List<java.lang.String>, com.temenos.api.TString, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `postUpdateRequest` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.util.List<com.temenos.t24.api.complex.eb.servicehook.TransactionData>, java.util.List<com.temenos.api.TStructure>, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `isOverrideAutoApprove` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext, com.temenos.t24.api.complex.eb.templatehook.ErrorText` |
| `getTransactionMessage` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `updateRecord` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext, java.util.List<com.temenos.t24.api.complex.eb.templatehook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `getServiceControlDetail` | `com.temenos.t24.api.complex.eb.servicehook.ServiceControl` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |
| `enableAutomaticAuthorisation` | `com.temenos.api.TBoolean` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext, com.temenos.t24.api.complex.eb.templatehook.AutomaticAuthorisationContext` |
| `getLookupRecordAmendments` | `java.util.List<com.temenos.t24.api.complex.eb.templatehook.LookupRecordAmendment>` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TStructure, com.temenos.t24.api.complex.eb.templatehook.TransactionContext` |

---
## `Collateral`

**JAR:** `FICOLL_CollateralHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.finland`

This interface enables the implementer to return the calculated depreciation amount.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getDepreciationAmount` | `com.temenos.api.TNumber` | `java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TNumber, com.temenos.t24.api.complex.ficoll.collateralhook.DepreciationContext` |

---
## `InwardEntry`

**JAR:** `FT_ClearingHook.jar`  **Package:** `com.temenos.t24.api.hook.clearing`

This interface enables the implementer to modify the local reference fields in the clearingRecord parameter.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `modifyLocalReferenceValues` | `void` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.ft.clearinghook.ClearingContext, com.temenos.t24.api.records.acinwardentry.AcInwardEntryRecord, com.temenos.api.TString` |
| `validateEntry` | `com.temenos.t24.api.complex.ft.clearinghook.ValidationResponse` | `com.temenos.api.TStructure, com.temenos.t24.api.records.acinwardentry.AcInwardEntryRecord, com.temenos.t24.api.complex.ft.clearinghook.ClearingContext` |

---
## `FundsTransfer`

**JAR:** `FT_ContractHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface enables the implementer to return the values which will be used to update the FT.TAPE.REFERENCE record by the FT.TAPES.RUN.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateFundsTransferTapeReference` | `com.temenos.t24.api.complex.ft.contracthook.FtTapeReferenceFields` | `java.lang.String` |

---
## `TransactionFee`

**JAR:** `HUTXNF_TransactionFeeHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.hungary`

This interface enables the implementer to return the customer's previous card number for the given card number, if the given card number is the first issued an empty string must be returned.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getPreviousCardNumber` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.hutxnf.transactionfeehook.CardNumberContext` |
| `processEligibleTransaction` | `void` | `java.lang.String, com.temenos.t24.api.records.hutxnflevytransaction.HutxnfLevyTransactionRecord, com.temenos.t24.api.complex.hutxnf.transactionfeehook.TransactionContext` |
| `isHungaryResident` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.t24.api.complex.hutxnf.transactionfeehook.ResidenceContext` |

---
## `InternationalAccountingStandards`

**JAR:** `IA_AccountingHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateContractBalance` | `void` | `java.lang.String, java.util.List<com.temenos.api.TNumber>, com.temenos.t24.api.records.iasapplicationparam.IasApplicationParamRecord, java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.iascontractbalances.IasContractBalancesRecord, java.lang.String, java.lang.String, com.temenos.api.TString, com.temenos.api.TString` |
| `getExpectedCreditLoss` | `com.temenos.t24.api.complex.ia.accountinghook.ExpectedCreditLoss` | `com.temenos.t24.api.complex.ia.accountinghook.Contract, java.util.List<com.temenos.api.TNumber>, com.temenos.api.TNumber, com.temenos.t24.api.records.ebcashflow.EbCashflowRecord, java.util.List<com.temenos.t24.api.complex.ia.accountinghook.CashFlow>` |
| `getCollateralDetails` | `com.temenos.t24.api.complex.ia.accountinghook.CollateralDetails` | `java.lang.String, com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord, com.temenos.t24.api.complex.ia.accountinghook.CollateralContext` |

---
## `IFRSValuation`

**JAR:** `IA_ValuationApi.jar`  **Package:** `com.temenos.t24.api.accounting`

Create a new IFRSValuation using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getEffectiveInterestRate` | `com.temenos.api.TNumber` | `java.util.List<com.temenos.t24.api.complex.ia.valuationapi.CashFlow>, com.temenos.t24.api.complex.ia.valuationapi.InterestBasisSource` |
| `getEffectiveInterestRate` | `com.temenos.api.TNumber` | `java.util.List<com.temenos.t24.api.complex.ia.valuationapi.CashFlow>, com.temenos.t24.api.complex.ia.valuationapi.InterestBasisSource, com.temenos.api.TNumber` |
| `getNetPresentValue` | `com.temenos.api.TNumber` | `java.util.List<com.temenos.t24.api.complex.ia.valuationapi.CashFlow>, com.temenos.t24.api.complex.ia.valuationapi.InterestBasisSource, com.temenos.api.TNumber, com.temenos.t24.api.complex.ia.valuationapi.Margin, com.temenos.api.TDate` |
| `getNetPresentValue` | `com.temenos.api.TNumber` | `java.util.List<com.temenos.t24.api.complex.ia.valuationapi.CashFlow>, com.temenos.t24.api.complex.ia.valuationapi.InterestBasisSource, com.temenos.api.TNumber, com.temenos.api.TDate` |
| `getNetPresentValue` | `com.temenos.api.TNumber` | `java.util.List<com.temenos.t24.api.complex.ia.valuationapi.CashFlow>, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.ia.valuationapi.Margin, java.lang.String, com.temenos.api.TDate` |
| `getNetPresentValue` | `com.temenos.api.TNumber` | `java.util.List<com.temenos.t24.api.complex.ia.valuationapi.CashFlow>, java.lang.String, java.lang.String, com.temenos.t24.api.complex.ia.valuationapi.Margin, java.lang.String, com.temenos.api.TDate` |

---
## `IntegrationFramework`

**JAR:** `IF_IntegrationFrameworkHook.jar`  **Package:** `com.temenos.t24.api.hook.integration`

This interface enables the implementer to return join Ids where the data from two related tables need to be fetched but does not have common key fields

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getJoinIds` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, java.util.List<java.lang.String>, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.complex.ifr.integrationframeworkhook.IntegrationContext` |

---
## `InitialPublicOffering`

**JAR:** `ILIPOA_InitialPublicOfferingHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.israel`

This Interface enables the implementer to calculate and return the allocation to be fulfilled for the security order against an Initial public offering.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getSecurityAllocation` | `com.temenos.t24.api.complex.ilipoa.initialpublicofferinghook.SecurityAllocation` | `java.lang.String, com.temenos.api.TNumber, com.temenos.api.TNumber, com.temenos.t24.api.complex.ilipoa.initialpublicofferinghook.AllocationContext` |

---
## `IBAN`

**JAR:** `IN_IbanSystemApi.jar`  **Package:** `com.temenos.t24.api.account`

Default constructor. Create an empty IBAN.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateIBAN` | `com.temenos.t24.api.complex.in.ibansystemapi.ResponseMessage` | `java.lang.String` |
| `getIbanInformation` | `com.temenos.t24.api.complex.in.ibansystemapi.IbanInformation` | `java.lang.String` |
| `getBic` | `java.lang.String` | `java.lang.String, com.temenos.api.TString` |

---
## `RegulatoryReporting`

**JAR:** `ITREGE_TransactionsAPI.jar`  **Package:** `com.temenos.t24.api.countrymodelbank.italy`

Create a new RegulatoryReporting using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `isTransactionEligibleForReporting` | `com.temenos.api.TBoolean` | `com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TDate, com.temenos.api.TBoolean` |

---
## `XmlStatementGenerator`

**JAR:** `IX_XmlStatementHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This Interface enables the implementer to return the values for each child tag defined in the xmlTagDefintionRecord.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getGroupTagValues` | `java.util.List<com.temenos.t24.api.complex.ix.xmlstatementhook.Tags>` | `java.lang.String, com.temenos.t24.api.records.xmltagdefinition.XmlTagDefinitionRecord, java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, java.lang.String, com.temenos.t24.api.complex.ix.xmlstatementhook.XmlStatementContext` |

---
## `LetterOfCredit`

**JAR:** `LC_LetterOfCreditHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

Deprecated.  No further information

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getDiscountRate` | `com.temenos.api.TNumber` | `java.lang.String, com.temenos.api.TDate, java.lang.String, com.temenos.t24.api.complex.lc.letterofcredithook.TransactionContext` |
| `calculateChargeAmount` | `com.temenos.t24.api.complex.lc.letterofcredithook.ChargeAmount` | `com.temenos.api.TNumber, com.temenos.t24.api.complex.lc.letterofcredithook.Amount, com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.lc.letterofcredithook.TransactionContext, java.util.List<com.temenos.t24.api.complex.lc.letterofcredithook.CalculationData>` |
| `getDiscrepancyText` | `java.lang.String` | `com.temenos.t24.api.records.letterofcredit.LetterOfCreditRecord, com.temenos.t24.api.records.drawings.DrawingsRecord, com.temenos.t24.api.complex.lc.letterofcredithook.TransactionContext` |
| `updateDocumentaryCreditRecords` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.t24.api.records.letterofcredit.LetterOfCreditRecord, com.temenos.t24.api.complex.lc.letterofcredithook.InwardMessageContext, java.util.List<com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData>, java.util.List<com.temenos.api.TStructure>` |

---
## `LoansAndDeposits`

**JAR:** `LD_LoansAndDepositsApi.jar`  **Package:** `com.temenos.t24.api.contract`

Create a new LoansAndDeposits using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getContractType` | `com.temenos.t24.api.complex.ld.loansanddepositsapi.ContractType` | `java.lang.String` |
| `getInterestRate` | `com.temenos.t24.api.complex.ld.loansanddepositsapi.BasicInterestRate` | `java.lang.String, java.lang.String, com.temenos.api.TDate` |
| `getInterestRate` | `com.temenos.t24.api.complex.ld.loansanddepositsapi.BasicInterestRate` | `java.lang.String, java.lang.String` |
| `getSchedule` | `java.util.List<com.temenos.t24.api.complex.ld.loansanddepositsapi.ScheduleEvent>` | `java.lang.String` |

---
## `LoansAndDeposits`

**JAR:** `LD_LoansAndDepositsHook.jar`  **Package:** `com.temenos.t24.api.hook.contracts`

This interface enables the implementer to update an LD.LOANS.AND.DEPOSITS and its LD.SCHEDULE.DEFINE record from a service using the version and id specified in the transactionData parameter.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateLoanDepositRecordWithSchedule` | `void` | `java.lang.String, com.temenos.t24.api.complex.eb.servicehook.ServiceData, java.lang.String, com.temenos.api.TString, com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData, com.temenos.t24.api.records.ldloansanddeposits.LdLoansAndDepositsRecord, com.temenos.t24.api.records.ldscheduledefine.LdScheduleDefineRecord` |

---
## `Insurance`

**JAR:** `LENINS_InsuranceHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.canada`

This interface enables the implementer to Calculate and return the lending insurance charge amount.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getCharge` | `com.temenos.api.TNumber` | `java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate, com.temenos.t24.api.complex.lenins.insurancehook.InsuranceContext` |

---
## `LoanRenewal`

**JAR:** `LENREN_LoanRenewalHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.canada`

This interface enables the implementer to determine whether automatic loan renewal is to be rejected.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `rejectRenewal` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.t24.api.complex.lenren.loanrenewalhook.RenewalContext` |

---
## `Limit`

**JAR:** `LI_LimitApi.jar`  **Package:** `com.temenos.t24.api.party`

Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setLimitId` | `void` | `java.lang.String` |
| `getCurrencyAmount` | `com.temenos.t24.api.complex.li.limitapi.LimitCurrencyAmount` | `com.temenos.api.TBoolean, com.temenos.api.TDate` |
| `getLiabilityReferences` | `java.util.List<com.temenos.t24.api.complex.li.limitapi.LiabilityReferences>` | `java.lang.String, java.lang.String` |
| `getLiabilities` | `java.util.List<com.temenos.t24.api.complex.li.limitapi.Liability>` | `java.util.List<com.temenos.t24.api.complex.li.limitapi.LiabilityReferences>` |

---
## `Guarantee`

**JAR:** `MD_MdDealHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface enables the implementer to define one or more records to be input using the specified records and transaction data.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateGuaranteeRecords` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.t24.api.records.mddeal.MdDealRecord, com.temenos.t24.api.complex.md.mddealhook.InwardMessageContext, java.util.List<com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData>, java.util.List<com.temenos.api.TStructure>` |

---
## `Loan`

**JAR:** `NOLEND_LoanApi.jar`  **Package:** `com.temenos.t24.api.countrymodelbank.norway`

Default constructor. Create an empty Loan.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getCharge` | `com.temenos.t24.api.complex.nolend.loanapi.Charge` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TNumber` |

---
## `Integrator`

**JAR:** `OC_IntegrationHook.jar`  **Package:** `com.temenos.t24.api.hook.contract.overthecounter`

This interface enables the implementor to generate and return a unique id.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getUniqueTransactionId` | `com.temenos.t24.api.complex.oc.integrationhook.UniqueId` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.oc.integrationhook.TransactionContext` |

---
## `Obligor`

**JAR:** `OX_ObligorHook.jar`  **Package:** `com.temenos.t24.api.hook.party`

This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getObligors` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.ox.obligorhook.ObligorContext` |
| `getReferenceObligor` | `java.lang.String` | `java.util.List<java.lang.String>, com.temenos.t24.api.complex.ox.obligorhook.ReferenceObligorContext` |
| `getObligorRiskClass` | `java.lang.String` | `java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.ox.obligorhook.ObligorRiskClassContext` |

---
## `PaymentOrderHook`

**JAR:** `PI_PaymentOrderHook.jar`  **Package:** `com.temenos.t24.api.hook`

Deprecated.  use PaymentOrderLifecycle.setProductId instead

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `isChargeApplied` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.api.TString` |
| `setPaymentOrderProduct` | `void` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.api.TString, com.temenos.api.TString` |
| `getPaymentOrderProductId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.api.TString` |
| `validateRecord` | `void` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.api.TString` |

---
## `PaymentOrderLifecycle`

**JAR:** `PI_PaymentOrderLifecycleHook.jar`  **Package:** `com.temenos.t24.api.hook.payments`

Create a new PaymentOrderLifecycle using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `handleValidationEvent` | `void` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.records.porsupplementaryinfo.PorSupplementaryInfoRecord, com.temenos.t24.api.records.poragreementandadvice.PorAgreementAndAdviceRecord, com.temenos.t24.api.records.porpostingandconfirmation.PorPostingAndConfirmationRecord, com.temenos.t24.api.records.poraudittrail.PorAuditTrailRecord, com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.TransactionContext` |
| `applyChargeType` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.PaymentOrderValidationContext` |
| `setProductId` | `void` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.PaymentOrderValidationContext, com.temenos.api.TString` |
| `validatePaymentOrderRecord` | `com.temenos.api.TValidationResponse` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.PaymentOrderValidationContext` |
| `getPaymentSystemType` | `com.temenos.t24.api.hook.payments.PaymentOrderLifecycle$PaymentSystemType` | `java.lang.String, java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.TransactionContext` |

---
## `Position`

**JAR:** `PM_PositionHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface is used to obtain the position class values and calculates interest rate and obtains notional currency.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getSecurityPosition` | `com.temenos.t24.api.complex.pm.positionhook.SecurityPosition` | `java.lang.String, com.temenos.t24.api.records.sctradingposition.ScTradingPositionRecord, com.temenos.t24.api.complex.pm.positionhook.PositionContext` |
| `getForexPosition` | `com.temenos.t24.api.complex.pm.positionhook.ForexPosition` | `java.lang.String, com.temenos.t24.api.complex.pm.positionhook.GapClass, com.temenos.t24.api.complex.pm.positionhook.PositionContext` |
| `getForwardRateAgreementPosition` | `com.temenos.t24.api.complex.pm.positionhook.ForwardRateAgreementPosition` | `com.temenos.t24.api.complex.pm.positionhook.PositionContext, com.temenos.t24.api.records.fradeal.FraDealRecord` |

---
## `AccountPool`

**JAR:** `PO_AccountPoolHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This interface enables the implemnter to provide a value for the CURRENT.BALANCE field in the AC.CASH.POOL table in T24.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateCurrentBalance` | `com.temenos.api.TNumber` | `com.temenos.api.TStructure, com.temenos.t24.api.complex.po.accountpoolhook.TransactionContext` |

---
## `BalanceCheckApiHook`

**JAR:** `PP_BalanceCheckApiHook.jar`  **Package:** `com.temenos.t24.api.hook`

Deprecated.  use PaymentLifecycle.getRequestType instead

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `recyclerLookup` | `void` | `com.temenos.t24.api.complex.pp.balancecheckapihook.TransactionInformation, java.util.List<com.temenos.t24.api.complex.pp.balancecheckapihook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.balancecheckapihook.DebitParty>, com.temenos.t24.api.complex.pp.balancecheckapihook.DebitAuthorityInformation, com.temenos.t24.api.complex.pp.balancecheckapihook.RecyclerInformation` |

---
## `ComponentApiHook`

**JAR:** `PP_ComponentApiHook.jar`  **Package:** `com.temenos.t24.api.hook`

Deprecated.  use PaymentLifecycle.updateProcessSequence instead

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getCreditAccount` | `com.temenos.t24.api.complex.pp.componentapihook.Account` | `com.temenos.t24.api.complex.pp.componentapihook.TransactionContext, com.temenos.t24.api.complex.pp.componentapihook.CreditParty` |
| `getDebitAccount` | `com.temenos.t24.api.complex.pp.componentapihook.DebitAccount` | `com.temenos.t24.api.complex.pp.componentapihook.TransactionContext, com.temenos.t24.api.complex.pp.componentapihook.DebitParty` |
| `validateCreditParty` | `com.temenos.t24.api.complex.pp.componentapihook.Response` | `com.temenos.t24.api.complex.pp.componentapihook.TransactionContext, com.temenos.t24.api.complex.pp.componentapihook.CreditParty` |
| `validateDebitParty` | `com.temenos.t24.api.complex.pp.componentapihook.Response` | `com.temenos.t24.api.complex.pp.componentapihook.TransactionContext, com.temenos.t24.api.complex.pp.componentapihook.DebitParty` |
| `getCodewordFlag` | `com.temenos.api.TBoolean` | `com.temenos.t24.api.complex.pp.componentapihook.TransactionContext, com.temenos.t24.api.complex.pp.componentapihook.InboundCodeWord, com.temenos.t24.api.complex.pp.componentapihook.ProcessRoutine, com.temenos.t24.api.complex.pp.componentapihook.ProcessSequence` |
| `setCalculatedDate` | `com.temenos.t24.api.complex.pp.componentapihook.CalculatedDates` | `com.temenos.t24.api.complex.pp.componentapihook.InDateDetails, com.temenos.t24.api.complex.pp.componentapihook.Channel, java.util.List<com.temenos.t24.api.complex.pp.componentapihook.DebitCondition>, java.util.List<com.temenos.t24.api.complex.pp.componentapihook.Credit>, java.util.List<com.temenos.t24.api.complex.pp.componentapihook.AccountInfo>` |

---
## `DataAccess`

**JAR:** `PP_DataAccessApi.jar`  **Package:** `com.temenos.t24.api.payments`

Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getPaymentRecord` | `com.temenos.t24.api.records.portransaction.PorTransactionRecord` | `java.lang.String` |
| `getActiveId` | `java.lang.String` | `java.lang.String, java.lang.String` |

---
## `FeeDeterminationHook`

**JAR:** `PP_FeeDeterminationHook.jar`  **Package:** `com.temenos.t24.api.hook`

Deprecated.  use PaymentLifecycle.getChargeResponse instead

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getChargeAmount` | `com.temenos.api.TNumber` | `com.temenos.t24.api.complex.pp.feedeterminationhook.PaymentDetails` |

---
## `MessageAcceptanceParamHook`

**JAR:** `PP_MessageAcceptanceParamHook.jar`  **Package:** `com.temenos.t24.api.hook`

This interface enables the implementer to validate the ACH messages.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateSwiftMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | `java.lang.String, com.temenos.t24.api.complex.pp.messageacceptanceparamhook.ReceivedFileDetails` |
| `ackNackMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | `java.lang.String, com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageAcceptanceParameter, com.temenos.t24.api.complex.pp.messageacceptanceparamhook.ReceivedFileDetails` |
| `messageForward` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TString` |
| `debulkMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.FileInformation` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.pp.messageacceptanceparamhook.ChannelInfo, com.temenos.api.TString, com.temenos.api.TString` |
| `validateBacsMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.BacsInfo, com.temenos.api.TString` |
| `validateAchMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | `java.lang.String, com.temenos.t24.api.complex.pp.messageacceptanceparamhook.ReceivedFileDetails` |
| `validateChequeClearingMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.ChequeClearing` |
| `validateClearingMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | `java.lang.String` |
| `ackClearingMessage` | `void` | `java.lang.String, com.temenos.api.TString` |

---
## `Message`

**JAR:** `PP_MessageHook.jar`  **Package:** `com.temenos.t24.api.hook.payments`

This interface enables the developer to update a field value for non-xml message to be mapped to a payment.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateInformationLine` | `void` | `java.util.List<com.temenos.t24.api.complex.pp.messagehook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.DebitParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.coverInformation>, com.temenos.t24.api.complex.pp.messagehook.DebitAuthorityInformation, com.temenos.t24.api.complex.pp.messagehook.HeaderInformation, com.temenos.t24.api.complex.pp.messagehook.RemittanceInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.HistoryLog>, com.temenos.t24.api.complex.pp.messagehook.DirectDebitInitiation, com.temenos.t24.api.complex.pp.messagehook.PaymentFlowInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.StatusInformation>, com.temenos.t24.api.complex.pp.messagehook.TransactionInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.InformationLineDetails>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.AdditionalInformationLineDetails>` |
| `updateFieldValue` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TBoolean, java.lang.String, com.temenos.t24.api.complex.pp.messagehook.MessageContext, com.temenos.api.TString` |
| `updatePaymentObject` | `void` | `com.temenos.t24.api.complex.pp.messagehook.paymentObjectContext, java.util.List<com.temenos.t24.api.complex.pp.messagehook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.DebitParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.coverInformation>, com.temenos.t24.api.complex.pp.messagehook.DebitAuthorityInformation, com.temenos.t24.api.complex.pp.messagehook.HeaderInformation, com.temenos.t24.api.complex.pp.messagehook.RemittanceInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.HistoryLog>, com.temenos.t24.api.complex.pp.messagehook.DirectDebitInitiation, com.temenos.t24.api.complex.pp.messagehook.PaymentFlowInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.StatusInformation>, com.temenos.t24.api.complex.pp.messagehook.TransactionInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.InformationLineDetails>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.AdditionalInformationLineDetails>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.LocalReference>` |
| `updateMessageStatus` | `com.temenos.t24.api.complex.pp.messagehook.ValidationResponse` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.pp.messagehook.MessageContext, com.temenos.t24.api.complex.pp.messagehook.MessageCriteria, com.temenos.t24.api.complex.pp.messagehook.MessageStatus` |

---
## `PaymentLifecycle`

**JAR:** `PP_PaymentLifecycleHook.jar`  **Package:** `com.temenos.t24.api.hook.payments`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateRequestToExternalCoreSystem` | `void` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.StatusAction, com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentContext, com.temenos.t24.api.records.porsupplementaryinfo.PorSupplementaryInfoRecord, com.temenos.t24.api.records.poragreementandadvice.PorAgreementAndAdviceRecord, com.temenos.t24.api.records.porpostingandconfirmation.PorPostingAndConfirmationRecord, com.temenos.t24.api.records.poraudittrail.PorAuditTrailRecord, com.temenos.t24.api.records.ppcompanyproperties.PpCompanyPropertiesRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CommonData, com.temenos.t24.api.records.ebqueriesanswers.EbQueriesAnswersRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Flags, com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentApplicationUpdate` |
| `getTransactionCode` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionCode` | `com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.records.porsupplementaryinfo.PorSupplementaryInfoRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentPostingContext` |
| `validatePaymentForClearing` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.ValidationResponse` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.InputChannel, java.util.List<com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitParty>, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ClearingContext` |
| `getAccountLocation` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountLocation` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountDetails, com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountLocationContext` |
| `getRoutingProductId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.pp.paymentlifecyclehook.RoutingProductContext` |
| `getExternalRequestFieldValue` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TBoolean, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ExternalRequestContext` |
| `updateProduct` | `void` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.RoutingProductContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Transaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Product` |
| `postRequestToExternalSystem` | `com.temenos.api.TBoolean` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.StatusAction, com.temenos.t24.api.records.ppcompanyproperties.PpCompanyPropertiesRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CommonData, com.temenos.t24.api.records.ebqueriesanswers.EbQueriesAnswersRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentContext, com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.records.porsupplementaryinfo.PorSupplementaryInfoRecord, com.temenos.t24.api.records.poragreementandadvice.PorAgreementAndAdviceRecord, com.temenos.t24.api.records.porpostingandconfirmation.PorPostingAndConfirmationRecord, com.temenos.t24.api.records.poraudittrail.PorAuditTrailRecord` |
| `postUpdateRequest` | `void` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.StatusAction, com.temenos.t24.api.records.ppcompanyproperties.PpCompanyPropertiesRecord, com.temenos.t24.api.records.ebqueriesanswers.EbQueriesAnswersRecord, com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.records.porsupplementaryinfo.PorSupplementaryInfoRecord, com.temenos.t24.api.records.poragreementandadvice.PorAgreementAndAdviceRecord, com.temenos.t24.api.records.porpostingandconfirmation.PorPostingAndConfirmationRecord, com.temenos.t24.api.records.poraudittrail.PorAuditTrailRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentContext, java.util.List<com.temenos.t24.api.complex.eb.servicehook.TransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `getChargeResponse` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.ChargeResponse` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.ChargeCriteria` |
| `getFileName` | `java.lang.String` | `com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.FileInformation` |
| `getCreditAccount` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Account` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditTransaction` |
| `getDebitAccount` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitAccount` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitTransaction` |
| `validateCreditParty` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Response` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditTransaction` |
| `validateDebitParty` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Response` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitTransaction` |
| `getPaymentDate` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentDate` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Transaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ChannelControl, java.util.List<com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitBankCondition>, java.util.List<com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentAccount>, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Payment, com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `updateProcessSequence` | `void` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.InboundCodeWord, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ProcessSequence, com.temenos.api.TBoolean` |
| `skipMessage` | `com.temenos.api.TBoolean` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Transaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Charge, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CurrencyExchangeInstruction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Payment, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditTransaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitTransaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `validatePayment` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Response` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `getSource` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.pp.paymentlifecyclehook.MappingContext` |
| `getSwiftSource` | `java.lang.String` | `java.util.List<com.temenos.t24.api.complex.pp.messagehook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.DebitParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.coverInformation>, com.temenos.t24.api.complex.pp.messagehook.DebitAuthorityInformation, com.temenos.t24.api.complex.pp.messagehook.HeaderInformation, com.temenos.t24.api.complex.pp.messagehook.RemittanceInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.HistoryLog>, com.temenos.t24.api.complex.pp.messagehook.DirectDebitInitiation, com.temenos.t24.api.complex.pp.messagehook.PaymentFlowInformation, com.temenos.t24.api.complex.pp.messagehook.StatusInformation, com.temenos.t24.api.complex.pp.messagehook.TransactionInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.InformationLineDetails>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.AdditionalInformationLineDetails>, com.temenos.t24.api.complex.pp.paymentlifecyclehook.MappingContext` |
| `getStatementNarrative` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `getRequestType` | `java.lang.String` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitTransaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.CreditTransaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Transaction, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ProcessSequence, com.temenos.t24.api.complex.pp.paymentlifecyclehook.Product, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ChannelControl, com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentDate, com.temenos.t24.api.complex.pp.paymentlifecyclehook.BatchPayment` |
| `getExternalRequestField` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Field` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure, com.temenos.api.TBoolean, com.temenos.t24.api.complex.pp.paymentlifecyclehook.ExternalRequestContext` |
| `getGroupingCriteria` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.GroupingCriteria` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentCriteria, com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `getCustomGroupingValues` | `java.util.List<java.lang.String>` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `getBulkPaymentReference` | `java.lang.String` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext` |
| `updateOutgoingPaymentRecords` | `void` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionContext, com.temenos.t24.api.records.portransaction.PorTransactionRecord, com.temenos.t24.api.records.porsupplementaryinfo.PorSupplementaryInfoRecord, com.temenos.t24.api.records.ebqueriesanswers.EbQueriesAnswersRecord, com.temenos.api.TBoolean, com.temenos.api.TBoolean, com.temenos.api.TString` |
| `getSwiftOriginatingSource` | `java.lang.String` | `java.util.List<com.temenos.t24.api.complex.pp.messagehook.CreditParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.DebitParty>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.coverInformation>, com.temenos.t24.api.complex.pp.messagehook.DebitAuthorityInformation, com.temenos.t24.api.complex.pp.messagehook.HeaderInformation, com.temenos.t24.api.complex.pp.messagehook.RemittanceInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.HistoryLog>, com.temenos.t24.api.complex.pp.messagehook.DirectDebitInitiation, com.temenos.t24.api.complex.pp.messagehook.PaymentFlowInformation, com.temenos.t24.api.complex.pp.messagehook.StatusInformation, com.temenos.t24.api.complex.pp.messagehook.TransactionInformation, java.util.List<com.temenos.t24.api.complex.pp.messagehook.InformationLineDetails>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.AdditionalInformationLineDetails>, java.util.List<com.temenos.t24.api.complex.pp.messagehook.LocalReference>, com.temenos.t24.api.complex.pp.paymentlifecyclehook.MappingContext` |
| `getPostingRestriction` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountRestrictions` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountDetails` |

---
## `PostingSchemeAPIHook`

**JAR:** `PP_PostingSchemeAPIHook.jar`  **Package:** `com.temenos.t24.api.hook`

Deprecated.  use PaymentLifecycle.getStatementNarrative instead

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getTextTokenValue` | `java.lang.String` | `java.lang.String` |

---
## `DebitOrderHook`

**JAR:** `PPADEB_DebitOrderHook.jar`  **Package:** `com.temenos.t24.api.hook`

This interface enables the implementer to validate payment order Product record.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateDebitOrder` | `void` | `java.lang.String, com.temenos.api.TString, com.temenos.api.TString` |
| `autoAcceptanceAPI` | `void` | `java.lang.String, com.temenos.api.TString, com.temenos.api.TString` |

---
## `Assessment`

**JAR:** `PV_ContractAssessmentHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This Interface enables the implementer to return Days Past Due(DPD) related details of the contract from external system.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getContractStatus` | `void` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.pv.contractassessmenthook.AssessmentContext, com.temenos.t24.api.complex.pv.contractassessmenthook.PastDue` |
| `getObligorStatus` | `void` | `java.lang.String, java.lang.String, com.temenos.t24.api.complex.pv.contractassessmenthook.AssessmentContext, com.temenos.t24.api.complex.pv.contractassessmenthook.PastDueCondition, java.util.List<com.temenos.t24.api.complex.pv.contractassessmenthook.Indicator>, com.temenos.t24.api.complex.pv.contractassessmenthook.Status` |

---
## `ProvisionManagement`

**JAR:** `PV_ProvisionManagementHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface enables the implementer to calculate and return the provision information for a contract.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getRiskClass` | `java.lang.String` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.RiskContext, java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `getRiskSegment` | `java.lang.String` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.RiskContext, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TStructure` |
| `getRiskCollateralValue` | `com.temenos.api.TNumber` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.RiskContext, java.lang.String, com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord, java.lang.String` |
| `getSegmentationProvision` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.SegmentationProvision` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.pv.provisionmanagementhook.SegmentContext` |
| `getProvision` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.Provision` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord, com.temenos.t24.api.records.pvprofile.PvProfileRecord, com.temenos.t24.api.complex.pv.provisionmanagementhook.ProvisionContext` |

---
## `Process`

**JAR:** `PW_ProcessHook.jar`  **Package:** `com.temenos.t24.api.hook.foundation`

This interface enables the implementer to return the evaluated condition for processing activity.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getActivity` | `java.lang.String` | `java.lang.String, java.lang.String, com.temenos.api.TStructure` |

---
## `TransactionRecycler`

**JAR:** `RC_ContractHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setTransactionCapture` | `void` | `com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.rc.contracthook.HandOffFormat, com.temenos.api.TBoolean` |
| `modifyRecyclingCaptureData` | `void` | `com.temenos.api.TStructure, java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate, com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord, com.temenos.t24.api.records.rcdetail.RcDetailRecord, com.temenos.api.TString` |
| `evaluateSettlement` | `com.temenos.t24.api.complex.rc.contracthook.SettlementResponse` | `java.lang.String, com.temenos.t24.api.complex.rc.contracthook.SettlementContext, com.temenos.t24.api.records.rcdetail.RcDetailRecord` |
| `processSettlement` | `com.temenos.t24.api.complex.rc.contracthook.SettlementResponse` | `java.lang.String, com.temenos.t24.api.complex.rc.contracthook.SettlementContext, com.temenos.t24.api.records.rcdetail.RcDetailRecord, com.temenos.t24.api.complex.rc.contracthook.SettlementTransactionControl, java.util.List<com.temenos.t24.api.complex.rc.contracthook.SettlementTransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `updateRecord` | `void` | `java.lang.String, com.temenos.t24.api.complex.rc.contracthook.SettlementContext, com.temenos.t24.api.records.rcdetail.RcDetailRecord, com.temenos.t24.api.complex.rc.contracthook.SettlementTransactionControl, java.util.List<com.temenos.t24.api.complex.rc.contracthook.SettlementTransactionData>, java.util.List<com.temenos.api.TStructure>` |
| `sortRetryRequests` | `void` | `java.util.List<java.lang.String>, java.util.List<com.temenos.t24.api.records.rcdetail.RcDetailRecord>, com.temenos.api.TString` |

---
## `Report`

**JAR:** `RE_AccountingReportApi.jar`  **Package:** `com.temenos.t24.api.accounting`

Create a new Report using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getAssetLiabilityReportLines` | `java.util.List<com.temenos.t24.api.complex.re.accountingreportapi.ReportLine>` | `java.lang.String, java.lang.String` |
| `getProfitLossReportLines` | `java.util.List<com.temenos.t24.api.complex.re.accountingreportapi.ReportLine>` | `java.lang.String, java.lang.String` |

---
## `Balance`

**JAR:** `RE_ContractBalanceApi.jar`  **Package:** `com.temenos.t24.api.contract`

Create a new Balance using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `get` | `com.temenos.t24.api.complex.re.contractbalanceapi.Balance` | `java.lang.String, com.temenos.api.TBoolean, java.lang.String, java.lang.String, com.temenos.api.TDate` |
| `get` | `com.temenos.t24.api.complex.re.contractbalanceapi.Balance` | `java.lang.String, java.lang.String` |
| `get` | `com.temenos.t24.api.complex.re.contractbalanceapi.Balance` | `java.lang.String, java.lang.String, com.temenos.api.TDate` |

---
## `RfRtpOrderHook`

**JAR:** `RF_RTPOrderHook.jar`  **Package:** `com.temenos.t24.api.hook`

This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateRecord` | `void` | `java.lang.String, com.temenos.t24.api.records.rfrtporder.RfRtpOrderRecord, com.temenos.api.TString` |
| `getResultOption` | `void` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, java.lang.String, com.temenos.api.TString, com.temenos.api.TString` |
| `mapPOAToRtp` | `void` | `java.lang.String, com.temenos.t24.api.records.paymentorder.PaymentOrderRecord, java.lang.String, com.temenos.api.TString` |

---
## `Earlyclosureapi`

**JAR:** `SAREGS_EarlyClosureAPI.jar`  **Package:** `com.temenos.t24.api`

Default constructor. Create an empty Earlyclosureapi.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateEarlyClosureChargesMurabaha` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, java.lang.String` |
| `calculateEarlyClosureChargesIjara` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, java.lang.String` |

---
## `IslamicLoan`

**JAR:** `SAREGS_IslamicLoanApi.jar`  **Package:** `com.temenos.t24.api.countrymodelbank.saudiarabia`

Create a new IslamicLoan using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculatePartialEarlyPayment` | `com.temenos.t24.api.complex.saregs.islamicloanapi.PartialPaymentResponse` | `com.temenos.api.TNumber, java.lang.String` |

---
## `Delivery`

**JAR:** `SC_DeliveryHook.jar`  **Package:** `com.temenos.t24.api.hook.securities`

This interface enables the implementer to define one or more records to be input using the specified transaction data.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateSecuritiesRecords` | `void` | `com.temenos.t24.api.complex.sc.deliveryhook.InwardContext, java.lang.String, java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.records.demessage.DeMessageRecord, java.util.List<com.temenos.t24.api.complex.eb.servicehook.SynchronousTransactionData>, java.util.List<com.temenos.api.TStructure>, com.temenos.api.TString` |

---
## `Security`

**JAR:** `SC_SecuritiesApi.jar`  **Package:** `com.temenos.t24.api.contract`

Create a new Security using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.sc.securitiesapi.CategoryDetail, com.temenos.api.TNumber, java.lang.String, java.lang.String` |
| `getMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.sc.securitiesapi.CategoryDetail, com.temenos.api.TNumber, java.lang.String` |
| `getMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | `java.lang.String, java.lang.String` |
| `getSecurityMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.sc.securitiesapi.MarginRates, com.temenos.api.TNumber, java.lang.String` |
| `getSecurityMarginValues` | `com.temenos.t24.api.complex.sc.securitiesapi.MarginValues` | `java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.complex.sc.securitiesapi.MarginRates, com.temenos.api.TNumber` |
| `map513MessageToExecuteSecurityOrdersRecord` | `void` | `java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.api.TString, com.temenos.api.TString, com.temenos.t24.api.records.scexesecorders.ScExeSecOrdersRecord` |
| `map515MessageToRecord` | `void` | `java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TStructure` |
| `map540ToSecurityTransferRecord` | `void` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, com.temenos.t24.api.records.demessage.DeMessageRecord, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString, com.temenos.api.TString, com.temenos.t24.api.records.securitytransfer.SecurityTransferRecord` |

---
## `Transaction`

**JAR:** `SC_TransactionHook.jar`  **Package:** `com.temenos.t24.api.hook.securities`

This interface allows the developer to allocate the executed nominal for a single security order in a bulk order group.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `allocateOrderNominals` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.records.secopenorder.SecOpenOrderRecord, com.temenos.t24.api.records.scexesecorders.ScExeSecOrdersRecord` |
| `isGroupSecurityOrder` | `com.temenos.api.TBoolean` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.records.secopenorder.SecOpenOrderRecord, com.temenos.t24.api.records.secopenorder.SecOpenOrderRecord` |

---
## `Valuation`

**JAR:** `SC_ValuationHook.jar`  **Package:** `com.temenos.t24.api.hook.securities`

This interface enables the implementer to calculate the stamp tax and EBV(Effectenboursenverein) fees amount during the tax calculation process, literally it is the deal amount passing during tax calculation etc.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateStampTaxAndEbvFees` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.complex.sc.valuationhook.SecurityValuationData, com.temenos.t24.api.complex.sc.valuationhook.UserContext, com.temenos.t24.api.complex.sc.valuationhook.TaxData, com.temenos.t24.api.complex.sc.valuationhook.StampTaxData, com.temenos.t24.api.complex.sc.valuationhook.EbvFeesData` |
| `setSecurityPortfolioAssetPositions` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.records.scposasset.ScPosAssetRecord` |
| `updatePortfolioAssetPositions` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.complex.sc.valuationhook.ValuationContext, com.temenos.t24.api.records.scposasset.ScPosAssetRecord` |
| `getSecurityPortfolioContracts` | `java.util.List<java.lang.String>` | `java.lang.String, com.temenos.api.TBoolean, java.lang.String` |
| `sortTransactionPositionHistory` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.records.sctransposhistory.ScTransPosHistoryRecord, com.temenos.t24.api.records.sctradingposition.ScTradingPositionRecord, com.temenos.t24.api.records.sctransposhistory.ScTransPosHistoryRecord` |
| `sortSecurityTradePosition` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.complex.sc.valuationhook.PositionAccuralContext, com.temenos.t24.api.records.sctradingposition.ScTradingPositionRecord, com.temenos.t24.api.records.sctransposhistory.ScTransPosHistoryRecord, com.temenos.t24.api.records.sctradingposition.ScTradingPositionRecord` |
| `setStructuredProductsAssetPositions` | `void` | `java.lang.String, com.temenos.api.TBoolean, com.temenos.t24.api.complex.sc.valuationhook.ValuationContext, com.temenos.t24.api.records.scposasset.ScPosAssetRecord` |

---
## `BIC`

**JAR:** `ST_BicApi.jar`  **Package:** `com.temenos.t24.api.party`

Create a new BIC using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getBicInformation` | `com.temenos.t24.api.complex.st.bicapi.BicInformation` | `java.lang.String` |

---
## `Calculation`

**JAR:** `ST_CalculationHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface enables the implementer to calculate the Base amount during the tax calculation process, literally it is the deal amount passing during charge calculation, tax splitting process etc.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `calculateBaseAmount` | `void` | `java.lang.String, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TStructure, com.temenos.api.TNumber` |
| `calculateTaxAmount` | `com.temenos.t24.api.complex.st.calculationhook.ChargeAmount` | `java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.tax.TaxRecord, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TStructure` |
| `getTaxAmount` | `com.temenos.t24.api.complex.st.calculationhook.ChargeAmount` | `java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.t24.api.records.tax.TaxRecord, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TStructure, com.temenos.t24.api.complex.st.calculationhook.TaxContext` |
| `calculateCharge` | `com.temenos.t24.api.complex.st.calculationhook.ChargeAmount` | `java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TStructure` |
| `calculateRate` | `void` | `java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TStructure, com.temenos.api.TNumber, com.temenos.api.TNumber` |
| `calculateSweepAmount` | `com.temenos.api.TNumber` | `com.temenos.t24.api.records.accashpoollink.AcCashPoolLinkRecord` |
| `calculateTwoWaySweepAmount` | `com.temenos.api.TNumber` | `com.temenos.t24.api.complex.st.calculationhook.CashPoolAccountBalance, com.temenos.t24.api.complex.st.calculationhook.CashPoolAccountBalance, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TDate` |
| `calculateEodSweepAmount` | `com.temenos.api.TNumber` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String` |
| `updatePrincipal` | `void` | `java.lang.String, com.temenos.t24.api.records.ebaccrualparam.EbAccrualParamRecord, java.lang.String, com.temenos.t24.api.complex.st.calculationhook.AccrualContext, java.util.List<com.temenos.t24.api.complex.st.calculationhook.Principal>` |
| `getAmortizationAmount` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, java.util.List<com.temenos.t24.api.complex.st.calculationhook.Accrual>, java.util.List<com.temenos.t24.api.complex.st.calculationhook.Interest>, com.temenos.t24.api.complex.st.calculationhook.CalculationCondition, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.t24.api.complex.st.calculationhook.AccrualPeriod, com.temenos.t24.api.complex.st.calculationhook.AmortizationContext` |

---
## `Currency`

**JAR:** `ST_CurrencyApi.jar`  **Package:** `com.temenos.t24.api.rates`

Create a new Currency using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setCurrencyId` | `void` | `java.lang.String` |
| `calculateExchangeRate` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, java.lang.String, com.temenos.api.TNumber` |
| `getRoundAmount` | `com.temenos.api.TNumber` | `com.temenos.api.TNumber, java.lang.String` |
| `calculateForwardBidValueRate` | `com.temenos.t24.api.complex.st.currencyapi.ForwardRate` | `com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TBoolean, com.temenos.api.TBoolean` |
| `calculateForwardMidValueRate` | `com.temenos.t24.api.complex.st.currencyapi.ForwardRate` | `com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TBoolean, com.temenos.api.TBoolean` |
| `calculateForwardOfferValueRate` | `com.temenos.t24.api.complex.st.currencyapi.ForwardRate` | `com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TDate, com.temenos.api.TBoolean, com.temenos.api.TBoolean` |
| `getCurrencyRates` | `java.util.List<com.temenos.t24.api.complex.st.currencyapi.CurrencyRate>` | `com.temenos.api.TDate` |
| `getForwardRate` | `com.temenos.t24.api.records.forwardrates.ForwardRatesRecord` | `com.temenos.api.TDate, java.lang.String` |
| `calculateRate` | `com.temenos.api.TNumber` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TDate` |
| `calculateBuyAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeAmount` | `java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate` |
| `calculateSellAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeAmount` | `java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate` |
| `calculateBuyExchangeRateAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeRateAmount` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TNumber` |
| `calculateSellExchangeRateAmount` | `com.temenos.t24.api.complex.st.currencyapi.ExchangeRateAmount` | `java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TNumber` |

---
## `Customer`

**JAR:** `ST_CustomerApi.jar`  **Package:** `com.temenos.t24.api.party`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setCustomerId` | `void` | `java.lang.String` |
| `customerExists` | `com.temenos.api.TBoolean` | `` |
| `getPersonalInfo` | `com.temenos.t24.api.complex.st.customerapi.PersonalInfo` | `` |
| `getProfile` | `com.temenos.t24.api.complex.st.customerapi.Profile` | `` |
| `getOfficer` | `com.temenos.t24.api.complex.st.customerapi.Officer` | `` |
| `getName` | `com.temenos.t24.api.complex.st.customerapi.Name` | `` |
| `getContactInfo` | `com.temenos.t24.api.complex.st.customerapi.ContactInfo` | `` |
| `getLanguage` | `java.lang.String` | `` |
| `getIdForMnemonic` | `java.lang.String` | `java.lang.String` |
| `getAccountNumbers` | `java.util.List<java.lang.String>` | `` |
| `getParentId` | `java.lang.String` | `` |
| `getRelationDetail` | `java.util.List<com.temenos.t24.api.complex.st.customerapi.Relationship>` | `` |
| `getPostingRestriction` | `com.temenos.t24.api.complex.st.customerapi.Restriction` | `` |
| `getMandateItems` | `java.util.List<com.temenos.t24.api.complex.st.customerapi.Mandates>` | `` |
| `getIdentificationDocuments` | `java.util.List<com.temenos.t24.api.complex.st.customerapi.Document>` | `` |
| `getSwiftAddress` | `com.temenos.t24.api.complex.st.customerapi.SwiftAddress` | `java.lang.String, com.temenos.api.TNumber, java.lang.String` |
| `getDeliverySecureMessageAddress` | `com.temenos.t24.api.complex.st.customerapi.SecureMessageAddress` | `java.lang.String, com.temenos.api.TNumber, java.lang.String` |
| `getEmailAddress` | `com.temenos.t24.api.complex.st.customerapi.EmailAddress` | `java.lang.String, com.temenos.api.TNumber, java.lang.String` |
| `getAgency` | `com.temenos.t24.api.complex.st.customerapi.Agency` | `` |
| `getLimit` | `com.temenos.t24.api.complex.st.customerapi.LimitAmount` | `java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TBoolean` |
| `getLiableLimit` | `com.temenos.t24.api.complex.st.customerapi.LimitAmount` | `java.lang.String, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TBoolean` |
| `getSettlementAccountId` | `com.temenos.t24.api.complex.st.customerapi.Settlement` | `java.lang.String, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TNumber, java.lang.String` |

---
## `CustomerPosition`

**JAR:** `ST_EnquiryHook.jar`  **Package:** `com.temenos.t24.api.hook.party`

This interface enables the implementer to return the list of contract id's which will be taken forward by CUSTOMER.POSITION enquiry.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getContractIds` | `java.util.List<com.temenos.t24.api.complex.st.enquiryhook.CustomerPositionId>` | `java.lang.String, java.lang.String` |
| `inputCustomerPositionRecord` | `void` | `com.temenos.t24.api.complex.st.enquiryhook.CustomerPositionId, java.lang.String, com.temenos.api.TBoolean, com.temenos.api.TNumber, com.temenos.t24.api.records.customerposition.CustomerPositionRecord` |

---
## `Interest`

**JAR:** `ST_InterestApi.jar`  **Package:** `com.temenos.t24.api.rates`

Default constructor. Create an empty Interest.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `setInterestId` | `void` | `java.lang.String` |
| `calculateAccrualDays` | `com.temenos.api.TNumber` | `com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String` |
| `getBasicRate` | `com.temenos.api.TNumber` | `java.lang.String, com.temenos.api.TDate` |
| `getTermRate` | `com.temenos.t24.api.complex.st.interestapi.TermRate` | `java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String` |
| `getTermMarginRate` | `com.temenos.t24.api.complex.st.interestapi.TermRate` | `java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String` |
| `getTermMisRate` | `com.temenos.t24.api.complex.st.interestapi.TermRate` | `java.lang.String, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate, com.temenos.api.TDate, java.lang.String` |
| `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.Period, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.util.List<com.temenos.t24.api.complex.st.interestapi.Spread>, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate` |
| `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.Period, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.util.List<com.temenos.t24.api.complex.st.interestapi.Spread>, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate` |
| `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.Period, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.util.List<com.temenos.t24.api.complex.st.interestapi.Spread>, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate` |
| `getRiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.RiskFreeRate` | `com.temenos.t24.api.complex.st.interestapi.Period, java.lang.String, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.lang.String, com.temenos.api.TNumber, java.lang.String, java.lang.String, com.temenos.api.TNumber, java.util.List<com.temenos.t24.api.complex.st.interestapi.Spread>, java.lang.String, com.temenos.api.TNumber, com.temenos.api.TDate` |

---
## `StatementEntry`

**JAR:** `ST_StatementHook.jar`  **Package:** `com.temenos.t24.api.hook.accounting`

This interface enables the implementer to return the transaction Id of the application.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getTransactionType` | `java.lang.String` | `com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.st.statementhook.StatementContext` |
| `getTransactionId` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.records.stmtentry.StmtEntryRecord, com.temenos.t24.api.complex.st.statementhook.StatementContext` |

---
## `Swap`

**JAR:** `SW_SwapHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface allows the implementer to calculate the forward rate used to calculate the cash flow amount for the swap Net Present Value details enquiry.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `getForwardRate` | `com.temenos.api.TNumber` | `com.temenos.t24.api.records.swapbalances.SwapBalancesRecord, com.temenos.t24.api.records.swaprevalparameter.SwapRevalParameterRecord, com.temenos.t24.api.records.swap.SwapRecord, com.temenos.t24.api.complex.sw.swaphook.TransactionContext` |

---
## `Message`

**JAR:** `SWFTAL_FoundationApi.jar`  **Package:** `com.temenos.t24.api.countrymodelbank.genericpackage.swiftalliance`

Create a new Message using a specific context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `formatHeader` | `void` | `java.lang.String, com.temenos.api.TString` |

---
## `DDAServiceAPI`

**JAR:** `t24-AC_DDAService-t24service.jar`  **Package:** `com.temenos.services.dda`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `DDAServiceProxyAPI`

**JAR:** `t24-AC_DDAService-t24service.jar`  **Package:** `com.temenos.services.dda`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `DfMappingServiceAPI`

**JAR:** `t24-DF_DfMappingService-t24service.jar`  **Package:** `com.temenos.services.dfmapping`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `DfMappingServiceProxyAPI`

**JAR:** `t24-DF_DfMappingService-t24service.jar`  **Package:** `com.temenos.services.dfmapping`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `DesignStudioInstallerServiceAPI`

**JAR:** `t24-DS_DesignStudioInstallerService-t24service.jar`  **Package:** `com.temenos.services.designstudioinstaller`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `DesignStudioInstallerServiceProxyAPI`

**JAR:** `t24-DS_DesignStudioInstallerService-t24service.jar`  **Package:** `com.temenos.services.designstudioinstaller`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `AuthenticationServiceAPI`

**JAR:** `t24-EB_AuthenticationService-t24service.jar`  **Package:** `com.temenos.services.authentication`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `AuthenticationServiceProxyAPI`

**JAR:** `t24-EB_AuthenticationService-t24service.jar`  **Package:** `com.temenos.services.authentication`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `AuthorizationServiceAPI`

**JAR:** `t24-EB_AuthorizationService-t24service.jar`  **Package:** `com.temenos.services.authorization`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `AuthorizationServiceProxyAPI`

**JAR:** `t24-EB_AuthorizationService-t24service.jar`  **Package:** `com.temenos.services.authorization`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `AutomationServiceAPI`

**JAR:** `t24-EB_AutomationService-t24service.jar`  **Package:** `com.temenos.services.automation`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `AutomationServiceProxyAPI`

**JAR:** `t24-EB_AutomationService-t24service.jar`  **Package:** `com.temenos.services.automation`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `CatalogServiceAPI`

**JAR:** `t24-EB_CatalogService-t24service.jar`  **Package:** `com.temenos.services.catalog`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `CatalogServiceProxyAPI`

**JAR:** `t24-EB_CatalogService-t24service.jar`  **Package:** `com.temenos.services.catalog`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `EntitlementServiceAPI`

**JAR:** `t24-EB_EntitlementService-t24service.jar`  **Package:** `com.temenos.services.entitlement`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `EntitlementServiceProxyAPI`

**JAR:** `t24-EB_EntitlementService-t24service.jar`  **Package:** `com.temenos.services.entitlement`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `OFSConnectorServiceAPI`

**JAR:** `t24-EB_OFSConnectorService-t24service.jar`  **Package:** `com.temenos.services.ofsconnector`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `OFSConnectorServiceProxyAPI`

**JAR:** `t24-EB_OFSConnectorService-t24service.jar`  **Package:** `com.temenos.services.ofsconnector`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `ResourceProviderServiceAPI`

**JAR:** `t24-EB_ResourceProviderService-t24service.jar`  **Package:** `com.temenos.services.resourceprovider`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `ResourceProviderServiceProxyAPI`

**JAR:** `t24-EB_ResourceProviderService-t24service.jar`  **Package:** `com.temenos.services.resourceprovider`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `SmsAPI`

**JAR:** `t24-EB_Sms-t24service.jar`  **Package:** `com.temenos.services.sms`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `SmsProxyAPI`

**JAR:** `t24-EB_Sms-t24service.jar`  **Package:** `com.temenos.services.sms`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `InboundSecurityServiceAPI`

**JAR:** `t24-IF_InboundSecurityService-t24service.jar`  **Package:** `com.temenos.services.inboundsecurity`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `InboundSecurityServiceProxyAPI`

**JAR:** `t24-IF_InboundSecurityService-t24service.jar`  **Package:** `com.temenos.services.inboundsecurity`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `InflowServiceAPI`

**JAR:** `t24-IF_InflowService-t24service.jar`  **Package:** `com.temenos.services.inflow`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `InflowServiceProxyAPI`

**JAR:** `t24-IF_InflowService-t24service.jar`  **Package:** `com.temenos.services.inflow`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `IntegrationFlowServiceAPI`

**JAR:** `t24-IF_IntegrationFlowService-t24service.jar`  **Package:** `com.temenos.services.integrationflow`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `IntegrationFlowServiceProxyAPI`

**JAR:** `t24-IF_IntegrationFlowService-t24service.jar`  **Package:** `com.temenos.services.integrationflow`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `IntegrationFrameworkServiceAPI`

**JAR:** `t24-IF_IntegrationFrameworkService-t24service.jar`  **Package:** `com.temenos.services.integrationframework`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `IntegrationFrameworkServiceProxyAPI`

**JAR:** `t24-IF_IntegrationFrameworkService-t24service.jar`  **Package:** `com.temenos.services.integrationframework`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `IntegrationLandscapeServiceAPI`

**JAR:** `t24-IF_IntegrationLandscapeService-t24service.jar`  **Package:** `com.temenos.services.integrationlandscape`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `IntegrationLandscapeServiceProxyAPI`

**JAR:** `t24-IF_IntegrationLandscapeService-t24service.jar`  **Package:** `com.temenos.services.integrationlandscape`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `TraFixServiceAPI`

**JAR:** `t24-PP_TraFixService-t24service.jar`  **Package:** `com.temenos.services.trafix`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `TraFixServiceProxyAPI`

**JAR:** `t24-PP_TraFixService-t24service.jar`  **Package:** `com.temenos.services.trafix`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `HumanTaskServiceAPI`

**JAR:** `t24-PW_HumanTaskService-t24service.jar`  **Package:** `com.temenos.services.humantask`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `HumanTaskServiceProxyAPI`

**JAR:** `t24-PW_HumanTaskService-t24service.jar`  **Package:** `com.temenos.services.humantask`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `ProcessEngineServiceAPI`

**JAR:** `t24-PW_ProcessEngineService-t24service.jar`  **Package:** `com.temenos.services.processengine`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `ProcessEngineServiceProxyAPI`

**JAR:** `t24-PW_ProcessEngineService-t24service.jar`  **Package:** `com.temenos.services.processengine`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `ReplicationServiceAPI`

**JAR:** `t24-RR_ReplicationService-t24service.jar`  **Package:** `com.temenos.services.replication`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `ReplicationServiceProxyAPI`

**JAR:** `t24-RR_ReplicationService-t24service.jar`  **Package:** `com.temenos.services.replication`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `CustomerServiceAPI`

**JAR:** `t24-ST_CustomerService-t24service.jar`  **Package:** `com.temenos.services.customer`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getMetaData` | `java.lang.String` | `` |
| `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` | `` |
| `setServiceHandler` | `void` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |
| `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` | `` |
| `setUserContextCallBack` | `void` | `com.temenos.soa.services.UserContextCallBack` |
| `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` | `` |
| `tidyUp` | `void` | `` |
| `cleanup` | `void` | `` |

---
## `CustomerServiceProxyAPI`

**JAR:** `t24-ST_CustomerService-t24service.jar`  **Package:** `com.temenos.services.customer`



| Method | Returns | Parameters |
|--------|---------|------------|
| `setSecurityContext` | `void` | `com.temenos.soa.services.UserContextCallBack` |

---
## `Table_IF_FLOW_API`

**JAR:** `Tables.jar`  **Package:** `com.temenos.t24`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getFields` | `java.lang.String` | `` |
| `getTableName` | `java.lang.String` | `` |

---
## `Table_EB_API`

**JAR:** `Tables.jar`  **Package:** `com.temenos.t24`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getFields` | `java.lang.String` | `` |
| `getTableName` | `java.lang.String` | `` |

---
## `Table_DW_EXPORT_API`

**JAR:** `Tables.jar`  **Package:** `com.temenos.t24`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getFields` | `java.lang.String` | `` |
| `getTableName` | `java.lang.String` | `` |

---
## `Table_CMBASE_TAX_EXEMPTION_API`

**JAR:** `Tables.jar`  **Package:** `com.temenos.t24`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getFields` | `java.lang.String` | `` |
| `getTableName` | `java.lang.String` | `` |

---
## `Table_ARACCT_FX_PAYMENT_CANCEL_API`

**JAR:** `Tables.jar`  **Package:** `com.temenos.t24`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getFields` | `java.lang.String` | `` |
| `getTableName` | `java.lang.String` | `` |

---
## `Table_AA_PRD_DES_ACTIVITY_API`

**JAR:** `Tables.jar`  **Package:** `com.temenos.t24`



| Method | Returns | Parameters |
|--------|---------|------------|
| `getFields` | `java.lang.String` | `` |
| `getTableName` | `java.lang.String` | `` |

---
## `Tax`

**JAR:** `TAXGST_TaxRegulatoryApi.jar`  **Package:** `com.temenos.t24.api.countrymodelbank.regulatory`

Default constructor. Create an empty Tax.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `updateTaxRefund` | `com.temenos.t24.api.complex.taxgst.taxregulatoryapi.UpdateResponse` | `java.lang.String, com.temenos.t24.api.complex.taxgst.taxregulatoryapi.TaxDetails` |
| `updateGoodsAndServicesTaxRecord` | `com.temenos.t24.api.complex.taxgst.taxregulatoryapi.UpdateResponse` | `java.lang.String, com.temenos.t24.api.records.taxreggstdetails.TaxregGstDetailsRecord` |

---
## `TaxEngine`

**JAR:** `TX_TaxEngineHook.jar`  **Package:** `com.temenos.t24.api.hook.contract`

This interface enables the implementer to return a converted field value for the transaction report.

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `convertReportFieldValue` | `java.lang.String` | `java.lang.String, com.temenos.api.TStructure, java.lang.String, java.lang.String, com.temenos.t24.api.complex.tx.taxenginehook.ReportContext` |

---
## `Fedwire`

**JAR:** `USRTGS_FedwireHook.jar`  **Package:** `com.temenos.t24.api.hook.countrymodelbank.usa`

Default constructor. Create an empty Fedwire.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context..

| Method | Returns | Parameters |
|--------|---------|------------|
| `getVersion` | `java.lang.String` | `` |
| `getBuildDate` | `java.lang.String` | `` |
| `getComponentVersion` | `java.lang.String` | `` |
| `validateAccountNumber` | `java.lang.String` | `java.lang.String, com.temenos.t24.api.complex.usrtgs.fedwirehook.FedwireContext` |
| `getOutwardFileName` | `java.lang.String` | `com.temenos.t24.api.complex.usrtgs.fedwirehook.FedwireOutwardFileContext` |
| `getScreeningStatus` | `com.temenos.t24.api.hook.countrymodelbank.usa.Fedwire$ScreeningStatus` | `java.lang.String, com.temenos.t24.api.records.fedwirenvmessage.FedwireNvMessageRecord, com.temenos.t24.api.complex.usrtgs.fedwirehook.FedwireScreeningContext` |

---
