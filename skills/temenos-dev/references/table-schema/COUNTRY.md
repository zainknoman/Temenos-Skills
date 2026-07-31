# COUNTRY — Table Schema

> Source: `INSERTS/I_F.COUNTRY` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.COU.CURRENCY.CODE` | `Country_CurrencyCode` |  |  |  |
| 2 | `EB.COU.COUNTRY.NAME` | `Country_CountryName` |  |  |  |
| 3 | `EB.COU.SHORT.NAME` | `Country_ShortName` |  |  |  |
| 4 | `EB.COU.PRESENTATION.CODE` | `Country_PresentationCode` | TField |  | Validation Rules: Up to 4 type 'S' (SWIFT) characters. |
| 5 | `EB.COU.CENTRAL.BANK.CODE` | `Country_CentralBankCode` | TField |  | Validation Rules: Up to 5 type 'S' (SWIFT) characters. |
| 6 | `EB.COU.GEOGRAPHICAL.BLOCK` | `Country_GeographicalBlock` | TField |  | Country's geographical block. Options are: ID DESCRIPTION COUNTRY == =========== ======= AMERICA The Americas AR CA UM US VG VI ASIA Far East/Asia AU ID EMERGING Emerging Markets AL CL HU IL SA EUROPE Continental Europe AD BE ES EU FR GI GR IE IT KY MC NO PT SE SM VA GERMAN Dem Block - Europe AT CH DD DE LI LU JAPAN Japan JP MULTINAT Multi-country XE OTHER Unallocated New Countries TJ UK United Kingdom GB GG IM JE |
| 7 | `EB.COU.BUSINESS.CENTRE` | `Country_BusinessCentre` | TField | No | This field is used to define the main business centre for the relevant country. Validation Rules: Upto 35 type S characters. Optional input. |
| 8 | `EB.COU.CG.INDEX.DATE` | `Country_CgIndexDate` |  |  |  |
| 9 | `EB.COU.CG.INDEX` | `Country_CgIndex` |  |  |  |
| 10 | `EB.COU.TRACER.DAYS` | `Country_TracerDays` | TField |  | Accepts valid days format. If defined, will be used to default TRACER.DAYS field in EB.FREE.MESSAGE file. Eg : +2W or 25W etc Validation Rules: : Tracer days should be like +NW or NNW, where N stands for Number of days and W stands for Working days. |
| 11 | `EB.COU.HIGH.RISK` | `Country_HighRisk` | TField |  | Indicates whether this country is considered high risk. |
| 12 | `EB.COU.IDD.PREFIX.PHONE` | `Country_IddPrefixPhone` | TField |  | This field represents an international call prefix or dial out code for a specific country. Validation Rules: Value must exists on IDD.CODE.DEF table,Should be set with CONCAT file COUNTRY.IDD.PREFIX phone. So that on input / amend this field on particular country the concat file will get update automatically. |
| 13 | `EB.COU.ALPHA.THREE.CODE` | `Country_AlphaThreeCode` | TField |  | This field represents an alternative name of country code is length 3 characters for a specific country. Validation Rules: Should be set with CONCAT file COUNTRY.ALPHATHREE. So that on input / amend this field on particular country the concat file will get update automatically. |
| 14 | `EB.COU.NUMERIC.CODE` | `Country_NumericCode` | TField |  | This field represents a numeric value of country code is length 3 digit numbers for a specific country. Validation Rules: Should be set with CONCAT file COUNTRY.NUMERIC. So that on input / amend this field on particular country the concat file will get update automatically. |
| 15 | `EB.COU.REPORTING.COUNTRY` | `Country_ReportingCountry` | TField |  | This field represents a reporting country and must be a valid COUNTRY id but cannot be the same as its own Country ID or ID suffixed with year for a specific country. Validation Rules: this field NOINPUT if the ID is suffixed with year, ex: GB.2020 |
| 16 | `EB.COU.FISCAL.JURISDICTION` | `Country_FiscalJurisdiction` | TField |  | This field will be used to record the fiscal jurisdiction of a country if it is not itself. This can be the case when a country is actually a territory of another country. For example, Guam has a country code of GU but it is actually a territory of the United States, and should be considered as US for reporting purposes. Validation Rules: valid record in country table It cannot be the same as its own Country ID |
| 17 | `EB.COU.LOCAL.REF` | `Country_LocalRef` |  |  |  |
| 18 | `EB.COU.RECORD.STATUS` | `Country_RecordStatus` | String |  |  |
| 19 | `EB.COU.CURR.NO` | `Country_CurrNo` | String |  |  |
| 20 | `EB.COU.INPUTTER` | `Country_Inputter` |  |  |  |
| 21 | `EB.COU.DATE.TIME` | `Country_DateTime` |  |  |  |
| 22 | `EB.COU.AUTHORISER` | `Country_Authoriser` | String |  |  |
| 23 | `EB.COU.CO.CODE` | `Country_CoCode` | String |  |  |
| 24 | `EB.COU.DEPT.CODE` | `Country_DeptCode` | String |  |  |
| 25 | `EB.COU.AUDITOR.CODE` | `Country_AuditorCode` | String |  |  |
| 26 | `EB.COU.AUDIT.DATE.TIME` | `Country_AuditDateTime` | String |  |  |
| 27 | `EB.COU.NATIONALITY` | `Country_Nationality` | TField |  | This field will be used to indicate if this country code can be used as a nationality code. Allowed values are YES, NO or Null |
| 28 | `EB.COU.ID.DOCS` | `Country_IdDocs` | TField |  | This field will be used to indicate if this country code can issues its own identity documents. Allowed values are YES, NO or Null |
