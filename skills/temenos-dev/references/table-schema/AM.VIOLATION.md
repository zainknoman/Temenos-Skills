# AM.VIOLATION — Table Schema

> Source: `INSERTS/I_F.AM.VIOLATION` in `AM_ModellingConstraints.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.VIO.TYPE` | `AmViolation_Type` | TField |  | The type of violation that has occurred, i.e. what triggered the violation. |
| 2 | `AM.VIO.SEC.CONSTRAINT` | `AmViolation_SecConstraint` | TField |  | Record key for the SC.SECURITY.CONSTRAINT record that triggered this violation (if applicable). |
| 3 | `AM.VIO.SEVERITY` | `AmViolation_Severity` | TField |  | Type of constraint triggered - error or override. |
| 4 | `AM.VIO.MSG.TXT` | `AmViolation_MsgTxt` | TField |  | Override or error message narrative. |
| 5 | `AM.VIO.MANUAL.OVR` | `AmViolation_ManualOvr` | TField |  | This field allows manual override of the violation to enable processing to continue. |
| 6 | `AM.VIO.RESTRICTION` | `AmViolation_Restriction` | TField |  | Restriction ID. |
| 7 | `AM.VIO.RESTRICTION.KEY` | `AmViolation_RestrictionKey` | TField |  | Record key for the restriction. |
| 8 | `AM.VIO.VIEW.MARKER` | `AmViolation_ViewMarker` | TField |  | Shows who last viewed this record and when it was viewed. |
| 9 | `AM.VIO.REVIEW.MARKER` | `AmViolation_ReviewMarker` | TField |  | Marker to show that this violation needs to be reviewed. |
| 10 | `AM.VIO.REASON.TYPE` | `AmViolation_ReasonType` | TField |  | Defaulted from the field RESON.TYPE in AM.SCENARIO application. Validation Rules: a NOINPUT field |
| 11 | `AM.VIO.REASON.TYPE.DESC` | `AmViolation_ReasonTypeDesc` | TField |  | Default the value from REASON.TYPE.DESC field of AM.SCENARIO application. Validation Rules: a NOINPUT field. |
| 12 | `AM.VIO.RESERVED.04` | `AmViolation_Reserved04` | TField |  | Reserved for future use. |
| 13 | `AM.VIO.RESERVED.03` | `AmViolation_Reserved03` | TField |  | Reserved for future use. |
| 14 | `AM.VIO.RESERVED.02` | `AmViolation_Reserved02` | TField |  | Reserved for future use. |
| 15 | `AM.VIO.RESERVED.01` | `AmViolation_Reserved01` | TField |  | Reserved for future use. |
| 16 | `AM.VIO.LOCAL.REF` | `AmViolation_LocalRef` |  |  |  |
| 17 | `AM.VIO.RECORD.STATUS` | `AmViolation_RecordStatus` | String |  |  |
| 18 | `AM.VIO.CURR.NO` | `AmViolation_CurrNo` | String |  |  |
| 19 | `AM.VIO.INPUTTER` | `AmViolation_Inputter` |  |  |  |
| 20 | `AM.VIO.DATE.TIME` | `AmViolation_DateTime` |  |  |  |
| 21 | `AM.VIO.AUTHORISER` | `AmViolation_Authoriser` | String |  |  |
| 22 | `AM.VIO.CO.CODE` | `AmViolation_CoCode` | String |  |  |
| 23 | `AM.VIO.DEPT.CODE` | `AmViolation_DeptCode` | String |  |  |
| 24 | `AM.VIO.AUDITOR.CODE` | `AmViolation_AuditorCode` | String |  |  |
| 25 | `AM.VIO.AUDIT.DATE.TIME` | `AmViolation_AuditDateTime` | String |  |  |
