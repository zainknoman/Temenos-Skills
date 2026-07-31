# FS.TAX.REGIME — Table Schema

> Source: `INSERTS/I_F.FS.TAX.REGIME` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TAX.REGIME.DESCRIPTION` | `FsTaxRegime_Description` |  |  |  |
| 2 | `FS.TAX.REGIME.FILTER.KEY` | `FsTaxRegime_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TAX.REGIME.RECORD.ID` | `FsTaxRegime_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TAX.REGIME.RESERVED10` | `FsTaxRegime_Reserved10` | TField |  |  |
| 5 | `FS.TAX.REGIME.RESERVED9` | `FsTaxRegime_Reserved9` | TField |  |  |
| 6 | `FS.TAX.REGIME.RESERVED8` | `FsTaxRegime_Reserved8` | TField |  |  |
| 7 | `FS.TAX.REGIME.RESERVED7` | `FsTaxRegime_Reserved7` | TField |  |  |
| 8 | `FS.TAX.REGIME.RESERVED6` | `FsTaxRegime_Reserved6` | TField |  |  |
| 9 | `FS.TAX.REGIME.RESERVED5` | `FsTaxRegime_Reserved5` | TField |  |  |
| 10 | `FS.TAX.REGIME.RESERVED4` | `FsTaxRegime_Reserved4` | TField |  |  |
| 11 | `FS.TAX.REGIME.RESERVED3` | `FsTaxRegime_Reserved3` | TField |  |  |
| 12 | `FS.TAX.REGIME.RESERVED2` | `FsTaxRegime_Reserved2` | TField |  |  |
| 13 | `FS.TAX.REGIME.RESERVED1` | `FsTaxRegime_Reserved1` | TField |  |  |
| 14 | `FS.TAX.REGIME.LOCAL.REF` | `FsTaxRegime_LocalRef` |  |  |  |
| 15 | `FS.TAX.REGIME.OVERRIDE` | `FsTaxRegime_Override` |  |  |  |
| 16 | `FS.TAX.REGIME.RECORD.STATUS` | `FsTaxRegime_RecordStatus` | String |  |  |
| 17 | `FS.TAX.REGIME.CURR.NO` | `FsTaxRegime_CurrNo` | String |  |  |
| 18 | `FS.TAX.REGIME.INPUTTER` | `FsTaxRegime_Inputter` |  |  |  |
| 19 | `FS.TAX.REGIME.DATE.TIME` | `FsTaxRegime_DateTime` |  |  |  |
| 20 | `FS.TAX.REGIME.AUTHORISER` | `FsTaxRegime_Authoriser` | String |  |  |
| 21 | `FS.TAX.REGIME.CO.CODE` | `FsTaxRegime_CoCode` | String |  |  |
| 22 | `FS.TAX.REGIME.DEPT.CODE` | `FsTaxRegime_DeptCode` | String |  |  |
| 23 | `FS.TAX.REGIME.AUDITOR.CODE` | `FsTaxRegime_AuditorCode` | String |  |  |
| 24 | `FS.TAX.REGIME.AUDIT.DATE.TIME` | `FsTaxRegime_AuditDateTime` | String |  |  |
