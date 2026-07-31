# FS.TAX.CODE — Table Schema

> Source: `INSERTS/I_F.FS.TAX.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TAX.CODE.DESCRIPTION` | `FsTaxCode_Description` |  |  |  |
| 2 | `FS.TAX.CODE.FILTER.KEY` | `FsTaxCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TAX.CODE.RECORD.ID` | `FsTaxCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TAX.CODE.RESERVED10` | `FsTaxCode_Reserved10` | TField |  |  |
| 5 | `FS.TAX.CODE.RESERVED9` | `FsTaxCode_Reserved9` | TField |  |  |
| 6 | `FS.TAX.CODE.RESERVED8` | `FsTaxCode_Reserved8` | TField |  |  |
| 7 | `FS.TAX.CODE.RESERVED7` | `FsTaxCode_Reserved7` | TField |  |  |
| 8 | `FS.TAX.CODE.RESERVED6` | `FsTaxCode_Reserved6` | TField |  |  |
| 9 | `FS.TAX.CODE.RESERVED5` | `FsTaxCode_Reserved5` | TField |  |  |
| 10 | `FS.TAX.CODE.RESERVED4` | `FsTaxCode_Reserved4` | TField |  |  |
| 11 | `FS.TAX.CODE.RESERVED3` | `FsTaxCode_Reserved3` | TField |  |  |
| 12 | `FS.TAX.CODE.RESERVED2` | `FsTaxCode_Reserved2` | TField |  |  |
| 13 | `FS.TAX.CODE.RESERVED1` | `FsTaxCode_Reserved1` | TField |  |  |
| 14 | `FS.TAX.CODE.LOCAL.REF` | `FsTaxCode_LocalRef` |  |  |  |
| 15 | `FS.TAX.CODE.OVERRIDE` | `FsTaxCode_Override` |  |  |  |
| 16 | `FS.TAX.CODE.RECORD.STATUS` | `FsTaxCode_RecordStatus` | String |  |  |
| 17 | `FS.TAX.CODE.CURR.NO` | `FsTaxCode_CurrNo` | String |  |  |
| 18 | `FS.TAX.CODE.INPUTTER` | `FsTaxCode_Inputter` |  |  |  |
| 19 | `FS.TAX.CODE.DATE.TIME` | `FsTaxCode_DateTime` |  |  |  |
| 20 | `FS.TAX.CODE.AUTHORISER` | `FsTaxCode_Authoriser` | String |  |  |
| 21 | `FS.TAX.CODE.CO.CODE` | `FsTaxCode_CoCode` | String |  |  |
| 22 | `FS.TAX.CODE.DEPT.CODE` | `FsTaxCode_DeptCode` | String |  |  |
| 23 | `FS.TAX.CODE.AUDITOR.CODE` | `FsTaxCode_AuditorCode` | String |  |  |
| 24 | `FS.TAX.CODE.AUDIT.DATE.TIME` | `FsTaxCode_AuditDateTime` | String |  |  |
