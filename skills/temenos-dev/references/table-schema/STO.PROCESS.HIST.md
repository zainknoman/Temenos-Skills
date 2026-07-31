# STO.PROCESS.HIST — Table Schema

> Source: `INSERTS/I_F.STO.PROCESS.HIST` in `AC_StandingOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STO.HIS.ACTUAL.EXECUTION.STAGE` | `StoProcessHist_ActualExecutionStage` |  |  |  |
| 2 | `STO.HIS.SPECIFIED.PROCESSING.DATE` | `StoProcessHist_SpecifiedProcessingDate` |  |  |  |
| 3 | `STO.HIS.ACTUAL.PROCESSING.DATE` | `StoProcessHist_ActualProcessingDate` |  |  |  |
| 4 | `STO.HIS.PROCESSING.SYSTEM.DATE` | `StoProcessHist_ProcessingSystemDate` |  |  |  |
| 5 | `STO.HIS.SPECIFIED.EXECUTION.TIME` | `StoProcessHist_SpecifiedExecutionTime` |  |  |  |
| 6 | `STO.HIS.ACTUAL.EXECUTION.TIME` | `StoProcessHist_ActualExecutionTime` |  |  |  |
