# FS.GI.TXN.ADL.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ADL.DETAILS` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ADL.DETAILS.PARENT.REF.ID` | `FsGiTxnAdlDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ADL.DETAILS.ORA.ROWID` | `FsGiTxnAdlDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ADL.DETAILS.EXCHANGE.GROUP` | `FsGiTxnAdlDetails_ExchangeGroup` | TField |  | Exchange group for which ADL is applicable. Multifonds DB Column is CGROUPE_COURS. |
| 4 | `FS.GI.TXN.ADL.DETAILS.FUND.ID` | `FsGiTxnAdlDetails_FundId` | TField |  | Master Fund ID linked to the order. Multifonds DB Column is MULTIFONDS_ID. |
| 5 | `FS.GI.TXN.ADL.DETAILS.CALC.DATE` | `FsGiTxnAdlDetails_CalcDate` | TField |  | Date on which ADL is calculated. Multifonds DB Column is DATE_CAL. |
| 6 | `FS.GI.TXN.ADL.DETAILS.ORDER.ID` | `FsGiTxnAdlDetails_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 7 | `FS.GI.TXN.ADL.DETAILS.DEAL.REFERENCE` | `FsGiTxnAdlDetails_DealReference` | TField |  | Unique Deal Reference. Multifonds DB Column is DEAL_REF. |
| 8 | `FS.GI.TXN.ADL.DETAILS.AGENT.ID` | `FsGiTxnAdlDetails_AgentId` | TField |  | Agent ID linked to the order. Multifonds DB Column is NOUTLET. |
| 9 | `FS.GI.TXN.ADL.DETAILS.REGISTER.ID` | `FsGiTxnAdlDetails_RegisterId` | TField |  | Register ID linked to the order. Multifonds DB Column is NREGISTER. |
| 10 | `FS.GI.TXN.ADL.DETAILS.TA.FUND.ID` | `FsGiTxnAdlDetails_TaFundId` | TField |  | TA Fund ID linked to the order. Multifonds DB Column is NPTF. |
| 11 | `FS.GI.TXN.ADL.DETAILS.SHARE.CLASS.CODE` | `FsGiTxnAdlDetails_ShareClassCode` | TField |  | Share class code linked to the fund. Multifonds DB Column is TPART. |
| 12 | `FS.GI.TXN.ADL.DETAILS.OPERATION.CODE` | `FsGiTxnAdlDetails_OperationCode` | TField |  | The operation code for which ADL is applicable. Multifonds DB Column is COPERATION. |
| 13 | `FS.GI.TXN.ADL.DETAILS.TA.FUND.CURRENCY` | `FsGiTxnAdlDetails_TaFundCurrency` | TField |  | TA Fund and shareclass currency (in 3 letter format eg. &apos;EUR&apos;). Multifonds DB Column is CMON_PTF. |
| 14 | `FS.GI.TXN.ADL.DETAILS.ORDER.TRADE.DATE` | `FsGiTxnAdlDetails_OrderTradeDate` | TField |  | Trade date of the order. Multifonds DB Column is DATE_EXE. |
| 15 | `FS.GI.TXN.ADL.DETAILS.AMOUNT` | `FsGiTxnAdlDetails_Amount` | TField |  | Order amount. Multifonds DB Column is AMOUNT. |
| 16 | `FS.GI.TXN.ADL.DETAILS.PAYMENT.CURRENCY` | `FsGiTxnAdlDetails_PaymentCurrency` | TField |  | Payment settlement currency (in 3 letter format eg. &apos;EUR&apos;). Multifonds DB Column is CMON_PAY. |
| 17 | `FS.GI.TXN.ADL.DETAILS.QUANTITY` | `FsGiTxnAdlDetails_Quantity` | TField |  | Order quantity. Multifonds DB Column is QUANTITY. |
| 18 | `FS.GI.TXN.ADL.DETAILS.CASH.EXCESS` | `FsGiTxnAdlDetails_CashExcess` | TField |  | Excess cash for the orders after the calculation has been performed by the system. Multifonds DB Column is CASH_EXCESS. |
| 19 | `FS.GI.TXN.ADL.DETAILS.ADL.DEFAULT.RATE` | `FsGiTxnAdlDetails_AdlDefaultRate` | TField |  | Anti Dilution Levy (ADL) rate applicable for the order. Multifonds DB Column is ADL_RATE. |
| 20 | `FS.GI.TXN.ADL.DETAILS.ADL.AMOUNT` | `FsGiTxnAdlDetails_AdlAmount` | TField |  | Anti Dilution Levy (ADL) amount for the order. Multifonds DB Column is ADL_AMOUNT. |
| 21 | `FS.GI.TXN.ADL.DETAILS.LEG.LINK` | `FsGiTxnAdlDetails_LegLink` | TField |  | Leg link for switch / transfer orders; automatically populated. Multifonds DB Column is LEG_LINK. |
| 22 | `FS.GI.TXN.ADL.DETAILS.ADL.AMOUNT.PAY.CCY` | `FsGiTxnAdlDetails_AdlAmountPayCcy` | TField |  | Anti Dilution Levy (ADL) Amount pay for the order. Multifonds DB Column is ADL_AMOUNT_PAY. |
| 23 | `FS.GI.TXN.ADL.DETAILS.SWUNG.NAV` | `FsGiTxnAdlDetails_SwungNav` | TField |  | Swung unit price. Multifonds DB Column is MNT_UNIT_SWUNG. |
| 24 | `FS.GI.TXN.ADL.DETAILS.SWUNG.PRICE.TYPE` | `FsGiTxnAdlDetails_SwungPriceType` | TField |  | Swung unit price type. Multifonds DB Column is SWUNG_TYPE. |
| 25 | `FS.GI.TXN.ADL.DETAILS.NAV.PRICE` | `FsGiTxnAdlDetails_NavPrice` | TField |  | Unit price for the order. Multifonds DB Column is UNIT_PRICE. |
| 26 | `FS.GI.TXN.ADL.DETAILS.FORCED.ADL.FLAG` | `FsGiTxnAdlDetails_ForcedAdlFlag` | TField |  | Flag to indicate ADL is forced. Multifonds DB Column is FLG_FORCE. |
| 27 | `FS.GI.TXN.ADL.DETAILS.FORCED.RECALC.ADL.FLAG` | `FsGiTxnAdlDetails_ForcedRecalcAdlFlag` | TField |  | Flag indicating whether the ADL has been recalculated after receiving the NAV and before batch process. Multifonds DB Column is FLG_RECALC_ADL. |
| 28 | `FS.GI.TXN.ADL.DETAILS.RESERVED10` | `FsGiTxnAdlDetails_Reserved10` | TField |  |  |
| 29 | `FS.GI.TXN.ADL.DETAILS.RESERVED9` | `FsGiTxnAdlDetails_Reserved9` | TField |  |  |
| 30 | `FS.GI.TXN.ADL.DETAILS.RESERVED8` | `FsGiTxnAdlDetails_Reserved8` | TField |  |  |
| 31 | `FS.GI.TXN.ADL.DETAILS.RESERVED7` | `FsGiTxnAdlDetails_Reserved7` | TField |  |  |
| 32 | `FS.GI.TXN.ADL.DETAILS.RESERVED6` | `FsGiTxnAdlDetails_Reserved6` | TField |  |  |
| 33 | `FS.GI.TXN.ADL.DETAILS.RESERVED5` | `FsGiTxnAdlDetails_Reserved5` | TField |  |  |
| 34 | `FS.GI.TXN.ADL.DETAILS.RESERVED4` | `FsGiTxnAdlDetails_Reserved4` | TField |  |  |
| 35 | `FS.GI.TXN.ADL.DETAILS.RESERVED3` | `FsGiTxnAdlDetails_Reserved3` | TField |  |  |
| 36 | `FS.GI.TXN.ADL.DETAILS.RESERVED2` | `FsGiTxnAdlDetails_Reserved2` | TField |  |  |
| 37 | `FS.GI.TXN.ADL.DETAILS.RESERVED1` | `FsGiTxnAdlDetails_Reserved1` | TField |  |  |
| 38 | `FS.GI.TXN.ADL.DETAILS.LOCAL.REF` | `FsGiTxnAdlDetails_LocalRef` |  |  |  |
| 39 | `FS.GI.TXN.ADL.DETAILS.OVERRIDE` | `FsGiTxnAdlDetails_Override` |  |  |  |
| 40 | `FS.GI.TXN.ADL.DETAILS.RECORD.STATUS` | `FsGiTxnAdlDetails_RecordStatus` | String |  |  |
| 41 | `FS.GI.TXN.ADL.DETAILS.CURR.NO` | `FsGiTxnAdlDetails_CurrNo` | String |  |  |
| 42 | `FS.GI.TXN.ADL.DETAILS.INPUTTER` | `FsGiTxnAdlDetails_Inputter` |  |  |  |
| 43 | `FS.GI.TXN.ADL.DETAILS.DATE.TIME` | `FsGiTxnAdlDetails_DateTime` |  |  |  |
| 44 | `FS.GI.TXN.ADL.DETAILS.AUTHORISER` | `FsGiTxnAdlDetails_Authoriser` | String |  |  |
| 45 | `FS.GI.TXN.ADL.DETAILS.CO.CODE` | `FsGiTxnAdlDetails_CoCode` | String |  |  |
| 46 | `FS.GI.TXN.ADL.DETAILS.DEPT.CODE` | `FsGiTxnAdlDetails_DeptCode` | String |  |  |
| 47 | `FS.GI.TXN.ADL.DETAILS.AUDITOR.CODE` | `FsGiTxnAdlDetails_AuditorCode` | String |  |  |
| 48 | `FS.GI.TXN.ADL.DETAILS.AUDIT.DATE.TIME` | `FsGiTxnAdlDetails_AuditDateTime` | String |  |  |
