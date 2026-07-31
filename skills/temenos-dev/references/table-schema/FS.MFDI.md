# FS.MFDI — Table Schema

> Source: `INSERTS/I_F.FS.MFDI` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.MFDI.DESCRIPTION` | `FsMfdi_Description` |  |  |  |
| 2 | `FS.MFDI.FILTER.KEY` | `FsMfdi_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.MFDI.RECORD.ID` | `FsMfdi_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.MFDI.RESERVED10` | `FsMfdi_Reserved10` | TField |  |  |
| 5 | `FS.MFDI.RESERVED9` | `FsMfdi_Reserved9` | TField |  |  |
| 6 | `FS.MFDI.RESERVED8` | `FsMfdi_Reserved8` | TField |  |  |
| 7 | `FS.MFDI.RESERVED7` | `FsMfdi_Reserved7` | TField |  |  |
| 8 | `FS.MFDI.RESERVED6` | `FsMfdi_Reserved6` | TField |  |  |
| 9 | `FS.MFDI.RESERVED5` | `FsMfdi_Reserved5` | TField |  |  |
| 10 | `FS.MFDI.RESERVED4` | `FsMfdi_Reserved4` | TField |  |  |
| 11 | `FS.MFDI.RESERVED3` | `FsMfdi_Reserved3` | TField |  |  |
| 12 | `FS.MFDI.RESERVED2` | `FsMfdi_Reserved2` | TField |  |  |
| 13 | `FS.MFDI.RESERVED1` | `FsMfdi_Reserved1` | TField |  |  |
| 14 | `FS.MFDI.LOCAL.REF` | `FsMfdi_LocalRef` |  |  |  |
| 15 | `FS.MFDI.OVERRIDE` | `FsMfdi_Override` |  |  |  |
| 16 | `FS.MFDI.RECORD.STATUS` | `FsMfdi_RecordStatus` | String |  |  |
| 17 | `FS.MFDI.CURR.NO` | `FsMfdi_CurrNo` | String |  |  |
| 18 | `FS.MFDI.INPUTTER` | `FsMfdi_Inputter` |  |  |  |
| 19 | `FS.MFDI.DATE.TIME` | `FsMfdi_DateTime` |  |  |  |
| 20 | `FS.MFDI.AUTHORISER` | `FsMfdi_Authoriser` | String |  |  |
| 21 | `FS.MFDI.CO.CODE` | `FsMfdi_CoCode` | String |  |  |
| 22 | `FS.MFDI.DEPT.CODE` | `FsMfdi_DeptCode` | String |  |  |
| 23 | `FS.MFDI.AUDITOR.CODE` | `FsMfdi_AuditorCode` | String |  |  |
| 24 | `FS.MFDI.AUDIT.DATE.TIME` | `FsMfdi_AuditDateTime` | String |  |  |
