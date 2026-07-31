# FS.GA.ACCOUNTING.METHOD.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTING.METHOD.EXCEPTION` in `FS_Accounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.PARENT.REF.ID` | `FsGaAccountingMethodException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.ORA.ROWID` | `FsGaAccountingMethodException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.CHART.OF.ACCOUNTS.CODE` | `FsGaAccountingMethodException_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.TRANSACTION.SERVICE.CODE` | `FsGaAccountingMethodException_TransactionServiceCode` | TField |  | This is the transaction type. Multifonds DB Column is CSERV. |
| 5 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.GTI.CODE` | `FsGaAccountingMethodException_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.PERIOD.DAYS` | `FsGaAccountingMethodException_PeriodDays` | TField |  | Period Days Multifonds DB Column is NBJ_JOURS. |
| 7 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.HEDGING` | `FsGaAccountingMethodException_Hedging` | TField |  | Hedging Flag Multifonds DB Column is FLG_HEDGE. |
| 8 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.ACCOUNTING.METHOD` | `FsGaAccountingMethodException_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 9 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.FUND.ID` | `FsGaAccountingMethodException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 10 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.MANAGER.CODE` | `FsGaAccountingMethodException_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 11 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.BROKER.CODE` | `FsGaAccountingMethodException_BrokerCode` | TField |  | The code to identify a broker. Multifonds DB Column is BROKER. |
| 12 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED10` | `FsGaAccountingMethodException_Reserved10` | TField |  |  |
| 13 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED9` | `FsGaAccountingMethodException_Reserved9` | TField |  |  |
| 14 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED8` | `FsGaAccountingMethodException_Reserved8` | TField |  |  |
| 15 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED7` | `FsGaAccountingMethodException_Reserved7` | TField |  |  |
| 16 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED6` | `FsGaAccountingMethodException_Reserved6` | TField |  |  |
| 17 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED5` | `FsGaAccountingMethodException_Reserved5` | TField |  |  |
| 18 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED4` | `FsGaAccountingMethodException_Reserved4` | TField |  |  |
| 19 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED3` | `FsGaAccountingMethodException_Reserved3` | TField |  |  |
| 20 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED2` | `FsGaAccountingMethodException_Reserved2` | TField |  |  |
| 21 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RESERVED1` | `FsGaAccountingMethodException_Reserved1` | TField |  |  |
| 22 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.LOCAL.REF` | `FsGaAccountingMethodException_LocalRef` |  |  |  |
| 23 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.OVERRIDE` | `FsGaAccountingMethodException_Override` |  |  |  |
| 24 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.RECORD.STATUS` | `FsGaAccountingMethodException_RecordStatus` | String |  |  |
| 25 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.CURR.NO` | `FsGaAccountingMethodException_CurrNo` | String |  |  |
| 26 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.INPUTTER` | `FsGaAccountingMethodException_Inputter` |  |  |  |
| 27 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.DATE.TIME` | `FsGaAccountingMethodException_DateTime` |  |  |  |
| 28 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.AUTHORISER` | `FsGaAccountingMethodException_Authoriser` | String |  |  |
| 29 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.CO.CODE` | `FsGaAccountingMethodException_CoCode` | String |  |  |
| 30 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.DEPT.CODE` | `FsGaAccountingMethodException_DeptCode` | String |  |  |
| 31 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.AUDITOR.CODE` | `FsGaAccountingMethodException_AuditorCode` | String |  |  |
| 32 | `FS.GA.ACCOUNTING.METHOD.EXCEPTION.AUDIT.DATE.TIME` | `FsGaAccountingMethodException_AuditDateTime` | String |  |  |
