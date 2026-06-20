# Temenos T24/Transact — Product Map

## Contents
1. [Product Inventory](#product-inventory)
2. [Module Ownership](#module-ownership)
3. [Framework Overview](#framework-overview)
4. [JAR-to-Product Mapping](#jar-to-product-mapping)

---

## Product Inventory

<!-- Populate from JAR analysis: one row per product family -->

| Product Code | Full Name | JAR Prefix | Primary Framework |
|-------------|-----------|------------|-------------------|
| AA | Arrangement Architecture | AA_* | AA Framework |
| AC | Accounts | AC_* | EB.API |
| FT | Funds Transfer / Payments | FT_* | Payments Framework |
| LD | Lending | LD_* | EB.API / AA |
| TD | Term Deposits | TD_* | EB.API / AA |
| ST | System | ST_* | EB.API |
| TT | Teller / ATM | TT_* | ATM Framework |
| TPH | Transaction Processing Hub | TPH_* | TPH Framework |
| COB | Close of Business | COB_* | COB Framework |
| DE | Document / Delivery Engine | CBI.DE* | DE Framework |

---

## Module Ownership

<!-- Map each module to owning team / product squad -->

| Module | Owner Team | Key Applications |
|--------|-----------|-----------------|
| AA Framework | AA Core | ARRANGEMENT, AA.PRODUCT, AA.ACTIVITY |
| Payments | Payments Core | FUNDS.TRANSFER, FT.COMMISSION |
| Accounts | Core Banking | ACCOUNT, AC.ENTRY |
| Customer | Core Banking | CUSTOMER, ST.CUSTOMER.LOCAL |
| Lending | Lending | LD.LOANS.AND.DEPOSITS, AA.LENDING |
| Deposits | Deposits | TD.DEPOSIT, AA.TERM.DEPOSIT |
| TPH | Payments Hub | TP.PAYMENT.ORDER, TP.HUB |
| ATM | Channels | TT.CONTRACT, TT.TELLER |
| COB | Operations | COB.SERVICE, COB.PROCESS |

---

## Framework Overview

<!-- Summary of each framework — detail in architecture/frameworks.md -->

| Framework | Purpose | Entry Point |
|-----------|---------|-------------|
| AA Framework | Lifecycle and property management for financial products | AA.ACTIVITY |
| EB.API | Core record read/write, validation, authorisation | EB.CONTRACT.BALANCES |
| OFS | Programmatic T24 transaction submission | OfsBuildRecord / OfsCallBulkManager |
| DE | Document generation and print interface | ApplicationHandoff / CBI.DE.EVENT.MAPPING |
| TPH | Payment hub routing, adapters, message transformation | TP.PAYMENT.ORDER |
| COB | End-of-day batch processing | COB.SERVICE |
| ATM/Teller | Cash, denomination, teller operations | TT.CONTRACT.TELLER |

---

## JAR-to-Product Mapping

<!-- Auto-generated from jar/t24lib — populate with JAR analysis output -->

| JAR File | Product | Primary Package | Key Classes |
|----------|---------|-----------------|-------------|
| AA_Framework.jar | AA | com.temenos.t24.api.arrangement | (populate) |
| AA_ActivityAPI.jar | AA | com.temenos.t24.api.arrangement.activity | (populate) |
| AA_ContractApi.jar | AA | com.temenos.t24.api.contract | (populate) |
| AA_ProductApi.jar | AA | com.temenos.t24.api.product | (populate) |

<!-- Continue for all 2050 JARs -->
