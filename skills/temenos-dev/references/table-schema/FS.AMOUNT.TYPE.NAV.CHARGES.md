# FS.AMOUNT.TYPE.NAV.CHARGES — Table Schema

> Source: `INSERTS/I_F.FS.AMOUNT.TYPE.NAV.CHARGES` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.AMOUNT.TYPE.NAV.CHARGES.DESCRIPTION` | `FsAmountTypeNavCharges_Description` |  |  |  |
| 2 | `FS.AMOUNT.TYPE.NAV.CHARGES.FILTER.KEY` | `FsAmountTypeNavCharges_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.AMOUNT.TYPE.NAV.CHARGES.RECORD.ID` | `FsAmountTypeNavCharges_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED10` | `FsAmountTypeNavCharges_Reserved10` | TField |  |  |
| 5 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED9` | `FsAmountTypeNavCharges_Reserved9` | TField |  |  |
| 6 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED8` | `FsAmountTypeNavCharges_Reserved8` | TField |  |  |
| 7 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED7` | `FsAmountTypeNavCharges_Reserved7` | TField |  |  |
| 8 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED6` | `FsAmountTypeNavCharges_Reserved6` | TField |  |  |
| 9 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED5` | `FsAmountTypeNavCharges_Reserved5` | TField |  |  |
| 10 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED4` | `FsAmountTypeNavCharges_Reserved4` | TField |  |  |
| 11 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED3` | `FsAmountTypeNavCharges_Reserved3` | TField |  |  |
| 12 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED2` | `FsAmountTypeNavCharges_Reserved2` | TField |  |  |
| 13 | `FS.AMOUNT.TYPE.NAV.CHARGES.RESERVED1` | `FsAmountTypeNavCharges_Reserved1` | TField |  |  |
| 14 | `FS.AMOUNT.TYPE.NAV.CHARGES.LOCAL.REF` | `FsAmountTypeNavCharges_LocalRef` |  |  |  |
| 15 | `FS.AMOUNT.TYPE.NAV.CHARGES.OVERRIDE` | `FsAmountTypeNavCharges_Override` |  |  |  |
| 16 | `FS.AMOUNT.TYPE.NAV.CHARGES.RECORD.STATUS` | `FsAmountTypeNavCharges_RecordStatus` | String |  |  |
| 17 | `FS.AMOUNT.TYPE.NAV.CHARGES.CURR.NO` | `FsAmountTypeNavCharges_CurrNo` | String |  |  |
| 18 | `FS.AMOUNT.TYPE.NAV.CHARGES.INPUTTER` | `FsAmountTypeNavCharges_Inputter` |  |  |  |
| 19 | `FS.AMOUNT.TYPE.NAV.CHARGES.DATE.TIME` | `FsAmountTypeNavCharges_DateTime` |  |  |  |
| 20 | `FS.AMOUNT.TYPE.NAV.CHARGES.AUTHORISER` | `FsAmountTypeNavCharges_Authoriser` | String |  |  |
| 21 | `FS.AMOUNT.TYPE.NAV.CHARGES.CO.CODE` | `FsAmountTypeNavCharges_CoCode` | String |  |  |
| 22 | `FS.AMOUNT.TYPE.NAV.CHARGES.DEPT.CODE` | `FsAmountTypeNavCharges_DeptCode` | String |  |  |
| 23 | `FS.AMOUNT.TYPE.NAV.CHARGES.AUDITOR.CODE` | `FsAmountTypeNavCharges_AuditorCode` | String |  |  |
| 24 | `FS.AMOUNT.TYPE.NAV.CHARGES.AUDIT.DATE.TIME` | `FsAmountTypeNavCharges_AuditDateTime` | String |  |  |
