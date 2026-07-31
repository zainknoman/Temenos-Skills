# AA.SPLITS.MERGES.SERVICE.LIST — Table Schema

> Source: `INSERTS/I_F.AA.SPLITS.MERGES.SERVICE.LIST` in `AA_SplitsMerges.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SMS.CAPTURE.REF` | `AaSplitsMergesServiceList_CaptureRef` |  |  |  |
| 2 | `AA.SMS.SOURCE.REF` | `AaSplitsMergesServiceList_SourceRef` |  |  |  |
| 3 | `AA.SMS.TARGET.REF` | `AaSplitsMergesServiceList_TargetRef` |  |  |  |
| 4 | `AA.SMS.FIELD.NAME` | `AaSplitsMergesServiceList_FieldName` |  |  |  |
| 5 | `AA.SMS.FIELD.VALUE` | `AaSplitsMergesServiceList_FieldValue` |  |  |  |
