# FS.GA.STOCK.EXCHANGE.SCALE — Table Schema

> Source: `INSERTS/I_F.FS.GA.STOCK.EXCHANGE.SCALE` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.STOCK.EXCHANGE.SCALE.LOCAL.CURRENCY` | `FsGaStockExchangeScale_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 2 | `GA.STOCK.EXCHANGE.SCALE.OPERATION.CODE` | `FsGaStockExchangeScale_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 3 | `GA.STOCK.EXCHANGE.SCALE.FEE.CODE` | `FsGaStockExchangeScale_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 4 | `GA.STOCK.EXCHANGE.SCALE.HIGHEST` | `FsGaStockExchangeScale_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 5 | `GA.STOCK.EXCHANGE.SCALE.FEES.RATE` | `FsGaStockExchangeScale_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 6 | `GA.STOCK.EXCHANGE.SCALE.AMOUNT.IN.SECURITY.CURRENCY` | `FsGaStockExchangeScale_AmountInSecurityCurrency` | TField |  | Amount in deal currency Multifonds DB Column is AMOUNT. |
| 7 | `GA.STOCK.EXCHANGE.SCALE.FUND.ID` | `FsGaStockExchangeScale_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 8 | `GA.STOCK.EXCHANGE.SCALE.CORRESPONDENT` | `FsGaStockExchangeScale_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 9 | `GA.STOCK.EXCHANGE.SCALE.COUNTERPARTY.CORRESPONDENT` | `FsGaStockExchangeScale_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 10 | `GA.STOCK.EXCHANGE.SCALE.INSTRUMENT.CODE` | `FsGaStockExchangeScale_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 11 | `GA.STOCK.EXCHANGE.SCALE.REPO.TYPE.CODE` | `FsGaStockExchangeScale_RepoTypeCode` | TField |  | The field which links to deal. The list of values is available through F9 in which draws the repo type code from the new repo type definition. Multifonds DB Column is REPO_ID. |
| 12 | `GA.STOCK.EXCHANGE.SCALE.QUOTATION.PLACE` | `FsGaStockExchangeScale_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 13 | `GA.STOCK.EXCHANGE.SCALE.ISSUE.COUNTRY` | `FsGaStockExchangeScale_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 14 | `GA.STOCK.EXCHANGE.SCALE.GTI.CODE` | `FsGaStockExchangeScale_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 15 | `GA.STOCK.EXCHANGE.SCALE.RESERVED10` | `FsGaStockExchangeScale_Reserved10` | TField |  |  |
| 16 | `GA.STOCK.EXCHANGE.SCALE.RESERVED9` | `FsGaStockExchangeScale_Reserved9` | TField |  |  |
| 17 | `GA.STOCK.EXCHANGE.SCALE.RESERVED8` | `FsGaStockExchangeScale_Reserved8` | TField |  |  |
| 18 | `GA.STOCK.EXCHANGE.SCALE.RESERVED7` | `FsGaStockExchangeScale_Reserved7` | TField |  |  |
| 19 | `GA.STOCK.EXCHANGE.SCALE.RESERVED6` | `FsGaStockExchangeScale_Reserved6` | TField |  |  |
| 20 | `GA.STOCK.EXCHANGE.SCALE.RESERVED5` | `FsGaStockExchangeScale_Reserved5` | TField |  |  |
| 21 | `GA.STOCK.EXCHANGE.SCALE.RESERVED4` | `FsGaStockExchangeScale_Reserved4` | TField |  |  |
| 22 | `GA.STOCK.EXCHANGE.SCALE.RESERVED3` | `FsGaStockExchangeScale_Reserved3` | TField |  |  |
| 23 | `GA.STOCK.EXCHANGE.SCALE.RESERVED2` | `FsGaStockExchangeScale_Reserved2` | TField |  |  |
| 24 | `GA.STOCK.EXCHANGE.SCALE.RESERVED1` | `FsGaStockExchangeScale_Reserved1` | TField |  |  |
| 25 | `GA.STOCK.EXCHANGE.SCALE.LOCAL.REF` | `FsGaStockExchangeScale_LocalRef` |  |  |  |
| 26 | `GA.STOCK.EXCHANGE.SCALE.OVERRIDE` | `FsGaStockExchangeScale_Override` |  |  |  |
| 27 | `GA.STOCK.EXCHANGE.SCALE.RECORD.STATUS` | `FsGaStockExchangeScale_RecordStatus` | String |  |  |
| 28 | `GA.STOCK.EXCHANGE.SCALE.CURR.NO` | `FsGaStockExchangeScale_CurrNo` | String |  |  |
| 29 | `GA.STOCK.EXCHANGE.SCALE.INPUTTER` | `FsGaStockExchangeScale_Inputter` |  |  |  |
| 30 | `GA.STOCK.EXCHANGE.SCALE.DATE.TIME` | `FsGaStockExchangeScale_DateTime` |  |  |  |
| 31 | `GA.STOCK.EXCHANGE.SCALE.AUTHORISER` | `FsGaStockExchangeScale_Authoriser` | String |  |  |
| 32 | `GA.STOCK.EXCHANGE.SCALE.CO.CODE` | `FsGaStockExchangeScale_CoCode` | String |  |  |
| 33 | `GA.STOCK.EXCHANGE.SCALE.DEPT.CODE` | `FsGaStockExchangeScale_DeptCode` | String |  |  |
| 34 | `GA.STOCK.EXCHANGE.SCALE.AUDITOR.CODE` | `FsGaStockExchangeScale_AuditorCode` | String |  |  |
| 35 | `GA.STOCK.EXCHANGE.SCALE.AUDIT.DATE.TIME` | `FsGaStockExchangeScale_AuditDateTime` | String |  |  |
