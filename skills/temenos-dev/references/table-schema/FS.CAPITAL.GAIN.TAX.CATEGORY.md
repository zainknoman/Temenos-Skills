# FS.CAPITAL.GAIN.TAX.CATEGORY — Table Schema

> Source: `INSERTS/I_F.FS.CAPITAL.GAIN.TAX.CATEGORY` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CAPITAL.GAIN.TAX.CATEGORY.DESCRIPTION` | `FsCapitalGainTaxCategory_Description` |  |  |  |
| 2 | `FS.CAPITAL.GAIN.TAX.CATEGORY.FILTER.KEY` | `FsCapitalGainTaxCategory_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RECORD.ID` | `FsCapitalGainTaxCategory_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED10` | `FsCapitalGainTaxCategory_Reserved10` | TField |  |  |
| 5 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED9` | `FsCapitalGainTaxCategory_Reserved9` | TField |  |  |
| 6 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED8` | `FsCapitalGainTaxCategory_Reserved8` | TField |  |  |
| 7 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED7` | `FsCapitalGainTaxCategory_Reserved7` | TField |  |  |
| 8 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED6` | `FsCapitalGainTaxCategory_Reserved6` | TField |  |  |
| 9 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED5` | `FsCapitalGainTaxCategory_Reserved5` | TField |  |  |
| 10 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED4` | `FsCapitalGainTaxCategory_Reserved4` | TField |  |  |
| 11 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED3` | `FsCapitalGainTaxCategory_Reserved3` | TField |  |  |
| 12 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED2` | `FsCapitalGainTaxCategory_Reserved2` | TField |  |  |
| 13 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RESERVED1` | `FsCapitalGainTaxCategory_Reserved1` | TField |  |  |
| 14 | `FS.CAPITAL.GAIN.TAX.CATEGORY.LOCAL.REF` | `FsCapitalGainTaxCategory_LocalRef` |  |  |  |
| 15 | `FS.CAPITAL.GAIN.TAX.CATEGORY.OVERRIDE` | `FsCapitalGainTaxCategory_Override` |  |  |  |
| 16 | `FS.CAPITAL.GAIN.TAX.CATEGORY.RECORD.STATUS` | `FsCapitalGainTaxCategory_RecordStatus` | String |  |  |
| 17 | `FS.CAPITAL.GAIN.TAX.CATEGORY.CURR.NO` | `FsCapitalGainTaxCategory_CurrNo` | String |  |  |
| 18 | `FS.CAPITAL.GAIN.TAX.CATEGORY.INPUTTER` | `FsCapitalGainTaxCategory_Inputter` |  |  |  |
| 19 | `FS.CAPITAL.GAIN.TAX.CATEGORY.DATE.TIME` | `FsCapitalGainTaxCategory_DateTime` |  |  |  |
| 20 | `FS.CAPITAL.GAIN.TAX.CATEGORY.AUTHORISER` | `FsCapitalGainTaxCategory_Authoriser` | String |  |  |
| 21 | `FS.CAPITAL.GAIN.TAX.CATEGORY.CO.CODE` | `FsCapitalGainTaxCategory_CoCode` | String |  |  |
| 22 | `FS.CAPITAL.GAIN.TAX.CATEGORY.DEPT.CODE` | `FsCapitalGainTaxCategory_DeptCode` | String |  |  |
| 23 | `FS.CAPITAL.GAIN.TAX.CATEGORY.AUDITOR.CODE` | `FsCapitalGainTaxCategory_AuditorCode` | String |  |  |
| 24 | `FS.CAPITAL.GAIN.TAX.CATEGORY.AUDIT.DATE.TIME` | `FsCapitalGainTaxCategory_AuditDateTime` | String |  |  |
