# SC.LOCAL.TAX.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.LOCAL.TAX.PARAM` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SLT.TAX.BASIS` | `ScLocalTaxParam_TaxBasis` | TField | Yes | This field holds the type of transaction basis for the allocation/unallocation of nominals in ET files. Validation Rules: Valid Inputs are 'FIFO'(First In First Out) ,'LIFO' (Last In First Out) or 'AVERAGE' This is a Mandatory field |
| 2 | `SC.SLT.RESERVED.2` | `ScLocalTaxParam_Reserved2` | TField |  |  |
| 3 | `SC.SLT.RESERVED.1` | `ScLocalTaxParam_Reserved1` | TField |  |  |
| 4 | `SC.SLT.LOCAL.REF` | `ScLocalTaxParam_LocalRef` |  |  |  |
| 5 | `SC.SLT.RECORD.STATUS` | `ScLocalTaxParam_RecordStatus` | String |  |  |
| 6 | `SC.SLT.CURR.NO` | `ScLocalTaxParam_CurrNo` | String |  |  |
| 7 | `SC.SLT.INPUTTER` | `ScLocalTaxParam_Inputter` |  |  |  |
| 8 | `SC.SLT.DATE.TIME` | `ScLocalTaxParam_DateTime` |  |  |  |
| 9 | `SC.SLT.AUTHORISER` | `ScLocalTaxParam_Authoriser` | String |  |  |
| 10 | `SC.SLT.CO.CODE` | `ScLocalTaxParam_CoCode` | String |  |  |
| 11 | `SC.SLT.DEPT.CODE` | `ScLocalTaxParam_DeptCode` | String |  |  |
| 12 | `SC.SLT.AUDITOR.CODE` | `ScLocalTaxParam_AuditorCode` | String |  |  |
| 13 | `SC.SLT.AUDIT.DATE.TIME` | `ScLocalTaxParam_AuditDateTime` | String |  |  |
