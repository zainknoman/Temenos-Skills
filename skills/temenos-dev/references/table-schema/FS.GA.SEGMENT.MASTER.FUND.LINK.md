# FS.GA.SEGMENT.MASTER.FUND.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GA.SEGMENT.MASTER.FUND.LINK` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SEGMENT.MASTER.FUND.LINK.FUND.ID` | `FsGaSegmentMasterFundLink_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.SEGMENT.MASTER.FUND.LINK.SUB.FUND.NAME` | `FsGaSegmentMasterFundLink_SubFundName` | TField |  | Corresponds to the ID of a Pool or to the ID of a fund partipating in a Pool or to the ID of a segment funds participating in a segment fund structure Multifonds DB Column is NPTF_LINK. |
| 3 | `FS.GA.SEGMENT.MASTER.FUND.LINK.FUND.TYPES` | `FsGaSegmentMasterFundLink_FundTypes` | TField |  | Based on the fund type multifonds compares the fund static data (e.g. the fund domicile , the reference currency...) of the segment and the master Multifonds DB Column is TYPE_LINK. |
| 4 | `FS.GA.SEGMENT.MASTER.FUND.LINK.FLAG.DOUBLE.VALUATION` | `FsGaSegmentMasterFundLink_FlagDoubleValuation` | TField |  | Flag Double Valuation Multifonds DB Column is FLG_DOUBLE_VALUATION. |
| 5 | `FS.GA.SEGMENT.MASTER.FUND.LINK.ASSET.VALUATION.DEVIANCE` | `FsGaSegmentMasterFundLink_AssetValuationDeviance` | TField |  | Asset Valuation Deviance Multifonds DB Column is MMF_ASSET_THRESHOLD. |
| 6 | `FS.GA.SEGMENT.MASTER.FUND.LINK.SWITCH.ASSET.VALUATION.TO.MMF` | `FsGaSegmentMasterFundLink_SwitchAssetValuationToMmf` | TField |  | Switch Asset Valuation to MMF Multifonds DB Column is MMF_SWITCH_ASSET_VALUATION. |
| 7 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED10` | `FsGaSegmentMasterFundLink_Reserved10` | TField |  |  |
| 8 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED9` | `FsGaSegmentMasterFundLink_Reserved9` | TField |  |  |
| 9 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED8` | `FsGaSegmentMasterFundLink_Reserved8` | TField |  |  |
| 10 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED7` | `FsGaSegmentMasterFundLink_Reserved7` | TField |  |  |
| 11 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED6` | `FsGaSegmentMasterFundLink_Reserved6` | TField |  |  |
| 12 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED5` | `FsGaSegmentMasterFundLink_Reserved5` | TField |  |  |
| 13 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED4` | `FsGaSegmentMasterFundLink_Reserved4` | TField |  |  |
| 14 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED3` | `FsGaSegmentMasterFundLink_Reserved3` | TField |  |  |
| 15 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED2` | `FsGaSegmentMasterFundLink_Reserved2` | TField |  |  |
| 16 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RESERVED1` | `FsGaSegmentMasterFundLink_Reserved1` | TField |  |  |
| 17 | `FS.GA.SEGMENT.MASTER.FUND.LINK.RECORD.STATUS` | `FsGaSegmentMasterFundLink_RecordStatus` | String |  |  |
| 18 | `FS.GA.SEGMENT.MASTER.FUND.LINK.CURR.NO` | `FsGaSegmentMasterFundLink_CurrNo` | String |  |  |
| 19 | `FS.GA.SEGMENT.MASTER.FUND.LINK.INPUTTER` | `FsGaSegmentMasterFundLink_Inputter` |  |  |  |
| 20 | `FS.GA.SEGMENT.MASTER.FUND.LINK.DATE.TIME` | `FsGaSegmentMasterFundLink_DateTime` |  |  |  |
| 21 | `FS.GA.SEGMENT.MASTER.FUND.LINK.AUTHORISER` | `FsGaSegmentMasterFundLink_Authoriser` | String |  |  |
| 22 | `FS.GA.SEGMENT.MASTER.FUND.LINK.CO.CODE` | `FsGaSegmentMasterFundLink_CoCode` | String |  |  |
| 23 | `FS.GA.SEGMENT.MASTER.FUND.LINK.DEPT.CODE` | `FsGaSegmentMasterFundLink_DeptCode` | String |  |  |
| 24 | `FS.GA.SEGMENT.MASTER.FUND.LINK.AUDITOR.CODE` | `FsGaSegmentMasterFundLink_AuditorCode` | String |  |  |
| 25 | `FS.GA.SEGMENT.MASTER.FUND.LINK.AUDIT.DATE.TIME` | `FsGaSegmentMasterFundLink_AuditDateTime` | String |  |  |
