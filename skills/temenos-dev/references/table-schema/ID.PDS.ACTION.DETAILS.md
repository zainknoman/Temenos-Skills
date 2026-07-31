# ID.PDS.ACTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.PDS.ACTION.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPD.ACTION` | `IdPdsActionDetails_Action` | TField |  | This defines the PDS action to be performed. Validation Rules: 1. Standard T24 Alphanumeric field.. |
| 2 | `ID.IPD.POOL.REF` | `IdPdsActionDetails_PoolRef` | TField |  | This field holds the reference of the pool parameter. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Must be a valid record from the file ID.POOL.PARAMETER. |
| 3 | `ID.IPD.SH.AMOUNT` | `IdPdsActionDetails_ShAmount` | TField |  | The Share Holder investment amount to be used for calculation. |
| 4 | `ID.IPD.SH.TOTAL.AMOUNT` | `IdPdsActionDetails_ShTotalAmount` | TField |  | The Total Share Holder investment amount to be used for calculation. |
| 5 | `ID.IPD.SH.PROFIT.AMOUNT` | `IdPdsActionDetails_ShProfitAmount` | TField |  | The Share Holder profit amount to be used for calculation. |
| 6 | `ID.IPD.NET.PROFIT.AMOUNT` | `IdPdsActionDetails_NetProfitAmount` | TField |  | The Net profit amount to be used for calculation. |
| 7 | `ID.IPD.TOTAL.BALANCE` | `IdPdsActionDetails_TotalBalance` | TField |  | The total average balance of all the contracts to be used for the calculation. Validation Rules: 1. Valid values are 'Y' and NULL while checking and unchecking the checkbox respectively. |
| 8 | `ID.IPD.TOTAL.WEIGHTED.BALANCES` | `IdPdsActionDetails_TotalWeightedBalances` | TField |  | The total weighted average balance of all the contracts to be used for the calculation. |
| 9 | `ID.IPD.TOTAL.WAK.BALANCE` | `IdPdsActionDetails_TotalWakBalance` | TField |  | The total wakala balance of all the contracts to be used for the calculation. |
| 10 | `ID.IPD.TOTAL.WAK.WEIGHTED.BALANCES` | `IdPdsActionDetails_TotalWakWeightedBalances` | TField |  | The total weighted wakala average balance of all the contracts to be used for the calculation. |
| 11 | `ID.IPD.TOTAL.AFTER.PER.BAL` | `IdPdsActionDetails_TotalAfterPerBal` | TField |  | The profit amount calculated after the profit equalisation reserve is set. |
| 12 | `ID.IPD.TOTAL.AFTER.MUD.BAL` | `IdPdsActionDetails_TotalAfterMudBal` | TField |  | The profit amount calculated after the mudarib share is set. Validation Rules: 1. Must be a valid record from the table IS.PARAMETER. |
| 13 | `ID.IPD.TOTAL.AFTER.IRR.BAL` | `IdPdsActionDetails_TotalAfterIrrBal` | TField |  | The profit amount calculated after the Investment equalisation reserve is set. |
| 14 | `ID.IPD.TOTAL.ACCT.BALANCE` | `IdPdsActionDetails_TotalAcctBalance` | TField |  |  |
| 15 | `ID.IPD.ACCT.WEIGHTED.BALANCE` | `IdPdsActionDetails_AcctWeightedBalance` | TField |  |  |
| 16 | `ID.IPD.ACCT.EXCL.BALANCES` | `IdPdsActionDetails_AcctExclBalances` | TField |  |  |
| 17 | `ID.IPD.TOTAL.DEPOSIT.BALANCE` | `IdPdsActionDetails_TotalDepositBalance` | TField |  |  |
| 18 | `ID.IPD.DEPOSIT.WEIGHTED.BALANCE` | `IdPdsActionDetails_DepositWeightedBalance` | TField |  |  |
| 19 | `ID.IPD.DEPOSIT.EXCL.BALANCES` | `IdPdsActionDetails_DepositExclBalances` | TField |  |  |
| 20 | `ID.IPD.AVG.SH.INVESTED.AMT` | `IdPdsActionDetails_AvgShInvestedAmt` | TField |  |  |
| 21 | `ID.IPD.HIBA.AMOUNT` | `IdPdsActionDetails_HibaAmount` | TField |  |  |
| 22 | `ID.IPD.RTN.ALTERED.PROFIT` | `IdPdsActionDetails_RtnAlteredProfit` | TField |  |  |
| 23 | `ID.IPD.TRGT.PRFT.AMT` | `IdPdsActionDetails_TrgtPrftAmt` | TField |  |  |
| 24 | `ID.IPD.CALCULATED.PROFIT` | `IdPdsActionDetails_CalculatedProfit` | TField |  |  |
| 25 | `ID.IPD.DEPOSIT.EM.BALANCE` | `IdPdsActionDetails_DepositEmBalance` | TField |  |  |
| 26 | `ID.IPD.AC.NON.INV.BALANCE` | `IdPdsActionDetails_AcNonInvBalance` | TField |  |  |
| 27 | `ID.IPD.DEP.NON.INV.BALANCE` | `IdPdsActionDetails_DepNonInvBalance` | TField |  |  |
| 28 | `ID.IPD.PRFT.AFT.ADDL.RESRV` | `IdPdsActionDetails_PrftAftAddlResrv` | TField |  |  |
| 29 | `ID.IPD.MUD.EXPECTED.PROFIT` | `IdPdsActionDetails_MudExpectedProfit` | TField |  |  |
| 30 | `ID.IPD.MUD.PDS.PROFIT` | `IdPdsActionDetails_MudPdsProfit` | TField |  |  |
| 31 | `ID.IPD.DIST.RUN.DATE` | `IdPdsActionDetails_DistRunDate` | TField |  |  |
| 32 | `ID.IPD.POOL.CURRENCY` | `IdPdsActionDetails_PoolCurrency` | TField |  |  |
| 33 | `ID.IPD.TOTAL.ARR.PAY.PROFIT` | `IdPdsActionDetails_TotalArrPayProfit` | TField |  | This field holds the value of total profit amount distributed across deposits/accounts. This will hold the consolidated rounded values of all the deposits/accounts (from AA.INTEREST.ACCRUALS) participated in the PDS Distribution. |
| 34 | `ID.IPD.STMT.NOS` | `IdPdsActionDetails_StmtNos` |  |  |  |
