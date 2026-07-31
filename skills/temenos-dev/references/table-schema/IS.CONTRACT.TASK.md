# IS.CONTRACT.TASK — Table Schema

> Source: `INSERTS/I_F.IS.CONTRACT.TASK` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.CNT.ACTION.TEXT` | `IsContractTask_ActionText` |  |  |  |
| 2 | `IS.CNT.RESERVED.5` | `IsContractTask_Reserved5` | TField |  |  |
| 3 | `IS.CNT.RESERVED.4` | `IsContractTask_Reserved4` | TField |  |  |
| 4 | `IS.CNT.RESERVED.3` | `IsContractTask_Reserved3` | TField |  |  |
| 5 | `IS.CNT.RESERVED.2` | `IsContractTask_Reserved2` | TField |  |  |
| 6 | `IS.CNT.RESERVED.1` | `IsContractTask_Reserved1` | TField |  |  |
| 7 | `IS.CNT.LOCAL.REF` | `IsContractTask_LocalRef` |  |  |  |
| 8 | `IS.CNT.OVERRIDE` | `IsContractTask_Override` |  |  |  |
| 9 | `IS.CNT.RECORD.STATUS` | `IsContractTask_RecordStatus` | String |  |  |
| 10 | `IS.CNT.CURR.NO` | `IsContractTask_CurrNo` | String |  |  |
| 11 | `IS.CNT.INPUTTER` | `IsContractTask_Inputter` |  |  |  |
| 12 | `IS.CNT.DATE.TIME` | `IsContractTask_DateTime` |  |  |  |
| 13 | `IS.CNT.AUTHORISER` | `IsContractTask_Authoriser` | String |  |  |
| 14 | `IS.CNT.CO.CODE` | `IsContractTask_CoCode` | String |  |  |
| 15 | `IS.CNT.DEPT.CODE` | `IsContractTask_DeptCode` | String |  |  |
| 16 | `IS.CNT.AUDITOR.CODE` | `IsContractTask_AuditorCode` | String |  |  |
| 17 | `IS.CNT.AUDIT.DATE.TIME` | `IsContractTask_AuditDateTime` | String |  |  |
