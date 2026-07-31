# CRS.INDICIA.HISTORY — Table Schema

> Source: `INSERTS/I_F.CRS.INDICIA.HISTORY` in `CD_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CRS.IHIS.END.DATE` | `CrsIndiciaHistory_EndDate` |  |  |  |
| 2 | `CRS.IHIS.INDICIA.SUMMARY` | `CrsIndiciaHistory_IndiciaSummary` |  |  |  |
| 3 | `CRS.IHIS.INDICIA.START.DATE` | `CrsIndiciaHistory_IndiciaStartDate` |  |  |  |
| 4 | `CRS.IHIS.INDICIA.COUNTRY` | `CrsIndiciaHistory_IndiciaCountry` |  |  |  |
| 5 | `CRS.IHIS.REPORTING.JURISDICTION` | `CrsIndiciaHistory_ReportingJurisdiction` |  |  |  |
| 6 | `CRS.IHIS.TAX.RESIDENCE` | `CrsIndiciaHistory_TaxResidence` |  |  |  |
| 7 | `CRS.IHIS.INDICIA.DATA.RULE` | `CrsIndiciaHistory_IndiciaDataRule` |  |  |  |
| 8 | `CRS.IHIS.INDICIA.DATA.VALUE` | `CrsIndiciaHistory_IndiciaDataValue` |  |  |  |
| 9 | `CRS.IHIS.SELF.CERTIFICATION` | `CrsIndiciaHistory_SelfCertification` |  |  |  |
| 10 | `CRS.IHIS.CRS.STATUS` | `CrsIndiciaHistory_CrsStatus` |  |  |  |
