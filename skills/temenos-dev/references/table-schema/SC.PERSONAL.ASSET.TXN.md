# SC.PERSONAL.ASSET.TXN — Table Schema

> Source: `INSERTS/I_F.SC.PERSONAL.ASSET.TXN` in `SC_SctOtherAssets.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PATXN.SECURITY.MASTER.ID` | `ScPersonalAssetTxn_SecurityMasterId` | TField | Yes | This field holds SM id of underliying asset. Incase of EXTERNAL.ASSET deal type user inputted, for PERSONAL.ASSET sytem generated. Validation Rules: Should be a valid SECURITY.MASTER record. Mandatory input for EXTERNAL.ASSET deal type. No input for PEROSNAL.ASSET. |
| 2 | `SC.PATXN.PORTFOLIO.ID` | `ScPersonalAssetTxn_PortfolioId` | TField | Yes | Holds the SEC.ACC.MASTER id, for which the transaction should be made. This will be mapped to portfolio field in underlying security transfer created. Validation Rules: Should be a valid SEC.ACC.MASTER record. Mandatory input. Change is not allowed. |
| 3 | `SC.PATXN.PORTFOLIO.NAME` | `ScPersonalAssetTxn_PortfolioName` | TField |  | This field carries the name of the portfolio. Information purpose only. If not inputted system defaults form portoflio name field in SEC.ACC.MASTER. Free text field holds upto 35 char. |
| 4 | `SC.PATXN.INVESTOR.CODE` | `ScPersonalAssetTxn_InvestorCode` | TField |  |  |
| 5 | `SC.PATXN.PERSONAL.ASSET.TYPE` | `ScPersonalAssetTxn_PersonalAssetType` | TField | Yes | Field to attach the asset type for the transaction. This record has asset level information. Validation Rules: Input mandatory for deal type PERSONAL.ASSET. Change not allowed. A valid SC.PERSONAL.ASSET.TYPE record. |
| 6 | `SC.PATXN.ASSET.CURRENCY` | `ScPersonalAssetTxn_AssetCurrency` | TField |  |  |
| 7 | `SC.PATXN.ASSET.CATEGORY` | `ScPersonalAssetTxn_AssetCategory` | TField |  | Holds the category of the asset being created. Defaulted form ASSET.TYPE field in SC.PERSONAL.ASSET.TYPE record attached. Validation Rules: No input field. |
| 8 | `SC.PATXN.ASSET.DESCRIPTION` | `ScPersonalAssetTxn_AssetDescription` | TField | Yes | Description for the asset. Mapped to DESCRIPTION and SHORT.NAME field in SM. Validation Rules: Mandatory field. Allows upto 35 char. Change not allowed. |
| 9 | `SC.PATXN.ASSET.DOMICILE` | `ScPersonalAssetTxn_AssetDomicile` | TField |  | Holds the country of asset. Mapped to asset domicile. Validation Rules: Should be a valid COUNTRY record. Change not allowed. |
| 10 | `SC.PATXN.INSTITUTION` | `ScPersonalAssetTxn_Institution` | TField |  | Hold the name of the institution. Mapped to COMPANY.NAME field in SECURITY.MASTER Validation Rules: Free text field holds upto 35 char. |
| 11 | `SC.PATXN.REGISTERED.HOLDING` | `ScPersonalAssetTxn_RegisteredHolding` | TField |  | Displays the holding details. LOOKUP field, with set of predefined values. Possible Rules: CLIENT.CONTROLLED.INC,CLIENT.CONTROLLED.NO.INC,DEALER.CONTROLLED,MONITOR.ONLY.NO.INC,NOMINEE,THIRD.PARTY.INC,THIRD.PARTY.NO.IN |
| 12 | `SC.PATXN.DISPOSAL.TAX.TREATMENT` | `ScPersonalAssetTxn_DisposalTaxTreatment` | TField |  | This field contains disposal treatment method for the asset. Defaulted from DISPOSAL.TAX.TREATEMENT field in SC.PERSONAL.ASSET.TYPE record. Validation Rules: Input not allowed. |
| 13 | `SC.PATXN.TRADE.RESTRICTION` | `ScPersonalAssetTxn_TradeRestriction` | TField |  | Field to restrict any debit or credit type of transaction at any stage. Used along with INITIAL.UPDATE type of txn. Can be uncheck at any stage of txn. Validation Rules: YES or blank field. Allowed only when txn type is INITIAL.UPDATE. |
| 14 | `SC.PATXN.PRICE` | `ScPersonalAssetTxn_Price` | TField |  | This field holds the price for the asset. It is mapped to LAST.PRICE field in SM. This is used with INITIAL.UPDATEtype of txn for doing price update activity. If PRICE is not updated untill any credit txn, then system will update price using TRANSACTION.AMOUNTand QUANTITY field details. Validation Rules: Numeric field with PRICE validation. |
| 15 | `SC.PATXN.PRICE.EFFECTIVE.DATE` | `ScPersonalAssetTxn_PriceEffectiveDate` | TField |  |  |
| 16 | `SC.PATXN.INCOME.FREQUENCY` | `ScPersonalAssetTxn_IncomeFrequency` | TField |  | Frequency field to record the income frequency. Validation Rules: T24 frequency format. |
| 17 | `SC.PATXN.TRANSACTION.TYPE` | `ScPersonalAssetTxn_TransactionType` | TField |  | This field defines the type of transaction for the deal. Validation Rules: First transaction for PERSONAL.ASSET deal should be INITIAL.UPDATE whichcreates the asset first. For EXTERNAL.ASSET INITIAL.UPDATE is not allowed. Second transaction should be any credit transaction BUY or WRITE.IN. Final transction should be debit transaction SALE or WRITE.OUT or MATURITY If MULTIPLE.LOTS is set in SC.PERSONAL.ASSET.TYPE, then any number of credit or debit is allowed. If not then one credit and debit txn is possible. INS.BOND.CONTRIBUTION and INS.BOND.WITHDRAWAL is allowed only when DISPOSAL.TAX.TREATMENT in SC.PERSONAL.ASSET.TYPE is SPECIAL. To update only price of the asset PRICE.UPDATE type of transaction is used. Can be used anytime after initial update. For amending any previous transaction AMEND.TXN type is used along with id of transaction to be amended. Can happen any time after a SECURITY.TRANSFER record id created. |
| 18 | `SC.PATXN.TRANSACTION.AMOUNT` | `ScPersonalAssetTxn_TransactionAmount` | TField |  |  |
| 19 | `SC.PATXN.QUANTITY` | `ScPersonalAssetTxn_Quantity` | TField |  | Hold the qunaity of nominal to be debited or credited. For credit transaction if no input is provided system will default to '1' For debit transaction if MULTIPLE.LOTS is not set then, it should be same as credit transaction. For INS.BOND.WITHDRAWAL if FULL.WITHDRAWAL is set then sytem will default remaining quantity. Validation Rules: For non MULTIPLE.LOTS transaction debit and credit qunaity should always be same. Except for insurance type of transactions. |
| 20 | `SC.PATXN.TRANSACTION.DATE` | `ScPersonalAssetTxn_TransactionDate` | TField |  | This field holds date of transaction. If not inputted defaults to today date. This field is mapped to TRADE.DATE field in SECURITY.TRANSFER. Validation Rules: Valid T24 DATE format. No input for INITIAL.UPDATE. |
| 21 | `SC.PATXN.TERM` | `ScPersonalAssetTxn_Term` | TField |  | Holds the term of the transaction. Validation Rules: Should be in the form of xxZ. Where xx refers to any numbers, Z refers to 'D' - for Days 'M' - for Month 'W' - for Week 'Y' - for Year |
| 22 | `SC.PATXN.MATURITY.DATE` | `ScPersonalAssetTxn_MaturityDate` | TField |  |  |
| 23 | `SC.PATXN.SETTLEMENT.DATE` | `ScPersonalAssetTxn_SettlementDate` | TField |  | This field holds the settlement date of transaction. Which is defaulted to TRANSACTION.DATE. Which is mapped to VALUE.DATE fieldin SECURITY.TRANSFER. Validation Rules: Valid T24 DATE format. Can not be greater than TRANSACTION.DATE. No input for INITIAL.UPDATE |
| 24 | `SC.PATXN.ACQUISITION.DATE` | `ScPersonalAssetTxn_AcquisitionDate` | TField |  | This field holds the date of acquisiton of the asset. This field is mapped to TRFR.EFF.DATE field in SECURITY.TRASNFER. If not inputted TRANSACTION.DATE is defaulted. Validation Rules: Valid T24 DATE format. Input allowed only for the credit transaction. |
| 25 | `SC.PATXN.TAX.EFFECTIVE.DATE` | `ScPersonalAssetTxn_TaxEffectiveDate` | TField |  | This field holds the tax effective date of the transaction. This field is mapped to CGTAX.EFF.DATE field in SECURITY.TRANSFER. Validation Rules: Valid T24 DATE format. Date can not be less than ACQUISITION.DATE. Input not allowed for INITIAL.UPDATE |
| 26 | `SC.PATXN.RATE` | `ScPersonalAssetTxn_Rate` | TField |  | This field denotes the fixed rate of income for the asset. Information purpose. Validation Rules: Input must be in T24 AMT format. |
| 27 | `SC.PATXN.DUE.DATE` | `ScPersonalAssetTxn_DueDate` | TField |  | This field holds the due date of the asset. Validation Rules: Valid T24 DATE format. |
| 28 | `SC.PATXN.TXN.EXPENSES` | `ScPersonalAssetTxn_TxnExpenses` | TField |  | Field to record expenses of the transaction. This is used to calculate NET.TRANSACTION amount. Validation Rules: Input must be in T24 AMT format. |
| 29 | `SC.PATXN.GST` | `ScPersonalAssetTxn_Gst` | TField |  | Field to record the GST applied on the transaction. Validation Rules: Input must be in T24 AMT format. |
| 30 | `SC.PATXN.INTEREST.AMT` | `ScPersonalAssetTxn_InterestAmt` | TField |  | Filed to record the interest amt for the given transaction. Validation Rules: Input must be in T24 AMT format. |
| 31 | `SC.PATXN.NET.TRANSACTION.AMOUNT` | `ScPersonalAssetTxn_NetTransactionAmount` | TField |  | This field holds the net amount for a transaction. This field is calulated by negating GST, INTEREST.AMT, TXN.EXPENSES from TRANSACTION.AMOUNT Validation Rules: Input must be in T24 AMT format. |
| 32 | `SC.PATXN.REDUCED.COST` | `ScPersonalAssetTxn_ReducedCost` | TField |  | This field holds the reduced cost of the asset. If not inputted defaults to NET.TRANSACTION.AMOUNT. Validation Rules: Input must be in T24 AMT format. |
| 33 | `SC.PATXN.INDEXED.COST` | `ScPersonalAssetTxn_IndexedCost` | TField |  | This field holds the indexed cost of the asset. If not inputted defaults to NET.TRANSACTION.AMOUNT. Validation Rules: Input must be in T24 AMT format. |
| 34 | `SC.PATXN.CG.EXEMPT` | `ScPersonalAssetTxn_CgExempt` | TField |  | This field denotes if CG need to be calculated for the asset during debit transaction. For PERSONAL.ASSET.TYPEwhose DISPOSAL.TAX.TREATMENT is CG.EXEMPT If CG.EXEMPT.VALUE is provided in SC.PERSONAL.ASSET.TYPE then if CG.VALUE.LCY is less than that this field is set to YES. This field will be mapped to CG.EXEMPT field in SECURITY.TRANSFER. Validation Rules: YES or blank field. Exempt is not allowed for PERSONAL.ASSET.TYPE whose DISPOSAL.TAX.TREATMENT is REVENUE. Can not be set to YES for LIABILITY txn. |
| 35 | `SC.PATXN.CG.EXEMPT.REASON` | `ScPersonalAssetTxn_CgExemptReason` |  |  |  |
| 36 | `SC.PATXN.SERVICE.REQUEST.ID` | `ScPersonalAssetTxn_ServiceRequestId` | TField |  | This field holds the service request id of the transaction. Validation Rules: Free text field carry upto 35 char. |
| 37 | `SC.PATXN.NARRATIVE` | `ScPersonalAssetTxn_Narrative` |  |  |  |
| 38 | `SC.PATXN.PAYMENT.REQUIRED` | `ScPersonalAssetTxn_PaymentRequired` | TField |  | This field is to denote the payment requirement for the transaction. Validation Rules: YES or blank field. Input allowed only for debit transaction. |
| 39 | `SC.PATXN.AUTO.PAY` | `ScPersonalAssetTxn_AutoPay` | TField |  | This field denotes the payment type of transaction.If set to YES, DELIVERY.INSTR field in SECURITY.TRANSRER is set to dap code set in SC.STD.SEC.TRADE. Validation Rules: YES or blank field. Input allowed only for debit type of transaction. |
| 40 | `SC.PATXN.ACCOUNT.NUMBER` | `ScPersonalAssetTxn_AccountNumber` | TField |  | This field holds the customer account number used for the transaction. Incase of deal type PERSONAL.ASSET this account will bemapped to CU.ACCOUNT.NUMBER field in SECURITY.TRANSFER. Validation Rules: A valid record in ACCOUNT table. |
| 41 | `SC.PATXN.PAYMENT.METHOD` | `ScPersonalAssetTxn_PaymentMethod` | TField |  | This field denotes the method of payment for the transaction. Information purpose only. Validation Rules: Input allowed only for debit type of transaction. Free text field holds upto 35 char. |
| 42 | `SC.PATXN.BANK` | `ScPersonalAssetTxn_Bank` | TField |  | This field shows the detail of bank involved in the transaction. Validation Rules: Input allowed only for debit type of transaction. Free text field holds upto 35 char. |
| 43 | `SC.PATXN.EXT.ACCOUNT.NO` | `ScPersonalAssetTxn_ExtAccountNo` | TField |  | This field holds the details of external account used for the transaction. Validation Rules: Input allowed only for debit type of transaction. Free text field holds upto 35 char. |
| 44 | `SC.PATXN.EXT.ACCOUNT.NAME` | `ScPersonalAssetTxn_ExtAccountName` | TField |  | Name of the external account used for the transaction. Validation Rules: Input allowed only for debit type of transaction. Free text field holds upto 35 char. |
| 45 | `SC.PATXN.PAYEE.NARRATIVE` | `ScPersonalAssetTxn_PayeeNarrative` | TField |  | This field holds the narrative of the payee. Information purpose only. Validation Rules: Input allowed only for debit type of transaction. Free text field holds upto 35 char. |
| 46 | `SC.PATXN.STATEMENT.NARRATIVE` | `ScPersonalAssetTxn_StatementNarrative` | TField |  | This field hold the statement narrative. Information purpose only. Validation Rules: Input allowed only for debit type of transaction. Free text field holds upto 35 char. |
| 47 | `SC.PATXN.DATE.RESET.REQD` | `ScPersonalAssetTxn_DateResetReqd` | TField |  | This filed is used to show if date reset is requied for the transaction. If set to YES it will update theACQUISITION.DATE field with date in RESET.DATE. If RESET.DATE is blank default with today date. Validation Rules: YES or blank field. Input allowed only for INS.BOND.CONTRIBUTION and INS.BOND.WITHDRAWAL transaction. |
| 48 | `SC.PATXN.RESET.DATE` | `ScPersonalAssetTxn_ResetDate` | TField |  | This field holds the date to be used for acquisition of INSURANCE.BOND. Works along with DATE.RESET.REQD field. Validation Rules: A valid T24 date field. Input allowed only for INS.BOND.CONTRIBUTION and INS.BOND.WITHDRAWAL transaction. |
| 49 | `SC.PATXN.FULL.WITHDRAWAL` | `ScPersonalAssetTxn_FullWithdrawal` | TField |  | This field shows if, INS.BOND.WITHDRAWAL transaction is to be done for all the remaining quanity. If set to YES systme withdefaults the remaining qunaity in QUANTITY field. Validation Rules: YES or blank field. Input allowed only for INS.BOND.WITHDRAWAL transaction. |
| 50 | `SC.PATXN.BOND.BONUS` | `ScPersonalAssetTxn_BondBonus` | TField | Yes | This field holds the bonus amount allowed for INS.BOND.WITHDRAWAL transaction. Validation Rules: Input mandatory and allowed for INS.BOND.WITHDRAWAL transaction. |
| 51 | `SC.PATXN.EXEMPT.BONUS` | `ScPersonalAssetTxn_ExemptBonus` | TField |  | This field will define if bonus is to be exempted or not. If set to YES, then BOND.FACTOR is modified to '0' Validation Rules: YES or blank field. Input allowed only for INS.BOND.WITHDRAWAL transaction. |
| 52 | `SC.PATXN.EXEMPT.REASON` | `ScPersonalAssetTxn_ExemptReason` | TField |  | This filed shows the description of reason for exemption. Validation Rules: Free text field holds upto 35 char. Input allowed only for INS.BOND.WITHDRAWAL transaction. |
| 53 | `SC.PATXN.BOND.FACTOR` | `ScPersonalAssetTxn_BondFactor` | TField |  | This field holds the factor for BOND.BONUS. for which CG is calculated. If the withdrawal happen with in 8 years, factor '1' is defaulted. Between 8 and 9 years '2/3' Between 9 and 10 years '1/3' Greater than 10 years '1' Validation Rules: Input allowed only for INS.BOND.WITHDRAWAL transaction. Dropdown field has '0', '1/3' , '2/3' , '1' values. |
| 54 | `SC.PATXN.SAVE.TRANSACTION.TYPE` | `ScPersonalAssetTxn_SaveTransactionType` |  |  |  |
| 55 | `SC.PATXN.SAVE.TRANSACTION.AMOUNT` | `ScPersonalAssetTxn_SaveTransactionAmount` |  |  |  |
| 56 | `SC.PATXN.SAVE.QUANTITY` | `ScPersonalAssetTxn_SaveQuantity` |  |  |  |
| 57 | `SC.PATXN.SAVE.TRANSACTION.DATE` | `ScPersonalAssetTxn_SaveTransactionDate` |  |  |  |
| 58 | `SC.PATXN.SAVE.TERM` | `ScPersonalAssetTxn_SaveTerm` |  |  |  |
| 59 | `SC.PATXN.SAVE.MATURITY.DATE` | `ScPersonalAssetTxn_SaveMaturityDate` |  |  |  |
| 60 | `SC.PATXN.SAVE.SETTLEMENT.DATE` | `ScPersonalAssetTxn_SaveSettlementDate` |  |  |  |
| 61 | `SC.PATXN.SAVE.ACQUISITION.DATE` | `ScPersonalAssetTxn_SaveAcquisitionDate` |  |  |  |
| 62 | `SC.PATXN.SAVE.TAX.EFFECTIVE.DATE` | `ScPersonalAssetTxn_SaveTaxEffectiveDate` |  |  |  |
| 63 | `SC.PATXN.SAVE.RATE` | `ScPersonalAssetTxn_SaveRate` |  |  |  |
| 64 | `SC.PATXN.SAVE.DUE.DATE` | `ScPersonalAssetTxn_SaveDueDate` |  |  |  |
| 65 | `SC.PATXN.SAVE.TXN.EXPENSES` | `ScPersonalAssetTxn_SaveTxnExpenses` |  |  |  |
| 66 | `SC.PATXN.SAVE.GST` | `ScPersonalAssetTxn_SaveGst` |  |  |  |
| 67 | `SC.PATXN.SAVE.INTEREST.AMT` | `ScPersonalAssetTxn_SaveInterestAmt` |  |  |  |
| 68 | `SC.PATXN.SAVE.NET.TRANSACTION.AMOUNT` | `ScPersonalAssetTxn_SaveNetTransactionAmount` |  |  |  |
| 69 | `SC.PATXN.SAVE.REDUCED.COST` | `ScPersonalAssetTxn_SaveReducedCost` |  |  |  |
| 70 | `SC.PATXN.SAVE.INDEXED.COST` | `ScPersonalAssetTxn_SaveIndexedCost` |  |  |  |
| 71 | `SC.PATXN.SAVE.CG.EXEMPT` | `ScPersonalAssetTxn_SaveCgExempt` |  |  |  |
| 72 | `SC.PATXN.SAVE.CG.EXEMPT.REASON` | `ScPersonalAssetTxn_SaveCgExemptReason` |  |  |  |
| 73 | `SC.PATXN.SAVE.SERVICE.REQUEST.ID` | `ScPersonalAssetTxn_SaveServiceRequestId` |  |  |  |
| 74 | `SC.PATXN.SAVE.NARRATIVE` | `ScPersonalAssetTxn_SaveNarrative` |  |  |  |
| 75 | `SC.PATXN.SAVE.PAYMENT.REQUIRED` | `ScPersonalAssetTxn_SavePaymentRequired` |  |  |  |
| 76 | `SC.PATXN.SAVE.AUTO.PAY` | `ScPersonalAssetTxn_SaveAutoPay` |  |  |  |
| 77 | `SC.PATXN.SAVE.ACCOUNT.NUMBER` | `ScPersonalAssetTxn_SaveAccountNumber` |  |  |  |
| 78 | `SC.PATXN.SAVE.PAYMENT.METHOD` | `ScPersonalAssetTxn_SavePaymentMethod` |  |  |  |
| 79 | `SC.PATXN.SAVE.BANK` | `ScPersonalAssetTxn_SaveBank` |  |  |  |
| 80 | `SC.PATXN.SAVE.EXT.ACCOUNT.NO` | `ScPersonalAssetTxn_SaveExtAccountNo` |  |  |  |
| 81 | `SC.PATXN.SAVE.EXT.ACCOUNT.NAME` | `ScPersonalAssetTxn_SaveExtAccountName` |  |  |  |
| 82 | `SC.PATXN.SAVE.PAYEE.NARRATIVE` | `ScPersonalAssetTxn_SavePayeeNarrative` |  |  |  |
| 83 | `SC.PATXN.SAVE.STATEMENT.NARRATIVE` | `ScPersonalAssetTxn_SaveStatementNarrative` |  |  |  |
| 84 | `SC.PATXN.SAVE.DATE.RESET.REQD` | `ScPersonalAssetTxn_SaveDateResetReqd` |  |  |  |
| 85 | `SC.PATXN.SAVE.RESET.DATE` | `ScPersonalAssetTxn_SaveResetDate` |  |  |  |
| 86 | `SC.PATXN.SAVE.FULL.WITHDRAWAL` | `ScPersonalAssetTxn_SaveFullWithdrawal` |  |  |  |
| 87 | `SC.PATXN.SAVE.BOND.BONUS` | `ScPersonalAssetTxn_SaveBondBonus` |  |  |  |
| 88 | `SC.PATXN.SAVE.EXEMPT.BONUS` | `ScPersonalAssetTxn_SaveExemptBonus` |  |  |  |
| 89 | `SC.PATXN.SAVE.EXEMPT.REASON` | `ScPersonalAssetTxn_SaveExemptReason` |  |  |  |
| 90 | `SC.PATXN.SAVE.BOND.FACTOR` | `ScPersonalAssetTxn_SaveBondFactor` |  |  |  |
| 91 | `SC.PATXN.APPLICATION.UPDATED` | `ScPersonalAssetTxn_ApplicationUpdated` |  |  |  |
| 92 | `SC.PATXN.APP.TXN.ID` | `ScPersonalAssetTxn_AppTxnId` |  |  |  |
| 93 | `SC.PATXN.TOTAL.QUANTITY` | `ScPersonalAssetTxn_TotalQuantity` | TField |  | This field displays the current total nominal at the time for the transaction. Validation Rules: No input fields. |
| 94 | `SC.PATXN.EXT.CUSTODIAN` | `ScPersonalAssetTxn_ExtCustodian` | TField | Yes | This field holds external custodian detail of transaction for EXTERNAL.ASSET deal. Validation Rules: A valid customer Record. CUSTOMER.TYPE should be DESPOSITORY. Input mandatory for EXTERNAL.ASSET |
| 95 | `SC.PATXN.GRP.DEPT.CODE` | `ScPersonalAssetTxn_GrpDeptCode` |  |  |  |
| 96 | `SC.PATXN.CG.VALUE` | `ScPersonalAssetTxn_CgValue` | TField |  | This field holds the value of credit transaction for which CG need to be calculated. CG.VALUE is defined in asset currency User can overwrite this value. Validation Rules: T24 amount field. |
| 97 | `SC.PATXN.CG.EXCH.RATE` | `ScPersonalAssetTxn_CgExchRate` | TField |  | Holds the exchange rate used for calculating CG.VALUE.LCY Validation Rules: T24 rate field. |
| 98 | `SC.PATXN.CG.VALUE.LCY` | `ScPersonalAssetTxn_CgValueLcy` | TField |  | This field holds the value of CG in local currency. Validation Rules: Input not allowed. T24 amount field. |
| 99 | `SC.PATXN.RESERVED.9` | `ScPersonalAssetTxn_Reserved9` | TField |  |  |
| 100 | `SC.PATXN.RESERVED.8` | `ScPersonalAssetTxn_Reserved8` | TField |  |  |
| 101 | `SC.PATXN.RESERVED.7` | `ScPersonalAssetTxn_Reserved7` | TField |  |  |
| 102 | `SC.PATXN.RESERVED.6` | `ScPersonalAssetTxn_Reserved6` | TField |  |  |
| 103 | `SC.PATXN.RESERVED.5` | `ScPersonalAssetTxn_Reserved5` | TField |  |  |
| 104 | `SC.PATXN.RESERVED.4` | `ScPersonalAssetTxn_Reserved4` | TField |  |  |
| 105 | `SC.PATXN.RESERVED.3` | `ScPersonalAssetTxn_Reserved3` | TField |  |  |
| 106 | `SC.PATXN.RESERVED.2` | `ScPersonalAssetTxn_Reserved2` | TField |  |  |
| 107 | `SC.PATXN.RESERVED.1` | `ScPersonalAssetTxn_Reserved1` | TField |  |  |
| 108 | `SC.PATXN.LOCAL.REF` | `ScPersonalAssetTxn_LocalRef` |  |  |  |
| 109 | `SC.PATXN.STMT.NOS` | `ScPersonalAssetTxn_StmtNos` |  |  |  |
| 110 | `SC.PATXN.OVERRIDE` | `ScPersonalAssetTxn_Override` |  |  |  |
| 111 | `SC.PATXN.RECORD.STATUS` | `ScPersonalAssetTxn_RecordStatus` | String |  |  |
| 112 | `SC.PATXN.CURR.NO` | `ScPersonalAssetTxn_CurrNo` | String |  |  |
| 113 | `SC.PATXN.INPUTTER` | `ScPersonalAssetTxn_Inputter` |  |  |  |
| 114 | `SC.PATXN.DATE.TIME` | `ScPersonalAssetTxn_DateTime` |  |  |  |
| 115 | `SC.PATXN.AUTHORISER` | `ScPersonalAssetTxn_Authoriser` | String |  |  |
| 116 | `SC.PATXN.CO.CODE` | `ScPersonalAssetTxn_CoCode` | String |  |  |
| 117 | `SC.PATXN.DEPT.CODE` | `ScPersonalAssetTxn_DeptCode` | String |  |  |
| 118 | `SC.PATXN.AUDITOR.CODE` | `ScPersonalAssetTxn_AuditorCode` | String |  |  |
| 119 | `SC.PATXN.AUDIT.DATE.TIME` | `ScPersonalAssetTxn_AuditDateTime` | String |  |  |
| 120 | `SC.PATXN.DEAL.TYPE` | `ScPersonalAssetTxn_DealType` | TField | Yes | This field is used to set deal type of transaction. If left blank sytem defaults to PERSONAL.ASSET deal type. Validation Rules: Mandatory input Possible values are: PERSONAL.ASSET - For internal type of transaction. EXTERNAL.ASSET - For external type of transaction. |
| 121 | `SC.PATXN.TRANSACTION.CODE` | `ScPersonalAssetTxn_TransactionCode` | TField |  | This field holds the transaction code to be used in SECURITY.TRANSFER for a given transaction. Validation Rules: No input field. Transaction code for all type of transaction need to be provided in SC.PERSONAL.ASSET.PARAM record. Seperate transaction type for both PERSONAL.ASSET and EXTERNAL.ASSET. For external asset trandaction code should be avilable in EXT.CR.CODE of SC.PARAMETER for credit txn and EXT.DB.CODE for debit txn. |
| 122 | `SC.PATXN.PRICE.SOURCE` | `ScPersonalAssetTxn_PriceSource` | TField |  | Field holds the price soruce for the asset. If not provided defaults from PRICE.SOURCE field in SC.PERSONALA.ASSET.PARAM record. PRICE.SOURCE is mapped to PRICE.UPDATE.CODE field in SM. Validation Rules: Shoulde a valid PRICE.UPDATE record. |
| 123 | `SC.PATXN.EXPENSE.TAX.TREATMENT` | `ScPersonalAssetTxn_ExpenseTaxTreatment` | TField |  | Expense tax treatment applicable for the asset. Defaults from EXPENSE.TAX.TREATMENT field in SC.PERSONAL.ASSET.TYPE record. Validation Rules: No input field |
| 124 | `SC.PATXN.INCOME.TAX.TREATMENT` | `ScPersonalAssetTxn_IncomeTaxTreatment` | TField |  | Income tax treatment applicable for this asset. Defaults from INCOME.TAX.TREATMENT field in SC.PERSONAL.ASSET.TYPE record. Validation Rules: No input field |
| 125 | `SC.PATXN.AMEND.TXN.ID` | `ScPersonalAssetTxn_AmendTxnId` | TField | Yes | Hold the id of SECURITY.TRANSFER created to to be amended. Validation Rules: Should be a SECURITY.TRANSFER created by the SC.PERSONAL.ASSET.TXN application. Mandatory for AMEND.TXN type. |
| 126 | `SC.PATXN.REVERSAL.IND` | `ScPersonalAssetTxn_ReversalInd` |  |  |  |
| 127 | `SC.PATXN.SAVE.TRANSACTION.CODE` | `ScPersonalAssetTxn_SaveTransactionCode` |  |  |  |
| 128 | `SC.PATXN.TAXLOT.ALLOCATE` | `ScPersonalAssetTxn_TaxlotAllocate` |  |  |  |
| 129 | `SC.PATXN.QTY.ALLOTED` | `ScPersonalAssetTxn_QtyAlloted` |  |  |  |
| 130 | `SC.PATXN.SAVE.TAXLOT.ALLOCATE` | `ScPersonalAssetTxn_SaveTaxlotAllocate` |  |  |  |
| 131 | `SC.PATXN.SAVE.QTY.ALLOTED` | `ScPersonalAssetTxn_SaveQtyAlloted` |  |  |  |
| 132 | `SC.PATXN.SAVE.TRANS.ID` | `ScPersonalAssetTxn_SaveTransId` |  |  |  |
