# PP.ROUTING.PRODUCT — Table Schema

> Source: `INSERTS/I_F.PP.ROUTING.PRODUCT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ROP.CompanyID` | `PpRoutingProduct_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.ROP.Description` | `PpRoutingProduct_Description` |  |  |  |
| 3 | `PP.ROP.RESERVED.5` | `PpRoutingProduct_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.ROP.RESERVED.4` | `PpRoutingProduct_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.ROP.RESERVED.3` | `PpRoutingProduct_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.ROP.RESERVED.2` | `PpRoutingProduct_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.ROP.RESERVED.1` | `PpRoutingProduct_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.ROP.LOCAL.REF` | `PpRoutingProduct_LocalRef` |  |  |  |
| 9 | `PP.ROP.OVERRIDE` | `PpRoutingProduct_Override` |  |  |  |
| 10 | `PP.ROP.RECORD.STATUS` | `PpRoutingProduct_RecordStatus` | String |  |  |
| 11 | `PP.ROP.CURR.NO` | `PpRoutingProduct_CurrNo` | String |  |  |
| 12 | `PP.ROP.INPUTTER` | `PpRoutingProduct_Inputter` |  |  |  |
| 13 | `PP.ROP.DATE.TIME` | `PpRoutingProduct_DateTime` |  |  |  |
| 14 | `PP.ROP.AUTHORISER` | `PpRoutingProduct_Authoriser` | String |  |  |
| 15 | `PP.ROP.CO.CODE` | `PpRoutingProduct_CoCode` | String |  |  |
| 16 | `PP.ROP.DEPT.CODE` | `PpRoutingProduct_DeptCode` | String |  |  |
| 17 | `PP.ROP.AUDITOR.CODE` | `PpRoutingProduct_AuditorCode` | String |  |  |
| 18 | `PP.ROP.AUDIT.DATE.TIME` | `PpRoutingProduct_AuditDateTime` | String |  |  |
