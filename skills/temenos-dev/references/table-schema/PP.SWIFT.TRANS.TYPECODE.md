# PP.SWIFT.TRANS.TYPECODE — Table Schema

> Source: `INSERTS/I_F.PP.SWIFT.TRANS.TYPECODE` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.STC.SWIFTTransactionTypeCode` | `PpSwiftTransTypecode_Swifttransactiontypecode` | TField |  | Represents the SWIFT Transaction Type Code to be reported in MT940 for Tag 61. Validation Rules: 4 Alphanumeric characters. |
| 2 | `PP.STC.RESERVED.5` | `PpSwiftTransTypecode_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 3 | `PP.STC.RESERVED.4` | `PpSwiftTransTypecode_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.STC.RESERVED.3` | `PpSwiftTransTypecode_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.STC.RESERVED.2` | `PpSwiftTransTypecode_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.STC.RESERVED.1` | `PpSwiftTransTypecode_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.STC.LOCAL.REF` | `PpSwiftTransTypecode_LocalRef` |  |  |  |
| 8 | `PP.STC.OVERRIDE` | `PpSwiftTransTypecode_Override` |  |  |  |
| 9 | `PP.STC.RECORD.STATUS` | `PpSwiftTransTypecode_RecordStatus` | String |  |  |
| 10 | `PP.STC.CURR.NO` | `PpSwiftTransTypecode_CurrNo` | String |  |  |
| 11 | `PP.STC.INPUTTER` | `PpSwiftTransTypecode_Inputter` |  |  |  |
| 12 | `PP.STC.DATE.TIME` | `PpSwiftTransTypecode_DateTime` |  |  |  |
| 13 | `PP.STC.AUTHORISER` | `PpSwiftTransTypecode_Authoriser` | String |  |  |
| 14 | `PP.STC.CO.CODE` | `PpSwiftTransTypecode_CoCode` | String |  |  |
| 15 | `PP.STC.DEPT.CODE` | `PpSwiftTransTypecode_DeptCode` | String |  |  |
| 16 | `PP.STC.AUDITOR.CODE` | `PpSwiftTransTypecode_AuditorCode` | String |  |  |
| 17 | `PP.STC.AUDIT.DATE.TIME` | `PpSwiftTransTypecode_AuditDateTime` | String |  |  |
