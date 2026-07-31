# CAMB.ARR.LOC.BALANCES.HIST — Table Schema

> Source: `INSERTS/I_F.CAMB.ARR.LOC.BALANCES.HIST` in `CALOCR_LineOfCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LOCH.NXT.PYMT.DUE.DATE` | `CambArrLocBalancesHist_NxtPymtDueDate` |  |  |  |
| 2 | `LOCH.MIN.PYMT.AMOUNT` | `CambArrLocBalancesHist_MinPymtAmount` |  |  |  |
| 3 | `LOCH.PAST.DUE.DATE` | `CambArrLocBalancesHist_PastDueDate` |  |  |  |
| 4 | `LOCH.PAST.DUE.BALANCE` | `CambArrLocBalancesHist_PastDueBalance` |  |  |  |
| 5 | `LOCH.TOTAL.DUE` | `CambArrLocBalancesHist_TotalDue` |  |  |  |
| 6 | `LOCH.REQ.FOR.CLOSURE` | `CambArrLocBalancesHist_ReqForClosure` |  |  |  |
| 7 | `LOCH.CLOSURE.DATE` | `CambArrLocBalancesHist_ClosureDate` |  |  |  |
| 8 | `LOCH.LAST.ACTIVITY` | `CambArrLocBalancesHist_LastActivity` |  |  |  |
| 9 | `LOCH.LAST.PAY.DATE` | `CambArrLocBalancesHist_LastPayDate` |  |  |  |
| 10 | `LOCH.ACTUAL.MIN.PYMT.AMT` | `CambArrLocBalancesHist_ActualMinPymtAmt` |  |  |  |
| 11 | `LOCH.CO.CODE` | `CambArrLocBalancesHist_CoCode` |  |  |  |
| 12 | `LOCH.RESERVED.5` | `CambArrLocBalancesHist_Reserved5` |  |  |  |
| 13 | `LOCH.RESERVED.6` | `CambArrLocBalancesHist_Reserved6` |  |  |  |
| 14 | `LOCH.RESERVED.7` | `CambArrLocBalancesHist_Reserved7` |  |  |  |
| 15 | `LOCH.RESERVED.8` | `CambArrLocBalancesHist_Reserved8` |  |  |  |
| 16 | `LOCH.RESERVED.9` | `CambArrLocBalancesHist_Reserved9` |  |  |  |
| 17 | `LOCH.RESERVED.10` | `CambArrLocBalancesHist_Reserved10` |  |  |  |
| 18 | `LOCH.RESERVED.11` | `CambArrLocBalancesHist_Reserved11` |  |  |  |
| 19 | `LOCH.RESERVED.12` | `CambArrLocBalancesHist_Reserved12` |  |  |  |
| 20 | `LOCH.RESERVED.13` | `CambArrLocBalancesHist_Reserved13` |  |  |  |
| 21 | `LOCH.RESERVED.14` | `CambArrLocBalancesHist_Reserved14` |  |  |  |
