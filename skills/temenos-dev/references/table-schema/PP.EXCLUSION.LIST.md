# PP.EXCLUSION.LIST — Table Schema

> Source: `INSERTS/I_F.PP.EXCLUSION.LIST` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.EXL.BICCode` | `PpExclusionList_Biccode` | TField |  | Participant�s BIC Validation Rules: 35 alphanumeric characters. |
| 2 | `PP.EXL.OverrideThroughUpload` | `PpExclusionList_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process. |
| 3 | `PP.EXL.SourceKey` | `PpExclusionList_Sourcekey` | TField |  | System generated number. Not for user input. |
| 4 | `PP.EXL.RESERVED.5` | `PpExclusionList_Reserved5` | TField |  |  |
| 5 | `PP.EXL.RESERVED.4` | `PpExclusionList_Reserved4` | TField |  |  |
| 6 | `PP.EXL.RESERVED.3` | `PpExclusionList_Reserved3` | TField |  |  |
| 7 | `PP.EXL.RESERVED.2` | `PpExclusionList_Reserved2` | TField |  |  |
| 8 | `PP.EXL.RESERVED.1` | `PpExclusionList_Reserved1` | TField |  |  |
| 9 | `PP.EXL.LOCAL.REF` | `PpExclusionList_LocalRef` |  |  |  |
| 10 | `PP.EXL.OVERRIDE` | `PpExclusionList_Override` |  |  |  |
| 11 | `PP.EXL.RECORD.STATUS` | `PpExclusionList_RecordStatus` | String |  |  |
| 12 | `PP.EXL.CURR.NO` | `PpExclusionList_CurrNo` | String |  |  |
| 13 | `PP.EXL.INPUTTER` | `PpExclusionList_Inputter` |  |  |  |
| 14 | `PP.EXL.DATE.TIME` | `PpExclusionList_DateTime` |  |  |  |
| 15 | `PP.EXL.AUTHORISER` | `PpExclusionList_Authoriser` | String |  |  |
| 16 | `PP.EXL.CO.CODE` | `PpExclusionList_CoCode` | String |  |  |
| 17 | `PP.EXL.DEPT.CODE` | `PpExclusionList_DeptCode` | String |  |  |
| 18 | `PP.EXL.AUDITOR.CODE` | `PpExclusionList_AuditorCode` | String |  |  |
| 19 | `PP.EXL.AUDIT.DATE.TIME` | `PpExclusionList_AuditDateTime` | String |  |  |
