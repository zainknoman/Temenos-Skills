# IRIS (Interaction Framework) Provider & Publisher APIs

**Source (authoritative):** Temenos *IRIS R18 User Guide* (`docs/TCIB-IRIS/`), pp. 4–54 and
114–119. Supporting: *Temenos UXP IRIS Integration Guide*, *TAFJ-Eclipse-debugging-T24-JBC-Invoked-via-IRIS*.
IRIS is not present in the `C:\R25` install scanned for this project. Nothing below is checked
against a runtime: confirm the IRIS version on the target before generating.

## Architecture (guide p. 4)

IRIS is a REST layer that talks to T24 in **OFS message format**, so one API works across
releases. Its components:

| Layer | Role |
|-------|------|
| **Provider API** | REST APIs over T24 artefacts. Each is driven by an **inventory** that maps it to an ENQUIRY (read) or VERSION (write) |
| **Published API** | Maps provider APIs to external/standard formats (e.g. PSD2) |
| Connectors | TAFC / TAFJ connectivity |
| Consent management | Access control on API requests |
| Service catalogue | Swagger docs: `<base>/api/v1.0.0/meta/apidocs` (filter `?resource=` / `?tag=`) |
| Apache Camel | REST endpoints, routing, transformation (Spring XML camel contexts) |

## 1. Prepare the T24 artefacts (guide pp. 16–17) — mandatory rules

| Rule | Enquiry | Version |
|------|---------|---------|
| ID naming (semantic version suffix) | `PZ.API.<RESOURCE>.<SUBRESOURCE>.1.0.0` e.g. `PZ.API.ACCOUNTS.BALANCES.1.0.0` | `<APP>,<PFX>.API.<NAME>.1.0.0` e.g. `FUNDS.TRANSFER,AC.API.CREATE.TRANSFER.1.0.0` |
| Data type per field | `FIELD.DISP.TYPE` | `ATTRIBS` |
| Operation name (`verbResource`, e.g. `getAccountBalances`, `createAccountTransfer`) | `DESCRIPT` | `DESCRIPTION` |
| JSON labels from the Temenos vocabulary | `FIELD.LABEL` / `SEL.LABEL` in API style | `TEXT` |

Fields default to alphanumeric unless typed Date or Amount. Amounts and dates must be
**unformatted** (`20170123`, `1234.56`). Mapping: ALPHANUMERIC → `string`, AMOUNT → `number`.
API enquiries must not use header fields, static labels or drill-downs. Remove `HEADER`,
literal `OPERATION` columns, and `ENQUIRY.NAME`/`SEL.CRIT`/`LABEL.FIELD`/`NXT.DESC`.
Set `ATTRIBS` to `''`.

Every field named on these records must still pass the Field Verification Gate
(`validate_fields.py --app ENQUIRY` / `--app VERSION`).

## 2. Build the projects (guide pp. 18–36)

```bash
# Service container (hosts the Camel runtime + T24 connectivity)
mvn archetype:generate -DarchetypeGroupId=com.temenos.irf \
  -DarchetypeArtifactId=irf-service-container-archetype -DarchetypeVersion=1.0 \
  -DgroupId=<group> -DartifactId=<name>-container -Dpackage=<pkg> -Dversion=<ver>

# Service project (holds one or more provider/published APIs)
mvn archetype:generate -DarchetypeGroupId=com.temenos.irf \
  -DarchetypeArtifactId=irf-service-archetype -DarchetypeVersion=1.0 \
  -DgroupId=<group> -DartifactId=<name>-api -Dpackage=<pkg> -Dversion=<ver>
```

Then reference the service project in the container's `pom.xml`, `mvn clean install`, and run
`jetty:run` (container check: `http://localhost:8080/api/v1.0.0/meta/apis`).

## 3. Create a Provider API (Workbench, guide pp. 25–36)

1. *APIs > Create Provider API*. Set the group/key, title and version.
2. Pick the artefacts. Each one becomes an endpoint with a proposed URL and operation.
3. **VERSION:** set only the HTTP method. The payload comes from the T24 model.
   `POST` creates, `PUT` amends, `GET` views, `DELETE` removes.
   **ENQUIRY:** map each URL path/query parameter to an enquiry selection field. Several
   parameters may map to one field (`fromDate` + `toDate` → `valueDate`).
4. Review, then *Finish*. The download zip holds the **swagger spec, Camel routes, mappings and
   mock responses**. Extract it into the service project's `src/main/resources/services` and
   `mvn clean install`.

The inventory (`*-inventory.json`) is the source of truth. Swagger and routes are **generated**
from it. Change the inventory or the T24 artefact and regenerate, rather than hand-editing
generated routes. Bulk path: the *RIM Importer* (`-i` builds the inventory from a CSV of APIs,
`-s` generates the Camel service context; pp. 75–88).

Generated route files contain T24 processor beans and route properties (the enquiry/version
target, selections, function). Their exact names depend on the IRIS version and **are not
documented in the guide**. Take them from the Workbench output for the target release; never
write them from memory or copy them from another project.

## 4. Published API → Provider API (guide pp. 51–54)

Import the publisher swagger (*APIs > Import API Definition*), generate, and wire each published
route to the provider route with Camel `direct-vm`. `direct-vm` finds routes in every
CamelContext in the same JVM:

```xml
<rest path="/v1.0.0/published" produces="application/json" id="published.service.restlet">
  <get uri="/payments/{accountid}/statusreport" id="PublishedPaymentStatusReport">
    <param name="accountid" type="path" required="true"/>
    <to uri="direct:published.PublishedPaymentStatusReport"/>
  </get>
</rest>
<route id="direct.published.PublishedPaymentStatusReport">
  <from uri="direct:published.PublishedPaymentStatusReport"/>
  <to uri="direct-vm:order-PSD2.getPaymentTransferList"/>   <!-- provider route -->
  <process ref="FTStatusReportResponseMapper"/>             <!-- Java bean: provider JSON -> published JSON -->
</route>
```

Request/response mappers are Spring beans (`<bean id="..." class="..."/>` declared before the
`camelContext`) holding the Java transformation code.

## 5. Security (guide p. 46)

Token validation runs as a Spring Security filter. The authenticated principal
(`IRISAuthenticatedUser`, held in the `SecurityContext`) is available to the IRIS version and
enquiry processors. Do not pass T24 credentials in API payloads or headers as a design
default. Configure them through the container's connectivity/security setup.

## Checklist before handing over an IRIS API

- [ ] Enquiry id `PZ.API.*.<semver>` / version id `<APP>,<X>.API.*.<semver>`
- [ ] Every column/field typed (`FIELD.DISP.TYPE` / `ATTRIBS`); amounts and dates unformatted
- [ ] Operation name in `DESCRIPT`/`DESCRIPTION` follows `verbResource`
- [ ] Labels come from the standard vocabulary
- [ ] Routes/swagger regenerated from the inventory, not hand-edited
- [ ] Published routes reach provider routes via `direct-vm`
