# CAREGS.CDIC.RESPONSIBLE.PERSON — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.RESPONSIBLE.PERSON` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.RES.PRT.DESCRIPTION` | `CaregsCdicResponsiblePerson_Description` | TField |  | Field to store the description of the title for the responsible person. |
| 2 | `CDIC.RES.PRT.RESERVED.1` | `CaregsCdicResponsiblePerson_Reserved1` | TField |  |  |
| 3 | `CDIC.RES.PRT.RESERVED.2` | `CaregsCdicResponsiblePerson_Reserved2` | TField |  |  |
| 4 | `CDIC.RES.PRT.RESERVED.3` | `CaregsCdicResponsiblePerson_Reserved3` | TField |  |  |
| 5 | `CDIC.RES.PRT.RESERVED.4` | `CaregsCdicResponsiblePerson_Reserved4` | TField |  |  |
| 6 | `CDIC.RES.PRT.RESERVED.5` | `CaregsCdicResponsiblePerson_Reserved5` | TField |  |  |
| 7 | `CDIC.RES.PRT.RECORD.STATUS` | `CaregsCdicResponsiblePerson_RecordStatus` | String |  |  |
| 8 | `CDIC.RES.PRT.CURR.NO` | `CaregsCdicResponsiblePerson_CurrNo` | String |  |  |
| 9 | `CDIC.RES.PRT.INPUTTER` | `CaregsCdicResponsiblePerson_Inputter` |  |  |  |
| 10 | `CDIC.RES.PRT.DATE.TIME` | `CaregsCdicResponsiblePerson_DateTime` |  |  |  |
| 11 | `CDIC.RES.PRT.AUTHORISER` | `CaregsCdicResponsiblePerson_Authoriser` | String |  |  |
| 12 | `CDIC.RES.PRT.CO.CODE` | `CaregsCdicResponsiblePerson_CoCode` | String |  |  |
| 13 | `CDIC.RES.PRT.DEPT.CODE` | `CaregsCdicResponsiblePerson_DeptCode` | String |  |  |
| 14 | `CDIC.RES.PRT.AUDITOR.CODE` | `CaregsCdicResponsiblePerson_AuditorCode` | String |  |  |
| 15 | `CDIC.RES.PRT.AUDIT.DATE.TIME` | `CaregsCdicResponsiblePerson_AuditDateTime` | String |  |  |
