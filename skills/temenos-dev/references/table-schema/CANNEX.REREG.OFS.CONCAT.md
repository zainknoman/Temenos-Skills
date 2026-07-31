# CANNEX.REREG.OFS.CONCAT — Table Schema

> Source: `INSERTS/I_F.CANNEX.REREG.OFS.CONCAT` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REG.OFS.CNT.FT.OFS.MSG` | `CannexReregOfsConcat_FtOfsMsg` | TField |  | This field will holds the FT ofs message when the event type is 'P' while processing the re-registration file |
| 2 | `REG.OFS.CNT.FILE.NAME` | `CannexReregOfsConcat_FileName` | TField |  | This field will holds the file name when the event type is 'P' while processing the re-registration file |
