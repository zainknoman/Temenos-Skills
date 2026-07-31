# CAMB.XML.ORIG.DATA — Table Schema

> Source: `INSERTS/I_F.CAMB.XML.ORIG.DATA` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.DATA.SOURCE.DATA` | `CambXmlOrigData_SourceData` |  |  |  |
| 2 | `CAMB.DATA.DESTINATION.DATA` | `CambXmlOrigData_DestinationData` |  |  |  |
| 3 | `CAMB.DATA.RECORD.STATUS` | `CambXmlOrigData_RecordStatus` |  |  |  |
| 4 | `CAMB.DATA.CURR.NO` | `CambXmlOrigData_CurrNo` |  |  |  |
| 5 | `CAMB.DATA.INPUTTER` | `CambXmlOrigData_Inputter` |  |  |  |
| 6 | `CAMB.DATA.DATE.TIME` | `CambXmlOrigData_DateTime` |  |  |  |
| 7 | `CAMB.DATA.AUTHORISER` | `CambXmlOrigData_Authoriser` |  |  |  |
| 8 | `CAMB.DATA.CO.CODE` | `CambXmlOrigData_CoCode` |  |  |  |
| 9 | `CAMB.DATA.DEPT.CODE` | `CambXmlOrigData_DeptCode` |  |  |  |
| 10 | `CAMB.DATA.AUDITOR.CODE` | `CambXmlOrigData_AuditorCode` |  |  |  |
| 11 | `CAMB.DATA.AUDIT.DATE.TIME` | `CambXmlOrigData_AuditDateTime` |  |  |  |
