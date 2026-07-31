# ID.DEPOSIT.BALANCES.HIST — Table Schema

> Source: `INSERTS/I_F.ID.DEPOSIT.BALANCES.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IDBH.DEPOSIT.BAND` | `IdDepositBalancesHist_DepositBand` | TField |  |  |
| 2 | `ID.IDBH.PDS.ACTION.REF` | `IdDepositBalancesHist_PdsActionRef` | TField |  |  |
| 3 | `ID.IDBH.POOL` | `IdDepositBalancesHist_Pool` | TField |  |  |
| 4 | `ID.IDBH.CONTRACT.REF` | `IdDepositBalancesHist_ContractRef` | TField |  |  |
| 5 | `ID.IDBH.CUSTOMER` | `IdDepositBalancesHist_Customer` | TField |  |  |
| 6 | `ID.IDBH.DEPOSIT.TYPE` | `IdDepositBalancesHist_DepositType` | TField |  |  |
| 7 | `ID.IDBH.DAYS.IN.POOL` | `IdDepositBalancesHist_DaysInPool` | TField |  |  |
| 8 | `ID.IDBH.CONTRACT.CURRENCY` | `IdDepositBalancesHist_ContractCurrency` | TField |  |  |
| 9 | `ID.IDBH.EXCHANGE.RATE` | `IdDepositBalancesHist_ExchangeRate` | TField |  |  |
| 10 | `ID.IDBH.SIM.BALANCE.TYPE` | `IdDepositBalancesHist_SimBalanceType` | TField |  |  |
| 11 | `ID.IDBH.SIM.CONTRACT.BALANCE` | `IdDepositBalancesHist_SimContractBalance` | TField |  |  |
| 12 | `ID.IDBH.SIM.BALANCE.POOL.CCY` | `IdDepositBalancesHist_SimBalancePoolCcy` | TField |  |  |
| 13 | `ID.IDBH.DIST.BALANCE.TYPE` | `IdDepositBalancesHist_DistBalanceType` | TField |  |  |
| 14 | `ID.IDBH.DIST.CONTRACT.BALANCE` | `IdDepositBalancesHist_DistContractBalance` | TField |  |  |
| 15 | `ID.IDBH.DIST.BALANCE.POOL.CCY` | `IdDepositBalancesHist_DistBalancePoolCcy` | TField |  |  |
| 16 | `ID.IDBH.WEIGHTAGE` | `IdDepositBalancesHist_Weightage` | TField |  |  |
| 17 | `ID.IDBH.WEIGHTED.BALANCE` | `IdDepositBalancesHist_WeightedBalance` | TField |  |  |
| 18 | `ID.IDBH.NON.INVESTED.BALANCE` | `IdDepositBalancesHist_NonInvestedBalance` | TField |  |  |
| 19 | `ID.IDBH.CALCULATED.PROFIT` | `IdDepositBalancesHist_CalculatedProfit` | TField |  |  |
| 20 | `ID.IDBH.MUDARIB.FEE.PCT` | `IdDepositBalancesHist_MudaribFeePct` | TField |  |  |
| 21 | `ID.IDBH.MUDARIB.FEE` | `IdDepositBalancesHist_MudaribFee` | TField |  |  |
| 22 | `ID.IDBH.PROFIT.AFTER.MUDARIB` | `IdDepositBalancesHist_ProfitAfterMudarib` | TField |  |  |
| 23 | `ID.IDBH.PER.PCT` | `IdDepositBalancesHist_PerPct` | TField |  |  |
| 24 | `ID.IDBH.PER.AMOUNT` | `IdDepositBalancesHist_PerAmount` | TField |  |  |
| 25 | `ID.IDBH.PROFIT.AFTER.PER` | `IdDepositBalancesHist_ProfitAfterPer` | TField |  |  |
| 26 | `ID.IDBH.IRR.PCT` | `IdDepositBalancesHist_IrrPct` | TField |  |  |
| 27 | `ID.IDBH.IRR.AMOUNT` | `IdDepositBalancesHist_IrrAmount` | TField |  |  |
| 28 | `ID.IDBH.PROFIT.AFTER.IRR` | `IdDepositBalancesHist_ProfitAfterIrr` | TField |  |  |
| 29 | `ID.IDBH.RTN.ALTERED.PROFIT` | `IdDepositBalancesHist_RtnAlteredProfit` | TField |  |  |
| 30 | `ID.IDBH.PROFIT.AMOUNT` | `IdDepositBalancesHist_ProfitAmount` | TField |  |  |
| 31 | `ID.IDBH.PROFIT.PERCENT` | `IdDepositBalancesHist_ProfitPercent` | TField |  |  |
| 32 | `ID.IDBH.PAY.PROFIT` | `IdDepositBalancesHist_PayProfit` | TField |  |  |
| 33 | `ID.IDBH.NO.PROFIT.REASON` | `IdDepositBalancesHist_NoProfitReason` | TField |  |  |
| 34 | `ID.IDBH.EXCLUDED.BALANCE` | `IdDepositBalancesHist_ExcludedBalance` | TField |  |  |
| 35 | `ID.IDBH.EXCLUDED.BALANCE.POOL.CCY` | `IdDepositBalancesHist_ExcludedBalancePoolCcy` | TField |  |  |
| 36 | `ID.IDBH.EXPECTED.PROFIT` | `IdDepositBalancesHist_ExpectedProfit` | TField |  |  |
| 37 | `ID.IDBH.PAY.STATUS` | `IdDepositBalancesHist_PayStatus` | TField |  |  |
| 38 | `ID.IDBH.EM.EXCLUDED.BALANCE` | `IdDepositBalancesHist_EmExcludedBalance` | TField |  |  |
| 39 | `ID.IDBH.EM.EXCL.BAL.POOL.CCY` | `IdDepositBalancesHist_EmExclBalPoolCcy` | TField |  |  |
| 40 | `ID.IDBH.APPLY.PDS.PROFIT.RATE` | `IdDepositBalancesHist_ApplyPdsProfitRate` | TField |  |  |
| 41 | `ID.IDBH.SPL.HIBA.PROFIT` | `IdDepositBalancesHist_SplHibaProfit` | TField |  |  |
| 42 | `ID.IDBH.SPL.HIBA.AMOUNT` | `IdDepositBalancesHist_SplHibaAmount` | TField |  |  |
| 43 | `ID.IDBH.SPL.HIBA.STATUS` | `IdDepositBalancesHist_SplHibaStatus` | TField |  |  |
| 44 | `ID.IDBH.CALCULATED.PFT.POOL.CCY` | `IdDepositBalancesHist_CalculatedPftPoolCcy` | TField |  |  |
| 45 | `ID.IDBH.ARR.PAY.PROFIT` | `IdDepositBalancesHist_ArrPayProfit` | TField |  |  |
