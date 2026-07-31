# CAMB.L.ACH.RETRY.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAMB.L.ACH.RETRY.DETAILS` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.RTRY.RETRY.COUNT` | `CambLAchRetryDetails_RetryCount` |  |  |  |
| 2 | `CAMB.RTRY.STATUS` | `CambLAchRetryDetails_Status` |  |  |  |
| 3 | `CAMB.RTRY.RESERVED.5` | `CambLAchRetryDetails_Reserved5` |  |  |  |
| 4 | `CAMB.RTRY.RESERVED.4` | `CambLAchRetryDetails_Reserved4` |  |  |  |
| 5 | `CAMB.RTRY.RESERVED.3` | `CambLAchRetryDetails_Reserved3` |  |  |  |
| 6 | `CAMB.RTRY.RESERVED.2` | `CambLAchRetryDetails_Reserved2` |  |  |  |
| 7 | `CAMB.RTRY.RESERVED.1` | `CambLAchRetryDetails_Reserved1` |  |  |  |
