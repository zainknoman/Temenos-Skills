# FS.VAT.CODE — Table Schema

> Source: `INSERTS/I_F.FS.VAT.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.VAT.CODE.DESCRIPTION` | `FsVatCode_Description` |  |  |  |
| 2 | `FS.VAT.CODE.FILTER.KEY` | `FsVatCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.VAT.CODE.RECORD.ID` | `FsVatCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.VAT.CODE.RESERVED10` | `FsVatCode_Reserved10` | TField |  |  |
| 5 | `FS.VAT.CODE.RESERVED9` | `FsVatCode_Reserved9` | TField |  |  |
| 6 | `FS.VAT.CODE.RESERVED8` | `FsVatCode_Reserved8` | TField |  |  |
| 7 | `FS.VAT.CODE.RESERVED7` | `FsVatCode_Reserved7` | TField |  |  |
| 8 | `FS.VAT.CODE.RESERVED6` | `FsVatCode_Reserved6` | TField |  |  |
| 9 | `FS.VAT.CODE.RESERVED5` | `FsVatCode_Reserved5` | TField |  |  |
| 10 | `FS.VAT.CODE.RESERVED4` | `FsVatCode_Reserved4` | TField |  |  |
| 11 | `FS.VAT.CODE.RESERVED3` | `FsVatCode_Reserved3` | TField |  |  |
| 12 | `FS.VAT.CODE.RESERVED2` | `FsVatCode_Reserved2` | TField |  |  |
| 13 | `FS.VAT.CODE.RESERVED1` | `FsVatCode_Reserved1` | TField |  |  |
| 14 | `FS.VAT.CODE.LOCAL.REF` | `FsVatCode_LocalRef` |  |  |  |
| 15 | `FS.VAT.CODE.OVERRIDE` | `FsVatCode_Override` |  |  |  |
| 16 | `FS.VAT.CODE.RECORD.STATUS` | `FsVatCode_RecordStatus` | String |  |  |
| 17 | `FS.VAT.CODE.CURR.NO` | `FsVatCode_CurrNo` | String |  |  |
| 18 | `FS.VAT.CODE.INPUTTER` | `FsVatCode_Inputter` |  |  |  |
| 19 | `FS.VAT.CODE.DATE.TIME` | `FsVatCode_DateTime` |  |  |  |
| 20 | `FS.VAT.CODE.AUTHORISER` | `FsVatCode_Authoriser` | String |  |  |
| 21 | `FS.VAT.CODE.CO.CODE` | `FsVatCode_CoCode` | String |  |  |
| 22 | `FS.VAT.CODE.DEPT.CODE` | `FsVatCode_DeptCode` | String |  |  |
| 23 | `FS.VAT.CODE.AUDITOR.CODE` | `FsVatCode_AuditorCode` | String |  |  |
| 24 | `FS.VAT.CODE.AUDIT.DATE.TIME` | `FsVatCode_AuditDateTime` | String |  |  |
