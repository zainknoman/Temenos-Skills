# CARD.ISSUE.ID.LIST — Table Schema

> Source: `INSERTS/I_F.CARD.ISSUE.ID.LIST` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CI.IDS.RESERVED.3` | `CardIssueIdList_Reserved3` |  |  |  |
| 2 | `CI.IDS.RESERVED.2` | `CardIssueIdList_Reserved2` |  |  |  |
| 3 | `CI.IDS.RESERVED.1` | `CardIssueIdList_Reserved1` | TField |  |  |
| 4 | `CI.IDS.LOCAL.REF` | `CardIssueIdList_LocalRef` |  |  |  |
