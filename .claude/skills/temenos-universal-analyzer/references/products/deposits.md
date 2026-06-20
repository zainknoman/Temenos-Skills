# Deposits Product Reference

## Contents
1. [Key Applications](#key-applications)
2. [Key Classes](#key-classes)
3. [Maturity and Rollover](#maturity-and-rollover)
4. [Notice Withdrawal](#notice-withdrawal)
5. [Code Patterns](#code-patterns)

---

## Key Applications

| Application | Purpose |
|------------|---------|
| TD.DEPOSIT | Classic term deposit |
| AA.TERM.DEPOSIT | AA-based term deposit |
| AA.NOTICE.WITHDRAWAL | Notice period withdrawal |
| AA.MATURITY | Maturity processing |

---

## Key Classes

<!-- Populate from TD_* and AA_DepositData.jar analysis -->

| Class | Package | JAR | Role |
|-------|---------|-----|------|
| (populate) | | AA_DepositData.jar | Deposit data access |
| (populate) | | AA_NoticeWithdrawal.jar | Notice withdrawal |
| (populate) | | AA_Closure.jar | Deposit closure |

---

## Maturity and Rollover

**Rollover types**: Auto, Manual, Principal-only, Principal-and-Interest

**Rollover hooks**: (populate — from AA_PayoutRules.jar, AA_RestructureRules.jar)

**Maturity workflow**: (populate)

---

## Notice Withdrawal

**Notice period types**: (populate)

**Penalty calculation on early withdrawal**: (populate)

**NoticeWithdrawal API**: (populate)

---

## Code Patterns

### Set rollover instruction

```java
// populate
```

### Process maturity

```java
// populate
```
