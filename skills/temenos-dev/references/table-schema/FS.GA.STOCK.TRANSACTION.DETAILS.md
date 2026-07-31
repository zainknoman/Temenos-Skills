# FS.GA.STOCK.TRANSACTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GA.STOCK.TRANSACTION.DETAILS` in `FS_StockTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STOCK.TRANSACTION.DETAILS.PARENT.REF.ID` | `FsGaStockTransactionDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STOCK.TRANSACTION.DETAILS.ORA.ROWID` | `FsGaStockTransactionDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STOCK.TRANSACTION.DETAILS.FUND.ID` | `FsGaStockTransactionDetails_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.STOCK.TRANSACTION.DETAILS.SERVICE.CODE` | `FsGaStockTransactionDetails_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.STOCK.TRANSACTION.DETAILS.TRANSACTION.NUMBER` | `FsGaStockTransactionDetails_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.STOCK.TRANSACTION.DETAILS.NEXT` | `FsGaStockTransactionDetails_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 7 | `FS.GA.STOCK.TRANSACTION.DETAILS.INTERNAL.SECURITY.ID` | `FsGaStockTransactionDetails_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 8 | `FS.GA.STOCK.TRANSACTION.DETAILS.DEPOSITORY.NUMBER` | `FsGaStockTransactionDetails_DepositoryNumber` | TField |  | Depositary Number Multifonds DB Column is NDEPOSIT. |
| 9 | `FS.GA.STOCK.TRANSACTION.DETAILS.LOT.NUMBER` | `FsGaStockTransactionDetails_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 10 | `FS.GA.STOCK.TRANSACTION.DETAILS.TRADE.DATE` | `FsGaStockTransactionDetails_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 11 | `FS.GA.STOCK.TRANSACTION.DETAILS.QUANTITY` | `FsGaStockTransactionDetails_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 12 | `FS.GA.STOCK.TRANSACTION.DETAILS.TRANSACTION.PRICE` | `FsGaStockTransactionDetails_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 13 | `FS.GA.STOCK.TRANSACTION.DETAILS.USED.QUANTITY` | `FsGaStockTransactionDetails_UsedQuantity` | TField |  | Quantity which is used for closing Multifonds DB Column is QUANTITE_USED. |
| 14 | `FS.GA.STOCK.TRANSACTION.DETAILS.GROSS.AMOUNT.IN.LOCAL.CCY` | `FsGaStockTransactionDetails_GrossAmountInLocalCcy` | TField |  | Gross amount in security currency Multifonds DB Column is MONTANT_OPER. |
| 15 | `FS.GA.STOCK.TRANSACTION.DETAILS.TRANSACTION.FEES.AMOUNT` | `FsGaStockTransactionDetails_TransactionFeesAmount` | TField |  | This field denotes the fee amount of the transaction Multifonds DB Column is MFRAIS_OPER. |
| 16 | `FS.GA.STOCK.TRANSACTION.DETAILS.ACCRUED.INTEREST.AMOUNT` | `FsGaStockTransactionDetails_AccruedInterestAmount` | TField |  | Purchase/sale interest on a interest bearing instrument Multifonds DB Column is MINT_OPER. |
| 17 | `FS.GA.STOCK.TRANSACTION.DETAILS.RATE.OF.EXCHANGE` | `FsGaStockTransactionDetails_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 18 | `FS.GA.STOCK.TRANSACTION.DETAILS.NET.AMOUNT.IN.SECURITY.CCY` | `FsGaStockTransactionDetails_NetAmountInSecurityCcy` | TField |  | Net amount in security currency Multifonds DB Column is MONTNET_OPER. |
| 19 | `FS.GA.STOCK.TRANSACTION.DETAILS.NET.SETTLEMENT.AMOUNT` | `FsGaStockTransactionDetails_NetSettlementAmount` | TField |  | Net settlement amount on a transaction Multifonds DB Column is MONTNET_CPT. |
| 20 | `FS.GA.STOCK.TRANSACTION.DETAILS.MANAGER.CODE` | `FsGaStockTransactionDetails_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 21 | `FS.GA.STOCK.TRANSACTION.DETAILS.UNREC.TAX.IN.AMOUNT.TYPE.1` | `FsGaStockTransactionDetails_UnrecTaxInAmountType1` | TField |  | Unrecoverable tax amount on Income , type 1 Multifonds DB Column is MNTUNRECTAX. |
| 22 | `FS.GA.STOCK.TRANSACTION.DETAILS.UNREC.TAX.IN.AMOUNT.TYPE.2` | `FsGaStockTransactionDetails_UnrecTaxInAmountType2` | TField |  | Unrecoverable tax amount on Income , type 2 Multifonds DB Column is MNTUNRECTAX_2. |
| 23 | `FS.GA.STOCK.TRANSACTION.DETAILS.REC.TAX.IN.AMOUNT.TYPE.1` | `FsGaStockTransactionDetails_RecTaxInAmountType1` | TField |  | Recoverable tax amount on Income , type 1 Multifonds DB Column is MNTRECTAX. |
| 24 | `FS.GA.STOCK.TRANSACTION.DETAILS.RETROCESSION.COMMISSION.AMOUNT` | `FsGaStockTransactionDetails_RetrocessionCommissionAmount` | TField |  | Recoverable tax amount on Income , type 2 Multifonds DB Column is MNTRECTAX_2. |
| 25 | `FS.GA.STOCK.TRANSACTION.DETAILS.ARCHIVE` | `FsGaStockTransactionDetails_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 26 | `FS.GA.STOCK.TRANSACTION.DETAILS.PIK.INTEREST.AMOUNT` | `FsGaStockTransactionDetails_PikInterestAmount` | TField |  | PIK Interest Amount Multifonds DB Column is PIK_MINT_OPER. |
| 27 | `FS.GA.STOCK.TRANSACTION.DETAILS.OID.AMOUNT` | `FsGaStockTransactionDetails_OidAmount` | TField |  | OID Amount Multifonds DB Column is MNT_OID. |
| 28 | `FS.GA.STOCK.TRANSACTION.DETAILS.MARKET.PREMIUM.AMOUNT` | `FsGaStockTransactionDetails_MarketPremiumAmount` | TField |  | Market Premium Amount Multifonds DB Column is MNT_MKT_PREM. |
| 29 | `FS.GA.STOCK.TRANSACTION.DETAILS.MARKET.DISCOUNT.AMOUNT` | `FsGaStockTransactionDetails_MarketDiscountAmount` | TField |  | Market Discount Amount Multifonds DB Column is MNT_MKT_DISC. |
| 30 | `FS.GA.STOCK.TRANSACTION.DETAILS.ACQUISITION.PREMIUM.AMOUNT` | `FsGaStockTransactionDetails_AcquisitionPremiumAmount` | TField |  | Acquisition Premuim Amount Multifonds DB Column is MNT_ACQ_PREM. |
| 31 | `FS.GA.STOCK.TRANSACTION.DETAILS.OID.FUND.AMOUNT` | `FsGaStockTransactionDetails_OidFundAmount` | TField |  | OID Fund Amount Multifonds DB Column is MNT_OID_PTF. |
| 32 | `FS.GA.STOCK.TRANSACTION.DETAILS.MARKET.PREMIUM.FUND.AMOUNT` | `FsGaStockTransactionDetails_MarketPremiumFundAmount` | TField |  | Market Premium Fund Amount Multifonds DB Column is MNT_MKT_PREM_PTF. |
| 33 | `FS.GA.STOCK.TRANSACTION.DETAILS.MARKET.DISCOUNT.FUND.AMOUNT` | `FsGaStockTransactionDetails_MarketDiscountFundAmount` | TField |  | Market Discount Fund Amount Multifonds DB Column is MNT_MKT_DISC_PTF. |
| 34 | `FS.GA.STOCK.TRANSACTION.DETAILS.ACQUISITION.PREMIUM.FUND.AMNT` | `FsGaStockTransactionDetails_AcquisitionPremiumFundAmnt` | TField |  | Acquisition Premium Fund Amnt Multifonds DB Column is MNT_ACQ_PREM_PTF. |
| 35 | `FS.GA.STOCK.TRANSACTION.DETAILS.MANUAL.LOT.SELECTION` | `FsGaStockTransactionDetails_ManualLotSelection` | TField |  | Flag to denote that the lots relieved have been manually selected Multifonds DB Column is FLG_MANUAL_LOT. |
| 36 | `FS.GA.STOCK.TRANSACTION.DETAILS.AMORTISSEMENT.INFL.AMOUNT` | `FsGaStockTransactionDetails_AmortissementInflAmount` | TField |  | Amortissement INFL amount Multifonds DB Column is MNT_AMORTISSEMENT_INFL. |
| 37 | `FS.GA.STOCK.TRANSACTION.DETAILS.FUND.AMORTISSEMENT.INFL.AMOUNT` | `FsGaStockTransactionDetails_FundAmortissementInflAmount` | TField |  | Fund Amortissement INFL amount Multifonds DB Column is MNT_AMORTISSEMENT_INFL_PTF. |
| 38 | `FS.GA.STOCK.TRANSACTION.DETAILS.IFRS.TAG` | `FsGaStockTransactionDetails_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 39 | `FS.GA.STOCK.TRANSACTION.DETAILS.AMORTISATION.AMOUNT` | `FsGaStockTransactionDetails_AmortisationAmount` | TField |  | Amortization Amount Multifonds DB Column is MNT_AMORT. |
| 40 | `FS.GA.STOCK.TRANSACTION.DETAILS.FUND.AMORTISATION.AMOUNT` | `FsGaStockTransactionDetails_FundAmortisationAmount` | TField |  | Fund Amortization Amount Multifonds DB Column is MNT_AMORT_PTF. |
| 41 | `FS.GA.STOCK.TRANSACTION.DETAILS.TOFA` | `FsGaStockTransactionDetails_Tofa` | TField |  | It enables the button TOFA&quot; which allows the user to specify the Pre TOFA and TOFA Fair Value cut-off dates.&quot; Multifonds DB Column is FLG_TOFA. |
| 42 | `FS.GA.STOCK.TRANSACTION.DETAILS.TRANSACTION.ID` | `FsGaStockTransactionDetails_TransactionId` | TField |  | Transaction ID Multifonds DB Column is TRAN_ID. |
| 43 | `FS.GA.STOCK.TRANSACTION.DETAILS.SEC.TRANSACTION.TAX.INDICATOR` | `FsGaStockTransactionDetails_SecTransactionTaxIndicator` | TField |  | Indicator whether a transaction has been subject to security transaction tax for CGT computation. Multifonds DB Column is CGT_IND_STT_FLG. |
| 44 | `FS.GA.STOCK.TRANSACTION.DETAILS.CGT.CATEGORY` | `FsGaStockTransactionDetails_CgtCategory` | TField |  | CGT Category Multifonds DB Column is CGT_IND_CATEGORY. |
| 45 | `FS.GA.STOCK.TRANSACTION.DETAILS.FUND.TCOURS` | `FsGaStockTransactionDetails_FundTcours` | TField |  | Fund Tcours Multifonds DB Column is TCOURS_PTF. |
| 46 | `FS.GA.STOCK.TRANSACTION.DETAILS.LOT.ID` | `FsGaStockTransactionDetails_LotId` | TField |  | Lot ID Multifonds DB Column is LOTID. |
| 47 | `FS.GA.STOCK.TRANSACTION.DETAILS.MIGRATION.AMORT.DEAL.AMOUNT` | `FsGaStockTransactionDetails_MigrationAmortDealAmount` | TField |  | Migration amort deal amount Multifonds DB Column is MIG_MNT_AMORT_DEAL. |
| 48 | `FS.GA.STOCK.TRANSACTION.DETAILS.MIGRATION.AMORT.FUND.AMOUNT` | `FsGaStockTransactionDetails_MigrationAmortFundAmount` | TField |  | Migration amort fund amount Multifonds DB Column is MIG_MNT_AMORT_PTF. |
| 49 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED10` | `FsGaStockTransactionDetails_Reserved10` | TField |  |  |
| 50 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED9` | `FsGaStockTransactionDetails_Reserved9` | TField |  |  |
| 51 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED8` | `FsGaStockTransactionDetails_Reserved8` | TField |  |  |
| 52 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED7` | `FsGaStockTransactionDetails_Reserved7` | TField |  |  |
| 53 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED6` | `FsGaStockTransactionDetails_Reserved6` | TField |  |  |
| 54 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED5` | `FsGaStockTransactionDetails_Reserved5` | TField |  |  |
| 55 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED4` | `FsGaStockTransactionDetails_Reserved4` | TField |  |  |
| 56 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED3` | `FsGaStockTransactionDetails_Reserved3` | TField |  |  |
| 57 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED2` | `FsGaStockTransactionDetails_Reserved2` | TField |  |  |
| 58 | `FS.GA.STOCK.TRANSACTION.DETAILS.RESERVED1` | `FsGaStockTransactionDetails_Reserved1` | TField |  |  |
| 59 | `FS.GA.STOCK.TRANSACTION.DETAILS.LOCAL.REF` | `FsGaStockTransactionDetails_LocalRef` |  |  |  |
| 60 | `FS.GA.STOCK.TRANSACTION.DETAILS.OVERRIDE` | `FsGaStockTransactionDetails_Override` |  |  |  |
| 61 | `FS.GA.STOCK.TRANSACTION.DETAILS.RECORD.STATUS` | `FsGaStockTransactionDetails_RecordStatus` | String |  |  |
| 62 | `FS.GA.STOCK.TRANSACTION.DETAILS.CURR.NO` | `FsGaStockTransactionDetails_CurrNo` | String |  |  |
| 63 | `FS.GA.STOCK.TRANSACTION.DETAILS.INPUTTER` | `FsGaStockTransactionDetails_Inputter` |  |  |  |
| 64 | `FS.GA.STOCK.TRANSACTION.DETAILS.DATE.TIME` | `FsGaStockTransactionDetails_DateTime` |  |  |  |
| 65 | `FS.GA.STOCK.TRANSACTION.DETAILS.AUTHORISER` | `FsGaStockTransactionDetails_Authoriser` | String |  |  |
| 66 | `FS.GA.STOCK.TRANSACTION.DETAILS.CO.CODE` | `FsGaStockTransactionDetails_CoCode` | String |  |  |
| 67 | `FS.GA.STOCK.TRANSACTION.DETAILS.DEPT.CODE` | `FsGaStockTransactionDetails_DeptCode` | String |  |  |
| 68 | `FS.GA.STOCK.TRANSACTION.DETAILS.AUDITOR.CODE` | `FsGaStockTransactionDetails_AuditorCode` | String |  |  |
| 69 | `FS.GA.STOCK.TRANSACTION.DETAILS.AUDIT.DATE.TIME` | `FsGaStockTransactionDetails_AuditDateTime` | String |  |  |
