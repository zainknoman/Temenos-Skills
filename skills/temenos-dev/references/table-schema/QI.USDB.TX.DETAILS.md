# QI.USDB.TX.DETAILS — Table Schema

> Source: `INSERTS/I_F.QI.USDB.TX.DETAILS` in `QI_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QI.USDB.SOURCE` | `QiUsdbTxDetails_Source` | TField |  | Flag to indicate whether the QI.USDB.TX.DETAILS record was updated by system or manually. System generated field containing SYSTEM or MANUAL. This field will automatically be set to SYSTEM when the QI.USDB.TX.DETAILS record is created by RT service and setto MANUAL when input has been made to it by a user. Validation Rules: This is a NOINPUT field. |
| 2 | `QI.USDB.CUST.TAX.RESIDENCE` | `QiUsdbTxDetails_CustTaxResidence` | TField |  | Field holds the customer's Tax Residence based on configuration in Rules APP Validation Rules: Valid record in COUNTRY table |
| 3 | `QI.USDB.CUST.LEGAL.RESIDENCE` | `QiUsdbTxDetails_CustLegalResidence` | TField |  | Field holds the customer's Legal Residence based on configuration in Rules APP Validation Rules: Valid record in COUNTRY table |
| 4 | `QI.USDB.CUSTOMER.TYPE` | `QiUsdbTxDetails_CustomerType` | TField |  | Based on the sector of the customer, customer type is updated by system as either Individual or Entity Validation Rules: Allowed values are ENTITY,INDIVIDUAL |
| 5 | `QI.USDB.QI.STATUS.CUST` | `QiUsdbTxDetails_QiStatusCust` | TField |  | Field holds the status updated in QCSI table. |
| 6 | `QI.USDB.LIMITN.BENE.APP` | `QiUsdbTxDetails_LimitnBeneApp` | TField |  | Field holds the value of CUS.LIMITATION.ON.BENEFITS from QCSI table. |
| 7 | `QI.USDB.FATCA.STATUS.CUST` | `QiUsdbTxDetails_FatcaStatusCust` | TField |  | The field used to specify the FATCA STATUS |
| 8 | `QI.USDB.FATCA.STATUS.TXN` | `QiUsdbTxDetails_FatcaStatusTxn` | TField |  | The field used to specify the PORTFOLIO.STATUS in FCSI |
| 9 | `QI.USDB.QI.DB.RESERVED.1` | `QiUsdbTxDetails_QiDbReserved1` | TField |  |  |
| 10 | `QI.USDB.QI.DB.RESERVED.2` | `QiUsdbTxDetails_QiDbReserved2` | TField |  |  |
| 11 | `QI.USDB.QI.DB.RESERVED.3` | `QiUsdbTxDetails_QiDbReserved3` | TField |  |  |
| 12 | `QI.USDB.QI.DB.RESERVED.4` | `QiUsdbTxDetails_QiDbReserved4` | TField |  |  |
| 13 | `QI.USDB.EVENT.REFERENCE` | `QiUsdbTxDetails_EventReference` | TField |  | This field holds the Diary id of the Entitlement |
| 14 | `QI.USDB.CORP.REFERENCE` | `QiUsdbTxDetails_CorpReference` | TField |  | This field used to specify the Corp reference in Diary Application |
| 15 | `QI.USDB.DEPOSITORY` | `QiUsdbTxDetails_Depository` | TField |  | This field holds the depository information present in Entitlement |
| 16 | `QI.USDB.EVENT.TYPE` | `QiUsdbTxDetails_EventType` | TField |  | This field holds the Event type in Diary application. |
| 17 | `QI.USDB.EVENT.CURRENCY` | `QiUsdbTxDetails_EventCurrency` | TField |  | This field holds the event currency in Entitlement |
| 18 | `QI.USDB.PORTFOLIO.NO` | `QiUsdbTxDetails_PortfolioNo` | TField |  | This field holds the Portfolio no in Entitlement |
| 19 | `QI.USDB.SECURITY.NO` | `QiUsdbTxDetails_SecurityNo` | TField |  | This field holds the security no in Entitlement |
| 20 | `QI.USDB.I.S.I.N.` | `QiUsdbTxDetails_ISIN` | TField |  | This field holds the I.S.I.N. in SECURITY.MASTER attached to Entitlement |
| 21 | `QI.USDB.ASSET.TYPE` | `QiUsdbTxDetails_AssetType` | TField |  | This field holds the ASSET.TYPE in SECURITY.MASTER attached to Entitlement |
| 22 | `QI.USDB.SUB.ASSET.TYPE` | `QiUsdbTxDetails_SubAssetType` | TField |  | If the Diary is created for a DX contract, this field holds the SUB.ASSET.TYPE in DX.CONTRACT.MASTER attached to Entitlement Otherwise, this field holds the SUB.ASSET.TYPE in SECURITY.MASTER attached to Entitlement |
| 23 | `QI.USDB.SYMBOL` | `QiUsdbTxDetails_Symbol` | TField |  | This field holds the TICKER.SYMBOL in SECURITY.SUPP application attached to Entitlement |
| 24 | `QI.USDB.SECURITY.NAME` | `QiUsdbTxDetails_SecurityName` | TField |  | This field holds the SHORT.NAME in SECURITY.MASTER attached to Entitlement |
| 25 | `QI.USDB.PRODUCT.TYPE` | `QiUsdbTxDetails_ProductType` | TField |  | This field holds the SUB.ASSET.TYPE in SECURITY.MASTER attached to Entitlement |
| 26 | `QI.USDB.QUALIFYING.NOMINAL` | `QiUsdbTxDetails_QualifyingNominal` | TField |  | This field holds the QUALIFYING.HOLDING in Entitlement |
| 27 | `QI.USDB.PYMT.VAL.DATE` | `QiUsdbTxDetails_PymtValDate` | TField |  | This field holds the VALUE.DATE in Entitlement |
| 28 | `QI.USDB.ACT.PYMT.DATE` | `QiUsdbTxDetails_ActPymtDate` | TField |  | This field holds the PAY.DATE in Diary |
| 29 | `QI.USDB.RECORD.DATE` | `QiUsdbTxDetails_RecordDate` | TField |  | This field holds the RECORD.DATE in Diary |
| 30 | `QI.USDB.CASH.RECEIVED` | `QiUsdbTxDetails_CashReceived` | TField |  | This field holds the CASH.RECEIVED from Entitlement in event currency |
| 31 | `QI.USDB.RATE` | `QiUsdbTxDetails_Rate` | TField |  | This field holds the RATE from Entitlement |
| 32 | `QI.USDB.SHARE.RECEIVED` | `QiUsdbTxDetails_ShareReceived` |  |  |  |
| 33 | `QI.USDB.SHARE.PRICE` | `QiUsdbTxDetails_SharePrice` |  |  |  |
| 34 | `QI.USDB.TOT.AMT.PAID` | `QiUsdbTxDetails_TotAmtPaid` | TField |  | This field holds the TOT.AMT.PAID from Entitlement |
| 35 | `QI.USDB.TOT.AMT.PAID.USD` | `QiUsdbTxDetails_TotAmtPaidUsd` | TField |  | This field holds the TOT.AMT.PAID from Entitlement in USD currency |
| 36 | `QI.USDB.TAX.TYPE` | `QiUsdbTxDetails_TaxType` | TField |  | This field holds the SC.TAX.TYPE from Entitlement |
| 37 | `QI.USDB.FATCA.TAX.RATE` | `QiUsdbTxDetails_FatcaTaxRate` | TField |  | This field holds the rate from Entitlement.Applicable only if TAX.TYPE matches with FATCA.TAX.TYPE in QI.PARAMETER |
| 38 | `QI.USDB.FATCA.TAX.AMT` | `QiUsdbTxDetails_FatcaTaxAmt` | TField |  | This field holds the MAN.TAX.ACY/SC.AMT.ACY from Entitlement.MAN.TAX.ACY takes precedence.Applicable only if TAX.TYPE matches with FATCA.TAX.TYPE in QI.PARAMETER |
| 39 | `QI.USDB.FATCA.TAX.AMT.USD` | `QiUsdbTxDetails_FatcaTaxAmtUsd` | TField |  | This field holds the usd equivalent amount of FATCA.TAX.TYPE |
| 40 | `QI.USDB.FATCA.TAX.AMT.EXCH.RATE` | `QiUsdbTxDetails_FatcaTaxAmtExchRate` | TField |  | This field holds the exchange rate from Entitlement |
| 41 | `QI.USDB.FATCA.TAX.INDICATOR` | `QiUsdbTxDetails_FatcaTaxIndicator` | TField |  | This field holds the value of Source or local from Entitlement |
| 42 | `QI.USDB.QI.TAX.INDICATOR` | `QiUsdbTxDetails_QiTaxIndicator` | TField |  | This field holds the value of Source or local from Entitlement |
| 43 | `QI.USDB.INCOME.CODE` | `QiUsdbTxDetails_IncomeCode` |  |  |  |
| 44 | `QI.USDB.QI.STATUS.TXN` | `QiUsdbTxDetails_QiStatusTxn` |  |  |  |
| 45 | `QI.USDB.QI.TXN.TAX.APPLN.CNTRY` | `QiUsdbTxDetails_QiTxnTaxApplnCntry` |  |  |  |
| 46 | `QI.USDB.TAXABLE.INDICATOR` | `QiUsdbTxDetails_TaxableIndicator` |  |  |  |
| 47 | `QI.USDB.REPORTABLE.INDICATOR` | `QiUsdbTxDetails_ReportableIndicator` |  |  |  |
| 48 | `QI.USDB.EXEM.CODE.CHAP.4` | `QiUsdbTxDetails_ExemCodeChap4` |  |  |  |
| 49 | `QI.USDB.RECP.CODE.CHAP.4` | `QiUsdbTxDetails_RecpCodeChap4` |  |  |  |
| 50 | `QI.USDB.EXEM.CODE.CHAP.3` | `QiUsdbTxDetails_ExemCodeChap3` |  |  |  |
| 51 | `QI.USDB.RECP.CODE.CHAP.3` | `QiUsdbTxDetails_RecpCodeChap3` |  |  |  |
| 52 | `QI.USDB.INCOME.RATE` | `QiUsdbTxDetails_IncomeRate` |  |  |  |
| 53 | `QI.USDB.INCOME.PERCENTAGE` | `QiUsdbTxDetails_IncomePercentage` |  |  |  |
| 54 | `QI.USDB.INCOME.AMT` | `QiUsdbTxDetails_IncomeAmt` |  |  |  |
| 55 | `QI.USDB.INCOME.AMT.USD` | `QiUsdbTxDetails_IncomeAmtUsd` |  |  |  |
| 56 | `QI.USDB.IC.TAX.RATE` | `QiUsdbTxDetails_IcTaxRate` |  |  |  |
| 57 | `QI.USDB.TAX.DATE` | `QiUsdbTxDetails_TaxDate` |  |  |  |
| 58 | `QI.USDB.IC.TAX.AMT` | `QiUsdbTxDetails_IcTaxAmt` |  |  |  |
| 59 | `QI.USDB.IC.TAX.AMT.USD` | `QiUsdbTxDetails_IcTaxAmtUsd` |  |  |  |
| 60 | `QI.USDB.QI.DB.RESERVED.5` | `QiUsdbTxDetails_QiDbReserved5` |  |  |  |
| 61 | `QI.USDB.QI.DB.RESERVED.6` | `QiUsdbTxDetails_QiDbReserved6` |  |  |  |
| 62 | `QI.USDB.QI.DB.RESERVED.7` | `QiUsdbTxDetails_QiDbReserved7` |  |  |  |
| 63 | `QI.USDB.QI.DB.RESERVED.8` | `QiUsdbTxDetails_QiDbReserved8` |  |  |  |
| 64 | `QI.USDB.TOT.IC.INCOME.AMT` | `QiUsdbTxDetails_TotIcIncomeAmt` | TField |  | This field holds the value of entitlement amount for customers based on their owning percentage |
| 65 | `QI.USDB.TOT.IC.INCOME.AMT.USD` | `QiUsdbTxDetails_TotIcIncomeAmtUsd` | TField |  | This field holds the USD equivalent amount of total income amount |
| 66 | `QI.USDB.TOT.IC.TAX.AMT` | `QiUsdbTxDetails_TotIcTaxAmt` | TField |  | This field holds the summation of tax amount for each income code |
| 67 | `QI.USDB.TOT.IC.TAX.AMT.USD` | `QiUsdbTxDetails_TotIcTaxAmtUsd` | TField |  | This field holds the USD equivalent amount of Total Tax amount |
| 68 | `QI.USDB.TAX.AMT.EXCH.RATE` | `QiUsdbTxDetails_TaxAmtExchRate` | TField |  | This field holds the value of exchange rate of entitlement |
| 69 | `QI.USDB.TAX.PERCENTAGE` | `QiUsdbTxDetails_TaxPercentage` | TField |  | This field holds the Tax percentage.Calculated based on the formula = revised total tax amount / revised total income amount |
| 70 | `QI.USDB.OWNING.PERCENTAGE` | `QiUsdbTxDetails_OwningPercentage` | TField |  | This field holds the owning percentage for the customer from ST.TAX.REPORT.DETAILS |
| 71 | `QI.USDB.LINK.TABLE.REF` | `QiUsdbTxDetails_LinkTableRef` | TField |  | This field holds the tax report details ID for joint holders |
| 72 | `QI.USDB.QI.DB.RESERVED.9` | `QiUsdbTxDetails_QiDbReserved9` | TField |  |  |
| 73 | `QI.USDB.QI.DB.RESERVED.10` | `QiUsdbTxDetails_QiDbReserved10` | TField |  |  |
| 74 | `QI.USDB.QI.DB.RESERVED.11` | `QiUsdbTxDetails_QiDbReserved11` | TField |  |  |
| 75 | `QI.USDB.QI.DB.RESERVED.12` | `QiUsdbTxDetails_QiDbReserved12` | TField |  |  |
| 76 | `QI.USDB.QI.DB.RESERVED.13` | `QiUsdbTxDetails_QiDbReserved13` | TField |  |  |
| 77 | `QI.USDB.QI.DB.RESERVED.14` | `QiUsdbTxDetails_QiDbReserved14` | TField |  |  |
| 78 | `QI.USDB.REV.INCOME.CODE` | `QiUsdbTxDetails_RevIncomeCode` |  |  |  |
| 79 | `QI.USDB.REV.QI.STATUS.TXN` | `QiUsdbTxDetails_RevQiStatusTxn` |  |  |  |
| 80 | `QI.USDB.REV.QI.TXN.TAX.APPLN.CNTRY` | `QiUsdbTxDetails_RevQiTxnTaxApplnCntry` |  |  |  |
| 81 | `QI.USDB.REV.TAXABLE.INDICATOR` | `QiUsdbTxDetails_RevTaxableIndicator` |  |  |  |
| 82 | `QI.USDB.REV.REPORTABLE.INDICATOR` | `QiUsdbTxDetails_RevReportableIndicator` |  |  |  |
| 83 | `QI.USDB.REV.EXEM.CODE.CHAP.4` | `QiUsdbTxDetails_RevExemCodeChap4` |  |  |  |
| 84 | `QI.USDB.REV.RECP.CODE.CHAP.4` | `QiUsdbTxDetails_RevRecpCodeChap4` |  |  |  |
| 85 | `QI.USDB.REV.EXEM.CODE.CHAP.3` | `QiUsdbTxDetails_RevExemCodeChap3` |  |  |  |
| 86 | `QI.USDB.REV.RECP.CODE.CHAP.3` | `QiUsdbTxDetails_RevRecpCodeChap3` |  |  |  |
| 87 | `QI.USDB.REV.INCOME.RATE` | `QiUsdbTxDetails_RevIncomeRate` |  |  |  |
| 88 | `QI.USDB.REV.INCOME.PERCENTAGE` | `QiUsdbTxDetails_RevIncomePercentage` |  |  |  |
| 89 | `QI.USDB.REV.INCOME.AMT` | `QiUsdbTxDetails_RevIncomeAmt` |  |  |  |
| 90 | `QI.USDB.REV.INCOME.AMT.USD` | `QiUsdbTxDetails_RevIncomeAmtUsd` |  |  |  |
| 91 | `QI.USDB.REV.IC.TAX.RATE` | `QiUsdbTxDetails_RevIcTaxRate` |  |  |  |
| 92 | `QI.USDB.REV.TAX.DATE` | `QiUsdbTxDetails_RevTaxDate` |  |  |  |
| 93 | `QI.USDB.REV.IC.TAX.AMT` | `QiUsdbTxDetails_RevIcTaxAmt` |  |  |  |
| 94 | `QI.USDB.REV.IC.TAX.AMT.USD` | `QiUsdbTxDetails_RevIcTaxAmtUsd` |  |  |  |
| 95 | `QI.USDB.QI.DB.RESERVED.15` | `QiUsdbTxDetails_QiDbReserved15` |  |  |  |
| 96 | `QI.USDB.QI.DB.RESERVED.16` | `QiUsdbTxDetails_QiDbReserved16` |  |  |  |
| 97 | `QI.USDB.QI.DB.RESERVED.17` | `QiUsdbTxDetails_QiDbReserved17` |  |  |  |
| 98 | `QI.USDB.QI.DB.RESERVED.18` | `QiUsdbTxDetails_QiDbReserved18` |  |  |  |
| 99 | `QI.USDB.REV.TOT.IC.INCOME.AMT` | `QiUsdbTxDetails_RevTotIcIncomeAmt` |  |  |  |
| 100 | `QI.USDB.REV.TOT.IC.INCOME.AMT.USD` | `QiUsdbTxDetails_RevTotIcIncomeAmtUsd` |  |  |  |
| 101 | `QI.USDB.REV.TOT.IC.TAX.AMT` | `QiUsdbTxDetails_RevTotIcTaxAmt` |  |  |  |
| 102 | `QI.USDB.REV.TOT.IC.TAX.AMT.USD` | `QiUsdbTxDetails_RevTotIcTaxAmtUsd` |  |  |  |
| 103 | `QI.USDB.REV.ADJ.AMT` | `QiUsdbTxDetails_RevAdjAmt` |  |  |  |
| 104 | `QI.USDB.REV.TAX.AMT.EXCH.RATE` | `QiUsdbTxDetails_RevTaxAmtExchRate` |  |  |  |
| 105 | `QI.USDB.REV.TAX.PERCENTAGE` | `QiUsdbTxDetails_RevTaxPercentage` |  |  |  |
| 106 | `QI.USDB.REV.ADJ.TYPE` | `QiUsdbTxDetails_RevAdjType` |  |  |  |
| 107 | `QI.USDB.REV.TXN.DATE` | `QiUsdbTxDetails_RevTxnDate` |  |  |  |
| 108 | `QI.USDB.REV.OWNING.PERCENTAGE` | `QiUsdbTxDetails_RevOwningPercentage` |  |  |  |
| 109 | `QI.USDB.REV.REFERENCE.ID` | `QiUsdbTxDetails_RevReferenceId` |  |  |  |
| 110 | `QI.USDB.REV.JNT.REF.LINK` | `QiUsdbTxDetails_RevJntRefLink` |  |  |  |
| 111 | `QI.USDB.QI.DB.RESERVED.19` | `QiUsdbTxDetails_QiDbReserved19` |  |  |  |
| 112 | `QI.USDB.QI.DB.RESERVED.20` | `QiUsdbTxDetails_QiDbReserved20` |  |  |  |
| 113 | `QI.USDB.QI.DB.RESERVED.21` | `QiUsdbTxDetails_QiDbReserved21` |  |  |  |
| 114 | `QI.USDB.QI.DB.RESERVED.22` | `QiUsdbTxDetails_QiDbReserved22` |  |  |  |
| 115 | `QI.USDB.QI.DB.RESERVED.23` | `QiUsdbTxDetails_QiDbReserved23` |  |  |  |
| 116 | `QI.USDB.QI.DB.RESERVED.24` | `QiUsdbTxDetails_QiDbReserved24` |  |  |  |
| 117 | `QI.USDB.REP.INCOME.CODE` | `QiUsdbTxDetails_RepIncomeCode` |  |  |  |
| 118 | `QI.USDB.REP.QI.STATUS.TXN` | `QiUsdbTxDetails_RepQiStatusTxn` |  |  |  |
| 119 | `QI.USDB.REP.QI.TXN.TAX.APPLN.CNTRY` | `QiUsdbTxDetails_RepQiTxnTaxApplnCntry` |  |  |  |
| 120 | `QI.USDB.REP.TAXABLE.INDICATOR` | `QiUsdbTxDetails_RepTaxableIndicator` |  |  |  |
| 121 | `QI.USDB.REP.REPORTABLE.INDICATOR` | `QiUsdbTxDetails_RepReportableIndicator` |  |  |  |
| 122 | `QI.USDB.REP.EXEM.CODE.CHAP.4` | `QiUsdbTxDetails_RepExemCodeChap4` |  |  |  |
| 123 | `QI.USDB.REP.RECP.CODE.CHAP.4` | `QiUsdbTxDetails_RepRecpCodeChap4` |  |  |  |
| 124 | `QI.USDB.REP.EXEM.CODE.CHAP.3` | `QiUsdbTxDetails_RepExemCodeChap3` |  |  |  |
| 125 | `QI.USDB.REP.RECP.CODE.CHAP.3` | `QiUsdbTxDetails_RepRecpCodeChap3` |  |  |  |
| 126 | `QI.USDB.REP.INCOME.RATE` | `QiUsdbTxDetails_RepIncomeRate` |  |  |  |
| 127 | `QI.USDB.REP.INCOME.PERCENTAGE` | `QiUsdbTxDetails_RepIncomePercentage` |  |  |  |
| 128 | `QI.USDB.REP.INCOME.AMT` | `QiUsdbTxDetails_RepIncomeAmt` |  |  |  |
| 129 | `QI.USDB.REP.INCOME.AMT.USD` | `QiUsdbTxDetails_RepIncomeAmtUsd` |  |  |  |
| 130 | `QI.USDB.REP.IC.TAX.RATE` | `QiUsdbTxDetails_RepIcTaxRate` |  |  |  |
| 131 | `QI.USDB.REP.TAX.DATE` | `QiUsdbTxDetails_RepTaxDate` |  |  |  |
| 132 | `QI.USDB.REP.IC.TAX.AMT` | `QiUsdbTxDetails_RepIcTaxAmt` |  |  |  |
| 133 | `QI.USDB.REP.IC.TAX.AMT.USD` | `QiUsdbTxDetails_RepIcTaxAmtUsd` |  |  |  |
| 134 | `QI.USDB.QI.DB.RESERVED.25` | `QiUsdbTxDetails_QiDbReserved25` |  |  |  |
| 135 | `QI.USDB.QI.DB.RESERVED.26` | `QiUsdbTxDetails_QiDbReserved26` |  |  |  |
| 136 | `QI.USDB.QI.DB.RESERVED.27` | `QiUsdbTxDetails_QiDbReserved27` |  |  |  |
| 137 | `QI.USDB.QI.DB.RESERVED.28` | `QiUsdbTxDetails_QiDbReserved28` |  |  |  |
| 138 | `QI.USDB.REP.TOT.IC.INCOME.AMT` | `QiUsdbTxDetails_RepTotIcIncomeAmt` | TField |  | This field holds the summation of reportable income amount for customers based on their owning percentage |
| 139 | `QI.USDB.REP.TOT.IC.INCOME.AMT.USD` | `QiUsdbTxDetails_RepTotIcIncomeAmtUsd` | TField |  | This field holds the USD equivalent amount of reportable total income amount |
| 140 | `QI.USDB.REP.TOT.IC.TAX.AMT` | `QiUsdbTxDetails_RepTotIcTaxAmt` | TField |  | This field holds the summation of reportable tax amount for each income code |
| 141 | `QI.USDB.REP.TOT.IC.TAX.AMT.USD` | `QiUsdbTxDetails_RepTotIcTaxAmtUsd` | TField |  | This field holds the USD equivalent amount of reportable Total Tax amount |
| 142 | `QI.USDB.REP.ADJ.AMT` | `QiUsdbTxDetails_RepAdjAmt` | TField |  |  |
| 143 | `QI.USDB.REP.TAX.AMT.EXCH.RATE` | `QiUsdbTxDetails_RepTaxAmtExchRate` | TField |  | This field holds the value of reportable exchange rate |
| 144 | `QI.USDB.REP.TAX.PERCENTAGE` | `QiUsdbTxDetails_RepTaxPercentage` | TField |  | This field holds the latest Tax percentage.Calculated based on the formula = reportable total tax amount / reportable total income amount |
| 145 | `QI.USDB.REP.ADJ.TYPE` | `QiUsdbTxDetails_RepAdjType` | TField |  |  |
| 146 | `QI.USDB.REP.TXN.DATE` | `QiUsdbTxDetails_RepTxnDate` | TField |  |  |
| 147 | `QI.USDB.REP.OWNING.PERCENTAGE` | `QiUsdbTxDetails_RepOwningPercentage` | TField |  | This field holds the final owning percentage for the customer |
| 148 | `QI.USDB.REP.REFERENCE.ID` | `QiUsdbTxDetails_RepReferenceId` | TField |  |  |
| 149 | `QI.USDB.REP.JNT.REF.LINK` | `QiUsdbTxDetails_RepJntRefLink` | TField |  |  |
| 150 | `QI.USDB.QI.DB.RESERVED.29` | `QiUsdbTxDetails_QiDbReserved29` | TField |  |  |
| 151 | `QI.USDB.QI.DB.RESERVED.30` | `QiUsdbTxDetails_QiDbReserved30` | TField |  |  |
| 152 | `QI.USDB.QI.DB.RESERVED.31` | `QiUsdbTxDetails_QiDbReserved31` | TField |  |  |
| 153 | `QI.USDB.QI.DB.RESERVED.32` | `QiUsdbTxDetails_QiDbReserved32` | TField |  |  |
| 154 | `QI.USDB.QI.DB.RESERVED.33` | `QiUsdbTxDetails_QiDbReserved33` | TField |  |  |
| 155 | `QI.USDB.QI.DB.RESERVED.34` | `QiUsdbTxDetails_QiDbReserved34` | TField |  |  |
| 156 | `QI.USDB.ST.SECURITY.CODE` | `QiUsdbTxDetails_StSecurityCode` | TField |  | This field holds security code attached to security trade |
| 157 | `QI.USDB.ST.SUB.ASSET.TYPE` | `QiUsdbTxDetails_StSubAssetType` | TField |  | This field holds the sub asset type in security master attcahed to sec trade |
| 158 | `QI.USDB.ST.TRADE.DATE` | `QiUsdbTxDetails_StTradeDate` | TField |  | This field holds the trade date in sec trade |
| 159 | `QI.USDB.ST.VALUE.DATE` | `QiUsdbTxDetails_StValueDate` | TField |  | This field holds the value date in sec trade |
| 160 | `QI.USDB.ST.TRADE.CCY` | `QiUsdbTxDetails_StTradeCcy` | TField |  | This field holds the trade currency in sec trade |
| 161 | `QI.USDB.ST.TRANSACTION.TYPE` | `QiUsdbTxDetails_StTransactionType` | TField |  | This field holds the value of CU.TRANS.CODE in sec trade |
| 162 | `QI.USDB.ST.TRANSACTION.NOMINAL` | `QiUsdbTxDetails_StTransactionNominal` |  |  |  |
| 163 | `QI.USDB.ST.TRANSACTION.PRICE` | `QiUsdbTxDetails_StTransactionPrice` |  |  |  |
| 164 | `QI.USDB.ST.WHT.TAX.CODE` | `QiUsdbTxDetails_StWhtTaxCode` | TField |  | This field holds the WHT.TAX.CODE in sec trade |
| 165 | `QI.USDB.ST.WHT.TAX.AMT` | `QiUsdbTxDetails_StWhtTaxAmt` | TField |  | This field holds the CU.WHT.TAX in sec trade |
| 166 | `QI.USDB.ST.SALE.PROCEEDS.GROSS` | `QiUsdbTxDetails_StSaleProceedsGross` | TField |  | This field holds the CU.GROSS.AM.TRD in sec trade |
| 167 | `QI.USDB.ST.SALE.PROCEEDS.NET` | `QiUsdbTxDetails_StSaleProceedsNet` | TField |  | This field holds the CU.NET.AM.TRD in sec trade |
| 168 | `QI.USDB.DX.UNDERLYING.SECURITY` | `QiUsdbTxDetails_DxUnderlyingSecurity` | TField |  | This field holds the security no in Entitlement only if the entitlement is created for DX diary event. |
| 169 | `QI.USDB.EX.DIV.DATE` | `QiUsdbTxDetails_ExDivDate` | TField |  | This field holds the EX.DATE in DIARY only if the corresponding entitlement is created for DX diary event. |
| 170 | `QI.USDB.DX.TAX.EVENT.TYPE` | `QiUsdbTxDetails_DxTaxEventType` | TField |  | This field holds the DX.TAX.EVENT.TYPE in DIARY.TYPE with the ID mentioned in the EVENT.TYPE of Entitlement. |
| 171 | `QI.USDB.DX.CONTRACT.NUMBER` | `QiUsdbTxDetails_DxContractNumber` | TField |  | This field holds the CONTRACT.NO in Entitlement only if the corresponding entitlement is created for DX diary event. |
| 172 | `QI.USDB.DX.CONTRACT.TYPE` | `QiUsdbTxDetails_DxContractType` | TField |  | This field holds the CONTRACT.TYPE in DX.CONTRACT.MASTER with the ID mentioned in CONTRACT.NO of Entitlement only if the corresponding entitlement is created for DX diary event. |
| 173 | `QI.USDB.DX.CONTRACT.CLASS` | `QiUsdbTxDetails_DxContractClass` | TField |  | This field holds the CONTRACT.CLASS in DX.CONTRACT.MASTER with the ID mentioned in CONTRACT.NO of Entitlement only if the corresponding entitlement is created for DX diary event. |
| 174 | `QI.USDB.LNK.TRANS.ID` | `QiUsdbTxDetails_LnkTransId` |  |  |  |
| 175 | `QI.USDB.LNK.SYNTHETIC.CONTRACT` | `QiUsdbTxDetails_LnkSyntheticContract` |  |  |  |
| 176 | `QI.USDB.LNK.TRANS.DATE` | `QiUsdbTxDetails_LnkTransDate` |  |  |  |
| 177 | `QI.USDB.LNK.TRANS.QTY` | `QiUsdbTxDetails_LnkTransQty` |  |  |  |
| 178 | `QI.USDB.LNK.TRANS.DELTA` | `QiUsdbTxDetails_LnkTransDelta` |  |  |  |
| 179 | `QI.USDB.QI.DB.RESERVED.46` | `QiUsdbTxDetails_QiDbReserved46` | TField |  |  |
| 180 | `QI.USDB.QI.DB.RESERVED.47` | `QiUsdbTxDetails_QiDbReserved47` | TField |  |  |
| 181 | `QI.USDB.QI.DB.RESERVED.48` | `QiUsdbTxDetails_QiDbReserved48` | TField |  |  |
| 182 | `QI.USDB.QI.DB.RESERVED.49` | `QiUsdbTxDetails_QiDbReserved49` | TField |  |  |
| 183 | `QI.USDB.QI.DB.RESERVED.50` | `QiUsdbTxDetails_QiDbReserved50` | TField |  |  |
| 184 | `QI.USDB.QI.DB.RESERVED.51` | `QiUsdbTxDetails_QiDbReserved51` | TField |  |  |
| 185 | `QI.USDB.QI.DB.RESERVED.52` | `QiUsdbTxDetails_QiDbReserved52` | TField |  |  |
| 186 | `QI.USDB.QI.DB.RESERVED.53` | `QiUsdbTxDetails_QiDbReserved53` | TField |  |  |
| 187 | `QI.USDB.QI.DB.RESERVED.54` | `QiUsdbTxDetails_QiDbReserved54` | TField |  |  |
| 188 | `QI.USDB.QI.DB.RESERVED.55` | `QiUsdbTxDetails_QiDbReserved55` | TField |  |  |
| 189 | `QI.USDB.QI.DB.RESERVED.56` | `QiUsdbTxDetails_QiDbReserved56` | TField |  |  |
| 190 | `QI.USDB.QI.DB.RESERVED.57` | `QiUsdbTxDetails_QiDbReserved57` | TField |  |  |
| 191 | `QI.USDB.QI.DB.RESERVED.58` | `QiUsdbTxDetails_QiDbReserved58` | TField |  |  |
| 192 | `QI.USDB.QI.DB.RESERVED.59` | `QiUsdbTxDetails_QiDbReserved59` | TField |  |  |
| 193 | `QI.USDB.QI.DB.RESERVED.60` | `QiUsdbTxDetails_QiDbReserved60` | TField |  |  |
| 194 | `QI.USDB.LOCAL.REF` | `QiUsdbTxDetails_LocalRef` |  |  |  |
| 195 | `QI.USDB.OVERRIDE` | `QiUsdbTxDetails_Override` |  |  |  |
| 196 | `QI.USDB.RECORD.STATUS` | `QiUsdbTxDetails_RecordStatus` | String |  | Status of the record |
| 197 | `QI.USDB.CURR.NO` | `QiUsdbTxDetails_CurrNo` | String |  | Curr No |
| 198 | `QI.USDB.INPUTTER` | `QiUsdbTxDetails_Inputter` |  |  |  |
| 199 | `QI.USDB.DATE.TIME` | `QiUsdbTxDetails_DateTime` |  |  |  |
| 200 | `QI.USDB.AUTHORISER` | `QiUsdbTxDetails_Authoriser` | String |  | Authoriser |
| 201 | `QI.USDB.CO.CODE` | `QiUsdbTxDetails_CoCode` | String |  | Company code |
| 202 | `QI.USDB.DEPT.CODE` | `QiUsdbTxDetails_DeptCode` | String |  | Department code |
| 203 | `QI.USDB.AUDITOR.CODE` | `QiUsdbTxDetails_AuditorCode` | String |  | Auditor Code |
| 204 | `QI.USDB.AUDIT.DATE.TIME` | `QiUsdbTxDetails_AuditDateTime` | String |  | Audit Date and time |
| 205 | `QI.USDB.EXEM.CHAP.3.UNDER.FATCA` | `QiUsdbTxDetails_ExemChap3UnderFatca` | TField |  |  |
| 206 | `QI.USDB.EXEM.CHAP.4.UNDER.FATCA` | `QiUsdbTxDetails_ExemChap4UnderFatca` | TField |  |  |
| 207 | `QI.USDB.FATCA.OWNING.AMT` | `QiUsdbTxDetails_FatcaOwningAmt` | TField |  |  |
| 208 | `QI.USDB.FATCA.OWNING.AMT.USD` | `QiUsdbTxDetails_FatcaOwningAmtUsd` | TField |  |  |
| 209 | `QI.USDB.FATCA.TAX.DATE` | `QiUsdbTxDetails_FatcaTaxDate` | TField |  |  |
