# TPH — Transaction Processing Hub Reference

## Contents
1. [Architecture Overview](#architecture-overview)
2. [Key Classes](#key-classes)
3. [Adapters](#adapters)
4. [Message Transformation](#message-transformation)
5. [Payment Order Lifecycle](#payment-order-lifecycle)
6. [Code Patterns](#code-patterns)

---

## Architecture Overview

TPH is Temenos's payment hub layer, sitting between originating channels and the core
payment engines (FT, AA Settlement, external rails). It provides routing, enrichment,
message transformation, and adapter management.

**Core application**: TP.PAYMENT.ORDER

---

## Key Classes

<!-- Populate from TPH_* JAR analysis -->

| Class | Package | JAR | Role |
|-------|---------|-----|------|
| (populate) | | | Payment order access |
| (populate) | | | Routing engine |
| (populate) | | | Adapter base class |
| (populate) | | | Message transformer |

---

## Adapters

**Adapter types**: (populate)

**Adapter registration**: (populate)

**Custom adapter pattern**: (populate)

---

## Message Transformation

**Input formats**: (populate)

**Output formats**: (populate)

**Transformation API**: (populate)

---

## Payment Order Lifecycle

| Stage | Hook Point | Class |
|-------|-----------|-------|
| Receive | (populate) | |
| Validate | (populate) | |
| Enrich | (populate) | |
| Route | (populate) | |
| Execute | (populate) | |
| Confirm | (populate) | |

---

## Code Patterns

### Custom adapter implementation

```java
// populate
```

### Payment order enrichment hook

```java
// populate
```
