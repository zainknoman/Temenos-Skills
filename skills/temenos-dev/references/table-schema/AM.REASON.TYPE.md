# AM.REASON.TYPE — Table Schema

> Source: `INSERTS/I_F.AM.REASON.TYPE` in `AM_ModellingConstraints.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.ART.SHORT.DESCRIPTION` | `AmReasonType_ShortDescription` |  |  |  |
| 2 | `AM.ART.DESCRIPTION` | `AmReasonType_Description` |  |  |  |
| 3 | `AM.ART.REASON.TYPE` | `AmReasonType_ReasonType` | TField |  | Holds the reason type. Holds values using EB.LOOKUP application. Validation Rules: Alphabetic |
| 4 | `AM.ART.RESERVED.06` | `AmReasonType_Reserved06` | TField |  |  |
| 5 | `AM.ART.RESERVED.05` | `AmReasonType_Reserved05` | TField |  |  |
| 6 | `AM.ART.RESERVED.04` | `AmReasonType_Reserved04` | TField |  |  |
| 7 | `AM.ART.RESERVED.03` | `AmReasonType_Reserved03` | TField |  |  |
| 8 | `AM.ART.RESERVED.02` | `AmReasonType_Reserved02` | TField |  |  |
| 9 | `AM.ART.RESERVED.01` | `AmReasonType_Reserved01` | TField |  |  |
| 10 | `AM.ART.LOCAL.REF` | `AmReasonType_LocalRef` |  |  |  |
| 11 | `AM.ART.OVERRIDE` | `AmReasonType_Override` |  |  |  |
| 12 | `AM.ART.RECORD.STATUS` | `AmReasonType_RecordStatus` | String |  |  |
| 13 | `AM.ART.CURR.NO` | `AmReasonType_CurrNo` | String |  |  |
| 14 | `AM.ART.INPUTTER` | `AmReasonType_Inputter` |  |  |  |
| 15 | `AM.ART.DATE.TIME` | `AmReasonType_DateTime` |  |  |  |
| 16 | `AM.ART.AUTHORISER` | `AmReasonType_Authoriser` | String |  |  |
| 17 | `AM.ART.CO.CODE` | `AmReasonType_CoCode` | String |  |  |
| 18 | `AM.ART.DEPT.CODE` | `AmReasonType_DeptCode` | String |  |  |
| 19 | `AM.ART.AUDITOR.CODE` | `AmReasonType_AuditorCode` | String |  |  |
| 20 | `AM.ART.AUDIT.DATE.TIME` | `AmReasonType_AuditDateTime` | String |  |  |
