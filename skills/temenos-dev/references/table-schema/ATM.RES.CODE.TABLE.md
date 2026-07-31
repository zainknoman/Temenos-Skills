# ATM.RES.CODE.TABLE — Table Schema

> Source: `INSERTS/I_F.ATM.RES.CODE.TABLE` in `ATMFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AT.RES.CDE.DESCRIPTION` | `AtmResCodeTable_Description` |  |  |  |
| 2 | `AT.RES.CDE.MESSAGE` | `AtmResCodeTable_Message` |  |  |  |
| 3 | `AT.RES.CDE.RESPONSE.CODE` | `AtmResCodeTable_ResponseCode` |  |  |  |
| 4 | `AT.RES.CDE.RESERVED.5` | `AtmResCodeTable_Reserved5` |  |  |  |
| 5 | `AT.RES.CDE.RESERVED.4` | `AtmResCodeTable_Reserved4` |  |  |  |
| 6 | `AT.RES.CDE.RESERVED.3` | `AtmResCodeTable_Reserved3` |  |  |  |
| 7 | `AT.RES.CDE.RESERVED.2` | `AtmResCodeTable_Reserved2` |  |  |  |
| 8 | `AT.RES.CDE.RESERVED.1` | `AtmResCodeTable_Reserved1` |  |  |  |
| 9 | `AT.RES.CDE.PASS.RESP.CODE` | `AtmResCodeTable_PassRespCode` | TField |  |  |
| 10 | `AT.RES.CDE.FAIL.RESP.CODE` | `AtmResCodeTable_FailRespCode` | TField |  |  |
| 11 | `AT.RES.CDE.LOCAL.REF` | `AtmResCodeTable_LocalRef` |  |  |  |
| 12 | `AT.RES.CDE.GEN.ERR.MSG` | `AtmResCodeTable_GenErrMsg` |  |  |  |
| 13 | `AT.RES.CDE.GEN.RESP.CODE` | `AtmResCodeTable_GenRespCode` |  |  |  |
| 14 | `AT.RES.CDE.PARTIAL.AUTH.RESP.CODE` | `AtmResCodeTable_PartialAuthRespCode` | TField |  |  |
| 15 | `AT.RES.CDE.RESERVED.7` | `AtmResCodeTable_Reserved7` | TField |  |  |
| 16 | `AT.RES.CDE.RESERVED.6` | `AtmResCodeTable_Reserved6` | TField |  |  |
| 17 | `AT.RES.CDE.RECORD.STATUS` | `AtmResCodeTable_RecordStatus` | String |  |  |
| 18 | `AT.RES.CDE.CURR.NO` | `AtmResCodeTable_CurrNo` | String |  |  |
| 19 | `AT.RES.CDE.INPUTTER` | `AtmResCodeTable_Inputter` |  |  |  |
| 20 | `AT.RES.CDE.DATE.TIME` | `AtmResCodeTable_DateTime` |  |  |  |
| 21 | `AT.RES.CDE.AUTHORISER` | `AtmResCodeTable_Authoriser` | String |  |  |
| 22 | `AT.RES.CDE.CO.CODE` | `AtmResCodeTable_CoCode` | String |  |  |
| 23 | `AT.RES.CDE.DEPT.CODE` | `AtmResCodeTable_DeptCode` | String |  |  |
| 24 | `AT.RES.CDE.AUDITOR.CODE` | `AtmResCodeTable_AuditorCode` | String |  |  |
| 25 | `AT.RES.CDE.AUDIT.DATE.TIME` | `AtmResCodeTable_AuditDateTime` | String |  |  |
