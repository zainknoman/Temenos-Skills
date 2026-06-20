# Arrangement Architecture (AA) — Reference

> Sources: JAR analysis (99 JARs, 2026-06-20) + PDF training materials (AACT1–AACT9, AA Common Building Blocks Implementation 2020 Q4, AA Retail Accounts Foundation R19).

---

## Overview

Arrangement Architecture (AA) is the core Temenos Transact framework for building and managing financial products across three product lines:

- **LENDING** — loans, mortgages, revolving credit, facilities
- **DEPOSITS** — term deposits, notice accounts, call deposits
- **ACCOUNTS** — current accounts, savings accounts, overdraft accounts

An **Arrangement** is an agreement between the bank and a customer to provide services associated with a **Product**. All arrangements are account-based: when a financial arrangement is created, Transact automatically generates a linked ACCOUNT record. Arrangements can only be updated via **Activities** — both online (user-initiated) and during Close of Business (COB/batch).

### AA Dependencies

AA requires the following Transact core modules:
- **CUSTOMER** — counterparty reference
- **ACCOUNT** — automatically created per arrangement; holds arrangement balances
- **Delivery (Accounting)** — generates accounting entries on authorisation
- **Limits** — for loans and overdraft accounts (optional; system generates override if absent)
- Static tables: COUNTRY, HOLIDAY, CURRENCY, CURRENCY.PARAM

---

## Product Hierarchy

```
Product Line  (e.g. LENDING, DEPOSITS, ACCOUNTS)
  └── Product Group  (e.g. Personal Loans, Current Accounts)
        └── Product  (specific product definition with conditions)
              └── Arrangement  (instance for a specific customer)
```

| Level | Defined By | Purpose |
|-------|-----------|---------|
| Product Line | Temenos (description only editable by client) | Highest level; contains reusable Business Components |
| Product Group | Client | Subset of Product Line; selects which Business Components (Properties) to include |
| Product | Client | Assigns values to Business Component fields (Product Conditions) |
| Arrangement | System + User negotiation | Customer-specific instance; holds Arrangement Conditions |

**Product Conditions** are the values assigned to Business Component fields at product level. They are stored in `AA.PRD.DES.<PROPERTY.CLASS>` applications.

**Arrangement Conditions** are the values at arrangement level — a copy of Product Conditions negotiated with the customer (where allowed by Negotiation Rules).

---

## Product Lifecycle: Proof and Publish

Products go through three stages before customer arrangements can be created:

1. **Design** — Attach Properties and Product Conditions using the Product Browser / Product Designer.
2. **Proof** — Validates the product configuration. Checks that all mandatory properties have conditions, no conflicts exist, currency conditions cover all allowed currencies. Sets the `AVAILABLE.DATE` and `EXPIRY.DATE`. Errors written to `PRODUCT.ERROR` field with `SUGGESTION` remediation hints. Proofed data stored in `AA.PRODUCT.PROOF` and `AA.PRD.PRF.<PROPERTY.CLASS>`.
3. **Publish** — Moves product to the Product Catalog. `AA.PRODUCT.PROOF` is deleted; `AA.PRODUCT.CATALOG` and `AA.PRD.CAT.<PROPERTY.CLASS>` are updated. Arrangements can only be created for published products.

**Key applications:**

| Application | Purpose |
|------------|---------|
| `AA.PRODUCT` | Product definition, properties, activities, proof/publish status |
| `AA.PRODUCT.MANAGER` | Manages proof/publish actions; PROCESS.METHOD = Online or Service |
| `AA.PRODUCT.PROOF` | Intermediate state during proofing |
| `AA.PRODUCT.CATALOG` | Published product catalog — source for new arrangements |
| `AA.PRD.PRF.<CLASS>` | Proofed product conditions |
| `AA.PRD.CAT.<CLASS>` | Published/cataloged product conditions |
| `AA.PRODUCT.CHILDREN` | List of child products under a parent |
| `AA.PUBLISH.SERVICE.LIST` | Queue for service-based publish |
| `AA.PUBLISH.SERVICE.MONITOR` | Enquiry for tracking publish status |

When proofing/publishing a parent product, the operation cascades to all child products.

---

## AA Configuration Tables (Core Setup)

### AA.PROPERTY.CLASS

Released by Temenos. Defines the available types of business components. Clients may only amend the description field.

**Key TYPE field values:**

| Type | Meaning |
|------|---------|
| `CURRENCY.SPECIFIC` | Product Conditions vary by currency (e.g. INTEREST, TERM.AMOUNT) |
| `CURRENCY.OPTIONAL` | Properties may or may not have a currency component |
| `DATED` | Product Conditions can vary by date; effective date included in record key |
| `MULTIPLE` | More than one property of this class can be defined per product |
| `MERGE` | Child condition does not blindly override parent condition |
| `FORWARD.DATED` | Allows new Activity charge definitions at arrangement level |
| `ARRANGEMENT` | Special arrangement-level processing; values not merged with previous amended values |
| `TRIGGER` | Property appears in arrangement after an Activity charge is triggered (e.g. CHARGE.OVERRIDE) |
| `VARIATION` | ID structure includes an additional component for AA.PRODUCT.VARIATION value (e.g. BRANCH, INTERNET, MOBILE) |
| `TRACKING.ONLY` | Values cannot be viewed or edited at arrangement level; always track product condition changes |

**DEL.INFO.REQD field**: When set to Y, this property class is included in the delivery handoff record for ACTIVITY.MESSAGING. Pre-configured by Temenos.

### AA.PROPERTY.CLASS.ACTION

Released by Temenos. Holds information on the actions that can be performed for each Property Class — including whether an action generates an accounting entry and which Product Line it belongs to. (Prior to R9, this was part of AA.PROPERTY.CLASS itself.)

### AA.PROPERTY

Client-created named instances (types) of a Property Class — known as Properties. Multiple properties of the same class can be used in one product if the class allows it (MULTIPLE type).

**PROPERTY.TYPE field values:** `Product only`, `Suspend`, `Suspend overdue`, `Residual`, `Variation`, `Forward dated`, `Rebated unamortised`, `Credit`, `Trigger`, `Commission`, `Accrual by bills`, or null.

A property is attached to a Product Group and is the link between the abstract Property Class and a specific product's use of that feature.

### AA.PRD.DES.\<Property Class\>

One application per Property Class. Holds the product conditions (field values for each component). The record ID structure is determined by the Property Class TYPE:

```
<CONDITION.NAME>[-CURRENCY][-VARIATION][-EFFECTIVE.DATE]

Examples:
  FIXED.RATE                        -- simple condition
  FIXED.RATE-USD                    -- currency-specific
  FIXED.INTEREST-GBP-BRANCH         -- currency + variation
  FIXED.RATE-USD--20181101          -- currency + effective date
  FIXED.INTEREST-GBP-BRANCH-20181101 -- currency + variation + date
```

**Negotiation Rules fields** in the Product Condition:

| Field | Purpose |
|-------|---------|
| `DEFAULT.NEGOTIABLE` | Mandatory. YES/NO — can all fields be negotiated at arrangement level |
| `DEFAULT.ATTR.OPTION` | RESETTING (reset from product on rollover/renewal) or NON-RESETTING (maintain arrangement-level values) |
| `NR.ATTRIBUTE` | Multi-value. Specific attribute for which a negotiation rule is defined |
| `NR.ATTRIBUTE.RULE` | Rule expression using ==, !=, <, <=, >, >=, AND, OR to pinpoint a specific MV/SV set |
| `NR.OPTION` | Negotiation type (e.g. RANGE, MAXIMUM, MAXIMUM.PERCENTAGE) |
| `NR.VALUE` | The negotiation constraint value |
| `NR.VALUE.SOURCE` | Dynamic source for NR.VALUE (format: `BALANCE.TYPE>BALANCENAME`) |
| `NR.MESSAGE` | Override/error message when negotiation rule violated |

### AA.PRODUCT (Published product record)

Holds the overall product definition including the list of attached properties, activities, proof/publish status, available date, last published date, and product version (increments by 0.1 per change action).

### AA.PRODUCT.CATALOG

The live product catalog. Created when a product is published. New arrangements fetch their initial conditions from `AA.PRD.CAT.<PROPERTY.CLASS>` records.

### AA.PRODUCT.VARIATION

Virtual table (maintained via EB.LOOKUP). Defines valid variation codes such as BRANCH, INTERNET, MOBILE, STAFF, FOREIGNER. Used with VARIATION type Property Classes.

### AA.CUSTOMER.ROLE

Defines customer roles for arrangements (e.g. Beneficial Owner, Guarantor, Beneficiary, Co-applicant). Used in the CUSTOMER property to classify each involved party.

### AA.OFFICER.ROLE

Virtual table (maintained via EB.LOOKUP). Defines valid roles for Other Officers (Application, Approval, Collection, Disbursement, etc.).

### AA.ACCRUAL.FREQUENCY

Defines the accrual frequency for charge/commission amortisation, used alongside ACCOUNTING product condition ACCRUE.PERIOD settings.

---

## Property Classes

### CUSTOMER (mandatory — Lending, Deposits, Accounts)

Used to specify the involved parties of an arrangement and their respective roles. Primarily an arrangement-level class — typically configured as fully negotiable. Customer Property cannot be set as Tracking and it is Dated.

**Key characteristics:**
- At least one Beneficial Owner is mandatory per arrangement
- Multiple beneficial owners supported; first owner used for accounting, tax, and limits
- Owner change possible via `<PRODUCT.LINE>-CHANGE-CUSTOMER` activity class
- Customer automatically defaulted as owner when arrangement is validated

**Customer Role fields (in AA.CUSTOMER.ROLE):**

| Field | Purpose |
|-------|---------|
| `BENEFICIAL.OWNER` | Whether customer is a beneficial owner (YES/NO) |
| `TAXABLE.CUSTOMER` | Whether the customer is subject to tax |
| `MAXIMUM.TAX.LIABILITY.PERCENT` | Max tax liability % for taxable customers (R16+) |
| `LIMIT.CUSTOMER` | Whether this role requires a limit |
| `DELIVERY.CUSTOMER` | Sends delivery messages to this customer for arrangement events |
| `RELATIONSHIP.PRICING.CUSTOMER` | Includes customer in preferential pricing evaluation |
| `EXCLUDE.DORMANCY` | Excludes this customer role from dormancy processing |
| `MAINTAIN.INFO` | Controls which tables are updated: Basic (AA.ARRANGEMENT only), Comprehensive/Null (AA.ARRANGEMENT + AA.CUSTOMER.ARRANGEMENT + AA.CUSTOMER.RELATED.ARRANGEMENTS), High Volume (AA.ARRANGEMENT + AA.MASS.CUSTOMER.ARRANGEMENT) |

**Related Arrangements (R20+):** The `CRA.CUSTOMER` field at arrangement level links customers related to the beneficial owner, populating `AA.CUSTOMER.RELATED.ARRANGEMENTS`. Relationship codes are defined in `AA.CRA.PARAMETER`.

### ELIGIBILITY (optional — Lending, Deposits, Accounts)

Defines eligibility conditions for a customer to opt for a product. Type: TRACKING.ONLY, DATED, VARIATION supported.

**Eligibility types (examples):**
- Customer type: Student (<18), Staff, Resident, Non-resident, Corporate, Foreigner
- Relationship value (total business with bank)
- Relationship length (time as customer)
- Age thresholds
- Salary thresholds

**Eligibility rules** are created using `EB.CONTEXT` → `EB.RULES.VERSION` → `EB.RULES`, then linked to the Eligibility product condition.

**Evaluation triggers:**
- When primary customer changes
- When product changes
- On periodic review

**On eligibility failure:**
- Error or Override (configurable)
- During COB: arrangement moved to `ELIGIBLE.DEFAULT.PRD` (default product)

**Product Condition fields:**
- `ELIGIBLE.DEFAULT.PRD` — the product to which the arrangement is moved if eligibility review fails during COB
- `DEFAULT.PRODUCT` — set to YES on the default product (which has no eligibility condition)

### OFFICERS (optional — Lending, Deposits, Accounts)

Specifies the account officers responsible for an arrangement. Can be set as Tracking. Update action is possible. Does not generate accounting entries.

**Key fields:**
- `PRIMARY.OFFICER` — main officer; ID copied to the underlying ACCOUNT.OFFICER field of the AA Account
- `OTHER.OFFICER` — multi-value; additional officers
- `ROLE` — role of each other officer (from AA.OFFICER.ROLE virtual table)

If no officer specified in the arrangement, ACCOUNT.OFFICER defaults from the CUSTOMER record.

**Usage:** Account Officer is used for balance consolidation reporting, MI module (average balances, profitability by Account Officer).

### ACTIVITY.MAPPING (mandatory — Lending, Deposits, Accounts)

Maps Transact Transaction Codes from external applications (Funds Transfer, Teller, AC.CASH.POOL) to AA Activities. Only one property of this class per Product Group. Type: TRACKING.ONLY — values cannot be viewed or edited at arrangement level.

**Key fields:**
- `TRANSACTION` — transaction code from external application
- `TXN.ACTIVITY` — AA activity to trigger when that transaction code is posted to the arrangement account
- Default activities for unmapped debit and credit transaction codes

**Example mappings:**
```
TXN Code 850  →  LENDING-DISBURSE-COMMITMENT
TXN Code 851  →  LENDING-APPLYPAYMENT-PR.PRINCIPAL.DECREASE
Default Credit →  LENDING-CREDIT-ARRANGEMENT
Default Debit  →  LENDING-DEBIT-ARRANGEMENT
```

**Event Mapping (R17+):** TEC items can also be mapped to AA activities for non-financial transactions through external applications.

### ACCOUNTING (mandatory — Lending, Deposits, Accounts)

Specifies the soft (rule-based) accounting rules for each property requiring accounting entries. Type: TRACKING.ONLY — values cannot be viewed or edited at arrangement level. Update action possible. Does not itself generate accounting entries.

**Key product condition fields:**

| Field | Purpose |
|-------|---------|
| `PROPERTY` | The property to which accounting rules apply |
| `ACCT.ACTION` | The action for which the rule is defined (must be one with ACCOUNTING=YES in AA.PROPERTY.CLASS.ACTION) |
| `ACCT.RULE` | Accounting allocation rule from AC.ALLOCATION.RULE |
| `ACCRUE.AMORT` | AMORT (amortise charge) or ACCRUE (accrue charge, R17+) |
| `ACCRUE.PERIOD` | MATURITY, RENEWAL, SCHEDULE (charges only), or specific period (1M, 1Y) |
| `PC.CONSOLIDATION` | Property class method for raising entries: Net or Itemised |
| `CONSOLIDATION` | Property-specific override of PC.CONSOLIDATION |
| `CONSOL.METHOD` | Net or Itemised — how charge/tax entries are raised |

**INTERNAL.BOOKING field** (on Interest, Charge, Periodic Charge property classes): When set to YES, income/expense is posted to internal account categories instead of P&L categories.

**Charge Amortisation (R15+):** Amortisation period can be RENEWAL, MATURITY, or a fixed period. On renewal date change, remaining unamortised amount is amortised to the new renewal date. Change product activity immediately recognises any remaining unamortised amount to P&L.

**Process Dated Accounting (R20+):** Extended from Accounts to Lending and Deposits. Entries stored with CONTEXT.NAME and CONTEXT.VALUE in AA.ARRANGEMENT.ACTIVITY.

### BALANCE.MAINTENANCE

Used for data migration (taking over and adjusting balances from legacy systems) and for defining periodic balance restrictions.

**Steps in data migration using Balance Maintenance:**
1. Define the property and product condition for BALANCE.MAINTENANCE
2. Create an arrangement
3. Use BALANCE.MAINTENANCE activities to inject historical balances
4. Verify balances are correct before going live

Activities include scheduled balance checks and restrictions based on balance thresholds.

### COMMITMENT / TERM.AMOUNT (mandatory — Lending)

Defines the commitment amount, term, maturity date, and disbursement parameters for lending arrangements.

**Record class:** `AaPrdDesTermAmountRecord`

**Key characteristics:**
- Currency is mandatory and cannot be amended after authorisation
- Supports partial or full disbursement
- CURACCOUNT balance tracks current principal; TOTCOMMITMENT tracks original commitment
- Cancellation moves arrangement to PENDING.CLOSURE status; closure scheduled per CLOSURE property condition

### INTEREST

Defines interest rate type, basis, and accrual method for lending and deposit arrangements.

**Record class:** `AaPrdDesInterestRecord`

**Interest types:**
- Fixed rate (flat rate, manually changed)
- Floating rate (pegged to BASIC.INTEREST table / BASIC.RATE.TEXT index; FLOATING.INDEX field)
- Periodic (PERIODIC.INTEREST / PERIODIC.AUTOMATIC — rate reviews on scheduled dates, can be auto-updated from Reuters etc.)
- Banded/tiered (mix of fixed and floating by balance tier)

**Interest day basis types:**

| Type | Description |
|------|-------------|
| A (A1, A2) | 30/360 — 30 days per month, 360 denominator |
| A4 | 30 days if monthly frequency with same dates or month end |
| B | Actual/360 |
| C | Actual/Actual (365 or 366) |
| D | 30/Actual (365 or 366) |
| E | Actual/365 |
| F (F1, F2) | 30/365 |
| H | 30/356 |
| S | Special |
| W, W1 | Brazilian working days basis |

For lending with floating rates, when rates change: either term adjusts (constant instalment) or instalment adjusts (constant term).

**Repayment types (Lending):** Constant (annuity), Linear (equal principal), Actual, or User-defined. Supports bullet payment (interest during term, principal at end).

### PAYMENT.SCHEDULE

Defines when and how payments are collected, applied, capitalised, or deferred.

**Record class:** `AaPrdDesPaymentRulesRecord`

### CHARGE

Defines fee amounts, charge types (Activity, Periodic, Calculated), insurance percentages, and waiver rules.

**Record class:** `AaPrdDesChargeRecord`

**Charge types:**
- **Activity charges** — triggered by specific activities
- **Periodic charges** — collected on a schedule (e.g. account management fee)
- **Calculated charges** — computed based on balances or usage

### ACCOUNT

Linked account reference; holds account-specific parameters including overdraft limits, IBAN, posting restrictions, dormancy criteria, and statement frequency.

**Record class:** `AaPrdDesAccountRecord`

### CLOSURE

Defines the closure period and process for arrangement termination. Used to schedule the closure activity when an arrangement reaches PENDING.CLOSURE status.

### LIMIT

Defines the limit type and amount for lending or overdraft accounts. For retail accounts, specifying a limit in the arrangement automatically creates the corresponding Limit record.

**Record class:** `AaPrdDesLimitRecord`

---

## AA Accounting

### Overview

AA uses **rule-based (soft) accounting**. Applications generate basic accounting events; central accounting tables process these events to generate actual entries. This removes the need for hard-coded accounting logic in each application.

**Accounting flow:**
```
Activity performed → Accounting event raised → AC.ALLOCATION.RULE applied
  → AC.POSTING.DETAIL builds entry content
  → STMT.ENTRY (account balance movement)
  → CATEG.ENTRY (P&L movement)
  → RE.CONSOL.SPEC.ENTRY (balance type movement)
```

Default SYSTEM.ID for AA transactions: `AAAA`

From R20: STMT.ENTRY, CATEG.ENTRY, and RE.CONSOL.SPEC.ENTRY include `SOFT.ACCTNG.DTLS` field with AC.EVENT and AC.ALLOCATION.RULE details for audit purposes.

### AC.BALANCE.TYPE

Defines the financial components of a product. Not all balance types can be changed via this application (some are hard-coded by Transact).

**REPORTING.TYPE values:**
- `CONTINGENT` — off-balance sheet (reported as contingent)
- `NON-CONTINGENT` — on-balance sheet
- `INTERNAL` — not used in reporting
- `VIRTUAL` — summation of other balances; used for calculation (e.g. memo balances, undrawn commitment)

**ACTIVITY.UPDATE field:** Controls whether a dated historical balance file (ACCT.ACTIVITY) is updated. Not applicable for Virtual balances.

**SUSPEND.BALANCE:** If a balance is to be suspended, set here; a balance type with suffix SP must exist.

### Arrangement Balances

Balances are associated with Properties. Each Property can have multiple Balances in different lifecycle stages. Balance Type ID format: `<BALANCE.PREFIX><PROPERTY.NAME>`.

Example: `DELCOMMITMENT` = Balance prefix DEL + Property name COMMITMENT.

**Balance Prefixes — Lending:**

| Prefix | Meaning |
|--------|---------|
| `CUR` | Current/live value of property (e.g. CURACCOUNT = current principal) |
| `ACC` | Current accrued balance (for P&L properties: Interest, Charges) |
| `DUE` | Due balance — property made due in Payment Schedule |
| `AGE` | Aged balance — prefix determined by overdue status (e.g. NAB for Non-Accrual Basis) |
| `UNC` | Unallocated/advance credits (Account property only) |
| `UND` | Unallocated debits (Account property only) |
| `AVL` | Available to disburse — contingent credit balance on commitment |

**Balance Prefixes — Deposits (additional):**

| Prefix | Meaning |
|--------|---------|
| `EXP` | Expected balance from customer (contingent) |
| `PAY` | Amount payable by Bank to customer or vice versa |

**Balance Prefixes — Accounts:**

| Prefix | Meaning |
|--------|---------|
| `CUR` | Current balance (e.g. CURBALANCE) |
| `ACC` | Accrued balance (Interest, Charges) |
| `UNC` | Unallocated/excess credits |
| `UND` | Unallocated debits |

**Balance suffix `SP`:** Indicates a suspended (non-accrual basis) balance.

### AC.ALLOCATION.RULE

Defines how an accounting event creates entries. One rule per event type per property/action combination. Specifies:
- Target balance, contra balance
- Transaction codes to use
- Entry type (STMT, CATEG, SPEC)
- Narrative/reference via AC.POSTING.DETAIL

Multiple entries and contra entries can be created from a single accounting event. Target options: P&L, internal account, specific balance type.

### Accounting Balances and Data Storage

| Store | Purpose |
|-------|---------|
| `EB.CONTRACT.BALANCES` | Current balance amounts by balance type; ID = AA Account ID |
| `ACCT.BALANCE.ACTIVITY` | ACCT.ACTIVITY data by AA account balance type |
| `ACCT.ACTIVITY` | Dated historical balance file (optional per balance type) |

**AASUSPENSE balance type:** Replaces the old suspense account approach (pre-R12). Payment in/out of a Loan or Deposit via FT or Teller uses this internal balance type instead of posting through a suspense account. Improves performance and reconciliation.

### Interest and Charge Accounting

Each Interest and Charge property typically gets its own P&L category. Debit/credit customer movements use separate TRANSACTION codes (linked to charge/interest type, not product). Both configured via AC.ALLOCATION.RULE. The recommended approach is to copy an existing allocation rule and modify for new properties.

---

## Activity Phases

Activities are the only way to update arrangements — both online and during COB. Creating a new arrangement is itself an activity. Activities are user-definable and grouped into Activity Classes (defined by Temenos).

### Activity Class Structure

An **Activity Class** is made up of **Actions** on Property Classes. The Activity Class ID format is: `<PRODUCT.LINE>-<PROCESS>-<PROPERTY.CLASS.NAME>`.

An **Activity** is an instance of an Activity Class that acts on a specific Property. Activity ID format: `<PRODUCT.LINE>-<PROCESS>-<PROPERTY.NAME>`.

Example: `LENDING-DISBURSE-TERM.AMOUNT` (activity class) → `LENDING-DISBURSE-COMMITMENT` (activity, where COMMITMENT is a property of TERM.AMOUNT class).

### Standard Activity Types

| ACTIVITY.TYPE | When Triggered |
|--------------|---------------|
| `SCHEDULED` | During COB batch (AA.EOD.PROCESS) |
| `SOD-PROCESS` | During start-of-day batch (AA.SOD.PROCESS) |
| `SIMULATION` | For simulation only — cannot be made LIVE |

### Core Activity Phases

| Phase | Activity Pattern | Key Property Classes Affected |
|-------|-----------------|------------------------------|
| New Arrangement | `<LINE>-NEW-ARRANGEMENT` | All; generates account, sets all conditions |
| Disburse | `<LINE>-DISBURSE-TERM.AMOUNT` | TERM.AMOUNT (draw), ACCOUNT (disburse), PAYMENT.SCHEDULE (recalculate) |
| Apply Payment / Repayment | `<LINE>-APPLYPAYMENT-<PROP>` | PAYMENT.SCHEDULE, ACCOUNT, INTEREST |
| Accrue Interest | `<LINE>-ACCRUE-INTEREST` | INTEREST; runs daily; reuses unique ID to prevent record accumulation |
| Change Interest | `<LINE>-CHANGE-<INTEREST.PROP>` | INTEREST |
| Decrease Commitment | `LENDING-DECREASE-TERM.AMOUNT` | TERM.AMOUNT, PAYMENT.SCHEDULE |
| Payment Holiday | `LENDING-UPDATE-PAYMENT.HOLIDAY` | PAYMENT.SCHEDULE |
| Payoff / Close | `LENDING-PAYOFF-ARRANGEMENT`, `DEPOSITS-CLOSE-ARRANGEMENT` | ACCOUNT, PAYMENT.SCHEDULE, all |
| Rollover | `DEPOSITS-ROLLOVER-ARRANGEMENT` | TERM.AMOUNT, INTEREST, PAYMENT.SCHEDULE |
| Charge/Fee | `<LINE>-CHANGE-DEFERPFT` | CHARGE |
| Suspend | `<LINE>-SUSPEND-ARRANGEMENT` | All |
| Resume | `<LINE>-RESUME-ARRANGEMENT` | All |
| Change Product | `<LINE>-CHANGE.PRODUCT-ARRANGEMENT` | All |
| Change Customer | `<LINE>-CHANGE-CUSTOMER` | CUSTOMER |
| Renegotiate | `<LINE>-RENEGOTIATE-ARRANGEMENT` | Any negotiable property |
| Update Account | `<LINE>-UPDATE-ACCOUNT` | ACCOUNT |
| Update Officers | `<LINE>-UPDATE-<OFFICERS.PROP>` | OFFICERS |
| Balance Update | `ACCOUNTS-UPDATE-BALANCE` | ACCOUNT |

### Activity Logging

**AA.ARRANGEMENT.ACTIVITY** — application used to input and store activity details. ID format: `AAACTYYDDDxxxxx`.

**AA.ACTIVITY.HISTORY** — log of all activities per arrangement. Key fields:

| Field | Purpose |
|-------|---------|
| `EFFECTIVE.DATE` | Date the activity was processed |
| `ACTIVITY.REF` | Reference to the AA.ARRANGEMENT.ACTIVITY record |
| `ACTIVITY` | Name of the activity performed |
| `SYSTEM.DATE` | Transact date when activity was triggered |
| `ACT.STATUS` | UNAUTH, UNAUTH-REV, UNAUTH-CHG, AUTH, AUTH-REV, DELETE-REV, DELETE |
| `INITIATION` | SCHEDULED, TRANSACTION, USER, SECONDARY |
| `ACTIVITY.ID` | Activity performed |
| `ACT.DATE` | Effective date |
| `ACT.COUNT` | Number of times activity performed on that date |
| `TOT.ACT.AMT` | Total count of times activity performed on arrangement |
| `ACTIVITY.AMOUNT` | Amount transacted (in arrangement currency) |

**AA.SCHEDULED.ACTIVITY** — holds scheduled activities for an arrangement with LAST.DATE, NEXT.DATE, and NEXT.RUN.DATE.

**AA.LENDING.NEXT.ACTIVITY** / **AA.DEPOSITS.NEXT.ACTIVITY** — list files driving COB batch selection. ID format: `<ARRANGEMENT.ID>-<DATE>`.

### COB Batch Structure

| Batch | Stage | Jobs |
|-------|-------|------|
| `AA.EOD.PROCESS` | End-of-Day (S022) | AA.ARR.PRODUCT.TRACKER, AA.COB.PAY.IN.OUT, AA.SERVICE.PROCESS |
| `AA.SOD.PROCESS` | Start-of-Day (D250) | AA.COB.PAY.IN.OUT, AA.SERVICE.PROCESS |

`AA.SERVICE.PROCESS` reads AA.SCHEDULED.ACTIVITY and processes due activities for each arrangement. The sequence number for each scheduled activity is set by Temenos in `BATCH.SEQ` on the activity class.

---

## Named Activities

Standard activities auto-generated from the Product Group are of the form `<PRODUCT.LINE>-<PROCESS>-<PROPERTY>`. These are shared across all products using that property.

**Named Activities** allow product-specific extensions:
1. Manually create a record in `AA.ACTIVITY`
2. Set `LINKED.ACTIVITY` to the base system activity (which must have `SYSTEM.ACTIVITY=YES`)
3. The named activity performs all actions of the linked activity PLUS any routines added via ACTIVITY.API

Named activities appear alongside the base activity in the arrangement's available activity list.

**Auto-generation of activities:** Set `REBUILD.ACTIVITIES=YES` in the Product Group to auto-generate all standard activities for each property. The system picks all properties → property classes → activity classes → generates activities. After generation, modify descriptions as these appear in the Activity Log.

---

## Product Tracker and COB

### AA.PRODUCT.TRACKER.CATALOG

When a product is re-proofed or re-published, Transact detects changes to product conditions and records them in this file. This drives propagation of product changes to existing arrangements.

**Not tracked:**
- Products set to inheritance-only (but affected child products are tracked)
- First publish event
- Classic (non-AA) products

**Tracking behaviour:**
- On PROOF: changes written to `AA.PRODUCT.TRACKER.PROOF`
- On PUBLISH: `AA.PRODUCT.TRACKER.PROOF` deleted, changes copied to `AA.PRODUCT.TRACKER.CATALOG`
- Negotiation fields are ignored during comparison

### AA.ARR.PRODUCT.TRACKER Service

Reads `AA.PRODUCT.TRACKER.CATALOG` and updates arrangement conditions (`AA.ARR.<PROPERTY.CLASS>`) for each affected arrangement. Auto-triggered on product re-publish. Uses OFS.BULK.MANAGER for transaction management (ADDITIONAL.INFO set to .NTX in PGM.FILE).

Until the service runs, existing arrangements see updated values when an activity is performed (values are merged from product condition at activity time).

### Product Condition Precedence Rules

When multiple product conditions exist for the same property on the same date, the system uses the following rules:
- Back-dated conditions: the one most recently introduced takes priority
- A product condition chain is maintained — once an arrangement uses a condition from a given product condition ID, subsequent updates must come from the same ID (cannot switch between condition IDs)

---

## Local Reference Fields in AA

AA property classes share fields across five applications:

| Application Pattern | Purpose |
|--------------------|----|
| `AA.PRD.DES.<CLASS>` | Designer information (product condition definition) |
| `AA.PRD.PRF.<CLASS>` | Proofed product conditions |
| `AA.PRD.CAT.<CLASS>` | Published/catalogued product conditions |
| `AA.ARR.<CLASS>` | Live arrangement conditions |
| `AA.SIM.<CLASS>` | Simulated arrangement conditions |

Adding a local reference field to `AA.PRD.DES.<CLASS>` via LOCAL.REF.TABLE automatically replicates the field to all other four applications (PRF, CAT, ARR, SIM). This is triggered when the LOCAL.REF.TABLE record is authorised — the standard selection records for all related files are rebuilt.

**Use case:** Adding custom fields to a property class (e.g. CUST.SECTOR to CUSTOMER, POSTNG.RESTRICT to TERM.AMOUNT) that are specific to local implementation without modifying Temenos-released property classes.

**Access in OFS messages:** Local reference fields can be supplied in OFS messages for AA the same way as standard fields — by specifying the property and field name in the message data.

---

## ACTIVITY.PRESENTATION Property Class

Controls which version (screen layout) is displayed dynamically based on the current activity.

**Why:** Versions allow users to enter data in custom-designed screens. Different activities may need different field presentations for the same property.

**Version attachment levels** (priority highest to lowest):
1. **Activity level** — version for a specific activity (e.g. LENDING-DECREASE-COMMITMENT)
2. **Property level** — version for a specific property (e.g. MYCUST)
3. **Property Class level** — version for all properties of that class (e.g. CUSTOMER)

If no version found at any level, the default application screen is used.

**Key product condition fields:**

| Field | Purpose |
|-------|---------|
| `SUPPRESS.SEE.MODE` | YES = hide properties that are in SEE-only (not-input) mode during the activity, to reduce screen clutter |
| `CLASS.VERSION` | Version attached at property class level |
| `PROP.VERSION` | Version attached at property level |
| `ACT.VERSION` | Version attached at activity level |
| `CLASS.SIM.VER` | Simulation version at property class level |
| `PROP.SIM.VER` | Simulation version at property level |
| `ACT.SIM.VER` | Simulation version at activity level |

**Inheritance (TRACKING.ONLY):** If a child product does not define a version for an activity but the parent does, the parent's version is used (merging behaviour). Conditions are merged mutually exclusively during proofing.

**Restriction:** Versions cannot contain version routines in AA.ARR.XXX files — all fields accepting version routines become no-input fields. Use ACTIVITY.API for custom logic.

---

## ACTIVITY.API Property Class

Allows user-defined routines to be linked to arrangement activities. Replaces the old approach of attaching routines directly to versions.

**Purpose:** Extend or customise activity behaviour — pre/post validation, secondary activity generation, updating fields in properties not open for input during an activity.

### Configuration Steps

1. Write and compile/catalogue the routine
2. Register the routine in `EB.API`
3. Create an ACTIVITY.API product condition attaching the routine to an Activity Class or Activity
4. Attach the product condition to the product; proof and publish

### Routine Attachment Options

| Field | When Executed |
|-------|--------------|
| `PRE.VALIDATE.RTN` | Before core property validation — can modify inputtable fields |
| `PRE.ROUTINE` | Before the activity action executes |
| `POST.ROUTINE` | After the activity action executes |

Multiple routines can be attached to the same activity or activity class.

### Inheritance and Merging (cumulative)

ACTIVITY.API is a **cumulative** property class — routines from both child and parent products execute. Merging order during proofing:
- Child routines first, then parent routines
- Activity-level routines take precedence over Activity Class level routines
- Execution order: Pre-validate → Pre-routines (child→parent, Activity→ActivityClass) → Post-routines (child→parent, Activity→ActivityClass)

### Common Insert Files for AA API Routines

| Insert File | Contents |
|-------------|---------|
| `I_COMMON` | Common Transact variables |
| `I_EQUATE` | Standard equates |
| `I_AA.LOCAL.COMMON` | AA named common variables — key variables below |
| `I_F.AA.ACCOUNT` | Field name equates for ACCOUNT property class |
| `I_F.AA.TERM.AMOUNT` | Field name equates for TERM.AMOUNT property class |

**Key variables in I_AA.LOCAL.COMMON:**

| Variable | Contents |
|---------|---------|
| `c_aalocArrangementRec` | Main arrangement record |
| `c_aalocArrProductId` | Product ID used by the arrangement |
| `c_aalocArrId` | Arrangement ID |
| `c_aalocArrActivityId` | Arrangement activity ID |
| `c_aalocActivityId` | Activity ID being processed |
| `c_aalocActivityEffDate` | Effective date of the activity |
| `c_aalocProductRecord` | Published product record for the arrangement |

### Key jBC Routines for ACTIVITY.API

| Routine | Purpose |
|---------|---------|
| `AA.GET.PROPERTY.NAME(PRODUCT.RECORD, PROPERTY.CLASS, PROPERTY)` | Returns list of properties for a given property class |
| `AA.GEN.ARRANGEMENT.ACTIVITY.FIELDS(ARR.PROPERTY.LIST, ARR.FIELD.NAME.LIST, ARR.FIELD.VALUE.LIST, ARR.ACT.FIELDS.REC)` | Builds mapped arrangement activity record from property/field/value lists |
| `AA.GEN.NEW.ARRANGEMENT.ACTIVITY(ARRANGEMENT.ID, NEW.ACTIVITY, EFFECTIVE.DATE, ARR.TXN.DETAILS, ARR.ACTIVITY.ID, ARR.ACT.FIELDS.REC, RETURN.ERROR)` | Creates and queues a secondary AA activity |
| `AA.SECONDARY.ACTIVITY.MANAGER` | Called by AA.GEN.NEW.ARRANGEMENT.ACTIVITY to append secondary activity |
| `GET.STANDARD.SELECTION.DETS` | Retrieves STANDARD.SELECTION record for an AA.ARR.XXX application |
| `FIELD.NUMBERS.TO.NAMES(IN.FIELD.NUMBER, R.STANDARD.SELECTION, FIELD.NAME, DATA.TYPE, ERR.MSG)` | Converts field numbers to field names |

---

## ACTIVITY.MESSAGING Property Class

Manages delivery message generation for arrangement activities. Optional property class. Can be configured at both product and arrangement level.

**Delivery integration:** AA uses rules-based (soft) delivery via the EB.ADVICES / DE framework. One or more delivery message types can be generated from a single delivery event.

### Configuration Steps

1. Create `EB.ADVICES` record (no EB.ACTIVITY check required when prefixed with AA)
   - `MESSAGE.TYPE` — references a DE.MESSAGE record (must be 1–9999 for AA)
   - `MAPPING.KEY` — references DE.MAPPING (format: `<MessageType>.AA.<SubType>`)
   - `USER.ROUTINE` — optional routine for custom handoff data (accepts two parameters: control flag TRUE/FALSE, handoff array)
2. Create ACTIVITY.MESSAGING product condition, attaching EB.ADVICES record to specific activities
3. Attach product condition to product; proof and publish

### DE.MAPPING Configuration

| Field | Purpose |
|-------|---------|
| `INPUT.REC.NUMBER` | Position in handoff record (1–9 for positional; name for named) |
| `INPUT.REC.DES` | Description of the record |
| `INPUT.FILE` | T24 file (from STANDARD.SELECTION) to populate at this position |
| `RECORD.NAME.LOC` | Array position (hardcoded 7) that holds the list of allowed property names for named handoff records |

**Named handoff records:** AA supports flexible named records beyond position 9. Specify a name (e.g. ACCOUNT) in INPUT.REC.NO and the file (e.g. AA.ARR.ACCOUNT) in INPUT.FILE.

**INPUT.POSITION mapping styles:**
- By position: `2.3` (record 2, field 3)
- By field name: reference field name in INPUT.FILE

### Arrangement-Level Control (R9+)

The `SEND.ADVICE` field at arrangement level controls delivery for specific activities. ACTIVITY.MESSAGING is no longer TRACKING.ONLY — property type must be null for arrangement-level editing.

**MSG.CONTENT field:**
- `ALL` — passes previous (R.OLD) and current (R.NEW) property values in the delivery message
- `CHANGE` — passes current values only

### Pre-notification Advices

Activity classes `ACCOUNTS-PRE.NOTICE-ARRANGEMENT`, `DEPOSITS-PRE.NOTICE-ARRANGEMENT`, and `LENDING-PRE.NOTICE-ARRANGEMENT` (with SEND.MESSAGE action) generate pre-notification advices for scheduled activities. After setting `PRE.NOTICE.ACTIVITY` and rebuilding activities, a `*-PRE.NOTICE` activity is created.

### ALERTS Property Class

Companion to ACTIVITY.MESSAGING. Allows user-configurable event-based alerts (e.g. balance below threshold).

**Configuration applications:**

| Application | Purpose |
|------------|---------|
| `EB.ACTIVITY` | Links T24 table to event |
| `EB.EVENT.TYPE` | Defines alert trigger metrics/conditions |
| `TEC.ITEMS` | Event items |
| `AA.PRD.DES.ALERTS` | Product condition for ALERTS property class (specifies EVENT field) |
| `EB.ALERT.REQUEST` | Alert subscription record |
| `AA.ARR.ALERTS` | Arrangement-level alert records (created when arrangement activity triggers subscription) |
| `F.EVENT.LIST` | Queue of events to process |

**Processing:** Trigger activity → generates `<LINE>-SUBSCRIBE-<ALERTS.PROP>` activity → creates AA.ARR.ALERTS record → events written to F.EVENT.LIST → service BNK/EVENT processes alerts.

---

## AA and OFS

All arrangement operations use OFS via the application `AA.ARRANGEMENT.ACTIVITY`. Everything in AA is an activity; the application name is always `AA.ARRANGEMENT.ACTIVITY` regardless of what underlying data is being updated.

### OFS Message Structure for AA

```
AA.ARRANGEMENT.ACTIVITY,<VERSION>/I/PROCESS
<SIGNON.NAME>/<PASSWORD>/<COMPANY>
<RECORD.ID>//<MSG.ID>
AA.ARRANGEMENT=NEW,ACTIVITY=LENDING-NEW-ARRANGEMENT,
CUSTOMER=<CUST.ID>,CURRENCY=<CCY>,PRODUCT=<PRODUCT.ID>,...
```

**Key fields in the OFS message data:**

| Field | Purpose |
|-------|---------|
| `AA.ARRANGEMENT` | Set to NEW for new arrangements; system creates the arrangement record |
| `ACTIVITY` | The activity to perform (e.g. LENDING-NEW-ARRANGEMENT, LENDING-CHANGE-INTEREST) |
| `CUSTOMER` | Customer ID or mnemonic |
| `CURRENCY` | Arrangement currency |
| `PRODUCT` | Product ID from AA.PRODUCT.CATALOG |
| `PROPERTY:n:m` | Property to update (multi-value position n, sub-value m) |
| `FIELD.NAME:n:m` | Field name within the property |
| `FIELD.VALUE:n:m` | Value for the field |

**Defaulting:** Product Condition defaults need not be specified in the OFS message — they are automatically applied. Only mandatory and negotiated fields need to be supplied.

**Local reference fields** can be supplied in OFS messages alongside standard fields by specifying the property and field name in the same manner.

**For amending existing arrangements:** Supply the arrangement ID in the RECORD.ID section (not NEW).

### OFS.BULK.MANAGER

AA activities update multiple applications simultaneously (`AA.ARRANGEMENT`, `AA.ARRANGEMENT.ACTIVITY`, `AA.ARR.XXX` files). OFS.BULK.MANAGER handles this by:

1. Receiving bulk OFS messages (multiple messages delimited by FM)
2. Splitting them and queuing in `c_Txn_RequestQueue` (memory)
3. Starting a single transaction block
4. Processing each message through the standard OFS pipeline (PROCESS.MANAGER → SESSION.MANAGER → REQUEST.MANAGER → application)
5. Application-level transaction management is suppressed — OFS.BULK.MANAGER owns the transaction boundary
6. On success: commits all. On any error: rolls back all (EB.TRANS ABORT)

**Not bulk-processed:**
- Enquiry requests (application name = ENQUIRY.SELECT)
- Applications with `ADDITIONAL.INFO=.NBK` (No Bulking) in PGM.FILE (e.g. AA.PRODUCT.MANAGER)
- Applications with TYPE=S (subroutine) or TYPE=W (work file) in PGM.FILE
- Delivery requests (application name = DECARRIER)
- TEC applications or applications with no PGM.FILE record

**Debugging:** Set `ATTRIBUTES=BULK.TRACE` in the OFS.SOURCE record to create log files named `OBM_<SOURCE.ID>_<SYSTEM(101)>` in the .run directory.

### Internal OFS Generation from Routines

```basic
* From within a jBC routine — generate an AA arrangement via OFS
CALL OFS.POST.MESSAGE(OFS.SOURCE.ID, OFS.MSG, RESPONSE, ERR)
* OFS.SOURCE must have SOURCE.TYPE = GLOBUS
* Message is queued in F.OFS.MESSAGE.QUEUE
* Process with OFS.MESSAGE.SERVICE
```

---

## Simulation Engine

Simulation allows performing operations and viewing outcomes without applying changes to live arrangements. Useful for product testing, what-if analysis, and customer negotiation.

### Three Stages of Simulation

**Stage 1 — Data Capture:**
- Data entered in `AA.SIMULATION.CAPTURE` (similar to AA.ARRANGEMENT.ACTIVITY)
- Stored in `AA.SIM.<PROPERTY.CLASS>` (parallel to AA.ARR.<PROPERTY.CLASS>)
- Action routines NOT triggered at this stage; only basic validations
- `AUTO.RUN` field controls stage transitions:
  - `SIMULATE` — on authorise, immediately runs simulation
  - `EXECUTE` — on authorise, executes a previously simulated result to LIVE
  - `DIRECT.EXECUTE` — skips simulate stage; directly makes LIVE on authorise
  - blank — manual control via AA.SIMULATION.RUNNER

**Stage 2 — Simulation Runner:**
- `AA.SIMULATION.RUNNER` record is created (auto or manually)
- Key fields: `ARRANGEMENT.REF`, `SIM.RUN.DATE`, `SIM.END.DATE`, `SIM.CAPTURE.REF` (multi-value for multiple captures), `EXECUTE.SIMULATION`
- Authorising generates OFS string in `AA.SIMULATION.SERVICE.LIST` with ID format `<RUNNER.ID>.SIMULATE` or `<RUNNER.ID>.EXECUTE`
- `S.ACTIVITY` / `U.ACTIVITY` / `T.ACTIVITY` fields specify scheduled, user, and transaction activities to simulate
- `STATUS` field: COMPLETED - SUCCESSFULLY, COMPLETED - ERROR, PROCESSING

**Stage 3 — Simulation Service:**
- Service `AA.SIMULATION.SERVICE` processes the OFS string from AA.SIMULATION.SERVICE.LIST
- Stores results in `$SIM` files (e.g. `AA.ARR.TERM.AMOUNT$SIM`) and `F.SIMULATION.DETAILS`
- Updates AA.SIMULATION.RUNNER with STATUS
- Action routines ARE triggered during simulate and execute phases; data is not written to live DB during simulate, but IS written during execute
- Overrides accepted by default during simulation

### Simulation Data Storage

| Store | Purpose |
|-------|---------|
| `AA.ARRANGEMENT.SIM` | Simulated arrangement master (parallel to AA.ARRANGEMENT) |
| `AA.SIM.<PROPERTY.CLASS>` | Simulated property conditions (parallel to AA.ARR.<PROPERTY.CLASS>) |
| `AA.ACTIVITY.HISTORY.SIM` | Log of simulated activities (uses AA.SIMULATION.CAPTURE ID instead of AA.ARRANGEMENT.ACTIVITY ID) |
| `$SIM files` | Simulated snapshots per property (ID: `<ARR.ID>-<PROP>-<EFF.DATE>.<SEQ>%<RUNNER.ID>`) |
| `F.SIMULATION.DETAILS` | Additional simulation data store |
| `AA.SCHEDULED.ACTIVITY$SIM` | Scheduled activities generated during simulation |

### Simulation and ACTIVITY.PRESENTATION

Versions for simulated activities should be created for `AA.SIM.<PROPERTY.CLASS>` applications (not AA.ARR.XXX). Use the SIM version fields in the ACTIVITY.PRESENTATION product condition (`CLASS.SIM.VER`, `PROP.SIM.VER`, `ACT.SIM.VER`).

`SIM.READ` routine fetches the correct simulated record:
1. Checks $SIM file for the record
2. If found, reads the simulated record
3. If not found, reads from F.SIMULATION.DETAILS
4. If neither exists, falls back to the live file via F.READ

### Related Activities in Simulation

`RELATED.ACTIVITY` field on AA.ACTIVITY record: specifies an activity to trigger automatically after the current simulated activity. Controlled at the activity class level via `RELATED.ACT.CLASS`. Only valid for simulations — not for live arrangements.

### Monitoring

Enquiry `AA.SIMULATION.MONITOR` shows the status of all simulations (successful and failed).

---

## Public APIs

| Class | JAR | Method | Returns | Description |
|-------|-----|--------|---------|-------------|
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `getVersion` | `java.lang.String` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `defaultFieldValues` | `void` | Called before user sees activity screen; populate field defaults |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `generateSecondaryActivity` | `void` | Triggers follow-up AA activity after primary activity completes |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `postCoreTableUpdate` | `void` | Called after authorisation and DB commit; post-authorise side effects |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `validateRecord` | `com.temenos.api.TValidationResponse` | Full-record validation on commit; cross-field validation |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `updateLookupTable` | `com.temenos.api.TBoolean` | Maintains custom concat/lookup tables during activity processing |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `setElementData` | `void` | Sets element-level data (seldom used) |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `filterElements` | `java.util.List<java.lang.String>` | Filters the set of elements available in the activity |
| `ActivityLifecycle` | `AA_ActivityHook.jar` | `filterAccrualProperties` | `void` | Filters properties included in accrual processing |
| `Bill` | `AA_BillApi.jar` | `getVersion` | `java.lang.String` | Bill API — create and access Bill records |
| `Bill` | `AA_BillApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Bill` | `AA_BillApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Bill` | `AA_BillApi.jar` | `setContractId` | `void` | Set the arrangement (contract) ID context |
| `Bill` | `AA_BillApi.jar` | `getContractId` | `java.lang.String` | Get the current arrangement ID |
| `Bill` | `AA_BillApi.jar` | `setBillId` | `void` | Set the Bill ID to read |
| `Bill` | `AA_BillApi.jar` | `getBillId` | `java.lang.String` | Get the current Bill ID |
| `Bill` | `AA_BillApi.jar` | `getBillRecord` | `com.temenos.t24.api.records.aabilldetails.AaBillDetailsRecord` | Read the full AA.BILL.DETAILS record for the set Bill ID |
| `Calculation` | `AA_CalculationHook.jar` | `getVersion` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Calculation` | `AA_CalculationHook.jar` | `calculateSourceBalance` | `void` | Override the source balance used for interest/charge calculation |
| `Calculation` | `AA_CalculationHook.jar` | `calculatePayment` | `com.temenos.api.TNumber` | Override the payment amount in the payment schedule |
| `Calculation` | `AA_CalculationHook.jar` | `calculateUncSettledAmount` | `com.temenos.api.TNumber` | Override the unsettled credit amount |
| `Calculation` | `AA_CalculationHook.jar` | `calculateCharge` | `void` | Override charge calculation |
| `Calculation` | `AA_CalculationHook.jar` | `calculateAdjustedCharge` | `void` | Override adjusted charge calculation |
| `Calculation` | `AA_CalculationHook.jar` | `SortDrawingsArrangements` | `void` | Custom sort order for drawings/sub-arrangements |
| `Calculation` | `AA_CalculationHook.jar` | `getChargeAmount` | `com.temenos.api.TNumber` | Return the calculated charge amount |
| `Calculation` | `AA_CalculationHook.jar` | `getAdjustedChargeAmount` | `com.temenos.t24.api.complex.aa.calculationhook.ChargeAdjustment` | Return adjusted charge amount with adjustment details |
| `Calculation` | `AA_CalculationHook.jar` | `getDataElementValue` | `java.lang.String` | Return a data element value used in calculation |
| `Calculation` | `AA_CalculationHook.jar` | `getBreakCostFeeInterestRates` | `com.temenos.t24.api.complex.aa.calculationhook.AdjustedInterest` | Return interest rates used for break cost fee calculation |
| `Calculation` | `AA_CalculationHook.jar` | `getInterestCustomRate` | `void` | Override interest rate with custom value |
| `Contract` | `AA_ContractApi.jar` | `getVersion` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Contract` | `AA_ContractApi.jar` | `setContractId` | `void` | Set the arrangement ID for subsequent API calls |
| `Contract` | `AA_ContractApi.jar` | `getContractId` | `java.lang.String` | Get the current arrangement ID |
| `Contract` | `AA_ContractApi.jar` | `getBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get balance movements for the arrangement |
| `Contract` | `AA_ContractApi.jar` | `getBalanceMovementsForPeriod` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get balance movements for a specific period |
| `Contract` | `AA_ContractApi.jar` | `getForwardCreditBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get forward-dated credit balance movements |
| `Contract` | `AA_ContractApi.jar` | `getForwardDebitBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get forward-dated debit balance movements |
| `Contract` | `AA_ContractApi.jar` | `getAllBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get all balance movements |
| `Contract` | `AA_ContractApi.jar` | `getContractBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get contract-level balance movements |
| `Contract` | `AA_ContractApi.jar` | `getContractBalanceMovementsForPeriod` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Get contract balance movements for a period |
| `Contract` | `AA_ContractApi.jar` | `getContractForwardCreditBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Forward credit movements at contract level |
| `Contract` | `AA_ContractApi.jar` | `getContractForwardDebitBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | Forward debit movements at contract level |
| `Contract` | `AA_ContractApi.jar` | `getAllContractBalanceMovements` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.BalanceMovement>` | All contract-level balance movements |
| `Contract` | `AA_ContractApi.jar` | `getInterestAmounts` | `com.temenos.t24.api.complex.aa.contractapi.InterestAmount` | Get interest amounts (accrued, due, etc.) |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepayment` | `com.temenos.api.TNumber` | Total repayments received |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepaymentForProperty` | `com.temenos.api.TNumber` | Total repayments received for a specific property |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepaymentForPeriod` | `com.temenos.api.TNumber` | Total repayments received for a date period |
| `Contract` | `AA_ContractApi.jar` | `getTotalReceivedRepaymentForMonth` | `com.temenos.api.TNumber` | Total repayments received for a specific month |
| `Contract` | `AA_ContractApi.jar` | `getLastRepayment` | `com.temenos.t24.api.complex.aa.contractapi.Payment` | Details of the most recent repayment |
| `Contract` | `AA_ContractApi.jar` | `getNextPayment` | `com.temenos.t24.api.complex.aa.contractapi.Payment` | Details of the next scheduled payment |
| `Contract` | `AA_ContractApi.jar` | `getAccountDetailsRecord` | `com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord` | Get the AA.ACCOUNT.DETAILS record |
| `Contract` | `AA_ContractApi.jar` | `getInterestAccrualsRecord` | `com.temenos.t24.api.records.aainterestaccruals.AaInterestAccrualsRecord` | Get the AA interest accruals record |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForPayMethod` | `java.util.List<java.lang.String>` | Get bill IDs filtered by payment method |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForDate` | `java.util.List<java.lang.String>` | Get bill IDs filtered by date |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForPaymentDate` | `java.util.List<java.lang.String>` | Get bill IDs filtered by payment date |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForBillType` | `java.util.List<java.lang.String>` | Get bill IDs filtered by bill type |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForBillStatus` | `java.util.List<java.lang.String>` | Get bill IDs filtered by bill status (DUE, PAID, etc.) |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForSettlementStatus` | `java.util.List<java.lang.String>` | Get bill IDs filtered by settlement status |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForAgingStatus` | `java.util.List<java.lang.String>` | Get bill IDs filtered by aging status |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForNextAgeDate` | `java.util.List<java.lang.String>` | Get bill IDs by next aging date |
| `Contract` | `AA_ContractApi.jar` | `getBillIdsForRepaymentReference` | `java.util.List<java.lang.String>` | Get bill IDs by repayment reference |
| `Contract` | `AA_ContractApi.jar` | `getBillIds` | `java.util.List<java.lang.String>` | Get all bill IDs for the arrangement |
| `Contract` | `AA_ContractApi.jar` | `getContract` | `com.temenos.t24.api.records.aaarrangement.AaArrangementRecord` | Get the AA.ARRANGEMENT record |
| `Contract` | `AA_ContractApi.jar` | `getCustomerRole` | `com.temenos.t24.api.complex.aa.contractapi.CustomerRole` | Get the customer roles for the arrangement |
| `Contract` | `AA_ContractApi.jar` | `getNextDueDate` | `com.temenos.api.TDate` | Get the next bill due date |
| `Contract` | `AA_ContractApi.jar` | `getFirstOverdueDate` | `com.temenos.api.TDate` | Get the date of the first overdue bill |
| `Contract` | `AA_ContractApi.jar` | `getLastOverDueDate` | `com.temenos.api.TDate` | Get the date of the most recent overdue bill |
| `Contract` | `AA_ContractApi.jar` | `getNumberOfOverDueBills` | `com.temenos.api.TNumber` | Count of currently overdue bills |
| `Contract` | `AA_ContractApi.jar` | `getMaturityDate` | `com.temenos.api.TDate` | Get the arrangement maturity date |
| `Contract` | `AA_ContractApi.jar` | `getPropertyIds` | `java.util.List<java.lang.String>` | Get all property IDs for the arrangement |
| `Contract` | `AA_ContractApi.jar` | `getPropertyIdsForPropertyClass` | `java.util.List<java.lang.String>` | Get property IDs filtered by property class |
| `Contract` | `AA_ContractApi.jar` | `getTerm` | `java.lang.String` | Get the arrangement term (e.g. 1Y, 6M) |
| `Contract` | `AA_ContractApi.jar` | `getTermAmount` | `com.temenos.api.TNumber` | Get the commitment/term amount |
| `Contract` | `AA_ContractApi.jar` | `getContractAgeStatus` | `java.lang.String` | Get the current aging status of the arrangement |
| `Contract` | `AA_ContractApi.jar` | `getProductId` | `java.lang.String` | Get the current product ID |
| `Contract` | `AA_ContractApi.jar` | `getProductIdForEffectiveDate` | `java.lang.String` | Get the product ID as of a specific date |
| `Contract` | `AA_ContractApi.jar` | `getSimulationId` | `java.lang.String` | Get the simulation ID if this is a simulated arrangement |
| `Contract` | `AA_ContractApi.jar` | `getAccountCondition` | `com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord` | Get current ACCOUNT property condition |
| `Contract` | `AA_ContractApi.jar` | `getAccountConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddesaccount.AaPrdDesAccountRecord` | Get ACCOUNT condition as of a date |
| `Contract` | `AA_ContractApi.jar` | `getCustomerCondition` | `com.temenos.t24.api.records.aaprddescustomer.AaPrdDesCustomerRecord` | Get current CUSTOMER property condition |
| `Contract` | `AA_ContractApi.jar` | `getCustomerConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddescustomer.AaPrdDesCustomerRecord` | Get CUSTOMER condition as of a date |
| `Contract` | `AA_ContractApi.jar` | `getInterestCondition` | `java.util.List<com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord>` | Get current INTEREST property conditions |
| `Contract` | `AA_ContractApi.jar` | `getInterestConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord>` | Get INTEREST conditions as of a date |
| `Contract` | `AA_ContractApi.jar` | `getLimitCondition` | `com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord` | Get current LIMIT property condition |
| `Contract` | `AA_ContractApi.jar` | `getLimitConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddeslimit.AaPrdDesLimitRecord` | Get LIMIT condition as of a date |
| `Contract` | `AA_ContractApi.jar` | `getOfficersCondition` | `com.temenos.t24.api.records.aaprddesofficers.AaPrdDesOfficersRecord` | Get current OFFICERS property condition |
| `Contract` | `AA_ContractApi.jar` | `getOfficersConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddesofficers.AaPrdDesOfficersRecord` | Get OFFICERS condition as of a date |
| `Contract` | `AA_ContractApi.jar` | `getCommitmentCondition` | `com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord` | Get current TERM.AMOUNT (commitment) condition |
| `Contract` | `AA_ContractApi.jar` | `getCommitmentConditionForEffectiveDate` | `com.temenos.t24.api.records.aaprddestermamount.AaPrdDesTermAmountRecord` | Get commitment condition as of a date |
| `Contract` | `AA_ContractApi.jar` | `getChargeCondition` | `java.util.List<com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord>` | Get current CHARGE property conditions |
| `Contract` | `AA_ContractApi.jar` | `getChargeConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord>` | Get CHARGE conditions as of a date |
| `Contract` | `AA_ContractApi.jar` | `getRepaymentCondition` | `java.util.List<com.temenos.t24.api.records.aaprddespaymentrules.AaPrdDesPaymentRulesRecord>` | Get current PAYMENT.SCHEDULE conditions |
| `Contract` | `AA_ContractApi.jar` | `getRepaymentConditionForEffectiveDate` | `java.util.List<com.temenos.t24.api.records.aaprddespaymentrules.AaPrdDesPaymentRulesRecord>` | Get payment schedule conditions as of a date |
| `Contract` | `AA_ContractApi.jar` | `getConditionForProperty` | `com.temenos.api.TStructure` | Get condition for any property (generic) |
| `Contract` | `AA_ContractApi.jar` | `getConditionForPropertyEffectiveDate` | `com.temenos.api.TStructure` | Get condition for any property as of a date |
| `Contract` | `AA_ContractApi.jar` | `getSimulationConditionForProperty` | `com.temenos.api.TStructure` | Get the simulated condition for a property |
| `Contract` | `AA_ContractApi.jar` | `getFirstVersionOfProperty` | `com.temenos.api.TStructure` | Get the original/first version of a property condition |
| `Contract` | `AA_ContractApi.jar` | `getPreviousDatedProperty` | `com.temenos.api.TStructure` | Get the previous dated version of a property condition |
| `Contract` | `AA_ContractApi.jar` | `getPreviousProperty` | `com.temenos.api.TStructure` | Get the immediately preceding property condition |
| `Contract` | `AA_ContractApi.jar` | `buildPaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.PaymentSchedule>` | Build the full payment schedule for the arrangement |
| `Contract` | `AA_ContractApi.jar` | `buildPaymentScheduleForProperty` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.PaymentSchedule>` | Build payment schedule for a specific property |
| `Contract` | `AA_ContractApi.jar` | `getFutureRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | Get future repayment schedule |
| `Contract` | `AA_ContractApi.jar` | `getRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | Get full repayment schedule |
| `Contract` | `AA_ContractApi.jar` | `getContractBeneficialOwner` | `java.lang.String` | Get the primary beneficial owner customer ID |
| `Contract` | `AA_ContractApi.jar` | `getOutstandingBalance` | `com.temenos.t24.api.complex.aa.contractapi.OutstandingBalances` | Get outstanding balances (principal, interest, charges) |
| `Contract` | `AA_ContractApi.jar` | `getEffectiveInterestRate` | `com.temenos.t24.api.complex.aa.contractapi.EffectiveInterestRate` | Get the effective interest rate |
| `Contract` | `AA_ContractApi.jar` | `getInterestProfitAmount` | `com.temenos.t24.api.complex.aa.contractapi.ProfitAmount` | Get the interest/profit amount |
| `Contract` | `AA_ContractApi.jar` | `getActualDate` | `com.temenos.t24.api.complex.aa.contractapi.DateConversion` | Convert a scheduled date to an actual (business day adjusted) date |
| `Contract` | `AA_ContractApi.jar` | `getFutureSimulationRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | Get future repayment schedule from simulation |
| `Contract` | `AA_ContractApi.jar` | `getSimulationRepaymentSchedule` | `java.util.List<com.temenos.t24.api.complex.aa.contractapi.RepaymentSchedule>` | Get full repayment schedule from simulation |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getVersion` | `java.lang.String` | Payment schedule hook — override available balance calculation |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `PaymentSchedule` | `AA_PaymentScheduleHook.jar` | `getAvailableBalance` | `void` | Override the available balance used in payment schedule calculations |
| `Product` | `AA_ProductApi.jar` | `getVersion` | `java.lang.String` | Product API — access published product catalog records |
| `Product` | `AA_ProductApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Product` | `AA_ProductApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Product` | `AA_ProductApi.jar` | `setProductId` | `void` | Set the product ID context |
| `Product` | `AA_ProductApi.jar` | `getProductId` | `java.lang.String` | Get the current product ID |
| `Product` | `AA_ProductApi.jar` | `getProduct` | `com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord` | Get the AA.PRODUCT.CATALOG record |
| `Property` | `AA_PropertyApi.jar` | `getVersion` | `java.lang.String` | Property API — access property definitions for an arrangement |
| `Property` | `AA_PropertyApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Property` | `AA_PropertyApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Property` | `AA_PropertyApi.jar` | `setPropertyId` | `void` | Set the property ID context |
| `Property` | `AA_PropertyApi.jar` | `getPropertyId` | `java.lang.String` | Get the current property ID |
| `Property` | `AA_PropertyApi.jar` | `getPropertyClassId` | `java.lang.String` | Get the property class ID for this property |
| `Property` | `AA_PropertyApi.jar` | `getPropertiesForProduct` | `com.temenos.api.TStructure` | Get all properties defined for a product |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getVersion` | `java.lang.String` | PropertyClass API — access property class definitions |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `setPropertyClassId` | `void` | Set the property class ID context |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getPropertyClassId` | `java.lang.String` | Get the current property class ID |
| `PropertyClass` | `AA_PropertyClassApi.jar` | `getPropertyIdsForProduct` | `java.util.List<java.lang.String>` | Get all property IDs of this class for a product |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getVersion` | `java.lang.String` | RuleComparison hook — compare arrangement values against product defaults |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getComparableValues` | `void` | Provide custom comparable values for rule evaluation |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `compareNegotiatedValue` | `void` | Compare a negotiated value against the product default |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `validateNegotiableField` | `void` | Validate whether a field value is within negotiation bounds |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getRelatedArrangements` | `void` | Return related arrangements for comparison (preferential pricing) |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getDormancyException` | `com.temenos.t24.api.complex.aa.rulecomparisonhook.DormancyResponse` | Override dormancy processing for specific accounts |
| `RuleComparison` | `AA_RuleComparisonHook.jar` | `getComparableStringValues` | `void` | Provide string-type comparable values |
| `Settlement` | `AA_SettlementHook.jar` | `getVersion` | `java.lang.String` | Settlement hook — validate or override settlement processing |
| `Settlement` | `AA_SettlementHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `Settlement` | `AA_SettlementHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Settlement` | `AA_SettlementHook.jar` | `validateUserRoutine` | `void` | Custom validation during settlement; return exceptions if any |

---

## Key T24 Applications

| Application | Purpose |
|------------|---------|
| `AA.ARRANGEMENT` | Arrangement master record |
| `AA.ARRANGEMENT.ACTIVITY` | Activity input and log application; ID: AAACTYYDDDxxxxx |
| `AA.ARR.<PROPERTY.CLASS>` | Live arrangement conditions per property class |
| `AA.SIM.<PROPERTY.CLASS>` | Simulated arrangement conditions |
| `AA.PRD.DES.<CLASS>` | Product condition definitions (designer) |
| `AA.PRD.PRF.<CLASS>` | Proofed product conditions |
| `AA.PRD.CAT.<CLASS>` | Published/catalogued product conditions |
| `AA.ACCOUNT.DETAILS` | Arrangement status, linked account number |
| `AA.PRODUCT` | Product definition, proof/publish status |
| `AA.PRODUCT.CATALOG` | Published product catalog |
| `AA.ACTIVITY.HISTORY` | Full activity log per arrangement |
| `AA.BILL.DETAILS` | Bill records (charge/fee demands); statuses: DUE, PAID, OVERDUE |
| `AA.SCHEDULED.ACTIVITY` | Scheduled activity queue per arrangement |
| `AA.CUSTOMER.ARRANGEMENT` | Cross-reference: customer to arrangement |
| `AA.MASS.CUSTOMER.ARRANGEMENT` | High-volume non-beneficial owner cross-reference |
| `AA.CUSTOMER.RELATED.ARRANGEMENTS` | Related customers per arrangement (R20+) |
| `AA.SIMULATION.CAPTURE` | Simulation data capture application |
| `AA.SIMULATION.RUNNER` | Simulation execution controller |
| `AA.ARRANGEMENT.SIM` | Simulated arrangement master |
| `AA.ACTIVITY.HISTORY.SIM` | Simulated activity log |
| `AA.PRODUCT.TRACKER.CATALOG` | Product change tracking for arrangement updates |
| `AA.PRODUCT.TRACKER.PROOF` | Product change tracking during proof stage |
| `EB.CONTRACT.BALANCES` | Current balance amounts by type; ID = AA Account ID |
| `ACCT.BALANCE.ACTIVITY` | Balance history by account + balance type |
| `AC.BALANCE.TYPE` | Balance type definitions (CONTINGENT, NON-CONTINGENT, INTERNAL, VIRTUAL) |
| `AC.ALLOCATION.RULE` | Accounting event → entry mapping rules |
| `AC.POSTING.DETAIL` | Entry content configuration (references, narratives) |

---

## JAR Inventory

| JAR | Class Count | Component Types Present |
|-----|-------------|------------------------|
| `AA_AaActivityExtractorService.jar` | 7 | unknown |
| `AA_Account.jar` | 165 | unknown |
| `AA_Accounting.jar` | 55 | unknown |
| `AA_ActivityAPI.jar` | 18 | unknown |
| `AA_ActivityCharges.jar` | 39 | unknown |
| `AA_ActivityControl.jar` | 6 | unknown |
| `AA_ActivityHook.jar` | 11 | public-api, unknown |
| `AA_ActivityMapping.jar` | 11 | unknown |
| `AA_ActivityMessaging.jar` | 49 | unknown |
| `AA_ActivityPresentation.jar` | 12 | unknown |
| `AA_ActivityRestriction.jar` | 31 | unknown |
| `AA_AgentCommission.jar` | 52 | unknown |
| `AA_Alerts.jar` | 18 | unknown |
| `AA_ARAccountsData.jar` | 4 | unknown |
| `AA_ARC.jar` | 43 | unknown |
| `AA_BalanceAvailability.jar` | 15 | unknown |
| `AA_BalanceMaintenance.jar` | 28 | unknown |
| `AA_BillApi.jar` | 3 | public-api, unknown |
| `AA_BundleHierarchy.jar` | 48 | unknown |
| `AA_CalculationHook.jar` | 14 | public-api, unknown |
| `AA_ChangeProduct.jar` | 17 | unknown |
| `AA_ChannelAccess.jar` | 11 | unknown |
| `AA_Channels.jar` | 13 | unknown |
| `AA_ChargeOff.jar` | 32 | unknown |
| `AA_ChargeOverride.jar` | 14 | unknown |
| `AA_ClassicProducts.jar` | 102 | unknown |
| `AA_Closure.jar` | 26 | unknown |
| `AA_Constraint.jar` | 21 | unknown |
| `AA_ContractApi.jar` | 59 | public-api, unknown |
| `AA_Customer.jar` | 68 | unknown |
| `AA_DepositData.jar` | 4 | unknown |
| `AA_Dormancy.jar` | 50 | unknown |
| `AA_Eligibility.jar` | 24 | unknown |
| `AA_EventStructures.jar` | 63 | unknown |
| `AA_Evidence.jar` | 21 | unknown |
| `AA_ExchangeRate.jar` | 14 | unknown |
| `AA_Facility.jar` | 27 | unknown |
| `AA_Feature.jar` | 42 | unknown |
| `AA_Fees.jar` | 127 | unknown |
| `AA_Framework.jar` | 837 | unknown |
| `AA_Inheritance.jar` | 11 | unknown |
| `AA_IntegrationFramework.jar` | 39 | unknown |
| `AA_Interest.jar` | 258 | unknown |
| `AA_InterestCompensation.jar` | 17 | unknown |
| `AA_Interfaces.jar` | 13 | unknown |
| `AA_LendingData.jar` | 3 | unknown |
| `AA_Limit.jar` | 62 | unknown |
| `AA_MarketingCatalogue.jar` | 86 | unknown |
| `AA_ModelBank.jar` | 437 | unknown |
| `AA_ModelBankBb.jar` | 5 | unknown |
| `AA_NoticeWithdrawal.jar` | 21 | unknown |
| `AA_Officers.jar` | 11 | unknown |
| `AA_Overdue.jar` | 49 | unknown |
| `AA_Participant.jar` | 54 | unknown |
| `AA_PaymentHoliday.jar` | 15 | unknown |
| `AA_PaymentPriority.jar` | 28 | unknown |
| `AA_PaymentRules.jar` | 47 | unknown |
| `AA_PaymentSchedule.jar` | 332 | unknown |
| `AA_PaymentScheduleHook.jar` | 3 | public-api, unknown |
| `AA_Payoff.jar` | 36 | unknown |
| `AA_PayoutRules.jar` | 17 | unknown |
| `AA_PeriodicCharges.jar` | 65 | unknown |
| `AA_PreferentialPricing.jar` | 12 | unknown |
| `AA_PreferentialPricingFx.jar` | 8 | unknown |
| `AA_PricingAdjustments.jar` | 11 | unknown |
| `AA_PricingGrid.jar` | 30 | unknown |
| `AA_PricingRules.jar` | 53 | unknown |
| `AA_ProductApi.jar` | 3 | public-api, unknown |
| `AA_ProductAttribute.jar` | 42 | unknown |
| `AA_ProductBundle.jar` | 40 | unknown |
| `AA_ProductCommission.jar` | 14 | unknown |
| `AA_ProductFramework.jar` | 117 | unknown |
| `AA_ProductImporter.jar` | 32 | unknown |
| `AA_ProductManagement.jar` | 125 | unknown |
| `AA_PromotionRules.jar` | 21 | unknown |
| `AA_PropertyApi.jar` | 4 | public-api, unknown |
| `AA_PropertyClassApi.jar` | 3 | public-api, unknown |
| `AA_PropertyControl.jar` | 12 | unknown |
| `AA_Quotation.jar` | 58 | unknown |
| `AA_Reporting.jar` | 59 | unknown |
| `AA_RestructureRules.jar` | 24 | unknown |
| `AA_RuleComparisonHook.jar` | 8 | public-api, unknown |
| `AA_Rules.jar` | 99 | unknown |
| `AA_SafeDepositBox.jar` | 12 | unknown |
| `AA_SeatInfra.jar` | 7 | unknown |
| `AA_Services.jar` | 31 | unknown |
| `AA_Settlement.jar` | 112 | unknown |
| `AA_SettlementHook.jar` | 3 | public-api, unknown |
| `AA_ShareTransfer.jar` | 15 | unknown |
| `AA_SplitsMerges.jar` | 27 | unknown |
| `AA_Statement.jar` | 26 | unknown |
| `AA_SubArrangementCondition.jar` | 12 | unknown |
| `AA_SubArrangementRules.jar` | 13 | unknown |
| `AA_SubLimits.jar` | 13 | unknown |
| `AA_Swift.jar` | 9 | unknown |
| `AA_Tax.jar` | 42 | unknown |
| `AA_TermAmount.jar` | 124 | unknown |
| `AA_TransactionRules.jar` | 5 | unknown |
| `AA_Util.jar` | 69 | unknown |
