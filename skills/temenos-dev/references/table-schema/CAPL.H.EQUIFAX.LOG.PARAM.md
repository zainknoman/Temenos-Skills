# CAPL.H.EQUIFAX.LOG.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.EQUIFAX.LOG.PARAM` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CB.DESCRIPTION` | `CaplHEquifaxLogParam_Description` | TField |  |  |
| 2 | `CAPL.CB.RESERVED.1` | `CaplHEquifaxLogParam_Reserved1` | TField |  |  |
| 3 | `CAPL.CB.RESERVED.2` | `CaplHEquifaxLogParam_Reserved2` | TField |  |  |
| 4 | `CAPL.CB.RESERVED.3` | `CaplHEquifaxLogParam_Reserved3` | TField |  |  |
| 5 | `CAPL.CB.RESERVED.4` | `CaplHEquifaxLogParam_Reserved4` | TField |  |  |
| 6 | `CAPL.CB.RESERVED.5` | `CaplHEquifaxLogParam_Reserved5` | TField |  |  |
| 7 | `CAPL.CB.LOCAL.REF` | `CaplHEquifaxLogParam_LocalRef` |  |  |  |
| 8 | `CAPL.CB.OVERRIDES` | `CaplHEquifaxLogParam_Overrides` |  |  |  |
| 9 | `CAPL.CB.RECORD.STATUS` | `CaplHEquifaxLogParam_RecordStatus` | String |  |  |
| 10 | `CAPL.CB.CURR.NO` | `CaplHEquifaxLogParam_CurrNo` | String |  |  |
| 11 | `CAPL.CB.INPUTTER` | `CaplHEquifaxLogParam_Inputter` |  |  |  |
| 12 | `CAPL.CB.DATE.TIME` | `CaplHEquifaxLogParam_DateTime` |  |  |  |
| 13 | `CAPL.CB.AUTHORISER` | `CaplHEquifaxLogParam_Authoriser` | String |  |  |
| 14 | `CAPL.CB.CO.CODE` | `CaplHEquifaxLogParam_CoCode` | String |  |  |
| 15 | `CAPL.CB.DEPT.CODE` | `CaplHEquifaxLogParam_DeptCode` | String |  |  |
| 16 | `CAPL.CB.AUDITOR.CODE` | `CaplHEquifaxLogParam_AuditorCode` | String |  |  |
| 17 | `CAPL.CB.AUDIT.DATE.TIME` | `CaplHEquifaxLogParam_AuditDateTime` | String |  |  |
