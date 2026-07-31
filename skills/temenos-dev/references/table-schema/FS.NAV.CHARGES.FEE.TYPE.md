# FS.NAV.CHARGES.FEE.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.NAV.CHARGES.FEE.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.NAV.CHARGES.FEE.TYPE.DESCRIPTION` | `FsNavChargesFeeType_Description` |  |  |  |
| 2 | `FS.NAV.CHARGES.FEE.TYPE.FILTER.KEY` | `FsNavChargesFeeType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.NAV.CHARGES.FEE.TYPE.RECORD.ID` | `FsNavChargesFeeType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED10` | `FsNavChargesFeeType_Reserved10` | TField |  |  |
| 5 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED9` | `FsNavChargesFeeType_Reserved9` | TField |  |  |
| 6 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED8` | `FsNavChargesFeeType_Reserved8` | TField |  |  |
| 7 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED7` | `FsNavChargesFeeType_Reserved7` | TField |  |  |
| 8 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED6` | `FsNavChargesFeeType_Reserved6` | TField |  |  |
| 9 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED5` | `FsNavChargesFeeType_Reserved5` | TField |  |  |
| 10 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED4` | `FsNavChargesFeeType_Reserved4` | TField |  |  |
| 11 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED3` | `FsNavChargesFeeType_Reserved3` | TField |  |  |
| 12 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED2` | `FsNavChargesFeeType_Reserved2` | TField |  |  |
| 13 | `FS.NAV.CHARGES.FEE.TYPE.RESERVED1` | `FsNavChargesFeeType_Reserved1` | TField |  |  |
| 14 | `FS.NAV.CHARGES.FEE.TYPE.LOCAL.REF` | `FsNavChargesFeeType_LocalRef` |  |  |  |
| 15 | `FS.NAV.CHARGES.FEE.TYPE.OVERRIDE` | `FsNavChargesFeeType_Override` |  |  |  |
| 16 | `FS.NAV.CHARGES.FEE.TYPE.RECORD.STATUS` | `FsNavChargesFeeType_RecordStatus` | String |  |  |
| 17 | `FS.NAV.CHARGES.FEE.TYPE.CURR.NO` | `FsNavChargesFeeType_CurrNo` | String |  |  |
| 18 | `FS.NAV.CHARGES.FEE.TYPE.INPUTTER` | `FsNavChargesFeeType_Inputter` |  |  |  |
| 19 | `FS.NAV.CHARGES.FEE.TYPE.DATE.TIME` | `FsNavChargesFeeType_DateTime` |  |  |  |
| 20 | `FS.NAV.CHARGES.FEE.TYPE.AUTHORISER` | `FsNavChargesFeeType_Authoriser` | String |  |  |
| 21 | `FS.NAV.CHARGES.FEE.TYPE.CO.CODE` | `FsNavChargesFeeType_CoCode` | String |  |  |
| 22 | `FS.NAV.CHARGES.FEE.TYPE.DEPT.CODE` | `FsNavChargesFeeType_DeptCode` | String |  |  |
| 23 | `FS.NAV.CHARGES.FEE.TYPE.AUDITOR.CODE` | `FsNavChargesFeeType_AuditorCode` | String |  |  |
| 24 | `FS.NAV.CHARGES.FEE.TYPE.AUDIT.DATE.TIME` | `FsNavChargesFeeType_AuditDateTime` | String |  |  |
