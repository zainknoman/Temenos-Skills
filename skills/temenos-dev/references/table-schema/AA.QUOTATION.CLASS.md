# AA.QUOTATION.CLASS — Table Schema

> Source: `INSERTS/I_F.AA.QUOTATION.CLASS` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.QC.DESCRIPTION` | `AaQuotationClass_Description` |  |  |  |
| 2 | `AA.QC.FULL.DESC` | `AaQuotationClass_FullDesc` |  |  |  |
| 3 | `AA.QC.TYPE` | `AaQuotationClass_Type` |  |  |  |
| 4 | `AA.QC.RESERVED.10` | `AaQuotationClass_Reserved10` | TField |  |  |
| 5 | `AA.QC.RESERVED.9` | `AaQuotationClass_Reserved9` | TField |  |  |
| 6 | `AA.QC.RESERVED.8` | `AaQuotationClass_Reserved8` | TField |  |  |
| 7 | `AA.QC.RESERVED.7` | `AaQuotationClass_Reserved7` | TField |  |  |
| 8 | `AA.QC.RESERVED.6` | `AaQuotationClass_Reserved6` | TField |  |  |
| 9 | `AA.QC.RESERVED.5` | `AaQuotationClass_Reserved5` | TField |  |  |
| 10 | `AA.QC.RESERVED.4` | `AaQuotationClass_Reserved4` | TField |  |  |
| 11 | `AA.QC.RESERVED.3` | `AaQuotationClass_Reserved3` | TField |  |  |
| 12 | `AA.QC.RESERVED.2` | `AaQuotationClass_Reserved2` | TField |  |  |
| 13 | `AA.QC.RESERVED.1` | `AaQuotationClass_Reserved1` | TField |  |  |
| 14 | `AA.QC.LOCAL.REF` | `AaQuotationClass_LocalRef` |  |  |  |
| 15 | `AA.QC.OVERRIDE` | `AaQuotationClass_Override` |  |  |  |
| 16 | `AA.QC.RECORD.STATUS` | `AaQuotationClass_RecordStatus` | String |  |  |
| 17 | `AA.QC.CURR.NO` | `AaQuotationClass_CurrNo` | String |  |  |
| 18 | `AA.QC.INPUTTER` | `AaQuotationClass_Inputter` |  |  |  |
| 19 | `AA.QC.DATE.TIME` | `AaQuotationClass_DateTime` |  |  |  |
| 20 | `AA.QC.AUTHORISER` | `AaQuotationClass_Authoriser` | String |  |  |
| 21 | `AA.QC.CO.CODE` | `AaQuotationClass_CoCode` | String |  |  |
| 22 | `AA.QC.DEPT.CODE` | `AaQuotationClass_DeptCode` | String |  |  |
| 23 | `AA.QC.AUDITOR.CODE` | `AaQuotationClass_AuditorCode` | String |  |  |
| 24 | `AA.QC.AUDIT.DATE.TIME` | `AaQuotationClass_AuditDateTime` | String |  |  |
