# ACCT.OD.HIST — Table Schema

> Source: `INSERTS/I_F.ACCT.OD.HIST` in `AC_BalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCT.OD.HIST.YEAR` | `AcctOdHist_Year` |  |  |  |
| 2 | `ACCT.OD.HIST.NO.OD.PERIOD` | `AcctOdHist_NoOdPeriod` |  |  |  |
| 3 | `ACCT.OD.HIST.PERIOD.OD.DAYS` | `AcctOdHist_PeriodOdDays` |  |  |  |
| 4 | `ACCT.OD.HIST.OD.START.DATE` | `AcctOdHist_OdStartDate` |  |  |  |
| 5 | `ACCT.OD.HIST.OD.END.DATE` | `AcctOdHist_OdEndDate` |  |  |  |
| 6 | `ACCT.OD.HIST.OD.HIST.ID` | `AcctOdHist_OdHistId` |  |  |  |
| 7 | `ACCT.OD.HIST.TOTAL.OD.DAYS` | `AcctOdHist_TotalOdDays` |  |  |  |
| 8 | `ACCT.OD.HIST.RESERVED.05` | `AcctOdHist_Reserved05` | TField |  |  |
| 9 | `ACCT.OD.HIST.RESERVED.04` | `AcctOdHist_Reserved04` | TField |  |  |
| 10 | `ACCT.OD.HIST.RESERVED.03` | `AcctOdHist_Reserved03` | TField |  |  |
| 11 | `ACCT.OD.HIST.RESERVED.02` | `AcctOdHist_Reserved02` | TField |  |  |
| 12 | `ACCT.OD.HIST.RESERVED.01` | `AcctOdHist_Reserved01` | TField |  |  |
