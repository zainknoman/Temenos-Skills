# Temenos Packager (DSF Packager) Reference

Sources, in order of authority:

1. **The R25 install at `C:\R25` (read-only).** It runs Temenos Packager **25.0.2**:
   `jboss-eap-8.1/standalone/deployments/dsf-iris.war` and `dsf-transact.war`
   (`META-INF/maven/com.temenos.dsf.dev-tools/dsf-iris-container/pom.properties`).
   Property names and data-structure files below marked **(R25)** were read from those WARs.
2. **The Temenos course "Transact Temenos Packager"** (course code TRxDSPAC, certification T3TTP),
   in two parts: **Foundation** and **Advanced**. They were OCR'd from slide screenshots by
   `pipeline/docx_extract.py` on 2026-11-23 into `docs/T3TTP/`. Page N of each PDF is slide N.
   References below are written `P1 s.27` (Part 1 / Foundation, slide 27) and `P2 s.232`
   (Part 2 / Advanced, slide 232).
3. **A clearer but incomplete copy of Foundation lessons 1.1-1.31** (`R00.TR1DSPAC`, 136 slides plus
   a few typed notes), indexed as `docs/T3TTP/T3TTP Packaging Part 1 Lessons 1.1-1.12.pdf`. Use it to
   read Part 1 slides whose OCR is poor. It is a cross-check only, not a full source.

For anything not summarised here, search the course:

```
py -3 pipeline/query_docs.py "<question>" --topic T3TTP -n 5
```

The course slides were screenshots, and small-font table text OCR'd badly. When a detail matters
(an API path, a property name), open the PDF page cited here and read the slide image.

---

## 1. What it is

Temenos Packager moves Transact **configuration** (and L3 **code**) through the SDLC, from DEV to
SIT, UAT and PROD, with source control and DevOps tooling (P1 s.3-6).

- **DDL-like data**: LOCAL.REF.TABLE, EB.TABLE.DEFINITION, FILE.CONTROL, STANDARD.SELECTION.
- **DML-like data**: ENQUIRY, VERSION and other configuration records.
- Every data record is stored as **JSON** in the package (P1 s.47).
- It is the successor of the **Design Studio Packager** (DSL/ESON-based, see
  `TAFJ-DSPackageInstaller.pdf` in `docs/TAFJ-Migration/`).

| Feature | Design Studio Packager | Temenos Packager |
|---|---|---|
| Workspace | models + models-gen + data-code + packager projects; n projects per package | 1 project = 1 package |
| Data records | DSL + data ESON | JSON |
| Build | XText indexing, slow | fast, optional Transact validation |
| Ad-hoc packages | limited | pre/post actions, field-level updates |
| Atomicity | only with EDP mode | supported |
| Package dependencies, workspace-T24 sync | not supported | supported |
| Incremental deployment | limited | supported |

(P1 s.7)

## 2. Components and install

Temenos Packager is module **Temenos Packager**, product code **TMNPACK**, available from
**Transact R19 AMR** onwards (P1 s.7). Artefacts that must be deployed in the application server:

| Artefact | Role |
|---|---|
| `dsf-iris.war` | Packager API server ("IRIS"). Package build, validate, deploy, inspect APIs |
| `dsf-transact-[version].war` (`dsf-transact-jms-[version].war` when dsf-iris is not in the same app server as Transact) | Transact connector; ships the data-structure definitions |
| `irf-t24catalog-services.war` | Transact catalog services |
| `t24-EB_CatalogService-ejb.jar` | Catalog EJB |
| `TAFJJEE_EAR.ear` | TAFJ runtime |
| `dsf-uxp.war` | Temenos Workbench web UI (package manager) |
| `dsf-m2repo-*.zip` | Maven repository with the DSF archetypes, for CLI and IDE mode |
| `dsf-p2repo-*.zip` | Eclipse/Design Studio plugin update site, for IDE mode |
| `dsf-encryption-tool.zip` | Password encryption (`encrypt.bat` / `encrypt.sh <password>`) (P2 s.10-12) |

**R25 fact:** `C:\R25` deploys `dsf-iris.war` and `dsf-transact.war` only. No `dsf-uxp.war` or
`irf-t24catalog-services.war` is in that deployments folder, so the Workbench web mode is not
installed there.

**Health check** (P1 s.7, P2 s.26-29):

```
GET http://localhost:9089/dsf-iris/api/v1.0.0/meta/api/health
GET .../meta/api/health?verbose=true&capabilityBootstrapDependency=true
```

`status` is UP or DOWN. `checks` lists capabilities, split into core and extension. Verbose mode adds
the bootstrap deployment status, capability metadata (for configservice: description,
groupIdPrefix, types) and per-package `name` / `deployed` / `version`. Both query parameters
default to false.

**IDE mode setup** (P1 s.10-12, s.36, s.87):

- Unzip `dsf-m2repo` and use it as the local Maven repository in `settings.xml`.
- For code packaging, set the properties `tafjHome` and `t24Lib` in the IDE's `settings.xml`.
- Register the archetype catalogue in Eclipse Maven settings. The slides name it both
  `dsf-archetype-catalog.xml` and `archetype-catalog.xml`, at the root of `dsf-m2repo`.
- Install the plugin from `dsf-p2repo` via Help > Install New Software.
- After the first package, edit `dsf-connection.json` in the generated `dsf-server` project:
  the dsf-iris URL (HTTP by default), active connection name, release (for example R24) (P1 s.38, P2 s.179).

## 3. Application-server configuration (P2 s.4-18)

| What | Where | Notes |
|---|---|---|
| JMS user and queues | `jms.properties`, externalised from `dsf-iris.war` | Default credential is the INPUTT user |
| Changing the Transact credential | create a Transact user (for example copy INPUTT), update `connection.properties` in `dsf-transact-jms.war`, create the app-server user with role `t24user` (needed by `irf-t24catalog-services`) | Encrypt the password with the encryption tool |
| Logging | `log4j.properties` in `dsf-uxp.war` and `dsf-transact-jms.war` (WEB-INF/classes) | INFO by default; set DEBUG to troubleshoot. R25 ships `log4j2.properties` |
| Logs to read | `dsf-iris.log` (deploy result, per-record time, the request uuid), `dsf-package.log` (released packages) | P1 s.63-66 |
| Company for INT records | system property `dsf.package.t24data.allowCompany` = list of INT applications, set in the startup script, then restart | Use it for INT applications whose ID needs a company, where ID.COMPANY must match the current company (P2 s.15-18) |
| Package repository | `-Ddsfconfig.dsfFile.com.temenos.dsf.packagedef=%NITRITE_HOME%/dsf.db` in the JBoss startup script | See §9 |
| User variables | system properties in `setenv.bat`, then restart JBoss | See §8 |

### Properties in `dsf-iris.war` `WEB-INF/classes/dsf.properties` (R25, verbatim)

```properties
dsf.package.ofs.chunksize=500
dsf.package.ofs.bulkSize=500
dsf.package.ignoreFluReEntrantErrors=true
dsf.package.ignoreAllActionErrors=false
dsf.package.skipCsvAdvancedValidations=false
dsf.package.skipPackageDuplicateCheck=false
dsf.packager.csoldformat.groupIdPrefixes=com.temenos.irf.api.extensions,com.temenos.payments
dsf.packager.t24data.notransactiontypes=EB.TABLE.DEFINITION;LOCAL.TABLE;LOCAL.REF.TABLE
dsf.package.dupRecordsCheck.versions=all
dsf.package.skipPhaseIfErrors=main,post
```

- `notransactiontypes`: these applications are never deployed in single-transaction (OFS bulk) mode.
- `skipPackageDuplicateCheck`: the R25 default is **false**. The course shows it set to true in a
  test area so that an already-deployed package can be redeployed (P2 s.161, s.286). The course
  narration also calls it `disableDuplicateChecks` / `-Ddsf.disableDuplicateChecks=Yes`. The
  R25 file name is the one to use.
- `dsf.package.product.threadpool.size`: number of components deployed in parallel. When unset,
  the number of available threads is used (P2 s.295). Not present in the R25 file.

`dsf-transact.war` `WEB-INF/classes/dsf.transact.properties` (R25) holds, among others,
`dsf.json.noinput.fields.<APP>=<fields|*>` (fields the packager never inputs, for example
`VERSION=TABLE.LINE,TABLE.COLUMN,MULTI.POSSIBLE,LOCAL.REF.FIELD`), `dsf.cli.enableINAUrecord=false`,
`dsf.package.ofs.companyAppChunks=20`, `dsf.package.t24data.processValidFieldsOnly=true` and
`dsf.package.knownActionErrors.t24data=...` (action errors treated as known).

## 4. Package anatomy

A package is a Maven project (P1 s.38):

```
<package>/
  src/t-package.json      package definition and contents list (no record bodies)
  src/data/<folder>/      one JSON file per data record
  pom.xml                 build and/or validate the package in CI
```

- Record file name: `<component>.<APPLICATION>!<ID>.json`, for example
  `t24data.ENQUIRY!CUSTOMER.LIMITS.SCV.json`. A field-level update adds `!<FLU-ID>`:
  `t24data.PW.PROCESS.DEFINITION!ACCOUNT.OPENING!DEMOFLU.json` (P2 s.42, s.202).
- Record JSON has a `header` (for example `dsfApiType: Table`, component `t24data`, an
  `installed` flag) and a `body` with the field values. `installed` is NO on import and becomes
  YES only after a successful deployment (P2 s.204).
- Package definition: name, semantic version (1.0.0 by default), description, status
  **DEFINING** or **FINAL**. FINAL disables the package: no more edits (P1 s.19, P2 s.148).
- The package name may not contain an underscore (P2 s.145). Copying a package to a version that
  exists is refused with "Next available version is ..." (P2 s.149-150).
- Built output is a zip (or a jar inside a multi-package zip), for example
  `PracticeWebPackage-1.0.0.zip`. The downloaded zip is what moves to the target environment.
- The default record folder is `src\data`. A folder name containing a backslash creates a sub-folder.
  The Company field appears only for some applications (see `allowCompany` in §3).

The JSON body uses the Transact field names as they appear on screen (for example
`FIXED.SELECTION`, `MANDATORY.FIELD`). Layer A stores the EQU names with the application prefix
(`ENQ.FIXED.SELECTION`). See §12 for the verified names.

## 5. Creating packages: three modes

| Mode | Tool | Typical use |
|---|---|---|
| **Web** | Temenos Workbench > Package Manager > Packages (`http://localhost:5000/...` in the course) | Business analysts, ad-hoc packages, DEV/SIT |
| **CLI** | Maven + a CSV file | Scripted creation |
| **IDE** | Eclipse or Design Studio with the DSF plugin and archetypes | Developers working with Git |

### Web mode (P1 s.16-25, s.49-59)

1. Package Manager > Add Package. Fill the Definition tab (Content and Sequence tabs appear only
   once the mandatory fields are filled and a record is added, P2 s.146-147).
2. Content tab > Add Data Record: component (default Configuration / `t24data`), type
   (application), ID, optional company and folder.
3. Save, then Validate or Deploy, or Download the zip. Deploy always runs validation first.

Other actions: edit (changes only the record **ID**, not its content), delete one or many records,
search existing records with Package Search, import records from a CSV file (More Options > Import
Data Records from CSV).

**Sequence tab.** The packager retries records that fail on a dependency, so a sequence is optional,
but a custom sequence makes deployment faster. Define it per data record or per application
(component + type), and reorder with Move Up / Move Down (P1 s.52-53). Recommended T24 sequence,
to adapt per package: PGM.FILE, FILE.CONTROL, STANDARD.SELECTION, LOCAL.TABLE, LOCAL.REF.TABLE,
EB.TABLE.DATA.TYPE, EB.TABLE.DEFINITION, EB.API, EB.TABLE.PROCEDURE, AA.CLASS.TYPE,
AA.CLASS.DEFINITION, BATCH, LANGUAGE, EB.RULES, EB.RULE.GATEWAY (P1 s.53).

### CSV formats (P1 s.27-28, s.53, P2 s.71, s.112)

CLI CSV:

```
package_name,package_version,package_description,dependencies     <- first line
package_name#package_version#DEPLOY|BUILD                           <- dependency syntax, default DEPLOY
t24data,ENQUIRY,%CATEGORY                                           <- component,type,ID[,company]
t24data,CURRENCY,AUD
```

Web/IDE import CSV columns:

| Col | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| | Component | Type | Record ID | Company | Folder | Data Structure (Y/N) | Custom Data Structure | Phase | Action |

- F=Y and G empty: use the default data structure, which also imports its dependencies.
- F empty or N and G=name: use a custom data structure. F and G empty: plain record.
- When F or G is used, column I (Action) must be empty. For AA applications, Action is only PR,
  PB or PP.
- Import fails on duplicate rows ("The CSV has duplicate records") and on folder names that differ
  only by case (P2 s.153-154).

### CLI mode (P1 s.26-34)

Prerequisites: `dsf-m2repo` unzipped into the Maven repository, `dsf-iris.war` and Transact running.
Default API server: `http://localhost:9089/dsf-iris`. Edit the provided `pom.xml`: argument 1 is
the CSV folder, argument 2 the output folder, and set the groupId. Then run Maven from that
folder (`mvn -version` checks Maven is on the PATH). The package zip lands in the output folder.

```
mvn -Ddsf.iris18.host=http://localhost:9089/dsf-iris -Dmaven.repo.local=<t24-binaries or m2repo> -f ./pom.xml test
```

### IDE mode (P1 s.35-45, P2 s.178-204)

- File > New > Project > Maven Project, untick "Create a simple project", pick the DSF Packager
  catalogue and archetype **`dsf-package-archetype`**. Or File > Import an existing package zip.
- Opening `t-package.json` the first time creates the `dsf-server` project.
- Context menu **Temenos Workbench**:
  - **Import Temenos Transact Data Record (JSON)**: pick application, record ID (content assist),
    optional country/company and Duplicate Of. Wildcards: `*` all records, `AA*` begins with,
    `*AA` ends with. A `*` in the middle is literal. Existing files are overwritten.
  - **Reload Data Record(s)**: replace the file with the Transact record.
  - **Reload Data Record(s)...**: same, but keeps custom tags and user/system variables
    (checkboxes "Retain Custom tags", "Retain Placeholders").
  - **Deploy Data Records**: deploy one JSON file or a whole folder. Failures appear red in the
    report, the Problems view and the Workbench Deployment console.
- **Synchronization** (IDE only): Check Sync compares workspace and Transact. Records show RIGHT
  (in sync) or CROSSED. Sync per package or per record, Product to Workspace or Workspace to
  Product. Uses: switching environment, pulling Screen Designer changes into the workspace,
  deploying only the records other developers changed in Git (P2 s.169-177, s.209-212).

## 6. Deploying packages

Ways to deploy: **API** (any environment, mainly UAT/PROD by DevOps), **CLI/Maven**, **IDE**,
**Workbench** (should not be used in PROD) (P1 s.63).

### Modes

| Mode | Behaviour |
|---|---|
| Full | All records input and validated |
| Incremental hash (`incremental=hash`) | Only records whose hash changed since the last deployment of the package |
| Incremental file (`incremental-file=<file>`) | Only the records listed in a text file, sent as form-data, not as a query parameter |

| Transaction mode | Behaviour | Retry |
|---|---|---|
| Single (`transactionMode=single`) | Records sent as one OFS bulk per company and phase | Resends all records, successes first, until all succeed or the same failure repeats |
| No transaction (`transactionMode=without`) | Records sent one by one | Resends only the failed records |

The course recommends **no transaction** for now. Single transaction suits low volumes with no
dependencies between chunks, and most products do not support OFS bulk (P2 s.229-230).

Defaults (P2 s.232):

| Deploy mode | Retry | Transaction | Incremental |
|---|---|---|---|
| curl / API | true (`retry=false` to turn off) | no transaction (`transactionMode=single` to change) | full (`incremental=hash` to change) |
| Web, import package from zip | true | no transaction | full |
| Web, package deploy | true | user chooses | full |

The CLI table (P1 s.67) lists `-Ddsf.transactionMode` default **single**, which contradicts the
API default above. Pass the mode explicitly in scripts.

### API (dsf-iris)

Base: `http://localhost:9089/dsf-iris/api/v1.0.0/meta/dsfpackages` (P1 s.64, P2 s.250-292)

| Purpose | Call |
|---|---|
| List packages | `GET /` |
| Validate a zip/jar | `POST /validate?retry=true&incremental=hash` |
| Deploy a zip/jar | `POST /deploy?transactionMode=without&retry=true&incremental=hash` |
| Download a package | `PUT /{packageId}/download` |
| Deploy a multi-package zip | `POST /multiPackageDeploy` with headers `retry:true` and `multipackageRetry:true` |
| Inspect (post-deployment check) | `POST /inspect` |
| Record hash status / refresh | `GET` / `PUT /packageRecordHash?packages=<name>-<version>` |
| Check an async deployment | `GET /checkDeploy/{deployId}` |
| Async deploy (V4) | `POST http://localhost:9089/dsf-iris/api/v4.0.0/meta/dsfpackages/deploy?async=true` |

```
curl -X POST -L -F "package=@PaymentScreen-1.0.0.zip;type=application/zip" \
  "http://localhost:9089/dsf-iris/api/v1.0.0/meta/dsfpackages/deploy?retry=false"
```

### CLI (Maven) (P1 s.67-69, s.78-80)

```
mvn clean install -Ddsf.iris18.host=http://localhost:9089/dsf-iris \
  -Dmaven.repo.local=<m2repo> -Ddsf.command=deploy -Ddsf.tenant.id=<tenant-id> -f pom.xml
```

| Parameter | Default |
|---|---|
| `-Ddsf.command=deploy\|validate` | validate |
| `-Ddsf.retry=true\|false` | true |
| `-Ddsf.transactionMode=single\|without` | single (see the contradiction above) |
| `-Ddsf.incremental=hash` | not set, full deployment |
| `-Ddsf.incremental-file=<path>` | not set |
| `-Ddsf.tenant.id=<tenant-id>` | not set |

The package `pom.xml` runs main class `com.temenos.dsf.packager.PackageInstaller` with the built
zip as argument. Adding the argument `validateOnly` makes it validate only.

### Verifying a deployment

- Transact table **DS.DSF.PACKAGE**: one record per `<package>-<version>` with the user, the date
  and the deployed records. Since the Packager Repository (§9) this table is the **audit**
  repository only.
- `dsf-iris.log`: per-record result, total time, and a uuid on every line of one request, so
  concurrent deployments can be told apart (P2 s.299).

## 7. Advanced packaging features (Part 2)

### Field-level update (FLU) (P2 s.32-55)

Deploys only a field change, not the whole record. Use it for sensitive tables shared by teams.
In Web mode: Content > Add Field Level Update. Three tabs:

- **FIELD**: application, record ID and a unique FLU ID (upper case and dots).
- **SELECTOR**: up to three levels. Selector 1 is a top attribute or a multi-value group. Selector 2
  is a multi-value attribute or a sub-value group. Selector 3 is a sub-value attribute
  (value-equals only). Each level takes a condition such as position-equals.
- **OPERATION**: the allowed actions depend on the last filled selector.
  Top attribute: SET, DELETE. MV/SV group: INSERT-AFTER, DELETE, REPLACE. MV/SV attribute: SET,
  DELETE. "IMPORT VALUE FROM T24" loads the current value as editable JSON.

Course examples: insert a new `PROCESS.ACTIVITY` / `ACTIVITY.STATUS` set after position 1 of the
`ALLOWED.STATUS` group in PW.PROCESS.DEFINITION ACCOUNT.OPENING, and insert DEBIT.AMOUNT after
position 2 of `MANDATORY.FIELD` in VERSION FUNDS.TRANSFER,AC.

### Package dependencies (P2 s.56-62)

Definition tab > Add new Package: package plus version. **Build and Deploy** (default) means the
dependency must be referenced at Maven build time. An `x` in the version then needs an explicit
version at build. **Deploy Only** is checked at deployment only. The course says both behave the
same for now. Deployment fails with "Missing package dependency" until the dependency is deployed.
Keep business streams isolated, plus one common package for shared configuration, because complex
dependency graphs make the SDLC hard.

### Data structures (P2 s.63-102)

Add a whole object with its dependencies in one step (choose a Data Structure when adding a record,
or column F/G in the CSV). Structures can nest, a parent can block nested structures at level 1, and
one application can have several structures.

Shipped structures **(R25)**, in `dsf-transact.war` > `dsf-packages/t24data-datastructures-25.0.2.jar`
> `src/data/datastructures/dsfpkg.datastructure!<name>.json`:

| File | Object | `filterOnlyLocal` |
|---|---|---|
| `t24data_version` | VERSION with associated, next, confirm and preview versions, drop-down enquiries, EB.API routines | true |
| `t24data_aa` | AA product with its conditions | not set |
| `t24data_pwd` / `t24data_pwa` / `t24data_pwt` | Process workflow definition / activity / transition | true / not set / not set |
| `t24data_menu` / `t24data_mainmenu` | HELPTEXT.MENU and main menu, loading the applications, enquiries, versions, composite screens and workflows it points to | true |
| `t24data_tabscreen` | Tabbed screen | true |
| `t24data_cos` / `t24data_uxpbcos` | Composite screen / UXP browser composite screen | true |
| `t24data_ebmapping` | EB mapping | not set |
| `local_records_patterns` | L3 filters: VERSION `.*(,BANK\.).*`, ENQUIRY `BANK.*` | n/a |

- **`filterOnlyLocal: true`** loads only L3 (local) dependents, matched by the patterns in
  `local_records_patterns.json`. Core model-bank records are skipped. The course tells you to set it
  to false to fetch model-bank records (P2 s.66). Only one patterns file exists at runtime. Edit it,
  then redeploy the WAR.
- **Regex extraction**: a model entry can carry `"id-value"`. For example VERSION `NEXT.VERSION`
  uses `([^\s]+)` to keep only the version name when the field holds extra parameters.

### Pre/post actions (P2 s.103-121)

Each record can carry a **Phase** (pre or post) and an **Action**, automating what used to be manual
installation steps:

| Code | Action | Applies to |
|---|---|---|
| D | Delete the record | non-AA |
| R | Reverse (OFS) | application or version records |
| H | Restore from history | non-AA |
| HLD | Put the record in IHLD | non-AA |
| PR / PB / PP | Proof / Publish / Proof and publish | AA products (AA.PRODUCT.MANAGER) |

Order at validation and deployment: pre, main, post, each with the same sequence. Within a phase,
non-company records go first, then company-specific ones. Failures retry within their own phase.
`dsf.package.skipPhaseIfErrors=main,post` (R25) stops later phases when an earlier one fails.

### User and system variables (P2 s.123-142)

Placeholders in field values and in record IDs, resolved at deployment:

| Kind | Syntax | Source |
|---|---|---|
| System (Transact) | `"!SYSTEM.TODAY!"` | Application EB.SYSTEM.VARIABLES. Examples: SYSTEM.COMPANY, SYSTEM.MNEMONIC, SYSTEM.NEXT.WORKING.DAY, SYSTEM.PREV.WORKING.DAY, SYSTEM.TODAY, the local currency, UTC time |
| DSF system | `${DSF.TODAY}` | DATES record of the company. Format YYYYMMDD. Change it for the system with `-Ddsf.package.record.dateformat=yyyymmdd` in `dsf.properties`, or per field with `${DSF.TODAY\|yyyy-MM-dd'T'HH:mm:ss.SSSZ}` |
| User | `${USER.PATH}`, or with a default `${SERVER.URL\|DEFAULT.VALUE}` | A system property in `setenv.bat` (restart JBoss). If missing, deployment fails with "Unable to resolve user variable" |

Example from the course: OFS.SOURCE FT.BULK with `IN.QUEUE.DIR` = user variable + company ID.
IF.INTEGRATION.SERVICE.PARAM with the destination queue prefixed by the company mnemonic.

### Validations (P2 s.143-161)

- **Design**: name format, FINAL warning, duplicate version on copy, duplicate record in a package,
  CSV duplicates and folder case.
- **Deploy**: a package is refused if any record was already deployed by **another** package
  (for example VERSION PAYMENT.ORDER,BULK in two packages). Redeploying the same package with a
  new version is allowed. Controlled by `dsf.package.skipPackageDuplicateCheck` and
  `dsf.package.dupRecordsCheck.versions`.

## 8. Multi-package, async and scalable deployment (P2 s.233-307)

- **Multi-package**: build each package with Maven (`Run As > Maven install` gives a
  `-SNAPSHOT.jar`), create a project from **`dsf-multi-package-archetype`**, list the packages in
  `module/pom.xml` (publishes the jars to the local repo), list them again as dependencies in the
  root `pom.xml` (builds one zip), then `POST /multiPackageDeploy`. `retry` works per package,
  `multipackageRetry` retries all failed records across packages until the error count stops falling.
  Circular dependencies are covered.
- **Async (V4)**: `POST .../api/v4.0.0/meta/dsfpackages/deploy?async=true` returns a `deployId`.
  `GET .../v1.0.0/meta/dsfpackages/checkDeploy/{deployId}` returns status InProgress, Success or
  Failure, with `totalRecords`, `extensions` (t24data, tapdata, fcmdata, ...), `transactionType`,
  `errorRecords`, `errors`, and for multi-package `totalPackages`, `errorPackages`, `retries`.
- **Scalable deployment**: dependent packages deploy in sequence, independent ones in parallel.
  Thread count: `dsf.package.product.threadpool.size`.

## 9. Package repository (P2 s.19-24)

The repository of package definitions is now product-agnostic:

- **DSF ConfigService**: Nitrite DB (NoSQL in one file), for simple setups and developers.
  Configured in the JBoss startup script with
  `-Ddsfconfig.dsfFile.com.temenos.dsf.packagedef=%NITRITE_HOME%/dsf.db`.
- **Config microservice**: for scaled or cloud setups.
- Transact's DS.DSF.PACKAGE stays as the audit trail.
- There is one repository per environment, active by default and used by every deployment.

APIs, base `http://localhost:9089/dsf-iris/api/v2.0.0`:

| API | URI |
|---|---|
| packagedef search (GET) | `/meta/dsfpackages` |
| packagedef GET / POST / PUT / DELETE | `/system/configurationGroups/{groupId}/configuration/{configName}` |

## 10. Post- and pre-deployment checks (P2 s.273-284)

- `POST /inspect` compares a package (or multi-package) with the target. Response: `synchronized`,
  `totalRecords`, `syncRecords`, `notInSyncRecords`, `undefinedRecords` (application or record
  not found), and per record `inSync` / `notInSync` (with `diffText`: `op` remove/replace,
  `path`, `value`) / `undefined`. With incremental mode it checks only records whose hash differs.
- `GET /packageRecordHash?packages=payment-config-1.0.0` reports records whose product hash changed
  after a manual edit in Transact. `PUT` on the same URL sets the package hash to the product hash.
  Without a version, the latest version is used.

## 11. Code Packager: L3 jBC and Java (P1 s.85-103)

Builds a JAR of L3 routines from an IDE project. **IDE mode only** (Eclipse or Design Studio).
Java extensions are mandatory for new clients from R19, jBC is for existing clients upgrading.

| Archetype | Project |
|---|---|
| `dsf-package-parent-archetype` | Parent project. Create it first and run Maven install |
| `dsf-code-jbc-package-archetype` | jBC only. Sources in `src/main/jbc` |
| `dsf-code-java-package-archetype` | L3 Java only. Sources in `src/main/java`. Declare the L1/L2 JARs it uses as dependencies in `pom.xml` |
| `dsf-code-jbc-java-package-archetype` | jBC and Java together, typical for upgrading clients |
| `dsf-code-jbc-java-sample-archetype` | jBC + Java with sample code |

- Needs `tafjHome` and `t24Lib` in the IDE `settings.xml`.
- For jBC, copy `TemnCache-*.jar` from `TAFJ/ext/caching` into `TAFJ/lib` first (P1 s.93).
- Build with Run As > Maven install. The JAR lands in `target/` and is copied to the target
  application server.

For writing the routines themselves, use `temenos-jbc`, `temenos-infobasic` or `temenos-l3`.
For TAFJ compilation tooling (tCompile, Maven plugin), use `temenos-devsecops`.

## 12. Names checked against Layer A

The course and the R25 files mention these. Field names in packager JSON are screen names. Layer A
holds them with their EQU prefix. Checked in R23 and R25 on 2026-11-23:

| Application | Course name | Layer A name (R23 and R25) |
|---|---|---|
| PW.PROCESS.DEFINITION | ALLOWED.STATUS, PROCESS.ACTIVITY, ACTIVITY.STATUS | PW.DEF.ALLOWED.STATUS, PW.DEF.PROCESS.ACTIVITY, PW.DEF.ACTIVITY.STATUS |
| ENQUIRY | FIXED.SELECTION | ENQ.FIXED.SELECTION |
| HELPTEXT.MENU | APPLICATION | EB.MEN.APPLICATION |
| OFS.SOURCE | IN.QUEUE.DIR, LOG.FILE.DIR | OFS.SRC.IN.QUEUE.DIR, OFS.SRC.LOG.FILE.DIR |
| DE.PRODUCT | PRIORITY | DE.PRD.PRIORITY |

**No schema in Layer A** for VERSION, DS.DSF.PACKAGE, IF.INTEGRATION.SERVICE.PARAM, DATES and
LOCAL.REF.TABLE, in either release. Names such as VERSION MANDATORY.FIELD and NEXT.VERSION come
only from the course and from the R25 data-structure JSON. Do not use them in generated code
without asking. Applications that do have a schema: EB.SYSTEM.VARIABLES, EB.TABBED.SCREEN,
AA.PRODUCT.MANAGER, EB.TABLE.DEFINITION, LOCAL.TABLE, EB.COMPOSITE.SCREEN.

## 13. Best practices (P2 s.285-286)

- One naming convention and semantic versioning for packages. No duplicate records across
  packages. Use CSV import and wildcards to add records quickly.
- Write the package deployment order in the Implementation Guide.
- Put post-deployment steps in the package (pre/post actions, variables) instead of manual
  instructions.
- Keep the Temenos Workbench version in step with the Temenos Packager version.
- Eclipse plugin error about a missing bundle classpath JAR (`failureaccess`): restart with
  `eclipse.exe -clean` (P2 s.271-272).
