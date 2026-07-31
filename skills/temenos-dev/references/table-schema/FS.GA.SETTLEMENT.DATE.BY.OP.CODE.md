# FS.GA.SETTLEMENT.DATE.BY.OP.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.SETTLEMENT.DATE.BY.OP.CODE` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.FUND.ID` | `FsGaSettlementDateByOpCode_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.OPERATION.CODE` | `FsGaSettlementDateByOpCode_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 3 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.DAYS.OF.ACCRUED.INTEREST` | `FsGaSettlementDateByOpCode_DaysOfAccruedInterest` | TField |  | Number of days of purchase/sale interest in a transaction done on an interest bearing instrument Multifonds DB Column is NBJOURS. |
| 4 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.WORKING.DAYS` | `FsGaSettlementDateByOpCode_WorkingDays` | TField |  | If set, the number of days entered will be added as business days to the trade date on a capstock or deal to obtain the value date Multifonds DB Column is FJOUVR. |
| 5 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED10` | `FsGaSettlementDateByOpCode_Reserved10` | TField |  |  |
| 6 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED9` | `FsGaSettlementDateByOpCode_Reserved9` | TField |  |  |
| 7 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED8` | `FsGaSettlementDateByOpCode_Reserved8` | TField |  |  |
| 8 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED7` | `FsGaSettlementDateByOpCode_Reserved7` | TField |  |  |
| 9 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED6` | `FsGaSettlementDateByOpCode_Reserved6` | TField |  |  |
| 10 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED5` | `FsGaSettlementDateByOpCode_Reserved5` | TField |  |  |
| 11 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED4` | `FsGaSettlementDateByOpCode_Reserved4` | TField |  |  |
| 12 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED3` | `FsGaSettlementDateByOpCode_Reserved3` | TField |  |  |
| 13 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED2` | `FsGaSettlementDateByOpCode_Reserved2` | TField |  |  |
| 14 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RESERVED1` | `FsGaSettlementDateByOpCode_Reserved1` | TField |  |  |
| 15 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.RECORD.STATUS` | `FsGaSettlementDateByOpCode_RecordStatus` | String |  |  |
| 16 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.CURR.NO` | `FsGaSettlementDateByOpCode_CurrNo` | String |  |  |
| 17 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.INPUTTER` | `FsGaSettlementDateByOpCode_Inputter` |  |  |  |
| 18 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.DATE.TIME` | `FsGaSettlementDateByOpCode_DateTime` |  |  |  |
| 19 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.AUTHORISER` | `FsGaSettlementDateByOpCode_Authoriser` | String |  |  |
| 20 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.CO.CODE` | `FsGaSettlementDateByOpCode_CoCode` | String |  |  |
| 21 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.DEPT.CODE` | `FsGaSettlementDateByOpCode_DeptCode` | String |  |  |
| 22 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.AUDITOR.CODE` | `FsGaSettlementDateByOpCode_AuditorCode` | String |  |  |
| 23 | `FS.GA.SETTLEMENT.DATE.BY.OP.CODE.AUDIT.DATE.TIME` | `FsGaSettlementDateByOpCode_AuditDateTime` | String |  |  |
