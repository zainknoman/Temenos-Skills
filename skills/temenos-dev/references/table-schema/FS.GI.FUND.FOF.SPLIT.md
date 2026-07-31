# FS.GI.FUND.FOF.SPLIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.FOF.SPLIT` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.FOF.SPLIT.PARENT.REF.ID` | `FsGiFundFofSplit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.FOF.SPLIT.ORA.ROWID` | `FsGiFundFofSplit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.FOF.SPLIT.FOF.FUND.ID` | `FsGiFundFofSplit_FofFundId` | TField |  | Fund ID of the underlying TA Fund that will be part of the fund of fund functionality. Multifonds DB Column is NPTF_FOF. |
| 4 | `FS.GI.FUND.FOF.SPLIT.EFFECTIVE.DATE` | `FsGiFundFofSplit_EffectiveDate` | TField |  | The date from which the fund of fund functionality will be effective. Multifonds DB Column is EFFECTIVE_DATE. |
| 5 | `FS.GI.FUND.FOF.SPLIT.END.DATE` | `FsGiFundFofSplit_EndDate` | TField |  | The date from which the fund of fund functionality will end. Multifonds DB Column is END_DATE. |
| 6 | `FS.GI.FUND.FOF.SPLIT.PORTFOLIO.LINK` | `FsGiFundFofSplit_PortfolioLink` | TField |  | Fund of Fund Portfolio Link. Multifonds DB Column is PORTFOLIO_LINK. |
| 7 | `FS.GI.FUND.FOF.SPLIT.TA.FUND.ID` | `FsGiFundFofSplit_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 8 | `FS.GI.FUND.FOF.SPLIT.SHARE.CLASS.CODE` | `FsGiFundFofSplit_ShareClassCode` | TField |  | Fund share class code Multifonds DB Column is TPART. |
| 9 | `FS.GI.FUND.FOF.SPLIT.SPLIT.PERCENTAGE` | `FsGiFundFofSplit_SplitPercentage` | TField |  | Split percentage of Fund of funds proportion of the investment. Multifonds DB Column is PCT_SPLIT. |
| 10 | `FS.GI.FUND.FOF.SPLIT.THRESHOLD.FLAG` | `FsGiFundFofSplit_ThresholdFlag` | TField |  | Threshold Flag. Multifonds DB Column is FLG_THRESHOLD. |
| 11 | `FS.GI.FUND.FOF.SPLIT.THRESHOLD.AMOUNT` | `FsGiFundFofSplit_ThresholdAmount` | TField |  | The threshold amount defined for the fund share class. Multifonds DB Column is THRESHOLD_AMT. |
| 12 | `FS.GI.FUND.FOF.SPLIT.CURRENCY` | `FsGiFundFofSplit_Currency` | TField |  | Threshold currency code (in 3 letter format eg: USD). Multifonds DB Column is THRESHOLD_CMON. |
| 13 | `FS.GI.FUND.FOF.SPLIT.SEQUENCE.ID` | `FsGiFundFofSplit_SequenceId` | TField |  | Sequence ID for the fund of fund split. Multifonds DB Column is SEQUENCE_NO. |
| 14 | `FS.GI.FUND.FOF.SPLIT.SPLIT.SEQ.DELETE.FLAG` | `FsGiFundFofSplit_SplitSeqDeleteFlag` | TField |  | Fund of Fund Split sequence deletion flag Multifonds DB Column is SEQ_DELETE. |
| 15 | `FS.GI.FUND.FOF.SPLIT.INTERNAL.ID` | `FsGiFundFofSplit_InternalId` | TField |  | Unique internal identifier of the FOF split record. Multifonds DB Column is INTERNAL_ID. |
| 16 | `FS.GI.FUND.FOF.SPLIT.FUND.ID` | `FsGiFundFofSplit_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 17 | `FS.GI.FUND.FOF.SPLIT.CLASS.CURRENCY` | `FsGiFundFofSplit_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 18 | `FS.GI.FUND.FOF.SPLIT.FOF.SHARE.CLASS` | `FsGiFundFofSplit_FofShareClass` | TField |  | Feeder share class Multifonds DB Column is TPART_FOF. |
| 19 | `FS.GI.FUND.FOF.SPLIT.FOF.REGISTER.ID` | `FsGiFundFofSplit_FofRegisterId` | TField |  | Feeder Register ID Multifonds DB Column is NREGISTER_FOF. |
| 20 | `FS.GI.FUND.FOF.SPLIT.CAPITAL.FLOW.MASTER` | `FsGiFundFofSplit_CapitalFlowMaster` | TField |  | Capital Flow to Master Multifonds DB Column is CAPFLW_MAS. |
| 21 | `FS.GI.FUND.FOF.SPLIT.FOF.FLAG.MGMT.FEE` | `FsGiFundFofSplit_FofFlagMgmtFee` | TField |  | Flag to define if the management fees to be allocated to feeder fund Multifonds DB Column is FLG_MGTFEE_FOF. |
| 22 | `FS.GI.FUND.FOF.SPLIT.RESERVED10` | `FsGiFundFofSplit_Reserved10` | TField |  |  |
| 23 | `FS.GI.FUND.FOF.SPLIT.RESERVED9` | `FsGiFundFofSplit_Reserved9` | TField |  |  |
| 24 | `FS.GI.FUND.FOF.SPLIT.RESERVED8` | `FsGiFundFofSplit_Reserved8` | TField |  |  |
| 25 | `FS.GI.FUND.FOF.SPLIT.RESERVED7` | `FsGiFundFofSplit_Reserved7` | TField |  |  |
| 26 | `FS.GI.FUND.FOF.SPLIT.RESERVED6` | `FsGiFundFofSplit_Reserved6` | TField |  |  |
| 27 | `FS.GI.FUND.FOF.SPLIT.RESERVED5` | `FsGiFundFofSplit_Reserved5` | TField |  |  |
| 28 | `FS.GI.FUND.FOF.SPLIT.RESERVED4` | `FsGiFundFofSplit_Reserved4` | TField |  |  |
| 29 | `FS.GI.FUND.FOF.SPLIT.RESERVED3` | `FsGiFundFofSplit_Reserved3` | TField |  |  |
| 30 | `FS.GI.FUND.FOF.SPLIT.RESERVED2` | `FsGiFundFofSplit_Reserved2` | TField |  |  |
| 31 | `FS.GI.FUND.FOF.SPLIT.RESERVED1` | `FsGiFundFofSplit_Reserved1` | TField |  |  |
| 32 | `FS.GI.FUND.FOF.SPLIT.LOCAL.REF` | `FsGiFundFofSplit_LocalRef` |  |  |  |
| 33 | `FS.GI.FUND.FOF.SPLIT.OVERRIDE` | `FsGiFundFofSplit_Override` |  |  |  |
| 34 | `FS.GI.FUND.FOF.SPLIT.RECORD.STATUS` | `FsGiFundFofSplit_RecordStatus` | String |  |  |
| 35 | `FS.GI.FUND.FOF.SPLIT.CURR.NO` | `FsGiFundFofSplit_CurrNo` | String |  |  |
| 36 | `FS.GI.FUND.FOF.SPLIT.INPUTTER` | `FsGiFundFofSplit_Inputter` |  |  |  |
| 37 | `FS.GI.FUND.FOF.SPLIT.DATE.TIME` | `FsGiFundFofSplit_DateTime` |  |  |  |
| 38 | `FS.GI.FUND.FOF.SPLIT.AUTHORISER` | `FsGiFundFofSplit_Authoriser` | String |  |  |
| 39 | `FS.GI.FUND.FOF.SPLIT.CO.CODE` | `FsGiFundFofSplit_CoCode` | String |  |  |
| 40 | `FS.GI.FUND.FOF.SPLIT.DEPT.CODE` | `FsGiFundFofSplit_DeptCode` | String |  |  |
| 41 | `FS.GI.FUND.FOF.SPLIT.AUDITOR.CODE` | `FsGiFundFofSplit_AuditorCode` | String |  |  |
| 42 | `FS.GI.FUND.FOF.SPLIT.AUDIT.DATE.TIME` | `FsGiFundFofSplit_AuditDateTime` | String |  |  |
