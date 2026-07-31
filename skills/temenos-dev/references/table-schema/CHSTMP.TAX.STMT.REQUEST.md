# CHSTMP.TAX.STMT.REQUEST — Table Schema

> Source: `INSERTS/I_F.CHSTMP.TAX.STMT.REQUEST` in `CHSTMP_SwissTaxStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STMTREQ.PORTFOLIO` | `ChstmpTaxStmtRequest_Portfolio` |  |  |  |
| 2 | `STMTREQ.START.SERVICE` | `ChstmpTaxStmtRequest_StartService` | TField |  | Flag to start the Adhoc Tax statement service named as CHSTMP.TAX.STMT.PORTFOLIO. |
| 3 | `STMTREQ.LOCAL.REF` | `ChstmpTaxStmtRequest_LocalRef` |  |  |  |
| 4 | `STMTREQ.RESERVED.1` | `ChstmpTaxStmtRequest_Reserved1` | TField |  |  |
| 5 | `STMTREQ.RESERVED.2` | `ChstmpTaxStmtRequest_Reserved2` | TField |  |  |
| 6 | `STMTREQ.RESERVED.3` | `ChstmpTaxStmtRequest_Reserved3` | TField |  |  |
| 7 | `STMTREQ.RESERVED.4` | `ChstmpTaxStmtRequest_Reserved4` | TField |  |  |
| 8 | `STMTREQ.RESERVED.5` | `ChstmpTaxStmtRequest_Reserved5` | TField |  |  |
| 9 | `STMTREQ.OVERRIDE` | `ChstmpTaxStmtRequest_Override` |  |  |  |
| 10 | `STMTREQ.RECORD.STATUS` | `ChstmpTaxStmtRequest_RecordStatus` | String |  |  |
| 11 | `STMTREQ.CURR.NO` | `ChstmpTaxStmtRequest_CurrNo` | String |  |  |
| 12 | `STMTREQ.INPUTTER` | `ChstmpTaxStmtRequest_Inputter` |  |  |  |
| 13 | `STMTREQ.DATE.TIME` | `ChstmpTaxStmtRequest_DateTime` |  |  |  |
| 14 | `STMTREQ.AUTHORISER` | `ChstmpTaxStmtRequest_Authoriser` | String |  |  |
| 15 | `STMTREQ.CO.CODE` | `ChstmpTaxStmtRequest_CoCode` | String |  |  |
| 16 | `STMTREQ.DEPT.CODE` | `ChstmpTaxStmtRequest_DeptCode` | String |  |  |
| 17 | `STMTREQ.AUDITOR.CODE` | `ChstmpTaxStmtRequest_AuditorCode` | String |  |  |
| 18 | `STMTREQ.AUDIT.DATE.TIME` | `ChstmpTaxStmtRequest_AuditDateTime` | String |  |  |
