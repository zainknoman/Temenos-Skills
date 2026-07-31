# SL.FT.DETS — Table Schema

> Source: `INSERTS/I_F.SL.FT.DETS` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.FT.DETS.PART.ID` | `SlFtDets_PartId` |  |  |  |
| 2 | `SL.FT.DETS.FT.REF` | `SlFtDets_FtRef` |  |  |  |
| 3 | `SL.FT.DETS.STATUS` | `SlFtDets_Status` |  |  |  |
