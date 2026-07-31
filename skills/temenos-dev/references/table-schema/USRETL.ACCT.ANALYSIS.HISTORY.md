# USRETL.ACCT.ANALYSIS.HISTORY — Table Schema

> Source: `INSERTS/I_F.USRETL.ACCT.ANALYSIS.HISTORY` in `USRETL_AccountAnalysis.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCT.ANA.ANALYSIS.DATE` | `UsretlAcctAnalysisHistory_AnalysisDate` |  |  |  |
| 2 | `ACCT.ANA.AVG.LEDGER` | `UsretlAcctAnalysisHistory_AvgLedger` |  |  |  |
| 3 | `ACCT.ANA.AVG.COLLECTED` | `UsretlAcctAnalysisHistory_AvgCollected` |  |  |  |
| 4 | `ACCT.ANA.RES.REQUIREMENT` | `UsretlAcctAnalysisHistory_ResRequirement` |  |  |  |
| 5 | `ACCT.ANA.CR.RATE` | `UsretlAcctAnalysisHistory_CrRate` |  |  |  |
| 6 | `ACCT.ANA.EARNINGS.ALLOWANCE` | `UsretlAcctAnalysisHistory_EarningsAllowance` |  |  |  |
| 7 | `ACCT.ANA.SERVICE.CHARGE` | `UsretlAcctAnalysisHistory_ServiceCharge` |  |  |  |
| 8 | `ACCT.ANA.NET.CHARGE` | `UsretlAcctAnalysisHistory_NetCharge` |  |  |  |
| 9 | `ACCT.ANA.AGGR.COLLECTED` | `UsretlAcctAnalysisHistory_AggrCollected` |  |  |  |
| 10 | `ACCT.ANA.AGGR.LEDGER` | `UsretlAcctAnalysisHistory_AggrLedger` |  |  |  |
| 11 | `ACCT.ANA.AGGR.FLOAT` | `UsretlAcctAnalysisHistory_AggrFloat` |  |  |  |
| 12 | `ACCT.ANA.RESERVED.20` | `UsretlAcctAnalysisHistory_Reserved20` |  |  |  |
| 13 | `ACCT.ANA.RESERVED.19` | `UsretlAcctAnalysisHistory_Reserved19` |  |  |  |
| 14 | `ACCT.ANA.RESERVED.18` | `UsretlAcctAnalysisHistory_Reserved18` |  |  |  |
| 15 | `ACCT.ANA.RESERVED.17` | `UsretlAcctAnalysisHistory_Reserved17` |  |  |  |
| 16 | `ACCT.ANA.RESERVED.16` | `UsretlAcctAnalysisHistory_Reserved16` |  |  |  |
| 17 | `ACCT.ANA.RESERVED.15` | `UsretlAcctAnalysisHistory_Reserved15` |  |  |  |
| 18 | `ACCT.ANA.RESERVED.14` | `UsretlAcctAnalysisHistory_Reserved14` |  |  |  |
| 19 | `ACCT.ANA.RESERVED.13` | `UsretlAcctAnalysisHistory_Reserved13` |  |  |  |
| 20 | `ACCT.ANA.RESERVED.12` | `UsretlAcctAnalysisHistory_Reserved12` |  |  |  |
| 21 | `ACCT.ANA.RESERVED.11` | `UsretlAcctAnalysisHistory_Reserved11` |  |  |  |
| 22 | `ACCT.ANA.START.DATE` | `UsretlAcctAnalysisHistory_StartDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 23 | `ACCT.ANA.MONTH.TO.DATE.COLL` | `UsretlAcctAnalysisHistory_MonthToDateColl` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 24 | `ACCT.ANA.MONTH.TO.DATE.LEDGER` | `UsretlAcctAnalysisHistory_MonthToDateLedger` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 25 | `ACCT.ANA.MONTH.TO.DATE.FLOAT` | `UsretlAcctAnalysisHistory_MonthToDateFloat` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 26 | `ACCT.ANA.QUART.TO.DATE.COLL` | `UsretlAcctAnalysisHistory_QuartToDateColl` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 27 | `ACCT.ANA.QUART.TO.DATE.LEDGER` | `UsretlAcctAnalysisHistory_QuartToDateLedger` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 28 | `ACCT.ANA.QUART.TO.DATE.FLOAT` | `UsretlAcctAnalysisHistory_QuartToDateFloat` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 29 | `ACCT.ANA.YEAR.TO.DATE.COLL` | `UsretlAcctAnalysisHistory_YearToDateColl` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 30 | `ACCT.ANA.YEAR.TO.DATE.LEDGER` | `UsretlAcctAnalysisHistory_YearToDateLedger` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 31 | `ACCT.ANA.YEAR.TO.DATE.FLOAT` | `UsretlAcctAnalysisHistory_YearToDateFloat` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 32 | `ACCT.ANA.RESERVED.10` | `UsretlAcctAnalysisHistory_Reserved10` | TField |  |  |
| 33 | `ACCT.ANA.RESERVED.9` | `UsretlAcctAnalysisHistory_Reserved9` | TField |  |  |
| 34 | `ACCT.ANA.RESERVED.8` | `UsretlAcctAnalysisHistory_Reserved8` | TField |  |  |
| 35 | `ACCT.ANA.RESERVED.7` | `UsretlAcctAnalysisHistory_Reserved7` | TField |  |  |
| 36 | `ACCT.ANA.RESERVED.6` | `UsretlAcctAnalysisHistory_Reserved6` | TField |  |  |
| 37 | `ACCT.ANA.RESERVED.5` | `UsretlAcctAnalysisHistory_Reserved5` | TField |  |  |
| 38 | `ACCT.ANA.RESERVED.4` | `UsretlAcctAnalysisHistory_Reserved4` | TField |  |  |
| 39 | `ACCT.ANA.RESERVED.3` | `UsretlAcctAnalysisHistory_Reserved3` | TField |  |  |
| 40 | `ACCT.ANA.RESERVED.2` | `UsretlAcctAnalysisHistory_Reserved2` | TField |  |  |
| 41 | `ACCT.ANA.RESERVED.1` | `UsretlAcctAnalysisHistory_Reserved1` | TField |  |  |
