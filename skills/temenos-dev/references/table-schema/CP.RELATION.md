# CP.RELATION — Table Schema

> Source: `INSERTS/I_F.CP.RELATION` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.REL.APP.NAME` | `CpRelation_AppName` |  |  |  |
| 2 | `CP.REL.DAS.VALUE` | `CpRelation_DasValue` |  |  |  |
| 3 | `CP.REL.DAS.NUMBER` | `CpRelation_DasNumber` |  |  |  |
| 4 | `CP.REL.EXCEPTION` | `CpRelation_Exception` |  |  |  |
| 5 | `CP.REL.RESERVED.9` | `CpRelation_Reserved9` | TField |  |  |
| 6 | `CP.REL.RESERVED.8` | `CpRelation_Reserved8` | TField |  |  |
| 7 | `CP.REL.RESERVED.7` | `CpRelation_Reserved7` | TField |  |  |
| 8 | `CP.REL.RESERVED.6` | `CpRelation_Reserved6` | TField |  |  |
| 9 | `CP.REL.RESERVED.5` | `CpRelation_Reserved5` | TField |  |  |
| 10 | `CP.REL.RESERVED.4` | `CpRelation_Reserved4` | TField |  |  |
| 11 | `CP.REL.RESERVED.3` | `CpRelation_Reserved3` | TField |  |  |
| 12 | `CP.REL.RESERVED.2` | `CpRelation_Reserved2` | TField |  |  |
| 13 | `CP.REL.RESERVED.1` | `CpRelation_Reserved1` | TField |  |  |
| 14 | `CP.REL.LOCAL.REF` | `CpRelation_LocalRef` |  |  |  |
| 15 | `CP.REL.OVERRIDE` | `CpRelation_Override` |  |  |  |
| 16 | `CP.REL.RECORD.STATUS` | `CpRelation_RecordStatus` | String |  |  |
| 17 | `CP.REL.CURR.NO` | `CpRelation_CurrNo` | String |  |  |
| 18 | `CP.REL.INPUTTER` | `CpRelation_Inputter` |  |  |  |
| 19 | `CP.REL.DATE.TIME` | `CpRelation_DateTime` |  |  |  |
| 20 | `CP.REL.AUTHORISER` | `CpRelation_Authoriser` | String |  |  |
| 21 | `CP.REL.CO.CODE` | `CpRelation_CoCode` | String |  |  |
| 22 | `CP.REL.DEPT.CODE` | `CpRelation_DeptCode` | String |  |  |
| 23 | `CP.REL.AUDITOR.CODE` | `CpRelation_AuditorCode` | String |  |  |
| 24 | `CP.REL.AUDIT.DATE.TIME` | `CpRelation_AuditDateTime` | String |  |  |
