# FS.GI.DIST.REGISTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.REGISTER` in `FS_InvestorAccountStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.REGISTER.PARENT.REF.ID` | `FsGiDistRegister_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.REGISTER.ORA.ROWID` | `FsGiDistRegister_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.REGISTER.REGISTER.ID` | `FsGiDistRegister_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.REGISTER.FUND.PROMOTER.ID` | `FsGiDistRegister_FundPromoterId` | TField |  | Fund Promoter external ID linked to the register. Multifonds DB Column is NPROMOTER. |
| 5 | `FS.GI.DIST.REGISTER.AGENT.ID` | `FsGiDistRegister_AgentId` | TField |  | Agent internal ID linked to the register. Multifonds DB Column is NOUTLET. |
| 6 | `FS.GI.DIST.REGISTER.NAME` | `FsGiDistRegister_Name` | TField |  | Name of the register. Multifonds DB Column is NAME. |
| 7 | `FS.GI.DIST.REGISTER.CUSTODIAN.ID` | `FsGiDistRegister_CustodianId` | TField |  | Custody Bank ID. Multifonds DB Column is NCORRESP_CUST. |
| 8 | `FS.GI.DIST.REGISTER.FIRST.NAME` | `FsGiDistRegister_FirstName` | TField |  | First name of the register. Multifonds DB Column is FIRSTNAME. |
| 9 | `FS.GI.DIST.REGISTER.ACCOUNT.TYPE` | `FsGiDistRegister_AccountType` | TField |  | The shareholder legal entity type. Multifonds DB Column is TYPE_REGISTER. |
| 10 | `FS.GI.DIST.REGISTER.REGON.NUMBER` | `FsGiDistRegister_RegonNumber` | TField |  | Register Regon No. Multifonds DB Column is REGON_NO. |
| 11 | `FS.GI.DIST.REGISTER.PERSON.TYPE` | `FsGiDistRegister_PersonType` | TField |  | Person type of the register. Multifonds DB Column is TYPE_PERSON. |
| 12 | `FS.GI.DIST.REGISTER.ACCOUNT.REFERENCE` | `FsGiDistRegister_AccountReference` | TField |  | Alternate reference for the register. Multifonds DB Column is ID_NO. |
| 13 | `FS.GI.DIST.REGISTER.REPORTING.CCY` | `FsGiDistRegister_ReportingCcy` | TField |  | Reporting currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMONREF. |
| 14 | `FS.GI.DIST.REGISTER.REGISTER.EXTERNAL.ID` | `FsGiDistRegister_RegisterExternalId` | TField |  | Register external reference number. Multifonds DB Column is NREGISTER_EXTERN. |
| 15 | `FS.GI.DIST.REGISTER.GLOBAL.REGISTER.ID` | `FsGiDistRegister_GlobalRegisterId` | TField |  | Global register ID. Multifonds DB Column is NREGISTER_GLOBAL. |
| 16 | `FS.GI.DIST.REGISTER.INVESTOR.ID` | `FsGiDistRegister_InvestorId` | TField |  | Client Internal ID. Multifonds DB Column is NCLIENT. |
| 17 | `FS.GI.DIST.REGISTER.USE.TYPE` | `FsGiDistRegister_UseType` | TField |  | Use type code of the Register. Multifonds DB Column is TYPE_USE. |
| 18 | `FS.GI.DIST.REGISTER.DISTRIBUTION.CHANNEL` | `FsGiDistRegister_DistributionChannel` | TField |  | The distributer channel code of the Register. Multifonds DB Column is DIST_CHANNEL. |
| 19 | `FS.GI.DIST.REGISTER.MASKING.FLG` | `FsGiDistRegister_MaskingFlg` | TField |  | Masking Flag. Multifonds DB Column is FLG_MSK_CHG. |
| 20 | `FS.GI.DIST.REGISTER.TEMPORARY.REGISTER.FLAG` | `FsGiDistRegister_TemporaryRegisterFlag` | TField |  | Flag to indicate whether the register created is temporarily created for NSCC. Multifonds DB Column is TMP. |
| 21 | `FS.GI.DIST.REGISTER.CREATED.FROM.CLIENT.FLAG` | `FsGiDistRegister_CreatedFromClientFlag` | TField |  | Flag indicates if Register details have been created from Client details. Multifonds DB Column is FLG_CREATED_FROM_CLIENT. |
| 22 | `FS.GI.DIST.REGISTER.MARKETING.CODE` | `FsGiDistRegister_MarketingCode` | TField |  | Marketing code linked to the register. Multifonds DB Column is MARKET_CODE. |
| 23 | `FS.GI.DIST.REGISTER.PRODUCT.CODE` | `FsGiDistRegister_ProductCode` | TField |  | Product type code to group the registers for advice and reporting. Multifonds DB Column is NPROD. |
| 24 | `FS.GI.DIST.REGISTER.ADVISORY.TYPE` | `FsGiDistRegister_AdvisoryType` | TField |  | The Advisory service type code of the register. Multifonds DB Column is ADVISORY_TYPE. |
| 25 | `FS.GI.DIST.REGISTER.GDPR.PROCESSED.FLAG` | `FsGiDistRegister_GdprProcessedFlag` | TField |  | Flag to specify that the register is anonymised. Multifonds DB Column is FLG_GDPR_PROCESSED. |
| 26 | `FS.GI.DIST.REGISTER.EXCL.ROLLOVER.FLAG` | `FsGiDistRegister_ExclRolloverFlag` | TField |  | Exclude from rollover enable to all registers. Multifonds DB Column is FLG_EXLD_FRM_ROLL. |
| 27 | `FS.GI.DIST.REGISTER.INACTIVATION.DATE` | `FsGiDistRegister_InactivationDate` | TField |  | Date of inactivation of Register. Multifonds DB Column is DATE_INACTIVE. |
| 28 | `FS.GI.DIST.REGISTER.ACCOUNT.TYPE2` | `FsGiDistRegister_AccountType2` | TField |  | Type of register. For example: Corporate Register, Institutional Register, Private Register etc. Multifonds DB Column is REG_TYPE. |
| 29 | `FS.GI.DIST.REGISTER.SALESMAN.ID` | `FsGiDistRegister_SalesmanId` | TField |  | Salesman external ID linked to the register. Multifonds DB Column is NOUTLET_SMAN. |
| 30 | `FS.GI.DIST.REGISTER.FAX.INDEMNITY.FLAG` | `FsGiDistRegister_FaxIndemnityFlag` | TField |  | Flag allows shareholder to deal by fax. Multifonds DB Column is FLG_FAXINDEMNITY. |
| 31 | `FS.GI.DIST.REGISTER.DISCL.ACCOUNT.NAME.FLAG` | `FsGiDistRegister_DisclAccountNameFlag` | TField |  | Flag to allow the disclosure of register name on certain shareholder reports. Multifonds DB Column is FLG_DIS_ACC_NAME. |
| 32 | `FS.GI.DIST.REGISTER.PROVIDER.ID` | `FsGiDistRegister_ProviderId` | TField |  | Provider ID. Multifonds DB Column is PROV_ID. |
| 33 | `FS.GI.DIST.REGISTER.QUANTITY.ROUNDING.TYPE` | `FsGiDistRegister_QuantityRoundingType` | TField |  | Quantity Rounding type code at register level. This will override the parameters defined at fund level. Multifonds DB Column is CTYPE_ARRONDI. |
| 34 | `FS.GI.DIST.REGISTER.LEGAL.ENTITY.ID` | `FsGiDistRegister_LegalEntityId` | TField |  | Legal Entity external ID linked to the register. Multifonds DB Column is NTFC. |
| 35 | `FS.GI.DIST.REGISTER.PHONE.DEALING.FLAG` | `FsGiDistRegister_PhoneDealingFlag` | TField |  | Flag to enable the register to place deals by phone. Multifonds DB Column is FLG_PHONE_DEAL. |
| 36 | `FS.GI.DIST.REGISTER.NEW.ISSUE.STATUS` | `FsGiDistRegister_NewIssueStatus` | TField |  | Register New Issue Status. Multifonds DB Column is NEW_ISSUE_STATUS. |
| 37 | `FS.GI.DIST.REGISTER.AFFILIATED.FLAG` | `FsGiDistRegister_AffiliatedFlag` | TField |  | Flag to specify that the register is affiliated to the fund manager. Multifonds DB Column is FLG_AFFILIATED. |
| 38 | `FS.GI.DIST.REGISTER.PII.DISCLOSURE` | `FsGiDistRegister_PiiDisclosure` | TField |  | PII(Personally identifiable information) disclosure code to specify if the register consents to share its PII information or not. Multifonds DB Column is PII_DISCLOSURE. |
| 39 | `FS.GI.DIST.REGISTER.COUNTERPART.TYPE` | `FsGiDistRegister_CounterpartType` | TField |  | Counterpart account for credit and debit transactions. Multifonds DB Column is COUNTERPART_TYP. |
| 40 | `FS.GI.DIST.REGISTER.LANGUAGE.CODE` | `FsGiDistRegister_LanguageCode` | TField |  | Language code of the register. Multifonds DB Column is CLANGUE. |
| 41 | `FS.GI.DIST.REGISTER.CITIZENSHIP` | `FsGiDistRegister_Citizenship` | TField |  | Citizenship of the register. Multifonds DB Column is CITIZENSHIP. |
| 42 | `FS.GI.DIST.REGISTER.RESIDENCE.COUNTRY` | `FsGiDistRegister_ResidenceCountry` | TField |  | Register residence country code (in 2 letter format Eg: LU). Multifonds DB Column is RESIDENCE. |
| 43 | `FS.GI.DIST.REGISTER.CORRESPONDANT.ID` | `FsGiDistRegister_CorrespondantId` | TField |  | Correspondent bank ID. Multifonds DB Column is NCORRESP. |
| 44 | `FS.GI.DIST.REGISTER.TELEPHONE.NUMBER` | `FsGiDistRegister_TelephoneNumber` | TField |  | Telephone number of the register. Multifonds DB Column is NTEL. |
| 45 | `FS.GI.DIST.REGISTER.FREE.TEXT1` | `FsGiDistRegister_FreeText1` | TField |  | Free text field that allows upto 250 alpha numerical characters for generic information. Multifonds DB Column is TEXT. |
| 46 | `FS.GI.DIST.REGISTER.KYC` | `FsGiDistRegister_Kyc` | TField |  | Code for KYC (Know your client) status. Multifonds DB Column is KNOW_YOUR_CLIENT. |
| 47 | `FS.GI.DIST.REGISTER.NATIONAL.ID.TYPE` | `FsGiDistRegister_NationalIdType` | TField |  | National ID Type. Multifonds DB Column is CNAT_ID. |
| 48 | `FS.GI.DIST.REGISTER.NATIONAL.ID` | `FsGiDistRegister_NationalId` | TField |  | National Insurance Number (NINO) of register which is required for the UK market for ISAs and PEPs. Multifonds DB Column is NAT_ID. |
| 49 | `FS.GI.DIST.REGISTER.DEATH.DATE` | `FsGiDistRegister_DeathDate` | TField |  | Date of death of register. Multifonds DB Column is DDEATH. |
| 50 | `FS.GI.DIST.REGISTER.DEATH.NOTIFICATION.DATE` | `FsGiDistRegister_DeathNotificationDate` | TField |  | Date on which death of register is notified. Multifonds DB Column is DDEATH_NOTE. |
| 51 | `FS.GI.DIST.REGISTER.DEATH.CONFIRM.DATE` | `FsGiDistRegister_DeathConfirmDate` | TField |  | Date on which death of register is confirmed. Multifonds DB Column is DDEATH_CONFIRM. |
| 52 | `FS.GI.DIST.REGISTER.PROBATE.GRANT.DATE` | `FsGiDistRegister_ProbateGrantDate` | TField |  | Register Probate Grant Date. Multifonds DB Column is DPROBATE_GRANT. |
| 53 | `FS.GI.DIST.REGISTER.ESTABLISHMENT.DATE` | `FsGiDistRegister_EstablishmentDate` | TField |  | Establishment date of the register. Default value is application date. Multifonds DB Column is DESTABLISHMENT. |
| 54 | `FS.GI.DIST.REGISTER.BIRTH.COUNTRY` | `FsGiDistRegister_BirthCountry` | TField |  | Birth country of the register. Multifonds DB Column is CPAYS_BIRTH. |
| 55 | `FS.GI.DIST.REGISTER.BIRTH.PLACE` | `FsGiDistRegister_BirthPlace` | TField |  | Birth place of the register. Multifonds DB Column is BIRTH_PLACE. |
| 56 | `FS.GI.DIST.REGISTER.PASSPORT.EXPIRY.DATE` | `FsGiDistRegister_PassportExpiryDate` | TField |  | Register passport expiry date. Multifonds DB Column is DPASSPORT_EXPIRY. |
| 57 | `FS.GI.DIST.REGISTER.SINGLE.INVESTOR.ID` | `FsGiDistRegister_SingleInvestorId` | TField |  | Single Investor Identitifcation assinged by Indonesia Central Securities Depository (KSEI) for Indonesian registers investing in Indonesia security markets. Multifonds DB Column is SID. |
| 58 | `FS.GI.DIST.REGISTER.MARITAL.STATUS` | `FsGiDistRegister_MaritalStatus` | TField |  | Marital status of the register. Multifonds DB Column is CTYP_MSTAT. |
| 59 | `FS.GI.DIST.REGISTER.EDUCATION.TYPE` | `FsGiDistRegister_EducationType` | TField |  | The education level code of the register. Multifonds DB Column is CTYP_EDU. |
| 60 | `FS.GI.DIST.REGISTER.RELIGION` | `FsGiDistRegister_Religion` | TField |  | Register religion code. Multifonds DB Column is CTYP_RELG. |
| 61 | `FS.GI.DIST.REGISTER.PURPOSE.OF.INVESTMENT` | `FsGiDistRegister_PurposeOfInvestment` | TField |  | The purpose of investment for the register. Multifonds DB Column is CTYP_PURP_INV. |
| 62 | `FS.GI.DIST.REGISTER.PROFESSION` | `FsGiDistRegister_Profession` | TField |  | Profession of the register. Multifonds DB Column is PROFESSION. |
| 63 | `FS.GI.DIST.REGISTER.JOINT.ACC.REQUIRED.SIGNATURES` | `FsGiDistRegister_JointAccRequiredSignatures` | TField |  | Joint account signature requirement details. Multifonds DB Column is JOINT_ACC_SIGN. |
| 64 | `FS.GI.DIST.REGISTER.AUTO.MATCH.FLAG` | `FsGiDistRegister_AutoMatchFlag` | TField |  | Flag to block the user from auto-matching. Multifonds DB Column is FLG_AUTO_MATCH. |
| 65 | `FS.GI.DIST.REGISTER.PERSON.STATUS` | `FsGiDistRegister_PersonStatus` | TField |  | Register Person Status. Multifonds DB Column is PERSON_STATUS. |
| 66 | `FS.GI.DIST.REGISTER.SCREEN.REFERENCE` | `FsGiDistRegister_ScreenReference` | TField |  | Screening reference of the AML or Monitoring check performed. Multifonds DB Column is SCREEN_REF. |
| 67 | `FS.GI.DIST.REGISTER.APS.TRANSFER.DEATH.DATE` | `FsGiDistRegister_ApsTransferDeathDate` | TField |  | APS Transfer Date. Multifonds DB Column is APS_TRANS_DT. |
| 68 | `FS.GI.DIST.REGISTER.BIRTH.DATE` | `FsGiDistRegister_BirthDate` | TField |  | Birth date of the register. Multifonds DB Column is DATE_NAIS. |
| 69 | `FS.GI.DIST.REGISTER.GENDER` | `FsGiDistRegister_Gender` | TField |  | Gender of the register. Multifonds DB Column is SEXE. |
| 70 | `FS.GI.DIST.REGISTER.SHORT.NAME` | `FsGiDistRegister_ShortName` | TField |  | Short name of the register. Multifonds DB Column is SHORTNAME. |
| 71 | `FS.GI.DIST.REGISTER.LONG.NAME` | `FsGiDistRegister_LongName` | TField |  | Long name of the register. Multifonds DB Column is LONG_NAME. |
| 72 | `FS.GI.DIST.REGISTER.TITLE.CODE` | `FsGiDistRegister_TitleCode` | TField |  | Title code of the register. Multifonds DB Column is TITLE. |
| 73 | `FS.GI.DIST.REGISTER.CERTIFICATE` | `FsGiDistRegister_Certificate` | TField |  | Register Certificate Flag. Multifonds DB Column is CERTIF. |
| 74 | `FS.GI.DIST.REGISTER.SOURCE.OF.FUNDS` | `FsGiDistRegister_SourceOfFunds` | TField |  | Register source of funds code. Multifonds DB Column is CTYP_SRC_FUND. |
| 75 | `FS.GI.DIST.REGISTER.INCOME.TYPE` | `FsGiDistRegister_IncomeType` | TField |  | Income range code of the register. Multifonds DB Column is CTYP_INCOME. |
| 76 | `FS.GI.DIST.REGISTER.AML.JURISDICTION` | `FsGiDistRegister_AmlJurisdiction` | TField |  | AML jurisdiction of the register. Multifonds DB Column is JURISDICTION. |
| 77 | `FS.GI.DIST.REGISTER.AML.TYPE` | `FsGiDistRegister_AmlType` | TField |  | The AML type code of the register. Multifonds DB Column is CAML_TYPE. |
| 78 | `FS.GI.DIST.REGISTER.AML.AGENT.ID` | `FsGiDistRegister_AmlAgentId` | TField |  | Agent Internal ID relevant for AML documents check. This field is only for informative purpose. Multifonds DB Column is NOUTLET_AML. |
| 79 | `FS.GI.DIST.REGISTER.RISK.CLASS` | `FsGiDistRegister_RiskClass` | TField |  | Register risk class hierarchy code for managing investment restrictions. Multifonds DB Column is REG_RISK_CODE. |
| 80 | `FS.GI.DIST.REGISTER.REGISTER.BLOCKED.USER` | `FsGiDistRegister_RegisterBlockedUser` | TField |  | User who blocked the register. Multifonds DB Column is BLOCK_REG_USER. |
| 81 | `FS.GI.DIST.REGISTER.BLOCKED.QUANTITY` | `FsGiDistRegister_BlockedQuantity` | TField |  | Register Blocked Quantity. Multifonds DB Column is BLOCKED_QUANTITY. |
| 82 | `FS.GI.DIST.REGISTER.BLOCKED.AMOUNT` | `FsGiDistRegister_BlockedAmount` | TField |  | Register Blocked Amount. Multifonds DB Column is BLOCKED_AMOUNT. |
| 83 | `FS.GI.DIST.REGISTER.BLOCKING.REASON.TEXT` | `FsGiDistRegister_BlockingReasonText` | TField |  | Free text comment that allows upto 80 alpha numerical characters that can be used to include the reason for the register blocking. Multifonds DB Column is REASON_TEXT. |
| 84 | `FS.GI.DIST.REGISTER.BLOCK.INVESTOR.DATE` | `FsGiDistRegister_BlockInvestorDate` | TField |  | Date on which the register is blocked. Multifonds DB Column is DBLOCKED. |
| 85 | `FS.GI.DIST.REGISTER.BLOCKING.REASON.1` | `FsGiDistRegister_BlockingReason1` | TField |  | Register AML blocking reason code 1. Multifonds DB Column is BLOCK_CODE_1. |
| 86 | `FS.GI.DIST.REGISTER.BLOCKING.REASON.2` | `FsGiDistRegister_BlockingReason2` | TField |  | Register AML blocking reason code 2. Multifonds DB Column is BLOCK_CODE_2. |
| 87 | `FS.GI.DIST.REGISTER.BLOCKING.REASON.3` | `FsGiDistRegister_BlockingReason3` | TField |  | Register AML blocking reason code 3. Multifonds DB Column is BLOCK_CODE_3. |
| 88 | `FS.GI.DIST.REGISTER.BLOCKING.REASON.4` | `FsGiDistRegister_BlockingReason4` | TField |  | Register AML blocking reason code 4. Multifonds DB Column is BLOCK_CODE_4. |
| 89 | `FS.GI.DIST.REGISTER.COMMISSION.GROUP` | `FsGiDistRegister_CommissionGroup` | TField |  | Group commission code linked to the register. Multifonds DB Column is GROUP_COM. |
| 90 | `FS.GI.DIST.REGISTER.MIRRORING.REGISTER.ID` | `FsGiDistRegister_MirroringRegisterId` | TField |  | Mirroring register external ID linked to the register. Multifonds DB Column is NREGISTER_MIRROR. |
| 91 | `FS.GI.DIST.REGISTER.PAYING.AGENT.ID` | `FsGiDistRegister_PayingAgentId` | TField |  | Paying agent internal ID. Multifonds DB Column is NCORRESP_PAYING. |
| 92 | `FS.GI.DIST.REGISTER.DIVIDEND.PAYMENT.TYPE` | `FsGiDistRegister_DividendPaymentType` | TField |  | Dividend payment type code. Multifonds DB Column is CDIV_PAY_TYPE. |
| 93 | `FS.GI.DIST.REGISTER.DIVIDEND.BENEFICIARY.ID` | `FsGiDistRegister_DividendBeneficiaryId` | TField |  | Register&apos;s external ID to whom the dividend payment has to be done instead of the linked register. Multifonds DB Column is NDIV_BENEFICIARY. |
| 94 | `FS.GI.DIST.REGISTER.DIV.ON.SETTLED.SHARES` | `FsGiDistRegister_DivOnSettledShares` | TField |  | Field to specify whether dividend reinvestment or payment on the settled shares is allowed or not. Multifonds DB Column is FLG_DIV_SETT_SHARE. |
| 95 | `FS.GI.DIST.REGISTER.DAILY.DIV.PAYMENT.TYPE` | `FsGiDistRegister_DailyDivPaymentType` | TField |  | Field to specify whether or not interim dividends can be paid at trade date of full redemptions or full switches. Multifonds DB Column is DLYDIV_PAYMTHD. |
| 96 | `FS.GI.DIST.REGISTER.NO.CANC.RIGHTS.FLAG` | `FsGiDistRegister_NoCancRightsFlag` | TField |  | Flag to disable the cancellation rights for the register. Multifonds DB Column is FLG_NO_CNCL_RIGHT. |
| 97 | `FS.GI.DIST.REGISTER.CONTRACT.NOTES.MODEL` | `FsGiDistRegister_ContractNotesModel` | TField |  | The model code of contract note sent by the TA. Multifonds DB Column is CMODEL_CN. |
| 98 | `FS.GI.DIST.REGISTER.MEDIA.CN` | `FsGiDistRegister_MediaCn` | TField |  | The media code through which a contract note is sent to this register by the TA. Multifonds DB Column is CMEDIA_CN. |
| 99 | `FS.GI.DIST.REGISTER.CONTRACT.NOTES.RECIPIENT` | `FsGiDistRegister_ContractNotesRecipient` | TField |  | The recipient code who will receive a copy of the contract note. Multifonds DB Column is CRECIPIENT_CN. |
| 100 | `FS.GI.DIST.REGISTER.FEE.DISCOUNT` | `FsGiDistRegister_FeeDiscount` | TField |  | Shareholder&apos;s discount on commission (type 0008) on all operation codes. The field is expressed in percentage for all the funds. Multifonds DB Column is DISCOUNT_COM. |
| 101 | `FS.GI.DIST.REGISTER.ADMINISTRATION.FEE` | `FsGiDistRegister_AdministrationFee` | TField |  | Shareholder administration fee type code. Multifonds DB Column is NREGISTER_FEE. |
| 102 | `FS.GI.DIST.REGISTER.ADMIN.FEE.DISCOUNT` | `FsGiDistRegister_AdminFeeDiscount` | TField |  | Shareholder&apos;s discount on administration fee. This is expressed in percentage. Multifonds DB Column is REG_ADMIN_DISCOUNT. |
| 103 | `FS.GI.DIST.REGISTER.NSCC.MATRIX.LEVEL` | `FsGiDistRegister_NsccMatrixLevel` | TField |  | NSCC matrix level. Multifonds DB Column is MATRIX_LEVEL. |
| 104 | `FS.GI.DIST.REGISTER.NSCC.SOCIAL.CODE` | `FsGiDistRegister_NsccSocialCode` | TField |  | NSCC Social code. Multifonds DB Column is SOC_CODE. |
| 105 | `FS.GI.DIST.REGISTER.BANK.ACCOUNT.NUMBER` | `FsGiDistRegister_BankAccountNumber` | TField |  | Bank account number linked to the register. Multifonds DB Column is CPT_BANK. |
| 106 | `FS.GI.DIST.REGISTER.CUSTODY.SETTLEMENT` | `FsGiDistRegister_CustodySettlement` | TField |  | Custodian settlement type used for defining cash flows for transactions. Multifonds DB Column is CDEF_DELIV. |
| 107 | `FS.GI.DIST.REGISTER.EURO.PAY.COUNTRY` | `FsGiDistRegister_EuroPayCountry` | TField |  | It specifies the country code (in 2 letter code, Eg: LU) in which the register has bank details within the Euro zone. Multifonds DB Column is EUR_PAY_COUNTRY. |
| 108 | `FS.GI.DIST.REGISTER.CASH.ACC.MANAGEMENT.FLAG` | `FsGiDistRegister_CashAccManagementFlag` | TField |  | Flag allows to authorise the register for the cash account functionality. Multifonds DB Column is FLG_CASH_ACCOUNT. |
| 109 | `FS.GI.DIST.REGISTER.PAYMENT.BY.CHEQUE.FLAG` | `FsGiDistRegister_PaymentByChequeFlag` | TField |  | Flag to enable payment by cheque functionality for register to pay or receive payment by cheque. Multifonds DB Column is FLG_PAY_CHK. |
| 110 | `FS.GI.DIST.REGISTER.PAYMENT.AMOUNT.HANDLING` | `FsGiDistRegister_PaymentAmountHandling` | TField |  | The method code for payment amount handling used on the contract. If not specified, the calculated payment amount would apply. Multifonds DB Column is PAY_HANDLING. |
| 111 | `FS.GI.DIST.REGISTER.PAYMENT.PROCESS` | `FsGiDistRegister_PaymentProcess` | TField |  | The payment process flow to be applied for payments related to the register. Multifonds DB Column is PY_PROCESS. |
| 112 | `FS.GI.DIST.REGISTER.PASSPORT.ID` | `FsGiDistRegister_PassportId` | TField |  | Register passport number. Multifonds DB Column is PASSPORT_ID. |
| 113 | `FS.GI.DIST.REGISTER.SELECTED.PHY.ADDRESS.NO` | `FsGiDistRegister_SelectedPhyAddressNo` | TField |  | Register selected physical address number. Multifonds DB Column is CADRESSE. |
| 114 | `FS.GI.DIST.REGISTER.PESEL.NUMBER` | `FsGiDistRegister_PeselNumber` | TField |  | Register PESEL (Polish Powszechny Elektroniczny System Ewidencji LudnoA ci) Unique ID. Multifonds DB Column is PESEL. |
| 115 | `FS.GI.DIST.REGISTER.GUS.NUMBER` | `FsGiDistRegister_GusNumber` | TField |  | Register GUS number. Multifonds DB Column is GUS. |
| 116 | `FS.GI.DIST.REGISTER.PRODUCT.TYPE` | `FsGiDistRegister_ProductType` | TField |  | Product type code to group the registers for advice and reporting. Multifonds DB Column is NPRODUCT. |
| 117 | `FS.GI.DIST.REGISTER.UPDATE.FROM.INVESTOR.FLAG` | `FsGiDistRegister_UpdateFromInvestorFlag` | TField |  | Flag to indicate that the register is created through the client. Multifonds DB Column is FLG_CLIENT_UPD. |
| 118 | `FS.GI.DIST.REGISTER.REPORTING.FREQUENCY.CODE` | `FsGiDistRegister_ReportingFrequencyCode` | TField |  | Reporting frequency code for standing Instruction transactions. Multifonds DB Column is NFREQ. |
| 119 | `FS.GI.DIST.REGISTER.DATA.PROTECTION.FLAG` | `FsGiDistRegister_DataProtectionFlag` | TField |  | Flag to authorise TA to use register&apos;s address for advertisement mailing. Multifonds DB Column is FLG_DATAPROTECTION. |
| 120 | `FS.GI.DIST.REGISTER.ERISA.FLAG` | `FsGiDistRegister_ErisaFlag` | TField |  | Flag allows to do ERISA check for the register. Multifonds DB Column is FLG_ERISA_INVESTOR. |
| 121 | `FS.GI.DIST.REGISTER.FATCA.REPORTING.ENTITY` | `FsGiDistRegister_FatcaReportingEntity` | TField |  | Entity code in charge of FATCA reporting and controls. Multifonds DB Column is FAT_REP_ENTITY. |
| 122 | `FS.GI.DIST.REGISTER.KIID.COMPLIANCE.FLAG` | `FsGiDistRegister_KiidComplianceFlag` | TField |  | Flag to indicate that register is in scope for the KIID TA Compliance. Multifonds DB Column is KIID_COMP. |
| 123 | `FS.GI.DIST.REGISTER.KIID.STANDING.INSTR.FLAG` | `FsGiDistRegister_KiidStandingInstrFlag` | TField |  | Flag to indicate that the KIID standing instruction is received for the register. Multifonds DB Column is KIID_STDINS. |
| 124 | `FS.GI.DIST.REGISTER.NON.ERISA.BP.FLAG` | `FsGiDistRegister_NonErisaBpFlag` | TField |  | Flag indicates that the register is not an ERISA benefit plan register. Multifonds DB Column is FLG_NON_ERISA_BP. |
| 125 | `FS.GI.DIST.REGISTER.ERISA.PERCENTAGE` | `FsGiDistRegister_ErisaPercentage` | TField |  | ERISA investment percentage of the register. Multifonds DB Column is PCT_ERISA. |
| 126 | `FS.GI.DIST.REGISTER.NON.ERISA.BP.PERCENTAGE` | `FsGiDistRegister_NonErisaBpPercentage` | TField |  | The percentage of investment applied to non ERISA benefit plan (default 100% if a non-ERISA Benefit Plana flag is ticked). Multifonds DB Column is PCT_NON_ERISA_BP. |
| 127 | `FS.GI.DIST.REGISTER.AIFMD.REGISTER.TYPE` | `FsGiDistRegister_AifmdRegisterType` | TField |  | AIFMD (Alternative Investment Fund Managers Directive) Register type code. Multifonds DB Column is AIFMD_REGISTER_TYPE. |
| 128 | `FS.GI.DIST.REGISTER.MIFID.STATUS` | `FsGiDistRegister_MifidStatus` | TField |  | MIFID status of the register as per MIFID directives. Multifonds DB Column is MIFID_STAT. |
| 129 | `FS.GI.DIST.REGISTER.GDPR.INFORM.DATE` | `FsGiDistRegister_GdprInformDate` | TField |  | General Data Protection Regulation(GDPR) Informed On Date at Client level. Multifonds DB Column is GDPR_DINFORMED_ON. |
| 130 | `FS.GI.DIST.REGISTER.UNBLOCK.INVESTOR.DATE` | `FsGiDistRegister_UnblockInvestorDate` | TField |  | Unblock date. Multifonds DB Column is DUNBLOCKED. |
| 131 | `FS.GI.DIST.REGISTER.UNBLOCK.INVESOTR.BY` | `FsGiDistRegister_UnblockInvesotrBy` | TField |  | Unblocked by. Multifonds DB Column is UNBLOCKED_BY. |
| 132 | `FS.GI.DIST.REGISTER.ALL.DEBITS.BLOCKED.FLAG` | `FsGiDistRegister_AllDebitsBlockedFlag` | TField |  | Flag to block debit transactions for the register. Multifonds DB Column is FLG_DB_BLOCKED. |
| 133 | `FS.GI.DIST.REGISTER.MANUAL.RISK.RATING` | `FsGiDistRegister_ManualRiskRating` | TField |  | Manual risk rating code of the register. Multifonds DB Column is MRISK_RATE. |
| 134 | `FS.GI.DIST.REGISTER.CHANGE.REASON.CODE` | `FsGiDistRegister_ChangeReasonCode` | TField |  | Code to track the reason why a register field is updated by a user. Multifonds DB Column is CHG_REASON. |
| 135 | `FS.GI.DIST.REGISTER.CHANGE.REASON.COMMENT` | `FsGiDistRegister_ChangeReasonComment` | TField |  | User provided comments for the modification of the record. Multifonds DB Column is CHG_COMMENT. |
| 136 | `FS.GI.DIST.REGISTER.BLANKET.MIN.LIMIT.WAIVER.FLAG` | `FsGiDistRegister_BlanketMinLimitWaiverFlag` | TField |  | Flag to enable blanket waiver for transactions that do not meet the minimum investment limits. Multifonds DB Column is FLG_BLANKET_WAIVER. |
| 137 | `FS.GI.DIST.REGISTER.RISK.RATING` | `FsGiDistRegister_RiskRating` | TField |  | The auto-populated risk rate based on the Register Residence, Jurisdiction and AML type. Multifonds DB Column is RISK_RATE. |
| 138 | `FS.GI.DIST.REGISTER.ARCHIVE.DATE` | `FsGiDistRegister_ArchiveDate` | TField |  | Register Archive Date. Multifonds DB Column is DARCH. |
| 139 | `FS.GI.DIST.REGISTER.REGISTER.MIN.ARCH.DATE` | `FsGiDistRegister_RegisterMinArchDate` | TField |  | Register Minimum Archive Date Required. Multifonds DB Column is DMIN_ARCHIVE_REQD. |
| 140 | `FS.GI.DIST.REGISTER.MARKET.CODE` | `FsGiDistRegister_MarketCode` | TField |  | Market code linked to the register which is used to generate reports per market. Multifonds DB Column is CMARKET. |
| 141 | `FS.GI.DIST.REGISTER.FREE.TEXT2` | `FsGiDistRegister_FreeText2` | TField |  | Free text field that allows upto 180 alpha numerical characters for generic information . Multifonds DB Column is FREE_TEXT. |
| 142 | `FS.GI.DIST.REGISTER.COMMENT` | `FsGiDistRegister_Comment` | TField |  | Free text comment that allows upto 50 alpha numerical characters that can be used for AML and screening hit related information. Multifonds DB Column is AML_COMMENT. |
| 143 | `FS.GI.DIST.REGISTER.MONITORING.TYPE` | `FsGiDistRegister_MonitoringType` | TField |  | The monitoring hit type code of the register. Multifonds DB Column is MONITOR_TYPE. |
| 144 | `FS.GI.DIST.REGISTER.MONITORING.TYPE.DATE` | `FsGiDistRegister_MonitoringTypeDate` | TField |  | The system date and time when the a Monitoring typea was updated with a value in the Client main screen, or when it was Validated. Multifonds DB Column is DMONITOR_TYPE. |
| 145 | `FS.GI.DIST.REGISTER.INTERFACE.BLOCKED.FLAG` | `FsGiDistRegister_InterfaceBlockedFlag` | TField |  | Flag to block the register from placing transactions through interface. Multifonds DB Column is FLG_INT_BLOCKED_REG. |
| 146 | `FS.GI.DIST.REGISTER.DOCUMENT.HANDLING` | `FsGiDistRegister_DocumentHandling` | TField |  | Swift document handling details for theNon Swift Trigger ID 0008-Generic static data change. Multifonds DB Column is DOC_HANDLING. |
| 147 | `FS.GI.DIST.REGISTER.REPORTING.GROUP.TYPE` | `FsGiDistRegister_ReportingGroupType` | TField |  | Reporting group type to group the registers by category for reporting purposes. Multifonds DB Column is TYPE_GROUP. |
| 148 | `FS.GI.DIST.REGISTER.NO.AGENT.COPIES.FLAG` | `FsGiDistRegister_NoAgentCopiesFlag` | TField |  | Flag allows to block the generation of confirmation copy for the linked agent. Multifonds DB Column is NO_PR_OUTLET. |
| 149 | `FS.GI.DIST.REGISTER.TAX.NUMBER` | `FsGiDistRegister_TaxNumber` | TField |  | Tax number of the register. Multifonds DB Column is TAXE_NO. |
| 150 | `FS.GI.DIST.REGISTER.NO.TAX.CERT` | `FsGiDistRegister_NoTaxCert` | TField |  | It specifies if the non-taxable certificate is applicable. Multifonds DB Column is NOTAX_CERT. |
| 151 | `FS.GI.DIST.REGISTER.NO.TAX.CERT.START` | `FsGiDistRegister_NoTaxCertStart` | TField |  | Start date of the non-taxable certificate. Multifonds DB Column is NOTAX_STDATE. |
| 152 | `FS.GI.DIST.REGISTER.NO.TAX.CERT.END` | `FsGiDistRegister_NoTaxCertEnd` | TField |  | Expiry date of the non-taxable certificate. Multifonds DB Column is NOTAX_EXDATE. |
| 153 | `FS.GI.DIST.REGISTER.TAX.OPTION` | `FsGiDistRegister_TaxOption` | TField |  | Tax option code of the register. Multifonds DB Column is CTAX_OPTION. |
| 154 | `FS.GI.DIST.REGISTER.TAX.RESIDENCE` | `FsGiDistRegister_TaxResidence` | TField |  | Tax residence of the register. It determines which country taxation rules are applicable for register investment. Multifonds DB Column is CTAX_RESIDENCE. |
| 155 | `FS.GI.DIST.REGISTER.TAX.OPTION.RECEPT.DATE` | `FsGiDistRegister_TaxOptionReceptDate` | TField |  | Date on which the tax option of the register has been received. Multifonds DB Column is DTO_RECEPTION. |
| 156 | `FS.GI.DIST.REGISTER.IRISH.TAX.EXEMPT.FLAG` | `FsGiDistRegister_IrishTaxExemptFlag` | TField |  | Flag to enable the Irish Finance Act Exemption. Multifonds DB Column is CGT_EXEMPTION. |
| 157 | `FS.GI.DIST.REGISTER.SWEDISH.TAX.FLAG` | `FsGiDistRegister_SwedishTaxFlag` | TField |  | It specifies if Swedish tax calculation is applicable for the register. Multifonds DB Column is CSWEDISH_TAX. |
| 158 | `FS.GI.DIST.REGISTER.TAX.STATE.CODE` | `FsGiDistRegister_TaxStateCode` | TField |  | Tax state, corresponding to the state and country code combination in the state definition setup, based on the country code defined in the &apos;Tax residence&apos; field. Multifonds DB Column is CTAX_STATE. |
| 159 | `FS.GI.DIST.REGISTER.REGISTER.TYPE` | `FsGiDistRegister_RegisterType` | TField |  | Field to define type of register, for example, bearer shares register, pool register etc,. This field is required for the system to retrieve the correct Cash Handling. Multifonds DB Column is TYPE_REG. |
| 160 | `FS.GI.DIST.REGISTER.SETTLEMENT.TYPE` | `FsGiDistRegister_SettlementType` | TField |  | Settlement type code allowed for the register. Multifonds DB Column is TYPE_SETTLEMENT. |
| 161 | `FS.GI.DIST.REGISTER.DEAL.TYPE` | `FsGiDistRegister_DealType` | TField |  | Deal type code for cash handling. Multifonds DB Column is TYPE_DEAL. |
| 162 | `FS.GI.DIST.REGISTER.GLOBAL.ORDERING.FLAG` | `FsGiDistRegister_GlobalOrderingFlag` | TField |  | Flag to enable the global ordering functionality. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 163 | `FS.GI.DIST.REGISTER.GLOBAL.ORDERING.SENDING.TYPE` | `FsGiDistRegister_GlobalOrderingSendingType` | TField |  | Sending method and DN code for the Central TA. Multifonds DB Column is SUB_RED_METHOD. |
| 164 | `FS.GI.DIST.REGISTER.GLOBAL.ORDERING.SWITCH.TYPE` | `FsGiDistRegister_GlobalOrderingSwitchType` | TField |  | Sending method and DN code for the Central TA for Switch transactions. Multifonds DB Column is SWITCH_METHOD. |
| 165 | `FS.GI.DIST.REGISTER.GLOBAL.ORDERING.TRANSFER.TYPE` | `FsGiDistRegister_GlobalOrderingTransferType` | TField |  | Sending method and DN code for the Central TA for transfer transactions. Multifonds DB Column is TRANSFER_METHOD. |
| 166 | `FS.GI.DIST.REGISTER.CDSC.ROLLOVER.REGISTER.ID` | `FsGiDistRegister_CdscRolloverRegisterId` | TField |  | Register ID for CDSC roll over functionality. Multifonds DB Column is NREGISTER_ROLLOVER. |
| 167 | `FS.GI.DIST.REGISTER.QUANTITY.DECIMALS` | `FsGiDistRegister_QuantityDecimals` | TField |  | Number of decimal places in share quantity calculation. Multifonds DB Column is CODE_ARRONDI_QT. |
| 168 | `FS.GI.DIST.REGISTER.SHARE.CLASS.CURRENCY` | `FsGiDistRegister_ShareClassCurrency` | TField |  | Default currency which is used for transactions for the register. Multifonds DB Column is CMONCOTA. |
| 169 | `FS.GI.DIST.REGISTER.BED.BREAKFAST.FLAG` | `FsGiDistRegister_BedBreakfastFlag` | TField |  | Flag allows to enable all &quot;Aller Retour&quot; transactions of the shareholder to process with cash at the order entry level. Multifonds DB Column is FLG_ALLER_PAY. |
| 170 | `FS.GI.DIST.REGISTER.SWITCH.WITH.CASH.FLAG` | `FsGiDistRegister_SwitchWithCashFlag` | TField |  | Flag to enable all switch transactions to be proccessed with cash at order entry level. Multifonds DB Column is FLG_SWITCH_CASH. |
| 171 | `FS.GI.DIST.REGISTER.RECORD.ID` | `FsGiDistRegister_RecordId` | TField |  | Record Identifier Multifonds DB Column is RECORDID. |
| 172 | `FS.GI.DIST.REGISTER.CONFIRM.DATE` | `FsGiDistRegister_ConfirmDate` | TField |  | User who has confirmed the record. Multifonds DB Column is DCONFIRM. |
| 173 | `FS.GI.DIST.REGISTER.CONFIRM.USER` | `FsGiDistRegister_ConfirmUser` | TField |  | Confirm timestamp. Multifonds DB Column is CONFIRMED_BY. |
| 174 | `FS.GI.DIST.REGISTER.RESERVED10` | `FsGiDistRegister_Reserved10` | TField |  |  |
| 175 | `FS.GI.DIST.REGISTER.RESERVED9` | `FsGiDistRegister_Reserved9` | TField |  |  |
| 176 | `FS.GI.DIST.REGISTER.RESERVED8` | `FsGiDistRegister_Reserved8` | TField |  |  |
| 177 | `FS.GI.DIST.REGISTER.RESERVED7` | `FsGiDistRegister_Reserved7` | TField |  |  |
| 178 | `FS.GI.DIST.REGISTER.RESERVED6` | `FsGiDistRegister_Reserved6` | TField |  |  |
| 179 | `FS.GI.DIST.REGISTER.RESERVED5` | `FsGiDistRegister_Reserved5` | TField |  |  |
| 180 | `FS.GI.DIST.REGISTER.RESERVED4` | `FsGiDistRegister_Reserved4` | TField |  |  |
| 181 | `FS.GI.DIST.REGISTER.RESERVED3` | `FsGiDistRegister_Reserved3` | TField |  |  |
| 182 | `FS.GI.DIST.REGISTER.RESERVED2` | `FsGiDistRegister_Reserved2` | TField |  |  |
| 183 | `FS.GI.DIST.REGISTER.RESERVED1` | `FsGiDistRegister_Reserved1` | TField |  |  |
| 184 | `FS.GI.DIST.REGISTER.LOCAL.REF` | `FsGiDistRegister_LocalRef` |  |  |  |
| 185 | `FS.GI.DIST.REGISTER.OVERRIDE` | `FsGiDistRegister_Override` |  |  |  |
| 186 | `FS.GI.DIST.REGISTER.RECORD.STATUS` | `FsGiDistRegister_RecordStatus` | String |  |  |
| 187 | `FS.GI.DIST.REGISTER.CURR.NO` | `FsGiDistRegister_CurrNo` | String |  |  |
| 188 | `FS.GI.DIST.REGISTER.INPUTTER` | `FsGiDistRegister_Inputter` |  |  |  |
| 189 | `FS.GI.DIST.REGISTER.DATE.TIME` | `FsGiDistRegister_DateTime` |  |  |  |
| 190 | `FS.GI.DIST.REGISTER.AUTHORISER` | `FsGiDistRegister_Authoriser` | String |  |  |
| 191 | `FS.GI.DIST.REGISTER.CO.CODE` | `FsGiDistRegister_CoCode` | String |  |  |
| 192 | `FS.GI.DIST.REGISTER.DEPT.CODE` | `FsGiDistRegister_DeptCode` | String |  |  |
| 193 | `FS.GI.DIST.REGISTER.AUDITOR.CODE` | `FsGiDistRegister_AuditorCode` | String |  |  |
| 194 | `FS.GI.DIST.REGISTER.AUDIT.DATE.TIME` | `FsGiDistRegister_AuditDateTime` | String |  |  |
