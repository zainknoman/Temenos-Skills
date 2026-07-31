# DX.OPTION.TYPE — Table Schema

> Source: `INSERTS/I_F.DX.OPTION.TYPE` in `DX_Configuration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.OT.DESCRIPTION` | `DxOptionType_Description` |  |  |  |
| 2 | `DX.OT.SHORT.DESC` | `DxOptionType_ShortDesc` |  |  |  |
| 3 | `DX.OT.EXERCISE.EXPIRE` | `DxOptionType_ExerciseExpire` | TField |  | The exotic options set with EXERCISE are meant as KICKIN events and set to EXPIRE meant as KNOCKOUT events. Allowed values to this field are EXERCISE, EXPIRE and NULL. |
| 4 | `DX.OT.BARRIER.OR.TRIGGER` | `DxOptionType_BarrierOrTrigger` | TField |  | The field denotes whether the defined option is a barrier or trigger type of field. Validation Rules: NOCHANGE field. Trigger - As per Mt 2023 Swift Standards, Trigger event is removed. If Trigger is selected, system will convert to Barrier type. |
| 5 | `DX.OT.UPPER.OR.LOWER` | `DxOptionType_UpperOrLower` | TField |  | The field denotes whether the option type is used to define the upper or lower value. Validation Rules: NOCHANGE field.When value in this field then USR.FLD.TYPE can hold only the value as PRICE. |
| 6 | `DX.OT.RESERVED.12` | `DxOptionType_Reserved12` |  |  |  |
| 7 | `DX.OT.RESERVED.11` | `DxOptionType_Reserved11` |  |  |  |
| 8 | `DX.OT.RESERVED.10` | `DxOptionType_Reserved10` | TField |  |  |
| 9 | `DX.OT.RESERVED.09` | `DxOptionType_Reserved09` | TField |  |  |
| 10 | `DX.OT.RESERVED.08` | `DxOptionType_Reserved08` | TField |  |  |
| 11 | `DX.OT.USR.FLD.NAME` | `DxOptionType_UsrFldName` |  |  |  |
| 12 | `DX.OT.USR.FLD.TYPE` | `DxOptionType_UsrFldType` |  |  |  |
| 13 | `DX.OT.USR.FLD.TEXT` | `DxOptionType_UsrFldText` |  |  |  |
| 14 | `DX.OT.USR.FLD.PRICE` | `DxOptionType_UsrFldPrice` |  |  |  |
| 15 | `DX.OT.USR.FLD.MIN` | `DxOptionType_UsrFldMin` |  |  |  |
| 16 | `DX.OT.USR.FLD.MAX` | `DxOptionType_UsrFldMax` |  |  |  |
| 17 | `DX.OT.USR.RSVD.01` | `DxOptionType_UsrRsvd01` |  |  |  |
| 18 | `DX.OT.RESERVED.07` | `DxOptionType_Reserved07` | TField |  |  |
| 19 | `DX.OT.CO.PGM` | `DxOptionType_CoPgm` | TField |  | A user defined program or API which is triggered during closeout processing when the EXOTIC.EVENT flag is set ona DX.ORDER or DX.TRADE record associated with this option type. Validation Rules: Must be a valid record on DX.OBJECT.LIBRARY |
| 20 | `DX.OT.RESERVED.06` | `DxOptionType_Reserved06` | TField |  |  |
| 21 | `DX.OT.RESERVED.05` | `DxOptionType_Reserved05` | TField |  |  |
| 22 | `DX.OT.RESERVED.04` | `DxOptionType_Reserved04` | TField |  |  |
| 23 | `DX.OT.RESERVED.03` | `DxOptionType_Reserved03` | TField |  |  |
| 24 | `DX.OT.RESERVED.02` | `DxOptionType_Reserved02` | TField |  |  |
| 25 | `DX.OT.RESERVED.01` | `DxOptionType_Reserved01` | TField |  |  |
| 26 | `DX.OT.LOCAL.REF` | `DxOptionType_LocalRef` |  |  |  |
| 27 | `DX.OT.OVERRIDE` | `DxOptionType_Override` |  |  |  |
| 28 | `DX.OT.RECORD.STATUS` | `DxOptionType_RecordStatus` | String |  |  |
| 29 | `DX.OT.CURR.NO` | `DxOptionType_CurrNo` | String |  |  |
| 30 | `DX.OT.INPUTTER` | `DxOptionType_Inputter` |  |  |  |
| 31 | `DX.OT.DATE.TIME` | `DxOptionType_DateTime` |  |  |  |
| 32 | `DX.OT.AUTHORISER` | `DxOptionType_Authoriser` | String |  |  |
| 33 | `DX.OT.CO.CODE` | `DxOptionType_CoCode` | String |  |  |
| 34 | `DX.OT.DEPT.CODE` | `DxOptionType_DeptCode` | String |  |  |
| 35 | `DX.OT.AUDITOR.CODE` | `DxOptionType_AuditorCode` | String |  |  |
| 36 | `DX.OT.AUDIT.DATE.TIME` | `DxOptionType_AuditDateTime` | String |  |  |
