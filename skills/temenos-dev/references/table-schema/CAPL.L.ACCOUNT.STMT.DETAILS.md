# CAPL.L.ACCOUNT.STMT.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAPL.L.ACCOUNT.STMT.DETAILS` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.AC.STMT.STATEMENT.DATE` | `CaplLAccountStmtDetails_StatementDate` | TField |  | This field Holds the account statement dateValid T24 date is captured here. |
| 2 | `CAPL.AC.STMT.STMT.SECTION` | `CaplLAccountStmtDetails_StmtSection` | TField |  |  |
| 3 | `CAPL.AC.STMT.PRD.DESCRIPTION` | `CaplLAccountStmtDetails_PrdDescription` | TField |  |  |
| 4 | `CAPL.AC.STMT.PRODUCT.DETAILS` | `CaplLAccountStmtDetails_ProductDetails` | TField |  |  |
| 5 | `CAPL.AC.STMT.CURRENCY` | `CaplLAccountStmtDetails_Currency` | TField |  |  |
| 6 | `CAPL.AC.STMT.OPENING.BALANCE` | `CaplLAccountStmtDetails_OpeningBalance` | TField |  | Field holds the opening balance of the account.Valid amount is captured here. |
| 7 | `CAPL.AC.STMT.TOTAL.WITHDRAWALS` | `CaplLAccountStmtDetails_TotalWithdrawals` | TField |  | The field holds the total withdrawal amount of the account.Valid amount is captured here. |
| 8 | `CAPL.AC.STMT.TOTAL.DEPOSITS` | `CaplLAccountStmtDetails_TotalDeposits` | TField |  | This field holds the total deposit amount of the account.Valid amount is captured here. |
| 9 | `CAPL.AC.STMT.CLOSING.BALANCE` | `CaplLAccountStmtDetails_ClosingBalance` | TField |  | This field holds the closing balance of the account.Valid amount is captured here. |
| 10 | `CAPL.AC.STMT.STMT.ENTRY.ID` | `CaplLAccountStmtDetails_StmtEntryId` |  |  |  |
| 11 | `CAPL.AC.STMT.BOOKING.DATE` | `CaplLAccountStmtDetails_BookingDate` |  |  |  |
| 12 | `CAPL.AC.STMT.VALUE.DATE` | `CaplLAccountStmtDetails_ValueDate` |  |  |  |
| 13 | `CAPL.AC.STMT.TRANSACTION` | `CaplLAccountStmtDetails_Transaction` |  |  |  |
| 14 | `CAPL.AC.STMT.NARRATIVE` | `CaplLAccountStmtDetails_Narrative` |  |  |  |
| 15 | `CAPL.AC.STMT.WITHDRAWALS` | `CaplLAccountStmtDetails_Withdrawals` |  |  |  |
| 16 | `CAPL.AC.STMT.DEPOSITS` | `CaplLAccountStmtDetails_Deposits` |  |  |  |
| 17 | `CAPL.AC.STMT.LOAN.INTEREST` | `CaplLAccountStmtDetails_LoanInterest` |  |  |  |
| 18 | `CAPL.AC.STMT.LOAN.PRINCIPAL` | `CaplLAccountStmtDetails_LoanPrincipal` |  |  |  |
| 19 | `CAPL.AC.STMT.LOAN.CHARGE` | `CaplLAccountStmtDetails_LoanCharge` |  |  |  |
| 20 | `CAPL.AC.STMT.BALANCE` | `CaplLAccountStmtDetails_Balance` |  |  |  |
| 21 | `CAPL.AC.STMT.PREVIOUS.STMT.DATE` | `CaplLAccountStmtDetails_PreviousStmtDate` | TField |  |  |
| 22 | `CAPL.AC.STMT.MEMBERSHIP.NUMBER` | `CaplLAccountStmtDetails_MembershipNumber` | TField |  | Holds the customer number |
| 23 | `CAPL.AC.STMT.CUSTOMER.NUMBER` | `CaplLAccountStmtDetails_CustomerNumber` |  |  |  |
| 24 | `CAPL.AC.STMT.CUSTOMER.ROLE` | `CaplLAccountStmtDetails_CustomerRole` |  |  |  |
| 25 | `CAPL.AC.STMT.CUSTOMER.ADDR` | `CaplLAccountStmtDetails_CustomerAddr` |  |  |  |
| 26 | `CAPL.AC.STMT.CUST.NAME.ORDER.1` | `CaplLAccountStmtDetails_CustNameOrder1` | TField |  |  |
| 27 | `CAPL.AC.STMT.CUST.NAME.ORDER.2` | `CaplLAccountStmtDetails_CustNameOrder2` | TField |  |  |
| 28 | `CAPL.AC.STMT.STATEMENT.WAIVE` | `CaplLAccountStmtDetails_StatementWaive` | TField |  |  |
| 29 | `CAPL.AC.STMT.STMT.BRANCH.ADD` | `CaplLAccountStmtDetails_StmtBranchAdd` | TField |  | Holds the account company branch |
| 30 | `CAPL.AC.STMT.ACCT.STATUS` | `CaplLAccountStmtDetails_AcctStatus` | TField |  |  |
| 31 | `CAPL.AC.STMT.CHEQUE.IMAGE` | `CaplLAccountStmtDetails_ChequeImage` | TField |  |  |
| 32 | `CAPL.AC.STMT.DORMANCY.MSG` | `CaplLAccountStmtDetails_DormancyMsg` |  |  |  |
| 33 | `CAPL.AC.STMT.ACCT.STMT.OPT` | `CaplLAccountStmtDetails_AcctStmtOpt` | TField |  |  |
| 34 | `CAPL.AC.STMT.TOT.CHEQUE.TXNS` | `CaplLAccountStmtDetails_TotChequeTxns` | TField |  |  |
| 35 | `CAPL.AC.STMT.NET.CHANGE.AMT` | `CaplLAccountStmtDetails_NetChangeAmt` | TField |  | This field holds the net change(deposits - withdrawal)Valid amount is captured here. |
| 36 | `CAPL.AC.STMT.TERM.MAT.MSG` | `CaplLAccountStmtDetails_TermMatMsg` |  |  |  |
| 37 | `CAPL.AC.STMT.TERM.MAT.DATE` | `CaplLAccountStmtDetails_TermMatDate` | TField |  |  |
| 38 | `CAPL.AC.STMT.STMT.REF.NO` | `CaplLAccountStmtDetails_StmtRefNo` | TField |  |  |
| 39 | `CAPL.AC.STMT.TOTAL.LOAN.INTEREST` | `CaplLAccountStmtDetails_TotalLoanInterest` | TField |  | Updates the total interest of all the entries which is affecting the INTEREST property class |
| 40 | `CAPL.AC.STMT.TOTAL.LOAN.PRINCIPAL` | `CaplLAccountStmtDetails_TotalLoanPrincipal` | TField |  | Updates the total principal of all the entries which is affecting the ACCOUNT property class |
| 41 | `CAPL.AC.STMT.TOTAL.LOAN.CHARGE` | `CaplLAccountStmtDetails_TotalLoanCharge` | TField |  | Updates the total charge of all the entries which is affecting the CHARGE property class |
| 42 | `CAPL.AC.STMT.RESERVED.4` | `CaplLAccountStmtDetails_Reserved4` | TField |  |  |
| 43 | `CAPL.AC.STMT.RESERVED.5` | `CaplLAccountStmtDetails_Reserved5` | TField |  |  |
| 44 | `CAPL.AC.STMT.RESERVED.6` | `CaplLAccountStmtDetails_Reserved6` | TField |  |  |
| 45 | `CAPL.AC.STMT.RESERVED.7` | `CaplLAccountStmtDetails_Reserved7` | TField |  |  |
| 46 | `CAPL.AC.STMT.RESERVED.8` | `CaplLAccountStmtDetails_Reserved8` | TField |  |  |
| 47 | `CAPL.AC.STMT.RESERVED.9` | `CaplLAccountStmtDetails_Reserved9` | TField |  |  |
| 48 | `CAPL.AC.STMT.RESERVED.10` | `CaplLAccountStmtDetails_Reserved10` | TField |  |  |
