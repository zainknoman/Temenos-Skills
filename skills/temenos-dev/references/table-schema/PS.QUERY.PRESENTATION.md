# PS.QUERY.PRESENTATION — Table Schema

> Source: `INSERTS/I_F.PS.QUERY.PRESENTATION` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.QP.PRESENTATION.XML` | `PsQueryPresentation_PresentationXml` |  |  |  |
| 2 | `PS.QP.RESERVED.9` | `PsQueryPresentation_Reserved9` | TField |  |  |
| 3 | `PS.QP.RESERVED.8` | `PsQueryPresentation_Reserved8` | TField |  |  |
| 4 | `PS.QP.RESERVED.7` | `PsQueryPresentation_Reserved7` | TField |  |  |
| 5 | `PS.QP.RESERVED.6` | `PsQueryPresentation_Reserved6` | TField |  |  |
| 6 | `PS.QP.RESERVED.5` | `PsQueryPresentation_Reserved5` | TField |  |  |
| 7 | `PS.QP.RESERVED.4` | `PsQueryPresentation_Reserved4` | TField |  |  |
| 8 | `PS.QP.RESERVED.3` | `PsQueryPresentation_Reserved3` | TField |  |  |
| 9 | `PS.QP.RESERVED.2` | `PsQueryPresentation_Reserved2` | TField |  |  |
| 10 | `PS.QP.RESERVED.1` | `PsQueryPresentation_Reserved1` | TField |  |  |
| 11 | `PS.QP.LOCAL.REF` | `PsQueryPresentation_LocalRef` |  |  |  |
| 12 | `PS.QP.OVERRIDE` | `PsQueryPresentation_Override` |  |  |  |
| 13 | `PS.QP.RECORD.STATUS` | `PsQueryPresentation_RecordStatus` | String |  |  |
| 14 | `PS.QP.CURR.NO` | `PsQueryPresentation_CurrNo` | String |  |  |
| 15 | `PS.QP.INPUTTER` | `PsQueryPresentation_Inputter` |  |  |  |
| 16 | `PS.QP.DATE.TIME` | `PsQueryPresentation_DateTime` |  |  |  |
| 17 | `PS.QP.AUTHORISER` | `PsQueryPresentation_Authoriser` | String |  |  |
| 18 | `PS.QP.CO.CODE` | `PsQueryPresentation_CoCode` | String |  |  |
| 19 | `PS.QP.DEPT.CODE` | `PsQueryPresentation_DeptCode` | String |  |  |
| 20 | `PS.QP.AUDITOR.CODE` | `PsQueryPresentation_AuditorCode` | String |  |  |
| 21 | `PS.QP.AUDIT.DATE.TIME` | `PsQueryPresentation_AuditDateTime` | String |  |  |
