# CAMB.L.FT.DETS — Table Schema

> Source: `INSERTS/I_F.CAMB.L.FT.DETS` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.DET.EXTRACT.LINE` | `CambLFtDets_ExtractLine` | TField |  |  |
| 2 | `CAMB.DET.DEBIT.AMOUNT` | `CambLFtDets_DebitAmount` | TField |  |  |
| 3 | `CAMB.DET.CREDIT.AMOUNT` | `CambLFtDets_CreditAmount` | TField |  |  |
| 4 | `CAMB.DET.RESERVED.3` | `CambLFtDets_Reserved3` |  |  |  |
| 5 | `CAMB.DET.RESERVED.4` | `CambLFtDets_Reserved4` | TField |  |  |
| 6 | `CAMB.DET.RESERVED.5` | `CambLFtDets_Reserved5` | TField |  |  |
| 7 | `CAMB.DET.RESERVED.6` | `CambLFtDets_Reserved6` | TField |  |  |
| 8 | `CAMB.DET.RESERVED.7` | `CambLFtDets_Reserved7` | TField |  |  |
| 9 | `CAMB.DET.RESERVED.8` | `CambLFtDets_Reserved8` | TField |  |  |
| 10 | `CAMB.DET.RESERVED.9` | `CambLFtDets_Reserved9` | TField |  |  |
| 11 | `CAMB.DET.OVERRIDE` | `CambLFtDets_Override` |  |  |  |
