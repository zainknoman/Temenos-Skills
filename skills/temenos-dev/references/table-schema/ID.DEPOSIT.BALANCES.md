# ID.DEPOSIT.BALANCES — Table Schema

> Source: `INSERTS/I_F.ID.DEPOSIT.BALANCES` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IDB.DEPOSIT.BAND` | `IdDepositBalances_DepositBand` | TField |  |  |
| 2 | `ID.IDB.PDS.ACTION.REF` | `IdDepositBalances_PdsActionRef` | TField |  |  |
| 3 | `ID.IDB.POOL` | `IdDepositBalances_Pool` | TField |  |  |
| 4 | `ID.IDB.CONTRACT.REF` | `IdDepositBalances_ContractRef` | TField |  |  |
| 5 | `ID.IDB.CUSTOMER` | `IdDepositBalances_Customer` | TField |  |  |
| 6 | `ID.IDB.DEPOSIT.TYPE` | `IdDepositBalances_DepositType` | TField |  |  |
| 7 | `ID.IDB.DAYS.IN.POOL` | `IdDepositBalances_DaysInPool` | TField |  |  |
| 8 | `ID.IDB.CONTRACT.CURRENCY` | `IdDepositBalances_ContractCurrency` | TField |  |  |
| 9 | `ID.IDB.EXCHANGE.RATE` | `IdDepositBalances_ExchangeRate` | TField |  |  |
| 10 | `ID.IDB.SIM.BALANCE.TYPE` | `IdDepositBalances_SimBalanceType` | TField |  |  |
| 11 | `ID.IDB.SIM.CONTRACT.BALANCE` | `IdDepositBalances_SimContractBalance` | TField |  |  |
| 12 | `ID.IDB.SIM.BALANCE.POOL.CCY` | `IdDepositBalances_SimBalancePoolCcy` | TField |  |  |
| 13 | `ID.IDB.DIST.BALANCE.TYPE` | `IdDepositBalances_DistBalanceType` | TField |  |  |
| 14 | `ID.IDB.DIST.CONTRACT.BALANCE` | `IdDepositBalances_DistContractBalance` | TField |  |  |
| 15 | `ID.IDB.DIST.BALANCE.POOL.CCY` | `IdDepositBalances_DistBalancePoolCcy` | TField |  |  |
| 16 | `ID.IDB.WEIGHTAGE` | `IdDepositBalances_Weightage` | TField |  |  |
| 17 | `ID.IDB.WEIGHTED.BALANCE` | `IdDepositBalances_WeightedBalance` | TField |  |  |
| 18 | `ID.IDB.NON.INVESTED.BALANCE` | `IdDepositBalances_NonInvestedBalance` | TField |  |  |
| 19 | `ID.IDB.CALCULATED.PROFIT` | `IdDepositBalances_CalculatedProfit` | TField |  |  |
| 20 | `ID.IDB.MUDARIB.FEE.PCT` | `IdDepositBalances_MudaribFeePct` | TField |  |  |
| 21 | `ID.IDB.MUDARIB.FEE` | `IdDepositBalances_MudaribFee` | TField |  |  |
| 22 | `ID.IDB.PROFIT.AFTER.MUDARIB` | `IdDepositBalances_ProfitAfterMudarib` | TField |  |  |
| 23 | `ID.IDB.PER.PCT` | `IdDepositBalances_PerPct` | TField |  |  |
| 24 | `ID.IDB.PER.AMOUNT` | `IdDepositBalances_PerAmount` | TField |  |  |
| 25 | `ID.IDB.PROFIT.AFTER.PER` | `IdDepositBalances_ProfitAfterPer` | TField |  |  |
| 26 | `ID.IDB.IRR.PCT` | `IdDepositBalances_IrrPct` | TField |  |  |
| 27 | `ID.IDB.IRR.AMOUNT` | `IdDepositBalances_IrrAmount` | TField |  |  |
| 28 | `ID.IDB.PROFIT.AFTER.IRR` | `IdDepositBalances_ProfitAfterIrr` | TField |  |  |
| 29 | `ID.IDB.RTN.ALTERED.PROFIT` | `IdDepositBalances_RtnAlteredProfit` | TField |  |  |
| 30 | `ID.IDB.PROFIT.AMOUNT` | `IdDepositBalances_ProfitAmount` | TField |  |  |
| 31 | `ID.IDB.PROFIT.PERCENT` | `IdDepositBalances_ProfitPercent` | TField |  |  |
| 32 | `ID.IDB.PAY.PROFIT` | `IdDepositBalances_PayProfit` | TField |  |  |
| 33 | `ID.IDB.NO.PROFIT.REASON` | `IdDepositBalances_NoProfitReason` | TField |  |  |
| 34 | `ID.IDB.EXCLUDED.BALANCE` | `IdDepositBalances_ExcludedBalance` | TField |  |  |
| 35 | `ID.IDB.EXCLUDED.BALANCE.POOL.CCY` | `IdDepositBalances_ExcludedBalancePoolCcy` | TField |  |  |
| 36 | `ID.IDB.EXPECTED.PROFIT` | `IdDepositBalances_ExpectedProfit` | TField |  |  |
| 37 | `ID.IDB.PAY.STATUS` | `IdDepositBalances_PayStatus` | TField |  |  |
| 38 | `ID.IDB.EM.EXCLUDED.BALANCE` | `IdDepositBalances_EmExcludedBalance` | TField |  |  |
| 39 | `ID.IDB.EM.EXCL.BAL.POOL.CCY` | `IdDepositBalances_EmExclBalPoolCcy` | TField |  |  |
| 40 | `ID.IDB.APPLY.PDS.PROFIT.RATE` | `IdDepositBalances_ApplyPdsProfitRate` | TField |  |  |
| 41 | `ID.IDB.SPL.HIBA.PROFIT` | `IdDepositBalances_SplHibaProfit` | TField |  |  |
| 42 | `ID.IDB.SPL.HIBA.AMOUNT` | `IdDepositBalances_SplHibaAmount` | TField |  |  |
| 43 | `ID.IDB.SPL.HIBA.STATUS` | `IdDepositBalances_SplHibaStatus` | TField |  |  |
| 44 | `ID.IDB.CALCULATED.PFT.POOL.CCY` | `IdDepositBalances_CalculatedPftPoolCcy` | TField |  |  |
| 45 | `ID.IDB.ARR.PAY.PROFIT` | `IdDepositBalances_ArrPayProfit` | TField |  |  |
