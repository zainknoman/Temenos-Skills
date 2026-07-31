# FS.CURRENCY.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.CURRENCY.GROUP` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CURRENCY.GROUP.DESCRIPTION` | `FsCurrencyGroup_Description` |  |  |  |
| 2 | `FS.CURRENCY.GROUP.FILTER.KEY` | `FsCurrencyGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CURRENCY.GROUP.RECORD.ID` | `FsCurrencyGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CURRENCY.GROUP.RESERVED10` | `FsCurrencyGroup_Reserved10` | TField |  |  |
| 5 | `FS.CURRENCY.GROUP.RESERVED9` | `FsCurrencyGroup_Reserved9` | TField |  |  |
| 6 | `FS.CURRENCY.GROUP.RESERVED8` | `FsCurrencyGroup_Reserved8` | TField |  |  |
| 7 | `FS.CURRENCY.GROUP.RESERVED7` | `FsCurrencyGroup_Reserved7` | TField |  |  |
| 8 | `FS.CURRENCY.GROUP.RESERVED6` | `FsCurrencyGroup_Reserved6` | TField |  |  |
| 9 | `FS.CURRENCY.GROUP.RESERVED5` | `FsCurrencyGroup_Reserved5` | TField |  |  |
| 10 | `FS.CURRENCY.GROUP.RESERVED4` | `FsCurrencyGroup_Reserved4` | TField |  |  |
| 11 | `FS.CURRENCY.GROUP.RESERVED3` | `FsCurrencyGroup_Reserved3` | TField |  |  |
| 12 | `FS.CURRENCY.GROUP.RESERVED2` | `FsCurrencyGroup_Reserved2` | TField |  |  |
| 13 | `FS.CURRENCY.GROUP.RESERVED1` | `FsCurrencyGroup_Reserved1` | TField |  |  |
| 14 | `FS.CURRENCY.GROUP.LOCAL.REF` | `FsCurrencyGroup_LocalRef` |  |  |  |
| 15 | `FS.CURRENCY.GROUP.OVERRIDE` | `FsCurrencyGroup_Override` |  |  |  |
| 16 | `FS.CURRENCY.GROUP.RECORD.STATUS` | `FsCurrencyGroup_RecordStatus` | String |  |  |
| 17 | `FS.CURRENCY.GROUP.CURR.NO` | `FsCurrencyGroup_CurrNo` | String |  |  |
| 18 | `FS.CURRENCY.GROUP.INPUTTER` | `FsCurrencyGroup_Inputter` |  |  |  |
| 19 | `FS.CURRENCY.GROUP.DATE.TIME` | `FsCurrencyGroup_DateTime` |  |  |  |
| 20 | `FS.CURRENCY.GROUP.AUTHORISER` | `FsCurrencyGroup_Authoriser` | String |  |  |
| 21 | `FS.CURRENCY.GROUP.CO.CODE` | `FsCurrencyGroup_CoCode` | String |  |  |
| 22 | `FS.CURRENCY.GROUP.DEPT.CODE` | `FsCurrencyGroup_DeptCode` | String |  |  |
| 23 | `FS.CURRENCY.GROUP.AUDITOR.CODE` | `FsCurrencyGroup_AuditorCode` | String |  |  |
| 24 | `FS.CURRENCY.GROUP.AUDIT.DATE.TIME` | `FsCurrencyGroup_AuditDateTime` | String |  |  |
