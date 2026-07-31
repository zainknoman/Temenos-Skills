# SEAT.RESULTS — Table Schema

> Source: `INSERTS/I_F.SEAT.RESULTS` in `EB_Seat.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SR.TOTAL.PATHLENGTH` | `SeatResults_TotalPathlength` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `EB.SR.TOTAL.ELAPSED` | `SeatResults_TotalElapsed` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `EB.SR.TOTAL.IO` | `SeatResults_TotalIo` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `EB.SR.TOTAL.CALLS` | `SeatResults_TotalCalls` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `EB.SR.SUBROUTINE` | `SeatResults_Subroutine` |  |  |  |
| 6 | `EB.SR.PATHLENGTH` | `SeatResults_Pathlength` |  |  |  |
| 7 | `EB.SR.ITERATIONS` | `SeatResults_Iterations` |  |  |  |
| 8 | `EB.SR.ELAPSED` | `SeatResults_Elapsed` |  |  |  |
| 9 | `EB.SR.IO` | `SeatResults_Io` |  |  |  |
| 10 | `EB.SR.IO.COUNT` | `SeatResults_IoCount` |  |  |  |
| 11 | `EB.SR.WARNINGS` | `SeatResults_Warnings` |  |  |  |
| 12 | `EB.SR.EXECUTES` | `SeatResults_Executes` |  |  |  |
| 13 | `EB.SR.OVERALL.RESULT` | `SeatResults_OverallResult` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 14 | `EB.SR.SEAT.RTN.ID` | `SeatResults_SeatRtnId` |  |  |  |
| 15 | `EB.SR.RESULT` | `SeatResults_Result` |  |  |  |
| 16 | `EB.SR.REASON` | `SeatResults_Reason` |  |  |  |
| 17 | `EB.SR.EXPECTED` | `SeatResults_Expected` |  |  |  |
| 18 | `EB.SR.ACTUAL` | `SeatResults_Actual` |  |  |  |
| 19 | `EB.SR.UPLOAD.STATUS` | `SeatResults_UploadStatus` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 20 | `EB.SR.MACHINE.DATE` | `SeatResults_MachineDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 21 | `EB.SR.MACHINE.TIME` | `SeatResults_MachineTime` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 22 | `EB.SR.COMPANY` | `SeatResults_Company` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 23 | `EB.SR.APPLICATION` | `SeatResults_Application` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 24 | `EB.SR.FUNCTION` | `SeatResults_Function` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 25 | `EB.SR.CONTRACT.ID` | `SeatResults_ContractId` |  |  |  |
| 26 | `EB.SR.RELEASE` | `SeatResults_Release` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 27 | `EB.SR.OFS.MESSAGE` | `SeatResults_OfsMessage` |  |  |  |
| 28 | `EB.SR.SEAT.ID` | `SeatResults_SeatId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 29 | `EB.SR.BANK.DATE` | `SeatResults_BankDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 30 | `EB.SR.T24.SESSION.NO` | `SeatResults_T24SessionNo` | TField |  |  |
| 31 | `EB.SR.CONTRACT.COUNT` | `SeatResults_ContractCount` | TField |  |  |
| 32 | `EB.SR.PW.ACTIVITY.TXN.ID` | `SeatResults_PwActivityTxnId` | TField |  |  |
| 33 | `EB.SR.FIELD.CACHE` | `SeatResults_FieldCache` | TField |  | Denotes the status of field cache functionality whether it is used in current application for which the request has been processed.It can hold the values, 1. FOUND - Field cache is enabled or utilised (it is applicable for very first request in a session or subsequent request of same application). 2. NOT.FOUND - Field cache is not enabled so not used (it can apply for even old format templates or applications forcefully disabled field cache). For AA parent and its child OFS response when it has mismatch in Field cache status, the FIELD.CACHE will be updated accordingly. And all response will be stored in OFS.MESSAGE field. When there is no mismatch in field cache status, then FIELD.CACHE = FOUND will be updated. Validation Rules: Standard T24 alphanumeric field with a maximum of 50 characters. |
