# NSF.DESK.GROUP — Table Schema

> Source: `INSERTS/I_F.NSF.DESK.GROUP` in `NSFDES_DeskMgmt.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DSK.GRP.DESCRIPTION` | `NsfDeskGroup_Description` |  |  |  |
| 2 | `DSK.GRP.DESK.ID` | `NsfDeskGroup_DeskId` |  |  |  |
| 3 | `DSK.GRP.ALERT.LEVEL` | `NsfDeskGroup_AlertLevel` |  |  |  |
| 4 | `DSK.GRP.RESERVED.10` | `NsfDeskGroup_Reserved10` | TField |  |  |
| 5 | `DSK.GRP.RESERVED.9` | `NsfDeskGroup_Reserved9` | TField |  |  |
| 6 | `DSK.GRP.RESERVED.8` | `NsfDeskGroup_Reserved8` | TField |  |  |
| 7 | `DSK.GRP.RESERVED.7` | `NsfDeskGroup_Reserved7` | TField |  |  |
| 8 | `DSK.GRP.RESERVED.6` | `NsfDeskGroup_Reserved6` | TField |  |  |
| 9 | `DSK.GRP.RESERVED.5` | `NsfDeskGroup_Reserved5` | TField |  |  |
| 10 | `DSK.GRP.RESERVED.4` | `NsfDeskGroup_Reserved4` | TField |  |  |
| 11 | `DSK.GRP.RESERVED.3` | `NsfDeskGroup_Reserved3` | TField |  |  |
| 12 | `DSK.GRP.RESERVED.2` | `NsfDeskGroup_Reserved2` | TField |  |  |
| 13 | `DSK.GRP.RESERVED.1` | `NsfDeskGroup_Reserved1` | TField |  |  |
| 14 | `DSK.GRP.LOCAL.REF` | `NsfDeskGroup_LocalRef` |  |  |  |
| 15 | `DSK.GRP.OVERRIDE` | `NsfDeskGroup_Override` |  |  |  |
| 16 | `DSK.GRP.RECORD.STATUS` | `NsfDeskGroup_RecordStatus` | String |  |  |
| 17 | `DSK.GRP.CURR.NO` | `NsfDeskGroup_CurrNo` | String |  |  |
| 18 | `DSK.GRP.INPUTTER` | `NsfDeskGroup_Inputter` |  |  |  |
| 19 | `DSK.GRP.DATE.TIME` | `NsfDeskGroup_DateTime` |  |  |  |
| 20 | `DSK.GRP.AUTHORISER` | `NsfDeskGroup_Authoriser` | String |  |  |
| 21 | `DSK.GRP.CO.CODE` | `NsfDeskGroup_CoCode` | String |  |  |
| 22 | `DSK.GRP.DEPT.CODE` | `NsfDeskGroup_DeptCode` | String |  |  |
| 23 | `DSK.GRP.AUDITOR.CODE` | `NsfDeskGroup_AuditorCode` | String |  |  |
| 24 | `DSK.GRP.AUDIT.DATE.TIME` | `NsfDeskGroup_AuditDateTime` | String |  |  |
