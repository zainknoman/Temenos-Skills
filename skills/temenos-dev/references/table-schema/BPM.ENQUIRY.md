# BPM.ENQUIRY — Table Schema

> Source: `INSERTS/I_F.BPM.ENQUIRY` in `JP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `JP.BPM.PROCESS.NO` | `BpmEnquiry_ProcessNo` |  |  |  |
| 2 | `JP.BPM.BUSINESS.VAR.NAME` | `BpmEnquiry_BusinessVarName` |  |  |  |
| 3 | `JP.BPM.BUSINESS.VAR.VALUE` | `BpmEnquiry_BusinessVarValue` |  |  |  |
| 4 | `JP.BPM.TASK.ID` | `BpmEnquiry_TaskId` |  |  |  |
| 5 | `JP.BPM.TASK.STATUS` | `BpmEnquiry_TaskStatus` |  |  |  |
| 6 | `JP.BPM.PROCESS.PW` | `BpmEnquiry_ProcessPw` |  |  |  |
| 7 | `JP.BPM.PW.ACT.DESC` | `BpmEnquiry_PwActDesc` |  |  |  |
| 8 | `JP.BPM.PW.STATUS` | `BpmEnquiry_PwStatus` |  |  |  |
| 9 | `JP.BPM.DISP.ID` | `BpmEnquiry_DispId` |  |  |  |
| 10 | `JP.BPM.DATE` | `BpmEnquiry_Date` |  |  |  |
| 11 | `JP.BPM.PW.ACTIVITY` | `BpmEnquiry_PwActivity` |  |  |  |
| 12 | `JP.BPM.DISP.REF.ID` | `BpmEnquiry_DispRefId` |  |  |  |
| 13 | `JP.BPM.PROCESS.NAME` | `BpmEnquiry_ProcessName` |  |  |  |
| 14 | `JP.BPM.PW.ACTIVITY.TXN.ID` | `BpmEnquiry_PwActivityTxnId` |  |  |  |
| 15 | `JP.BPM.DEPT` | `BpmEnquiry_Dept` |  |  |  |
| 16 | `JP.BPM.OWNER` | `BpmEnquiry_Owner` |  |  |  |
| 17 | `JP.BPM.REF.ID` | `BpmEnquiry_RefId` |  |  |  |
| 18 | `JP.BPM.RECORD.STATUS` | `BpmEnquiry_RecordStatus` |  |  |  |
| 19 | `JP.BPM.CURR.NO` | `BpmEnquiry_CurrNo` |  |  |  |
| 20 | `JP.BPM.INPUTTER` | `BpmEnquiry_Inputter` |  |  |  |
| 21 | `JP.BPM.DATE.TIME` | `BpmEnquiry_DateTime` |  |  |  |
| 22 | `JP.BPM.AUTHORISER` | `BpmEnquiry_Authoriser` |  |  |  |
| 23 | `JP.BPM.CO.CODE` | `BpmEnquiry_CoCode` |  |  |  |
| 24 | `JP.BPM.DEPT.CODE` | `BpmEnquiry_DeptCode` |  |  |  |
| 25 | `JP.BPM.AUDITOR.CODE` | `BpmEnquiry_AuditorCode` |  |  |  |
| 26 | `JP.BPM.AUDIT.DATE.TIME` | `BpmEnquiry_AuditDateTime` |  |  |  |
