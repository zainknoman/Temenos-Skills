# Cross-JAR Dependency Graph

> Manually curated 2026-06-20. Runtime dependency tracing is not derivable from JAR bytecode alone.
> This file documents the logical dependency layers and key JAR-to-JAR relationships.

---

## Dependency Principles

- **Core JARs** have no product dependencies — they provide framework interfaces only
- **Product JARs** depend on Core and optionally on sibling products
- **Integration JARs** (OFS, DE, REST) depend on product JARs they bridge
- **Custom L3 code** depends on product JARs via `$USING` declarations (jBC) or `import` (Java)
- **Country/localisation JARs** (prefix like `AR`, `CA`, `AU`) depend on the product JARs they extend

---

## Core Layer (no upstream T24 dependencies)

| JAR | Package | Role |
|-----|---------|------|
| `EB_API.jar` | `com.temenos.t24.api.hook.system` | RecordLifecycle, ServiceLifecycle, Enquiry interfaces |
| `AA_ActivityHook.jar` | `com.temenos.t24.api.hook.arrangement` | ActivityLifecycle interface |
| `com.temenos.api` (runtime) | `com.temenos.api` | TStructure, TField, TValidationResponse, TBoolean |
| `com.temenos.tafj.*` (runtime) | `com.temenos.tafj` | TAFJ runtime, jRunTime, jSession, jVar |
| TAFJ servlet (runtime) | — | HTTP routing for jBC REST components |

---

## Product Layer

### AA Framework Dependencies

```
AA_ActivityHook.jar   (interface — no product deps)
      ↑
AA_Framework.jar      (core AA framework classes)
      ↑
AA_ActivityAPI.jar    (ActivityAPI, ArrangementContext types)
      ↑
AA_ContractApi.jar    (Contract API)
      ↑
AA_BillApi.jar        (Bill — depends on ContractApi)
      ↑
AA_CalculationHook.jar (Calculation hook — depends on ActivityHook)
      ↑
AA_PaymentScheduleHook.jar  (payment schedule hooks)
      ↑
AA_PaymentRules.jar   (payment rule evaluation)
      ↑
AA_NoticeWithdrawal.jar  (notice withdrawal — depends on AA_Framework)
      ↑
AA_Closure.jar        (arrangement closure — depends on AA_Framework)
```

### Accounts (AC) Dependencies

```
EB_API.jar            (RecordLifecycle interface)
      ↑
AC_API.jar            (Account API — depends on EB_API)
      ↑
AC_PaymentNetting.jar (Payment netting — depends on AC_API)
      ↑
AC_PositionEntry.jar  (Position entry — depends on AC_API)
```

### Payments (FT/PP/PI) Dependencies

```
EB_API.jar
      ↑
FT_*.jar              (FUNDS.TRANSFER classes)
      ↑
PP_PaymentLifecycleHook.jar    (payment lifecycle hook)
PI_PaymentOrderHook.jar        (payment order hook)
PI_PaymentOrderLifecycleHook.jar (payment order lifecycle)
      ↑
TP_*.jar              (TPH payment order classes)
```

### Customer (ST) Dependencies

```
EB_API.jar
      ↑
ST_Customer.jar          (CustomerRecord — depends on EB_API)
ST_CustomerApi.jar       (Customer API classes)
      ↑
t24-ST_CustomerService-t24service.jar  (CustomerServiceAPI)
t24-ST_CustomerService-Data.jar        (Customer data DTOs)
```

---

## Integration Layer

### OFS Dependencies

OFS is jBC-based. The `OFS.GLOBUS.MANAGER` subroutine is part of the T24 jBC runtime and depends on:
- T24 session context (COMMON area)
- OFS.SOURCE configuration
- Target application's VERSION and validation routines

### DE (Document Engine) Dependencies

```
DE.EVENT.MAPPING   → triggered by T24 event framework
      ↓
ApplicationHandoff routine (jBC)   → depends on target application record
      ↓
DE.GET.* FUNCTION routines        → depend on business data applications
      ↓
DE.PRINT.INTERFACE             → depends on document delivery system
```

### REST API Dependencies

```
Transact REST Microservices (Spring Boot)
      → T24 Core via DataAccess / OFS
      → No direct JAR dependency on product JARs (service-oriented architecture)

jBC REST Components
      → TAFJ servlet (runtime)
      → jBC COMMON area / application file handles
```

---

## Full Dependency Matrix (Key Relationships)

| Dependent JAR / Component | Depends On |
|--------------------------|-----------|
| `AA_CalculationHook.jar` | `AA_ActivityHook.jar`, `com.temenos.api` |
| `AA_ContractApi.jar` | `AA_Framework.jar`, `AA_ActivityAPI.jar` |
| `AA_BillApi.jar` | `AA_ContractApi.jar`, `AA_Framework.jar` |
| `AA_NoticeWithdrawal.jar` | `AA_Framework.jar`, `AC_API.jar` |
| `PI_PaymentOrderLifecycleHook.jar` | `EB_API.jar`, `com.temenos.api` |
| `PP_PaymentLifecycleHook.jar` | `EB_API.jar`, `com.temenos.api` |
| `t24-ST_CustomerService-t24service.jar` | `ST_Customer.jar`, `EB_API.jar` |
| L3 Java hook class | Product JAR for its application (e.g. `AC_API.jar` for ACCOUNT hooks) |
| jBC `$USING AA.Framework` | TAFJ runtime — resolves to `AA_Framework.jar` |

---

## $USING to JAR Mapping (jBC → Java)

jBC `$USING` package declarations map to Java packages in product JARs:

| `$USING` Declaration | Java Package | Key JAR |
|---------------------|-------------|---------|
| `$USING AA.Framework` | `com.temenos.t24.api.arrangement` | `AA_Framework.jar` |
| `$USING AA.Interest` | `com.temenos.t24.api.arrangement.interest` | `AA_Interest.jar` |
| `$USING AA.Customer` | `com.temenos.t24.api.arrangement.customer` | `AA_Customer.jar` |
| `$USING AC.Fees` | `com.temenos.t24.api.account.fees` | `AC_Fees.jar` |
| `$USING EB.API` | `com.temenos.t24.api` | `EB_API.jar` |
| `$USING EB.SystemTables` | `com.temenos.t24.api.system` | `EB_SystemTables.jar` |
| `$USING ST.Customer` | `com.temenos.t24.api.customer` | `ST_Customer.jar` |

> For the complete `$USING` to package map, see [references/packages/package-index.md](../packages/package-index.md).

---

## Common Dependency Anti-Patterns

| Anti-Pattern | Problem | Correct Approach |
|-------------|---------|-----------------|
| L3 Java importing from TAFJ runtime directly | Breaks on upgrade | Use typed API classes from product JARs |
| jBC `$USING` a deprecated package | Silent failure in new T24 release | Verify package in current JAR set |
| Circular dependency between L3 JARs | Classloader failure | Structure L3 code so customisation JARs have no cross-dependencies |
| Hardcoding JAR version numbers | Version lock | Use T24 product JAR versions from the release |
