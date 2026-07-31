# AA.STANDARD.FIELD.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.STANDARD.FIELD.TYPE` in `AA_MarketingCatalogue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.STF.DESCRIPTION` | `AaStandardFieldType_Description` |  |  |  |
| 2 | `AA.STF.FULL.DESCRIPTION` | `AaStandardFieldType_FullDescription` |  |  |  |
| 3 | `AA.STF.FIELD.NAME` | `AaStandardFieldType_FieldName` |  |  |  |
| 4 | `AA.STF.FIELD.DESCRIPTION` | `AaStandardFieldType_FieldDescription` |  |  |  |
| 5 | `AA.STF.CONDITION.DESCRIPTION` | `AaStandardFieldType_ConditionDescription` | TField |  | It accepts YES or NO values. This field decides that FULL.DESCRIPTION of the property condition to be displayed in enquiry screen or not. If it set as YES then FULL.DESCRIPTION defined in property condition will displayed in enquiry screen. If it set as NO then FULL.DESCRIPTION in property condition will not display in enquiry screen. |
| 6 | `AA.STF.RESERVED.5` | `AaStandardFieldType_Reserved5` | TField |  |  |
| 7 | `AA.STF.RESERVED.4` | `AaStandardFieldType_Reserved4` | TField |  |  |
| 8 | `AA.STF.RESERVED.3` | `AaStandardFieldType_Reserved3` | TField |  |  |
| 9 | `AA.STF.RESERVED.2` | `AaStandardFieldType_Reserved2` | TField |  |  |
| 10 | `AA.STF.RESERVED.1` | `AaStandardFieldType_Reserved1` | TField |  |  |
| 11 | `AA.STF.LOCAL.REF` | `AaStandardFieldType_LocalRef` |  |  |  |
| 12 | `AA.STF.OVERRIDE` | `AaStandardFieldType_Override` |  |  |  |
| 13 | `AA.STF.RECORD.STATUS` | `AaStandardFieldType_RecordStatus` | String |  |  |
| 14 | `AA.STF.CURR.NO` | `AaStandardFieldType_CurrNo` | String |  |  |
| 15 | `AA.STF.INPUTTER` | `AaStandardFieldType_Inputter` |  |  |  |
| 16 | `AA.STF.DATE.TIME` | `AaStandardFieldType_DateTime` |  |  |  |
| 17 | `AA.STF.AUTHORISER` | `AaStandardFieldType_Authoriser` | String |  |  |
| 18 | `AA.STF.CO.CODE` | `AaStandardFieldType_CoCode` | String |  |  |
| 19 | `AA.STF.DEPT.CODE` | `AaStandardFieldType_DeptCode` | String |  |  |
| 20 | `AA.STF.AUDITOR.CODE` | `AaStandardFieldType_AuditorCode` | String |  |  |
| 21 | `AA.STF.AUDIT.DATE.TIME` | `AaStandardFieldType_AuditDateTime` | String |  |  |
