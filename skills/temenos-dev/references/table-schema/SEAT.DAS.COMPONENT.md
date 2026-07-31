# SEAT.DAS.COMPONENT — Table Schema

> Source: `INSERTS/I_F.SEAT.DAS.COMPONENT` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DAS.COM.COMPANY` | `SeatDasComponent_Company` | TField |  | This is a user input field, here user has to input the current Company mnemonic. Example: BNK,CO3 |
| 2 | `DAS.COM.OPTION` | `SeatDasComponent_Option` |  |  |  |
| 3 | `DAS.COM.ARG.FIELD` | `SeatDasComponent_ArgField` |  |  |  |
| 4 | `DAS.COM.ARG.OPERAND` | `SeatDasComponent_ArgOperand` |  |  |  |
| 5 | `DAS.COM.ARG.VALUE` | `SeatDasComponent_ArgValue` |  |  |  |
| 6 | `DAS.COM.ARG.DAS.VALUE` | `SeatDasComponent_ArgDasValue` |  |  |  |
| 7 | `DAS.COM.JOIN.OPERAND` | `SeatDasComponent_JoinOperand` |  |  |  |
| 8 | `DAS.COM.SORT` | `SeatDasComponent_Sort` |  |  |  |
| 9 | `DAS.COM.TEST.OPTION` | `SeatDasComponent_TestOption` |  |  |  |
| 10 | `DAS.COM.TEST.WITHOUT.DAS` | `SeatDasComponent_TestWithoutDas` |  |  |  |
| 11 | `DAS.COM.TEST.WITH.DAS` | `SeatDasComponent_TestWithDas` |  |  |  |
| 12 | `DAS.COM.RESULT` | `SeatDasComponent_Result` |  |  |  |
| 13 | `DAS.COM.OVERALL.RESULT` | `SeatDasComponent_OverallResult` | TField |  | This field check if all the queries match otherwise says ERROR. |
| 14 | `DAS.COM.RESERVED.7` | `SeatDasComponent_Reserved7` | TField |  |  |
| 15 | `DAS.COM.RESERVED.6` | `SeatDasComponent_Reserved6` | TField |  |  |
| 16 | `DAS.COM.RESERVED.5` | `SeatDasComponent_Reserved5` | TField |  |  |
| 17 | `DAS.COM.RESERVED.4` | `SeatDasComponent_Reserved4` | TField |  |  |
| 18 | `DAS.COM.RESERVED.3` | `SeatDasComponent_Reserved3` | TField |  |  |
| 19 | `DAS.COM.RESERVED.2` | `SeatDasComponent_Reserved2` | TField |  |  |
| 20 | `DAS.COM.RESERVED.1` | `SeatDasComponent_Reserved1` | TField |  |  |
| 21 | `DAS.COM.LOCAL.REF` | `SeatDasComponent_LocalRef` |  |  |  |
| 22 | `DAS.COM.OVERRIDE` | `SeatDasComponent_Override` |  |  |  |
| 23 | `DAS.COM.RECORD.STATUS` | `SeatDasComponent_RecordStatus` | String |  |  |
| 24 | `DAS.COM.CURR.NO` | `SeatDasComponent_CurrNo` | String |  |  |
| 25 | `DAS.COM.INPUTTER` | `SeatDasComponent_Inputter` |  |  |  |
| 26 | `DAS.COM.DATE.TIME` | `SeatDasComponent_DateTime` |  |  |  |
| 27 | `DAS.COM.AUTHORISER` | `SeatDasComponent_Authoriser` | String |  |  |
| 28 | `DAS.COM.CO.CODE` | `SeatDasComponent_CoCode` | String |  |  |
| 29 | `DAS.COM.DEPT.CODE` | `SeatDasComponent_DeptCode` | String |  |  |
| 30 | `DAS.COM.AUDITOR.CODE` | `SeatDasComponent_AuditorCode` | String |  |  |
| 31 | `DAS.COM.AUDIT.DATE.TIME` | `SeatDasComponent_AuditDateTime` | String |  |  |
