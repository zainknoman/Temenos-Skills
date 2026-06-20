# jbc-componentise Skill — Developer Reference

A Claude skill for writing, customising, reviewing, and debugging Temenos T24 jBC componentisation code. Works with any T24 package and covers all component artefact types.

---

## Quick Start

Type `/jbc-componentise` followed by your request. The skill detects whether you want to **develop** new code, **customise** existing code, or **review/debug** a routine.

```
/jbc-componentise Create a REST GET API that returns loan details for a given loan ID
/jbc-componentise Add a dateOpened field to the existing GetAccountDetails component
/jbc-componentise Review this .b file and tell me why it always returns an empty response
```

---

## How the Skill Works

The skill runs a structured workflow for new development:

```
Phase 0   →  Parse the business requirement
Phase 1   →  Dispatch 4 parallel sub-agents (data model, output schema, process flow, REST design)
Phase 2   →  Classify each operation and select the correct template
Phase 3   →  Generate the .component declaration file
Phase 3b  →  Generate the .complex DTO file (if methods use typed return/request objects)
Phase 4   →  Generate the .b implementation file(s)
Phase 5   →  Validate all files against the T24 jBC checklist
```

For customisation and review, the skill skips to the relevant phase and applies targeted changes or analysis.

### Output file types

| File | Purpose |
|------|---------|
| `<Name>.component` | Component declaration — artefacts, methods, REST annotations |
| `<NAME>.b` | jBC implementation — FUNCTION or SUBROUTINE |
| `<Namespace>.complex` | DTO class definitions used as typed return/request types in REST methods |

---

## Use Case 1: DEVELOPMENT — Writing New Code

### Example 1.1 — Simple REST GET API

**Prompt:**
```
/jbc-componentise
Package: MY.PROJECT
Create a REST GET API that accepts a customer ID and returns the customer's
full name, date of birth, nationality, and sector code from ST.Customer.
```

**What the skill produces:**

*`MyDTOs.complex`*
```
complex MyDTOs

@Containment byValue
classes {

    CustomerProfile
    {
        fullName    : string
        dateOfBirth : string
        nationality : string
        sectorCode  : string
    }

}
```

*`GetCustomerProfile.component`*
```
component MY.PROJECT.GetCustomerProfile
metamodelVersion 1.6

    public table Customer {
        t24: ST.Customer
        fields: {
            Name1       = 2
            DateOfBirth = 18
            Nationality = 14
            SectorCode  = 21
        }
    }

    public table GetCustomerProfile {
        t24: MY.PROJECT.GetCustomerProfile
        fields: {
            fullName    = 1
            dateOfBirth = 2
            nationality = 3
            sectorCode  = 4
        }
    }

    @Response("")
    @Path("/customers/{customerId}/profile")
    @GET
    #@RolesAllowed("api-admin")
    public method getCustomerProfile : MyDTOs:CustomerProfile (

        @QueryParam("customerId")
        IN customerId string

    )
    {
        jBC: MY.PKG.GET.CUSTOMER.PROFILE
    }
```

*`MY.PKG.GET.CUSTOMER.PROFILE.b`*
```jBC
* @ValidationCode : 
* @ValidationInfo : Timestamp         : 18 Jun 2026 09:00:00
* @ValidationInfo : Encoding          : Cp1252
* @ValidationInfo : User Name         : Convenience
* @ValidationInfo : Nb tests success  : N/A
* @ValidationInfo : Nb tests failure  : N/A
* @ValidationInfo : Rating            : N/A
* @ValidationInfo : Coverage          : N/A
* @ValidationInfo : Strict flag       : true
* @ValidationInfo : Bypass GateKeeper : false
* @ValidationInfo : Compiler Version  : R22_AMR.0
* @ValidationInfo : Copyright Temenos Headquarters SA 1993-2021. All rights reserved.
$PACKAGE MY.PROJECT
*
* Implementation of MY.PROJECT.GetCustomerProfile.getCustomerProfile
*
* customerId(IN) : T24 customer mnemonic or number
*
FUNCTION MY.PKG.GET.CUSTOMER.PROFILE(customerId)
*-----------------------------------------------------------------------------
* @author - Jane Developer - jane@mybank.com
* @for    - My Bank (June 2026)
* @Client - My Bank
*------------------------------------------------------------------------------

    $USING EB.SystemTables
    $USING EB.API
    $USING EB.DataAccess
    $USING ST.Customer
*-----------------------------------------------------------------------------
    IF MY.PROJECT.getinitialised() NE 'Y' THEN
        MY.PROJECT.initialiseProject()
    END

    custRecord = ST.Customer.Customer.Read(customerId, custError)

    fullName    = custRecord<ST.Customer.Customer.Name1>
    dateOfBirth = custRecord<ST.Customer.Customer.DateOfBirth>
    nationality = custRecord<ST.Customer.Customer.Nationality>
    sectorCode  = custRecord<ST.Customer.Customer.SectorCode>

    outRecord<MY.PROJECT.GetCustomerProfile.fullName>    = fullName
    outRecord<MY.PROJECT.GetCustomerProfile.dateOfBirth> = dateOfBirth
    outRecord<MY.PROJECT.GetCustomerProfile.nationality> = nationality
    outRecord<MY.PROJECT.GetCustomerProfile.sectorCode>  = sectorCode

RETURN outRecord
```

---

### Example 1.2 — REST POST API (OFS Transaction)

**Prompt:**
```
/jbc-componentise
Package: CORP.PAYMENTS
Create a REST POST API that accepts a debit account, credit account,
amount, currency, and narrative, then creates a FUNDS.TRANSFER record
in T24. Return the transaction ID and status.
```

**What the skill produces:**

*`CorpDTOs.complex`*
```
complex CorpDTOs

@Containment byValue
classes {

    TransferRequest
    {
        debitAccount  : string
        creditAccount : string
        amount        : string
        currency      : string
        narrative     : string
    }

    TransferResponse
    {
        transactionId : string
        status        : string
    }

}
```

*`ProcessTransfer.component`* (excerpt)
```
component CORP.PAYMENTS.ProcessTransfer
metamodelVersion 1.6

    private constant ofsSource { value: '<OFS.SOURCE.NAME>' }

    @Response("")
    @Path("/transfers")
    @POST
    public method processTransfer : CorpDTOs:TransferResponse (

        @RequestBody
        IN transferDetails CorpDTOs:TransferRequest

    )
    {
        jBC: CORP.PMT.PROCESS.TRANSFER
    }
```

*`CORP.PMT.PROCESS.TRANSFER.b`* (excerpt)
```jBC
$PACKAGE CORP.PAYMENTS
*
* Implementation of CORP.PAYMENTS.ProcessTransfer.processTransfer
*
FUNCTION CORP.PMT.PROCESS.TRANSFER(transferDetails)

    $USING EB.SystemTables
    $USING EB.API
    $USING EB.DataAccess
    $USING EB.Foundation
    $USING EB.Interface
    $USING FT.Contract
*-----------------------------------------------------------------------------
    IF CORP.PAYMENTS.getinitialised() NE 'Y' THEN
        CORP.PAYMENTS.initialisePayments()
    END

    R.FT = ''
    R.FT<FT.Contract.FundsTransfer.DebitAcctNo>   = transferDetails<CORP.PAYMENTS.ProcessTransferRequest.debitAccount>
    R.FT<FT.Contract.FundsTransfer.CreditAcctNo>  = transferDetails<CORP.PAYMENTS.ProcessTransferRequest.creditAccount>
    R.FT<FT.Contract.FundsTransfer.DebitAmount>   = transferDetails<CORP.PAYMENTS.ProcessTransferRequest.amount>
    R.FT<FT.Contract.FundsTransfer.DebitCurrency> = transferDetails<CORP.PAYMENTS.ProcessTransferRequest.currency>
    R.FT<FT.Contract.FundsTransfer.PaymentDetails>= transferDetails<CORP.PAYMENTS.ProcessTransferRequest.narrative>

    AppName       = 'FUNDS.TRANSFER'
    Ofsfunct      = 'I'
    Process       = 'PROCESS'
    OfsVersion    = 'FUNDS.TRANSFER,STANDARD'
    Gtsmode       = ''
    NoOfAuth      = ''
    transactionId = ''

    Options<1> = CORP.PAYMENTS.ofsSource

    EB.Foundation.OfsBuildRecord(AppName, Ofsfunct, Process, OfsVersion, Gtsmode, NoOfAuth, transactionId, R.FT, OfsRecord)
    EB.Interface.OfsCallBulkManager(Options, TheRequest, TheResponse, TxnCommitted)

    IF TxnCommitted EQ '1' THEN
        output<CORP.PAYMENTS.ProcessTransferResponse.transactionId> = transactionId
        output<CORP.PAYMENTS.ProcessTransferResponse.status>        = TheResponse
    END ELSE
        output<CORP.PAYMENTS.ProcessTransferResponse.status> = TheResponse
    END

RETURN output
```

---

### Example 1.3 — Enquiry / Search API (date range filter)

**Prompt:**
```
/jbc-componentise
Package: RETAIL.BANKING
Create a REST GET API that accepts an account number, start date,
and end date, then returns a list of statement entries between those dates.
Use EB.DataAccess.QueryBuilder on the STMT.ENTRY application.
```

**What the skill produces:**

*`RetailDTOs.complex`*
```
complex RetailDTOs

@Containment byValue
classes {

    StatementEntry
    {
        entryDate    : string
        description  : string
        debitAmount  : string
        creditAmount : string
        balance      : string
    }

}
```

*`GetAccountStatement.component`* (excerpt)
```
component RETAIL.BANKING.GetAccountStatement
metamodelVersion 1.6

    @Response("")
    @Path("/accounts/{accountId}/statement")
    @GET
    #@RolesAllowed("api-admin")
    public method getAccountStatement : list<RetailDTOs:StatementEntry> (

        @QueryParam("accountId")
        IN accountId string

        @QueryParam("startDate")
        IN startDate date

        @QueryParam("endDate")
        IN endDate date

    )
    {
        jBC: RB.GET.ACCOUNT.STATEMENT
    }
```

*`RB.GET.ACCOUNT.STATEMENT.b`* (key section)
```jBC
    GOSUB INITIALISE
    GOSUB QUERY.ENTRIES
    GOSUB PROCESS.ENTRIES

RETURN outRecord

*-----------------------------------------------------------------------------
INITIALISE:
    outRecord   = ''
    resultSet   = ''
    entryCount  = 0
RETURN

*-----------------------------------------------------------------------------
QUERY.ENTRIES:
    queryId = EB.DataAccess.QueryBuilder('STMT.ENTRY', '')
    EB.DataAccess.QueryCondition(queryId, 'ACCOUNT.NO', 'EQ', accountId)
    EB.DataAccess.QueryCondition(queryId, 'BOOKING.DATE', 'GE', startDate)
    EB.DataAccess.QueryCondition(queryId, 'BOOKING.DATE', 'LE', endDate)
    resultSet = EB.DataAccess.BatchBuildList(queryId, '')
RETURN

*-----------------------------------------------------------------------------
PROCESS.ENTRIES:
    LOOP
        REMOVE entryId FROM resultSet SETTING moreRecords
    WHILE entryId NE '' DO
        entryRecord = STMT.ENTRY.StmtEntry.Read(entryId, entryError)
        entryCount += 1

        outRecord<RETAIL.BANKING.GetAccountStatement.entryDate,   entryCount> = entryRecord<STMT.ENTRY.StmtEntry.BookingDate>
        outRecord<RETAIL.BANKING.GetAccountStatement.description, entryCount> = entryRecord<STMT.ENTRY.StmtEntry.Description>
        outRecord<RETAIL.BANKING.GetAccountStatement.debitAmount, entryCount> = entryRecord<STMT.ENTRY.StmtEntry.DebitAmount>
        outRecord<RETAIL.BANKING.GetAccountStatement.creditAmount,entryCount> = entryRecord<STMT.ENTRY.StmtEntry.CreditAmount>
        outRecord<RETAIL.BANKING.GetAccountStatement.balance,     entryCount> = entryRecord<STMT.ENTRY.StmtEntry.RunningBalance>
    REPEAT
RETURN
```

---

### Example 1.4 — Validation Hook

**Prompt:**
```
/jbc-componentise
Package: TRADE.FINANCE
Create a validation routine that checks a letter of credit's expiry date
field. If the expiry date is in the past, set an error message.
This attaches to the LC.ISSUANCE application as a VALIDATION.ROUTINE.
```

**What the skill produces:**

*`ValidateLCExpiry.component`* (excerpt)
```
component TRADE.FINANCE.ValidateLCExpiry
metamodelVersion 1.6

    public method validateLCExpiry(
        INOUT record string,
        OUT   errorCode string
    ) {
        jBC: TF.V.LC.EXPIRY.VALIDATION
    }
```

*`TF.V.LC.EXPIRY.VALIDATION.b`*
```jBC
$PACKAGE TRADE.FINANCE
*
* Implementation of TRADE.FINANCE.ValidateLCExpiry.validateLCExpiry
*
SUBROUTINE TF.V.LC.EXPIRY.VALIDATION

    $USING EB.SystemTables
*-----------------------------------------------------------------------------
    expiryDate = EB.SystemTables.getRNew('EXPIRY.DATE', '', 1, '')
    today      = EB.SystemTables.getRNew('TODAY', '', 1, '')

    IF expiryDate LT today THEN
        EB.SystemTables.setE('LC.ISSUANCE ':expiryDate:' EXPIRY DATE CANNOT BE IN THE PAST')
    END

RETURN
```

---

### Example 1.5 — Template Definition (custom application schema)

**Prompt:**
```
/jbc-componentise
Package: CORP.FINANCE
Create a template definition routine that defines the structure of a
custom application called CORP.PAYMENT.INSTRUCTION with fields:
PayerName (Alpha, 100, mandatory), PayeeAccount (Alpha, 35, mandatory),
PaymentAmount (Amount, 18, mandatory), PaymentDate (Date, 11, optional),
Reference (Alpha, 50, optional).
```

**What the skill produces:**

*`TF.CORP.PAY.INST.PARAM.b`*
```jBC
$PACKAGE CORP.FINANCE
*
* Implementation of CORP.FINANCE.DefinePaymentInstruction.defineSchema
*
SUBROUTINE CORP.FIN.PAYMENT.INSTRUCTION.PARAM

    $USING EB.Template
*-----------------------------------------------------------------------------
    EB.Template.setTableId('CORP.PAYMENT.INSTRUCTION')
    EB.Template.setTableDescription('Corporate Payment Instruction — custom application')
    EB.Template.setTableSysId('CF')

    EB.Template.setTableField(1, 'PAYER.NAME',       'Payer full name',            'A',  '100', 'Y')
    EB.Template.setTableField(2, 'PAYEE.ACCOUNT',    'Beneficiary account number', 'A',  '35',  'Y')
    EB.Template.setTableField(3, 'PAYMENT.AMOUNT',   'Payment amount',             'AM', '18',  'Y')
    EB.Template.setTableField(4, 'PAYMENT.DATE',     'Payment value date',         'D',  '11',  'N')
    EB.Template.setTableField(5, 'REFERENCE',        'Payment reference',          'A',  '50',  'N')

RETURN
```

---

### Example 1.6 — Document Engine Handler

**Prompt:**
```
/jbc-componentise
Package: DOCS.ENGINE
Create a DE handoff routine that populates a print job for a Funds Transfer
advice. It must read the FT record (with history fallback), extract the
debit account, credit account, amount, currency, value date, and narrative,
then call DE.API.ApplicationHandoff for each field in order.
```

**What the skill produces:**

*`DOCS.DE.FT.ADVICE.DETAILS.b`* (key sections)
```jBC
$PACKAGE DOCS.ENGINE
*
SUBROUTINE DOCS.DE.FT.ADVICE.DETAILS(handOffRecord, errorMsg)

    $USING EB.SystemTables
    $USING EB.API
    $USING EB.DataAccess
    $USING DE.API
    $USING FT.Contract
*-----------------------------------------------------------------------------
    GOSUB PREP
    GOSUB GET.FT.DATA
    GOSUB BUILD.HANDOFF.VALUES
RETURN

*-----------------------------------------------------------------------------
PREP:
    errorMsg      = ''
    transactionId = handOffRecord<DE.API.HandoffRec.transactionId>
RETURN

*-----------------------------------------------------------------------------
GET.FT.DATA:
    ftRecord = FT.Contract.FundsTransfer.Read(transactionId, ftError)
    IF ftError THEN
        ftRecord = FT.Contract.FundsTransfer.ReadHis(transactionId, ftError)
    END
RETURN

*-----------------------------------------------------------------------------
BUILD.HANDOFF.VALUES:
    handOffValues    = ''
    handOffValues<1> = ftRecord<FT.Contract.FundsTransfer.DebitAcctNo>
    handOffValues<2> = ftRecord<FT.Contract.FundsTransfer.CreditAcctNo>
    handOffValues<3> = ftRecord<FT.Contract.FundsTransfer.DebitAmount>
    handOffValues<4> = ftRecord<FT.Contract.FundsTransfer.DebitCurrency>
    handOffValues<5> = ftRecord<FT.Contract.FundsTransfer.ValueDate>
    handOffValues<6> = ftRecord<FT.Contract.FundsTransfer.PaymentDetails>

    noOfFields = DCOUNT(handOffValues, @FM)
    FOR i = 1 TO noOfFields
        DE.API.ApplicationHandoff(handOffRecord, i, handOffValues<i>, errorMsg)
    NEXT i
RETURN
```

---

## Use Case 2: CUSTOMISE — Extending Existing Code

### Example 2.1 — Add a new field to an existing GET API

**Prompt:**
```
/jbc-componentise
Package: MY.PROJECT
I have an existing GetAccountDetails component that returns accountTitle,
workingBalance, and customer. I need to add a new field: availableBalance
from AC.AccountOpening position 16. Update both the .component file and
the .b file.
```

**What the skill does:**
1. Asks you to paste (or reads) the existing `.component` and `.b` files
2. Identifies the exact insertion points
3. Adds `availableBalance = 4` to the `GetAccountDetails` output table
4. Adds `$USING` for any new namespace needed (none in this case)
5. Adds the field extraction and outRecord assignment lines
6. Runs Phase 5 checklist on the modified files

**Targeted changes only — nothing else is restructured.**

---

### Example 2.2 — Add REST annotations to a non-REST method

**Prompt:**
```
/jbc-componentise
Package: CORP.FINANCE
This existing method in my component is not REST-exposed. Add GET REST
annotations to it so it can be called from a mobile app.

Existing component artefact:
    public method getLoanSummary (
        IN loanId string
    )
    {
        jBC: CF.GET.LOAN.SUMMARY
    }
```

**What the skill produces:**

```
    @Response("")
    @Path("/loans/{loanId}/summary")
    @GET
    #@RolesAllowed("api-admin")
    public method getLoanSummary : FinanceDTOs:LoanSummary (

        @QueryParam("loanId")
        IN loanId string

    )
    {
        jBC: CF.GET.LOAN.SUMMARY
    }
```

The `.b` file does not need to change — REST annotations are purely in the `.component` declaration. If a typed return type is added (`FinanceDTOs:LoanSummary`), the class must exist in the corresponding `.complex` file.

---

### Example 2.3 — Add a second method to an existing component

**Prompt:**
```
/jbc-componentise
Package: RETAIL.BANKING
My existing GetAccountDetails component has one method. I need to add a
second REST GET method: getAccountCurrency, which accepts accountId and
returns just the currency code from AC.AccountOpening position 12.
```

**What the skill produces:**

Additional class appended to the existing `.complex` file:
```
    AccountCurrency
    {
        currency : string
    }
```

Additional artefacts appended to the existing `.component` file:
```
    @Response("")
    @Path("/accounts/{accountId}/currency")
    @GET
    #@RolesAllowed("api-admin")
    public method getAccountCurrency : RetailDTOs:AccountCurrency (

        @QueryParam("accountId")
        IN accountId string

    )
    {
        jBC: RB.GET.ACCOUNT.CURRENCY
    }
```

Plus a new `RB.GET.ACCOUNT.CURRENCY.b` implementation file.

---

### Example 2.4 — Convert a SUBROUTINE to a FUNCTION

**Prompt:**
```
/jbc-componentise
Package: TRADE.FINANCE
I have an existing SUBROUTINE TF.GET.GUARANTEE.DETAILS that returns data
through INOUT parameters. I need to convert it to a FUNCTION that returns
an outRecord, and add REST GET annotations.
```

**What the skill does:**
1. Reads the existing SUBROUTINE structure
2. Identifies all INOUT output parameters (these become outRecord fields)
3. Converts the SUBROUTINE to a FUNCTION with `RETURN outRecord`
4. Replaces INOUT parameter assignments with `outRecord<TRADE.FINANCE.GetGuaranteeDetails.field> = value`
5. Updates the `.component` method declaration: removes `INOUT` params, adds `: string` return type, adds REST annotations
6. Runs Phase 5 checklist

---

## Use Case 3: REVIEW / DEBUG — Analysing Existing Code

### Example 3.1 — "My method always returns an empty response"

**Prompt:**
```
/jbc-componentise Review this .b file. The REST endpoint calls it successfully
but the JSON response always has empty fields.

FUNCTION MY.PKG.GET.ACCOUNT.DETAILS(accountId)
    $USING EB.SystemTables
    $USING EB.DataAccess
    $USING AC.AccountOpening

    accountRecord = AC.AccountOpening.Account.Read(accountId, acError)
    accountTitle = accountRecord<AC.AccountOpening.Account.AccountTitleOne>
    workingBalance = accountRecord<AC.AccountOpening.Account.WorkingBalance>

    outRecord<MY.PROJECT.GetAccountDetails.accountTitle> = accountTitle
    outRecord<MY.PROJECT.GetAccountDetails.workingBalance> = workingBalance

RETURN
```

**What the skill reports:**

```
ANALYSIS — MY.PKG.GET.ACCOUNT.DETAILS
  Operation type: GET_API

  Issues found:
    [CRITICAL] Line 14: Bare RETURN discards the outRecord.
               A FUNCTION must return its value with RETURN <variable>.
               Bare RETURN returns an empty string regardless of what was built.

    [WARNING]  Missing initialisation guard.
               If MY.PROJECT has an initialise routine, the Record.Read call
               will fail with no T24 company context on the first invocation.

    [WARNING]  Missing $USING EB.API — standard base import for all CBI functions.

  Suggested fixes:
    Replace:  RETURN
    With:     RETURN outRecord

    Add before the Read call:
        IF MY.PROJECT.getinitialised() NE 'Y' THEN
            MY.PROJECT.initialiseProject()
        END

    Add import:
        $USING EB.API

  Checklist result: FAIL (3 issues — 1 critical, 2 warnings)
```

---

### Example 3.2 — "My loop only processes the first record"

**Prompt:**
```
/jbc-componentise Debug this loop. It only ever builds one entry in outRecord
even when multiple statement IDs are in resultSet.

    entryCount = 0
    FOR entryCount = 1 TO DCOUNT(resultSet, @FM)
        entryId = resultSet<entryCount>
        IF entryId NE '' THEN
            entryRecord = STMT.ENTRY.StmtEntry.Read(entryId, entryError)
            outRecord<MY.PROJECT.GetStatement.entryDate, entryCount> = entryRecord<STMT.ENTRY.StmtEntry.BookingDate>
        END
    NEXT entryCount
```

**What the skill reports:**

```
ANALYSIS — Loop pattern
  Issues found:
    [CRITICAL] Wrong iteration construct for a query resultSet string.
               DCOUNT(resultSet, @FM) counts field marks in the result string,
               but a resultSet from BatchBuildList is a dynamic string where IDs
               are separated by field marks that are consumed as you iterate.
               Using FOR/NEXT with DCOUNT calculates the count once upfront;
               if resultSet changes during the loop (REMOVE modifies it),
               the count is stale and behaviour is unpredictable.

               The correct pattern for iterating a resultSet is LOOP/REMOVE/WHILE:

  Suggested fix:
    Replace the FOR/NEXT block with:

        LOOP
            REMOVE entryId FROM resultSet SETTING moreRecords
        WHILE entryId NE '' DO
            entryRecord = STMT.ENTRY.StmtEntry.Read(entryId, entryError)
            entryCount += 1
            outRecord<MY.PROJECT.GetStatement.entryDate, entryCount> = entryRecord<STMT.ENTRY.StmtEntry.BookingDate>
        REPEAT

  Rule: LOOP/REMOVE/WHILE/REPEAT for query result set strings.
        FOR/NEXT + DCOUNT for fixed multi-value arrays with known count.

  Checklist result: FAIL (1 critical issue)
```

---

### Example 3.3 — Component file review

**Prompt:**
```
/jbc-componentise Review this .component file for correctness.

component MY.PROJECT.ProcessPayment
metamodelVersion 1.6

    table PaymentRequest {
        t24: MY.PROJECT.PaymentRequest
        fields: {
            debitAccount  = 1
            creditAccount = 2
            amount        = 3
        }
    }

    method processPayment(
        IN paymentDetails string
    ) : string {
        jBC: MY.PKG.PROCESS.PAYMENT
    }
```

**What the skill reports:**

```
ANALYSIS — ProcessPayment.component
  Issues found:
    [CRITICAL] Line 4: Table artefact missing scope keyword.
               All artefacts must declare scope: public, module, or private.
               Fix: "public table PaymentRequest {"

    [CRITICAL] Line 13: Method artefact missing scope keyword.
               Fix: "public method processPayment("

    [WARNING]  No REST annotations on method.
               If this is intended as a REST endpoint, add @POST / @Path / @PermitAll
               above the method declaration. If it is an internal method only,
               this is acceptable — confirm intent.

    [STYLE]    No output table declared.
               The method returns : string but there is no output table artefact
               defining the response field positions. The REST framework cannot
               map field positions to JSON keys without it. Add a response table.

  Suggested corrected file (with REST annotations and typed DTO):
    component MY.PROJECT.ProcessPayment
    metamodelVersion 1.6

        public table PaymentRequest {
            t24: MY.PROJECT.PaymentRequest
            fields: {
                debitAccount  = 1
                creditAccount = 2
                amount        = 3
            }
        }

        @Response("")
        @Path("/payments/process")
        @POST
        public method processPayment : PayDTOs:PaymentResponse (

            @RequestBody
            IN paymentDetails PayDTOs:PaymentRequest

        )
        {
            jBC: MY.PKG.PROCESS.PAYMENT
        }

  Also generate PayDTOs.complex with PaymentRequest and PaymentResponse classes.

  Checklist result: FAIL (2 critical, 1 warning, 1 style)
```

---

### Example 3.4 — Full file review with no issues

**Prompt:**
```
/jbc-componentise Review this implementation file before I deploy it to UAT.
[paste .b file]
```

**What the skill reports (when clean):**

```
ANALYSIS — MY.PKG.GET.CUSTOMER.PROFILE
  Operation type: GET_API

  Issues found: None

  Checklist result: PASS (0 issues)
  Ready for UAT deployment.
```

---

## Prompt Tips

### Be specific about the package name
```
Package: CORP.FINANCE
```
The skill will ask if you omit it.

### Include T24 application names when you know them
```
Read from FT.Contract application (FundsTransfer record)
```

### Paste existing code for CUSTOMISE and REVIEW tasks
The skill reads the current state of the files before making targeted changes. The more context you give, the more precise the output.

### Specify REST requirements explicitly
```
REST: GET /loans/{loanId}    → skill adds @GET @Path @PermitAll
REST: POST                   → skill adds @POST @Path @PermitAll
No REST needed               → skill omits all REST annotations
```

### Ask for partial generation if you need only one file
```
/jbc-componentise Generate only the .component file, I will write the .b myself.
/jbc-componentise Generate only the .b implementation, here is the existing .component: [paste]
/jbc-componentise Generate only the .complex DTO file for this response schema: [describe fields]
```

### Tell the skill which .complex namespace to use
```
/jbc-componentise
Package: MY.PROJECT
DTOs namespace: MyDTOs    ← skill will use MyDTOs:ClassName in return types and MyDTOs.complex
Create a REST GET API that returns loan details...
```
If no namespace is given, the skill will derive one from the package name.

### Review a .complex file
```
/jbc-componentise Review this .complex file for correctness.
[paste .complex file]
```
The skill checks class names, field types, multi-value `*` markers, and that all classes referenced in component methods are present.

---

## Output Files Reference

| File | Naming convention | Example |
|------|-------------------|---------|
| Component declaration | `<ComponentName>.component` | `GetLoanDetails.component` |
| DTO class definitions | `<Namespace>.complex` | `FinanceDTOs.complex` |
| Implementation routine | `<PKG.ROUTINE.NAME>.b` | `CF.GET.LOAN.DETAILS.b` |
| Initialise routine | `<PKG.INITIALISE>.b` | `CF.PROJECT.INITIALISE.b` |
| Validation hook | `<PKG.V.APP.FIELD.VALIDATION>.b` | `CF.V.LC.EXPIRY.VALIDATION.b` |
| Template definition | `<PKG.APP.PARAM>.b` | `CF.PAYMENT.INSTRUCTION.PARAM.b` |
| DE handler | `<PKG.DE.APP.DETAILS>.b` | `CF.DE.FT.ADVICE.DETAILS.b` |

**Compile order:** `.complex` first → Initialise SUBROUTINE → all FUNCTION/SUBROUTINE `.b` files → `.component`

---

## Common Mistakes the Skill Catches

| Mistake | Impact | Checklist flag |
|---------|--------|----------------|
| `RETURN` instead of `RETURN outRecord` | Response always empty | CRITICAL |
| Missing `$USING` namespace | Compile error | CRITICAL |
| `jBC:` name mismatches FUNCTION name | Wrong routine dispatched | CRITICAL |
| No scope on component artefact | Compile error | CRITICAL |
| FOR/NEXT on a query result set | Only first ID processed | CRITICAL |
| Return type after `)` instead of on method declaration line | Component parse error | CRITICAL |
| Typed return class missing from `.complex` file | Compile error: class not found | CRITICAL |
| `@QueryParam` before method instead of inside parameter block | Query param always null | CRITICAL |
| `@Response` / `@Path` / `@GET` in wrong order | REST endpoint not registered | WARNING |
| Missing `.ReadHis` for FT/LD/SC | Returns nothing for completed transactions | WARNING |
| No initialisation guard | Record reads fail without T24 context | WARNING |
| INOUT where IN is correct | Unexpected parameter mutation | WARNING |
| `IN param string` instead of `IN param Namespace:ClassName` for POST body | Body not deserialized | WARNING |
| `@RequestBody` missing on POST body parameter | POST body ignored — fields always empty | WARNING |
| Missing `response` field in output type | No error signalling possible | STYLE |

---

## Skill Version

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | Jun 2026 | Added `.complex` file template (Phase 3b); corrected REST annotation order (`@Response` → `@Path` → verb); fixed `@QueryParam` placement (inside param block); added `@RequestBody` for POST; added `date` parameter type; added typed return/request type patterns (`Namespace:ClassName`, `list<Namespace:ClassName>`); 5 new bugs in checklist; compile order updated |
| 2.0.0 | Jun 2026 | Generic rewrite — removed project-specific details; added CUSTOMISE and REVIEW/DEBUG modes; added mode detection; expanded common bug table |
| 1.0.0 | Jun 2026 | Initial version |
