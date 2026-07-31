# DESCTX.SECTRAS.SCDX.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.SCDX.TRANSACTIONS` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DESCTX.SCDX.INTERFACE` | `DesctxSectrasScdxTransactions_Interface` | TField |  | Interface to be used SECTRAS request and response |
| 2 | `DESCTX.SCDX.TRANSACTION.ID` | `DesctxSectrasScdxTransactions_TransactionId` | TField |  | ID of the transaction |
| 3 | `DESCTX.SCDX.TRANS.DATE` | `DesctxSectrasScdxTransactions_TransDate` | TField |  | Date on which the transaction is authorized |
| 4 | `DESCTX.SCDX.PORTFOLIO` | `DesctxSectrasScdxTransactions_Portfolio` | TField |  | Security account master number |
| 5 | `DESCTX.SCDX.ACCOUNT` | `DesctxSectrasScdxTransactions_Account` | TField |  | Account number of the given security account master |
| 6 | `DESCTX.SCDX.FEE.LCY` | `DesctxSectrasScdxTransactions_FeeLcy` | TField |  | Fees in local currency |
| 7 | `DESCTX.SCDX.FEE.CHG.DATE` | `DesctxSectrasScdxTransactions_FeeChgDate` | TField |  | Date onwhich the fee is charged |
| 8 | `DESCTX.SCDX.YEAR.CHARGED` | `DesctxSectrasScdxTransactions_YearCharged` | TField |  | Year on which the fee is charged |
| 9 | `DESCTX.SCDX.TRNS.REVE` | `DesctxSectrasScdxTransactions_TrnsReve` | TField |  | Indicator to see if the transaction is reversed or not |
| 10 | `DESCTX.SCDX.STATUS` | `DesctxSectrasScdxTransactions_Status` | TField |  | status of the response |
| 11 | `DESCTX.SCDX.ERROR.CODE` | `DesctxSectrasScdxTransactions_ErrorCode` | TField |  | Error code to describe the status of the response |
| 12 | `DESCTX.SCDX.ERROR.DESC` | `DesctxSectrasScdxTransactions_ErrorDesc` | TField |  | Error description to describe the status |
| 13 | `DESCTX.SCDX.TRANS.TYPE` | `DesctxSectrasScdxTransactions_TransType` | TField |  | Transaction type of the current contract |
| 14 | `DESCTX.SCDX.SECURITY.CODE` | `DesctxSectrasScdxTransactions_SecurityCode` | TField |  | Security master number |
| 15 | `DESCTX.SCDX.TRADE.CCY` | `DesctxSectrasScdxTransactions_TradeCcy` | TField |  | Trade currency value |
| 16 | `DESCTX.SCDX.TRADE.NOM` | `DesctxSectrasScdxTransactions_TradeNom` | TField |  | No of nominals involved in the transaction |
| 17 | `DESCTX.SCDX.TRADE.AMT` | `DesctxSectrasScdxTransactions_TradeAmt` | TField |  | Amount involved in the transaction |
| 18 | `DESCTX.SCDX.FEE.CHARGE` | `DesctxSectrasScdxTransactions_FeeCharge` | TField |  | Charge amount of commissions and fee |
| 19 | `DESCTX.SCDX.BID.NUMBER` | `DesctxSectrasScdxTransactions_BidNumber` | TField |  | Bid Number |
| 20 | `DESCTX.SCDX.UD.KD.EVENT` | `DesctxSectrasScdxTransactions_UdKdEvent` | TField |  | Ud Kd Event number |
| 21 | `DESCTX.SCDX.BNF.SVCR.ID.TYPE` | `DesctxSectrasScdxTransactions_BnfSvcrIdType` | TField |  | Beneficiary service account Type |
| 22 | `DESCTX.SCDX.BNF.SVCR.ID` | `DesctxSectrasScdxTransactions_BnfSvcrId` | TField |  | Beneficiary service account ID |
| 23 | `DESCTX.SCDX.BNF.ACCT.KEY` | `DesctxSectrasScdxTransactions_BnfAcctKey` | TField |  | Beneficiary service account key |
| 24 | `DESCTX.SCDX.BNF.ACCT.NAME` | `DesctxSectrasScdxTransactions_BnfAcctName` | TField |  | Beneficiary service account name |
| 25 | `DESCTX.SCDX.BNF.LAST.NAME.1` | `DesctxSectrasScdxTransactions_BnfLastName1` | TField |  | Beneficiary service account last name |
| 26 | `DESCTX.SCDX.BNF.FIRST.NAME.1` | `DesctxSectrasScdxTransactions_BnfFirstName1` | TField |  | Beneficiary service account first name |
| 27 | `DESCTX.SCDX.BNF.BIRTH.DATE.1` | `DesctxSectrasScdxTransactions_BnfBirthDate1` | TField |  | Beneficiary service account holder birth date |
| 28 | `DESCTX.SCDX.BNF.TIN.1` | `DesctxSectrasScdxTransactions_BnfTin1` | TField |  | Beneficiary service account holder tin number |
| 29 | `DESCTX.SCDX.BNF.STREET.1` | `DesctxSectrasScdxTransactions_BnfStreet1` | TField |  | Beneficiary service account holder sreet address |
| 30 | `DESCTX.SCDX.BNF.HOUSE.1` | `DesctxSectrasScdxTransactions_BnfHouse1` | TField |  | Beneficiary service account holder house address |
| 31 | `DESCTX.SCDX.BNF.POST.CODE.1` | `DesctxSectrasScdxTransactions_BnfPostCode1` | TField |  | Beneficiary service account holder post code |
| 32 | `DESCTX.SCDX.BNF.TOWN.1` | `DesctxSectrasScdxTransactions_BnfTown1` | TField |  | Beneficiary service account holder town |
| 33 | `DESCTX.SCDX.BNF.CTRY.CODE.1` | `DesctxSectrasScdxTransactions_BnfCtryCode1` | TField |  | Beneficiary service account holder country code |
| 34 | `DESCTX.SCDX.BASE.AMT` | `DesctxSectrasScdxTransactions_BaseAmt` | TField |  | Base amount |
| 35 | `DESCTX.SCDX.TAX.INDICATOR` | `DesctxSectrasScdxTransactions_TaxIndicator` |  |  |  |
| 36 | `DESCTX.SCDX.TAX.AMOUNT` | `DesctxSectrasScdxTransactions_TaxAmount` |  |  |  |
| 37 | `DESCTX.SCDX.ISIN.NUMBER` | `DesctxSectrasScdxTransactions_IsinNumber` | TField |  | Isin number of the security master |
| 38 | `DESCTX.SCDX.EX.DATE` | `DesctxSectrasScdxTransactions_ExDate` | TField |  | Date of Diary execution |
| 39 | `DESCTX.SCDX.EVENT.TYPE` | `DesctxSectrasScdxTransactions_EventType` | TField |  | Event type of the diary |
| 40 | `DESCTX.SCDX.SZK.NUMBER` | `DesctxSectrasScdxTransactions_SzkNumber` | TField |  | Sort Number of the Corporate event |
| 41 | `DESCTX.SCDX.VERSION.NUMBER` | `DesctxSectrasScdxTransactions_VersionNumber` | TField |  |  |
| 42 | `DESCTX.SCDX.CORRECTION.IND` | `DesctxSectrasScdxTransactions_CorrectionInd` | TField |  | Indicator to see if the transaction is modified or not |
| 43 | `DESCTX.SCDX.INTERNAL.SECURITY` | `DesctxSectrasScdxTransactions_InternalSecurity` | TField |  | Flag to indicate if it is internal security or not |
| 44 | `DESCTX.SCDX.DATA.PROV.CODE` | `DesctxSectrasScdxTransactions_DataProvCode` | TField |  | Date provider code |
| 45 | `DESCTX.SCDX.BUS.YEAR.END` | `DesctxSectrasScdxTransactions_BusYearEnd` | TField |  | Business year end date |
| 46 | `DESCTX.SCDX.CANCEL.TRANS.IND` | `DesctxSectrasScdxTransactions_CancelTransInd` | TField |  | Indicator to see if the transaction is cancelled or not |
| 47 | `DESCTX.SCDX.CANCEL.DATE` | `DesctxSectrasScdxTransactions_CancelDate` | TField |  | Date on which the transaction is cancelled |
| 48 | `DESCTX.SCDX.BUY.SELL.IND` | `DesctxSectrasScdxTransactions_BuySellInd` | TField |  | Indicator to denote buy or sell |
| 49 | `DESCTX.SCDX.TRADE.TIME` | `DesctxSectrasScdxTransactions_TradeTime` | TField |  | Time on which the trade is put |
| 50 | `DESCTX.SCDX.DATA.ENRICH.IND` | `DesctxSectrasScdxTransactions_DataEnrichInd` | TField |  | Date Enrichment indicator |
| 51 | `DESCTX.SCDX.TRANS.METH` | `DesctxSectrasScdxTransactions_TransMeth` | TField |  | Transfer method indicator |
| 52 | `DESCTX.SCDX.TRADE.CCY.RATE` | `DesctxSectrasScdxTransactions_TradeCcyRate` | TField |  | Trade currency rate |
| 53 | `DESCTX.SCDX.PAY.CCY` | `DesctxSectrasScdxTransactions_PayCcy` | TField |  | Account currency |
| 54 | `DESCTX.SCDX.PAY.CCY.RATE` | `DesctxSectrasScdxTransactions_PayCcyRate` | TField |  | Account currency rate |
| 55 | `DESCTX.SCDX.BID.UPDATE` | `DesctxSectrasScdxTransactions_BidUpdate` | TField |  | Flag to see if Bid id to be updated or not |
| 56 | `DESCTX.SCDX.CUSTODY.DOM.IND` | `DesctxSectrasScdxTransactions_CustodyDomInd` | TField |  | Custody Domicile Indicator |
| 57 | `DESCTX.SCDX.APPLICATION` | `DesctxSectrasScdxTransactions_Application` | TField |  | Current application of the transaction |
| 58 | `DESCTX.SCDX.OPEN.CLOSE.IND` | `DesctxSectrasScdxTransactions_OpenCloseInd` | TField |  | Flag to indicate if it is DX open or close trade |
| 59 | `DESCTX.SCDX.CALL.PUT.IND` | `DesctxSectrasScdxTransactions_CallPutInd` | TField |  | Flag to indicate if it is DX call or put trade |
| 60 | `DESCTX.SCDX.LONG.SHORT.IND` | `DesctxSectrasScdxTransactions_LongShortInd` | TField |  | Flag to indicate if it is DX long or short trade |
| 61 | `DESCTX.SCDX.DX.SEC.TYPE` | `DesctxSectrasScdxTransactions_DxSecType` | TField |  | Security type of DX indicator |
| 62 | `DESCTX.SCDX.DX.SEC.NO` | `DesctxSectrasScdxTransactions_DxSecNo` | TField |  | Security number of DX trade |
| 63 | `DESCTX.SCDX.DX.PREMIUM.CCY` | `DesctxSectrasScdxTransactions_DxPremiumCcy` | TField |  | Trade currency of DX trade |
| 64 | `DESCTX.SCDX.LOCATION.REF` | `DesctxSectrasScdxTransactions_LocationRef` | TField |  | Location reference indicator |
| 65 | `DESCTX.SCDX.UNIQUE.LOCATION.IND` | `DesctxSectrasScdxTransactions_UniqueLocationInd` | TField |  |  |
| 66 | `DESCTX.SCDX.DX.STRIKE.PRICE` | `DesctxSectrasScdxTransactions_DxStrikePrice` | TField |  | Strike price of the DX trade |
| 67 | `DESCTX.SCDX.DX.EXPIRY.DATE` | `DesctxSectrasScdxTransactions_DxExpiryDate` | TField |  | Expiry date of the DX trade |
| 68 | `DESCTX.SCDX.PRICE` | `DesctxSectrasScdxTransactions_Price` | TField |  | Price amount |
| 69 | `DESCTX.SCDX.PRICE.DATE` | `DesctxSectrasScdxTransactions_PriceDate` | TField |  | Date on which the price amount is calculated |
| 70 | `DESCTX.SCDX.VALUE.DATE` | `DesctxSectrasScdxTransactions_ValueDate` | TField |  | Value date of the transaction |
| 71 | `DESCTX.SCDX.STOCK.EXCH` | `DesctxSectrasScdxTransactions_StockExch` | TField |  | Stock exchange involved in the transaction |
| 72 | `DESCTX.SCDX.LOCAL.REF` | `DesctxSectrasScdxTransactions_LocalRef` |  |  |  |
| 73 | `DESCTX.SCDX.DEPOSITORY` | `DesctxSectrasScdxTransactions_Depository` | TField |  | Depository involved in the transaction |
| 74 | `DESCTX.SCDX.TAX.STMT.ENTRY` | `DesctxSectrasScdxTransactions_TaxStmtEntry` |  |  |  |
| 75 | `DESCTX.SCDX.REFERENCE.BZR` | `DesctxSectrasScdxTransactions_ReferenceBzr` | TField |  | This field is to capture Rights reference BZR |
| 76 | `DESCTX.SCDX.UD.KD.EVENT.BZR` | `DesctxSectrasScdxTransactions_UdKdEventBzr` | TField |  | This field is to capture UD KD Event BZR |
| 77 | `DESCTX.SCDX.VD005.REF` | `DesctxSectrasScdxTransactions_Vd005Ref` | TField |  | This field is to capture the VD005 reference |
| 78 | `DESCTX.SCDX.VD036.REF` | `DesctxSectrasScdxTransactions_Vd036Ref` | TField |  | This field is to capture the VD036 reference |
| 79 | `DESCTX.SCDX.DX.INSTRUMENT.NO` | `DesctxSectrasScdxTransactions_DxInstrumentNo` | TField |  | This field is to capture contract code of derivative |
| 80 | `DESCTX.SCDX.DX.DIARY` | `DesctxSectrasScdxTransactions_DxDiary` | TField |  | This field is to capture diary number of derivative |
| 81 | `DESCTX.SCDX.OVERRIDE` | `DesctxSectrasScdxTransactions_Override` |  |  |  |
| 82 | `DESCTX.SCDX.RECORD.STATUS` | `DesctxSectrasScdxTransactions_RecordStatus` | String |  |  |
| 83 | `DESCTX.SCDX.CURR.NO` | `DesctxSectrasScdxTransactions_CurrNo` | String |  |  |
| 84 | `DESCTX.SCDX.INPUTTER` | `DesctxSectrasScdxTransactions_Inputter` |  |  |  |
| 85 | `DESCTX.SCDX.DATE.TIME` | `DesctxSectrasScdxTransactions_DateTime` |  |  |  |
| 86 | `DESCTX.SCDX.AUTHORISER` | `DesctxSectrasScdxTransactions_Authoriser` | String |  |  |
| 87 | `DESCTX.SCDX.CO.CODE` | `DesctxSectrasScdxTransactions_CoCode` | String |  |  |
| 88 | `DESCTX.SCDX.DEPT.CODE` | `DesctxSectrasScdxTransactions_DeptCode` | String |  |  |
| 89 | `DESCTX.SCDX.AUDITOR.CODE` | `DesctxSectrasScdxTransactions_AuditorCode` | String |  |  |
| 90 | `DESCTX.SCDX.AUDIT.DATE.TIME` | `DesctxSectrasScdxTransactions_AuditDateTime` | String |  |  |
| 91 | `DESCTX.SCDX.SOURCE` | `DesctxSectrasScdxTransactions_Source` | TField |  | Business area of releated transaction |
| 92 | `DESCTX.SCDX.VERSION.NO.EXT` | `DesctxSectrasScdxTransactions_VersionNoExt` | TField |  | Version Number Client |
| 93 | `DESCTX.SCDX.ENTITY.CODE` | `DesctxSectrasScdxTransactions_EntityCode` | TField |  | Entity Identifier |
| 94 | `DESCTX.SCDX.AMNT.INPUT.IND` | `DesctxSectrasScdxTransactions_AmntInputInd` | TField |  | Amount indicator |
| 95 | `DESCTX.SCDX.WORKFLOW.ENTRY` | `DesctxSectrasScdxTransactions_WorkflowEntry` | TField |  | Workflow entry point |
| 96 | `DESCTX.SCDX.SIM.IND` | `DesctxSectrasScdxTransactions_SimInd` | TField |  | Simulation Indicator |
| 97 | `DESCTX.SCDX.DELTA.IND` | `DesctxSectrasScdxTransactions_DeltaInd` | TField |  | Delta correction indicator |
| 98 | `DESCTX.SCDX.OBJ.TYPE` | `DesctxSectrasScdxTransactions_ObjType` | TField |  | Account identifier type |
| 99 | `DESCTX.SCDX.EXT.CODE.ACCT` | `DesctxSectrasScdxTransactions_ExtCodeAcct` | TField |  | Account number |
| 100 | `DESCTX.SCDX.SEC.CODE.TYPE` | `DesctxSectrasScdxTransactions_SecCodeType` | TField |  | Securities identifier type |
| 101 | `DESCTX.SCDX.SEC.CODE` | `DesctxSectrasScdxTransactions_SecCode` | TField |  | Securities identifier |
| 102 | `DESCTX.SCDX.SEC.PROD.TYPE` | `DesctxSectrasScdxTransactions_SecProdType` | TField |  | Securities type |
| 103 | `DESCTX.SCDX.SEC.SHORT.CODE` | `DesctxSectrasScdxTransactions_SecShortCode` | TField |  | Security short name |
| 104 | `DESCTX.SCDX.VVT.IND` | `DesctxSectrasScdxTransactions_VvtInd` | TField |  | Lost consumption account equities indicator |
| 105 | `DESCTX.SCDX.REPL.VALUE.IND` | `DesctxSectrasScdxTransactions_ReplValueInd` | TField |  | Replacement Value Indicator |
| 106 | `DESCTX.SCDX.TRANSP.IND` | `DesctxSectrasScdxTransactions_TranspInd` | TField |  | Transperancy Indicator |
| 107 | `DESCTX.SCDX.POST.TRN.REF` | `DesctxSectrasScdxTransactions_PostTrnRef` | TField |  | Booking Number |
| 108 | `DESCTX.SCDX.DEVIATE.INC.DATE` | `DesctxSectrasScdxTransactions_DeviateIncDate` | TField |  | Deviate Income Date |
| 109 | `DESCTX.SCDX.EAV.IND` | `DesctxSectrasScdxTransactions_EavInd` | TField |  | Equation of earnings indicator |
| 110 | `DESCTX.SCDX.INTR.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_IntrAmntTrdCcy` | TField |  | Interest in trade currency |
| 111 | `DESCTX.SCDX.SIR.ACCR.INTR.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_SirAccrIntrAmntTrdCcy` | TField |  | Notification amount EU direcitve (accrued interest) in trade currency |
| 112 | `DESCTX.SCDX.SIR.SALES.TOTAL.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_SirSalesTotalAmntTrdCcy` | TField |  | Notification amount EU directive (sales revenue) in trade currency |
| 113 | `DESCTX.SCDX.PROFIT.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_ProfitAmntTrdCcy` | TField |  | Profit in trade currency |
| 114 | `DESCTX.SCDX.LOSS.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_LossAmntTrdCcy` | TField |  | Loss in trade currency |
| 115 | `DESCTX.SCDX.LUMP.SUM.IND` | `DesctxSectrasScdxTransactions_LumpSumInd` | TField |  | Lump sum indicator |
| 116 | `DESCTX.SCDX.LUMP.SUM.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_LumpSumAmntTrdCcy` | TField |  | Lump sum amount in trade currency |
| 117 | `DESCTX.SCDX.AKAE.AMNT.DIFF.TRD.CCY` | `DesctxSectrasScdxTransactions_AkaeAmntDiffTrdCcy` | TField |  | Profit of accumulated deemed distribution in trade currency |
| 118 | `DESCTX.SCDX.FWT.DEDU.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_FwtDeduAmntTrdCcy` | TField |  | Deducted foreign tax amount in trade / income currency |
| 119 | `DESCTX.SCDX.FWT.CHARG.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_FwtChargAmntTrdCcy` | TField |  | Chargeable foreign tax amount in trade / income currency |
| 120 | `DESCTX.SCDX.ADD.TRN.INFO` | `DesctxSectrasScdxTransactions_AddTrnInfo` | TField |  | Additional transaction information |
| 121 | `DESCTX.SCDX.DETAIL.STATUS` | `DesctxSectrasScdxTransactions_DetailStatus` | TField |  | Detail status |
| 122 | `DESCTX.SCDX.AGID` | `DesctxSectrasScdxTransactions_Agid` | TField |  | Segment indicator |
| 123 | `DESCTX.SCDX.MAINT.USER.ID` | `DesctxSectrasScdxTransactions_MaintUserId` | TField |  | User identifier |
| 124 | `DESCTX.SCDX.OBJ.ID` | `DesctxSectrasScdxTransactions_ObjId` | TField |  | Securities Account Identifier |
| 125 | `DESCTX.SCDX.PARTNER.GRP.ID` | `DesctxSectrasScdxTransactions_PartnerGrpId` | TField |  | Partner group identifier |
| 126 | `DESCTX.SCDX.SEC.ID` | `DesctxSectrasScdxTransactions_SecId` | TField |  | Securities Identifier |
| 127 | `DESCTX.SCDX.INT.EARNING` | `DesctxSectrasScdxTransactions_IntEarning` | TField |  | Interim earning per unit in trade currency |
| 128 | `DESCTX.SCDX.AKAE` | `DesctxSectrasScdxTransactions_Akae` | TField |  | Accumulated deemed distribution income per unit in trade currency |
| 129 | `DESCTX.SCDX.AKAE.CCY` | `DesctxSectrasScdxTransactions_AkaeCcy` | TField |  | Currency of accumulated deemed distribution income |
| 130 | `DESCTX.SCDX.AKAE.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_AkaeAmntTrdCcy` | TField |  | Accumulated deemed distribution income in trade currency |
| 131 | `DESCTX.SCDX.FEE.AMNT.TOTAL.TRD.CCY` | `DesctxSectrasScdxTransactions_FeeAmntTotalTrdCcy` | TField |  | Transacion fee in trade currency |
| 132 | `DESCTX.SCDX.PRICE.FACTOR` | `DesctxSectrasScdxTransactions_PriceFactor` | TField |  | Price Factor |
| 133 | `DESCTX.SCDX.QUOTE.TYPE` | `DesctxSectrasScdxTransactions_QuoteType` | TField |  | Quote Type |
| 134 | `DESCTX.SCDX.INDEX.FACTOR` | `DesctxSectrasScdxTransactions_IndexFactor` | TField |  | Index Factor |
| 135 | `DESCTX.SCDX.GRANDFATHERING.TYPE` | `DesctxSectrasScdxTransactions_GrandfatheringType` | TField |  | Grandfathering Indicator |
| 136 | `DESCTX.SCDX.ACQUISITION.AMNT.IND` | `DesctxSectrasScdxTransactions_AcquisitionAmntInd` | TField |  | Acquisition Amount Indicator |
| 137 | `DESCTX.SCDX.HIST.HOLDING.IND` | `DesctxSectrasScdxTransactions_HistHoldingInd` | TField |  | History Holding Indicator |
| 138 | `DESCTX.SCDX.TRANS.AREA` | `DesctxSectrasScdxTransactions_TransArea` | TField |  | Transfer Area Indicator |
| 139 | `DESCTX.SCDX.EXT.TRN.REF` | `DesctxSectrasScdxTransactions_ExtTrnRef` | TField |  | External reference number |
| 140 | `DESCTX.SCDX.INVEST.FUND.LAW.IND` | `DesctxSectrasScdxTransactions_InvestFundLawInd` | TField |  | Application of Investment Tax Act |
| 141 | `DESCTX.SCDX.INVEST.FUND.TAX.EXEMPT.RATE` | `DesctxSectrasScdxTransactions_InvestFundTaxExemptRate` | TField |  | Partial tax exemption (percentage) |
| 142 | `DESCTX.SCDX.FUND.PRE.LUMPSUM.M` | `DesctxSectrasScdxTransactions_FundPreLumpsumM` | TField |  | Preliminary Lump Sum p per unit and month (EUR) |
| 143 | `DESCTX.SCDX.FUND.PRE.LUMPSUM.Y` | `DesctxSectrasScdxTransactions_FundPreLumpsumY` | TField |  | Preliminary Lump Sum p per unit and year (EUR) |
| 144 | `DESCTX.SCDX.FUND.ACCU.TAXFREE` | `DesctxSectrasScdxTransactions_FundAccuTaxfree` | TField |  | Accumulated tax free asset distribution per unit (in EUR) |
| 145 | `DESCTX.SCDX.AKAE.PRICE.RETAINED` | `DesctxSectrasScdxTransactions_AkaePriceRetained` | TField |  | Estimated accumulated deemed distribution income amount |
| 146 | `DESCTX.SCDX.ACCU.SURPLUS` | `DesctxSectrasScdxTransactions_AccuSurplus` | TField |  | Accumulated increase amount |
| 147 | `DESCTX.SCDX.REALITY.PROFIT` | `DesctxSectrasScdxTransactions_RealityProfit` | TField |  | Tax free capital gain from foreing real property amount |
| 148 | `DESCTX.SCDX.REALITY.PROFIT.CCY` | `DesctxSectrasScdxTransactions_RealityProfitCcy` | TField |  | Currency of the Tax free capital gain from foreing real property amount |
| 149 | `DESCTX.SCDX.REALITY.PROFIT.CCY.RATE` | `DesctxSectrasScdxTransactions_RealityProfitCcyRate` | TField |  | Currency Rate |
| 150 | `DESCTX.SCDX.ACCU.PROFIT.FUND` | `DesctxSectrasScdxTransactions_AccuProfitFund` | TField |  | Accumulated capital gain amount before 1.1.2009 |
| 151 | `DESCTX.SCDX.ACCU.PROFIT.FUND.CCY` | `DesctxSectrasScdxTransactions_AccuProfitFundCcy` | TField |  | Currency of accumulated capital gain amount before 1.1.2009 |
| 152 | `DESCTX.SCDX.ACCU.PROFIT.FUND.CCY.RATE` | `DesctxSectrasScdxTransactions_AccuProfitFundCcyRate` | TField |  | Currency rate |
| 153 | `DESCTX.SCDX.AKAE.ADJUSTED` | `DesctxSectrasScdxTransactions_AkaeAdjusted` | TField |  | Rectified accumulated deemed distributed income amount |
| 154 | `DESCTX.SCDX.ACCU.SUBS.PROFIT` | `DesctxSectrasScdxTransactions_AccuSubsProfit` | TField |  | Accumulated substance distribution amount |
| 155 | `DESCTX.SCDX.TAX.DEPT.ACCT.PRICE` | `DesctxSectrasScdxTransactions_TaxDeptAcctPrice` | TField |  | Price of tax deposit account |
| 156 | `DESCTX.SCDX.UNDERLYING.CODE.TYPE` | `DesctxSectrasScdxTransactions_UnderlyingCodeType` | TField |  | Securities identifier type |
| 157 | `DESCTX.SCDX.UNDERLYING.CODE` | `DesctxSectrasScdxTransactions_UnderlyingCode` | TField |  | Securities identifier |
| 158 | `DESCTX.SCDX.OPT.REF` | `DesctxSectrasScdxTransactions_OptRef` | TField |  | Reference option |
| 159 | `DESCTX.SCDX.CLOSE.REASON` | `DesctxSectrasScdxTransactions_CloseReason` | TField |  | Close reason |
| 160 | `DESCTX.SCDX.BNF.LAST.NAME.2` | `DesctxSectrasScdxTransactions_BnfLastName2` | TField |  | Beneficiary Last name 2 |
| 161 | `DESCTX.SCDX.BNF.FIRST.NAME.2` | `DesctxSectrasScdxTransactions_BnfFirstName2` | TField |  | Beneficiary First name 2 |
| 162 | `DESCTX.SCDX.BNF.BIRTH.DATE.2` | `DesctxSectrasScdxTransactions_BnfBirthDate2` | TField |  | Beneficiary Birth date 2 |
| 163 | `DESCTX.SCDX.BNF.TIN.2` | `DesctxSectrasScdxTransactions_BnfTin2` | TField |  | Beneficiary Tin number 2 |
| 164 | `DESCTX.SCDX.BNF.STREET.2` | `DesctxSectrasScdxTransactions_BnfStreet2` | TField |  | Beneficiary Street 2 |
| 165 | `DESCTX.SCDX.BNF.HOUSE.2` | `DesctxSectrasScdxTransactions_BnfHouse2` | TField |  | Beneficiary House 2 |
| 166 | `DESCTX.SCDX.BNF.POST.CODE.2` | `DesctxSectrasScdxTransactions_BnfPostCode2` | TField |  | Beneficiary post code 2 |
| 167 | `DESCTX.SCDX.BNF.TOWN.2` | `DesctxSectrasScdxTransactions_BnfTown2` | TField |  | Beneficiary Town 2 |
| 168 | `DESCTX.SCDX.BNF.CTRY.CODE.2` | `DesctxSectrasScdxTransactions_BnfCtryCode2` | TField |  | Beneficiary Country code 2 |
| 169 | `DESCTX.SCDX.BNF.IBAN` | `DesctxSectrasScdxTransactions_BnfIban` | TField |  | Beneficiary IBAN 2 |
| 170 | `DESCTX.SCDX.PAGINATION.ID` | `DesctxSectrasScdxTransactions_PaginationId` | TField |  | Pagination identifier |
| 171 | `DESCTX.SCDX.SIR.DEPT.CLASS` | `DesctxSectrasScdxTransactions_SirDeptClass` | TField |  | Classification EU saving directive |
| 172 | `DESCTX.SCDX.CUM.EX.IND` | `DesctxSectrasScdxTransactions_CumExInd` | TField |  | Cum / Ex indicator |
| 173 | `DESCTX.SCDX.TAX.STMT.CBF.IND` | `DesctxSectrasScdxTransactions_TaxStmtCbfInd` | TField |  | Tax statement Clearstream banking Frankfurt indicator |
| 174 | `DESCTX.SCDX.TAX.AGENT` | `DesctxSectrasScdxTransactions_TaxAgent` | TField |  | Tax Agent |
| 175 | `DESCTX.SCDX.FED.STATE.ISSUER` | `DesctxSectrasScdxTransactions_FedStateIssuer` | TField |  | Federal state issuer |
| 176 | `DESCTX.SCDX.GROSS.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_GrossAmntTrdCcy` | TField |  | Gross amount in trade / income currency |
| 177 | `DESCTX.SCDX.DIVD.PAY.TRD.CCY` | `DesctxSectrasScdxTransactions_DivdPayTrdCcy` | TField |  | Domestic dividend portion paying agent in trade / income currency |
| 178 | `DESCTX.SCDX.DIVD.ISSUER.TRD.CCY` | `DesctxSectrasScdxTransactions_DivdIssuerTrdCcy` | TField |  | Domestic dividend portion issuer in trade / income currency |
| 179 | `DESCTX.SCDX.DIVF.PAY.TRD.CCY` | `DesctxSectrasScdxTransactions_DivfPayTrdCcy` | TField |  | Foreign dividend portion in trade / income currency |
| 180 | `DESCTX.SCDX.DIV.DR.BASE.CCY` | `DesctxSectrasScdxTransactions_DivDrBaseCcy` | TField |  | Dividend portion ADR in trade / income currency |
| 181 | `DESCTX.SCDX.RENTAL.INCOME.TRD.CCY` | `DesctxSectrasScdxTransactions_RentalIncomeTrdCcy` | TField |  | Taxable rental income in trade / income currency |
| 182 | `DESCTX.SCDX.TAX.LIQU.FUND.TRD.CCY` | `DesctxSectrasScdxTransactions_TaxLiquFundTrdCcy` | TField |  | Tax liquidity amount for german accumulation funds |
| 183 | `DESCTX.SCDX.INCOME.CCY` | `DesctxSectrasScdxTransactions_IncomeCcy` | TField |  | Income Currency |
| 184 | `DESCTX.SCDX.INCOME.CCY.RATE` | `DesctxSectrasScdxTransactions_IncomeCcyRate` | TField |  | Income Currency Rate |
| 185 | `DESCTX.SCDX.ACCUM.IND` | `DesctxSectrasScdxTransactions_AccumInd` | TField |  | Accumulation Indicator |
| 186 | `DESCTX.SCDX.FWT.VIRT.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_FwtVirtAmntTrdCcy` | TField |  | Virtual foreign withholding tax |
| 187 | `DESCTX.SCDX.FUND.DISTR.TRD.CCY` | `DesctxSectrasScdxTransactions_FundDistrTrdCcy` | TField |  | Fund distribution |
| 188 | `DESCTX.SCDX.FUND.DISTR.EXPT.TRD.CCY` | `DesctxSectrasScdxTransactions_FundDistrExptTrdCcy` | TField |  | Taxable distribution after partial exemption |
| 189 | `DESCTX.SCDX.INVEST.FUND.LIQUIDATION.IND` | `DesctxSectrasScdxTransactions_InvestFundLiquidationInd` | TField |  | Investment fund in liquidation indicator |
| 190 | `DESCTX.SCDX.TAX.DEP.ACCT.IND` | `DesctxSectrasScdxTransactions_TaxDepAcctInd` | TField |  | Tax debit account indicator |
| 191 | `DESCTX.SCDX.INTR.PERIOD.FROM` | `DesctxSectrasScdxTransactions_IntrPeriodFrom` | TField |  | Interest period start |
| 192 | `DESCTX.SCDX.INTR.PERIOD.TO` | `DesctxSectrasScdxTransactions_IntrPeriodTo` | TField |  | Interest period end |
| 193 | `DESCTX.SCDX.SIR.CE.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_SirCeAmntTrdCcy` | TField |  | Notification amount EU direcitve |
| 194 | `DESCTX.SCDX.DDI.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_DdiAmntTrdCcy` | TField |  | Deemed distribution amount |
| 195 | `DESCTX.SCDX.HOLD.PERIOD.VIOLATION.IND` | `DesctxSectrasScdxTransactions_HoldPeriodViolationInd` | TField |  | Violation holding period |
| 196 | `DESCTX.SCDX.POS.CALC` | `DesctxSectrasScdxTransactions_PosCalc` | TField |  | Position Calculation |
| 197 | `DESCTX.SCDX.POS.DATE` | `DesctxSectrasScdxTransactions_PosDate` | TField |  | Date Position Calculation |
| 198 | `DESCTX.SCDX.EQUITY.RELATED.INCOME.IND` | `DesctxSectrasScdxTransactions_EquityRelatedIncomeInd` | TField |  | Equity related income indicator |
| 199 | `DESCTX.SCDX.CONV.IND` | `DesctxSectrasScdxTransactions_ConvInd` | TField |  | Conversion Indicator |
| 200 | `DESCTX.SCDX.PAYMENT.AMNT.BASE.CCY` | `DesctxSectrasScdxTransactions_PaymentAmntBaseCcy` | TField |  | Payment amount |
| 201 | `DESCTX.SCDX.PAYMENT.TYPE` | `DesctxSectrasScdxTransactions_PaymentType` | TField |  |  |
| 202 | `DESCTX.SCDX.WM.FIELD.OF.ACTIVITY` | `DesctxSectrasScdxTransactions_WmFieldOfActivity` | TField |  | WM Field of Activity |
| 203 | `DESCTX.SCDX.CLIENT` | `DesctxSectrasScdxTransactions_Client` | TField |  | Client |
| 204 | `DESCTX.SCDX.DATE.OF.ACTION` | `DesctxSectrasScdxTransactions_DateOfAction` | TField |  | Date of Action |
| 205 | `DESCTX.SCDX.REFERENCE` | `DesctxSectrasScdxTransactions_Reference` | TField |  | Reference |
| 206 | `DESCTX.SCDX.RESEND.FLAG` | `DesctxSectrasScdxTransactions_ResendFlag` | TField |  | Resend Flag |
| 207 | `DESCTX.SCDX.RETURN.CODE` | `DesctxSectrasScdxTransactions_ReturnCode` | TField |  | Return code |
| 208 | `DESCTX.SCDX.RETURN.TEXT` | `DesctxSectrasScdxTransactions_ReturnText` | TField |  | Return Text |
| 209 | `DESCTX.SCDX.TAX.STATUS` | `DesctxSectrasScdxTransactions_TaxStatus` | TField |  | Tax Status |
| 210 | `DESCTX.SCDX.TAX.STATUS.APPL` | `DesctxSectrasScdxTransactions_TaxStatusAppl` | TField |  | Applied Tax Status |
| 211 | `DESCTX.SCDX.CASSIT.NO` | `DesctxSectrasScdxTransactions_CassitNo` | TField |  | Cassit Number |
| 212 | `DESCTX.SCDX.CIN.P1` | `DesctxSectrasScdxTransactions_CinP1` | TField |  | Customer identification number P1 |
| 213 | `DESCTX.SCDX.RELI.DENOM.P1` | `DesctxSectrasScdxTransactions_ReliDenomP1` | TField |  | Religion denomination Partner 1 |
| 214 | `DESCTX.SCDX.CT.RATE.P1` | `DesctxSectrasScdxTransactions_CtRateP1` | TField |  | Church tax rate Partner 1 |
| 215 | `DESCTX.SCDX.CIN.P2` | `DesctxSectrasScdxTransactions_CinP2` | TField |  | Customer identification number P2 |
| 216 | `DESCTX.SCDX.RELI.DENOM.P2` | `DesctxSectrasScdxTransactions_ReliDenomP2` | TField |  | Religion denomination Partner 2 |
| 217 | `DESCTX.SCDX.CT.RATE.P2` | `DesctxSectrasScdxTransactions_CtRateP2` | TField |  | Church tax rate Partner 2 |
| 218 | `DESCTX.SCDX.TAX.CERT.IND` | `DesctxSectrasScdxTransactions_TaxCertInd` | TField |  | Reclaim indicator for tax certificate |
| 219 | `DESCTX.SCDX.LCA.CERT.IND` | `DesctxSectrasScdxTransactions_LcaCertInd` | TField |  | Reclaim indicator for loss consumption report |
| 220 | `DESCTX.SCDX.FA.TYPE` | `DesctxSectrasScdxTransactions_FaType` | TField |  | Product Code |
| 221 | `DESCTX.SCDX.DE.TAX.FLAG` | `DesctxSectrasScdxTransactions_DeTaxFlag` | TField |  | Tax Exclusion Flag |
| 222 | `DESCTX.SCDX.CT.TCI.P1` | `DesctxSectrasScdxTransactions_CtTciP1` | TField |  | Church tax calculation indicator Partner 1 |
| 223 | `DESCTX.SCDX.CT.TCI.P2` | `DesctxSectrasScdxTransactions_CtTciP2` | TField |  | Church tax calculation indicator Partner 2 |
| 224 | `DESCTX.SCDX.NAC.TYPE` | `DesctxSectrasScdxTransactions_NacType` | TField |  | Type of non assessment certificate |
| 225 | `DESCTX.SCDX.NAC.ID` | `DesctxSectrasScdxTransactions_NacId` | TField |  | non assessment certificate identification |
| 226 | `DESCTX.SCDX.NAC.VALID.FROM` | `DesctxSectrasScdxTransactions_NacValidFrom` | TField |  | Valid from date of the non assessment certificate |
| 227 | `DESCTX.SCDX.NAC.VALID.TO` | `DesctxSectrasScdxTransactions_NacValidTo` | TField |  | Valid to date of the non assessment certificate |
| 228 | `DESCTX.SCDX.TAX.ALLOW` | `DesctxSectrasScdxTransactions_TaxAllow` | TField |  | Tax Allowance |
| 229 | `DESCTX.SCDX.PART.PERCENT.P1` | `DesctxSectrasScdxTransactions_PartPercentP1` | TField |  | Participation percentage partner 1 |
| 230 | `DESCTX.SCDX.PART.PERCENT.P2` | `DesctxSectrasScdxTransactions_PartPercentP2` | TField |  | Participation percentage partner 2 |
| 231 | `DESCTX.SCDX.AGS.PROV` | `DesctxSectrasScdxTransactions_AgsProv` | TField |  | Province |
| 232 | `DESCTX.SCDX.LEGAL.TYPE` | `DesctxSectrasScdxTransactions_LegalType` | TField |  | Legal Type |
| 233 | `DESCTX.SCDX.CODE.TAX.COLLECT.ORG.UNIT.P1` | `DesctxSectrasScdxTransactions_CodeTaxCollectOrgUnitP1` | TField |  | Numeric code of the tax collectable organization unit Partner 1 |
| 234 | `DESCTX.SCDX.NAME.TAX.COLLECT.ORG.UNIT.P1` | `DesctxSectrasScdxTransactions_NameTaxCollectOrgUnitP1` | TField |  | Name of the tax collectable organization unit Partner 1 |
| 235 | `DESCTX.SCDX.CODE.TAX.COLLECT.ORG.UNIT.P2` | `DesctxSectrasScdxTransactions_CodeTaxCollectOrgUnitP2` | TField |  | Numeric code of the tax collectable organization unit Partner 2 |
| 236 | `DESCTX.SCDX.NAME.TAX.COLLECT.ORG.UNIT.P2` | `DesctxSectrasScdxTransactions_NameTaxCollectOrgUnitP2` | TField |  | Name of the tax collectable organization unit Partner 2 |
| 237 | `DESCTX.SCDX.EQUITY.PROFIT.ESTG.AMNT` | `DesctxSectrasScdxTransactions_EquityProfitEstgAmnt` | TField |  | Equity Profit Business Asset EStG |
| 238 | `DESCTX.SCDX.EQUITY.PROFIT.ESTG.CCY` | `DesctxSectrasScdxTransactions_EquityProfitEstgCcy` | TField |  | Currency Equity Profit Business Asset EStG |
| 239 | `DESCTX.SCDX.EQUITY.PROFIT.ESTG.WM` | `DesctxSectrasScdxTransactions_EquityProfitEstgWm` | TField |  | Percentage Equity Profit Business Asset EStG |
| 240 | `DESCTX.SCDX.EQUITY.PROFIT.KSTG.AMNT` | `DesctxSectrasScdxTransactions_EquityProfitKstgAmnt` | TField |  | Equity Profit Business Asset KStG |
| 241 | `DESCTX.SCDX.EQUITY.PROFIT.KSTG.CCY` | `DesctxSectrasScdxTransactions_EquityProfitKstgCcy` | TField |  | Currency Equity Profit Business Asset KStG |
| 242 | `DESCTX.SCDX.EQUITY.PROFIT.KSTG.WM` | `DesctxSectrasScdxTransactions_EquityProfitKstgWm` | TField |  | Percentage Equity Profit Business Asset KStG |
| 243 | `DESCTX.SCDX.REALITY.PROFIT.AMNT` | `DesctxSectrasScdxTransactions_RealityProfitAmnt` | TField |  | Tax free capital gain from foreign real property |
| 244 | `DESCTX.SCDX.REALITY.PROFIT.WM` | `DesctxSectrasScdxTransactions_RealityProfitWm` | TField |  | Percentage tax free capital gain from foreign real property |
| 245 | `DESCTX.SCDX.INT.PROF.PRICE.WM` | `DesctxSectrasScdxTransactions_IntProfPriceWm` | TField |  | Interim profit price per unit |
| 246 | `DESCTX.SCDX.INT.PROF.PRICE.CCY.WM` | `DesctxSectrasScdxTransactions_IntProfPriceCcyWm` | TField |  | Currency of Interim profit price per unit |
| 247 | `DESCTX.SCDX.INT.PROF.PRICE.DATE.WM` | `DesctxSectrasScdxTransactions_IntProfPriceDateWm` | TField |  | Date of interim profit price |
| 248 | `DESCTX.SCDX.AKAE.PER.UNIT.WM` | `DesctxSectrasScdxTransactions_AkaePerUnitWm` | TField |  | Accumulated deemed distribution income per unit |
| 249 | `DESCTX.SCDX.AKAE.DATE.WM` | `DesctxSectrasScdxTransactions_AkaeDateWm` | TField |  | Date as of which the Accumulated deemed distribution income was effected |
| 250 | `DESCTX.SCDX.QTY.HOLD.PERIOD.VIOLATION` | `DesctxSectrasScdxTransactions_QtyHoldPeriodViolation` | TField |  | Quantity holding period violation |
| 251 | `DESCTX.SCDX.AMNT.IND` | `DesctxSectrasScdxTransactions_AmntInd` |  |  |  |
| 252 | `DESCTX.SCDX.CALC.IND` | `DesctxSectrasScdxTransactions_CalcInd` |  |  |  |
| 253 | `DESCTX.SCDX.NULL.CALC.IND` | `DesctxSectrasScdxTransactions_NullCalcInd` |  |  |  |
| 254 | `DESCTX.SCDX.AMNT.TRD.CCY` | `DesctxSectrasScdxTransactions_AmntTrdCcy` |  |  |  |
| 255 | `DESCTX.SCDX.AMNT.PAY.CCY` | `DesctxSectrasScdxTransactions_AmntPayCcy` |  |  |  |
| 256 | `DESCTX.SCDX.AMNT.BASE.CCY` | `DesctxSectrasScdxTransactions_AmntBaseCcy` |  |  |  |
| 257 | `DESCTX.SCDX.CANC.TRN.REF` | `DesctxSectrasScdxTransactions_CancTrnRef` | TField |  | Cancellation transaction number |
| 258 | `DESCTX.SCDX.DIARY.NO` | `DesctxSectrasScdxTransactions_DiaryNo` | TField |  | Diary Number |
| 259 | `DESCTX.SCDX.EVENT.CASH.RATE` | `DesctxSectrasScdxTransactions_EventCashRate` | TField |  | Cash event rate |
| 260 | `DESCTX.SCDX.EVENT.CURRENCY` | `DesctxSectrasScdxTransactions_EventCurrency` | TField |  | Event currency |
| 261 | `DESCTX.SCDX.REV.TAX.STMT.ENTRY` | `DesctxSectrasScdxTransactions_RevTaxStmtEntry` |  |  |  |
| 262 | `DESCTX.SCDX.NEW.REBATE.AMT` | `DesctxSectrasScdxTransactions_NewRebateAmt` | TField |  | New Rebate Amount for Modified Trailer Fees |
| 263 | `DESCTX.SCDX.BOOKING.DATE` | `DesctxSectrasScdxTransactions_BookingDate` | TField |  | Booking Date |
