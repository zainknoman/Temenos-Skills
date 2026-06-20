# Cross-JAR Dependency Graph

## Contents
1. [Dependency Principles](#dependency-principles)
2. [Core Layer](#core-layer)
3. [Product Layer](#product-layer)
4. [Integration Layer](#integration-layer)
5. [Full Dependency Matrix](#full-dependency-matrix)

---

## Dependency Principles

- Core JARs have no product dependencies
- Product JARs depend on Core and optionally on sibling products
- Integration JARs (OFS, DE, REST) depend on product JARs they bridge
- Custom L3 code depends on product JARs via $USING declarations

---

## Core Layer

<!-- JARs that have no upstream T24 dependencies -->

| JAR | Dependents |
|-----|-----------|
| (populate from JAR manifest analysis) | |

---

## Product Layer

<!-- Per-product dependency chains -->

### AA Dependencies

| JAR | Depends On | Used By |
|-----|-----------|---------|
| AA_Framework.jar | (populate) | (populate) |
| AA_ActivityAPI.jar | AA_Framework.jar, (populate) | (populate) |

### Payments Dependencies

| JAR | Depends On | Used By |
|-----|-----------|---------|
| (populate) | | |

### Accounts Dependencies

| JAR | Depends On | Used By |
|-----|-----------|---------|
| (populate) | | |

---

## Integration Layer

| JAR | Bridges | Depends On |
|-----|---------|-----------|
| (OFS JARs) | OFS <-> Core | (populate) |
| (DE JARs) | DE <-> Products | (populate) |
| (REST JARs) | REST <-> Products | (populate) |

---

## Full Dependency Matrix

<!-- Auto-generated from JAR MANIFEST.MF Class-Path entries -->
<!-- Format: source-jar -> [dependency1, dependency2, ...] -->

```
(populate via JAR analysis)
```
