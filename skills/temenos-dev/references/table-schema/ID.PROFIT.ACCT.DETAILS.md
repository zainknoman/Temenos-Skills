# ID.PROFIT.ACCT.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.PROFIT.ACCT.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IAA.OUR.REFERENCE` | `IdProfitAcctDetails_OurReference` |  |  |  |
| 2 | `ID.IAA.ORIG.AMT` | `IdProfitAcctDetails_OrigAmt` |  |  |  |
| 3 | `ID.IAA.CALC.PERC` | `IdProfitAcctDetails_CalcPerc` |  |  |  |
| 4 | `ID.IAA.CALC.AMT.LCY` | `IdProfitAcctDetails_CalcAmtLcy` |  |  |  |
| 5 | `ID.IAA.CURRENCY` | `IdProfitAcctDetails_Currency` |  |  |  |
| 6 | `ID.IAA.CALC.AMT.FCY` | `IdProfitAcctDetails_CalcAmtFcy` |  |  |  |
| 7 | `ID.IAA.TOTAL.AMT` | `IdProfitAcctDetails_TotalAmt` | TField |  | The total amount to be used for calculation with the internal accounting entries details. |
| 8 | `ID.IAA.PROFIT.EXPENSE` | `IdProfitAcctDetails_ProfitExpense` | TField |  | The type of the PL entries that are captured must be profit or expense. Validation Rules: 1. Allowed Values are Profit or Expense. |
| 9 | `ID.IAA.RESERVED.5` | `IdProfitAcctDetails_Reserved5` | TField |  |  |
| 10 | `ID.IAA.RESERVED.4` | `IdProfitAcctDetails_Reserved4` | TField |  |  |
| 11 | `ID.IAA.RESERVED.3` | `IdProfitAcctDetails_Reserved3` | TField |  |  |
| 12 | `ID.IAA.RESERVED.2` | `IdProfitAcctDetails_Reserved2` | TField |  |  |
| 13 | `ID.IAA.RESERVED.1` | `IdProfitAcctDetails_Reserved1` | TField |  |  |
