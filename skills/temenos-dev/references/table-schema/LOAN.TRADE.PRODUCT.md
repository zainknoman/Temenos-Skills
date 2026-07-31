# LOAN.TRADE.PRODUCT — Table Schema

> Source: `INSERTS/I_F.LOAN.TRADE.PRODUCT` in `LNTRAD_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LN.TRA.SHORT.DESCRIPTION` | `LoanTradeProduct_ShortDescription` |  |  |  |
| 2 | `LN.TRA.FULL.DESCRIPTION` | `LoanTradeProduct_FullDescription` |  |  |  |
| 3 | `LN.TRA.GOVERNING.LAW` | `LoanTradeProduct_GoverningLaw` | TField | Yes | Specify the Trade's governing body. Validation Rules:Mandatory Field Valid input 1. LMA - Loan Market (EMEA) 2. LSTA - Loan Market (Americas) 3. APMLA - Loan Market (Asia and Pacific) 4. Others - Loan Market (Others) |
| 4 | `LN.TRA.TYPE` | `LoanTradeProduct_Type` | TField |  | Specify the type of Trade Validation Rules: Par � For capturing a trade at Par value Distressed � For capturing a trade at Distressed value. |
| 5 | `LN.TRA.ALLOWED.CCY` | `LoanTradeProduct_AllowedCcy` |  |  |  |
| 6 | `LN.TRA.RESTRICTED.CCY` | `LoanTradeProduct_RestrictedCcy` |  |  |  |
| 7 | `LN.TRA.CURRENCY` | `LoanTradeProduct_Currency` |  |  |  |
| 8 | `LN.TRA.SETTLE.DAYS` | `LoanTradeProduct_SettleDays` |  |  |  |
| 9 | `LN.TRA.BUS.DAY.CENTRES` | `LoanTradeProduct_BusDayCentres` |  |  |  |
| 10 | `LN.TRA.EFFECTIVE.DATE` | `LoanTradeProduct_EffectiveDate` | TField |  | If set to YES, the Deal will expire on the date specified in the MATURITY.DATE. If set to NO, the STATUS of the Deal will be held as 'CUR' even past the Maturity Date. |
| 11 | `LN.TRA.EXPIRY.DATE` | `LoanTradeProduct_ExpiryDate` | TField |  | The date from which this product ceases to exist in the Loan Product Catalog. It means new trades cannot be captured using the product from this date |
| 12 | `LN.TRA.ACTION` | `LoanTradeProduct_Action` | TField | Yes | Available option is Publish. Once the product is published, it will be listed in LOAN.TRADE.PRODUCT.CATALOG. When user publishes a product, transact validates all the mandatory input. Validation and Usage Rule: Publish |
| 13 | `LN.TRA.ACTIVITY.ID` | `LoanTradeProduct_ActivityId` |  |  |  |
| 14 | `LN.TRA.CHARGE.NAME` | `LoanTradeProduct_ChargeName` |  |  |  |
| 15 | `LN.TRA.CLOSURE.DAYS` | `LoanTradeProduct_ClosureDays` | TField |  | Specify the number of days after the trade is settled for the trade to move to archive. |
| 16 | `LN.TRA.INC.PREMIUM.SALE` | `LoanTradeProduct_IncPremiumSale` | TField |  | Specify the income under which any Premium or discount, Netback and benefit of commitment reduction can be collected for a premium sale type of trade. It should be a valid record of LOAN.TRADE.CHARGE.CONDITIONS with INC.EXP.TREATMENT set as Yes |
| 17 | `LN.TRA.INC.DISCOUNTED.PURCHASE` | `LoanTradeProduct_IncDiscountedPurchase` | TField |  | Specify the income charge under which any Premium or discount, Netback and benefit of commitment reduction can be collected for a discounted purchase type of trade. It should be a valid record of LOAN.TRADE.CHARGE.CONDITIONS with INC.EXP.TREATMENT set as Yes |
| 18 | `LN.TRA.EXP.PREMIUM.PURCHASE` | `LoanTradeProduct_ExpPremiumPurchase` | TField |  | Specify the expenditure charge under which any Premium or discount, Netback and benefit of commitment reduction can be collected for a premium purchase type of trade. It should be a valid record of LOAN.TRADE.CHARGE.CONDITIONS with INC.EXP.TREATMENT set as Yes |
| 19 | `LN.TRA.EXP.DISCOUNTED.SALE` | `LoanTradeProduct_ExpDiscountedSale` | TField |  | Specify the expenditure charge under which any Premium or discount, Netback and benefit of commitment reduction can be collected for a discounted sale type of trade. It should be a valid record of LOAN.TRADE.CHARGE.CONDITIONS with INC.EXP.TREATMENT set as Yes |
| 20 | `LN.TRA.CATEGORY` | `LoanTradeProduct_Category` | TField |  | Contains the Category Code to which this transaction will be assigned. The CATEGORY must exist on the Category Table. The category must be within the range 35001 to 35101 |
| 21 | `LN.TRA.RULE.ID` | `LoanTradeProduct_RuleId` | TField |  | Indicates the accounting rule that is associated with the product. The rule will be used for the trades create for the product for all accounting entries. It must be a valid record from the table AC.ALLOCATION.RULE |
| 22 | `LN.TRA.RESERVED10` | `LoanTradeProduct_Reserved10` | TField |  |  |
| 23 | `LN.TRA.LOCAL.REF` | `LoanTradeProduct_LocalRef` |  |  |  |
| 24 | `LN.TRA.OVERRIDE` | `LoanTradeProduct_Override` |  |  |  |
| 25 | `LN.TRA.RECORD.STATUS` | `LoanTradeProduct_RecordStatus` | String |  |  |
| 26 | `LN.TRA.CURR.NO` | `LoanTradeProduct_CurrNo` | String |  |  |
| 27 | `LN.TRA.INPUTTER` | `LoanTradeProduct_Inputter` |  |  |  |
| 28 | `LN.TRA.DATE.TIME` | `LoanTradeProduct_DateTime` |  |  |  |
| 29 | `LN.TRA.AUTHORISER` | `LoanTradeProduct_Authoriser` | String |  |  |
| 30 | `LN.TRA.CO.CODE` | `LoanTradeProduct_CoCode` | String |  |  |
| 31 | `LN.TRA.DEPT.CODE` | `LoanTradeProduct_DeptCode` | String |  |  |
| 32 | `LN.TRA.AUDITOR.CODE` | `LoanTradeProduct_AuditorCode` | String |  |  |
| 33 | `LN.TRA.AUDIT.DATE.TIME` | `LoanTradeProduct_AuditDateTime` | String |  |  |
