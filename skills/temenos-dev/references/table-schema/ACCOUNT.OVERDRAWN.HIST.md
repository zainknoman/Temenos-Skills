# ACCOUNT.OVERDRAWN.HIST — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.OVERDRAWN.HIST` in `AC_BalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.OD.HIST.LIMIT.NARRATIVE` | `AccountOverdrawnHist_LimitNarrative` |  |  |  |
| 2 | `AC.OD.HIST.ACCOUNT.OFFICER` | `AccountOverdrawnHist_AccountOfficer` |  |  |  |
| 3 | `AC.OD.HIST.CUSTOMER` | `AccountOverdrawnHist_Customer` |  |  |  |
| 4 | `AC.OD.HIST.CURRENCY` | `AccountOverdrawnHist_Currency` |  |  |  |
| 5 | `AC.OD.HIST.CLRD.BAL.LIMIT` | `AccountOverdrawnHist_ClrdBalLimit` |  |  |  |
| 6 | `AC.OD.HIST.ACT.BAL.TOT.OUT` | `AccountOverdrawnHist_ActBalTotOut` |  |  |  |
| 7 | `AC.OD.HIST.DATE.FIRST.OD` | `AccountOverdrawnHist_DateFirstOd` |  |  |  |
| 8 | `AC.OD.HIST.DATE.LAST.MOVE` | `AccountOverdrawnHist_DateLastMove` |  |  |  |
| 9 | `AC.OD.HIST.OD.EXCESS.NARR` | `AccountOverdrawnHist_OdExcessNarr` |  |  |  |
| 10 | `AC.OD.HIST.MOVED.NARR` | `AccountOverdrawnHist_MovedNarr` |  |  |  |
| 11 | `AC.OD.HIST.CURR.OD.STATUS` | `AccountOverdrawnHist_CurrOdStatus` | TField |  |  |
| 12 | `AC.OD.HIST.PREV.OD.STATUS` | `AccountOverdrawnHist_PrevOdStatus` |  |  |  |
| 13 | `AC.OD.HIST.STATUS.CHANGE.ON` | `AccountOverdrawnHist_StatusChangeOn` |  |  |  |
| 14 | `AC.OD.HIST.CURR.OD.START.DATE` | `AccountOverdrawnHist_CurrOdStartDate` | TField |  |  |
| 15 | `AC.OD.HIST.CURR.OD.DAYS` | `AccountOverdrawnHist_CurrOdDays` | TField |  |  |
| 16 | `AC.OD.HIST.OVERDRAWN.AMT` | `AccountOverdrawnHist_OverdrawnAmt` | TField |  |  |
| 17 | `AC.OD.HIST.THRESHOLD.AMT` | `AccountOverdrawnHist_ThresholdAmt` | TField |  |  |
| 18 | `AC.OD.HIST.OD.FEE.DATE` | `AccountOverdrawnHist_OdFeeDate` | TField |  |  |
| 19 | `AC.OD.HIST.RESERVED.05` | `AccountOverdrawnHist_Reserved05` | TField |  |  |
| 20 | `AC.OD.HIST.RESERVED.04` | `AccountOverdrawnHist_Reserved04` | TField |  |  |
| 21 | `AC.OD.HIST.RESERVED.03` | `AccountOverdrawnHist_Reserved03` | TField |  |  |
| 22 | `AC.OD.HIST.RESERVED.02` | `AccountOverdrawnHist_Reserved02` | TField |  |  |
| 23 | `AC.OD.HIST.RESERVED.01` | `AccountOverdrawnHist_Reserved01` | TField |  |  |
