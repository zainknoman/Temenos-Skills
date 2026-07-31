# SEAT.COMPONENT — Table Schema

> Source: `INSERTS/I_F.SEAT.COMPONENT` in `SE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.COM.DESCRIPTION` | `SeatComponent_Description` |  |  |  |
| 2 | `SE.COM.PRODUCT` | `SeatComponent_Product` | TField |  | This field represents the T24 product the component belongs to. Should be a valid T24 product |
| 3 | `SE.COM.NUM.PASS.ARGS` | `SeatComponent_NumPassArgs` | TField | Yes | This field denotes total number of arguments of the component (routine) . Mandatory field |
| 4 | `SE.COM.ARGUMENT.NAME` | `SeatComponent_ArgumentName` |  |  |  |
| 5 | `SE.COM.ARGU.DES` | `SeatComponent_ArguDes` |  |  |  |
| 6 | `SE.COM.ARGUMENT.NUM` | `SeatComponent_ArgumentNum` |  |  |  |
| 7 | `SE.COM.ARG.DIRECTION` | `SeatComponent_ArgDirection` |  |  |  |
| 8 | `SE.COM.WRAP.ROUTINE` | `SeatComponent_WrapRoutine` | TField |  | This field represents the name of the wrapper routine. If some common variables, which are not part of the argument list needs to be passed to the component , a wrapper routine needs to be defined. The wrapper routine contains three arguments, COMPONENT.ID - name of the component ARG.LIST - List of arguments passed to the component COM.LIST - List of common arguments to be used by the routine |
| 9 | `SE.COM.PUBLISHED` | `SeatComponent_Published` | TField |  | This field denotes whether the component has been published. Allowed values are Y or null |
| 10 | `SE.COM.COMMON.ROUTINE` | `SeatComponent_CommonRoutine` | TField | No | This field optionally denotes the name of a Common routine for use with the component. If specified, this field should contain an alphanumeric name not exceeding 35 characters in length. |
| 11 | `SE.COM.JAVA.ROUTINE` | `SeatComponent_JavaRoutine` | TField |  | This field specifies the type of program call (Basic routine/Java API) If set to YES, then it indicates that the call is to a java program |
| 12 | `SE.COM.RESERVED.8` | `SeatComponent_Reserved8` | TField |  |  |
| 13 | `SE.COM.RESERVED.7` | `SeatComponent_Reserved7` | TField |  |  |
| 14 | `SE.COM.RESERVED.6` | `SeatComponent_Reserved6` | TField |  |  |
| 15 | `SE.COM.RESERVED.5` | `SeatComponent_Reserved5` | TField |  |  |
| 16 | `SE.COM.RESERVED.4` | `SeatComponent_Reserved4` | TField |  |  |
| 17 | `SE.COM.RESERVED.3` | `SeatComponent_Reserved3` | TField |  |  |
| 18 | `SE.COM.RESERVED.2` | `SeatComponent_Reserved2` | TField |  |  |
| 19 | `SE.COM.RESERVED.1` | `SeatComponent_Reserved1` | TField |  |  |
| 20 | `SE.COM.RECORD.STATUS` | `SeatComponent_RecordStatus` | String |  |  |
| 21 | `SE.COM.CURR.NO` | `SeatComponent_CurrNo` | String |  |  |
| 22 | `SE.COM.INPUTTER` | `SeatComponent_Inputter` |  |  |  |
| 23 | `SE.COM.DATE.TIME` | `SeatComponent_DateTime` |  |  |  |
| 24 | `SE.COM.AUTHORISER` | `SeatComponent_Authoriser` | String |  |  |
| 25 | `SE.COM.CO.CODE` | `SeatComponent_CoCode` | String |  |  |
| 26 | `SE.COM.DEPT.CODE` | `SeatComponent_DeptCode` | String |  |  |
| 27 | `SE.COM.AUDITOR.CODE` | `SeatComponent_AuditorCode` | String |  |  |
| 28 | `SE.COM.AUDIT.DATE.TIME` | `SeatComponent_AuditDateTime` | String |  |  |
