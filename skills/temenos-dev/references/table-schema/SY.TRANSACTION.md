# SY.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.SY.TRANSACTION` in `SY_Trading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.TX.PRODUCT.DEFINITION` | `SyTransaction_ProductDefinition` | TField |  | The product definiton ID which is applicable to this transaction. |
| 2 | `SY.TX.USER.APPLICATION` | `SyTransaction_UserApplication` | TField |  | The application which was used to capture this deal. i.e. SY.CRAN |
| 3 | `SY.TX.USER.APP.ID` | `SyTransaction_UserAppId` | TField |  | The ID of the record used to capture this deal. |
| 4 | `SY.TX.CUSTOMER` | `SyTransaction_Customer` | TField |  | This is the customer who the deal was created for. |
| 5 | `SY.TX.PORTFOLIO` | `SyTransaction_Portfolio` | TField |  | This is the customers portfolio to which this deal applies. |
| 6 | `SY.TX.COUNTERPARTY` | `SyTransaction_Counterparty` | TField |  | The counterparty customer of the deal. |
| 7 | `SY.TX.COUNTERPARTY.PTFO` | `SyTransaction_CounterpartyPtfo` | TField |  | Hold the counterparty of the deals portfolio where this is not the banks own book. |
| 8 | `SY.TX.ACCOUNT` | `SyTransaction_Account` | TField |  | The customers account from which the funding from the deal is taken. |
| 9 | `SY.TX.DEPOSIT.AMT` | `SyTransaction_DepositAmt` | TField |  | This is the initial investment amount for this deal. i.e. A $1Million CRAN. |
| 10 | `SY.TX.DEPOSIT.CCY` | `SyTransaction_DepositCcy` | TField |  | The currency of the initial investment. |
| 11 | `SY.TX.TRADE.DATE` | `SyTransaction_TradeDate` | TField |  | The trade date of this deal. |
| 12 | `SY.TX.VALUE.DATE` | `SyTransaction_ValueDate` | TField |  | The value date of this deal. |
| 13 | `SY.TX.TERMINATED` | `SyTransaction_Terminated` | TField |  | If this is Yes then the deal has been through a Terminal Event which means this deal has reached the end of its lifecycle. |
| 14 | `SY.TX.REVERSAL.BLOCKED` | `SyTransaction_ReversalBlocked` | TField |  | Defines is refersal of the deal record (USER.APP.ID) held in the USER.APPLICATION table can be reversed. |
| 15 | `SY.TX.CHANGE.BLOCKED` | `SyTransaction_ChangeBlocked` | TField |  | Defines is refersal of the deal record (USER.APP.ID) held in the USER.APPLICATION table can be ammended. |
| 16 | `SY.TX.PRODUCT` | `SyTransaction_Product` | TField |  | The SY.PRODUCT record linked to this deal. |
| 17 | `SY.TX.TRANSACTION` | `SyTransaction_Transaction` | TField |  | The key to this deal. |
| 18 | `SY.TX.MATURITY.DATE` | `SyTransaction_MaturityDate` | TField |  | This is the maturity date of the deal. |
| 19 | `SY.TX.PRODUCT.CATEGORY` | `SyTransaction_ProductCategory` | TField |  | This field holds a generic category id which degfines the category of the product. This information is defaulted from the SY.PRODUCT record. |
| 20 | `SY.TX.VARIANT` | `SyTransaction_Variant` | TField |  | The variant used in the SY contract. Valid record in SY.PRODUCT.VARIANT. |
| 21 | `SY.TX.EVENT.LOG` | `SyTransaction_EventLog` |  |  |  |
| 22 | `SY.TX.UNIT.LOG` | `SyTransaction_UnitLog` |  |  |  |
| 23 | `SY.TX.CONTRACT.CCY` | `SyTransaction_ContractCcy` | TField |  | The contract currency of SY contract. Valid currency. This field will map from the relevant Structured Product contract. |
| 24 | `SY.TX.COUNTERPARTY.ACC` | `SyTransaction_CounterpartyAcc` | TField |  | Counterparty account in contract currency.This field will map from the relevant Structured Product contract. |
| 25 | `SY.TX.STORE.NAME` | `SyTransaction_StoreName` |  |  |  |
| 26 | `SY.TX.STORE.VALUE` | `SyTransaction_StoreValue` |  |  |  |
| 27 | `SY.TX.STORE.BY` | `SyTransaction_StoreBy` |  |  |  |
| 28 | `SY.TX.EXTERNAL.REF` | `SyTransaction_ExternalRef` | TField |  | This field is for information purpose used by client during interface. This field will map from the relevant Structured Product contract. It will hold the reference of this contract in the external system from where it is interfaced. |
| 29 | `SY.TX.SY.DX.REFERENCE` | `SyTransaction_SyDxReference` | TField |  | This field holds the unique reference.This field will map from the relevant Structured Product contract. It enables easy identification of Structured contracts and thier underlying component. This field also updates SY.DX.LINK.FILE which lists all contracts which have the same SY.DX.REFERENCE. |
| 30 | `SY.TX.UNIT.DEFINITION` | `SyTransaction_UnitDefinition` |  |  |  |
| 31 | `SY.TX.LAST.UNIT.INST` | `SyTransaction_LastUnitInst` |  |  |  |
| 32 | `SY.TX.B2B.REFERENCE` | `SyTransaction_B2bReference` | TField |  | This field holds the Back to Back reference.This field will map from the relevant Structured Product contract. This reference helps to map a structured product contract and its Back-to-back contract to ensure that all contracts are covered. |
| 33 | `SY.TX.CURRENCY.MARKET` | `SyTransaction_CurrencyMarket` | TField |  | The system recognizes the need for a number of different markets within one currency. For this reason this field identifies which Exchange Rate Currency Market is accessed for this transaction. The system caters for the need to have more than one market within a given currency. The use of this field will only be applicable for those countries where the exchange market defines different rates for the same foreign Currency according to rules determined by the local authorities or local central bank. A typical example would be Belgium where foreign currencies are quoted on the Regular Market and also on the Free Market. Different sets of exchange rates will exist for these two markets. |
| 34 | `SY.TX.POSITION.TYPE` | `SyTransaction_PositionType` | TField |  | The position type used for this deal. Defaulted from SY.PARAMETER. |
| 35 | `SY.TX.WASH.ACCOUNT` | `SyTransaction_WashAccount` | TField |  | The SY wash account / internal account through which entries are routed from the Structured product deal to the underlying application and vice-versa. The account will be in contract currency. |
| 36 | `SY.TX.DEALER.DESK` | `SyTransaction_DealerDesk` | TField |  | Identifies the dealer desk position which needs to be updated by the deal being created. The dealer desk code is held on the position record so that the exchange position can be displayed at dealer desk level. Each deal on the system will be allocated a two-digit dealer desk code. This code will be used to maintain position at the dealer desk level. |
| 37 | `SY.TX.ACCOUNT.OFFICER` | `SyTransaction_AccountOfficer` | TField |  | Identifies the account officer responsible for the relationship with the CPARTY. This information will be used by the Management Information System (MIS) for the determination of the Customer Profitability Analysis. This field has been provided to enable the user to override at transaction level the CPARTY default account officer defined in the CUSTOMER file. |
| 38 | `SY.TX.UNDERLYING.APP` | `SyTransaction_UnderlyingApp` |  |  |  |
| 39 | `SY.TX.UNDERLYING.ID` | `SyTransaction_UnderlyingId` |  |  |  |
| 40 | `SY.TX.RESERVED.2` | `SyTransaction_Reserved2` | TField |  |  |
| 41 | `SY.TX.STATEMENT.NOS` | `SyTransaction_StatementNos` |  |  |  |
| 42 | `SY.TX.LOCAL.REF` | `SyTransaction_LocalRef` |  |  |  |
| 43 | `SY.TX.OVERRIDE` | `SyTransaction_Override` |  |  |  |
| 44 | `SY.TX.MTM.DATE` | `SyTransaction_MtmDate` | TField |  |  |
| 45 | `SY.TX.MTM.CCY` | `SyTransaction_MtmCcy` | TField |  |  |
| 46 | `SY.TX.MTM.AMT` | `SyTransaction_MtmAmt` | TField |  |  |
| 47 | `SY.TX.MTM.ACCOUNT` | `SyTransaction_MtmAccount` | TField |  |  |
| 48 | `SY.TX.MTM.LCCY` | `SyTransaction_MtmLccy` | TField |  |  |
| 49 | `SY.TX.MTM.LCCY.RATE` | `SyTransaction_MtmLccyRate` | TField |  |  |
| 50 | `SY.TX.PREV.MTM.DATE` | `SyTransaction_PrevMtmDate` | TField |  |  |
| 51 | `SY.TX.PREV.MTM.CCY` | `SyTransaction_PrevMtmCcy` | TField |  |  |
| 52 | `SY.TX.PREV.MTM.AMT` | `SyTransaction_PrevMtmAmt` | TField |  |  |
| 53 | `SY.TX.PREV.MTM.ACCOUNT` | `SyTransaction_PrevMtmAccount` | TField |  |  |
| 54 | `SY.TX.PREV.MTM.LCCY` | `SyTransaction_PrevMtmLccy` | TField |  |  |
| 55 | `SY.TX.PREV.MTM.LCCY.RATE` | `SyTransaction_PrevMtmLccyRate` | TField |  |  |
| 56 | `SY.TX.MTM.TERMINATED` | `SyTransaction_MtmTerminated` | TField |  |  |
| 57 | `SY.TX.EVENT.DEFINITION` | `SyTransaction_EventDefinition` |  |  |  |
| 58 | `SY.TX.ACTIVITY.CODE` | `SyTransaction_ActivityCode` |  |  |  |
| 59 | `SY.TX.MESSAGE.TYPE` | `SyTransaction_MessageType` |  |  |  |
| 60 | `SY.TX.MESSAGE.REF` | `SyTransaction_MessageRef` |  |  |  |
| 61 | `SY.TX.REP.CUSTOMER` | `SyTransaction_RepCustomer` | TField |  |  |
| 62 | `SY.TX.PO.EVENT.DEFINITION` | `SyTransaction_PoEventDefinition` |  |  |  |
| 63 | `SY.TX.PO.REFERENCE` | `SyTransaction_PoReference` |  |  |  |
