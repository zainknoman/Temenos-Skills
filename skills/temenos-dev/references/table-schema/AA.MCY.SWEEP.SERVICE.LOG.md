# AA.MCY.SWEEP.SERVICE.LOG — Table Schema

> Source: `INSERTS/I_F.AA.MCY.SWEEP.SERVICE.LOG` in `MCYAAR_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MCY.SWP.DATE` | `AaMcySweepServiceLog_Date` | TField |  | Contains the effective date on which the failure was happened. |
| 2 | `MCY.SWP.FAILURE.REASON` | `AaMcySweepServiceLog_FailureReason` |  |  |  |
| 3 | `MCY.SWP.ERR.SOURCE` | `AaMcySweepServiceLog_ErrSource` |  |  |  |
| 4 | `MCY.SWP.ERR.MESSAGE` | `AaMcySweepServiceLog_ErrMessage` |  |  |  |
