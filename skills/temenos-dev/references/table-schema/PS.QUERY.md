# PS.QUERY — Table Schema

> Source: `INSERTS/I_F.PS.QUERY` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.Q.DESCRIPTION` | `PsQuery_Description` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `PS.Q.SELECTION.TITLE` | `PsQuery_SelectionTitle` |  |  |  |
| 3 | `PS.Q.RESULTS.TITLE` | `PsQuery_ResultsTitle` |  |  |  |
| 4 | `PS.Q.ENQUIRY.ID` | `PsQuery_EnquiryId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `PS.Q.VIEW.ID` | `PsQuery_ViewId` |  |  |  |
| 6 | `PS.Q.VIEW.LABEL` | `PsQuery_ViewLabel` |  |  |  |
| 7 | `PS.Q.PRESENTATION.ID` | `PsQuery_PresentationId` |  |  |  |
| 8 | `PS.Q.CONTEXT.LINK.ID` | `PsQuery_ContextLinkId` |  |  |  |
| 9 | `PS.Q.REFRESH.SECONDS` | `PsQuery_RefreshSeconds` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `PS.Q.RESERVED.18` | `PsQuery_Reserved18` | TField |  |  |
| 11 | `PS.Q.RESERVED.17` | `PsQuery_Reserved17` | TField |  |  |
| 12 | `PS.Q.RESERVED.16` | `PsQuery_Reserved16` | TField |  |  |
| 13 | `PS.Q.RESERVED.15` | `PsQuery_Reserved15` | TField |  |  |
| 14 | `PS.Q.RESERVED.14` | `PsQuery_Reserved14` | TField |  |  |
| 15 | `PS.Q.RESERVED.13` | `PsQuery_Reserved13` | TField |  |  |
| 16 | `PS.Q.RESERVED.12` | `PsQuery_Reserved12` | TField |  |  |
| 17 | `PS.Q.RESERVED.11` | `PsQuery_Reserved11` | TField |  |  |
| 18 | `PS.Q.RESERVED.10` | `PsQuery_Reserved10` | TField |  |  |
| 19 | `PS.Q.RESERVED.9` | `PsQuery_Reserved9` | TField |  |  |
| 20 | `PS.Q.RESERVED.8` | `PsQuery_Reserved8` | TField |  |  |
| 21 | `PS.Q.RESERVED.7` | `PsQuery_Reserved7` | TField |  |  |
| 22 | `PS.Q.RESERVED.6` | `PsQuery_Reserved6` | TField |  |  |
| 23 | `PS.Q.RESERVED.5` | `PsQuery_Reserved5` | TField |  |  |
| 24 | `PS.Q.RESERVED.4` | `PsQuery_Reserved4` | TField |  |  |
| 25 | `PS.Q.RESERVED.3` | `PsQuery_Reserved3` | TField |  |  |
| 26 | `PS.Q.RESERVED.2` | `PsQuery_Reserved2` | TField |  |  |
| 27 | `PS.Q.RESERVED.1` | `PsQuery_Reserved1` | TField |  |  |
| 28 | `PS.Q.LOCAL.REF` | `PsQuery_LocalRef` |  |  |  |
| 29 | `PS.Q.OVERRIDE` | `PsQuery_Override` |  |  |  |
| 30 | `PS.Q.RECORD.STATUS` | `PsQuery_RecordStatus` | String |  |  |
| 31 | `PS.Q.CURR.NO` | `PsQuery_CurrNo` | String |  |  |
| 32 | `PS.Q.INPUTTER` | `PsQuery_Inputter` |  |  |  |
| 33 | `PS.Q.DATE.TIME` | `PsQuery_DateTime` |  |  |  |
| 34 | `PS.Q.AUTHORISER` | `PsQuery_Authoriser` | String |  |  |
| 35 | `PS.Q.CO.CODE` | `PsQuery_CoCode` | String |  |  |
| 36 | `PS.Q.DEPT.CODE` | `PsQuery_DeptCode` | String |  |  |
| 37 | `PS.Q.AUDITOR.CODE` | `PsQuery_AuditorCode` | String |  |  |
| 38 | `PS.Q.AUDIT.DATE.TIME` | `PsQuery_AuditDateTime` | String |  |  |
