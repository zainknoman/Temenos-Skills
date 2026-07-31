# AC.DEFINE.PAY.RECV.ALLOWED — Table Schema

> Source: `INSERTS/I_F.AC.DEFINE.PAY.RECV.ALLOWED` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAY.REC.PAY.RECV.OPTIONS` | `AcDefinePayRecvAllowed_PayRecvOptions` |  |  |  |
| 2 | `PAY.REC.LOCAL.REF` | `AcDefinePayRecvAllowed_LocalRef` |  |  |  |
| 3 | `PAY.REC.OVERRIDE` | `AcDefinePayRecvAllowed_Override` |  |  |  |
| 4 | `PAY.REC.RECORD.STATUS` | `AcDefinePayRecvAllowed_RecordStatus` | String |  |  |
| 5 | `PAY.REC.CURR.NO` | `AcDefinePayRecvAllowed_CurrNo` | String |  |  |
| 6 | `PAY.REC.INPUTTER` | `AcDefinePayRecvAllowed_Inputter` |  |  |  |
| 7 | `PAY.REC.DATE.TIME` | `AcDefinePayRecvAllowed_DateTime` |  |  |  |
| 8 | `PAY.REC.AUTHORISER` | `AcDefinePayRecvAllowed_Authoriser` | String |  |  |
| 9 | `PAY.REC.CO.CODE` | `AcDefinePayRecvAllowed_CoCode` | String |  |  |
| 10 | `PAY.REC.DEPT.CODE` | `AcDefinePayRecvAllowed_DeptCode` | String |  |  |
| 11 | `PAY.REC.AUDITOR.CODE` | `AcDefinePayRecvAllowed_AuditorCode` | String |  |  |
| 12 | `PAY.REC.AUDIT.DATE.TIME` | `AcDefinePayRecvAllowed_AuditDateTime` | String |  |  |
