# TINFO.EXTRACT — Table Schema

> Source: `INSERTS/I_F.TINFO.EXTRACT` in `EI_SupportUtilities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TINFO.APPLICATION` | `TInfoExtract_Application` |  |  |  |
| 2 | `TINFO.CONTRACT.ID` | `TInfoExtract_ContractId` |  |  |  |
| 3 | `TINFO.NO.OF.HISTORY` | `TInfoExtract_NoOfHistory` |  |  |  |
| 4 | `TINFO.START.DATE` | `TInfoExtract_StartDate` |  |  |  |
| 5 | `TINFO.LIST.NAME` | `TInfoExtract_ListName` |  |  |  |
| 6 | `TINFO.FREE.PRINT` | `TInfoExtract_FreePrint` |  |  |  |
| 7 | `TINFO.AD.ROUTINE` | `TInfoExtract_AdRoutine` |  |  |  |
| 8 | `TINFO.EXECUTION.STATUS` | `TInfoExtract_ExecutionStatus` |  |  |  |
| 9 | `TINFO.RESULT.APPL` | `TInfoExtract_ResultAppl` |  |  |  |
| 10 | `TINFO.HOLD.IDS` | `TInfoExtract_HoldIds` |  |  |  |
| 11 | `TINFO.RESERVED.10` | `TInfoExtract_Reserved10` |  |  |  |
| 12 | `TINFO.RESERVED.09` | `TInfoExtract_Reserved09` |  |  |  |
| 13 | `TINFO.RESERVED.08` | `TInfoExtract_Reserved08` |  |  |  |
| 14 | `TINFO.RESERVED.07` | `TInfoExtract_Reserved07` |  |  |  |
| 15 | `TINFO.RESERVED.06` | `TInfoExtract_Reserved06` |  |  |  |
| 16 | `TINFO.RESERVED.05` | `TInfoExtract_Reserved05` |  |  |  |
| 17 | `TINFO.RESERVED.04` | `TInfoExtract_Reserved04` |  |  |  |
| 18 | `TINFO.RESERVED.03` | `TInfoExtract_Reserved03` |  |  |  |
| 19 | `TINFO.RESERVED.02` | `TInfoExtract_Reserved02` |  |  |  |
| 20 | `TINFO.RESERVED.01` | `TInfoExtract_Reserved01` |  |  |  |
| 21 | `TINFO.RECORD.STATUS` | `TInfoExtract_RecordStatus` |  |  |  |
| 22 | `TINFO.CURR.NO` | `TInfoExtract_CurrNo` |  |  |  |
| 23 | `TINFO.INPUTTER` | `TInfoExtract_Inputter` |  |  |  |
| 24 | `TINFO.DATE.TIME` | `TInfoExtract_DateTime` |  |  |  |
| 25 | `TINFO.AUTHORISER` | `TInfoExtract_Authoriser` |  |  |  |
| 26 | `TINFO.CO.CODE` | `TInfoExtract_CoCode` |  |  |  |
| 27 | `TINFO.DEPT.CODE` | `TInfoExtract_DeptCode` |  |  |  |
| 28 | `TINFO.AUDITOR.CODE` | `TInfoExtract_AuditorCode` |  |  |  |
| 29 | `TINFO.AUDIT.DATE.TIME` | `TInfoExtract_AuditDateTime` |  |  |  |
