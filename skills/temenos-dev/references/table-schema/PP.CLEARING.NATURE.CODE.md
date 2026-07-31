# PP.CLEARING.NATURE.CODE — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.NATURE.CODE` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CGN.CompanyID` | `PpClearingNatureCode_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.CGN.ClearingNatureCodeDesc` | `PpClearingNatureCode_Clearingnaturecodedesc` |  |  |  |
| 3 | `PP.CGN.ChequeType` | `PpClearingNatureCode_Chequetype` | TField |  | Indicates the type of cheque for the clearing. Validation Rules: 4 alphanumeric characters. |
| 4 | `PP.CGN.InstType` | `PpClearingNatureCode_Insttype` | TField |  | Specifies if the clearing nature code is used as part of instant (INST) or near real instant (NRINST) payments Possible Values: INST,NRINST,BLANK. |
| 5 | `PP.CGN.RESERVED.4` | `PpClearingNatureCode_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.CGN.RESERVED.3` | `PpClearingNatureCode_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.CGN.RESERVED.2` | `PpClearingNatureCode_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.CGN.RESERVED.1` | `PpClearingNatureCode_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.CGN.LOCAL.REF` | `PpClearingNatureCode_LocalRef` |  |  |  |
| 10 | `PP.CGN.OVERRIDE` | `PpClearingNatureCode_Override` |  |  |  |
| 11 | `PP.CGN.RECORD.STATUS` | `PpClearingNatureCode_RecordStatus` | String |  |  |
| 12 | `PP.CGN.CURR.NO` | `PpClearingNatureCode_CurrNo` | String |  |  |
| 13 | `PP.CGN.INPUTTER` | `PpClearingNatureCode_Inputter` |  |  |  |
| 14 | `PP.CGN.DATE.TIME` | `PpClearingNatureCode_DateTime` |  |  |  |
| 15 | `PP.CGN.AUTHORISER` | `PpClearingNatureCode_Authoriser` | String |  |  |
| 16 | `PP.CGN.CO.CODE` | `PpClearingNatureCode_CoCode` | String |  |  |
| 17 | `PP.CGN.DEPT.CODE` | `PpClearingNatureCode_DeptCode` | String |  |  |
| 18 | `PP.CGN.AUDITOR.CODE` | `PpClearingNatureCode_AuditorCode` | String |  |  |
| 19 | `PP.CGN.AUDIT.DATE.TIME` | `PpClearingNatureCode_AuditDateTime` | String |  |  |
