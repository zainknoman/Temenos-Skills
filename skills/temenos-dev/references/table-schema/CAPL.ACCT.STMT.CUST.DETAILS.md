# CAPL.ACCT.STMT.CUST.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAPL.ACCT.STMT.CUST.DETAILS` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.SSCA.ACCT.TYPE` | `CaplAcctStmtCustDetails_AcctType` |  |  |  |
| 2 | `CAPL.SSCA.RESERVED.1` | `CaplAcctStmtCustDetails_Reserved1` |  |  |  |
| 3 | `CAPL.SSCA.RESERVED.2` | `CaplAcctStmtCustDetails_Reserved2` |  |  |  |
| 4 | `CAPL.SSCA.RESERVED.3` | `CaplAcctStmtCustDetails_Reserved3` |  |  |  |
| 5 | `CAPL.SSCA.ACCOUNT.NO` | `CaplAcctStmtCustDetails_AccountNo` |  |  |  |
| 6 | `CAPL.SSCA.STMT.SORT.OPT` | `CaplAcctStmtCustDetails_StmtSortOpt` | TField |  | The purpose of the field stores the statement sort option.Field length is 2 with alphanumeric character. |
| 7 | `CAPL.SSCA.MEM1.NAME` | `CaplAcctStmtCustDetails_Mem1Name` |  |  |  |
| 8 | `CAPL.SSCA.MEM2.NAME` | `CaplAcctStmtCustDetails_Mem2Name` |  |  |  |
| 9 | `CAPL.SSCA.MEM.ADDRESS` | `CaplAcctStmtCustDetails_MemAddress` | TField |  | Field Holds the address of the customer.Valid address of the customer is captured. |
| 10 | `CAPL.SSCA.PROMO.FLAG` | `CaplAcctStmtCustDetails_PromoFlag` | TField |  | This field holds the flag to indicate if promotion messages is required for customer or not. |
| 11 | `CAPL.SSCA.ACCT.STMT.OPT` | `CaplAcctStmtCustDetails_AcctStmtOpt` | TField |  | Holds the account statement option, EMAIL, PRINT, ELECTRONIC etc. PRINT is required for printing |
| 12 | `CAPL.SSCA.OWNER.NO` | `CaplAcctStmtCustDetails_OwnerNo` |  |  |  |
| 13 | `CAPL.SSCA.MEM.FREQUENCY` | `CaplAcctStmtCustDetails_MemFrequency` | TField |  | This field holds the frequency of the customer statement.Valid t24 frequency is captured. |
| 14 | `CAPL.SSCA.MEM.COMP.BOOK` | `CaplAcctStmtCustDetails_MemCompBook` | TField |  | Field is used to store the Customer Company.Valid record from COMPANY table. |
| 15 | `CAPL.SSCA.PRE.STMT.DATE` | `CaplAcctStmtCustDetails_PreStmtDate` | TField |  | Purpose of the field is to store the previous statement date.Valid date to be defined here. |
| 16 | `CAPL.SSCA.STMT.DATE` | `CaplAcctStmtCustDetails_StmtDate` | TField |  | Purpose of the field is to store the Holds the current statement date.Valid date to be defined here. |
| 17 | `CAPL.SSCA.MEM.TYPE` | `CaplAcctStmtCustDetails_MemType` | TField |  | This field is used to store the Mem Customer type.Allowed value 35 alphanumeric character. |
| 18 | `CAPL.SSCA.MEM.OMR` | `CaplAcctStmtCustDetails_MemOmr` | TField |  |  |
| 19 | `CAPL.SSCA.MEM.ENCL.CHQ` | `CaplAcctStmtCustDetails_MemEnclChq` | TField |  | Field denotes whether Cheque is required to be printed for statement or not.Allowed values are Y/N |
| 20 | `CAPL.SSCA.MEM.NO.CHQ` | `CaplAcctStmtCustDetails_MemNoChq` | TField |  | Not in use. |
| 21 | `CAPL.SSCA.MEM.HONOR1` | `CaplAcctStmtCustDetails_MemHonor1` | TField |  | This field holds the Title of the customer name to be printed in the statement.Allowed value 60 alphanumeric character. |
| 22 | `CAPL.SSCA.MEM.ADDR1` | `CaplAcctStmtCustDetails_MemAddr1` | TField |  | Field holds the customer address which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 23 | `CAPL.SSCA.MEM.ADDR2` | `CaplAcctStmtCustDetails_MemAddr2` | TField |  | Field holds the customer address which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 24 | `CAPL.SSCA.MEM.ADDR3` | `CaplAcctStmtCustDetails_MemAddr3` | TField |  | Field holds the customer address which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 25 | `CAPL.SSCA.MEM.ADDR4` | `CaplAcctStmtCustDetails_MemAddr4` | TField |  | Field holds the customer address which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 26 | `CAPL.SSCA.MEM.ADDR5` | `CaplAcctStmtCustDetails_MemAddr5` | TField |  | Field holds the customer address which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 27 | `CAPL.SSCA.MEM.ADDR6` | `CaplAcctStmtCustDetails_MemAddr6` | TField |  | Field holds the customer address which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 28 | `CAPL.SSCA.MEM.POSTAL` | `CaplAcctStmtCustDetails_MemPostal` | TField |  | Field holds the postal code which needs to be printed in the statement.Allowed value 60 alphanumeric character. |
| 29 | `CAPL.SSCA.MEM.HONOR2` | `CaplAcctStmtCustDetails_MemHonor2` | TField |  | Not in use. |
| 30 | `CAPL.SSCA.FINS.TOTAL.AMT` | `CaplAcctStmtCustDetails_FinsTotalAmt` | TField |  | This field holds the value of the customer financial balance.Net balance of the customer (assets - liabilities).Allowed value 18 numeric character. |
| 31 | `CAPL.SSCA.FIN.TOT.ASSET.AMT` | `CaplAcctStmtCustDetails_FinTotAssetAmt` | TField |  | This field is used to store the total asset of the customerAllowed value 18 numeric character. |
| 32 | `CAPL.SSCA.FIN.TOT.LIAB.AMT` | `CaplAcctStmtCustDetails_FinTotLiabAmt` | TField |  | This field is used to store the total liabilities of the customerAllowed value 18 numeric character. |
| 33 | `CAPL.SSCA.TOT.CHQ.SAV.AMT` | `CaplAcctStmtCustDetails_TotChqSavAmt` | TField |  | Field holds the total of all chequing and saving accounts balance (CAD).Allowed value 18 numeric character. |
| 34 | `CAPL.SSCA.TOT.TERM.AMT` | `CaplAcctStmtCustDetails_TotTermAmt` | TField |  | Field stores the total of all term deposits balance.Allowed value 18 numeric character. |
| 35 | `CAPL.SSCA.TOT.SHARE.AMT` | `CaplAcctStmtCustDetails_TotShareAmt` | TField |  | Field holds the total of all share account balance.Allowed value 18 numeric character. |
| 36 | `CAPL.SSCA.TOT.TFSA.AMT` | `CaplAcctStmtCustDetails_TotTfsaAmt` | TField |  | Field holds the total of all TFSA plan balance of customerAllowed value 18 numeric character. |
| 37 | `CAPL.SSCA.TOT.RRIF.AMT` | `CaplAcctStmtCustDetails_TotRrifAmt` | TField |  | Field holds the total of all RRIF plan balance of customer.Allowed value 18 numeric character. |
| 38 | `CAPL.SSCA.TOT.RRSP.AMT` | `CaplAcctStmtCustDetails_TotRrspAmt` | TField |  | Field hodls the total of all RSP plan balance of customerAllowed value 18 numeric character.. |
| 39 | `CAPL.SSCA.TOT.US.FUND.AMT` | `CaplAcctStmtCustDetails_TotUsFundAmt` | TField |  | Field holds the total of all US account of customer.Allowed value 18 numeric character. |
| 40 | `CAPL.SSCA.TOT.OVDRFT.AMT` | `CaplAcctStmtCustDetails_TotOvdrftAmt` | TField |  | This field holds the total of overdraft account.Allowed value 18 numeric character. |
| 41 | `CAPL.SSCA.TOT.LOC.AMT` | `CaplAcctStmtCustDetails_TotLocAmt` | TField |  | Field hodls the total of all LOC account balances.Allowed value 18 numeric character. |
| 42 | `CAPL.SSCA.TOT.LOAN.AMT` | `CaplAcctStmtCustDetails_TotLoanAmt` | TField |  | The field holds the total of all loan amounts of customer.Allowed value 18 numeric character. |
| 43 | `CAPL.SSCA.TOT.MORTGAGE.AMT` | `CaplAcctStmtCustDetails_TotMortgageAmt` | TField |  | Field holds the total of all Mortgage amounts of customer.Allowed value 18 numeric character. |
| 44 | `CAPL.SSCA.TOT.US.LOAN.AMT` | `CaplAcctStmtCustDetails_TotUsLoanAmt` | TField |  | This field holds total of all US loan amounts of customer.Allowed value 18 numeric character. |
| 45 | `CAPL.SSCA.LOAN.GRP.HEADER` | `CaplAcctStmtCustDetails_LoanGrpHeader` | TField |  | The field Holds the loan header name, defaulted to Loan of the customer.Allowed value 35 numeric character. |
| 46 | `CAPL.SSCA.STMT.START.DATE` | `CaplAcctStmtCustDetails_StmtStartDate` | TField |  | Individual Statement:Hold the next statement frequency date from ACCOUNT.STATEMENTCombined Statement:Hold the next statement frequency date from CUSTOMERIn case of new account, account-opening date from ACCOUNT considered. |
| 47 | `CAPL.SSCA.BAD.ADDRESS` | `CaplAcctStmtCustDetails_BadAddress` | TField |  | Field hold the Bad address flag from CUSTOMER, if set as YES |
| 48 | `CAPL.SSCA.RESERVED.9` | `CaplAcctStmtCustDetails_Reserved9` |  |  |  |
| 49 | `CAPL.SSCA.RESERVED.10` | `CaplAcctStmtCustDetails_Reserved10` | TField |  |  |
| 50 | `CAPL.SSCA.RESERVED.11` | `CaplAcctStmtCustDetails_Reserved11` | TField |  |  |
| 51 | `CAPL.SSCA.RESERVED.12` | `CaplAcctStmtCustDetails_Reserved12` | TField |  |  |
| 52 | `CAPL.SSCA.RESERVED.13` | `CaplAcctStmtCustDetails_Reserved13` | TField |  |  |
| 53 | `CAPL.SSCA.RESERVED.14` | `CaplAcctStmtCustDetails_Reserved14` | TField |  |  |
| 54 | `CAPL.SSCA.RESERVED.15` | `CaplAcctStmtCustDetails_Reserved15` | TField |  |  |
