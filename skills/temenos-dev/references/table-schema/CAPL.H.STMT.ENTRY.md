# CAPL.H.STMT.ENTRY — Table Schema

> Source: `INSERTS/I_F.CAPL.H.STMT.ENTRY` in `CABASE_LegacyFinancial.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.SE.ACCOUNT.NUMBER` | `CaplHStmtEntry_AccountNumber` | TField |  | This field is used to define the T24 account number for legacy transaction migration.Allowed value is valid account number from ACCOUNT table. |
| 2 | `CAPL.SE.COMPANY.CODE` | `CaplHStmtEntry_CompanyCode` | TField |  | This field is to define the company code to which the account belongs.Valid COMPANY record. |
| 3 | `CAPL.SE.AMOUNT.LCY` | `CaplHStmtEntry_AmountLcy` | TField |  | This field is to define the transaction amount.Valid amount to be defined. |
| 4 | `CAPL.SE.TRANSACTION.CODE` | `CaplHStmtEntry_TransactionCode` | TField |  | This field hold the transaction code.Valide record from TRANSACTION table. |
| 5 | `CAPL.SE.THEIR.REFERENCE` | `CaplHStmtEntry_TheirReference` | TField |  | This field hold the transaction reference of the non T24 account. |
| 6 | `CAPL.SE.NARRATIVE` | `CaplHStmtEntry_Narrative` |  |  |  |
| 7 | `CAPL.SE.PL.CATEGORY` | `CaplHStmtEntry_PlCategory` | TField |  | Field is to define the PL category to update the commission and charges for the transaction.Valid CATEGORY record. |
| 8 | `CAPL.SE.CUSTOMER.ID` | `CaplHStmtEntry_CustomerId` | TField |  | This field is used to capture the customer id of the |
| 9 | `CAPL.SE.ACCOUNT.OFFICER` | `CaplHStmtEntry_AccountOfficer` | TField |  | Account Officer code from Account record for Account in Field 1 or, if the Account record has no Account Officer code, the Account Officer code from the Customer record.Valid record from department account officer table. |
| 10 | `CAPL.SE.PRODUCT.CATEGORY` | `CaplHStmtEntry_ProductCategory` | TField |  | This field holds the Category Code from Account record.Valid CATEGORY code. |
| 11 | `CAPL.SE.VALUE.DATE` | `CaplHStmtEntry_ValueDate` | TField |  | The date on which the entry is to be given value for interest purposes. |
| 12 | `CAPL.SE.CURRENCY` | `CaplHStmtEntry_Currency` | TField |  | This field is used to capture the Currency of there account.Valid CURRENCY code to be defined. |
| 13 | `CAPL.SE.AMOUNT.FCY` | `CaplHStmtEntry_AmountFcy` | TField |  | For Entries over foreign Currency Accounts, this field contains the Amount of the Entry in the Currency of the Account.Valid amount is captured here. |
| 14 | `CAPL.SE.EXCHANGE.RATE` | `CaplHStmtEntry_ExchangeRate` | TField |  | For Entries over foreign Currency Accounts, this field contains the Rate which was used to convert the Currency Amount to the local currency. |
| 15 | `CAPL.SE.NEGOTIATED.REF.NUM` | `CaplHStmtEntry_NegotiatedRefNum` | TField |  |  |
| 16 | `CAPL.SE.POSITION.TYPE` | `CaplHStmtEntry_PositionType` | TField |  | Future use |
| 17 | `CAPL.SE.OUR.REFERENCE` | `CaplHStmtEntry_OurReference` | TField |  | This field contains the Reference given to the transaction/deal by the Bank.Free text field with max length of 60 character. |
| 18 | `CAPL.SE.REVERSAL.MARKER` | `CaplHStmtEntry_ReversalMarker` | TField |  | This field Indicates that the Entry is the reversal of a previous Entry with the same Transaction code. Amounts and volumes of Entries accumulated for charging and MIS purposes will be reduced.Field with length 1 character. |
| 19 | `CAPL.SE.EXPOSURE.DATE` | `CaplHStmtEntry_ExposureDate` | TField |  | The date on which the available balance will be credited with the Entry, i.e. the date on which the Entry can be drawn against and is given value for credit limit position processing.Valid date is stored here. |
| 20 | `CAPL.SE.CURRENCY.MARKET` | `CaplHStmtEntry_CurrencyMarket` | TField |  | This field Indicates which type of currency funds are being used for those currencies where there is more than one type. Different exchange rates may be quoted for the different markets.Valid record from CURRENT.MARKET |
| 21 | `CAPL.SE.LOCAL.REF` | `CaplHStmtEntry_LocalRef` |  |  |  |
| 22 | `CAPL.SE.DEPARTMENT.CODE` | `CaplHStmtEntry_DepartmentCode` | TField |  | This field is used to Identifies the Department where the original transaction was input.1-4 numeric characters Department Account Officer code |
| 23 | `CAPL.SE.TRANS.REFERENCE` | `CaplHStmtEntry_TransReference` | TField |  | This field contains the reference number by which the originating transaction may be accessed in the front end Application system which generated the Entry .Free text field with max length of 60 character. |
| 24 | `CAPL.SE.SYSTEM.ID` | `CaplHStmtEntry_SystemId` | TField |  | This field is used to Identifies the system by which the Entry was generated and the file from which further details may be obtained. |
| 25 | `CAPL.SE.BOOKING.DATE` | `CaplHStmtEntry_BookingDate` | TField |  | This field is used to define the booking date of the transaction.Valid date to be defined. |
| 26 | `CAPL.SE.STMT.NO` | `CaplHStmtEntry_StmtNo` |  |  |  |
| 27 | `CAPL.SE.OVERRIDE` | `CaplHStmtEntry_Override` |  |  |  |
| 28 | `CAPL.SE.SUSPENSE.CATEGORY` | `CaplHStmtEntry_SuspenseCategory` | TField |  |  |
| 29 | `CAPL.SE.SUSPENSE.VALUE.DATE` | `CaplHStmtEntry_SuspenseValueDate` | TField |  |  |
| 30 | `CAPL.SE.SUPPRESS.POSITION` | `CaplHStmtEntry_SuppressPosition` | TField |  |  |
| 31 | `CAPL.SE.CRF.TYPE` | `CaplHStmtEntry_CrfType` | TField |  |  |
| 32 | `CAPL.SE.CRF.TXN.CODE` | `CaplHStmtEntry_CrfTxnCode` | TField |  |  |
| 33 | `CAPL.SE.CRF.CURRENCY` | `CaplHStmtEntry_CrfCurrency` | TField |  |  |
| 34 | `CAPL.SE.CONSOL.KEY` | `CaplHStmtEntry_ConsolKey` | TField |  |  |
| 35 | `CAPL.SE.CRF.MAT.DATE` | `CaplHStmtEntry_CrfMatDate` | TField |  |  |
| 36 | `CAPL.SE.CRF.PROD.CAT` | `CaplHStmtEntry_CrfProdCat` | TField |  |  |
| 37 | `CAPL.SE.PM.TYPE` | `CaplHStmtEntry_PmType` | TField |  |  |
| 38 | `CAPL.SE.DEALER.DESK` | `CaplHStmtEntry_DealerDesk` | TField |  |  |
| 39 | `CAPL.SE.COUNTER.PARTY` | `CaplHStmtEntry_CounterParty` | TField |  |  |
| 40 | `CAPL.SE.LIQUIDATION.MODE` | `CaplHStmtEntry_LiquidationMode` | TField |  |  |
| 41 | `CAPL.SE.REPAYMENT.DATE` | `CaplHStmtEntry_RepaymentDate` | TField |  |  |
| 42 | `CAPL.SE.REPAYMENT.TYPE` | `CaplHStmtEntry_RepaymentType` |  |  |  |
| 43 | `CAPL.SE.REPAMENT.AMOUNT` | `CaplHStmtEntry_RepamentAmount` |  |  |  |
| 44 | `CAPL.SE.OUTSTANDING.BAL` | `CaplHStmtEntry_OutstandingBal` | TField |  |  |
| 45 | `CAPL.SE.CONTRACT.INT.RATE` | `CaplHStmtEntry_ContractIntRate` | TField |  |  |
| 46 | `CAPL.SE.CONTRACT.INT.KEY` | `CaplHStmtEntry_ContractIntKey` | TField |  |  |
| 47 | `CAPL.SE.CYCLE.FORWARD` | `CaplHStmtEntry_CycleForward` | TField |  |  |
| 48 | `CAPL.SE.ORIG.LOCAL.EQUIV` | `CaplHStmtEntry_OrigLocalEquiv` | TField |  |  |
| 49 | `CAPL.SE.ORIGINAL.AMOUNT` | `CaplHStmtEntry_OriginalAmount` | TField |  |  |
| 50 | `CAPL.SE.ORIGINAL.CCY` | `CaplHStmtEntry_OriginalCcy` | TField |  |  |
| 51 | `CAPL.SE.ORIGINAL.ACCT` | `CaplHStmtEntry_OriginalAcct` | TField |  |  |
| 52 | `CAPL.SE.ORIGINAL.EXCH.RATE` | `CaplHStmtEntry_OriginalExchRate` | TField |  |  |
| 53 | `CAPL.SE.EXP.SPLIT.DATE` | `CaplHStmtEntry_ExpSplitDate` |  |  |  |
| 54 | `CAPL.SE.EXP.SPLIT.AMT` | `CaplHStmtEntry_ExpSplitAmt` |  |  |  |
| 55 | `CAPL.SE.ORIG.AMOUNT.LCY` | `CaplHStmtEntry_OrigAmountLcy` | TField |  |  |
| 56 | `CAPL.SE.BANK.SORT.CODE` | `CaplHStmtEntry_BankSortCode` |  |  |  |
| 57 | `CAPL.SE.CHEQUE.NUMBER` | `CaplHStmtEntry_ChequeNumber` |  |  |  |
| 58 | `CAPL.SE.CHQ.COLL.ID` | `CaplHStmtEntry_ChqCollId` | TField |  |  |
| 59 | `CAPL.SE.DRAWN.ACCOUNT` | `CaplHStmtEntry_DrawnAccount` | TField |  |  |
| 60 | `CAPL.SE.ACCOUNTING.DATE` | `CaplHStmtEntry_AccountingDate` | TField |  |  |
| 61 | `CAPL.SE.PC.PERIOD.END` | `CaplHStmtEntry_PcPeriodEnd` |  |  |  |
| 62 | `CAPL.SE.PC.APPLIED` | `CaplHStmtEntry_PcApplied` |  |  |  |
| 63 | `CAPL.SE.GROSS.INT.TAX.LCY` | `CaplHStmtEntry_GrossIntTaxLcy` | TField |  |  |
| 64 | `CAPL.SE.TAX.ALLOW.ADJ.LCY` | `CaplHStmtEntry_TaxAllowAdjLcy` | TField |  |  |
| 65 | `CAPL.SE.TAX.EXEMPT.ADJ.LCY` | `CaplHStmtEntry_TaxExemptAdjLcy` | TField |  |  |
| 66 | `CAPL.SE.POOL2.ADJ.LCY` | `CaplHStmtEntry_Pool2AdjLcy` | TField |  |  |
| 67 | `CAPL.SE.GROSS.INT.TAX.FCY` | `CaplHStmtEntry_GrossIntTaxFcy` | TField |  |  |
| 68 | `CAPL.SE.TAX.ALLOW.ADJ.FCY` | `CaplHStmtEntry_TaxAllowAdjFcy` | TField |  |  |
| 69 | `CAPL.SE.TAX.EXEMPT.ADJ.FCY` | `CaplHStmtEntry_TaxExemptAdjFcy` | TField |  |  |
| 70 | `CAPL.SE.POOL2.ADJ.FCY` | `CaplHStmtEntry_Pool2AdjFcy` | TField |  |  |
| 71 | `CAPL.SE.UPDATE.POOL.SEQ` | `CaplHStmtEntry_UpdatePoolSeq` | TField |  |  |
| 72 | `CAPL.SE.NET.INT.TAX.LCY` | `CaplHStmtEntry_NetIntTaxLcy` | TField |  |  |
| 73 | `CAPL.SE.NET.INT.TAX.FCY` | `CaplHStmtEntry_NetIntTaxFcy` | TField |  |  |
| 74 | `CAPL.SE.TAX.ALLOWANCE.CCY` | `CaplHStmtEntry_TaxAllowanceCcy` | TField |  |  |
| 75 | `CAPL.SE.POOL1.MOVEMENT` | `CaplHStmtEntry_Pool1Movement` | TField |  |  |
| 76 | `CAPL.SE.POOL2.MOVEMENT` | `CaplHStmtEntry_Pool2Movement` | TField |  |  |
| 77 | `CAPL.SE.AMOUNT.DEAL.CCY` | `CaplHStmtEntry_AmountDealCcy` | TField |  |  |
| 78 | `CAPL.SE.DEAL.CCY` | `CaplHStmtEntry_DealCcy` | TField |  |  |
| 79 | `CAPL.SE.DEAL.EXCH.RATE` | `CaplHStmtEntry_DealExchRate` | TField |  |  |
| 80 | `CAPL.SE.MASK.PRINT` | `CaplHStmtEntry_MaskPrint` | TField |  |  |
| 81 | `CAPL.SE.MASK.NARRATIVE` | `CaplHStmtEntry_MaskNarrative` | TField |  |  |
| 82 | `CAPL.SE.STMT1.DATE` | `CaplHStmtEntry_Stmt1Date` | TField |  |  |
| 83 | `CAPL.SE.STMT2.DATE` | `CaplHStmtEntry_Stmt2Date` |  |  |  |
| 84 | `CAPL.SE.CHQ.TYPE` | `CaplHStmtEntry_ChqType` | TField |  |  |
| 85 | `CAPL.SE.TAX.EXCH.RATE` | `CaplHStmtEntry_TaxExchRate` | TField |  |  |
| 86 | `CAPL.SE.NET.PARAM` | `CaplHStmtEntry_NetParam` | TField |  |  |
| 87 | `CAPL.SE.MASTER.ACCOUNT` | `CaplHStmtEntry_MasterAccount` | TField |  |  |
| 88 | `CAPL.SE.ADDL.TRANS.REF` | `CaplHStmtEntry_AddlTransRef` |  |  |  |
| 89 | `CAPL.SE.INTEREST.RATE` | `CaplHStmtEntry_InterestRate` | TField |  |  |
| 90 | `CAPL.SE.DD.MANDATE.REF` | `CaplHStmtEntry_DdMandateRef` | TField |  |  |
| 91 | `CAPL.SE.DD.ITEM.REF` | `CaplHStmtEntry_DdItemRef` | TField |  |  |
| 92 | `CAPL.SE.DD.MANDATE.DATE` | `CaplHStmtEntry_DdMandateDate` | TField |  |  |
| 93 | `CAPL.SE.CONTRACT.BAL.ID` | `CaplHStmtEntry_ContractBalId` | TField |  |  |
| 94 | `CAPL.SE.TRADE.DATE` | `CaplHStmtEntry_TradeDate` | TField |  |  |
| 95 | `CAPL.SE.PROCESSING.DATE` | `CaplHStmtEntry_ProcessingDate` | TField |  |  |
| 96 | `CAPL.SE.BALANCE.TYPE` | `CaplHStmtEntry_BalanceType` | TField |  |  |
| 97 | `CAPL.SE.AA.ITEM.REF` | `CaplHStmtEntry_AaItemRef` | TField |  |  |
| 98 | `CAPL.SE.ACCRUAL.DATA` | `CaplHStmtEntry_AccrualData` |  |  |  |
| 99 | `CAPL.SE.ORIG.CCY.MARKET` | `CaplHStmtEntry_OrigCcyMarket` | TField |  |  |
| 100 | `CAPL.SE.END.BAL` | `CaplHStmtEntry_EndBal` | TField |  |  |
| 101 | `CAPL.SE.EXT.TXN.CODE` | `CaplHStmtEntry_ExtTxnCode` | TField |  |  |
| 102 | `CAPL.SE.ATM.LOCATION` | `CaplHStmtEntry_AtmLocation` | TField |  |  |
| 103 | `CAPL.SE.TRACE.NO` | `CaplHStmtEntry_TraceNo` | TField |  |  |
| 104 | `CAPL.SE.ATM.NUMBER` | `CaplHStmtEntry_AtmNumber` | TField |  |  |
| 105 | `CAPL.SE.ACCOUNT.TITLE.2` | `CaplHStmtEntry_AccountTitle2` | TField |  |  |
| 106 | `CAPL.SE.PAYMENT.DETAILS` | `CaplHStmtEntry_PaymentDetails` | TField |  |  |
| 107 | `CAPL.SE.CHARGE.AMT` | `CaplHStmtEntry_ChargeAmt` | TField |  |  |
| 108 | `CAPL.SE.CHEQUE.DATE` | `CaplHStmtEntry_ChequeDate` | TField |  |  |
| 109 | `CAPL.SE.TRANSIT` | `CaplHStmtEntry_Transit` | TField |  |  |
| 110 | `CAPL.SE.INSTITUTE.NO` | `CaplHStmtEntry_InstituteNo` | TField |  |  |
| 111 | `CAPL.SE.PAYEE.NAME` | `CaplHStmtEntry_PayeeName` | TField |  |  |
| 112 | `CAPL.SE.INTEREST.AMT` | `CaplHStmtEntry_InterestAmt` | TField |  |  |
| 113 | `CAPL.SE.LN.PRIN.RED.AMT` | `CaplHStmtEntry_LnPrinRedAmt` | TField |  |  |
| 114 | `CAPL.SE.PAYEE.ID` | `CaplHStmtEntry_PayeeId` | TField |  |  |
| 115 | `CAPL.SE.PAYER.BP.AC.NO` | `CaplHStmtEntry_PayerBpAcNo` | TField |  |  |
| 116 | `CAPL.SE.RECORD.STATUS` | `CaplHStmtEntry_RecordStatus` | String |  |  |
| 117 | `CAPL.SE.CURR.NO` | `CaplHStmtEntry_CurrNo` | String |  |  |
| 118 | `CAPL.SE.INPUTTER` | `CaplHStmtEntry_Inputter` |  |  |  |
| 119 | `CAPL.SE.DATE.TIME` | `CaplHStmtEntry_DateTime` |  |  |  |
| 120 | `CAPL.SE.AUTHORISER` | `CaplHStmtEntry_Authoriser` | String |  |  |
| 121 | `CAPL.SE.CO.CODE` | `CaplHStmtEntry_CoCode` | String |  |  |
| 122 | `CAPL.SE.DEPT.CODE` | `CaplHStmtEntry_DeptCode` | String |  |  |
| 123 | `CAPL.SE.AUDITOR.CODE` | `CaplHStmtEntry_AuditorCode` | String |  |  |
| 124 | `CAPL.SE.AUDIT.DATE.TIME` | `CaplHStmtEntry_AuditDateTime` | String |  |  |
