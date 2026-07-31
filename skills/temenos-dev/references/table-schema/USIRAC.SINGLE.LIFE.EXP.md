# USIRAC.SINGLE.LIFE.EXP — Table Schema

> Source: `INSERTS/I_F.USIRAC.SINGLE.LIFE.EXP` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SINGLE.LE.LIFE.EXPECTANCY` | `UsiracSingleLifeExp_LifeExpectancy` | TField | Yes | This field shows the life expectancy of IRA participants Mandatory Field, Text Field 5 digits is inclusive of decimal points For example 70.50, 20.60 |
| 2 | `SINGLE.LE.DISTRIB.PERIOD` | `UsiracSingleLifeExp_DistribPeriod` | TField |  |  |
| 3 | `SINGLE.LE.RESERVED.9` | `UsiracSingleLifeExp_Reserved9` | TField |  |  |
| 4 | `SINGLE.LE.RESERVED.8` | `UsiracSingleLifeExp_Reserved8` | TField |  |  |
| 5 | `SINGLE.LE.RESERVED.7` | `UsiracSingleLifeExp_Reserved7` | TField |  |  |
| 6 | `SINGLE.LE.RESERVED.6` | `UsiracSingleLifeExp_Reserved6` | TField |  |  |
| 7 | `SINGLE.LE.RESERVED.5` | `UsiracSingleLifeExp_Reserved5` | TField |  |  |
| 8 | `SINGLE.LE.RESERVED.4` | `UsiracSingleLifeExp_Reserved4` | TField |  |  |
| 9 | `SINGLE.LE.RESERVED.3` | `UsiracSingleLifeExp_Reserved3` | TField |  |  |
| 10 | `SINGLE.LE.RESERVED.2` | `UsiracSingleLifeExp_Reserved2` | TField |  |  |
| 11 | `SINGLE.LE.RESERVED.1` | `UsiracSingleLifeExp_Reserved1` | TField |  |  |
| 12 | `SINGLE.LE.OVERRIDE` | `UsiracSingleLifeExp_Override` |  |  |  |
| 13 | `SINGLE.LE.RECORD.STATUS` | `UsiracSingleLifeExp_RecordStatus` | String |  |  |
| 14 | `SINGLE.LE.CURR.NO` | `UsiracSingleLifeExp_CurrNo` | String |  |  |
| 15 | `SINGLE.LE.INPUTTER` | `UsiracSingleLifeExp_Inputter` |  |  |  |
| 16 | `SINGLE.LE.DATE.TIME` | `UsiracSingleLifeExp_DateTime` |  |  |  |
| 17 | `SINGLE.LE.AUTHORISER` | `UsiracSingleLifeExp_Authoriser` | String |  |  |
| 18 | `SINGLE.LE.CO.CODE` | `UsiracSingleLifeExp_CoCode` | String |  |  |
| 19 | `SINGLE.LE.DEPT.CODE` | `UsiracSingleLifeExp_DeptCode` | String |  |  |
| 20 | `SINGLE.LE.AUDITOR.CODE` | `UsiracSingleLifeExp_AuditorCode` | String |  |  |
| 21 | `SINGLE.LE.AUDIT.DATE.TIME` | `UsiracSingleLifeExp_AuditDateTime` | String |  |  |
