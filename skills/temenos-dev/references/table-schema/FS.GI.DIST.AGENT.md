# FS.GI.DIST.AGENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT` in `FS_AgentStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.PARENT.REF.ID` | `FsGiDistAgent_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.ORA.ROWID` | `FsGiDistAgent_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.FUND.PROMOTER.ID` | `FsGiDistAgent_FundPromoterId` | TField |  | Fund Promoter ID linked to the Agent Multifonds DB Column is NPROMOTER. |
| 4 | `FS.GI.DIST.AGENT.AGENT.ID` | `FsGiDistAgent_AgentId` | TField |  | Agent Internal ID Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.DIST.AGENT.NAME` | `FsGiDistAgent_Name` | TField |  | Name of the Agent Multifonds DB Column is NAME. |
| 6 | `FS.GI.DIST.AGENT.AGENT.EXTERNAL.ID` | `FsGiDistAgent_AgentExternalId` | TField |  | Agent External ID Multifonds DB Column is SIB_CODE. |
| 7 | `FS.GI.DIST.AGENT.AGENT.TYPE` | `FsGiDistAgent_AgentType` | TField |  | Agent Type Code Multifonds DB Column is OUTLET_TYPE. |
| 8 | `FS.GI.DIST.AGENT.USE.TYPE` | `FsGiDistAgent_UseType` | TField |  | Agent Status code Multifonds DB Column is TYPE_USE. |
| 9 | `FS.GI.DIST.AGENT.PAYMENT.FREQUENCY.CODE` | `FsGiDistAgent_PaymentFrequencyCode` | TField |  | Frequency of commission payment from the Transfer Agent to the agent Multifonds DB Column is FREQUENCY. |
| 10 | `FS.GI.DIST.AGENT.FSA.NUMBER` | `FsGiDistAgent_FsaNumber` | TField |  | The Distributor ID given by the UK Fund Services Regulator Multifonds DB Column is FCA_NO. |
| 11 | `FS.GI.DIST.AGENT.ADDRESS.LINE1` | `FsGiDistAgent_AddressLine1` | TField |  | Address Line 1 Multifonds DB Column is ADRESSE. |
| 12 | `FS.GI.DIST.AGENT.ADDRESS.LINE2` | `FsGiDistAgent_AddressLine2` | TField |  | Address Line 2 Multifonds DB Column is ADDRESS2. |
| 13 | `FS.GI.DIST.AGENT.POSTCODE` | `FsGiDistAgent_Postcode` | TField |  | Postcode of the agent Multifonds DB Column is CVILLE. |
| 14 | `FS.GI.DIST.AGENT.COUNTRY` | `FsGiDistAgent_Country` | TField |  | The agent country code(in 2 letter format eg &apos;LU&apos;) Multifonds DB Column is CPAYS. |
| 15 | `FS.GI.DIST.AGENT.TELEPHONE.NUMBER` | `FsGiDistAgent_TelephoneNumber` | TField |  | Telephone Number Multifonds DB Column is NTEL. |
| 16 | `FS.GI.DIST.AGENT.LANGUAGE.CODE` | `FsGiDistAgent_LanguageCode` | TField |  | Language code Multifonds DB Column is CLANGUE. |
| 17 | `FS.GI.DIST.AGENT.CONTACT.PERSON` | `FsGiDistAgent_ContactPerson` | TField |  | Agent contact person Multifonds DB Column is CONTACT_PERSON. |
| 18 | `FS.GI.DIST.AGENT.MIFID.STATUS` | `FsGiDistAgent_MifidStatus` | TField |  | Status of Agent as per MIFID directives Multifonds DB Column is MIFID_STAT. |
| 19 | `FS.GI.DIST.AGENT.FREE.TEXT1` | `FsGiDistAgent_FreeText1` | TField |  | Free text field that allows upto 150 alpha numerical characters for generic information Multifonds DB Column is TEXT. |
| 20 | `FS.GI.DIST.AGENT.ADVISORY.TYPE` | `FsGiDistAgent_AdvisoryType` | TField |  | The Advisory service type of the Agent Multifonds DB Column is ADVISORY_TYPE. |
| 21 | `FS.GI.DIST.AGENT.MARKETING.CODE` | `FsGiDistAgent_MarketingCode` | TField |  | Marketing code linked to the Agent Multifonds DB Column is MARKET_CODE. |
| 22 | `FS.GI.DIST.AGENT.START.DATE` | `FsGiDistAgent_StartDate` | TField |  | Start date of Distribution Agreement Multifonds DB Column is DATE_DEB. |
| 23 | `FS.GI.DIST.AGENT.END.DATE` | `FsGiDistAgent_EndDate` | TField |  | End date of Distribution Agreement Multifonds DB Column is DATE_FIN. |
| 24 | `FS.GI.DIST.AGENT.NEXT.PAYMENT.DATE` | `FsGiDistAgent_NextPaymentDate` | TField |  | Date of next commission payment Multifonds DB Column is DATE_NEXT_PAYMENT. |
| 25 | `FS.GI.DIST.AGENT.IRREGULAR.START.DATE` | `FsGiDistAgent_IrregularStartDate` | TField |  | Irregular first payment start date Multifonds DB Column is DATE_DEB_IRR. |
| 26 | `FS.GI.DIST.AGENT.IRREGULAR.END.DATE` | `FsGiDistAgent_IrregularEndDate` | TField |  | Irregular first payment end date Multifonds DB Column is DATE_FIN_ERR. |
| 27 | `FS.GI.DIST.AGENT.NSCC.AGENT.TYPE` | `FsGiDistAgent_NsccAgentType` | TField | Yes | NSCC Agent Type code. This field is mandatory only if Agent type is &apos;0006-Main agent&apos; and Settlement type is &apos;0003-NSCC&apos; Multifonds DB Column is STP_OUTLET_TYPE. |
| 28 | `FS.GI.DIST.AGENT.TAX.NUMBER` | `FsGiDistAgent_TaxNumber` | TField | Yes | Tax number Field is mandatory when country of residence has been defined as &apos;Tax No. mandatory&apos; for clients in the &apos;ZWIST calculation&apos; definition Multifonds DB Column is TAXE_NO. |
| 29 | `FS.GI.DIST.AGENT.BANK.ID` | `FsGiDistAgent_BankId` | TField |  | Bank ID linked to the Agent Multifonds DB Column is NCORESP. |
| 30 | `FS.GI.DIST.AGENT.BANK.ACCOUNT.NUMBER` | `FsGiDistAgent_BankAccountNumber` | TField |  | Bank Account Number linked to the Agent Multifonds DB Column is BANK_ACCOUNT. |
| 31 | `FS.GI.DIST.AGENT.INTERMEDIATE.BANK.ID` | `FsGiDistAgent_IntermediateBankId` | TField |  | Intermediate bank ID linked to the agent Multifonds DB Column is NCORESP_INTER. |
| 32 | `FS.GI.DIST.AGENT.INTERMEDIATE.BANK.ACC.NUMBER` | `FsGiDistAgent_IntermediateBankAccNumber` | TField |  | Intermediate bank account number linked to the agent Multifonds DB Column is CPT_BANK_INTER. |
| 33 | `FS.GI.DIST.AGENT.EQUALIZATION.REGISTER.ID` | `FsGiDistAgent_EqualizationRegisterId` | TField |  | Equalization Register external ID at the agent level Multifonds DB Column is NREGISTER_EQUI. |
| 34 | `FS.GI.DIST.AGENT.AGENT.GROUP` | `FsGiDistAgent_AgentGroup` | TField |  | Agent group code for fund/agent restriction Multifonds DB Column is OUT_CGROUP. |
| 35 | `FS.GI.DIST.AGENT.PAYING.AGENT.ID` | `FsGiDistAgent_PayingAgentId` | TField |  | Paying Agent ID Multifonds DB Column is NCORRESP_PAYING. |
| 36 | `FS.GI.DIST.AGENT.AGENT.PAYMENT.CURRENCY` | `FsGiDistAgent_AgentPaymentCurrency` | TField |  | The agent commission and trailer Fees payment currency (in 3 letter format eg USD) Multifonds DB Column is CMON_TA. |
| 37 | `FS.GI.DIST.AGENT.REPORTING.CURRENCY` | `FsGiDistAgent_ReportingCurrency` | TField |  | Reporting Currency (in 3 letter ISO code, Eg: EUR) Multifonds DB Column is CMON_REP. |
| 38 | `FS.GI.DIST.AGENT.COMMISSION.GROUP` | `FsGiDistAgent_CommissionGroup` | TField |  | Group commission distribution to which this Agent is linked to Multifonds DB Column is GROUP_COM. |
| 39 | `FS.GI.DIST.AGENT.TRAILER.FEE.STRUCTURE.ID` | `FsGiDistAgent_TrailerFeeStructureId` | TField |  | Trailer fee distribution structure ID Multifonds DB Column is STRUCTURE_ID_TF. |
| 40 | `FS.GI.DIST.AGENT.RISK.CODE` | `FsGiDistAgent_RiskCode` | TField |  | Agent Risk Rating assgined as per AML Country Parameterization Multifonds DB Column is OUT_RISK_CODE. |
| 41 | `FS.GI.DIST.AGENT.REGISTER.TYPE` | `FsGiDistAgent_RegisterType` | TField |  | Register Type code for cash handling Multifonds DB Column is TYPE_REG. |
| 42 | `FS.GI.DIST.AGENT.SETTLEMENT.TYPE` | `FsGiDistAgent_SettlementType` | TField |  | Settlement type code allowed for the investor Multifonds DB Column is TYPE_SETTLEMENT. |
| 43 | `FS.GI.DIST.AGENT.DEAL.TYPE` | `FsGiDistAgent_DealType` | TField |  | Deal type code for Cash handling Multifonds DB Column is TYPE_DEAL. |
| 44 | `FS.GI.DIST.AGENT.AGENT.COMMISSION.GROUP` | `FsGiDistAgent_AgentCommissionGroup` | TField |  | Agent commission group type Multifonds DB Column is OUTLET_GRP_COMM. |
| 45 | `FS.GI.DIST.AGENT.AGENT.TRAILER.FEE.GROUP` | `FsGiDistAgent_AgentTrailerFeeGroup` | TField |  | Agent trailer fee commission group code Multifonds DB Column is OUTLET_GRP_TF. |
| 46 | `FS.GI.DIST.AGENT.CUT.OFF.GROUP` | `FsGiDistAgent_CutOffGroup` | TField |  | Cutoff group code linked to the Agent for the exception cut off parameterization Multifonds DB Column is CUT_OFF_GRP. |
| 47 | `FS.GI.DIST.AGENT.GL.ACCOUNT.GROUP.ID` | `FsGiDistAgent_GlAccountGroupId` | TField |  | General Ledger account group ID Multifonds DB Column is GL_ACCT_GROUP_ID. |
| 48 | `FS.GI.DIST.AGENT.SALESWATCH.TYPE` | `FsGiDistAgent_SaleswatchType` | TField |  | Saleswatch type of the agent Multifonds DB Column is TYPE_SWATCH. |
| 49 | `FS.GI.DIST.AGENT.COMMISSION.DISCLOSURE.CODE` | `FsGiDistAgent_CommissionDisclosureCode` | TField |  | It specifies whether the split of commission between the Management company and agents have to be disclosed on contract notes or not Multifonds DB Column is COMM_DISCLOSURE. |
| 50 | `FS.GI.DIST.AGENT.VALUE.DATE.METHOD` | `FsGiDistAgent_ValueDateMethod` | TField |  | Value date method to manage the settlement date based on the holidays to consider Multifonds DB Column is WORKING_DAY. |
| 51 | `FS.GI.DIST.AGENT.VALUE.DATE.NUMBER.OF.DAYS` | `FsGiDistAgent_ValueDateNumberOfDays` | TField |  | The number of days to be added to Trade date to arrive at the settlement date Multifonds DB Column is NUMBER_DAYS. |
| 52 | `FS.GI.DIST.AGENT.BIN.CHECK` | `FsGiDistAgent_BinCheck` | TField |  | It specifies the Broker Identification Number(BIN). It is available only if Agent type is &apos;0006&apos;-&apos;Main agent&apos; and &apos;Settlement type&apos;-&apos;0003&apos;-&apos;NSCC&apos; Multifonds DB Column is BIN_CHECK. |
| 53 | `FS.GI.DIST.AGENT.AGENT.COPIES.TRANS.FLAG` | `FsGiDistAgent_AgentCopiesTransFlag` | TField |  | Flag allows the Agent to receive copies of all transactions confirmation Multifonds DB Column is PR_TRANS. |
| 54 | `FS.GI.DIST.AGENT.AGENT.COPIES.INSTR.FLAG` | `FsGiDistAgent_AgentCopiesInstrFlag` | TField |  | Flag allows the Agent to receive copies of Savings Plan, Annuity and reinvestment confirmation Multifonds DB Column is PR_INST. |
| 55 | `FS.GI.DIST.AGENT.AGENT.COPIES.REG.POS.FLAG` | `FsGiDistAgent_AgentCopiesRegPosFlag` | TField |  | Flag allows the Agent to receive copies of Register position statement Multifonds DB Column is PR_POS. |
| 56 | `FS.GI.DIST.AGENT.AGENT.CLIENT.MONEY.FLAG` | `FsGiDistAgent_AgentClientMoneyFlag` | TField |  | Client Money Flag related to UK functionality Multifonds DB Column is CLNT_MONEY_FLG. |
| 57 | `FS.GI.DIST.AGENT.IN.FAVOR.OF.AGENT.FLAG` | `FsGiDistAgent_InFavorOfAgentFlag` | TField |  | In favor of agent flag related to UK functionality Multifonds DB Column is CFAVOUR. |
| 58 | `FS.GI.DIST.AGENT.MANUAL.GLOBAL.CONFIRM.FLAG` | `FsGiDistAgent_ManualGlobalConfirmFlag` | TField |  | Agent Global Confirm Flag Multifonds DB Column is FLG_GLOBAL_CONFIRM. |
| 59 | `FS.GI.DIST.AGENT.PHONE.DEALING.FLAG` | `FsGiDistAgent_PhoneDealingFlag` | TField |  | Flag to enable the phone dealing functionality Multifonds DB Column is FLG_PHONE_DEAL. |
| 60 | `FS.GI.DIST.AGENT.EXCL.ROLLOVER.FLAG` | `FsGiDistAgent_ExclRolloverFlag` | TField |  | Flag to indicate exclude from rollover Multifonds DB Column is FLG_EXLD_FRM_ROLL. |
| 61 | `FS.GI.DIST.AGENT.COUNTERPART.TYPE` | `FsGiDistAgent_CounterpartType` | TField |  | Counterpart account for credit and debit transactions Multifonds DB Column is COUNTERPART_TYP. |
| 62 | `FS.GI.DIST.AGENT.CONTRACT.NOTES.MODEL` | `FsGiDistAgent_ContractNotesModel` | TField |  | The model code of contract note sent by the TA Multifonds DB Column is CMODEL_CN. |
| 63 | `FS.GI.DIST.AGENT.MEDIA.CN` | `FsGiDistAgent_MediaCn` | TField |  | The media code through which a contract note is sent to this register by the TA Multifonds DB Column is CMEDIA_CN. |
| 64 | `FS.GI.DIST.AGENT.CONTRACT.NOTES.RECIPIENT` | `FsGiDistAgent_ContractNotesRecipient` | TField |  | The recipient code who will receive a copy of the contract note Multifonds DB Column is CRECIPIENT_CN. |
| 65 | `FS.GI.DIST.AGENT.CONTACT.AGENT.ID` | `FsGiDistAgent_ContactAgentId` | TField |  | It specifies that the Agent is linked to the Contact lists of the Agent External ID Multifonds DB Column is NOUTLET_CONTACT. |
| 66 | `FS.GI.DIST.AGENT.FATCA.REPORTING.ENTITY` | `FsGiDistAgent_FatcaReportingEntity` | TField |  | Entity code in charge of FATCA reporting and controls Multifonds DB Column is FAT_REP_ENTITY. |
| 67 | `FS.GI.DIST.AGENT.AML.TYPE` | `FsGiDistAgent_AmlType` | TField |  | The AML type code of the Agent Multifonds DB Column is CAML_TYPE. |
| 68 | `FS.GI.DIST.AGENT.AML.AGENT.ID` | `FsGiDistAgent_AmlAgentId` | TField |  | Agent ID relevant for AML documents check Multifonds DB Column is NOUTLET_AML. |
| 69 | `FS.GI.DIST.AGENT.PAYMENT.AMOUNT.HANDLING` | `FsGiDistAgent_PaymentAmountHandling` | TField |  | Payment amount handling method code Multifonds DB Column is PAY_HANDLING. |
| 70 | `FS.GI.DIST.AGENT.PAYMENT.PROCESS` | `FsGiDistAgent_PaymentProcess` | TField |  | Payment process code for the deals Multifonds DB Column is PY_PROCESS. |
| 71 | `FS.GI.DIST.AGENT.RIGHT.TYPE` | `FsGiDistAgent_RightType` | TField |  | The rights on Funds by right type ID Multifonds DB Column is RIGHT_TYPE. |
| 72 | `FS.GI.DIST.AGENT.BRANCH.LENGTH` | `FsGiDistAgent_BranchLength` | TField |  | It specifies the maximum length of the External Reference of Outlet for NSCC deal. Allowed values are from 1 to 9 Multifonds DB Column is BRANCH_LENGTH. |
| 73 | `FS.GI.DIST.AGENT.DISTRIBUTION.CHANNEL` | `FsGiDistAgent_DistributionChannel` | TField |  | The distributer channel code of the Agent Multifonds DB Column is DIST_CHANNEL. |
| 74 | `FS.GI.DIST.AGENT.GDPR.INFORM.DATE` | `FsGiDistAgent_GdprInformDate` | TField |  | Date on which the GDPR informed to agent Multifonds DB Column is GDPR_DINFORMED_ON. |
| 75 | `FS.GI.DIST.AGENT.PII.DISCLOSURE` | `FsGiDistAgent_PiiDisclosure` | TField |  | PII disclosure code to specify if the entity consents to share its PII information or not Multifonds DB Column is PII_DISCLOSURE. |
| 76 | `FS.GI.DIST.AGENT.DEFAULT.COMMISSION.TYPE` | `FsGiDistAgent_DefaultCommissionType` | TField |  | It specifies the default commission type of the agent Multifonds DB Column is COMM_TYPE. |
| 77 | `FS.GI.DIST.AGENT.GLOBAL.ORDERING.FLAG` | `FsGiDistAgent_GlobalOrderingFlag` | TField |  | Flag allows to enable the global ordering functionality Multifonds DB Column is FLG_GLOBAL_ORD. |
| 78 | `FS.GI.DIST.AGENT.CASH.DIVIDEND.REGISTER.ID` | `FsGiDistAgent_CashDividendRegisterId` | TField |  | Cash dividend register ID which is Technical Register having &apos;Person type&apos; as &apos;0900-Fund&apos; Multifonds DB Column is NREGISTER_CASH_DIV. |
| 79 | `FS.GI.DIST.AGENT.TRANSACTION.BULKING.NETTING` | `FsGiDistAgent_TransactionBulkingNetting` | TField |  | It specifies the cash movements are to be grouped or Netted Multifonds DB Column is TRNS_BULK_NET. |
| 80 | `FS.GI.DIST.AGENT.REINVESTMENT.REGISTER.ID` | `FsGiDistAgent_ReinvestmentRegisterId` | TField |  | Reinvestment register ID which is Technical Register having &apos;Person type&apos; as &apos;0900-Fund&apos; Multifonds DB Column is NREGISTER_REINVEST. |
| 81 | `FS.GI.DIST.AGENT.FATCA.STATUS` | `FsGiDistAgent_FatcaStatus` | TField |  | FATCA status code Multifonds DB Column is FAT_STATUS. |
| 82 | `FS.GI.DIST.AGENT.GIIN.NUMBER` | `FsGiDistAgent_GiinNumber` | TField |  | GIIN identification number Multifonds DB Column is FAT_GIIN. |
| 83 | `FS.GI.DIST.AGENT.FATCA.EFFECTIVE.DATE` | `FsGiDistAgent_FatcaEffectiveDate` | TField |  | FATCA effective date Multifonds DB Column is FAT_DEFFECTIVE. |
| 84 | `FS.GI.DIST.AGENT.FATCA.EXPIRY.DATE` | `FsGiDistAgent_FatcaExpiryDate` | TField |  | FATCA expiry date Multifonds DB Column is FAT_DEXPIRY. |
| 85 | `FS.GI.DIST.AGENT.FATCA.REVOKE.DATE` | `FsGiDistAgent_FatcaRevokeDate` | TField |  | FATCA revoke date Multifonds DB Column is FAT_DREVOKE. |
| 86 | `FS.GI.DIST.AGENT.FATCA.EXEMPTION.REASON` | `FsGiDistAgent_FatcaExemptionReason` | TField |  | FATCA exempt reason code of the Fund promoter Multifonds DB Column is FAT_EXEM_REASON. |
| 87 | `FS.GI.DIST.AGENT.CRS.STATUS` | `FsGiDistAgent_CrsStatus` | TField |  | CRS status code Multifonds DB Column is CRS_STATUS. |
| 88 | `FS.GI.DIST.AGENT.TAX.ID.NUMBER` | `FsGiDistAgent_TaxIdNumber` | TField |  | Tax ID for FATCA process Multifonds DB Column is TIN_NUMBER. |
| 89 | `FS.GI.DIST.AGENT.MAIN.AGENT.ID` | `FsGiDistAgent_MainAgentId` | TField |  | Main agent ID Multifonds DB Column is OUTLET_GROUP. |
| 90 | `FS.GI.DIST.AGENT.DISTRIBUTION.FLAG` | `FsGiDistAgent_DistributionFlag` | TField |  | Flag allows to enable Commission distribution definition per fund or per group Multifonds DB Column is DISTRIBUTION. |
| 91 | `FS.GI.DIST.AGENT.COMMISSION.AMOUNT.CURRENCY` | `FsGiDistAgent_CommissionAmountCurrency` | TField |  | Commission amount currency Multifonds DB Column is CMON_OPEN. |
| 92 | `FS.GI.DIST.AGENT.COMMISSION.AMOUNT` | `FsGiDistAgent_CommissionAmount` | TField |  | Commission amount Multifonds DB Column is CMON_AMOUNT. |
| 93 | `FS.GI.DIST.AGENT.COMMISSION.SCALE.CURRENCY` | `FsGiDistAgent_CommissionScaleCurrency` | TField |  | Commission scale currency code Multifonds DB Column is CMON_SCALE. |
| 94 | `FS.GI.DIST.AGENT.ARCHIVE.DATE` | `FsGiDistAgent_ArchiveDate` | TField |  | Archive date Multifonds DB Column is DARCH. |
| 95 | `FS.GI.DIST.AGENT.INACTIVATION.DATE` | `FsGiDistAgent_InactivationDate` | TField |  | Inactivation date Multifonds DB Column is DATE_INACTIVE. |
| 96 | `FS.GI.DIST.AGENT.PAYMENT.WEEK.DAY` | `FsGiDistAgent_PaymentWeekDay` | TField |  | It specifies the payment week day code Multifonds DB Column is WEEK_DAY. |
| 97 | `FS.GI.DIST.AGENT.PAYMENT.MONTH.DATE` | `FsGiDistAgent_PaymentMonthDate` | TField | Yes | It specifies the payment month date The field is mandatory when &apos;Frequency&apos; code is set as &apos;0001&apos; - &apos;Monthly&apos; Available selections start from 1 to 31 Multifonds DB Column is MONTH_DATE. |
| 98 | `FS.GI.DIST.AGENT.PAYMENT.IN.QUOTATION.CCY.FLAG` | `FsGiDistAgent_PaymentInQuotationCcyFlag` | TField |  | Flag allows the agent commission payment in quotation currency of the fund Multifonds DB Column is FLG_PAY_CCY. |
| 99 | `FS.GI.DIST.AGENT.SELECTED.ADDRESS.NUMBER` | `FsGiDistAgent_SelectedAddressNumber` | TField |  | Agent selected physical address number. Multifonds DB Column is CADRESSE. |
| 100 | `FS.GI.DIST.AGENT.AGENT.BLOCKED.USER` | `FsGiDistAgent_AgentBlockedUser` | TField |  | Agent Blocke By User Multifonds DB Column is BLOCK_AGT_USER. |
| 101 | `FS.GI.DIST.AGENT.BLOCK.INVESTOR.DATE` | `FsGiDistAgent_BlockInvestorDate` | TField |  | Agent Block Date Multifonds DB Column is DBLOCKED. |
| 102 | `FS.GI.DIST.AGENT.UNBLOCK.INVESOTR.BY` | `FsGiDistAgent_UnblockInvesotrBy` | TField |  | Unblocked By User Multifonds DB Column is UNBLOCKED_BY. |
| 103 | `FS.GI.DIST.AGENT.UNBLOCK.INVESTOR.DATE` | `FsGiDistAgent_UnblockInvestorDate` | TField |  | Unblocked Date Multifonds DB Column is DUNBLOCKED. |
| 104 | `FS.GI.DIST.AGENT.CHANGE.REASON.CODE` | `FsGiDistAgent_ChangeReasonCode` | TField |  | Change reason code Multifonds DB Column is CHG_REASON. |
| 105 | `FS.GI.DIST.AGENT.CHANGE.REASON.COMMENT` | `FsGiDistAgent_ChangeReasonComment` | TField |  | Change reason comment Multifonds DB Column is CHG_COMMENT. |
| 106 | `FS.GI.DIST.AGENT.TF.PARENT.AGENT.ID` | `FsGiDistAgent_TfParentAgentId` | TField |  | Trailer fee parent agent ID Multifonds DB Column is NOUTLET_PARENT_TF. |
| 107 | `FS.GI.DIST.AGENT.COMMISSION.OVERRIDES.FLAG` | `FsGiDistAgent_CommissionOverridesFlag` | TField |  | Flag allows to override the commission STP - interface file Multifonds DB Column is FLAG_COMM_OVERRIDE. |
| 108 | `FS.GI.DIST.AGENT.GDPR.PROCESSED.FLAG` | `FsGiDistAgent_GdprProcessedFlag` | TField |  | Flag to specify that the agent is anonymized Multifonds DB Column is FLG_GDPR_PROCESSED. |
| 109 | `FS.GI.DIST.AGENT.RESERVED10` | `FsGiDistAgent_Reserved10` | TField |  |  |
| 110 | `FS.GI.DIST.AGENT.RESERVED9` | `FsGiDistAgent_Reserved9` | TField |  |  |
| 111 | `FS.GI.DIST.AGENT.RESERVED8` | `FsGiDistAgent_Reserved8` | TField |  |  |
| 112 | `FS.GI.DIST.AGENT.RESERVED7` | `FsGiDistAgent_Reserved7` | TField |  |  |
| 113 | `FS.GI.DIST.AGENT.RESERVED6` | `FsGiDistAgent_Reserved6` | TField |  |  |
| 114 | `FS.GI.DIST.AGENT.RESERVED5` | `FsGiDistAgent_Reserved5` | TField |  |  |
| 115 | `FS.GI.DIST.AGENT.RESERVED4` | `FsGiDistAgent_Reserved4` | TField |  |  |
| 116 | `FS.GI.DIST.AGENT.RESERVED3` | `FsGiDistAgent_Reserved3` | TField |  |  |
| 117 | `FS.GI.DIST.AGENT.RESERVED2` | `FsGiDistAgent_Reserved2` | TField |  |  |
| 118 | `FS.GI.DIST.AGENT.RESERVED1` | `FsGiDistAgent_Reserved1` | TField |  |  |
| 119 | `FS.GI.DIST.AGENT.LOCAL.REF` | `FsGiDistAgent_LocalRef` |  |  |  |
| 120 | `FS.GI.DIST.AGENT.OVERRIDE` | `FsGiDistAgent_Override` |  |  |  |
| 121 | `FS.GI.DIST.AGENT.RECORD.STATUS` | `FsGiDistAgent_RecordStatus` | String |  |  |
| 122 | `FS.GI.DIST.AGENT.CURR.NO` | `FsGiDistAgent_CurrNo` | String |  |  |
| 123 | `FS.GI.DIST.AGENT.INPUTTER` | `FsGiDistAgent_Inputter` |  |  |  |
| 124 | `FS.GI.DIST.AGENT.DATE.TIME` | `FsGiDistAgent_DateTime` |  |  |  |
| 125 | `FS.GI.DIST.AGENT.AUTHORISER` | `FsGiDistAgent_Authoriser` | String |  |  |
| 126 | `FS.GI.DIST.AGENT.CO.CODE` | `FsGiDistAgent_CoCode` | String |  |  |
| 127 | `FS.GI.DIST.AGENT.DEPT.CODE` | `FsGiDistAgent_DeptCode` | String |  |  |
| 128 | `FS.GI.DIST.AGENT.AUDITOR.CODE` | `FsGiDistAgent_AuditorCode` | String |  |  |
| 129 | `FS.GI.DIST.AGENT.AUDIT.DATE.TIME` | `FsGiDistAgent_AuditDateTime` | String |  |  |
