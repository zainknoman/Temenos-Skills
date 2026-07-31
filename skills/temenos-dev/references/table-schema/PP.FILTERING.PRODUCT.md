# PP.FILTERING.PRODUCT — Table Schema

> Source: `INSERTS/I_F.PP.FILTERING.PRODUCT` in `PP_FilteringService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.FLP.CompanyID` | `PpFilteringProduct_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.FLP.Description` | `PpFilteringProduct_Description` |  |  |  |
| 3 | `PP.FLP.RESERVED.5` | `PpFilteringProduct_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.FLP.RESERVED.4` | `PpFilteringProduct_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.FLP.RESERVED.3` | `PpFilteringProduct_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.FLP.RESERVED.2` | `PpFilteringProduct_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.FLP.RESERVED.1` | `PpFilteringProduct_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.FLP.LOCAL.REF` | `PpFilteringProduct_LocalRef` |  |  |  |
| 9 | `PP.FLP.OVERRIDE` | `PpFilteringProduct_Override` |  |  |  |
| 10 | `PP.FLP.RECORD.STATUS` | `PpFilteringProduct_RecordStatus` | String |  |  |
| 11 | `PP.FLP.CURR.NO` | `PpFilteringProduct_CurrNo` | String |  |  |
| 12 | `PP.FLP.INPUTTER` | `PpFilteringProduct_Inputter` |  |  |  |
| 13 | `PP.FLP.DATE.TIME` | `PpFilteringProduct_DateTime` |  |  |  |
| 14 | `PP.FLP.AUTHORISER` | `PpFilteringProduct_Authoriser` | String |  |  |
| 15 | `PP.FLP.CO.CODE` | `PpFilteringProduct_CoCode` | String |  |  |
| 16 | `PP.FLP.DEPT.CODE` | `PpFilteringProduct_DeptCode` | String |  |  |
| 17 | `PP.FLP.AUDITOR.CODE` | `PpFilteringProduct_AuditorCode` | String |  |  |
| 18 | `PP.FLP.AUDIT.DATE.TIME` | `PpFilteringProduct_AuditDateTime` | String |  |  |
