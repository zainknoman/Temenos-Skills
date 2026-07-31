# FS.GA.CORP.ACTION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORP.ACTION.PARAMETER` in `FS_CorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORP.ACTION.PARAMETER.PARENT.REF.ID` | `FsGaCorpActionParameter_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORP.ACTION.PARAMETER.ORA.ROWID` | `FsGaCorpActionParameter_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORP.ACTION.PARAMETER.OPERATION.CODE` | `FsGaCorpActionParameter_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.CORP.ACTION.PARAMETER.OPTION.AND.FUTURES.SEC.TYPE` | `FsGaCorpActionParameter_OptionAndFuturesSecType` | TField |  | Option And Futures Security Type Multifonds DB Column is TYPE. |
| 5 | `FS.GA.CORP.ACTION.PARAMETER.UNIT.AMOUNT.CODE` | `FsGaCorpActionParameter_UnitAmountCode` | TField |  | Unit amount Code like Receive Pay for Corporate action Multifonds DB Column is COD_CASH. |
| 6 | `FS.GA.CORP.ACTION.PARAMETER.UNIT.AMOUNT.CA` | `FsGaCorpActionParameter_UnitAmountCa` | TField |  | Unit amount to Receive Pay for Corporate action Multifonds DB Column is MNT_PD. |
| 7 | `FS.GA.CORP.ACTION.PARAMETER.CLOSE.OLD.POSITION` | `FsGaCorpActionParameter_CloseOldPosition` | TField |  | Close Old position Identifier for CA Multifonds DB Column is CLOSE. |
| 8 | `FS.GA.CORP.ACTION.PARAMETER.QUANTITY.EXISTING.SECURITY.CA` | `FsGaCorpActionParameter_QuantityExistingSecurityCa` | TField |  | Qty of existing security CA to be exchanged from Multifonds DB Column is QTE_RIGHT_C1. |
| 9 | `FS.GA.CORP.ACTION.PARAMETER.QTY.EXISTING.OR.NEWSECURITY.CA` | `FsGaCorpActionParameter_QtyExistingOrNewsecurityCa` | TField |  | Qty of existing or new security CA to be exchanged to Multifonds DB Column is QTE_RIGHT_C2. |
| 10 | `FS.GA.CORP.ACTION.PARAMETER.CA.ADDITION.TYPE` | `FsGaCorpActionParameter_CaAdditionType` | TField |  | Type of CA addition like In addition , In replacement , Subtraction Multifonds DB Column is TYPE_C2. |
| 11 | `FS.GA.CORP.ACTION.PARAMETER.BOOK.VALUE.ADJ.TYPE.CA` | `FsGaCorpActionParameter_BookValueAdjTypeCa` | TField |  | Book Value Adjustment and other types like Stock divident, Split action Multifonds DB Column is COD_AJUST. |
| 12 | `FS.GA.CORP.ACTION.PARAMETER.BOOK.VALUE.CORRECTION.TYPE.CA` | `FsGaCorpActionParameter_BookValueCorrectionTypeCa` | TField |  | Correct book value by: Book Unit Amount , Ratio , Percentage Multifonds DB Column is COD_AJUST_CPTA. |
| 13 | `FS.GA.CORP.ACTION.PARAMETER.COST.EXCHANGE.RATE.CA` | `FsGaCorpActionParameter_CostExchangeRateCa` | TField |  | Use Cost exchange rate in Corporate action Multifonds DB Column is COST_TCHG. |
| 14 | `FS.GA.CORP.ACTION.PARAMETER.DROP.FRACTIONAL.SHARES.CA` | `FsGaCorpActionParameter_DropFractionalSharesCa` | TField |  | Drop Fractional shares in case of odd shares entitled in Corporate action Multifonds DB Column is FLG_DROP_FRC_SHRS. |
| 15 | `FS.GA.CORP.ACTION.PARAMETER.CASH.RECEIVED.ON.OLD.SECURITY` | `FsGaCorpActionParameter_CashReceivedOnOldSecurity` | TField |  | Cash Received on Old security for corporate action Multifonds DB Column is RECD_ON_OLD_SECURITY. |
| 16 | `FS.GA.CORP.ACTION.PARAMETER.TRADE.DATE.IDENTIFIER` | `FsGaCorpActionParameter_TradeDateIdentifier` | TField |  | if the trade calculation process is run after the trade cut off time, the trade will be calculated with a trade date of T+1 rather than taking no action Multifonds DB Column is FLG_DOPER. |
| 17 | `FS.GA.CORP.ACTION.PARAMETER.IFRS.DEFAULT.CATEGORY` | `FsGaCorpActionParameter_IfrsDefaultCategory` | TField |  | IFRS default category like AFS, HTM etc for the GTI and Security predefined Multifonds DB Column is FLG_DEFAULT. |
| 18 | `FS.GA.CORP.ACTION.PARAMETER.FLAG.COST.ADJUSTMENT.CA` | `FsGaCorpActionParameter_FlagCostAdjustmentCa` | TField |  | Flag Cost Adustment CA Multifonds DB Column is FLG_ROC_CA_TCHG. |
| 19 | `FS.GA.CORP.ACTION.PARAMETER.CORPORATE.ACTION.TYPE` | `FsGaCorpActionParameter_CorporateActionType` | TField |  | Corporate Action Type Multifonds DB Column is CA_TYPE. |
| 20 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED10` | `FsGaCorpActionParameter_Reserved10` | TField |  |  |
| 21 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED9` | `FsGaCorpActionParameter_Reserved9` | TField |  |  |
| 22 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED8` | `FsGaCorpActionParameter_Reserved8` | TField |  |  |
| 23 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED7` | `FsGaCorpActionParameter_Reserved7` | TField |  |  |
| 24 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED6` | `FsGaCorpActionParameter_Reserved6` | TField |  |  |
| 25 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED5` | `FsGaCorpActionParameter_Reserved5` | TField |  |  |
| 26 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED4` | `FsGaCorpActionParameter_Reserved4` | TField |  |  |
| 27 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED3` | `FsGaCorpActionParameter_Reserved3` | TField |  |  |
| 28 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED2` | `FsGaCorpActionParameter_Reserved2` | TField |  |  |
| 29 | `FS.GA.CORP.ACTION.PARAMETER.RESERVED1` | `FsGaCorpActionParameter_Reserved1` | TField |  |  |
| 30 | `FS.GA.CORP.ACTION.PARAMETER.LOCAL.REF` | `FsGaCorpActionParameter_LocalRef` |  |  |  |
| 31 | `FS.GA.CORP.ACTION.PARAMETER.OVERRIDE` | `FsGaCorpActionParameter_Override` |  |  |  |
| 32 | `FS.GA.CORP.ACTION.PARAMETER.RECORD.STATUS` | `FsGaCorpActionParameter_RecordStatus` | String |  |  |
| 33 | `FS.GA.CORP.ACTION.PARAMETER.CURR.NO` | `FsGaCorpActionParameter_CurrNo` | String |  |  |
| 34 | `FS.GA.CORP.ACTION.PARAMETER.INPUTTER` | `FsGaCorpActionParameter_Inputter` |  |  |  |
| 35 | `FS.GA.CORP.ACTION.PARAMETER.DATE.TIME` | `FsGaCorpActionParameter_DateTime` |  |  |  |
| 36 | `FS.GA.CORP.ACTION.PARAMETER.AUTHORISER` | `FsGaCorpActionParameter_Authoriser` | String |  |  |
| 37 | `FS.GA.CORP.ACTION.PARAMETER.CO.CODE` | `FsGaCorpActionParameter_CoCode` | String |  |  |
| 38 | `FS.GA.CORP.ACTION.PARAMETER.DEPT.CODE` | `FsGaCorpActionParameter_DeptCode` | String |  |  |
| 39 | `FS.GA.CORP.ACTION.PARAMETER.AUDITOR.CODE` | `FsGaCorpActionParameter_AuditorCode` | String |  |  |
| 40 | `FS.GA.CORP.ACTION.PARAMETER.AUDIT.DATE.TIME` | `FsGaCorpActionParameter_AuditDateTime` | String |  |  |
