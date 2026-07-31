# TCIB.RECENT.TRANS — Table Schema

> Source: `INSERTS/I_F.TCIB.RECENT.TRANS` in `T2_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCIB.COM.SE.NAME` | `TcibRecentTrans_SeName` |  |  |  |
| 2 | `TCIB.COM.TOTAL.RECORDS` | `TcibRecentTrans_TotalRecords` | TField |  |  |
| 3 | `TCIB.COM.PROCESSED` | `TcibRecentTrans_Processed` | TField |  |  |
