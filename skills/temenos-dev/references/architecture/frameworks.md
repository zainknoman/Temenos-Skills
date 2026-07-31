# Temenos Framework Internal Architecture

> Manually curated 2026-06-20. Sources: JAR analysis, T24 Technical Training, L3 Java CSD standards, Transact Architecture PDFs, TAFJ R19 Course Document.

---

## Temenos Enterprise Framework Architecture (TEFA)

Transact is built on a platform of **six frameworks** called the Temenos Enterprise Framework Architecture (TEFA). The "cube" model shows the technical direction Temenos has taken for Transact product architecture.

| Framework | Alias | Purpose |
|-----------|-------|---------|
| 1. Event Framework | Integration | System-to-system integration (B2B) — asynchronous event messaging |
| 2. API Framework | Interaction | User interface / API mediation — synchronous RESTful resource access |
| 3. Data Hub | — | Database independence — OLTP + OLAP persistence abstraction |
| 4. Design Framework | — | Model-driven design and development environment |
| 5. Component Framework | — | Modular banking capability — componentised, independently deployable |
| 6. Platform Framework | — | Middleware and database underpinning — application server + TAFJ |

**Key benefits**: Multi-platform, fully modular, componentised, event-based coding, model-driven, supports in-memory OLTP and column-store OLAP data models.

---

## 1. Event Framework (Integration)

**Role**: Mediates between Transact and external systems (B2B). Enables exchange of business events and transactional messaging with third-party systems without writing code or understanding OFS syntax.

**Technology**: Event-driven integration using XML / XSD / XSLT. Messages carried by:
- Java Message Service (JMS)
- Message Queue (MQ)
- Enterprise Service Bus (ESB)

**Supported ESB Middleware**: IBM Integration Bus (IIB / WebSphere Message Broker), Fiorano Server, BizTalk Server, Oracle Service Bus, Mule Software (.NET).

**Key Concepts**:

| Concept | Description |
|---------|-------------|
| Exit Point | Hook/API in Transact where an event notification leaves. Linked to VERSIONs, applications, or component service operations |
| Integration Flow | XML message layout definition emitted when a business event occurs |
| Flow Catalog | Transact table containing all Integration Flows created by integrators |
| Service Repository | Contains all available component services, operations, data types and direction (in/out/inout) |
| Event Delivery Service | Polls the interface table and delivers events to JMS with 2PC |

**vs API Framework**: Event = asynchronous system-to-system (pairs of one-way messages). API = synchronous request/response between systems and humans via UIs.

---

## 2. API Framework (Interaction)

**Role**: Mediates between user interfaces and banking capability. Exposes banking resources in a standard way (RESTful API) so bank and third-party designers can build UIs.

**Technology**: Strict RESTful interaction patterns using URIs to identify resources and HTTP for requests.

**Implementation — IRIS**:
- Standalone lightweight edition of Temenos Interaction Framework
- Communicates to Transact via OFS (Open Financial Service)
- Uses Java Message Service (JMS) and Message Driven Bean (MDB)
- Based on Open API — both Provider APIs and Published APIs
- RESTful (REST = Representational State Transfer)

**API vs Event**:
- API Framework supports **synchronous** calls (request/response between systems and UIs)
- Event Framework supports **asynchronous** system-to-system messaging

---

## 3. Data Hub

**Role**: Makes Temenos product code independent of the database regardless of the underlying database platform.

**Supported Databases**: Oracle, DB2, MS SQL Server, NuoDB, H2 (development).

**Two simultaneous storage areas**:

| Area | Type | Purpose |
|------|------|---------|
| OLTP Engine | Transactional (row-based) | Insert business events — online banking transactions |
| OLAP | Column-store analytical | Transact Analytics: FRM (Financial Risk Management), FCM (Financial Crime Mitigation) |

**Data Lifecycle Management (DLM)** — licensed product:
- Manages archiving of non-active data into NVDB (Non-Volatile Database / Read-Only Database)
- Data remains visible from both live DB and NVDB
- Configurable: retention time, timing of transfers, objects to include, partition timespans

**DLM Stages**: Move (old transactions to NVDB) → Report (daily time series) → Archive (old data to cheap storage) → Analyse/Report (ETL for cubes/graphs).

---

## 4. Design Framework

**Role**: Provides a model-driven design and development environment. Separates design-time from run-time data.

**Implementations**:
- **Design Studio** (Eclipse-based) — for Transact, TAP
- **Temenos Workbench** — web and Eclipse compatible

**Design Studio capabilities**:
- Represent Transact data models using the Graphical Domain Viewer
- Design design-time artefacts: Versions, Enquiries, Composite Screens, Tabbed Screens, Context Enquiries, Menus, Local References
- Package software changes and deploy on Transact runtime environments (Design Studio Packager)
- Develop local code (jBC) for TAFJ runtime — IDE Local Code Management
- Design events and flows for the Integration Framework (Integration Studio)
- Add interaction-plugin dependencies (RIM files) for the Interaction Framework
- Create Temenos Web Services (Web Service Composer)
- Create BPM workflows
- Create RESTful web services for the Interaction Framework

**Temenos Workbench** includes:
- API designers (Transact API creation with vision/enquiry designers)
- Local field/reference management
- Local application designers
- Transact configuration designers: Version, Enquiry, Menu, Composite Screen, Tabbed Screens, Rules, PW activity/transition
- Packager: web + Eclipse compatible, AA+PW packaging, SCM/Transact synchronisation, atomic deployment, deployment custom sequence, pre/post phases, incremental deployments, field-level updates

---

## 5. Component Framework

**Role**: Lies at the heart of Transact. Separates the logic of different Temenos functions into independently deployable components.

**Two parts**:

| Part | Description |
|------|-------------|
| SOA Common Runtime | Released with TAFC or TAFJ — common functionalities required by all components |
| Individually designed components | Provide unique functionality for TAFC or TAFJ; use Eclipse Modelling tool to generate APIs |

**Benefits**:
- Banks deploy only the solutions they need (no need to replace entire core banking system)
- Progressive renovation of legacy systems
- Incremental upgrade and online update (hot deployment of fixes)
- Reusability, lower cost of innovation
- Shared components (Interest, Fees, Product Lifecycle Management) can be componentised across Loans and Deposits modules

---

## 6. Platform Framework (TAFJ)

**Role**: Built for the middleware and database that underpins all other frameworks. Provides flexibility, independence, scalability, and cost-efficiency.

### TAFJ Overview

**TAFJ (Temenos Application Framework Java)** is the proprietary runtime and compiler for jBC code. It allows compiling and running jBC programs on Java, enabling T24 to harness full J2EE functionality (connection pooling, threading, security, etc.).

**Supported databases via JDBC**: Oracle, Microsoft SQL Server, DB2, DB2-zOS, NuoDB, H2 (development).

**Supported application servers (JEE)**: JBoss EAP, Oracle WebLogic, IBM WebSphere.

**Runtime**: T24 on TAFJ R18+ runs on JDK 1.8 and above.

### TAFJ Architecture

```
T24 source (*.b files)
  → TAFJ lexer/parser/tree-walker
  → Java source (*.java)
  → javac compiler
  → Java bytecode (*.class)
  → packaged into JAR files
  → deployed on J2EE server
```

- Platform independent: JVM interprets bytecode on any OS (Windows, Unix, zOS)
- JDBC drivers connect to JDBC-compliant databases
- log4j 2 (and SLF4J, Log4J 1.2, logback) for logging
- TAFJ lock manager for database lock management
- Streams redirectable to remote client console

### TAFJ_HOME Directory Structure

| Directory | Purpose |
|-----------|---------|
| `bin/` | TAFJ tools (tCompile, DBTools, tDiag, tShow, tCrypt, etc.) |
| `lib/` | TAFJ runtime libraries (including TAFJClient.jar) |
| `conf/` | Project property files (.properties) |
| `data/` | Compilation output (classes, jars, java folders) |
| `dbdrivers/` | JDBC drivers for all supported databases |
| `dbscripts/` | Database scripts for DB2, Oracle, MSSQL, H2 |
| `appserver/` | Application server configuration files (JBoss, WebSphere, WebLogic) |
| `3rdParty/` | Third-party jars (Apache Ignite, JackRabbit, Jackson, etc.) |
| `eclipse/plugins/` | TAFJ Eclipse plugins for Design Studio |
| `ext/` | Java extensions |
| `log/` | TAFJ runtime logs |
| `log_T24/` | T24 application logs |
| `TAFJSessionMonitor/` | TAFJ session monitoring tool |
| `JMSInjector/` | Standalone tool to inject OFS into queues |
| `CodeCoverageReceiver/` | Standalone app for calculating/reporting test coverage |

### TAFJ Properties

All configuration is stored in `.properties` files under `%TAFJ_HOME%\conf`. Key properties:

| Property | Purpose |
|----------|---------|
| `tafj.home` | Points to TAFJ_HOME folder |
| `temn.tafj.directory.java` | Output folder for generated Java source files |
| `temn.tafj.directory.classes` | Output folder for compiled class files |
| `temn.tafj.directory.precompile` | Location of precompiled JARs (T24 core libraries) |
| `temn.tafj.jdbc.url` | Database connection URL |
| `temn.tafj.jdbc.driver` | JDBC driver class |
| `temn.tafj.jdbc.username` | Database username |
| `temn.tafj.jdbc.password` | Database password (DES3-encrypted by tCrypt) |
| `temn.tafj.package` | Java package name for compiled classes (default: `com.temenos.t24`) |
| `temn.tafj.compiler.grammar.maxlevel` | Maximum grammar level for compilation |
| `temn.tafj.compiler.grammar.minlevel` | Minimum grammar level for compilation |
| `temn.tafj.runtime.phantom.as.process` | `true` = services spawn multiple JVMs; `false` = multithreaded |

**Default project**: Set by `.default` file in conf. Default file is `tafj.properties`. Each `.properties` file = one TAFJ project.

**Logger configuration**: `TAFJTrace.properties` — default logger config for writing execution logs. Separate loggers for T24, MDB, EJB, database, runtime etc.

**Log folder customisation**:
- TAFJ logs: `temenos.log.directory=<path>`
- T24 logs: `temenos.log.directory.t24=<path>`
- COMO logs: `temenos.log.directory.como=<path>`

### TAFJ Grammar Levels

During compilation, BASIC code is translated to Java at one of two grammar levels:

| Level | Description |
|-------|-------------|
| Grammar 2/3 | No GOTO/label control flow within IF, BEGIN CASE, FOR, LOOP constructs. Most optimised — generates well-formed, maintainable Java |
| Grammar 0 | Contains branching to labels within looping constructs. Required for existing T24 code that has GOTOs and labels |

Grammar level controlled by: `temn.tafj.compiler.grammar.maxlevel` and `temn.tafj.compiler.grammar.minlevel`.

### TAFJ Standalone Tools

| Tool | Purpose |
|------|---------|
| `tCompile` | Compile BASIC (.b) files to Java classes |
| `tRun` | Execute a compiled BASIC program (syntax: `tRun [-cf <conf>] <program> [<params>]`) |
| `tDiag` | Display diagnostic details of TAFJ setup — equivalent of jdiag in TAFC |
| `tShow` | Show compilation details of a BASIC routine — equivalent of jShow in TAFC |
| `tCrypt` | Encrypt database password in property file (DES3 algorithm) |
| `tFindDevice` | List available printers; configure printer channels in properties |
| `tUserMgnt` | Create/reset/delete TAFJ users for DBTools access (--Add, --Reset, --Del) |
| `Bootstrap` | Batch file executed by all scripts — sets JVM memory (Xss, Xms, Xmx) |
| `DBTools` | Database management console — SQL, JQL, OFS, JQL2SQL modes |

### TAFJ Deployment (JBoss EAP 7)

**Application package**: `TAFJJEE_EAR.ear` — the main enterprise application archive.

**Deployment steps**:
1. Install TAFJ module (`module.xml` — declares TAFJ libraries)
2. Install T24 module (generate `T24 module.xml` with T24 core JARs)
3. Install H2 driver module (if using H2)
4. Configure standalone profiles and datasources
5. Configure thread pooling
6. Configure JMS destinations
7. Deploy Browser Servlet
8. Deploy `TAFJJEE_EAR.ear`
9. Optionally: install JBoss client JARs for remote EJB access

**Key JBoss configuration files**:
- `standalone.xml` / `T24.xml` — datasources, thread pools, JMS destinations
- `TAFJ_CONFIGURATION` table — runtime configuration stored in the database

### TAFJ Web Services

| Invocation Type | Description |
|-----------------|-------------|
| Synchronous Invocation | WebService or EJB invocation using TAFJClient API |
| Subroutine Invoker | Invoke a T24 subroutine directly via TAFJEE |
| tRun Invoker | Invoke a T24 routine via tRun mechanism |
| Asynchronous | JMS message via JMS client or CALLJEE statement |

**Two internal resolutions inside TAFJ**: OFS or CALL_AT.

### TAFJ Session Monitor

A tool to monitor T24 session activities: number of method calls, reads, writes, etc. Launched via browser using the HTTP port in `SessionMonitor.properties`.

### TAFJ Clustering and Threading

- Application server clustering applied to T24 automatically (inherits AS cluster configuration)
- COB and services on standalone: each agent executes as a distinct process (multiprocessing)
- COB on application server: multi-threaded — each tSA executes as a distinct thread; thread resource management done by AS

---

## Extensibility Framework

**Overview**: Enables developers to extend or customise Temenos product solutions for specific business requirements. Combines design-time tooling (Temenos Workbench) with runtime components.

**Components**:

| Component | Purpose |
|-----------|---------|
| Adapter Framework Microservice | Integrations via Apache Camel — event-to-REST, bulking, debulking, API-to-API |
| Virtual Table Microservice | Data addition (new tables) via JSON schema, Python scripting hooks |
| API Framework (IRIS R18) | API payload validation and defaults via Drools rules engine, Regex validations, data composition |
| Transact data extension | Additional data elements on Transact tables; auto-propagates to API payloads and events |
| Temenos Workbench | Design-time tooling for configuring and packaging extensibility features |

### Configuring Transact Models (via Extensibility Framework)

| Model Type | Purpose |
|-----------|---------|
| Version | Design screens for any Transact model. Created in four stages: core definition, field selection, field details, associations |
| Enquiry | Parameter definitions for enquiry system. Three stages: core definition, field selection, drill-down |
| Menu | Define sub-menu contents, linked to Main Menu |
| Main Menu | Define main menus attached to user profiles; linked to sub-menus |
| Composite Screen | Title and multi-value frames for composite screens |
| Tabbed Screen | Tabs displaying separate enquiries/contracts to save screen space |
| UXP Browser Composite Screen (COS) | Composite screens for UXP Browser |
| Rules (EB Rules) | Business rules — design, modify, validate, and publish via Rules > EB Rules |

### Extending the Data Model

- **Local/User Fields**: Custom data elements added to existing Transact application tables
- **Local Applications**: New Transact applications for user-specific requirements
- **Reference Tables**: Supporting reference data tables
- **External Hooks**: APIs enabling customisations to Transact applications through version routines and hook classes

### Adapter Framework Interface Patterns

| Pattern | Description |
|---------|-------------|
| Event → REST | Transform an incoming event into a REST API request to a target system |
| Simple Bulking | Receive data as events and batch events as a flat file |
| Flat-file Debulking | Read data from CSV/JSON file and push into target system as API or events |
| API → API | Accept data (JSON/XML) on API endpoint, transform to message, deliver on streaming platform or JMS Queue |

---

## TAFJ Test Framework (Platform Framework)

### TAFJ Application Test Framework (ATF)

- Runs OFS requests and makes assertions; requires complete Transact libraries and database
- Test files: `.tat` extension (TESTCASE declarations)
- Key methods: `ATF.runOfs()`, `ATF.mockData()`, `ATF.isRequestCommitted()`, `ATF.setDate()`, `ATF.setTime()`

### TAFJ Unit Test Framework (UTF)

- Tests individual jBC subroutines without a running database (in-memory)
- Test files: `.tut` extension (TESTCASE declarations)
- Execution: `tRun -test <testname>` or `tRun -test -recurs <directory>`
- Key methods: `UTF.setTarget()`, `UTF.addParam()`, `UTF.addStub()`, `UTF.runTest()`, `UTF.assertEquals()`, `UTF.setRecord()`, `UTF.getRecord()`

### TAFJ Code Coverage Receiver (CCR)

- Standalone program receiving coverage data from JBC code via TCP
- Generates HTML reports with line-level and subroutine-level coverage
- Managed via web interface (`http://<ip>:<port>/CoverageReceiver`) or command line (`ccr start`, `ccr create`, `ccr make`)
- Configuration in `CCReceiver.properties`

---

## Data Hub / Temenos Analytics Platform

### Transact Data Hub (TDH)

- Near-real time extraction of online data; historical extraction via batch
- Out-of-the-box ETL workflows for Temenos Transact data
- Metadata management and lineage
- Supports on-premise or cloud deployment

### Temenos Data Lake (TDL)

- All TDH capabilities plus Enterprise Data Integration
- ML/AI integration
- Supports structured, semi-structured, and unstructured data from third-party sources
- Big Data Architecture

### Temenos Data Engineering (TDE)

- ETL configuration and web front-end
- Administrator module: configures ETL for ODS and SDS
- Designer module: monitors ODS, SDS, and ADS workflows
- Data cleansing, parsing, transformation, metadata management

**Data Stores**:

| Store | Abbreviation | Purpose |
|-------|-------------|---------|
| Operational Data Store | ODS | Near-real time operational data |
| Snapshot Data Store | SDS | Historical snapshots |
| Analytics Data Warehouse | ADS | Staging tables, Dim/Fact tables, abstraction views |

**Data Event Streaming**: Mechanism by which Transact pushes change events to TDH/TDL.

### Temenos Analytics Content Packages

| Package | Description |
|---------|-------------|
| Embedded Analytics | Embed Analytics Information tiles, KPI tiles, Pivot Reports and Dashboards in Transact |
| XAI / Machine Learning | Business analysis and forecasts via ML models (customer attrition, life-time value, etc.) |
| Digital Analytics | Manages Digital Campaigns, Digital Engagements, Clickstream Analytics |
| Customer Profitability | Calculates current customer and account-based profitability |
| Retail Analytics | Data relationships, quick/pivot reports, visuals and dashboards |
| Financial Analytics | Financial data relationships, quick/pivot reports, visuals and dashboards |
| Corporate Analytics | Corporate data pivot reports and dashboards |
| Risk Analytics | Data relationships and datasets |
| API Services | Publish Analytics datasets through APIs for Transact, Digital, and third-party solutions (e.g. Power BI) |

---

## Process Orchestration (Process Workflow)

**Purpose**: Business process automation — groups various business and banking procedures into logical processes of activities.

**Key concepts**:

| Concept | Description |
|---------|-------------|
| Process | A particular course of action intended to achieve an end result |
| Workflow | Progress of work done by a business — a series of steps through which work is routed |
| PW.BUILDER | Composite screen (supplied with Model Bank) providing access to all PW configuration applications |
| PW.PROCESS.DEFINITION | Application where logical prerequisite conditions are defined using parenthesis |

**Features**:
- Pattern-based workflows (in addition to sequential workflows)
- Process variables for governing flow logic
- Versioning — process instances follow the version of the definition at creation
- Mapping — transfer information automatically from one activity to another
- External user task allocation via process variables
- External BPM integration (e.g. jBPM) via `LOCAL.TABLE` configuration
- Monitoring and reporting

**Configuration prerequisites**:
- `AUTO.ID.START` configured (installed automatically by Model Bank)
- `PW.CREATE.LOCAL.REF` service run to create local reference fields in all applications
- Local reference fields: `PROCESS.ID` (stores process instance ID) and `TASK.ID` (stores task instance ID)

---

## EB.API Framework (RecordLifecycle)

**Purpose**: Core record lifecycle — read, write, validate, authorise any T24 record.

### Key Packages

| Package | Contents |
|---------|---------|
| `com.temenos.t24.api.hook.system` | `RecordLifecycle`, `ServiceLifecycle`, `Enquiry` superclasses |
| `com.temenos.t24.api.complex.eb.templatehook` | `TransactionContext`, `TransactionData` (for updateRecord) |
| `com.temenos.t24.api.complex.eb.servicehook` | `TransactionData` (for postUpdateRequest), `ServiceData` |
| `com.temenos.t24.api.complex.eb.enquiryhook` | `EnquiryContext`, `FilterCriteria` |
| `com.temenos.t24.api.system` | `DataAccess`, `Session` |
| `com.temenos.api` | `TStructure`, `TField`, `TValidationResponse`, `TBoolean` |
| `com.temenos.t24.api.records.<app>` | Generated typed record classes per T24 application |
| `com.temenos.t24.api.tables.<app>` | Generated table classes for direct read/write/delete |

### TAFJ 'T' Types (TAFJClient.jar)

| Type | Purpose |
|------|---------|
| `TStructure` | Generic container for record or complex type parameters; maps Transact data to Java objects |
| `TField` | Getters and setters for field values, errors, and enrichments |
| `TValidationResponse` | Holds the validation response of any record |
| `T24Context` | Encapsulates the current session; all Hook classes are instances of T24Context |
| `FilterCriteria` | Selection criteria objects used in enquiry BUILD.ROUTINEs |
| `TransactionData` | Packages data for asynchronous transaction request posting |
| `SynchronousTransactionData` | Packages data for synchronous transaction request posting |
| `DataAccess` | Utility class to read, select, and access data in T24 (`com.temenos.t24.api.system`) |

### Hook Points (RecordLifecycle override methods)

| Method | When Called | Typical Use |
|--------|------------|-------------|
| `checkId` | Before record load, on ID entry | Validate/transform record ID |
| `defaultFieldValues` | After record load, before user input | Set field defaults |
| `validateField` | On each field change in browser | Real-time field validation |
| `checkRecord` | Full-record validation before commit | Cross-field validation |
| `updateRecord` | On AUTHORISE — drives linked transactions | Create child records via TransactionData |
| `postUpdateRequest` | After authorisation and DB commit | Post-authorise side effects |
| `updateCoreRecord` | Override: writes to core T24 tables | Direct core table manipulation |
| `generateSecondaryActivity` | AA: generate follow-up activity | Triggers secondary AA activity |
| `updateLookupTable` | AA: maintain concat files | Update custom lookup tables |

### VERSION Record Configuration

```
VERSION     CUSTOMER,CUSTOMER.OPEN
HOOK.CLASS  MyPackage.MyHook
```

The `HOOK.CLASS` field on the VERSION record points to the fully qualified class name.

---

## AA Framework

**Purpose**: Lifecycle and property management for financial products (lending, deposits, savings, current accounts). All products are modelled as Arrangements with configurable Properties.

### Key Packages

| Package | Contents |
|---------|---------|
| `com.temenos.t24.api.hook.arrangement` | `ActivityLifecycle` superclass |
| `com.temenos.t24.api.complex.aa.activityhook` | `ArrangementContext`, `TransactionData`, `SecondaryActivity`, `LookupData` |
| `com.temenos.t24.api.arrangement.accounting` | `Contract` — access arrangement property conditions |
| `com.temenos.t24.api.records.aaarrangement` | `AaArrangementRecord` |
| `com.temenos.t24.api.records.aaarrangementactivity` | `AaArrangementActivityRecord` |
| `com.temenos.t24.api.records.aaaccountdetails` | `AaAccountDetailsRecord` |
| `com.temenos.t24.api.records.aaproductcatalog` | `AaProductCatalogRecord` |
| `com.temenos.t24.api.records.aaprddes*` | Property definition record classes (Interest, PaymentSchedule, TermAmount, Charge, Account, etc.) |
| `com.temenos.t24.api.records.aaactivityhistory` | `AaActivityHistoryRecord` |

### Lifecycle Phases

| Phase | AA Activity Name Pattern | Key Hook |
|-------|------------------------|---------|
| Open | `LENDING-NEW-ARRANGEMENT`, `DEPOSITS-NEW-ARRANGEMENT` | defaultFieldValues, validateRecord |
| Amend | `LENDING-RENEGOTIATE-ARRANGEMENT` | validateRecord, postCoreTableUpdate |
| Payment Holiday | `LENDING-UPDATE-PAYMENT.HOLIDAY` | validateRecord |
| Close / Payoff | `DEPOSITS-CLOSE-ARRANGEMENT`, `LENDING-PAYOFF-ARRANGEMENT` | postCoreTableUpdate |
| Rollover | `DEPOSITS-ROLLOVER-ARRANGEMENT` | generateSecondaryActivity |
| Charge / Fee | `LENDING-CHANGE-DEFERPFT` | calculateCharge hook |
| Balance Update | `ACCOUNTS-UPDATE-BALANCE` | postCoreTableUpdate |

### Property Types (AA.PRODUCT configuration)

| Property Class | Record Class Suffix | Purpose |
|---------------|--------------------|---------| 
| COMMITMENT | `AaPrdDesTermAmountRecord` | Term, maturity date, amount |
| INTEREST | `AaPrdDesInterestRecord` | Rate, basis, accrual method |
| PAYMENT.SCHEDULE | `AaPrdDesPaymentScheduleRecord` | Payment type, frequency, amounts |
| CHARGE | `AaPrdDesChargeRecord` | Fee amounts, insurance percentages |
| ACCOUNT | `AaPrdDesAccountRecord` | Linked account reference |
| BALANCE.MAINTENANCE | `AaPrdDesBalanceMaintenanceRecord` | Balance adjustment rules |

### ActivityLifecycle Hook Points

| Method | When Called |
|--------|------------|
| `defaultFieldValues` | Before user sees activity screen |
| `validateRecord` | On commit, validates activity |
| `postCoreTableUpdate` | After authorisation, DB committed |
| `updateLookupTable` | Maintains custom concat/lookup tables |
| `generateSecondaryActivity` | Triggers follow-up AA activity |
| `setElementData` | Sets element-level data (seldom used) |
| `filterElements` | Filters available elements |

### T24 Applications Used

| Application | Purpose |
|------------|---------|
| `ARRANGEMENT` | Arrangement master record |
| `AA.ARRANGEMENT.ACTIVITY` | Activity input application |
| `AA.ACCOUNT.DETAILS` | Arrangement status, linked account |
| `AA.PRODUCT` | Product definition (properties, activities) |
| `AA.PRODUCT.CATALOG` | Published product catalog |
| `AA.ACTIVITY.HISTORY` | History of activities per arrangement |
| `AA.BILL.DETAILS` | Bill records (charge/fee demands) |
| `EB.CONTRACT.BALANCES` | Balance types (CURACCOUNT, TOTCOMMITMENT, etc.) |

---

## OFS Framework

**Purpose**: Programmatic T24 transaction submission via OFS messages. TAFC/jBC-based.

**Key call**: `CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)`

**Message format**: `APPLICATION,VERSION/FUNCTION/RECORD.ID/FIELD:::VALUE/`

**Status codes**: 0=error, 1=success, 3=override required

> See [ofs-api.md](../apis/ofs-api.md) for full patterns.

---

## DE Framework (Delivery Engine)

**Purpose**: Document generation and delivery — feeds Docupilot, PDF generators, and print interfaces from T24 events.

### Pipeline

```
1. Event fires on T24 application (e.g. ACCOUNT authorised)
2. DE.EVENT.MAPPING routes to ApplicationHandoff routine
3. ApplicationHandoff builds Array.5 with document data
4. DE.GET.* FUNCTION routines supply field-level data
5. DE.PRINT.INTERFACE dispatches to Docupilot/PDF engine
6. Document delivered via email/portal/print queue
```

### Key Applications / Tables

| Application | Purpose |
|------------|---------|
| `DE.EVENT.MAPPING` | Maps T24 events to document templates and handoff routines |
| `DE.PRINT.INTERFACE` | Configures delivery channel (email, portal, print) |
| `DE.DOC.TEMPLATE` | Template definitions |

### jBC Coding Pattern

```basic
* ApplicationHandoff routine — fires on event
SUBROUTINE MYBANK.DE.ACCOUNT.OPEN(ARRAY.5, EVENT.REC, ERR)

    $INSERT I_COMMON
    $INSERT I_EQUATE

    GOSUB INITIALISE
    GOSUB POPULATE.ARRAY
    RETURN

INITIALISE:
    ERR = ''
    ACCOUNT.ID = ARRAY.5<1,1>      * Record ID passed by DE framework
    RETURN

POPULATE.ARRAY:
    * Field positions in Array.5 defined by DE.EVENT.MAPPING
    ARRAY.5<2,1> = ACCOUNT.CURRENCY
    ARRAY.5<3,1> = ACCOUNT.BALANCE
    RETURN
END


* DE.GET.* FUNCTION — supplies a computed field to the document
FUNCTION MYBANK.GET.ACCOUNT.OFFICER(ACCOUNT.ID, ERR)
    CALL EB.READ.ANY('ACCOUNT', ACCOUNT.ID, R.ACCOUNT, ERR)
    MYBANK.GET.ACCOUNT.OFFICER = R.ACCOUNT<F.ACCOUNT.OFFICER>
END
```

---

## TPH Framework (Transaction Processing Hub)

**Purpose**: Payment hub — routes, enriches, transforms, and dispatches payments from any channel to any clearing network.

### Architecture Stages

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Acceptance | Receive payment message/files; de-bulk; Accept/Reject |
| 2 | Mapping | Parse and map to TPH neutral format (ISO 20022 internal model) |
| 3 | Preparation | Validation, duplicate detection, prioritisation |
| 4 | Processing | Routing, settlement selection, exception handling |
| 5 | Filtering | Regulatory / sanctions screening |
| 6 | Fees, FX & Posting | Fee calculation, FX conversion, ledger postings |
| 7 | Message Generation | Format outgoing messages (SWIFT MT, ISO 20022 XML, RTGS, etc.) |
| 8 | Finalisation | Reports, reconciliation, archiving |

### Key Applications

| Application | Purpose |
|------------|---------|
| `TP.PAYMENT.ORDER` | Core TPH payment order record |
| `PP.PAYMENT` | Processed payment record |
| `PP.PAYMENT.BENEFICIARY` | Beneficiary details |
| `PP.PAYMENT.DEBIT` | Debit side of payment |
| `PP.PAYMENT.SETTLEMENT` | Settlement instructions |

### Java Hook Classes (from JAR analysis)

| Class | JAR | Purpose |
|-------|-----|---------|
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | Hook on payment order input |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | Hook on payment processing lifecycle |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | Hook on payment order lifecycle |

### Supported Clearing Systems

| Type | Networks |
|------|---------|
| SWIFT | MT103, MT202, MX ISO 20022 |
| RTGS | TARGET2 (EU), FEDWIRE (US), CHATS (HK), SARIE (SA) |
| Bulk/ACH | BACS (UK), SEPA (EU), ACH |
| Instant | SEPA Instant, UK FPS, ISO 20022 pacs.008 |

---

## COB Framework (Close of Business)

**Purpose**: End-of-day batch processing — runs product-specific services, interest accruals, position updates.

### Service Lifecycle

| Phase | ServiceLifecycle Method | Purpose |
|-------|------------------------|---------|
| 1. Get IDs | `getIds` | Select records to process |
| 2. Process each | `updateRecord` | Process one record, build TransactionData |
| 3. Post-commit | `postUpdateRequest` | Post-authorise actions per record |

### Key Applications

| Application | Purpose |
|------------|---------|
| `COB.SERVICE` | COB service definition (ROUTINE, FREQUENCY, etc.) |
| `COB.PROCESS` | Current COB run status |
| `COB.PARAM` | COB parameters (date, company, etc.) |
| `TSA.SERVICE` | Task Scheduling Architecture service |

### COB Service jBC Pattern

```basic
* COB routine called by COB.SERVICE framework
SUBROUTINE MYBANK.COB.PROCESS.SERVICE

    $INSERT I_COMMON
    $INSERT I_EQUATE

    IF EB.INITIAL.CALL THEN
        * Runs once at start of service — open files, initialise
        FN.MY.APP = 'F.MY.APPLICATION'
        F.MY.APP  = ''
        CALL OPF(FN.MY.APP, F.MY.APP)
    END ELSE
        * Runs once per record selected by COB.SERVICE
        GOSUB PROCESS.RECORD
    END
    RETURN
```

---

## ATM / Teller Framework

**Purpose**: Cash management, denomination handling, teller operations, ATM interface.

### Key Applications

| Application | Purpose |
|------------|---------|
| `TT.CONTRACT` | Teller transaction/contract |
| `TT.TELLER` | Teller session record |
| `TT.DENOMINATION` | Cash denomination configuration |
| `TT.BRANCH.LIMIT` | Branch-level cash limit |
| `TT.RECON` | Teller end-of-day reconciliation |
| `TT.STOCK` | Cash stock/vault management |

### ATM Integration Layer

T24 ATM connects via FHM (Front-end Host Message) adapters using ISO 8583 message format. Integration JARs include:

| JAR | Adapter |
|-----|---------|
| `CAATMD_CardtronicsFHM.jar` | Cardtronics ATM adapter |
| `CAATMI_EverlinkFHM.jar` | Everlink ATM adapter |
| `CAATMI_ISOListener.jar` | Generic ISO 8583 listener |

### Denomination Handling

Cash denominations are defined in `TT.DENOMINATION`. Teller operations compute denomination counts for withdrawals/deposits using configured note/coin denominations per currency.

### Java Customization

Teller applications use standard `RecordLifecycle` hooks. Bind your hook class to `TT.CONTRACT,VERSION.NAME` in the VERSION record.
