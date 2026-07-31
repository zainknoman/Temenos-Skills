# FS.GI.APP.BANK.ACCOUNT.CON — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.BANK.ACCOUNT.CON` in `FS_TransactionEntry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.BANK.ACCOUNT.CON.PARENT.REF.ID` | `FsGiAppBankAccountCon_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.BANK.ACCOUNT.CON.ORA.ROWID` | `FsGiAppBankAccountCon_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.BANK.ACCOUNT.CON.PARENT.ID.TYPE` | `FsGiAppBankAccountCon_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.BANK.ACCOUNT.CON.PARENT.ID` | `FsGiAppBankAccountCon_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.BANK.ACCOUNT.CON.OPERATION.CODE` | `FsGiAppBankAccountCon_OperationCode` | TField |  | Operation code for which this account is to be used; e.g. sub, red, switch out/in, reinvest, saving plan, annuity, dividend payment, tax reclaims, constitution, all operations. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.APP.BANK.ACCOUNT.CON.TA.FUND.ID` | `FsGiAppBankAccountCon_TaFundId` | TField |  | Fund ID linked to the Bank Account. Multifonds DB Column is NPTF_PAY. |
| 7 | `FS.GI.APP.BANK.ACCOUNT.CON.FUND.ID` | `FsGiAppBankAccountCon_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.APP.BANK.ACCOUNT.CON.CLASS.CURRENCY` | `FsGiAppBankAccountCon_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.APP.BANK.ACCOUNT.CON.SHARE.CLASS` | `FsGiAppBankAccountCon_ShareClass` | TField |  | Share class to which the bank account is linked. Multifonds DB Column is CLASS_CODE. |
| 10 | `FS.GI.APP.BANK.ACCOUNT.CON.PRODUCT.CODE` | `FsGiAppBankAccountCon_ProductCode` | TField |  | Retail product type restriction for this account. Multifonds DB Column is NPROD. |
| 11 | `FS.GI.APP.BANK.ACCOUNT.CON.ACCOUNT.CURRENCY` | `FsGiAppBankAccountCon_AccountCurrency` | TField |  | Bank account currency code (in 3 letter format eg : USD). Multifonds DB Column is CMON. |
| 12 | `FS.GI.APP.BANK.ACCOUNT.CON.ACCOUNT.TYPE` | `FsGiAppBankAccountCon_AccountType` | TField |  | Account type code. Multifonds DB Column is ACC_TYPE. |
| 13 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDENT.ID` | `FsGiAppBankAccountCon_CorrespondentId` | TField |  | ID of the Bank for this instruction. Multifonds DB Column is NCORRESP. |
| 14 | `FS.GI.APP.BANK.ACCOUNT.CON.SWIFT.CODE` | `FsGiAppBankAccountCon_SwiftCode` | TField |  | Swift Code is a Standard format of Bank identifier code (BIC). Multifonds DB Column is SWIFT_CODE. |
| 15 | `FS.GI.APP.BANK.ACCOUNT.CON.BENEFICIARY.ACCOUNT.NAME` | `FsGiAppBankAccountCon_BeneficiaryAccountName` | TField |  | Name of the Beneficiary Account Holder. Multifonds DB Column is ACCOUNT_NAME. |
| 16 | `FS.GI.APP.BANK.ACCOUNT.CON.BENEFICIARY.ACCOUNT.NUMBER` | `FsGiAppBankAccountCon_BeneficiaryAccountNumber` | TField |  | Beneficiary Account Number. Multifonds DB Column is ACCOUNT_NO. |
| 17 | `FS.GI.APP.BANK.ACCOUNT.CON.IBAN.CODE` | `FsGiAppBankAccountCon_IbanCode` | TField |  | The International Bank Account Number (IBAN) , internationally agreed system of identifying bank accounts across national borders. Multifonds DB Column is IBAN_CODE. |
| 18 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.METHOD` | `FsGiAppBankAccountCon_RoutingMethod` | TField |  | Bank Routing Method. Multifonds DB Column is ROUTING_METHOD. |
| 19 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.CODE` | `FsGiAppBankAccountCon_RoutingCode` | TField |  | Bank Routing Code. Multifonds DB Column is ROUTING_CODE. |
| 20 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.SWIFT.FLAG` | `FsGiAppBankAccountCon_PaySwiftFlag` | TField |  | Flag allows to use the Beneficiary Bank SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT. |
| 21 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.ROUTING.FLAG` | `FsGiAppBankAccountCon_PayRoutingFlag` | TField |  | Flag allows to use the beneficiary bank routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING. |
| 22 | `FS.GI.APP.BANK.ACCOUNT.CON.FINAL.BENEFICIARY.TYPE` | `FsGiAppBankAccountCon_FinalBeneficiaryType` | TField |  | Final beneficiary type. Multifonds DB Column is CTYPE. |
| 23 | `FS.GI.APP.BANK.ACCOUNT.CON.ACCOUNT.REFERENCE` | `FsGiAppBankAccountCon_AccountReference` | TField |  | Free text to add any special information specific to payments in the account. Multifonds DB Column is ACCOUNT_REFERENCE. |
| 24 | `FS.GI.APP.BANK.ACCOUNT.CON.CHARGES.FLAG` | `FsGiAppBankAccountCon_ChargesFlag` | TField |  | It specifies if the bank charges are associated to the wire. Multifonds DB Column is CHARGES. |
| 25 | `FS.GI.APP.BANK.ACCOUNT.CON.CHARGES.CODE` | `FsGiAppBankAccountCon_ChargesCode` | TField |  | It specifies the entity who should bear the bank charges associated to the wire. Multifonds DB Column is CHARGES_DETAILS. |
| 26 | `FS.GI.APP.BANK.ACCOUNT.CON.NETTING.GROUP` | `FsGiAppBankAccountCon_NettingGroup` | TField |  | Cash movements of the bank to be grouped and / or netted. Multifonds DB Column is GROUP_NET. |
| 27 | `FS.GI.APP.BANK.ACCOUNT.CON.NETTING.GROUP.TYPE` | `FsGiAppBankAccountCon_NettingGroupType` | TField |  | Grouping/Netting type of the cash movements. Multifonds DB Column is GROUP_NET_TYP. |
| 28 | `FS.GI.APP.BANK.ACCOUNT.CON.FINAL.BENEFICIARY` | `FsGiAppBankAccountCon_FinalBeneficiary` | TField |  | Name of the FFC account holder. Multifonds DB Column is FINAL_BENEFICIARY. |
| 29 | `FS.GI.APP.BANK.ACCOUNT.CON.FCC.REFERENCE` | `FsGiAppBankAccountCon_FccReference` | TField |  | For Further Credit (FFC) reference, free text to add any special information specific to payments in the account. Multifonds DB Column is FCC_REFERENCE. |
| 30 | `FS.GI.APP.BANK.ACCOUNT.CON.FCC.ACCOUNT.NUMBER` | `FsGiAppBankAccountCon_FccAccountNumber` | TField |  | For Further Credit (FFC) account Number. Multifonds DB Column is FCC_ACC_NO. |
| 31 | `FS.GI.APP.BANK.ACCOUNT.CON.PENDING.PAYMENT.STOP.FLAG` | `FsGiAppBankAccountCon_PendingPaymentStopFlag` | TField |  | Flag allows to suspend any pending payments in case a change to the bank mandate has been received. Multifonds DB Column is STP_PEND_PYMT. |
| 32 | `FS.GI.APP.BANK.ACCOUNT.CON.THIRD.PARTY.PAYMENT.FLAG` | `FsGiAppBankAccountCon_ThirdPartyPaymentFlag` | TField |  | Flag allows to use this bank account detail for third party payments. Multifonds DB Column is FLG_THIRD_PARTY_PAY. |
| 33 | `FS.GI.APP.BANK.ACCOUNT.CON.SEPA.COMPLIANT` | `FsGiAppBankAccountCon_SepaCompliant` | TField |  | Flag to enable or disable Bank Account for SEPA compliant. Multifonds DB Column is FLG_SEPA_COMPLIANT. |
| 34 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.EXTERNAL.ID.1` | `FsGiAppBankAccountCon_CorrespondantExternalId1` | TField |  | Correspondent Bank 1 Id. Multifonds DB Column is NCORRESP1. |
| 35 | `FS.GI.APP.BANK.ACCOUNT.CON.SWIFT.CODE1` | `FsGiAppBankAccountCon_SwiftCode1` | TField |  | Correspondent Bank 1 Swift Code (BIC). Multifonds DB Column is SWIFT_CODE1. |
| 36 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NAME.1` | `FsGiAppBankAccountCon_CorrespondantAccountName1` | TField |  | Name of the Correspondant Account Holder 1. Multifonds DB Column is ACCOUNT_NAME1. |
| 37 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NUMBER.1` | `FsGiAppBankAccountCon_CorrespondantAccountNumber1` | TField |  | Correspondant Account Number 1. Multifonds DB Column is ACCOUNT_NO1. |
| 38 | `FS.GI.APP.BANK.ACCOUNT.CON.IBAN.CODE1` | `FsGiAppBankAccountCon_IbanCode1` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 1. Multifonds DB Column is IBAN_CODE1. |
| 39 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.METHOD1` | `FsGiAppBankAccountCon_RoutingMethod1` | TField |  | Correspondent Bank 1 Routing Method. Multifonds DB Column is ROUTING_METHOD1. |
| 40 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.CODE1` | `FsGiAppBankAccountCon_RoutingCode1` | TField |  | Correspondent Bank 1 Routing Code. Multifonds DB Column is ROUTING_CODE1. |
| 41 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.SWIFT.FLAG1` | `FsGiAppBankAccountCon_PaySwiftFlag1` | TField |  | Flag allows to use the Beneficiary Bank 1 SWIFT code while creating payment instruction.. Multifonds DB Column is PAY_SWIFT1. |
| 42 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.ROUTING.FLAG1` | `FsGiAppBankAccountCon_PayRoutingFlag1` | TField |  | Flag allows to use the Beneficiary Bank 1 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING1. |
| 43 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.EXTERNAL.ID.2` | `FsGiAppBankAccountCon_CorrespondantExternalId2` | TField |  | Correspondent Bank 2 Id. Multifonds DB Column is NCORRESP2. |
| 44 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NAME.2` | `FsGiAppBankAccountCon_CorrespondantAccountName2` | TField |  | Name of the Correspondant Account Holder 2. Multifonds DB Column is ACCOUNT_NAME2. |
| 45 | `FS.GI.APP.BANK.ACCOUNT.CON.SWIFT.CODE2` | `FsGiAppBankAccountCon_SwiftCode2` | TField |  | Correspondent Bank 2 Swift Code (BIC). Multifonds DB Column is SWIFT_CODE2. |
| 46 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NUMBER.2` | `FsGiAppBankAccountCon_CorrespondantAccountNumber2` | TField |  | Correspondant Account Number 2. Multifonds DB Column is ACCOUNT_NO2. |
| 47 | `FS.GI.APP.BANK.ACCOUNT.CON.IBAN.CODE2` | `FsGiAppBankAccountCon_IbanCode2` | TField |  | International Bank Account Number (IBAN) of Correspondant Bank 2. Multifonds DB Column is IBAN_CODE2. |
| 48 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.METHOD2` | `FsGiAppBankAccountCon_RoutingMethod2` | TField |  | Routing Method 2. Multifonds DB Column is ROUTING_METHOD2. |
| 49 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.CODE2` | `FsGiAppBankAccountCon_RoutingCode2` | TField |  | Correspondent Bank 2 Routing Code. Multifonds DB Column is ROUTING_CODE2. |
| 50 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.SWIFT.FLAG2` | `FsGiAppBankAccountCon_PaySwiftFlag2` | TField |  | Flag allows to use the Beneficiary Bank 2 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT2. |
| 51 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.ROUTING.FLAG2` | `FsGiAppBankAccountCon_PayRoutingFlag2` | TField |  | Flag allows to use the Beneficiary Bank 2 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING2. |
| 52 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.EXTERNAL.ID.3` | `FsGiAppBankAccountCon_CorrespondantExternalId3` | TField |  | Correspondent Bank 3 Id. Multifonds DB Column is NCORRESP3. |
| 53 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NAME.3` | `FsGiAppBankAccountCon_CorrespondantAccountName3` | TField |  | Name of the Correspondant Account Holder 3. Multifonds DB Column is ACCOUNT_NAME3. |
| 54 | `FS.GI.APP.BANK.ACCOUNT.CON.SWIFT.CODE3` | `FsGiAppBankAccountCon_SwiftCode3` | TField |  | Correspondent Bank 3 Swift Code (BIC). Multifonds DB Column is SWIFT_CODE3. |
| 55 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NUMBER.3` | `FsGiAppBankAccountCon_CorrespondantAccountNumber3` | TField |  | Correspondant Account Number 3. Multifonds DB Column is ACCOUNT_NO3. |
| 56 | `FS.GI.APP.BANK.ACCOUNT.CON.IBAN.CODE3` | `FsGiAppBankAccountCon_IbanCode3` | TField |  | International Bank Account Number (IBAN) of Correspondant Bank 3. Multifonds DB Column is IBAN_CODE3. |
| 57 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.METHOD3` | `FsGiAppBankAccountCon_RoutingMethod3` | TField |  | Correspondent Bank 3 Routing Method 3. Multifonds DB Column is ROUTING_METHOD3. |
| 58 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.CODE3` | `FsGiAppBankAccountCon_RoutingCode3` | TField |  | Correspondent Bank 3 Routing Code. Multifonds DB Column is ROUTING_CODE3. |
| 59 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.SWIFT.FLAG3` | `FsGiAppBankAccountCon_PaySwiftFlag3` | TField |  | Flag allows to use the Beneficiary Bank 3 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT3. |
| 60 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.ROUTING.FLAG3` | `FsGiAppBankAccountCon_PayRoutingFlag3` | TField |  | Flag allows to use the Beneficiary Bank 3 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING3. |
| 61 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.EXTERNAL.ID.4` | `FsGiAppBankAccountCon_CorrespondantExternalId4` | TField |  | Correspondent Bank 4 Id. Multifonds DB Column is NCORRESP4. |
| 62 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NAME.4` | `FsGiAppBankAccountCon_CorrespondantAccountName4` | TField |  | Name of the Correspondant Account Holder 4. Multifonds DB Column is ACCOUNT_NAME4. |
| 63 | `FS.GI.APP.BANK.ACCOUNT.CON.SWIFT.CODE4` | `FsGiAppBankAccountCon_SwiftCode4` | TField |  | Correspondent Bank 4 Swift Code (BIC). Multifonds DB Column is SWIFT_CODE4. |
| 64 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NUMBER.4` | `FsGiAppBankAccountCon_CorrespondantAccountNumber4` | TField |  | Correspondant Account Number 4. Multifonds DB Column is ACCOUNT_NO4. |
| 65 | `FS.GI.APP.BANK.ACCOUNT.CON.IBAN.CODE4` | `FsGiAppBankAccountCon_IbanCode4` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 4. Multifonds DB Column is IBAN_CODE4. |
| 66 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.METHOD4` | `FsGiAppBankAccountCon_RoutingMethod4` | TField |  | Correspondent Bank 4 Routing Method. Multifonds DB Column is ROUTING_METHOD4. |
| 67 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.CODE4` | `FsGiAppBankAccountCon_RoutingCode4` | TField |  | Correspondent Bank 4 Routing Code. Multifonds DB Column is ROUTING_CODE4. |
| 68 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.SWIFT.FLAG4` | `FsGiAppBankAccountCon_PaySwiftFlag4` | TField |  | Flag allows to use the Beneficiary Bank 4 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT4. |
| 69 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.ROUTING.FLAG4` | `FsGiAppBankAccountCon_PayRoutingFlag4` | TField |  | Flag allows to use the Beneficiary Bank 4 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING4. |
| 70 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.EXTERNAL.ID.5` | `FsGiAppBankAccountCon_CorrespondantExternalId5` | TField |  | Correspondent Bank 5 Id. Multifonds DB Column is NCORRESP5. |
| 71 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NAME.5` | `FsGiAppBankAccountCon_CorrespondantAccountName5` | TField |  | Name of the Correspondant Account Holder 5. Multifonds DB Column is ACCOUNT_NAME5. |
| 72 | `FS.GI.APP.BANK.ACCOUNT.CON.SWIFT.CODE5` | `FsGiAppBankAccountCon_SwiftCode5` | TField |  | Correspondent Bank 5 Swift Code (BIC). Multifonds DB Column is SWIFT_CODE5. |
| 73 | `FS.GI.APP.BANK.ACCOUNT.CON.CORRESPONDANT.ACCOUNT.NUMBER.5` | `FsGiAppBankAccountCon_CorrespondantAccountNumber5` | TField |  | Correspondant Account Number 5. Multifonds DB Column is ACCOUNT_NO5. |
| 74 | `FS.GI.APP.BANK.ACCOUNT.CON.IBAN.CODE5` | `FsGiAppBankAccountCon_IbanCode5` | TField |  | The International Bank Account Number (IBAN) of Correspondant Bank 5. Multifonds DB Column is IBAN_CODE5. |
| 75 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.METHOD5` | `FsGiAppBankAccountCon_RoutingMethod5` | TField |  | Correspondent Bank 5 Routing Method. Multifonds DB Column is ROUTING_METHOD5. |
| 76 | `FS.GI.APP.BANK.ACCOUNT.CON.ROUTING.CODE5` | `FsGiAppBankAccountCon_RoutingCode5` | TField |  | Correspondent Bank 5 Routing Code. Multifonds DB Column is ROUTING_CODE5. |
| 77 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.SWIFT.FLAG5` | `FsGiAppBankAccountCon_PaySwiftFlag5` | TField |  | Flag allows to use the Beneficiary Bank 5 SWIFT code while creating payment instruction. Multifonds DB Column is PAY_SWIFT5. |
| 78 | `FS.GI.APP.BANK.ACCOUNT.CON.PAY.ROUTING.FLAG5` | `FsGiAppBankAccountCon_PayRoutingFlag5` | TField |  | Flag allows to use the Beneficiary Bank 5 routing method while creating payment instruction. Multifonds DB Column is PAY_ROUTING5. |
| 79 | `FS.GI.APP.BANK.ACCOUNT.CON.BENEFICIARY.BANK.COUNTRY` | `FsGiAppBankAccountCon_BeneficiaryBankCountry` | TField |  | Beneficiary bank country. Multifonds DB Column is EUR_PAY_COUNTRY. |
| 80 | `FS.GI.APP.BANK.ACCOUNT.CON.SELECT.FLAG` | `FsGiAppBankAccountCon_SelectFlag` | TField |  | Flag indicates the selectin of bank account record. Multifonds DB Column is SEL. |
| 81 | `FS.GI.APP.BANK.ACCOUNT.CON.ORDER.ID` | `FsGiAppBankAccountCon_OrderId` | TField |  | Order internal ID. Multifonds DB Column is NORDER. |
| 82 | `FS.GI.APP.BANK.ACCOUNT.CON.AGENT.ID` | `FsGiAppBankAccountCon_AgentId` | TField |  | Agent internal ID. Multifonds DB Column is NOUTLET. |
| 83 | `FS.GI.APP.BANK.ACCOUNT.CON.COUNTERPART` | `FsGiAppBankAccountCon_Counterpart` | TField |  | Counterpart internal ID. Multifonds DB Column is COUNTERPARTY. |
| 84 | `FS.GI.APP.BANK.ACCOUNT.CON.COUNTERPART.AGENT.ID` | `FsGiAppBankAccountCon_CounterpartAgentId` | TField |  | Counterpart Agent internal ID. Multifonds DB Column is NOUTLET_CP. |
| 85 | `FS.GI.APP.BANK.ACCOUNT.CON.DEAL.REFERENCE` | `FsGiAppBankAccountCon_DealReference` | TField |  | Deal reference number of the order. Multifonds DB Column is DEAL_REF. |
| 86 | `FS.GI.APP.BANK.ACCOUNT.CON.DEAL.REFERENCE.INTERNAL` | `FsGiAppBankAccountCon_DealReferenceInternal` | TField |  | Internal Deal reference number. Multifonds DB Column is DEAL_REF_IN. |
| 87 | `FS.GI.APP.BANK.ACCOUNT.CON.LEG.LINK` | `FsGiAppBankAccountCon_LegLink` | TField |  | Leg link of the order. Multifonds DB Column is LEG_LINK. |
| 88 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED10` | `FsGiAppBankAccountCon_Reserved10` | TField |  |  |
| 89 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED9` | `FsGiAppBankAccountCon_Reserved9` | TField |  |  |
| 90 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED8` | `FsGiAppBankAccountCon_Reserved8` | TField |  |  |
| 91 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED7` | `FsGiAppBankAccountCon_Reserved7` | TField |  |  |
| 92 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED6` | `FsGiAppBankAccountCon_Reserved6` | TField |  |  |
| 93 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED5` | `FsGiAppBankAccountCon_Reserved5` | TField |  |  |
| 94 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED4` | `FsGiAppBankAccountCon_Reserved4` | TField |  |  |
| 95 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED3` | `FsGiAppBankAccountCon_Reserved3` | TField |  |  |
| 96 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED2` | `FsGiAppBankAccountCon_Reserved2` | TField |  |  |
| 97 | `FS.GI.APP.BANK.ACCOUNT.CON.RESERVED1` | `FsGiAppBankAccountCon_Reserved1` | TField |  |  |
| 98 | `FS.GI.APP.BANK.ACCOUNT.CON.LOCAL.REF` | `FsGiAppBankAccountCon_LocalRef` |  |  |  |
| 99 | `FS.GI.APP.BANK.ACCOUNT.CON.OVERRIDE` | `FsGiAppBankAccountCon_Override` |  |  |  |
| 100 | `FS.GI.APP.BANK.ACCOUNT.CON.RECORD.STATUS` | `FsGiAppBankAccountCon_RecordStatus` | String |  |  |
| 101 | `FS.GI.APP.BANK.ACCOUNT.CON.CURR.NO` | `FsGiAppBankAccountCon_CurrNo` | String |  |  |
| 102 | `FS.GI.APP.BANK.ACCOUNT.CON.INPUTTER` | `FsGiAppBankAccountCon_Inputter` |  |  |  |
| 103 | `FS.GI.APP.BANK.ACCOUNT.CON.DATE.TIME` | `FsGiAppBankAccountCon_DateTime` |  |  |  |
| 104 | `FS.GI.APP.BANK.ACCOUNT.CON.AUTHORISER` | `FsGiAppBankAccountCon_Authoriser` | String |  |  |
| 105 | `FS.GI.APP.BANK.ACCOUNT.CON.CO.CODE` | `FsGiAppBankAccountCon_CoCode` | String |  |  |
| 106 | `FS.GI.APP.BANK.ACCOUNT.CON.DEPT.CODE` | `FsGiAppBankAccountCon_DeptCode` | String |  |  |
| 107 | `FS.GI.APP.BANK.ACCOUNT.CON.AUDITOR.CODE` | `FsGiAppBankAccountCon_AuditorCode` | String |  |  |
| 108 | `FS.GI.APP.BANK.ACCOUNT.CON.AUDIT.DATE.TIME` | `FsGiAppBankAccountCon_AuditDateTime` | String |  |  |
