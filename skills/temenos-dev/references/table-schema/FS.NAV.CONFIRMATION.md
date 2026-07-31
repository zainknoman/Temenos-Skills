# FS.NAV.CONFIRMATION — Table Schema

> Source: `INSERTS/I_F.FS.NAV.CONFIRMATION` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.NAV.CONFIRMATION.DESCRIPTION` | `FsNavConfirmation_Description` |  |  |  |
| 2 | `FS.NAV.CONFIRMATION.FILTER.KEY` | `FsNavConfirmation_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.NAV.CONFIRMATION.RECORD.ID` | `FsNavConfirmation_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.NAV.CONFIRMATION.RESERVED10` | `FsNavConfirmation_Reserved10` | TField |  |  |
| 5 | `FS.NAV.CONFIRMATION.RESERVED9` | `FsNavConfirmation_Reserved9` | TField |  |  |
| 6 | `FS.NAV.CONFIRMATION.RESERVED8` | `FsNavConfirmation_Reserved8` | TField |  |  |
| 7 | `FS.NAV.CONFIRMATION.RESERVED7` | `FsNavConfirmation_Reserved7` | TField |  |  |
| 8 | `FS.NAV.CONFIRMATION.RESERVED6` | `FsNavConfirmation_Reserved6` | TField |  |  |
| 9 | `FS.NAV.CONFIRMATION.RESERVED5` | `FsNavConfirmation_Reserved5` | TField |  |  |
| 10 | `FS.NAV.CONFIRMATION.RESERVED4` | `FsNavConfirmation_Reserved4` | TField |  |  |
| 11 | `FS.NAV.CONFIRMATION.RESERVED3` | `FsNavConfirmation_Reserved3` | TField |  |  |
| 12 | `FS.NAV.CONFIRMATION.RESERVED2` | `FsNavConfirmation_Reserved2` | TField |  |  |
| 13 | `FS.NAV.CONFIRMATION.RESERVED1` | `FsNavConfirmation_Reserved1` | TField |  |  |
| 14 | `FS.NAV.CONFIRMATION.LOCAL.REF` | `FsNavConfirmation_LocalRef` |  |  |  |
| 15 | `FS.NAV.CONFIRMATION.OVERRIDE` | `FsNavConfirmation_Override` |  |  |  |
| 16 | `FS.NAV.CONFIRMATION.RECORD.STATUS` | `FsNavConfirmation_RecordStatus` | String |  |  |
| 17 | `FS.NAV.CONFIRMATION.CURR.NO` | `FsNavConfirmation_CurrNo` | String |  |  |
| 18 | `FS.NAV.CONFIRMATION.INPUTTER` | `FsNavConfirmation_Inputter` |  |  |  |
| 19 | `FS.NAV.CONFIRMATION.DATE.TIME` | `FsNavConfirmation_DateTime` |  |  |  |
| 20 | `FS.NAV.CONFIRMATION.AUTHORISER` | `FsNavConfirmation_Authoriser` | String |  |  |
| 21 | `FS.NAV.CONFIRMATION.CO.CODE` | `FsNavConfirmation_CoCode` | String |  |  |
| 22 | `FS.NAV.CONFIRMATION.DEPT.CODE` | `FsNavConfirmation_DeptCode` | String |  |  |
| 23 | `FS.NAV.CONFIRMATION.AUDITOR.CODE` | `FsNavConfirmation_AuditorCode` | String |  |  |
| 24 | `FS.NAV.CONFIRMATION.AUDIT.DATE.TIME` | `FsNavConfirmation_AuditDateTime` | String |  |  |
