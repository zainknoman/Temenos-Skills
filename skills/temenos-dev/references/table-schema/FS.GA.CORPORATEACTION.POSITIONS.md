# FS.GA.CORPORATEACTION.POSITIONS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORPORATEACTION.POSITIONS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORPORATEACTION.POS.TRANSACTION.CODE` | `FsGaCorporateactionPositions_OperationCode` |  |  |  |
| 2 | `CORPORATEACTION.POS.SECURITY` | `FsGaCorporateactionPositions_Security` | TField |  | Security Multifonds DB Column is NOVAL. |
| 3 | `CORPORATEACTION.POS.SEQUENCE.NUMBER` | `FsGaCorporateactionPositions_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is NSEQ. |
| 4 | `CORPORATEACTION.POS.SUBSEQUENCE.NUMBER` | `FsGaCorporateactionPositions_SubsequenceNumber` | TField |  | Subsequence Number Multifonds DB Column is NSUB_SEQ. |
| 5 | `CORPORATEACTION.POS.FUND.ID` | `FsGaCorporateactionPositions_Fund` |  |  |  |
| 6 | `CORPORATEACTION.POS.CORRESPONDENT` | `FsGaCorporateactionPositions_Correspondent` | TField |  | Correspondent Multifonds DB Column is NCORRESP. |
| 7 | `CORPORATEACTION.POS.STATUS.CODE` | `FsGaCorporateactionPositions_StatusCode` | TField |  | Status Code Multifonds DB Column is CDSTATUS. |
| 8 | `CORPORATEACTION.POS.TRANSACTION.NUMBER` | `FsGaCorporateactionPositions_EntryNumber` |  |  |  |
| 9 | `CORPORATEACTION.POS.CONTRACT.NUMBER` | `FsGaCorporateactionPositions_ContractNumber` | TField |  | Contract Number Multifonds DB Column is NCONTRAT. |
| 10 | `CORPORATEACTION.POS.SERVICE.CODE` | `FsGaCorporateactionPositions_ServiceCode` | TField |  | Service Code Multifonds DB Column is CSERV. |
| 11 | `CORPORATEACTION.POS.ACCOUNT.NUMBER` | `FsGaCorporateactionPositions_AccountNumber` | TField |  | Account Number Multifonds DB Column is NRUBR. |
| 12 | `CORPORATEACTION.POS.SUB.ACCOUNT.NUMBER` | `FsGaCorporateactionPositions_SubAccountNumber` | TField |  | Sub Account Number Multifonds DB Column is NSUFF. |
| 13 | `CORPORATEACTION.POS.CURRENCY.CODE` | `FsGaCorporateactionPositions_CurrencyCode` | TField |  | Currency code Multifonds DB Column is CMON. |
| 14 | `CORPORATEACTION.POS.TRADE.DATE` | `FsGaCorporateactionPositions_TradeDate` | TField |  | Trade Date Multifonds DB Column is DOPER. |
| 15 | `CORPORATEACTION.POS.VALUE.DATE` | `FsGaCorporateactionPositions_ValueDate` | TField |  | Value Date Multifonds DB Column is DVALEUR. |
| 16 | `CORPORATEACTION.POS.EXECUTION.DATE` | `FsGaCorporateactionPositions_ExecutionDate` | TField |  | Execution date Multifonds DB Column is DEXEC. |
| 17 | `CORPORATEACTION.POS.DEPOSIT.NUMBER` | `FsGaCorporateactionPositions_DepositNumber` | TField |  | Deposit Number Multifonds DB Column is DCONTRAT. |
| 18 | `CORPORATEACTION.POS.MANAGER.CODE` | `FsGaCorporateactionPositions_Manager` |  |  |  |
| 19 | `CORPORATEACTION.POS.COUNTERPARTY` | `FsGaCorporateactionPositions_Counterparty` | TField |  | Counterparty Multifonds DB Column is NCORRESP_CTR. |
| 20 | `CORPORATEACTION.POS.NEW.SECURITY` | `FsGaCorporateactionPositions_NewSecurity` | TField |  | New Security Multifonds DB Column is NOVAL_C1. |
| 21 | `CORPORATEACTION.POS.OLD.QUANTITY` | `FsGaCorporateactionPositions_OldQuantity` | TField |  | Old quantity Multifonds DB Column is QTE_OLD. |
| 22 | `CORPORATEACTION.POS.OLD.TRANSACTION.PRICE` | `FsGaCorporateactionPositions_OldPrice` | TField |  | Old price Multifonds DB Column is PRX_OLD. |
| 23 | `CORPORATEACTION.POS.AMOUNT.COST.IN.LOCAL.LOCAL.CURRENCY` | `FsGaCorporateactionPositions_AmountBookCost` | TField |  | Amount book cost Multifonds DB Column is MNT_ACH_OLD. |
| 24 | `CORPORATEACTION.POS.RIGHT.QUANTITY` | `FsGaCorporateactionPositions_RightQuantity` | TField |  | Right quantity Multifonds DB Column is QTE_RIGHT. |
| 25 | `CORPORATEACTION.POS.BROKEN.QUANTITY` | `FsGaCorporateactionPositions_BrokenQuantity` | TField |  | Broken quantity Multifonds DB Column is QTE_RPU. |
| 26 | `CORPORATEACTION.POS.CLOSED.QUANTITY` | `FsGaCorporateactionPositions_ClosedQuantity` | TField |  | Closed quantity Multifonds DB Column is QTE_CLOSED. |
| 27 | `CORPORATEACTION.POS.RIGHT.AMOUNT` | `FsGaCorporateactionPositions_RightAmount` | TField |  | Right amount Multifonds DB Column is MNT_RIGHT. |
| 28 | `CORPORATEACTION.POS.CORRECTION.AMOUNT` | `FsGaCorporateactionPositions_CorrectionAmount` | TField |  | Correction amount Multifonds DB Column is MNT_AJUST. |
| 29 | `CORPORATEACTION.POS.CORRECTION.AMOUNT.IN.FUND.CCY` | `FsGaCorporateactionPositions_CorrectionAmountInFundCcy` | TField |  | Correction amount in fund Ccy Multifonds DB Column is MNT_AJUST_PTF. |
| 30 | `CORPORATEACTION.POS.RIGHT.AMOUNT.OF.CORPORATE.ACT` | `FsGaCorporateactionPositions_RightAmountOfCorporateAct` | TField |  | Right amount of corporate act Multifonds DB Column is MRX_RIGHT. |
| 31 | `CORPORATEACTION.POS.RIGHT.AMT.OF.CA.IN.FUND.CCY` | `FsGaCorporateactionPositions_RightAmtOfCaInFundCcy` | TField |  | Right amt of CA in fund Ccy Multifonds DB Column is MRX_RIGHT_PTF. |
| 32 | `CORPORATEACTION.POS.CASH.CODE` | `FsGaCorporateactionPositions_CashCode` | TField |  | Cash Code Multifonds DB Column is COD_CASH. |
| 33 | `CORPORATEACTION.POS.CASH.CURRENCY.CODE` | `FsGaCorporateactionPositions_CashCurrencyCode` | TField |  | Cash currency code Multifonds DB Column is CMON_CASH. |
| 34 | `CORPORATEACTION.POS.QUANTITY.AT.EXECUTION.DATE` | `FsGaCorporateactionPositions_QuantityAtExecutionDate` | TField |  | Quantity at execution date Multifonds DB Column is QTE_BASE. |
| 35 | `CORPORATEACTION.POS.UNIT.AMOUNT.TO.PAY` | `FsGaCorporateactionPositions_UnitAmountToPay` | TField |  | Unit amount to pay Multifonds DB Column is MNT_PD. |
| 36 | `CORPORATEACTION.POS.AMOUNT.TO.PAY` | `FsGaCorporateactionPositions_AmountToPay` | TField |  | Amount to pay Multifonds DB Column is MNT_PAYED. |
| 37 | `CORPORATEACTION.POS.ADJUSTED.AMOUNT.UNIT` | `FsGaCorporateactionPositions_AdjustedUnitAmount` | TField |  | Adjusted Unit Amount Multifonds DB Column is MNT_UNIT_AJUST. |
| 38 | `CORPORATEACTION.POS.CORRECTION.UNIT.AMNT.FUND.CCY` | `FsGaCorporateactionPositions_CorrectionUnitAmntFundCcy` | TField |  | Correction unit amnt fund Ccy Multifonds DB Column is MNT_UNIT_AJUST_PTF. |
| 39 | `CORPORATEACTION.POS.CORRECTION.RATIO` | `FsGaCorporateactionPositions_CorrectionRatio` | TField |  | Correction ratio Multifonds DB Column is PCT_RATIO. |
| 40 | `CORPORATEACTION.POS.CORRECTION.PERCENTAGE` | `FsGaCorporateactionPositions_CorrectionPercentage` | TField |  | Correction percentage Multifonds DB Column is PCT_AJUST. |
| 41 | `CORPORATEACTION.POS.TAXABLE.AMOUNT` | `FsGaCorporateactionPositions_TaxableAmount` | TField |  | Taxable amount Multifonds DB Column is MNT_TAX. |
| 42 | `CORPORATEACTION.POS.FEES.AMOUNT` | `FsGaCorporateactionPositions_FeesAmount` | TField |  | Fees amount Multifonds DB Column is MNT_TAX_TIT. |
| 43 | `CORPORATEACTION.POS.TAX.AMOUNT.IN.FUND.LOCAL.CURRENCY` | `FsGaCorporateactionPositions_TaxAmountInFundCurrency` | TField |  | Tax amount in fund currency Multifonds DB Column is MNT_TAX_PTF. |
| 44 | `CORPORATEACTION.POS.NET.AMOUNT.IN.LOCAL.LOCAL.CURRENCY` | `FsGaCorporateactionPositions_NetAmount` |  |  |  |
| 45 | `CORPORATEACTION.POS.SETTLEMENT.AMOUNT.OF.CA` | `FsGaCorporateactionPositions_SettlementAmountOfCa` | TField |  | Settlement amount of CA Multifonds DB Column is MNT_NET_CORR. |
| 46 | `CORPORATEACTION.POS.NET.AMOUNT.IN.FUND.LOCAL.CURRENCY` | `FsGaCorporateactionPositions_NetAmountInFundCurrency` | TField |  | Net amount in fund currency Multifonds DB Column is MNT_NET_PTF. |
| 47 | `CORPORATEACTION.POS.AMOUNT.BOOK.COST.IN.FUND.CCY` | `FsGaCorporateactionPositions_AmountBookCostInFundCcy` | TField |  | Amount book cost in fund Ccy Multifonds DB Column is MNT_ACH_OLD_PTF. |
| 48 | `CORPORATEACTION.POS.ARCHIVE` | `FsGaCorporateactionPositions_Archive` | TField |  | ARCHIVE Multifonds DB Column is ARCHIVE. |
| 49 | `CORPORATEACTION.POS.RATE.OF.EXCHANGE` | `FsGaCorporateactionPositions_ExchangeRate` |  |  |  |
| 50 | `CORPORATEACTION.POS.STATUS.PENDING` | `FsGaCorporateactionPositions_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 51 | `CORPORATEACTION.POS.MARKET.TRANSACTION.PRICE` | `FsGaCorporateactionPositions_MarketPrice` | TField |  | Market Price Multifonds DB Column is COURSVAL. |
| 52 | `CORPORATEACTION.POS.PRICE.IN.FUND.LOCAL.CURRENCY` | `FsGaCorporateactionPositions_PriceInFundCurrency` | TField |  | Price in fund currency Multifonds DB Column is COURSVAL_PTF. |
| 53 | `CORPORATEACTION.POS.CODE.TO.TELL.TYPE.OF.BV.ADJ` | `FsGaCorporateactionPositions_CodeToTellTypeOfBvAdj` | TField |  | Code to tell type of BV adj Multifonds DB Column is COD_AJUST_CPTA. |
| 54 | `CORPORATEACTION.POS.CORRECTION.AMOUNT2` | `FsGaCorporateactionPositions_CorrectionAmount2` | TField |  | Correction amount2 Multifonds DB Column is MNT_AJUST_2. |
| 55 | `CORPORATEACTION.POS.ACCOUNT.INSTRUCTION` | `FsGaCorporateactionPositions_AccountInstruction` | TField |  | Account instruction Multifonds DB Column is FLG_ACCOUNT. |
| 56 | `CORPORATEACTION.POS.CONTRACT` | `FsGaCorporateactionPositions_Contract` | TField |  | Contract Multifonds DB Column is NCONTRAT_NEW. |
| 57 | `CORPORATEACTION.POS.ADJUSTMENT.AMOUNT` | `FsGaCorporateactionPositions_AdjustmentAmount` | TField |  | Adjustment amount Multifonds DB Column is BOOK_MNT. |
| 58 | `CORPORATEACTION.POS.ADJUSTMENT.AMOUNT.IN.FUND.CCY` | `FsGaCorporateactionPositions_AdjustmentAmountInFundCcy` | TField |  | Adjustment amount in fund Ccy Multifonds DB Column is BOOK_MNT_PTF. |
| 59 | `CORPORATEACTION.POS.SHOW.ON.SCREEN` | `FsGaCorporateactionPositions_ShowOnScreen` | TField |  | Show on screen Multifonds DB Column is FLG_SHOW. |
| 60 | `CORPORATEACTION.POS.ENTRY.NUMBER.SALE` | `FsGaCorporateactionPositions_EntryNumberSale` | TField |  | Entry number sale Multifonds DB Column is NECRITUR_SALE. |
| 61 | `CORPORATEACTION.POS.MNT.VENTE.OLD` | `FsGaCorporateactionPositions_MntVenteOld` | TField |  | MNT VENTE OLD Multifonds DB Column is MNT_VENTE_OLD. |
| 62 | `CORPORATEACTION.POS.MNT.VENTE.OLD.PTF` | `FsGaCorporateactionPositions_MntVenteOldPtf` | TField |  | MNT VENTE OLD PTF Multifonds DB Column is MNT_VENTE_OLD_PTF. |
| 63 | `CORPORATEACTION.POS.MARKET.TRANSACTION.CODE` | `FsGaCorporateactionPositions_MarketOperationCode` | TField |  | Market operation code Multifonds DB Column is COPER_MARKET. |
| 64 | `CORPORATEACTION.POS.FUTURE.NUMBER` | `FsGaCorporateactionPositions_FutureNumber` | TField |  | Future number Multifonds DB Column is NFUT. |
| 65 | `CORPORATEACTION.POS.ENTRY.NUMBER1` | `FsGaCorporateactionPositions_EntryNumber1` | TField |  | Entry Number1 Multifonds DB Column is NECRITUR_1. |
| 66 | `CORPORATEACTION.POS.ENTRY.NUMBER2` | `FsGaCorporateactionPositions_EntryNumber2` | TField |  | Entry Number2 Multifonds DB Column is NECRITUR_2. |
| 67 | `CORPORATEACTION.POS.TYP.TRAIT.NEW` | `FsGaCorporateactionPositions_TypTraitNew` | TField |  | TYP TRAIT NEW Multifonds DB Column is TYP_TRAIT_NEW. |
| 68 | `CORPORATEACTION.POS.MRX.RIGHT.CASH` | `FsGaCorporateactionPositions_MrxRightCash` | TField |  | MRX RIGHT CASH Multifonds DB Column is MRX_RIGHT_CASH. |
| 69 | `CORPORATEACTION.POS.MBS.FACTOR.OLD` | `FsGaCorporateactionPositions_MbsFactorOld` | TField |  | MBS factor old Multifonds DB Column is FACTOR_OLD. |
| 70 | `CORPORATEACTION.POS.MBS.FACTOR.NEW` | `FsGaCorporateactionPositions_MbsFactorNew` | TField |  | MBS factor new Multifonds DB Column is FACTOR_NEW. |
| 71 | `CORPORATEACTION.POS.CGTI.IFRS.NEW` | `FsGaCorporateactionPositions_CgtiIfrsNew` | TField |  | CGTI IFRS NEW Multifonds DB Column is CGTI_IFRS_NEW. |
| 72 | `CORPORATEACTION.POS.IFRS.CLASS` | `FsGaCorporateactionPositions_IfrsClass` | TField |  | IFRS class Multifonds DB Column is CGTI_IFRS. |
| 73 | `CORPORATEACTION.POS.FLG.TAX.VA` | `FsGaCorporateactionPositions_FlgTaxVa` | TField |  | FLG TAX VA Multifonds DB Column is FLG_TAX_VA. |
| 74 | `CORPORATEACTION.POS.FLG.AUTO.PROCESS` | `FsGaCorporateactionPositions_FlgAutoProcess` | TField |  | FLG AUTO PROCESS Multifonds DB Column is FLG_AUTO_PROCESS. |
| 75 | `CORPORATEACTION.POS.NCONTRAT.LEN` | `FsGaCorporateactionPositions_NcontratLen` | TField |  | NCONTRAT LEN Multifonds DB Column is NCONTRAT_LEN. |
| 76 | `CORPORATEACTION.POS.NCONTRAT.LEN.NEW` | `FsGaCorporateactionPositions_NcontratLenNew` | TField |  | NCONTRAT LEN NEW Multifonds DB Column is NCONTRAT_LEN_NEW. |
| 77 | `CORPORATEACTION.POS.MNT.AJUST.LDBW` | `FsGaCorporateactionPositions_MntAjustLdbw` | TField |  | MNT AJUST LDBW Multifonds DB Column is MNT_AJUST_LDBW. |
| 78 | `CORPORATEACTION.POS.MNT.AJUST.LDBW.2` | `FsGaCorporateactionPositions_MntAjustLdbw2` | TField |  | MNT AJUST LDBW 2 Multifonds DB Column is MNT_AJUST_LDBW_2. |
| 79 | `CORPORATEACTION.POS.QTE.FRAC` | `FsGaCorporateactionPositions_QteFrac` | TField |  | QTE FRAC Multifonds DB Column is QTE_FRAC. |
| 80 | `CORPORATEACTION.POS.ACCOUNTING.DATE` | `FsGaCorporateactionPositions_AccountingDate` | TField |  | Accounting date Multifonds DB Column is DJOURNAL. |
| 81 | `CORPORATEACTION.POS.NECRITUR.DIV` | `FsGaCorporateactionPositions_NecriturDiv` | TField |  | NECRITUR DIV Multifonds DB Column is NECRITUR_DIV. |
| 82 | `CORPORATEACTION.POS.ELECTION.STATUS` | `FsGaCorporateactionPositions_ElectionStatus` | TField |  | ELECTION STATUS Multifonds DB Column is ELECTION_STATUS. |
| 83 | `CORPORATEACTION.POS.INSTRUCTION.STATUS` | `FsGaCorporateactionPositions_InstructionStatus` | TField |  | INSTRUCTION STATUS Multifonds DB Column is INSTRUCTION_STATUS. |
| 84 | `CORPORATEACTION.POS.SEC.RATIO` | `FsGaCorporateactionPositions_SecRatio` | TField |  | SEC RATIO Multifonds DB Column is SEC_RATIO. |
| 85 | `CORPORATEACTION.POS.FLG.ACCEPT` | `FsGaCorporateactionPositions_FlgAccept` | TField |  | FLG ACCEPT Multifonds DB Column is FLG_ACCEPT. |
| 86 | `CORPORATEACTION.POS.FLG.REJECT` | `FsGaCorporateactionPositions_FlgReject` | TField |  | FLG REJECT Multifonds DB Column is FLG_REJECT. |
| 87 | `CORPORATEACTION.POS.FLG.PA.MODULE` | `FsGaCorporateactionPositions_FlgPaModule` | TField |  | FLG PA MODULE Multifonds DB Column is FLG_PA_MODULE. |
| 88 | `CORPORATEACTION.POS.CA.OPTION` | `FsGaCorporateactionPositions_CaOption` | TField |  | CA OPTION Multifonds DB Column is CA_OPTION. |
| 89 | `CORPORATEACTION.POS.CSERV.DIV` | `FsGaCorporateactionPositions_CservDiv` | TField |  | CSERV DIV Multifonds DB Column is CSERV_DIV. |
| 90 | `CORPORATEACTION.POS.PA.CDSTATUS` | `FsGaCorporateactionPositions_PaCdstatus` | TField |  | PA CDSTATUS Multifonds DB Column is PA_CDSTATUS. |
| 91 | `CORPORATEACTION.POS.ADJUSTED.AMOUNT` | `FsGaCorporateactionPositions_AdjustedAmount` | TField |  | Adjusted Amount Multifonds DB Column is MNT_NET_AJUST. |
| 92 | `CORPORATEACTION.POS.DOPER.BO` | `FsGaCorporateactionPositions_DoperBo` | TField |  | DOPER BO Multifonds DB Column is DOPER_BO. |
| 93 | `CORPORATEACTION.POS.DVALEUR.BO` | `FsGaCorporateactionPositions_DvaleurBo` | TField |  | DVALEUR BO Multifonds DB Column is DVALEUR_BO. |
| 94 | `CORPORATEACTION.POS.MRX.RIGHT.DEF` | `FsGaCorporateactionPositions_MrxRightDef` | TField |  | MRX RIGHT DEF Multifonds DB Column is MRX_RIGHT_DEF. |
| 95 | `CORPORATEACTION.POS.MRX.RIGHT.DEF.PTF` | `FsGaCorporateactionPositions_MrxRightDefPtf` | TField |  | MRX RIGHT DEF PTF Multifonds DB Column is MRX_RIGHT_DEF_PTF. |
| 96 | `CORPORATEACTION.POS.MNT.AJUST.2.PTF` | `FsGaCorporateactionPositions_MntAjust2Ptf` | TField |  | MNT AJUST 2 PTF Multifonds DB Column is MNT_AJUST_2_PTF. |
| 97 | `CORPORATEACTION.POS.TCHG.BO` | `FsGaCorporateactionPositions_TchgBo` | TField |  | TCHG BO Multifonds DB Column is TCHG_BO. |
| 98 | `CORPORATEACTION.POS.SEC.SETTL.FX.VCI` | `FsGaCorporateactionPositions_SecSettlFxVci` | TField |  | SEC SETTL FX VCI Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 99 | `CORPORATEACTION.POS.SEC.PTF.FX.VCI` | `FsGaCorporateactionPositions_SecPtfFxVci` | TField |  | SEC PTF FX VCI Multifonds DB Column is SEC_PTF_FX_VCI. |
| 100 | `CORPORATEACTION.POS.SETTL.PTF.FX.VCI` | `FsGaCorporateactionPositions_SettlPtfFxVci` | TField |  | SETTL PTF FX VCI Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 101 | `CORPORATEACTION.POS.NEW.DERIVATIVE.SEC.ID` | `FsGaCorporateactionPositions_NewDerivativeSecId` | TField |  | New Derivative Sec Id Multifonds DB Column is DERIVATIVE_ID_C1. |
| 102 | `CORPORATEACTION.POS.GTI.CHOIX` | `FsGaCorporateactionPositions_GtiChoix` | TField |  | GTI CHOIX Multifonds DB Column is GTI_CHOIX. |
| 103 | `CORPORATEACTION.POS.LOC.PTF.AVG.VCI` | `FsGaCorporateactionPositions_LocPtfAvgVci` | TField |  | LOC PTF AVG VCI Multifonds DB Column is LOC_PTF_AVG_VCI. |
| 104 | `CORPORATEACTION.POS.CLIENT.RESPONSE.RECEIPT.DATE` | `FsGaCorporateactionPositions_ClientResponseReceiptDate` | TField |  | Client response receipt date Multifonds DB Column is DCLIENT_RES_RECEIPT. |
| 105 | `CORPORATEACTION.POS.CUSTODIAN.STATUS.ADVICE.DATE` | `FsGaCorporateactionPositions_CustodianStatusAdviceDate` | TField |  | Custodian status advice date Multifonds DB Column is DCUST_STAT_RECEIPT. |
| 106 | `CORPORATEACTION.POS.MNT.AJUST.NCY` | `FsGaCorporateactionPositions_MntAjustNcy` | TField |  | MNT AJUST NCY Multifonds DB Column is MNT_AJUST_NCY. |
| 107 | `CORPORATEACTION.POS.LINK.FUND.ID` | `FsGaCorporateactionPositions_LinkFund` | TField |  | Link fund Multifonds DB Column is NPTF_LINK. |
| 108 | `CORPORATEACTION.POS.NPTF.DEFAULT` | `FsGaCorporateactionPositions_NptfDefault` | TField |  | NPTF DEFAULT Multifonds DB Column is NPTF_DEFAULT. |
| 109 | `CORPORATEACTION.POS.PERCENTAGE` | `FsGaCorporateactionPositions_Percentage` | TField |  | Percentage Multifonds DB Column is PERCENTAGE. |
| 110 | `CORPORATEACTION.POS.CGT.IND.CATEGORY` | `FsGaCorporateactionPositions_CgtIndCategory` | TField |  | CGT IND CATEGORY Multifonds DB Column is CGT_IND_CATEGORY. |
| 111 | `CORPORATEACTION.POS.LOT.ID` | `FsGaCorporateactionPositions_LotId` | TField |  | Lot ID Multifonds DB Column is LOTID. |
| 112 | `CORPORATEACTION.POS.TRADE.ID` | `FsGaCorporateactionPositions_TradeId` | TField |  | Trade ID Multifonds DB Column is TRADEID. |
| 113 | `CORPORATEACTION.POS.NEW.LOT.ID` | `FsGaCorporateactionPositions_NewLotId` | TField |  | NEW LOT ID Multifonds DB Column is NEWLOTID. |
| 114 | `CORPORATEACTION.POS.KNOWLEDGE.DATE` | `FsGaCorporateactionPositions_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 115 | `CORPORATEACTION.POS.RECORD.STATUS` | `FsGaCorporateactionPositions_RecordStatus` | String |  |  |
| 116 | `CORPORATEACTION.POS.CURR.NO` | `FsGaCorporateactionPositions_CurrNo` | String |  |  |
| 117 | `CORPORATEACTION.POS.INPUTTER` | `FsGaCorporateactionPositions_Inputter` |  |  |  |
| 118 | `CORPORATEACTION.POS.DATE.TIME` | `FsGaCorporateactionPositions_DateTime` |  |  |  |
| 119 | `CORPORATEACTION.POS.AUTHORISER` | `FsGaCorporateactionPositions_Authoriser` | String |  |  |
| 120 | `CORPORATEACTION.POS.CO.CODE` | `FsGaCorporateactionPositions_CoCode` | String |  |  |
| 121 | `CORPORATEACTION.POS.DEPT.CODE` | `FsGaCorporateactionPositions_DeptCode` | String |  |  |
| 122 | `CORPORATEACTION.POS.AUDITOR.CODE` | `FsGaCorporateactionPositions_AuditorCode` | String |  |  |
| 123 | `CORPORATEACTION.POS.AUDIT.DATE.TIME` | `FsGaCorporateactionPositions_AuditDateTime` | String |  |  |
