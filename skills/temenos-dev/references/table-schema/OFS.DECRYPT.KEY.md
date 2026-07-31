# OFS.DECRYPT.KEY — Table Schema

> Source: `INSERTS/I_F.OFS.DECRYPT.KEY` in `EB_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OF.DECR.DESCRIPTION` | `OfsDecryptKey_Description` |  |  |  |
| 2 | `OF.DECR.MSG.DECRYPT.KEY` | `OfsDecryptKey_MsgDecryptKey` | TField | No | MESSAGE.DECRYPT.KEY holds the Decryption Key (which is same as that used for Encryption). Validation Rules: 1. An optional Field 2. Length: Maximum of 50 |
| 3 | `OF.DECR.CIPHER.METHOD` | `OfsDecryptKey_CipherMethod` | TField |  | CIPHER.METHOD should have a list of methods supported by JBase decrypt command picked up from EB.LOOKUP list. User needs to specify the cipher method with "." instead of "_". T24 will convert back to "_". e.g. "JBASE_CRYPT_RC2" should be specified as "JBASE.CRYPT.RC2" Validation Rules: 1. Has specified options - JBASE.CRYPT.GENERAL, JBASE.CRYPT.ROT13, JBASE.CRYPT.XOR11, JBASE.CRYPT.RC2, JBASE.CRYPT.BASE64, JBASE.CRYPT.DES, JBASE.CRYPT.3DES, JBASE.CRYPT.BLOWFISH, JBASE.CRYPT.BASE64.MASK, JBASE.CRYPT.RC2.BASE64, JBASE.CRYPT.DES.BASE64, JBASE.CRYPT.3DES.BASE64, JBASE.CRYPT.BLOWFISH.BASE64 2. Has a default value of "JBASE.CRYPT.GENERAL" 3. Need not specify a MESSAGE.DECRYPT.KEY if the CIPHER.METHOD is "JBASE.CRYPT.ROT13" |
| 4 | `OF.DECR.RESERVED.10` | `OfsDecryptKey_Reserved10` | TField |  |  |
| 5 | `OF.DECR.RESERVED.9` | `OfsDecryptKey_Reserved9` | TField |  |  |
| 6 | `OF.DECR.RESERVED.8` | `OfsDecryptKey_Reserved8` | TField |  |  |
| 7 | `OF.DECR.RESERVED.7` | `OfsDecryptKey_Reserved7` | TField |  |  |
| 8 | `OF.DECR.RESERVED.6` | `OfsDecryptKey_Reserved6` | TField |  |  |
| 9 | `OF.DECR.RESERVED.5` | `OfsDecryptKey_Reserved5` | TField |  |  |
| 10 | `OF.DECR.RESERVED.4` | `OfsDecryptKey_Reserved4` | TField |  |  |
| 11 | `OF.DECR.RESERVED.3` | `OfsDecryptKey_Reserved3` | TField |  |  |
| 12 | `OF.DECR.RESERVED.2` | `OfsDecryptKey_Reserved2` | TField |  |  |
| 13 | `OF.DECR.RESERVED.1` | `OfsDecryptKey_Reserved1` | TField |  |  |
| 14 | `OF.DECR.LOCAL.REF` | `OfsDecryptKey_LocalRef` |  |  |  |
| 15 | `OF.DECR.OVERRIDE` | `OfsDecryptKey_Override` |  |  |  |
| 16 | `OF.DECR.RECORD.STATUS` | `OfsDecryptKey_RecordStatus` | String |  |  |
| 17 | `OF.DECR.CURR.NO` | `OfsDecryptKey_CurrNo` | String |  |  |
| 18 | `OF.DECR.INPUTTER` | `OfsDecryptKey_Inputter` |  |  |  |
| 19 | `OF.DECR.DATE.TIME` | `OfsDecryptKey_DateTime` |  |  |  |
| 20 | `OF.DECR.AUTHORISER` | `OfsDecryptKey_Authoriser` | String |  |  |
| 21 | `OF.DECR.CO.CODE` | `OfsDecryptKey_CoCode` | String |  |  |
| 22 | `OF.DECR.DEPT.CODE` | `OfsDecryptKey_DeptCode` | String |  |  |
| 23 | `OF.DECR.AUDITOR.CODE` | `OfsDecryptKey_AuditorCode` | String |  |  |
| 24 | `OF.DECR.AUDIT.DATE.TIME` | `OfsDecryptKey_AuditDateTime` | String |  |  |
