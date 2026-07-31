# STATEMENT.CONTROL — Table Schema

> Source: `INSERTS/I_F.STATEMENT.CONTROL` in `AC_StmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SCONT.NON.STMT.TXNS` | `StatementControl_NonStmtTxns` |  |  |  |
| 2 | `SCONT.BATCH.OUTPUT` | `StatementControl_BatchOutput` | TField | Yes | Validation Rules: Mandatory input. A maximum of 3 characters may be entered. The following values are permitted: YES NO |
| 3 | `SCONT.MAPPING.ROUTINE` | `StatementControl_MappingRoutine` | TField |  | Specify either a jBC subroutine(exist on PGM.FILE as a type 'S') or an EB.API record of type METHOD which implements an interface defined in the EB.API record HOOK.SCONT.MAPPING.RTN, used to attach a routine which will be called while preparing statement handoff record. This routine will be called from DE.PRODUCT.SWIFT.STMT passing the current processing ENTRY.ID, ENTRY.RECORD, CURRENT.MULTIVALUE.POSITION and CARRIER.LIST for the account. Using this routine we can add the extra information required from the entry for local development in the handoff record The information to be updated has to be returned to the core by this routine, MODIFIED.POSITION and MODIFIED.DATA core will update the modified data in the handoff record Validation Rules: Must be a valid compiled routine in the system A maximum of 40 characters may be entered. |
| 4 | `SCONT.STMT.INTEG.CHK` | `StatementControl_StmtIntegChk` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `SCONT.STMT.DATE.TYPE` | `StatementControl_StmtDateType` | TField |  |  |
| 6 | `SCONT.LOCAL.REF` | `StatementControl_LocalRef` |  |  |  |
| 7 | `SCONT.PREFORMAT.TAGS` | `StatementControl_Reserved1` |  |  |  |
| 8 | `SCONT.RECORD.STATUS` | `StatementControl_RecordStatus` | String |  |  |
| 9 | `SCONT.CURR.NO` | `StatementControl_CurrNo` | String |  |  |
| 10 | `SCONT.INPUTTER` | `StatementControl_Inputter` |  |  |  |
| 11 | `SCONT.DATE.TIME` | `StatementControl_DateTime` |  |  |  |
| 12 | `SCONT.AUTHORISER` | `StatementControl_Authoriser` | String |  |  |
| 13 | `SCONT.CO.CODE` | `StatementControl_CoCode` | String |  |  |
| 14 | `SCONT.DEPT.CODE` | `StatementControl_DeptCode` | String |  |  |
| 15 | `SCONT.AUDITOR.CODE` | `StatementControl_AuditorCode` | String |  |  |
| 16 | `SCONT.AUDIT.DATE.TIME` | `StatementControl_AuditDateTime` | String |  |  |
