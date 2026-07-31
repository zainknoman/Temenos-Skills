# EB.COB.MONITOR.OUTPUT — Table Schema

> Source: `INSERTS/I_F.EB.COB.MONITOR.OUTPUT` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.COB.COB.RUN.DATE` | `EbCobMonitorOutput_EbCobCobRunDate` |  |  |  |
| 2 | `EB.COB.START.TIME` | `EbCobMonitorOutput_EbStageStartTime` |  |  |  |
| 3 | `EB.COB.END.TIME` | `EbCobMonitorOutput_EbStageEndTime` |  |  |  |
| 4 | `EB.COB.EXPECTED.RUNTIME` | `EbCobMonitorOutput_EbCobExpectedRuntime` |  |  |  |
| 5 | `EB.COB.ACTUAL.RUNTIME` | `EbCobMonitorOutput_EbCobActualRunTime` |  |  |  |
| 6 | `EB.COB.STAGE.THRESHOLD` | `EbCobMonitorOutput_StageThreshold` | TField |  | It stores calculated deviation or stage threshold value for the particular stage or COB. Value in the format NN.nn format (Example - 3.45 or 10.65) |
| 7 | `EB.COB.BREACH.INFO` | `EbCobMonitorOutput_BreachInfo` | TField |  | It stored breach details Possible values : INFO/IGNORE/WARNING/CRITICAL as configured against the TEC.ITEM |
