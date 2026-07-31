# RD.PARTI.CO.CCY.CONCAT — Table Schema

> Source: `INSERTS/I_F.RD.PARTI.CO.CCY.CONCAT` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.PCCC.COMBINED.KEY` | `RdPartiCoCcyConcat_CombinedKey` |  |  |  |
| 2 | `RD.PCCC.CUSTOM.KEY` | `RdPartiCoCcyConcat_CustomKey` |  |  |  |
| 3 | `RD.PCCC.MASTER.KEY` | `RdPartiCoCcyConcat_MasterKey` |  |  |  |
| 4 | `RD.PCCC.FUTURE.KEY` | `RdPartiCoCcyConcat_FutureKey` |  |  |  |
| 5 | `RD.PCCC.DEFAULT.CUSTOM.KEY` | `RdPartiCoCcyConcat_DefaultCustomKey` |  |  |  |
