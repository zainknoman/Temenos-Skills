# ID.PDS.ACTION.DETAILS.HIST — Table Schema

> Source: `INSERTS/I_F.ID.PDS.ACTION.DETAILS.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPDH.ACTION` | `IdPdsActionDetailsHist_Action` | TField |  |  |
| 2 | `ID.IPDH.POOL.REF` | `IdPdsActionDetailsHist_PoolRef` | TField |  |  |
| 3 | `ID.IPDH.SH.AMOUNT` | `IdPdsActionDetailsHist_ShAmount` | TField |  |  |
| 4 | `ID.IPDH.SH.TOTAL.AMOUNT` | `IdPdsActionDetailsHist_ShTotalAmount` | TField |  |  |
| 5 | `ID.IPDH.SH.PROFIT.AMOUNT` | `IdPdsActionDetailsHist_ShProfitAmount` | TField |  |  |
| 6 | `ID.IPDH.NET.PROFIT.AMOUNT` | `IdPdsActionDetailsHist_NetProfitAmount` | TField |  |  |
| 7 | `ID.IPDH.TOTAL.BALANCE` | `IdPdsActionDetailsHist_TotalBalance` | TField |  |  |
| 8 | `ID.IPDH.TOTAL.WEIGHTED.BALANCES` | `IdPdsActionDetailsHist_TotalWeightedBalances` | TField |  |  |
| 9 | `ID.IPDH.TOTAL.WAK.BALANCE` | `IdPdsActionDetailsHist_TotalWakBalance` | TField |  |  |
| 10 | `ID.IPDH.TOTAL.WAK.WEIGHTED.BALANCES` | `IdPdsActionDetailsHist_TotalWakWeightedBalances` | TField |  |  |
| 11 | `ID.IPDH.TOTAL.AFTER.PER.BAL` | `IdPdsActionDetailsHist_TotalAfterPerBal` | TField |  |  |
| 12 | `ID.IPDH.TOTAL.AFTER.MUD.BAL` | `IdPdsActionDetailsHist_TotalAfterMudBal` | TField |  |  |
| 13 | `ID.IPDH.TOTAL.AFTER.IRR.BAL` | `IdPdsActionDetailsHist_TotalAfterIrrBal` | TField |  |  |
| 14 | `ID.IPDH.TOTAL.ACCT.BALANCE` | `IdPdsActionDetailsHist_TotalAcctBalance` | TField |  |  |
| 15 | `ID.IPDH.ACCT.WEIGHTED.BALANCE` | `IdPdsActionDetailsHist_AcctWeightedBalance` | TField |  |  |
| 16 | `ID.IPDH.ACCT.EXCL.BALANCES` | `IdPdsActionDetailsHist_AcctExclBalances` | TField |  |  |
| 17 | `ID.IPDH.TOTAL.DEPOSIT.BALANCE` | `IdPdsActionDetailsHist_TotalDepositBalance` | TField |  |  |
| 18 | `ID.IPDH.DEPOSIT.WEIGHTED.BALANCE` | `IdPdsActionDetailsHist_DepositWeightedBalance` | TField |  |  |
| 19 | `ID.IPDH.DEPOSIT.EXCL.BALANCES` | `IdPdsActionDetailsHist_DepositExclBalances` | TField |  |  |
| 20 | `ID.IPDH.AVG.SH.INVESTED.AMT` | `IdPdsActionDetailsHist_AvgShInvestedAmt` | TField |  |  |
| 21 | `ID.IPDH.HIBA.AMOUNT` | `IdPdsActionDetailsHist_HibaAmount` | TField |  |  |
| 22 | `ID.IPDH.RTN.ALTERED.PROFIT` | `IdPdsActionDetailsHist_RtnAlteredProfit` | TField |  |  |
| 23 | `ID.IPDH.TRGT.PRFT.AMT` | `IdPdsActionDetailsHist_TrgtPrftAmt` | TField |  |  |
| 24 | `ID.IPDH.CALCULATED.PROFIT` | `IdPdsActionDetailsHist_CalculatedProfit` | TField |  |  |
| 25 | `ID.IPDH.DEPOSIT.EM.BALANCE` | `IdPdsActionDetailsHist_DepositEmBalance` | TField |  |  |
| 26 | `ID.IPDH.AC.NON.INV.BALANCE` | `IdPdsActionDetailsHist_AcNonInvBalance` | TField |  |  |
| 27 | `ID.IPDH.DEP.NON.INV.BALANCE` | `IdPdsActionDetailsHist_DepNonInvBalance` | TField |  |  |
| 28 | `ID.IPDH.PRFT.AFT.ADDL.RESRV` | `IdPdsActionDetailsHist_PrftAftAddlResrv` | TField |  |  |
| 29 | `ID.IPDH.MUD.EXPECTED.PROFIT` | `IdPdsActionDetailsHist_MudExpectedProfit` | TField |  |  |
| 30 | `ID.IPDH.MUD.PDS.PROFIT` | `IdPdsActionDetailsHist_MudPdsProfit` | TField |  |  |
| 31 | `ID.IPDH.DIST.RUN.DATE` | `IdPdsActionDetailsHist_DistRunDate` | TField |  |  |
| 32 | `ID.IPDH.POOL.CURRENCY` | `IdPdsActionDetailsHist_PoolCurrency` | TField |  |  |
| 33 | `ID.IPDH.TOTAL.ARR.PAY.PROFIT` | `IdPdsActionDetailsHist_TotalArrPayProfit` | TField |  |  |
| 34 | `ID.IPDH.STMT.NOS` | `IdPdsActionDetailsHist_StmtNos` |  |  |  |
