# HOLD.GROUP.DEFAULT.PARAM — Table Schema

> Source: `INSERTS/I_F.HOLD.GROUP.DEFAULT.PARAM` in `NACUST_CustomerHolds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HLD.GRP.DECISION.FIELD.NAME` | `HoldGroupDefaultParam_DecisionFieldName` |  |  |  |
| 2 | `HLD.GRP.DECISION.OPERAND` | `HoldGroupDefaultParam_DecisionOperand` |  |  |  |
| 3 | `HLD.GRP.DECISION.FROM` | `HoldGroupDefaultParam_DecisionFrom` |  |  |  |
| 4 | `HLD.GRP.DECISION.TO` | `HoldGroupDefaultParam_DecisionTo` |  |  |  |
| 5 | `HLD.GRP.OWNERS.CHECK` | `HoldGroupDefaultParam_OwnersCheck` |  |  |  |
| 6 | `HLD.GRP.PRO.DES.FLD.NAME` | `HoldGroupDefaultParam_ProDesFldName` |  |  |  |
| 7 | `HLD.GRP.PRO.DES.FLD.VALUE` | `HoldGroupDefaultParam_ProDesFldValue` |  |  |  |
| 8 | `HLD.GRP.PROF.FLD.TO.CHK` | `HoldGroupDefaultParam_ProfFldToChk` |  |  |  |
| 9 | `HLD.GRP.PROFILE.FLD.OPTION` | `HoldGroupDefaultParam_ProfileFldOption` |  |  |  |
| 10 | `HLD.GRP.HOLD.GROUP` | `HoldGroupDefaultParam_HoldGroup` |  |  |  |
| 11 | `HLD.GRP.FIELD.NAME` | `HoldGroupDefaultParam_FieldName` |  |  |  |
| 12 | `HLD.GRP.FIELD.OPERAND` | `HoldGroupDefaultParam_FieldOperand` |  |  |  |
| 13 | `HLD.GRP.FIELD.FROM` | `HoldGroupDefaultParam_FieldFrom` |  |  |  |
| 14 | `HLD.GRP.FIELD.TO` | `HoldGroupDefaultParam_FieldTo` |  |  |  |
| 15 | `HLD.GRP.RESERVED.5` | `HoldGroupDefaultParam_Reserved5` | TField |  |  |
| 16 | `HLD.GRP.RESERVED.4` | `HoldGroupDefaultParam_Reserved4` | TField |  |  |
| 17 | `HLD.GRP.RESERVED.3` | `HoldGroupDefaultParam_Reserved3` | TField |  |  |
| 18 | `HLD.GRP.RESERVED.2` | `HoldGroupDefaultParam_Reserved2` | TField |  |  |
| 19 | `HLD.GRP.RESERVED.1` | `HoldGroupDefaultParam_Reserved1` | TField |  |  |
| 20 | `HLD.GRP.OVERRIDE` | `HoldGroupDefaultParam_Override` |  |  |  |
| 21 | `HLD.GRP.RECORD.STATUS` | `HoldGroupDefaultParam_RecordStatus` | String |  |  |
| 22 | `HLD.GRP.CURR.NO` | `HoldGroupDefaultParam_CurrNo` | String |  |  |
| 23 | `HLD.GRP.INPUTTER` | `HoldGroupDefaultParam_Inputter` |  |  |  |
| 24 | `HLD.GRP.DATE.TIME` | `HoldGroupDefaultParam_DateTime` |  |  |  |
| 25 | `HLD.GRP.AUTHORISER` | `HoldGroupDefaultParam_Authoriser` | String |  |  |
| 26 | `HLD.GRP.CO.CODE` | `HoldGroupDefaultParam_CoCode` | String |  |  |
| 27 | `HLD.GRP.DEPT.CODE` | `HoldGroupDefaultParam_DeptCode` | String |  |  |
| 28 | `HLD.GRP.AUDITOR.CODE` | `HoldGroupDefaultParam_AuditorCode` | String |  |  |
| 29 | `HLD.GRP.AUDIT.DATE.TIME` | `HoldGroupDefaultParam_AuditDateTime` | String |  |  |
