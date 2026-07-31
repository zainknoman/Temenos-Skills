# IS.VENDOR — Table Schema

> Source: `INSERTS/I_F.IS.VENDOR` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.VEN.NAME` | `IsVendor_Name` | TField |  | Defines the Name of the Vendor. Defaulted as Name of the Customer (@ID being Customer Reference). It can be over-written to specify User-Defined names. Validation Rules: 1. Defaulted as NAME.1 from the Customer table. 2. Standard T24 Alphanumeric field. |
| 2 | `IS.VEN.STATUS` | `IsVendor_Status` | TField | Yes | Identifies the Status of the Vendor. No transactions are permitted for a Vendor with status as &quot;Inactive&quot; Validation Rules: 1. Mandatory Input. 2. The values to the field are defined in the EB.LOOKUP table with prefix &quot;IS.VENDOR.STATUS*&quot;. |
| 3 | `IS.VEN.COMPANY` | `IsVendor_Company` |  |  |  |
| 4 | `IS.VEN.CURRENCY` | `IsVendor_Currency` |  |  |  |
| 5 | `IS.VEN.ACCOUNT` | `IsVendor_Account` |  |  |  |
| 6 | `IS.VEN.BENEFICIARY` | `IsVendor_Beneficiary` |  |  |  |
| 7 | `IS.VEN.RESERVED.13` | `IsVendor_Reserved13` |  |  |  |
| 8 | `IS.VEN.RESERVED.12` | `IsVendor_Reserved12` |  |  |  |
| 9 | `IS.VEN.RESERVED.11` | `IsVendor_Reserved11` |  |  |  |
| 10 | `IS.VEN.COMMODITY` | `IsVendor_Commodity` |  |  |  |
| 11 | `IS.VEN.REBATE.CCY` | `IsVendor_RebateCcy` |  |  |  |
| 12 | `IS.VEN.REBATE.TYPE` | `IsVendor_RebateType` |  |  |  |
| 13 | `IS.VEN.REBATE.VALUE` | `IsVendor_RebateValue` |  |  |  |
| 14 | `IS.VEN.START.DATE` | `IsVendor_StartDate` |  |  |  |
| 15 | `IS.VEN.SPL.REBATE.TYPE` | `IsVendor_SplRebateType` |  |  |  |
| 16 | `IS.VEN.SPL.REBATE.VALUE` | `IsVendor_SplRebateValue` |  |  |  |
| 17 | `IS.VEN.END.DATE` | `IsVendor_EndDate` |  |  |  |
| 18 | `IS.VEN.RESERVED.2` | `IsVendor_Reserved2` | TField |  |  |
| 19 | `IS.VEN.RESERVED.1` | `IsVendor_Reserved1` | TField |  |  |
| 20 | `IS.VEN.LOCAL.REF` | `IsVendor_LocalRef` |  |  |  |
| 21 | `IS.VEN.OVERRIDE` | `IsVendor_Override` |  |  |  |
| 22 | `IS.VEN.RECORD.STATUS` | `IsVendor_RecordStatus` | String |  |  |
| 23 | `IS.VEN.CURR.NO` | `IsVendor_CurrNo` | String |  |  |
| 24 | `IS.VEN.INPUTTER` | `IsVendor_Inputter` |  |  |  |
| 25 | `IS.VEN.DATE.TIME` | `IsVendor_DateTime` |  |  |  |
| 26 | `IS.VEN.AUTHORISER` | `IsVendor_Authoriser` | String |  |  |
| 27 | `IS.VEN.CO.CODE` | `IsVendor_CoCode` | String |  |  |
| 28 | `IS.VEN.DEPT.CODE` | `IsVendor_DeptCode` | String |  |  |
| 29 | `IS.VEN.AUDITOR.CODE` | `IsVendor_AuditorCode` | String |  |  |
| 30 | `IS.VEN.AUDIT.DATE.TIME` | `IsVendor_AuditDateTime` | String |  |  |
