# CAPL.H.ACCT.STMT.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.ACCT.STMT.PARAM` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.AMSP.CUS.TYPE` | `CaplHAcctStmtParam_CusType` |  |  |  |
| 2 | `CAPL.AMSP.MEMBER.TYPE` | `CaplHAcctStmtParam_MemberType` |  |  |  |
| 3 | `CAPL.AMSP.RESERVED.12` | `CaplHAcctStmtParam_Reserved12` |  |  |  |
| 4 | `CAPL.AMSP.RESERVED.13` | `CaplHAcctStmtParam_Reserved13` |  |  |  |
| 5 | `CAPL.AMSP.STMT.NAME.DEF` | `CaplHAcctStmtParam_StmtNameDef` |  |  |  |
| 6 | `CAPL.AMSP.CUS.INDUSTRY` | `CaplHAcctStmtParam_CusIndustry` |  |  |  |
| 7 | `CAPL.AMSP.RESERVED.14` | `CaplHAcctStmtParam_Reserved14` |  |  |  |
| 8 | `CAPL.AMSP.RESERVED.15` | `CaplHAcctStmtParam_Reserved15` |  |  |  |
| 9 | `CAPL.AMSP.STMT.ABB` | `CaplHAcctStmtParam_StmtAbb` |  |  |  |
| 10 | `CAPL.AMSP.CHEQUE.FLAG` | `CaplHAcctStmtParam_ChequeFlag` |  |  |  |
| 11 | `CAPL.AMSP.DORMANCY.MSG` | `CaplHAcctStmtParam_DormancyMsg` |  |  |  |
| 12 | `CAPL.AMSP.STMT.SORT.OPT.FROM` | `CaplHAcctStmtParam_StmtSortOptFrom` |  |  |  |
| 13 | `CAPL.AMSP.STMT.SORT.OPT.TO` | `CaplHAcctStmtParam_StmtSortOptTo` |  |  |  |
| 14 | `CAPL.AMSP.MEM.INDUSTRY` | `CaplHAcctStmtParam_MemIndustry` |  |  |  |
| 15 | `CAPL.AMSP.RSP.REX.CATEG` | `CaplHAcctStmtParam_RspRexCateg` |  |  |  |
| 16 | `CAPL.AMSP.CIF.TITLE` | `CaplHAcctStmtParam_CifTitle` | TField |  | This field is used to define the title of the customer that needs to be displayed in customer statement for customer. The title based on the field CUSTOMER &gt; CIF.TITLE must be parameterized. |
| 17 | `CAPL.AMSP.TERM.MAT.MSG` | `CaplHAcctStmtParam_TermMatMsg` |  |  |  |
| 18 | `CAPL.AMSP.BOKNG.DTE.TXN` | `CaplHAcctStmtParam_BokngDteTxn` |  |  |  |
| 19 | `CAPL.AMSP.AZ.TERM.TXN.AMT` | `CaplHAcctStmtParam_AzTermTxnAmt` |  |  |  |
| 20 | `CAPL.AMSP.CHK.AA.STATUS` | `CaplHAcctStmtParam_ChkAaStatus` |  |  |  |
| 21 | `CAPL.AMSP.ACCOUNT.INFO.LINE` | `CaplHAcctStmtParam_AccountInfoLine` |  |  |  |
| 22 | `CAPL.AMSP.CONVERSION` | `CaplHAcctStmtParam_Conversion` |  |  |  |
| 23 | `CAPL.AMSP.ADHOC.STMT.PROD.TYPE` | `CaplHAcctStmtParam_AdhocStmtProdType` | TField |  |  |
| 24 | `CAPL.AMSP.LOCAL.REF` | `CaplHAcctStmtParam_LocalRef` |  |  |  |
| 25 | `CAPL.AMSP.OVERRIDE` | `CaplHAcctStmtParam_Override` |  |  |  |
| 26 | `CAPL.AMSP.RECORD.STATUS` | `CaplHAcctStmtParam_RecordStatus` | String |  |  |
| 27 | `CAPL.AMSP.CURR.NO` | `CaplHAcctStmtParam_CurrNo` | String |  |  |
| 28 | `CAPL.AMSP.INPUTTER` | `CaplHAcctStmtParam_Inputter` |  |  |  |
| 29 | `CAPL.AMSP.DATE.TIME` | `CaplHAcctStmtParam_DateTime` |  |  |  |
| 30 | `CAPL.AMSP.AUTHORISER` | `CaplHAcctStmtParam_Authoriser` | String |  |  |
| 31 | `CAPL.AMSP.CO.CODE` | `CaplHAcctStmtParam_CoCode` | String |  |  |
| 32 | `CAPL.AMSP.DEPT.CODE` | `CaplHAcctStmtParam_DeptCode` | String |  |  |
| 33 | `CAPL.AMSP.AUDITOR.CODE` | `CaplHAcctStmtParam_AuditorCode` | String |  |  |
| 34 | `CAPL.AMSP.AUDIT.DATE.TIME` | `CaplHAcctStmtParam_AuditDateTime` | String |  |  |
