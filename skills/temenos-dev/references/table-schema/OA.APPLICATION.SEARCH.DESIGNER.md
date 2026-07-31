# OA.APPLICATION.SEARCH.DESIGNER — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.SEARCH.DESIGNER` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.ASD.DESCRIPTION` | `OaApplicationSearchDesigner_Description` |  |  |  |
| 2 | `OA.ASD.FULL.DESCRIPTION` | `OaApplicationSearchDesigner_FullDescription` |  |  |  |
| 3 | `OA.ASD.RESERVED.10` | `OaApplicationSearchDesigner_Reserved10` | TField |  |  |
| 4 | `OA.ASD.RESERVED.9` | `OaApplicationSearchDesigner_Reserved9` | TField |  |  |
| 5 | `OA.ASD.RESERVED.8` | `OaApplicationSearchDesigner_Reserved8` | TField |  |  |
| 6 | `OA.ASD.ENQ.CRITERIA.NAME` | `OaApplicationSearchDesigner_EnqCriteriaName` |  |  |  |
| 7 | `OA.ASD.CRITERIA.DESCRIPTION` | `OaApplicationSearchDesigner_CriteriaDescription` |  |  |  |
| 8 | `OA.ASD.DATA.OBJECT` | `OaApplicationSearchDesigner_DataObject` |  |  |  |
| 9 | `OA.ASD.ATTRIBUTE` | `OaApplicationSearchDesigner_Attribute` |  |  |  |
| 10 | `OA.ASD.STATUS.CODES` | `OaApplicationSearchDesigner_StatusCodes` |  |  |  |
| 11 | `OA.ASD.RESERVED.7` | `OaApplicationSearchDesigner_Reserved7` | TField |  |  |
| 12 | `OA.ASD.RESERVED.6` | `OaApplicationSearchDesigner_Reserved6` | TField |  |  |
| 13 | `OA.ASD.RESERVED.5` | `OaApplicationSearchDesigner_Reserved5` | TField |  |  |
| 14 | `OA.ASD.RESERVED.4` | `OaApplicationSearchDesigner_Reserved4` | TField |  |  |
| 15 | `OA.ASD.RESERVED.3` | `OaApplicationSearchDesigner_Reserved3` | TField |  |  |
| 16 | `OA.ASD.RESERVED.2` | `OaApplicationSearchDesigner_Reserved2` | TField |  |  |
| 17 | `OA.ASD.RESERVED.1` | `OaApplicationSearchDesigner_Reserved1` | TField |  |  |
| 18 | `OA.ASD.ACTION` | `OaApplicationSearchDesigner_Action` | TField |  | Option PUBLISH would be allowed in this field and authorization of the record with this option would trigger publishing of this record. |
| 19 | `OA.ASD.PUBLISH.STATUS` | `OaApplicationSearchDesigner_PublishStatus` | TField |  | Noinput, System maintained field - indicating the status of publish action. |
| 20 | `OA.ASD.PUBLISH.DATE` | `OaApplicationSearchDesigner_PublishDate` | TField |  | Noinput, System maintained field - indicating the last published date of this record. |
| 21 | `OA.ASD.PUBLISH.ERROR` | `OaApplicationSearchDesigner_PublishError` |  |  |  |
| 22 | `OA.ASD.ERROR.SUGGESTION` | `OaApplicationSearchDesigner_ErrorSuggestion` |  |  |  |
| 23 | `OA.ASD.REFERENCE` | `OaApplicationSearchDesigner_Reference` | TField |  | Indicates the First part of the @ID - System maintained, Noinput field. |
| 24 | `OA.ASD.VERSION` | `OaApplicationSearchDesigner_Version` | TField |  | Indicates the second part of the @ID - System maintained, Noinput field. |
| 25 | `OA.ASD.LOCAL.REF` | `OaApplicationSearchDesigner_LocalRef` |  |  |  |
| 26 | `OA.ASD.OVERRIDE` | `OaApplicationSearchDesigner_Override` |  |  |  |
| 27 | `OA.ASD.RECORD.STATUS` | `OaApplicationSearchDesigner_RecordStatus` | String |  |  |
| 28 | `OA.ASD.CURR.NO` | `OaApplicationSearchDesigner_CurrNo` | String |  |  |
| 29 | `OA.ASD.INPUTTER` | `OaApplicationSearchDesigner_Inputter` |  |  |  |
| 30 | `OA.ASD.DATE.TIME` | `OaApplicationSearchDesigner_DateTime` |  |  |  |
| 31 | `OA.ASD.AUTHORISER` | `OaApplicationSearchDesigner_Authoriser` | String |  |  |
| 32 | `OA.ASD.CO.CODE` | `OaApplicationSearchDesigner_CoCode` | String |  |  |
| 33 | `OA.ASD.DEPT.CODE` | `OaApplicationSearchDesigner_DeptCode` | String |  |  |
| 34 | `OA.ASD.AUDITOR.CODE` | `OaApplicationSearchDesigner_AuditorCode` | String |  |  |
| 35 | `OA.ASD.AUDIT.DATE.TIME` | `OaApplicationSearchDesigner_AuditDateTime` | String |  |  |
