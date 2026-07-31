# FS.GI.APP.INVESTMENT.LIMIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.INVESTMENT.LIMIT` in `FS_InvestmentRestrictions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.INVESTMENT.LIMIT.PARENT.REF.ID` | `FsGiAppInvestmentLimit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.INVESTMENT.LIMIT.ORA.ROWID` | `FsGiAppInvestmentLimit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.INVESTMENT.LIMIT.PARENT.TYPE` | `FsGiAppInvestmentLimit_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.INVESTMENT.LIMIT.PARENT.TYPE.ID` | `FsGiAppInvestmentLimit_ParentTypeId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.INVESTMENT.LIMIT.OPERATION.CODE` | `FsGiAppInvestmentLimit_OperationCode` | TField |  | The operation code for which the investment limit check is applicable. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.APP.INVESTMENT.LIMIT.TA.FUND.ID` | `FsGiAppInvestmentLimit_TaFundId` | TField |  | Fund linked to the investment limit check. Multifonds DB Column is NPTF. |
| 7 | `FS.GI.APP.INVESTMENT.LIMIT.LEGAL.ENTITY.ID` | `FsGiAppInvestmentLimit_LegalEntityId` | TField |  | Legal entity linked to the investment limit check. Multifonds DB Column is NTFC. |
| 8 | `FS.GI.APP.INVESTMENT.LIMIT.SHARE.CLASS.CODE` | `FsGiAppInvestmentLimit_ShareClassCode` | TField |  | Fund share class linked to the investment limit check. Multifonds DB Column is TPART. |
| 9 | `FS.GI.APP.INVESTMENT.LIMIT.PAYMENT.CURRENCY` | `FsGiAppInvestmentLimit_PaymentCurrency` | TField |  | The currency (in 3 letter format eg: EUR) of the investment limit check. Multifonds DB Column is CMON. |
| 10 | `FS.GI.APP.INVESTMENT.LIMIT.MINIMUM.LIMIT` | `FsGiAppInvestmentLimit_MinimumLimit` | TField |  | The minimum transaction limit check that will be performed at order level for a fund share class. Multifonds DB Column is NMIN_LIMIT. |
| 11 | `FS.GI.APP.INVESTMENT.LIMIT.MAXIMUM.LIMIT` | `FsGiAppInvestmentLimit_MaximumLimit` | TField |  | The maximum transaction limit check that will be performed at order level for a fund share class. Multifonds DB Column is NMAX_LIMIT. |
| 12 | `FS.GI.APP.INVESTMENT.LIMIT.MINIMUM.BATCH.LIMIT` | `FsGiAppInvestmentLimit_MinimumBatchLimit` | TField |  | The minimum transaction limit check that will be performed at batch process level for a fund share class. Multifonds DB Column is NBATCH_LIMIT. |
| 13 | `FS.GI.APP.INVESTMENT.LIMIT.FIRST.SUBSCRIPTION.FLAG` | `FsGiAppInvestmentLimit_FirstSubscriptionFlag` | TField |  | Its an internal technical flag to indicate the transaction limits defined for the fund share class first subscription functionality. Multifonds DB Column is FLG_FIRST_SUB. |
| 14 | `FS.GI.APP.INVESTMENT.LIMIT.FIRST.TRANSACTION.FLAG` | `FsGiAppInvestmentLimit_FirstTransactionFlag` | TField |  | Its an internal technical flag to indicate the transaction limits defined for the fund share class first transaction limit functionality. Multifonds DB Column is FLG_FIRST_TRANS. |
| 15 | `FS.GI.APP.INVESTMENT.LIMIT.INVESTMENT.LIMIT.ID` | `FsGiAppInvestmentLimit_InvestmentLimitId` | TField |  | Unique internal investment limit identifier. Multifonds DB Column is INTERNAL_ID. |
| 16 | `FS.GI.APP.INVESTMENT.LIMIT.FUND.ID` | `FsGiAppInvestmentLimit_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 17 | `FS.GI.APP.INVESTMENT.LIMIT.CLASS.CURRENCY` | `FsGiAppInvestmentLimit_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 18 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED10` | `FsGiAppInvestmentLimit_Reserved10` | TField |  |  |
| 19 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED9` | `FsGiAppInvestmentLimit_Reserved9` | TField |  |  |
| 20 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED8` | `FsGiAppInvestmentLimit_Reserved8` | TField |  |  |
| 21 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED7` | `FsGiAppInvestmentLimit_Reserved7` | TField |  |  |
| 22 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED6` | `FsGiAppInvestmentLimit_Reserved6` | TField |  |  |
| 23 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED5` | `FsGiAppInvestmentLimit_Reserved5` | TField |  |  |
| 24 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED4` | `FsGiAppInvestmentLimit_Reserved4` | TField |  |  |
| 25 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED3` | `FsGiAppInvestmentLimit_Reserved3` | TField |  |  |
| 26 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED2` | `FsGiAppInvestmentLimit_Reserved2` | TField |  |  |
| 27 | `FS.GI.APP.INVESTMENT.LIMIT.RESERVED1` | `FsGiAppInvestmentLimit_Reserved1` | TField |  |  |
| 28 | `FS.GI.APP.INVESTMENT.LIMIT.LOCAL.REF` | `FsGiAppInvestmentLimit_LocalRef` |  |  |  |
| 29 | `FS.GI.APP.INVESTMENT.LIMIT.OVERRIDE` | `FsGiAppInvestmentLimit_Override` |  |  |  |
| 30 | `FS.GI.APP.INVESTMENT.LIMIT.RECORD.STATUS` | `FsGiAppInvestmentLimit_RecordStatus` | String |  |  |
| 31 | `FS.GI.APP.INVESTMENT.LIMIT.CURR.NO` | `FsGiAppInvestmentLimit_CurrNo` | String |  |  |
| 32 | `FS.GI.APP.INVESTMENT.LIMIT.INPUTTER` | `FsGiAppInvestmentLimit_Inputter` |  |  |  |
| 33 | `FS.GI.APP.INVESTMENT.LIMIT.DATE.TIME` | `FsGiAppInvestmentLimit_DateTime` |  |  |  |
| 34 | `FS.GI.APP.INVESTMENT.LIMIT.AUTHORISER` | `FsGiAppInvestmentLimit_Authoriser` | String |  |  |
| 35 | `FS.GI.APP.INVESTMENT.LIMIT.CO.CODE` | `FsGiAppInvestmentLimit_CoCode` | String |  |  |
| 36 | `FS.GI.APP.INVESTMENT.LIMIT.DEPT.CODE` | `FsGiAppInvestmentLimit_DeptCode` | String |  |  |
| 37 | `FS.GI.APP.INVESTMENT.LIMIT.AUDITOR.CODE` | `FsGiAppInvestmentLimit_AuditorCode` | String |  |  |
| 38 | `FS.GI.APP.INVESTMENT.LIMIT.AUDIT.DATE.TIME` | `FsGiAppInvestmentLimit_AuditDateTime` | String |  |  |
