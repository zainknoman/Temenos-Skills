# RP.ALT.NOSTRO — Table Schema

> Source: `INSERTS/I_F.RP.ALT.NOSTRO` in `RP_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RP.ALT.DEP.NO` | `RpAltNostro_DepNo` |  |  |  |
| 2 | `RP.ALT.RP.ACCOUNT` | `RpAltNostro_RpAccount` |  |  |  |
| 3 | `RP.ALT.COUNTERPARTY` | `RpAltNostro_Counterparty` |  |  |  |
| 4 | `RP.ALT.RP.NOMINAL` | `RpAltNostro_RpNominal` |  |  |  |
| 5 | `RP.ALT.RP.GROSS.AMT` | `RpAltNostro_RpGrossAmt` |  |  |  |
| 6 | `RP.ALT.RP.SRC.TAX` | `RpAltNostro_RpSrcTax` |  |  |  |
| 7 | `RP.ALT.RP.TOT.CHGS` | `RpAltNostro_RpTotChgs` |  |  |  |
| 8 | `RP.ALT.RP.NET.AMT` | `RpAltNostro_RpNetAmt` |  |  |  |
| 9 | `RP.ALT.RP.CASH.CCY` | `RpAltNostro_RpCashCcy` |  |  |  |
| 10 | `RP.ALT.RP.CASH.XCH` | `RpAltNostro_RpCashXch` |  |  |  |
| 11 | `RP.ALT.RP.NET.LCY` | `RpAltNostro_RpNetLcy` |  |  |  |
| 12 | `RP.ALT.RP.ENTL.AMT` | `RpAltNostro_RpEntlAmt` |  |  |  |
| 13 | `RP.ALT.RP.MBS.AMT` | `RpAltNostro_RpMbsAmt` |  |  |  |
