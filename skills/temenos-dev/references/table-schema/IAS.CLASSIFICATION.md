# IAS.CLASSIFICATION — Table Schema

> Source: `INSERTS/I_F.IAS.CLASSIFICATION` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IASC.DESCRIPTION` | `IasClassification_Description` |  |  |  |
| 2 | `IASC.RESERVED.5` | `IasClassification_Reserved5` | TField |  |  |
| 3 | `IASC.RESERVED.4` | `IasClassification_Reserved4` | TField |  |  |
| 4 | `IASC.RESERVED.3` | `IasClassification_Reserved3` | TField |  |  |
| 5 | `IASC.RESERVED.2` | `IasClassification_Reserved2` | TField |  |  |
| 6 | `IASC.RESERVED.1` | `IasClassification_Reserved1` | TField |  |  |
| 7 | `IASC.LOCAL.REF` | `IasClassification_LocalRef` |  |  |  |
| 8 | `IASC.OVERRIDE` | `IasClassification_Override` |  |  |  |
| 9 | `IASC.RECORD.STATUS` | `IasClassification_RecordStatus` | String |  |  |
| 10 | `IASC.CURR.NO` | `IasClassification_CurrNo` | String |  |  |
| 11 | `IASC.INPUTTER` | `IasClassification_Inputter` |  |  |  |
| 12 | `IASC.DATE.TIME` | `IasClassification_DateTime` |  |  |  |
| 13 | `IASC.AUTHORISER` | `IasClassification_Authoriser` | String |  |  |
| 14 | `IASC.CO.CODE` | `IasClassification_CoCode` | String |  |  |
| 15 | `IASC.DEPT.CODE` | `IasClassification_DeptCode` | String |  |  |
| 16 | `IASC.AUDITOR.CODE` | `IasClassification_AuditorCode` | String |  |  |
| 17 | `IASC.AUDIT.DATE.TIME` | `IasClassification_AuditDateTime` | String |  |  |
