# DX.OPTSTRUCT — Table Schema

> Source: `INSERTS/I_F.DX.OPTSTRUCT` in `DX_OptStructContract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.OPT.VARIANT` | `DxOptstruct_Variant` | TField |  |  |
| 2 | `DX.OPT.DESCRIPTION` | `DxOptstruct_Description` |  |  |  |
| 3 | `DX.OPT.TRADE.DATE` | `DxOptstruct_TradeDate` | TField |  | This field holds the trade date of the structure. This will also be the trade date of the underlying options |
| 4 | `DX.OPT.VALUE.DATE` | `DxOptstruct_ValueDate` | TField |  | This field holds the value date of the structure. This will also be the value date of the underlying options |
| 5 | `DX.OPT.MATURITY.DATE` | `DxOptstruct_MaturityDate` | TField |  | This field holds the maturity date of the structure. |
| 6 | `DX.OPT.TRADE.CCY` | `DxOptstruct_TradeCcy` | TField |  | The trade currency of the contract |
| 7 | `DX.OPT.NOTIONAL.AMT` | `DxOptstruct_NotionalAmt` | TField |  | This field will hold the notional amount for the structure. Contingent entries raised from underlying trades will be suppressed. For this amount, contingent entry will be raised from SY. |
| 8 | `DX.OPT.RUN.NOTIONAL.AMT` | `DxOptstruct_RunNotionalAmt` | TField |  | When EXERCISE/EXPIRE is set in OPT.EXERCISE field, this field is to be manually changed. During fixing, existing notional will be reversed and entry will be raised for the amount entered in this field.Notional amount would be in trade currency. |
| 9 | `DX.OPT.PREMIUM.CCY` | `DxOptstruct_PremiumCcy` | TField |  | This field will hold the currency associated with the premium amount.This field be defaulted with Trade currency. |
| 10 | `DX.OPT.PREM.PAYMENT.DATE` | `DxOptstruct_PremPaymentDate` | TField |  | This field will hold the date on which the premium should be posted. |
| 11 | `DX.OPT.PREM.RESERVED.4` | `DxOptstruct_PremReserved4` | TField |  | Reserved for future |
| 12 | `DX.OPT.PREM.RESERVED.3` | `DxOptstruct_PremReserved3` | TField |  | Reserved for future |
| 13 | `DX.OPT.PREM.RESERVED.2` | `DxOptstruct_PremReserved2` | TField |  | Reserved for future |
| 14 | `DX.OPT.PREM.RESERVED.1` | `DxOptstruct_PremReserved1` | TField |  | Reserved for future |
| 15 | `DX.OPT.CUSTOMER` | `DxOptstruct_Customer` | TField | Yes | This field will hold the customer for the structure deal.It can also be a dealer book for back to back deal. This will also be the primary customer in the underlying options. Validation Rules: Mandatory Field. |
| 16 | `DX.OPT.CUST.PORT` | `DxOptstruct_CustPort` | TField |  | This field will hold the portfolio of the customer against which the contract is created. This field will be defaulted with the first portfolio of the customer. |
| 17 | `DX.OPT.CUST.CASH.SETT.ACC` | `DxOptstruct_CustCashSettAcc` | TField |  | This field will hold the account where cash settlement will be debited/credited if there is a cash exercise. This will be with respect to cash currency if Cash exercise is chosen. |
| 18 | `DX.OPT.CUST.PREM.PAY.REC` | `DxOptstruct_CustPremPayRec` | TField |  | This field will say whether the customer have to receive/pay the premium amount |
| 19 | `DX.OPT.CUST.PREM.AMT` | `DxOptstruct_CustPremAmt` | TField |  | This holds the premium amount paid or received by the customer. Validation Rules: Allowed to Input when Customer is a non Dealer Book |
| 20 | `DX.OPT.CUST.PREM.ACC` | `DxOptstruct_CustPremAcc` | TField |  | This field will hold the premium account of the customer where premium will be paid or from where premimum will be received.This account will be with respect to PREMIUM.CCY |
| 21 | `DX.OPT.COUNTERPARTY` | `DxOptstruct_Counterparty` | TField | Yes | The counter party of the contract is defined in this field. The customer should be defined in CUSTOMER.SECURITY. Either counter party or customer should be a dealer book. Validation Rules: Mandatory Field. |
| 22 | `DX.OPT.CPARTY.PORT` | `DxOptstruct_CpartyPort` | TField |  | This field will hold the portfolio of the counterparty against which the contract is created. This field will be defaulted with the first portfolio of the counterparty. |
| 23 | `DX.OPT.CPARTY.CASH.SETT.ACC` | `DxOptstruct_CpartyCashSettAcc` | TField |  | This field will hold the account where cash settlement will be debited/credited if there is a cash exercise. This will be with respect to cash currency if Cash exercise is chosen. |
| 24 | `DX.OPT.CPA.PREM.PAY.REC` | `DxOptstruct_CpaPremPayRec` | TField |  | This field will say whether the counterparty have to receive/pay the premium amount. This will be the opposite of CUST.PREM.PAY.REC |
| 25 | `DX.OPT.CPA.PREM.AMT` | `DxOptstruct_CpaPremAmt` | TField |  | This holds the premium amount paid or received by the Counterparty. Validation Rules: Allowed to Input when Counterparty is a non Dealer Book. |
| 26 | `DX.OPT.CPA.PREM.ACC` | `DxOptstruct_CpaPremAcc` | TField |  | This field will hold the premium account of the customer where premium will be paid or from where preimum will be received.This account will be with respect to PREMIUM.CCY |
| 27 | `DX.OPT.SY.DX.REFERENCE` | `DxOptstruct_SyDxReference` | TField |  | The unique reference will be updated in all the underlying contracts, in order to track all the underlying's generated from the SY.OPTSTRUCT contract. This field will be defaulted with ID of the contract |
| 28 | `DX.OPT.B2B.REFERENCE` | `DxOptstruct_B2bReference` |  |  |  |
| 29 | `DX.OPT.SY.TRANSACTION.REF` | `DxOptstruct_SyTransactionRef` | TField |  | This field will hold the SY.TRANSACTION ID |
| 30 | `DX.OPT.SETTLEMENT.METHOD` | `DxOptstruct_SettlementMethod` | TField |  | This field specifies whether the contract is physically settled or cash settled. Underlying options will also have the same settlement method. |
| 31 | `DX.OPT.LIMIT.REF` | `DxOptstruct_LimitRef` | TField |  | The Limit reference identifying the non dealer book customer credit line . |
| 32 | `DX.OPT.LIMIT.DETS` | `DxOptstruct_LimitDets` | TField |  | This field is used to store limit related details. Technical use. |
| 33 | `DX.OPT.FEE.CCY` | `DxOptstruct_FeeCcy` | TField |  | This field will store the currency in which in fee has to be collected. |
| 34 | `DX.OPT.CUST.FEE.AMT` | `DxOptstruct_CustFeeAmt` | TField |  | This field will store the fee amount to be collected from the customer. Validation Rules: Allowed to Input when Customer is a non Dealer Book |
| 35 | `DX.OPT.CUST.FEE.ACCT` | `DxOptstruct_CustFeeAcct` | TField |  | This field will hold the fee account of the customer where fee will be paid or from where preimum will be received.This account will be with respect to FEE.CCY |
| 36 | `DX.OPT.CPA.FEE.AMT` | `DxOptstruct_CpaFeeAmt` | TField |  | Reserved for future |
| 37 | `DX.OPT.CPA.FEE.ACCT` | `DxOptstruct_CpaFeeAcct` | TField |  | Reserved for future |
| 38 | `DX.OPT.OPT.STYLE` | `DxOptstruct_OptStyle` | TField |  | This field will hold the option style and this will be defaulted in all the underlying options |
| 39 | `DX.OPT.SUPPRESS.UNDERLYING` | `DxOptstruct_SuppressUnderlying` | TField |  | This field will say whether the underlying contracts to be suppressed or not. This field will be defaulted from SY.PRODUCT.VARIANT if VARIANT is given else it will be defaulted from SY.PRODUCT.DEFINITION |
| 40 | `DX.OPT.BUILD.STRUCTURE` | `DxOptstruct_BuildStructure` | TField |  | This field will decide whether underying options will have to be created manually or not. |
| 41 | `DX.OPT.DX.TRADE.ID` | `DxOptstruct_DxTradeId` |  |  |  |
| 42 | `DX.OPT.OPT.DX.CONTRACT.MASTER` | `DxOptstruct_OptDxContractMaster` |  |  |  |
| 43 | `DX.OPT.OPT.STRIKE.PRICE` | `DxOptstruct_OptStrikePrice` |  |  |  |
| 44 | `DX.OPT.OPT.CALL.PUT` | `DxOptstruct_OptCallPut` |  |  |  |
| 45 | `DX.OPT.OPT.BUY.SELL` | `DxOptstruct_OptBuySell` |  |  |  |
| 46 | `DX.OPT.OPT.LOT.SIZE` | `DxOptstruct_OptLotSize` |  |  |  |
| 47 | `DX.OPT.OPT.MATURITY.DATE` | `DxOptstruct_OptMaturityDate` |  |  |  |
| 48 | `DX.OPT.OPT.FIX.DATE` | `DxOptstruct_OptFixDate` |  |  |  |
| 49 | `DX.OPT.OPT.EXERCISE` | `DxOptstruct_OptExercise` |  |  |  |
| 50 | `DX.OPT.OPT.STATUS` | `DxOptstruct_OptStatus` |  |  |  |
| 51 | `DX.OPT.RESERVED.30` | `DxOptstruct_Reserved30` |  |  |  |
| 52 | `DX.OPT.RESERVED.29` | `DxOptstruct_Reserved29` |  |  |  |
| 53 | `DX.OPT.RESERVED.28` | `DxOptstruct_Reserved28` |  |  |  |
| 54 | `DX.OPT.RESERVED.27` | `DxOptstruct_Reserved27` |  |  |  |
| 55 | `DX.OPT.RESERVED.26` | `DxOptstruct_Reserved26` |  |  |  |
| 56 | `DX.OPT.RESERVED.25` | `DxOptstruct_Reserved25` |  |  |  |
| 57 | `DX.OPT.RESERVED.24` | `DxOptstruct_Reserved24` |  |  |  |
| 58 | `DX.OPT.RESERVED.23` | `DxOptstruct_Reserved23` |  |  |  |
| 59 | `DX.OPT.RESERVED.22` | `DxOptstruct_Reserved22` |  |  |  |
| 60 | `DX.OPT.RESERVED.21` | `DxOptstruct_Reserved21` |  |  |  |
| 61 | `DX.OPT.RESERVED.20` | `DxOptstruct_Reserved20` |  |  |  |
| 62 | `DX.OPT.RESERVED.19` | `DxOptstruct_Reserved19` |  |  |  |
| 63 | `DX.OPT.RESERVED.18` | `DxOptstruct_Reserved18` |  |  |  |
| 64 | `DX.OPT.RESERVED.17` | `DxOptstruct_Reserved17` |  |  |  |
| 65 | `DX.OPT.RESERVED.16` | `DxOptstruct_Reserved16` |  |  |  |
| 66 | `DX.OPT.DEAL.STATUS` | `DxOptstruct_DealStatus` | TField |  | This field says whether the contract is active or matured or unwound. This field will accept the values 'ACTIVE' 'MATURED' 'UNWOUND'. The field will be defaulted to Active when a new contract is done. |
| 67 | `DX.OPT.FIX.STRUCTURE` | `DxOptstruct_FixStructure` | TField |  | This field can chosen to fix the structure as a whole.Options that are marked EXERCISE will be exercised and marked as EXPIRE/null will be expired and DEAL.STATUS marked as MATURED indicating that the structure is closed. If field CASH.EXERCISE is set as YES, cash settlement would happen for the amount given in field CASH.AMOUNT. |
| 68 | `DX.OPT.STRUCTURE.FIX.DATE` | `DxOptstruct_StructureFixDate` | TField |  | This field will hold the fixing date for the entire structure. This field will be mapped to TRADE.DATE in SEC.TRADE created during exercise. |
| 69 | `DX.OPT.CASH.EXERCISE` | `DxOptstruct_CashExercise` | TField |  | This field will decide whether to generate cash payout. Input allowed only when SETTLEMENT.METHOD is CASH |
| 70 | `DX.OPT.CASH.CCY` | `DxOptstruct_CashCcy` | TField |  | This field holds the Payout currency in which cash amount is paid out. The cash settlement would happen in this currency. Input allowed only when CASH.EXERCISE is set as YES |
| 71 | `DX.OPT.CASH.AMOUNT` | `DxOptstruct_CashAmount` | TField |  | This field holds the cash amount that needs to be paid out for a cash settled option. Input allowed only when CASH.EXERCISE is set as YES |
| 72 | `DX.OPT.CASH.RESERVED.10` | `DxOptstruct_CashReserved10` | TField |  | Reserved for future |
| 73 | `DX.OPT.CASH.RESERVED.9` | `DxOptstruct_CashReserved9` | TField |  | Reserved for future |
| 74 | `DX.OPT.CASH.RESERVED.8` | `DxOptstruct_CashReserved8` | TField |  | Reserved for future |
| 75 | `DX.OPT.CASH.RESERVED.7` | `DxOptstruct_CashReserved7` | TField |  | Reserved for future |
| 76 | `DX.OPT.CASH.RESERVED.6` | `DxOptstruct_CashReserved6` | TField |  | Reserved for future |
| 77 | `DX.OPT.CASH.RESERVED.5` | `DxOptstruct_CashReserved5` | TField |  | Reserved for future |
| 78 | `DX.OPT.CASH.RESERVED.4` | `DxOptstruct_CashReserved4` | TField |  | Reserved for future |
| 79 | `DX.OPT.CASH.RESERVED.3` | `DxOptstruct_CashReserved3` | TField |  | Reserved for future |
| 80 | `DX.OPT.CASH.RESERVED.2` | `DxOptstruct_CashReserved2` | TField |  | Reserved for future |
| 81 | `DX.OPT.CASH.RESERVED.1` | `DxOptstruct_CashReserved1` | TField |  | Reserved for future |
| 82 | `DX.OPT.UNWIND` | `DxOptstruct_Unwind` | TField |  | When this field holds the value as YES, then the contract is unwound. |
| 83 | `DX.OPT.UNWIND.CHG.CCY` | `DxOptstruct_UnwindChgCcy` | TField |  | This field will store the currency in which unwinding charges are to be collected. |
| 84 | `DX.OPT.CUST.UNWIND.CHG.AMT` | `DxOptstruct_CustUnwindChgAmt` | TField |  | This field will store the unwinding charge amount. Validation Rules: Allowed to Input when Customer is a non Dealer Book |
| 85 | `DX.OPT.CUST.UNWIND.CHG.ACC` | `DxOptstruct_CustUnwindChgAcc` | TField |  | This field will hold the account where unwind should be performed.This will be with respect to UNWIND.CHG.CCY if UNWIND is chosen |
| 86 | `DX.OPT.CPA.UNWIND.CHG.AMT` | `DxOptstruct_CpaUnwindChgAmt` | TField |  | This field will hold the date from which the unwind is effective. The date will always be defaulted to today if UNWIND is set. Validation Rules: Allowed to Input when Counterparty is a non Dealer Book. |
| 87 | `DX.OPT.CPA.UNWIND.CHG.ACC` | `DxOptstruct_CpaUnwindChgAcc` | TField |  | This field will hold the account where unwind should be performed.This will be with respect to UNWIND.CHG.CCY if UNWIND is chosen |
| 88 | `DX.OPT.UNWIND.EFF.DATE` | `DxOptstruct_UnwindEffDate` | TField |  | This field will hold the date on which the unwind should be posted. |
| 89 | `DX.OPT.UNWIND.RESERVED.5` | `DxOptstruct_UnwindReserved5` | TField |  | Reserved for future |
| 90 | `DX.OPT.UNWIND.RESERVED.4` | `DxOptstruct_UnwindReserved4` | TField |  | Reserved for future |
| 91 | `DX.OPT.UNWIND.RESERVED.3` | `DxOptstruct_UnwindReserved3` | TField |  | Reserved for future |
| 92 | `DX.OPT.UNWIND.RESERVED.2` | `DxOptstruct_UnwindReserved2` | TField |  | Reserved for future |
| 93 | `DX.OPT.UNWIND.RESERVED.1` | `DxOptstruct_UnwindReserved1` | TField |  | Reserved for future |
| 94 | `DX.OPT.DEALER.DESK` | `DxOptstruct_DealerDesk` | TField |  | This field will hold DEALER.DESK of the contract |
| 95 | `DX.OPT.PYMT.MSG.REQD` | `DxOptstruct_PymtMsgReqd` | TField |  | When this field holds the value as YES, then payment message will be generated |
| 96 | `DX.OPT.BEN.BANK` | `DxOptstruct_BenBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 97 | `DX.OPT.BEN.ADD` | `DxOptstruct_BenAdd` |  |  |  |
| 98 | `DX.OPT.BEN.ACCT` | `DxOptstruct_BenAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 99 | `DX.OPT.INTR.BANK` | `DxOptstruct_IntrBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 100 | `DX.OPT.INTR.ADD` | `DxOptstruct_IntrAdd` |  |  |  |
| 101 | `DX.OPT.CPTY.NO` | `DxOptstruct_CptyNo` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 102 | `DX.OPT.CPTY.ADD` | `DxOptstruct_CptyAdd` |  |  |  |
| 103 | `DX.OPT.CPTY.ACCT` | `DxOptstruct_CptyAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 104 | `DX.OPT.RESERVED.15` | `DxOptstruct_Reserved15` | TField |  | Reserved for future |
| 105 | `DX.OPT.RESERVED.14` | `DxOptstruct_Reserved14` | TField |  | Reserved for future |
| 106 | `DX.OPT.RESERVED.13` | `DxOptstruct_Reserved13` | TField |  | Reserved for future |
| 107 | `DX.OPT.RESERVED.12` | `DxOptstruct_Reserved12` | TField |  | Reserved for future |
| 108 | `DX.OPT.RESERVED.11` | `DxOptstruct_Reserved11` | TField |  | Reserved for future |
| 109 | `DX.OPT.RESERVED.10` | `DxOptstruct_Reserved10` | TField |  | Reserved for future |
| 110 | `DX.OPT.RESERVED.9` | `DxOptstruct_Reserved9` | TField |  | Reserved for future |
| 111 | `DX.OPT.RESERVED.8` | `DxOptstruct_Reserved8` | TField |  | Reserved for future |
| 112 | `DX.OPT.RESERVED.7` | `DxOptstruct_Reserved7` | TField |  | Reserved for future |
| 113 | `DX.OPT.RESERVED.6` | `DxOptstruct_Reserved6` | TField |  | Reserved for future |
| 114 | `DX.OPT.RESERVED.5` | `DxOptstruct_Reserved5` | TField |  | Reserved for future |
| 115 | `DX.OPT.RESERVED.4` | `DxOptstruct_Reserved4` | TField |  | Reserved for future |
| 116 | `DX.OPT.RESERVED.3` | `DxOptstruct_Reserved3` | TField |  | Reserved for future |
| 117 | `DX.OPT.RESERVED.2` | `DxOptstruct_Reserved2` | TField |  | Reserved for future |
| 118 | `DX.OPT.RESERVED.1` | `DxOptstruct_Reserved1` | TField |  | Reserved for future |
| 119 | `DX.OPT.LOCAL.REF` | `DxOptstruct_LocalRef` |  |  |  |
| 120 | `DX.OPT.STMT.NOS` | `DxOptstruct_StmtNos` |  |  |  |
| 121 | `DX.OPT.OVERRIDE` | `DxOptstruct_Override` |  |  |  |
| 122 | `DX.OPT.RECORD.STATUS` | `DxOptstruct_RecordStatus` | String |  |  |
| 123 | `DX.OPT.CURR.NO` | `DxOptstruct_CurrNo` | String |  |  |
| 124 | `DX.OPT.INPUTTER` | `DxOptstruct_Inputter` |  |  |  |
| 125 | `DX.OPT.DATE.TIME` | `DxOptstruct_DateTime` |  |  |  |
| 126 | `DX.OPT.AUTHORISER` | `DxOptstruct_Authoriser` | String |  |  |
| 127 | `DX.OPT.CO.CODE` | `DxOptstruct_CoCode` | String |  |  |
| 128 | `DX.OPT.DEPT.CODE` | `DxOptstruct_DeptCode` | String |  |  |
| 129 | `DX.OPT.AUDITOR.CODE` | `DxOptstruct_AuditorCode` | String |  |  |
| 130 | `DX.OPT.AUDIT.DATE.TIME` | `DxOptstruct_AuditDateTime` | String |  |  |
