# FS.GI.FUND.INITIAL.SUB.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.INITIAL.SUB.PERIOD` in `FS_FundDealing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.INITIAL.SUB.PERIOD.PARENT.REF.ID` | `FsGiFundInitialSubPeriod_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.INITIAL.SUB.PERIOD.ORA.ROWID` | `FsGiFundInitialSubPeriod_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.INITIAL.SUB.PERIOD.TA.FUND.ID` | `FsGiFundInitialSubPeriod_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.INITIAL.SUB.PERIOD.SHARE.CLASS.CODE` | `FsGiFundInitialSubPeriod_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.INITIAL.SUB.PERIOD.NAV.PRICE` | `FsGiFundInitialSubPeriod_NavPrice` | TField |  | Fixed NAV price to be applied on the initial subscription period orders. Multifonds DB Column is UNIT_PRICE. |
| 6 | `FS.GI.FUND.INITIAL.SUB.PERIOD.START.DATE` | `FsGiFundInitialSubPeriod_StartDate` | TField |  | Date from which the initial subscription period starts. Multifonds DB Column is DSTART. |
| 7 | `FS.GI.FUND.INITIAL.SUB.PERIOD.END.DATE` | `FsGiFundInitialSubPeriod_EndDate` | TField |  | Date on which the initial subscription period ends. Multifonds DB Column is DEND. |
| 8 | `FS.GI.FUND.INITIAL.SUB.PERIOD.TRADE.DATE` | `FsGiFundInitialSubPeriod_TradeDate` | TField |  | Trade date applicabe on the Initial Subscription period orders. Multifonds DB Column is DOPER. |
| 9 | `FS.GI.FUND.INITIAL.SUB.PERIOD.INTERNAL.ID` | `FsGiFundInitialSubPeriod_InternalId` | TField |  | Unique internal identifier for the record. Multifonds DB Column is INTERNAL_ID. |
| 10 | `FS.GI.FUND.INITIAL.SUB.PERIOD.FUND.ID` | `FsGiFundInitialSubPeriod_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 11 | `FS.GI.FUND.INITIAL.SUB.PERIOD.CLASS.CURRENCY` | `FsGiFundInitialSubPeriod_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 12 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED10` | `FsGiFundInitialSubPeriod_Reserved10` | TField |  |  |
| 13 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED9` | `FsGiFundInitialSubPeriod_Reserved9` | TField |  |  |
| 14 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED8` | `FsGiFundInitialSubPeriod_Reserved8` | TField |  |  |
| 15 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED7` | `FsGiFundInitialSubPeriod_Reserved7` | TField |  |  |
| 16 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED6` | `FsGiFundInitialSubPeriod_Reserved6` | TField |  |  |
| 17 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED5` | `FsGiFundInitialSubPeriod_Reserved5` | TField |  |  |
| 18 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED4` | `FsGiFundInitialSubPeriod_Reserved4` | TField |  |  |
| 19 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED3` | `FsGiFundInitialSubPeriod_Reserved3` | TField |  |  |
| 20 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED2` | `FsGiFundInitialSubPeriod_Reserved2` | TField |  |  |
| 21 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RESERVED1` | `FsGiFundInitialSubPeriod_Reserved1` | TField |  |  |
| 22 | `FS.GI.FUND.INITIAL.SUB.PERIOD.LOCAL.REF` | `FsGiFundInitialSubPeriod_LocalRef` |  |  |  |
| 23 | `FS.GI.FUND.INITIAL.SUB.PERIOD.OVERRIDE` | `FsGiFundInitialSubPeriod_Override` |  |  |  |
| 24 | `FS.GI.FUND.INITIAL.SUB.PERIOD.RECORD.STATUS` | `FsGiFundInitialSubPeriod_RecordStatus` | String |  |  |
| 25 | `FS.GI.FUND.INITIAL.SUB.PERIOD.CURR.NO` | `FsGiFundInitialSubPeriod_CurrNo` | String |  |  |
| 26 | `FS.GI.FUND.INITIAL.SUB.PERIOD.INPUTTER` | `FsGiFundInitialSubPeriod_Inputter` |  |  |  |
| 27 | `FS.GI.FUND.INITIAL.SUB.PERIOD.DATE.TIME` | `FsGiFundInitialSubPeriod_DateTime` |  |  |  |
| 28 | `FS.GI.FUND.INITIAL.SUB.PERIOD.AUTHORISER` | `FsGiFundInitialSubPeriod_Authoriser` | String |  |  |
| 29 | `FS.GI.FUND.INITIAL.SUB.PERIOD.CO.CODE` | `FsGiFundInitialSubPeriod_CoCode` | String |  |  |
| 30 | `FS.GI.FUND.INITIAL.SUB.PERIOD.DEPT.CODE` | `FsGiFundInitialSubPeriod_DeptCode` | String |  |  |
| 31 | `FS.GI.FUND.INITIAL.SUB.PERIOD.AUDITOR.CODE` | `FsGiFundInitialSubPeriod_AuditorCode` | String |  |  |
| 32 | `FS.GI.FUND.INITIAL.SUB.PERIOD.AUDIT.DATE.TIME` | `FsGiFundInitialSubPeriod_AuditDateTime` | String |  |  |
