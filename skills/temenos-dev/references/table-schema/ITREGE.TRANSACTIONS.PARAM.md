# ITREGE.TRANSACTIONS.PARAM — Table Schema

> Source: `INSERTS/I_F.ITREGE.TRANSACTIONS.PARAM` in `ITREGE_PortfolioMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRANSACTIONS.PARAM.AREA.CODE` | `ItregeTransactionsParam_AreaCode` | TField |  | Inputs the Area code. |
| 2 | `TRANSACTIONS.PARAM.RECEPTION.CHANNEL` | `ItregeTransactionsParam_ReceptionChannel` | TField |  | Inputs the Reception channel. |
| 3 | `TRANSACTIONS.PARAM.SETTLEMENT.CHANNEL` | `ItregeTransactionsParam_SettlementChannel` | TField |  | Inputs the Settlement channel. |
| 4 | `TRANSACTIONS.PARAM.COMMISSION.TYPE` | `ItregeTransactionsParam_CommissionType` | TField |  | Inputs the Commission type. |
| 5 | `TRANSACTIONS.PARAM.SWIFT.CCY` | `ItregeTransactionsParam_SwiftCcy` | TField |  | Inputs the Swift currency. |
| 6 | `TRANSACTIONS.PARAM.CCY.CODE` | `ItregeTransactionsParam_CcyCode` | TField |  | Inputs the currency UIC. |
| 7 | `TRANSACTIONS.PARAM.TRANSMISSION.METHOD` | `ItregeTransactionsParam_TransmissionMethod` | TField |  | Inputs the method of transmission. |
| 8 | `TRANSACTIONS.PARAM.SERVICE` | `ItregeTransactionsParam_Service` | TField |  | Inputs the service. |
| 9 | `TRANSACTIONS.PARAM.CURRENCY` | `ItregeTransactionsParam_Currency` | TField |  | Inputs the currency |
| 10 | `TRANSACTIONS.PARAM.EXCHANGE` | `ItregeTransactionsParam_Exchange` | TField |  | Inputs the exchange. |
| 11 | `TRANSACTIONS.PARAM.SAL.PEN.PAYMENT.FLAG` | `ItregeTransactionsParam_SalPenPaymentFlag` | TField |  | Inputs the SAL.PEN.PAYMENT.FLAG. |
| 12 | `TRANSACTIONS.PARAM.CUSTOMER.RESIDENCE` | `ItregeTransactionsParam_CustomerResidence` | TField |  | Inputs the Customer residency. |
| 13 | `TRANSACTIONS.PARAM.CUST.NON.RESIDENCE` | `ItregeTransactionsParam_CustNonResidence` | TField |  | Inputs the Customer non residency. |
| 14 | `TRANSACTIONS.PARAM.DIRECTION.OUT` | `ItregeTransactionsParam_DirectionOut` | TField |  | Inputs the out direction. |
| 15 | `TRANSACTIONS.PARAM.DIRECTION.IN` | `ItregeTransactionsParam_DirectionIn` | TField |  | Inputs the in direction. |
| 16 | `TRANSACTIONS.PARAM.AMOUNT.FROM` | `ItregeTransactionsParam_AmountFrom` |  |  |  |
| 17 | `TRANSACTIONS.PARAM.AMOUNT.TO` | `ItregeTransactionsParam_AmountTo` |  |  |  |
| 18 | `TRANSACTIONS.PARAM.AMOUNT.CLASS` | `ItregeTransactionsParam_AmountClass` |  |  |  |
| 19 | `TRANSACTIONS.PARAM.TXN.INDICATOR` | `ItregeTransactionsParam_TxnIndicator` |  |  |  |
| 20 | `TRANSACTIONS.PARAM.TRANSFER.TYPE` | `ItregeTransactionsParam_TransferType` |  |  |  |
| 21 | `TRANSACTIONS.PARAM.TXN.TYPE.DEBIT` | `ItregeTransactionsParam_TxnTypeDebit` | TField |  | Inputs the debit transaction type. |
| 22 | `TRANSACTIONS.PARAM.TXN.TYPE.CREDIT` | `ItregeTransactionsParam_TxnTypeCredit` | TField |  | Inputs the credit trasnaction type. |
| 23 | `TRANSACTIONS.PARAM.RUN.DATE` | `ItregeTransactionsParam_RunDate` | TField |  | Inputs the last run date. |
| 24 | `TRANSACTIONS.PARAM.NOSTRO.CATEGORY` | `ItregeTransactionsParam_NostroCategory` |  |  |  |
| 25 | `TRANSACTIONS.PARAM.VOSTRO.CATEGORY` | `ItregeTransactionsParam_VostroCategory` |  |  |  |
| 26 | `TRANSACTIONS.PARAM.SOURCE.TYPE` | `ItregeTransactionsParam_SourceType` |  |  |  |
| 27 | `TRANSACTIONS.PARAM.MESSAGE.TYPE` | `ItregeTransactionsParam_MessageType` |  |  |  |
| 28 | `TRANSACTIONS.PARAM.BILL.TYPE.EXCH` | `ItregeTransactionsParam_BillTypeExch` |  |  |  |
| 29 | `TRANSACTIONS.PARAM.COLL.TYPE.CODE` | `ItregeTransactionsParam_CollTypeCode` |  |  |  |
| 30 | `TRANSACTIONS.PARAM.CUST.SECTOR` | `ItregeTransactionsParam_CustSector` |  |  |  |
| 31 | `TRANSACTIONS.PARAM.TXN.FLAG.MM` | `ItregeTransactionsParam_TxnFlagMm` | TField |  | Inputs the transaction flag. |
| 32 | `TRANSACTIONS.PARAM.TXN.FLAG.INDEPENDENT` | `ItregeTransactionsParam_TxnFlagIndependent` | TField |  | Inputs the transaction flag. |
| 33 | `TRANSACTIONS.PARAM.CODE.EVENT.TYPE` | `ItregeTransactionsParam_CodeEventType` | TField |  | Inputs the Code event type. |
| 34 | `TRANSACTIONS.PARAM.CODE.DURATION` | `ItregeTransactionsParam_CodeDuration` | TField |  | Inputs the Code duration. |
| 35 | `TRANSACTIONS.PARAM.CODE.SETT.CHANEL` | `ItregeTransactionsParam_CodeSettChanel` | TField |  | Inputs the Code settlement channel. |
| 36 | `TRANSACTIONS.PARAM.CODE.TXN.TYPE` | `ItregeTransactionsParam_CodeTxnType` | TField |  | Inputs the Code transaction type. |
| 37 | `TRANSACTIONS.PARAM.CODE.SETT.METHOD` | `ItregeTransactionsParam_CodeSettMethod` | TField |  | Inputs the Code settlement method |
| 38 | `TRANSACTIONS.PARAM.TXN.EXECU.PROV` | `ItregeTransactionsParam_TxnExecuProv` | TField |  | Inputs the Transaction exe province. |
| 39 | `TRANSACTIONS.PARAM.TXN.REF.CODE` | `ItregeTransactionsParam_TxnRefCode` | TField |  | Inputs the Transaction reference code. |
| 40 | `TRANSACTIONS.PARAM.UNPAID.FLAG` | `ItregeTransactionsParam_UnpaidFlag` | TField |  | Inputs the Unpaid flag. |
| 41 | `TRANSACTIONS.PARAM.SUCCESS.STATUS` | `ItregeTransactionsParam_SuccessStatus` |  |  |  |
| 42 | `TRANSACTIONS.PARAM.FAILURE.STATUS` | `ItregeTransactionsParam_FailureStatus` |  |  |  |
| 43 | `TRANSACTIONS.PARAM.RERUN.QUARTER` | `ItregeTransactionsParam_RerunQuarter` | TField |  | Value in the format 'Q' + Transaction quarter number + Transaction year. Eg. 'Q22019' Validation Rule: Should be among the last four quarters from today. |
| 44 | `TRANSACTIONS.PARAM.ACCOUNTING.COMP.CODE` | `ItregeTransactionsParam_AccountingCompCode` | TField |  | Inputs the accounting comp code |
| 45 | `TRANSACTIONS.PARAM.RATE.TYPE` | `ItregeTransactionsParam_RateType` | TField |  | Inputs the rate type |
| 46 | `TRANSACTIONS.PARAM.AVERAGE.BALANCE.SIGN` | `ItregeTransactionsParam_AverageBalanceSign` | TField |  | Inputs the average balance sign |
| 47 | `TRANSACTIONS.PARAM.BALANCE.SIGN` | `ItregeTransactionsParam_BalanceSign` | TField |  | Inputs the balance sign |
| 48 | `TRANSACTIONS.PARAM.ASSET.OR.LIABILITY` | `ItregeTransactionsParam_AssetOrLiability` | TField |  | Inputs asset/liabilty code |
| 49 | `TRANSACTIONS.PARAM.NO.OF.ACCOUNT` | `ItregeTransactionsParam_NoOfAccount` | TField |  | Inputs no of account |
| 50 | `TRANSACTIONS.PARAM.PRODUCT.LINE` | `ItregeTransactionsParam_ProductLine` |  |  |  |
| 51 | `TRANSACTIONS.PARAM.PRODUCT.GROUP` | `ItregeTransactionsParam_ProductGroup` |  |  |  |
| 52 | `TRANSACTIONS.PARAM.PRODUCT` | `ItregeTransactionsParam_Product` |  |  |  |
| 53 | `TRANSACTIONS.PARAM.EXCLUDE.PRODUCT` | `ItregeTransactionsParam_ExcludeProduct` |  |  |  |
| 54 | `TRANSACTIONS.PARAM.EXCLUDE.ACCOUNT.STATUS` | `ItregeTransactionsParam_ExcludeAccountStatus` |  |  |  |
| 55 | `TRANSACTIONS.PARAM.ACCOUNT.BALANCE` | `ItregeTransactionsParam_AccountBalance` | TField |  | Inputs balance type Validation Rule: Must be a valid entry in AC.BALANCE.TYPE |
| 56 | `TRANSACTIONS.PARAM.FISCAL.CODE` | `ItregeTransactionsParam_FiscalCode` | TField |  | Inputs Fiscal code |
| 57 | `TRANSACTIONS.PARAM.FREQUENCY` | `ItregeTransactionsParam_Frequency` | TField |  | Inputs Frequency code for the reporting |
| 58 | `TRANSACTIONS.PARAM.FREQ.PROGRESSIVE.NO` | `ItregeTransactionsParam_FreqProgressiveNo` | TField |  | Inputs Frequency Progressive Number for the report |
| 59 | `TRANSACTIONS.PARAM.OPENING.BAL.AMT.FROM` | `ItregeTransactionsParam_OpeningBalAmtFrom` |  |  |  |
| 60 | `TRANSACTIONS.PARAM.OPENING.BAL.AMT.TO` | `ItregeTransactionsParam_OpeningBalAmtTo` |  |  |  |
| 61 | `TRANSACTIONS.PARAM.OPENING.BAL.FLAG` | `ItregeTransactionsParam_OpeningBalFlag` |  |  |  |
| 62 | `TRANSACTIONS.PARAM.CLOSING.BAL.AMT.FROM` | `ItregeTransactionsParam_ClosingBalAmtFrom` |  |  |  |
| 63 | `TRANSACTIONS.PARAM.CLOSING.BAL.AMT.TO` | `ItregeTransactionsParam_ClosingBalAmtTo` |  |  |  |
| 64 | `TRANSACTIONS.PARAM.CLOSING.BAL.FLAG` | `ItregeTransactionsParam_ClosingBalFlag` |  |  |  |
| 65 | `TRANSACTIONS.PARAM.CREDIT.AMT.FROM` | `ItregeTransactionsParam_CreditAmtFrom` |  |  |  |
| 66 | `TRANSACTIONS.PARAM.CREDIT.AMT.TO` | `ItregeTransactionsParam_CreditAmtTo` |  |  |  |
| 67 | `TRANSACTIONS.PARAM.CREDIT.AMT.FLAG` | `ItregeTransactionsParam_CreditAmtFlag` |  |  |  |
| 68 | `TRANSACTIONS.PARAM.DEBIT.AMT.FROM` | `ItregeTransactionsParam_DebitAmtFrom` |  |  |  |
| 69 | `TRANSACTIONS.PARAM.DEBIT.AMT.TO` | `ItregeTransactionsParam_DebitAmtTo` |  |  |  |
| 70 | `TRANSACTIONS.PARAM.DEBIT.AMT.FLAG` | `ItregeTransactionsParam_DebitAmtFlag` |  |  |  |
| 71 | `TRANSACTIONS.PARAM.AVG.CREDIT.AMT.FROM` | `ItregeTransactionsParam_AvgCreditAmtFrom` |  |  |  |
| 72 | `TRANSACTIONS.PARAM.AVG.CREDIT.AMT.TO` | `ItregeTransactionsParam_AvgCreditAmtTo` |  |  |  |
| 73 | `TRANSACTIONS.PARAM.AVG.CREDIT.AMT.FLAG` | `ItregeTransactionsParam_AvgCreditAmtFlag` |  |  |  |
| 74 | `TRANSACTIONS.PARAM.ACCOUNT.TYPE` | `ItregeTransactionsParam_AccountType` | TField |  | Inputs Account Type for the reporting |
| 75 | `TRANSACTIONS.PARAM.ACCOUNT.TECH.SPEC` | `ItregeTransactionsParam_AccountTechSpec` | TField |  | Inputs Account Technical Specification for the reporting |
| 76 | `TRANSACTIONS.PARAM.CONTROL.CHARACTER` | `ItregeTransactionsParam_ControlCharacter` | TField |  | Inputs Control Character for the reporting |
| 77 | `TRANSACTIONS.PARAM.REPORT.CURRENCY` | `ItregeTransactionsParam_ReportCurrency` | TField |  | Inputs currency for the reporting |
| 78 | `TRANSACTIONS.PARAM.RERUN.YEAR` | `ItregeTransactionsParam_RerunYear` | TField |  | Inputs rerun year. Should be a valid year. |
| 79 | `TRANSACTIONS.PARAM.TRANSACTION.CODE` | `ItregeTransactionsParam_TransactionCode` |  |  |  |
| 80 | `TRANSACTIONS.PARAM.AMOUNT.LOWER.LIMIT` | `ItregeTransactionsParam_AmountLowerLimit` |  |  |  |
| 81 | `TRANSACTIONS.PARAM.AMOUNT.UPPER.LIMIT` | `ItregeTransactionsParam_AmountUpperLimit` |  |  |  |
| 82 | `TRANSACTIONS.PARAM.AMOUNT.FLAG` | `ItregeTransactionsParam_AmountFlag` |  |  |  |
| 83 | `TRANSACTIONS.PARAM.EXCLUDE.INTERNAL.ACCOUNT` | `ItregeTransactionsParam_ExcludeInternalAccount` |  |  |  |
| 84 | `TRANSACTIONS.PARAM.EXCLUDE.PL.ACCOUNT` | `ItregeTransactionsParam_ExcludePlAccount` |  |  |  |
| 85 | `TRANSACTIONS.PARAM.INCLUDE.INTERNAL.ACCOUNT` | `ItregeTransactionsParam_IncludeInternalAccount` |  |  |  |
| 86 | `TRANSACTIONS.PARAM.PISP.PAYMENT` | `ItregeTransactionsParam_PispPayment` | TField |  | This field refers to transfers ordered by Payment Initiation Service Provider |
| 87 | `TRANSACTIONS.PARAM.OVERRIDE` | `ItregeTransactionsParam_Override` |  |  |  |
| 88 | `TRANSACTIONS.PARAM.RECORD.STATUS` | `ItregeTransactionsParam_RecordStatus` | String |  |  |
| 89 | `TRANSACTIONS.PARAM.CURR.NO` | `ItregeTransactionsParam_CurrNo` | String |  |  |
| 90 | `TRANSACTIONS.PARAM.INPUTTER` | `ItregeTransactionsParam_Inputter` |  |  |  |
| 91 | `TRANSACTIONS.PARAM.DATE.TIME` | `ItregeTransactionsParam_DateTime` |  |  |  |
| 92 | `TRANSACTIONS.PARAM.AUTHORISER` | `ItregeTransactionsParam_Authoriser` | String |  |  |
| 93 | `TRANSACTIONS.PARAM.CO.CODE` | `ItregeTransactionsParam_CoCode` | String |  |  |
| 94 | `TRANSACTIONS.PARAM.DEPT.CODE` | `ItregeTransactionsParam_DeptCode` | String |  |  |
| 95 | `TRANSACTIONS.PARAM.AUDITOR.CODE` | `ItregeTransactionsParam_AuditorCode` | String |  |  |
| 96 | `TRANSACTIONS.PARAM.AUDIT.DATE.TIME` | `ItregeTransactionsParam_AuditDateTime` | String |  |  |
| 97 | `TRANSACTIONS.PARAM.MOB.OPER.TYPE` | `ItregeTransactionsParam_MobOperType` | TField |  | This field holds the type of mobile operator |
| 98 | `TRANSACTIONS.PARAM.IND.PAY.MOD.UNIFIED` | `ItregeTransactionsParam_IndPayModUnified` | TField |  | This field holds the value of unified payment models |
| 99 | `TRANSACTIONS.PARAM.CSCA` | `ItregeTransactionsParam_Csca` | TField |  | Holds the field name for CSCA details in payment record |
| 100 | `TRANSACTIONS.PARAM.CMOTDER.SCA` | `ItregeTransactionsParam_CmotderSca` | TField |  | Holds the field name for CMOTDER SCA details in payment record |
| 101 | `TRANSACTIONS.PARAM.TXN.TYPE.COMMISSION.FEE` | `ItregeTransactionsParam_TxnTypeCommissionFee` |  |  |  |
