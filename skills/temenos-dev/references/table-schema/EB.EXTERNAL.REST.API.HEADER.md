# EB.EXTERNAL.REST.API.HEADER — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.REST.API.HEADER` in `BE_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.REST.DESCRIPTION` | `EbExternalRestApiHeader_Description` |  |  |  |
| 2 | `EXT.REST.URL` | `EbExternalRestApiHeader_Url` | TField |  | This allows to defines URL for the external request. |
| 3 | `EXT.REST.METHODS` | `EbExternalRestApiHeader_Methods` | TField |  | Specifies the type of METHOD to be performed for the request. GET: The GET method is used to retrieve information. PUT: Replaces all current representations of the target resource with the uploaded content. POST: A POST request is used to send data to the external system DELETE: Removes all current representations of the target resource given in the request PATCH: It is used to make minor updates to target resources |
| 4 | `EXT.REST.API.NAME` | `EbExternalRestApiHeader_ApiName` | TField |  | REST APIs should be define and through this only sending payload information to invoke external request Validation Rules: Valid entry in EB.API application. |
| 5 | `EXT.REST.USER.NAME` | `EbExternalRestApiHeader_UserName` | TField |  | Identifies details of the user. |
| 6 | `EXT.REST.PASSWORD` | `EbExternalRestApiHeader_Password` | TField |  | Stores the User's secret Password. |
| 7 | `EXT.REST.RESET.PASSWORD` | `EbExternalRestApiHeader_ResetPassword` | TField |  | If a User has forgotten his secret Password, we can be reset password using this field. |
| 8 | `EXT.REST.HEADER.NAME` | `EbExternalRestApiHeader_HeaderName` |  |  |  |
| 9 | `EXT.REST.HEADER.VALUE` | `EbExternalRestApiHeader_HeaderValue` |  |  |  |
| 10 | `EXT.REST.RESERVEDFLD.6` | `EbExternalRestApiHeader_Reservedfld6` |  |  |  |
| 11 | `EXT.REST.RESERVEDFLD.5` | `EbExternalRestApiHeader_Reservedfld5` |  |  |  |
| 12 | `EXT.REST.RESERVEDFLD.4` | `EbExternalRestApiHeader_Reservedfld4` |  |  |  |
| 13 | `EXT.REST.RESERVEDFLD.3` | `EbExternalRestApiHeader_Reservedfld3` |  |  |  |
| 14 | `EXT.REST.RESERVEDFLD.2` | `EbExternalRestApiHeader_Reservedfld2` |  |  |  |
| 15 | `EXT.REST.RESERVEDFLD.1` | `EbExternalRestApiHeader_Reservedfld1` |  |  |  |
| 16 | `EXT.REST.RESERVED.10` | `EbExternalRestApiHeader_Reserved10` |  |  |  |
| 17 | `EXT.REST.RESERVED.9` | `EbExternalRestApiHeader_Reserved9` | TField |  |  |
| 18 | `EXT.REST.RESERVED.8` | `EbExternalRestApiHeader_Reserved8` | TField |  |  |
| 19 | `EXT.REST.RESERVED.7` | `EbExternalRestApiHeader_Reserved7` | TField |  |  |
| 20 | `EXT.REST.RESERVED.6` | `EbExternalRestApiHeader_Reserved6` | TField |  |  |
| 21 | `EXT.REST.RESERVED.5` | `EbExternalRestApiHeader_Reserved5` | TField |  |  |
| 22 | `EXT.REST.RESERVED.4` | `EbExternalRestApiHeader_Reserved4` | TField |  |  |
| 23 | `EXT.REST.RESERVED.3` | `EbExternalRestApiHeader_Reserved3` | TField |  |  |
| 24 | `EXT.REST.RESERVED.2` | `EbExternalRestApiHeader_Reserved2` | TField |  |  |
| 25 | `EXT.REST.RESERVED.1` | `EbExternalRestApiHeader_Reserved1` | TField |  |  |
| 26 | `EXT.REST.LOCAL.REF` | `EbExternalRestApiHeader_LocalRef` |  |  |  |
| 27 | `EXT.REST.OVERRIDE` | `EbExternalRestApiHeader_Override` |  |  |  |
| 28 | `EXT.REST.RECORD.STATUS` | `EbExternalRestApiHeader_RecordStatus` | String |  |  |
| 29 | `EXT.REST.CURR.NO` | `EbExternalRestApiHeader_CurrNo` | String |  |  |
| 30 | `EXT.REST.INPUTTER` | `EbExternalRestApiHeader_Inputter` |  |  |  |
| 31 | `EXT.REST.DATE.TIME` | `EbExternalRestApiHeader_DateTime` |  |  |  |
| 32 | `EXT.REST.AUTHORISER` | `EbExternalRestApiHeader_Authoriser` | String |  |  |
| 33 | `EXT.REST.CO.CODE` | `EbExternalRestApiHeader_CoCode` | String |  |  |
| 34 | `EXT.REST.DEPT.CODE` | `EbExternalRestApiHeader_DeptCode` | String |  |  |
| 35 | `EXT.REST.AUDITOR.CODE` | `EbExternalRestApiHeader_AuditorCode` | String |  |  |
| 36 | `EXT.REST.AUDIT.DATE.TIME` | `EbExternalRestApiHeader_AuditDateTime` | String |  |  |
