# FS.GA.ECONOMIC.AND.RISK.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.ECONOMIC.AND.RISK.CODE` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ECONOMIC.AND.RISK.CODE.FUND.ID` | `FsGaEconomicAndRiskCode_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.ECONOMIC.AND.RISK.CODE.INTERNAL.SECURITY.ID` | `FsGaEconomicAndRiskCode_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 3 | `FS.GA.ECONOMIC.AND.RISK.CODE.GTI.CODE` | `FsGaEconomicAndRiskCode_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 4 | `FS.GA.ECONOMIC.AND.RISK.CODE.SECTOR` | `FsGaEconomicAndRiskCode_Sector` | TField |  | Industry sector linked to a correspondent Multifonds DB Column is SCO. |
| 5 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED10` | `FsGaEconomicAndRiskCode_Reserved10` | TField |  |  |
| 6 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED9` | `FsGaEconomicAndRiskCode_Reserved9` | TField |  |  |
| 7 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED8` | `FsGaEconomicAndRiskCode_Reserved8` | TField |  |  |
| 8 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED7` | `FsGaEconomicAndRiskCode_Reserved7` | TField |  |  |
| 9 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED6` | `FsGaEconomicAndRiskCode_Reserved6` | TField |  |  |
| 10 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED5` | `FsGaEconomicAndRiskCode_Reserved5` | TField |  |  |
| 11 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED4` | `FsGaEconomicAndRiskCode_Reserved4` | TField |  |  |
| 12 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED3` | `FsGaEconomicAndRiskCode_Reserved3` | TField |  |  |
| 13 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED2` | `FsGaEconomicAndRiskCode_Reserved2` | TField |  |  |
| 14 | `FS.GA.ECONOMIC.AND.RISK.CODE.RESERVED1` | `FsGaEconomicAndRiskCode_Reserved1` | TField |  |  |
| 15 | `FS.GA.ECONOMIC.AND.RISK.CODE.RECORD.STATUS` | `FsGaEconomicAndRiskCode_RecordStatus` | String |  |  |
| 16 | `FS.GA.ECONOMIC.AND.RISK.CODE.CURR.NO` | `FsGaEconomicAndRiskCode_CurrNo` | String |  |  |
| 17 | `FS.GA.ECONOMIC.AND.RISK.CODE.INPUTTER` | `FsGaEconomicAndRiskCode_Inputter` |  |  |  |
| 18 | `FS.GA.ECONOMIC.AND.RISK.CODE.DATE.TIME` | `FsGaEconomicAndRiskCode_DateTime` |  |  |  |
| 19 | `FS.GA.ECONOMIC.AND.RISK.CODE.AUTHORISER` | `FsGaEconomicAndRiskCode_Authoriser` | String |  |  |
| 20 | `FS.GA.ECONOMIC.AND.RISK.CODE.CO.CODE` | `FsGaEconomicAndRiskCode_CoCode` | String |  |  |
| 21 | `FS.GA.ECONOMIC.AND.RISK.CODE.DEPT.CODE` | `FsGaEconomicAndRiskCode_DeptCode` | String |  |  |
| 22 | `FS.GA.ECONOMIC.AND.RISK.CODE.AUDITOR.CODE` | `FsGaEconomicAndRiskCode_AuditorCode` | String |  |  |
| 23 | `FS.GA.ECONOMIC.AND.RISK.CODE.AUDIT.DATE.TIME` | `FsGaEconomicAndRiskCode_AuditDateTime` | String |  |  |
