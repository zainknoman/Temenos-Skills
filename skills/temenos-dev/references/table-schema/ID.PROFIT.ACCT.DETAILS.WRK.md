# ID.PROFIT.ACCT.DETAILS.WRK — Table Schema

> Source: `INSERTS/I_F.ID.PROFIT.ACCT.DETAILS.WRK` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IAW.OUR.REFERENCE` | `IdProfitAcctDetailsWrk_OurReference` |  |  |  |
| 2 | `ID.IAW.ORIG.AMT` | `IdProfitAcctDetailsWrk_OrigAmt` |  |  |  |
| 3 | `ID.IAW.CALC.PERC` | `IdProfitAcctDetailsWrk_CalcPerc` |  |  |  |
| 4 | `ID.IAW.CALC.AMT.LCY` | `IdProfitAcctDetailsWrk_CalcAmtLcy` |  |  |  |
| 5 | `ID.IAW.CURRENCY` | `IdProfitAcctDetailsWrk_Currency` |  |  |  |
| 6 | `ID.IAW.CALC.AMT.FCY` | `IdProfitAcctDetailsWrk_CalcAmtFcy` |  |  |  |
| 7 | `ID.IAW.TOTAL.AMT` | `IdProfitAcctDetailsWrk_TotalAmt` | TField |  | The total amount to be used for calculation with the internal accounting entries details. |
| 8 | `ID.IAW.PROFIT.EXPENSE` | `IdProfitAcctDetailsWrk_ProfitExpense` | TField |  | The type of the PL entries that are captured must be profit or expense. Validation Rules: 1. Allowed Values are Profit or Expense. |
| 9 | `ID.IAW.RESERVED.5` | `IdProfitAcctDetailsWrk_Reserved5` | TField |  |  |
| 10 | `ID.IAW.RESERVED.4` | `IdProfitAcctDetailsWrk_Reserved4` | TField |  |  |
| 11 | `ID.IAW.RESERVED.3` | `IdProfitAcctDetailsWrk_Reserved3` | TField |  |  |
| 12 | `ID.IAW.RESERVED.2` | `IdProfitAcctDetailsWrk_Reserved2` | TField |  |  |
| 13 | `ID.IAW.RESERVED.1` | `IdProfitAcctDetailsWrk_Reserved1` | TField |  |  |
