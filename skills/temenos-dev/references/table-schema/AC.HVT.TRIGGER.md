# AC.HVT.TRIGGER — Table Schema

> Source: `INSERTS/I_F.AC.HVT.TRIGGER` in `AC_HighVolume.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.HVT.ACCOUNT.ID` | `AcHvtTrigger_AccountId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `AC.HVT.ECB.RECORD` | `AcHvtTrigger_EcbRecord` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `AC.HVT.AC.VIOLATION` | `AcHvtTrigger_AcViolation` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `AC.HVT.ENT.TODAY.ID` | `AcHvtTrigger_EntTodayId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `AC.HVT.TODAY.ENTRY` | `AcHvtTrigger_TodayEntry` |  |  |  |
| 6 | `AC.HVT.ENT.FWD.ID` | `AcHvtTrigger_EntFwdId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `AC.HVT.FWD.ENTRY` | `AcHvtTrigger_FwdEntry` |  |  |  |
| 8 | `AC.HVT.STMT.VAL.ID` | `AcHvtTrigger_StmtValId` |  |  |  |
| 9 | `AC.HVT.STMT.VAL.ENTRY` | `AcHvtTrigger_StmtValEntry` |  |  |  |
| 10 | `AC.HVT.ACCT.STMT.PRINT.ID` | `AcHvtTrigger_AcctStmtPrintId` |  |  |  |
| 11 | `AC.HVT.ACCT.STMT.PRINT` | `AcHvtTrigger_AcctStmtPrint` |  |  |  |
| 12 | `AC.HVT.STMT.PRINTED.ID` | `AcHvtTrigger_StmtPrintedId` |  |  |  |
| 13 | `AC.HVT.STMT.PRINT.ENTRY` | `AcHvtTrigger_StmtPrintEntry` |  |  |  |
| 14 | `AC.HVT.FWD.STMT1.ID` | `AcHvtTrigger_FwdStmt1Id` |  |  |  |
| 15 | `AC.HVT.FWD.STMT1.ENTRY` | `AcHvtTrigger_FwdStmt1Entry` |  |  |  |
| 16 | `AC.HVT.ACCT.STMT2.PRNT.ID` | `AcHvtTrigger_AcctStmt2PrntId` |  |  |  |
| 17 | `AC.HVT.ACCT.STMT2.PRINT` | `AcHvtTrigger_AcctStmt2Print` |  |  |  |
| 18 | `AC.HVT.STMT2.PRINTED.ID` | `AcHvtTrigger_Stmt2PrintedId` |  |  |  |
| 19 | `AC.HVT.STMT2.PRINT.ENTRY` | `AcHvtTrigger_Stmt2PrintEntry` |  |  |  |
| 20 | `AC.HVT.FWD.STMT2.ID` | `AcHvtTrigger_FwdStmt2Id` |  |  |  |
| 21 | `AC.HVT.FWD.STMT2.ENTRY` | `AcHvtTrigger_FwdStmt2Entry` |  |  |  |
| 22 | `AC.HVT.ACTIVITY.MONTH` | `AcHvtTrigger_ActivityMonth` |  |  |  |
| 23 | `AC.HVT.ACTIVITY.RECORD` | `AcHvtTrigger_ActivityRecord` |  |  |  |
| 24 | `AC.HVT.DATE.EXPOSURE.ID` | `AcHvtTrigger_DateExposureId` |  |  |  |
| 25 | `AC.HVT.DATE.EXPO.ENTRY` | `AcHvtTrigger_DateExpoEntry` |  |  |  |
| 26 | `AC.HVT.ACCOUNT.DETAILS` | `AcHvtTrigger_AccountDetails` | TField |  |  |
| 27 | `AC.HVT.ACTIVITY.HISTORY.DETAILS` | `AcHvtTrigger_ActivityHistoryDetails` | TField |  |  |
| 28 | `AC.HVT.ACCOUNT.MOVEMENT.DETAILS` | `AcHvtTrigger_AccountMovementDetails` | TField |  |  |
| 29 | `AC.HVT.AC.STMT.ENT.WORK` | `AcHvtTrigger_AcStmtEntWork` |  |  |  |
| 30 | `AC.HVT.ACT.RR.ADJUSTMENT.DETAILS` | `AcHvtTrigger_ActRrAdjustementDetails` |  |  |  |
| 31 | `AC.HVT.RESERVED.3` | `AcHvtTrigger_Reserved3` |  |  |  |
| 32 | `AC.HVT.RESERVED.2` | `AcHvtTrigger_Reserved2` | TField |  |  |
| 33 | `AC.HVT.RESERVED.1` | `AcHvtTrigger_Reserved1` | TField |  |  |
