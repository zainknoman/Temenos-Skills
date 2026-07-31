# ACH.ERROR — Table Schema

> Source: `INSERTS/I_F.ACH.ERROR` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHERR.FILE.NAME` | `AchError_FileName` | TField |  | Name of the ACH file which is loaded. |
| 2 | `ACHERR.SERVICE.NAME` | `AchError_ServiceName` | TField |  | Name of the TSA service which capture the runtime error messages. |
| 3 | `ACHERR.REMARKS` | `AchError_Remarks` |  |  |  |
| 4 | `ACHERR.LOG.TIME` | `AchError_LogTime` | TField |  | Date time recorded during error messages logged. |
| 5 | `ACHERR.LOG.DATE` | `AchError_LogDate` | TField |  | Date recorded during error messages logged. |
| 6 | `ACHERR.RESERVED.18` | `AchError_Reserved18` | TField |  |  |
| 7 | `ACHERR.RESERVED.17` | `AchError_Reserved17` | TField |  |  |
| 8 | `ACHERR.RESERVED.16` | `AchError_Reserved16` | TField |  |  |
| 9 | `ACHERR.RESERVED.15` | `AchError_Reserved15` | TField |  |  |
| 10 | `ACHERR.RESERVED.14` | `AchError_Reserved14` | TField |  |  |
| 11 | `ACHERR.RESERVED.13` | `AchError_Reserved13` | TField |  |  |
| 12 | `ACHERR.RESERVED.12` | `AchError_Reserved12` | TField |  |  |
| 13 | `ACHERR.RESERVED.11` | `AchError_Reserved11` | TField |  |  |
| 14 | `ACHERR.RESERVED.10` | `AchError_Reserved10` | TField |  |  |
| 15 | `ACHERR.RESERVED.9` | `AchError_Reserved9` | TField |  |  |
| 16 | `ACHERR.RESERVED.8` | `AchError_Reserved8` | TField |  |  |
| 17 | `ACHERR.RESERVED.7` | `AchError_Reserved7` | TField |  |  |
| 18 | `ACHERR.RESERVED.6` | `AchError_Reserved6` | TField |  |  |
| 19 | `ACHERR.RESERVED.5` | `AchError_Reserved5` | TField |  |  |
| 20 | `ACHERR.RESERVED.4` | `AchError_Reserved4` | TField |  |  |
| 21 | `ACHERR.RESERVED.3` | `AchError_Reserved3` | TField |  |  |
| 22 | `ACHERR.RESERVED.2` | `AchError_Reserved2` | TField |  |  |
| 23 | `ACHERR.RESERVED.1` | `AchError_Reserved1` | TField |  |  |
