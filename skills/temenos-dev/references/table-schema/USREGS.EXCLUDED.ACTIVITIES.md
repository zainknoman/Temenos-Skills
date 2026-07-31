# USREGS.EXCLUDED.ACTIVITIES — Table Schema

> Source: `INSERTS/I_F.USREGS.EXCLUDED.ACTIVITIES` in `USREGS_Escheat.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USREGS.EXCL.ACT.EFFECTIVE.DATE` | `ExcludedActivities_EffectiveDate` |  |  |  |
| 2 | `USREGS.EXCL.ACT.ACTIVITY.REF` | `ExcludedActivities_ActivityRef` |  |  |  |
| 3 | `USREGS.EXCL.ACT.ACTIVITY` | `ExcludedActivities_Activity` |  |  |  |
| 4 | `USREGS.EXCL.ACT.DESCRIPTION` | `ExcludedActivities_Description` |  |  |  |
| 5 | `USREGS.EXCL.ACT.STATUS` | `ExcludedActivities_Status` |  |  |  |
| 6 | `USREGS.EXCL.ACT.RESERVED.10` | `ExcludedActivities_Reserved8` |  |  |  |
| 7 | `USREGS.EXCL.ACT.RESERVED.9` | `ExcludedActivities_Reserved7` |  |  |  |
| 8 | `USREGS.EXCL.ACT.RESERVED.8` | `ExcludedActivities_Reserved8` |  |  |  |
| 9 | `USREGS.EXCL.ACT.RESERVED.7` | `ExcludedActivities_Reserved7` |  |  |  |
| 10 | `USREGS.EXCL.ACT.RESERVED.6` | `ExcludedActivities_Reserved6` |  |  |  |
| 11 | `USREGS.EXCL.ACT.RESERVED.5` | `ExcludedActivities_Reserved5` |  |  |  |
| 12 | `USREGS.EXCL.ACT.RESERVED.4` | `ExcludedActivities_Reserved4` |  |  |  |
| 13 | `USREGS.EXCL.ACT.RESERVED.3` | `ExcludedActivities_Reserved3` |  |  |  |
| 14 | `USREGS.EXCL.ACT.RESERVED.2` | `ExcludedActivities_Reserved2` |  |  |  |
| 15 | `USREGS.EXCL.ACT.RESERVED.1` | `ExcludedActivities_Reserved1` |  |  |  |
| 16 | `USREGS.EXCL.ACT.LOCAL.REF` | `ExcludedActivities_LocalRef` |  |  |  |
| 17 | `USREGS.EXCL.ACT.OVERRIDE` | `ExcludedActivities_Override` |  |  |  |
| 18 | `USREGS.EXCL.ACT.RECORD.STATUS` | `ExcludedActivities_RecordStatus` |  |  |  |
| 19 | `USREGS.EXCL.ACT.CURR.NO` | `ExcludedActivities_CurrNo` |  |  |  |
| 20 | `USREGS.EXCL.ACT.INPUTTER` | `ExcludedActivities_Inputter` |  |  |  |
| 21 | `USREGS.EXCL.ACT.DATE.TIME` | `ExcludedActivities_DateTime` |  |  |  |
| 22 | `USREGS.EXCL.ACT.AUTHORISER` | `ExcludedActivities_Authoriser` |  |  |  |
| 23 | `USREGS.EXCL.ACT.CO.CODE` | `ExcludedActivities_CoCode` |  |  |  |
| 24 | `USREGS.EXCL.ACT.DEPT.CODE` | `ExcludedActivities_DeptCode` |  |  |  |
| 25 | `USREGS.EXCL.ACT.AUDITOR.CODE` | `ExcludedActivities_AuditorCode` |  |  |  |
| 26 | `USREGS.EXCL.ACT.AUDIT.DATE.TIME` | `ExcludedActivities_AuditDateTime` |  |  |  |
