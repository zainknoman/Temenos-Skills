# CMBASE.TAX.STANDARD.RECORDS.LIST — Table Schema

> Source: `INSERTS/I_F.CMBASE.TAX.STANDARD.RECORDS.LIST` in `CMBASE_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RECORDS.LIST.PRODUCT` | `CmbaseTaxStandardRecordsList_Product` |  |  |  |
| 2 | `RECORDS.LIST.PROPERTY` | `CmbaseTaxStandardRecordsList_Property` |  |  |  |
| 3 | `RECORDS.LIST.ACTIVITY` | `CmbaseTaxStandardRecordsList_Activity` |  |  |  |
| 4 | `RECORDS.LIST.LOCAL.REF` | `CmbaseTaxStandardRecordsList_LocalRef` |  |  |  |
| 5 | `RECORDS.LIST.OVERRIDE` | `CmbaseTaxStandardRecordsList_Override` |  |  |  |
| 6 | `RECORDS.LIST.RECORD.STATUS` | `CmbaseTaxStandardRecordsList_RecordStatus` | String |  |  |
| 7 | `RECORDS.LIST.CURR.NO` | `CmbaseTaxStandardRecordsList_CurrNo` | String |  |  |
| 8 | `RECORDS.LIST.INPUTTER` | `CmbaseTaxStandardRecordsList_Inputter` |  |  |  |
| 9 | `RECORDS.LIST.DATE.TIME` | `CmbaseTaxStandardRecordsList_DateTime` |  |  |  |
| 10 | `RECORDS.LIST.AUTHORISER` | `CmbaseTaxStandardRecordsList_Authoriser` | String |  |  |
| 11 | `RECORDS.LIST.CO.CODE` | `CmbaseTaxStandardRecordsList_CoCode` | String |  |  |
| 12 | `RECORDS.LIST.DEPT.CODE` | `CmbaseTaxStandardRecordsList_DeptCode` | String |  |  |
| 13 | `RECORDS.LIST.AUDITOR.CODE` | `CmbaseTaxStandardRecordsList_AuditorCode` | String |  |  |
| 14 | `RECORDS.LIST.AUDIT.DATE.TIME` | `CmbaseTaxStandardRecordsList_AuditDateTime` | String |  |  |
