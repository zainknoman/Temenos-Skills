# DX.PORTFOLIO.MARGIN — Table Schema

> Source: `INSERTS/I_F.DX.PORTFOLIO.MARGIN` in `DX_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.PMR.REFERENCE.CCY` | `DxPortfolioMargin_ReferenceCcy` | TField |  | Holds the reference currency of the portfolio |
| 2 | `DX.PMR.NETTING.FMT` | `DxPortfolioMargin_NettingFmt` |  |  |  |
| 3 | `DX.PMR.CALL` | `DxPortfolioMargin_Call` |  |  |  |
| 4 | `DX.PMR.PUT` | `DxPortfolioMargin_Put` |  |  |  |
| 5 | `DX.PMR.EXPOSURE` | `DxPortfolioMargin_Exposure` |  |  |  |
| 6 | `DX.PMR.EXP.REFERENCE` | `DxPortfolioMargin_ExpReference` |  |  |  |
| 7 | `DX.PMR.CALL.TRANSACTION` | `DxPortfolioMargin_CallTransaction` |  |  |  |
| 8 | `DX.PMR.PUT.TRANSACTION` | `DxPortfolioMargin_PutTransaction` |  |  |  |
| 9 | `DX.PMR.FIRST.MATURITY` | `DxPortfolioMargin_FirstMaturity` |  |  |  |
| 10 | `DX.PMR.RESERVED.8` | `DxPortfolioMargin_Reserved8` |  |  |  |
| 11 | `DX.PMR.RESERVED.7` | `DxPortfolioMargin_Reserved7` |  |  |  |
| 12 | `DX.PMR.RESERVED.6` | `DxPortfolioMargin_Reserved6` |  |  |  |
| 13 | `DX.PMR.TOTAL.EXPOSURE` | `DxPortfolioMargin_TotalExposure` | TField |  | Sum of EXP.REFERENCE is updated. |
| 14 | `DX.PMR.RESERVED.9` | `DxPortfolioMargin_Reserved9` | TField |  |  |
| 15 | `DX.PMR.RESERVED.5` | `DxPortfolioMargin_Reserved5` | TField |  |  |
| 16 | `DX.PMR.RESERVED.4` | `DxPortfolioMargin_Reserved4` | TField |  |  |
| 17 | `DX.PMR.RESERVED.3` | `DxPortfolioMargin_Reserved3` | TField |  |  |
| 18 | `DX.PMR.RESERVED.2` | `DxPortfolioMargin_Reserved2` | TField |  |  |
| 19 | `DX.PMR.RESERVED.1` | `DxPortfolioMargin_Reserved1` | TField |  |  |
