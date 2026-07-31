# AM.GRP.POS — Table Schema

> Source: `INSERTS/I_F.AM.GRP.POS` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.GPS.DESCRIPTION` | `AmGrpPos_Description` |  |  |  |
| 2 | `AM.GPS.TYPE` | `AmGrpPos_Type` |  |  |  |
| 3 | `AM.GPS.APPLICATION` | `AmGrpPos_Application` |  |  |  |
| 4 | `AM.GPS.OPTION` | `AmGrpPos_Option` |  |  |  |
| 5 | `AM.GPS.CODE` | `AmGrpPos_Code` |  |  |  |
| 6 | `AM.GPS.CURRENCY` | `AmGrpPos_Currency` |  |  |  |
| 7 | `AM.GPS.VALUATION` | `AmGrpPos_Valuation` |  |  |  |
| 8 | `AM.GPS.NOMINAL` | `AmGrpPos_Nominal` |  |  |  |
| 9 | `AM.GPS.PRICE` | `AmGrpPos_Price` |  |  |  |
