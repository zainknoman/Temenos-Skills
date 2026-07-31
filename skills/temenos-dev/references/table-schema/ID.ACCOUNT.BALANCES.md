# ID.ACCOUNT.BALANCES — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNT.BALANCES` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IAB.BALANCE.BAND` | `IdAccountBalances_BalanceBand` | TField |  | This field will define the balance bracket under which the arrangement falls. |
| 2 | `ID.IAB.PDS.ACTION.REF` | `IdAccountBalances_PdsActionRef` | TField |  | This field will hold the PDS Action Reference. Validation Rules: 1. Must be a valid record in ID.PDS.ACTION. |
| 3 | `ID.IAB.POOL` | `IdAccountBalances_Pool` | TField |  | This field will hold the reference of the pool parameter. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Must be a valid record from the file ID.POOL.PARAMETER. |
| 4 | `ID.IAB.ACCOUNT.NO` | `IdAccountBalances_AccountNo` | TField |  | This field will specify the account reference number linked to the arrangement. Validation Rules: 1. Must be a valid record in ACCOUNT. |
| 5 | `ID.IAB.CUSTOMER` | `IdAccountBalances_Customer` | TField |  | This field will denote the customer of the arrangement. Validation Rules: 1. Must be a valid record in CUSTOMER. |
| 6 | `ID.IAB.ACCOUNT.TYPE` | `IdAccountBalances_AccountType` | TField |  | This field will specify the type of account. |
| 7 | `ID.IAB.DAYS.IN.POOL` | `IdAccountBalances_DaysInPool` | TField |  | This field will specify the number of days the arrangement was available in the pool during Simulation. Validation Rules: 1. Standard T24 Alphanumeric field. |
| 8 | `ID.IAB.ACCOUNT.CURRENCY` | `IdAccountBalances_AccountCurrency` | TField |  | This field will hold the currency of the arrangement contract. Validation Rules: 1. Must be a valid record in CURRENCY. |
| 9 | `ID.IAB.EXCHANGE.RATE` | `IdAccountBalances_ExchangeRate` | TField |  | This field will hold the exchange rate used for currency conversion. |
| 10 | `ID.IAB.SIM.BALANCE.TYPE` | `IdAccountBalances_SimBalanceType` | TField |  | This field will determine the type of balance based upon which Simulation calculation will be carried out. 1. Holds only 1 of the 3 values : Average, Minimum and Daily. |
| 11 | `ID.IAB.SIM.ACCOUNT.BALANCE` | `IdAccountBalances_SimAccountBalance` | TField |  | This field will hold the calculated balance amount based on the balance type specified. |
| 12 | `ID.IAB.SIM.BALANCE.POOL.CCY` | `IdAccountBalances_SimBalancePoolCcy` | TField |  | This field will hold the calculated balance amount in pool currency. |
| 13 | `ID.IAB.DIST.BALANCE.TYPE` | `IdAccountBalances_DistBalanceType` | TField |  | This field will determine the type of balance based upon which Simulation calculation will be carried out. 1. Holds only 1 of the 3 values : Average, Minimum and Daily. Reserved for future purposes. |
| 14 | `ID.IAB.DIST.ACCOUNT.BALANCE` | `IdAccountBalances_DistAccountBalance` | TField |  | Reserved for future purposes. |
| 15 | `ID.IAB.DIST.BALANCE.POOL.CCY` | `IdAccountBalances_DistBalancePoolCcy` | TField |  | This field will hold the calculated balance amount in pool currency. Reserved for future purposes. |
| 16 | `ID.IAB.WEIGHTAGE` | `IdAccountBalances_Weightage` | TField |  | This field will specify the weightage used for the particular contract. Validation Rules: 1. Must be a valid record in ID.PDS.WEIGHT for the particular pool, category and currency. |
| 17 | `ID.IAB.WEIGHTED.BALANCE` | `IdAccountBalances_WeightedBalance` | TField |  | This field will display the balance as a product of the Sim Account Balance and its Weightage. |
| 18 | `ID.IAB.NON.INVESTED.BALANCE` | `IdAccountBalances_NonInvestedBalance` | TField |  | This field will display the difference of Sim Account Balance and Weighted Balance. |
| 19 | `ID.IAB.CALCULATED.PROFIT` | `IdAccountBalances_CalculatedProfit` | TField |  | This field will hold the profit amount for the arrangement contract after Simulation. |
| 20 | `ID.IAB.MUDARIB.FEE.PCT` | `IdAccountBalances_MudaribFeePct` | TField |  | This field will specify the mudarib fee percentage used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 21 | `ID.IAB.MUDARIB.FEE` | `IdAccountBalances_MudaribFee` | TField |  | This field will specify the calculated mudarib fee amount. |
| 22 | `ID.IAB.PROFIT.AFTER.MUDARIB` | `IdAccountBalances_ProfitAfterMudarib` | TField |  | This field will hold the profit amount after deducting the MUDARIB.AMOUNT. |
| 23 | `ID.IAB.PER.PCT` | `IdAccountBalances_PerPct` | TField |  | This field will specify the profit equalisation reserve percentage used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 24 | `ID.IAB.PER.AMOUNT` | `IdAccountBalances_PerAmount` | TField |  | This field will specify the calculated profit equalisation reserve amount. |
| 25 | `ID.IAB.PROFIT.AFTER.PER` | `IdAccountBalances_ProfitAfterPer` | TField |  | This field will hold the profit amount after deducting the PER.AMOUNT. |
| 26 | `ID.IAB.IRR.PCT` | `IdAccountBalances_IrrPct` | TField |  | This field will specify the investment risk reserve percentage used in the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 27 | `ID.IAB.IRR.AMOUNT` | `IdAccountBalances_IrrAmount` | TField |  | This field will specify the calculated investment risk reserve amount. |
| 28 | `ID.IAB.PROFIT.AFTER.IRR` | `IdAccountBalances_ProfitAfterIrr` | TField |  | This field will hold the profit amount after deducting the IRR.AMOUNT. |
| 29 | `ID.IAB.RTN.ALTERED.PROFIT` | `IdAccountBalances_RtnAlteredProfit` | TField |  | This field will hold the profit amount altered by attached routine. |
| 30 | `ID.IAB.PROFIT.AMOUNT` | `IdAccountBalances_ProfitAmount` | TField |  | This field will hold the final profit amount to be paid after deduction of IRR, PER and Mudarib amounts. |
| 31 | `ID.IAB.PROFIT.PERCENT` | `IdAccountBalances_ProfitPercent` | TField |  | This field will hold the final profit rate used for profit distribution. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 32 | `ID.IAB.PAY.PROFIT` | `IdAccountBalances_PayProfit` | TField |  | This field is used to identify whether the arrangement is eligible for profit payment or not. Validation Rules: 1. Holds either Yes or No. |
| 33 | `ID.IAB.NO.PROFIT.REASON` | `IdAccountBalances_NoProfitReason` | TField |  | This field will be updated when PAY.PROFIT is set as NO and the reason for not paying the profit amount to the Arrangement. |
| 34 | `ID.IAB.EXCLUDED.BALANCE` | `IdAccountBalances_ExcludedBalance` | TField |  | This field will specify the balance amounts excluded during Simulation. This may be due to the fact that the account was closed before simulation or the account did not have minimum balance as mentioned in ID.PDS.CATEGORY. |
| 35 | `ID.IAB.EXCLUDED.BALANCE.POOL.CCY` | `IdAccountBalances_ExcludedBalancePoolCcy` | TField |  | This field will specify the excluded balance in pool currency. |
| 36 | `ID.IAB.PAY.STATUS` | `IdAccountBalances_PayStatus` | TField |  | This field will specify whether profit amount is paid or not. Validation Rules: 1. Holds either Due or Paid. |
| 37 | `ID.IAB.SPL.HIBA.PROFIT` | `IdAccountBalances_SplHibaProfit` | TField |  | This field will specify if the arrangement is eligible for Spl Hiba profit. Validation Rules: 1. Holds either Yes or No. |
| 38 | `ID.IAB.SPL.HIBA.AMOUNT` | `IdAccountBalances_SplHibaAmount` | TField |  | This field will hold the Spl Hiba amount to be paid. |
| 39 | `ID.IAB.SPL.HIBA.STATUS` | `IdAccountBalances_SplHibaStatus` | TField |  | This field will specify if Spl Hiba has been paid or not. Validation Rules: 1. Holds either Due or Paid. |
| 40 | `ID.IAB.TIER.TYPE.ID` | `IdAccountBalances_TierTypeId` | TField |  | This field will capture the tier wise group id(for BAND - B1,B2,... and for LEVEL - L1,L2,...) for each of the arrangement account. |
| 41 | `ID.IAB.CALCULATED.PFT.POOL.CCY` | `IdAccountBalances_CalculatedPftPoolCcy` | TField |  | This field will hold the profit amount for the arrangement contract after Simulation in pool currency. |
| 42 | `ID.IAB.ELIGIBILITY.TO.CLOSE.ON.PDS` | `IdAccountBalances_EligibilityToCloseOnPds` | TField |  | This field is used to know if an Islamic accounts arrangement is marked to close during PDS. This field will contain the value 'YES' if the account is marked to close during PDS. |
| 43 | `ID.IAB.CLOSE.REQUEST.DATE` | `IdAccountBalances_CloseRequestDate` | TField |  | This field is updated with the closure requested date whenever an Islamic accounts arrangement is marked to close during PDS. |
| 44 | `ID.IAB.RESERVED.2` | `IdAccountBalances_Reserved2` |  |  |  |
| 45 | `ID.IAB.RESERVED.1` | `IdAccountBalances_Reserved1` |  |  |  |
