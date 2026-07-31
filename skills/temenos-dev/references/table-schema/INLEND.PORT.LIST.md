# INLEND.PORT.LIST — Table Schema

> Source: `INSERTS/I_F.INLEND.PORT.LIST` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.PORT.PORT.CODE.NAME` | `InlendPortList_PortCodeName` |  |  |  |
| 2 | `INLEND.PORT.PORT.STATE` | `InlendPortList_PortState` | TField |  | State to which the port belongs |
| 3 | `INLEND.PORT.RESERVED.5` | `InlendPortList_Reserved5` | TField |  | Reserved for Future Use. |
| 4 | `INLEND.PORT.RESERVED.4` | `InlendPortList_Reserved4` | TField |  | Reserved for Future Use. |
| 5 | `INLEND.PORT.RESERVED.3` | `InlendPortList_Reserved3` | TField |  | Reserved for Future Use. |
| 6 | `INLEND.PORT.RESERVED.2` | `InlendPortList_Reserved2` | TField |  | Reserved for Future Use. |
| 7 | `INLEND.PORT.RESERVED.1` | `InlendPortList_Reserved1` | TField |  | Reserved for Future Use. |
| 8 | `INLEND.PORT.LOCAL.REF` | `InlendPortList_LocalRef` |  |  |  |
| 9 | `INLEND.PORT.OVERRIDE` | `InlendPortList_Override` |  |  |  |
| 10 | `INLEND.PORT.RECORD.STATUS` | `InlendPortList_RecordStatus` | String |  |  |
| 11 | `INLEND.PORT.CURR.NO` | `InlendPortList_CurrNo` | String |  |  |
| 12 | `INLEND.PORT.INPUTTER` | `InlendPortList_Inputter` |  |  |  |
| 13 | `INLEND.PORT.DATE.TIME` | `InlendPortList_DateTime` |  |  |  |
| 14 | `INLEND.PORT.AUTHORISER` | `InlendPortList_Authoriser` | String |  |  |
| 15 | `INLEND.PORT.CO.CODE` | `InlendPortList_CoCode` | String |  |  |
| 16 | `INLEND.PORT.DEPT.CODE` | `InlendPortList_DeptCode` | String |  |  |
| 17 | `INLEND.PORT.AUDITOR.CODE` | `InlendPortList_AuditorCode` | String |  |  |
| 18 | `INLEND.PORT.AUDIT.DATE.TIME` | `InlendPortList_AuditDateTime` | String |  |  |
