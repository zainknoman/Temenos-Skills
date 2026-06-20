# Data Exchange (DX) — Reference

> Generated 2026-06-20T03:39:43.046735+00:00 from 36 JARs. Re-run `aggregate.py` to refresh.

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
| `ContractLifecycle` | `DX_ContractLifecycleHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return a list of transaction details for close out processing by the system. |
| `ContractLifecycle` | `DX_ContractLifecycleHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return a list of transaction details for close out processing by the system. |
| `ContractLifecycle` | `DX_ContractLifecycleHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return a list of transaction details for close out processing by the system. |
| `ContractLifecycle` | `DX_ContractLifecycleHook.jar` | `getTransactionDetails` | `java.util.List<com.temenos.t24.api.complex.dx.contractlifecyclehook.TransactionDetail>` | This interface enables the implementer to return a list of transaction details for close out processing by the system. |
| `Valuation` | `DX_ValuationHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to calculate the credit exposure values, based on the add-on rates. |
| `Valuation` | `DX_ValuationHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to calculate the credit exposure values, based on the add-on rates. |
| `Valuation` | `DX_ValuationHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to calculate the credit exposure values, based on the add-on rates. |
| `Valuation` | `DX_ValuationHook.jar` | `calculateCreditExposureValues` | `com.temenos.t24.api.complex.dx.valuationhook.CreditExposure` | This interface enables the implementer to calculate the credit exposure values, based on the add-on rates. |
| `Valuation` | `DX_ValuationHook.jar` | `calculateNetCost` | `void` | This interface enables the implementer to calculate the credit exposure values, based on the add-on rates. |
| `Valuation` | `DX_ValuationHook.jar` | `getRevaluationMarginDetails` | `com.temenos.api.TStructure` | This interface enables the implementer to calculate the credit exposure values, based on the add-on rates. |

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
| `DX_Accounting.jar` | 49 | unknown |
| `DX_Archiving.jar` | 8 | unknown |
| `DX_Closeout.jar` | 60 | unknown |
| `DX_CloseoutAssign.jar` | 28 | unknown |
| `DX_CloseoutExercise.jar` | 26 | unknown |
| `DX_CloseoutExpiry.jar` | 38 | unknown |
| `DX_CloseoutFixing.jar` | 7 | unknown |
| `DX_CloseoutMaturity.jar` | 13 | unknown |
| `DX_CloseoutSettlement.jar` | 32 | unknown |
| `DX_COB.jar` | 55 | unknown |
| `DX_Configuration.jar` | 71 | unknown |
| `DX_Constraints.jar` | 9 | unknown |
| `DX_ContractLifecycleHook.jar` | 3 | public-api, unknown |
| `DX_CorporateActions.jar` | 20 | unknown |
| `DX_Customer.jar` | 10 | unknown |
| `DX_EuroConversion.jar` | 5 | unknown |
| `DX_Exotics.jar` | 15 | unknown |
| `DX_Fees.jar` | 13 | unknown |
| `DX_Foundation.jar` | 141 | unknown |
| `DX_Margining.jar` | 57 | unknown |
| `DX_ModelBank.jar` | 28 | unknown |
| `DX_OptStructContract.jar` | 18 | unknown |
| `DX_OptStructUnit.jar` | 9 | unknown |
| `DX_Order.jar` | 54 | unknown |
| `DX_OrderService.jar` | 8 | unknown |
| `DX_Portfolio.jar` | 5 | unknown |
| `DX_Position.jar` | 80 | unknown |
| `DX_PositionManagement.jar` | 7 | unknown |
| `DX_Pricing.jar` | 93 | unknown |
| `DX_PricingTheoretical.jar` | 15 | unknown |
| `DX_Reports.jar` | 13 | unknown |
| `DX_Revaluation.jar` | 59 | unknown |
| `DX_Trade.jar` | 124 | unknown |
| `DX_Transfer.jar` | 11 | unknown |
| `DX_Valuation.jar` | 20 | unknown |
| `DX_ValuationHook.jar` | 5 | public-api, unknown |
