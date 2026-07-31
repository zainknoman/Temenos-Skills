# ESLEND.BDE.RATES — Table Schema

> Source: `INSERTS/I_F.ESLEND.BDE.RATES` in `ESLEND_MortgageAct.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESLEND.MONTH` | `EslendBdeRates_Month` |  |  |  |
| 2 | `ESLEND.RATE.TERM` | `EslendBdeRates_RateTerm` |  |  |  |
| 3 | `ESLEND.CENTRAL.BANK.RATE` | `EslendBdeRates_CentralBankRate` |  |  |  |
| 4 | `ESLEND.IND.AVERAGE.RATE` | `EslendBdeRates_IndAverageRate` |  |  |  |
| 5 | `ESLEND.INT.RATE.SWAP.TERM` | `EslendBdeRates_IntRateSwapTerm` |  |  |  |
| 6 | `ESLEND.MONTH.TERM` | `EslendBdeRates_MonthTerm` |  |  |  |
| 7 | `ESLEND.DEFAULT.TERM` | `EslendBdeRates_DefaultTerm` | TField |  | Holds the defaulted term e.g 1Y |
| 8 | `ESLEND.RESERVED.4` | `EslendBdeRates_Reserved4` | TField |  |  |
| 9 | `ESLEND.RESERVED.5` | `EslendBdeRates_Reserved5` | TField |  |  |
| 10 | `ESLEND.RESERVED.6` | `EslendBdeRates_Reserved6` | TField |  |  |
| 11 | `ESLEND.RESERVED.7` | `EslendBdeRates_Reserved7` | TField |  |  |
| 12 | `ESLEND.RESERVED.8` | `EslendBdeRates_Reserved8` | TField |  |  |
| 13 | `ESLEND.RESERVED.9` | `EslendBdeRates_Reserved9` | TField |  |  |
| 14 | `ESLEND.RESERVED.10` | `EslendBdeRates_Reserved10` | TField |  |  |
| 15 | `ESLEND.RESERVED.11` | `EslendBdeRates_Reserved11` | TField |  |  |
| 16 | `ESLEND.LOCAL.REF` | `EslendBdeRates_LocalRef` |  |  |  |
| 17 | `ESLEND.OVERRIDE` | `EslendBdeRates_Override` |  |  |  |
| 18 | `ESLEND.RECORD.STATUS` | `EslendBdeRates_RecordStatus` | String |  |  |
| 19 | `ESLEND.CURR.NO` | `EslendBdeRates_CurrNo` | String |  |  |
| 20 | `ESLEND.INPUTTER` | `EslendBdeRates_Inputter` |  |  |  |
| 21 | `ESLEND.DATE.TIME` | `EslendBdeRates_DateTime` |  |  |  |
| 22 | `ESLEND.AUTHORISER` | `EslendBdeRates_Authoriser` | String |  |  |
| 23 | `ESLEND.CO.CODE` | `EslendBdeRates_CoCode` | String |  |  |
| 24 | `ESLEND.DEPT.CODE` | `EslendBdeRates_DeptCode` | String |  |  |
| 25 | `ESLEND.AUDITOR.CODE` | `EslendBdeRates_AuditorCode` | String |  |  |
| 26 | `ESLEND.AUDIT.DATE.TIME` | `EslendBdeRates_AuditDateTime` | String |  |  |
