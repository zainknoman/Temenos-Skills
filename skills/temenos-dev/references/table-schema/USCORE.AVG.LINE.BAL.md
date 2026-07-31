# USCORE.AVG.LINE.BAL — Table Schema

> Source: `INSERTS/I_F.USCORE.AVG.LINE.BAL` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.AVG.MTD.BAL` | `UscoreAvgLineBal_MtdBal` | TField |  | This field denotes the summation of closing balance of month to date for a particular line will and this will be restored to Zero every month. |
| 2 | `USCORE.AVG.QTD.BAL` | `UscoreAvgLineBal_QtdBal` | TField |  | This field denotes the summation of closing balance of Quarter to date for a particular line and this will be restored to Zero every quater |
| 3 | `USCORE.AVG.YTD.BAL` | `UscoreAvgLineBal_YtdBal` | TField |  | This field denotes the summation of closing balance of year to date for the particular line and this will be restored to Zero every Year. |
| 4 | `USCORE.AVG.ROLLING.AVG.BAL` | `UscoreAvgLineBal_RollingAvgBal` | TField |  | As per the rolling period defined in the RLGAAP.PARAMETER, the rolling average balance for the GL line will be updated here. |
| 5 | `USCORE.AVG.MONTH01` | `UscoreAvgLineBal_Month01` | TField |  |  |
| 6 | `USCORE.AVG.MONTH02` | `UscoreAvgLineBal_Month02` | TField |  |  |
| 7 | `USCORE.AVG.MONTH03` | `UscoreAvgLineBal_Month03` | TField |  |  |
| 8 | `USCORE.AVG.MONTH04` | `UscoreAvgLineBal_Month04` | TField |  |  |
| 9 | `USCORE.AVG.MONTH05` | `UscoreAvgLineBal_Month05` | TField |  |  |
| 10 | `USCORE.AVG.MONTH06` | `UscoreAvgLineBal_Month06` | TField |  |  |
| 11 | `USCORE.AVG.MONTH07` | `UscoreAvgLineBal_Month07` | TField |  |  |
| 12 | `USCORE.AVG.MONTH08` | `UscoreAvgLineBal_Month08` | TField |  |  |
| 13 | `USCORE.AVG.MONTH09` | `UscoreAvgLineBal_Month09` | TField |  |  |
| 14 | `USCORE.AVG.MONTH10` | `UscoreAvgLineBal_Month10` | TField |  |  |
| 15 | `USCORE.AVG.MONTH11` | `UscoreAvgLineBal_Month11` | TField |  |  |
| 16 | `USCORE.AVG.MONTH12` | `UscoreAvgLineBal_Month12` | TField |  |  |
| 17 | `USCORE.AVG.QUARTER01` | `UscoreAvgLineBal_Quarter01` | TField |  |  |
| 18 | `USCORE.AVG.QUARTER02` | `UscoreAvgLineBal_Quarter02` | TField |  |  |
| 19 | `USCORE.AVG.QUARTER03` | `UscoreAvgLineBal_Quarter03` | TField |  |  |
| 20 | `USCORE.AVG.QUARTER04` | `UscoreAvgLineBal_Quarter04` | TField |  |  |
| 21 | `USCORE.AVG.YTD.AVG.BAL` | `UscoreAvgLineBal_YtdAvgBal` | TField |  | The yearly average balance will be stored for present year. |
| 22 | `USCORE.AVG.BAL.MONTH01` | `UscoreAvgLineBal_BalMonth01` | TField |  |  |
| 23 | `USCORE.AVG.BAL.MONTH02` | `UscoreAvgLineBal_BalMonth02` | TField |  |  |
| 24 | `USCORE.AVG.BAL.MONTH03` | `UscoreAvgLineBal_BalMonth03` | TField |  |  |
| 25 | `USCORE.AVG.BAL.MONTH04` | `UscoreAvgLineBal_BalMonth04` | TField |  |  |
| 26 | `USCORE.AVG.BAL.MONTH05` | `UscoreAvgLineBal_BalMonth05` | TField |  |  |
| 27 | `USCORE.AVG.BAL.MONTH06` | `UscoreAvgLineBal_BalMonth06` | TField |  |  |
| 28 | `USCORE.AVG.BAL.MONTH07` | `UscoreAvgLineBal_BalMonth07` | TField |  |  |
| 29 | `USCORE.AVG.BAL.MONTH08` | `UscoreAvgLineBal_BalMonth08` | TField |  |  |
| 30 | `USCORE.AVG.BAL.MONTH09` | `UscoreAvgLineBal_BalMonth09` | TField |  |  |
| 31 | `USCORE.AVG.BAL.MONTH10` | `UscoreAvgLineBal_BalMonth10` | TField |  |  |
| 32 | `USCORE.AVG.BAL.MONTH11` | `UscoreAvgLineBal_BalMonth11` | TField |  |  |
| 33 | `USCORE.AVG.BAL.MONTH12` | `UscoreAvgLineBal_BalMonth12` | TField |  |  |
| 34 | `USCORE.AVG.RESERVED.10` | `UscoreAvgLineBal_Reserved10` | TField |  |  |
| 35 | `USCORE.AVG.RESERVED.9` | `UscoreAvgLineBal_Reserved9` | TField |  |  |
| 36 | `USCORE.AVG.RESERVED.8` | `UscoreAvgLineBal_Reserved8` | TField |  |  |
| 37 | `USCORE.AVG.RESERVED.7` | `UscoreAvgLineBal_Reserved7` | TField |  |  |
| 38 | `USCORE.AVG.RESERVED.6` | `UscoreAvgLineBal_Reserved6` | TField |  |  |
| 39 | `USCORE.AVG.RESERVED.5` | `UscoreAvgLineBal_Reserved5` | TField |  |  |
| 40 | `USCORE.AVG.RESERVED.4` | `UscoreAvgLineBal_Reserved4` | TField |  |  |
| 41 | `USCORE.AVG.RESERVED.3` | `UscoreAvgLineBal_Reserved3` | TField |  |  |
| 42 | `USCORE.AVG.RESERVED.2` | `UscoreAvgLineBal_Reserved2` | TField |  |  |
| 43 | `USCORE.AVG.RESERVED.1` | `UscoreAvgLineBal_Reserved1` | TField |  |  |
