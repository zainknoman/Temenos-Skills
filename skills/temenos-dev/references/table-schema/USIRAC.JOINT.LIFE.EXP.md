# USIRAC.JOINT.LIFE.EXP — Table Schema

> Source: `INSERTS/I_F.USIRAC.JOINT.LIFE.EXP` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `JOINT.LE.BEN.LIFE.EXPECTANCY` | `UsiracJointLifeExp_BenLifeExpectancy` | TField |  |  |
| 2 | `JOINT.LE.RESERVED.9` | `UsiracJointLifeExp_Reserved9` | TField |  |  |
| 3 | `JOINT.LE.RESERVED.8` | `UsiracJointLifeExp_Reserved8` | TField |  |  |
| 4 | `JOINT.LE.RESERVED.7` | `UsiracJointLifeExp_Reserved7` | TField |  |  |
| 5 | `JOINT.LE.RESERVED.6` | `UsiracJointLifeExp_Reserved6` | TField |  |  |
| 6 | `JOINT.LE.RESERVED.5` | `UsiracJointLifeExp_Reserved5` | TField |  |  |
| 7 | `JOINT.LE.RESERVED.4` | `UsiracJointLifeExp_Reserved4` | TField |  |  |
| 8 | `JOINT.LE.RESERVED.3` | `UsiracJointLifeExp_Reserved3` | TField |  |  |
| 9 | `JOINT.LE.RESERVED.2` | `UsiracJointLifeExp_Reserved2` | TField |  |  |
| 10 | `JOINT.LE.RESERVED.1` | `UsiracJointLifeExp_Reserved1` | TField |  |  |
| 11 | `JOINT.LE.OVERRIDE` | `UsiracJointLifeExp_Override` |  |  |  |
| 12 | `JOINT.LE.RECORD.STATUS` | `UsiracJointLifeExp_RecordStatus` | String |  |  |
| 13 | `JOINT.LE.CURR.NO` | `UsiracJointLifeExp_CurrNo` | String |  |  |
| 14 | `JOINT.LE.INPUTTER` | `UsiracJointLifeExp_Inputter` |  |  |  |
| 15 | `JOINT.LE.DATE.TIME` | `UsiracJointLifeExp_DateTime` |  |  |  |
| 16 | `JOINT.LE.AUTHORISER` | `UsiracJointLifeExp_Authoriser` | String |  |  |
| 17 | `JOINT.LE.CO.CODE` | `UsiracJointLifeExp_CoCode` | String |  |  |
| 18 | `JOINT.LE.DEPT.CODE` | `UsiracJointLifeExp_DeptCode` | String |  |  |
| 19 | `JOINT.LE.AUDITOR.CODE` | `UsiracJointLifeExp_AuditorCode` | String |  |  |
| 20 | `JOINT.LE.AUDIT.DATE.TIME` | `UsiracJointLifeExp_AuditDateTime` | String |  |  |
