# FATCA.AGGREGATE.BALANCES — Table Schema

> Source: `INSERTS/I_F.FATCA.AGGREGATE.BALANCES` in `FA_BalanceAggregation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.AGB.CUSTOMER.TYPE` | `FatcaAggregateBalances_CustomerType` | TField |  | The field will be updated as CUSTOMER or ACCOUNT based on relationship level defined in FATCA.AGGREGATION.PARAMETER. |
| 2 | `FA.AGB.SECTOR` | `FatcaAggregateBalances_Sector` | TField |  | This field stores the SECTOR of the customer. This field is defaulted from CUSTOMER application. |
| 3 | `FA.AGB.INDUSTRY` | `FatcaAggregateBalances_Industry` | TField |  | This field stores the INDUSTRY of the customer. This field is defaulted from CUSTOMER application. |
| 4 | `FA.AGB.CUSTOMER.STATUS` | `FatcaAggregateBalances_CustomerStatus` | TField |  | This field stores the CUSTOMER.STATUS of the customer. This field is defaulted from CUSTOMER application. |
| 5 | `FA.AGB.RELATED.CUSTOMER` | `FatcaAggregateBalances_RelatedCustomer` |  |  |  |
| 6 | `FA.AGB.RELATION.CODE` | `FatcaAggregateBalances_RelationCode` |  |  |  |
| 7 | `FA.AGB.ACC.PORT.NUMBER` | `FatcaAggregateBalances_AccPortNumber` |  |  |  |
| 8 | `FA.AGB.ACCOUNT.TYPE` | `FatcaAggregateBalances_AccountType` |  |  |  |
| 9 | `FA.AGB.JOINT.OWNER` | `FatcaAggregateBalances_JointOwner` |  |  |  |
| 10 | `FA.AGB.JNT.OWNER.REL.CODE` | `FatcaAggregateBalances_JntOwnerRelCode` |  |  |  |
| 11 | `FA.AGB.ACC.PORT.CCY` | `FatcaAggregateBalances_AccPortCcy` |  |  |  |
| 12 | `FA.AGB.ACC.BALANCE` | `FatcaAggregateBalances_AccBalance` |  |  |  |
| 13 | `FA.AGB.ACC.EXCH.RATE` | `FatcaAggregateBalances_AccExchRate` |  |  |  |
| 14 | `FA.AGB.ACC.BAL.USD` | `FatcaAggregateBalances_AccBalUsd` |  |  |  |
| 15 | `FA.AGB.TOT.ACC.BAL.DEPO` | `FatcaAggregateBalances_TotAccBalDepo` | TField |  | USD equivalent of total depository balance. Balances of the contracts with Account type as Depository will alone be considered. |
| 16 | `FA.AGB.TOT.ACC.BAL.CUST` | `FatcaAggregateBalances_TotAccBalCust` | TField |  | USD equivalent of total custody balance. Balances of the contracts with Account type as Custody will alone be considered. |
| 17 | `FA.AGB.INDIV.ENTITY` | `FatcaAggregateBalances_IndivEntity` | TField |  | This field says whether the customer is an individual or an entity. The value in this field is arrived based on the selection criteria given for customer in FATCA.AGGREGATION.PARAMETER. |
| 18 | `FA.AGB.BALANCE.STATUS` | `FatcaAggregateBalances_BalanceStatus` | TField |  | Depending on the balance held by the customer and the Account type to which it belongs, the system stamps theBalance status of the customer as follows: 1. EXEMPT IND : This value is updated by the system if the customer is an individual and both TOT.ACC.BAL.DEP and TOT.ACC.BAL.CUST is less than $50000 2. EXEMPT ENT : This value is updated by the system if the customer is an Entity and both TOT.ACC.BAL.DEP and TOT.ACC.BAL.CUST is less than $250000 3. HIGH VALUE : This value is updated by the system if sum of both TOT.ACC.BAL.DEPO and TOT.ACC.BAL.CUST exceeds $ 1 million |
