# PP.CLIENTCOND.PRODUCT — Table Schema

> Source: `INSERTS/I_F.PP.CLIENTCOND.PRODUCT` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CCP.CompanyID` | `PpClientcondProduct_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 3 | `PP.CCP.RESERVED.5` | `PpClientcondProduct_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.CCP.RESERVED.4` | `PpClientcondProduct_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.CCP.RESERVED.3` | `PpClientcondProduct_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.CCP.RESERVED.2` | `PpClientcondProduct_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.CCP.RESERVED.1` | `PpClientcondProduct_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.CCP.LOCAL.REF` | `PpClientcondProduct_LocalRef` |  |  |  |
| 9 | `PP.CCP.OVERRIDE` | `PpClientcondProduct_Override` |  |  |  |
| 10 | `PP.CCP.RECORD.STATUS` | `PpClientcondProduct_RecordStatus` | String |  |  |
| 11 | `PP.CCP.CURR.NO` | `PpClientcondProduct_CurrNo` | String |  |  |
| 12 | `PP.CCP.INPUTTER` | `PpClientcondProduct_Inputter` |  |  |  |
| 13 | `PP.CCP.DATE.TIME` | `PpClientcondProduct_DateTime` |  |  |  |
| 14 | `PP.CCP.AUTHORISER` | `PpClientcondProduct_Authoriser` | String |  |  |
| 15 | `PP.CCP.CO.CODE` | `PpClientcondProduct_CoCode` | String |  |  |
| 16 | `PP.CCP.DEPT.CODE` | `PpClientcondProduct_DeptCode` | String |  |  |
| 17 | `PP.CCP.AUDITOR.CODE` | `PpClientcondProduct_AuditorCode` | String |  |  |
| 18 | `PP.CCP.AUDIT.DATE.TIME` | `PpClientcondProduct_AuditDateTime` | String |  |  |
