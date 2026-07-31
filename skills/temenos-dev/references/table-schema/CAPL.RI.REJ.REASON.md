# CAPL.RI.REJ.REASON — Table Schema

> Source: `INSERTS/I_F.CAPL.RI.REJ.REASON` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.RI.RR.CODE` | `CaplRiRejReason_Code` | TField |  | Field to store the unique Reject Reason Codeeg DTE |
| 2 | `CAPL.RI.RR.DESCRIPTION` | `CaplRiRejReason_Description` | TField |  | Field to store Description for reject Reason code.Free text.Allowed upto 35 char |
| 3 | `CAPL.RI.RR.FT.COMM.TYPE` | `CaplRiRejReason_FtCommType` | TField |  | Field to indicate the commission type to be considered for reject items.Used to trigger additional charges during return item processValidation - valid FT.COMMISSION.TYPE record. |
| 4 | `CAPL.RI.RR.RESERVED.5` | `CaplRiRejReason_Reserved5` |  |  |  |
| 5 | `CAPL.RI.RR.RESERVED.4` | `CaplRiRejReason_Reserved4` |  |  |  |
| 6 | `CAPL.RI.RR.RESERVED.3` | `CaplRiRejReason_Reserved3` | TField |  |  |
| 7 | `CAPL.RI.RR.RESERVED.2` | `CaplRiRejReason_Reserved2` | TField |  |  |
| 8 | `CAPL.RI.RR.RESERVED.1` | `CaplRiRejReason_Reserved1` | TField |  |  |
| 9 | `CAPL.RI.RR.LOCAL.REF` | `CaplRiRejReason_LocalRef` |  |  |  |
| 10 | `CAPL.RI.RR.OVERRIDE` | `CaplRiRejReason_Override` |  |  |  |
| 11 | `CAPL.RI.RR.RECORD.STATUS` | `CaplRiRejReason_RecordStatus` | String |  |  |
| 12 | `CAPL.RI.RR.CURR.NO` | `CaplRiRejReason_CurrNo` | String |  |  |
| 13 | `CAPL.RI.RR.INPUTTER` | `CaplRiRejReason_Inputter` |  |  |  |
| 14 | `CAPL.RI.RR.DATE.TIME` | `CaplRiRejReason_DateTime` |  |  |  |
| 15 | `CAPL.RI.RR.AUTHORISER` | `CaplRiRejReason_Authoriser` | String |  |  |
| 16 | `CAPL.RI.RR.CO.CODE` | `CaplRiRejReason_CoCode` | String |  |  |
| 17 | `CAPL.RI.RR.DEPT.CODE` | `CaplRiRejReason_DeptCode` | String |  |  |
| 18 | `CAPL.RI.RR.AUDITOR.CODE` | `CaplRiRejReason_AuditorCode` | String |  |  |
| 19 | `CAPL.RI.RR.AUDIT.DATE.TIME` | `CaplRiRejReason_AuditDateTime` | String |  |  |
