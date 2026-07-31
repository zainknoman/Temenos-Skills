# BL.BATCH.CONDITIONS — Table Schema

> Source: `INSERTS/I_F.BL.BATCH.CONDITIONS` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.BC.DESCRIPTION` | `BlBatchConditions_Description` |  |  |  |
| 2 | `BL.BC.RESERVED7` | `BlBatchConditions_Reserved7` | TField |  |  |
| 3 | `BL.BC.RESERVED6` | `BlBatchConditions_Reserved6` | TField |  |  |
| 4 | `BL.BC.DEF.BL.TYPE` | `BlBatchConditions_DefBlType` | TField | Yes | Specifies the default product type to be used when conditions defined to determine product type is not satisfied. Validation Rules: Must be valid product from BL.TYPE. Not allowed when ID ACTION = "BATCH". Mandatory when ID ACTION = "PRODUCT". |
| 5 | `BL.BC.MAND.COND` | `BlBatchConditions_MandCond` |  |  |  |
| 6 | `BL.BC.BL.TYPE` | `BlBatchConditions_BlType` |  |  |  |
| 7 | `BL.BC.DECIS.FIELD` | `BlBatchConditions_DecisField` |  |  |  |
| 8 | `BL.BC.DECISION` | `BlBatchConditions_Decision` |  |  |  |
| 9 | `BL.BC.DECISION.FR` | `BlBatchConditions_DecisionFr` |  |  |  |
| 10 | `BL.BC.DECISION.TO` | `BlBatchConditions_DecisionTo` |  |  |  |
| 11 | `BL.BC.RESERVED5` | `BlBatchConditions_Reserved5` | TField |  |  |
| 12 | `BL.BC.RESERVED4` | `BlBatchConditions_Reserved4` | TField |  |  |
| 13 | `BL.BC.RESERVED3` | `BlBatchConditions_Reserved3` | TField |  |  |
| 14 | `BL.BC.RESERVED2` | `BlBatchConditions_Reserved2` | TField |  |  |
| 15 | `BL.BC.RESERVED1` | `BlBatchConditions_Reserved1` | TField |  |  |
| 16 | `BL.BC.LOCAL.REF` | `BlBatchConditions_LocalRef` |  |  |  |
| 17 | `BL.BC.OVERRIDE` | `BlBatchConditions_Override` |  |  |  |
| 18 | `BL.BC.RECORD.STATUS` | `BlBatchConditions_RecordStatus` | String |  |  |
| 19 | `BL.BC.CURR.NO` | `BlBatchConditions_CurrNo` | String |  |  |
| 20 | `BL.BC.INPUTTER` | `BlBatchConditions_Inputter` |  |  |  |
| 21 | `BL.BC.DATE.TIME` | `BlBatchConditions_DateTime` |  |  |  |
| 22 | `BL.BC.AUTHORISER` | `BlBatchConditions_Authoriser` | String |  |  |
| 23 | `BL.BC.CO.CODE` | `BlBatchConditions_CoCode` | String |  |  |
| 24 | `BL.BC.DEPT.CODE` | `BlBatchConditions_DeptCode` | String |  |  |
| 25 | `BL.BC.AUDITOR.CODE` | `BlBatchConditions_AuditorCode` | String |  |  |
| 26 | `BL.BC.AUDIT.DATE.TIME` | `BlBatchConditions_AuditDateTime` | String |  |  |
