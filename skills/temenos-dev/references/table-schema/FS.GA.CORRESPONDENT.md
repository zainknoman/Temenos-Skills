# FS.GA.CORRESPONDENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT` in `FS_ThirdParties.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.PARENT.REF.ID` | `FsGaCorrespondent_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.ORA.ROWID` | `FsGaCorrespondent_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.CORRESPONDENT` | `FsGaCorrespondent_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CORRESPONDENT.CORRESPONDENT.TYPE` | `FsGaCorrespondent_CorrespondentType` | TField |  | Type of correspondent whether broker, manager, custodian. Multifonds DB Column is CTCL. |
| 5 | `FS.GA.CORRESPONDENT.DESCRIPTION` | `FsGaCorrespondent_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 6 | `FS.GA.CORRESPONDENT.NATIONALITY` | `FsGaCorrespondent_Nationality` | TField |  | This is the Nationality of the Third Party, which is usually the country code Multifonds DB Column is CPAYNAT. |
| 7 | `FS.GA.CORRESPONDENT.DOMICILE` | `FsGaCorrespondent_Domicile` | TField |  | Domicile of correspondent Multifonds DB Column is CDOMICI. |
| 8 | `FS.GA.CORRESPONDENT.GL.ACCOUNT` | `FsGaCorrespondent_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 9 | `FS.GA.CORRESPONDENT.MARGIN.ACCOUNT.NUMBER` | `FsGaCorrespondent_MarginAccountNumber` | TField |  | Future margin account number Multifonds DB Column is NRUBR_MARG. |
| 10 | `FS.GA.CORRESPONDENT.CORRESP.CASH.ACCOUNT.SUFFIX` | `FsGaCorrespondent_CorrespCashAccountSuffix` | TField |  | The suffix account of the cash correspondent used in Trades Multifonds DB Column is NSUF. |
| 11 | `FS.GA.CORRESPONDENT.COUNTERPARTY.SURNAME` | `FsGaCorrespondent_CounterpartySurname` | TField |  | Surname of counterparty Multifonds DB Column is SURNAME. |
| 12 | `FS.GA.CORRESPONDENT.COUNTERPARTY.NAME` | `FsGaCorrespondent_CounterpartyName` | TField |  | Name of counterparty Multifonds DB Column is FORNAME. |
| 13 | `FS.GA.CORRESPONDENT.ADDRESS.LINE.1` | `FsGaCorrespondent_AddressLine1` | TField |  | Address Line 1 Multifonds DB Column is ADRESS1. |
| 14 | `FS.GA.CORRESPONDENT.ADDRESS.LINE.2` | `FsGaCorrespondent_AddressLine2` | TField |  | Address Line 2 Multifonds DB Column is ADRESS2. |
| 15 | `FS.GA.CORRESPONDENT.ADDRESS.LINE.3` | `FsGaCorrespondent_AddressLine3` | TField |  | Address Line 3 Multifonds DB Column is ADRESS3. |
| 16 | `FS.GA.CORRESPONDENT.ADDRESS.LINE.4` | `FsGaCorrespondent_AddressLine4` | TField |  | Address Line 4 Multifonds DB Column is ADRESS4. |
| 17 | `FS.GA.CORRESPONDENT.TELEPHONE.NO.1` | `FsGaCorrespondent_TelephoneNo1` | TField |  | This is the Primary Telephone Number Multifonds DB Column is TEL1. |
| 18 | `FS.GA.CORRESPONDENT.TELEPHONE.NO.2` | `FsGaCorrespondent_TelephoneNo2` | TField |  | This is the Alternate Telephone Number Multifonds DB Column is TEL2. |
| 19 | `FS.GA.CORRESPONDENT.TELEFAX.NUMBER` | `FsGaCorrespondent_TelefaxNumber` | TField |  | This is the Telefax number Multifonds DB Column is FAX. |
| 20 | `FS.GA.CORRESPONDENT.COUNTERPARTY.TELEX` | `FsGaCorrespondent_CounterpartyTelex` | TField |  | Telex number of counterparty Multifonds DB Column is TELEX. |
| 21 | `FS.GA.CORRESPONDENT.CORRESPONDENT.TITLE` | `FsGaCorrespondent_CorrespondentTitle` | TField |  | Title of correspondent Multifonds DB Column is TITLE. |
| 22 | `FS.GA.CORRESPONDENT.CORRESPONDENT.SALUTATION` | `FsGaCorrespondent_CorrespondentSalutation` | TField |  | Salutation of correspondent Multifonds DB Column is SALUTATION. |
| 23 | `FS.GA.CORRESPONDENT.TAX.RESIDENCE` | `FsGaCorrespondent_TaxResidence` | TField |  | Tax residence of correspondent Multifonds DB Column is TAX_RES. |
| 24 | `FS.GA.CORRESPONDENT.DESIGNATION` | `FsGaCorrespondent_Designation` | TField |  | This is the Designation in case of a third party individual Multifonds DB Column is DESIGN. |
| 25 | `FS.GA.CORRESPONDENT.OFFICER` | `FsGaCorrespondent_Officer` | TField |  | Person who made the transaction. Multifonds DB Column is AC_OFFICER. |
| 26 | `FS.GA.CORRESPONDENT.INTRODUCER` | `FsGaCorrespondent_Introducer` | TField |  | Person who introduced the holder for the transaction. Multifonds DB Column is INTRODUCER. |
| 27 | `FS.GA.CORRESPONDENT.MAIL.CORRESPONDENCE` | `FsGaCorrespondent_MailCorrespondence` | TField |  | Mail Correspondent ID Multifonds DB Column is CORRES. |
| 28 | `FS.GA.CORRESPONDENT.CODE.ANALYSIS` | `FsGaCorrespondent_CodeAnalysis` | TField |  | Analysis codes assigned to a correspondent Multifonds DB Column is CODE_ANALYS1. |
| 29 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.2` | `FsGaCorrespondent_AnalysisCode2` | TField |  | Analysis Code 2 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS2. |
| 30 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.3` | `FsGaCorrespondent_AnalysisCode3` | TField |  | Analysis Code 3 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS3. |
| 31 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.4` | `FsGaCorrespondent_AnalysisCode4` | TField |  | Analysis Code 4 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS4. |
| 32 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.5` | `FsGaCorrespondent_AnalysisCode5` | TField |  | Analysis Code 5 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS5. |
| 33 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.6` | `FsGaCorrespondent_AnalysisCode6` | TField |  | Analysis Code 6 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS6. |
| 34 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.7` | `FsGaCorrespondent_AnalysisCode7` | TField |  | Analysis Code 7 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS7. |
| 35 | `FS.GA.CORRESPONDENT.ANALYSIS.CODE.8` | `FsGaCorrespondent_AnalysisCode8` | TField |  | Analysis Code 8 is used for the Italian reporting and/or the investment restriction control Multifonds DB Column is CODE_ANALYS8. |
| 36 | `FS.GA.CORRESPONDENT.MAIL.CODE.1` | `FsGaCorrespondent_MailCode1` | TField |  | Mail Code 1 Multifonds DB Column is CODE_MAIL1. |
| 37 | `FS.GA.CORRESPONDENT.MAIL.CODE.2` | `FsGaCorrespondent_MailCode2` | TField |  | Mail Code 2 Multifonds DB Column is CODE_MAIL2. |
| 38 | `FS.GA.CORRESPONDENT.MAIL.TYPE.FOR.THIRD.PARTIES` | `FsGaCorrespondent_MailTypeForThirdParties` | TField |  | This field allow user to define the mail type for a third party in central register details Multifonds DB Column is CODE_MAIL3. |
| 39 | `FS.GA.CORRESPONDENT.MAIL.CODE.4` | `FsGaCorrespondent_MailCode4` | TField |  | Mail Code 4 Multifonds DB Column is CODE_MAIL4. |
| 40 | `FS.GA.CORRESPONDENT.PAYMENT.TYPE` | `FsGaCorrespondent_PaymentType` | TField |  | This denotes the payment type to be used Multifonds DB Column is CODE_PMT. |
| 41 | `FS.GA.CORRESPONDENT.PAYMENT.TYPE.DESCRIPTION` | `FsGaCorrespondent_PaymentTypeDescription` | TField |  | Fill in the payment type description Multifonds DB Column is LIB_PMT. |
| 42 | `FS.GA.CORRESPONDENT.LANGUAGE` | `FsGaCorrespondent_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 43 | `FS.GA.CORRESPONDENT.FEE.SHARE.CODE` | `FsGaCorrespondent_FeeShareCode` | TField |  | Share Fees flag Multifonds DB Column is SHARE_FEES. |
| 44 | `FS.GA.CORRESPONDENT.SWIFT.ADDRESS` | `FsGaCorrespondent_SwiftAddress` | TField |  | Corresponds to a free definable swift address if required. User needs to define it through the button corresp. IDs&quot; &quot; Multifonds DB Column is COD_SWIFT. |
| 45 | `FS.GA.CORRESPONDENT.CEE.CREDIT` | `FsGaCorrespondent_CeeCredit` | TField |  | CEE Credit Multifonds DB Column is CR_CEE. |
| 46 | `FS.GA.CORRESPONDENT.SWIFT.ID` | `FsGaCorrespondent_SwiftId` | TField |  | Corresponds to a free definable SWIFT ID if required Multifonds DB Column is SWIFT_ID. |
| 47 | `FS.GA.CORRESPONDENT.RATING.CODE` | `FsGaCorrespondent_RatingCode` | TField |  | Rating Code Multifonds DB Column is CRATING. |
| 48 | `FS.GA.CORRESPONDENT.RATING.TYPE` | `FsGaCorrespondent_RatingType` | TField |  | Rating Type Multifonds DB Column is TYP_RATING. |
| 49 | `FS.GA.CORRESPONDENT.CORRESPONDENT.CATEGORY` | `FsGaCorrespondent_CorrespondentCategory` | TField |  | Category of correspondent Multifonds DB Column is CAT_EMET. |
| 50 | `FS.GA.CORRESPONDENT.BANKLEITZAHL.NUMBER` | `FsGaCorrespondent_BankleitzahlNumber` | TField |  | Bankleitzahl Number Multifonds DB Column is BLZ. |
| 51 | `FS.GA.CORRESPONDENT.EXTERNAL.REF` | `FsGaCorrespondent_ExternalRef` | TField |  | External reference of the correspondent Multifonds DB Column is EXTERNAL_REF. |
| 52 | `FS.GA.CORRESPONDENT.SECTOR` | `FsGaCorrespondent_Sector` | TField |  | Industry sector linked to a correspondent Multifonds DB Column is SCO. |
| 53 | `FS.GA.CORRESPONDENT.MARGIN.SUFFIX.NUMBER` | `FsGaCorrespondent_MarginSuffixNumber` | TField |  | Future margin account suffix number Multifonds DB Column is NSUFF_MARG. |
| 54 | `FS.GA.CORRESPONDENT.LINKED.PARTY.1` | `FsGaCorrespondent_LinkedParty1` | TField |  | Linked counterparty id 1 Multifonds DB Column is VIA_1. |
| 55 | `FS.GA.CORRESPONDENT.LINKED.PARTY.2` | `FsGaCorrespondent_LinkedParty2` | TField |  | Linked counterparty id 2 Multifonds DB Column is VIA_2. |
| 56 | `FS.GA.CORRESPONDENT.LINKED.PARTY.1.ACCOUNT` | `FsGaCorrespondent_LinkedParty1Account` | TField |  | Account number of linked counterparty id 1 Multifonds DB Column is VIA_ACCOUNT_NO1. |
| 57 | `FS.GA.CORRESPONDENT.LEDGER.ACCOUNT.2` | `FsGaCorrespondent_LedgerAccount2` | TField |  | To define Ledger Account 2 Multifonds DB Column is VIA_ACCOUNT_NO2. |
| 58 | `FS.GA.CORRESPONDENT.VM.ACCOUNT` | `FsGaCorrespondent_VmAccount` | TField |  | This is the default account used to book the variation margin on Futures Multifonds DB Column is NRUBR_VAR_MARG. |
| 59 | `FS.GA.CORRESPONDENT.VARIATION.MARGIN.SUFFIX.NUMBER` | `FsGaCorrespondent_VariationMarginSuffixNumber` | TField |  | To enter variation margin suffix number. Multifonds DB Column is NSUFF_VAR_MARG. |
| 60 | `FS.GA.CORRESPONDENT.TRUST` | `FsGaCorrespondent_Trust` | TField |  | Trust identifier if the correspondent is linked to a wider trust group. Multifonds DB Column is NCORRESP_TRUST. |
| 61 | `FS.GA.CORRESPONDENT.ISSUE.CAPITAL.EQUITY` | `FsGaCorrespondent_IssueCapitalEquity` | TField |  | Total issue capital in units of the issuer Multifonds DB Column is NISSUER_EQUITY. |
| 62 | `FS.GA.CORRESPONDENT.DEPOSITORY.INSURANCE.CODE` | `FsGaCorrespondent_DepositoryInsuranceCode` | TField |  | Insurance code tagged to a depository Multifonds DB Column is NDEPOSIT_INSURANCE. |
| 63 | `FS.GA.CORRESPONDENT.SUCCESSION.TAX` | `FsGaCorrespondent_SuccessionTax` | TField |  | Succession Tax Multifonds DB Column is SUCC_TAX. |
| 64 | `FS.GA.CORRESPONDENT.FISCAL.YEAR.START` | `FsGaCorrespondent_FiscalYearStart` | TField |  | Fiscal Year Start Multifonds DB Column is DSTART_FISCAL_YR. |
| 65 | `FS.GA.CORRESPONDENT.FISCAL.YEAR.END` | `FsGaCorrespondent_FiscalYearEnd` | TField |  | Fiscal Year End Multifonds DB Column is DEND_FISCAL_YR. |
| 66 | `FS.GA.CORRESPONDENT.ADDRESS.LINE.5` | `FsGaCorrespondent_AddressLine5` | TField |  | Address Line 5 Multifonds DB Column is ADRESS5. |
| 67 | `FS.GA.CORRESPONDENT.MARGINACCOUNT.SECBORROWING` | `FsGaCorrespondent_MarginaccountSecborrowing` | TField |  | The account number used for booking the margin on Security borrowing with or without cash Multifonds DB Column is NRUBR_BW_MARG. |
| 68 | `FS.GA.CORRESPONDENT.MARGINSUFFIXACCOUNT.SEC.BORR` | `FsGaCorrespondent_MarginsuffixaccountSecBorr` | TField |  | The Suffix account number used for booking the margin on Security borrowing with or without cash Multifonds DB Column is NSUFF_BW_MARG. |
| 69 | `FS.GA.CORRESPONDENT.MARGINACCOUNT.SEC.LENDING` | `FsGaCorrespondent_MarginaccountSecLending` | TField |  | The account number used for booking the margin on Security lending with or without cash Multifonds DB Column is NRUBR_LD_MARG. |
| 70 | `FS.GA.CORRESPONDENT.MARGIN.SUFFIX.ACC.SEC.LENDING` | `FsGaCorrespondent_MarginSuffixAccSecLending` | TField |  | The Suffix account number used for booking the margin on Security lending with or without cash Multifonds DB Column is NSUFF_LD_MARG. |
| 71 | `FS.GA.CORRESPONDENT.SECTOR.CODE` | `FsGaCorrespondent_SectorCode` | TField |  | Sector code tagged to a correspondent Multifonds DB Column is SECT_CODE. |
| 72 | `FS.GA.CORRESPONDENT.CROSS.TRADE.BROKER` | `FsGaCorrespondent_CrossTradeBroker` | TField |  | Indicator at broker defimition level if it is a cross broker to report all transactions on cross broker Multifonds DB Column is FLG_CROSS_TRADE. |
| 73 | `FS.GA.CORRESPONDENT.WEIGHT` | `FsGaCorrespondent_Weight` | TField |  | Weight Multifonds DB Column is WEIGHT. |
| 74 | `FS.GA.CORRESPONDENT.INCEPTION.DATE` | `FsGaCorrespondent_InceptionDate` | TField |  | Inception date of correspondent Multifonds DB Column is DATE_INCEPTION. |
| 75 | `FS.GA.CORRESPONDENT.RATING.TYPE.FOR.SHORT` | `FsGaCorrespondent_RatingTypeForShort` | TField |  | Rating Type For Short Multifonds DB Column is TYP_RATING_S. |
| 76 | `FS.GA.CORRESPONDENT.RATING.FOR.SHORT` | `FsGaCorrespondent_RatingForShort` | TField |  | Rating For Short Multifonds DB Column is CRATING_S. |
| 77 | `FS.GA.CORRESPONDENT.RATING.TYPE.FOR.LONG` | `FsGaCorrespondent_RatingTypeForLong` | TField |  | Rating Type For Long Multifonds DB Column is TYP_RATING_L. |
| 78 | `FS.GA.CORRESPONDENT.RATING.FOR.LONG` | `FsGaCorrespondent_RatingForLong` | TField |  | Rating For Long Multifonds DB Column is CRATING_L. |
| 79 | `FS.GA.CORRESPONDENT.CORRESPONDENT.CODIFICATION` | `FsGaCorrespondent_CorrespondentCodification` | TField |  | Code at correspondent level to indicate if it a correspondent bank or management company Multifonds DB Column is CODE_DEPOSIT. |
| 80 | `FS.GA.CORRESPONDENT.COUNTERPARTY.MARKET.ID` | `FsGaCorrespondent_CounterpartyMarketId` | TField |  | Market identifier tagged to a counterparty definition Multifonds DB Column is CODE_CPLACE_ID. |
| 81 | `FS.GA.CORRESPONDENT.COUNTERPARTY.CORRESP.ID` | `FsGaCorrespondent_CounterpartyCorrespId` | TField |  | Correspondent code like BIC, FIN, BVI tagged to a counterparty Multifonds DB Column is CODE_CORR_ID. |
| 82 | `FS.GA.CORRESPONDENT.EXTERNAL.IDENTIFIER.SECURITY` | `FsGaCorrespondent_ExternalIdentifierSecurity` | TField |  | Security identifier external Multifonds DB Column is CODE_SEC_ID. |
| 83 | `FS.GA.CORRESPONDENT.LENDING.MARGIN.ACCOUNT` | `FsGaCorrespondent_LendingMarginAccount` | TField |  | Margin account tagged to correspondent which is used for Security lending transaction. Multifonds DB Column is NRUBR_LD_MARG_CS. |
| 84 | `FS.GA.CORRESPONDENT.LENDING.MARGIN.SUFFIX` | `FsGaCorrespondent_LendingMarginSuffix` | TField |  | Margin account suffix tagged to correspondent which is used for Security lending transaction. Multifonds DB Column is NSUFF_LD_MARG_CS. |
| 85 | `FS.GA.CORRESPONDENT.BORROWING.MARGIN.ACCOUNT` | `FsGaCorrespondent_BorrowingMarginAccount` | TField |  | Margin account tagged to correspondent which is used for Security borrowing transaction. Multifonds DB Column is NRUBR_BW_MARG_CS. |
| 86 | `FS.GA.CORRESPONDENT.BORROWING.MARGIN.SUFFIX` | `FsGaCorrespondent_BorrowingMarginSuffix` | TField |  | Margin account suffix tagged to correspondent which is used for Security borrowing transaction. Multifonds DB Column is NSUFF_BW_MARG_CS. |
| 87 | `FS.GA.CORRESPONDENT.EXTERNAL.IDENTIFIER.INDEX` | `FsGaCorrespondent_ExternalIdentifierIndex` | TField |  | Index identifier external Multifonds DB Column is CODE_INDEX_ID. |
| 88 | `FS.GA.CORRESPONDENT.ISSUER.CATEGORY` | `FsGaCorrespondent_IssuerCategory` | TField |  | Category of issuer Multifonds DB Column is ISSUER_CATEGORY. |
| 89 | `FS.GA.CORRESPONDENT.MAIL.CODE.3` | `FsGaCorrespondent_MailCode3` | TField |  | Mail Code 3 Multifonds DB Column is CODE_MAIL. |
| 90 | `FS.GA.CORRESPONDENT.MARGIN.VARIATION.ACC.FOR.OP` | `FsGaCorrespondent_MarginVariationAccForOp` | TField |  | This is the default account used to book the variation margin on Options Multifonds DB Column is NRUBR_VAR_MARG_OP. |
| 91 | `FS.GA.CORRESPONDENT.OP.VARIATION.MARGIN.SUFFIX` | `FsGaCorrespondent_OpVariationMarginSuffix` | TField |  | This is the asset class of the derivative, like Option on Equities etc Multifonds DB Column is NSUFF_VAR_MARG_OP. |
| 92 | `FS.GA.CORRESPONDENT.STOCK.DIVIDEND.BROKER` | `FsGaCorrespondent_StockDividendBroker` | TField |  | Stock Dividend broker Multifonds DB Column is STOCK_DIV_BROK. |
| 93 | `FS.GA.CORRESPONDENT.THIRD.PARTY.ALTERNATE.DESC` | `FsGaCorrespondent_ThirdPartyAlternateDesc` | TField |  | Third party alternate description Multifonds DB Column is XLIBELLE_ALT. |
| 94 | `FS.GA.CORRESPONDENT.COUNTERPARTY.DESCRIPTION` | `FsGaCorrespondent_CounterpartyDescription` | TField |  | Third party description Multifonds DB Column is XLIBELLE_FUL. |
| 95 | `FS.GA.CORRESPONDENT.CFD.RESET.APPLICABLE` | `FsGaCorrespondent_CfdResetApplicable` | TField |  | CFD Reset applicable flag Multifonds DB Column is FLG_CFD_RESET. |
| 96 | `FS.GA.CORRESPONDENT.USER.DEFINABLE.FIELDS.GROUP` | `FsGaCorrespondent_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 97 | `FS.GA.CORRESPONDENT.CTM.INDICATOR` | `FsGaCorrespondent_CtmIndicator` | TField |  | Flag to indicate if the correspondent is CTM or not Multifonds DB Column is FLG_BROKER_CTM. |
| 98 | `FS.GA.CORRESPONDENT.SSI.INDICATOR` | `FsGaCorrespondent_SsiIndicator` | TField |  | Flag to indicate if the correspondent is SSI or not Multifonds DB Column is FLG_ALERT_SSI. |
| 99 | `FS.GA.CORRESPONDENT.MONETARY.FI.APPLICABLE` | `FsGaCorrespondent_MonetaryFiApplicable` | TField |  | Monetary FI Applicable Multifonds DB Column is FLG_MFI. |
| 100 | `FS.GA.CORRESPONDENT.EXCLUDE.ISSUER.GROUP` | `FsGaCorrespondent_ExcludeIssuerGroup` | TField |  | Exclude Issuer Group Multifonds DB Column is FLG_EXCLUDE_ISSUER_GROUP. |
| 101 | `FS.GA.CORRESPONDENT.EQUITY.CAPITAL.MNT` | `FsGaCorrespondent_EquityCapitalMnt` | TField |  | Equity Capital MNT Multifonds DB Column is MNT_EQUITY_CAPITAL. |
| 102 | `FS.GA.CORRESPONDENT.PREFERENCE.CAPITAL.MNT` | `FsGaCorrespondent_PreferenceCapitalMnt` | TField |  | Preference Capital MNT Multifonds DB Column is MNT_PREFERENCE_CAPITAL. |
| 103 | `FS.GA.CORRESPONDENT.DEBT.MNT` | `FsGaCorrespondent_DebtMnt` | TField |  | Debt MNT Multifonds DB Column is MNT_DEBT. |
| 104 | `FS.GA.CORRESPONDENT.RESERVES.MNT` | `FsGaCorrespondent_ReservesMnt` | TField |  | Reserves MNT Multifonds DB Column is MNT_RESERVES. |
| 105 | `FS.GA.CORRESPONDENT.CAPITAL.CONTRIBUTION.MNT` | `FsGaCorrespondent_CapitalContributionMnt` | TField |  | Capital Contribution MNT Multifonds DB Column is MNT_CAPITAL_CONTRIBUTION. |
| 106 | `FS.GA.CORRESPONDENT.RESERVED10` | `FsGaCorrespondent_Reserved10` | TField |  |  |
| 107 | `FS.GA.CORRESPONDENT.RESERVED9` | `FsGaCorrespondent_Reserved9` | TField |  |  |
| 108 | `FS.GA.CORRESPONDENT.RESERVED8` | `FsGaCorrespondent_Reserved8` | TField |  |  |
| 109 | `FS.GA.CORRESPONDENT.RESERVED7` | `FsGaCorrespondent_Reserved7` | TField |  |  |
| 110 | `FS.GA.CORRESPONDENT.RESERVED6` | `FsGaCorrespondent_Reserved6` | TField |  |  |
| 111 | `FS.GA.CORRESPONDENT.RESERVED5` | `FsGaCorrespondent_Reserved5` | TField |  |  |
| 112 | `FS.GA.CORRESPONDENT.RESERVED4` | `FsGaCorrespondent_Reserved4` | TField |  |  |
| 113 | `FS.GA.CORRESPONDENT.RESERVED3` | `FsGaCorrespondent_Reserved3` | TField |  |  |
| 114 | `FS.GA.CORRESPONDENT.RESERVED2` | `FsGaCorrespondent_Reserved2` | TField |  |  |
| 115 | `FS.GA.CORRESPONDENT.RESERVED1` | `FsGaCorrespondent_Reserved1` | TField |  |  |
| 116 | `FS.GA.CORRESPONDENT.LOCAL.REF` | `FsGaCorrespondent_LocalRef` |  |  |  |
| 117 | `FS.GA.CORRESPONDENT.OVERRIDE` | `FsGaCorrespondent_Override` |  |  |  |
| 118 | `FS.GA.CORRESPONDENT.RECORD.STATUS` | `FsGaCorrespondent_RecordStatus` | String |  |  |
| 119 | `FS.GA.CORRESPONDENT.CURR.NO` | `FsGaCorrespondent_CurrNo` | String |  |  |
| 120 | `FS.GA.CORRESPONDENT.INPUTTER` | `FsGaCorrespondent_Inputter` |  |  |  |
| 121 | `FS.GA.CORRESPONDENT.DATE.TIME` | `FsGaCorrespondent_DateTime` |  |  |  |
| 122 | `FS.GA.CORRESPONDENT.AUTHORISER` | `FsGaCorrespondent_Authoriser` | String |  |  |
| 123 | `FS.GA.CORRESPONDENT.CO.CODE` | `FsGaCorrespondent_CoCode` | String |  |  |
| 124 | `FS.GA.CORRESPONDENT.DEPT.CODE` | `FsGaCorrespondent_DeptCode` | String |  |  |
| 125 | `FS.GA.CORRESPONDENT.AUDITOR.CODE` | `FsGaCorrespondent_AuditorCode` | String |  |  |
| 126 | `FS.GA.CORRESPONDENT.AUDIT.DATE.TIME` | `FsGaCorrespondent_AuditDateTime` | String |  |  |
