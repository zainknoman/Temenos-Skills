# ID.ACCOUNT.BALANCES.HIST — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNT.BALANCES.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IABH.BALANCE.BAND` | `IdAccountBalancesHist_BalanceBand` | TField |  | This field will define the balance bracket under which the arrangement falls. |
| 2 | `ID.IABH.PDS.ACTION.REF` | `IdAccountBalancesHist_PdsActionRef` | TField |  | This field will hold the PDS Action Reference. Validation Rules: 1. Must be a valid record in ID.PDS.ACTION. |
| 3 | `ID.IABH.POOL` | `IdAccountBalancesHist_Pool` | TField |  | This field will hold the reference of the pool parameter. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Must be a valid record from the file ID.POOL.PARAMETER. |
| 4 | `ID.IABH.ACCOUNT.NO` | `IdAccountBalancesHist_AccountNo` | TField |  | This field will specify the account reference number linked to the arrangement. Validation Rules: 1. Must be a valid record in ACCOUNT. |
| 5 | `ID.IABH.CUSTOMER` | `IdAccountBalancesHist_Customer` | TField |  | This field will denote the customer of the arrangement. Validation Rules: 1. Must be a valid record in CUSTOMER. |
| 6 | `ID.IABH.ACCOUNT.TYPE` | `IdAccountBalancesHist_AccountType` | TField |  | This field will specify the type of account. |
| 7 | `ID.IABH.DAYS.IN.POOL` | `IdAccountBalancesHist_DaysInPool` | TField |  | This field will specify the number of days the arrangement was available in the pool during Simulation. Validation Rules: 1. Standard T24 Alphanumeric field. |
| 8 | `ID.IABH.ACCOUNT.CURRENCY` | `IdAccountBalancesHist_AccountCurrency` | TField |  | This field will hold the currency of the arrangement contract. Validation Rules: 1. Must be a valid record in CURRENCY. |
| 9 | `ID.IABH.EXCHANGE.RATE` | `IdAccountBalancesHist_ExchangeRate` | TField |  | This field will hold the exchange rate used for currency conversion. |
| 10 | `ID.IABH.SIM.BALANCE.TYPE` | `IdAccountBalancesHist_SimBalanceType` | TField |  | This field will determine the type of balance based upon which Simulation calculation will be carried out. 1. Holds only 1 of the 3 values : Average, Minimum and Daily. |
| 11 | `ID.IABH.SIM.ACCOUNT.BALANCE` | `IdAccountBalancesHist_SimAccountBalance` | TField |  | This field will hold the calculated balance amount based on the balance type specified. |
| 12 | `ID.IABH.SIM.BALANCE.POOL.CCY` | `IdAccountBalancesHist_SimBalancePoolCcy` | TField |  | This field will hold the calculated balance amount in pool currency. |
| 13 | `ID.IABH.DIST.BALANCE.TYPE` | `IdAccountBalancesHist_DistBalanceType` | TField |  | This field will determine the type of balance based upon which Simulation calculation will be carried out. 1. Holds only 1 of the 3 values : Average, Minimum and Daily. Reserved for future purposes. |
| 14 | `ID.IABH.DIST.ACCOUNT.BALANCE` | `IdAccountBalancesHist_DistAccountBalance` | TField |  | Reserved for future purposes. |
| 15 | `ID.IABH.DIST.BALANCE.POOL.CCY` | `IdAccountBalancesHist_DistBalancePoolCcy` | TField |  | This field will hold the calculated balance amount in pool currency. Reserved for future purposes. |
| 16 | `ID.IABH.WEIGHTAGE` | `IdAccountBalancesHist_Weightage` | TField |  | This field will specify the weightage used for the particular contract. Validation Rules: 1. Must be a valid record in ID.PDS.WEIGHT for the particular pool, category and currency. |
| 17 | `ID.IABH.WEIGHTED.BALANCE` | `IdAccountBalancesHist_WeightedBalance` | TField |  | This field will display the balance as a product of the Sim Account Balance and its Weightage. |
| 18 | `ID.IABH.NON.INVESTED.BALANCE` | `IdAccountBalancesHist_NonInvestedBalance` | TField |  | This field will display the difference of Sim Account Balance and Weighted Balance. |
| 19 | `ID.IABH.CALCULATED.PROFIT` | `IdAccountBalancesHist_CalculatedProfit` | TField |  | This field will hold the profit amount for the arrangement contract after Simulation. |
| 20 | `ID.IABH.MUDARIB.FEE.PCT` | `IdAccountBalancesHist_MudaribFeePct` | TField |  | This field will specify the mudarib fee percentage used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 21 | `ID.IABH.MUDARIB.FEE` | `IdAccountBalancesHist_MudaribFee` | TField |  | This field will specify the calculated mudarib fee amount. |
| 22 | `ID.IABH.PROFIT.AFTER.MUDARIB` | `IdAccountBalancesHist_ProfitAfterMudarib` | TField |  | This field will hold the profit amount after deducting the MUDARIB.AMOUNT. |
| 23 | `ID.IABH.PER.PCT` | `IdAccountBalancesHist_PerPct` | TField |  | This field will specify the profit equalisation reserve percentage used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 24 | `ID.IABH.PER.AMOUNT` | `IdAccountBalancesHist_PerAmount` | TField |  | This field will specify the calculated profit equalisation reserve amount. |
| 25 | `ID.IABH.PROFIT.AFTER.PER` | `IdAccountBalancesHist_ProfitAfterPer` | TField |  | This field will hold the profit amount after deducting the PER.AMOUNT. |
| 26 | `ID.IABH.IRR.PCT` | `IdAccountBalancesHist_IrrPct` | TField |  | This field will specify the investment risk reserve percentage used in the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 27 | `ID.IABH.IRR.AMOUNT` | `IdAccountBalancesHist_IrrAmount` | TField |  | This field will specify the calculated investment risk reserve amount. |
| 28 | `ID.IABH.PROFIT.AFTER.IRR` | `IdAccountBalancesHist_ProfitAfterIrr` | TField |  | This field will hold the profit amount after deducting the IRR.AMOUNT. |
| 29 | `ID.IABH.RTN.ALTERED.PROFIT` | `IdAccountBalancesHist_RtnAlteredProfit` | TField |  | This field will hold the profit amount altered by attached routine. |
| 30 | `ID.IABH.PROFIT.AMOUNT` | `IdAccountBalancesHist_ProfitAmount` | TField |  | This field will hold the final profit amount to be paid after deduction of IRR, PER and Mudarib amounts. |
| 31 | `ID.IABH.PROFIT.PERCENT` | `IdAccountBalancesHist_ProfitPercent` | TField |  | This field will hold the final profit rate used for profit distribution. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 32 | `ID.IABH.PAY.PROFIT` | `IdAccountBalancesHist_PayProfit` | TField |  | This field is used to identify whether the arrangement is eligible for profit payment or not. Validation Rules: 1. Holds either Yes or No. |
| 33 | `ID.IABH.NO.PROFIT.REASON` | `IdAccountBalancesHist_NoProfitReason` | TField |  | This field will be updated when PAY.PROFIT is set as NO and the reason for not paying the profit amount to the Arrangement. |
| 34 | `ID.IABH.EXCLUDED.BALANCE` | `IdAccountBalancesHist_ExcludedBalance` | TField |  | This field will specify the balance amounts excluded during Simulation. This may be due to the fact that the account was closed before simulation or the account did not have minimum balance as mentioned in ID.PDS.CATEGORY. |
| 35 | `ID.IABH.EXCLUDED.BALANCE.POOL.CCY` | `IdAccountBalancesHist_ExcludedBalancePoolCcy` | TField |  | This field will specify the excluded balance in pool currency. |
| 36 | `ID.IABH.PAY.STATUS` | `IdAccountBalancesHist_PayStatus` | TField |  | This field will specify whether profit amount is paid or not. Validation Rules: 1. Holds either Due or Paid. |
| 37 | `ID.IABH.SPL.HIBA.PROFIT` | `IdAccountBalancesHist_SplHibaProfit` | TField |  | This field will specify if the arrangement is eligible for Spl Hiba profit. Validation Rules: 1. Holds either Yes or No. |
| 38 | `ID.IABH.SPL.HIBA.AMOUNT` | `IdAccountBalancesHist_SplHibaAmount` | TField |  | This field will hold the Spl Hiba amount to be paid. |
| 39 | `ID.IABH.SPL.HIBA.STATUS` | `IdAccountBalancesHist_SplHibaStatus` | TField |  | This field will specify if Spl Hiba has been paid or not. Validation Rules: 1. Holds either Due or Paid. |
| 40 | `ID.IABH.TIER.TYPE.ID` | `IdAccountBalancesHist_TierTypeId` | TField |  | This field will capture the tier wise group id(for BAND - B1,B2,... and for LEVEL - L1,L2,...) for each of the arrangement account. |
| 41 | `ID.IABH.CALCULATED.PFT.POOL.CCY` | `IdAccountBalancesHist_CalculatedPftPoolCcy` | TField |  | This field will hold the profit amount for the arrangement contract after Simulation in pool currency. |
| 42 | `ID.IABH.ELIGIBILITY.TO.CLOSE.ON.PDS` | `IdAccountBalancesHist_EligibilityToCloseOnPds` | TField |  | This field is used to know if an Islamic accounts arrangement is marked to close during PDS. This field will contain the value 'YES' if the account is marked to close during PDS. |
| 43 | `ID.IABH.CLOSE.REQUEST.DATE` | `IdAccountBalancesHist_CloseRequestDate` | TField |  | This field is updated with the closure requested date whenever an Islamic accounts arrangement is marked to close during PDS. |
| 44 | `ID.IABH.RESERVED.2` | `IdAccountBalancesHist_Reserved2` |  |  |  |
| 45 | `ID.IABH.RESERVED.1` | `IdAccountBalancesHist_Reserved1` |  |  |  |
