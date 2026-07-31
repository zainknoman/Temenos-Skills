# FS.GA.FUND.MANAGER — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.MANAGER` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.MANAGER.PARENT.REF.ID` | `FsGaFundManager_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUND.MANAGER.ORA.ROWID` | `FsGaFundManager_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUND.MANAGER.FUND.ID` | `FsGaFundManager_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUND.MANAGER.MANAGER.CODE` | `FsGaFundManager_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 5 | `FS.GA.FUND.MANAGER.CAPSTOCK.PERCENTAGE` | `FsGaFundManager_CapstockPercentage` | TField |  | This gives the user the ability to allocate percentages to the manager level relating to net cap stock subscriptions. This percentage must total 100%. Multifonds DB Column is PCT_ACT. |
| 6 | `FS.GA.FUND.MANAGER.GLOBAL.SUBSCRIPTION.PERCENTAGE` | `FsGaFundManager_GlobalSubscriptionPercentage` | TField |  | It should have the same percentage as the percentage indicated in the column &apos;Subscription percentage&apos; Multifonds DB Column is PCT. |
| 7 | `FS.GA.FUND.MANAGER.POOL.PORTFOLIO.MANAGER` | `FsGaFundManager_PoolPortfolioManager` | TField |  | The pool fund manager is defined in this field. Multifonds DB Column is PO_NS_PORTFOLIO. |
| 8 | `FS.GA.FUND.MANAGER.DATE.OF.EFFECTIVE` | `FsGaFundManager_DateOfEffective` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 9 | `FS.GA.FUND.MANAGER.CURRENCY.PERCENTAGE` | `FsGaFundManager_CurrencyPercentage` | TField |  | The allocation % of the Subs/Reds transaction between the fund&apos;s managers can be defined in different currency. It must not be filled in with the fund&apos;s reference currency. Multifonds DB Column is PCT_CMON. |
| 10 | `FS.GA.FUND.MANAGER.REDEMPTION.PERCENTAGE` | `FsGaFundManager_RedemptionPercentage` | TField |  | This gives the user the ability to allocate percentages to the manager level relating to net cap stock redemption. This percentage must total 100%. Multifonds DB Column is PCT_RED. |
| 11 | `FS.GA.FUND.MANAGER.GLOBAL.REDEMPTION.PERCENTAGE` | `FsGaFundManager_GlobalRedemptionPercentage` | TField |  | It should have the same percentage as the percentage indicated in the column Redemption percentage&apos; Multifonds DB Column is PCT_GL_RED. |
| 12 | `FS.GA.FUND.MANAGER.OTHER.PERCENTAGE` | `FsGaFundManager_OtherPercentage` | TField |  | If parameterized, the consolidated cash balance held at the fund level (to Manager id &apos;0&apos;) will be allocated between the fund&apos;s manager according to the percentages entered in this field. Multifonds DB Column is PCT_OTHER. |
| 13 | `FS.GA.FUND.MANAGER.RESERVED10` | `FsGaFundManager_Reserved10` | TField |  |  |
| 14 | `FS.GA.FUND.MANAGER.RESERVED9` | `FsGaFundManager_Reserved9` | TField |  |  |
| 15 | `FS.GA.FUND.MANAGER.RESERVED8` | `FsGaFundManager_Reserved8` | TField |  |  |
| 16 | `FS.GA.FUND.MANAGER.RESERVED7` | `FsGaFundManager_Reserved7` | TField |  |  |
| 17 | `FS.GA.FUND.MANAGER.RESERVED6` | `FsGaFundManager_Reserved6` | TField |  |  |
| 18 | `FS.GA.FUND.MANAGER.RESERVED5` | `FsGaFundManager_Reserved5` | TField |  |  |
| 19 | `FS.GA.FUND.MANAGER.RESERVED4` | `FsGaFundManager_Reserved4` | TField |  |  |
| 20 | `FS.GA.FUND.MANAGER.RESERVED3` | `FsGaFundManager_Reserved3` | TField |  |  |
| 21 | `FS.GA.FUND.MANAGER.RESERVED2` | `FsGaFundManager_Reserved2` | TField |  |  |
| 22 | `FS.GA.FUND.MANAGER.RESERVED1` | `FsGaFundManager_Reserved1` | TField |  |  |
| 23 | `FS.GA.FUND.MANAGER.LOCAL.REF` | `FsGaFundManager_LocalRef` |  |  |  |
| 24 | `FS.GA.FUND.MANAGER.OVERRIDE` | `FsGaFundManager_Override` |  |  |  |
| 25 | `FS.GA.FUND.MANAGER.RECORD.STATUS` | `FsGaFundManager_RecordStatus` | String |  |  |
| 26 | `FS.GA.FUND.MANAGER.CURR.NO` | `FsGaFundManager_CurrNo` | String |  |  |
| 27 | `FS.GA.FUND.MANAGER.INPUTTER` | `FsGaFundManager_Inputter` |  |  |  |
| 28 | `FS.GA.FUND.MANAGER.DATE.TIME` | `FsGaFundManager_DateTime` |  |  |  |
| 29 | `FS.GA.FUND.MANAGER.AUTHORISER` | `FsGaFundManager_Authoriser` | String |  |  |
| 30 | `FS.GA.FUND.MANAGER.CO.CODE` | `FsGaFundManager_CoCode` | String |  |  |
| 31 | `FS.GA.FUND.MANAGER.DEPT.CODE` | `FsGaFundManager_DeptCode` | String |  |  |
| 32 | `FS.GA.FUND.MANAGER.AUDITOR.CODE` | `FsGaFundManager_AuditorCode` | String |  |  |
| 33 | `FS.GA.FUND.MANAGER.AUDIT.DATE.TIME` | `FsGaFundManager_AuditDateTime` | String |  |  |
