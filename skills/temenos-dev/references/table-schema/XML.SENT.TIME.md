# XML.SENT.TIME — Table Schema

> Source: `INSERTS/I_F.XML.SENT.TIME` in `AC_AccountStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.DATA.TIME` | `XmlSentTime_Time` | TField |  | TIME specified in ACCOUNT.STATEMENT The time is in the format of HH:MM The service AC.XML.INTRMSTMT.GENERATE selects the TIME less than the current time to generate CAMT052 message |
