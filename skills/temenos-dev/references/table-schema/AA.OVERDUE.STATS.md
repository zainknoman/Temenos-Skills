# AA.OVERDUE.STATS — Table Schema

> Source: `INSERTS/I_F.AA.OVERDUE.STATS` in `AA_Overdue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.OD.ST.OD.STATUS` | `AaOverdueStats_OdStatus` |  |  |  |
| 2 | `AA.OD.ST.RESERVED.5` | `AaOverdueStats_Reserved5` |  |  |  |
| 3 | `AA.OD.ST.START.DATE` | `AaOverdueStats_StartDate` |  |  |  |
| 4 | `AA.OD.ST.END.DATE` | `AaOverdueStats_EndDate` |  |  |  |
| 5 | `AA.OD.ST.RESERVED.4` | `AaOverdueStats_Reserved4` |  |  |  |
| 6 | `AA.OD.ST.PRD.AVG.AMT` | `AaOverdueStats_PrdAvgAmt` |  |  |  |
| 7 | `AA.OD.ST.MVMT.DATE` | `AaOverdueStats_MvmtDate` |  |  |  |
| 8 | `AA.OD.ST.MVMT.CREDIT` | `AaOverdueStats_MvmtCredit` |  |  |  |
| 9 | `AA.OD.ST.RESERVED.3` | `AaOverdueStats_Reserved3` |  |  |  |
| 10 | `AA.OD.ST.MVMT.DEBIT` | `AaOverdueStats_MvmtDebit` |  |  |  |
| 11 | `AA.OD.ST.STATUS.COUNT` | `AaOverdueStats_StatusCount` |  |  |  |
| 12 | `AA.OD.ST.TOT.DAYS` | `AaOverdueStats_TotDays` |  |  |  |
| 13 | `AA.OD.ST.RESERVED.2` | `AaOverdueStats_Reserved2` |  |  |  |
| 14 | `AA.OD.ST.RESERVED.1` | `AaOverdueStats_Reserved1` |  |  |  |
| 15 | `AA.OD.ST.AVG.AMT` | `AaOverdueStats_AvgAmt` |  |  |  |
