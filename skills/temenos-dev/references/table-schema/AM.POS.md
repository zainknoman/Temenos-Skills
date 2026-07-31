# AM.POS — Table Schema

> Source: `INSERTS/I_F.AM.POS` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.POS.DESCRIPTION` | `AmPos_Description` |  |  |  |
| 2 | `AM.POS.TYPE` | `AmPos_Type` |  |  |  |
| 3 | `AM.POS.APPLICATION` | `AmPos_Application` |  |  |  |
| 4 | `AM.POS.OPTION` | `AmPos_Option` |  |  |  |
| 5 | `AM.POS.CODE` | `AmPos_Code` |  |  |  |
| 6 | `AM.POS.CURRENCY` | `AmPos_Currency` |  |  |  |
| 7 | `AM.POS.VALUATION` | `AmPos_Valuation` |  |  |  |
| 8 | `AM.POS.NOMINAL` | `AmPos_Nominal` |  |  |  |
| 9 | `AM.POS.PRICE` | `AmPos_Price` |  |  |  |
