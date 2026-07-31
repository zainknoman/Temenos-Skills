# AA.COMMISSION.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.COMMISSION.TYPE` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CMT.DESCRIPTION` | `AaCommissionType_Description` |  |  |  |
| 2 | `AA.CMT.CONTEXT.TYPE` | `AaCommissionType_ContextType` |  |  |  |
| 3 | `AA.CMT.SOURCE.TYPE` | `AaCommissionType_SourceType` |  |  |  |
| 4 | `AA.CMT.SOURCE.BALANCE` | `AaCommissionType_SourceBalance` |  |  |  |
| 5 | `AA.CMT.SOURCE.PROPERTY` | `AaCommissionType_SourceProperty` |  |  |  |
| 6 | `AA.CMT.RESERVED.5` | `AaCommissionType_Reserved5` | TField |  |  |
| 7 | `AA.CMT.RESERVED.4` | `AaCommissionType_Reserved4` | TField |  |  |
| 8 | `AA.CMT.RESERVED.3` | `AaCommissionType_Reserved3` | TField |  |  |
| 9 | `AA.CMT.RESERVED.2` | `AaCommissionType_Reserved2` | TField |  |  |
| 10 | `AA.CMT.RESERVED.1` | `AaCommissionType_Reserved1` | TField |  |  |
| 11 | `AA.CMT.LOCAL.REF` | `AaCommissionType_LocalRef` |  |  |  |
| 12 | `AA.CMT.OVERRIDE` | `AaCommissionType_Override` |  |  |  |
| 13 | `AA.CMT.RECORD.STATUS` | `AaCommissionType_RecordStatus` | String |  |  |
| 14 | `AA.CMT.CURR.NO` | `AaCommissionType_CurrNo` | String |  |  |
| 15 | `AA.CMT.INPUTTER` | `AaCommissionType_Inputter` |  |  |  |
| 16 | `AA.CMT.DATE.TIME` | `AaCommissionType_DateTime` |  |  |  |
| 17 | `AA.CMT.AUTHORISER` | `AaCommissionType_Authoriser` | String |  |  |
| 18 | `AA.CMT.CO.CODE` | `AaCommissionType_CoCode` | String |  |  |
| 19 | `AA.CMT.DEPT.CODE` | `AaCommissionType_DeptCode` | String |  |  |
| 20 | `AA.CMT.AUDITOR.CODE` | `AaCommissionType_AuditorCode` | String |  |  |
| 21 | `AA.CMT.AUDIT.DATE.TIME` | `AaCommissionType_AuditDateTime` | String |  |  |
