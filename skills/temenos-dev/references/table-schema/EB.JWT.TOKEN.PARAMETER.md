# EB.JWT.TOKEN.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.JWT.TOKEN.PARAMETER` in `EB_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.JTP.DESCRIPTION` | `EbJwtTokenParameter_Description` |  |  |  |
| 2 | `EB.JTP.ALGORITHM` | `EbJwtTokenParameter_Algorithm` | TField |  | This is the field to attach the algorithm that must be used to decode a JWT Validation Rules: A default RS256 is supported by the product out of box. New algorithm can be added by extending the virtual list using EB.LOOKUP with the pattern JWT.ALGORITHM. |
| 3 | `EB.JTP.PUBLIC.KEY` | `EbJwtTokenParameter_PublicKey` | TField | Yes | A text field to store the public key which is used for validating JWT Validation Rules: There is a free text field with no validation in Transact It can have maximum of 200 characters Atleast one of the three- PUBLIC.KEY, CERTIFICATE.FILE.PATH, JWK.URI is mandatory |
| 4 | `EB.JTP.CERTIFICATE.FILE.PATH` | `EbJwtTokenParameter_CertificateFilePath` | TField | Yes | This holds the path to actual certificate file Validation Rules: There is a free text field with no validation in Transact It can have maximum of 200 characters Atleast one of the three- PUBLIC.KEY, CERTIFICATE.FILE.PATH, JWK.URI is mandatory |
| 5 | `EB.JTP.JWK.URI` | `EbJwtTokenParameter_JwkUri` | TField | Yes | The URI would be hit were the certificate is placed Validation Rules: There is a free text field with no validation in Transact It can have maximum of 200 characters Atleast one of the three- PUBLIC.KEY, CERTIFICATE.FILE.PATH, JWK.URI is mandatory |
| 6 | `EB.JTP.USER.MAPPING` | `EbJwtTokenParameter_UserMapping` |  |  |  |
| 7 | `EB.JTP.PAYLOAD.ATTRIBUTE.NAME` | `EbJwtTokenParameter_PayloadAttributeName` |  |  |  |
| 8 | `EB.JTP.USER.MAPPING.NO` | `EbJwtTokenParameter_UserMappingNo` |  |  |  |
| 9 | `EB.JTP.DEFAULT.VALUE` | `EbJwtTokenParameter_DefaultValue` |  |  |  |
| 10 | `EB.JTP.ATTRIBUTES` | `EbJwtTokenParameter_Attributes` |  |  |  |
| 11 | `EB.JTP.RESERVED.10` | `EbJwtTokenParameter_Reserved10` | TField |  |  |
| 12 | `EB.JTP.RESERVED.9` | `EbJwtTokenParameter_Reserved9` | TField |  |  |
| 13 | `EB.JTP.RESERVED.8` | `EbJwtTokenParameter_Reserved8` | TField |  |  |
| 14 | `EB.JTP.RESERVED.7` | `EbJwtTokenParameter_Reserved7` | TField |  |  |
| 15 | `EB.JTP.RESERVED.6` | `EbJwtTokenParameter_Reserved6` | TField |  |  |
| 16 | `EB.JTP.RESERVED.5` | `EbJwtTokenParameter_Reserved5` | TField |  |  |
| 17 | `EB.JTP.RESERVED.4` | `EbJwtTokenParameter_Reserved4` | TField |  |  |
| 18 | `EB.JTP.RESERVED.3` | `EbJwtTokenParameter_Reserved3` | TField |  |  |
| 19 | `EB.JTP.RESERVED.2` | `EbJwtTokenParameter_Reserved2` | TField |  |  |
| 20 | `EB.JTP.RESERVED.1` | `EbJwtTokenParameter_Reserved1` | TField |  |  |
| 21 | `EB.JTP.LOCAL.REF` | `EbJwtTokenParameter_LocalRef` |  |  |  |
| 22 | `EB.JTP.OVERRIDE` | `EbJwtTokenParameter_Override` |  |  |  |
| 23 | `EB.JTP.RECORD.STATUS` | `EbJwtTokenParameter_RecordStatus` | String |  |  |
| 24 | `EB.JTP.CURR.NO` | `EbJwtTokenParameter_CurrNo` | String |  |  |
| 25 | `EB.JTP.INPUTTER` | `EbJwtTokenParameter_Inputter` |  |  |  |
| 26 | `EB.JTP.DATE.TIME` | `EbJwtTokenParameter_DateTime` |  |  |  |
| 27 | `EB.JTP.AUTHORISER` | `EbJwtTokenParameter_Authoriser` | String |  |  |
| 28 | `EB.JTP.CO.CODE` | `EbJwtTokenParameter_CoCode` | String |  |  |
| 29 | `EB.JTP.DEPT.CODE` | `EbJwtTokenParameter_DeptCode` | String |  |  |
| 30 | `EB.JTP.AUDITOR.CODE` | `EbJwtTokenParameter_AuditorCode` | String |  |  |
| 31 | `EB.JTP.AUDIT.DATE.TIME` | `EbJwtTokenParameter_AuditDateTime` | String |  |  |
