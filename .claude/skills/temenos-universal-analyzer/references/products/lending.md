# Lending — Reference

> Generated 2026-06-20T03:17:58.699072+00:00 from 22 JARs. Re-run `aggregate.py` to refresh.

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
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getVersion` | `java.lang.String` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getBuildDate` | `java.lang.String` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getContractType` | `com.temenos.t24.api.complex.ld.loansanddepositsapi.ContractType` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getInterestRate` | `com.temenos.t24.api.complex.ld.loansanddepositsapi.BasicInterestRate` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getInterestRate` | `com.temenos.t24.api.complex.ld.loansanddepositsapi.BasicInterestRate` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsApi.jar` | `getSchedule` | `java.util.List<com.temenos.t24.api.complex.ld.loansanddepositsapi.ScheduleEvent>` | Create a new LoansAndDeposits using a specific context.. |
| `LoansAndDeposits` | `LD_LoansAndDepositsHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to update an LD.LOANS.AND.DEPOSITS and its LD.SCHEDULE.DEFINE record from a service using the version and id specified in the transactionData parameter. |
| `LoansAndDeposits` | `LD_LoansAndDepositsHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to update an LD.LOANS.AND.DEPOSITS and its LD.SCHEDULE.DEFINE record from a service using the version and id specified in the transactionData parameter. |
| `LoansAndDeposits` | `LD_LoansAndDepositsHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to update an LD.LOANS.AND.DEPOSITS and its LD.SCHEDULE.DEFINE record from a service using the version and id specified in the transactionData parameter. |
| `LoansAndDeposits` | `LD_LoansAndDepositsHook.jar` | `updateLoanDepositRecordWithSchedule` | `void` | This interface enables the implementer to update an LD.LOANS.AND.DEPOSITS and its LD.SCHEDULE.DEFINE record from a service using the version and id specified in the transactionData parameter. |

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
| `LD_Accounting.jar` | 13 | unknown |
| `LD_Bills.jar` | 10 | unknown |
| `LD_Commitment.jar` | 32 | unknown |
| `LD_Config.jar` | 28 | unknown |
| `LD_Contract.jar` | 42 | unknown |
| `LD_Delivery.jar` | 21 | unknown |
| `LD_Fees.jar` | 5 | unknown |
| `LD_Foundation.jar` | 28 | unknown |
| `LD_Interest.jar` | 48 | unknown |
| `LD_LoansAndDepositsApi.jar` | 5 | public-api, unknown |
| `LD_LoansAndDepositsHook.jar` | 3 | public-api, unknown |
| `LD_ModelBank.jar` | 27 | unknown |
| `LD_Reports.jar` | 21 | unknown |
| `LD_Schedules.jar` | 41 | unknown |
| `LD_Versions.jar` | 2 | unknown |
| `LM_Config.jar` | 24 | unknown |
| `LM_Contract.jar` | 16 | unknown |
| `LM_Delivery.jar` | 7 | unknown |
| `LM_Fees.jar` | 5 | unknown |
| `LM_ModelBank.jar` | 7 | unknown |
| `LM_Schedules.jar` | 27 | unknown |
| `LM_Static.jar` | 2 | unknown |
