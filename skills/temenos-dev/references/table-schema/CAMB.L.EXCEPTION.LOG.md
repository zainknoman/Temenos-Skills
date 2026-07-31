# CAMB.L.EXCEPTION.LOG — Table Schema

> Source: `INSERTS/I_F.CAMB.L.EXCEPTION.LOG` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.LOG.BATCH.NAME` | `CambLExceptionLog_BatchName` | TField |  | The purpose of this field is used to store the batch job name while processing the CBR extract. |
| 2 | `CAMB.LOG.ERROR.MSG` | `CambLExceptionLog_ErrorMsg` |  |  |  |
| 3 | `CAMB.LOG.ISSUE.DATE` | `CambLExceptionLog_IssueDate` | TField |  | This field is used to capture the card reorder issue date. |
| 4 | `CAMB.LOG.RESERVED.2` | `CambLExceptionLog_Reserved2` | TField |  |  |
| 5 | `CAMB.LOG.RESERVED.3` | `CambLExceptionLog_Reserved3` | TField |  |  |
| 6 | `CAMB.LOG.RESERVED.4` | `CambLExceptionLog_Reserved4` | TField |  |  |
| 7 | `CAMB.LOG.RESERVED.5` | `CambLExceptionLog_Reserved5` | TField |  |  |
| 8 | `CAMB.LOG.RESERVED.6` | `CambLExceptionLog_Reserved6` | TField |  |  |
| 9 | `CAMB.LOG.RESERVED.7` | `CambLExceptionLog_Reserved7` | TField |  |  |
| 10 | `CAMB.LOG.RESERVED.8` | `CambLExceptionLog_Reserved8` | TField |  |  |
| 11 | `CAMB.LOG.RESERVED.9` | `CambLExceptionLog_Reserved9` | TField |  |  |
| 12 | `CAMB.LOG.RESERVED.10` | `CambLExceptionLog_Reserved10` | TField |  |  |
| 13 | `CAMB.LOG.LOCAL.REF` | `CambLExceptionLog_LocalRef` |  |  |  |
| 14 | `CAMB.LOG.OVERRIDE` | `CambLExceptionLog_Override` |  |  |  |
