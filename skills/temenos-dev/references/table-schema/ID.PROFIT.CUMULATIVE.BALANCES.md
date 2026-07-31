# ID.PROFIT.CUMULATIVE.BALANCES — Table Schema

> Source: `INSERTS/I_F.ID.PROFIT.CUMULATIVE.BALANCES` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.PCB.PDS.ACTION.REF` | `IdProfitCumulativeBalances_PdsActionRef` |  |  |  |
| 2 | `ID.PCB.START.DATE` | `IdProfitCumulativeBalances_StartDate` |  |  |  |
| 3 | `ID.PCB.END.DATE` | `IdProfitCumulativeBalances_EndDate` |  |  |  |
| 4 | `ID.PCB.PROFIT.RATE` | `IdProfitCumulativeBalances_ProfitRate` |  |  |  |
| 5 | `ID.PCB.PROFIT.AMOUNT` | `IdProfitCumulativeBalances_ProfitAmount` |  |  |  |
| 6 | `ID.PCB.TOTAL.PDS.PROFIT` | `IdProfitCumulativeBalances_TotalPdsProfit` | TField |  | This field will hold the value of accumulated profit amount, considering all the distributions related to the arrangem. Validation Rules: 1. Must be a valid Amount type field. |
| 7 | `ID.PCB.RESERVED.5` | `IdProfitCumulativeBalances_Reserved5` | TField |  |  |
| 8 | `ID.PCB.RESERVED.4` | `IdProfitCumulativeBalances_Reserved4` | TField |  |  |
| 9 | `ID.PCB.RESERVED.3` | `IdProfitCumulativeBalances_Reserved3` | TField |  |  |
| 10 | `ID.PCB.RESERVED.2` | `IdProfitCumulativeBalances_Reserved2` | TField |  |  |
| 11 | `ID.PCB.RESERVED.1` | `IdProfitCumulativeBalances_Reserved1` | TField |  |  |
