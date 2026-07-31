# PP.COMPONENT.API.HOOK — Table Schema

> Source: `INSERTS/I_F.PP.COMPONENT.API.HOOK` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CAH.HookAPIName` | `PpComponentApiHook_Hookapiname` |  |  |  |
| 2 | `PP.CAH.InvokeCall` | `PpComponentApiHook_Invokecall` |  |  |  |
| 3 | `PP.CAH.RESERVED.4` | `PpComponentApiHook_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.CAH.RESERVED.3` | `PpComponentApiHook_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.CAH.RESERVED.2` | `PpComponentApiHook_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.CAH.RESERVED.1` | `PpComponentApiHook_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.CAH.LOCAL.REF` | `PpComponentApiHook_LocalRef` |  |  |  |
| 8 | `PP.CAH.OVERRIDE` | `PpComponentApiHook_Override` |  |  |  |
| 9 | `PP.CAH.RECORD.STATUS` | `PpComponentApiHook_RecordStatus` | String |  |  |
| 10 | `PP.CAH.CURR.NO` | `PpComponentApiHook_CurrNo` | String |  |  |
| 11 | `PP.CAH.INPUTTER` | `PpComponentApiHook_Inputter` |  |  |  |
| 12 | `PP.CAH.DATE.TIME` | `PpComponentApiHook_DateTime` |  |  |  |
| 13 | `PP.CAH.AUTHORISER` | `PpComponentApiHook_Authoriser` | String |  |  |
| 14 | `PP.CAH.CO.CODE` | `PpComponentApiHook_CoCode` | String |  |  |
| 15 | `PP.CAH.DEPT.CODE` | `PpComponentApiHook_DeptCode` | String |  |  |
| 16 | `PP.CAH.AUDITOR.CODE` | `PpComponentApiHook_AuditorCode` | String |  |  |
| 17 | `PP.CAH.AUDIT.DATE.TIME` | `PpComponentApiHook_AuditDateTime` | String |  |  |
