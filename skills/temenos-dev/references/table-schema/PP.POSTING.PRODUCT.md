# PP.POSTING.PRODUCT — Table Schema

> Source: `INSERTS/I_F.PP.POSTING.PRODUCT` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.POP.CompanyID` | `PpPostingProduct_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.POP.Description` | `PpPostingProduct_Description` |  |  |  |
| 3 | `PP.POP.RESERVED.5` | `PpPostingProduct_Reserved5` |  |  |  |
| 4 | `PP.POP.RESERVED.4` | `PpPostingProduct_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.POP.RESERVED.3` | `PpPostingProduct_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.POP.RESERVED.2` | `PpPostingProduct_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.POP.RESERVED.1` | `PpPostingProduct_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.POP.LOCAL.REF` | `PpPostingProduct_LocalRef` |  |  |  |
| 9 | `PP.POP.OVERRIDE` | `PpPostingProduct_Override` |  |  |  |
| 10 | `PP.POP.RECORD.STATUS` | `PpPostingProduct_RecordStatus` | String |  |  |
| 11 | `PP.POP.CURR.NO` | `PpPostingProduct_CurrNo` | String |  |  |
| 12 | `PP.POP.INPUTTER` | `PpPostingProduct_Inputter` |  |  |  |
| 13 | `PP.POP.DATE.TIME` | `PpPostingProduct_DateTime` |  |  |  |
| 14 | `PP.POP.AUTHORISER` | `PpPostingProduct_Authoriser` | String |  |  |
| 15 | `PP.POP.CO.CODE` | `PpPostingProduct_CoCode` | String |  |  |
| 16 | `PP.POP.DEPT.CODE` | `PpPostingProduct_DeptCode` | String |  |  |
| 17 | `PP.POP.AUDITOR.CODE` | `PpPostingProduct_AuditorCode` | String |  |  |
| 18 | `PP.POP.AUDIT.DATE.TIME` | `PpPostingProduct_AuditDateTime` | String |  |  |
