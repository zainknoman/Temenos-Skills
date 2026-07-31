# CAREGS.CDIC.HOLD.CONCAT — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.HOLD.CONCAT` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.HOLD.AKCL.ID` | `CaregsCdicHoldConcat_AkclId` | TField |  |  |
| 2 | `CDIC.HOLD.RESERVED.5` | `CaregsCdicHoldConcat_Reserved5` | TField |  |  |
| 3 | `CDIC.HOLD.RESERVED.4` | `CaregsCdicHoldConcat_Reserved4` | TField |  |  |
| 4 | `CDIC.HOLD.RESERVED.3` | `CaregsCdicHoldConcat_Reserved3` | TField |  |  |
| 5 | `CDIC.HOLD.RESERVED.2` | `CaregsCdicHoldConcat_Reserved2` | TField |  |  |
| 6 | `CDIC.HOLD.RESERVED.1` | `CaregsCdicHoldConcat_Reserved1` | TField |  |  |
| 7 | `CDIC.HOLD.OVERRIDE` | `CaregsCdicHoldConcat_Override` |  |  |  |
| 8 | `CDIC.HOLD.RECORD.STATUS` | `CaregsCdicHoldConcat_RecordStatus` | String |  |  |
| 9 | `CDIC.HOLD.CURR.NO` | `CaregsCdicHoldConcat_CurrNo` | String |  |  |
| 10 | `CDIC.HOLD.INPUTTER` | `CaregsCdicHoldConcat_Inputter` |  |  |  |
| 11 | `CDIC.HOLD.DATE.TIME` | `CaregsCdicHoldConcat_DateTime` |  |  |  |
| 12 | `CDIC.HOLD.AUTHORISER` | `CaregsCdicHoldConcat_Authoriser` | String |  |  |
| 13 | `CDIC.HOLD.CO.CODE` | `CaregsCdicHoldConcat_CoCode` | String |  |  |
| 14 | `CDIC.HOLD.DEPT.CODE` | `CaregsCdicHoldConcat_DeptCode` | String |  |  |
| 15 | `CDIC.HOLD.AUDITOR.CODE` | `CaregsCdicHoldConcat_AuditorCode` | String |  |  |
| 16 | `CDIC.HOLD.AUDIT.DATE.TIME` | `CaregsCdicHoldConcat_AuditDateTime` | String |  |  |
