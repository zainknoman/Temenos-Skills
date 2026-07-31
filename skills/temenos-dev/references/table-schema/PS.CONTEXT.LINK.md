# PS.CONTEXT.LINK — Table Schema

> Source: `INSERTS/I_F.PS.CONTEXT.LINK` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.CL.DESCRIPTION` | `PsContextLink_Description` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `PS.CL.SOURCE.TYPE` | `PsContextLink_SourceType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `PS.CL.SOURCE.ID` | `PsContextLink_SourceId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `PS.CL.LINK.DEFINITION` | `PsContextLink_LinkDefinition` |  |  |  |
| 5 | `PS.CL.RESERVED.9` | `PsContextLink_Reserved9` | TField |  |  |
| 6 | `PS.CL.RESERVED.8` | `PsContextLink_Reserved8` | TField |  |  |
| 7 | `PS.CL.RESERVED.7` | `PsContextLink_Reserved7` | TField |  |  |
| 8 | `PS.CL.RESERVED.6` | `PsContextLink_Reserved6` | TField |  |  |
| 9 | `PS.CL.RESERVED.5` | `PsContextLink_Reserved5` | TField |  |  |
| 10 | `PS.CL.RESERVED.4` | `PsContextLink_Reserved4` | TField |  |  |
| 11 | `PS.CL.RESERVED.3` | `PsContextLink_Reserved3` | TField |  |  |
| 12 | `PS.CL.RESERVED.2` | `PsContextLink_Reserved2` | TField |  |  |
| 13 | `PS.CL.RESERVED.1` | `PsContextLink_Reserved1` | TField |  |  |
| 14 | `PS.CL.LOCAL.REF` | `PsContextLink_LocalRef` |  |  |  |
| 15 | `PS.CL.OVERRIDE` | `PsContextLink_Override` |  |  |  |
| 16 | `PS.CL.RECORD.STATUS` | `PsContextLink_RecordStatus` | String |  |  |
| 17 | `PS.CL.CURR.NO` | `PsContextLink_CurrNo` | String |  |  |
| 18 | `PS.CL.INPUTTER` | `PsContextLink_Inputter` |  |  |  |
| 19 | `PS.CL.DATE.TIME` | `PsContextLink_DateTime` |  |  |  |
| 20 | `PS.CL.AUTHORISER` | `PsContextLink_Authoriser` | String |  |  |
| 21 | `PS.CL.CO.CODE` | `PsContextLink_CoCode` | String |  |  |
| 22 | `PS.CL.DEPT.CODE` | `PsContextLink_DeptCode` | String |  |  |
| 23 | `PS.CL.AUDITOR.CODE` | `PsContextLink_AuditorCode` | String |  |  |
| 24 | `PS.CL.AUDIT.DATE.TIME` | `PsContextLink_AuditDateTime` | String |  |  |
