# AC.VIOLATION.HIST — Table Schema

> Source: `INSERTS/I_F.AC.VIOLATION.HIST` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.VIOL.HIST.STMT.ENTRY.ID` | `AcViolationHist_StmtEntryId` |  |  |  |
| 2 | `AC.VIOL.HIST.PROCESSING.DATE` | `AcViolationHist_ProcessingDate` |  |  |  |
| 3 | `AC.VIOL.HIST.TXN.STATUS` | `AcViolationHist_TxnStatus` |  |  |  |
| 4 | `AC.VIOL.HIST.WAIVE.CR.INT` | `AcViolationHist_WaiveCrInt` |  |  |  |
| 5 | `AC.VIOL.HIST.TXN.CODE` | `AcViolationHist_TxnCode` |  |  |  |
| 6 | `AC.VIOL.HIST.NARRATIVE` | `AcViolationHist_Narrative` |  |  |  |
| 7 | `AC.VIOL.HIST.VIOLATION.STATUS` | `AcViolationHist_ViolationStatus` | TField |  | This field indicates whether or not this particular violation record is in violation. It will either be set to Y (Yes) or N (No) Validation Rules: This is a NOINPUT field. |
| 8 | `AC.VIOL.HIST.WAIVE.CR.STATUS` | `AcViolationHist_WaiveCrStatus` | TField |  |  |
| 9 | `AC.VIOL.HIST.RESERVED7` | `AcViolationHist_Reserved7` | TField |  |  |
| 10 | `AC.VIOL.HIST.RESERVED6` | `AcViolationHist_Reserved6` | TField |  |  |
| 11 | `AC.VIOL.HIST.RESERVED5` | `AcViolationHist_Reserved5` | TField |  |  |
| 12 | `AC.VIOL.HIST.RESERVED4` | `AcViolationHist_Reserved4` | TField |  |  |
| 13 | `AC.VIOL.HIST.RESERVED3` | `AcViolationHist_Reserved3` | TField |  |  |
| 14 | `AC.VIOL.HIST.RESERVED2` | `AcViolationHist_Reserved2` | TField |  |  |
| 15 | `AC.VIOL.HIST.RESERVED1` | `AcViolationHist_Reserved1` | TField |  |  |
| 16 | `AC.VIOL.HIST.LOCAL.REF` | `AcViolationHist_LocalRef` |  |  |  |
| 17 | `AC.VIOL.HIST.OVERRIDE` | `AcViolationHist_Override` |  |  |  |
