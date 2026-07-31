# FS.GA.CLHIA.DISTRIBUTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CLHIA.DISTRIBUTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLHIA.DISTRIBUTION.ISSUER` | `FsGaClhiaDistribution_Issuer` | TField |  | Issuer Multifonds DB Column is NISSUING. |
| 2 | `CLHIA.DISTRIBUTION.ISSUE.COUNTRY` | `FsGaClhiaDistribution_CountryCode` |  |  |  |
| 3 | `CLHIA.DISTRIBUTION.REGION.CODE` | `FsGaClhiaDistribution_RegionCode` | TField |  | Region Code Multifonds DB Column is REGION_CODE. |
| 4 | `CLHIA.DISTRIBUTION.ASSET.TYPE` | `FsGaClhiaDistribution_AssetType` | TField |  | Asset Type Multifonds DB Column is ASSET_TYPE. |
| 5 | `CLHIA.DISTRIBUTION.EFFECTIVE.DATE` | `FsGaClhiaDistribution_EffectiveDate` | TField |  | Effective date Multifonds DB Column is EFFECTIVE_DATE. |
| 6 | `CLHIA.DISTRIBUTION.ASSET.ALLOCATION.PERCENTAGE` | `FsGaClhiaDistribution_AssetAllocationPercentage` | TField |  | Asset Allocation Percentage Multifonds DB Column is PCT_ALLOCATION. |
| 7 | `CLHIA.DISTRIBUTION.DWH.EXPORT` | `FsGaClhiaDistribution_DwhExport` | TField |  | DWH Export Multifonds DB Column is DWH_EXPORT. |
| 8 | `CLHIA.DISTRIBUTION.RECORD.STATUS` | `FsGaClhiaDistribution_RecordStatus` | String |  |  |
| 9 | `CLHIA.DISTRIBUTION.CURR.NO` | `FsGaClhiaDistribution_CurrNo` | String |  |  |
| 10 | `CLHIA.DISTRIBUTION.INPUTTER` | `FsGaClhiaDistribution_Inputter` |  |  |  |
| 11 | `CLHIA.DISTRIBUTION.DATE.TIME` | `FsGaClhiaDistribution_DateTime` |  |  |  |
| 12 | `CLHIA.DISTRIBUTION.AUTHORISER` | `FsGaClhiaDistribution_Authoriser` | String |  |  |
| 13 | `CLHIA.DISTRIBUTION.CO.CODE` | `FsGaClhiaDistribution_CoCode` | String |  |  |
| 14 | `CLHIA.DISTRIBUTION.DEPT.CODE` | `FsGaClhiaDistribution_DeptCode` | String |  |  |
| 15 | `CLHIA.DISTRIBUTION.AUDITOR.CODE` | `FsGaClhiaDistribution_AuditorCode` | String |  |  |
| 16 | `CLHIA.DISTRIBUTION.AUDIT.DATE.TIME` | `FsGaClhiaDistribution_AuditDateTime` | String |  |  |
