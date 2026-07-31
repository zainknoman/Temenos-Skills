# PP.FEE.PRODUCT — Table Schema

> Source: `INSERTS/I_F.PP.FEE.PRODUCT` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.FEP.CompanyID` | `PpFeeProduct_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.FEP.Description` | `PpFeeProduct_Description` |  |  |  |
| 3 | `PP.FEP.RESERVED.5` | `PpFeeProduct_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.FEP.RESERVED.4` | `PpFeeProduct_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.FEP.RESERVED.3` | `PpFeeProduct_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.FEP.RESERVED.2` | `PpFeeProduct_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.FEP.RESERVED.1` | `PpFeeProduct_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.FEP.LOCAL.REF` | `PpFeeProduct_LocalRef` |  |  |  |
| 9 | `PP.FEP.OVERRIDE` | `PpFeeProduct_Override` |  |  |  |
| 10 | `PP.FEP.RECORD.STATUS` | `PpFeeProduct_RecordStatus` | String |  |  |
| 11 | `PP.FEP.CURR.NO` | `PpFeeProduct_CurrNo` | String |  |  |
| 12 | `PP.FEP.INPUTTER` | `PpFeeProduct_Inputter` |  |  |  |
| 13 | `PP.FEP.DATE.TIME` | `PpFeeProduct_DateTime` |  |  |  |
| 14 | `PP.FEP.AUTHORISER` | `PpFeeProduct_Authoriser` | String |  |  |
| 15 | `PP.FEP.CO.CODE` | `PpFeeProduct_CoCode` | String |  |  |
| 16 | `PP.FEP.DEPT.CODE` | `PpFeeProduct_DeptCode` | String |  |  |
| 17 | `PP.FEP.AUDITOR.CODE` | `PpFeeProduct_AuditorCode` | String |  |  |
| 18 | `PP.FEP.AUDIT.DATE.TIME` | `PpFeeProduct_AuditDateTime` | String |  |  |
