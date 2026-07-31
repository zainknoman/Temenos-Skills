# ST.AGGREGATE.BALANCES — Table Schema

> Source: `INSERTS/I_F.ST.AGGREGATE.BALANCES` in `RT_BalanceAggregation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.AGB.CUSTOMER.TYPE` | `StAggregateBalances_CustomerType` | TField |  | The field will be updated as CUSTOMER or ACCOUNT based on relationship level defined in ST.AGGREGATION.PARAM. |
| 2 | `ST.AGB.SECTOR` | `StAggregateBalances_Sector` | TField |  | This field stores the SECTOR of the customer. This field is defaulted from CUSTOMER application. |
| 3 | `ST.AGB.INDUSTRY` | `StAggregateBalances_Industry` | TField |  | This field stores the INDUSTRY of the customer. This field is defaulted from CUSTOMER application. |
| 4 | `ST.AGB.CUSTOMER.STATUS` | `StAggregateBalances_CustomerStatus` | TField |  | This field stores the CUSTOMER.STATUS of the customer. This field is defaulted from CUSTOMER application. |
| 5 | `ST.AGB.RELATED.CUSTOMER` | `StAggregateBalances_RelatedCustomer` |  |  |  |
| 6 | `ST.AGB.RELATION.CODE` | `StAggregateBalances_RelationCode` |  |  |  |
| 7 | `ST.AGB.ACCT.PORTFOLIO.NO` | `StAggregateBalances_AcctPortfolioNo` |  |  |  |
| 8 | `ST.AGB.ACCOUNT.TYPE` | `StAggregateBalances_AccountType` |  |  |  |
| 9 | `ST.AGB.JOINT.OWNER` | `StAggregateBalances_JointOwner` |  |  |  |
| 10 | `ST.AGB.JOINT.OWN.REL.CODE` | `StAggregateBalances_JointOwnRelCode` |  |  |  |
| 11 | `ST.AGB.ACC.PORTFOLIO.CCY` | `StAggregateBalances_AccPortfolioCcy` |  |  |  |
| 12 | `ST.AGB.ACC.BALANCE` | `StAggregateBalances_AccBalance` |  |  |  |
| 13 | `ST.AGB.ACC.EXCH.RATE` | `StAggregateBalances_AccExchRate` |  |  |  |
| 14 | `ST.AGB.ACC.REPORTING.CCY` | `StAggregateBalances_AccReportingCcy` |  |  |  |
| 15 | `ST.AGB.ACC.BAL.IN.REP.CCY` | `StAggregateBalances_AccBalInRepCcy` |  |  |  |
| 16 | `ST.AGB.TOT.AC.BAL.DEP.RCY` | `StAggregateBalances_TotAcBalDepRcy` | TField |  | REPORTING.CCY equivalent of the total Depository balance. |
| 17 | `ST.AGB.TOT.AC.BAL.DEP.LCY` | `StAggregateBalances_TotAcBalDepLcy` | TField |  | Local currency equivalent of the total Depository balance. |
| 18 | `ST.AGB.TOT.AC.BAL.CUS.RCY` | `StAggregateBalances_TotAcBalCusRcy` | TField |  | REPORTING.CCY equivalent of the total Custody balance. |
| 19 | `ST.AGB.TOT.AC.BAL.CUS.LCY` | `StAggregateBalances_TotAcBalCusLcy` | TField |  | Local currency equivalent of the total Custody balance. |
| 20 | `ST.AGB.INDIVIDUAL.ENTITY` | `StAggregateBalances_IndividualEntity` | TField |  | This field says whether the customer is an individual or an entity. The value in this field is arrived based on the selection criteria given for customer in ST.AGGREGATION.PARAM. |
| 21 | `ST.AGB.BALANCE.STATUS` | `StAggregateBalances_BalanceStatus` | TField |  | Pre-Existing Individual Low, Pre-Existing Individual High, Pre-Existing Entity Low, Pre-Existing Entity High will be updated based on the amounts defined in CRS.PARAMETER for CRS Regulation. |
