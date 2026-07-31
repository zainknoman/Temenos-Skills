# LOAN.TRADE.BALANCES — Table Schema

> Source: `INSERTS/I_F.LOAN.TRADE.BALANCES` in `LNTRAD_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LN.TRAD.BAL.TRANSFER.PRICE` | `LoanTradeBalances_TransferPrice` | TField |  | Specifies the price applicable to the entire trade. The values can be entered from 0.01 to 999.99. For trade priced more than 100 is referred as Premium Trade and for a trade priced less than 100 is referred as discounted Trade. Note: For Transfer type trade, it is automatically defaulted to 100. It cannot take a value greater than or less than 100. |
| 2 | `LN.TRAD.BAL.TXN.DATE` | `LoanTradeBalances_TxnDate` |  |  |  |
| 3 | `LN.TRAD.BAL.LOAN.ACCOUNT` | `LoanTradeBalances_LoanAccount` |  |  |  |
| 4 | `LN.TRAD.BAL.SHARE.PERCENT` | `LoanTradeBalances_SharePercent` |  |  |  |
| 5 | `LN.TRAD.BAL.ACCOUNT.NAME` | `LoanTradeBalances_AccountName` |  |  |  |
| 6 | `LN.TRAD.BAL.LOAN.PRODUCT` | `LoanTradeBalances_LoanProduct` |  |  |  |
| 7 | `LN.TRAD.BAL.LOAN.CURRENCY` | `LoanTradeBalances_LoanCurrency` |  |  |  |
| 8 | `LN.TRAD.BAL.FX.RATE` | `LoanTradeBalances_FxRate` |  |  |  |
| 9 | `LN.TRAD.BAL.TOT.TRADE.AMT` | `LoanTradeBalances_TotTradeAmt` |  |  |  |
| 10 | `LN.TRAD.BAL.DRAWN` | `LoanTradeBalances_Drawn` |  |  |  |
| 11 | `LN.TRAD.BAL.UNDRAWN` | `LoanTradeBalances_Undrawn` |  |  |  |
| 12 | `LN.TRAD.BAL.PREM.DISC` | `LoanTradeBalances_PremDisc` |  |  |  |
| 13 | `LN.TRAD.BAL.NETBACK` | `LoanTradeBalances_Netback` |  |  |  |
| 14 | `LN.TRAD.BAL.BoCR` | `LoanTradeBalances_Bocr` |  |  |  |
| 15 | `LN.TRAD.BAL.SETTLEMENT.AMOUNT` | `LoanTradeBalances_SettlementAmount` |  |  |  |
