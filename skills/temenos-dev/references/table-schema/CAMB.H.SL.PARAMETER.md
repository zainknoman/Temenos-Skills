# CAMB.H.SL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAMB.H.SL.PARAMETER` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.H.SL.PARAM.SYN.CON.PRI.CAT` | `CambHSlParameter_SynConPriCat` | TField |  |  |
| 2 | `CAMB.H.SL.PARAM.SYN.CON.PRI.AC` | `CambHSlParameter_SynConPriAc` | TField |  |  |
| 3 | `CAMB.H.SL.PARAM.SYN.CON.INT.AC.CAT` | `CambHSlParameter_SynConIntAcCat` | TField |  |  |
| 4 | `CAMB.H.SL.PARAM.SYN.CON.INT.ACC.AC` | `CambHSlParameter_SynConIntAccAc` | TField |  |  |
| 5 | `CAMB.H.SL.PARAM.PL.INC.CAT` | `CambHSlParameter_PlIncCat` | TField |  | Field is used to define the P&amp;L Income Category used by AA Loans to book income into.If no PL Income Category is given in the ACCOUNTING property mentioned in CAMB.H.SL.PARAMETER &gt; AA.ACCTING.PROP, system uses this PL Income Category given in CAMB.H.SL.PARAMETER &gt; PL.INC.CAT to post the income towards the SL loan.Validation : Must be valid category code in the CATEGORY file in T24.eg. 51001 |
| 6 | `CAMB.H.SL.PARAM.PRI.BAL.TYPE` | `CambHSlParameter_PriBalType` | TField |  |  |
| 7 | `CAMB.H.SL.PARAM.INT.DUE.BAL.TYPE` | `CambHSlParameter_IntDueBalType` | TField |  | This field is used to define a "Virtual" Balance Type that includes the Balance Types for Due and Delinquent Interest Accrual Balances.The balance type defined here is considered for calculation of interest due balance towards participants.Validtion - Must be valid ID in the AC.BALANCE.TYPE file in T24.eg. DUEPRINCIPALINT |
| 8 | `CAMB.H.SL.PARAM.INT.ACC.BAL.TYPE` | `CambHSlParameter_IntAccBalType` | TField |  | This field is used to define a Balance Type used by AA Loans to store the Interest Accrual Balances.The balance type defined here is considered for calculation of interest accrual balance towards participants.Validation - Must be valid ID in the AC.BALANCE.TYPE file in T24.eg. ACCPRINCIPALINT |
| 9 | `CAMB.H.SL.PARAM.AA.INT.PROP` | `CambHSlParameter_AaIntProp` |  |  |  |
| 10 | `CAMB.H.SL.PARAM.AA.ACCTING.PROP` | `CambHSlParameter_AaAcctingProp` | TField |  | Field is used to define the property towards which the accounting entry to be posted during cob , for total Interest accruals towards participants.Defined AA Accounting Property links to the AA Loans.Validation - Must be valid ID in AA.PROPERTY with PROPERTY.CLASS&gt;ACCOUNTING.eg. ACCOUNTING |
| 11 | `CAMB.H.SL.PARAM.FT.TXN.TYPE.ID` | `CambHSlParameter_FtTxnTypeId` | TField |  | Field is used to define the transaction type to be used to raise FTs for allocating disbursements to Participant.Validation : Valid FT.TXN.TYPE.CONDITION record.Eg. AC |
| 12 | `CAMB.H.SL.PARAM.ACC.TXN.CODE` | `CambHSlParameter_AccTxnCode` | TField |  | Field is used to store the transaction code to be used to raise Accrual allocation entries to Participants during COBValidation : valid record from TRANSACTION table.Eg. AC90 |
| 13 | `CAMB.H.SL.PARAM.PRI.REPAY.TXN.CODE` | `CambHSlParameter_PriRepayTxnCode` | TField |  |  |
| 14 | `CAMB.H.SL.PARAM.INT.REPAY.TXN.CODE` | `CambHSlParameter_IntRepayTxnCode` | TField |  | Field is used to store the transaction code to be used to raise Interest repayment allocation entries to Participants during COBValidation : valid record from TRANSACTION table.Eg. AC94 |
| 15 | `CAMB.H.SL.PARAM.OFS.VERSION` | `CambHSlParameter_OfsVersion` | TField |  |  |
| 16 | `CAMB.H.SL.PARAM.OFS.SOURCE` | `CambHSlParameter_OfsSource` | TField |  |  |
| 17 | `CAMB.H.SL.PARAM.REVOLVE.NONREVOLVE` | `CambHSlParameter_RevolveNonrevolve` | TField |  | This field used to indicate whether FI want to use different accounts for revolving and non-revolving SL loans.Allowed inputs: YES/ NO. Defaults to No.if set to NO - System uses the below fields for posting accounting for both revolving and non revolving loans.SYN.CONTRA.PRIN.CAT / SYN.CONTRA.PRIN.ACSYN.CONTRA.INT.ACC.CAT / SYN.CONTRA.INT.ACC.ACPL.INT.CATif set to YES - System uses the different accounts for posting accounting for non revolving loans and different accounts for Revolving loans.Fields used for Non-Revolving laon:NON.REV.SYN.CONTRA.PRIN.CAT / NON.REV.SYN.CONTRA.PRIN.ACNON.REV.SYN.CONTRA.INT.ACC.CAT / NON.REV.SYN.CONTRA.INT.ACC.ACNON.REV.PL.CATEGORYFields used for Revolving laon:SYN.CONTRA.PRIN.CAT / SYN.CONTRA.PRIN.ACSYN.CONTRA.INT.ACC.CAT / SYN.CONTRA.INT.ACC.ACPL.INT.CAT |
| 18 | `CAMB.H.SL.PARAM.NON.REV.SYN.CONTRA.PRIN.CAT` | `CambHSlParameter_NonRevSynContraPrinCat` | TField | Yes | This field is used to define the T24 Internal Account Category to be used in building Syndication-Contra Principal Account to store Principal Outstanding Balances for all Syndication Participant.Validation - Must be valid Internal Account Category code in the CATEGORY file in T24.Mandatory and Applicable only if REVOLVE.NONREVOLVE is set to YES, else it is no inputtable field.Once the record is committed, it is a no change field. Either NON.REV.SYN.CONTRA.PRIN.CAT or NON.REV.SYN.CONTRA.PRIN.AC to be defined.eg. 10001 |
| 19 | `CAMB.H.SL.PARAM.NON.REV.SYN.CONTRA.PRIN.AC` | `CambHSlParameter_NonRevSynContraPrinAc` | TField | Yes | This field is used to define the T24 Internal Account to be used as Syndication-Contra Principal Account to store Principal Outstanding Balances for all Syndication Participants.Validation - Must be valid Internal Account in the ACCOUNT file in T24.Mandatory and Applicable only if REVOLVE.NONREVOLVE is set to YES, else it is no inputtable field.Once the record is committed, it is a no change field. Either NON.REV.SYN.CONTRA.PRIN.CAT or NON.REV.SYN.CONTRA.PRIN.AC to be defined and not both.eg. CAD1015000010011 |
| 20 | `CAMB.H.SL.PARAM.NON.REV.SYN.CONTRA.INT.ACC.CAT` | `CambHSlParameter_NonRevSynContraIntAccCat` | TField |  | This field is used to define T24 Internal Account Category to be used in building Syndication-Contra Interest Accrual Account to store Interest Accrual Balances for all Syndication Participants.Validation - Must be valid Internal Account category in the CATEGORY file in T24.Once the record is committed, it is a no change field. Either SYN.CONTRA.INT.ACC.CAT or SYN.CONTRA.INT.ACC.AC to be defined and not both.eg. 10001 |
| 21 | `CAMB.H.SL.PARAM.NON.REV.SYN.CONTRA.INT.ACC.AC` | `CambHSlParameter_NonRevSynContraIntAccAc` | TField | Yes | Field is used to define the T24 Internal Account to be used as Syndication-Contra Interest Accrual Account to store Interest Accrual Balances for all Syndication Participants.Validation - Must be valid Internal Account in the ACCOUNT file in T24.Mandatory and Applicable only if REVOLVE.NONREVOLVE is set to YES, else it is no inputtable field.Once the record is committed, it is a no change field. Either NON.REV.SYN.CONTRA.INT.ACC.CAT or NON.REV.SYN.CONTRA.INT.ACC.AC to be defined and not both.eg. CAD1015000010011 |
| 22 | `CAMB.H.SL.PARAM.NON.REV.PL.CATEGORY` | `CambHSlParameter_NonRevPlCategory` | TField |  |  |
| 23 | `CAMB.H.SL.PARAM.OFS.PO.VERSION` | `CambHSlParameter_OfsPoVersion` | TField |  | This field stores the version to be used to post PAYMENT ORDER via OFS for payment to participants. |
| 24 | `CAMB.H.SL.PARAM.ARR.ACTIVITY.VERSION` | `CambHSlParameter_ArrActivityVersion` | TField |  | This field stores the version to be used to for Arrangement Activity |
| 25 | `CAMB.H.SL.PARAM.CAP.AMOUNT` | `CambHSlParameter_CapAmount` | TField |  | This field holds the maximum cap amount allowed per company to open a Syndicated Loan.Input allowed only when ID = COMPANYValidation - Based on the SL agreement amount and amount in CAP.AMOUNT table MAX.CAP.SL.AMT table holds the total amount lent towards syndication.If total amount exceeds CAP.AMOUNT value, user is thrown with a warning message while committing CAMB.H.SL.DETAILS |
| 26 | `CAMB.H.SL.PARAM.INT.ADJ.PERT` | `CambHSlParameter_IntAdjPert` | TField |  | This field holds the percentage up to which the variation in the interest portion can be adjusted.Used when posting an FT in the version FUNDS.TRANSFER,SL for the interest payment received from the Lead Banker.Note: This is applicable only when FI acts as a Participant bank in Syndicated loan.Note: Main reason for this check, is to make sure System does not blindly override the Bill amount, instead check the tolerance percentage defined in INT.ADJ.PERT, if the adjustment percentage is within range, bill amount will be modified using ADJUST BILL activity, else the bill amount will not be modified and FT will be posted with actual amount and exception log will be updated for same.Note: Either INT.ADJ.PERT or INT.ADJ.AMT to be inputted. |
| 27 | `CAMB.H.SL.PARAM.INT.ADJ.AMT` | `CambHSlParameter_IntAdjAmt` | TField |  | This field holds the amount up to which the variation in the interest portion can be adjusted.Used when posting an FT in the version FUNDS.TRANSFER,SL for the interest payment received from the Lead Banker.Note: This is applicable only when FI acts as a Participant bank in Syndicated loan.Note: Main reason for this check, is to make sure System does not blindly override the Bill amount, instead check the amount defined in INT.ADJ.AMT, if the adjustment amount is within range, bill amount will be modified using ADJUST BILL activity, else the bill amount will not be modified and FT will be posted with actual amount and exception log will be updated for same.Note: Either INT.ADJ.PERT or INT.ADJ.AMT to be inputted. |
| 28 | `CAMB.H.SL.PARAM.SL.ACTIVITY` | `CambHSlParameter_SlActivity` |  |  |  |
| 29 | `CAMB.H.SL.PARAM.SL.ACTION` | `CambHSlParameter_SlAction` |  |  |  |
| 30 | `CAMB.H.SL.PARAM.ACCOUNTING` | `CambHSlParameter_Accounting` |  |  |  |
| 31 | `CAMB.H.SL.PARAM.LOAN.TYPE` | `CambHSlParameter_LoanType` |  |  |  |
| 32 | `CAMB.H.SL.PARAM.ACCOUNTING.RULE` | `CambHSlParameter_AccountingRule` |  |  |  |
| 33 | `CAMB.H.SL.PARAM.DR.ACCOUNTING` | `CambHSlParameter_DrAccounting` |  |  |  |
| 34 | `CAMB.H.SL.PARAM.T24.DEBIT.ACCT` | `CambHSlParameter_T24DebitAcct` |  |  |  |
| 35 | `CAMB.H.SL.PARAM.CR.ACCOUNTING` | `CambHSlParameter_CrAccounting` |  |  |  |
| 36 | `CAMB.H.SL.PARAM.T24.CREDIT.ACCT` | `CambHSlParameter_T24CreditAcct` |  |  |  |
| 37 | `CAMB.H.SL.PARAM.RES.1` | `CambHSlParameter_Res1` |  |  |  |
| 38 | `CAMB.H.SL.PARAM.RES.2` | `CambHSlParameter_Res2` |  |  |  |
| 39 | `CAMB.H.SL.PARAM.RES.3` | `CambHSlParameter_Res3` |  |  |  |
| 40 | `CAMB.H.SL.PARAM.RES.4` | `CambHSlParameter_Res4` |  |  |  |
| 41 | `CAMB.H.SL.PARAM.RES.5` | `CambHSlParameter_Res5` |  |  |  |
| 42 | `CAMB.H.SL.PARAM.AC.BAL.TYPE` | `CambHSlParameter_AcBalType` |  |  |  |
| 43 | `CAMB.H.SL.PARAM.INT.BAL.TYPE` | `CambHSlParameter_IntBalType` |  |  |  |
| 44 | `CAMB.H.SL.PARAM.CLOSURE.BALANCE.TYPE` | `CambHSlParameter_ClosureBalanceType` | TField |  | This field is used to define a Balance Type used by AA Loans to close the SL.The balance type defined here is considered for calculation of closing the SL details.Validation - Must be valid ID in the AC.BALANCE.TYPE file in T24.eg. TOTCOMMITMENT. |
| 45 | `CAMB.H.SL.PARAM.RESERVED.2` | `CambHSlParameter_Reserved2` | TField |  |  |
| 46 | `CAMB.H.SL.PARAM.RESERVED.3` | `CambHSlParameter_Reserved3` | TField |  |  |
| 47 | `CAMB.H.SL.PARAM.RESERVED.4` | `CambHSlParameter_Reserved4` | TField |  |  |
| 48 | `CAMB.H.SL.PARAM.RESERVED.5` | `CambHSlParameter_Reserved5` | TField |  |  |
| 49 | `CAMB.H.SL.PARAM.OVERRIDE` | `CambHSlParameter_Override` |  |  |  |
| 50 | `CAMB.H.SL.PARAM.RECORD.STATUS` | `CambHSlParameter_RecordStatus` | String |  |  |
| 51 | `CAMB.H.SL.PARAM.CURR.NO` | `CambHSlParameter_CurrNo` | String |  |  |
| 52 | `CAMB.H.SL.PARAM.INPUTTER` | `CambHSlParameter_Inputter` |  |  |  |
| 53 | `CAMB.H.SL.PARAM.DATE.TIME` | `CambHSlParameter_DateTime` |  |  |  |
| 54 | `CAMB.H.SL.PARAM.AUTHORISER` | `CambHSlParameter_Authoriser` | String |  |  |
| 55 | `CAMB.H.SL.PARAM.CO.CODE` | `CambHSlParameter_CoCode` | String |  |  |
| 56 | `CAMB.H.SL.PARAM.DEPT.CODE` | `CambHSlParameter_DeptCode` | String |  |  |
| 57 | `CAMB.H.SL.PARAM.AUDITOR.CODE` | `CambHSlParameter_AuditorCode` | String |  |  |
| 58 | `CAMB.H.SL.PARAM.AUDIT.DATE.TIME` | `CambHSlParameter_AuditDateTime` | String |  |  |
