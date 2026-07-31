# CAMB.L.INTRC.TXN.ENTRY — Table Schema

> Source: `INSERTS/I_F.CAMB.L.INTRC.TXN.ENTRY` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ITE.FT.REF` | `CambLIntrcTxnEntry_FtRef` | TField |  |  |
| 2 | `CAMB.ITE.REV.FT.REF` | `CambLIntrcTxnEntry_RevFtRef` | TField |  |  |
| 3 | `CAMB.ITE.RESERVED.1` | `CambLIntrcTxnEntry_Reserved1` |  |  |  |
| 4 | `CAMB.ITE.RESERVED.2` | `CambLIntrcTxnEntry_Reserved2` | TField |  |  |
| 5 | `CAMB.ITE.RESERVED.3` | `CambLIntrcTxnEntry_Reserved3` | TField |  |  |
| 6 | `CAMB.ITE.RESERVED.4` | `CambLIntrcTxnEntry_Reserved4` | TField |  |  |
| 7 | `CAMB.ITE.RESERVED.5` | `CambLIntrcTxnEntry_Reserved5` | TField |  |  |
