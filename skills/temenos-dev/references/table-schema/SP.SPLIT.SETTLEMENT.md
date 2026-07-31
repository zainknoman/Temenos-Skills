# SP.SPLIT.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.SP.SPLIT.SETTLEMENT` in `SP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SPST.SECURITY.NO` | `SpSplitSettlement_SecurityNo` | TField |  | System updated Field . Defaulted with Security No from Transaction Validation Rules: NOINPUT Field |
| 2 | `SC.SPST.CUSTOMER.NO` | `SpSplitSettlement_CustomerNo` | TField |  | System updated Field . Defaulted with Customer from Transaction Validation Rules: NOINPUT Field |
| 3 | `SC.SPST.PORTFOLIO.NO` | `SpSplitSettlement_PortfolioNo` | TField |  | System updated Field . Defaulted with Portfolio from Transaction Validation Rules: NOINPUT Field |
| 4 | `SC.SPST.BROKER.NO` | `SpSplitSettlement_BrokerNo` | TField |  | System updated Field . Defaulted with Broker from Transaction Validation Rules: NOINPUT Field |
| 5 | `SC.SPST.DEPOSITORY` | `SpSplitSettlement_Depository` | TField |  | System updated Field . Defaulted with Depository from Transaction Validation Rules: NOINPUT Field |
| 6 | `SC.SPST.SUB.ACCOUNT` | `SpSplitSettlement_SubAccount` | TField |  | System updated Field . Defaulted with SubAccount from Transaction Validation Rules: NOINPUT Field |
| 7 | `SC.SPST.VALUE.DATE` | `SpSplitSettlement_ValueDate` | TField |  | System updated Field . Defaulted with Value Date from Transaction Validation Rules: NOINPUT Field |
| 8 | `SC.SPST.SETTLEMENT.CCY` | `SpSplitSettlement_SettlementCcy` | TField |  | System updated Field . Defaulted with Trade Currency from Transaction Validation Rules: NOINPUT Field |
| 9 | `SC.SPST.TRANSACTION.REF` | `SpSplitSettlement_TransactionRef` |  |  |  |
| 10 | `SC.SPST.ORIG.QTY` | `SpSplitSettlement_OrigQty` |  |  |  |
| 11 | `SC.SPST.ORIG.AMT` | `SpSplitSettlement_OrigAmt` |  |  |  |
| 12 | `SC.SPST.CANC.DELIVERY.KEY` | `SpSplitSettlement_CancDeliveryKey` |  |  |  |
| 13 | `SC.SPST.SEND.SETT.ADV` | `SpSplitSettlement_SendSettAdv` |  |  |  |
| 14 | `SC.SPST.SPLIT.QTY` | `SpSplitSettlement_SplitQty` |  |  |  |
| 15 | `SC.SPST.SPLIT.AMT` | `SpSplitSettlement_SplitAmt` |  |  |  |
| 16 | `SC.SPST.SPLIT.VALUE.DATE` | `SpSplitSettlement_SplitValueDate` |  |  |  |
| 17 | `SC.SPST.SPLIT.REF` | `SpSplitSettlement_SplitRef` |  |  |  |
| 18 | `SC.SPST.SPLIT.DELIVERY.KEY` | `SpSplitSettlement_SplitDeliveryKey` |  |  |  |
| 19 | `SC.SPST.RESERVED.9` | `SpSplitSettlement_Reserved9` | TField |  |  |
| 20 | `SC.SPST.RESERVED.8` | `SpSplitSettlement_Reserved8` | TField |  |  |
| 21 | `SC.SPST.RESERVED.7` | `SpSplitSettlement_Reserved7` | TField |  |  |
| 22 | `SC.SPST.RESERVED.6` | `SpSplitSettlement_Reserved6` | TField |  |  |
| 23 | `SC.SPST.RESERVED.5` | `SpSplitSettlement_Reserved5` | TField |  |  |
| 24 | `SC.SPST.RESERVED.4` | `SpSplitSettlement_Reserved4` | TField |  |  |
| 25 | `SC.SPST.RESERVED.3` | `SpSplitSettlement_Reserved3` | TField |  |  |
| 26 | `SC.SPST.RESERVED.2` | `SpSplitSettlement_Reserved2` | TField |  |  |
| 27 | `SC.SPST.RESERVED.1` | `SpSplitSettlement_Reserved1` | TField |  |  |
| 28 | `SC.SPST.LOCAL.REF` | `SpSplitSettlement_LocalRef` |  |  |  |
| 29 | `SC.SPST.OVERRIDE` | `SpSplitSettlement_Override` |  |  |  |
| 30 | `SC.SPST.RECORD.STATUS` | `SpSplitSettlement_RecordStatus` | String |  |  |
| 31 | `SC.SPST.CURR.NO` | `SpSplitSettlement_CurrNo` | String |  |  |
| 32 | `SC.SPST.INPUTTER` | `SpSplitSettlement_Inputter` |  |  |  |
| 33 | `SC.SPST.DATE.TIME` | `SpSplitSettlement_DateTime` |  |  |  |
| 34 | `SC.SPST.AUTHORISER` | `SpSplitSettlement_Authoriser` | String |  |  |
| 35 | `SC.SPST.CO.CODE` | `SpSplitSettlement_CoCode` | String |  |  |
| 36 | `SC.SPST.DEPT.CODE` | `SpSplitSettlement_DeptCode` | String |  |  |
| 37 | `SC.SPST.AUDITOR.CODE` | `SpSplitSettlement_AuditorCode` | String |  |  |
| 38 | `SC.SPST.AUDIT.DATE.TIME` | `SpSplitSettlement_AuditDateTime` | String |  |  |
