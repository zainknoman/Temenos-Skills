# PAYRCN.REQUEST — Table Schema

> Source: `INSERTS/I_F.PAYRCN.REQUEST` in `FINEXT_ATMRECON.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RCNREQ.DESCRIPTION` | `PayrcnRequest_Description` |  |  |  |
| 2 | `RCNREQ.REQUEST.TYPE` | `PayrcnRequest_RequestType` | TField |  |  |
| 3 | `RCNREQ.RECORD.TYPE` | `PayrcnRequest_RecordType` | TField |  |  |
| 4 | `RCNREQ.RECON.DATE` | `PayrcnRequest_ReconDate` | TField |  |  |
| 5 | `RCNREQ.RESERVED.9` | `PayrcnRequest_Reserved9` | TField |  |  |
| 6 | `RCNREQ.RESERVED.8` | `PayrcnRequest_Reserved8` | TField |  |  |
| 7 | `RCNREQ.RESERVED.7` | `PayrcnRequest_Reserved7` | TField |  |  |
| 8 | `RCNREQ.RESERVED.6` | `PayrcnRequest_Reserved6` | TField |  |  |
| 9 | `RCNREQ.RESERVED.5` | `PayrcnRequest_Reserved5` | TField |  |  |
| 10 | `RCNREQ.RESERVED.4` | `PayrcnRequest_Reserved4` | TField |  |  |
| 11 | `RCNREQ.RESERVED.3` | `PayrcnRequest_Reserved3` | TField |  |  |
| 12 | `RCNREQ.RESERVED.2` | `PayrcnRequest_Reserved2` | TField |  |  |
| 13 | `RCNREQ.RESERVED.1` | `PayrcnRequest_Reserved1` | TField |  |  |
| 14 | `RCNREQ.RECORD.STATUS` | `PayrcnRequest_RecordStatus` | String |  |  |
| 15 | `RCNREQ.CURR.NO` | `PayrcnRequest_CurrNo` | String |  |  |
| 16 | `RCNREQ.INPUTTER` | `PayrcnRequest_Inputter` |  |  |  |
| 17 | `RCNREQ.DATE.TIME` | `PayrcnRequest_DateTime` |  |  |  |
| 18 | `RCNREQ.AUTHORISER` | `PayrcnRequest_Authoriser` | String |  |  |
| 19 | `RCNREQ.CO.CODE` | `PayrcnRequest_CoCode` | String |  |  |
| 20 | `RCNREQ.DEPT.CODE` | `PayrcnRequest_DeptCode` | String |  |  |
| 21 | `RCNREQ.AUDITOR.CODE` | `PayrcnRequest_AuditorCode` | String |  |  |
| 22 | `RCNREQ.AUDIT.DATE.TIME` | `PayrcnRequest_AuditDateTime` | String |  |  |
