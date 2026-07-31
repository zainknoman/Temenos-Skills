# CAMB.INTERFACE.STATUS — Table Schema

> Source: `INSERTS/I_F.CAMB.INTERFACE.STATUS` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INT.STA.DATE` | `CambInterfaceStatus_Date` | TField |  |  |
| 2 | `INT.STA.FILE.NAME` | `CambInterfaceStatus_FileName` |  |  |  |
| 3 | `INT.STA.PROCESS.STATUS` | `CambInterfaceStatus_ProcessStatus` |  |  |  |
| 4 | `INT.STA.REASON.FAILURE` | `CambInterfaceStatus_ReasonFailure` |  |  |  |
| 5 | `INT.STA.TIME` | `CambInterfaceStatus_Time` |  |  |  |
