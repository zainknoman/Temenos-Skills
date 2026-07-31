# FS.GA.INTEREST.RATE.TYPE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.INTEREST.RATE.TYPE.DEFINITION` in `FS_IncomeCorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.LOCAL.CURRENCY` | `FsGaInterestRateTypeDefinition_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 2 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.INTEREST.RATE.TYPE` | `FsGaInterestRateTypeDefinition_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 3 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.SETTLE.DATE` | `FsGaInterestRateTypeDefinition_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 4 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.TRADE.DATE` | `FsGaInterestRateTypeDefinition_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 5 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.ACCOUNTING.DATE` | `FsGaInterestRateTypeDefinition_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 6 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.LIABILITIES.INTEREST.RATE` | `FsGaInterestRateTypeDefinition_LiabilitiesInterestRate` | TField |  | Interest rate to be used for the payment side of the forward exchange contract. Multifonds DB Column is TAUX_CR. |
| 7 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.ASSETS.INTEREST.RATE` | `FsGaInterestRateTypeDefinition_AssetsInterestRate` | TField |  | Interest rate to be used for the delivery side of the forward exchange contract. Multifonds DB Column is TAUX_DB. |
| 8 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED10` | `FsGaInterestRateTypeDefinition_Reserved10` | TField |  |  |
| 9 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED9` | `FsGaInterestRateTypeDefinition_Reserved9` | TField |  |  |
| 10 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED8` | `FsGaInterestRateTypeDefinition_Reserved8` | TField |  |  |
| 11 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED7` | `FsGaInterestRateTypeDefinition_Reserved7` | TField |  |  |
| 12 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED6` | `FsGaInterestRateTypeDefinition_Reserved6` | TField |  |  |
| 13 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED5` | `FsGaInterestRateTypeDefinition_Reserved5` | TField |  |  |
| 14 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED4` | `FsGaInterestRateTypeDefinition_Reserved4` | TField |  |  |
| 15 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED3` | `FsGaInterestRateTypeDefinition_Reserved3` | TField |  |  |
| 16 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED2` | `FsGaInterestRateTypeDefinition_Reserved2` | TField |  |  |
| 17 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RESERVED1` | `FsGaInterestRateTypeDefinition_Reserved1` | TField |  |  |
| 18 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.RECORD.STATUS` | `FsGaInterestRateTypeDefinition_RecordStatus` | String |  |  |
| 19 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.CURR.NO` | `FsGaInterestRateTypeDefinition_CurrNo` | String |  |  |
| 20 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.INPUTTER` | `FsGaInterestRateTypeDefinition_Inputter` |  |  |  |
| 21 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.DATE.TIME` | `FsGaInterestRateTypeDefinition_DateTime` |  |  |  |
| 22 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.AUTHORISER` | `FsGaInterestRateTypeDefinition_Authoriser` | String |  |  |
| 23 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.CO.CODE` | `FsGaInterestRateTypeDefinition_CoCode` | String |  |  |
| 24 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.DEPT.CODE` | `FsGaInterestRateTypeDefinition_DeptCode` | String |  |  |
| 25 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.AUDITOR.CODE` | `FsGaInterestRateTypeDefinition_AuditorCode` | String |  |  |
| 26 | `FS.GA.INTEREST.RATE.TYPE.DEFINITION.AUDIT.DATE.TIME` | `FsGaInterestRateTypeDefinition_AuditDateTime` | String |  |  |
