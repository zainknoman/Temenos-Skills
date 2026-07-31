# QI.PORTFOLIO.RATE — Table Schema

> Source: `INSERTS/I_F.QI.PORTFOLIO.RATE` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.QPR.INCOME.CODE` | `QiPortfolioRate_IncomeCode` |  |  |  |
| 2 | `SC.QPR.TAX.KEY` | `QiPortfolioRate_TaxKey` |  |  |  |
| 3 | `SC.QPR.MULT.RESERVED.04` | `QiPortfolioRate_MultReserved04` |  |  |  |
| 4 | `SC.QPR.MULT.RESERVED.03` | `QiPortfolioRate_MultReserved03` |  |  |  |
| 5 | `SC.QPR.MULT.RESERVED.02` | `QiPortfolioRate_MultReserved02` |  |  |  |
| 6 | `SC.QPR.MULT.RESERVED.01` | `QiPortfolioRate_MultReserved01` |  |  |  |
| 7 | `SC.QPR.RESERVED.06` | `QiPortfolioRate_Reserved06` | TField |  |  |
| 8 | `SC.QPR.RESERVED.05` | `QiPortfolioRate_Reserved05` | TField |  |  |
| 9 | `SC.QPR.RESERVED.04` | `QiPortfolioRate_Reserved04` | TField |  |  |
| 10 | `SC.QPR.RESERVED.03` | `QiPortfolioRate_Reserved03` | TField |  |  |
| 11 | `SC.QPR.RESERVED.02` | `QiPortfolioRate_Reserved02` | TField |  |  |
| 12 | `SC.QPR.RESERVED.01` | `QiPortfolioRate_Reserved01` | TField |  |  |
| 13 | `SC.QPR.LOCAL.REF` | `QiPortfolioRate_LocalRef` |  |  |  |
| 14 | `SC.QPR.OVERRIDE` | `QiPortfolioRate_Override` |  |  |  |
| 15 | `SC.QPR.RECORD.STATUS` | `QiPortfolioRate_RecordStatus` | String |  |  |
| 16 | `SC.QPR.CURR.NO` | `QiPortfolioRate_CurrNo` | String |  |  |
| 17 | `SC.QPR.INPUTTER` | `QiPortfolioRate_Inputter` |  |  |  |
| 18 | `SC.QPR.DATE.TIME` | `QiPortfolioRate_DateTime` |  |  |  |
| 19 | `SC.QPR.AUTHORISER` | `QiPortfolioRate_Authoriser` | String |  |  |
| 20 | `SC.QPR.CO.CODE` | `QiPortfolioRate_CoCode` | String |  |  |
| 21 | `SC.QPR.DEPT.CODE` | `QiPortfolioRate_DeptCode` | String |  |  |
| 22 | `SC.QPR.AUDITOR.CODE` | `QiPortfolioRate_AuditorCode` | String |  |  |
| 23 | `SC.QPR.AUDIT.DATE.TIME` | `QiPortfolioRate_AuditDateTime` | String |  |  |
