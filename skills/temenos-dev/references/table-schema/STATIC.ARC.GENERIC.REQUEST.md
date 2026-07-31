# STATIC.ARC.GENERIC.REQUEST — Table Schema

> Source: `INSERTS/I_F.STATIC.ARC.GENERIC.REQUEST` in `PP_ArchivingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STATIC.ArchiveID` | `StaticArcGenericRequest_Archiveid` |  |  |  |
| 2 | `STATIC.RECORD.STATUS` | `StaticArcGenericRequest_RecordStatus` |  |  |  |
| 3 | `STATIC.CURR.NO` | `StaticArcGenericRequest_CurrNo` |  |  |  |
| 4 | `STATIC.INPUTTER` | `StaticArcGenericRequest_Inputter` |  |  |  |
| 5 | `STATIC.DATE.TIME` | `StaticArcGenericRequest_DateTime` |  |  |  |
| 6 | `STATIC.AUTHORISER` | `StaticArcGenericRequest_Authoriser` |  |  |  |
| 7 | `STATIC.CO.CODE` | `StaticArcGenericRequest_CoCode` |  |  |  |
| 8 | `STATIC.DEPT.CODE` | `StaticArcGenericRequest_DeptCode` |  |  |  |
| 9 | `STATIC.AUDITOR.CODE` | `StaticArcGenericRequest_AuditorCode` |  |  |  |
| 10 | `STATIC.AUDIT.DATE.TIME` | `StaticArcGenericRequest_AuditDateTime` |  |  |  |
