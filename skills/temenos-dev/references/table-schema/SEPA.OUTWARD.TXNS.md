# SEPA.OUTWARD.TXNS — Table Schema

> Source: `INSERTS/I_F.SEPA.OUTWARD.TXNS` in `EP_OutwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.OTXN.SEPA.OUTWARD.ID` | `SepaOutwardTxns_SepaOutwardId` | TField |  | The SEPA.OUTWARD record ID's of each transaction for the corresponding Outward Bulk Validation Rules: Up to 40 characters free text. |
