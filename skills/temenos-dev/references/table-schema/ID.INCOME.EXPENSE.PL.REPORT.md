# ID.INCOME.EXPENSE.PL.REPORT — Table Schema

> Source: `INSERTS/I_F.ID.INCOME.EXPENSE.PL.REPORT` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.INR.INCOME.LOCAL.PATH` | `IdIncomeExpensePlReport_IncomeLocalPath` | TField |  |  |
| 2 | `ID.INR.EXPENSE.LOCAL.PATH` | `IdIncomeExpensePlReport_ExpenseLocalPath` | TField |  |  |
| 3 | `ID.INR.LOCAL.REF` | `IdIncomeExpensePlReport_LocalRef` |  |  |  |
| 4 | `ID.INR.OVERRIDE` | `IdIncomeExpensePlReport_Override` |  |  |  |
| 5 | `ID.INR.RECORD.STATUS` | `IdIncomeExpensePlReport_RecordStatus` | String |  |  |
| 6 | `ID.INR.CURR.NO` | `IdIncomeExpensePlReport_CurrNo` | String |  |  |
| 7 | `ID.INR.INPUTTER` | `IdIncomeExpensePlReport_Inputter` |  |  |  |
| 8 | `ID.INR.DATE.TIME` | `IdIncomeExpensePlReport_DateTime` |  |  |  |
| 9 | `ID.INR.AUTHORISER` | `IdIncomeExpensePlReport_Authoriser` | String |  |  |
| 10 | `ID.INR.CO.CODE` | `IdIncomeExpensePlReport_CoCode` | String |  |  |
| 11 | `ID.INR.DEPT.CODE` | `IdIncomeExpensePlReport_DeptCode` | String |  |  |
| 12 | `ID.INR.AUDITOR.CODE` | `IdIncomeExpensePlReport_AuditorCode` | String |  |  |
| 13 | `ID.INR.AUDIT.DATE.TIME` | `IdIncomeExpensePlReport_AuditDateTime` | String |  |  |
