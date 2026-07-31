# ID.PROFIT.PL.DETAIL — Table Schema

> Source: `INSERTS/I_F.ID.PROFIT.PL.DETAIL` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPW.PL.CATEGORY` | `IdProfitPlDetail_PlCategory` |  |  |  |
| 2 | `ID.IPW.OUR.REFERENCE` | `IdProfitPlDetail_OurReference` |  |  |  |
| 3 | `ID.IPW.AMOUNT.LCY` | `IdProfitPlDetail_AmountLcy` |  |  |  |
| 4 | `ID.IPW.CURRENCY` | `IdProfitPlDetail_Currency` |  |  |  |
| 5 | `ID.IPW.AMOUNT.FCY` | `IdProfitPlDetail_AmountFcy` |  |  |  |
| 6 | `ID.IPW.CONTRACT.TYPE` | `IdProfitPlDetail_ContractType` |  |  |  |
| 7 | `ID.IPW.PL.TOTAL` | `IdProfitPlDetail_PlTotal` |  |  |  |
| 8 | `ID.IPW.CALC.PERC` | `IdProfitPlDetail_CalcPerc` |  |  |  |
| 9 | `ID.IPW.CALC.AMT.LCY` | `IdProfitPlDetail_CalcAmtLcy` |  |  |  |
| 10 | `ID.IPW.TOTAL.AMT` | `IdProfitPlDetail_TotalAmt` | TField |  |  |
| 11 | `ID.IPW.PROFIT.EXPENSE` | `IdProfitPlDetail_ProfitExpense` | TField |  |  |
| 12 | `ID.IPW.RESERVED.3` | `IdProfitPlDetail_Reserved3` | TField |  |  |
| 13 | `ID.IPW.RESERVED.2` | `IdProfitPlDetail_Reserved2` | TField |  |  |
| 14 | `ID.IPW.RESERVED.1` | `IdProfitPlDetail_Reserved1` | TField |  |  |
