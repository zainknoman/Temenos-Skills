# DIGITAL.KEYS — Table Schema

> Source: `INSERTS/I_F.DIGITAL.KEYS` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DK.CUSTOMER.ID` | `DigitalKeys_CustomerId` | TField |  | This field stores the ID of the CUSTOMER record. Validation Rules: 10 T24String characters. |
| 2 | `DK.PERSON.ENTITY.ID` | `DigitalKeys_PersonEntityId` | TField |  | This field stores the ID of the PERSON.ENTITY record. Validation Rules: 10 T24String characters. |
| 3 | `DK.ACCESS.TOKEN` | `DigitalKeys_AccessToken` | TField |  | This field stores the long term Access Token recived from the social media platform API. Validation Rules: Any 1000 characters. |
| 4 | `DK.DIGITAL.INFO.ID` | `DigitalKeys_DigitalInfoId` | TField |  | This field stores the ID of the DIGITAL.INFO record. Validation Rules: 16 string characters. |
| 5 | `DK.TOKEN.DATE` | `DigitalKeys_TokenDate` | TField |  | This field stores the date when the customer connected with bank� app using Social Media Login and approved the request for permissions. |
| 6 | `DK.TOKEN.EXP.DATE` | `DigitalKeys_TokenExpDate` | TField |  | This field stores the date when the long term access token expires. |
| 7 | `DK.MEDIA.TYPE` | `DigitalKeys_MediaType` | TField |  | This field stores the social media platform name. |
| 8 | `DK.DIGITAL.ID` | `DigitalKeys_DigitalId` | TField |  | This field stores the Digital ID received from the social media platform API. |
| 9 | `DK.SOCIAL.MEDIA.ID` | `DigitalKeys_SocialMediaId` | TField |  | This field stores the unique identifier associated with customer�s social media account which he/she shared with the bank. |
| 10 | `DK.RESERVED.5` | `DigitalKeys_Reserved5` | TField |  |  |
| 11 | `DK.RESERVED.4` | `DigitalKeys_Reserved4` | TField |  |  |
| 12 | `DK.RESERVED.3` | `DigitalKeys_Reserved3` | TField |  |  |
| 13 | `DK.RESERVED.2` | `DigitalKeys_Reserved2` | TField |  |  |
| 14 | `DK.RESERVED.1` | `DigitalKeys_Reserved1` | TField |  |  |
