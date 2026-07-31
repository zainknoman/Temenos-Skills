# EFT.NOMINEE.SETTLE — Table Schema

> Source: `INSERTS/I_F.EFT.NOMINEE.SETTLE` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EFT.NOM.SETT.AAA.ID` | `EftNomineeSettle_AaaId` |  |  |  |
| 2 | `EFT.NOM.SETT.RESERVED.8` | `EftNomineeSettle_Reserved8` |  |  |  |
| 3 | `EFT.NOM.SETT.RESERVED.9` | `EftNomineeSettle_Reserved9` |  |  |  |
| 4 | `EFT.NOM.SETT.RESERVED.10` | `EftNomineeSettle_Reserved10` |  |  |  |
| 5 | `EFT.NOM.SETT.RESERVED.11` | `EftNomineeSettle_Reserved11` |  |  |  |
| 6 | `EFT.NOM.SETT.RESERVED.12` | `EftNomineeSettle_Reserved12` |  |  |  |
