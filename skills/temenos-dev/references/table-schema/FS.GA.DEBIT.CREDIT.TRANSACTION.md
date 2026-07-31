# FS.GA.DEBIT.CREDIT.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEBIT.CREDIT.TRANSACTION` in `FS_DebitCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEBIT.CREDIT.TRANSACTION.PARENT.REF.ID` | `FsGaDebitCreditTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DEBIT.CREDIT.TRANSACTION.ORA.ROWID` | `FsGaDebitCreditTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DEBIT.CREDIT.TRANSACTION.FUND.ID` | `FsGaDebitCreditTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.DEBIT.CREDIT.TRANSACTION.TRANSACTION.NUMBER` | `FsGaDebitCreditTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.DEBIT.CREDIT.TRANSACTION.LINE` | `FsGaDebitCreditTransaction_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 6 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GL.ACCOUNT` | `FsGaDebitCreditTransaction_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 7 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GL.ACCOUNT.SUFFIX` | `FsGaDebitCreditTransaction_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 8 | `FS.GA.DEBIT.CREDIT.TRANSACTION.PAY.DATE` | `FsGaDebitCreditTransaction_PayDate` | TField |  | Pay Date Multifonds DB Column is DVAL. |
| 9 | `FS.GA.DEBIT.CREDIT.TRANSACTION.DESCRIPTION` | `FsGaDebitCreditTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 10 | `FS.GA.DEBIT.CREDIT.TRANSACTION.LOCAL.CURRENCY` | `FsGaDebitCreditTransaction_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 11 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaDebitCreditTransaction_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 12 | `FS.GA.DEBIT.CREDIT.TRANSACTION.REFERENCE.CCY` | `FsGaDebitCreditTransaction_ReferenceCcy` | TField |  | Reference Currency Multifonds DB Column is CMON_BASE. |
| 13 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AMOUNT.IN.REFERENCE.CURRENCY` | `FsGaDebitCreditTransaction_AmountInReferenceCurrency` | TField |  | Amount In Reference Currency Multifonds DB Column is MONT_BASE. |
| 14 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RATE.OF.EXCHANGE` | `FsGaDebitCreditTransaction_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 15 | `FS.GA.DEBIT.CREDIT.TRANSACTION.DEBIT.CREDIT.INDICATOR` | `FsGaDebitCreditTransaction_DebitCreditIndicator` | TField |  | Debit credit indicator tagged to an account number Multifonds DB Column is CSENS. |
| 16 | `FS.GA.DEBIT.CREDIT.TRANSACTION.OPERATION.CODE` | `FsGaDebitCreditTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 17 | `FS.GA.DEBIT.CREDIT.TRANSACTION.TRADE.DATE` | `FsGaDebitCreditTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 18 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SETTLE.DATE` | `FsGaDebitCreditTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 19 | `FS.GA.DEBIT.CREDIT.TRANSACTION.ACCOUNTING.DATE` | `FsGaDebitCreditTransaction_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 20 | `FS.GA.DEBIT.CREDIT.TRANSACTION.STATUS.CODE` | `FsGaDebitCreditTransaction_StatusCode` | TField |  | Status Code Multifonds DB Column is STATUS. |
| 21 | `FS.GA.DEBIT.CREDIT.TRANSACTION.ARCHIVE` | `FsGaDebitCreditTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 22 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SERVICE.CODE` | `FsGaDebitCreditTransaction_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 23 | `FS.GA.DEBIT.CREDIT.TRANSACTION.MANAGER.ID` | `FsGaDebitCreditTransaction_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 24 | `FS.GA.DEBIT.CREDIT.TRANSACTION.MANAGER.CODE` | `FsGaDebitCreditTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 25 | `FS.GA.DEBIT.CREDIT.TRANSACTION.STATUS.PENDING` | `FsGaDebitCreditTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 26 | `FS.GA.DEBIT.CREDIT.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaDebitCreditTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 27 | `FS.GA.DEBIT.CREDIT.TRANSACTION.DEPOSITORY.BANK.CODE` | `FsGaDebitCreditTransaction_DepositoryBankCode` | TField |  | Position for check status is used: if its &quot;Y&quot; then the load INSERTS a new line in the operation code equivalence. If its &quot;N&quot; then the load amends an already existing line in the op code equiv screen. Multifonds DB Column is CODE_DEP_BANK. |
| 28 | `FS.GA.DEBIT.CREDIT.TRANSACTION.INTERNAL.SECURITY.ID` | `FsGaDebitCreditTransaction_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 29 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CHARGE.CODE` | `FsGaDebitCreditTransaction_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 30 | `FS.GA.DEBIT.CREDIT.TRANSACTION.FUND.STRATEGY` | `FsGaDebitCreditTransaction_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 31 | `FS.GA.DEBIT.CREDIT.TRANSACTION.FUND.LINK.ID` | `FsGaDebitCreditTransaction_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 32 | `FS.GA.DEBIT.CREDIT.TRANSACTION.REPRISE` | `FsGaDebitCreditTransaction_Reprise` | TField |  | Reprise Identifier Multifonds DB Column is FLG_REPRISE. |
| 33 | `FS.GA.DEBIT.CREDIT.TRANSACTION.PA.IDENTIFIER` | `FsGaDebitCreditTransaction_PaIdentifier` | TField |  | PA Identifier Multifonds DB Column is FLG_PA. |
| 34 | `FS.GA.DEBIT.CREDIT.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaDebitCreditTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 35 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CHECK.DATE` | `FsGaDebitCreditTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 36 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CHECKED.BY` | `FsGaDebitCreditTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 37 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SPECIFIC.JOURNAL.ID` | `FsGaDebitCreditTransaction_SpecificJournalId` | TField |  | Specific Journal ID Multifonds DB Column is SPECIFIC_J_ID. |
| 38 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SHARE.CLASS.CODE` | `FsGaDebitCreditTransaction_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 39 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SERVICE.CODE.PA` | `FsGaDebitCreditTransaction_ServiceCodePa` | TField |  | Service Code PA Multifonds DB Column is CSERVICE_PA. |
| 40 | `FS.GA.DEBIT.CREDIT.TRANSACTION.ENTRY.NUMBER.PA` | `FsGaDebitCreditTransaction_EntryNumberPa` | TField |  | Entry Number PA Multifonds DB Column is NECRITUR_PA. |
| 41 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AMOUNT.3.DECIMAL` | `FsGaDebitCreditTransaction_Amount3Decimal` | TField |  | This field corresponds to the 3 decimal functionality of the amount Multifonds DB Column is MONTANT_3DEC. |
| 42 | `FS.GA.DEBIT.CREDIT.TRANSACTION.EXCHANGE.RATE.TRANSACTION.PAY` | `FsGaDebitCreditTransaction_ExchangeRateTransactionPay` | TField |  | Exchange Rate Transaction Pay Multifonds DB Column is TRANPAY_TCHG. |
| 43 | `FS.GA.DEBIT.CREDIT.TRANSACTION.LOCAL.BOOK.EXCHANGE.RATE` | `FsGaDebitCreditTransaction_LocalBookExchangeRate` | TField |  | Local Book Exchange Rate Multifonds DB Column is LOCALBOOK_TCHG. |
| 44 | `FS.GA.DEBIT.CREDIT.TRANSACTION.COUNTERPARTY.CORRESPONDENT` | `FsGaDebitCreditTransaction_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 45 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.CLAIM.ID` | `FsGaDebitCreditTransaction_GstClaimId` | TField |  | GST Claim ID Multifonds DB Column is GST_CLAIM_ID. |
| 46 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.UPDATED.DATE` | `FsGaDebitCreditTransaction_GstUpdatedDate` | TField |  | GST Updated date Multifonds DB Column is GST_DUPDATED. |
| 47 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.UPDATED.BY` | `FsGaDebitCreditTransaction_GstUpdatedBy` | TField |  | GST Updated By Multifonds DB Column is GST_UPDATED_BY. |
| 48 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.CONFIRMATION` | `FsGaDebitCreditTransaction_GstConfirmation` | TField |  | GST Confirmation Multifonds DB Column is GST_CONFIRM. |
| 49 | `FS.GA.DEBIT.CREDIT.TRANSACTION.FEE.CODE` | `FsGaDebitCreditTransaction_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 50 | `FS.GA.DEBIT.CREDIT.TRANSACTION.IDENTIFIER.TYPE` | `FsGaDebitCreditTransaction_IdentifierType` | TField |  | Corresponds to Idenfier Code type like security,Future,option and Industry type Multifonds DB Column is ID_TYPE. |
| 51 | `FS.GA.DEBIT.CREDIT.TRANSACTION.ID.CODE` | `FsGaDebitCreditTransaction_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 52 | `FS.GA.DEBIT.CREDIT.TRANSACTION.EXTERNAL.SECURITY.ID` | `FsGaDebitCreditTransaction_ExternalSecurityId` | TField |  | The External identification code for Security like 01 for Telekurs, 03 for Sedol. Also used for other provider identifiers Multifonds DB Column is SEC_ID. |
| 53 | `FS.GA.DEBIT.CREDIT.TRANSACTION.DESCRIPTION.OF.SECURITY` | `FsGaDebitCreditTransaction_DescriptionOfSecurity` | TField |  | Description Of Security Multifonds DB Column is XLIBVAL. |
| 54 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.REVISED.CLAIM.ID` | `FsGaDebitCreditTransaction_GstRevisedClaimId` | TField |  | GST Revised Claim ID Multifonds DB Column is GST_CLAIM_ID_REV. |
| 55 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.REVISED.UPDATED.BY` | `FsGaDebitCreditTransaction_GstRevisedUpdatedBy` | TField |  | GST Revised Updated By Multifonds DB Column is GST_UPDATED_BY_REV. |
| 56 | `FS.GA.DEBIT.CREDIT.TRANSACTION.GST.REVISED.UPDATED.DATE` | `FsGaDebitCreditTransaction_GstRevisedUpdatedDate` | TField |  | GST Revised Updated Date Multifonds DB Column is GST_DUPDATED_REV. |
| 57 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AMOUNT.IN.FUND.CURRENCY` | `FsGaDebitCreditTransaction_AmountInFundCurrency` | TField |  | Amount In Fund Currency Multifonds DB Column is MONTANT_PTF. |
| 58 | `FS.GA.DEBIT.CREDIT.TRANSACTION.INSTRUMENT.ID.CODE` | `FsGaDebitCreditTransaction_InstrumentIdCode` | TField |  | This field displays instrument code Multifonds DB Column is INSTRUMENTCODE. |
| 59 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SUB.INSTRUMENT.CODE` | `FsGaDebitCreditTransaction_SubInstrumentCode` | TField |  | Sub Instrument Code Multifonds DB Column is SUBINSTRUMENTCODE. |
| 60 | `FS.GA.DEBIT.CREDIT.TRANSACTION.INSTRUMENT.GROUPS` | `FsGaDebitCreditTransaction_InstrumentGroups` | TField |  | Instrument Groups Multifonds DB Column is INSTRUMENTGROUP. |
| 61 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CUSTODIAN.ACCOUNT` | `FsGaDebitCreditTransaction_CustodianAccount` | TField |  | Custodian Account Multifonds DB Column is CUSTODIANACCOUNT. |
| 62 | `FS.GA.DEBIT.CREDIT.TRANSACTION.TAX.LOT.TYPE` | `FsGaDebitCreditTransaction_TaxLotType` | TField |  | Tax Lot Type Multifonds DB Column is TAXLOTTYPE. |
| 63 | `FS.GA.DEBIT.CREDIT.TRANSACTION.INVENTORY.STATE` | `FsGaDebitCreditTransaction_InventoryState` | TField |  | Inventory State Multifonds DB Column is INVENTORYSTATE. |
| 64 | `FS.GA.DEBIT.CREDIT.TRANSACTION.TRADE.ID` | `FsGaDebitCreditTransaction_TradeId` | TField |  | Trade Id Multifonds DB Column is TRADEID. |
| 65 | `FS.GA.DEBIT.CREDIT.TRANSACTION.LOT.ID` | `FsGaDebitCreditTransaction_LotId` | TField |  | Lot ID Multifonds DB Column is LOTID. |
| 66 | `FS.GA.DEBIT.CREDIT.TRANSACTION.QUANTITIES` | `FsGaDebitCreditTransaction_Quantities` | TField |  | Quantities Multifonds DB Column is QUANTITY. |
| 67 | `FS.GA.DEBIT.CREDIT.TRANSACTION.TYPE.OF.ACCOUNT.NUMBER` | `FsGaDebitCreditTransaction_TypeOfAccountNumber` | TField |  | Account type. Only 2 expected values: Standard or Notional Multifonds DB Column is GLACCOUNTTYPE. |
| 68 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CUSTOM.FIELD.1` | `FsGaDebitCreditTransaction_CustomField1` | TField |  | Custom Field 1 Multifonds DB Column is CUSTOMFIELD1. |
| 69 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CUSTOM.FIELD.2` | `FsGaDebitCreditTransaction_CustomField2` | TField |  | Custom Field 2 Multifonds DB Column is CUSTOMFIELD2. |
| 70 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CUSTOM.FIELD.3` | `FsGaDebitCreditTransaction_CustomField3` | TField |  | Custom Field 3 Multifonds DB Column is CUSTOMFIELD3. |
| 71 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BALANCE.SHEET.GROUPING` | `FsGaDebitCreditTransaction_BalanceSheetGrouping` | TField |  | Balancesheet Group Multifonds DB Column is BSGROUP. |
| 72 | `FS.GA.DEBIT.CREDIT.TRANSACTION.ASSET.CATEGORY` | `FsGaDebitCreditTransaction_AssetCategory` | TField |  | Asset Category Multifonds DB Column is ASSETCATEGORY. |
| 73 | `FS.GA.DEBIT.CREDIT.TRANSACTION.KNOWLEDGE.DATE` | `FsGaDebitCreditTransaction_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 74 | `FS.GA.DEBIT.CREDIT.TRANSACTION.SUB.CUSTODIAN.ACCOUNT` | `FsGaDebitCreditTransaction_SubCustodianAccount` | TField |  | Sub Custodian Account Multifonds DB Column is SUBCUSTODIANACCOUNT. |
| 75 | `FS.GA.DEBIT.CREDIT.TRANSACTION.END.TAG.INDERTIFIER` | `FsGaDebitCreditTransaction_EndTagIndertifier` | TField |  | End Tag Identifier Multifonds DB Column is FLG_END_TAG. |
| 76 | `FS.GA.DEBIT.CREDIT.TRANSACTION.OPERATION.TYPE` | `FsGaDebitCreditTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 77 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED10` | `FsGaDebitCreditTransaction_Reserved10` | TField |  |  |
| 78 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED9` | `FsGaDebitCreditTransaction_Reserved9` | TField |  |  |
| 79 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED8` | `FsGaDebitCreditTransaction_Reserved8` | TField |  |  |
| 80 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED7` | `FsGaDebitCreditTransaction_Reserved7` | TField |  |  |
| 81 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED6` | `FsGaDebitCreditTransaction_Reserved6` | TField |  |  |
| 82 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED5` | `FsGaDebitCreditTransaction_Reserved5` | TField |  |  |
| 83 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED4` | `FsGaDebitCreditTransaction_Reserved4` | TField |  |  |
| 84 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED3` | `FsGaDebitCreditTransaction_Reserved3` | TField |  |  |
| 85 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED2` | `FsGaDebitCreditTransaction_Reserved2` | TField |  |  |
| 86 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RESERVED1` | `FsGaDebitCreditTransaction_Reserved1` | TField |  |  |
| 87 | `FS.GA.DEBIT.CREDIT.TRANSACTION.LOCAL.REF` | `FsGaDebitCreditTransaction_LocalRef` |  |  |  |
| 88 | `FS.GA.DEBIT.CREDIT.TRANSACTION.OVERRIDE` | `FsGaDebitCreditTransaction_Override` |  |  |  |
| 89 | `FS.GA.DEBIT.CREDIT.TRANSACTION.RECORD.STATUS` | `FsGaDebitCreditTransaction_RecordStatus` | String |  |  |
| 90 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CURR.NO` | `FsGaDebitCreditTransaction_CurrNo` | String |  |  |
| 91 | `FS.GA.DEBIT.CREDIT.TRANSACTION.INPUTTER` | `FsGaDebitCreditTransaction_Inputter` |  |  |  |
| 92 | `FS.GA.DEBIT.CREDIT.TRANSACTION.DATE.TIME` | `FsGaDebitCreditTransaction_DateTime` |  |  |  |
| 93 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AUTHORISER` | `FsGaDebitCreditTransaction_Authoriser` | String |  |  |
| 94 | `FS.GA.DEBIT.CREDIT.TRANSACTION.CO.CODE` | `FsGaDebitCreditTransaction_CoCode` | String |  |  |
| 95 | `FS.GA.DEBIT.CREDIT.TRANSACTION.DEPT.CODE` | `FsGaDebitCreditTransaction_DeptCode` | String |  |  |
| 96 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AUDITOR.CODE` | `FsGaDebitCreditTransaction_AuditorCode` | String |  |  |
| 97 | `FS.GA.DEBIT.CREDIT.TRANSACTION.AUDIT.DATE.TIME` | `FsGaDebitCreditTransaction_AuditDateTime` | String |  |  |
