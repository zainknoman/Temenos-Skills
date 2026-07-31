# FS.GA.COUNTRY.CODES — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUNTRY.CODES` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COUNTRY.CODES.ISSUE.COUNTRY` | `FsGaCountryCodes_CountryCode` |  |  |  |
| 2 | `COUNTRY.CODES.CONTINENT.CODE` | `FsGaCountryCodes_ContinentCode` | TField |  | Continent code Multifonds DB Column is CCONTINENT. |
| 3 | `COUNTRY.CODES.CENTRAL.EASTERN.EURO.COUNTRY` | `FsGaCountryCodes_CentralEasternEuroCountry` | TField |  | Central Eastern Euro Country Multifonds DB Column is C_CEE. |
| 4 | `COUNTRY.CODES.ORG.FOR.ECONOMIC.COOP.AND.DEV` | `FsGaCountryCodes_OrgForEconomicCoopAndDev` | TField |  | Org for Economic Coop and Dev Multifonds DB Column is C_OCDE. |
| 5 | `COUNTRY.CODES.SWISS.BANK.COUNTRY.GROUPS` | `FsGaCountryCodes_SwissBankCountryGroups` | TField |  | Swiss bank country groups Multifonds DB Column is GRP_PAYS. |
| 6 | `COUNTRY.CODES.STARTING.DATE.OF.LAW` | `FsGaCountryCodes_StartingDateOfLaw` | TField |  | Starting date of law Multifonds DB Column is DSTART_LAW. |
| 7 | `COUNTRY.CODES.END.TRANSIT.PERIOD` | `FsGaCountryCodes_EndTransitPeriod` | TField |  | End transit period Multifonds DB Column is DEND_LAW. |
| 8 | `COUNTRY.CODES.CE.MARKING.EURO.ECONOMIC.AREA` | `FsGaCountryCodes_CeMarkingEuroEconomicArea` | TField |  | CE marking Euro Economic Area Multifonds DB Column is C_CE. |
| 9 | `COUNTRY.CODES.DWH.EXPORT` | `FsGaCountryCodes_DwhExport` | TField |  | DWH Export Multifonds DB Column is DWH_EXPORT. |
| 10 | `COUNTRY.CODES.QI1` | `FsGaCountryCodes_Qi1` | TField |  | QI1 Multifonds DB Column is QI. |
| 11 | `COUNTRY.CODES.RECORD.STATUS` | `FsGaCountryCodes_RecordStatus` | String |  |  |
| 12 | `COUNTRY.CODES.CURR.NO` | `FsGaCountryCodes_CurrNo` | String |  |  |
| 13 | `COUNTRY.CODES.INPUTTER` | `FsGaCountryCodes_Inputter` |  |  |  |
| 14 | `COUNTRY.CODES.DATE.TIME` | `FsGaCountryCodes_DateTime` |  |  |  |
| 15 | `COUNTRY.CODES.AUTHORISER` | `FsGaCountryCodes_Authoriser` | String |  |  |
| 16 | `COUNTRY.CODES.CO.CODE` | `FsGaCountryCodes_CoCode` | String |  |  |
| 17 | `COUNTRY.CODES.DEPT.CODE` | `FsGaCountryCodes_DeptCode` | String |  |  |
| 18 | `COUNTRY.CODES.AUDITOR.CODE` | `FsGaCountryCodes_AuditorCode` | String |  |  |
| 19 | `COUNTRY.CODES.AUDIT.DATE.TIME` | `FsGaCountryCodes_AuditDateTime` | String |  |  |
