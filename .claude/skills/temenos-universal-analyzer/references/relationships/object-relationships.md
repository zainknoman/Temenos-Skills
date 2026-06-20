# Object Relationship Graph

## Contents
1. [Relationship Model](#relationship-model)
2. [Class to Application Relationships](#class-to-application-relationships)
3. [Class to Event Relationships](#class-to-event-relationships)
4. [Class to Hook Relationships](#class-to-hook-relationships)
5. [Product to Product Relationships](#product-to-product-relationships)
6. [Full Relationship Matrix](#full-relationship-matrix)

---

## Relationship Model

```
Class ─── reads/writes ──► T24 Application
Class ─── fires ─────────► Event
Class ─── implements ────► Hook Interface
Hook ─── fires on ───────► Lifecycle Phase
Event ─── triggers ──────► Listener Class
Product ─── depends on ──► Product
```

---

## Class to Application Relationships

<!-- Populate from JAR analysis — which classes read/write which T24 applications -->

| Class | Reads | Writes | Authorises |
|-------|-------|--------|-----------|
| AAActivityRecord | ARRANGEMENT, AA.ACTIVITY | | |
| AAArrangementRecord | ARRANGEMENT | | |
| ContractAPI | (populate) | (populate) | |
| (populate) | | | |

---

## Class to Event Relationships

<!-- Which classes fire which events, and which classes listen -->

| Class | Fires Events | Listens To |
|-------|-------------|-----------|
| (populate) | | |

---

## Class to Hook Relationships

<!-- Which hook interfaces are implemented by which classes -->

| Hook Interface | Implemented By | Applied To Application |
|--------------|---------------|----------------------|
| RecordLifecycle | (populate) | (populate) |
| (AA CalculationHook) | (populate) | (populate) |
| (AA SettlementHook) | (populate) | (populate) |
| (AA PaymentScheduleHook) | (populate) | (populate) |

---

## Product to Product Relationships

<!-- Inter-product dependencies and data flows -->

```
AA Framework
  |--- reads --> ACCOUNT (via AC APIs)
  |--- reads --> CUSTOMER (via ST APIs)
  |--- writes --> FT (via OFS for settlement)
  |--- uses --> COB (for batch processing)

FT Payments
  |--- reads --> ACCOUNT
  |--- reads --> CUSTOMER
  |--- uses --> TPH (for routing)

TPH
  |--- orchestrates --> FT
  |--- orchestrates --> AA.Settlement
```

---

## Full Relationship Matrix

<!-- Auto-generate from static analysis: class -> {reads, writes, fires, listens, implements} -->

```
(populate from JAR analysis)

Format:
ClassName:
  reads: [App1, App2]
  writes: [App3]
  fires: [Event1, Event2]
  listens: [Event3]
  implements: [HookInterface1]
  extends: [SuperClass]
```
