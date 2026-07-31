# AC.STMT.SERVICE.DETAIL — Table Schema

> Source: `INSERTS/I_F.AC.STMT.SERVICE.DETAIL` in `AC_AccountStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.STM.SRV.STMT.DATE` | `AcStmtServiceDetail_StmtDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `AC.STM.SRV.STMT.FQU.TYPE` | `AcStmtServiceDetail_StmtFquType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `AC.STM.SRV.STMT.FQU.CYCLE` | `AcStmtServiceDetail_StmtFquCycle` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `AC.STM.SRV.LAST.STMT.NO` | `AcStmtServiceDetail_LastStmtNo` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `AC.STM.SRV.STMT.AV` | `AcStmtServiceDetail_StmtAv` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `AC.STM.SRV.OPEN.STMT.DATE` | `AcStmtServiceDetail_OpenStmtDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `AC.STM.SRV.LAST.BALANCE` | `AcStmtServiceDetail_LastBalance` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `AC.STM.SRV.TOT.STM.AMT` | `AcStmtServiceDetail_TotStmAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `AC.STM.SRV.FWD.MVMT.REQD` | `AcStmtServiceDetail_FwdMvmtReqd` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `AC.STM.SRV.SWIFT.STMT` | `AcStmtServiceDetail_SwiftStmt` |  |  |  |
| 11 | `AC.STM.SRV.SPL.STMT` | `AcStmtServiceDetail_SplStmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `AC.STM.SRV.ADHOC.TODAY` | `AcStmtServiceDetail_AdhocToday` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `AC.STM.SRV.CLOSURE.STMT` | `AcStmtServiceDetail_ClosureStmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 14 | `AC.STM.SRV.SEND.VIA.DEL` | `AcStmtServiceDetail_SendViaDel` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `AC.STM.SRV.SEND.VIA.SWIFT` | `AcStmtServiceDetail_SendViaSwift` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 16 | `AC.STM.SRV.AC.CLEARED.BAL` | `AcStmtServiceDetail_AcClearedBal` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 17 | `AC.STM.SRV.AC.ACTUAL.BAL` | `AcStmtServiceDetail_AcActualBal` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 18 | `AC.STM.SRV.OPEN.AVAIL.BAL` | `AcStmtServiceDetail_OpenAvailBal` |  |  |  |
| 19 | `AC.STM.SRV.OPEN.AVAIL.DATE` | `AcStmtServiceDetail_OpenAvailDate` |  |  |  |
| 20 | `AC.STM.SRV.AUTH.DB.MVMT` | `AcStmtServiceDetail_AuthDbMvmt` |  |  |  |
| 21 | `AC.STM.SRV.NAU.DB.MVMT` | `AcStmtServiceDetail_NauDbMvmt` |  |  |  |
| 22 | `AC.STM.SRV.AUTH.CR.MVMT` | `AcStmtServiceDetail_AuthCrMvmt` |  |  |  |
| 23 | `AC.STM.SRV.NAU.CR.MVMT` | `AcStmtServiceDetail_NauCrMvmt` |  |  |  |
| 24 | `AC.STM.SRV.AVAILABLE.BAL` | `AcStmtServiceDetail_AvailableBal` |  |  |  |
| 25 | `AC.STM.SRV.FWD.MVMT` | `AcStmtServiceDetail_FwdMvmt` |  |  |  |
| 26 | `AC.STM.SRV.NEXT.AF.DATE` | `AcStmtServiceDetail_NextAfDate` |  |  |  |
| 27 | `AC.STM.SRV.FIRST.AF.DATE` | `AcStmtServiceDetail_FirstAfDate` |  |  |  |
| 28 | `AC.STM.SRV.STMT.PRINTED.ID` | `AcStmtServiceDetail_StmtPrintedId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 29 | `AC.STM.SRV.NO.MVMT.STMT` | `AcStmtServiceDetail_NoMvmtStmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 30 | `AC.STM.SRV.ADDITIONAL.STMT` | `AcStmtServiceDetail_AdditionalStmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 31 | `AC.STM.SRV.AC.PERIOD.END` | `AcStmtServiceDetail_AcPeriodEnd` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 32 | `AC.STM.SRV.AC.LWORKING.DAY` | `AcStmtServiceDetail_AcLworkingDay` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 33 | `AC.STM.SRV.DE.STMT.REQ` | `AcStmtServiceDetail_DeStmtReq` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 34 | `AC.STM.SRV.MAPPING.KEY` | `AcStmtServiceDetail_MappingKey` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 35 | `AC.STM.SRV.FWD.STMT.PRINTED` | `AcStmtServiceDetail_FwdStmtPrinted` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 36 | `AC.STM.SRV.NEW.STMT.NO` | `AcStmtServiceDetail_NewStmtNo` | TField |  |  |
| 37 | `AC.STM.SRV.CAMT.REF` | `AcStmtServiceDetail_CamtRef` | TField |  |  |
| 38 | `AC.STM.SRV.RESERVED.3` | `AcStmtServiceDetail_Reserved3` | TField |  |  |
| 39 | `AC.STM.SRV.RESERVED.2` | `AcStmtServiceDetail_Reserved2` | TField |  |  |
| 40 | `AC.STM.SRV.RESERVED.1` | `AcStmtServiceDetail_Reserved1` | TField |  |  |
