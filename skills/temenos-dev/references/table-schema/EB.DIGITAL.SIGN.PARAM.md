# EB.DIGITAL.SIGN.PARAM — Table Schema

> Source: `INSERTS/I_F.EB.DIGITAL.SIGN.PARAM` in `EB_Security.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DGL.SGR.DESCRIPTION` | `EbDigitalSignParam_Description` |  |  |  |
| 2 | `DGL.SGR.DS.DATA.RULE` | `EbDigitalSignParam_DsDataRule` |  |  |  |
| 3 | `DGL.SGR.DS.USER.DECRYPT.KEY` | `EbDigitalSignParam_DsUserDecryptKey` | TField | Yes | EB.API hook routine to fetch user's public key for decrypting the digital signature which comes from front end through IRIS for a transaction request. This field is enabled only for "SYSTEM" record. Accepts Two arguments. 1. Incoming argument - current user id. 2. Outgoing argument - is an array of value, first position to hold user's public key for digital signature verification. Validation Rules: Mandatory field for SYSTEM record. |
| 4 | `DGL.SGR.CIPHER.METHOD` | `EbDigitalSignParam_CipherMethod` | TField | Yes | To specify an Algorithm to be used for digital signature signing (by front end) and verification (at t24 layer). Input allowed only for SYSTEM record. This field accepts list of valid names pre-defined in field property and T24 will convert it into equivalent algorithm name (during run time) for digital signature verification. i.e Input value = GENERAL , real algorithm name = JBASE_CRYPT_GENERAL. Validation Rules: Mandatory field for SYSTEM record. Valid values are: GENERAL, XOR11, RC2, DES, 3DES, BLOWFISH, AES-BASE64, RC2-BASE64, DES-BASE64, 3DES-BASE64, BLOWFISH-BASE64 NOCHANGE field. |
| 5 | `DGL.SGR.RESERVED.5` | `EbDigitalSignParam_Reserved5` | TField |  |  |
| 6 | `DGL.SGR.RESERVED.4` | `EbDigitalSignParam_Reserved4` | TField |  |  |
| 7 | `DGL.SGR.RESERVED.3` | `EbDigitalSignParam_Reserved3` | TField |  |  |
| 8 | `DGL.SGR.RESERVED.2` | `EbDigitalSignParam_Reserved2` | TField |  |  |
| 9 | `DGL.SGR.RESERVED.1` | `EbDigitalSignParam_Reserved1` | TField |  |  |
| 10 | `DGL.SGR.RECORD.STATUS` | `EbDigitalSignParam_RecordStatus` | String |  |  |
| 11 | `DGL.SGR.CURR.NO` | `EbDigitalSignParam_CurrNo` | String |  |  |
| 12 | `DGL.SGR.INPUTTER` | `EbDigitalSignParam_Inputter` |  |  |  |
| 13 | `DGL.SGR.DATE.TIME` | `EbDigitalSignParam_DateTime` |  |  |  |
| 14 | `DGL.SGR.AUTHORISER` | `EbDigitalSignParam_Authoriser` | String |  |  |
| 15 | `DGL.SGR.CO.CODE` | `EbDigitalSignParam_CoCode` | String |  |  |
| 16 | `DGL.SGR.DEPT.CODE` | `EbDigitalSignParam_DeptCode` | String |  |  |
| 17 | `DGL.SGR.AUDITOR.CODE` | `EbDigitalSignParam_AuditorCode` | String |  |  |
| 18 | `DGL.SGR.AUDIT.DATE.TIME` | `EbDigitalSignParam_AuditDateTime` | String |  |  |
