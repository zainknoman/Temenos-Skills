# DIGITAL.INTERFACE — Table Schema

> Source: `INSERTS/I_F.DIGITAL.INTERFACE` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DGI.CUSTOMER.ID` | `DigitalInterface_CustomerId` | TField |  | This field stores the ID of the CUSTOMER record. Validation Rules: 10 T24String characters. |
| 2 | `DGI.PERSON.ENTITY.ID` | `DigitalInterface_PersonEntityId` | TField |  | This field stores the ID of the PERSON.ENTITY record. Validation Rules: 10 T24String characters. |
| 3 | `DGI.MEDIA.TYPE` | `DigitalInterface_MediaType` | TField |  | This field stores the social media platform name. Validation Rules: 35 string characters.NOINPUT field. |
| 4 | `DGI.DIGITAL.ID` | `DigitalInterface_DigitalId` | TField |  | This field stores the Digital ID recived from the social media platform API. Validation Rules: Any 1000 characters.NOINPUT field. |
| 5 | `DGI.ACCESS.TOKEN` | `DigitalInterface_AccessToken` | TField |  | This field stores the long term Access Token recived from the social media platform API. Validation Rules: Any 1000 characters. |
| 6 | `DGI.LOGIN.NAME` | `DigitalInterface_LoginName` | TField |  | This field stores the username used to login on the social media platform. Validation Rules: 35 string characters. |
| 7 | `DGI.USER.DEVICE.NAME` | `DigitalInterface_UserDeviceName` | TField |  | This field stores the alias assigned by the social media platform. Validation Rules: Any 50 characters. |
| 8 | `DGI.LINK.PROFILE` | `DigitalInterface_LinkProfile` | TField |  | This field stores whether the customer wants to link or unlink social media account.Values: Y/N. Validation Rules: 1 string character. |
| 9 | `DGI.SOCIAL.MEDIA.ID` | `DigitalInterface_SocialMediaId` | TField |  | This field stores the unique identifier associated with customer�s social media account which he/she shared with the bank. |
| 10 | `DGI.TOKEN.DATE` | `DigitalInterface_TokenDate` | TField |  | This field stores the date when the customer connected with bank� app using Social Media Login and approved the request for permissions. |
| 11 | `DGI.TOKEN.EXP.DATE` | `DigitalInterface_TokenExpDate` | TField |  | This field stores the date when the long term access token expires. |
| 12 | `DGI.RESERVED.7` | `DigitalInterface_Reserved7` | TField |  |  |
| 13 | `DGI.RESERVED.6` | `DigitalInterface_Reserved6` | TField |  |  |
| 14 | `DGI.RESERVED.5` | `DigitalInterface_Reserved5` | TField |  |  |
| 15 | `DGI.RESERVED.4` | `DigitalInterface_Reserved4` | TField |  |  |
| 16 | `DGI.RESERVED.3` | `DigitalInterface_Reserved3` | TField |  |  |
| 17 | `DGI.RESERVED.2` | `DigitalInterface_Reserved2` | TField |  |  |
| 18 | `DGI.RESERVED.1` | `DigitalInterface_Reserved1` | TField |  |  |
| 19 | `DGI.LOCAL.REF` | `DigitalInterface_LocalRef` |  |  |  |
| 20 | `DGI.OVERRIDE` | `DigitalInterface_Override` |  |  |  |
| 21 | `DGI.RECORD.STATUS` | `DigitalInterface_RecordStatus` | String |  |  |
| 22 | `DGI.CURR.NO` | `DigitalInterface_CurrNo` | String |  |  |
| 23 | `DGI.INPUTTER` | `DigitalInterface_Inputter` |  |  |  |
| 24 | `DGI.DATE.TIME` | `DigitalInterface_DateTime` |  |  |  |
| 25 | `DGI.AUTHORISER` | `DigitalInterface_Authoriser` | String |  |  |
| 26 | `DGI.CO.CODE` | `DigitalInterface_CoCode` | String |  |  |
| 27 | `DGI.DEPT.CODE` | `DigitalInterface_DeptCode` | String |  |  |
| 28 | `DGI.AUDITOR.CODE` | `DigitalInterface_AuditorCode` | String |  |  |
| 29 | `DGI.AUDIT.DATE.TIME` | `DigitalInterface_AuditDateTime` | String |  |  |
