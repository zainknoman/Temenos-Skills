# LC.SUMMARY — Table Schema

> Source: `INSERTS/I_F.LC.SUMMARY` in `LC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.SUM.DESCRIPTION` | `LcSummary_Description` |  |  |  |
| 2 | `LC.SUM.ISSUE.DATE` | `LcSummary_IssueDate` |  |  |  |
| 3 | `LC.SUM.CURRENCY` | `LcSummary_Currency` |  |  |  |
| 4 | `LC.SUM.LIAB.AMOUNT` | `LcSummary_LiabAmount` |  |  |  |
| 5 | `LC.SUM.OUTS.AMOUNT` | `LcSummary_OutsAmount` |  |  |  |
| 6 | `LC.SUM.TXN.REF` | `LcSummary_TxnRef` |  |  |  |
| 7 | `LC.SUM.CURR.NO` | `LcSummary_CurrNo` | String |  |  |
| 8 | `LC.SUM.DRAW.NO` | `LcSummary_DrawNo` |  |  |  |
