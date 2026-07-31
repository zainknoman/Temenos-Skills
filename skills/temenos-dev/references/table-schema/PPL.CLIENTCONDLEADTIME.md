# PPL.CLIENTCONDLEADTIME — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTCONDLEADTIME` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCLT.ClientLeadID` | `PplClientcondleadtime_Clientleadid` |  |  |  |
| 2 | `PPCLT.ClientConditionsID` | `PplClientcondleadtime_Clientconditionsid` |  |  |  |
| 3 | `PPCLT.CurrencyCode` | `PplClientcondleadtime_Currencycode` |  |  |  |
| 4 | `PPCLT.IncomingCutOffLeadTime` | `PplClientcondleadtime_Incomingcutoffleadtime` |  |  |  |
| 5 | `PPCLT.OutgoingCutOffLeadTime` | `PplClientcondleadtime_Outgoingcutoffleadtime` |  |  |  |
