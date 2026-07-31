# FS.UNIQUE.LOT.FUND.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.UNIQUE.LOT.FUND.GROUP` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.UNIQUE.LOT.FUND.GROUP.DESCRIPTION` | `FsUniqueLotFundGroup_Description` |  |  |  |
| 2 | `FS.UNIQUE.LOT.FUND.GROUP.FILTER.KEY` | `FsUniqueLotFundGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.UNIQUE.LOT.FUND.GROUP.RECORD.ID` | `FsUniqueLotFundGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED10` | `FsUniqueLotFundGroup_Reserved10` | TField |  |  |
| 5 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED9` | `FsUniqueLotFundGroup_Reserved9` | TField |  |  |
| 6 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED8` | `FsUniqueLotFundGroup_Reserved8` | TField |  |  |
| 7 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED7` | `FsUniqueLotFundGroup_Reserved7` | TField |  |  |
| 8 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED6` | `FsUniqueLotFundGroup_Reserved6` | TField |  |  |
| 9 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED5` | `FsUniqueLotFundGroup_Reserved5` | TField |  |  |
| 10 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED4` | `FsUniqueLotFundGroup_Reserved4` | TField |  |  |
| 11 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED3` | `FsUniqueLotFundGroup_Reserved3` | TField |  |  |
| 12 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED2` | `FsUniqueLotFundGroup_Reserved2` | TField |  |  |
| 13 | `FS.UNIQUE.LOT.FUND.GROUP.RESERVED1` | `FsUniqueLotFundGroup_Reserved1` | TField |  |  |
| 14 | `FS.UNIQUE.LOT.FUND.GROUP.LOCAL.REF` | `FsUniqueLotFundGroup_LocalRef` |  |  |  |
| 15 | `FS.UNIQUE.LOT.FUND.GROUP.OVERRIDE` | `FsUniqueLotFundGroup_Override` |  |  |  |
| 16 | `FS.UNIQUE.LOT.FUND.GROUP.RECORD.STATUS` | `FsUniqueLotFundGroup_RecordStatus` | String |  |  |
| 17 | `FS.UNIQUE.LOT.FUND.GROUP.CURR.NO` | `FsUniqueLotFundGroup_CurrNo` | String |  |  |
| 18 | `FS.UNIQUE.LOT.FUND.GROUP.INPUTTER` | `FsUniqueLotFundGroup_Inputter` |  |  |  |
| 19 | `FS.UNIQUE.LOT.FUND.GROUP.DATE.TIME` | `FsUniqueLotFundGroup_DateTime` |  |  |  |
| 20 | `FS.UNIQUE.LOT.FUND.GROUP.AUTHORISER` | `FsUniqueLotFundGroup_Authoriser` | String |  |  |
| 21 | `FS.UNIQUE.LOT.FUND.GROUP.CO.CODE` | `FsUniqueLotFundGroup_CoCode` | String |  |  |
| 22 | `FS.UNIQUE.LOT.FUND.GROUP.DEPT.CODE` | `FsUniqueLotFundGroup_DeptCode` | String |  |  |
| 23 | `FS.UNIQUE.LOT.FUND.GROUP.AUDITOR.CODE` | `FsUniqueLotFundGroup_AuditorCode` | String |  |  |
| 24 | `FS.UNIQUE.LOT.FUND.GROUP.AUDIT.DATE.TIME` | `FsUniqueLotFundGroup_AuditDateTime` | String |  |  |
