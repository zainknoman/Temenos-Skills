# RFR.CONDITION — Table Schema

> Source: `INSERTS/I_F.RFR.CONDITION` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RFR.CON.DESCRIPTION` | `RfrCondition_Description` |  |  |  |
| 2 | `RFR.CON.EXC.APPL.FIELD` | `RfrCondition_ExcApplField` |  |  |  |
| 3 | `RFR.CON.EXC.FLD.OPERAND` | `RfrCondition_ExcFldOperand` |  |  |  |
| 4 | `RFR.CON.EXC.VALUE.FROM` | `RfrCondition_ExcValueFrom` |  |  |  |
| 5 | `RFR.CON.EXC.VALUE.TO` | `RfrCondition_ExcValueTo` |  |  |  |
| 6 | `RFR.CON.EXC.FLD.OPERATION` | `RfrCondition_ExcFldOperation` |  |  |  |
| 7 | `RFR.CON.DFLT.RFR.PI.KEY` | `RfrCondition_DfltRfrPiKey` | TField | Yes | Default New PI key to be used for the contracts which does not falls in below condition. Validation rule: Mandatory input |
| 8 | `RFR.CON.DFLT.DELTA.SPREAD` | `RfrCondition_DfltDeltaSpread` | TField |  | Default New Spread to be used for the migration contracts |
| 9 | `RFR.CON.RFR.PI.KEY` | `RfrCondition_RfrPiKey` |  |  |  |
| 10 | `RFR.CON.RFR.DELTA.SPREAD` | `RfrCondition_RfrDeltaSpread` |  |  |  |
| 11 | `RFR.CON.APPL.FIELD.NAME` | `RfrCondition_ApplFieldName` |  |  |  |
| 12 | `RFR.CON.FIELD.OPERAND` | `RfrCondition_FieldOperand` |  |  |  |
| 13 | `RFR.CON.VALUE.FROM` | `RfrCondition_ValueFrom` |  |  |  |
| 14 | `RFR.CON.VALUE.TO` | `RfrCondition_ValueTo` |  |  |  |
| 15 | `RFR.CON.FIELD.OPERATION` | `RfrCondition_FieldOperation` |  |  |  |
| 16 | `RFR.CON.RESERVED.6` | `RfrCondition_Reserved6` | TField |  |  |
| 17 | `RFR.CON.RESERVED.5` | `RfrCondition_Reserved5` | TField |  |  |
| 18 | `RFR.CON.RESERVED.4` | `RfrCondition_Reserved4` | TField |  |  |
| 19 | `RFR.CON.RESERVED.3` | `RfrCondition_Reserved3` | TField |  |  |
| 20 | `RFR.CON.RESERVED.2` | `RfrCondition_Reserved2` | TField |  |  |
| 21 | `RFR.CON.RESERVED.1` | `RfrCondition_Reserved1` | TField |  |  |
| 22 | `RFR.CON.LOCAL.REF` | `RfrCondition_LocalRef` |  |  |  |
| 23 | `RFR.CON.OVERRIDE` | `RfrCondition_Override` |  |  |  |
| 24 | `RFR.CON.RECORD.STATUS` | `RfrCondition_RecordStatus` | String |  |  |
| 25 | `RFR.CON.CURR.NO` | `RfrCondition_CurrNo` | String |  |  |
| 26 | `RFR.CON.INPUTTER` | `RfrCondition_Inputter` |  |  |  |
| 27 | `RFR.CON.DATE.TIME` | `RfrCondition_DateTime` |  |  |  |
| 28 | `RFR.CON.AUTHORISER` | `RfrCondition_Authoriser` | String |  |  |
| 29 | `RFR.CON.CO.CODE` | `RfrCondition_CoCode` | String |  |  |
| 30 | `RFR.CON.DEPT.CODE` | `RfrCondition_DeptCode` | String |  |  |
| 31 | `RFR.CON.AUDITOR.CODE` | `RfrCondition_AuditorCode` | String |  |  |
| 32 | `RFR.CON.AUDIT.DATE.TIME` | `RfrCondition_AuditDateTime` | String |  |  |
| 33 | `RFR.CON.RFR.INT.PROPERTY` | `RfrCondition_RfrIntProperty` |  |  |  |
