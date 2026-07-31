# FS.GI.DIST.INVESTOR — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.INVESTOR` in `FS_InvestorStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.INVESTOR.PARENT.REF.ID` | `FsGiDistInvestor_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.INVESTOR.ORA.ROWID` | `FsGiDistInvestor_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.INVESTOR.INVESTOR.ID` | `FsGiDistInvestor_InvestorId` | TField |  | Client Internal ID. Multifonds DB Column is NCLIENT. |
| 4 | `FS.GI.DIST.INVESTOR.FUND.PROMOTER.ID` | `FsGiDistInvestor_FundPromoterId` | TField |  | Fund Promoter internal ID linked to the client. Multifonds DB Column is NPROMOTER. |
| 5 | `FS.GI.DIST.INVESTOR.PERSON.TYPE` | `FsGiDistInvestor_PersonType` | TField |  | Person Type code of the Client. Multifonds DB Column is CTYPE_PERSON. |
| 6 | `FS.GI.DIST.INVESTOR.ACCOUNT.TYPE` | `FsGiDistInvestor_AccountType` | TField |  | Account type code of the Client. Multifonds DB Column is CTYPE_REGISTER. |
| 7 | `FS.GI.DIST.INVESTOR.TITLE.CODE` | `FsGiDistInvestor_TitleCode` | TField |  | Title code of the Client. Multifonds DB Column is TITLE. |
| 8 | `FS.GI.DIST.INVESTOR.GENDER` | `FsGiDistInvestor_Gender` | TField |  | Gender of the Client. Multifonds DB Column is SEXE. |
| 9 | `FS.GI.DIST.INVESTOR.FIRST.NAME` | `FsGiDistInvestor_FirstName` | TField |  | First name of the Client. Multifonds DB Column is FIRSTNAME. |
| 10 | `FS.GI.DIST.INVESTOR.NAME` | `FsGiDistInvestor_Name` | TField |  | Name of the Client. Multifonds DB Column is NAME. |
| 11 | `FS.GI.DIST.INVESTOR.LONG.NAME` | `FsGiDistInvestor_LongName` | TField |  | Long name of the Client. Multifonds DB Column is LONG_NAME. |
| 12 | `FS.GI.DIST.INVESTOR.SHORT.NAME` | `FsGiDistInvestor_ShortName` | TField |  | Short Name of the Client. Multifonds DB Column is SHORTNAME. |
| 13 | `FS.GI.DIST.INVESTOR.BIRTH.DATE` | `FsGiDistInvestor_BirthDate` | TField |  | Birth date of the Client. Multifonds DB Column is DATE_NAIS. |
| 14 | `FS.GI.DIST.INVESTOR.BIRTH.COUNTRY` | `FsGiDistInvestor_BirthCountry` | TField |  | Birth country of the client. Multifonds DB Column is CPAYS_BIRTH. |
| 15 | `FS.GI.DIST.INVESTOR.BIRTH.PLACE` | `FsGiDistInvestor_BirthPlace` | TField |  | Birth place of the client. Multifonds DB Column is BIRTH_PLACE. |
| 16 | `FS.GI.DIST.INVESTOR.ESTABLISHMENT.DATE` | `FsGiDistInvestor_EstablishmentDate` | TField |  | Establishment date of the client. Default value is application date. Multifonds DB Column is DESTABLISHMENT. |
| 17 | `FS.GI.DIST.INVESTOR.ACCOUNT.REFERENCE` | `FsGiDistInvestor_AccountReference` | TField |  | Alternate reference for the client Multifonds DB Column is ID_NO. |
| 18 | `FS.GI.DIST.INVESTOR.AGENT.ID` | `FsGiDistInvestor_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 19 | `FS.GI.DIST.INVESTOR.REPORTING.CCY` | `FsGiDistInvestor_ReportingCcy` | TField |  | Reporting Currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMONREF. |
| 20 | `FS.GI.DIST.INVESTOR.LANGUAGE.CODE` | `FsGiDistInvestor_LanguageCode` | TField |  | Language code of the Client. Multifonds DB Column is CLANGUE. |
| 21 | `FS.GI.DIST.INVESTOR.CITIZENSHIP` | `FsGiDistInvestor_Citizenship` | TField |  | Citizenship of the Client. Multifonds DB Column is CITIZENSHIP. |
| 22 | `FS.GI.DIST.INVESTOR.RESIDENCE.COUNTRY` | `FsGiDistInvestor_ResidenceCountry` | TField |  | Client Residence country code (in 2 letter format Eg: LU). Multifonds DB Column is RESIDENCE. |
| 23 | `FS.GI.DIST.INVESTOR.TELEPHONE.NUMBER` | `FsGiDistInvestor_TelephoneNumber` | TField |  | Telephone number of the client. Multifonds DB Column is NTEL. |
| 24 | `FS.GI.DIST.INVESTOR.FREE.TEXT.1` | `FsGiDistInvestor_FreeText1` | TField |  | Free text field that allows upto 250 alpha numerical characters for generic information. Multifonds DB Column is TEXT. |
| 25 | `FS.GI.DIST.INVESTOR.USE.TYPE` | `FsGiDistInvestor_UseType` | TField |  | Use type code of the client. Multifonds DB Column is TYPE_USE. |
| 26 | `FS.GI.DIST.INVESTOR.INACTIVATION.DATE` | `FsGiDistInvestor_InactivationDate` | TField |  | Date of inactivation of Client. Multifonds DB Column is DATE_INACTIVE. |
| 27 | `FS.GI.DIST.INVESTOR.DISTRIBUTION.CHANNEL` | `FsGiDistInvestor_DistributionChannel` | TField |  | The distributer channel code of the client. Multifonds DB Column is DIST_CHANNEL. |
| 28 | `FS.GI.DIST.INVESTOR.MARKETING.CODE` | `FsGiDistInvestor_MarketingCode` | TField |  | Marketing code linked to the Client. Multifonds DB Column is MARKET_CODE. |
| 29 | `FS.GI.DIST.INVESTOR.ADVISORY.TYPE` | `FsGiDistInvestor_AdvisoryType` | TField |  | The Advisory service type code of the Client. Multifonds DB Column is ADVISORY_TYPE. |
| 30 | `FS.GI.DIST.INVESTOR.CONTACT.INVESTOR.ID` | `FsGiDistInvestor_ContactInvestorId` | TField |  | Client External ID that will be linked to the Contact lists of selected client. Multifonds DB Column is NCLIENT_CONTACT. |
| 31 | `FS.GI.DIST.INVESTOR.NATIONAL.ID.TYPE` | `FsGiDistInvestor_NationalIdType` | TField |  | National ID Type. Multifonds DB Column is CNAT_ID. |
| 32 | `FS.GI.DIST.INVESTOR.NATIONAL.ID` | `FsGiDistInvestor_NationalId` | TField | Yes | National ID number of the Client. This field is mandatory when the country of Investor residence has been defined. Multifonds DB Column is NAT_ID. |
| 33 | `FS.GI.DIST.INVESTOR.SINGLE.INVESTOR.ID` | `FsGiDistInvestor_SingleInvestorId` | TField |  | Single Investor Identitifcation of the Client. Assinged by Indonesia Central Securities Depository (KSEI) for Indonesia Client to Invest in Indonesia security markets. Multifonds DB Column is SID. |
| 34 | `FS.GI.DIST.INVESTOR.CHANGE.REASON.CODE` | `FsGiDistInvestor_ChangeReasonCode` | TField |  | A code to track the reason why a Client field is updated by a user. Multifonds DB Column is CHG_REASON. |
| 35 | `FS.GI.DIST.INVESTOR.CHANGE.REASON.COMMENT` | `FsGiDistInvestor_ChangeReasonComment` | TField |  | User provided comments for the modification of the record. Multifonds DB Column is CHG_COMMENT. |
| 36 | `FS.GI.DIST.INVESTOR.PII.DISCLOSURE` | `FsGiDistInvestor_PiiDisclosure` | TField |  | PII (Perosnally identifiable information) disclosure code to specify if the Client consents to share its PII information or not. Multifonds DB Column is PII_DISCLOSURE. |
| 37 | `FS.GI.DIST.INVESTOR.GDPR.PROCESSED.FLAG` | `FsGiDistInvestor_GdprProcessedFlag` | TField |  | Anonymized flag of the Client. Multifonds DB Column is FLG_GDPR_PROCESSED. |
| 38 | `FS.GI.DIST.INVESTOR.DISCL.ACCOUNT.NAME.FLAG` | `FsGiDistInvestor_DisclAccountNameFlag` | TField |  | Flag to allow the disclosure of client name on certain reports (Shareholder reports). Multifonds DB Column is FLG_DIS_ACC_NAME. |
| 39 | `FS.GI.DIST.INVESTOR.AML.TYPE` | `FsGiDistInvestor_AmlType` | TField |  | The AML type code of the Client. Multifonds DB Column is CAML_TYPE. |
| 40 | `FS.GI.DIST.INVESTOR.AML.JURISDICTION` | `FsGiDistInvestor_AmlJurisdiction` | TField |  | It specifies the AML jurisdiction of the Client. Multifonds DB Column is JURISDICTION. |
| 41 | `FS.GI.DIST.INVESTOR.AML.AGENT.ID` | `FsGiDistInvestor_AmlAgentId` | TField |  | Agent Internal ID relevant for AML documents check. This field is only for informative purpose. Multifonds DB Column is NOUTLET_AML. |
| 42 | `FS.GI.DIST.INVESTOR.RISK.RATING` | `FsGiDistInvestor_RiskRating` | TField |  | The auto-populated risk rate based on the Client Residence, Jurisdiction and AML type. Multifonds DB Column is RISK_RATE. |
| 43 | `FS.GI.DIST.INVESTOR.MANUAL.RISK.RATING` | `FsGiDistInvestor_ManualRiskRating` | TField |  | Manual Risk Rating code of the client. Multifonds DB Column is MRISK_RATE. |
| 44 | `FS.GI.DIST.INVESTOR.RISK.CLASS` | `FsGiDistInvestor_RiskClass` | TField |  | Client risk class hierarchy code for managing investment restrictions. Multifonds DB Column is REG_RISK_CODE. |
| 45 | `FS.GI.DIST.INVESTOR.KYC` | `FsGiDistInvestor_Kyc` | TField |  | Code for KYC (Know your client) status. Multifonds DB Column is KNOW_YOUR_CLIENT. |
| 46 | `FS.GI.DIST.INVESTOR.MONITORING.TYPE` | `FsGiDistInvestor_MonitoringType` | TField |  | The monitoring hit type code of the client. Multifonds DB Column is MONITOR_TYPE. |
| 47 | `FS.GI.DIST.INVESTOR.MONITORING.TYPE.DATE` | `FsGiDistInvestor_MonitoringTypeDate` | TField |  | The system date and time when the a Monitoring typea was updated with a value in the Client main screen, or when it was Validated. Multifonds DB Column is DMONITOR_TYPE. |
| 48 | `FS.GI.DIST.INVESTOR.SCREEN.REFERENCE` | `FsGiDistInvestor_ScreenReference` | TField |  | Screening reference of the AML or Monitoring check performed. Multifonds DB Column is SCREEN_REF. |
| 49 | `FS.GI.DIST.INVESTOR.SOURCE.OF.FUNDS` | `FsGiDistInvestor_SourceOfFunds` | TField |  | Client source of funds code. Multifonds DB Column is CTYP_SRC_FUND. |
| 50 | `FS.GI.DIST.INVESTOR.INCOME.TYPE` | `FsGiDistInvestor_IncomeType` | TField |  | Income range code of the client. Multifonds DB Column is CTYP_INCOME. |
| 51 | `FS.GI.DIST.INVESTOR.MARITAL.STATUS` | `FsGiDistInvestor_MaritalStatus` | TField |  | Marital status of the client. Multifonds DB Column is CTYP_MSTAT. |
| 52 | `FS.GI.DIST.INVESTOR.EDUCATION.TYPE` | `FsGiDistInvestor_EducationType` | TField |  | The education level code of the client. Multifonds DB Column is CTYP_EDU. |
| 53 | `FS.GI.DIST.INVESTOR.RELIGION` | `FsGiDistInvestor_Religion` | TField |  | Client religion code. Multifonds DB Column is CTYP_RELG. |
| 54 | `FS.GI.DIST.INVESTOR.PURPOSE.OF.INVESTMENT` | `FsGiDistInvestor_PurposeOfInvestment` | TField |  | The purpose of investment for the client. Multifonds DB Column is CTYP_PURP_INV. |
| 55 | `FS.GI.DIST.INVESTOR.PROFESSION` | `FsGiDistInvestor_Profession` | TField |  | Code for Profession of the client. Multifonds DB Column is PROFESSION. |
| 56 | `FS.GI.DIST.INVESTOR.PAYMENT.PROCESS` | `FsGiDistInvestor_PaymentProcess` | TField |  | The payment process flow to be applied for the payments related to the Client. Multifonds DB Column is PY_PROCESS. |
| 57 | `FS.GI.DIST.INVESTOR.PAYMENT.AMOUNT.HANDLING` | `FsGiDistInvestor_PaymentAmountHandling` | TField |  | The method code for payment amount handling used on the contract. If not specified, the calculated payment amount would apply. Multifonds DB Column is PAY_HANDLING. |
| 58 | `FS.GI.DIST.INVESTOR.CUSTODY.SETTLEMENT` | `FsGiDistInvestor_CustodySettlement` | TField |  | Custodian code for settlement used for defining cash flows for transactions. Multifonds DB Column is CDEF_DELIV. |
| 59 | `FS.GI.DIST.INVESTOR.MIN.DIV.PAY.OVERRIDE` | `FsGiDistInvestor_MinDivPayOverride` | TField |  | Flag to override the minimum payment limits defined at fund level for all accounts linked to the Client. Multifonds DB Column is FLG_MIN_DIV_PYM. |
| 60 | `FS.GI.DIST.INVESTOR.PASSPORT.ID` | `FsGiDistInvestor_PassportId` | TField |  | Client passport number. Multifonds DB Column is PASSPORT_ID. |
| 61 | `FS.GI.DIST.INVESTOR.TAX.RESIDENCE` | `FsGiDistInvestor_TaxResidence` | TField |  | Tax residence of the client. It determines which country taxation rules are applicable for client investment. Multifonds DB Column is CTAX_RESIDENCE. |
| 62 | `FS.GI.DIST.INVESTOR.PASSPORT.EXPIRY.DATE` | `FsGiDistInvestor_PassportExpiryDate` | TField |  | Client passport expiry date. Multifonds DB Column is DPASSPORT_EXPIRY. |
| 63 | `FS.GI.DIST.INVESTOR.TAX.NUMBER` | `FsGiDistInvestor_TaxNumber` | TField |  | Tax ID/Number of the Client. Multifonds DB Column is TAXE_NO. |
| 64 | `FS.GI.DIST.INVESTOR.FATCA.REPORTING.ENTITY` | `FsGiDistInvestor_FatcaReportingEntity` | TField |  | Entity code in charge of FATCA reporting and controls. Multifonds DB Column is FAT_REP_ENTITY. |
| 65 | `FS.GI.DIST.INVESTOR.KIID.COMPLIANCE.FLAG` | `FsGiDistInvestor_KiidComplianceFlag` | TField |  | Flag to indicate that Client is in scope for the KIID TA Compliance. Multifonds DB Column is KIID_COMP. |
| 66 | `FS.GI.DIST.INVESTOR.KIID.STANDING.INSTR.FLAG` | `FsGiDistInvestor_KiidStandingInstrFlag` | TField |  | Flag to indicate that the KIID standing instruction received for the Client. Multifonds DB Column is KIID_STDINS. |
| 67 | `FS.GI.DIST.INVESTOR.MIFID.STATUS` | `FsGiDistInvestor_MifidStatus` | TField |  | Code for MIFID status of the client as per Markets in financial instruments directive. Multifonds DB Column is MIFID_STAT. |
| 68 | `FS.GI.DIST.INVESTOR.GDPR.INFORM.DATE` | `FsGiDistInvestor_GdprInformDate` | TField |  | General Data Protection Regulation(GDPR) Informed On Date at Client level Multifonds DB Column is GDPR_DINFORMED_ON. |
| 69 | `FS.GI.DIST.INVESTOR.PAYING.AGENT.ID` | `FsGiDistInvestor_PayingAgentId` | TField |  | Paying Agent Internal ID. Multifonds DB Column is NCORRESP_PAYING. |
| 70 | `FS.GI.DIST.INVESTOR.TAX.OPTION` | `FsGiDistInvestor_TaxOption` | TField |  | Tax option code of the Client. Multifonds DB Column is CTAX_OPTION. |
| 71 | `FS.GI.DIST.INVESTOR.TAX.OPTION.RECEPT.DATE` | `FsGiDistInvestor_TaxOptionReceptDate` | TField |  | Date on which the tax option of the client has been received. Multifonds DB Column is DTO_RECEPTION. |
| 72 | `FS.GI.DIST.INVESTOR.NO.TAX.CERT` | `FsGiDistInvestor_NoTaxCert` | TField |  | It specifies if the Non-taxable Certificate is applicable. Multifonds DB Column is NOTAX_CERT. |
| 73 | `FS.GI.DIST.INVESTOR.NO.TAX.CERT.START` | `FsGiDistInvestor_NoTaxCertStart` | TField |  | Start date of the Non-taxable Certificate. Multifonds DB Column is NOTAX_STDATE. |
| 74 | `FS.GI.DIST.INVESTOR.NO.TAX.CERT.END` | `FsGiDistInvestor_NoTaxCertEnd` | TField |  | Expiry date of the Non-taxable Certificate. Multifonds DB Column is NOTAX_EXDATE. |
| 75 | `FS.GI.DIST.INVESTOR.IRISH.TAX.EXEMPT.FLAG` | `FsGiDistInvestor_IrishTaxExemptFlag` | TField |  | Flag allows to enable the Irish Finance Act Exemption. Multifonds DB Column is CGT_EXEMPTION. |
| 76 | `FS.GI.DIST.INVESTOR.COMMISSION.GROUP` | `FsGiDistInvestor_CommissionGroup` | TField |  | Group commission code linked to the Client. Client level code used to group registers at Register group structure link level similar to Commission group available at Agent level. Multifonds DB Column is GROUP_COM. |
| 77 | `FS.GI.DIST.INVESTOR.CDSC.ROLLOVER.REGISTER.ID` | `FsGiDistInvestor_CdscRolloverRegisterId` | TField |  | CDSC roll over Register External ID. Multifonds DB Column is NREGISTER_ROLLOVER. |
| 78 | `FS.GI.DIST.INVESTOR.EXCL.ROLLOVER.FLAG` | `FsGiDistInvestor_ExclRolloverFlag` | TField |  | Exclude from rollover enable to all registers linked to client. Multifonds DB Column is FLG_EXLD_FRM_ROLL. |
| 79 | `FS.GI.DIST.INVESTOR.QUANTITY.DECIMALS` | `FsGiDistInvestor_QuantityDecimals` | TField |  | Number of decimal places in the client share quantity calculation. Multifonds DB Column is CODE_ARRONDI_QT. |
| 80 | `FS.GI.DIST.INVESTOR.PHONE.DEALING.FLAG` | `FsGiDistInvestor_PhoneDealingFlag` | TField |  | Flag to enable the client to place deals by phone. This flag is only for informative purpose. Multifonds DB Column is FLG_PHONE_DEAL. |
| 81 | `FS.GI.DIST.INVESTOR.BLANKET.MIN.LIMIT.WAIVER.FLAG` | `FsGiDistInvestor_BlanketMinLimitWaiverFlag` | TField |  | Flag to enable blanket waiver for transactions that do not meet the minimum investment limits. Multifonds DB Column is FLG_BLANKET_WAIVER. |
| 82 | `FS.GI.DIST.INVESTOR.GLOBAL.ORDERING.FLAG` | `FsGiDistInvestor_GlobalOrderingFlag` | TField |  | Flag to enable the global ordering functionality for the client. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 83 | `FS.GI.DIST.INVESTOR.DOCUMENT.HANDLING` | `FsGiDistInvestor_DocumentHandling` | TField |  | Swift document handling details for theNon Swift Trigger ID 0008-Generic static data change. Multifonds DB Column is DOC_HANDLING. |
| 84 | `FS.GI.DIST.INVESTOR.FREE.TEXT2` | `FsGiDistInvestor_FreeText2` | TField |  | Free text field that allows upto 180 alpha numerical characters for generic information. Multifonds DB Column is FREE_TEXT. |
| 85 | `FS.GI.DIST.INVESTOR.COMMENT` | `FsGiDistInvestor_Comment` | TField |  | Free text comment that allows upto 50 alpha numerical characters that can be used for AML and screening hit related information. Multifonds DB Column is AML_COMMENT. |
| 86 | `FS.GI.DIST.INVESTOR.CLIENT.BLOCKED.FLAG` | `FsGiDistInvestor_ClientBlockedFlag` | TField |  | Flag to block the client. Multifonds DB Column is CLI_BLOCKED. |
| 87 | `FS.GI.DIST.INVESTOR.BLOCKING.REASON.1` | `FsGiDistInvestor_BlockingReason1` | TField |  | AML Blocking Reason 1. Multifonds DB Column is BLOCK_CODE_1. |
| 88 | `FS.GI.DIST.INVESTOR.BLOCKING.REASON.2` | `FsGiDistInvestor_BlockingReason2` | TField |  | AML Blocking Reason 2. Multifonds DB Column is BLOCK_CODE_2. |
| 89 | `FS.GI.DIST.INVESTOR.BLOCKING.REASON.3` | `FsGiDistInvestor_BlockingReason3` | TField |  | AML Blocking Reason 3. Multifonds DB Column is BLOCK_CODE_3. |
| 90 | `FS.GI.DIST.INVESTOR.BLOCKING.REASON.4` | `FsGiDistInvestor_BlockingReason4` | TField |  | AML Blocking Reason 4. Multifonds DB Column is BLOCK_CODE_4. |
| 91 | `FS.GI.DIST.INVESTOR.BLOCK.INVESTOR.USER` | `FsGiDistInvestor_BlockInvestorUser` | TField |  | User Blocked the client. Multifonds DB Column is BLOCK_CLI_USER. |
| 92 | `FS.GI.DIST.INVESTOR.BLOCK.INVESTOR.DATE` | `FsGiDistInvestor_BlockInvestorDate` | TField |  | Date of client blocking. Multifonds DB Column is DBLOCKED. |
| 93 | `FS.GI.DIST.INVESTOR.UNBLOCK.INVESOTR.BY` | `FsGiDistInvestor_UnblockInvesotrBy` | TField |  | Unblocked by. Multifonds DB Column is UNBLOCKED_BY. |
| 94 | `FS.GI.DIST.INVESTOR.UNBLOCK.INVESTOR.DATE` | `FsGiDistInvestor_UnblockInvestorDate` | TField |  | Unblock date. Multifonds DB Column is DUNBLOCKED. |
| 95 | `FS.GI.DIST.INVESTOR.CLIENT.SELECTED.PHY.ADDRESS.NO` | `FsGiDistInvestor_ClientSelectedPhyAddressNo` | TField |  | Client selected physical address number Multifonds DB Column is CADRESSE. |
| 96 | `FS.GI.DIST.INVESTOR.CLIENT.EXTERNAL.ID` | `FsGiDistInvestor_ClientExternalId` | TField |  | Client External identifier Multifonds DB Column is NCLIENT_EXTERN. |
| 97 | `FS.GI.DIST.INVESTOR.RESERVED10` | `FsGiDistInvestor_Reserved10` | TField |  |  |
| 98 | `FS.GI.DIST.INVESTOR.RESERVED9` | `FsGiDistInvestor_Reserved9` | TField |  |  |
| 99 | `FS.GI.DIST.INVESTOR.RESERVED8` | `FsGiDistInvestor_Reserved8` | TField |  |  |
| 100 | `FS.GI.DIST.INVESTOR.RESERVED7` | `FsGiDistInvestor_Reserved7` | TField |  |  |
| 101 | `FS.GI.DIST.INVESTOR.RESERVED6` | `FsGiDistInvestor_Reserved6` | TField |  |  |
| 102 | `FS.GI.DIST.INVESTOR.RESERVED5` | `FsGiDistInvestor_Reserved5` | TField |  |  |
| 103 | `FS.GI.DIST.INVESTOR.RESERVED4` | `FsGiDistInvestor_Reserved4` | TField |  |  |
| 104 | `FS.GI.DIST.INVESTOR.RESERVED3` | `FsGiDistInvestor_Reserved3` | TField |  |  |
| 105 | `FS.GI.DIST.INVESTOR.RESERVED2` | `FsGiDistInvestor_Reserved2` | TField |  |  |
| 106 | `FS.GI.DIST.INVESTOR.RESERVED1` | `FsGiDistInvestor_Reserved1` | TField |  |  |
| 107 | `FS.GI.DIST.INVESTOR.LOCAL.REF` | `FsGiDistInvestor_LocalRef` |  |  |  |
| 108 | `FS.GI.DIST.INVESTOR.OVERRIDE` | `FsGiDistInvestor_Override` |  |  |  |
| 109 | `FS.GI.DIST.INVESTOR.RECORD.STATUS` | `FsGiDistInvestor_RecordStatus` | String |  |  |
| 110 | `FS.GI.DIST.INVESTOR.CURR.NO` | `FsGiDistInvestor_CurrNo` | String |  |  |
| 111 | `FS.GI.DIST.INVESTOR.INPUTTER` | `FsGiDistInvestor_Inputter` |  |  |  |
| 112 | `FS.GI.DIST.INVESTOR.DATE.TIME` | `FsGiDistInvestor_DateTime` |  |  |  |
| 113 | `FS.GI.DIST.INVESTOR.AUTHORISER` | `FsGiDistInvestor_Authoriser` | String |  |  |
| 114 | `FS.GI.DIST.INVESTOR.CO.CODE` | `FsGiDistInvestor_CoCode` | String |  |  |
| 115 | `FS.GI.DIST.INVESTOR.DEPT.CODE` | `FsGiDistInvestor_DeptCode` | String |  |  |
| 116 | `FS.GI.DIST.INVESTOR.AUDITOR.CODE` | `FsGiDistInvestor_AuditorCode` | String |  |  |
| 117 | `FS.GI.DIST.INVESTOR.AUDIT.DATE.TIME` | `FsGiDistInvestor_AuditDateTime` | String |  |  |
