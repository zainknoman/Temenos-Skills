# FATCA.INDICIA.HISTORY — Table Schema

> Source: `INSERTS/I_F.FATCA.INDICIA.HISTORY` in `FA_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.FI.HIS.END.DATE` | `FatcaIndiciaHistory_EndDate` |  |  |  |
| 2 | `FA.FI.HIS.INDICIA.SUMMARY` | `FatcaIndiciaHistory_IndiciaSummary` |  |  |  |
| 3 | `FA.FI.HIS.INDICIA.START.DATE` | `FatcaIndiciaHistory_IndiciaStartDate` |  |  |  |
| 4 | `FA.FI.HIS.INDICIA.COUNTRY` | `FatcaIndiciaHistory_IndiciaCountry` |  |  |  |
| 5 | `FA.FI.HIS.INDICIA.DATA.VALUE` | `FatcaIndiciaHistory_IndiciaDataValue` |  |  |  |
| 6 | `FA.FI.HIS.INDICIA.DATA.RULE` | `FatcaIndiciaHistory_IndiciaDataRule` |  |  |  |
