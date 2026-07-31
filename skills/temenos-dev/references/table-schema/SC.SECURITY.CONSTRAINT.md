# SC.SECURITY.CONSTRAINT — Table Schema

> Source: `INSERTS/I_F.SC.SECURITY.CONSTRAINT` in `SC_SctConstraints.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SCO.DESCRIPTION` | `ScSecurityConstraint_Description` |  |  |  |
| 2 | `SC.SCO.NATIONALITY` | `ScSecurityConstraint_Nationality` |  |  |  |
| 3 | `SC.SCO.RESIDENCE` | `ScSecurityConstraint_Residence` |  |  |  |
| 4 | `SC.SCO.APP.APPLI` | `ScSecurityConstraint_AppAppli` |  |  |  |
| 5 | `SC.SCO.APP.FIELD` | `ScSecurityConstraint_AppField` |  |  |  |
| 6 | `SC.SCO.APP.OPERAND` | `ScSecurityConstraint_AppOperand` |  |  |  |
| 7 | `SC.SCO.APP.VALUE` | `ScSecurityConstraint_AppValue` |  |  |  |
| 8 | `SC.SCO.VALIDITY.DATE` | `ScSecurityConstraint_ValidityDate` |  |  |  |
| 9 | `SC.SCO.DIRECTION` | `ScSecurityConstraint_Direction` |  |  |  |
| 10 | `SC.SCO.APPLICATION` | `ScSecurityConstraint_Application` |  |  |  |
| 11 | `SC.SCO.RESTRICTION` | `ScSecurityConstraint_Restriction` |  |  |  |
| 12 | `SC.SCO.SEPARATOR` | `ScSecurityConstraint_Separator` | TField |  | This is the type of separator that will be used to determine multiple values in one field. The fields that allow the use of the separator are : Validation Rules: * (Asterisk) , (Comma) . (Full Stop) / (Forward Slash) NULL |
| 13 | `SC.SCO.RESTRICTION.KEY` | `ScSecurityConstraint_RestrictionKey` |  |  |  |
| 14 | `SC.SCO.RESTRICT.DESC` | `ScSecurityConstraint_RestrictDesc` |  |  |  |
| 15 | `SC.SCO.RESTRICT.TYPE` | `ScSecurityConstraint_RestrictType` |  |  |  |
| 16 | `SC.SCO.RANGE` | `ScSecurityConstraint_Range` |  |  |  |
| 17 | `SC.SCO.AMOUNT` | `ScSecurityConstraint_Amount` |  |  |  |
| 18 | `SC.SCO.AMOUNT.CCY` | `ScSecurityConstraint_AmountCcy` |  |  |  |
| 19 | `SC.SCO.REST.GROUP` | `ScSecurityConstraint_RestGroup` |  |  |  |
| 20 | `SC.SCO.HOLD.GROUP` | `ScSecurityConstraint_HoldGroup` |  |  |  |
| 21 | `SC.SCO.TEMP.FIELD` | `ScSecurityConstraint_TempField` |  |  |  |
| 22 | `SC.SCO.REST.APPLI` | `ScSecurityConstraint_RestAppli` |  |  |  |
| 23 | `SC.SCO.REST.FIELD` | `ScSecurityConstraint_RestField` |  |  |  |
| 24 | `SC.SCO.REST.OPERAND` | `ScSecurityConstraint_RestOperand` |  |  |  |
| 25 | `SC.SCO.RSTVAL.FILE` | `ScSecurityConstraint_RstvalFile` |  |  |  |
| 26 | `SC.SCO.RSTVAL.KEY` | `ScSecurityConstraint_RstvalKey` |  |  |  |
| 27 | `SC.SCO.RSTVAL.FIELD` | `ScSecurityConstraint_RstvalField` |  |  |  |
| 28 | `SC.SCO.REST.VALUE` | `ScSecurityConstraint_RestValue` |  |  |  |
| 29 | `SC.SCO.REST.LOGIC` | `ScSecurityConstraint_RestLogic` |  |  |  |
| 30 | `SC.SCO.RESERVED.10` | `ScSecurityConstraint_Reserved10` |  |  |  |
| 31 | `SC.SCO.RESERVED.9` | `ScSecurityConstraint_Reserved9` |  |  |  |
| 32 | `SC.SCO.RESERVED.8` | `ScSecurityConstraint_Reserved8` |  |  |  |
| 33 | `SC.SCO.HOLD.FIELD` | `ScSecurityConstraint_HoldField` |  |  |  |
| 34 | `SC.SCO.HOLD.OPERAND` | `ScSecurityConstraint_HoldOperand` |  |  |  |
| 35 | `SC.SCO.HLDVAL.FILE` | `ScSecurityConstraint_HldvalFile` |  |  |  |
| 36 | `SC.SCO.HLDVAL.KEY` | `ScSecurityConstraint_HldvalKey` |  |  |  |
| 37 | `SC.SCO.HLDVAL.FIELD` | `ScSecurityConstraint_HldvalField` |  |  |  |
| 38 | `SC.SCO.HOLD.VALUE` | `ScSecurityConstraint_HoldValue` |  |  |  |
| 39 | `SC.SCO.HOLD.LOGIC` | `ScSecurityConstraint_HoldLogic` |  |  |  |
| 40 | `SC.SCO.RESERVED.7` | `ScSecurityConstraint_Reserved7` |  |  |  |
| 41 | `SC.SCO.RESERVED.6` | `ScSecurityConstraint_Reserved6` |  |  |  |
| 42 | `SC.SCO.RESERVED.5` | `ScSecurityConstraint_Reserved5` |  |  |  |
| 43 | `SC.SCO.SUBROUTINE` | `ScSecurityConstraint_Subroutine` |  |  |  |
| 44 | `SC.SCO.VALUATION.BASIS` | `ScSecurityConstraint_ValuationBasis` |  |  |  |
| 45 | `SC.SCO.OVERRIDE.ERROR` | `ScSecurityConstraint_OverrideError` |  |  |  |
| 46 | `SC.SCO.OVERRIDE.MSG` | `ScSecurityConstraint_OverrideMsg` |  |  |  |
| 47 | `SC.SCO.OVERRIDE.TXT` | `ScSecurityConstraint_OverrideTxt` |  |  |  |
| 48 | `SC.SCO.CONSTRAINT.TYPE` | `ScSecurityConstraint_ConstraintType` | TField |  | Can be either Permission or Restriction. If set to Permission then the system can automatically allow the transaction if setup to do so. |
| 49 | `SC.SCO.RESERVED.4` | `ScSecurityConstraint_Reserved4` | TField |  |  |
| 50 | `SC.SCO.RESERVED.3` | `ScSecurityConstraint_Reserved3` | TField |  |  |
| 51 | `SC.SCO.RESERVED.2` | `ScSecurityConstraint_Reserved2` | TField |  |  |
| 52 | `SC.SCO.RESERVED.1` | `ScSecurityConstraint_Reserved1` | TField |  |  |
| 53 | `SC.SCO.LOCAL.REF` | `ScSecurityConstraint_LocalRef` |  |  |  |
| 54 | `SC.SCO.RECORD.STATUS` | `ScSecurityConstraint_RecordStatus` | String |  |  |
| 55 | `SC.SCO.CURR.NO` | `ScSecurityConstraint_CurrNo` | String |  |  |
| 56 | `SC.SCO.INPUTTER` | `ScSecurityConstraint_Inputter` |  |  |  |
| 57 | `SC.SCO.DATE.TIME` | `ScSecurityConstraint_DateTime` |  |  |  |
| 58 | `SC.SCO.AUTHORISER` | `ScSecurityConstraint_Authoriser` | String |  |  |
| 59 | `SC.SCO.CO.CODE` | `ScSecurityConstraint_CoCode` | String |  |  |
| 60 | `SC.SCO.DEPT.CODE` | `ScSecurityConstraint_DeptCode` | String |  |  |
| 61 | `SC.SCO.AUDITOR.CODE` | `ScSecurityConstraint_AuditorCode` | String |  |  |
| 62 | `SC.SCO.AUDIT.DATE.TIME` | `ScSecurityConstraint_AuditDateTime` | String |  |  |
