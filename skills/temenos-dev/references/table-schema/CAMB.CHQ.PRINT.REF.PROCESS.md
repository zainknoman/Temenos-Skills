# CAMB.CHQ.PRINT.REF.PROCESS — Table Schema

> Source: `INSERTS/I_F.CAMB.CHQ.PRINT.REF.PROCESS` in `CACQMG_ChequeManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHQ.PRO.VALUE.DATE` | `CambChqPrintRefProcess_ValueDate` | TField |  |  |
| 2 | `CHQ.PRO.CUSTOMER` | `CambChqPrintRefProcess_Customer` | TField |  |  |
| 3 | `CHQ.PRO.AGENT.NO` | `CambChqPrintRefProcess_AgentNo` | TField |  |  |
| 4 | `CHQ.PRO.PROCESS.DATE` | `CambChqPrintRefProcess_ProcessDate` | TField |  |  |
| 5 | `CHQ.PRO.ADDITIONAL.INFO` | `CambChqPrintRefProcess_AdditionalInfo` | TField |  |  |
| 6 | `CHQ.PRO.NOMINEE.FLAG` | `CambChqPrintRefProcess_NomineeFlag` | TField |  |  |
| 7 | `CHQ.PRO.CONSOLIDATE.PAYMENT` | `CambChqPrintRefProcess_ConsolidatePayment` | TField |  |  |
