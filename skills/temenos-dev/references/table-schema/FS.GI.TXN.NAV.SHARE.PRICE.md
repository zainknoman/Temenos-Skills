# FS.GI.TXN.NAV.SHARE.PRICE — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.NAV.SHARE.PRICE` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.NAV.SHARE.PRICE.PARENT.REF.ID` | `FsGiTxnNavSharePrice_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.NAV.SHARE.PRICE.ORA.ROWID` | `FsGiTxnNavSharePrice_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.NAV.SHARE.PRICE.TA.FUND.ID` | `FsGiTxnNavSharePrice_TaFundId` | TField |  | Fund internal ID for which NAV is defined. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.TXN.NAV.SHARE.PRICE.SHARE.CLASS.CODE` | `FsGiTxnNavSharePrice_ShareClassCode` | TField |  | Fund share class. Multifonds DB Column is TPART. |
| 5 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.DATE` | `FsGiTxnNavSharePrice_NavDate` | TField |  | Date on which the NAV per share prices are applicable. Multifonds DB Column is NAVDATE. |
| 6 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.BASIS` | `FsGiTxnNavSharePrice_NavBasis` | TField |  | Price Basis retreived based on valuation method from MF Fund used for Dual priced funds. Multifonds DB Column is PRICE_BASIS. |
| 7 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.CREATION` | `FsGiTxnNavSharePrice_NavCreation` | TField |  | Creation NAV price is used when agent is dealing at the creation price for dual priced funds. Multifonds DB Column is CREATION_PRICE. |
| 8 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.CANCEL` | `FsGiTxnNavSharePrice_NavCancel` | TField |  | Cancellation NAV price used for dual priced funds. Multifonds DB Column is CANCEL_PRICE. |
| 9 | `FS.GI.TXN.NAV.SHARE.PRICE.MAX.OFFER.NAV` | `FsGiTxnNavSharePrice_MaxOfferNav` | TField |  | Maximum NAV offer price for the fund and share class. Multifonds DB Column is MAX_OFFER_PRICE. |
| 10 | `FS.GI.TXN.NAV.SHARE.PRICE.MAX.OFFER.NAV.CALC` | `FsGiTxnNavSharePrice_MaxOfferNavCalc` | TField |  | Maximum calculated offer price for the fund and share class. Multifonds DB Column is MAX_OFFER_CALC. |
| 11 | `FS.GI.TXN.NAV.SHARE.PRICE.MIN.BID.NAV` | `FsGiTxnNavSharePrice_MinBidNav` | TField |  | Minimum NAV bid price for the fund and share class. Multifonds DB Column is MIN_BID_PRICE. |
| 12 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.SUB` | `FsGiTxnNavSharePrice_NavSub` | TField |  | Share price used for subscription. Multifonds DB Column is PRICE_PART_SUB. |
| 13 | `FS.GI.TXN.NAV.SHARE.PRICE.OFFER.NAV.CALC` | `FsGiTxnNavSharePrice_OfferNavCalc` | TField |  | Offer price calculated. Multifonds DB Column is QUOTED_OFFER_PRICE. |
| 14 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.RED` | `FsGiTxnNavSharePrice_NavRed` | TField |  | Share price used for redemption. Multifonds DB Column is PRICE_PART_RED. |
| 15 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.PRICE` | `FsGiTxnNavSharePrice_NavPrice` | TField |  | Share price, user definable for up to 6 decimals. The number of decimals should follow the TA fund set up in field Share price decimals. Multifonds DB Column is UNIT_PRICE. |
| 16 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.SUB.LEGAL.ENTITY` | `FsGiTxnNavSharePrice_NavSubLegalEntity` | TField |  | It specifies the subscription price officially published by the Legal Entity. Multifonds DB Column is TFC_SUB_PRICE. |
| 17 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.RED.LEGAL.ENTITY` | `FsGiTxnNavSharePrice_NavRedLegalEntity` | TField |  | It specifies the redemption price officially published by the Legal Entity. Multifonds DB Column is TFC_RED_PRICE. |
| 18 | `FS.GI.TXN.NAV.SHARE.PRICE.SHARE.PROFIT` | `FsGiTxnNavSharePrice_ShareProfit` | TField |  | It specifes the fiscal details (share profit) provided by the Legal Entity. Multifonds DB Column is SHARE_PROFIT. |
| 19 | `FS.GI.TXN.NAV.SHARE.PRICE.ACCUM.FISCAL.INCOME` | `FsGiTxnNavSharePrice_AccumFiscalIncome` | TField |  | Accumulated fiscal income details published by the Legal Entity. Multifonds DB Column is ACC_FISCAL_INCOME. |
| 20 | `FS.GI.TXN.NAV.SHARE.PRICE.DAILY.DIVIDEND.RATE` | `FsGiTxnNavSharePrice_DailyDividendRate` | TField |  | Daily dividend rate per share. Multifonds DB Column is MNT_DLY_DIVIDEND. |
| 21 | `FS.GI.TXN.NAV.SHARE.PRICE.RNI.SHARE` | `FsGiTxnNavSharePrice_RniShare` | TField |  | It specifies profit gain considered for German taxation when the Equalization code at the TA fund level is 000 - RNI part. Multifonds DB Column is RNI_PART. |
| 22 | `FS.GI.TXN.NAV.SHARE.PRICE.INTERIM.PROFIT` | `FsGiTxnNavSharePrice_InterimProfit` | TField |  | Interim profit gain considered for German taxation when the Equalization code at the TA fund level is 0002 - Interim profit/German tax part. Multifonds DB Column is ZWIST_PART. |
| 23 | `FS.GI.TXN.NAV.SHARE.PRICE.CAP.GAIN.SHARE` | `FsGiTxnNavSharePrice_CapGainShare` | TField |  | Profit earned on the sale of the units. Multifonds DB Column is GAIN_CAP_PART. |
| 24 | `FS.GI.TXN.NAV.SHARE.PRICE.EQUITY.PROFIT.GAIN.1` | `FsGiTxnNavSharePrice_EquityProfitGain1` | TField |  | Equity profit gain from shares considered for German taxation when the Equalization code at the TA fund level is 0003 - Gain cap part. Multifonds DB Column is AKTIEN_PART. |
| 25 | `FS.GI.TXN.NAV.SHARE.PRICE.EQUITY.PROFIT.GAIN.2` | `FsGiTxnNavSharePrice_EquityProfitGain2` | TField |  | Equity Profit Gain2 for GermanTax. Multifonds DB Column is AKTIEN_PART_CORP. |
| 26 | `FS.GI.TXN.NAV.SHARE.PRICE.IMMOBILIENGEWINN` | `FsGiTxnNavSharePrice_Immobiliengewinn` | TField |  | Real estate profit for German Tax. Multifonds DB Column is IMMOBILIENGEWINN_PART. |
| 27 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.GERMAN.TAX` | `FsGiTxnNavSharePrice_AssetTestGermanTax` | TField | Yes | Asset Test German Tax. This becomes mandatory when Tax regime os the MF fund chosen as &apos;03 - German Tax Mutual Fund&apos;. Multifonds DB Column is ASSET_TEST_GT. |
| 28 | `FS.GI.TXN.NAV.SHARE.PRICE.TG.1` | `FsGiTxnNavSharePrice_Tg1` | TField |  | Asset Test 1 use in calculation of German Tax. Multifonds DB Column is TG1. |
| 29 | `FS.GI.TXN.NAV.SHARE.PRICE.TG.2` | `FsGiTxnNavSharePrice_Tg2` | TField |  | Asset Test 2 use in calculation of German Tax. Multifonds DB Column is TG2. |
| 30 | `FS.GI.TXN.NAV.SHARE.PRICE.TG.3` | `FsGiTxnNavSharePrice_Tg3` | TField |  | Asset Test 3 use in calculation of German Tax. Multifonds DB Column is TG3. |
| 31 | `FS.GI.TXN.NAV.SHARE.PRICE.CONVERSION.FACTOR` | `FsGiTxnNavSharePrice_ConversionFactor` | TField |  | Price conversion factor. Multifonds DB Column is ACCU_FACTOR. |
| 32 | `FS.GI.TXN.NAV.SHARE.PRICE.FA.VALUATION.DATE` | `FsGiTxnNavSharePrice_FaValuationDate` | TField |  | It specifies the date for which the the prices are picked for Retro calculations. Multifonds DB Column is DREALNAV. |
| 33 | `FS.GI.TXN.NAV.SHARE.PRICE.TISR` | `FsGiTxnNavSharePrice_Tisr` | TField |  | Taxable income per share rate. Multifonds DB Column is TISR. |
| 34 | `FS.GI.TXN.NAV.SHARE.PRICE.TISD` | `FsGiTxnNavSharePrice_Tisd` | TField |  | Taxable interest amount per share. Multifonds DB Column is TISD. |
| 35 | `FS.GI.TXN.NAV.SHARE.PRICE.SWISS.TIS` | `FsGiTxnNavSharePrice_SwissTis` | TField |  | Taxable income per share. Multifonds DB Column is TIS_1. |
| 36 | `FS.GI.TXN.NAV.SHARE.PRICE.TOTAL.TAXABLE.INCOME` | `FsGiTxnNavSharePrice_TotalTaxableIncome` | TField |  | Total taxable income received from fund accounting. Multifonds DB Column is TOTAL_TI. |
| 37 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.1` | `FsGiTxnNavSharePrice_Tis1` | TField |  | Taxable income per share 1 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS1. |
| 38 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.1` | `FsGiTxnNavSharePrice_AssetTest1` | TField |  | Asset Test 1 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST1. |
| 39 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.2` | `FsGiTxnNavSharePrice_Tis2` | TField |  | Taxable income per share 2 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS2. |
| 40 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.2` | `FsGiTxnNavSharePrice_AssetTest2` | TField |  | Asset Test 2 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST2. |
| 41 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.3` | `FsGiTxnNavSharePrice_Tis3` | TField |  | Taxable income per share 3 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS3. |
| 42 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.3` | `FsGiTxnNavSharePrice_AssetTest3` | TField |  | Asset Test 3 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST3. |
| 43 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.4` | `FsGiTxnNavSharePrice_Tis4` | TField |  | Taxable income per share 4 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS4. |
| 44 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.4` | `FsGiTxnNavSharePrice_AssetTest4` | TField |  | Asset Test 4 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST4. |
| 45 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.5` | `FsGiTxnNavSharePrice_Tis5` | TField |  | Taxable income per share 5 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS5. |
| 46 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.5` | `FsGiTxnNavSharePrice_AssetTest5` | TField |  | Asset Test 5 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST5. |
| 47 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.6` | `FsGiTxnNavSharePrice_Tis6` | TField |  | Taxable income per share 6 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS6. |
| 48 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.6` | `FsGiTxnNavSharePrice_AssetTest6` | TField |  | Asset Test 6 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST6. |
| 49 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.7` | `FsGiTxnNavSharePrice_Tis7` | TField |  | Taxable income per share 7 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS7. |
| 50 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.7` | `FsGiTxnNavSharePrice_AssetTest7` | TField |  | Asset Test 7 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST7. |
| 51 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.8` | `FsGiTxnNavSharePrice_Tis8` | TField |  | Taxable income per share 8 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS8. |
| 52 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.8` | `FsGiTxnNavSharePrice_AssetTest8` | TField |  | Asset Test 8 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST8. |
| 53 | `FS.GI.TXN.NAV.SHARE.PRICE.TIS.9` | `FsGiTxnNavSharePrice_Tis9` | TField |  | Taxable income per share 9 use to calculate Belgum Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is TIS9. |
| 54 | `FS.GI.TXN.NAV.SHARE.PRICE.ASSET.TEST.9` | `FsGiTxnNavSharePrice_AssetTest9` | TField |  | Asset Test 9 use to calulate Belgian Tax if parameterize for an event when the tax basis is Belgian TIS logic (1) or (2). Multifonds DB Column is ASSET_TEST9. |
| 55 | `FS.GI.TXN.NAV.SHARE.PRICE.GROSS.NAV` | `FsGiTxnNavSharePrice_GrossNav` | TField |  | Gross NAV used for series of shares funds. Multifonds DB Column is NAV_GROSS. |
| 56 | `FS.GI.TXN.NAV.SHARE.PRICE.GAV` | `FsGiTxnNavSharePrice_Gav` | TField |  | Gross NAV per share. Multifonds DB Column is GAV_PER_SHARE. |
| 57 | `FS.GI.TXN.NAV.SHARE.PRICE.TOTAL.GAV` | `FsGiTxnNavSharePrice_TotalGav` | TField |  | Total Gross NAV of the unit type used during performance fee calculation. Multifonds DB Column is TOTAL_GAV. |
| 58 | `FS.GI.TXN.NAV.SHARE.PRICE.SWUNG.NAV` | `FsGiTxnNavSharePrice_SwungNav` | TField |  | Swung NAV used for ADL SSP calculations. Multifonds DB Column is SWUNG_PRICE. |
| 59 | `FS.GI.TXN.NAV.SHARE.PRICE.SSP.PROCESS.STATUS` | `FsGiTxnNavSharePrice_SspProcessStatus` | TField |  | Swinging Single Price process status automatically retreived by system. Multifonds DB Column is SSP_PROCESS_STATUS. |
| 60 | `FS.GI.TXN.NAV.SHARE.PRICE.CROSS.NAV.SUB` | `FsGiTxnNavSharePrice_CrossNavSub` | TField |  | Cross subscription price updated upon Cross price calculation/ Re calculation process. Multifonds DB Column is CROSS_SUB_PRICE. |
| 61 | `FS.GI.TXN.NAV.SHARE.PRICE.CROSS.NAV.RED` | `FsGiTxnNavSharePrice_CrossNavRed` | TField |  | Cross redemption price updated upon Cross price calculation/ Re calculation process. Multifonds DB Column is CROSS_RED_PRICE. |
| 62 | `FS.GI.TXN.NAV.SHARE.PRICE.REFERENCE.NAV` | `FsGiTxnNavSharePrice_ReferenceNav` | TField |  | Reference NAV used for Series of shares funds. Multifonds DB Column is NAV_BENCHMARK. |
| 63 | `FS.GI.TXN.NAV.SHARE.PRICE.SWUNG.NAV.FLAG` | `FsGiTxnNavSharePrice_SwungNavFlag` | TField |  | Flag to indicate if the share price is swung or not. System does not calculate the swung price if ticked. Multifonds DB Column is FLG_SWUNG_PRICE. |
| 64 | `FS.GI.TXN.NAV.SHARE.PRICE.NEW.PL.ISSUE.ELIGIBLE.SHARES` | `FsGiTxnNavSharePrice_NewPlIssueEligibleShares` | TField |  | New issue P/L (Profit and loss) for Series of shares. Multifonds DB Column is NEW_ISSUE_SHARES_PL. |
| 65 | `FS.GI.TXN.NAV.SHARE.PRICE.OTHER.FEES` | `FsGiTxnNavSharePrice_OtherFees` | TField |  | Other fees used in calculating &apos;Total Cost amount&apos; of the Fund. Multifonds DB Column is OTHER_COST. |
| 66 | `FS.GI.TXN.NAV.SHARE.PRICE.SAVINGS.DIRECTIVE.CODE` | `FsGiTxnNavSharePrice_SavingsDirectiveCode` | TField |  | Saving directive code retreived from Fund. Multifonds DB Column is CSAV_DIRECTIVE. |
| 67 | `FS.GI.TXN.NAV.SHARE.PRICE.EX.DIVIDEND.FLAG` | `FsGiTxnNavSharePrice_ExDividendFlag` | TField |  | Ex-dividend indicator for NAV. Multifonds DB Column is FLG_EX_DIV. |
| 68 | `FS.GI.TXN.NAV.SHARE.PRICE.ESTIMATED.NAV.FLAG` | `FsGiTxnNavSharePrice_EstimatedNavFlag` | TField |  | Flag to indicate if the NAV is an estimated one or not. Multifonds DB Column is ESTIMATED_NAV. |
| 69 | `FS.GI.TXN.NAV.SHARE.PRICE.LEGAL.ENTITY.ID` | `FsGiTxnNavSharePrice_LegalEntityId` | TField |  | Legal entity ID. Multifonds DB Column is NTFC. |
| 70 | `FS.GI.TXN.NAV.SHARE.PRICE.DIVIDEND.TYPE` | `FsGiTxnNavSharePrice_DividendType` | TField |  | It specifies if the dividend is distributed or reinvested. Multifonds DB Column is TYPE_DIVIDENDE. |
| 71 | `FS.GI.TXN.NAV.SHARE.PRICE.PRINT.FLAG` | `FsGiTxnNavSharePrice_PrintFlag` | TField |  | flag indicatess the print status. Multifonds DB Column is TO_PRINT. |
| 72 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.SUB.MASTER.CCY` | `FsGiTxnNavSharePrice_NavSubMasterCcy` | TField |  | Subscription NAV price in Fund Currency. Multifonds DB Column is PRICE_PART_SUB_MST. |
| 73 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.RED.MASTER.CCY` | `FsGiTxnNavSharePrice_NavRedMasterCcy` | TField |  | Redemption NAV price in Fund Currency. Multifonds DB Column is PRICE_PART_RED_MST. |
| 74 | `FS.GI.TXN.NAV.SHARE.PRICE.FX.RATE` | `FsGiTxnNavSharePrice_FxRate` | TField |  | FX rate applicable for the share price. Multifonds DB Column is TCHG. |
| 75 | `FS.GI.TXN.NAV.SHARE.PRICE.NAV.MASTER.CCY` | `FsGiTxnNavSharePrice_NavMasterCcy` | TField |  | NAV price in MF Fund currency. Multifonds DB Column is PRICE_PART. |
| 76 | `FS.GI.TXN.NAV.SHARE.PRICE.TNA.MASTER.CCY` | `FsGiTxnNavSharePrice_TnaMasterCcy` | TField |  | TNA calculated in MF Fund Currency Multifonds DB Column is MNT_PART. |
| 77 | `FS.GI.TXN.NAV.SHARE.PRICE.MIN.BID.NAV.CALC` | `FsGiTxnNavSharePrice_MinBidNavCalc` | TField |  | Minimum calculated bid price. Multifonds DB Column is MIN_BID_CALC. |
| 78 | `FS.GI.TXN.NAV.SHARE.PRICE.BID.NAV.CALC` | `FsGiTxnNavSharePrice_BidNavCalc` | TField |  | Bid NAV calculated. Multifonds DB Column is QUOTED_BID_PRICE. |
| 79 | `FS.GI.TXN.NAV.SHARE.PRICE.SERIES.DATE` | `FsGiTxnNavSharePrice_SeriesDate` | TField |  | Start date of Series of share class. Multifonds DB Column is SERIES_DATE. |
| 80 | `FS.GI.TXN.NAV.SHARE.PRICE.DAILY.TOTAL.COST` | `FsGiTxnNavSharePrice_DailyTotalCost` | TField |  | Daily total cost per fund share class along with the other NAV prices for a NAV date. Multifonds DB Column is DAILY_TOT_COST. |
| 81 | `FS.GI.TXN.NAV.SHARE.PRICE.ACCOUNTING.DATE.MF` | `FsGiTxnNavSharePrice_AccountingDateMf` | TField |  | Application date when NAV is entered. Multifonds DB Column is DCTA. |
| 82 | `FS.GI.TXN.NAV.SHARE.PRICE.INDIVIDUAL.EQ.RATE` | `FsGiTxnNavSharePrice_IndividualEqRate` | TField |  | Individual equalization rate Multifonds DB Column is IND_EQUI_RATE. |
| 83 | `FS.GI.TXN.NAV.SHARE.PRICE.CURRENCY` | `FsGiTxnNavSharePrice_Currency` | TField |  | Fund Share Class Currency Multifonds DB Column is CMONREF. |
| 84 | `FS.GI.TXN.NAV.SHARE.PRICE.FUND.ID` | `FsGiTxnNavSharePrice_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 85 | `FS.GI.TXN.NAV.SHARE.PRICE.CLASS.CURRENCY` | `FsGiTxnNavSharePrice_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 86 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED10` | `FsGiTxnNavSharePrice_Reserved10` | TField |  |  |
| 87 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED9` | `FsGiTxnNavSharePrice_Reserved9` | TField |  |  |
| 88 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED8` | `FsGiTxnNavSharePrice_Reserved8` | TField |  |  |
| 89 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED7` | `FsGiTxnNavSharePrice_Reserved7` | TField |  |  |
| 90 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED6` | `FsGiTxnNavSharePrice_Reserved6` | TField |  |  |
| 91 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED5` | `FsGiTxnNavSharePrice_Reserved5` | TField |  |  |
| 92 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED4` | `FsGiTxnNavSharePrice_Reserved4` | TField |  |  |
| 93 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED3` | `FsGiTxnNavSharePrice_Reserved3` | TField |  |  |
| 94 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED2` | `FsGiTxnNavSharePrice_Reserved2` | TField |  |  |
| 95 | `FS.GI.TXN.NAV.SHARE.PRICE.RESERVED1` | `FsGiTxnNavSharePrice_Reserved1` | TField |  |  |
| 96 | `FS.GI.TXN.NAV.SHARE.PRICE.LOCAL.REF` | `FsGiTxnNavSharePrice_LocalRef` |  |  |  |
| 97 | `FS.GI.TXN.NAV.SHARE.PRICE.OVERRIDE` | `FsGiTxnNavSharePrice_Override` |  |  |  |
| 98 | `FS.GI.TXN.NAV.SHARE.PRICE.RECORD.STATUS` | `FsGiTxnNavSharePrice_RecordStatus` | String |  |  |
| 99 | `FS.GI.TXN.NAV.SHARE.PRICE.CURR.NO` | `FsGiTxnNavSharePrice_CurrNo` | String |  |  |
| 100 | `FS.GI.TXN.NAV.SHARE.PRICE.INPUTTER` | `FsGiTxnNavSharePrice_Inputter` |  |  |  |
| 101 | `FS.GI.TXN.NAV.SHARE.PRICE.DATE.TIME` | `FsGiTxnNavSharePrice_DateTime` |  |  |  |
| 102 | `FS.GI.TXN.NAV.SHARE.PRICE.AUTHORISER` | `FsGiTxnNavSharePrice_Authoriser` | String |  |  |
| 103 | `FS.GI.TXN.NAV.SHARE.PRICE.CO.CODE` | `FsGiTxnNavSharePrice_CoCode` | String |  |  |
| 104 | `FS.GI.TXN.NAV.SHARE.PRICE.DEPT.CODE` | `FsGiTxnNavSharePrice_DeptCode` | String |  |  |
| 105 | `FS.GI.TXN.NAV.SHARE.PRICE.AUDITOR.CODE` | `FsGiTxnNavSharePrice_AuditorCode` | String |  |  |
| 106 | `FS.GI.TXN.NAV.SHARE.PRICE.AUDIT.DATE.TIME` | `FsGiTxnNavSharePrice_AuditDateTime` | String |  |  |
