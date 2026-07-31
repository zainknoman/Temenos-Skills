# VL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.VL.PARAMETER` in `VL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VLP.APPLICATION` | `VlParameter_Application` |  |  |  |
| 2 | `VLP.AML.CHECK` | `VlParameter_AmlCheck` |  |  |  |
| 3 | `VLP.AML.STATUS` | `VlParameter_AmlStatus` |  |  |  |
| 4 | `VLP.AML.STATUS.DESC` | `VlParameter_AmlStatusDesc` |  |  |  |
| 5 | `VLP.LOCAL.REF` | `VlParameter_LocalRef` |  |  |  |
| 6 | `VLP.OVERRIDE` | `VlParameter_Override` |  |  |  |
| 7 | `VLP.RECORD.STATUS` | `VlParameter_RecordStatus` | String |  |  |
| 8 | `VLP.CURR.NO` | `VlParameter_CurrNo` | String |  |  |
| 9 | `VLP.INPUTTER` | `VlParameter_Inputter` |  |  |  |
| 10 | `VLP.DATE.TIME` | `VlParameter_DateTime` |  |  |  |
| 11 | `VLP.AUTHORISER` | `VlParameter_Authoriser` | String |  |  |
| 12 | `VLP.CO.CODE` | `VlParameter_CoCode` | String |  |  |
| 13 | `VLP.DEPT.CODE` | `VlParameter_DeptCode` | String |  |  |
| 14 | `VLP.AUDITOR.CODE` | `VlParameter_AuditorCode` | String |  |  |
| 15 | `VLP.AUDIT.DATE.TIME` | `VlParameter_AuditDateTime` | String |  |  |
| 16 | `VLP.STP.RESPONSE` | `VlParameter_StpResponse` | TField |  | This is used for enabling straight through processing of responses received from FCM. When this is set Dispo processing will be skipped, this means it will not require OFS.MESSAGE.SERVICE/VL.PROCESS.RESPONSE to process the response. The transaction will either authorized/deleted at the OFS In.Msg.Rtn itself. |
| 17 | `VLP.RESP.WAIT.TIME` | `VlParameter_RespWaitTime` | TField |  | Maximum milliseconds should wait for processing the response. |
| 18 | `VLP.RESP.RETRY.NO` | `VlParameter_RespRetryNo` | TField |  | Retry no. of times on processing the response. |
