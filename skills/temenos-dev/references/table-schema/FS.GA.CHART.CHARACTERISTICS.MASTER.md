# FS.GA.CHART.CHARACTERISTICS.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.CHART.CHARACTERISTICS.MASTER` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CHART.CHARACTERISTICS.MASTER.CHART.OF.ACCOUNTS.CODE` | `FsGaChartCharacteristicsMaster_ChartOfAccountsNumber` |  |  |  |
| 2 | `FS.GA.CHART.CHARACTERISTICS.MASTER.FLAG.PROFIT.AND.LOSS.ACCOUNTS` | `FsGaChartCharacteristicsMaster_FlagProfitAndLossAccounts` | TField |  | To define Suffix accounts for Profit and Loss Accounts Multifonds DB Column is FLG_CMON_PL. |
| 3 | `FS.GA.CHART.CHARACTERISTICS.MASTER.FLAG.UNREALISED.ACCOUNTS` | `FsGaChartCharacteristicsMaster_FlagUnrealisedAccounts` | TField |  | To define Suffix accounts for Unrealised Accounts Multifonds DB Column is FLG_CMON_UR. |
| 4 | `FS.GA.CHART.CHARACTERISTICS.MASTER.FLAG.REALISED.ACCOUNTS` | `FsGaChartCharacteristicsMaster_FlagRealisedAccounts` | TField |  | To define Suffix accounts for Realised Accounts Multifonds DB Column is FLG_CMON_RE. |
| 5 | `FS.GA.CHART.CHARACTERISTICS.MASTER.QUOTATION.TYPE` | `FsGaChartCharacteristicsMaster_QuotationType` | TField |  | Quatation Type Multifonds DB Column is CTYPE. |
| 6 | `FS.GA.CHART.CHARACTERISTICS.MASTER.LOCAL.TYPE` | `FsGaChartCharacteristicsMaster_LocalType` | TField |  | Local Type of granular information to query in the Chart charesteric table Multifonds DB Column is CTABLE_COTLOCAL. |
| 7 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED10` | `FsGaChartCharacteristicsMaster_Reserved10` | TField |  |  |
| 8 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED9` | `FsGaChartCharacteristicsMaster_Reserved9` | TField |  |  |
| 9 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED8` | `FsGaChartCharacteristicsMaster_Reserved8` | TField |  |  |
| 10 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED7` | `FsGaChartCharacteristicsMaster_Reserved7` | TField |  |  |
| 11 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED6` | `FsGaChartCharacteristicsMaster_Reserved6` | TField |  |  |
| 12 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED5` | `FsGaChartCharacteristicsMaster_Reserved5` | TField |  |  |
| 13 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED4` | `FsGaChartCharacteristicsMaster_Reserved4` | TField |  |  |
| 14 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED3` | `FsGaChartCharacteristicsMaster_Reserved3` | TField |  |  |
| 15 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED2` | `FsGaChartCharacteristicsMaster_Reserved2` | TField |  |  |
| 16 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RESERVED1` | `FsGaChartCharacteristicsMaster_Reserved1` | TField |  |  |
| 17 | `FS.GA.CHART.CHARACTERISTICS.MASTER.RECORD.STATUS` | `FsGaChartCharacteristicsMaster_RecordStatus` | String |  |  |
| 18 | `FS.GA.CHART.CHARACTERISTICS.MASTER.CURR.NO` | `FsGaChartCharacteristicsMaster_CurrNo` | String |  |  |
| 19 | `FS.GA.CHART.CHARACTERISTICS.MASTER.INPUTTER` | `FsGaChartCharacteristicsMaster_Inputter` |  |  |  |
| 20 | `FS.GA.CHART.CHARACTERISTICS.MASTER.DATE.TIME` | `FsGaChartCharacteristicsMaster_DateTime` |  |  |  |
| 21 | `FS.GA.CHART.CHARACTERISTICS.MASTER.AUTHORISER` | `FsGaChartCharacteristicsMaster_Authoriser` | String |  |  |
| 22 | `FS.GA.CHART.CHARACTERISTICS.MASTER.CO.CODE` | `FsGaChartCharacteristicsMaster_CoCode` | String |  |  |
| 23 | `FS.GA.CHART.CHARACTERISTICS.MASTER.DEPT.CODE` | `FsGaChartCharacteristicsMaster_DeptCode` | String |  |  |
| 24 | `FS.GA.CHART.CHARACTERISTICS.MASTER.AUDITOR.CODE` | `FsGaChartCharacteristicsMaster_AuditorCode` | String |  |  |
| 25 | `FS.GA.CHART.CHARACTERISTICS.MASTER.AUDIT.DATE.TIME` | `FsGaChartCharacteristicsMaster_AuditDateTime` | String |  |  |
