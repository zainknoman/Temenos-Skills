# NON.CUSTOMER.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.NON.CUSTOMER.TRANSACTIONS` in `ESTELL_NonCustomerCash.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESTELL.NON.CUS.TXN.CUSTOMER` | `NonCustomerTransactions_Customer` | TField |  | This field captures the Customer Id from the @ID of NON.CUSTOMER.TRANSACTIONS table |
| 2 | `ESTELL.NON.CUS.TXN.TXN.DATE` | `NonCustomerTransactions_TxnDate` | TField |  | This field Captures the date when the Non Customer transaction was performed |
| 3 | `ESTELL.NON.CUS.TXN.TXN.ID` | `NonCustomerTransactions_TxnId` |  |  |  |
| 4 | `ESTELL.NON.CUS.TXN.TXN.AMOUNT` | `NonCustomerTransactions_TxnAmount` |  |  |  |
| 5 | `ESTELL.NON.CUS.TXN.CURRENCY` | `NonCustomerTransactions_Currency` |  |  |  |
| 6 | `ESTELL.NON.CUS.TXN.LEGAL.ID` | `NonCustomerTransactions_LegalId` |  |  |  |
| 7 | `ESTELL.NON.CUS.TXN.LEGAL.DOC.NAME` | `NonCustomerTransactions_LegalDocName` |  |  |  |
| 8 | `ESTELL.NON.CUS.TXN.DEPOSIT.WITHDRAWAL` | `NonCustomerTransactions_DepositWithdrawal` |  |  |  |
| 9 | `ESTELL.NON.CUS.TXN.DEPOSITOR.ID` | `NonCustomerTransactions_DepositorId` |  |  |  |
| 10 | `ESTELL.NON.CUS.TXN.CREDIT.ACCOUNT` | `NonCustomerTransactions_CreditAccount` |  |  |  |
