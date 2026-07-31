# OA.FORM.REPLICATE — Table Schema

> Source: `INSERTS/I_F.OA.FORM.REPLICATE` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.FRE.DESCRIPTION` | `OaFormReplicate_Description` |  |  |  |
| 2 | `OA.FRE.FULL.DESCRIPTION` | `OaFormReplicate_FullDescription` |  |  |  |
| 3 | `OA.FRE.INSTANCE` | `OaFormReplicate_Instance` |  |  |  |
| 4 | `OA.FRE.MAP.FIELD` | `OaFormReplicate_MapField` |  |  |  |
| 5 | `OA.FRE.MAP.RESTRICT.FIELD` | `OaFormReplicate_MapRestrictField` |  |  |  |
| 6 | `OA.FRE.RESERVED.5` | `OaFormReplicate_Reserved5` |  |  |  |
| 7 | `OA.FRE.RESERVED.4` | `OaFormReplicate_Reserved4` | TField |  |  |
| 8 | `OA.FRE.RESERVED.3` | `OaFormReplicate_Reserved3` | TField |  |  |
| 9 | `OA.FRE.RESERVED.2` | `OaFormReplicate_Reserved2` | TField |  |  |
| 10 | `OA.FRE.RESERVED.1` | `OaFormReplicate_Reserved1` | TField |  |  |
| 11 | `OA.FRE.LOCAL.REF` | `OaFormReplicate_LocalRef` |  |  |  |
| 12 | `OA.FRE.OVERRIDE` | `OaFormReplicate_Override` |  |  |  |
| 13 | `OA.FRE.RECORD.STATUS` | `OaFormReplicate_RecordStatus` | String |  |  |
| 14 | `OA.FRE.CURR.NO` | `OaFormReplicate_CurrNo` | String |  |  |
| 15 | `OA.FRE.INPUTTER` | `OaFormReplicate_Inputter` |  |  |  |
| 16 | `OA.FRE.DATE.TIME` | `OaFormReplicate_DateTime` |  |  |  |
| 17 | `OA.FRE.AUTHORISER` | `OaFormReplicate_Authoriser` | String |  |  |
| 18 | `OA.FRE.CO.CODE` | `OaFormReplicate_CoCode` | String |  |  |
| 19 | `OA.FRE.DEPT.CODE` | `OaFormReplicate_DeptCode` | String |  |  |
| 20 | `OA.FRE.AUDITOR.CODE` | `OaFormReplicate_AuditorCode` | String |  |  |
| 21 | `OA.FRE.AUDIT.DATE.TIME` | `OaFormReplicate_AuditDateTime` | String |  |  |
