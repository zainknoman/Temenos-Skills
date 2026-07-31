# FS.AMOUNT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.AMOUNT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.AMOUNT.TYPE.DESCRIPTION` | `FsAmountType_Description` |  |  |  |
| 2 | `FS.AMOUNT.TYPE.FILTER.KEY` | `FsAmountType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.AMOUNT.TYPE.RECORD.ID` | `FsAmountType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.AMOUNT.TYPE.RESERVED10` | `FsAmountType_Reserved10` | TField |  |  |
| 5 | `FS.AMOUNT.TYPE.RESERVED9` | `FsAmountType_Reserved9` | TField |  |  |
| 6 | `FS.AMOUNT.TYPE.RESERVED8` | `FsAmountType_Reserved8` | TField |  |  |
| 7 | `FS.AMOUNT.TYPE.RESERVED7` | `FsAmountType_Reserved7` | TField |  |  |
| 8 | `FS.AMOUNT.TYPE.RESERVED6` | `FsAmountType_Reserved6` | TField |  |  |
| 9 | `FS.AMOUNT.TYPE.RESERVED5` | `FsAmountType_Reserved5` | TField |  |  |
| 10 | `FS.AMOUNT.TYPE.RESERVED4` | `FsAmountType_Reserved4` | TField |  |  |
| 11 | `FS.AMOUNT.TYPE.RESERVED3` | `FsAmountType_Reserved3` | TField |  |  |
| 12 | `FS.AMOUNT.TYPE.RESERVED2` | `FsAmountType_Reserved2` | TField |  |  |
| 13 | `FS.AMOUNT.TYPE.RESERVED1` | `FsAmountType_Reserved1` | TField |  |  |
| 14 | `FS.AMOUNT.TYPE.LOCAL.REF` | `FsAmountType_LocalRef` |  |  |  |
| 15 | `FS.AMOUNT.TYPE.OVERRIDE` | `FsAmountType_Override` |  |  |  |
| 16 | `FS.AMOUNT.TYPE.RECORD.STATUS` | `FsAmountType_RecordStatus` | String |  |  |
| 17 | `FS.AMOUNT.TYPE.CURR.NO` | `FsAmountType_CurrNo` | String |  |  |
| 18 | `FS.AMOUNT.TYPE.INPUTTER` | `FsAmountType_Inputter` |  |  |  |
| 19 | `FS.AMOUNT.TYPE.DATE.TIME` | `FsAmountType_DateTime` |  |  |  |
| 20 | `FS.AMOUNT.TYPE.AUTHORISER` | `FsAmountType_Authoriser` | String |  |  |
| 21 | `FS.AMOUNT.TYPE.CO.CODE` | `FsAmountType_CoCode` | String |  |  |
| 22 | `FS.AMOUNT.TYPE.DEPT.CODE` | `FsAmountType_DeptCode` | String |  |  |
| 23 | `FS.AMOUNT.TYPE.AUDITOR.CODE` | `FsAmountType_AuditorCode` | String |  |  |
| 24 | `FS.AMOUNT.TYPE.AUDIT.DATE.TIME` | `FsAmountType_AuditDateTime` | String |  |  |
