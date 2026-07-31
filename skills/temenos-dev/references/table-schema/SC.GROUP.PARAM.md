# SC.GROUP.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.GROUP.PARAM` in `SC_SctOrderGrouping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.GRP.PRM.SYS.FIELDS` | `ScGroupParam_SysFields` |  |  |  |
| 2 | `SC.GRP.PRM.USER.FIELDS` | `ScGroupParam_UserFields` |  |  |  |
| 3 | `SC.GRP.PRM.SOO.LOC.REF` | `ScGroupParam_SooLocRef` |  |  |  |
| 4 | `SC.GRP.PRM.LOCAL.REF` | `ScGroupParam_LocalRef` | TField |  | LOCAL.REF FIELD |
| 5 | `SC.GRP.PRM.GROUP.ROUTINE` | `ScGroupParam_GroupRoutine` | TField |  | A user defined routine for specifying additional conditions to be checked for routing. Validation Rules: Must exist as a valid program. |
| 6 | `SC.GRP.PRM.CASH.CHK.ROUTINE` | `ScGroupParam_CashChkRoutine` | TField |  |  |
| 7 | `SC.GRP.PRM.CHK.DOMICILE.REGION` | `ScGroupParam_ChkDomicileRegion` | TField |  |  |
| 8 | `SC.GRP.PRM.RESET.CUT.OFF.DATE` | `ScGroupParam_ResetCutOffDate` | TField |  | If this field is set to yes, then the system should recycle the cut-off date when the grouped orders are transmitted manually on the cut-off date before the cut-off time. If set to Null then on the cut-off date, the system will recycle the cut-off date only when the cut-off time is reached. |
| 9 | `SC.GRP.PRM.RESERVED.6` | `ScGroupParam_Reserved6` | TField |  |  |
| 10 | `SC.GRP.PRM.RESERVED.5` | `ScGroupParam_Reserved5` | TField |  |  |
| 11 | `SC.GRP.PRM.RESERVED.4` | `ScGroupParam_Reserved4` | TField |  |  |
| 12 | `SC.GRP.PRM.RESERVED.3` | `ScGroupParam_Reserved3` | TField |  |  |
| 13 | `SC.GRP.PRM.RESERVED.2` | `ScGroupParam_Reserved2` | TField |  |  |
| 14 | `SC.GRP.PRM.RESERVED.1` | `ScGroupParam_Reserved1` | TField |  |  |
| 15 | `SC.GRP.PRM.RECORD.STATUS` | `ScGroupParam_RecordStatus` | String |  |  |
| 16 | `SC.GRP.PRM.CURR.NO` | `ScGroupParam_CurrNo` | String |  |  |
| 17 | `SC.GRP.PRM.INPUTTER` | `ScGroupParam_Inputter` |  |  |  |
| 18 | `SC.GRP.PRM.DATE.TIME` | `ScGroupParam_DateTime` |  |  |  |
| 19 | `SC.GRP.PRM.AUTHORISER` | `ScGroupParam_Authoriser` | String |  |  |
| 20 | `SC.GRP.PRM.CO.CODE` | `ScGroupParam_CoCode` | String |  |  |
| 21 | `SC.GRP.PRM.DEPT.CODE` | `ScGroupParam_DeptCode` | String |  |  |
| 22 | `SC.GRP.PRM.AUDITOR.CODE` | `ScGroupParam_AuditorCode` | String |  |  |
| 23 | `SC.GRP.PRM.AUDIT.DATE.TIME` | `ScGroupParam_AuditDateTime` | String |  |  |
