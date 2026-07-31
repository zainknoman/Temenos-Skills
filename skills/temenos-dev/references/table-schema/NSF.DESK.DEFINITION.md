# NSF.DESK.DEFINITION — Table Schema

> Source: `INSERTS/I_F.NSF.DESK.DEFINITION` in `NSFDES_DeskMgmt.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DSK.DEFN.DESCRIPTION` | `NsfDeskDefinition_Description` |  |  |  |
| 2 | `DSK.DEFN.ALERT.LEVEL` | `NsfDeskDefinition_AlertLevel` |  |  |  |
| 3 | `DSK.DEFN.RESERVED.10` | `NsfDeskDefinition_Reserved10` | TField |  |  |
| 4 | `DSK.DEFN.RESERVED.9` | `NsfDeskDefinition_Reserved9` | TField |  |  |
| 5 | `DSK.DEFN.RESERVED.8` | `NsfDeskDefinition_Reserved8` | TField |  |  |
| 6 | `DSK.DEFN.RESERVED.7` | `NsfDeskDefinition_Reserved7` | TField |  |  |
| 7 | `DSK.DEFN.RESERVED.6` | `NsfDeskDefinition_Reserved6` | TField |  |  |
| 8 | `DSK.DEFN.RESERVED.5` | `NsfDeskDefinition_Reserved5` | TField |  |  |
| 9 | `DSK.DEFN.RESERVED.4` | `NsfDeskDefinition_Reserved4` | TField |  |  |
| 10 | `DSK.DEFN.RESERVED.3` | `NsfDeskDefinition_Reserved3` | TField |  |  |
| 11 | `DSK.DEFN.RESERVED.2` | `NsfDeskDefinition_Reserved2` | TField |  |  |
| 12 | `DSK.DEFN.RESERVED.1` | `NsfDeskDefinition_Reserved1` | TField |  |  |
| 13 | `DSK.DEFN.LOCAL.REF` | `NsfDeskDefinition_LocalRef` |  |  |  |
| 14 | `DSK.DEFN.OVERRIDE` | `NsfDeskDefinition_Override` |  |  |  |
| 15 | `DSK.DEFN.RECORD.STATUS` | `NsfDeskDefinition_RecordStatus` | String |  |  |
| 16 | `DSK.DEFN.CURR.NO` | `NsfDeskDefinition_CurrNo` | String |  |  |
| 17 | `DSK.DEFN.INPUTTER` | `NsfDeskDefinition_Inputter` |  |  |  |
| 18 | `DSK.DEFN.DATE.TIME` | `NsfDeskDefinition_DateTime` |  |  |  |
| 19 | `DSK.DEFN.AUTHORISER` | `NsfDeskDefinition_Authoriser` | String |  |  |
| 20 | `DSK.DEFN.CO.CODE` | `NsfDeskDefinition_CoCode` | String |  |  |
| 21 | `DSK.DEFN.DEPT.CODE` | `NsfDeskDefinition_DeptCode` | String |  |  |
| 22 | `DSK.DEFN.AUDITOR.CODE` | `NsfDeskDefinition_AuditorCode` | String |  |  |
| 23 | `DSK.DEFN.AUDIT.DATE.TIME` | `NsfDeskDefinition_AuditDateTime` | String |  |  |
