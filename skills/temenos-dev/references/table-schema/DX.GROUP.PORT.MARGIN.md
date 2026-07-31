# DX.GROUP.PORT.MARGIN — Table Schema

> Source: `INSERTS/I_F.DX.GROUP.PORT.MARGIN` in `DX_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.GPM.REFERENCE.CCY` | `DxGroupPortMargin_ReferenceCcy` | TField |  | Holds the reference currency of the portfolio |
| 2 | `DX.GPM.NETTING.FMT` | `DxGroupPortMargin_NettingFmt` |  |  |  |
| 3 | `DX.GPM.CALL` | `DxGroupPortMargin_Call` |  |  |  |
| 4 | `DX.GPM.PUT` | `DxGroupPortMargin_Put` |  |  |  |
| 5 | `DX.GPM.EXPOSURE` | `DxGroupPortMargin_Exposure` |  |  |  |
| 6 | `DX.GPM.EXP.REFERENCE` | `DxGroupPortMargin_ExpReference` |  |  |  |
| 7 | `DX.GPM.CALL.TRANSACTION` | `DxGroupPortMargin_CallTransaction` |  |  |  |
| 8 | `DX.GPM.PUT.TRANSACTION` | `DxGroupPortMargin_PutTransaction` |  |  |  |
| 9 | `DX.GPM.FIRST.MATURITY` | `DxGroupPortMargin_FirstMaturity` |  |  |  |
| 10 | `DX.GPM.RESERVED.8` | `DxGroupPortMargin_Reserved8` |  |  |  |
| 11 | `DX.GPM.RESERVED.7` | `DxGroupPortMargin_Reserved7` |  |  |  |
| 12 | `DX.GPM.RESERVED.6` | `DxGroupPortMargin_Reserved6` |  |  |  |
| 13 | `DX.GPM.TOTAL.EXPOSURE` | `DxGroupPortMargin_TotalExposure` | TField |  | Sum of EXP.REFERENCE is updated. |
| 14 | `DX.GPM.RESERVED.9` | `DxGroupPortMargin_Reserved9` | TField |  |  |
| 15 | `DX.GPM.RESERVED.5` | `DxGroupPortMargin_Reserved5` | TField |  |  |
| 16 | `DX.GPM.RESERVED.4` | `DxGroupPortMargin_Reserved4` | TField |  |  |
| 17 | `DX.GPM.RESERVED.3` | `DxGroupPortMargin_Reserved3` | TField |  |  |
| 18 | `DX.GPM.RESERVED.2` | `DxGroupPortMargin_Reserved2` | TField |  |  |
| 19 | `DX.GPM.RESERVED.1` | `DxGroupPortMargin_Reserved1` | TField |  |  |
