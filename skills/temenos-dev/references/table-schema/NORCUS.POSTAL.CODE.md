# NORCUS.POSTAL.CODE — Table Schema

> Source: `INSERTS/I_F.NORCUS.POSTAL.CODE` in `FICUST_CustomerOnboarding.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORCUS.POSTAL.DESCRIPTION` | `NorcusPostalCode_Description` | TField |  | Description for the record is given. |
| 2 | `NORCUS.POSTAL.POST.CODE.NAME` | `NorcusPostalCode_PostCodeName` |  |  |  |
| 3 | `NORCUS.POSTAL.SHORT.NAME` | `NorcusPostalCode_ShortName` |  |  |  |
| 4 | `NORCUS.POSTAL.START.DATE` | `NorcusPostalCode_StartDate` | TField |  | Date field � YYYYMMDD � Start date can be defined. |
| 5 | `NORCUS.POSTAL.TYPE` | `NorcusPostalCode_Type` | TField |  | Describes post code type.1. Normal Postcode2. PO BOX postcode3. Corporate postcode4. Compilation postcode5. Reply mail postcode6. Smart post (parcel machine)7. Pick-up point8. Technical postcode |
| 6 | `NORCUS.POSTAL.ADMIN.REGION.CODE` | `NorcusPostalCode_AdminRegionCode` | TField |  | The purpose of the field is to define Admin Region Code value. |
| 7 | `NORCUS.POSTAL.ADMIN.REGION.NAME` | `NorcusPostalCode_AdminRegionName` |  |  |  |
| 8 | `NORCUS.POSTAL.MUNICIPALITY.CODE` | `NorcusPostalCode_MunicipalityCode` | TField |  | The purpose of the field is to define municipal code value. |
| 9 | `NORCUS.POSTAL.MUNICIPALITY.LANGUAGE.CODE` | `NorcusPostalCode_MunicipalityLanguageCode` | TField |  | The purpose of the field is to define language code.Eg:1. Finnish2. Swedish |
| 10 | `NORCUS.POSTAL.RESERVED.8` | `NorcusPostalCode_Reserved8` | TField |  |  |
| 11 | `NORCUS.POSTAL.RESERVED.7` | `NorcusPostalCode_Reserved7` | TField |  |  |
| 12 | `NORCUS.POSTAL.RESERVED.6` | `NorcusPostalCode_Reserved6` | TField |  |  |
| 13 | `NORCUS.POSTAL.RESERVED.5` | `NorcusPostalCode_Reserved5` | TField |  |  |
| 14 | `NORCUS.POSTAL.RESERVED.4` | `NorcusPostalCode_Reserved4` | TField |  |  |
| 15 | `NORCUS.POSTAL.RESERVED.3` | `NorcusPostalCode_Reserved3` | TField |  |  |
| 16 | `NORCUS.POSTAL.RESERVED.2` | `NorcusPostalCode_Reserved2` | TField |  |  |
| 17 | `NORCUS.POSTAL.RESERVED.1` | `NorcusPostalCode_Reserved1` | TField |  |  |
| 18 | `NORCUS.POSTAL.LOCAL.REF` | `NorcusPostalCode_LocalRef` |  |  |  |
| 19 | `NORCUS.POSTAL.OVERRIDE` | `NorcusPostalCode_Override` |  |  |  |
| 20 | `NORCUS.POSTAL.RECORD.STATUS` | `NorcusPostalCode_RecordStatus` | String |  |  |
| 21 | `NORCUS.POSTAL.CURR.NO` | `NorcusPostalCode_CurrNo` | String |  |  |
| 22 | `NORCUS.POSTAL.INPUTTER` | `NorcusPostalCode_Inputter` |  |  |  |
| 23 | `NORCUS.POSTAL.DATE.TIME` | `NorcusPostalCode_DateTime` |  |  |  |
| 24 | `NORCUS.POSTAL.AUTHORISER` | `NorcusPostalCode_Authoriser` | String |  |  |
| 25 | `NORCUS.POSTAL.CO.CODE` | `NorcusPostalCode_CoCode` | String |  |  |
| 26 | `NORCUS.POSTAL.DEPT.CODE` | `NorcusPostalCode_DeptCode` | String |  |  |
| 27 | `NORCUS.POSTAL.AUDITOR.CODE` | `NorcusPostalCode_AuditorCode` | String |  |  |
| 28 | `NORCUS.POSTAL.AUDIT.DATE.TIME` | `NorcusPostalCode_AuditDateTime` | String |  |  |
