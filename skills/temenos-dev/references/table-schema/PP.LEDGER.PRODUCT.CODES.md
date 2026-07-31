# PP.LEDGER.PRODUCT.CODES — Table Schema

> Source: `INSERTS/I_F.PP.LEDGER.PRODUCT.CODES` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PCL.CompanyID` | `PpLedgerProductCodes_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.PCL.ProductDescription` | `PpLedgerProductCodes_Productdescription1` |  |  |  |
| 3 | `PP.PCL.ShortProductDescription` | `PpLedgerProductCodes_Shortproductdescription1` |  |  |  |
| 4 | `PP.PCL.RESERVED.5` | `PpLedgerProductCodes_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.PCL.RESERVED.4` | `PpLedgerProductCodes_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.PCL.RESERVED.3` | `PpLedgerProductCodes_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.PCL.RESERVED.2` | `PpLedgerProductCodes_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.PCL.RESERVED.1` | `PpLedgerProductCodes_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.PCL.LOCAL.REF` | `PpLedgerProductCodes_LocalRef` |  |  |  |
| 10 | `PP.PCL.OVERRIDE` | `PpLedgerProductCodes_Override` |  |  |  |
| 11 | `PP.PCL.RECORD.STATUS` | `PpLedgerProductCodes_RecordStatus` | String |  |  |
| 12 | `PP.PCL.CURR.NO` | `PpLedgerProductCodes_CurrNo` | String |  |  |
| 13 | `PP.PCL.INPUTTER` | `PpLedgerProductCodes_Inputter` |  |  |  |
| 14 | `PP.PCL.DATE.TIME` | `PpLedgerProductCodes_DateTime` |  |  |  |
| 15 | `PP.PCL.AUTHORISER` | `PpLedgerProductCodes_Authoriser` | String |  |  |
| 16 | `PP.PCL.CO.CODE` | `PpLedgerProductCodes_CoCode` | String |  |  |
| 17 | `PP.PCL.DEPT.CODE` | `PpLedgerProductCodes_DeptCode` | String |  |  |
| 18 | `PP.PCL.AUDITOR.CODE` | `PpLedgerProductCodes_AuditorCode` | String |  |  |
| 19 | `PP.PCL.AUDIT.DATE.TIME` | `PpLedgerProductCodes_AuditDateTime` | String |  |  |
