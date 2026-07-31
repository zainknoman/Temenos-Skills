# FS.MOCKUP — Table Schema

> Source: `INSERTS/I_F.FS.MOCKUP` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.MK.DESCRIPTION` | `FsMockup_Description` |  |  |  |
| 2 | `FS.MK.APPL.RESPONSE` | `FsMockup_ApplResponse` |  |  |  |
| 3 | `FS.MK.RESERVED10` | `FsMockup_Reserved10` | TField |  |  |
| 4 | `FS.MK.RESERVED9` | `FsMockup_Reserved9` | TField |  |  |
| 5 | `FS.MK.RESERVED8` | `FsMockup_Reserved8` | TField |  |  |
| 6 | `FS.MK.RESERVED7` | `FsMockup_Reserved7` | TField |  |  |
| 7 | `FS.MK.RESERVED6` | `FsMockup_Reserved6` | TField |  |  |
| 8 | `FS.MK.RESERVED5` | `FsMockup_Reserved5` | TField |  |  |
| 9 | `FS.MK.RESERVED4` | `FsMockup_Reserved4` | TField |  |  |
| 10 | `FS.MK.RESERVED3` | `FsMockup_Reserved3` | TField |  |  |
| 11 | `FS.MK.RESERVED2` | `FsMockup_Reserved2` | TField |  |  |
| 12 | `FS.MK.RESERVED1` | `FsMockup_Reserved1` | TField |  |  |
| 13 | `FS.MK.LOCAL.REF` | `FsMockup_LocalRef` |  |  |  |
| 14 | `FS.MK.OVERRIDE` | `FsMockup_Override` |  |  |  |
| 15 | `FS.MK.RECORD.STATUS` | `FsMockup_RecordStatus` | String |  |  |
| 16 | `FS.MK.CURR.NO` | `FsMockup_CurrNo` | String |  |  |
| 17 | `FS.MK.INPUTTER` | `FsMockup_Inputter` |  |  |  |
| 18 | `FS.MK.DATE.TIME` | `FsMockup_DateTime` |  |  |  |
| 19 | `FS.MK.AUTHORISER` | `FsMockup_Authoriser` | String |  |  |
| 20 | `FS.MK.CO.CODE` | `FsMockup_CoCode` | String |  |  |
| 21 | `FS.MK.DEPT.CODE` | `FsMockup_DeptCode` | String |  |  |
| 22 | `FS.MK.AUDITOR.CODE` | `FsMockup_AuditorCode` | String |  |  |
| 23 | `FS.MK.AUDIT.DATE.TIME` | `FsMockup_AuditDateTime` | String |  |  |
