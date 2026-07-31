# FS.GI.FUND.PERMISSION.COUNTRY — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.PERMISSION.COUNTRY` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.PERMISSION.COUNTRY.PARENT.REF.ID` | `FsGiFundPermissionCountry_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.PERMISSION.COUNTRY.ORA.ROWID` | `FsGiFundPermissionCountry_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.PERMISSION.COUNTRY.TA.FUND.ID` | `FsGiFundPermissionCountry_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.PERMISSION.COUNTRY.COUNTRY` | `FsGiFundPermissionCountry_Country` | TField |  | Country code (in 2 letter format eg: LU) in which the fund has been authorized to deal. Multifonds DB Column is CPAYS. |
| 5 | `FS.GI.FUND.PERMISSION.COUNTRY.INTERNAL.ID` | `FsGiFundPermissionCountry_InternalId` | TField |  | Unique internal identifier for fund permission country record. Multifonds DB Column is INTERNAL_ID. |
| 6 | `FS.GI.FUND.PERMISSION.COUNTRY.FUND.ID` | `FsGiFundPermissionCountry_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 7 | `FS.GI.FUND.PERMISSION.COUNTRY.CLASS.CURRENCY` | `FsGiFundPermissionCountry_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 8 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED10` | `FsGiFundPermissionCountry_Reserved10` | TField |  |  |
| 9 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED9` | `FsGiFundPermissionCountry_Reserved9` | TField |  |  |
| 10 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED8` | `FsGiFundPermissionCountry_Reserved8` | TField |  |  |
| 11 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED7` | `FsGiFundPermissionCountry_Reserved7` | TField |  |  |
| 12 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED6` | `FsGiFundPermissionCountry_Reserved6` | TField |  |  |
| 13 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED5` | `FsGiFundPermissionCountry_Reserved5` | TField |  |  |
| 14 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED4` | `FsGiFundPermissionCountry_Reserved4` | TField |  |  |
| 15 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED3` | `FsGiFundPermissionCountry_Reserved3` | TField |  |  |
| 16 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED2` | `FsGiFundPermissionCountry_Reserved2` | TField |  |  |
| 17 | `FS.GI.FUND.PERMISSION.COUNTRY.RESERVED1` | `FsGiFundPermissionCountry_Reserved1` | TField |  |  |
| 18 | `FS.GI.FUND.PERMISSION.COUNTRY.LOCAL.REF` | `FsGiFundPermissionCountry_LocalRef` |  |  |  |
| 19 | `FS.GI.FUND.PERMISSION.COUNTRY.OVERRIDE` | `FsGiFundPermissionCountry_Override` |  |  |  |
| 20 | `FS.GI.FUND.PERMISSION.COUNTRY.RECORD.STATUS` | `FsGiFundPermissionCountry_RecordStatus` | String |  |  |
| 21 | `FS.GI.FUND.PERMISSION.COUNTRY.CURR.NO` | `FsGiFundPermissionCountry_CurrNo` | String |  |  |
| 22 | `FS.GI.FUND.PERMISSION.COUNTRY.INPUTTER` | `FsGiFundPermissionCountry_Inputter` |  |  |  |
| 23 | `FS.GI.FUND.PERMISSION.COUNTRY.DATE.TIME` | `FsGiFundPermissionCountry_DateTime` |  |  |  |
| 24 | `FS.GI.FUND.PERMISSION.COUNTRY.AUTHORISER` | `FsGiFundPermissionCountry_Authoriser` | String |  |  |
| 25 | `FS.GI.FUND.PERMISSION.COUNTRY.CO.CODE` | `FsGiFundPermissionCountry_CoCode` | String |  |  |
| 26 | `FS.GI.FUND.PERMISSION.COUNTRY.DEPT.CODE` | `FsGiFundPermissionCountry_DeptCode` | String |  |  |
| 27 | `FS.GI.FUND.PERMISSION.COUNTRY.AUDITOR.CODE` | `FsGiFundPermissionCountry_AuditorCode` | String |  |  |
| 28 | `FS.GI.FUND.PERMISSION.COUNTRY.AUDIT.DATE.TIME` | `FsGiFundPermissionCountry_AuditDateTime` | String |  |  |
