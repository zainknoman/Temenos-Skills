# FS.GI.APP.CORRESPONDENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.CORRESPONDENT` in `FS_Correspondent.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.CORRESPONDENT.PARENT.REF.ID` | `FsGiAppCorrespondent_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.CORRESPONDENT.ORA.ROWID` | `FsGiAppCorrespondent_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.CORRESPONDENT.CORRESPONDENT.ID` | `FsGiAppCorrespondent_CorrespondentId` | TField |  | Correspondent internal ID (User definable or system generated- based on application setup). Multifonds DB Column is NCORRESP. |
| 4 | `FS.GI.APP.CORRESPONDENT.THIRD.PARTY.TYPE` | `FsGiAppCorrespondent_ThirdPartyType` | TField |  | It specifies the type of correspondent. Multifonds DB Column is CTCL. |
| 5 | `FS.GI.APP.CORRESPONDENT.TRUST.ID` | `FsGiAppCorrespondent_TrustId` | TField |  | It specifies the trust company to measure the trust limits of an investment. Multifonds DB Column is NCORRESP_TRUST. |
| 6 | `FS.GI.APP.CORRESPONDENT.TITLE` | `FsGiAppCorrespondent_Title` | TField |  | Title code of the Correspondent. Multifonds DB Column is TITLE. |
| 7 | `FS.GI.APP.CORRESPONDENT.NAME` | `FsGiAppCorrespondent_Name` | TField |  | Name of the correspondent. Multifonds DB Column is XLIBELLE. |
| 8 | `FS.GI.APP.CORRESPONDENT.LAST.NAME` | `FsGiAppCorrespondent_LastName` | TField |  | Surname of the correspondent. Multifonds DB Column is SURNAME. |
| 9 | `FS.GI.APP.CORRESPONDENT.FIRST.NAME` | `FsGiAppCorrespondent_FirstName` | TField |  | First name of the correspondent. Multifonds DB Column is FORNAME. |
| 10 | `FS.GI.APP.CORRESPONDENT.SALUTATION` | `FsGiAppCorrespondent_Salutation` | TField |  | Salutation words of the correspondent. Multifonds DB Column is SALUTATION. |
| 11 | `FS.GI.APP.CORRESPONDENT.LANGUAGE.CODE` | `FsGiAppCorrespondent_LanguageCode` | TField |  | Language code. Multifonds DB Column is CLANGUE. |
| 12 | `FS.GI.APP.CORRESPONDENT.NATIONALITY` | `FsGiAppCorrespondent_Nationality` | TField |  | It specifies the nationality of the correspondent. Multifonds DB Column is CPAYNAT. |
| 13 | `FS.GI.APP.CORRESPONDENT.DOMICILE` | `FsGiAppCorrespondent_Domicile` | TField |  | Country of residence of the correspondent. Multifonds DB Column is CDOMICI. |
| 14 | `FS.GI.APP.CORRESPONDENT.TAX.RESIDENCE` | `FsGiAppCorrespondent_TaxResidence` | TField |  | It specifies the country to which the correspondent pays tax. Multifonds DB Column is TAX_RES. |
| 15 | `FS.GI.APP.CORRESPONDENT.TAX.ID.NUMBER` | `FsGiAppCorrespondent_TaxIdNumber` | TField |  | Tax ID for FATCA process. Multifonds DB Column is TIN_NUMBER. |
| 16 | `FS.GI.APP.CORRESPONDENT.TAX.OPTION` | `FsGiAppCorrespondent_TaxOption` | TField |  | Tax option code of the correspondent. Multifonds DB Column is CTAX_OPTION. |
| 17 | `FS.GI.APP.CORRESPONDENT.DESIGNATION` | `FsGiAppCorrespondent_Designation` | TField |  | Designation that the correspondent holds. Multifonds DB Column is DESIGN. |
| 18 | `FS.GI.APP.CORRESPONDENT.OFFICER` | `FsGiAppCorrespondent_Officer` | TField |  | Officer code. Multifonds DB Column is AC_OFFICER. |
| 19 | `FS.GI.APP.CORRESPONDENT.INTRODUCER` | `FsGiAppCorrespondent_Introducer` | TField |  | Introducer code. Multifonds DB Column is INTRODUCER. |
| 20 | `FS.GI.APP.CORRESPONDENT.PAYMENT.TYPE` | `FsGiAppCorrespondent_PaymentType` | TField |  | Payment type code of the correspondent. Multifonds DB Column is CODE_PMT. |
| 21 | `FS.GI.APP.CORRESPONDENT.PAYMENT.DESCRIPTION` | `FsGiAppCorrespondent_PaymentDescription` | TField |  | Payment type description of the correspondent. Multifonds DB Column is LIB_PMT. |
| 22 | `FS.GI.APP.CORRESPONDENT.PAYMENT.INSTUCTION.TYPE` | `FsGiAppCorrespondent_PaymentInstuctionType` | TField |  | The payment instruction type of the correspondent. Multifonds DB Column is PAYMT_INST_TYPE. |
| 23 | `FS.GI.APP.CORRESPONDENT.FEE.SHARE.CODE` | `FsGiAppCorrespondent_FeeShareCode` | TField |  | Fee share code. Multifonds DB Column is SHARE_FEES. |
| 24 | `FS.GI.APP.CORRESPONDENT.OECD.FLAG` | `FsGiAppCorrespondent_OecdFlag` | TField |  | OECD Flag of the correspondent. Multifonds DB Column is CR_CEE. |
| 25 | `FS.GI.APP.CORRESPONDENT.PAYING.AGENT.TYPE` | `FsGiAppCorrespondent_PayingAgentType` | TField |  | It specifies the paying agent type. Multifonds DB Column is CPA_TYPE. |
| 26 | `FS.GI.APP.CORRESPONDENT.CATEGORY` | `FsGiAppCorrespondent_Category` | TField |  | Category code of the correspondent. Multifonds DB Column is CAT_EMET. |
| 27 | `FS.GI.APP.CORRESPONDENT.ISSUERS.EQUITY` | `FsGiAppCorrespondent_IssuersEquity` | TField |  | Issuers equity. Multifonds DB Column is NISSUER_EQUITY. |
| 28 | `FS.GI.APP.CORRESPONDENT.DEPOSIT.INSURANCE` | `FsGiAppCorrespondent_DepositInsurance` | TField |  | Deposit Insurance specified as 0-9 +E (i.e. scientific notation). Related to the equity. Multifonds DB Column is NDEPOSIT_INSURANCE. |
| 29 | `FS.GI.APP.CORRESPONDENT.MEDIA.CN` | `FsGiAppCorrespondent_MediaCn` | TField |  | The media code through which a contract note is sent to this correspondant by the TA. Multifonds DB Column is CMEDIA_CN. |
| 30 | `FS.GI.APP.CORRESPONDENT.NO.DOCUMENT.GENERATION.FLAG` | `FsGiAppCorrespondent_NoDocumentGenerationFlag` | TField |  | Flag is relevant only if the &apos;thirdPartyType&apos; is GE - Management Company. For all others this field is stored as N. Multifonds DB Column is FLG_NO_DOCUMENT. |
| 31 | `FS.GI.APP.CORRESPONDENT.GIIN.NUMBER` | `FsGiAppCorrespondent_GiinNumber` | TField |  | GIIN identification number. Multifonds DB Column is FAT_GIIN. |
| 32 | `FS.GI.APP.CORRESPONDENT.SHORT.NAME` | `FsGiAppCorrespondent_ShortName` | TField |  | Short name of the correspondent. Multifonds DB Column is SHORT_ID. |
| 33 | `FS.GI.APP.CORRESPONDENT.GLOBAL.ORDERING.SENDING.TYPE` | `FsGiAppCorrespondent_GlobalOrderingSendingType` | TField |  | Sending method and DN code for the Central TA. Multifonds DB Column is SUB_RED_METHOD. |
| 34 | `FS.GI.APP.CORRESPONDENT.GLOBAL.ORDERING.SWITCH.TYPE` | `FsGiAppCorrespondent_GlobalOrderingSwitchType` | TField |  | Sending method and DN code for the Central TA for Switch transactions. Multifonds DB Column is SWITCH_METHOD. |
| 35 | `FS.GI.APP.CORRESPONDENT.GLOBAL.ORDERING.TRANSFER.TYPE` | `FsGiAppCorrespondent_GlobalOrderingTransferType` | TField |  | Sending method and DN code for the Central TA for transfer transactions. Multifonds DB Column is TRANSFER_METHOD. |
| 36 | `FS.GI.APP.CORRESPONDENT.RECEPTION.MODE` | `FsGiAppCorrespondent_ReceptionMode` | TField |  | To indicate the channel used with the STP Counterpart, related to NSCC and Swift. Multifonds DB Column is MODE_RECD. |
| 37 | `FS.GI.APP.CORRESPONDENT.STP.GROUP` | `FsGiAppCorrespondent_StpGroup` | TField |  | It specifies the User group ID for which user&apos;s rights to be given in order to load the STP orders. Multifonds DB Column is STP_GRP. |
| 38 | `FS.GI.APP.CORRESPONDENT.DEPOSITOR.ID` | `FsGiAppCorrespondent_DepositorId` | TField |  | Depositor linked to the correspondent. Multifonds DB Column is DEPOSITOR. |
| 39 | `FS.GI.APP.CORRESPONDENT.RIGHT.TYPE` | `FsGiAppCorrespondent_RightType` | TField |  | The rights on Funds by right type ID. Multifonds DB Column is RIGHT_TYPE. |
| 40 | `FS.GI.APP.CORRESPONDENT.ADDRESS.LINE1` | `FsGiAppCorrespondent_AddressLine1` | TField |  | Address line 1 of correspondent. Multifonds DB Column is ADRESS1. |
| 41 | `FS.GI.APP.CORRESPONDENT.ADDRESS.LINE2` | `FsGiAppCorrespondent_AddressLine2` | TField |  | Address line 2 of correspondent. Multifonds DB Column is ADRESS2. |
| 42 | `FS.GI.APP.CORRESPONDENT.ADDRESS.LINE3` | `FsGiAppCorrespondent_AddressLine3` | TField |  | Address line 3 of correspondent. Multifonds DB Column is ADRESS3. |
| 43 | `FS.GI.APP.CORRESPONDENT.ADDRESS.LINE4` | `FsGiAppCorrespondent_AddressLine4` | TField |  | Address line 4 of correspondent. Multifonds DB Column is ADRESS4. |
| 44 | `FS.GI.APP.CORRESPONDENT.ADDRESS.LINE5` | `FsGiAppCorrespondent_AddressLine5` | TField |  | Address line 5 of correspondent. Multifonds DB Column is ADRESS5. |
| 45 | `FS.GI.APP.CORRESPONDENT.ADDRESS.LINE6` | `FsGiAppCorrespondent_AddressLine6` | TField |  | Address line 6. Multifonds DB Column is ADRESS6. |
| 46 | `FS.GI.APP.CORRESPONDENT.ZIP.CODE` | `FsGiAppCorrespondent_ZipCode` | TField |  | Postal zip code of correspondent. Multifonds DB Column is ZIP_CODE. |
| 47 | `FS.GI.APP.CORRESPONDENT.ATTENTION.OF.LINE1` | `FsGiAppCorrespondent_AttentionOfLine1` | TField |  | Contact details for the address. Multifonds DB Column is ATTENTION_OF. |
| 48 | `FS.GI.APP.CORRESPONDENT.TELEPHONE.NUMBER1` | `FsGiAppCorrespondent_TelephoneNumber1` | TField |  | First telephone number of the correspondent. Multifonds DB Column is TEL1. |
| 49 | `FS.GI.APP.CORRESPONDENT.TELEPHONE.NUMBER2` | `FsGiAppCorrespondent_TelephoneNumber2` | TField |  | Second telephone phone number of the correspondent. Multifonds DB Column is TEL2. |
| 50 | `FS.GI.APP.CORRESPONDENT.FAX.NUMBER` | `FsGiAppCorrespondent_FaxNumber` | TField |  | FAX number of the correspondent. Multifonds DB Column is FAX. |
| 51 | `FS.GI.APP.CORRESPONDENT.TELEX.NUMBER` | `FsGiAppCorrespondent_TelexNumber` | TField |  | Telex number of the correspondent. Multifonds DB Column is TELEX. |
| 52 | `FS.GI.APP.CORRESPONDENT.MAIL.CORRESPONDENT.ID` | `FsGiAppCorrespondent_MailCorrespondentId` | TField |  | It specifies the correspondent to which the mails are sent to. Multifonds DB Column is CORRES. |
| 53 | `FS.GI.APP.CORRESPONDENT.CONTACT.ID` | `FsGiAppCorrespondent_ContactId` | TField |  | Allows to link this central register to the Contact lists of the selected central register. Multifonds DB Column is NCORRESP_CONTACT. |
| 54 | `FS.GI.APP.CORRESPONDENT.BLZ.CODE` | `FsGiAppCorrespondent_BlzCode` | TField |  | Bankleizahl number. Multifonds DB Column is BLZ. |
| 55 | `FS.GI.APP.CORRESPONDENT.BRANCH.CODE` | `FsGiAppCorrespondent_BranchCode` | TField |  | It specifies the branch code of the correspondent. Multifonds DB Column is SCO. |
| 56 | `FS.GI.APP.CORRESPONDENT.ACCOUNT.NUMBER1` | `FsGiAppCorrespondent_AccountNumber1` | TField |  | Intermediate account 1. Multifonds DB Column is VIA_ACCOUNT_NO1. |
| 57 | `FS.GI.APP.CORRESPONDENT.ACCOUNT.NUMBER2` | `FsGiAppCorrespondent_AccountNumber2` | TField |  | Intermediate account 2. Multifonds DB Column is VIA_ACCOUNT_NO2. |
| 58 | `FS.GI.APP.CORRESPONDENT.VIA1` | `FsGiAppCorrespondent_Via1` | TField |  | Via 1 value Multifonds DB Column is VIA_1. |
| 59 | `FS.GI.APP.CORRESPONDENT.VIA2` | `FsGiAppCorrespondent_Via2` | TField |  | Via 2 value Multifonds DB Column is VIA_2. |
| 60 | `FS.GI.APP.CORRESPONDENT.SWIFT.ADDRESS` | `FsGiAppCorrespondent_SwiftAddress` | TField |  | Bank Identifier code of the correspondant. Multifonds DB Column is COD_SWIFT. |
| 61 | `FS.GI.APP.CORRESPONDENT.SWIFT.BIC` | `FsGiAppCorrespondent_SwiftBic` | TField |  | Swift ID of the correspondent. Multifonds DB Column is SWIFT_ID. |
| 62 | `FS.GI.APP.CORRESPONDENT.SWIFT.DN` | `FsGiAppCorrespondent_SwiftDn` | TField |  | SWIFT Id as used for XML format messages. Distinguished Name Code for STP Counterparty using message format 20022. Multifonds DB Column is DN_CODE. |
| 63 | `FS.GI.APP.CORRESPONDENT.SWIFT.FORMAT` | `FsGiAppCorrespondent_SwiftFormat` | TField |  | Swift language of the correspondent. Multifonds DB Column is SWIFT_LANG. |
| 64 | `FS.GI.APP.CORRESPONDENT.RESERVED10` | `FsGiAppCorrespondent_Reserved10` | TField |  |  |
| 65 | `FS.GI.APP.CORRESPONDENT.RESERVED9` | `FsGiAppCorrespondent_Reserved9` | TField |  |  |
| 66 | `FS.GI.APP.CORRESPONDENT.RESERVED8` | `FsGiAppCorrespondent_Reserved8` | TField |  |  |
| 67 | `FS.GI.APP.CORRESPONDENT.RESERVED7` | `FsGiAppCorrespondent_Reserved7` | TField |  |  |
| 68 | `FS.GI.APP.CORRESPONDENT.RESERVED6` | `FsGiAppCorrespondent_Reserved6` | TField |  |  |
| 69 | `FS.GI.APP.CORRESPONDENT.RESERVED5` | `FsGiAppCorrespondent_Reserved5` | TField |  |  |
| 70 | `FS.GI.APP.CORRESPONDENT.RESERVED4` | `FsGiAppCorrespondent_Reserved4` | TField |  |  |
| 71 | `FS.GI.APP.CORRESPONDENT.RESERVED3` | `FsGiAppCorrespondent_Reserved3` | TField |  |  |
| 72 | `FS.GI.APP.CORRESPONDENT.RESERVED2` | `FsGiAppCorrespondent_Reserved2` | TField |  |  |
| 73 | `FS.GI.APP.CORRESPONDENT.RESERVED1` | `FsGiAppCorrespondent_Reserved1` | TField |  |  |
| 74 | `FS.GI.APP.CORRESPONDENT.LOCAL.REF` | `FsGiAppCorrespondent_LocalRef` |  |  |  |
| 75 | `FS.GI.APP.CORRESPONDENT.OVERRIDE` | `FsGiAppCorrespondent_Override` |  |  |  |
| 76 | `FS.GI.APP.CORRESPONDENT.RECORD.STATUS` | `FsGiAppCorrespondent_RecordStatus` | String |  |  |
| 77 | `FS.GI.APP.CORRESPONDENT.CURR.NO` | `FsGiAppCorrespondent_CurrNo` | String |  |  |
| 78 | `FS.GI.APP.CORRESPONDENT.INPUTTER` | `FsGiAppCorrespondent_Inputter` |  |  |  |
| 79 | `FS.GI.APP.CORRESPONDENT.DATE.TIME` | `FsGiAppCorrespondent_DateTime` |  |  |  |
| 80 | `FS.GI.APP.CORRESPONDENT.AUTHORISER` | `FsGiAppCorrespondent_Authoriser` | String |  |  |
| 81 | `FS.GI.APP.CORRESPONDENT.CO.CODE` | `FsGiAppCorrespondent_CoCode` | String |  |  |
| 82 | `FS.GI.APP.CORRESPONDENT.DEPT.CODE` | `FsGiAppCorrespondent_DeptCode` | String |  |  |
| 83 | `FS.GI.APP.CORRESPONDENT.AUDITOR.CODE` | `FsGiAppCorrespondent_AuditorCode` | String |  |  |
| 84 | `FS.GI.APP.CORRESPONDENT.AUDIT.DATE.TIME` | `FsGiAppCorrespondent_AuditDateTime` | String |  |  |
