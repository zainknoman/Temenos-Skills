# AC.XML.STMT.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.AC.XML.STMT.EXCEPTION` in `IX_XmlStmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IX.EXP.MESSAGE.STATUS` | `AcXmlStmtException_MessageStatus` | TField |  | Status of the CAMT message Value can be ERROR or SUCCESS The value "ERROR" denotes that the CAMT message has not been generated The value "SUCCESS" indicates that the CAMT message has been generated on the resubmission |
| 2 | `IX.EXP.MSG.RESUBMIT` | `AcXmlStmtException_MsgResubmit` | TField |  | MSG.RESUBMIT This field is used to resubmit the CAMT request for the messages that had failed Inputtable only for the XML.TRANFORM error Value can either be null or YES |
| 3 | `IX.EXP.MSG.RESUBMIT.DATE` | `AcXmlStmtException_MsgResubmitDate` | TField |  | Date of resubmission of CAMT request Holds the date on which the CAMT request was resubmitted |
| 4 | `IX.EXP.ERROR.SOURCE` | `AcXmlStmtException_ErrorSource` |  |  |  |
| 5 | `IX.EXP.ERROR.MESSAGE` | `AcXmlStmtException_ErrorMessage` |  |  |  |
| 6 | `IX.EXP.TAG.NAME` | `AcXmlStmtException_TagName` |  |  |  |
| 7 | `IX.EXP.TAG.ERROR.MESSAGE` | `AcXmlStmtException_TagErrorMessage` |  |  |  |
| 8 | `IX.EXP.ERROR.RESERVED1` | `AcXmlStmtException_ErrorReserved1` |  |  |  |
| 9 | `IX.EXP.STMT.DATE` | `AcXmlStmtException_StmtDate` | TField |  | STMT.DATE Date on which CAMT request was given |
| 10 | `IX.EXP.RESERVED.FIELDS.4` | `AcXmlStmtException_ReservedFields4` | TField |  |  |
| 11 | `IX.EXP.RESERVED.FIELDS.3` | `AcXmlStmtException_ReservedFields3` | TField |  |  |
| 12 | `IX.EXP.RESERVED.FIELDS.2` | `AcXmlStmtException_ReservedFields2` | TField |  |  |
| 13 | `IX.EXP.RESERVED.FIELDS.1` | `AcXmlStmtException_ReservedFields1` | TField |  |  |
| 14 | `IX.EXP.RECORD.STATUS` | `AcXmlStmtException_RecordStatus` | String |  |  |
| 15 | `IX.EXP.CURR.NO` | `AcXmlStmtException_CurrNo` | String |  |  |
| 16 | `IX.EXP.INPUTTER` | `AcXmlStmtException_Inputter` |  |  |  |
| 17 | `IX.EXP.DATE.TIME` | `AcXmlStmtException_DateTime` |  |  |  |
| 18 | `IX.EXP.AUTHORISER` | `AcXmlStmtException_Authoriser` | String |  |  |
| 19 | `IX.EXP.CO.CODE` | `AcXmlStmtException_CoCode` | String |  |  |
| 20 | `IX.EXP.DEPT.CODE` | `AcXmlStmtException_DeptCode` | String |  |  |
| 21 | `IX.EXP.AUDITOR.CODE` | `AcXmlStmtException_AuditorCode` | String |  |  |
| 22 | `IX.EXP.AUDIT.DATE.TIME` | `AcXmlStmtException_AuditDateTime` | String |  |  |
