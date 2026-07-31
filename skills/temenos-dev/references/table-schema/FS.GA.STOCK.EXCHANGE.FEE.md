# FS.GA.STOCK.EXCHANGE.FEE — Table Schema

> Source: `INSERTS/I_F.FS.GA.STOCK.EXCHANGE.FEE` in `FS_Fee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STOCK.EXCHANGE.FEE.PARENT.REF.ID` | `FsGaStockExchangeFee_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STOCK.EXCHANGE.FEE.ORA.ROWID` | `FsGaStockExchangeFee_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STOCK.EXCHANGE.FEE.LOCAL.CURRENCY` | `FsGaStockExchangeFee_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 4 | `FS.GA.STOCK.EXCHANGE.FEE.OPERATION.CODE` | `FsGaStockExchangeFee_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 5 | `FS.GA.STOCK.EXCHANGE.FEE.FEE.CODE` | `FsGaStockExchangeFee_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 6 | `FS.GA.STOCK.EXCHANGE.FEE.FEES.RATE` | `FsGaStockExchangeFee_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 7 | `FS.GA.STOCK.EXCHANGE.FEE.LOWEST` | `FsGaStockExchangeFee_Lowest` | TField |  | Enter the minimum scale amount Multifonds DB Column is MNT_MIN. |
| 8 | `FS.GA.STOCK.EXCHANGE.FEE.HIGHEST` | `FsGaStockExchangeFee_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 9 | `FS.GA.STOCK.EXCHANGE.FEE.MINIMUM` | `FsGaStockExchangeFee_Minimum` | TField |  | Enter the minimum fee amount to be charged. The minimum will apply if the amount calculated on the basis of the scales does not reach such minimum Multifonds DB Column is COM_MIN. |
| 10 | `FS.GA.STOCK.EXCHANGE.FEE.MAXIMUM` | `FsGaStockExchangeFee_Maximum` | TField |  | Enter the maximum fee to be charged. The maximum will apply if the amount calculated on the basis of the scales exceeds such maximum Multifonds DB Column is COM_MAX. |
| 11 | `FS.GA.STOCK.EXCHANGE.FEE.FUND.ID` | `FsGaStockExchangeFee_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 12 | `FS.GA.STOCK.EXCHANGE.FEE.CORRESPONDENT` | `FsGaStockExchangeFee_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 13 | `FS.GA.STOCK.EXCHANGE.FEE.SETTLEMENT.CCY` | `FsGaStockExchangeFee_SettlementCcy` | TField |  | Relates to the settlement currency of the transaction Multifonds DB Column is CMON_SETTLE. |
| 14 | `FS.GA.STOCK.EXCHANGE.FEE.BROKER` | `FsGaStockExchangeFee_Broker` | TField |  | Broker Multifonds DB Column is FLG_BROKER. |
| 15 | `FS.GA.STOCK.EXCHANGE.FEE.CAPITALIZE.FEE` | `FsGaStockExchangeFee_CapitalizeFee` | TField |  | If set, means that the fees amount calculated will be incorporated in securities book cost Multifonds DB Column is FLG_CAPITALISE. |
| 16 | `FS.GA.STOCK.EXCHANGE.FEE.ISSUE.COUNTRY` | `FsGaStockExchangeFee_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 17 | `FS.GA.STOCK.EXCHANGE.FEE.GTI.CODE` | `FsGaStockExchangeFee_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 18 | `FS.GA.STOCK.EXCHANGE.FEE.FEE.SETTLE` | `FsGaStockExchangeFee_FeeSettle` | TField |  | If set, the fees will be booked on a different payable account (Op. code 106) instead of being included in the transaction net amount. Multifonds DB Column is FLG_FEES_SETTLE. |
| 19 | `FS.GA.STOCK.EXCHANGE.FEE.INTERFACE.DEF.FEE` | `FsGaStockExchangeFee_InterfaceDefFee` | TField |  | If set, then this fee will be applied by default on interfaced transactions on this fund. Even if the interface file contains this fee, the system would consider the fees flagged here. Multifonds DB Column is FLG_INTF_DEF_FEES. |
| 20 | `FS.GA.STOCK.EXCHANGE.FEE.SETTLEMENT.CCY.IDENTIFIER` | `FsGaStockExchangeFee_SettlementCcyIdentifier` | TField |  | If set, then it is possible to have the fees in a different ccy than the settlement ccy. For this of course the fees must be defined as type 3 (fees amount) in FDCOM01 Multifonds DB Column is FLG_SETTLE_CCY. |
| 21 | `FS.GA.STOCK.EXCHANGE.FEE.INSTRUMENT.CODE` | `FsGaStockExchangeFee_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 22 | `FS.GA.STOCK.EXCHANGE.FEE.COUNTERPARTY.CORRESPONDENT` | `FsGaStockExchangeFee_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 23 | `FS.GA.STOCK.EXCHANGE.FEE.QUOTATION.PLACE` | `FsGaStockExchangeFee_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 24 | `FS.GA.STOCK.EXCHANGE.FEE.REPO.TYPE.CODE` | `FsGaStockExchangeFee_RepoTypeCode` | TField |  | The field which links to deal screen FDDEP01 and FDEMP02. The list of values is available through F9 in FDCBO01 screen which draws the repo type code from the new repo type definition screen FDRPO01. Multifonds DB Column is REPO_ID. |
| 25 | `FS.GA.STOCK.EXCHANGE.FEE.IFRS.CATEGORY` | `FsGaStockExchangeFee_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 26 | `FS.GA.STOCK.EXCHANGE.FEE.DELAY.DAYS` | `FsGaStockExchangeFee_DelayDays` | TField |  | Delay days to be applied on coupon/ paydown transactions to trigger payment Multifonds DB Column is DELAY_DAYS. |
| 27 | `FS.GA.STOCK.EXCHANGE.FEE.BUSINESS.DAY` | `FsGaStockExchangeFee_BusinessDay` | TField |  | Allows the settling of broker fees either on a calendar day or a business day Multifonds DB Column is BUS_DAY. |
| 28 | `FS.GA.STOCK.EXCHANGE.FEE.SEC.TRANSACTION.TAX.INDICATOR` | `FsGaStockExchangeFee_SecTransactionTaxIndicator` | TField |  | Indicator whether a transaction has been subject to security transaction tax for CGT computation. Multifonds DB Column is CGT_IND_STT_FLG. |
| 29 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED10` | `FsGaStockExchangeFee_Reserved10` | TField |  |  |
| 30 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED9` | `FsGaStockExchangeFee_Reserved9` | TField |  |  |
| 31 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED8` | `FsGaStockExchangeFee_Reserved8` | TField |  |  |
| 32 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED7` | `FsGaStockExchangeFee_Reserved7` | TField |  |  |
| 33 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED6` | `FsGaStockExchangeFee_Reserved6` | TField |  |  |
| 34 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED5` | `FsGaStockExchangeFee_Reserved5` | TField |  |  |
| 35 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED4` | `FsGaStockExchangeFee_Reserved4` | TField |  |  |
| 36 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED3` | `FsGaStockExchangeFee_Reserved3` | TField |  |  |
| 37 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED2` | `FsGaStockExchangeFee_Reserved2` | TField |  |  |
| 38 | `FS.GA.STOCK.EXCHANGE.FEE.RESERVED1` | `FsGaStockExchangeFee_Reserved1` | TField |  |  |
| 39 | `FS.GA.STOCK.EXCHANGE.FEE.LOCAL.REF` | `FsGaStockExchangeFee_LocalRef` |  |  |  |
| 40 | `FS.GA.STOCK.EXCHANGE.FEE.OVERRIDE` | `FsGaStockExchangeFee_Override` |  |  |  |
| 41 | `FS.GA.STOCK.EXCHANGE.FEE.RECORD.STATUS` | `FsGaStockExchangeFee_RecordStatus` | String |  |  |
| 42 | `FS.GA.STOCK.EXCHANGE.FEE.CURR.NO` | `FsGaStockExchangeFee_CurrNo` | String |  |  |
| 43 | `FS.GA.STOCK.EXCHANGE.FEE.INPUTTER` | `FsGaStockExchangeFee_Inputter` |  |  |  |
| 44 | `FS.GA.STOCK.EXCHANGE.FEE.DATE.TIME` | `FsGaStockExchangeFee_DateTime` |  |  |  |
| 45 | `FS.GA.STOCK.EXCHANGE.FEE.AUTHORISER` | `FsGaStockExchangeFee_Authoriser` | String |  |  |
| 46 | `FS.GA.STOCK.EXCHANGE.FEE.CO.CODE` | `FsGaStockExchangeFee_CoCode` | String |  |  |
| 47 | `FS.GA.STOCK.EXCHANGE.FEE.DEPT.CODE` | `FsGaStockExchangeFee_DeptCode` | String |  |  |
| 48 | `FS.GA.STOCK.EXCHANGE.FEE.AUDITOR.CODE` | `FsGaStockExchangeFee_AuditorCode` | String |  |  |
| 49 | `FS.GA.STOCK.EXCHANGE.FEE.AUDIT.DATE.TIME` | `FsGaStockExchangeFee_AuditDateTime` | String |  |  |
