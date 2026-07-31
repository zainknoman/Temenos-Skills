# FS.GA.ASSET.ALLOCATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ASSET.ALLOCATION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ASSET.ALLOCATION.PARENT.REF.ID` | `FsGaAssetAllocation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ASSET.ALLOCATION.ORA.ROWID` | `FsGaAssetAllocation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ASSET.ALLOCATION.FUND.ID` | `FsGaAssetAllocation_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.ASSET.ALLOCATION.ASSET.ALLOCATION.FUND.ID` | `FsGaAssetAllocation_AssetAllocationFundId` | TField |  | Asset Allocation Fund ID Multifonds DB Column is NPTF_BOT. |
| 5 | `FS.GA.ASSET.ALLOCATION.INTERNAL.SECURITY.ID` | `FsGaAssetAllocation_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 6 | `FS.GA.ASSET.ALLOCATION.SHARE.CLASS.CODE` | `FsGaAssetAllocation_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 7 | `FS.GA.ASSET.ALLOCATION.BEGIN.DATE` | `FsGaAssetAllocation_BeginDate` | TField |  | This field is used for the calculation of management expense ratio (MER) at the share class level. It refers to the launch date of a share class ID for MER reporting. Multifonds DB Column is BEGIN_DATE. |
| 8 | `FS.GA.ASSET.ALLOCATION.END.DATE` | `FsGaAssetAllocation_EndDate` | TField |  | This field is used for the calculation of management expense ratio (MER) at the share class level. It refers to the date upto which a share class is in existence for MER reporting. Multifonds DB Column is END_DATE. |
| 9 | `FS.GA.ASSET.ALLOCATION.RESERVED10` | `FsGaAssetAllocation_Reserved10` | TField |  |  |
| 10 | `FS.GA.ASSET.ALLOCATION.RESERVED9` | `FsGaAssetAllocation_Reserved9` | TField |  |  |
| 11 | `FS.GA.ASSET.ALLOCATION.RESERVED8` | `FsGaAssetAllocation_Reserved8` | TField |  |  |
| 12 | `FS.GA.ASSET.ALLOCATION.RESERVED7` | `FsGaAssetAllocation_Reserved7` | TField |  |  |
| 13 | `FS.GA.ASSET.ALLOCATION.RESERVED6` | `FsGaAssetAllocation_Reserved6` | TField |  |  |
| 14 | `FS.GA.ASSET.ALLOCATION.RESERVED5` | `FsGaAssetAllocation_Reserved5` | TField |  |  |
| 15 | `FS.GA.ASSET.ALLOCATION.RESERVED4` | `FsGaAssetAllocation_Reserved4` | TField |  |  |
| 16 | `FS.GA.ASSET.ALLOCATION.RESERVED3` | `FsGaAssetAllocation_Reserved3` | TField |  |  |
| 17 | `FS.GA.ASSET.ALLOCATION.RESERVED2` | `FsGaAssetAllocation_Reserved2` | TField |  |  |
| 18 | `FS.GA.ASSET.ALLOCATION.RESERVED1` | `FsGaAssetAllocation_Reserved1` | TField |  |  |
| 19 | `FS.GA.ASSET.ALLOCATION.LOCAL.REF` | `FsGaAssetAllocation_LocalRef` |  |  |  |
| 20 | `FS.GA.ASSET.ALLOCATION.OVERRIDE` | `FsGaAssetAllocation_Override` |  |  |  |
| 21 | `FS.GA.ASSET.ALLOCATION.RECORD.STATUS` | `FsGaAssetAllocation_RecordStatus` | String |  |  |
| 22 | `FS.GA.ASSET.ALLOCATION.CURR.NO` | `FsGaAssetAllocation_CurrNo` | String |  |  |
| 23 | `FS.GA.ASSET.ALLOCATION.INPUTTER` | `FsGaAssetAllocation_Inputter` |  |  |  |
| 24 | `FS.GA.ASSET.ALLOCATION.DATE.TIME` | `FsGaAssetAllocation_DateTime` |  |  |  |
| 25 | `FS.GA.ASSET.ALLOCATION.AUTHORISER` | `FsGaAssetAllocation_Authoriser` | String |  |  |
| 26 | `FS.GA.ASSET.ALLOCATION.CO.CODE` | `FsGaAssetAllocation_CoCode` | String |  |  |
| 27 | `FS.GA.ASSET.ALLOCATION.DEPT.CODE` | `FsGaAssetAllocation_DeptCode` | String |  |  |
| 28 | `FS.GA.ASSET.ALLOCATION.AUDITOR.CODE` | `FsGaAssetAllocation_AuditorCode` | String |  |  |
| 29 | `FS.GA.ASSET.ALLOCATION.AUDIT.DATE.TIME` | `FsGaAssetAllocation_AuditDateTime` | String |  |  |
