# Temenos T24/Transact — Product Map

> Manually curated 2026-06-20. Re-run `aggregate.py` and cross-reference with class-index.md to refresh JAR counts.
> Sources: JAR analysis, Transact Architecture PDFs, TAFJ R19 Course Document, Content Packages PDF.

---

## Product Inventory

| Product Code | Full Name | JAR Prefix | Primary Framework | Key T24 Applications |
|-------------|-----------|------------|-------------------|---------------------|
| AA | Arrangement Architecture | AA_* | AA Framework | ARRANGEMENT, AA.PRODUCT, AA.ACTIVITY, AA.ARRANGEMENT.ACTIVITY |
| AC | Accounts | AC_* | EB.API | ACCOUNT, AC.ENTRY, AC.POS.ENTRY |
| FT | Funds Transfer / Payments | FT_* | Payments Framework | FUNDS.TRANSFER, FT.COMMISSION, FT.TXN.HISTORY |
| LD | Lending (Classic) | LD_* | EB.API | LD.LOANS.AND.DEPOSITS |
| TD | Term Deposits (Classic) | TD_* | EB.API | TD.DEPOSIT, TD.ADVISE |
| ST | System / Core | ST_* | EB.API | CUSTOMER, COMPANY, CURRENCY, CATEGORY |
| TT | Teller / ATM | TT_* | ATM Framework | TT.CONTRACT, TT.TELLER, TT.DENOMINATION, TT.BRANCH.LIMIT |
| PI/PP/TP | Payment Initiation / TPH | PI_*, PP_*, TP_* | TPH Framework | TP.PAYMENT.ORDER, PP.PAYMENT |
| COB | Close of Business | COB_* | COB Framework | COB.SERVICE, COB.PROCESS, COB.PARAM |
| DE | Document / Delivery Engine | DE.* | DE Framework | DE.EVENT.MAPPING, DE.PRINT.INTERFACE |
| EB | Core Framework | EB_* | EB.API | EB.API, VERSION, ENQUIRY, SCREEN, AUTH.TASK |
| SC | Securities | SC_* | EB.API | SC.SEC.MASTER, SC.TRANS.ENTRY |
| AM | Asset Management | AM_* | EB.API | AM.FUND, AM.PORTFOLIO |
| CR | Credit / Limits | CR_* | EB.API | LIMIT, COLLATERAL |
| DX | Documents / Trade Finance | DX_* | EB.API | LC.BRANCH, LC.TERMS |
| RE | Regulatory | RE_*, AFRXXX | EB.API | RE.STAT.REPORT |

---

## Analytics Platform — Product Lines

The Temenos Analytics Platform sits above Transact and is composed of several licensed product tiers:

| Product | Description |
|---------|-------------|
| **Transact Data Hub (TDH)** | Near-real-time and batch ETL from T24 Transact into ODS and SDS stores. Out-of-the-box workflows, metadata management, on-premise or cloud |
| **Temenos Data Lake (TDL)** | Superset of TDH — adds Enterprise Data Integration, ML/AI, and support for semi-structured/unstructured third-party data |
| **Temenos Data Engineering (TDE)** | ETL configuration and monitoring web front-end; Administrator and Designer modules for ODS/SDS/ADS workflows |
| **Temenos Analytics** | Analytics Data Warehouse + Analytics Web UI; includes content packages (Retail, Financial, Corporate, Risk) |

### Analytics Content Packages and Add-on Modules

| Package / Add-on | License | Description |
|-----------------|---------|-------------|
| Embedded Analytics | Add-on | Embeds Analytics tiles, KPI tiles, Pivot Reports, and Dashboards directly in Transact |
| XAI / Machine Learning | Add-on (per model) | ML models for customer attrition, life-time value, and other key metrics |
| Digital Analytics | Add-on | Digital Campaign management, Digital Engagements, Clickstream Analytics |
| Customer Profitability | Add-on | Current customer and account-based profitability calculations |
| Retail Analytics | Content Package | Data relationships, quick/pivot reports, visuals and dashboards — retail banking |
| Financial Analytics | Content Package | Data relationships, quick/pivot reports, visuals and dashboards — financial reporting |
| Corporate Analytics | Content Package | Corporate data pivot reports and dashboards |
| Risk Analytics | Content Package | Data relationships and datasets only |
| API Services | Add-on | Publish Analytics datasets as APIs for Transact, Digital, Power BI, and third-party systems |
| Customer Data Protection (GDPR) | Add-on | GDPR data protection services |

---

## Module Ownership

| Module | Key Applications | Hook Superclass | Package |
|--------|-----------------|-----------------|---------|
| AA Framework | ARRANGEMENT, AA.ARRANGEMENT.ACTIVITY | ActivityLifecycle | com.temenos.t24.api.hook.arrangement |
| Classic Banking | ACCOUNT, FUNDS.TRANSFER, CUSTOMER | RecordLifecycle | com.temenos.t24.api.hook.system |
| Batch / COB | COB.SERVICE, COB.PROCESS | ServiceLifecycle | com.temenos.t24.api.hook.system |
| Enquiry | ENQUIRY, SCREEN | Enquiry | com.temenos.t24.api.hook.system |
| Payments | TP.PAYMENT.ORDER, PP.PAYMENT | PaymentLifecycle / PaymentOrderLifecycle | com.temenos.t24.api.hook.payments |
| ATM / Teller | TT.CONTRACT, TT.TELLER | RecordLifecycle (TT apps) | com.temenos.t24.api.hook.system |
| DE | DE.EVENT.MAPPING | ApplicationHandoff (jBC) | N/A — jBC-based |
| OFS | N/A (interface) | OfsBuildRecord / OfsCallBulkManager | com.temenos.t24 (jBC runtime) |

---

## TEFA Framework Overview (6-Framework Model)

The six TEFA frameworks apply to the full Transact product suite. Each framework addresses a distinct layer of the architecture:

| Framework | TEFA Role | Purpose | Entry Point | Customisation Layer |
|-----------|-----------|---------|-------------|---------------------|
| Event Framework (Integration) | System-to-system | Asynchronous B2B event messaging; XML/XSD/XSLT over JMS/MQ/ESB | Exit Point on VERSION/application | Integration Flow definitions; ESB adapters |
| API Framework (Interaction) | UI-to-system | RESTful API exposure; synchronous request/response for UI consumers | IRIS REST endpoints | REST annotations; OpenAPI spec; Adapter Framework Microservice |
| Data Hub | Data persistence | Database-independent OLTP + OLAP storage; ETL for analytics | JDBC datasource; Data Event Streaming | TDE ETL configuration; ODS/SDS/ADS workflows |
| Design Framework | Development tooling | Model-driven IDE: version/enquiry/screen design; packaging and deployment | Design Studio (Eclipse); Temenos Workbench | Version, Enquiry, Composite Screen, Rules designers |
| Component Framework | Banking capability | Independently deployable, modular banking components (Interest, Fees, Lifecycle) | Component service operations; Eclipse Modelling tool | jBC component methods (GET/WRITE/ENQUIRY); Java component APIs |
| Platform Framework | Runtime and middleware | TAFJ compiler/runtime; JEE application server integration; JDBC connectivity | JBoss EAP / WebLogic / WebSphere + TAFJ | TAFJ properties; module.xml; datasource configuration |

---

## Extensibility Framework — Model Artefact Types

Transact models configurable via Extensibility Framework (Design Studio / Temenos Workbench):

| Artefact | T24 Table / Feature | Description |
|----------|-------------------|-------------|
| Version | VERSION | Screen layouts for Transact applications; contains HOOK.CLASS for Java hooks |
| Enquiry | ENQUIRY | Query/report definitions with selection criteria and drill-down |
| Menu | MENU | Sub-menu contents linked to Main Menu |
| Main Menu | MAIN.MENU | Top-level menus attached to user profiles |
| Composite Screen | COMPOSITE.SCREEN | Multi-frame screens combining multiple enquiries |
| Tabbed Screen | TABBED.SCREEN | Tab-based screens for space-efficient viewing |
| UXP Browser COS | UXPB.COS | Composite screens for UXP Browser |
| Rules (EB Rules) | EB.RULES | Business rules — designed, modified, validated and published |
| Local Field | USER.FIELD | Custom data element on an existing Transact application table |
| Local Application | USER.APPLICATION | New Transact application for user-specific requirements |
| Reference Table | LOCAL.REF | Supporting reference data tables |

---

## Framework Overview — Detailed (Development Focus)

| Framework | Purpose | Entry Point | Customization Layer |
|-----------|---------|-------------|---------------------|
| AA Framework | Lifecycle and property management for lending/deposit/savings products | AA.ARRANGEMENT.ACTIVITY | ActivityLifecycle (Java), AA routines (jBC) |
| EB.API (RecordLifecycle) | Transaction-level hooks on any T24 application | VERSION record (HOOK field) | RecordLifecycle (Java) or version routines (jBC) |
| OFS | Programmatic T24 transaction submission without a screen | OFS.GLOBUS.MANAGER (jBC) / OfsBuildRecord | OFS routine (jBC) |
| DE | Document generation — feeds Docupilot and print interfaces | DE.EVENT.MAPPING | ApplicationHandoff + DE.GET.* FUNCTIONs (jBC) |
| TPH | Payment hub routing, message transform, adapter management | TP.PAYMENT.ORDER input/authorise | PaymentOrderLifecycle / PaymentLifecycle (Java) |
| COB | End-of-day batch processing | COB.SERVICE definition | ServiceLifecycle (Java) or COB service routines (jBC) |
| ATM/Teller | Cash management, teller operations, denomination handling | TT.CONTRACT.TELLER, TT.DENOMINATION | RecordLifecycle on TT.* apps |
| Process Orchestration (PW) | Business process workflow automation | PW.PROCESS.DEFINITION; PW.BUILDER screen | PW configuration; pattern-based workflow definitions |

---

## JAR-to-Product Mapping (Key JARs)

| JAR | Product | Primary Package | Component Types |
|-----|---------|-----------------|-----------------|
| AA_ActivityHook.jar | AA | com.temenos.t24.api.hook.arrangement | lifecycle-hook (ActivityLifecycle) |
| AA_ActivityAPI.jar | AA | com.temenos.t24.api.arrangement | public-api (ActivityAPI) |
| AA_ContractApi.jar | AA | com.temenos.t24.api.arrangement.accounting | public-api (Contract) |
| AA_BillApi.jar | AA | com.temenos.t24.api.arrangement | public-api (Bill) |
| AA_CalculationHook.jar | AA | com.temenos.t24.api.hook.arrangement | aa-calculation-hook |
| AA_Framework.jar | AA | com.temenos.t24.api | core AA framework |
| ST_CustomerApi.jar | ST | com.temenos.t24.api.system | public-api (Customer) |
| ST_Customer.jar | ST | com.temenos.t24 | record-model (CustomerRecord) |
| AC_API.jar | AC | com.temenos.t24.api | public-api (Account) |
| EB_API.jar | EB | com.temenos.t24.api.hook.system | RecordLifecycle, ServiceLifecycle, Enquiry superclasses |
| PI_PaymentOrderHook.jar | PI | com.temenos.t24.api.hook | public-api (PaymentOrderHook) |
| PP_PaymentLifecycleHook.jar | PP | com.temenos.t24.api.hook.payments | public-api (PaymentLifecycle) |
| PI_PaymentOrderLifecycleHook.jar | PI | com.temenos.t24.api.hook.payments | public-api (PaymentOrderLifecycle) |
| TT_Contract.jar | TT | com.temenos.t24 | teller record classes |
| TT_Foundation.jar | TT | com.temenos.t24 | ATM/teller foundation classes |
| TT_TellerFinancialService.jar | TT | com.temenos.t24 | teller financial services |
| COB_Framework.jar (if present) | COB | com.temenos.t24.api | ServiceLifecycle-based COB |
| AA_NoticeWithdrawal.jar | AA/TD | com.temenos.t24.api.arrangement | notice withdrawal API |
| AA_Closure.jar | AA | com.temenos.t24.api.arrangement | arrangement closure |
| AA_PaymentScheduleHook.jar | AA | com.temenos.t24.api.hook.arrangement | payment schedule hook |

> For the full 2,050-JAR inventory, see [references/relationships/dependency-graph.md](../relationships/dependency-graph.md).
