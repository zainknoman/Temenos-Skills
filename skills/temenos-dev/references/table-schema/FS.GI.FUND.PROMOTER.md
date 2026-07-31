# FS.GI.FUND.PROMOTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.PROMOTER` in `FS_FundPromoter.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.PROMOTER.PARENT.REF.ID` | `FsGiFundPromoter_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.PROMOTER.ORA.ROWID` | `FsGiFundPromoter_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.PROMOTER.EXTERNAL.ID` | `FsGiFundPromoter_ExternalId` | TField |  | External reference for the Fund Promoter. Multifonds DB Column is EXTERNAL_REF. |
| 4 | `FS.GI.FUND.PROMOTER.USE.TYPE` | `FsGiFundPromoter_UseType` | TField |  | Use type of the Fund Promoter. Multifonds DB Column is TYPE_USE. |
| 5 | `FS.GI.FUND.PROMOTER.FUND.PROMOTER.ID` | `FsGiFundPromoter_FundPromoterId` | TField |  | Fund Promoter internal ID. Multifonds DB Column is NPROMOTER. |
| 6 | `FS.GI.FUND.PROMOTER.FUND.PROMOTER.NAME` | `FsGiFundPromoter_FundPromoterName` | TField |  | Fund Promoter name. Multifonds DB Column is NPROMOTER_NAME. |
| 7 | `FS.GI.FUND.PROMOTER.LANGUAGE.CODE` | `FsGiFundPromoter_LanguageCode` | TField |  | Language code. Multifonds DB Column is CLANGUE. |
| 8 | `FS.GI.FUND.PROMOTER.ACCOUNT.HOLDER` | `FsGiFundPromoter_AccountHolder` | TField |  | Management company account holder. Multifonds DB Column is ACCOUNT_HOLDER. |
| 9 | `FS.GI.FUND.PROMOTER.CONTACT.PERSON.1` | `FsGiFundPromoter_ContactPerson1` | TField |  | Contact person 1 for Fund Promoter . Multifonds DB Column is CONTACT_PERSON1. |
| 10 | `FS.GI.FUND.PROMOTER.CONTACT.PERSON.2` | `FsGiFundPromoter_ContactPerson2` | TField |  | Contact person 2 for Fund Promoter. Multifonds DB Column is CONTACT_PERSON2. |
| 11 | `FS.GI.FUND.PROMOTER.ADDRESS.LINE.1` | `FsGiFundPromoter_AddressLine1` | TField |  | Address line 1. Multifonds DB Column is ADDRESSE_LINE1. |
| 12 | `FS.GI.FUND.PROMOTER.ADDRESS.LINE.2` | `FsGiFundPromoter_AddressLine2` | TField |  | Address line 2. Multifonds DB Column is ADDRESSE_LINE2. |
| 13 | `FS.GI.FUND.PROMOTER.ADDRESS.LINE.3` | `FsGiFundPromoter_AddressLine3` | TField |  | Address line 3. Multifonds DB Column is ADDRESSE_LINE3. |
| 14 | `FS.GI.FUND.PROMOTER.ADDRESS.LINE.4` | `FsGiFundPromoter_AddressLine4` | TField |  | Address line 4. Multifonds DB Column is ADDRESSE_LINE4. |
| 15 | `FS.GI.FUND.PROMOTER.POSTCODE` | `FsGiFundPromoter_Postcode` | TField |  | Post code of the address. Multifonds DB Column is CODE. |
| 16 | `FS.GI.FUND.PROMOTER.TOWN` | `FsGiFundPromoter_Town` | TField |  | City of the address. Multifonds DB Column is VILLE. |
| 17 | `FS.GI.FUND.PROMOTER.COUNTRY` | `FsGiFundPromoter_Country` | TField |  | Fund Promoter country (in 2 letter format eg &apos;LU&apos;). Multifonds DB Column is PAYS. |
| 18 | `FS.GI.FUND.PROMOTER.PHONE.NUMBER` | `FsGiFundPromoter_PhoneNumber` | TField |  | Telephone Number of the Fund Promoter. Multifonds DB Column is TEL_NO. |
| 19 | `FS.GI.FUND.PROMOTER.FOR.ATTENTION.OF.1` | `FsGiFundPromoter_ForAttentionOf1` | TField |  | Fax contact name 1 for the Fund Promoter. Multifonds DB Column is ATTENTION_OF1. |
| 20 | `FS.GI.FUND.PROMOTER.FAX.NUMBER.1` | `FsGiFundPromoter_FaxNumber1` | TField |  | Fax number 1 for the Fund Promoter. Multifonds DB Column is FAX_NO1. |
| 21 | `FS.GI.FUND.PROMOTER.FOR.ATTENTION.OF.2` | `FsGiFundPromoter_ForAttentionOf2` | TField |  | Fax contact name 2 for the Fund Promoter Multifonds DB Column is ATTENTION_OF2. |
| 22 | `FS.GI.FUND.PROMOTER.FAX.NUMBER.2` | `FsGiFundPromoter_FaxNumber2` | TField |  | Fax Number 2 for the Fund Promoter. Multifonds DB Column is FAX_NO2. |
| 23 | `FS.GI.FUND.PROMOTER.CORRESPONDANT.ID` | `FsGiFundPromoter_CorrespondantId` | TField |  | Correspondant Bank ID. Multifonds DB Column is NCORRESP. |
| 24 | `FS.GI.FUND.PROMOTER.BANK.ACCOUNT.NUMBER` | `FsGiFundPromoter_BankAccountNumber` | TField |  | Bank Account number. Multifonds DB Column is BANK_ACCOUNT. |
| 25 | `FS.GI.FUND.PROMOTER.BANK.ACCOUNT.TEXT` | `FsGiFundPromoter_BankAccountText` | TField |  | Free text to add information if any. Multifonds DB Column is BANK_ACCN_TEXT. |
| 26 | `FS.GI.FUND.PROMOTER.NOSTRO.ACCOUNT.ID` | `FsGiFundPromoter_NostroAccountId` | TField |  | Field allows to link the Fund Promotor to a NOSTRO account for payment by cheque functionality. Multifonds DB Column is NCORRESP_NOSTRO. |
| 27 | `FS.GI.FUND.PROMOTER.INTERNAL.ACCOUNT.NUMBER` | `FsGiFundPromoter_InternalAccountNumber` | TField |  | TA account number for fund supermarket module. Multifonds DB Column is INTERNAL_ACCOUNT. |
| 28 | `FS.GI.FUND.PROMOTER.TAX.NUMBER` | `FsGiFundPromoter_TaxNumber` | TField |  | Tax number for the Fund Promoter. Multifonds DB Column is TAXE_NO. |
| 29 | `FS.GI.FUND.PROMOTER.ROUNDING.DIFFERENCE` | `FsGiFundPromoter_RoundingDifference` | TField |  | The code to specify where the rounding difference can be allocated in case of multiple switches within the product. Multifonds DB Column is TYPE_RNDIFF. |
| 30 | `FS.GI.FUND.PROMOTER.CANCELLATION.TIMEFRAME` | `FsGiFundPromoter_CancellationTimeframe` | TField |  | Number of days in which an investor linked to the Fund Promoter can exercise his cancellation rights. Multifonds DB Column is NTIMEFRAME. |
| 31 | `FS.GI.FUND.PROMOTER.CANC.PROFIT.LOSS.BEARING` | `FsGiFundPromoter_CancProfitLossBearing` | TField |  | The code of the party who will bear the loss on cancellation of buy deal related to cancellation rights functionality. Multifonds DB Column is CLOSSBEAR. |
| 32 | `FS.GI.FUND.PROMOTER.TRADE.DATE.FOR.SWITCH` | `FsGiFundPromoter_TradeDateForSwitch` | TField |  | Trade date or value date calculation method for switch transaction. Multifonds DB Column is CSWITCH_ID. |
| 33 | `FS.GI.FUND.PROMOTER.BOX.MANAGER.ID` | `FsGiFundPromoter_BoxManagerId` | TField |  | Box Manager of the Fund Promoter linked to UK module. Multifonds DB Column is NREGISTER_BOX. |
| 34 | `FS.GI.FUND.PROMOTER.FIRST.TRANSACTION.MIN.LIMIT` | `FsGiFundPromoter_FirstTransactionMinLimit` | TField |  | Minimum limit amount for first transaction in fund linked to the Fund Promoter. The transaction will be blocked at simulation level if the minimum limit is not met. Multifonds DB Column is FIRST_TRANS_MIN_LMT. |
| 35 | `FS.GI.FUND.PROMOTER.UK.TERMS.OF.BUSINESS.FLAG` | `FsGiFundPromoter_UkTermsOfBusinessFlag` | TField |  | Flag to specify system to calculate the charges that are to be applied to the deal and the related terms of business linked to UK module. Multifonds DB Column is CFLG_UK_TERM. |
| 36 | `FS.GI.FUND.PROMOTER.UK.DISTRIBUTION.PROCESS.FLAG` | `FsGiFundPromoter_UkDistributionProcessFlag` | TField |  | Flag to specify whether the Fund Promoter is in scope of UK dividend distribution. Multifonds DB Column is CFLG_UK_DISTRIB. |
| 37 | `FS.GI.FUND.PROMOTER.COLLECTION.DATES` | `FsGiFundPromoter_CollectionDates` | TField |  | Dates allowed by the Fund Promoter to collect the amounts for the RSP investment linked to UK Module. Multifonds DB Column is COLLECT_TYPE. |
| 38 | `FS.GI.FUND.PROMOTER.UK.DIST.TAX.PARAMETERS.FLAG` | `FsGiFundPromoter_UkDistTaxParametersFlag` | TField |  | Flag to specify Fund Promoter is in scope of UK Distribution Tax Parameters. Multifonds DB Column is FLG_UK_DIST_TAX_PARM. |
| 39 | `FS.GI.FUND.PROMOTER.INHERIT.G1.G2.FLAG` | `FsGiFundPromoter_InheritG1G2Flag` | TField |  | Flag to check a Conversion/Switch Ina leg of a Conversion/Switch transaction at the order level linked to UK module. Multifonds DB Column is FLG_INHERIT_G1G2. |
| 40 | `FS.GI.FUND.PROMOTER.INTEREST.ROUND.FOR.INV.FLAG` | `FsGiFundPromoter_InterestRoundForInvFlag` | TField |  | Flag allows rounding of cash deposit accounts interest in favour of the client. Multifonds DB Column is INT_CLIENT_FLG. |
| 41 | `FS.GI.FUND.PROMOTER.INTEREST.ALLOCATION.METHOD` | `FsGiFundPromoter_InterestAllocationMethod` | TField |  | Interest allocation method applicable for the cash deposit accounts. Multifonds DB Column is INT_ALLOC_MTHD. |
| 42 | `FS.GI.FUND.PROMOTER.VALUATION.STATEMENT.FORMAT` | `FsGiFundPromoter_ValuationStatementFormat` | TField |  | Valuation statement report format. Multifonds DB Column is VALUATION_STAT_FORMAT. |
| 43 | `FS.GI.FUND.PROMOTER.PERIODIC.STATEMENT.FORMAT` | `FsGiFundPromoter_PeriodicStatementFormat` | TField |  | Periodic statement report format. Multifonds DB Column is PERIODIC_STAT_FORMAT. |
| 44 | `FS.GI.FUND.PROMOTER.BRANCH.ID` | `FsGiFundPromoter_BranchId` | TField |  | Branch internal ID of the Fund Promoter. Multifonds DB Column is BRANCH. |
| 45 | `FS.GI.FUND.PROMOTER.COVERING.LETTER` | `FsGiFundPromoter_CoveringLetter` | TField |  | Print instruction for contract notes/statement cover letters/acknowledgement. Multifonds DB Column is COVERING_LETTER. |
| 46 | `FS.GI.FUND.PROMOTER.RIGHT.TYPE` | `FsGiFundPromoter_RightType` | TField |  | Right type ID of the Fund Promoter. Multifonds DB Column is RIGHT_TYPE. |
| 47 | `FS.GI.FUND.PROMOTER.SWITCH.AT.NAV.PRICE` | `FsGiFundPromoter_SwitchAtNavPrice` | TField |  | The NAV price to consider for switch and conversion contracts. Multifonds DB Column is FLG_SWITCH_NAV_PRICE. |
| 48 | `FS.GI.FUND.PROMOTER.CASH.FLOW.ID` | `FsGiFundPromoter_CashFlowId` | TField |  | Cash flow ID linked to the Fund Promoter. Multifonds DB Column is CASH_FLOW_ID. |
| 49 | `FS.GI.FUND.PROMOTER.CDSC.BUCKET` | `FsGiFundPromoter_CdscBucket` | TField |  | CDSC bucket method applied for switches and transfers. Multifonds DB Column is CDSC_BUCKET_FIFO. |
| 50 | `FS.GI.FUND.PROMOTER.CTL.ON.ORDER.BANK.DETAILS` | `FsGiFundPromoter_CtlOnOrderBankDetails` | TField |  | Control to check bank details of redemption orders at order entry level. Multifonds DB Column is CTRL_BNK_DET. |
| 51 | `FS.GI.FUND.PROMOTER.PAYMENT.AMOUNT.HANDLING` | `FsGiFundPromoter_PaymentAmountHandling` | TField |  | Payment amount handling method in contract level. Multifonds DB Column is PAY_HANDLING. |
| 52 | `FS.GI.FUND.PROMOTER.SHORT.POSITION.CONTROL` | `FsGiFundPromoter_ShortPositionControl` | TField |  | Short position control to carry out an automated adjustment to cash redemption orders when the NAV is dropped and the original order has insufficient units to cover the instruction. Multifonds DB Column is SHORT_POS_CTRL. |
| 53 | `FS.GI.FUND.PROMOTER.DIV.ON.SETTLED.SHARES` | `FsGiFundPromoter_DivOnSettledShares` | TField |  | It specifies if the dividend reinvestment or payment on the settled shares shall be allowed. Multifonds DB Column is FLG_DIV_SETT_SHARE. |
| 54 | `FS.GI.FUND.PROMOTER.PAYMENT.PROCESS` | `FsGiFundPromoter_PaymentProcess` | TField |  | The payment process to be followed for the deals. Multifonds DB Column is PY_PROCESS. |
| 55 | `FS.GI.FUND.PROMOTER.DOCUMENT.HANDLING` | `FsGiFundPromoter_DocumentHandling` | TField |  | Swift document handling details for theNon Swift Trigger ID &apos;0008-generic static data change&apos;. Multifonds DB Column is DOC_HANDLING. |
| 56 | `FS.GI.FUND.PROMOTER.CUSTODIAN` | `FsGiFundPromoter_Custodian` | TField |  | It specifies if the custodian is internal or external. Multifonds DB Column is CUSTODIAN. |
| 57 | `FS.GI.FUND.PROMOTER.UPDATEFROM.FUND.PROMOTER` | `FsGiFundPromoter_UpdatefromFundPromoter` | TField |  | Model code linked to Fund Promoter which is used to update the Legal Entity based on Fund Promoter fields. Multifonds DB Column is UPD_FROM_FP_MODEL. |
| 58 | `FS.GI.FUND.PROMOTER.GL.FLOW.ID` | `FsGiFundPromoter_GlFlowId` | TField |  | General Ledger Flow ID linked to the Fund Promoter. Multifonds DB Column is GL_FLOW_ID. |
| 59 | `FS.GI.FUND.PROMOTER.GDPR.INFORM.DATE` | `FsGiFundPromoter_GdprInformDate` | TField |  | Date when GDPR was informed. Multifonds DB Column is GDPR_DINFORMED_ON. |
| 60 | `FS.GI.FUND.PROMOTER.GL.ACCOUNT.GROUP.ID` | `FsGiFundPromoter_GlAccountGroupId` | TField |  | General Ledger Accounts group linked to the Fund Promoter. Multifonds DB Column is GL_ACCT_GROUP_ID. |
| 61 | `FS.GI.FUND.PROMOTER.SALESMAN.MANDATORY.FLAG` | `FsGiFundPromoter_SalesmanMandatoryFlag` | TField | Yes | Flag to allow parameterization of a salesman for all registers willing to invest in funds linked to the Fund Promoter mandatory. Multifonds DB Column is FLG_SMAN. |
| 62 | `FS.GI.FUND.PROMOTER.SALESWATCH.ENABLED.FLAG` | `FsGiFundPromoter_SaleswatchEnabledFlag` | TField | Yes | Flag to allow parameterization of saleswatch type for dealing agents of registers linked to the Fund Promoter mandatory. Multifonds DB Column is FLG_SWATCH. |
| 63 | `FS.GI.FUND.PROMOTER.REDEEM.SETTLED.SHARES.FLAG` | `FsGiFundPromoter_RedeemSettledSharesFlag` | TField |  | Flag to allow redemption of only settled shares at order entry level. Multifonds DB Column is FLG_REDEEM. |
| 64 | `FS.GI.FUND.PROMOTER.DB.PEND.ORD.FOR.EST.POS.FLAG` | `FsGiFundPromoter_DbPendOrdForEstPosFlag` | TField |  | Flag to allow including the pending debit orders for position calculation. Multifonds DB Column is FLG_ALL_DB_PENDING. |
| 65 | `FS.GI.FUND.PROMOTER.PARTIAL.SETTLEMENT.SUBS.FLAG` | `FsGiFundPromoter_PartialSettlementSubsFlag` | TField |  | Flag to enable partial settlement functionality. Multifonds DB Column is FLG_PART_SETT_SUB. |
| 66 | `FS.GI.FUND.PROMOTER.STP.CANCEL.REV.VIA.INTF.FLAG` | `FsGiFundPromoter_StpCancelRevViaIntfFlag` | TField |  | Flag to allow STP cancel/reversal via interface. Multifonds DB Column is FLG_STP_OCR. |
| 67 | `FS.GI.FUND.PROMOTER.BACKDATED.REV.CTL.FLAG` | `FsGiFundPromoter_BackdatedRevCtlFlag` | TField |  | Flag to block backdated and reversal orders. Multifonds DB Column is FLG_BACK_REV_CTRL. |
| 68 | `FS.GI.FUND.PROMOTER.BACKDATED.REV.REPROC.FLAG` | `FsGiFundPromoter_BackdatedRevReprocFlag` | TField |  | Flag to enable reprocessing of contract linkages for all debit contracts after a backdated transaction or reversal of a historical contract. Multifonds DB Column is FLG_BACK_REV_REPROCESS. |
| 69 | `FS.GI.FUND.PROMOTER.AGENT.ORDER.OVERRIDE.FLAG` | `FsGiFundPromoter_AgentOrderOverrideFlag` | TField |  | Flag to allow override of agent at order entry level. Multifonds DB Column is FLG_OVERRIDE_NOUTLET. |
| 70 | `FS.GI.FUND.PROMOTER.PHONE.DEALING.FLAG` | `FsGiFundPromoter_PhoneDealingFlag` | TField |  | Flag to enable phone dealing functionality for all underlying funds. Multifonds DB Column is FLG_PHONE_DEAL. |
| 71 | `FS.GI.FUND.PROMOTER.CTV.CONTROL.FLAG` | `FsGiFundPromoter_CtvControlFlag` | TField |  | Flag to check at simulation level if the trade limitations set up at MF fund level have been overcome. Multifonds DB Column is CTV_CONTROL. |
| 72 | `FS.GI.FUND.PROMOTER.CHECK.ON.REGISTER.POS.FLAG` | `FsGiFundPromoter_CheckOnRegisterPosFlag` | TField |  | Flag to allow first subscription limits to be applied when a register without current holdings re-subscribes. Multifonds DB Column is FLG_CHK_REG_POS. |
| 73 | `FS.GI.FUND.PROMOTER.POS.CHECK.AT.DIV.CONF.FLAG` | `FsGiFundPromoter_PosCheckAtDivConfFlag` | TField |  | Flag to allow automatic payout of the dividends and daily dividends irrespective of the reinvestment instruction set up. Multifonds DB Column is FLG_POS_CHECK. |
| 74 | `FS.GI.FUND.PROMOTER.ERISA.CHECK.FLAG` | `FsGiFundPromoter_ErisaCheckFlag` | TField |  | Flag define whether ERISA check should be done for investors investing in the funds linked to the Fund Promoter. Multifonds DB Column is FLG_ERISA_CHECK. |
| 75 | `FS.GI.FUND.PROMOTER.AMEND.PAYMENT.FLAG` | `FsGiFundPromoter_AmendPaymentFlag` | TField |  | Flag to allow amending the payment information generated. Multifonds DB Column is FLG_AMEND_PYMT. |
| 76 | `FS.GI.FUND.PROMOTER.SOFT.CLOSURE.SWITCH.FLAG` | `FsGiFundPromoter_SoftClosureSwitchFlag` | TField |  | Flag to enable soft closure only for the switches between different Fund Promoter. Multifonds DB Column is FLG_SOFT_CLOSURES. |
| 77 | `FS.GI.FUND.PROMOTER.NAV.VALIDITY.PF.CONTROL.FLAG` | `FsGiFundPromoter_NavValidityPfControlFlag` | TField |  | Flag to block performance fee calculation if the NAV for a performance fee fund is not equal to (GAV - Performance fee). Multifonds DB Column is FLG_NAV_CONTROL. |
| 78 | `FS.GI.FUND.PROMOTER.MIN.LIMITS.MONITORING.FLAG` | `FsGiFundPromoter_MinLimitsMonitoringFlag` | TField |  | Flag allows to check the minimum transaction limit at order level. Multifonds DB Column is FLG_MIN_LMT_MON. |
| 79 | `FS.GI.FUND.PROMOTER.INTER.LE.SWITCHES.RESTR.FLAG` | `FsGiFundPromoter_InterLeSwitchesRestrFlag` | TField |  | Flag allows to block the switch between two funds linked to different Fund Promoters. Multifonds DB Column is FLG_INT_TFC_SWITCH. |
| 80 | `FS.GI.FUND.PROMOTER.CDSC.WRITE.DOWN.FLAG` | `FsGiFundPromoter_CdscWriteDownFlag` | TField |  | Flag to activate reporting functionality for CDSC bucket share classes. Multifonds DB Column is FLG_CDSC_WRDN. |
| 81 | `FS.GI.FUND.PROMOTER.FX.REVERSAL.FLAG` | `FsGiFundPromoter_FxReversalFlag` | TField |  | Flag to include reversed/cancelled order in the client trading desk report. Multifonds DB Column is FLG_FX_REV. |
| 82 | `FS.GI.FUND.PROMOTER.FX.EXPORTING.FLAG` | `FsGiFundPromoter_FxExportingFlag` | TField |  | Flag to enable export of forex deals. Multifonds DB Column is FLG_FX_EXPRT. |
| 83 | `FS.GI.FUND.PROMOTER.BLOCK.ORDER.DELETION.FLAG` | `FsGiFundPromoter_BlockOrderDeletionFlag` | TField |  | Flag to activate blocking the order from deletion functionality. Multifonds DB Column is FLG_BLK_ORD_DEL. |
| 84 | `FS.GI.FUND.PROMOTER.OVER.CONV.FLAG` | `FsGiFundPromoter_OverConvFlag` | TField |  | Flag to allow override of conversion flag at Manager Application screen. Multifonds DB Column is FLG_OVER_CONV. |
| 85 | `FS.GI.FUND.PROMOTER.ACC.OPENING.NOTICE.FLAG` | `FsGiFundPromoter_AccOpeningNoticeFlag` | TField |  | Flag to send account opening notice for Fund Promoter. Multifonds DB Column is FLG_ACC_OPEN_NOTICE. |
| 86 | `FS.GI.FUND.PROMOTER.SAME.TD.FOR.FOF.TRANS.FLAG` | `FsGiFundPromoter_SameTdForFofTransFlag` | TField |  | Flag to calculate common valid trade date for the Fund of fund structures at order entry level. Multifonds DB Column is FLG_SAME_TD_FOF. |
| 87 | `FS.GI.FUND.PROMOTER.PROFIT.LOSS.METHOD` | `FsGiFundPromoter_ProfitLossMethod` | TField |  | Method for calculation profit/loss. Multifonds DB Column is PL_METHOD. |
| 88 | `FS.GI.FUND.PROMOTER.GLOBAL.ORDERING.FLAG` | `FsGiFundPromoter_GlobalOrderingFlag` | TField |  | Flag to enable global ordering functionality. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 89 | `FS.GI.FUND.PROMOTER.EXTERNAL.TA.ID` | `FsGiFundPromoter_ExternalTaId` | TField |  | External TA linked to the Fund Promoter. Multifonds DB Column is EXTERNAL_TA. |
| 90 | `FS.GI.FUND.PROMOTER.TRANSFER.AGENT` | `FsGiFundPromoter_TransferAgent` | TField |  | It specifies if the management company is administrated inside the transfer agency or as external. Multifonds DB Column is TA_TFC. |
| 91 | `FS.GI.FUND.PROMOTER.CASH.DIVIDEND.REGISTER.ID` | `FsGiFundPromoter_CashDividendRegisterId` | TField | Yes | Technical register for cash dividend. This field is mandatory when the global ordering flag is ticked. Multifonds DB Column is NREGISTER_CASH_DIV. |
| 92 | `FS.GI.FUND.PROMOTER.REINVESTMENT.REGISTER.ID` | `FsGiFundPromoter_ReinvestmentRegisterId` | TField | Yes | Technical register for reinvestment. This field is mandatory when the global ordering flag is ticked. Multifonds DB Column is NREGISTER_REINVEST. |
| 93 | `FS.GI.FUND.PROMOTER.COLLECTION.ACCOUNT.GROUP` | `FsGiFundPromoter_CollectionAccountGroup` | TField |  | Collection account group code used to group deals and receipts that can be matched together. Multifonds DB Column is COLL_ACC_GRP. |
| 94 | `FS.GI.FUND.PROMOTER.CREDITOR.ID` | `FsGiFundPromoter_CreditorId` | TField |  | Creditor ID to identify the institution that collects the money for standing instructions under savings plan functionality. Multifonds DB Column is CREDITOR_ID. |
| 95 | `FS.GI.FUND.PROMOTER.MATCHING.TOLERANCE.AMOUNT` | `FsGiFundPromoter_MatchingToleranceAmount` | TField |  | Tolerance amount applicable for cash receipts matching. Multifonds DB Column is TOLERANCE_AMT. |
| 96 | `FS.GI.FUND.PROMOTER.RET.CALC.CYC.END.DATE.ADD.BD` | `FsGiFundPromoter_RetCalcCycEndDateAddBd` | TField |  | Number of days to be added to business day to calculate cycle end date for retrocession calculation. Multifonds DB Column is BDAYS_ADD_PAY. |
| 97 | `FS.GI.FUND.PROMOTER.SETTLEMENT.DATE` | `FsGiFundPromoter_SettlementDate` | TField |  | Behavior of the settlement date update during cash receipt matching. Multifonds DB Column is SETTLEMENT_DATE. |
| 98 | `FS.GI.FUND.PROMOTER.IMR.FLAG` | `FsGiFundPromoter_ImrFlag` | TField |  | Flag to activate Investor Money Regulation functionality. Multifonds DB Column is FLG_IMR. |
| 99 | `FS.GI.FUND.PROMOTER.RETRO.CASH.DB.PER.FUNDS.FLAG` | `FsGiFundPromoter_RetroCashDbPerFundsFlag` | TField |  | Flag to enable hierarchy mechanism to retrieve the retrocession debit account to be used for retrocession payment. Multifonds DB Column is FLG_RET_CASH_DB_FUNDS. |
| 100 | `FS.GI.FUND.PROMOTER.FATCA.STATUS` | `FsGiFundPromoter_FatcaStatus` | TField |  | FATCA Status of the Fund Promoter. Multifonds DB Column is FAT_STATUS. |
| 101 | `FS.GI.FUND.PROMOTER.FATCA.MODEL` | `FsGiFundPromoter_FatcaModel` | TField |  | IGA Model for FATCA purposes. Multifonds DB Column is FAT_MODEL. |
| 102 | `FS.GI.FUND.PROMOTER.GIIN.NUMBER` | `FsGiFundPromoter_GiinNumber` | TField |  | FATCA Global Internediaery Identification Number. Multifonds DB Column is FAT_GIIN. |
| 103 | `FS.GI.FUND.PROMOTER.FATCA.EFFECTIVE.DATE` | `FsGiFundPromoter_FatcaEffectiveDate` | TField |  | FATCA effective date. Multifonds DB Column is FAT_DEFFECTIVE. |
| 104 | `FS.GI.FUND.PROMOTER.FATCA.EXPIRY.DATE` | `FsGiFundPromoter_FatcaExpiryDate` | TField |  | FATCA expiry date. Multifonds DB Column is FAT_DEXPIRY. |
| 105 | `FS.GI.FUND.PROMOTER.FATCA.SERVICE.OFFERING` | `FsGiFundPromoter_FatcaServiceOffering` | TField |  | The entity responsible for the due diligence which is used for reporting to Internal Revenue Service. Multifonds DB Column is FAT_SERV_OFFER. |
| 106 | `FS.GI.FUND.PROMOTER.FATCA.REVOKE.DATE` | `FsGiFundPromoter_FatcaRevokeDate` | TField |  | FATCA revoke date. Multifonds DB Column is FAT_DREVOKE. |
| 107 | `FS.GI.FUND.PROMOTER.CRS.STATUS` | `FsGiFundPromoter_CrsStatus` | TField |  | CRS status. Multifonds DB Column is CRS_STATUS. |
| 108 | `FS.GI.FUND.PROMOTER.JURISDICTION` | `FsGiFundPromoter_Jurisdiction` | TField |  | Fund Promoter jurisdiction country for FATCA reporting purposes. Multifonds DB Column is JURISDICTION. |
| 109 | `FS.GI.FUND.PROMOTER.TAX.ID.NUMBER` | `FsGiFundPromoter_TaxIdNumber` | TField |  | Tax Identifier Number for FATCA reporting purposes. Multifonds DB Column is TIN_NUMBER. |
| 110 | `FS.GI.FUND.PROMOTER.DEPOSITOR.ID` | `FsGiFundPromoter_DepositorId` | TField |  | Depositor linked to the Fund Promoter. Multifonds DB Column is DEPOSITOR. |
| 111 | `FS.GI.FUND.PROMOTER.FATCA.EXEMPTION.REASON` | `FsGiFundPromoter_FatcaExemptionReason` | TField |  | Fatca excemption reason of the Fund Promoter. Multifonds DB Column is FAT_EXEM_REASON. |
| 112 | `FS.GI.FUND.PROMOTER.SPONSORING.ENTITY.ID` | `FsGiFundPromoter_SponsoringEntityId` | TField |  | FATCA sponsoring entity. Multifonds DB Column is FAT_SPONSOR. |
| 113 | `FS.GI.FUND.PROMOTER.CANC.LOSS.THRESHOLD` | `FsGiFundPromoter_CancLossThreshold` | TField |  | Threshold whithin which Fund Promoter will bear the loss arising out of cancellation of buy deal. Multifonds DB Column is NLOSSTHRESH. |
| 114 | `FS.GI.FUND.PROMOTER.CANC.LOSS.THRESHOLD.CURRENCY` | `FsGiFundPromoter_CancLossThresholdCurrency` | TField |  | The currency code (in 3 letter ISO code, Eg: EUR) for threshold calculation related to cancellation rights functionality. Multifonds DB Column is CCY_THRESH. |
| 115 | `FS.GI.FUND.PROMOTER.CONTRACT.NOTES.DETAILS` | `FsGiFundPromoter_ContractNotesDetails` | TField |  | Flag to allow populating additional information in contract note such as contract date and time,valuation point etc,. Multifonds DB Column is FLG_CN_DETAIL. |
| 116 | `FS.GI.FUND.PROMOTER.FIRST.TRS.MIN.LIMIT.CURRENCY` | `FsGiFundPromoter_FirstTrsMinLimitCurrency` | TField |  | The currency of the minimum limit for first transaction. Multifonds DB Column is CMON_MIN. |
| 117 | `FS.GI.FUND.PROMOTER.MATCHING.TOLERANCE.CURRENCY` | `FsGiFundPromoter_MatchingToleranceCurrency` | TField |  | Tolerance amount currency applicable for cash receipts matching. Multifonds DB Column is TOLERANCE_CCY. |
| 118 | `FS.GI.FUND.PROMOTER.TRANSACTION.BULKING.NETTING` | `FsGiFundPromoter_TransactionBulkingNetting` | TField |  | Transaction bulking or netting code of cash movements. Multifonds DB Column is TRNS_BULK_NET. |
| 119 | `FS.GI.FUND.PROMOTER.INACTIVATION.DATE` | `FsGiFundPromoter_InactivationDate` | TField |  | Fund Promoter Inactivation date Multifonds DB Column is DATE_INACTIVE. |
| 120 | `FS.GI.FUND.PROMOTER.RESERVED10` | `FsGiFundPromoter_Reserved10` | TField |  |  |
| 121 | `FS.GI.FUND.PROMOTER.RESERVED9` | `FsGiFundPromoter_Reserved9` | TField |  |  |
| 122 | `FS.GI.FUND.PROMOTER.RESERVED8` | `FsGiFundPromoter_Reserved8` | TField |  |  |
| 123 | `FS.GI.FUND.PROMOTER.RESERVED7` | `FsGiFundPromoter_Reserved7` | TField |  |  |
| 124 | `FS.GI.FUND.PROMOTER.RESERVED6` | `FsGiFundPromoter_Reserved6` | TField |  |  |
| 125 | `FS.GI.FUND.PROMOTER.RESERVED5` | `FsGiFundPromoter_Reserved5` | TField |  |  |
| 126 | `FS.GI.FUND.PROMOTER.RESERVED4` | `FsGiFundPromoter_Reserved4` | TField |  |  |
| 127 | `FS.GI.FUND.PROMOTER.RESERVED3` | `FsGiFundPromoter_Reserved3` | TField |  |  |
| 128 | `FS.GI.FUND.PROMOTER.RESERVED2` | `FsGiFundPromoter_Reserved2` | TField |  |  |
| 129 | `FS.GI.FUND.PROMOTER.RESERVED1` | `FsGiFundPromoter_Reserved1` | TField |  |  |
| 130 | `FS.GI.FUND.PROMOTER.LOCAL.REF` | `FsGiFundPromoter_LocalRef` |  |  |  |
| 131 | `FS.GI.FUND.PROMOTER.OVERRIDE` | `FsGiFundPromoter_Override` |  |  |  |
| 132 | `FS.GI.FUND.PROMOTER.RECORD.STATUS` | `FsGiFundPromoter_RecordStatus` | String |  |  |
| 133 | `FS.GI.FUND.PROMOTER.CURR.NO` | `FsGiFundPromoter_CurrNo` | String |  |  |
| 134 | `FS.GI.FUND.PROMOTER.INPUTTER` | `FsGiFundPromoter_Inputter` |  |  |  |
| 135 | `FS.GI.FUND.PROMOTER.DATE.TIME` | `FsGiFundPromoter_DateTime` |  |  |  |
| 136 | `FS.GI.FUND.PROMOTER.AUTHORISER` | `FsGiFundPromoter_Authoriser` | String |  |  |
| 137 | `FS.GI.FUND.PROMOTER.CO.CODE` | `FsGiFundPromoter_CoCode` | String |  |  |
| 138 | `FS.GI.FUND.PROMOTER.DEPT.CODE` | `FsGiFundPromoter_DeptCode` | String |  |  |
| 139 | `FS.GI.FUND.PROMOTER.AUDITOR.CODE` | `FsGiFundPromoter_AuditorCode` | String |  |  |
| 140 | `FS.GI.FUND.PROMOTER.AUDIT.DATE.TIME` | `FsGiFundPromoter_AuditDateTime` | String |  |  |
