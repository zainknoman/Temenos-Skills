# AA.STATEMENT.NARR.FORMAT — Table Schema

> Source: `INSERTS/I_F.AA.STATEMENT.NARR.FORMAT` in `AA_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SNF.DESCRIPTION` | `AaStatementNarrFormat_Description` | TField |  | Description of the narrative format. |
| 2 | `AA.SNF.APPLICATION` | `AaStatementNarrFormat_Application` | TField |  | Application for which narrative format is defined. |
| 3 | `AA.SNF.FIELD.TEXT` | `AaStatementNarrFormat_FieldText` |  |  |  |
| 4 | `AA.SNF.CONVERSION` | `AaStatementNarrFormat_Conversion` |  |  |  |
| 5 | `AA.SNF.FIELD.IDX` | `AaStatementNarrFormat_FieldIdx` |  |  |  |
| 6 | `AA.SNF.TRANS.TYPE` | `AaStatementNarrFormat_TransType` | TField |  | User-defined transaction type for this narrative that can be used for filtering account statement enquiry. The transaction types available for selection are defined in EB.LOOKUP table. |
| 7 | `AA.SNF.SPLIT.SD.REV` | `AaStatementNarrFormat_SplitSdRev` | TField |  | Flag to indicate whether the system should display the original and the reversed transaction line for transactions reversed on the same day. If not set, the reversed transaction would be displayed in a single line |
| 8 | `AA.SNF.HIDE.COMP` | `AaStatementNarrFormat_HideComp` | TField |  | Flag to indicate that the financial components (AA properties) of the transaction should be hidden, even when the show properties attribute on the AA parameter file is set. |
| 9 | `AA.SNF.INCL.COMP` | `AaStatementNarrFormat_InclComp` |  |  |  |
| 10 | `AA.SNF.HIDE.LINE` | `AaStatementNarrFormat_HideLine` | TField |  | Flag to indicate that the statement line should be hidden if the total transaction amount (affecting statement balance) is zero |
| 11 | `AA.SNF.HIDE.AMT` | `AaStatementNarrFormat_HideAmt` | TField |  | Flag to indicate that the transaction amount should be hidden. |
| 12 | `AA.SNF.SPEC.PROC.TYPE` | `AaStatementNarrFormat_SpecProcType` | TField |  | Special processing type for the statement line display. Currently two options are available: SEP.MAKEDUE.COMP � split lending makedue activity components into separate lines, with additional text given after the property name. SHOW.TOT.AMOUNT � use the amount affecting the statement balance as the transaction amount. |
| 13 | `AA.SNF.RESERVED.8` | `AaStatementNarrFormat_Reserved8` | TField |  |  |
| 14 | `AA.SNF.RESERVED.9` | `AaStatementNarrFormat_Reserved9` | TField |  |  |
| 15 | `AA.SNF.LOCAL.REF` | `AaStatementNarrFormat_LocalRef` |  |  |  |
| 16 | `AA.SNF.OVERRIDE` | `AaStatementNarrFormat_Override` |  |  |  |
| 17 | `AA.SNF.RECORD.STATUS` | `AaStatementNarrFormat_RecordStatus` | String |  |  |
| 18 | `AA.SNF.CURR.NO` | `AaStatementNarrFormat_CurrNo` | String |  |  |
| 19 | `AA.SNF.INPUTTER` | `AaStatementNarrFormat_Inputter` |  |  |  |
| 20 | `AA.SNF.DATE.TIME` | `AaStatementNarrFormat_DateTime` |  |  |  |
| 21 | `AA.SNF.AUTHORISER` | `AaStatementNarrFormat_Authoriser` | String |  |  |
| 22 | `AA.SNF.CO.CODE` | `AaStatementNarrFormat_CoCode` | String |  |  |
| 23 | `AA.SNF.DEPT.CODE` | `AaStatementNarrFormat_DeptCode` | String |  |  |
| 24 | `AA.SNF.AUDITOR.CODE` | `AaStatementNarrFormat_AuditorCode` | String |  |  |
| 25 | `AA.SNF.AUDIT.DATE.TIME` | `AaStatementNarrFormat_AuditDateTime` | String |  |  |
