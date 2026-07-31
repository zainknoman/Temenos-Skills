# FS.METHOD.CODE.NAV.CHARGES — Table Schema

> Source: `INSERTS/I_F.FS.METHOD.CODE.NAV.CHARGES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.METHOD.CODE.NAV.CHARGES.DESCRIPTION` | `FsMethodCodeNavCharges_Description` |  |  |  |
| 2 | `FS.METHOD.CODE.NAV.CHARGES.FILTER.KEY` | `FsMethodCodeNavCharges_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.METHOD.CODE.NAV.CHARGES.RECORD.ID` | `FsMethodCodeNavCharges_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED10` | `FsMethodCodeNavCharges_Reserved10` | TField |  |  |
| 5 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED9` | `FsMethodCodeNavCharges_Reserved9` | TField |  |  |
| 6 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED8` | `FsMethodCodeNavCharges_Reserved8` | TField |  |  |
| 7 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED7` | `FsMethodCodeNavCharges_Reserved7` | TField |  |  |
| 8 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED6` | `FsMethodCodeNavCharges_Reserved6` | TField |  |  |
| 9 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED5` | `FsMethodCodeNavCharges_Reserved5` | TField |  |  |
| 10 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED4` | `FsMethodCodeNavCharges_Reserved4` | TField |  |  |
| 11 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED3` | `FsMethodCodeNavCharges_Reserved3` | TField |  |  |
| 12 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED2` | `FsMethodCodeNavCharges_Reserved2` | TField |  |  |
| 13 | `FS.METHOD.CODE.NAV.CHARGES.RESERVED1` | `FsMethodCodeNavCharges_Reserved1` | TField |  |  |
| 14 | `FS.METHOD.CODE.NAV.CHARGES.LOCAL.REF` | `FsMethodCodeNavCharges_LocalRef` |  |  |  |
| 15 | `FS.METHOD.CODE.NAV.CHARGES.OVERRIDE` | `FsMethodCodeNavCharges_Override` |  |  |  |
| 16 | `FS.METHOD.CODE.NAV.CHARGES.RECORD.STATUS` | `FsMethodCodeNavCharges_RecordStatus` | String |  |  |
| 17 | `FS.METHOD.CODE.NAV.CHARGES.CURR.NO` | `FsMethodCodeNavCharges_CurrNo` | String |  |  |
| 18 | `FS.METHOD.CODE.NAV.CHARGES.INPUTTER` | `FsMethodCodeNavCharges_Inputter` |  |  |  |
| 19 | `FS.METHOD.CODE.NAV.CHARGES.DATE.TIME` | `FsMethodCodeNavCharges_DateTime` |  |  |  |
| 20 | `FS.METHOD.CODE.NAV.CHARGES.AUTHORISER` | `FsMethodCodeNavCharges_Authoriser` | String |  |  |
| 21 | `FS.METHOD.CODE.NAV.CHARGES.CO.CODE` | `FsMethodCodeNavCharges_CoCode` | String |  |  |
| 22 | `FS.METHOD.CODE.NAV.CHARGES.DEPT.CODE` | `FsMethodCodeNavCharges_DeptCode` | String |  |  |
| 23 | `FS.METHOD.CODE.NAV.CHARGES.AUDITOR.CODE` | `FsMethodCodeNavCharges_AuditorCode` | String |  |  |
| 24 | `FS.METHOD.CODE.NAV.CHARGES.AUDIT.DATE.TIME` | `FsMethodCodeNavCharges_AuditDateTime` | String |  |  |
