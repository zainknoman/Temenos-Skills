# CAPL.ACCT.STMT.SELECTION — Table Schema

> Source: `INSERTS/I_F.CAPL.ACCT.STMT.SELECTION` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.ACSTMT.DESCRIPTION` | `CaplAcctStmtSelection_Description` |  |  |  |
| 2 | `CAPL.ACSTMT.RECORD.STATUS` | `CaplAcctStmtSelection_RecordStatus` | String |  |  |
| 3 | `CAPL.ACSTMT.CURR.NO` | `CaplAcctStmtSelection_CurrNo` | String |  |  |
| 4 | `CAPL.ACSTMT.INPUTTER` | `CaplAcctStmtSelection_Inputter` |  |  |  |
| 5 | `CAPL.ACSTMT.DATE.TIME` | `CaplAcctStmtSelection_DateTime` |  |  |  |
| 6 | `CAPL.ACSTMT.AUTHORISER` | `CaplAcctStmtSelection_Authoriser` | String |  |  |
| 7 | `CAPL.ACSTMT.CO.CODE` | `CaplAcctStmtSelection_CoCode` | String |  |  |
| 8 | `CAPL.ACSTMT.DEPT.CODE` | `CaplAcctStmtSelection_DeptCode` | String |  |  |
| 9 | `CAPL.ACSTMT.AUDITOR.CODE` | `CaplAcctStmtSelection_AuditorCode` | String |  |  |
| 10 | `CAPL.ACSTMT.AUDIT.DATE.TIME` | `CaplAcctStmtSelection_AuditDateTime` | String |  |  |
