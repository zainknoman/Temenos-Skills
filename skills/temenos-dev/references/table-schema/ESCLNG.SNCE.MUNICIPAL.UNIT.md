# ESCLNG.SNCE.MUNICIPAL.UNIT — Table Schema

> Source: `INSERTS/I_F.ESCLNG.SNCE.MUNICIPAL.UNIT` in `ESCLNG_EntityInformation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MUNIC.UNIT.MUNICIPALITY.NAME` | `EsclngSnceMunicipalUnit_MunicipalityName` |  |  |  |
| 2 | `MUNIC.UNIT.BANKING.MUNICIPAL.UNIT` | `EsclngSnceMunicipalUnit_BankingMunicipalUnit` | TField |  | B = Banking municipal unit;Blank = Non-Banking municipal unit |
| 3 | `MUNIC.UNIT.BANK.ENTITY.CODE` | `EsclngSnceMunicipalUnit_BankEntityCode` |  |  |  |
| 4 | `MUNIC.UNIT.DATE` | `EsclngSnceMunicipalUnit_Date` |  |  |  |
| 5 | `MUNIC.UNIT.FESTIVE.DAY.INDICATOR` | `EsclngSnceMunicipalUnit_FestiveDayIndicator` |  |  |  |
| 6 | `MUNIC.UNIT.SITUATION` | `EsclngSnceMunicipalUnit_Situation` |  |  |  |
| 7 | `MUNIC.UNIT.LOCAL.REF` | `EsclngSnceMunicipalUnit_LocalRef` |  |  |  |
| 8 | `MUNIC.UNIT.RESERVED.5` | `EsclngSnceMunicipalUnit_Reserved5` | TField |  | Reserved field for future use |
| 9 | `MUNIC.UNIT.RESERVED.4` | `EsclngSnceMunicipalUnit_Reserved4` | TField |  | Reserved field for future use |
| 10 | `MUNIC.UNIT.RESERVED.3` | `EsclngSnceMunicipalUnit_Reserved3` | TField |  | Reserved field for future use |
| 11 | `MUNIC.UNIT.RESERVED.2` | `EsclngSnceMunicipalUnit_Reserved2` | TField |  | Reserved field for future use |
| 12 | `MUNIC.UNIT.RESERVED.1` | `EsclngSnceMunicipalUnit_Reserved1` | TField |  | Reserved field for future use |
| 13 | `MUNIC.UNIT.OVERRIDE` | `EsclngSnceMunicipalUnit_Override` |  |  |  |
| 14 | `MUNIC.UNIT.RECORD.STATUS` | `EsclngSnceMunicipalUnit_RecordStatus` | String |  |  |
| 15 | `MUNIC.UNIT.CURR.NO` | `EsclngSnceMunicipalUnit_CurrNo` | String |  |  |
| 16 | `MUNIC.UNIT.INPUTTER` | `EsclngSnceMunicipalUnit_Inputter` |  |  |  |
| 17 | `MUNIC.UNIT.DATE.TIME` | `EsclngSnceMunicipalUnit_DateTime` |  |  |  |
| 18 | `MUNIC.UNIT.AUTHORISER` | `EsclngSnceMunicipalUnit_Authoriser` | String |  |  |
| 19 | `MUNIC.UNIT.CO.CODE` | `EsclngSnceMunicipalUnit_CoCode` | String |  |  |
| 20 | `MUNIC.UNIT.DEPT.CODE` | `EsclngSnceMunicipalUnit_DeptCode` | String |  |  |
| 21 | `MUNIC.UNIT.AUDITOR.CODE` | `EsclngSnceMunicipalUnit_AuditorCode` | String |  |  |
| 22 | `MUNIC.UNIT.AUDIT.DATE.TIME` | `EsclngSnceMunicipalUnit_AuditDateTime` | String |  |  |
