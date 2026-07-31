# CARD.ISSUE.ORDER.ID.LIST — Table Schema

> Source: `INSERTS/I_F.CARD.ISSUE.ORDER.ID.LIST` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CISS.CO.RESERVED.3` | `CardIssueOrderIdList_Reserved3` | TField |  |  |
| 2 | `CISS.CO.RESERVED.2` | `CardIssueOrderIdList_Reserved2` | TField |  |  |
| 3 | `CISS.CO.RESERVED.1` | `CardIssueOrderIdList_Reserved1` | TField |  |  |
| 4 | `CISS.CO.LOCAL.REF` | `CardIssueOrderIdList_LocalRef` |  |  |  |
