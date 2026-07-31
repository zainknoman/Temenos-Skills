# CAMB.CHQ.PRINT.REF — Table Schema

> Source: `INSERTS/I_F.CAMB.CHQ.PRINT.REF` in `CACQMG_ChequeManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHQ.PR.ARRANGEMENT` | `CambChqPrintRef_Arrangement` | TField |  | Field is used to store the Arrangement ID for which payment order is generated.Validation : record from AA.ARRANGEMENT |
| 2 | `CHQ.PR.ACTIVITY` | `CambChqPrintRef_Activity` |  |  |  |
| 3 | `CHQ.PR.CONSOL.PO` | `CambChqPrintRef_ConsolPo` |  |  |  |
