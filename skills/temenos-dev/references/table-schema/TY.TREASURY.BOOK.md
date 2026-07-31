# TY.TREASURY.BOOK — Table Schema

> Source: `INSERTS/I_F.TY.TREASURY.BOOK` in `TY_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.TRES.BOOK.BOOK.NAME` | `TyTreasuryBook_BookName` | TField | Yes | Specifies the name given for the book created which will be identified along with the record ID of the application. Validation rules: Standard T24 Alphanumeric field Mandatory field. |
| 2 | `TY.TRES.BOOK.BOOK.DESCRIPTION` | `TyTreasuryBook_BookDescription` | TField | Yes | This field holds the description of the book. Validation rules: Standard T24 Alphanumeric field Mandatory field. |
| 3 | `TY.TRES.BOOK.APPLICATION.NAME` | `TyTreasuryBook_ApplicationName` |  |  |  |
| 4 | `TY.TRES.BOOK.APPL.FIELD` | `TyTreasuryBook_ApplField` |  |  |  |
| 5 | `TY.TRES.BOOK.APPL.CRITERIA` | `TyTreasuryBook_ApplCriteria` |  |  |  |
| 6 | `TY.TRES.BOOK.FIELD.VALUE` | `TyTreasuryBook_FieldValue` |  |  |  |
| 7 | `TY.TRES.BOOK.PROCESS.STATUS` | `TyTreasuryBook_ProcessStatus` | TField |  | This field denotes if the newly created record or an amended record is processed i.e., if the service requires this record to be picked up for processing to create portfolio. This field defaults to No whenever a record is created, or an existing record is amended. Validation rules: Allowed values are Yes or No. |
| 8 | `TY.TRES.BOOK.RESERVED.10` | `TyTreasuryBook_Reserved10` | TField |  |  |
| 9 | `TY.TRES.BOOK.RESERVED.9` | `TyTreasuryBook_Reserved9` | TField |  |  |
| 10 | `TY.TRES.BOOK.RESERVED.8` | `TyTreasuryBook_Reserved8` | TField |  |  |
| 11 | `TY.TRES.BOOK.RESERVED.7` | `TyTreasuryBook_Reserved7` | TField |  |  |
| 12 | `TY.TRES.BOOK.RESERVED.6` | `TyTreasuryBook_Reserved6` | TField |  |  |
| 13 | `TY.TRES.BOOK.RESERVED.5` | `TyTreasuryBook_Reserved5` | TField |  |  |
| 14 | `TY.TRES.BOOK.RESERVED.4` | `TyTreasuryBook_Reserved4` | TField |  |  |
| 15 | `TY.TRES.BOOK.RESERVED.3` | `TyTreasuryBook_Reserved3` | TField |  |  |
| 16 | `TY.TRES.BOOK.RESERVED.2` | `TyTreasuryBook_Reserved2` | TField |  |  |
| 17 | `TY.TRES.BOOK.RESERVED.1` | `TyTreasuryBook_Reserved1` | TField |  |  |
| 18 | `TY.TRES.BOOK.LOCAL.REF` | `TyTreasuryBook_LocalRef` |  |  |  |
| 19 | `TY.TRES.BOOK.OVERRIDE` | `TyTreasuryBook_Override` |  |  |  |
| 20 | `TY.TRES.BOOK.RECORD.STATUS` | `TyTreasuryBook_RecordStatus` | String |  |  |
| 21 | `TY.TRES.BOOK.CURR.NO` | `TyTreasuryBook_CurrNo` | String |  |  |
| 22 | `TY.TRES.BOOK.INPUTTER` | `TyTreasuryBook_Inputter` |  |  |  |
| 23 | `TY.TRES.BOOK.DATE.TIME` | `TyTreasuryBook_DateTime` |  |  |  |
| 24 | `TY.TRES.BOOK.AUTHORISER` | `TyTreasuryBook_Authoriser` | String |  |  |
| 25 | `TY.TRES.BOOK.CO.CODE` | `TyTreasuryBook_CoCode` | String |  |  |
| 26 | `TY.TRES.BOOK.DEPT.CODE` | `TyTreasuryBook_DeptCode` | String |  |  |
| 27 | `TY.TRES.BOOK.AUDITOR.CODE` | `TyTreasuryBook_AuditorCode` | String |  |  |
| 28 | `TY.TRES.BOOK.AUDIT.DATE.TIME` | `TyTreasuryBook_AuditDateTime` | String |  |  |
