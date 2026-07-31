# SAAELM.RESPONSE — Table Schema

> Source: `INSERTS/I_F.SAAELM.RESPONSE` in `SAAELM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAAELM.RESP.SERVICE.NAME` | `SaaelmResponse_ServiceName` | TField |  | This field is to capture the Service Name which has to be triggered for getting the response.To be Validated against Template : SAAELM.SERVIVCE.NAME |
| 2 | `SAAELM.RESP.LEGAL.ID.NUM` | `SaaelmResponse_LegalIdNumber` |  |  |  |
| 3 | `SAAELM.RESP.BIRTH.DATE` | `SaaelmResponse_DateOfBirth` |  |  |  |
| 4 | `SAAELM.RESP.REF.NUMBER` | `SaaelmResponse_ReferenceNumber` |  |  |  |
| 5 | `SAAELM.RESP.NATIONALITY` | `SaaelmResponse_Nationality` | TField |  | Identifies the Nationality of the Customer.Can be upto 5 numeric characters. |
| 6 | `SAAELM.RESP.CHARGE.CODE` | `SaaelmResponse_ChargeCode` | A (alphanumeric) |  | Charge code is a static configured value = �PROD�.1-20 type A (alphanumeric) characters. |
| 7 | `SAAELM.RESP.ADDRESS.LANG` | `SaaelmResponse_AddressLanguage` |  |  |  |
| 8 | `SAAELM.RESP.FIRST.NAME` | `SaaelmResponse_FirstName` | A (alphanumeric) |  | Identifies the first name of the Customer. 1-20 type A (alphanumeric) characters. |
| 9 | `SAAELM.RESP.SECOND.NAME` | `SaaelmResponse_SecondName` | A (alphanumeric) |  | Identifies the second name of the Customer. 1-20 type A (alphanumeric) characters. |
| 10 | `SAAELM.RESP.THIRD.NAME` | `SaaelmResponse_ThirdName` | A (alphanumeric) |  | Identifies the third name of the Customer. 1-20 type A (alphanumeric) characters. |
| 11 | `SAAELM.RESP.LAST.NAME` | `SaaelmResponse_LastName` | A (alphanumeric) |  | Identifies the last name of the Customer. 1-20 type A (alphanumeric) characters. |
| 12 | `SAAELM.RESP.FATHER.NAME` | `SaaelmResponse_FatherName` | A (alphanumeric) |  | Identifies the Father's name of the Customer. 1-20 type A (alphanumeric) characters. |
| 13 | `SAAELM.RESP.GRANDFATHER.NAME` | `SaaelmResponse_GrandfatherName` | A (alphanumeric) |  | Identifies the Grand Father's name of the Customer. 1-20 type A (alphanumeric) characters. |
| 14 | `SAAELM.RESP.SUBTRIBE.NAME` | `SaaelmResponse_SubTribeName` |  |  |  |
| 15 | `SAAELM.RESP.NAME.FAMILY` | `SaaelmResponse_FamilyName` |  |  |  |
| 16 | `SAAELM.RESP.ENG.FIRST.NAME` | `SaaelmResponse_EnglishFirstName` |  |  |  |
| 17 | `SAAELM.RESP.ENG.SECOND.NAME` | `SaaelmResponse_EnglishSecondName` |  |  |  |
| 18 | `SAAELM.RESP.ENG.THIRD.NAME` | `SaaelmResponse_EnglishThirdName` |  |  |  |
| 19 | `SAAELM.RESP.ENG.LAST.NAME` | `SaaelmResponse_EnglishLastName` |  |  |  |
| 20 | `SAAELM.RESP.GENDER` | `SaaelmResponse_Gender` | TField |  | Identifies the Gender of the Customer. The values can be Male, Female or Undefined. |
| 21 | `SAAELM.RESP.PLACE.OF.BIRTH` | `SaaelmResponse_PlaceOfBirth` | A (alphanumeric) |  | Identifies the Place where the Customer was born. 1-25 type A (alphanumeric) characters. |
| 22 | `SAAELM.RESP.NATIONALITY.DES` | `SaaelmResponse_NationalityDescription` |  |  |  |
| 23 | `SAAELM.RESP.DOC.EXP.DATE` | `SaaelmResponse_LegalExpDate` |  |  |  |
| 24 | `SAAELM.RESP.DOC.EXP.DATE.HIJRI` | `SaaelmResponse_LegalExpDateHijri` |  |  |  |
| 25 | `SAAELM.RESP.BIRTH.DATE.HIJRI` | `SaaelmResponse_DateOfBirthInHijri` |  |  |  |
| 26 | `SAAELM.RESP.ADDITIONAL.NUM` | `SaaelmResponse_AdditionalNumber` |  |  |  |
| 27 | `SAAELM.RESP.BUILDING.NUM` | `SaaelmResponse_BuildingNumber` |  |  |  |
| 28 | `SAAELM.RESP.CITY` | `SaaelmResponse_City` |  |  |  |
| 29 | `SAAELM.RESP.DISTRICT` | `SaaelmResponse_District` |  |  |  |
| 30 | `SAAELM.RESP.PRIMARY.ADDRESS` | `SaaelmResponse_PrimaryAddress` |  |  |  |
| 31 | `SAAELM.RESP.LOCATION.COORDINATES` | `SaaelmResponse_LocationCoordinates` |  |  |  |
| 32 | `SAAELM.RESP.POST.CODE` | `SaaelmResponse_PostCode` |  |  |  |
| 33 | `SAAELM.RESP.STREET.NAME` | `SaaelmResponse_StreetName` |  |  |  |
| 34 | `SAAELM.RESP.UNIT.NUMBER` | `SaaelmResponse_UnitNumber` |  |  |  |
| 35 | `SAAELM.RESP.ERROR.CODE` | `SaaelmResponse_ErrorCode` | TField |  | In case of a faulty message error code will be sent by Yakeen which is captured in this field. 1-3 type Numeric characters. |
| 36 | `SAAELM.RESP.ERROR.MESSAGE` | `SaaelmResponse_ErrorMessage` | A (alphanumeric) |  | In case of a faulty message an Error Message will be sent along with error code by Yakeen which is captured in this field. 1-100 type A (alphanumeric) characters. |
| 37 | `SAAELM.RESP.ERROR.TYPE` | `SaaelmResponse_ErrorType` | A (alphanumeric) |  | In case of a faulty message Error Type will be sent along with error code and Message by Yakeen which is captured in this field.1-50 type A (alphanumeric) characters. |
| 38 | `SAAELM.RESP.NATIONALITY.CODE` | `SaaelmResponse_NationalityCode` | TField |  | Nationality Code received as response |
| 39 | `SAAELM.RESP.BIRTH.DATE.G` | `SaaelmResponse_DateOfBirthG` |  |  |  |
| 40 | `SAAELM.RESP.LOG.ID` | `SaaelmResponse_LogId` | A (alphanumeric) |  | This field holds the Log Id received in response.1-20 type A (alphanumeric) characters. |
| 41 | `SAAELM.RESP.RESERVED.1` | `SaaelmResponse_Reserved1` | TField |  |  |
| 42 | `SAAELM.RESP.RESERVED.2` | `SaaelmResponse_Reserved2` | TField |  |  |
| 43 | `SAAELM.RESP.RESERVED.3` | `SaaelmResponse_Reserved3` | TField |  |  |
| 44 | `SAAELM.RESP.RESERVED.4` | `SaaelmResponse_Reserved4` | TField |  |  |
| 45 | `SAAELM.RESP.RESERVED.5` | `SaaelmResponse_Reserved5` | TField |  |  |
| 46 | `SAAELM.RESP.RESERVED.6` | `SaaelmResponse_Reserved6` | TField |  |  |
| 47 | `SAAELM.RESP.RESERVED.7` | `SaaelmResponse_Reserved7` | TField |  |  |
| 48 | `SAAELM.RESP.RESERVED.8` | `SaaelmResponse_Reserved8` | TField |  |  |
| 49 | `SAAELM.RESP.RESERVED.9` | `SaaelmResponse_Reserved9` | TField |  |  |
| 50 | `SAAELM.RESP.RESERVED.10` | `SaaelmResponse_Reserved10` | TField |  |  |
| 51 | `SAAELM.RESP.RECORD.STATUS` | `SaaelmResponse_RecordStatus` | String |  |  |
| 52 | `SAAELM.RESP.CURR.NO` | `SaaelmResponse_CurrNo` | String |  |  |
| 53 | `SAAELM.RESP.INPUTTER` | `SaaelmResponse_Inputter` |  |  |  |
| 54 | `SAAELM.RESP.DATE.TIME` | `SaaelmResponse_DateTime` |  |  |  |
| 55 | `SAAELM.RESP.AUTHORISER` | `SaaelmResponse_Authoriser` | String |  |  |
| 56 | `SAAELM.RESP.CO.CODE` | `SaaelmResponse_CoCode` | String |  |  |
| 57 | `SAAELM.RESP.DEPT.CODE` | `SaaelmResponse_DeptCode` | String |  |  |
| 58 | `SAAELM.RESP.AUDITOR.CODE` | `SaaelmResponse_AuditorCode` | String |  |  |
| 59 | `SAAELM.RESP.AUDIT.DATE.TIME` | `SaaelmResponse_AuditDateTime` | String |  |  |
