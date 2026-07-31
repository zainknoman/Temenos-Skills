# FS.GI.FUND.LEGAL.ENTITY — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.LEGAL.ENTITY` in `FS_FundLegalEntity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.LEGAL.ENTITY.PARENT.REF.ID` | `FsGiFundLegalEntity_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.LEGAL.ENTITY.ORA.ROWID` | `FsGiFundLegalEntity_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.LEGAL.ENTITY.FUND.PROMOTER.ID` | `FsGiFundLegalEntity_FundPromoterId` | TField |  | Fund Promoter internal ID linked to Legal Entity. Multifonds DB Column is NPROMOTER. |
| 4 | `FS.GI.FUND.LEGAL.ENTITY.EXTERNAL.ID` | `FsGiFundLegalEntity_ExternalId` | TField |  | Legal Entity external refernece ID. Multifonds DB Column is NTFC_EXTERN. |
| 5 | `FS.GI.FUND.LEGAL.ENTITY.LEGAL.ENTITY.ID` | `FsGiFundLegalEntity_LegalEntityId` | TField |  | Legal Entity internal identifier. Multifonds DB Column is NTFC. |
| 6 | `FS.GI.FUND.LEGAL.ENTITY.NAME` | `FsGiFundLegalEntity_Name` | TField |  | Legal Entity name. Multifonds DB Column is TFC_NAME. |
| 7 | `FS.GI.FUND.LEGAL.ENTITY.LANGUAGE.CODE` | `FsGiFundLegalEntity_LanguageCode` | TField |  | Language code. Multifonds DB Column is CLANGUE. |
| 8 | `FS.GI.FUND.LEGAL.ENTITY.ACCOUNT.HOLDER` | `FsGiFundLegalEntity_AccountHolder` | TField |  | Management company account holder. Multifonds DB Column is ACCOUNT_HOLDER. |
| 9 | `FS.GI.FUND.LEGAL.ENTITY.CONTACT.PERSON.1` | `FsGiFundLegalEntity_ContactPerson1` | TField |  | Contact person 1 for Legal Entity. Multifonds DB Column is CONTACT_PERSON1. |
| 10 | `FS.GI.FUND.LEGAL.ENTITY.CONTACT.PERSON.2` | `FsGiFundLegalEntity_ContactPerson2` | TField |  | Contact person 2 for Legal Entity. Multifonds DB Column is CONTACT_PERSON2. |
| 11 | `FS.GI.FUND.LEGAL.ENTITY.ADDRESS.LINE.1` | `FsGiFundLegalEntity_AddressLine1` | TField |  | Address Line 1. Multifonds DB Column is ADDRESSE_LINE1. |
| 12 | `FS.GI.FUND.LEGAL.ENTITY.ADDRESS.LINE.2` | `FsGiFundLegalEntity_AddressLine2` | TField |  | Address Line 2. Multifonds DB Column is ADDRESSE_LINE2. |
| 13 | `FS.GI.FUND.LEGAL.ENTITY.ADDRESS.LINE.3` | `FsGiFundLegalEntity_AddressLine3` | TField |  | Address Line 3. Multifonds DB Column is ADDRESSE_LINE3. |
| 14 | `FS.GI.FUND.LEGAL.ENTITY.ADDRESS.LINE.4` | `FsGiFundLegalEntity_AddressLine4` | TField |  | Address Line 4. Multifonds DB Column is ADDRESSE_LINE4. |
| 15 | `FS.GI.FUND.LEGAL.ENTITY.POSTCODE` | `FsGiFundLegalEntity_Postcode` | TField |  | Postcode of the address. Multifonds DB Column is CODE. |
| 16 | `FS.GI.FUND.LEGAL.ENTITY.TOWN` | `FsGiFundLegalEntity_Town` | TField |  | City of address. Multifonds DB Column is VILLE. |
| 17 | `FS.GI.FUND.LEGAL.ENTITY.COUNTRY` | `FsGiFundLegalEntity_Country` | TField |  | Legal Entity country (in 2 letter format eg &apos;LU&apos;). Multifonds DB Column is PAYS. |
| 18 | `FS.GI.FUND.LEGAL.ENTITY.PHONE.NUMBER` | `FsGiFundLegalEntity_PhoneNumber` | TField |  | Telephone number of Legal Entity. Multifonds DB Column is TEL_NO. |
| 19 | `FS.GI.FUND.LEGAL.ENTITY.FOR.ATTENTION.OF.1` | `FsGiFundLegalEntity_ForAttentionOf1` | TField |  | Fax contact name 1 for the Legal Entity. Multifonds DB Column is ATTENTION_OF1. |
| 20 | `FS.GI.FUND.LEGAL.ENTITY.FAX.NUMBER.1` | `FsGiFundLegalEntity_FaxNumber1` | TField |  | Fax number 1 for Legal Entity. Multifonds DB Column is FAX_NO1. |
| 21 | `FS.GI.FUND.LEGAL.ENTITY.FOR.ATTENTION.OF.2` | `FsGiFundLegalEntity_ForAttentionOf2` | TField |  | Fax contact name 2 for the Legal Entity. Multifonds DB Column is ATTENTION_OF2. |
| 22 | `FS.GI.FUND.LEGAL.ENTITY.FAX.NUMBER.2` | `FsGiFundLegalEntity_FaxNumber2` | TField |  | Fax number 2 for Legal Entity. Multifonds DB Column is FAX_NO2. |
| 23 | `FS.GI.FUND.LEGAL.ENTITY.CORRESPONDANT.ID` | `FsGiFundLegalEntity_CorrespondantId` | TField |  | Correspondant Bank ID. Multifonds DB Column is NCORRESP. |
| 24 | `FS.GI.FUND.LEGAL.ENTITY.BANK.ACCOUNT.NUMBER` | `FsGiFundLegalEntity_BankAccountNumber` | TField |  | Bank Account number. Multifonds DB Column is BANK_ACCOUNT. |
| 25 | `FS.GI.FUND.LEGAL.ENTITY.BANK.ACCOUNT.TEXT` | `FsGiFundLegalEntity_BankAccountText` | TField |  | Free text to add information if any. Multifonds DB Column is BANK_ACCN_TEXT. |
| 26 | `FS.GI.FUND.LEGAL.ENTITY.NOSTRO.ACCOUNT.ID` | `FsGiFundLegalEntity_NostroAccountId` | TField |  | Field allows to link the Legal Entity to a NOSTRO account for Payment by cheque functionality. Multifonds DB Column is NCORRESP_NOSTRO. |
| 27 | `FS.GI.FUND.LEGAL.ENTITY.INTERNAL.ACCOUNT.NUMBER` | `FsGiFundLegalEntity_InternalAccountNumber` | TField |  | TA account number for fund supermarket module. Multifonds DB Column is INTERNAL_ACCOUNT. |
| 28 | `FS.GI.FUND.LEGAL.ENTITY.TAX.NUMBER` | `FsGiFundLegalEntity_TaxNumber` | TField |  | Tax number for the Legal Entity. Multifonds DB Column is TAXE_NO. |
| 29 | `FS.GI.FUND.LEGAL.ENTITY.ROUNDING.DIFFERENCE` | `FsGiFundLegalEntity_RoundingDifference` | TField |  | The code to specify where the rounding difference can be allocated in case of multiple switches within the product. Multifonds DB Column is TYPE_RNDIFF. |
| 30 | `FS.GI.FUND.LEGAL.ENTITY.CANCELLATION.TIMEFRAME` | `FsGiFundLegalEntity_CancellationTimeframe` | TField |  | Number of days in which an investor linked to the Legal Entity can exercise his cancellation rights. Multifonds DB Column is NTIMEFRAME. |
| 31 | `FS.GI.FUND.LEGAL.ENTITY.CANC.PROFIT.LOSS.BEARING` | `FsGiFundLegalEntity_CancProfitLossBearing` | TField |  | The code of the party who will bear the loss on cancellation of buy deal related to cancellation rights functionality. Multifonds DB Column is CLOSSBEAR. |
| 32 | `FS.GI.FUND.LEGAL.ENTITY.TRADE.DATE.FOR.SWITCH` | `FsGiFundLegalEntity_TradeDateForSwitch` | TField |  | The Trade Date or Value Date calculation method for switch transactions. Multifonds DB Column is CSWITCH_TD. |
| 33 | `FS.GI.FUND.LEGAL.ENTITY.BOX.MANAGER.ID` | `FsGiFundLegalEntity_BoxManagerId` | TField |  | Box Manager of the Legal Entity linked to UK module. Multifonds DB Column is NREGISTER_BOX. |
| 34 | `FS.GI.FUND.LEGAL.ENTITY.FIRST.TRANSACTION.MIN.LIMIT` | `FsGiFundLegalEntity_FirstTransactionMinLimit` | TField |  | Minimum limit amount for first transaction in fund linked to the Legal Entity. The transaction will be blocked at simulation level if the minimum limit is not met. Multifonds DB Column is FIRST_TRANS_MIN_LMT. |
| 35 | `FS.GI.FUND.LEGAL.ENTITY.UK.TERMS.OF.BUSINESS.FLAG` | `FsGiFundLegalEntity_UkTermsOfBusinessFlag` | TField |  | Flag to specify system to calculate the charges that are to be applied to the deal and the related terms of business linked to UK module. Multifonds DB Column is CFLG_UK_TERM. |
| 36 | `FS.GI.FUND.LEGAL.ENTITY.UK.DISTRIBUTION.PROCESS.FLAG` | `FsGiFundLegalEntity_UkDistributionProcessFlag` | TField |  | Flag to specify whether the Legal Entity is in scope of UK dividend distribution. Multifonds DB Column is CFLG_UK_DISTRIB. |
| 37 | `FS.GI.FUND.LEGAL.ENTITY.COLLECTION.DATES` | `FsGiFundLegalEntity_CollectionDates` | TField |  | Dates allowed by the Legal Entity to collect the amounts for the RSP investment linked to UK Module. Multifonds DB Column is COLLECT_TYPE. |
| 38 | `FS.GI.FUND.LEGAL.ENTITY.UK.DIST.TAX.PARAMETERS.FLAG` | `FsGiFundLegalEntity_UkDistTaxParametersFlag` | TField |  | Flag to specify Legal Entity is in scope of UK Distribution Tax Parameters. Multifonds DB Column is FLG_UK_DIST_TAX_PARM. |
| 39 | `FS.GI.FUND.LEGAL.ENTITY.INHERIT.G1.G2.FLAG` | `FsGiFundLegalEntity_InheritG1G2Flag` | TField |  | Flag to check a Conversion/Switch Ina leg of a Conversion/Switch transaction at the order level linked to UK module. Multifonds DB Column is FLG_INHERIT_G1G2. |
| 40 | `FS.GI.FUND.LEGAL.ENTITY.INTEREST.ROUND.FOR.INV.FLAG` | `FsGiFundLegalEntity_InterestRoundForInvFlag` | TField |  | Flag allows rounding of cash deposit accounts interest in favour of the client. Multifonds DB Column is INT_CLIENT_FLG. |
| 41 | `FS.GI.FUND.LEGAL.ENTITY.INTEREST.ALLOCATION.METHOD` | `FsGiFundLegalEntity_InterestAllocationMethod` | TField |  | Interest allocation method applicable for the cash deposit accounts. Multifonds DB Column is INT_ALLOC_MTHD. |
| 42 | `FS.GI.FUND.LEGAL.ENTITY.VALUATION.STATEMENT.FORMAT` | `FsGiFundLegalEntity_ValuationStatementFormat` | TField |  | Valuation statement report format. Multifonds DB Column is VALUATION_STAT_FORMAT. |
| 43 | `FS.GI.FUND.LEGAL.ENTITY.PERIODIC.STATEMENT.FORMAT` | `FsGiFundLegalEntity_PeriodicStatementFormat` | TField |  | Periodic statement report format. Multifonds DB Column is PERIODIC_STAT_FORMAT. |
| 44 | `FS.GI.FUND.LEGAL.ENTITY.BRANCH.ID` | `FsGiFundLegalEntity_BranchId` | TField |  | Branch internal ID of the Legal Entity. Multifonds DB Column is BRANCH. |
| 45 | `FS.GI.FUND.LEGAL.ENTITY.COVERING.LETTER` | `FsGiFundLegalEntity_CoveringLetter` | TField |  | Print instruction for contract notes/statement cover letters/acknowledgement. Multifonds DB Column is COVERING_LETTER. |
| 46 | `FS.GI.FUND.LEGAL.ENTITY.RIGHT.TYPE` | `FsGiFundLegalEntity_RightType` | TField |  | Right type ID of the Legal Entity. Multifonds DB Column is RIGHT_TYPE. |
| 47 | `FS.GI.FUND.LEGAL.ENTITY.SWITCH.NAV.PRICE` | `FsGiFundLegalEntity_SwitchNavPrice` | TField |  | The NAV price to consider for switch and conversion contracts. Multifonds DB Column is FLG_SWITCH_NAV_PRICE. |
| 48 | `FS.GI.FUND.LEGAL.ENTITY.CASH.FLOW.ID` | `FsGiFundLegalEntity_CashFlowId` | TField |  | Cash flow ID linked to the Legal Entity. Multifonds DB Column is CASH_FLOW_ID. |
| 49 | `FS.GI.FUND.LEGAL.ENTITY.CDSC.BUCKET` | `FsGiFundLegalEntity_CdscBucket` | TField |  | CDSC bucket method applied for switches and transfers. Multifonds DB Column is CDSC_BUCKET_FIFO. |
| 50 | `FS.GI.FUND.LEGAL.ENTITY.CTL.ON.ORDER.BANK.DETAILS` | `FsGiFundLegalEntity_CtlOnOrderBankDetails` | TField |  | Control to check bank details of redemption orders at order entry level. Multifonds DB Column is CTRL_BNK_DET. |
| 51 | `FS.GI.FUND.LEGAL.ENTITY.PAYMENT.AMOUNT.HANDLING` | `FsGiFundLegalEntity_PaymentAmountHandling` | TField |  | Payment amount handling method in contract level. Multifonds DB Column is PAY_HANDLING. |
| 52 | `FS.GI.FUND.LEGAL.ENTITY.SHORT.POSITION.CONTROL` | `FsGiFundLegalEntity_ShortPositionControl` | TField |  | Short position control to carry out an automated adjustment to cash redemption orders when the NAV is dropped and the original order has insufficient units to cover the instruction. Multifonds DB Column is SHORT_POS_CTRL. |
| 53 | `FS.GI.FUND.LEGAL.ENTITY.DIV.ON.SETTLED.SHARES` | `FsGiFundLegalEntity_DivOnSettledShares` | TField |  | It specifies if the dividend reinvestment or payment on the settled shares shall be allowed. Multifonds DB Column is FLG_DIV_SETT_SHARE. |
| 54 | `FS.GI.FUND.LEGAL.ENTITY.PAYMENT.PROCESS` | `FsGiFundLegalEntity_PaymentProcess` | TField |  | The payment process to be followed for the deals. Multifonds DB Column is PY_PROCESS. |
| 55 | `FS.GI.FUND.LEGAL.ENTITY.DOCUMENT.HANDLING` | `FsGiFundLegalEntity_DocumentHandling` | TField |  | Swift document handling details for theNon Swift Trigger ID &apos;0008-generic static data change&apos;. Multifonds DB Column is DOC_HANDLING. |
| 56 | `FS.GI.FUND.LEGAL.ENTITY.CUSTODIAN` | `FsGiFundLegalEntity_Custodian` | TField |  | It specifies if the custodian is internal or external. Multifonds DB Column is CUSTODIAN. |
| 57 | `FS.GI.FUND.LEGAL.ENTITY.CREDITOR.ID` | `FsGiFundLegalEntity_CreditorId` | TField |  | Creditor ID to identify the institution that collects the money for standing instructions under savings plan functionality. Multifonds DB Column is CREDITOR_ID. |
| 58 | `FS.GI.FUND.LEGAL.ENTITY.GL.FLOW.ID` | `FsGiFundLegalEntity_GlFlowId` | TField |  | General Ledger Flow ID linked to the Legal Entity. Multifonds DB Column is GL_FLOW_ID. |
| 59 | `FS.GI.FUND.LEGAL.ENTITY.RETRO.CASH.DB.PER.FUNDS.FLAG` | `FsGiFundLegalEntity_RetroCashDbPerFundsFlag` | TField |  | Flag to enable hierarchy mechanism to retrieve the retrocession debit account to be used for retrocession payment. Multifonds DB Column is FLG_RET_CASH_DB_FUNDS. |
| 60 | `FS.GI.FUND.LEGAL.ENTITY.GL.ACCOUNT.GROUP.ID` | `FsGiFundLegalEntity_GlAccountGroupId` | TField |  | General Ledger Accounts group linked to the Legal Entity. Multifonds DB Column is GL_ACCT_GROUP_ID. |
| 61 | `FS.GI.FUND.LEGAL.ENTITY.CONTRACT.NOTES.DETAILS` | `FsGiFundLegalEntity_ContractNotesDetails` | TField |  | Flag to allow populating additional information in contract note such as contract date and time,valuation point etc,. Multifonds DB Column is FLG_CN_DETAIL. |
| 62 | `FS.GI.FUND.LEGAL.ENTITY.SALESMAN.MANDATORY.FLAG` | `FsGiFundLegalEntity_SalesmanMandatoryFlag` | TField | Yes | Flag to allow parameterization of a salesman for all registers willing to invest in funds linked to the Legal Entity mandatory. Multifonds DB Column is FLG_SMAN. |
| 63 | `FS.GI.FUND.LEGAL.ENTITY.SALESWATCH.ENABLED.FLAG` | `FsGiFundLegalEntity_SaleswatchEnabledFlag` | TField | Yes | Flag to allow parameterization of saleswatch type for dealing agents of registers linked to the Legal Entity mandatory. Multifonds DB Column is FLG_SWATCH. |
| 64 | `FS.GI.FUND.LEGAL.ENTITY.REDEEM.SETTLED.SHARES.FLAG` | `FsGiFundLegalEntity_RedeemSettledSharesFlag` | TField |  | Flag to allow redemption of only settled shares at order entry level. Multifonds DB Column is FLG_REDEEM. |
| 65 | `FS.GI.FUND.LEGAL.ENTITY.DB.PEND.ORD.FOR.EST.POS.FLAG` | `FsGiFundLegalEntity_DbPendOrdForEstPosFlag` | TField |  | Flag to allow including the pending debit orders for position calculation. Multifonds DB Column is FLG_ALL_DB_PENDING. |
| 66 | `FS.GI.FUND.LEGAL.ENTITY.PARTIAL.SETTLEMENT.SUBS.FLAG` | `FsGiFundLegalEntity_PartialSettlementSubsFlag` | TField |  | Flag to enable partial settlement functionality. Multifonds DB Column is FLG_PART_SETT_SUB. |
| 67 | `FS.GI.FUND.LEGAL.ENTITY.STP.CANCEL.REV.VIA.INTF.FLAG` | `FsGiFundLegalEntity_StpCancelRevViaIntfFlag` | TField |  | Flag to allow STP cancel/reversal via interface. Multifonds DB Column is FLG_STP_OCR. |
| 68 | `FS.GI.FUND.LEGAL.ENTITY.BACKDATED.REV.CTL.FLAG` | `FsGiFundLegalEntity_BackdatedRevCtlFlag` | TField |  | Flag to block backdated and reversal orders. Multifonds DB Column is FLG_BACK_REV_CTRL. |
| 69 | `FS.GI.FUND.LEGAL.ENTITY.BACKDATED.REV.REPROC.FLAG` | `FsGiFundLegalEntity_BackdatedRevReprocFlag` | TField |  | Flag to enable reprocessing of contract linkages for all debit contracts after a backdated transaction or reversal of a historical contract. Multifonds DB Column is FLG_BACK_REV_REPROCESS. |
| 70 | `FS.GI.FUND.LEGAL.ENTITY.AGENT.ORDER.OVERRIDE.FLAG` | `FsGiFundLegalEntity_AgentOrderOverrideFlag` | TField |  | Flag to allow override of agent at order entry level. Multifonds DB Column is FLG_OVERRIDE_NOUTLET. |
| 71 | `FS.GI.FUND.LEGAL.ENTITY.PHONE.DEALING.FLAG` | `FsGiFundLegalEntity_PhoneDealingFlag` | TField |  | Flag to enable phone dealing functionality for all underlying funds. Multifonds DB Column is FLG_PHONE_DEAL. |
| 72 | `FS.GI.FUND.LEGAL.ENTITY.CTV.CONTROL.FLAG` | `FsGiFundLegalEntity_CtvControlFlag` | TField |  | Flag to check at simulation level if the trade limitations set up at MF fund level have been overcome. Multifonds DB Column is CTV_CONTROL. |
| 73 | `FS.GI.FUND.LEGAL.ENTITY.CHECK.ON.REGISTER.POS.FLAG` | `FsGiFundLegalEntity_CheckOnRegisterPosFlag` | TField |  | Flag to allow first subscription limits to be applied when a register without current holdings re-subscribes. Multifonds DB Column is FLG_CHK_REG_POS. |
| 74 | `FS.GI.FUND.LEGAL.ENTITY.POS.CHECK.AT.DIV.CONF.FLAG` | `FsGiFundLegalEntity_PosCheckAtDivConfFlag` | TField |  | Flag to allow automatic payout of the dividends and daily dividends irrespective of the reinvestment instruction set up. Multifonds DB Column is FLG_POS_CHECK. |
| 75 | `FS.GI.FUND.LEGAL.ENTITY.ERISA.CHECK.FLAG` | `FsGiFundLegalEntity_ErisaCheckFlag` | TField |  | Flag define whether ERISA check should be done for investors investing in the funds linked to the Legal Entity. Multifonds DB Column is FLG_ERISA_CHECK. |
| 76 | `FS.GI.FUND.LEGAL.ENTITY.AMEND.PAYMENT.FLAG` | `FsGiFundLegalEntity_AmendPaymentFlag` | TField |  | Flag to allow amending the payment information generated. Multifonds DB Column is FLG_AMEND_PYMT. |
| 77 | `FS.GI.FUND.LEGAL.ENTITY.SOFT.CLOSURE.SWITCH.FLAG` | `FsGiFundLegalEntity_SoftClosureSwitchFlag` | TField |  | Flag to enable soft closure only for the switches between different Legal Entities. Multifonds DB Column is FLG_SOFT_CLOSURES. |
| 78 | `FS.GI.FUND.LEGAL.ENTITY.NAV.VALIDITY.PF.CONTROL.FLAG` | `FsGiFundLegalEntity_NavValidityPfControlFlag` | TField |  | Flag to block performance fee calculation if the NAV for a performance fee fund is not equal to (GAV - Performance fee). Multifonds DB Column is FLG_NAV_CONTROL. |
| 79 | `FS.GI.FUND.LEGAL.ENTITY.MIN.LIMITS.MONITORING.FLAG` | `FsGiFundLegalEntity_MinLimitsMonitoringFlag` | TField |  | Flag allows to check the minimum transaction limit at order level. Multifonds DB Column is FLG_MIN_LMT_MON. |
| 80 | `FS.GI.FUND.LEGAL.ENTITY.INTER.LE.SWITCHES.RESTR.FLAG` | `FsGiFundLegalEntity_InterLeSwitchesRestrFlag` | TField |  | Flag allows to block the switch between two funds linked to different Legal Entities. Multifonds DB Column is FLG_INT_TFC_SWITCH. |
| 81 | `FS.GI.FUND.LEGAL.ENTITY.CDSC.WRITE.DOWN.FLAG` | `FsGiFundLegalEntity_CdscWriteDownFlag` | TField |  | Flag to activate reporting functionality for CDSC bucket share classes. Multifonds DB Column is FLG_CDSC_WRDN. |
| 82 | `FS.GI.FUND.LEGAL.ENTITY.FX.REVERSAL.FLAG` | `FsGiFundLegalEntity_FxReversalFlag` | TField |  | Flag to include reversed/cancelled order in the client trading desk report. Multifonds DB Column is FLG_FX_REV. |
| 83 | `FS.GI.FUND.LEGAL.ENTITY.FX.EXPORTING.FLAG` | `FsGiFundLegalEntity_FxExportingFlag` | TField |  | Flag to enable export of forex deals. Multifonds DB Column is FLG_FX_EXPRT. |
| 84 | `FS.GI.FUND.LEGAL.ENTITY.BLOCK.ORDER.DELETION.FLAG` | `FsGiFundLegalEntity_BlockOrderDeletionFlag` | TField |  | Flag to activate blocking the order from deletion functionality. Multifonds DB Column is FLG_BLK_ORD_DEL. |
| 85 | `FS.GI.FUND.LEGAL.ENTITY.OVER.CONV.FLAG` | `FsGiFundLegalEntity_OverConvFlag` | TField |  | Flag to allow override of conversion flag at Manager Application screen. Multifonds DB Column is FLG_OVER_CONV. |
| 86 | `FS.GI.FUND.LEGAL.ENTITY.ACC.OPENING.NOTICE.FLAG` | `FsGiFundLegalEntity_AccOpeningNoticeFlag` | TField |  | Flag to send account opening notice for Legal Entity. Multifonds DB Column is FLG_ACC_OPEN_NOTICE. |
| 87 | `FS.GI.FUND.LEGAL.ENTITY.SAME.TD.FOR.FOF.TRANS.FLAG` | `FsGiFundLegalEntity_SameTdForFofTransFlag` | TField |  | Flag to calculate common valid trade date for the Fund of fund structures at order entry level. Multifonds DB Column is FLG_SAME_TD_FOF. |
| 88 | `FS.GI.FUND.LEGAL.ENTITY.PROFIT.LOSS.METHOD` | `FsGiFundLegalEntity_ProfitLossMethod` | TField |  | Method for calculation profit/loss. Multifonds DB Column is PL_METHOD. |
| 89 | `FS.GI.FUND.LEGAL.ENTITY.SEL.OPER.CODES.FUND.TDSK.FLAG` | `FsGiFundLegalEntity_SelOperCodesFundTdskFlag` | TField |  | Flag to enable the selection of operation codes for fund trading desk. Multifonds DB Column is FLG_OPR_FUND_TDSK. |
| 90 | `FS.GI.FUND.LEGAL.ENTITY.MANAGEMENT.COMMISSION.FLAG` | `FsGiFundLegalEntity_ManagementCommissionFlag` | TField |  | Flag allows the agent commission calculated for &apos;Agent Type&apos; - &apos;0010&apos;(Management Company) to be paid to the management company. Multifonds DB Column is FLG_MANAGE_COMM. |
| 91 | `FS.GI.FUND.LEGAL.ENTITY.AUTO.FUND.TRADING.DESK.FLAG` | `FsGiFundLegalEntity_AutoFundTradingDeskFlag` | TField |  | Flag to enable automatic fund trading desk process for the exchange group linked to Legal Entity. Multifonds DB Column is FLG_AUTO_FUND_TDSK. |
| 92 | `FS.GI.FUND.LEGAL.ENTITY.GDPR.INFORM.DATE` | `FsGiFundLegalEntity_GdprInformDate` | TField |  | Date when GDPR was informed. Multifonds DB Column is GDPR_DINFORMED_ON. |
| 93 | `FS.GI.FUND.LEGAL.ENTITY.GLOBAL.ORDERING.FLAG` | `FsGiFundLegalEntity_GlobalOrderingFlag` | TField |  | Flag to enable global ordering functionality. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 94 | `FS.GI.FUND.LEGAL.ENTITY.EXTERNAL.TA.ID` | `FsGiFundLegalEntity_ExternalTaId` | TField |  | External TA linked to the Legal Entity. Multifonds DB Column is EXTERNAL_TA. |
| 95 | `FS.GI.FUND.LEGAL.ENTITY.TRANSFER.AGENT` | `FsGiFundLegalEntity_TransferAgent` | TField |  | It specifies if the management company is administrated inside the transfer agency or as external. Multifonds DB Column is TA_TFC. |
| 96 | `FS.GI.FUND.LEGAL.ENTITY.CASH.DIVIDEND.REGISTER.ID` | `FsGiFundLegalEntity_CashDividendRegisterId` | TField | Yes | Technical register for cash dividend. This field is mandatory when the global ordering flag is ticked. Multifonds DB Column is NREGISTER_CASH_DIV. |
| 97 | `FS.GI.FUND.LEGAL.ENTITY.TRANSACTION.BULKING.NETTING` | `FsGiFundLegalEntity_TransactionBulkingNetting` | TField |  | Transaction bulking or netting code of cash movements. Multifonds DB Column is TRNS_BULK_NET. |
| 98 | `FS.GI.FUND.LEGAL.ENTITY.REINVESTMENT.REGISTER.ID` | `FsGiFundLegalEntity_ReinvestmentRegisterId` | TField | Yes | Technical register for reinvestment. This field is mandatory when the global ordering flag is ticked. Multifonds DB Column is NREGISTER_REINVEST. |
| 99 | `FS.GI.FUND.LEGAL.ENTITY.COLLECTION.ACCOUNT.GROUP` | `FsGiFundLegalEntity_CollectionAccountGroup` | TField |  | Collection account group code used to group deals and receipts that can be matched together. Multifonds DB Column is COLL_ACC_GRP. |
| 100 | `FS.GI.FUND.LEGAL.ENTITY.MATCHING.TOLERANCE.AMOUNT` | `FsGiFundLegalEntity_MatchingToleranceAmount` | TField |  | Tolerance amount applicable for cash receipts matching. Multifonds DB Column is TOLERANCE_AMT. |
| 101 | `FS.GI.FUND.LEGAL.ENTITY.SETTLEMENT.DATE` | `FsGiFundLegalEntity_SettlementDate` | TField |  | Behavior of the settlement date update during cash receipt matching. Multifonds DB Column is SETTLEMENT_DATE. |
| 102 | `FS.GI.FUND.LEGAL.ENTITY.IMR.FLAG` | `FsGiFundLegalEntity_ImrFlag` | TField |  | Flag to activate Investor Money Regulation functionality. Multifonds DB Column is FLG_IMR. |
| 103 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.STATUS` | `FsGiFundLegalEntity_FatcaStatus` | TField |  | FATCA Status of the Legal Entity. Multifonds DB Column is FAT_STATUS. |
| 104 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.MODEL` | `FsGiFundLegalEntity_FatcaModel` | TField |  | IGA Model for FATCA purposes. Multifonds DB Column is FAT_MODEL. |
| 105 | `FS.GI.FUND.LEGAL.ENTITY.GIIN.NUMBER` | `FsGiFundLegalEntity_GiinNumber` | TField |  | FATCA Global Internediaery Identification Number. Multifonds DB Column is FAT_GIIN. |
| 106 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.EFFECTIVE.DATE` | `FsGiFundLegalEntity_FatcaEffectiveDate` | TField |  | FATCA effective date. Multifonds DB Column is FAT_DEFFECTIVE. |
| 107 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.EXPIRY.DATE` | `FsGiFundLegalEntity_FatcaExpiryDate` | TField |  | FATCA expiry date. Multifonds DB Column is FAT_DEXPIRY. |
| 108 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.SERVICE.OFFERING` | `FsGiFundLegalEntity_FatcaServiceOffering` | TField |  | The entity responsible for the due diligence which is used for reporting to Internal Revenue Service. Multifonds DB Column is FAT_SERV_OFFER. |
| 109 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.REVOKE.DATE` | `FsGiFundLegalEntity_FatcaRevokeDate` | TField |  | FATCA revoke date. Multifonds DB Column is FAT_DREVOKE. |
| 110 | `FS.GI.FUND.LEGAL.ENTITY.FATCA.EXEMPTION.REASON` | `FsGiFundLegalEntity_FatcaExemptionReason` | TField |  | Fatca excemption reason of the Legal Entity. Multifonds DB Column is FAT_EXEM_REASON. |
| 111 | `FS.GI.FUND.LEGAL.ENTITY.SPONSORING.ENTITY.ID` | `FsGiFundLegalEntity_SponsoringEntityId` | TField |  | FATCA sponsoring entity. Multifonds DB Column is FAT_SPONSOR. |
| 112 | `FS.GI.FUND.LEGAL.ENTITY.CRS.STATUS` | `FsGiFundLegalEntity_CrsStatus` | TField |  | CRS status. Multifonds DB Column is CRS_STATUS. |
| 113 | `FS.GI.FUND.LEGAL.ENTITY.JURISDICTION` | `FsGiFundLegalEntity_Jurisdiction` | TField |  | Legal Entity jurisdiction country for FATCA reporting purposes. Multifonds DB Column is JURISDICTION. |
| 114 | `FS.GI.FUND.LEGAL.ENTITY.TAX.ID.NUMBER` | `FsGiFundLegalEntity_TaxIdNumber` | TField |  | Tax Identifier Number for FATCA reporting purposes. Multifonds DB Column is TIN_NUMBER. |
| 115 | `FS.GI.FUND.LEGAL.ENTITY.DEPOSITOR.ID` | `FsGiFundLegalEntity_DepositorId` | TField |  | Depositor linked to the Legal Entity. Multifonds DB Column is DEPOSITOR. |
| 116 | `FS.GI.FUND.LEGAL.ENTITY.CANC.LOSS.THRESHOLD` | `FsGiFundLegalEntity_CancLossThreshold` | TField |  | Threshold whithin which Legal Entity will bear the loss arising out of cancellation of buy deal. Multifonds DB Column is NLOSSTHRESH. |
| 117 | `FS.GI.FUND.LEGAL.ENTITY.CANC.LOSS.THRESHOLD.CURRENCY` | `FsGiFundLegalEntity_CancLossThresholdCurrency` | TField |  | The currency code (in 3 letter ISO code, Eg: EUR) for threshold calculation related to cancellation rights functionality. Multifonds DB Column is CCY_THRESH. |
| 118 | `FS.GI.FUND.LEGAL.ENTITY.FIRST.TRS.MIN.LIMIT.CURRENCY` | `FsGiFundLegalEntity_FirstTrsMinLimitCurrency` | TField |  | The currency of the minimum limit for first transaction. Multifonds DB Column is CMON_MIN. |
| 119 | `FS.GI.FUND.LEGAL.ENTITY.AUTO.PAY.FLAG` | `FsGiFundLegalEntity_AutoPayFlag` | TField |  | Flag to allow automatic simulation of payments Multifonds DB Column is FLG_AUTO_PAY. |
| 120 | `FS.GI.FUND.LEGAL.ENTITY.MATCHING.TOLERANCE.CURRENCY` | `FsGiFundLegalEntity_MatchingToleranceCurrency` | TField |  | Tolerance amount currency applicable for cash receipts matching. Multifonds DB Column is TOLERANCE_CCY. |
| 121 | `FS.GI.FUND.LEGAL.ENTITY.UPDATE.FROM.FUND.PROMOTER` | `FsGiFundLegalEntity_UpdateFromFundPromoter` | TField |  | The model used to update the Legal Entity based on the Fund Promoter fields. Multifonds DB Column is UPDATE_FP. |
| 122 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED10` | `FsGiFundLegalEntity_Reserved10` | TField |  |  |
| 123 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED9` | `FsGiFundLegalEntity_Reserved9` | TField |  |  |
| 124 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED8` | `FsGiFundLegalEntity_Reserved8` | TField |  |  |
| 125 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED7` | `FsGiFundLegalEntity_Reserved7` | TField |  |  |
| 126 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED6` | `FsGiFundLegalEntity_Reserved6` | TField |  |  |
| 127 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED5` | `FsGiFundLegalEntity_Reserved5` | TField |  |  |
| 128 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED4` | `FsGiFundLegalEntity_Reserved4` | TField |  |  |
| 129 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED3` | `FsGiFundLegalEntity_Reserved3` | TField |  |  |
| 130 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED2` | `FsGiFundLegalEntity_Reserved2` | TField |  |  |
| 131 | `FS.GI.FUND.LEGAL.ENTITY.RESERVED1` | `FsGiFundLegalEntity_Reserved1` | TField |  |  |
| 132 | `FS.GI.FUND.LEGAL.ENTITY.LOCAL.REF` | `FsGiFundLegalEntity_LocalRef` |  |  |  |
| 133 | `FS.GI.FUND.LEGAL.ENTITY.OVERRIDE` | `FsGiFundLegalEntity_Override` |  |  |  |
| 134 | `FS.GI.FUND.LEGAL.ENTITY.RECORD.STATUS` | `FsGiFundLegalEntity_RecordStatus` | String |  |  |
| 135 | `FS.GI.FUND.LEGAL.ENTITY.CURR.NO` | `FsGiFundLegalEntity_CurrNo` | String |  |  |
| 136 | `FS.GI.FUND.LEGAL.ENTITY.INPUTTER` | `FsGiFundLegalEntity_Inputter` |  |  |  |
| 137 | `FS.GI.FUND.LEGAL.ENTITY.DATE.TIME` | `FsGiFundLegalEntity_DateTime` |  |  |  |
| 138 | `FS.GI.FUND.LEGAL.ENTITY.AUTHORISER` | `FsGiFundLegalEntity_Authoriser` | String |  |  |
| 139 | `FS.GI.FUND.LEGAL.ENTITY.CO.CODE` | `FsGiFundLegalEntity_CoCode` | String |  |  |
| 140 | `FS.GI.FUND.LEGAL.ENTITY.DEPT.CODE` | `FsGiFundLegalEntity_DeptCode` | String |  |  |
| 141 | `FS.GI.FUND.LEGAL.ENTITY.AUDITOR.CODE` | `FsGiFundLegalEntity_AuditorCode` | String |  |  |
| 142 | `FS.GI.FUND.LEGAL.ENTITY.AUDIT.DATE.TIME` | `FsGiFundLegalEntity_AuditDateTime` | String |  |  |
