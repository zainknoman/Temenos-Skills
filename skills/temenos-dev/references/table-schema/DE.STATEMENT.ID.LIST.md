# DE.STATEMENT.ID.LIST — Table Schema

> Source: `INSERTS/I_F.DE.STATEMENT.ID.LIST` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.STMTID.DELIVERY.LISTENER.ID` | `DeStatementIdList_DeliveryListenerId` |  |  |  |
| 2 | `DE.STMTID.TOTAL.PAGES` | `DeStatementIdList_TotalPages` | TField |  | Indicates the total number of pages available for a statement. |
