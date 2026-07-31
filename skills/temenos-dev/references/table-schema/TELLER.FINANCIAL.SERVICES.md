# TELLER.FINANCIAL.SERVICES — Table Schema

> Source: `INSERTS/I_F.TELLER.FINANCIAL.SERVICES` in `TT_TellerFinancialService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TFS.BOOKING.DATE` | `TellerFinancialServices_BookingDate` | TField |  | The date on which this TFS Transaction was booked. This has no systemic/accounting significance but rather used for reporting purposes. Validation Rules: = Defaulted to current bank date. But can be overriden. Input must be less than or equal to current bank date. |
| 2 | `TFS.PRIMARY.CUSTOMER` | `TellerFinancialServices_PrimaryCustomer` | TField |  | The Customer of the account specified in PRIMARY.ACCOUNT. Defaulted from the field validation of PRIMARY.ACCOUNT. Validation Rules: = If left blank and if PRIMARY.ACCOUNT is keyed in, then this is defaulted with the Customer number in the account record of the PRIMARY.ACCOUNT. If keyed in, and if PRIMARY.ACCOUNT is left blank, then will default the first account as held in CUSTOMER.ACCOUNT table. The value in this field must be the same as the Customer of the PRIMARY.ACCOUNT, as held in the Account record. |
| 3 | `TFS.PRIMARY.ACCOUNT` | `TellerFinancialServices_PrimaryAccount` | TField | Conditional | When a number of TFS legs are input by the user, it is more likely that all of them have one thing in common - the main "transaction account" of the customer (a.k.a Current Accounts or Checking Accounts or DDAs). Instead of requiring the user to key in the same account number again and again in each of the TFS legs, this field can be used. Once keyed in, it also defaults the Customer of this account in the PRIMARY.CUSTOMER field. Subsequently in user input legs, this is used as one side of the leg while the other side could be a Till/Suspense account (based on CAT.DEP.CODE.1, CAT.DEPT.CODE.2 specifications in TELLER.TRANSACTION) or input in the associated SURROGATE.AC field for that TFS leg. When consolidation is enabled, the user input legs are defaulted with the washthru account of the same currency as this account. A final consolidated leg is automatically calculated by the system between that Washthru account and this account at the end when the user instructs the system by setting the field CONSOLIDATE.NOW to YES. Validation Rules: Optional Input. Input mandatory if Consolidation is enabled. Input can be of any currency and can be either a Customer or an Internal account or even a PL Category (although the latter two are not really applicable for Teller Operations). If left blank and if PRIMARY.CUSTOMER is keyed in, then the first available account of that customer is defaulted in this field. |
| 4 | `TFS.PRIMARY.ACCOUNT.INT` | `TellerFinancialServices_PrimaryAccountInt` | TField |  | This field gets populated with the value of PRIMARY.ACCOUNT field.In browser if user changes the PRIMARY.ACCOUNT, the old value of PRIMARY.ACCOUNT is not known to the user hence we make use of this field for checking with user changed value to clear out the defaults done on the individual TFS Legs. Validation Rules: = Noinput field. Automatically defaulted by the system. |
| 5 | `TFS.CONSOL.INSTRUCTION` | `TellerFinancialServices_ConsolInstruction` | TField |  | If Consolidation is enabled at TFS.PARAMETER level, it is possible to override it at an individual TFS Transaction level by setting this field to NO. Although, it is not possible to enable at TFS transaction level if Consolidation is disabled at TFS.PARAMETER level. When set to YES, all the user input TFS legs will be consolidated for the Primary Account. These consolidated legs could be just 1 in number or more depending on the settings in CONSOL.METHOD and CONSOL.LEVEL.ADDON. TFS achieves this by using a temporary washthru account (a placeholder)on the user input legs and eventually when the user indicates that he/she is done with entering the transactions, it creates one or more consolidated leg(s) between this Washthru account and the account specified in PRIMARY.ACCOUNT field. The consolidated Leg is really just another TFS Leg corresponding to a TELLER Transaction. Even if Consolidation is enabled, if for a given TFS Leg, the field CONSOL.EXCLUDE in the respective TFS.TRANSACTION is set to YES, then that TFS leg will not be included in the Consolidation Process. Validation Rules: Defaulted to YES if CONSOLIDATION in TFS.PARAMETER is set to ENABLE. Can be overridden by user. Defaulted to NO if CONSOLIDATION in TFS.PARAMETER is set to DISABLE. Cannot be overridden by user. |
| 6 | `TFS.CONSOL.METHOD` | `TellerFinancialServices_ConsolMethod` | TField | No | This is the same field as in TFS.PARAMETER. Any settings in this field in TFS.PARAMETER can be overridden here at a TFS Transaction level. If Consolidation is enabled, then TFS will combine all the user input transactions on a single TFS screen and create that as a single transaction hitting the account specified in PRIMARY.ACCOUNT field. This field allows to define if the combined transaction should be "NET" - Consolidation of all debits and credits or "GROSS" - Consolidate all debits together and Consolidate all credits together. Even if this field is set to NET, there is an exception - if the Consolidated amount happens to be 0, then if the field CONSOL.AMT.ZERO in TFS.PARAMETER is set to FORCE.GROSS, then the consolidation is forced to be at GROSS level. Similarly, if there are Credit and Debit TFS legs and if even one of the Credit leg carries a forward exposure, then the system will automatically force the Consolidation to be at GROSS level becasue it is not possible to combine credits with forward exposure &amp; debits. Validation Rules: ================= Optional Input. Allowed Values: GROSS, NET Input not allowed if CONSOLIDATION is disabled. |
| 7 | `TFS.CONSOL.LEVEL.ADDON` | `TellerFinancialServices_ConsolLevelAddon` | TField | No | This is the same field as in TFS.PARAMETER. Any settings in this field in TFS.PARAMETER can be overridden here at a TFS transaction level. If Consolidation is enabled, then TFS will combine all the user input transactions on a single TFS screen and create that as a single transaction hitting the account specified in PRIMARY.ACCOUNT field. The default Consolidation level is the VALUE.DATE of the individual user input TFS transactions. On top of that, if there is a need to combine transactions using additional attributes, that can be set in this field. Validation Rules: ================= Optional Input. Allowed Values: NO, CCY, CCY.TXN, TXN. Default Value: NO Input not allowed if CONSOLIDATION is set to DISABLE. If set to CCY, then all user input legs of a TFS transaction will be combined based on VALUE.DATE &amp; CURRENCY of the Leg. If set to CCY.TXN, then all user input legs of a TFS transaction will be combined based on VALUE.DATE, CURRENCY &amp; TRANSACTION type of the Leg. If set to TXN, then all user input legs of a TFS transaction will be combined based on VALUE.DATE &amp; TRANSACTION type of the Leg. |
| 8 | `TFS.RESERVED.8` | `TellerFinancialServices_Reserved8` | TField |  |  |
| 9 | `TFS.RESERVED.9` | `TellerFinancialServices_Reserved9` | TField |  |  |
| 10 | `TFS.RESERVED.10` | `TellerFinancialServices_Reserved10` | TField |  |  |
| 11 | `TFS.RESERVED.11` | `TellerFinancialServices_Reserved11` | TField |  |  |
| 12 | `TFS.RESERVED.12` | `TellerFinancialServices_Reserved12` | TField |  |  |
| 13 | `TFS.TRANSACTION` | `TellerFinancialServices_Transaction` |  |  |  |
| 14 | `TFS.TRANSACTION.INT` | `TellerFinancialServices_TransactionInt` |  |  |  |
| 15 | `TFS.BENEFICIARY.ID` | `TellerFinancialServices_BeneficiaryId` |  |  |  |
| 16 | `TFS.RESERVED.16` | `TellerFinancialServices_Reserved16` |  |  |  |
| 17 | `TFS.SURROGATE.AC` | `TellerFinancialServices_SurrogateAc` |  |  |  |
| 18 | `TFS.ACCOUNT.DR` | `TellerFinancialServices_AccountDr` |  |  |  |
| 19 | `TFS.CURRENCY.DR` | `TellerFinancialServices_CurrencyDr` |  |  |  |
| 20 | `TFS.CCY.DR.INT` | `TellerFinancialServices_CcyDrInt` |  |  |  |
| 21 | `TFS.EXCH.TXN.DR` | `TellerFinancialServices_ExchTxnDr` |  |  |  |
| 22 | `TFS.AMOUNT.DR` | `TellerFinancialServices_AmountDr` |  |  |  |
| 23 | `TFS.AMOUNT.DR.LCY` | `TellerFinancialServices_AmountDrLcy` |  |  |  |
| 24 | `TFS.ACCOUNT.CR` | `TellerFinancialServices_AccountCr` |  |  |  |
| 25 | `TFS.CURRENCY.CR` | `TellerFinancialServices_CurrencyCr` |  |  |  |
| 26 | `TFS.CCY.CR.INT` | `TellerFinancialServices_CcyCrInt` |  |  |  |
| 27 | `TFS.EXCH.TXN.CR` | `TellerFinancialServices_ExchTxnCr` |  |  |  |
| 28 | `TFS.AMOUNT.CR` | `TellerFinancialServices_AmountCr` |  |  |  |
| 29 | `TFS.AMOUNT.CR.LCY` | `TellerFinancialServices_AmountCrLcy` |  |  |  |
| 30 | `TFS.CURRENCY` | `TellerFinancialServices_Currency` |  |  |  |
| 31 | `TFS.CURRENCY.INT` | `TellerFinancialServices_CurrencyInt` |  |  |  |
| 32 | `TFS.AMOUNT` | `TellerFinancialServices_Amount` |  |  |  |
| 33 | `TFS.AMOUNT.INT` | `TellerFinancialServices_AmountInt` |  |  |  |
| 34 | `TFS.AMOUNT.LCY` | `TellerFinancialServices_AmountLcy` |  |  |  |
| 35 | `TFS.DEAL.RATE` | `TellerFinancialServices_DealRate` |  |  |  |
| 36 | `TFS.DEAL.RATE.INT` | `TellerFinancialServices_DealRateInt` |  |  |  |
| 37 | `TFS.WASHTHRU.SIDE` | `TellerFinancialServices_WashthruSide` |  |  |  |
| 38 | `TFS.WAIVE.CHARGE` | `TellerFinancialServices_WaiveCharge` |  |  |  |
| 39 | `TFS.CHG.CODE` | `TellerFinancialServices_ChgCode` |  |  |  |
| 40 | `TFS.CHG.ACCOUNT` | `TellerFinancialServices_ChgAccount` |  |  |  |
| 41 | `TFS.CHG.CCY` | `TellerFinancialServices_ChgCcy` |  |  |  |
| 42 | `TFS.CHG.AMT` | `TellerFinancialServices_ChgAmt` |  |  |  |
| 43 | `TFS.CHG.AMT.LCY` | `TellerFinancialServices_ChgAmtLcy` |  |  |  |
| 44 | `TFS.CR.VALUE.DATE` | `TellerFinancialServices_CrValueDate` |  |  |  |
| 45 | `TFS.DR.VALUE.DATE` | `TellerFinancialServices_DrValueDate` |  |  |  |
| 46 | `TFS.NO.OF.CHEQUES` | `TellerFinancialServices_NoOfCheques` |  |  |  |
| 47 | `TFS.CHEQUE.DRAWN` | `TellerFinancialServices_ChequeDrawn` |  |  |  |
| 48 | `TFS.CHEQUE.DATE` | `TellerFinancialServices_ChequeDate` |  |  |  |
| 49 | `TFS.SORT.CODE` | `TellerFinancialServices_SortCode` |  |  |  |
| 50 | `TFS.CHEQUE.NUMBER` | `TellerFinancialServices_ChequeNumber` |  |  |  |
| 51 | `TFS.CHEQUE.ACCT.NO` | `TellerFinancialServices_ChequeAcctNo` |  |  |  |
| 52 | `TFS.CHQ.TYPE` | `TellerFinancialServices_ChqType` |  |  |  |
| 53 | `TFS.SPLIT.DATE` | `TellerFinancialServices_SplitDate` |  |  |  |
| 54 | `TFS.SPLIT.AMT` | `TellerFinancialServices_SplitAmt` |  |  |  |
| 55 | `TFS.CR.EXP.DATE` | `TellerFinancialServices_CrExpDate` |  |  |  |
| 56 | `TFS.DR.EXP.DATE` | `TellerFinancialServices_DrExpDate` |  |  |  |
| 57 | `TFS.CR.DENOM` | `TellerFinancialServices_CrDenom` |  |  |  |
| 58 | `TFS.CR.AVAIL` | `TellerFinancialServices_CrAvail` |  |  |  |
| 59 | `TFS.CR.DEN.UNIT` | `TellerFinancialServices_CrDenUnit` |  |  |  |
| 60 | `TFS.CR.SERIAL.NO` | `TellerFinancialServices_CrSerialNo` |  |  |  |
| 61 | `TFS.DR.DENOM` | `TellerFinancialServices_DrDenom` |  |  |  |
| 62 | `TFS.DR.AVAIL` | `TellerFinancialServices_DrAvail` |  |  |  |
| 63 | `TFS.DR.DEN.UNIT` | `TellerFinancialServices_DrDenUnit` |  |  |  |
| 64 | `TFS.DR.SERIAL.NO` | `TellerFinancialServices_DrSerialNo` |  |  |  |
| 65 | `TFS.OUR.REFERENCE` | `TellerFinancialServices_OurReference` |  |  |  |
| 66 | `TFS.NARRATIVE` | `TellerFinancialServices_Narrative` |  |  |  |
| 67 | `TFS.PAYMENT.DETS` | `TellerFinancialServices_PaymentDets` |  |  |  |
| 68 | `TFS.DC.PROD.CATEG` | `TellerFinancialServices_DcProdCateg` |  |  |  |
| 69 | `TFS.DC.CUSTOMER.NO` | `TellerFinancialServices_DcCustomerNo` |  |  |  |
| 70 | `TFS.DC.ACCT.OFFICER` | `TellerFinancialServices_DcAcctOfficer` |  |  |  |
| 71 | `TFS.DC.REVERSE.MARK` | `TellerFinancialServices_DcReverseMark` |  |  |  |
| 72 | `TFS.CARD.NUMBER` | `TellerFinancialServices_CardNumber` |  |  |  |
| 73 | `TFS.CARD.DETAILS` | `TellerFinancialServices_CardDetails` |  |  |  |
| 74 | `TFS.DR.CURR.MKT` | `TellerFinancialServices_DrCurrMkt` |  |  |  |
| 75 | `TFS.CR.CURR.MKT` | `TellerFinancialServices_CrCurrMkt` |  |  |  |
| 76 | `TFS.UNDERLYING` | `TellerFinancialServices_Underlying` |  |  |  |
| 77 | `TFS.RESERVED.77` | `TellerFinancialServices_UlStatus` |  |  |  |
| 78 | `TFS.UL.STMT.NO` | `TellerFinancialServices_UlStmtNo` |  |  |  |
| 79 | `TFS.RESERVED.79` | `TellerFinancialServices_Reserved79` |  |  |  |
| 80 | `TFS.RESERVED.80` | `TellerFinancialServices_Reserved80` |  |  |  |
| 81 | `TFS.R.UNDERLYING` | `TellerFinancialServices_RUnderlying` |  |  |  |
| 82 | `TFS.R.UL.STMT.NO` | `TellerFinancialServices_RUlStmtNo` |  |  |  |
| 83 | `TFS.RESERVED.83` | `TellerFinancialServices_RUlStatus` |  |  |  |
| 84 | `TFS.UL.COMPANY` | `TellerFinancialServices_UlCompany` |  |  |  |
| 85 | `TFS.LOCK.REF` | `TellerFinancialServices_LockRef` |  |  |  |
| 86 | `TFS.CONSOL.LEG` | `TellerFinancialServices_ConsolLeg` |  |  |  |
| 87 | `TFS.VAL.ERROR` | `TellerFinancialServices_ValError` |  |  |  |
| 88 | `TFS.REVERSAL.MARK` | `TellerFinancialServices_ReversalMark` |  |  |  |
| 89 | `TFS.CONSOLIDATE.NOW` | `TellerFinancialServices_ConsolidateNow` | TField | Yes | This field is used only when Consolidation is enabled. From a transaction processing perspective, this field marks the end of the user capturing all the information provided by the customer for a TFS transaction. By setting this field to YES, the user indicates that all information has been captured and essentially instructs the system to consolidate the legs. By setting this field to NO, the user instructs the system to Undo the consolidation. By setting this field to REVERSE, the user instructs the system to mark all the legs of that TFS Transaction, for reversal. Validation Rules: = Mandatory Input of YES required when Consolidation is enabled. Input not allowed if Consolidation is disabled (field CONSOL.INSTRUCTION set to NO) |
| 90 | `TFS.AML.CUSTOMER.NO` | `TellerFinancialServices_AmlCustomerNo` | TField | No | This field is part of the AML details captured as part of a TFS Transaction. If the TFS transaction is being done for an existing T24 customer, then the customer number can be keyed in here. This can also be different from the Primary Customer (where this customer is doing transactions on behalf of the Primary Customer) Validation Rules: ================= Optional Input. Input must be key to a valid record in CUSTOMER table. If the field AML.DETAILS in TFS.PARAMETER is set to VALIDATION, When this field is left blank and if Primary Customer has been input, then this field will automatically be defaulted with that value and an Override will be raised to that effect. |
| 91 | `TFS.AML.NAME` | `TellerFinancialServices_AmlName` |  |  |  |
| 92 | `TFS.AML.ADDRESS` | `TellerFinancialServices_AmlAddress` |  |  |  |
| 93 | `TFS.AML.NATIONALITY` | `TellerFinancialServices_AmlNationality` | TField | No | This field is part of the AML details captured as part of a TFS Transaction. It holds the nationality of the walk-in customer. Validation Rules: ================= Optional Input. Input not allowed when AML.CUSTOMER.NO has been keyed in with a valid T24 Customer Number. |
| 94 | `TFS.LEGAL.ID` | `TellerFinancialServices_LegalId` |  |  |  |
| 95 | `TFS.LEGAL.DOC.NAME` | `TellerFinancialServices_LegalDocName` |  |  |  |
| 96 | `TFS.LEGAL.HOLDER.NAME` | `TellerFinancialServices_LegalHolderName` |  |  |  |
| 97 | `TFS.LEGAL.ISS.AUTH` | `TellerFinancialServices_LegalIssAuth` |  |  |  |
| 98 | `TFS.LEGAL.ISS.DATE` | `TellerFinancialServices_LegalIssDate` |  |  |  |
| 99 | `TFS.LEGAL.EXP.DATE` | `TellerFinancialServices_LegalExpDate` |  |  |  |
| 100 | `TFS.COMM.TYPE` | `TellerFinancialServices_CommType` |  |  |  |
| 101 | `TFS.COMM.REFERENCE` | `TellerFinancialServices_CommReference` |  |  |  |
| 102 | `TFS.RT.ACCOUNT.NO` | `TellerFinancialServices_RtAccountNo` |  |  |  |
| 103 | `TFS.RUNNING.TOTAL` | `TellerFinancialServices_RunningTotal` |  |  |  |
| 104 | `TFS.MKT.EXCH.PROFIT` | `TellerFinancialServices_MktExchProfit` | TField |  | Total Market exchange calculated on all TFS legs. This has no significance other than to present the value to the user on the screen. Validation Rules: Noinput field. Defaulted by the system. |
| 105 | `TFS.UL.OFS.MSGS` | `TellerFinancialServices_UlOfsMsgs` |  |  |  |
| 106 | `TFS.RESERVED.106` | `TellerFinancialServices_Reserved106` | TField |  |  |
| 107 | `TFS.RESERVED.107` | `TellerFinancialServices_Reserved107` | TField |  |  |
| 108 | `TFS.RESERVED.108` | `TellerFinancialServices_Reserved108` | TField |  |  |
| 109 | `TFS.RESERVED.109` | `TellerFinancialServices_Reserved109` | TField |  |  |
| 110 | `TFS.RESERVED.110` | `TellerFinancialServices_Reserved110` | TField |  |  |
| 111 | `TFS.RESERVED.111` | `TellerFinancialServices_Reserved111` | TField |  |  |
| 112 | `TFS.RESERVED.112` | `TellerFinancialServices_Reserved112` | TField |  |  |
| 113 | `TFS.RESERVED.113` | `TellerFinancialServices_Reserved113` | TField |  |  |
| 114 | `TFS.RESERVED.114` | `TellerFinancialServices_Reserved114` | TField |  |  |
| 115 | `TFS.RESERVED.115` | `TellerFinancialServices_Reserved115` | TField |  |  |
| 116 | `TFS.LOCAL.REF` | `TellerFinancialServices_LocalRef` |  |  |  |
| 117 | `TFS.OVERRIDE` | `TellerFinancialServices_Override` |  |  |  |
| 118 | `TFS.RECORD.STATUS` | `TellerFinancialServices_RecordStatus` | String |  |  |
| 119 | `TFS.CURR.NO` | `TellerFinancialServices_CurrNo` | String |  |  |
| 120 | `TFS.INPUTTER` | `TellerFinancialServices_Inputter` |  |  |  |
| 121 | `TFS.DATE.TIME` | `TellerFinancialServices_DateTime` |  |  |  |
| 122 | `TFS.AUTHORISER` | `TellerFinancialServices_Authoriser` | String |  |  |
| 123 | `TFS.CO.CODE` | `TellerFinancialServices_CoCode` | String |  |  |
| 124 | `TFS.DEPT.CODE` | `TellerFinancialServices_DeptCode` | String |  |  |
| 125 | `TFS.AUDITOR.CODE` | `TellerFinancialServices_AuditorCode` | String |  |  |
| 126 | `TFS.AUDIT.DATE.TIME` | `TellerFinancialServices_AuditDateTime` | String |  |  |
