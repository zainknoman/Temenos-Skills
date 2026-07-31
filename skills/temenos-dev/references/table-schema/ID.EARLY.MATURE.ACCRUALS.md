# ID.EARLY.MATURE.ACCRUALS — Table Schema

> Source: `INSERTS/I_F.ID.EARLY.MATURE.ACCRUALS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.EMA.FROM.DATE` | `IdEarlyMatureAccruals_FromDate` |  |  |  |
| 2 | `ID.EMA.TO.DATE` | `IdEarlyMatureAccruals_ToDate` |  |  |  |
| 3 | `ID.EMA.DAYS` | `IdEarlyMatureAccruals_Days` |  |  |  |
| 4 | `ID.EMA.BALANCE` | `IdEarlyMatureAccruals_Balance` |  |  |  |
| 5 | `ID.EMA.BASIS` | `IdEarlyMatureAccruals_Basis` |  |  |  |
| 6 | `ID.EMA.OLD.RATE` | `IdEarlyMatureAccruals_OldRate` |  |  |  |
| 7 | `ID.EMA.OLD.ACCRUAL.AMT` | `IdEarlyMatureAccruals_OldAccrualAmt` |  |  |  |
| 8 | `ID.EMA.NEW.RATE` | `IdEarlyMatureAccruals_NewRate` |  |  |  |
| 9 | `ID.EMA.NEW.RATE.REF` | `IdEarlyMatureAccruals_NewRateRef` |  |  |  |
| 10 | `ID.EMA.NEW.ACCRUAL.AMT` | `IdEarlyMatureAccruals_NewAccrualAmt` |  |  |  |
| 11 | `ID.EMA.RESERVED.9` | `IdEarlyMatureAccruals_Reserved9` |  |  |  |
| 12 | `ID.EMA.RESERVED.8` | `IdEarlyMatureAccruals_Reserved8` |  |  |  |
| 13 | `ID.EMA.RECALC.FROM` | `IdEarlyMatureAccruals_RecalcFrom` | TField |  |  |
| 14 | `ID.EMA.RECALC.T0` | `IdEarlyMatureAccruals_RecalcT0` | TField |  |  |
| 15 | `ID.EMA.TOT.OLD.ACCRUAL.AMT` | `IdEarlyMatureAccruals_TotOldAccrualAmt` | TField |  |  |
| 16 | `ID.EMA.TOT.NEW.ACCRUAL.AMT` | `IdEarlyMatureAccruals_TotNewAccrualAmt` | TField |  |  |
| 17 | `ID.EMA.LAST.PERIOD.PFT.AMT` | `IdEarlyMatureAccruals_LastPeriodPftAmt` | TField |  |  |
| 18 | `ID.EMA.RECALC.PROFIT.ADJ.PCT` | `IdEarlyMatureAccruals_EmaRecalcProfitAdjPct` |  |  |  |
| 19 | `ID.EMA.RECALCULATED.PROFIT` | `IdEarlyMatureAccruals_EmaRecalcultedProfit` |  |  |  |
