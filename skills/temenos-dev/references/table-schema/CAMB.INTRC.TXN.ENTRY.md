# CAMB.INTRC.TXN.ENTRY — Table Schema

> Source: `INSERTS/I_F.CAMB.INTRC.TXN.ENTRY` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ITE.FT.REF` | `CambIntrcTxnEntry_FtRef` |  |  |  |
| 2 | `CAMB.ITE.REV.FT.REF` | `CambIntrcTxnEntry_RevFtRef` |  |  |  |
| 3 | `CAMB.ITE.RESERVED.1` | `CambIntrcTxnEntry_Reserved1` |  |  |  |
| 4 | `CAMB.ITE.RESERVED.2` | `CambIntrcTxnEntry_Reserved2` |  |  |  |
| 5 | `CAMB.ITE.RESERVED.3` | `CambIntrcTxnEntry_Reserved3` |  |  |  |
| 6 | `CAMB.ITE.RESERVED.4` | `CambIntrcTxnEntry_Reserved4` |  |  |  |
| 7 | `CAMB.ITE.RESERVED.5` | `CambIntrcTxnEntry_Reserved5` |  |  |  |
