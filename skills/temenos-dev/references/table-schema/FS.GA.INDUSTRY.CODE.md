# FS.GA.INDUSTRY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.INDUSTRY.CODE` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INDUSTRY.CODE.PARENT.REF.ID` | `FsGaIndustryCode_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.INDUSTRY.CODE.ORA.ROWID` | `FsGaIndustryCode_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.INDUSTRY.CODE.ID.CODE` | `FsGaIndustryCode_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 4 | `FS.GA.INDUSTRY.CODE.SECTOR` | `FsGaIndustryCode_Sector` | TField |  | Industry sector linked to a correspondent Multifonds DB Column is SCO. |
| 5 | `FS.GA.INDUSTRY.CODE.INDUSTRY.CODES` | `FsGaIndustryCode_IndustryCodes` | TField |  | Industry Codes Multifonds DB Column is IND_CODE. |
| 6 | `FS.GA.INDUSTRY.CODE.DESCRIPTION` | `FsGaIndustryCode_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.INDUSTRY.CODE.LANGUAGE` | `FsGaIndustryCode_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 8 | `FS.GA.INDUSTRY.CODE.INDUSTRY.CLASS.YIELD` | `FsGaIndustryCode_IndustryClassYield` | TField |  | Industry Class Yield. Multifonds DB Column is IND_CLASS_YLD. |
| 9 | `FS.GA.INDUSTRY.CODE.EXCLUDE.INDUSTRY` | `FsGaIndustryCode_ExcludeIndustry` | TField |  | Exclude Industry Identifier Multifonds DB Column is FLG_EXCLUDE_INDUSTRY. |
| 10 | `FS.GA.INDUSTRY.CODE.RESERVED10` | `FsGaIndustryCode_Reserved10` | TField |  |  |
| 11 | `FS.GA.INDUSTRY.CODE.RESERVED9` | `FsGaIndustryCode_Reserved9` | TField |  |  |
| 12 | `FS.GA.INDUSTRY.CODE.RESERVED8` | `FsGaIndustryCode_Reserved8` | TField |  |  |
| 13 | `FS.GA.INDUSTRY.CODE.RESERVED7` | `FsGaIndustryCode_Reserved7` | TField |  |  |
| 14 | `FS.GA.INDUSTRY.CODE.RESERVED6` | `FsGaIndustryCode_Reserved6` | TField |  |  |
| 15 | `FS.GA.INDUSTRY.CODE.RESERVED5` | `FsGaIndustryCode_Reserved5` | TField |  |  |
| 16 | `FS.GA.INDUSTRY.CODE.RESERVED4` | `FsGaIndustryCode_Reserved4` | TField |  |  |
| 17 | `FS.GA.INDUSTRY.CODE.RESERVED3` | `FsGaIndustryCode_Reserved3` | TField |  |  |
| 18 | `FS.GA.INDUSTRY.CODE.RESERVED2` | `FsGaIndustryCode_Reserved2` | TField |  |  |
| 19 | `FS.GA.INDUSTRY.CODE.RESERVED1` | `FsGaIndustryCode_Reserved1` | TField |  |  |
| 20 | `FS.GA.INDUSTRY.CODE.LOCAL.REF` | `FsGaIndustryCode_LocalRef` |  |  |  |
| 21 | `FS.GA.INDUSTRY.CODE.OVERRIDE` | `FsGaIndustryCode_Override` |  |  |  |
| 22 | `FS.GA.INDUSTRY.CODE.RECORD.STATUS` | `FsGaIndustryCode_RecordStatus` | String |  |  |
| 23 | `FS.GA.INDUSTRY.CODE.CURR.NO` | `FsGaIndustryCode_CurrNo` | String |  |  |
| 24 | `FS.GA.INDUSTRY.CODE.INPUTTER` | `FsGaIndustryCode_Inputter` |  |  |  |
| 25 | `FS.GA.INDUSTRY.CODE.DATE.TIME` | `FsGaIndustryCode_DateTime` |  |  |  |
| 26 | `FS.GA.INDUSTRY.CODE.AUTHORISER` | `FsGaIndustryCode_Authoriser` | String |  |  |
| 27 | `FS.GA.INDUSTRY.CODE.CO.CODE` | `FsGaIndustryCode_CoCode` | String |  |  |
| 28 | `FS.GA.INDUSTRY.CODE.DEPT.CODE` | `FsGaIndustryCode_DeptCode` | String |  |  |
| 29 | `FS.GA.INDUSTRY.CODE.AUDITOR.CODE` | `FsGaIndustryCode_AuditorCode` | String |  |  |
| 30 | `FS.GA.INDUSTRY.CODE.AUDIT.DATE.TIME` | `FsGaIndustryCode_AuditDateTime` | String |  |  |
