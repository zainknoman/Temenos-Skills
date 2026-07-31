# NORCUS.MUNICIPAL.CODE — Table Schema

> Source: `INSERTS/I_F.NORCUS.MUNICIPAL.CODE` in `FICUST_CustomerOnboarding.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORCUS.MUNICIPAL.DESCRIPTION` | `NorcusMunicipalCode_Description` | TField |  | Description for the record is given. |
| 2 | `NORCUS.MUNICIPAL.END.DATE` | `NorcusMunicipalCode_EndDate` | TField |  | Date field - YYYYMMDD � End date can be defined |
| 3 | `NORCUS.MUNICIPAL.START.DATE` | `NorcusMunicipalCode_StartDate` | TField |  | Date field � YYYYMMDD � Start date can be defined |
| 4 | `NORCUS.MUNICIPAL.LANGUAGE.CODE` | `NorcusMunicipalCode_LanguageCode` | TField |  | The purpose of the field is to define language code.Eg:1. Finnish2. Swedish |
| 5 | `NORCUS.MUNICIPAL.MUNICIPALITY.NAME` | `NorcusMunicipalCode_MunicipalityName` |  |  |  |
| 6 | `NORCUS.MUNICIPAL.PROVINCE.CODE` | `NorcusMunicipalCode_ProvinceCode` | TField |  | The purpose of the field is to define province code value. |
| 7 | `NORCUS.MUNICIPAL.AGRI.DISTRICT.CODE` | `NorcusMunicipalCode_AgriDistrictCode` | TField |  | The purpose of the field is to define Agri District code value. |
| 8 | `NORCUS.MUNICIPAL.INT.AREA.CODE.1` | `NorcusMunicipalCode_IntAreaCode1` | TField |  | The purpose of the field is to define Internal Area code value. |
| 9 | `NORCUS.MUNICIPAL.INT.AREA.CODE.2` | `NorcusMunicipalCode_IntAreaCode2` | TField |  | The purpose of the field is to define Internal Area code value. |
| 10 | `NORCUS.MUNICIPAL.SUBSIDY.AREA.CODE` | `NorcusMunicipalCode_SubsidyAreaCode` | TField |  | The purpose of the field is to define subsidy code value. |
| 11 | `NORCUS.MUNICIPAL.REGION.CODE` | `NorcusMunicipalCode_RegionCode` | TField |  | The purpose of the field is to define Regional code value. |
| 12 | `NORCUS.MUNICIPAL.INT.HOUSING.NAME` | `NorcusMunicipalCode_IntHousingName` | TField |  | The purpose of the field is to define Internal Municipal Names. |
| 13 | `NORCUS.MUNICIPAL.RISK.AREA.CODE` | `NorcusMunicipalCode_RiskAreaCode` | TField |  | Area Codes which is defined for each Municipality. |
| 14 | `NORCUS.MUNICIPAL.RESERVED.6` | `NorcusMunicipalCode_Reserved6` | TField |  |  |
| 15 | `NORCUS.MUNICIPAL.RESERVED.5` | `NorcusMunicipalCode_Reserved5` | TField |  |  |
| 16 | `NORCUS.MUNICIPAL.RESERVED.4` | `NorcusMunicipalCode_Reserved4` | TField |  |  |
| 17 | `NORCUS.MUNICIPAL.RESERVED.3` | `NorcusMunicipalCode_Reserved3` | TField |  |  |
| 18 | `NORCUS.MUNICIPAL.RESERVED.2` | `NorcusMunicipalCode_Reserved2` | TField |  |  |
| 19 | `NORCUS.MUNICIPAL.RESERVED.1` | `NorcusMunicipalCode_Reserved1` | TField |  |  |
| 20 | `NORCUS.MUNICIPAL.LOCAL.REF` | `NorcusMunicipalCode_LocalRef` |  |  |  |
| 21 | `NORCUS.MUNICIPAL.OVERRIDE` | `NorcusMunicipalCode_Override` |  |  |  |
| 22 | `NORCUS.MUNICIPAL.RECORD.STATUS` | `NorcusMunicipalCode_RecordStatus` | String |  |  |
| 23 | `NORCUS.MUNICIPAL.CURR.NO` | `NorcusMunicipalCode_CurrNo` | String |  |  |
| 24 | `NORCUS.MUNICIPAL.INPUTTER` | `NorcusMunicipalCode_Inputter` |  |  |  |
| 25 | `NORCUS.MUNICIPAL.DATE.TIME` | `NorcusMunicipalCode_DateTime` |  |  |  |
| 26 | `NORCUS.MUNICIPAL.AUTHORISER` | `NorcusMunicipalCode_Authoriser` | String |  |  |
| 27 | `NORCUS.MUNICIPAL.CO.CODE` | `NorcusMunicipalCode_CoCode` | String |  |  |
| 28 | `NORCUS.MUNICIPAL.DEPT.CODE` | `NorcusMunicipalCode_DeptCode` | String |  |  |
| 29 | `NORCUS.MUNICIPAL.AUDITOR.CODE` | `NorcusMunicipalCode_AuditorCode` | String |  |  |
| 30 | `NORCUS.MUNICIPAL.AUDIT.DATE.TIME` | `NorcusMunicipalCode_AuditDateTime` | String |  |  |
