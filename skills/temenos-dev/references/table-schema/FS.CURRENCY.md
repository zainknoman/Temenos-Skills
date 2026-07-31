# FS.CURRENCY — Table Schema

> Source: `INSERTS/I_F.FS.CURRENCY` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CURRENCY.DESCRIPTION` | `FsCurrency_Description` |  |  |  |
| 2 | `FS.CURRENCY.FILTER.KEY` | `FsCurrency_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CURRENCY.RECORD.ID` | `FsCurrency_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CURRENCY.RESERVED10` | `FsCurrency_Reserved10` | TField |  |  |
| 5 | `FS.CURRENCY.RESERVED9` | `FsCurrency_Reserved9` | TField |  |  |
| 6 | `FS.CURRENCY.RESERVED8` | `FsCurrency_Reserved8` | TField |  |  |
| 7 | `FS.CURRENCY.RESERVED7` | `FsCurrency_Reserved7` | TField |  |  |
| 8 | `FS.CURRENCY.RESERVED6` | `FsCurrency_Reserved6` | TField |  |  |
| 9 | `FS.CURRENCY.RESERVED5` | `FsCurrency_Reserved5` | TField |  |  |
| 10 | `FS.CURRENCY.RESERVED4` | `FsCurrency_Reserved4` | TField |  |  |
| 11 | `FS.CURRENCY.RESERVED3` | `FsCurrency_Reserved3` | TField |  |  |
| 12 | `FS.CURRENCY.RESERVED2` | `FsCurrency_Reserved2` | TField |  |  |
| 13 | `FS.CURRENCY.RESERVED1` | `FsCurrency_Reserved1` | TField |  |  |
| 14 | `FS.CURRENCY.LOCAL.REF` | `FsCurrency_LocalRef` |  |  |  |
| 15 | `FS.CURRENCY.OVERRIDE` | `FsCurrency_Override` |  |  |  |
| 16 | `FS.CURRENCY.RECORD.STATUS` | `FsCurrency_RecordStatus` | String |  |  |
| 17 | `FS.CURRENCY.CURR.NO` | `FsCurrency_CurrNo` | String |  |  |
| 18 | `FS.CURRENCY.INPUTTER` | `FsCurrency_Inputter` |  |  |  |
| 19 | `FS.CURRENCY.DATE.TIME` | `FsCurrency_DateTime` |  |  |  |
| 20 | `FS.CURRENCY.AUTHORISER` | `FsCurrency_Authoriser` | String |  |  |
| 21 | `FS.CURRENCY.CO.CODE` | `FsCurrency_CoCode` | String |  |  |
| 22 | `FS.CURRENCY.DEPT.CODE` | `FsCurrency_DeptCode` | String |  |  |
| 23 | `FS.CURRENCY.AUDITOR.CODE` | `FsCurrency_AuditorCode` | String |  |  |
| 24 | `FS.CURRENCY.AUDIT.DATE.TIME` | `FsCurrency_AuditDateTime` | String |  |  |
