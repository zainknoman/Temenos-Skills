# Temenos Framework Internal Architecture

## Contents
1. [EB.API Framework](#ebapi-framework)
2. [AA Framework](#aa-framework)
3. [OFS Framework](#ofs-framework)
4. [DE (Delivery Engine) Framework](#de-framework)
5. [TPH Framework](#tph-framework)
6. [COB Framework](#cob-framework)
7. [ATM / Teller Framework](#atm--teller-framework)

---

## EB.API Framework

<!-- Populate from JAR analysis of EB_* and core JARs -->

**Purpose**: Core record lifecycle — read, write, validate, authorise T24 records.

**Key packages**: (populate)

**Core classes**:
| Class | Role |
|-------|------|
| (populate) | |

**Hook points**: CheckId, CheckRecord, AutoField, Validation, Input, BeforeAuth, Auth

---

## AA Framework

<!-- Populate from AA_Framework.jar, AA_ActivityAPI.jar, AA_ProductApi.jar analysis -->

**Purpose**: Lifecycle and property management for financial products (lending, deposits, accounts).

**Key packages**: (populate)

**Lifecycle phases**: Open, Amend, Close, Rollover, Restructure, Payoff, ChargeOff

**Property types**: (populate)

**Activity types**: (populate)

**Hook classes**:
| Hook Type | Class | When Fired |
|-----------|-------|-----------|
| Calculation | (populate) | |
| Check | (populate) | |
| Getter | (populate) | |
| SettlementHook | (populate) | |
| PaymentScheduleHook | (populate) | |

---

## OFS Framework

<!-- Populate from OFS_* JAR analysis -->

**Purpose**: Programmatic T24 transaction submission via OFS messages.

**Key classes**:
| Class | Role |
|-------|------|
| OfsBuildRecord | Build OFS request message |
| OfsCallBulkManager | Submit batch OFS calls |
| (populate) | |

**Message format**: (populate)

**Error handling pattern**: (populate)

---

## DE Framework

<!-- Populate from DE_* / CBI.DE analysis -->

**Purpose**: Document generation and delivery — feeds Docupilot and other print interfaces.

**Pipeline**:
1. ApplicationHandoff routine fires on event
2. Array.5 positions mapped to output fields
3. CBI.DE.EVENT.MAPPING configures template + fields routines
4. CBI.DE.PRINT.INTERFACE dispatches to Docupilot
5. CBI.GET.* FUNCTION routines supply document data

**Key tables**: CBI.DE.EVENT.MAPPING, CBI.DE.PRINT.INTERFACE

---

## TPH Framework

<!-- Populate from TPH_* JAR analysis -->

**Purpose**: Payment hub routing, message transformation, adapter management.

**Key packages**: (populate)

**Adapter types**: (populate)

**Message types**: (populate)

---

## COB Framework

<!-- Populate from COB_* JAR analysis -->

**Purpose**: End-of-day batch processing and service orchestration.

**Service lifecycle**: (populate)

**Key classes**: (populate)

---

## ATM / Teller Framework

<!-- Populate from TT_* JAR analysis -->

**Purpose**: Cash management, denomination handling, teller operations.

**Key classes**: (populate)

**Key applications**: TT.CONTRACT, TT.TELLER, TT.DENOMINATION
