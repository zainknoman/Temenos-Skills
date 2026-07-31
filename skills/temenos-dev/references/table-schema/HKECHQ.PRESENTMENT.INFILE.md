# HKECHQ.PRESENTMENT.INFILE — Table Schema

> Source: `INSERTS/I_F.HKECHQ.PRESENTMENT.INFILE` in `HKECHQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HKECHQ.INFILE.INWARD.FILE.NAME` | `HkechqPresentmentInfile_InwardFileName` |  |  |  |
| 2 | `HKECHQ.INFILE.FILE.PROCESS.STATUS` | `HkechqPresentmentInfile_FileProcessStatus` | TField |  | Indicates outward file generation status |
| 3 | `HKECHQ.INFILE.LOCAL.REF` | `HkechqPresentmentInfile_LocalRef` |  |  |  |
| 4 | `HKECHQ.INFILE.OVERRIDE` | `HkechqPresentmentInfile_Override` |  |  |  |
| 5 | `HKECHQ.INFILE.RECORD.STATUS` | `HkechqPresentmentInfile_RecordStatus` | String |  |  |
| 6 | `HKECHQ.INFILE.CURR.NO` | `HkechqPresentmentInfile_CurrNo` | String |  |  |
| 7 | `HKECHQ.INFILE.INPUTTER` | `HkechqPresentmentInfile_Inputter` |  |  |  |
| 8 | `HKECHQ.INFILE.DATE.TIME` | `HkechqPresentmentInfile_DateTime` |  |  |  |
| 9 | `HKECHQ.INFILE.AUTHORISER` | `HkechqPresentmentInfile_Authoriser` | String |  |  |
| 10 | `HKECHQ.INFILE.CO.CODE` | `HkechqPresentmentInfile_CoCode` | String |  |  |
| 11 | `HKECHQ.INFILE.DEPT.CODE` | `HkechqPresentmentInfile_DeptCode` | String |  |  |
| 12 | `HKECHQ.INFILE.AUDITOR.CODE` | `HkechqPresentmentInfile_AuditorCode` | String |  |  |
| 13 | `HKECHQ.INFILE.AUDIT.DATE.TIME` | `HkechqPresentmentInfile_AuditDateTime` | String |  |  |
