# FS.GI.APP.BANK.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.BANK.ACCOUNT` in `FS_BankAccount.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.BANK.ACCOUNT.PARENT.REF.ID` | `FsGiAppBankAccount_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.BANK.ACCOUNT.ORA.ROWID` | `FsGiAppBankAccount_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.BANK.ACCOUNT.PARENT.ID.TYPE` | `FsGiAppBankAccount_ParentIdType` | TField |  | Type of Entity for which this instruction is held Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.BANK.ACCOUNT.PARENT.ID` | `FsGiAppBankAccount_ParentId` | TField |  | ID of the Entity for which this instruction is held Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.BANK.ACCOUNT.OPERATION.CODE` | `FsGiAppBankAccount_OperationCode` | TField |  | Operation code for which this account is to be used; e.g. sub, red, switch out/in, reinvest, saving plan, annuity, dividend payment, tax reclaims, constitution, all operations Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.APP.BANK.ACCOUNT.TA.FUND.ID` | `FsGiAppBankAccount_TaFundId` | TField |  | Fund External ID linked to the Bank Account. Multifonds DB Column is NPTF_PAY. |
| 7 | `FS.GI.APP.BANK.ACCOUNT.FUND.ID` | `FsGiAppBankAccount_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.APP.BANK.ACCOUNT.CLASS.CURRENCY` | `FsGiAppBankAccount_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.APP.BANK.ACCOUNT.SHARE.CLASS` | `FsGiAppBankAccount_ShareClass` | TField |  | Share class to which the bank account is linked. Multifonds DB Column is CLASS_CODE. |
| 10 | `FS.GI.APP.BANK.ACCOUNT.PRODUCT.CODE` | `FsGiAppBankAccount_ProductCode` | TField |  | Retail product type restriction for this account Multifonds DB Column is NPROD. |
| 11 | `FS.GI.APP.BANK.ACCOUNT.ACCOUNT.CURRENCY` | `FsGiAppBankAccount_AccountCurrency` | TField |  | The bank account currency code (in 3 letter format eg : USD). Multifonds DB Column is CMON. |
| 12 | `FS.GI.APP.BANK.ACCOUNT.ACCOUNT.TYPE` | `FsGiAppBankAccount_AccountType` | TField |  | The account type code. Multifonds DB Column is ACC_TYPE. |
| 13 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDENT.ID` | `FsGiAppBankAccount_CorrespondentId` | TField |  | ID of the Bank for this instruction Multifonds DB Column is NCORRESP. |
| 14 | `FS.GI.APP.BANK.ACCOUNT.SWIFT.CODE` | `FsGiAppBankAccount_SwiftCode` | TField |  | Swift Code is a Standard format of Bank identifier code (BIC). Multifonds DB Column is SWIFT_CODE. |
| 15 | `FS.GI.APP.BANK.ACCOUNT.BENEFICIARY.ACCOUNT.NAME` | `FsGiAppBankAccount_BeneficiaryAccountName` | TField |  | Name of the Beneficiary Account Holder Multifonds DB Column is ACCOUNT_NAME. |
| 16 | `FS.GI.APP.BANK.ACCOUNT.BENEFICIARY.ACCOUNT.NUMBER` | `FsGiAppBankAccount_BeneficiaryAccountNumber` | TField |  | Beneficiary Account Number Multifonds DB Column is ACCOUNT_NO. |
| 17 | `FS.GI.APP.BANK.ACCOUNT.IBAN.CODE` | `FsGiAppBankAccount_IbanCode` | TField |  | The International Bank Account Number (IBAN) , internationally agreed system of identifying bank accounts across national borders. Multifonds DB Column is IBAN_CODE. |
| 18 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.METHOD` | `FsGiAppBankAccount_RoutingMethod` | TField |  | Bank Routing Method Multifonds DB Column is ROUTING_METHOD. |
| 19 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.CODE` | `FsGiAppBankAccount_RoutingCode` | TField |  | Bank Routing Code Multifonds DB Column is ROUTING_CODE. |
| 20 | `FS.GI.APP.BANK.ACCOUNT.PAY.SWIFT.FLAG` | `FsGiAppBankAccount_PaySwiftFlag` | TField |  | Flag allows to use the Beneficiary Bank SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT. |
| 21 | `FS.GI.APP.BANK.ACCOUNT.PAY.ROUTING.FLAG` | `FsGiAppBankAccount_PayRoutingFlag` | TField |  | Flag allows to use the beneficiary bank routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING. |
| 22 | `FS.GI.APP.BANK.ACCOUNT.FINAL.BENEFICIARY.TYPE` | `FsGiAppBankAccount_FinalBeneficiaryType` | TField |  | The final beneficiary type. Multifonds DB Column is CTYPE. |
| 23 | `FS.GI.APP.BANK.ACCOUNT.ACCOUNT.REFERENCE` | `FsGiAppBankAccount_AccountReference` | TField |  | Free text to add any special information specific to payments in the account Multifonds DB Column is ACCOUNT_REFERENCE. |
| 24 | `FS.GI.APP.BANK.ACCOUNT.CHARGES.FLAG` | `FsGiAppBankAccount_ChargesFlag` | TField |  | It specifies if the bank charges are associated to the wire. Multifonds DB Column is CHARGES. |
| 25 | `FS.GI.APP.BANK.ACCOUNT.CHARGES.CODE` | `FsGiAppBankAccount_ChargesCode` | TField |  | It specifies the entity who should bear the bank charges associated to the wire. Multifonds DB Column is CHARGES_DETAILS. |
| 26 | `FS.GI.APP.BANK.ACCOUNT.NETTING.GROUP` | `FsGiAppBankAccount_NettingGroup` | TField |  | The description of cash movements of the bank to be grouped and / or netted. Multifonds DB Column is GROUP_NET. |
| 27 | `FS.GI.APP.BANK.ACCOUNT.NETTING.GROUP.TYPE` | `FsGiAppBankAccount_NettingGroupType` | TField |  | Grouping/Netting type of the cash movements. Multifonds DB Column is GROUP_NET_TYP. |
| 28 | `FS.GI.APP.BANK.ACCOUNT.FINAL.BENEFICIARY` | `FsGiAppBankAccount_FinalBeneficiary` | TField |  | Name of the FFC account holder Multifonds DB Column is FINAL_BENEFICIARY. |
| 29 | `FS.GI.APP.BANK.ACCOUNT.FCC.REFERENCE` | `FsGiAppBankAccount_FccReference` | TField |  | For Further Credit (FFC) reference, free text to add any special information specific to payments in the account Multifonds DB Column is FCC_REFERENCE. |
| 30 | `FS.GI.APP.BANK.ACCOUNT.FCC.ACCOUNT.NUMBER` | `FsGiAppBankAccount_FccAccountNumber` | TField |  | For Further Credit (FFC) account Number Multifonds DB Column is FCC_ACC_NO. |
| 31 | `FS.GI.APP.BANK.ACCOUNT.PENDING.PAYMENT.STOP.FLAG` | `FsGiAppBankAccount_PendingPaymentStopFlag` | TField |  | Flag allows to suspend any pending payments in case a change to the bank mandate has been received. Multifonds DB Column is STP_PEND_PYMT. |
| 32 | `FS.GI.APP.BANK.ACCOUNT.THIRD.PARTY.PAYMENT.FLAG` | `FsGiAppBankAccount_ThirdPartyPaymentFlag` | TField |  | Flag allows to use this bank account detail for third party payments. Multifonds DB Column is FLG_THIRD_PARTY_PAY. |
| 33 | `FS.GI.APP.BANK.ACCOUNT.SEPA.COMPLIANT` | `FsGiAppBankAccount_SepaCompliant` | TField |  | Flag to enable or disable Bank Account for SEPA compliant. Multifonds DB Column is FLG_SEPA_COMPLIANT. |
| 34 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.EXTERNAL.ID.1` | `FsGiAppBankAccount_CorrespondantExternalId1` | TField |  | Correspondent Bank 1 Id Multifonds DB Column is NCORRESP1. |
| 35 | `FS.GI.APP.BANK.ACCOUNT.SWIFT.CODE1` | `FsGiAppBankAccount_SwiftCode1` | TField |  | Correspondent Bank 1 Swift Code (BIC) Multifonds DB Column is SWIFT_CODE1. |
| 36 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NAME.1` | `FsGiAppBankAccount_CorrespondantAccountName1` | TField |  | Name of the Correspondant Account Holder 1 Multifonds DB Column is ACCOUNT_NAME1. |
| 37 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NUMBER.1` | `FsGiAppBankAccount_CorrespondantAccountNumber1` | TField |  | Correspondant Account Number 1 Multifonds DB Column is ACCOUNT_NO1. |
| 38 | `FS.GI.APP.BANK.ACCOUNT.IBAN.CODE1` | `FsGiAppBankAccount_IbanCode1` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 1 Multifonds DB Column is IBAN_CODE1. |
| 39 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.METHOD1` | `FsGiAppBankAccount_RoutingMethod1` | TField |  | Correspondent Bank 1 Routing Method Multifonds DB Column is ROUTING_METHOD1. |
| 40 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.CODE1` | `FsGiAppBankAccount_RoutingCode1` | TField |  | Correspondent Bank 1 Routing Code Multifonds DB Column is ROUTING_CODE1. |
| 41 | `FS.GI.APP.BANK.ACCOUNT.PAY.SWIFT.FLAG1` | `FsGiAppBankAccount_PaySwiftFlag1` | TField |  | Flag allows to use the Beneficiary Bank 1 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT1. |
| 42 | `FS.GI.APP.BANK.ACCOUNT.PAY.ROUTING.FLAG1` | `FsGiAppBankAccount_PayRoutingFlag1` | TField |  | Flag allows to use the Beneficiary Bank 1 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING1. |
| 43 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.EXTERNAL.ID.2` | `FsGiAppBankAccount_CorrespondantExternalId2` | TField |  | Correspondent Bank 2 Id Multifonds DB Column is NCORRESP2. |
| 44 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NAME.2` | `FsGiAppBankAccount_CorrespondantAccountName2` | TField |  | Name of the Correspondant Account Holder 2 Multifonds DB Column is ACCOUNT_NAME2. |
| 45 | `FS.GI.APP.BANK.ACCOUNT.SWIFT.CODE2` | `FsGiAppBankAccount_SwiftCode2` | TField |  | Correspondent Bank 2 Swift Code (BIC) Multifonds DB Column is SWIFT_CODE2. |
| 46 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NUMBER.2` | `FsGiAppBankAccount_CorrespondantAccountNumber2` | TField |  | Correspondant Account Number 2 Multifonds DB Column is ACCOUNT_NO2. |
| 47 | `FS.GI.APP.BANK.ACCOUNT.IBAN.CODE2` | `FsGiAppBankAccount_IbanCode2` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 2 Multifonds DB Column is IBAN_CODE2. |
| 48 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.METHOD2` | `FsGiAppBankAccount_RoutingMethod2` | TField |  | Routing Method 2 Multifonds DB Column is ROUTING_METHOD2. |
| 49 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.CODE2` | `FsGiAppBankAccount_RoutingCode2` | TField |  | Correspondent Bank 2 Routing Code Multifonds DB Column is ROUTING_CODE2. |
| 50 | `FS.GI.APP.BANK.ACCOUNT.PAY.SWIFT.FLAG2` | `FsGiAppBankAccount_PaySwiftFlag2` | TField |  | Flag allows to use the Beneficiary Bank 2 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT2. |
| 51 | `FS.GI.APP.BANK.ACCOUNT.PAY.ROUTING.FLAG2` | `FsGiAppBankAccount_PayRoutingFlag2` | TField |  | Flag allows to use the Beneficiary Bank 2 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING2. |
| 52 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.EXTERNAL.ID.3` | `FsGiAppBankAccount_CorrespondantExternalId3` | TField |  | Correspondent Bank 3 Id Multifonds DB Column is NCORRESP3. |
| 53 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NAME.3` | `FsGiAppBankAccount_CorrespondantAccountName3` | TField |  | Name of the Correspondant Account Holder 3 Multifonds DB Column is ACCOUNT_NAME3. |
| 54 | `FS.GI.APP.BANK.ACCOUNT.SWIFT.CODE3` | `FsGiAppBankAccount_SwiftCode3` | TField |  | Correspondent Bank 3 Swift Code (BIC) Multifonds DB Column is SWIFT_CODE3. |
| 55 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NUMBER.3` | `FsGiAppBankAccount_CorrespondantAccountNumber3` | TField |  | Correspondant Account Number 3 Multifonds DB Column is ACCOUNT_NO3. |
| 56 | `FS.GI.APP.BANK.ACCOUNT.IBAN.CODE3` | `FsGiAppBankAccount_IbanCode3` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 3 Multifonds DB Column is IBAN_CODE3. |
| 57 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.METHOD3` | `FsGiAppBankAccount_RoutingMethod3` | TField |  | Correspondent Bank 3 Routing Method 3 Multifonds DB Column is ROUTING_METHOD3. |
| 58 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.CODE3` | `FsGiAppBankAccount_RoutingCode3` | TField |  | Correspondent Bank 3 Routing Code Multifonds DB Column is ROUTING_CODE3. |
| 59 | `FS.GI.APP.BANK.ACCOUNT.PAY.SWIFT.FLAG3` | `FsGiAppBankAccount_PaySwiftFlag3` | TField |  | Flag allows to use the Beneficiary Bank 3 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT3. |
| 60 | `FS.GI.APP.BANK.ACCOUNT.PAY.ROUTING.FLAG3` | `FsGiAppBankAccount_PayRoutingFlag3` | TField |  | Flag allows to use the Beneficiary Bank 3 routing method while creating payment instruction Multifonds DB Column is PAY_ROUTING3. |
| 61 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.EXTERNAL.ID.4` | `FsGiAppBankAccount_CorrespondantExternalId4` | TField |  | Correspondent Bank 4 Id Multifonds DB Column is NCORRESP4. |
| 62 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NAME.4` | `FsGiAppBankAccount_CorrespondantAccountName4` | TField |  | Name of the Correspondant Account Holder 4 Multifonds DB Column is ACCOUNT_NAME4. |
| 63 | `FS.GI.APP.BANK.ACCOUNT.SWIFT.CODE4` | `FsGiAppBankAccount_SwiftCode4` | TField |  | Correspondent Bank 4 Swift Code (BIC) Multifonds DB Column is SWIFT_CODE4. |
| 64 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NUMBER.4` | `FsGiAppBankAccount_CorrespondantAccountNumber4` | TField |  | Correspondant Account Number 4 Multifonds DB Column is ACCOUNT_NO4. |
| 65 | `FS.GI.APP.BANK.ACCOUNT.IBAN.CODE4` | `FsGiAppBankAccount_IbanCode4` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 4 Multifonds DB Column is IBAN_CODE4. |
| 66 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.METHOD4` | `FsGiAppBankAccount_RoutingMethod4` | TField |  | Correspondent Bank 4 Routing Method Multifonds DB Column is ROUTING_METHOD4. |
| 67 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.CODE4` | `FsGiAppBankAccount_RoutingCode4` | TField |  | Correspondent Bank 4 Routing Code Multifonds DB Column is ROUTING_CODE4. |
| 68 | `FS.GI.APP.BANK.ACCOUNT.PAY.SWIFT.FLAG4` | `FsGiAppBankAccount_PaySwiftFlag4` | TField |  | Flag allows to use the Beneficiary Bank 4 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT4. |
| 69 | `FS.GI.APP.BANK.ACCOUNT.PAY.ROUTING.FLAG4` | `FsGiAppBankAccount_PayRoutingFlag4` | TField |  | Flag allows to use the Beneficiary Bank 4 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING4. |
| 70 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.EXTERNAL.ID.5` | `FsGiAppBankAccount_CorrespondantExternalId5` | TField |  | Correspondent Bank 5 Id Multifonds DB Column is NCORRESP5. |
| 71 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NAME.5` | `FsGiAppBankAccount_CorrespondantAccountName5` | TField |  | Name of the Correspondant Account Holder 5 Multifonds DB Column is ACCOUNT_NAME5. |
| 72 | `FS.GI.APP.BANK.ACCOUNT.SWIFT.CODE5` | `FsGiAppBankAccount_SwiftCode5` | TField |  | Correspondent Bank 5 Swift Code (BIC) Multifonds DB Column is SWIFT_CODE5. |
| 73 | `FS.GI.APP.BANK.ACCOUNT.CORRESPONDANT.ACCOUNT.NUMBER.5` | `FsGiAppBankAccount_CorrespondantAccountNumber5` | TField |  | Correspondant Account Number 5 Multifonds DB Column is ACCOUNT_NO5. |
| 74 | `FS.GI.APP.BANK.ACCOUNT.IBAN.CODE5` | `FsGiAppBankAccount_IbanCode5` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 5 Multifonds DB Column is IBAN_CODE5. |
| 75 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.METHOD5` | `FsGiAppBankAccount_RoutingMethod5` | TField |  | Correspondent Bank 5 Routing Method Multifonds DB Column is ROUTING_METHOD5. |
| 76 | `FS.GI.APP.BANK.ACCOUNT.ROUTING.CODE5` | `FsGiAppBankAccount_RoutingCode5` | TField |  | Correspondent Bank 5 Routing Code Multifonds DB Column is ROUTING_CODE5. |
| 77 | `FS.GI.APP.BANK.ACCOUNT.PAY.SWIFT.FLAG5` | `FsGiAppBankAccount_PaySwiftFlag5` | TField |  | Flag allows to use the Beneficiary Bank 5 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT5. |
| 78 | `FS.GI.APP.BANK.ACCOUNT.PAY.ROUTING.FLAG5` | `FsGiAppBankAccount_PayRoutingFlag5` | TField |  | Flag allows to use the Beneficiary Bank 5 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING5. |
| 79 | `FS.GI.APP.BANK.ACCOUNT.CHANGE.REASON.CODE` | `FsGiAppBankAccount_ChangeReasonCode` | TField |  | A code to track the reason why an Account field is updated by a user. Multifonds DB Column is CHG_REASON. |
| 80 | `FS.GI.APP.BANK.ACCOUNT.CHANGE.REASON.COMMENT` | `FsGiAppBankAccount_ChangeReasonComment` | TField |  | Account Change Comment Multifonds DB Column is CHG_COMMENT. |
| 81 | `FS.GI.APP.BANK.ACCOUNT.BENEFICIARY.BANK.COUNTRY` | `FsGiAppBankAccount_BeneficiaryBankCountry` | TField |  | Beneficiary bank country Multifonds DB Column is EUR_PAY_COUNTRY. |
| 82 | `FS.GI.APP.BANK.ACCOUNT.RESERVED10` | `FsGiAppBankAccount_Reserved10` | TField |  |  |
| 83 | `FS.GI.APP.BANK.ACCOUNT.RESERVED9` | `FsGiAppBankAccount_Reserved9` | TField |  |  |
| 84 | `FS.GI.APP.BANK.ACCOUNT.RESERVED8` | `FsGiAppBankAccount_Reserved8` | TField |  |  |
| 85 | `FS.GI.APP.BANK.ACCOUNT.RESERVED7` | `FsGiAppBankAccount_Reserved7` | TField |  |  |
| 86 | `FS.GI.APP.BANK.ACCOUNT.RESERVED6` | `FsGiAppBankAccount_Reserved6` | TField |  |  |
| 87 | `FS.GI.APP.BANK.ACCOUNT.RESERVED5` | `FsGiAppBankAccount_Reserved5` | TField |  |  |
| 88 | `FS.GI.APP.BANK.ACCOUNT.RESERVED4` | `FsGiAppBankAccount_Reserved4` | TField |  |  |
| 89 | `FS.GI.APP.BANK.ACCOUNT.RESERVED3` | `FsGiAppBankAccount_Reserved3` | TField |  |  |
| 90 | `FS.GI.APP.BANK.ACCOUNT.RESERVED2` | `FsGiAppBankAccount_Reserved2` | TField |  |  |
| 91 | `FS.GI.APP.BANK.ACCOUNT.RESERVED1` | `FsGiAppBankAccount_Reserved1` | TField |  |  |
| 92 | `FS.GI.APP.BANK.ACCOUNT.LOCAL.REF` | `FsGiAppBankAccount_LocalRef` |  |  |  |
| 93 | `FS.GI.APP.BANK.ACCOUNT.OVERRIDE` | `FsGiAppBankAccount_Override` |  |  |  |
| 94 | `FS.GI.APP.BANK.ACCOUNT.RECORD.STATUS` | `FsGiAppBankAccount_RecordStatus` | String |  |  |
| 95 | `FS.GI.APP.BANK.ACCOUNT.CURR.NO` | `FsGiAppBankAccount_CurrNo` | String |  |  |
| 96 | `FS.GI.APP.BANK.ACCOUNT.INPUTTER` | `FsGiAppBankAccount_Inputter` |  |  |  |
| 97 | `FS.GI.APP.BANK.ACCOUNT.DATE.TIME` | `FsGiAppBankAccount_DateTime` |  |  |  |
| 98 | `FS.GI.APP.BANK.ACCOUNT.AUTHORISER` | `FsGiAppBankAccount_Authoriser` | String |  |  |
| 99 | `FS.GI.APP.BANK.ACCOUNT.CO.CODE` | `FsGiAppBankAccount_CoCode` | String |  |  |
| 100 | `FS.GI.APP.BANK.ACCOUNT.DEPT.CODE` | `FsGiAppBankAccount_DeptCode` | String |  |  |
| 101 | `FS.GI.APP.BANK.ACCOUNT.AUDITOR.CODE` | `FsGiAppBankAccount_AuditorCode` | String |  |  |
| 102 | `FS.GI.APP.BANK.ACCOUNT.AUDIT.DATE.TIME` | `FsGiAppBankAccount_AuditDateTime` | String |  |  |
