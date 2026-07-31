# CAMB.L.REG.FUT.FT.LOG — Table Schema

> Source: `INSERTS/I_F.CAMB.L.REG.FUT.FT.LOG` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FT.LOG.STATUS` | `CambLRegFutFtLog_Status` |  |  |  |
| 2 | `FT.LOG.MESSAGE` | `CambLRegFutFtLog_Message` |  |  |  |
| 3 | `FT.LOG.FT.REFERENCE` | `CambLRegFutFtLog_FtReference` |  |  |  |
| 4 | `FT.LOG.LOCAL.REF` | `CambLRegFutFtLog_LocalRef` |  |  |  |
| 5 | `FT.LOG.OVERRIDES` | `CambLRegFutFtLog_Overrides` |  |  |  |
