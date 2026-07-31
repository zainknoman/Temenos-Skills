# FS.GA.BALANCESHEET — Table Schema

> Source: `INSERTS/I_F.FS.GA.BALANCESHEET` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BALANCESHEET.INVENTORY.STATE` | `FsGaBalancesheet_InventoryState` | TField |  | Inventory State Multifonds DB Column is INVENTORYSTATE. |
| 2 | `BALANCESHEET.MARKTOMARKET.ID` | `FsGaBalancesheet_MarktomarketId` | TField |  | MarkToMarket Id Multifonds DB Column is BALANCESHEETID. |
| 3 | `BALANCESHEET.LOT.ID` | `FsGaBalancesheet_LotId` | TField |  | lot id Multifonds DB Column is LOTID. |
| 4 | `BALANCESHEET.QUANTITY.AT.EXECUTION.DATE` | `FsGaBalancesheet_QuantityAtExecutionDate` | TField |  | Quantity at execution date Multifonds DB Column is QUANTITY. |
| 5 | `BALANCESHEET.LOCAL.AMOUNT` | `FsGaBalancesheet_LocalAmount` | TField |  | Local Amount Multifonds DB Column is LOCALAMOUNT. |
| 6 | `BALANCESHEET.BOOK.AMOUNT` | `FsGaBalancesheet_BookAmount` | TField |  | Book Amount Multifonds DB Column is BOOKAMOUNT. |
| 7 | `BALANCESHEET.ACCOUNT.TYPE` | `FsGaBalancesheet_AccountType` | TField |  | Account type Multifonds DB Column is GLACCOUNTTYPE. |
| 8 | `BALANCESHEET.GL.ACCOUNT` | `FsGaBalancesheet_GlAccount` | TField |  | Gl Account Multifonds DB Column is GLACCOUNT. |
| 9 | `BALANCESHEET.FEECODE` | `FsGaBalancesheet_Feecode` | TField |  | FeeCode Multifonds DB Column is FEECODE. |
| 10 | `BALANCESHEET.ACCOUNTING.COMPONENT` | `FsGaBalancesheet_AccountingComponent` | TField |  | Accounting Component Multifonds DB Column is ACCOUNTINGCOMPONENT. |
| 11 | `BALANCESHEET.ACCOUNTING.KEY` | `FsGaBalancesheet_AccountingKey` | TField |  | Accounting Key Multifonds DB Column is ACCOUNTINGKEY. |
| 12 | `BALANCESHEET.POSITION.KEY` | `FsGaBalancesheet_PositionKey` | TField |  | Position Key Multifonds DB Column is POSITIONKEY. |
| 13 | `BALANCESHEET.CUSTOMFIELD.1` | `FsGaBalancesheet_Customfield1` | TField |  | CustomField 1 Multifonds DB Column is CUSTOMFIELD1. |
| 14 | `BALANCESHEET.CUSTOMFILED.2` | `FsGaBalancesheet_Customfiled2` | TField |  | CustomFiled 2 Multifonds DB Column is CUSTOMFIELD2. |
| 15 | `BALANCESHEET.CUSTOMFIELD.3` | `FsGaBalancesheet_Customfield3` | TField |  | CustomField 3 Multifonds DB Column is CUSTOMFIELD3. |
| 16 | `BALANCESHEET.BS.GROUP` | `FsGaBalancesheet_BsGroup` | TField |  | Bs Group Multifonds DB Column is BSGROUP. |
| 17 | `BALANCESHEET.ASSET.CATEGORY` | `FsGaBalancesheet_AssetCategory` | TField |  | Asset Category Multifonds DB Column is ASSETCATEGORY. |
| 18 | `BALANCESHEET.TRANSACTION.ADJUSTMENT` | `FsGaBalancesheet_TransactionAdjustment` | TField |  | Transaction Adjustment Multifonds DB Column is TRANSACTIONADJUSTMENT. |
| 19 | `BALANCESHEET.FUNDSTRUCTURE.SOURCE` | `FsGaBalancesheet_FundstructureSource` | TField |  | FundStructure Source Multifonds DB Column is FUNDSTRUCTURESOURCE. |
| 20 | `BALANCESHEET.FUNDSTRUCTURE.TARGET` | `FsGaBalancesheet_FundstructureTarget` | TField |  | FundStructure Target Multifonds DB Column is FUNDSTRUCTURETARGET. |
| 21 | `BALANCESHEET.ACCRUAL.PAIRS` | `FsGaBalancesheet_AccrualPairs` | TField |  | Accrual Pairs Multifonds DB Column is ACCRUALPAIRS. |
| 22 | `BALANCESHEET.FUND.OBJECTID` | `FsGaBalancesheet_FundObjectid` | TField |  | Fund ObjectId Multifonds DB Column is FUNDOBJECTID. |
| 23 | `BALANCESHEET.INSTRUMENT.OBJECTID` | `FsGaBalancesheet_InstrumentObjectid` | TField |  | Instrument ObjectId Multifonds DB Column is INSTRUMENTOBJECTID. |
| 24 | `BALANCESHEET.SUB.INSTRUMENT.OBJECTID` | `FsGaBalancesheet_SubInstrumentObjectid` | TField |  | Sub Instrument ObjectId Multifonds DB Column is SUBINSTRUMENTOBJECTID. |
| 25 | `BALANCESHEET.WORKSPACEID` | `FsGaBalancesheet_Workspaceid` | TField |  | WORKSPACEID Multifonds DB Column is WORKSPACEID. |
| 26 | `BALANCESHEET.KNOWLEDGEDATE` | `FsGaBalancesheet_Knowledgedate` | TField |  | KNOWLEDGEDATE Multifonds DB Column is KNOWLEDGEDATE. |
| 27 | `BALANCESHEET.DESCRIPTION` | `FsGaBalancesheet_Description` | TField |  | Description Multifonds DB Column is DESCRIPTION. |
| 28 | `BALANCESHEET.SUB.CUSTODIAN.ACCOUNT` | `FsGaBalancesheet_SubCustodianAccount` | TField |  | Sub Custodian Account Multifonds DB Column is SUBCUSTODIANACCOUNT. |
| 29 | `BALANCESHEET.GL.SUBACCOUNT` | `FsGaBalancesheet_GlSubaccount` | TField |  | Gl SubAccount Multifonds DB Column is GLSUBACCOUNT. |
| 30 | `BALANCESHEET.TRAN.OPCODE` | `FsGaBalancesheet_TranOpcode` | TField |  | Tran OpCode Multifonds DB Column is TRANSACTIONSUBTYPE. |
| 31 | `BALANCESHEET.TRANSACTION.PRICE` | `FsGaBalancesheet_Price` |  |  |  |
| 32 | `BALANCESHEET.DATE.OF.PRICE` | `FsGaBalancesheet_PriceDate` |  |  |  |
| 33 | `BALANCESHEET.RATE.OF.EXCHANGE` | `FsGaBalancesheet_ExchangeRate` |  |  |  |
| 34 | `BALANCESHEET.EXCHANGE.RATE.DATE` | `FsGaBalancesheet_ExchangeRateDate` | TField |  | Exchange Rate Date Multifonds DB Column is EXCHANGERATEDATE. |
| 35 | `BALANCESHEET.INSTRUMENT.SUB.GROUP` | `FsGaBalancesheet_InstrumentSubGroup` | TField |  | Instrument sub group Multifonds DB Column is INSTRUMENTSUBGROUP. |
| 36 | `BALANCESHEET.ACCOUNTING.SUB.COMPONENT` | `FsGaBalancesheet_AccountingSubComponent` | TField |  | Accounting sub component Multifonds DB Column is ACCOUNTINGSUBCOMPONENT. |
| 37 | `BALANCESHEET.RECORDID` | `FsGaBalancesheet_Recordid` | TField |  | Recordid Multifonds DB Column is RECORDID. |
| 38 | `BALANCESHEET.OBJECTID` | `FsGaBalancesheet_Objectid` | TField |  | Objectid Multifonds DB Column is OBJECTID. |
| 39 | `BALANCESHEET.CLIENTID` | `FsGaBalancesheet_Clientid` | TField |  | Clientid Multifonds DB Column is CLIENTID. |
| 40 | `BALANCESHEET.KNOWLEDGE.START.DATE` | `FsGaBalancesheet_KnowledgeStartDate` | TField |  | Knowledge start date Multifonds DB Column is KNOWLEDGEDATESTART. |
| 41 | `BALANCESHEET.USERNAME` | `FsGaBalancesheet_Username` | TField |  | Username Multifonds DB Column is USERNAME. |
| 42 | `BALANCESHEET.FUND.CODE` | `FsGaBalancesheet_FundCode` | TField |  | Fund Code Multifonds DB Column is FUNDCODE. |
| 43 | `BALANCESHEET.BOOK.CODE` | `FsGaBalancesheet_BookCode` | TField |  | Book Code Multifonds DB Column is BOOKCODE. |
| 44 | `BALANCESHEET.OPERATION.CODE` | `FsGaBalancesheet_TransactionType` |  |  |  |
| 45 | `BALANCESHEET.INSTRUMENTCODE` | `FsGaBalancesheet_Instrumentcode` | TField |  | InstrumentCode Multifonds DB Column is INSTRUMENTCODE. |
| 46 | `BALANCESHEET.SUB.INSTRUMENT.CODE` | `FsGaBalancesheet_SubInstrumentCode` | TField |  | Sub Instrument Code Multifonds DB Column is SUBINSTRUMENTCODE. |
| 47 | `BALANCESHEET.INSTRUMENT.GROUP` | `FsGaBalancesheet_InstrumentGroup` | TField |  | Instrument Group Multifonds DB Column is INSTRUMENTGROUP. |
| 48 | `BALANCESHEET.ACCOUNTING.DATE` | `FsGaBalancesheet_AccountingDate` | TField |  | Accounting Date Multifonds DB Column is ACCOUNTINGDATE. |
| 49 | `BALANCESHEET.MARKTOMARKET.DATE` | `FsGaBalancesheet_MarktomarketDate` | TField |  | MarkToMarket Date Multifonds DB Column is VALUATIONDATE. |
| 50 | `BALANCESHEET.LOCAL.CCY` | `FsGaBalancesheet_LocalCcy` | TField |  | Local Ccy Multifonds DB Column is LOCALCCY. |
| 51 | `BALANCESHEET.BOOK.CCY` | `FsGaBalancesheet_BookCcy` | TField |  | Book Ccy Multifonds DB Column is BOOKCCY. |
| 52 | `BALANCESHEET.CUSTODIAN.ACCOUNT` | `FsGaBalancesheet_CustodianAccount` | TField |  | Custodian Account Multifonds DB Column is CUSTODIANACCOUNT. |
| 53 | `BALANCESHEET.STRATEGY.CODE` | `FsGaBalancesheet_StrategyCode` | TField |  | Strategy Code Multifonds DB Column is STRATEGYCODE. |
| 54 | `BALANCESHEET.FUNDSTRUCTURE.CODE` | `FsGaBalancesheet_FundstructureCode` | TField |  | FundStructure Code Multifonds DB Column is FUNDSTRUCTURECODE. |
| 55 | `BALANCESHEET.TAXLOT.TYPE` | `FsGaBalancesheet_TaxlotType` | TField |  | TaxLot Type Multifonds DB Column is TAXLOTTYPE. |
| 56 | `BALANCESHEET.RECORD.STATUS` | `FsGaBalancesheet_RecordStatus` | String |  |  |
| 57 | `BALANCESHEET.CURR.NO` | `FsGaBalancesheet_CurrNo` | String |  |  |
| 58 | `BALANCESHEET.INPUTTER` | `FsGaBalancesheet_Inputter` |  |  |  |
| 59 | `BALANCESHEET.DATE.TIME` | `FsGaBalancesheet_DateTime` |  |  |  |
| 60 | `BALANCESHEET.AUTHORISER` | `FsGaBalancesheet_Authoriser` | String |  |  |
| 61 | `BALANCESHEET.CO.CODE` | `FsGaBalancesheet_CoCode` | String |  |  |
| 62 | `BALANCESHEET.DEPT.CODE` | `FsGaBalancesheet_DeptCode` | String |  |  |
| 63 | `BALANCESHEET.AUDITOR.CODE` | `FsGaBalancesheet_AuditorCode` | String |  |  |
| 64 | `BALANCESHEET.AUDIT.DATE.TIME` | `FsGaBalancesheet_AuditDateTime` | String |  |  |
