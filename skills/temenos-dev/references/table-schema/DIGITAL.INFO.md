# DIGITAL.INFO — Table Schema

> Source: `INSERTS/I_F.DIGITAL.INFO` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DG.CUSTOMER.ID` | `DigitalInfo_CustomerId` | TField |  | This field stores the ID of the CUSTOMER record. Validation Rules: 10 T24String characters. |
| 2 | `DG.PERSON.ENTITY.ID` | `DigitalInfo_PersonEntityId` | TField |  | This field stores the ID of the PERSON.ENTITY record. Validation Rules: 10 T24String characters. |
| 3 | `DG.MEDIA.TYPE` | `DigitalInfo_MediaType` |  |  |  |
| 4 | `DG.DIGITAL.ID` | `DigitalInfo_DigitalId` |  |  |  |
| 5 | `DG.ACCESS.TOKEN` | `DigitalInfo_AccessToken` |  |  |  |
| 6 | `DG.DIGITAL.KEY` | `DigitalInfo_DigitalKey` |  |  |  |
| 7 | `DG.LOGIN.NAME` | `DigitalInfo_LoginName` |  |  |  |
| 8 | `DG.USER.DEVICE.NAME` | `DigitalInfo_UserDeviceName` |  |  |  |
| 9 | `DG.SOCIAL.MEDIA.ID` | `DigitalInfo_SocialMediaId` |  |  |  |
| 10 | `DG.TOKEN.DATE` | `DigitalInfo_TokenDate` |  |  |  |
| 11 | `DG.TOKEN.EXP.DATE` | `DigitalInfo_TokenExpDate` |  |  |  |
| 12 | `DG.RESERVED.7` | `DigitalInfo_Reserved7` | TField |  |  |
| 13 | `DG.RESERVED.6` | `DigitalInfo_Reserved6` | TField |  |  |
| 14 | `DG.RESERVED.5` | `DigitalInfo_Reserved5` | TField |  |  |
| 15 | `DG.RESERVED.4` | `DigitalInfo_Reserved4` | TField |  |  |
| 16 | `DG.RESERVED.3` | `DigitalInfo_Reserved3` | TField |  |  |
| 17 | `DG.RESERVED.2` | `DigitalInfo_Reserved2` | TField |  |  |
| 18 | `DG.RESERVED.1` | `DigitalInfo_Reserved1` | TField |  |  |
| 19 | `DG.LOCAL.REF` | `DigitalInfo_LocalRef` |  |  |  |
| 20 | `DG.OVERRIDE` | `DigitalInfo_Override` |  |  |  |
| 21 | `DG.RECORD.STATUS` | `DigitalInfo_RecordStatus` | String |  |  |
| 22 | `DG.CURR.NO` | `DigitalInfo_CurrNo` | String |  |  |
| 23 | `DG.INPUTTER` | `DigitalInfo_Inputter` |  |  |  |
| 24 | `DG.DATE.TIME` | `DigitalInfo_DateTime` |  |  |  |
| 25 | `DG.AUTHORISER` | `DigitalInfo_Authoriser` | String |  |  |
| 26 | `DG.CO.CODE` | `DigitalInfo_CoCode` | String |  |  |
| 27 | `DG.DEPT.CODE` | `DigitalInfo_DeptCode` | String |  |  |
| 28 | `DG.AUDITOR.CODE` | `DigitalInfo_AuditorCode` | String |  |  |
| 29 | `DG.AUDIT.DATE.TIME` | `DigitalInfo_AuditDateTime` | String |  |  |
