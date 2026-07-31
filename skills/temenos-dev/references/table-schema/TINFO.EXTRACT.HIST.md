# TINFO.EXTRACT.HIST — Table Schema

> Source: `INSERTS/I_F.TINFO.EXTRACT.HIST` in `EI_SupportUtilities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TINFO.HIS.APPLICATION` | `TinfoExtractHist_Application` |  |  |  |
| 2 | `TINFO.HIS.CONTRACT.ID` | `TinfoExtractHist_ContractId` |  |  |  |
| 3 | `TINFO.HIS.NO.OF.HISTORY` | `TinfoExtractHist_NoOfHistory` |  |  |  |
| 4 | `TINFO.HIS.START.DATE` | `TinfoExtractHist_StartDate` |  |  |  |
| 5 | `TINFO.HIS.LIST.NAME` | `TinfoExtractHist_ListName` |  |  |  |
| 6 | `TINFO.HIS.FREE.PRINT` | `TinfoExtractHist_FreePrint` |  |  |  |
| 7 | `TINFO.HIS.AD.ROUTINE` | `TinfoExtractHist_AdRoutine` | TField |  | Reserved for future use |
| 8 | `TINFO.HIS.EXECUTION.STATUS` | `TinfoExtractHist_ExecutionStatus` | TField |  | This field is used to indicate the current status of the tool running Validation Rules: No Input field Values are Process Started;Process Finished |
| 9 | `TINFO.HIS.RESULT.APPL` | `TinfoExtractHist_ResultAppl` |  |  |  |
| 10 | `TINFO.HIS.HOLD.IDS` | `TinfoExtractHist_HoldIds` |  |  |  |
| 11 | `TINFO.HIS.RESERVED.10` | `TinfoExtractHist_Reserved10` | TField |  |  |
| 12 | `TINFO.HIS.RESERVED.09` | `TinfoExtractHist_Reserved09` | TField |  |  |
| 13 | `TINFO.HIS.RESERVED.08` | `TinfoExtractHist_Reserved08` | TField |  |  |
| 14 | `TINFO.HIS.RESERVED.07` | `TinfoExtractHist_Reserved07` | TField |  |  |
| 15 | `TINFO.HIS.RESERVED.06` | `TinfoExtractHist_Reserved06` | TField |  |  |
| 16 | `TINFO.HIS.RESERVED.05` | `TinfoExtractHist_Reserved05` | TField |  |  |
| 17 | `TINFO.HIS.RESERVED.04` | `TinfoExtractHist_Reserved04` | TField |  |  |
| 18 | `TINFO.HIS.RESERVED.03` | `TinfoExtractHist_Reserved03` | TField |  |  |
| 19 | `TINFO.HIS.RESERVED.02` | `TinfoExtractHist_Reserved02` | TField |  |  |
| 20 | `TINFO.HIS.RESERVED.01` | `TinfoExtractHist_Reserved01` | TField |  |  |
