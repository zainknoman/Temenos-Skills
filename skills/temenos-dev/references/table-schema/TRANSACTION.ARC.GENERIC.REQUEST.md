# TRANSACTION.ARC.GENERIC.REQUEST — Table Schema

> Source: `INSERTS/I_F.TRANSACTION.ARC.GENERIC.REQUEST` in `PP_ArchivingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRANS.ArchiveID` | `TransactionArcGenericRequest_Archiveid` |  |  |  |
| 2 | `TRANS.RECORD.STATUS` | `TransactionArcGenericRequest_RecordStatus` |  |  |  |
| 3 | `TRANS.CURR.NO` | `TransactionArcGenericRequest_CurrNo` |  |  |  |
| 4 | `TRANS.INPUTTER` | `TransactionArcGenericRequest_Inputter` |  |  |  |
| 5 | `TRANS.DATE.TIME` | `TransactionArcGenericRequest_DateTime` |  |  |  |
| 6 | `TRANS.AUTHORISER` | `TransactionArcGenericRequest_Authoriser` |  |  |  |
| 7 | `TRANS.CO.CODE` | `TransactionArcGenericRequest_CoCode` |  |  |  |
| 8 | `TRANS.DEPT.CODE` | `TransactionArcGenericRequest_DeptCode` |  |  |  |
| 9 | `TRANS.AUDITOR.CODE` | `TransactionArcGenericRequest_AuditorCode` |  |  |  |
| 10 | `TRANS.AUDIT.DATE.TIME` | `TransactionArcGenericRequest_AuditDateTime` |  |  |  |
