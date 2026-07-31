# CR.CUSTOMER.INTELLIGENCE — Table Schema

> Source: `INSERTS/I_F.CR.CUSTOMER.INTELLIGENCE` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.CUST.NO.PRODTS` | `CrCustomerIntelligence_NoProdts` | TField |  | Customer Number of Products as assigned in Insight. Validation Rules Numeric to format.2 numeric characters allowed including zero. |
| 2 | `CR.CUST.NO.PRODTS.STATUS` | `CrCustomerIntelligence_NoProdtsStatus` | TField |  | Customer Number of Products Status Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 3 | `CR.CUST.NO.PRODTS.TREND` | `CrCustomerIntelligence_NoProdtsTrend` | TField |  | Customer Number of Products Trend Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 4 | `CR.CUST.NO.PRODTS.CHG.DATE` | `CrCustomerIntelligence_NoProdtsChgDate` | TField |  | Customer Number of Products Last Changed Date. Validation Rules T24 Date Type Field. |
| 5 | `CR.CUST.LOYALTY.SCORE` | `CrCustomerIntelligence_LoyaltyScore` | TField |  | Customer Loyalty Score as assigned in Insight. Validation Rules 2 numeric character allowed including zero. |
| 6 | `CR.CUST.LOYALTY.STATUS` | `CrCustomerIntelligence_LoyaltyStatus` | TField |  | Customer Loyalty Score Status Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 7 | `CR.CUST.LOYALTY.TREND` | `CrCustomerIntelligence_LoyaltyTrend` | TField |  | Customer Loyalty Score Trend Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 8 | `CR.CUST.LOYALTY.CHG.DATE` | `CrCustomerIntelligence_LoyaltyChgDate` | TField |  | Cutomer Loyalty Score Last Changed Date. Validation Rules T24 Date Type Field. |
| 9 | `CR.CUST.PROFIT.GRP` | `CrCustomerIntelligence_ProfitGrp` | TField |  | Customer Profitability Group as assigned in Insight. Validation Rules 2 numeric character allowed including zero. |
| 10 | `CR.CUST.PROFIT.GRP.STATUS` | `CrCustomerIntelligence_ProfitGrpStatus` | TField |  | Customer Profitability Group Status Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 11 | `CR.CUST.PROFIT.GRP.TREND` | `CrCustomerIntelligence_ProfitGrpTrend` | TField |  | Customer Profitability Group Trend Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 12 | `CR.CUST.PROFIT.CHG.DATE` | `CrCustomerIntelligence_ProfitChgDate` | TField |  | Customer Profitability Group Last Changed Date. Validation Rules T24 Date Type Field. |
| 13 | `CR.CUST.ATTRITION.RISK` | `CrCustomerIntelligence_AttritionRisk` | TField |  | Customer Attrition Risk as assigned in Insight. Validation Rules 2 numeric character allowed including zero. |
| 14 | `CR.CUST.ATTRITION.STATUS` | `CrCustomerIntelligence_AttritionStatus` | TField |  | Customer Attrition Risk Status Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 15 | `CR.CUST.ATTRITION.TREND` | `CrCustomerIntelligence_AttritionTrend` | TField |  | Customer Attrition Risk Trend Indicator. Validation Rules 4 numeric character allowed including -ve or zero. |
| 16 | `CR.CUST.ATTRITION.CHG.DATE` | `CrCustomerIntelligence_AttritionChgDate` | TField |  | Customer Attrition Risk Last Changed Date. Validation Rules T24 Date Type Field. |
| 17 | `CR.CUST.3M.LOYALTY.SCORE` | `CrCustomerIntelligence_3mLoyaltyScore` |  |  |  |
| 18 | `CR.CUST.12M.LOYALTY.SCORE` | `CrCustomerIntelligence_12mLoyaltyScore` |  |  |  |
| 19 | `CR.CUST.3M.PROFIT.SCORE` | `CrCustomerIntelligence_3mProfitScore` |  |  |  |
| 20 | `CR.CUST.12M.PROFIT.SCORE` | `CrCustomerIntelligence_12mProfitScore` |  |  |  |
| 21 | `CR.CUST.RESERVED.05` | `CrCustomerIntelligence_Reserved05` | TField |  |  |
| 22 | `CR.CUST.RESERVED.04` | `CrCustomerIntelligence_Reserved04` | TField |  |  |
| 23 | `CR.CUST.RESERVED.03` | `CrCustomerIntelligence_Reserved03` | TField |  |  |
| 24 | `CR.CUST.RESERVED.02` | `CrCustomerIntelligence_Reserved02` | TField |  |  |
| 25 | `CR.CUST.RESERVED.01` | `CrCustomerIntelligence_Reserved01` | TField |  |  |
| 26 | `CR.CUST.LOCAL.REF` | `CrCustomerIntelligence_LocalRef` |  |  |  |
| 27 | `CR.CUST.OVERRIDE` | `CrCustomerIntelligence_Override` |  |  |  |
| 28 | `CR.CUST.RECORD.STATUS` | `CrCustomerIntelligence_RecordStatus` | String |  |  |
| 29 | `CR.CUST.CURR.NO` | `CrCustomerIntelligence_CurrNo` | String |  |  |
| 30 | `CR.CUST.INPUTTER` | `CrCustomerIntelligence_Inputter` |  |  |  |
| 31 | `CR.CUST.DATE.TIME` | `CrCustomerIntelligence_DateTime` |  |  |  |
| 32 | `CR.CUST.AUTHORISER` | `CrCustomerIntelligence_Authoriser` | String |  |  |
| 33 | `CR.CUST.CO.CODE` | `CrCustomerIntelligence_CoCode` | String |  |  |
| 34 | `CR.CUST.DEPT.CODE` | `CrCustomerIntelligence_DeptCode` | String |  |  |
| 35 | `CR.CUST.AUDITOR.CODE` | `CrCustomerIntelligence_AuditorCode` | String |  |  |
| 36 | `CR.CUST.AUDIT.DATE.TIME` | `CrCustomerIntelligence_AuditDateTime` | String |  |  |
