# CAMB.EVR.LOG.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAMB.EVR.LOG.DETAILS` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.EVRLOG.LOG.FILE.DIR` | `CambEvrLogDetails_LogFileDir` | TField |  |  |
| 2 | `CAPL.EVRLOG.LOG.FILENAME` | `CambEvrLogDetails_LogFilename` | TField |  |  |
| 3 | `CAPL.EVRLOG.POS.FILE.DIR` | `CambEvrLogDetails_PosFileDir` | TField |  |  |
| 4 | `CAPL.EVRLOG.POS.FILENAME` | `CambEvrLogDetails_PosFilename` | TField |  |  |
| 5 | `CAPL.EVRLOG.RESERVED.4` | `CambEvrLogDetails_Reserved4` | TField |  |  |
| 6 | `CAPL.EVRLOG.RESERVED.3` | `CambEvrLogDetails_Reserved3` | TField |  |  |
| 7 | `CAPL.EVRLOG.RESERVED.2` | `CambEvrLogDetails_Reserved2` | TField |  |  |
| 8 | `CAPL.EVRLOG.RESERVED.1` | `CambEvrLogDetails_Reserved1` | TField |  |  |
| 9 | `CAPL.EVRLOG.LOCAL.REF` | `CambEvrLogDetails_LocalRef` |  |  |  |
| 10 | `CAPL.EVRLOG.OVERRIDE` | `CambEvrLogDetails_Override` |  |  |  |
| 11 | `CAPL.EVRLOG.RECORD.STATUS` | `CambEvrLogDetails_RecordStatus` | String |  |  |
| 12 | `CAPL.EVRLOG.CURR.NO` | `CambEvrLogDetails_CurrNo` | String |  |  |
| 13 | `CAPL.EVRLOG.INPUTTER` | `CambEvrLogDetails_Inputter` |  |  |  |
| 14 | `CAPL.EVRLOG.DATE.TIME` | `CambEvrLogDetails_DateTime` |  |  |  |
| 15 | `CAPL.EVRLOG.AUTHORISER` | `CambEvrLogDetails_Authoriser` | String |  |  |
| 16 | `CAPL.EVRLOG.CO.CODE` | `CambEvrLogDetails_CoCode` | String |  |  |
| 17 | `CAPL.EVRLOG.DEPT.CODE` | `CambEvrLogDetails_DeptCode` | String |  |  |
| 18 | `CAPL.EVRLOG.AUDITOR.CODE` | `CambEvrLogDetails_AuditorCode` | String |  |  |
| 19 | `CAPL.EVRLOG.AUDIT.DATE.TIME` | `CambEvrLogDetails_AuditDateTime` | String |  |  |
