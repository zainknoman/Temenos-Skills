# SC.MIFID.CLIENT.INFO — Table Schema

> Source: `INSERTS/I_F.SC.MIFID.CLIENT.INFO` in `SC_Mifid.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MIFID.CURRENCY` | `ScMifidClientInfo_Currency` | TField |  | Denotes the currency in which the amounts and values in this table are specified |
| 2 | `SC.MIFID.MIFID.REQUIRED` | `ScMifidClientInfo_MifidRequired` | TField |  | This Field Specifies whether Mifid Check is Required or not |
| 3 | `SC.MIFID.REVIEW.DATE` | `ScMifidClientInfo_ReviewDate` | TField |  | This Field Specifies the Date when lats Review was made |
| 4 | `SC.MIFID.REVIEW.FQNCY` | `ScMifidClientInfo_ReviewFqncy` | TField |  | Frequency field showing the frequency in which review needs to be made |
| 5 | `SC.MIFID.NEXT.REVIEW.DATE` | `ScMifidClientInfo_NextReviewDate` | TField |  | Date when next review is due. System will calculate based on review date and frequency |
| 6 | `SC.MIFID.AGE` | `ScMifidClientInfo_Age` | TField |  | This Field Specifies Customer's Age |
| 7 | `SC.MIFID.EDUCATION.LEVEL` | `ScMifidClientInfo_EducationLevel` | TField |  | Specifies the customer's highest level of Education This field should be linked to EB.LOOKUP with ID as MIFID.CLIENT.EDUCATION*LEV |
| 8 | `SC.MIFID.PROFESSION` | `ScMifidClientInfo_Profession` |  |  |  |
| 9 | `SC.MIFID.EXPERIENCE` | `ScMifidClientInfo_Experience` |  |  |  |
| 10 | `SC.MIFID.INCOME.SOURCE` | `ScMifidClientInfo_IncomeSource` |  |  |  |
| 11 | `SC.MIFID.AMT.INCOME` | `ScMifidClientInfo_AmtIncome` |  |  |  |
| 12 | `SC.MIFID.ASSETS.HELD` | `ScMifidClientInfo_AssetsHeld` |  |  |  |
| 13 | `SC.MIFID.VALUE.ASSETS` | `ScMifidClientInfo_ValueAssets` |  |  |  |
| 14 | `SC.MIFID.FIN.COMMIT` | `ScMifidClientInfo_FinCommit` |  |  |  |
| 15 | `SC.MIFID.VAL.FIN.COMMIT` | `ScMifidClientInfo_ValFinCommit` |  |  |  |
| 16 | `SC.MIFID.INVEST.AMOUNT` | `ScMifidClientInfo_InvestAmount` | TField |  | Indicates the initial investment amount of the customer This field is linked to EB.LOOKUP with ID as SC.MIFID.INV.AMT*AMT |
| 17 | `SC.MIFID.INVEST.PERIOD` | `ScMifidClientInfo_InvestPeriod` | TField |  | This Field Specifies Desired Investment Period This field is linked to EB.LOOKUP with ID as SC.MIFID.INV.AMT*AMT |
| 18 | `SC.MIFID.REG.PYMT.AMT` | `ScMifidClientInfo_RegPymtAmt` | TField |  | Field Specifies the regular amount that will be invested into the investment program by the customer |
| 19 | `SC.MIFID.REG.PAY.FREQ` | `ScMifidClientInfo_RegPayFreq` | TField |  | Defines the frequency of the regular investment amount This field is linked to EB.LOOKUP with ID as FREQUENCY.GENERAL |
| 20 | `SC.MIFID.REG.PAY.START.DATE` | `ScMifidClientInfo_RegPayStartDate` | TField |  | Defines the start date for when first regular payment will start |
| 21 | `SC.MIFID.REG.PAY.END.DATE` | `ScMifidClientInfo_RegPayEndDate` | TField |  | Defines the end date for the last regular payment |
| 22 | `SC.MIFID.INVESTMENT.OBJECTIVE` | `ScMifidClientInfo_InvestmentObjective` |  |  |  |
| 23 | `SC.MIFID.RISK.APPETITE` | `ScMifidClientInfo_RiskAppetite` | TField |  | Defines the level of risk that a customer is willing to take This Field is linked to EB.LOOKUP with ID as AM.MIFID.RISK |
| 24 | `SC.MIFID.EXPECT.RETURN` | `ScMifidClientInfo_ExpectReturn` | TField |  | Specifies the annual return that is expected by the customer |
| 25 | `SC.MIFID.TRANS.ACTIVITIES` | `ScMifidClientInfo_TransActivities` |  |  |  |
| 26 | `SC.MIFID.TRANS.VOL` | `ScMifidClientInfo_TransVol` |  |  |  |
| 27 | `SC.MIFID.TRANS.FREQ` | `ScMifidClientInfo_TransFreq` |  |  |  |
| 28 | `SC.MIFID.TRANS.PERIOD` | `ScMifidClientInfo_TransPeriod` | TField |  | This field relates to the TRANS.ACTIVITIES and indicates the period for which the transactions have taken place This Field is linked to EB.LOOKUP with ID as MIFID.TRANS.PERIOD |
| 29 | `SC.MIFID.BONDS` | `ScMifidClientInfo_Bonds` | TField |  | Indicates the customer's knowledge level in Bonds including Money Market This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 30 | `SC.MIFID.MONEY.MARKET.INSTRUMENTS` | `ScMifidClientInfo_MoneyMarketInstruments` | TField |  | Indicates the customer's knowledge level in Money Market instruments This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 31 | `SC.MIFID.FIXED.DEPOSITS` | `ScMifidClientInfo_FixedDeposits` | TField |  | This field shows the customer's level of knowledge in Fixed Deposits This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 32 | `SC.MIFID.SHARES` | `ScMifidClientInfo_Shares` | TField |  | Specifies the customer's knowledge level in Shares/Equity This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 33 | `SC.MIFID.MUTUAL.FUNDS` | `ScMifidClientInfo_MutualFunds` | TField |  | Indicates the customer's knowledge level in Mutual Funds This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 34 | `SC.MIFID.HEDGE.FUNDS` | `ScMifidClientInfo_HedgeFunds` | TField |  | Indicates the customer's knowledge level in Hedge Funds This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 35 | `SC.MIFID.PVT.EQUITY` | `ScMifidClientInfo_PvtEquity` | TField |  | This filed shows the customer's level of knowledge in Private Equity and other unquoted products This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 36 | `SC.MIFID.STRUCTURED.PRDS` | `ScMifidClientInfo_StructuredPrds` | TField |  | Specifies the customer's knowledge level in Structured Products This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 37 | `SC.MIFID.WARRANTS` | `ScMifidClientInfo_Warrants` | TField |  | Indicates the customer's knowledge level in Warrants This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 38 | `SC.MIFID.DERIVATIVES` | `ScMifidClientInfo_Derivatives` | TField |  | This field shows the customer's level of knowledge in Derivatives. This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 39 | `SC.MIFID.METALS.COMMO` | `ScMifidClientInfo_MetalsCommo` | TField |  | Indicates the customer's knowledge level in Metals and Commodities. This Field is linked to EB.LOOKUP with ID as MIFID.KNOWLEDGE.INFO*KNOW4 |
| 40 | `SC.MIFID.ASSET.CLASS` | `ScMifidClientInfo_AssetClass` |  |  |  |
| 41 | `SC.MIFID.KNOW.ASSET.CLASS` | `ScMifidClientInfo_KnowAssetClass` |  |  |  |
| 42 | `SC.MIFID.CLASSIFICATION` | `ScMifidClientInfo_Classification` | TField |  | MiFID Category of the client : RETAIL PROFESSIONAL PROFESSIONAL.ON.REQUEST ELIGIBLE.COUNTERPARTY |
| 43 | `SC.MIFID.REQUEST.DATE` | `ScMifidClientInfo_RequestDate` | TField |  | Indicates the date on which the client�s request to be classified as professional has been received |
| 44 | `SC.MIFID.BEST.EXE.MANDATE.STATUS` | `ScMifidClientInfo_BestExeMandateStatus` | TField |  | Indicates the status of the client�s approval on the mandate shared This Field is linked to EB.LOOKUP with ID as MIFID.MANDATE.STATUS |
| 45 | `SC.MIFID.RISK.PROFILE` | `ScMifidClientInfo_RiskProfile` | TField |  |  |
| 46 | `SC.MIFID.SUB.ASSET.CLASS` | `ScMifidClientInfo_SubAssetClass` |  |  |  |
| 47 | `SC.MIFID.KNOW.SUB.ASSET.CLASS` | `ScMifidClientInfo_KnowSubAssetClass` |  |  |  |
| 48 | `SC.MIFID.QUESTION.ID` | `ScMifidClientInfo_QuestionId` |  |  |  |
| 49 | `SC.MIFID.QUESTION` | `ScMifidClientInfo_Question` |  |  |  |
| 50 | `SC.MIFID.ANSWERS` | `ScMifidClientInfo_Answers` |  |  |  |
| 51 | `SC.MIFID.SCORE.ID` | `ScMifidClientInfo_ScoreId` |  |  |  |
| 52 | `SC.MIFID.SYS.POINTS` | `ScMifidClientInfo_SysPoints` |  |  |  |
| 53 | `SC.MIFID.POINTS` | `ScMifidClientInfo_Points` |  |  |  |
| 54 | `SC.MIFID.TOTAL.POINTS` | `ScMifidClientInfo_TotalPoints` | TField |  | This field contains sum of points from all scoreId Validation Rules: This will be NOINPUT field |
| 55 | `SC.MIFID.SYS.INVESTMENT.PGM` | `ScMifidClientInfo_SysInvestmentPgm` | TField |  | This field contains investment program determined by system based on the total points Validation Rules: This will be NOINPUT field |
| 56 | `SC.MIFID.CHOSEN.INVESTMENT.PGM` | `ScMifidClientInfo_ChosenInvestmentPgm` | TField |  | This field contains user inputed investment program will be defaulted to SEC.ACC.MASTER if left blank then value from SYS.INVESTMENT.PGM will be defaulted Validation Rules: valid INVESTMENT.PROGRAM |
| 57 | `SC.MIFID.LIQUIDITY` | `ScMifidClientInfo_Liquidity` | TField |  | This field refers to the ability of clients to access their investment and/or exit the investment early. Validation Rules: Input to this field accepts valid record from EB.LOOKUP table whose id starts with LIQUIDITY*Text |
| 58 | `SC.MIFID.LOSS.TOLERANCE` | `ScMifidClientInfo_LossTolerance` | TField |  | This field indicates whether the product is designed to offer capital protection i.e. no tolerance for loss or subject to any risk of potential loss. Validation Rules: Input to this field accepts valid record from EB.LOOKUP table whose id starts with LOSS.TOL*Text Common categories are: 'No tolerance for loss' ,'Moderate loss', 'Large loss', 'More than total loss'. Wealth suite clients should set Lookup values with ^ separator to separate the Indicator Value from Indicator Attribute eg: Retail^Yes |
| 59 | `SC.MIFID.RESERVED15` | `ScMifidClientInfo_Reserved15` | TField |  |  |
| 60 | `SC.MIFID.RESERVED16` | `ScMifidClientInfo_Reserved16` | TField |  |  |
| 61 | `SC.MIFID.RESERVED17` | `ScMifidClientInfo_Reserved17` | TField |  |  |
| 62 | `SC.MIFID.RESERVED18` | `ScMifidClientInfo_Reserved18` | TField |  |  |
| 63 | `SC.MIFID.RESERVED19` | `ScMifidClientInfo_Reserved19` | TField |  |  |
| 64 | `SC.MIFID.RESERVED20` | `ScMifidClientInfo_Reserved20` | TField |  |  |
| 65 | `SC.MIFID.LOCAL.REF` | `ScMifidClientInfo_LocalRef` |  |  |  |
| 66 | `SC.MIFID.OVERRIDE` | `ScMifidClientInfo_Override` |  |  |  |
| 67 | `SC.MIFID.RECORD.STATUS` | `ScMifidClientInfo_RecordStatus` | String |  |  |
| 68 | `SC.MIFID.CURR.NO` | `ScMifidClientInfo_CurrNo` | String |  |  |
| 69 | `SC.MIFID.INPUTTER` | `ScMifidClientInfo_Inputter` |  |  |  |
| 70 | `SC.MIFID.DATE.TIME` | `ScMifidClientInfo_DateTime` |  |  |  |
| 71 | `SC.MIFID.AUTHORISER` | `ScMifidClientInfo_Authoriser` | String |  |  |
| 72 | `SC.MIFID.CO.CODE` | `ScMifidClientInfo_CoCode` | String |  |  |
| 73 | `SC.MIFID.DEPT.CODE` | `ScMifidClientInfo_DeptCode` | String |  |  |
| 74 | `SC.MIFID.AUDITOR.CODE` | `ScMifidClientInfo_AuditorCode` | String |  |  |
| 75 | `SC.MIFID.AUDIT.DATE.TIME` | `ScMifidClientInfo_AuditDateTime` | String |  |  |
| 76 | `SC.MIFID.ASSET.TYPE` | `ScMifidClientInfo_AssetType` |  |  |  |
| 77 | `SC.MIFID.SUB.ASSET.TYPE` | `ScMifidClientInfo_SubAssetType` |  |  |  |
