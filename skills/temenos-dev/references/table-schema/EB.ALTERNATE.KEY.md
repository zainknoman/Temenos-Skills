# EB.ALTERNATE.KEY — Table Schema

> Source: `INSERTS/I_F.EB.ALTERNATE.KEY` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.ALT.KEY.ALT.KEY.MAX.LENGTH` | `EbAlternateKey_AltKeyMaxLength` | TField |  | This is a no input field that indicates the maximum length of all possible key fields. This can be of any length irrespective of the current key field length defined in the application program.This will allow the actual alternate value input to be accepted by the lowest level validation routines. ACCOUNT, CUSTOMER fields in applications will be resized to the length specified here. For SECTOR, INDUSTRY fields, length specified in MAX.LENGTH field in EB.OBJECT will be used for resizing. Validation Rules: System generated field |
| 2 | `EB.ALT.KEY.ALT.KEY.FIELD` | `EbAlternateKey_AltKeyField` |  |  |  |
| 3 | `EB.ALT.KEY.CONCAT.TYPE` | `EbAlternateKey_ConcatType` |  |  |  |
| 4 | `EB.ALT.KEY.ACCESS.METHOD` | `EbAlternateKey_AccessMethod` |  |  |  |
| 5 | `EB.ALT.KEY.UNIQUE` | `EbAlternateKey_Unique` |  |  |  |
| 6 | `EB.ALT.KEY.ENQUIRY` | `EbAlternateKey_Enquiry` |  |  |  |
| 7 | `EB.ALT.KEY.BUILD.ROUTINE` | `EbAlternateKey_BuildRoutine` |  |  |  |
| 8 | `EB.ALT.KEY.VALIDATION.RTN` | `EbAlternateKey_ValidationRtn` |  |  |  |
| 9 | `EB.ALT.KEY.UNIQUE.KEY.FIELD` | `EbAlternateKey_UniqueKeyField` |  |  |  |
| 10 | `EB.ALT.KEY.ALTERNATE.KEY.TABLE` | `EbAlternateKey_AlternateKeyTable` |  |  |  |
| 11 | `EB.ALT.KEY.USE.CLASSIFICATION` | `EbAlternateKey_UseClassification` |  |  |  |
| 12 | `EB.ALT.KEY.RESERVED.18` | `EbAlternateKey_Reserved18` |  |  |  |
| 13 | `EB.ALT.KEY.RESERVED.17` | `EbAlternateKey_Reserved17` |  |  |  |
| 14 | `EB.ALT.KEY.RESERVED.16` | `EbAlternateKey_Reserved16` |  |  |  |
| 15 | `EB.ALT.KEY.RESERVED.15` | `EbAlternateKey_Reserved15` |  |  |  |
| 16 | `EB.ALT.KEY.ENRI.FIELD` | `EbAlternateKey_EnriField` | A (alphanumeric) |  | On inputting a duplicate alternate key (multiple keys with the same alternate key) a drop down list with all the real keys that corresponds to that alternate key appears along with an enrichment for each key. This field specifies the field to be used for enrichment if the DEFAULT.ENRI field in STANDARD.SELECTION record is null. Validation Rules: 1 to 35 type A (alphanumeric) character field. The value entered, must be a valid field on the STANDARD.SELECTION record. |
| 17 | `EB.ALT.KEY.RESERVED.14` | `EbAlternateKey_Reserved14` | TField |  |  |
| 18 | `EB.ALT.KEY.RESERVED.13` | `EbAlternateKey_Reserved13` | TField |  |  |
| 19 | `EB.ALT.KEY.RESERVED.12` | `EbAlternateKey_Reserved12` | TField |  |  |
| 20 | `EB.ALT.KEY.RESERVED.11` | `EbAlternateKey_Reserved11` | TField |  |  |
| 21 | `EB.ALT.KEY.RESERVED.10` | `EbAlternateKey_Reserved10` | TField |  |  |
| 22 | `EB.ALT.KEY.RESERVED.9` | `EbAlternateKey_Reserved9` | TField |  |  |
| 23 | `EB.ALT.KEY.RESERVED.8` | `EbAlternateKey_Reserved8` | TField |  |  |
| 24 | `EB.ALT.KEY.RESERVED.7` | `EbAlternateKey_Reserved7` | TField |  |  |
| 25 | `EB.ALT.KEY.RESERVED.6` | `EbAlternateKey_Reserved6` | TField |  |  |
| 26 | `EB.ALT.KEY.RESERVED.5` | `EbAlternateKey_Reserved5` | TField |  |  |
| 27 | `EB.ALT.KEY.RESERVED.4` | `EbAlternateKey_Reserved4` | TField |  |  |
| 28 | `EB.ALT.KEY.RESERVED.3` | `EbAlternateKey_Reserved3` | TField |  |  |
| 29 | `EB.ALT.KEY.RESERVED.2` | `EbAlternateKey_Reserved2` | TField |  |  |
| 30 | `EB.ALT.KEY.RESERVED.1` | `EbAlternateKey_Reserved1` | TField |  |  |
| 31 | `EB.ALT.KEY.RECORD.STATUS` | `EbAlternateKey_RecordStatus` | String |  |  |
| 32 | `EB.ALT.KEY.CURR.NO` | `EbAlternateKey_CurrNo` | String |  |  |
| 33 | `EB.ALT.KEY.INPUTTER` | `EbAlternateKey_Inputter` |  |  |  |
| 34 | `EB.ALT.KEY.DATE.TIME` | `EbAlternateKey_DateTime` |  |  |  |
| 35 | `EB.ALT.KEY.AUTHORISER` | `EbAlternateKey_Authoriser` | String |  |  |
| 36 | `EB.ALT.KEY.CO.CODE` | `EbAlternateKey_CoCode` | String |  |  |
| 37 | `EB.ALT.KEY.DEPT.CODE` | `EbAlternateKey_DeptCode` | String |  |  |
| 38 | `EB.ALT.KEY.AUDITOR.CODE` | `EbAlternateKey_AuditorCode` | String |  |  |
| 39 | `EB.ALT.KEY.AUDIT.DATE.TIME` | `EbAlternateKey_AuditDateTime` | String |  |  |
