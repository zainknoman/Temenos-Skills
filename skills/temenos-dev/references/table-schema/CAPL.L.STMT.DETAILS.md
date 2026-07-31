# CAPL.L.STMT.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAPL.L.STMT.DETAILS` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.STMT.TRACER.NO` | `CaplLStmtDetails_TracerNo` | TField |  |  |
| 2 | `CAPL.STMT.VALUE.DATE` | `CaplLStmtDetails_ValueDate` | TField |  | Field Holds the value date of the transaction.Valid date to be stored here. |
| 3 | `CAPL.STMT.BOOKING.DATE` | `CaplLStmtDetails_BookingDate` | TField |  | Field holds the booking date of the transaction.Valid date to be stored here. |
| 4 | `CAPL.STMT.TRANSACTION` | `CaplLStmtDetails_Transaction` | TField |  | Field Holds the description of the transaction (description of FTTC/Transaction table), to indicate type of transaction. |
| 5 | `CAPL.STMT.NARRATIVE` | `CaplLStmtDetails_Narrative` |  |  |  |
| 6 | `CAPL.STMT.RESERVED.1` | `CaplLStmtDetails_Reserved1` | TField |  |  |
| 7 | `CAPL.STMT.BOLD.FLAG` | `CaplLStmtDetails_BoldFlag` | TField |  |  |
| 8 | `CAPL.STMT.WITHDRAWL.AMT` | `CaplLStmtDetails_WithdrawlAmt` | TField |  | Field holds the withdrawal /debit amount of the transaction.Allowed value 18 numeric character. |
| 9 | `CAPL.STMT.DEPOSIT.AMT` | `CaplLStmtDetails_DepositAmt` | TField |  | Field holds the deposit/credit amount of the transaction.Allowed value 18 numeric character. |
| 10 | `CAPL.STMT.BALANCE` | `CaplLStmtDetails_Balance` | TField |  | Field holds the running balance of the account, after the transaction. |
| 11 | `CAPL.STMT.BAL.FLAG` | `CaplLStmtDetails_BalFlag` | TField |  |  |
| 12 | `CAPL.STMT.LOAN.INTEREST` | `CaplLStmtDetails_LoanInterest` | TField |  | Field holds the loan interest amount paid Holds the loan interest amount paid.Allowed value 10 numeric character. |
| 13 | `CAPL.STMT.LOAN.PRINCIPAL` | `CaplLStmtDetails_LoanPrincipal` | TField |  | Field holds the loan principal amount paid.Allowed value 50 numeric character. |
| 14 | `CAPL.STMT.TRXN.BAL.CR` | `CaplLStmtDetails_TrxnBalCr` | TField |  |  |
| 15 | `CAPL.STMT.TRXN.PRINCIPAL.CR` | `CaplLStmtDetails_TrxnPrincipalCr` | TField |  |  |
| 16 | `CAPL.STMT.CHARGES.FOR.LOANS` | `CaplLStmtDetails_ChargesForLoans` | TField |  |  |
| 17 | `CAPL.STMT.STMT.ID` | `CaplLStmtDetails_StmtId` |  |  |  |
| 18 | `CAPL.STMT.SPEC.ID` | `CaplLStmtDetails_SpecId` |  |  |  |
| 19 | `CAPL.STMT.RESERVED.6` | `CaplLStmtDetails_Reserved6` | TField |  |  |
| 20 | `CAPL.STMT.RESERVED.7` | `CaplLStmtDetails_Reserved7` | TField |  |  |
