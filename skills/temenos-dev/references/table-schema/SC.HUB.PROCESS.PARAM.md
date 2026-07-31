# SC.HUB.PROCESS.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.HUB.PROCESS.PARAM` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.HPP.COMPANY` | `ScHubProcessParam_Company` | TField |  | Company specified in the first part of Id is defaulted in this field. Validation Rules: No Input field. |
| 2 | `SC.HPP.APPLICATION` | `ScHubProcessParam_Application` | TField |  | Application specified in the second part of Id will be defaulted by the system Validation Rules: No Input field. |
| 3 | `SC.HPP.APP.FILE` | `ScHubProcessParam_AppFile` |  |  |  |
| 4 | `SC.HPP.APP.FIELD` | `ScHubProcessParam_AppField` |  |  |  |
| 5 | `SC.HPP.APP.OPERAND` | `ScHubProcessParam_AppOperand` |  |  |  |
| 6 | `SC.HPP.APP.VALUE` | `ScHubProcessParam_AppValue` |  |  |  |
| 7 | `SC.HPP.JOINTS` | `ScHubProcessParam_Joints` |  |  |  |
| 8 | `SC.HPP.RESERVED15` | `ScHubProcessParam_Reserved15` | TField |  |  |
| 9 | `SC.HPP.RESERVED14` | `ScHubProcessParam_Reserved14` | TField |  |  |
| 10 | `SC.HPP.RESERVED13` | `ScHubProcessParam_Reserved13` | TField |  |  |
| 11 | `SC.HPP.RESERVED12` | `ScHubProcessParam_Reserved12` | TField |  |  |
| 12 | `SC.HPP.RESERVED11` | `ScHubProcessParam_Reserved11` | TField |  |  |
| 13 | `SC.HPP.RESERVED10` | `ScHubProcessParam_Reserved10` | TField |  |  |
| 14 | `SC.HPP.RESERVED9` | `ScHubProcessParam_Reserved9` | TField |  |  |
| 15 | `SC.HPP.RESERVED8` | `ScHubProcessParam_Reserved8` | TField |  |  |
| 16 | `SC.HPP.RESERVED7` | `ScHubProcessParam_Reserved7` | TField |  |  |
| 17 | `SC.HPP.RESERVED6` | `ScHubProcessParam_Reserved6` | TField |  |  |
| 18 | `SC.HPP.RESERVED5` | `ScHubProcessParam_Reserved5` | TField |  |  |
| 19 | `SC.HPP.RESERVED4` | `ScHubProcessParam_Reserved4` | TField |  |  |
| 20 | `SC.HPP.RESERVED3` | `ScHubProcessParam_Reserved3` | TField |  |  |
| 21 | `SC.HPP.RESERVED2` | `ScHubProcessParam_Reserved2` | TField |  |  |
| 22 | `SC.HPP.RESERVED1` | `ScHubProcessParam_Reserved1` | TField |  |  |
| 23 | `SC.HPP.LOCAL.REF` | `ScHubProcessParam_LocalRef` |  |  |  |
| 24 | `SC.HPP.OVERRIDE` | `ScHubProcessParam_Override` |  |  |  |
| 25 | `SC.HPP.RECORD.STATUS` | `ScHubProcessParam_RecordStatus` | String |  |  |
| 26 | `SC.HPP.CURR.NO` | `ScHubProcessParam_CurrNo` | String |  |  |
| 27 | `SC.HPP.INPUTTER` | `ScHubProcessParam_Inputter` |  |  |  |
| 28 | `SC.HPP.DATE.TIME` | `ScHubProcessParam_DateTime` |  |  |  |
| 29 | `SC.HPP.AUTHORISER` | `ScHubProcessParam_Authoriser` | String |  |  |
| 30 | `SC.HPP.CO.CODE` | `ScHubProcessParam_CoCode` | String |  |  |
| 31 | `SC.HPP.DEPT.CODE` | `ScHubProcessParam_DeptCode` | String |  |  |
| 32 | `SC.HPP.AUDITOR.CODE` | `ScHubProcessParam_AuditorCode` | String |  |  |
| 33 | `SC.HPP.AUDIT.DATE.TIME` | `ScHubProcessParam_AuditDateTime` | String |  |  |
