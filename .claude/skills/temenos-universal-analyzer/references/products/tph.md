# TPH — Transaction Processing Hub Reference

> Manually curated 2026-06-20. Sources: TPH Core.txt, JAR analysis, T24 Technical Training.

---

## Architecture Overview

TPH is Temenos's payment hub layer, sitting between originating channels (TCIB, mobile, core apps) and clearing networks (SWIFT, RTGS, ACH, Instant). It provides routing, enrichment, message transformation, and adapter management.

```
Originating Channel       TPH Middle Office              Clearing Network
─────────────────    ───────────────────────────    ────────────────────
  PAYMENT ORDER  →   Accept → Map → Prepare        →   SWIFT
  (Front Office)      → Process → Filter           →   RTGS (TARGET2, FEDWIRE)
                      → Post → Generate            →   SEPA/ACH
  TRANSACT       ←   Finalise (Back Office)        →   Instant (pacs.008)
```

**Key distinction:**
- **PAYMENT ORDER (PO)** = Front Office — customer-initiated payment instruction
- **PAYMENT HUB (TPH)** = Middle Office — routing and processing
- **TRANSACT** = Back Office — accounting and settlement

---

## Architecture Stages

| # | Stage | Description |
|---|-------|-------------|
| 1 | **Acceptance** | Receive payment messages/files; de-bulk batch files; Accept or Reject |
| 2 | **Mapping** | Parse and map to TPH internal neutral format (ISO 20022 base) |
| 3 | **Preparation** | Duplicate detection, priority setting, format validation |
| 4 | **Processing** | Automatic exception handling, routing selection, settlement choice |
| 5 | **Filtering** | Regulatory / sanctions / AML screening |
| 6 | **Fees, FX & Posting** | Fee calculation, FX conversion, own-ledger postings |
| 7 | **Message & File Generation** | Format outbound messages (MT103, pacs.008, ACH NACHA, etc.) |
| 8 | **Finalisation** | Reconciliation, reports, archiving |

---

## Key Applications

| Application | Purpose |
|------------|---------|
| `TP.PAYMENT.ORDER` | Core TPH payment order record (input and processing) |
| `PP.PAYMENT` | Processed payment record |
| `PP.PAYMENT.BENEFICIARY` | Beneficiary information |
| `PP.PAYMENT.DEBIT` | Debit-side details |
| `PP.PAYMENT.SETTLEMENT` | Settlement instructions and status |
| `PP.PAYMENT.FEES` | Computed fees per payment |
| `PP.ROUTING.RULES` | Routing rule configuration |
| `PP.CLEARING.CHANNEL` | Clearing channel definition |
| `PP.PAYMENT.TYPES` | Payment type configuration |

---

## Key Classes (from JAR Analysis)

| Class | JAR | Package | Role |
|-------|-----|---------|------|
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `com.temenos.t24.api.hook` | Hook on PAYMENT.ORDER input lifecycle |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `com.temenos.t24.api.hook.payments` | Hook on payment processing lifecycle |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `com.temenos.t24.api.hook.payments` | Hook on payment order lifecycle |

---

## Java Hook Development

### PaymentOrderLifecycle — Hook on TP.PAYMENT.ORDER

Extend `PaymentOrderLifecycle` (from `PI_PaymentOrderLifecycleHook.jar`) to customise payment order processing:

```java
package com.mybank.payments;

import com.temenos.t24.api.hook.payments.PaymentOrderLifecycle;
import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;

public class PaymentOrderValidationHook extends PaymentOrderLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, /* context params */) {

        // Validate payment order fields
        // Access TP.PAYMENT.ORDER record fields via generated record class
        return super.validateRecord(...);
    }
}
```

### PaymentLifecycle — Hook on PP.PAYMENT

Extend `PaymentLifecycle` (from `PP_PaymentLifecycleHook.jar`) to hook into payment processing:

```java
package com.mybank.payments;

import com.temenos.t24.api.hook.payments.PaymentLifecycle;

public class PaymentProcessingHook extends PaymentLifecycle {

    @Override
    public void postUpdateRequest(/* payment lifecycle params */) {
        // Post-authorise: update ledger, send notification, etc.
    }
}
```

---

## Payment Order Lifecycle

| Stage | Hook Point | Description |
|-------|-----------|-------------|
| Input | `PaymentOrderLifecycle.defaultFieldValues` | Set defaults on payment order |
| Validate | `PaymentOrderLifecycle.validateRecord` | Validate business rules |
| Process | TPH engine stages 1–8 | Automatic routing and processing |
| Settle | `PaymentLifecycle.updateRecord` | Post settlement entries |
| Confirm | `PaymentLifecycle.postUpdateRequest` | Send confirmations |

---

## Supported Payment Types

| Category | Types |
|----------|-------|
| Customer Credit Transfer | Domestic, International (SWIFT MT103, ISO pacs.008) |
| Bank Transfer | MT202, pacs.009 |
| Direct Debit | SEPA SDD, UK BACS DD |
| Bulk/Batch | Salary upload, utility batch |
| RTGS | TARGET2, FEDWIRE, CHATS, SARIE |
| Instant | SEPA Instant (pacs.008), UK FPS |
| Standing Orders | Recurring credit transfers |

---

## Supported Clearing Systems

| Region | System | Protocol |
|--------|--------|---------|
| Global | SWIFT | MT103, MT202, MT202COV, MX ISO 20022 |
| EU | TARGET2 RTGS | ISO 20022 |
| EU | SEPA SCT/SDD | PAIN/PACS XML |
| US | FEDWIRE | Proprietary |
| UK | BACS / FPS | BACSTEL-IP, ISO 20022 |
| HK | CHATS | ISO 20022 |
| SA | SARIE | Proprietary |

---

## Routing Rules

Routing in TPH is configured via `PP.ROUTING.RULES`. Key routing criteria:

| Criterion | Description |
|-----------|-------------|
| Payment type | CREDIT.TRANSFER, DIRECT.DEBIT |
| Currency | ISO currency code |
| Country | Beneficiary/debit country |
| Amount threshold | Route large payments to RTGS |
| Customer segment | Priority routing for VIP customers |
| Correspondent bank | BIC-based routing |

---

## OFS Integration — Submit to TPH

Payments can be initiated from jBC via OFS to `TP.PAYMENT.ORDER`:

```basic
OFS.MSG  = 'TP.PAYMENT.ORDER,CUSTOMER.TRANSFER//'
OFS.MSG := 'PAYMENT.TYPE:::CREDIT.TRANSFER/'
OFS.MSG := 'DEBIT.ACCOUNT:::' : DEBIT.ACCOUNT : '/'
OFS.MSG := 'CREDIT.ACCOUNT:::' : CREDIT.ACCOUNT : '/'
OFS.MSG := 'PAYMENT.CURRENCY:::' : CURRENCY : '/'
OFS.MSG := 'PAYMENT.AMOUNT:::' : AMOUNT : '/'
OFS.MSG := 'VALUE.DATE:::' : VALUE.DATE : '/'
OFS.MSG := 'BENEFICIARY.NAME:::' : BEN.NAME : '/'
OFS.MSG := 'BENEFICIARY.BIC:::' : BEN.BIC : '/'
CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)

OFS.STAT = FIELD(FIELD(OFS.MSG,'/',3),',',1)
IF OFS.STAT EQ 1 THEN
    PO.ID = FIELD(OFS.MSG,'/',1)
END
```

---

## TPH Dependencies

| Component | Depends On |
|-----------|-----------|
| TPH Middle Office | TRANSACT core (CUSTOMER, ACCOUNT, FUNDS.TRANSFER) |
| Payment Order | Customer validation (ST module), Account validation (AC module) |
| Settlement | FUNDS.TRANSFER module, FX rates (ST module) |
| SWIFT messaging | SWIFT Alliance gateway or SWIFTNet link |
| Instant payments | Clearing house API adapter |

---

## Key jBC Patterns (TPH Routines)

TPH calls custom jBC routines at extension points:

```basic
* TPH routing extension — maps DEBIT.COLLECTION to TPH
SUBROUTINE DD.MAPPING.TO.TPH(DD.ID, TPH.MSG, ERR)

    $INSERT I_COMMON
    $INSERT I_EQUATE

    DD.AMT  = ''   ;* extract from DD record
    DD.DATE = ''

    * Build TPH payment order OFS
    OFS.MSG  = 'TP.PAYMENT.ORDER,DD.INITIATION//'
    OFS.MSG := 'PAYMENT.TYPE:::DIRECT.DEBIT/'
    OFS.MSG := 'PAYMENT.AMOUNT:::' : DD.AMT : '/'
    OFS.MSG := 'VALUE.DATE:::' : DD.DATE : '/'
    CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)

    ERR = ''
    RETURN
END
```
