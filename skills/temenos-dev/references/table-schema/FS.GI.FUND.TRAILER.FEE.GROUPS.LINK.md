# FS.GI.FUND.TRAILER.FEE.GROUPS.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.TRAILER.FEE.GROUPS.LINK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.PARENT.REF.ID` | `FsGiFundTrailerFeeGroupsLink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.ORA.ROWID` | `FsGiFundTrailerFeeGroupsLink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.FUND.ID` | `FsGiFundTrailerFeeGroupsLink_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.SHARE.CLASS.CODE` | `FsGiFundTrailerFeeGroupsLink_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.AGENT.GROUP` | `FsGiFundTrailerFeeGroupsLink_AgentGroup` | TField |  | Type of the trailer fee agent designated for Investors. For example 0001-Retail, 0002-Institutional etc., Multifonds DB Column is OUTLET_GRP. |
| 6 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.TRAILER.FEE.FUND.GROUP` | `FsGiFundTrailerFeeGroupsLink_TrailerFeeFundGroup` | TField |  | Linking the trailer fee group in order to calculate the trailer fees for the fund. Multifonds DB Column is CGROUP_TF. |
| 7 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED10` | `FsGiFundTrailerFeeGroupsLink_Reserved10` | TField |  |  |
| 8 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED9` | `FsGiFundTrailerFeeGroupsLink_Reserved9` | TField |  |  |
| 9 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED8` | `FsGiFundTrailerFeeGroupsLink_Reserved8` | TField |  |  |
| 10 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED7` | `FsGiFundTrailerFeeGroupsLink_Reserved7` | TField |  |  |
| 11 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED6` | `FsGiFundTrailerFeeGroupsLink_Reserved6` | TField |  |  |
| 12 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED5` | `FsGiFundTrailerFeeGroupsLink_Reserved5` | TField |  |  |
| 13 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED4` | `FsGiFundTrailerFeeGroupsLink_Reserved4` | TField |  |  |
| 14 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED3` | `FsGiFundTrailerFeeGroupsLink_Reserved3` | TField |  |  |
| 15 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED2` | `FsGiFundTrailerFeeGroupsLink_Reserved2` | TField |  |  |
| 16 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RESERVED1` | `FsGiFundTrailerFeeGroupsLink_Reserved1` | TField |  |  |
| 17 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.LOCAL.REF` | `FsGiFundTrailerFeeGroupsLink_LocalRef` |  |  |  |
| 18 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.OVERRIDE` | `FsGiFundTrailerFeeGroupsLink_Override` |  |  |  |
| 19 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.RECORD.STATUS` | `FsGiFundTrailerFeeGroupsLink_RecordStatus` | String |  |  |
| 20 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.CURR.NO` | `FsGiFundTrailerFeeGroupsLink_CurrNo` | String |  |  |
| 21 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.INPUTTER` | `FsGiFundTrailerFeeGroupsLink_Inputter` |  |  |  |
| 22 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.DATE.TIME` | `FsGiFundTrailerFeeGroupsLink_DateTime` |  |  |  |
| 23 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.AUTHORISER` | `FsGiFundTrailerFeeGroupsLink_Authoriser` | String |  |  |
| 24 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.CO.CODE` | `FsGiFundTrailerFeeGroupsLink_CoCode` | String |  |  |
| 25 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.DEPT.CODE` | `FsGiFundTrailerFeeGroupsLink_DeptCode` | String |  |  |
| 26 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.AUDITOR.CODE` | `FsGiFundTrailerFeeGroupsLink_AuditorCode` | String |  |  |
| 27 | `FS.GI.FUND.TRAILER.FEE.GROUPS.LINK.AUDIT.DATE.TIME` | `FsGiFundTrailerFeeGroupsLink_AuditDateTime` | String |  |  |
