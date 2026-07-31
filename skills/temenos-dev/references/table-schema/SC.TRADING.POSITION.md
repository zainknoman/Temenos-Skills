# SC.TRADING.POSITION — Table Schema

> Source: `INSERTS/I_F.SC.TRADING.POSITION` in `SC_SctDealerBookPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TRP.DEALER.BOOK` | `ScTradingPosition_DealerBook` | TField |  | Defines the Security Account Number portion of the key, together with the Short Name Description. Validation Rules: Non Input Field. |
| 2 | `SC.TRP.SECURITY.CODE` | `ScTradingPosition_SecurityCode` | TField |  | Defines the Security Code portion of the key, together with the Short Name. Validation Rules: Non Input Field. |
| 3 | `SC.TRP.SECURITY.CCY` | `ScTradingPosition_SecurityCcy` | TField |  | Specifies the Currency of the Security traded. Validation Rules: Non Input Field. |
| 4 | `SC.TRP.SETTLEMENT.CCY` | `ScTradingPosition_SettlementCcy` | TField |  | Specifies the Settlement Currency of the security traded. Validation Rules: Non Input Field. |
| 5 | `SC.TRP.CURRENT.POSITION` | `ScTradingPosition_CurrentPosition` | TField |  | Specifies the Current Position in the designated security. This is provided on-line and includes the start of period position plus all transactions up to the present. Validation Rules: Non Input Field. |
| 6 | `SC.TRP.CUR.AVG.PRICE` | `ScTradingPosition_CurAvgPrice` | TField |  | Specifies the Current Average Price of the security. This is provided on-line and is the average of the start of period average price plus the prices of all transactions up to the present. Validation Rules: Non Input Field. |
| 7 | `SC.TRP.CUR.COST.POSITION` | `ScTradingPosition_CurCostPosition` | TField |  | Specifies the Current Cost of Position for the designated security. This is provided on-line and includes the start of period cost of position plus the cost of all transactions up to the present position. Validation Rules: Non Input Field. |
| 8 | `SC.TRP.CPN.ACCR.POSTED` | `ScTradingPosition_CpnAccrPosted` | TField |  | Specifies the Current Accrual IENC Balance that has accrued on the designated security. Validation Rules: Non Input Field. |
| 9 | `SC.TRP.TAX.BALANCE` | `ScTradingPosition_TaxBalance` | TField |  | Specifies the Current Accrual Repo IENC Balance that has accrued on the particular security to date. Validation Rules: Non Input Field. This field is reserved for future use. |
| 10 | `SC.TRP.DISCOUNT.ACCRUED` | `ScTradingPosition_DiscountAccrued` | TField |  | Specifies the Discount Accrual IENC Balance that has accrued on the particular security to date. This is the -ve of discount provision to date. Validation Rules: Non Input Field. |
| 11 | `SC.TRP.CONSOL.TRADING.BAL` | `ScTradingPosition_ConsolTradingBal` | TField |  | Specifies the Consolidation Asset Balance of the designated security. Validation Rules: Non Input Field. |
| 12 | `SC.TRP.CONTINGENT.BAL.CR` | `ScTradingPosition_ContingentBalCr` | TField |  | Specifies the Consolidation Contingent Credit Balance of the designated security. Validation Rules: Non Input Field. This field is reserved for future use. |
| 13 | `SC.TRP.CONTINGENT.BAL.DB` | `ScTradingPosition_ContingentBalDb` | TField |  | Specifies the Consolidation Contingent Debit Balance of the designated security. Validation Rules: Non Input Field. This field is reserved for future use. |
| 14 | `SC.TRP.CUR.REALIZED.PL` | `ScTradingPosition_CurRealizedPl` | TField |  | Specifies the Current Realized Profit/Loss on the particular security. Validation Rules: Non Input Field. |
| 15 | `SC.TRP.DISC.ACCR.POSTED` | `ScTradingPosition_DiscAccrPosted` | TField | Yes | Validation Rules: Mandatory input. A maximum of 18 characters may be entered. |
| 16 | `SC.TRP.VALUE.DATE` | `ScTradingPosition_ValueDate` |  |  |  |
| 17 | `SC.TRP.NET.OPEN.NOM` | `ScTradingPosition_NetOpenNom` |  |  |  |
| 18 | `SC.TRP.NET.OPEN.CONSID` | `ScTradingPosition_NetOpenConsid` |  |  |  |
| 19 | `SC.TRP.NET.OPEN.ACCR` | `ScTradingPosition_NetOpenAccr` |  |  |  |
| 20 | `SC.TRP.VALUE.DATED.POS` | `ScTradingPosition_ValueDatedPos` | TField |  | Specifies the amount of the Value Dated Position. Calculated as Current Position less all Net Open Nominals. Validation Rules: Non Input Field. |
| 21 | `SC.TRP.V.DATE.COST.OF.POS` | `ScTradingPosition_VDateCostOfPos` | TField |  | Specifies the amount of the Value Dated Cost of Position. Calculated as Current Cost of Position less all Net Open Considerations. Validation Rules: Non Input Field. |
| 22 | `SC.TRP.V.DATED.CPN.ACCR` | `ScTradingPosition_VDatedCpnAccr` | TField |  | Specifies the daily accrual balance for this security position. Validation Rules: Non Input Field. |
| 23 | `SC.TRP.V.DATE.REAL.PROFIT` | `ScTradingPosition_VDateRealProfit` | TField |  | The field holds the value dated realized profit/loss of the position. Validation Rules: NoInput Field. |
| 24 | `SC.TRP.V.DATED.DISC.PREM` | `ScTradingPosition_VDatedDiscPrem` | TField |  | Specifies the discount/premium of the value dated position. Validation Rules: Non Input Field. |
| 25 | `SC.TRP.V.DATED.YLD.TO.MAT` | `ScTradingPosition_VDatedYldToMat` | TField |  | This field will display an Average Yield which is derived from the yields on the transactions. The system will use the average price concept to derive the average yield of the position. The rules are as follows: 1. If position changes from 'long to short' or 'short to long' then use the yield on the new trade; else 2. if 'buy on short' or 'sell on long' then use the current average yield on the position; 3. otherwise work out the new average yield by using the true cost of position where true cost of pos = value dated cost of pos - discount provision Validation Rules: No input field. |
| 26 | `SC.TRP.V.DATED.DIS.ACC` | `ScTradingPosition_VDatedDisAcc` |  |  |  |
| 27 | `SC.TRP.AMORTISED.AMOUNT` | `ScTradingPosition_AmortisedAmount` | TField |  | The amortised amount of the compound discount/premium from the following formula: ((1+Yield)**(Ndays/YD)) - 1 AMORT = DISC.PREM * (---------------------------) ((1+Yield)**(DM/YD)) - 1 where Yield - value dated yield to maturity Ndays - Number of days to amortise DM - Days to maturity YD - Year days Validation Rules: No Input Field. |
| 28 | `SC.TRP.HISTORIC.DISC.ACCR` | `ScTradingPosition_HistoricDiscAccr` | TField |  | This field holds the discount accrual prior to the Euro Security redenomination. |
| 29 | `SC.TRP.EX.DIV.ACCR.DET` | `ScTradingPosition_ExDivAccrDet` |  |  |  |
| 30 | `SC.TRP.DATE` | `ScTradingPosition_Date` |  |  |  |
| 31 | `SC.TRP.CPN.ACCR` | `ScTradingPosition_CpnAccr` |  |  |  |
| 32 | `SC.TRP.COUPON.DATE` | `ScTradingPosition_CouponDate` | TField |  | Specifies the date the Coupon was calculated and posted to the Accounting System. Validation Rules: Non Input Field. |
| 33 | `SC.TRP.COUPON.AMOUNT` | `ScTradingPosition_CouponAmount` | TField |  | Specifies the amount of Coupon that was posted to the Accounting System. Validation Rules: Non Input Field. |
| 34 | `SC.TRP.DIFFERENCE.AMOUNT` | `ScTradingPosition_DifferenceAmount` | TField |  | Specifies any coupon difference amount that was posted to the Accounting System, in order to zeroise the IENC balance. Validation Rules: Non Input Field. |
| 35 | `SC.TRP.SETTLED.POSITION` | `ScTradingPosition_SettledPosition` | TField |  | Specifies the amount of the Settled Position in the particular security. Validation Rules: Non Input Field. This field is reserved for future use. |
| 36 | `SC.TRP.COST.OF.SET.POS` | `ScTradingPosition_CostOfSetPos` | TField |  | Specifies the Cost of the Settled Position. Validation Rules: Non Input Field. This field is reserved for future use. |
| 37 | `SC.TRP.FUNDING.AMOUNT` | `ScTradingPosition_FundingAmount` | TField |  | Specifies the Amount of Funding required for the existing position. Validation Rules: Non Input Field. This field is reserved for future use. |
| 38 | `SC.TRP.DATE.LAST.TRADED` | `ScTradingPosition_DateLastTraded` | TField |  | Specifies the Date that the security was last Traded. Validation Rules: Non Input Field. |
| 39 | `SC.TRP.LAST.TRADE.PRICE` | `ScTradingPosition_LastTradePrice` | TField |  | Specifies the last trade price that was used during Trade Input. Validation Rules: Non Input Field. |
| 40 | `SC.TRP.CONSOL.KEY` | `ScTradingPosition_ConsolKey` | TField |  | Defines the Key to the Consolidation entry record. Validation Rules: Non Input Field. |
| 41 | `SC.TRP.REVALUATION.DATE` | `ScTradingPosition_RevaluationDate` | TField |  | Specifies the Date of the last Revaluation. Validation Rules: Non Input Field. |
| 42 | `SC.TRP.REVAL.UNREAL.PL` | `ScTradingPosition_RevalUnrealPl` | TField |  | Specifies the amount of the Revalued Unrealized Profit/Loss. Validation Rules: Non Input Field. |
| 43 | `SC.TRP.REVAL.UNREAL.P.LCY` | `ScTradingPosition_RevalUnrealPLcy` | TField |  | Specifies the amount of the Revalued Unrealized Profit/Loss in the Local Currency. Validation Rules: Non Input Field. |
| 44 | `SC.TRP.TRD.REF` | `ScTradingPosition_TrdRef` |  |  |  |
| 45 | `SC.TRP.TRD.TRANS.TYPE` | `ScTradingPosition_TrdTransType` |  |  |  |
| 46 | `SC.TRP.TRD.NOMINAL` | `ScTradingPosition_TrdNominal` |  |  |  |
| 47 | `SC.TRP.TRD.CLEAN.PRC` | `ScTradingPosition_TrdCleanPrc` |  |  |  |
| 48 | `SC.TRP.TRD.CONSID` | `ScTradingPosition_TrdConsid` |  |  |  |
| 49 | `SC.TRP.TRD.ACCR.INT` | `ScTradingPosition_TrdAccrInt` |  |  |  |
| 50 | `SC.TRP.TRD.VALUE.DATE` | `ScTradingPosition_TrdValueDate` |  |  |  |
| 51 | `SC.TRP.TRD.DISC.ACCR` | `ScTradingPosition_TrdDiscAccr` |  |  |  |
| 52 | `SC.TRP.TRD.YLD.TO.MAT` | `ScTradingPosition_TrdYldToMat` |  |  |  |
| 53 | `SC.TRP.TRD.DISC.PREM` | `ScTradingPosition_TrdDiscPrem` |  |  |  |
| 54 | `SC.TRP.TRD.DIS.PRV.ADJ` | `ScTradingPosition_TrdDisPrvAdj` |  |  |  |
| 55 | `SC.TRP.TRD.GR.REAL.PL` | `ScTradingPosition_TrdGrRealPl` |  |  |  |
| 56 | `SC.TRP.TRD.POS.DATETME` | `ScTradingPosition_TrdPosDatetme` |  |  |  |
| 57 | `SC.TRP.TRD.CAP.INT.AMT` | `ScTradingPosition_TrdCapIntAmt` |  |  |  |
| 58 | `SC.TRP.STATEMENT.NO` | `ScTradingPosition_StatementNo` |  |  |  |
| 59 | `SC.TRP.OVERRIDE` | `ScTradingPosition_Override` |  |  |  |
| 60 | `SC.TRP.ISSUER` | `ScTradingPosition_Issuer` | TField |  | Issuer from security details. |
| 61 | `SC.TRP.LIMIT.REFERENCE` | `ScTradingPosition_LimitReference` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 35 characters may be entered. |
| 62 | `SC.TRP.CAP.INT.AMT` | `ScTradingPosition_CapIntAmt` | TField |  | This field holds the capitalised interest amount for the dealer book portfolio. This field will be re-valued every day in accordance with the daily increases and market price. Validation Rules: No Input Allowed |
| 63 | `SC.TRP.REVALUATION.PRICE` | `ScTradingPosition_RevaluationPrice` | TField |  | This field holds the lowest recorded market price for the security of this holding. The field is cleared if the nominal of the holding is returned to zero. It is used for the revaluation of dealer books that have the POST.UNREAL.PL field set to RVAL. |
| 64 | `SC.TRP.POST.UNREAL.PL` | `ScTradingPosition_PostUnrealPl` | TField |  | Unrealised P&amp;L. |
| 65 | `SC.TRP.CONT.REAL.PL` | `ScTradingPosition_ContRealPl` | TField |  | This field contains the value of Contingent P/L. It represents the P/L of trades which are forward valued dated.The value in this field will reduced on the value date. The amount in this field is represented in the Trade Currency. Validation Rules: None |
| 66 | `SC.TRP.CONT.REAL.PL.LCY` | `ScTradingPosition_ContRealPlLcy` | TField |  | This field contains the value of Contingent P/L. It represents the P/L of trades which are forward valued dated.The value in this field will reduced on the value date. The amount in this field is represented in the Local Currency. Validation Rules: None |
| 67 | `SC.TRP.LAST.COB.TXNS.DATE` | `ScTradingPosition_LastCobTxnsDate` | TField |  | Date of COB entered transactions, non-stop processing only. |
| 68 | `SC.TRP.LAST.COB.TXNS` | `ScTradingPosition_LastCobTxns` |  |  |  |
| 69 | `SC.TRP.CONT.INT.PAID` | `ScTradingPosition_ContIntPaid` | TField |  | Currently not updated by the T24 core system. |
| 70 | `SC.TRP.CONT.INT.RECD` | `ScTradingPosition_ContIntRecd` | TField |  | Currently not updated by the T24 core system. |
| 71 | `SC.TRP.CONT.DISCOUNT` | `ScTradingPosition_ContDiscount` | TField |  | Currently not updated by the T24 core system. |
| 72 | `SC.TRP.CONT.CAP.INT.PAID` | `ScTradingPosition_ContCapIntPaid` | TField |  | Currently not updated by the T24 core system. |
| 73 | `SC.TRP.CONT.CAP.INT.RECD` | `ScTradingPosition_ContCapIntRecd` | TField |  | Currently not updated by the T24 core system. |
| 74 | `SC.TRP.CONT.BELG.TAX` | `ScTradingPosition_ContBelgTax` | TField |  | Currently not updated by the T24 core system. |
| 75 | `SC.TRP.CONSOL.TRD.BAL.LCY` | `ScTradingPosition_ConsolTrdBalLcy` | TField |  | This field will hold the sum of local currency equivalent of the entries raised against LIVEDB/LIVECR bucket.(i.e. Entries that will update CONSOL.TRADING.BAL field) |
| 76 | `SC.TRP.FX.REVAL.LCY` | `ScTradingPosition_FxRevalLcy` | TField |  | Currency revaluation amount posted in local currency. |
| 77 | `SC.TRP.ORIG.IMPAIR.AMT` | `ScTradingPosition_OrigImpairAmt` | TField |  | This field specfies the highest loss of Impairment |
| 78 | `SC.TRP.CURR.IMPAIR.AMT` | `ScTradingPosition_CurrImpairAmt` | TField |  | This field specifies the current Impairment loss |
| 79 | `SC.TRP.CUR.IMPAIR.AMT.LCY` | `ScTradingPosition_CurImpairAmtLcy` | TField |  | This field specifies the current impairment loss in local currency |
| 80 | `SC.TRP.EFF.INT.RATE` | `ScTradingPosition_EffIntRate` | TField |  | This field is used to hold EIR(EFFECTIVE INTEERSET RATE |
| 81 | `SC.TRP.NET.COST.POSITION` | `ScTradingPosition_NetCostPosition` | TField |  | This field holds the net cost of the position unadjusted for inflation. This is calculated as ,(Nominal * Price of the bond)/ Inflation index at the time of purchase, where price represents the clean price of the bond Validation Rules: No Input Allowed |
