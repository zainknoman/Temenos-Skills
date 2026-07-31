# ID.PROFIT.PL.DETAILS.WRK — Table Schema

> Source: `INSERTS/I_F.ID.PROFIT.PL.DETAILS.WRK` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPE.PL.CATEGORY` | `IdProfitPlDetailsWrk_PlCategory` |  |  |  |
| 2 | `ID.IPE.OUR.REFERENCE` | `IdProfitPlDetailsWrk_OurReference` |  |  |  |
| 3 | `ID.IPE.AMOUNT.LCY` | `IdProfitPlDetailsWrk_AmountLcy` |  |  |  |
| 4 | `ID.IPE.CURRENCY` | `IdProfitPlDetailsWrk_Currency` |  |  |  |
| 5 | `ID.IPE.AMOUNT.FCY` | `IdProfitPlDetailsWrk_AmountFcy` |  |  |  |
| 6 | `ID.IPE.CONTRACT.TYPE` | `IdProfitPlDetailsWrk_ContractType` |  |  |  |
| 7 | `ID.IPE.PL.TOTAL` | `IdProfitPlDetailsWrk_PlTotal` |  |  |  |
| 8 | `ID.IPE.CALC.PERC` | `IdProfitPlDetailsWrk_CalcPerc` |  |  |  |
| 9 | `ID.IPE.CALC.AMT.LCY` | `IdProfitPlDetailsWrk_CalcAmtLcy` |  |  |  |
| 10 | `ID.IPE.TOTAL.AMT` | `IdProfitPlDetailsWrk_TotalAmt` | TField |  | The total amount to be used for calculation with the PL entries details. |
| 11 | `ID.IPE.PROFIT.EXPENSE` | `IdProfitPlDetailsWrk_ProfitExpense` | TField |  | The type of the PL entries that are captured must be profit or expense. Validation Rules: 1. Allowed Values are Profit or Expense. |
| 12 | `ID.IPE.RESERVED.3` | `IdProfitPlDetailsWrk_Reserved3` | TField |  |  |
| 13 | `ID.IPE.RESERVED.2` | `IdProfitPlDetailsWrk_Reserved2` | TField |  |  |
| 14 | `ID.IPE.RESERVED.1` | `IdProfitPlDetailsWrk_Reserved1` | TField |  |  |
