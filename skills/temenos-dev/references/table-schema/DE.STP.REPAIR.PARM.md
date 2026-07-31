# DE.STP.REPAIR.PARM — Table Schema

> Source: `INSERTS/I_F.DE.STP.REPAIR.PARM` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.STP.DESC` | `DeStpRepairParm_Desc` |  |  |  |
| 2 | `DE.STP.CARRIER` | `DeStpRepairParm_Carrier` |  |  |  |
| 3 | `DE.STP.MESSAGE.TYPE` | `DeStpRepairParm_MessageType` |  |  |  |
| 4 | `DE.STP.DIRECTION` | `DeStpRepairParm_Direction` |  |  |  |
| 5 | `DE.STP.RESERVED.5` | `DeStpRepairParm_Reserved5` | TField |  |  |
| 6 | `DE.STP.RESERVED.4` | `DeStpRepairParm_Reserved4` | TField |  |  |
| 7 | `DE.STP.RESERVED.3` | `DeStpRepairParm_Reserved3` | TField |  |  |
| 8 | `DE.STP.RESERVED.2` | `DeStpRepairParm_Reserved2` | TField |  |  |
| 9 | `DE.STP.RESERVED.1` | `DeStpRepairParm_Reserved1` | TField |  |  |
| 10 | `DE.STP.RECORD.STATUS` | `DeStpRepairParm_RecordStatus` | String |  |  |
| 11 | `DE.STP.CURR.NO` | `DeStpRepairParm_CurrNo` | String |  |  |
| 12 | `DE.STP.INPUTTER` | `DeStpRepairParm_Inputter` |  |  |  |
| 13 | `DE.STP.DATE.TIME` | `DeStpRepairParm_DateTime` |  |  |  |
| 14 | `DE.STP.AUTHORISER` | `DeStpRepairParm_Authoriser` | String |  |  |
| 15 | `DE.STP.CO.CODE` | `DeStpRepairParm_CoCode` | String |  |  |
| 16 | `DE.STP.DEPT.CODE` | `DeStpRepairParm_DeptCode` | String |  |  |
| 17 | `DE.STP.AUDITOR.CODE` | `DeStpRepairParm_AuditorCode` | String |  |  |
| 18 | `DE.STP.AUDIT.DATE.TIME` | `DeStpRepairParm_AuditDateTime` | String |  |  |
