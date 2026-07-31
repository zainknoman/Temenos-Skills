# CAPL.H.TAX.SLIPS.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TAX.SLIPS.PARAM` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.TAX.PARAM.TAX.YEAR` | `CaplHTaxSlipsParam_TaxYear` | TField |  | This field is to define the tax year, the year on which the tax slip to be generated.E.g. 2015 |
| 2 | `CAPL.TAX.PARAM.SEL.CRITERIA` | `CaplHTaxSlipsParam_SelCriteria` |  |  |  |
| 3 | `CAPL.TAX.PARAM.RUN.BATCH` | `CaplHTaxSlipsParam_RunBatch` | TField |  | Field denoted whether the slip to be run through batch or not.Allowed values are Yes/No |
| 4 | `CAPL.TAX.PARAM.LOCAL.REF` | `CaplHTaxSlipsParam_LocalRef` |  |  |  |
| 5 | `CAPL.TAX.PARAM.RESERVED.9` | `CaplHTaxSlipsParam_Reserved9` |  |  |  |
| 6 | `CAPL.TAX.PARAM.RESERVED.8` | `CaplHTaxSlipsParam_Reserved8` |  |  |  |
| 7 | `CAPL.TAX.PARAM.RESERVED.7` | `CaplHTaxSlipsParam_Reserved7` |  |  |  |
| 8 | `CAPL.TAX.PARAM.RESERVED.6` | `CaplHTaxSlipsParam_Reserved6` |  |  |  |
| 9 | `CAPL.TAX.PARAM.RESERVED.5` | `CaplHTaxSlipsParam_Reserved5` |  |  |  |
| 10 | `CAPL.TAX.PARAM.RESERVED.4` | `CaplHTaxSlipsParam_Reserved4` |  |  |  |
| 11 | `CAPL.TAX.PARAM.RESERVED.3` | `CaplHTaxSlipsParam_Reserved3` |  |  |  |
| 12 | `CAPL.TAX.PARAM.RESERVED.2` | `CaplHTaxSlipsParam_Reserved2` |  |  |  |
| 13 | `CAPL.TAX.PARAM.RESERVED.1` | `CaplHTaxSlipsParam_Reserved1` |  |  |  |
| 14 | `CAPL.TAX.PARAM.OVERRIDE` | `CaplHTaxSlipsParam_Override` |  |  |  |
| 15 | `CAPL.TAX.PARAM.RECORD.STATUS` | `CaplHTaxSlipsParam_RecordStatus` | String |  |  |
| 16 | `CAPL.TAX.PARAM.CURR.NO` | `CaplHTaxSlipsParam_CurrNo` | String |  |  |
| 17 | `CAPL.TAX.PARAM.INPUTTER` | `CaplHTaxSlipsParam_Inputter` |  |  |  |
| 18 | `CAPL.TAX.PARAM.DATE.TIME` | `CaplHTaxSlipsParam_DateTime` |  |  |  |
| 19 | `CAPL.TAX.PARAM.AUTHORISER` | `CaplHTaxSlipsParam_Authoriser` | String |  |  |
| 20 | `CAPL.TAX.PARAM.CO.CODE` | `CaplHTaxSlipsParam_CoCode` | String |  |  |
| 21 | `CAPL.TAX.PARAM.DEPT.CODE` | `CaplHTaxSlipsParam_DeptCode` | String |  |  |
| 22 | `CAPL.TAX.PARAM.AUDITOR.CODE` | `CaplHTaxSlipsParam_AuditorCode` | String |  |  |
| 23 | `CAPL.TAX.PARAM.AUDIT.DATE.TIME` | `CaplHTaxSlipsParam_AuditDateTime` | String |  |  |
