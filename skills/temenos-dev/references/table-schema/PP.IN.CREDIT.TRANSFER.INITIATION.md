# PP.IN.CREDIT.TRANSFER.INITIATION — Table Schema

> Source: `INSERTS/I_F.PP.IN.CREDIT.TRANSFER.INITIATION` in `PP_InwardCreditTransferInitiationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPICI.FileRefIncoming` | `PpInCreditTransferInitiation_Filerefincoming` | TField |  | Unique reference of the file to which the transaction belongs to |
| 2 | `PPICI.BulkRefIncoming` | `PpInCreditTransferInitiation_Bulkrefincoming` | TField |  | Unique reference of the bulk to which the transaction belongs to |
| 3 | `PPICI.MessageRefIncoming` | `PpInCreditTransferInitiation_Messagerefincoming` | TField |  | Unique reference of the transaction, as received. |
| 4 | `PPICI.TPSTrxCompanyID` | `PpInCreditTransferInitiation_Tpstrxcompanyid` | TField |  | TPS Company ID that needs to process the payment. Example: BNK, GB1 |
| 5 | `PPICI.TPSTrxOriginatingChannel` | `PpInCreditTransferInitiation_Tpstrxoriginatingchannel` | TField |  | Channel on which the payment came. |
| 6 | `PPICI.TPSTrxOriginatingSource` | `PpInCreditTransferInitiation_Tpstrxoriginatingsource` | TField |  | Source that initiated the payment. |
| 7 | `PPICI.TPSTrxFileMessageFormat` | `PpInCreditTransferInitiation_Tpstrxfilemessageformat` | TField |  | Format of the message that came in with the payment. |
| 8 | `PPICI.TPSTrxIncomingMessageTp` | `PpInCreditTransferInitiation_Tpstrxincomingmessagetp` | TField |  | Extracted from the PP.INPUT.FILE from FileMessageFormat or BulkFormat or provided directly in the payment instruction. Example: will contain the value �pain.001" or "pacs.008". |
| 9 | `PPICI.TPSTrxBatchInd` | `PpInCreditTransferInitiation_Tpstrxbatchind` | TField |  | Indicates if the transaction is part of a batch - as a parent transaction (debtor) or a child transaction (creditor). Values: - "P" - parent - "C" - child |
| 10 | `PPICI.TPSTrxTransferTp` | `PpInCreditTransferInitiation_Tpstrxtransfertp` | TField |  | Indicates if the transaction is a bank transfer or a client transfer. Values: - "B" - bank - "C" - client |
| 11 | `PPICI.PmtInfPmtMethod` | `PpInCreditTransferInitiation_Pmtinfpmtmethod` | TField |  | Specifies the means of payment that will be used to move the amount of money. Example of values: CHK (Cheque), TRF (Credit Transfer), TRA (Transfer Advice). For now, only limited to accept TRF. This will be used to determine the clearing transaction type. |
| 12 | `PPICI.PmtInfBatchBooking` | `PpInCreditTransferInitiation_Pmtinfbatchbooking` | TField |  | Identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested. Values: Y/N. |
| 13 | `PPICI.PmtInfPmtTpInfInstrPri` | `PpInCreditTransferInitiation_Pmtinfpmttpinfinstrpri` | TField |  | Indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction. |
| 14 | `PPICI.PmtInfPmtTpInfSrvLvCd` | `PpInCreditTransferInitiation_Pmtinfpmttpinfsrvlvcd` | TField |  | Indicates the agreement or rules under which the transaction should be processed. Example of values: "SEPA", "POPS", etc. This will be used to determine clearing nature code. |
| 15 | `PPICI.PmtInfPmtTpInfCatPurpCd` | `PpInCreditTransferInitiation_Pmtinfpmttpinfcatpurpcd` | TField |  | Indicates the high level purpose of the instruction, as it was put at bulk level (in pain.001). This field is a code as published in an external list. |
| 16 | `PPICI.PmtInfPmtTpInfCatPurpProp` | `PpInCreditTransferInitiation_Pmtinfpmttpinfcatpurpprop` | TField |  | Indicates the high level purpose of the instruction, but in a proprietary form. |
| 17 | `PPICI.PmtInfReqExecDt` | `PpInCreditTransferInitiation_Pmtinfreqexecdt` | TField |  | Date at which the initiating party requests the clearing agent to process the payment. |
| 18 | `PPICI.PmtInfDbtNm` | `PpInCreditTransferInitiation_Pmtinfdbtnm` | TField |  | Debtor is the party that owes an amount of money to the (ultimate) creditor. This field holds the debtor name. |
| 19 | `PPICI.PmtInfDbtPostAddTp` | `PpInCreditTransferInitiation_Pmtinfdbtpostaddtp` | TField |  | Debtor address type. Example of values: ADDR (Postal), PBOX (POBox), HOME (Residential), BIZZ (Business), MLTO (MailTo), DLVY (DeliveryTo) |
| 20 | `PPICI.PmtInfDbtPostAddCtry` | `PpInCreditTransferInitiation_Pmtinfdbtpostaddctry` | TField |  | Debtor country address. ISO standard. |
| 21 | `PPICI.PmtInfDbtPostAddLine1` | `PpInCreditTransferInitiation_Pmtinfdbtpostaddline1` | TField |  | Information that locates and identifies a specific address, as defined by postal services, pre-sented in free format text. |
| 22 | `PPICI.PmtInfDbtPostAddLine2` | `PpInCreditTransferInitiation_Pmtinfdbtpostaddline2` | TField |  | Information that locates and identifies a specific address, as defined by postal services, pre-sented in free format text. |
| 23 | `PPICI.PmtInfDbtIdOrgIdAnyBIC` | `PpInCreditTransferInitiation_Pmtinfdbtidorgidanybic` | TField |  | Unique identification of the debtor organisation, in BIC format. ISO Standard. |
| 24 | `PPICI.PmtInfDbtIdOrgIdOthId` | `PpInCreditTransferInitiation_Pmtinfdbtidorgidothid` |  |  |  |
| 25 | `PPICI.PmtInfDbtIdOrgIdSchNmCd` | `PpInCreditTransferInitiation_Pmtinfdbtidorgidschnmcd` |  |  |  |
| 26 | `PPICI.PmtInfDbtIdOrgIdSchNmProp` | `PpInCreditTransferInitiation_Pmtinfdbtidorgidschnmprop` |  |  |  |
| 27 | `PPICI.PmtInfDbtIdOrgIdOthIssuer` | `PpInCreditTransferInitiation_Pmtinfdbtidorgidothissuer` |  |  |  |
| 28 | `PPICI.PmtInfDbtIdPrvIdDtPlOfBrBrDt` | `PpInCreditTransferInitiation_Pmtinfdbtidprviddtplofbrbrdt` | TField |  | Debtor birth date. |
| 29 | `PPICI.PmtInfDbtIdPrvIdDtPlBrPvOfBr` | `PpInCreditTransferInitiation_Pmtinfdbtidprviddtplbrpvofbr` | TField |  | Debtor province of birth. |
| 30 | `PPICI.PmtInfDbtIdPrvIdDtPlBrCityBr` | `PpInCreditTransferInitiation_Pmtinfdbtidprviddtplbrcitybr` | TField |  | Debtor city of birth. |
| 31 | `PPICI.PmtInfDbtIdPrvIdDtPlBrCtryBr` | `PpInCreditTransferInitiation_Pmtinfdbtidprviddtplbrctrybr` | TField |  | Debtor country of birth. ISO standard. |
| 32 | `PPICI.PmtInfDbtIdPrvIdOthId` | `PpInCreditTransferInitiation_Pmtinfdbtidprvidothid` |  |  |  |
| 33 | `PPICI.PmtInfDbtIdPrvIdOthSchNmCd` | `PpInCreditTransferInitiation_Pmtinfdbtidprvidothschnmcd` |  |  |  |
| 34 | `PPICI.PmtInfDbtIdPrvIdOtSchNmPro` | `PpInCreditTransferInitiation_Pmtinfdbtidprvidotschnmpro` |  |  |  |
| 35 | `PPICI.PmtInfDbtIdPrvIdOthIssur` | `PpInCreditTransferInitiation_Pmtinfdbtidprvidothissur` |  |  |  |
| 36 | `PPICI.PmtInfDbtAccIdIBAN` | `PpInCreditTransferInitiation_Pmtinfdbtaccidiban` | TField |  | Specifies the unique identification of the debtor account as assigned by the account servicer. Unambiguous identification of the account of the debtor to which a debit entry will be made as a result of the transaction. ISO Standard. |
| 37 | `PPICI.PmtInfDbtAccIdOthId` | `PpInCreditTransferInitiation_Pmtinfdbtaccidothid` | TField |  | Unique identification of the debtor account in another format. |
| 38 | `PPICI.PmtInfDbtAccCcy` | `PpInCreditTransferInitiation_Pmtinfdbtaccccy` | TField |  | Currency of the debtor account. |
| 39 | `PPICI.PmtInfDbtAgFinIdBICFI` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidbicfi` | TField |  | Debtor Agent is the financial institution servicing an account for the debtor. This is the debtor agent expressed in BIC. |
| 40 | `PPICI.PmtInfDbtAgFinIdCgSysMemIdCd` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidcgsysmemidcd` | TField |  | Information used to identify the debtor agent as a member within a clearing system. This is the identification of a clearing system, in a coded form as published in an external list. |
| 41 | `PPICI.PmtInfDbtAgFinCgSysMemIdProp` | `PpInCreditTransferInitiation_Pmtinfdbtagfincgsysmemidprop` | TField |  | Identification code for a clearing system, that has not yet been identified in the list of clearing systems. |
| 42 | `PPICI.PmtInfDbtAgFinIdCgSysMemId` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidcgsysmemid` | TField |  | Identification of a member of a clearing system. Example: National ID can be set here |
| 43 | `PPICI.PmtInfDbtAgFinIdNm` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidnm` | TField |  | Name by which the debtor agent is known and which is usually used to identify that agent. |
| 44 | `PPICI.PmtInfDbtAgFinIdPostAddTp` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidpostaddtp` | TField |  | Debtor agent address type. Example of values: ADDR (Postal), PBOX (POBox), HOME (Residential), BIZZ (Business), MLTO (MailTo), DLVY (DeliveryTo). |
| 45 | `PPICI.PmtInfDbtAgFinIdPostAddLine1` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidpostaddline1` | TField |  | Adress of the debtor agent, in free format. |
| 46 | `PPICI.PmtInfDbtAgFinIdOthId` | `PpInCreditTransferInitiation_Pmtinfdbtagfinidothid` | TField |  | Other identification of the debtor agent. |
| 47 | `PPICI.TrxPmtIdInstrId` | `PpInCreditTransferInitiation_Trxpmtidinstrid` | TField |  | Unique identification as assigned by an instructing party for an instructed party to unambiguously identify the instruction. The instruction identification is a point to point reference that can be used between the instructing party and the instructed party to refer to the individual instruction. It can be included in several messages related to the instruction. |
| 48 | `PPICI.TrxPmtIdEndToEndId` | `PpInCreditTransferInitiation_Trxpmtidendtoendid` | TField |  | Unique identification assigned by the initiating party to unumbiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. The end-to-end identification can be used for reconciliation or to link tasks relating to the transaction. It can be included in several messages related to the transaction. |
| 49 | `PPICI.TPSTrxSndrToRcvrInfText` | `PpInCreditTransferInitiation_Tpstrxsndrtorcvrinftext` |  |  |  |
| 50 | `PPICI.TPSTrxBankInstrInfText` | `PpInCreditTransferInitiation_Tpstrxbankinstrinftext` |  |  |  |
| 51 | `PPICI.TPSTrxDbValueDt` | `PpInCreditTransferInitiation_Tpstrxdbvaluedt` | TField |  | If present, imposed for TPS. Not present in pain.001 files. |
| 52 | `PPICI.TPSTrxCrValueDt` | `PpInCreditTransferInitiation_Tpstrxcrvaluedt` | TField |  | If present, imposed for TPS. Not present in pain.001 files. |
| 53 | `PPICI.TrxAm` | `PpInCreditTransferInitiation_Trxam` | TField |  | Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. |
| 54 | `PPICI.TrxAmCcy` | `PpInCreditTransferInitiation_Trxamccy` | TField |  | Currency of the transaction amount. |
| 55 | `PPICI.TrxEqAm` | `PpInCreditTransferInitiation_Trxeqam` | TField |  | Amount of money to be moved between debtor and creditor, before deduction of charges, expressed in the currency of the debtor's account, and to be moved in a different currency. The first agent will convert the equivalent amount into the amount to be moved. |
| 56 | `PPICI.TrxEqAmCcy` | `PpInCreditTransferInitiation_Trxeqamccy` | TField |  | Currency of the equivalent amount. |
| 57 | `PPICI.TrxEqAmCcyOfTransfer` | `PpInCreditTransferInitiation_Trxeqamccyoftransfer` | TField |  | Specifies the currency of the to be transferred amount, which is different from the currency of the debtor's account. |
| 58 | `PPICI.TrxFxRateInfUnitCcy` | `PpInCreditTransferInitiation_Trxfxrateinfunitccy` | TField |  | Provides details on the currency exchange rate and contract. This is the currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP. |
| 59 | `PPICI.TrxFxRateInfFxRate` | `PpInCreditTransferInitiation_Trxfxrateinffxrate` | TField |  | The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. 11 digits, out of which 10 are fraction digits. Example: 0.789 |
| 60 | `PPICI.TrxFxRateInfRateTp` | `PpInCreditTransferInitiation_Trxfxrateinfratetp` | TField |  | Specifies the type used to complete the currency exchange. Example of values: SPOT, SALE, AGRD |
| 61 | `PPICI.TrxFxRateInfContractId` | `PpInCreditTransferInitiation_Trxfxrateinfcontractid` | TField |  | Unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent. |
| 62 | `PPICI.TPSTrxFxRateInfTreasuryRate` | `PpInCreditTransferInitiation_Tpstrxfxrateinftreasuryrate` | TField |  | Exchange rate is imposed by treasury. Not present in pain.001 files. |
| 63 | `PPICI.TPSTrxFxRateInfRateSpread` | `PpInCreditTransferInitiation_Tpstrxfxrateinfratespread` | TField |  | Spread rate applied to the FX. Not present in pain.001 files. |
| 64 | `PPICI.TrxChargeBearer` | `PpInCreditTransferInitiation_Trxchargebearer` | TField |  | Specifies which party/parties will bear the charges associated with the processing of the payment transaction. Example of values, DEBT (borne by debtor), CRED (borne by creditor), SHAR (shared), SLEV (following service level agreement). |
| 65 | `PPICI.TPSTrxChargeWaiver` | `PpInCreditTransferInitiation_Tpstrxchargewaiver` | TField |  | Charges to be skipped. Not present in pain.001 files. |
| 66 | `PPICI.TrxUltDbtNm` | `PpInCreditTransferInitiation_Trxultdbtnm` | TField |  | Ultimate Debtor is the ultimate party that owes an amount of money to the (ultimate) creditor. This holds the ultimate debtor name. |
| 67 | `PPICI.TrxUltDbtIdOrgIdAnyBIC` | `PpInCreditTransferInitiation_Trxultdbtidorgidanybic` | TField |  | Ultimate Debtor identified by a BIC. ISO Standard. |
| 68 | `PPICI.TrxUltDbtIdOrgIdOthId` | `PpInCreditTransferInitiation_Trxultdbtidorgidothid` |  |  |  |
| 69 | `PPICI.TrxUltDbtIdOrgIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxultdbtidorgidothschnmcd` |  |  |  |
| 70 | `PPICI.TrxUltDbtIdOrgIdOtSchNmPro` | `PpInCreditTransferInitiation_Trxultdbtidorgidotschnmpro` |  |  |  |
| 71 | `PPICI.TrxUltDbtIdOrgIdOthIssuer` | `PpInCreditTransferInitiation_Trxultdbtidorgidothissuer` |  |  |  |
| 72 | `PPICI.TrxUltDbtIdPrvIdDtPlOfBrBrDt` | `PpInCreditTransferInitiation_Trxultdbtidprviddtplofbrbrdt` | TField |  | Ultimate debtor birth date. |
| 73 | `PPICI.TrxUltDbtIdPrvIdDtPlBrPvOfBr` | `PpInCreditTransferInitiation_Trxultdbtidprviddtplbrpvofbr` | TField |  | Ultimate debtor province of birth. |
| 74 | `PPICI.TrxUltDbtIdPrvIdDtPlBrCityBr` | `PpInCreditTransferInitiation_Trxultdbtidprviddtplbrcitybr` | TField |  | Ultimate debtor city of birth. |
| 75 | `PPICI.TrxUltDbtIdPrvIdDtPlBrCtryBr` | `PpInCreditTransferInitiation_Trxultdbtidprviddtplbrctrybr` | TField |  | Ultimate debtor country of birth. ISO standard. |
| 76 | `PPICI.TrxUltDbtIdPrvIdOthId` | `PpInCreditTransferInitiation_Trxultdbtidprvidothid` |  |  |  |
| 77 | `PPICI.TrxUltDbtIdPrvIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxultdbtidprvidothschnmcd` |  |  |  |
| 78 | `PPICI.TrxUltDbtIdPrvIdOtSchNmPro` | `PpInCreditTransferInitiation_Trxultdbtidprvidotschnmpro` |  |  |  |
| 79 | `PPICI.TrxUltDbtIdPrvIdOthIssuer` | `PpInCreditTransferInitiation_Trxultdbtidprvidothissuer` |  |  |  |
| 80 | `PPICI.TrxItmAg1FinIdBICFI` | `PpInCreditTransferInitiation_Trxitmag1finidbicfi` | TField |  | This is the agent between the debtor's agent and the creditor's agent. This field holds the indetification of the intermediary agent, in BIC format. In TPS: Intermediary Agent will be mapped to POR_PartyCredit (�INTINS"). |
| 81 | `PPICI.TrxItmAg1FinIdCgSysMemIdCd` | `PpInCreditTransferInitiation_Trxitmag1finidcgsysmemidcd` | TField |  | Information used to identify the intermediary agent as a member within a clearing system. This is the identification of a clearing system, in a coded form as published in an external list. |
| 82 | `PPICI.TrxItmAg1FinIdCgSysMemIdProp` | `PpInCreditTransferInitiation_Trxitmag1finidcgsysmemidprop` | TField |  | Identification code for a clearing system, that has not yet been identified in the list of clearing systems. |
| 83 | `PPICI.TrxItmAg1FinIdCgSysMemId` | `PpInCreditTransferInitiation_Trxitmag1finidcgsysmemid` | TField |  | Identification of a member of a clearing system. Example: National ID can be set here |
| 84 | `PPICI.TrxItmAg1FinIdNm` | `PpInCreditTransferInitiation_Trxitmag1finidnm` | TField |  | Name by which the intermediary agent is known and which is usually used to identify that agent. |
| 85 | `PPICI.TrxItmAg1FinIdPostAddTp` | `PpInCreditTransferInitiation_Trxitmag1finidpostaddtp` | TField |  | Intermediary agent address type. Example of values: ADDR (Postal), PBOX (POBox), HOME (Residential), BIZZ (Business), MLTO (MailTo), DLVY (DeliveryTo). |
| 86 | `PPICI.TrxItmAg1FinIdPostAddLine1` | `PpInCreditTransferInitiation_Trxitmag1finidpostaddline1` | TField |  | Adress of the intermediary agent, in free format. |
| 87 | `PPICI.TrxItmAg1FinIdOthId` | `PpInCreditTransferInitiation_Trxitmag1finidothid` | TField |  | Other identification of the intermediary agent. |
| 88 | `PPICI.TrxItmAg1AccIdIBAN` | `PpInCreditTransferInitiation_Trxitmag1accidiban` | TField |  | Account of the intermediary agent as IBAN. ISO standard. |
| 89 | `PPICI.TrxItmAg1AccIdOthId` | `PpInCreditTransferInitiation_Trxitmag1accidothid` | TField |  | Account of the intermediary agent in another format. |
| 90 | `PPICI.TrxCrdAgFinIdBICFI` | `PpInCreditTransferInitiation_Trxcrdagfinidbicfi` | TField |  | Creditor Agent is the financial institution servicing an account for the creditor. This is the BIC identification of the creditor agent. In TPS: Creditor Agent will be mapped to POR_PartyCredit (�ACWINS"). |
| 91 | `PPICI.TrxCrdAgFinIdCgSysMemIdCd` | `PpInCreditTransferInitiation_Trxcrdagfinidcgsysmemidcd` | TField |  | Information used to identify the creditor agent as a member within a clearing system. This is the identification of a clearing system, in a coded form as published in an external list. |
| 92 | `PPICI.TrxCrdAgFinIdCgSysMemIdProp` | `PpInCreditTransferInitiation_Trxcrdagfinidcgsysmemidprop` | TField |  | Identification code for a clearing system, that has not yet been identified in the list of clearing systems. |
| 93 | `PPICI.TrxCrdAgFinIdCgSysMemId` | `PpInCreditTransferInitiation_Trxcrdagfinidcgsysmemid` | TField |  | Identification of a member of a clearing system. Example: National ID can be set here |
| 94 | `PPICI.TrxCrdAgFinIdNm` | `PpInCreditTransferInitiation_Trxcrdagfinidnm` | TField |  | Name by which the creditor agent is known and which is usually used to identify that agent. |
| 95 | `PPICI.TrxCrdAgFinIdPostAddTp` | `PpInCreditTransferInitiation_Trxcrdagfinidpostaddtp` | TField |  | Creditor agent address type. Example of values: ADDR (Postal), PBOX (POBox), HOME (Residential), BIZZ (Business), MLTO (MailTo), DLVY (DeliveryTo). |
| 96 | `PPICI.TrxCrdAgFinIdPostAddLine1` | `PpInCreditTransferInitiation_Trxcrdagfinidpostaddline1` | TField |  | Adress of the creditor agent, in free format. |
| 97 | `PPICI.TrxCrdAgFinIdOthId` | `PpInCreditTransferInitiation_Trxcrdagfinidothid` | TField |  | Other identification of the creditor agent. |
| 98 | `PPICI.TrxCrdAgAccIdIBAN` | `PpInCreditTransferInitiation_Trxcrdagaccidiban` | TField |  | Account of the creditor agent as IBAN. ISO standard. |
| 99 | `PPICI.TrxCrdAgAccIdOthId` | `PpInCreditTransferInitiation_Trxcrdagaccidothid` | TField |  | Account of the creditor agent in a different format. |
| 100 | `PPICI.TrxCrdNm` | `PpInCreditTransferInitiation_Trxcrdnm` | TField |  | The creditor is the party to which an amount of money is due. This holds the creditor name. |
| 101 | `PPICI.TrxCrdPostAddTp` | `PpInCreditTransferInitiation_Trxcrdpostaddtp` | TField |  | Creditor address type. Example of values: ADDR (Postal), PBOX (POBox), HOME (Residential), BIZZ (Business), MLTO (MailTo), DLVY (DeliveryTo). |
| 102 | `PPICI.TrxCrdPostAddDep` | `PpInCreditTransferInitiation_Trxcrdpostadddep` | TField |  | Creditor address department. Identification of a division of a large organisation or building. |
| 103 | `PPICI.TrxCrdPostAddSubDep` | `PpInCreditTransferInitiation_Trxcrdpostaddsubdep` | TField |  | Creditor address sub-department. Identification of a sub-division of a large organisation or building. |
| 104 | `PPICI.TrxCrdPostAddStreetNm` | `PpInCreditTransferInitiation_Trxcrdpostaddstreetnm` | TField |  | Creditor address street name. |
| 105 | `PPICI.TrxCrdPostAddBuildingNr` | `PpInCreditTransferInitiation_Trxcrdpostaddbuildingnr` | TField |  | Creditor address building number (on a street). |
| 106 | `PPICI.TrxCrdPostAddPostCd` | `PpInCreditTransferInitiation_Trxcrdpostaddpostcd` | TField |  | Creditor address postal code. |
| 107 | `PPICI.TrxCrdPostAddTownNm` | `PpInCreditTransferInitiation_Trxcrdpostaddtownnm` | TField |  | Creditor address town name. |
| 108 | `PPICI.TrxCrdPostAddCtrySubDiv` | `PpInCreditTransferInitiation_Trxcrdpostaddctrysubdiv` | TField |  | Creditor address county / state / region. |
| 109 | `PPICI.TrxCrdPostAddCtry` | `PpInCreditTransferInitiation_Trxcrdpostaddctry` | TField |  | Creditor address country. ISO standard. |
| 110 | `PPICI.TrxCrdPostAddLine1` | `PpInCreditTransferInitiation_Trxcrdpostaddline1` | TField |  | Information that locates and identifies a specific address, as defined by postal services, pre-sented in free format text. |
| 111 | `PPICI.TrxCrdPostAddLine2` | `PpInCreditTransferInitiation_Trxcrdpostaddline2` | TField |  |  |
| 112 | `PPICI.TrxCrdPostAddLine3` | `PpInCreditTransferInitiation_Trxcrdpostaddline3` | TField |  |  |
| 113 | `PPICI.TrxCrdPostAddLine4` | `PpInCreditTransferInitiation_Trxcrdpostaddline4` | TField |  |  |
| 114 | `PPICI.TrxCrdPostAddLine5` | `PpInCreditTransferInitiation_Trxcrdpostaddline5` | TField |  |  |
| 115 | `PPICI.TrxCrdPostAddLine6` | `PpInCreditTransferInitiation_Trxcrdpostaddline6` | TField |  |  |
| 116 | `PPICI.TrxCrdPostAddLine7` | `PpInCreditTransferInitiation_Trxcrdpostaddline7` | TField |  |  |
| 117 | `PPICI.TrxCrdIdOrgIdAnyBIC` | `PpInCreditTransferInitiation_Trxcrdidorgidanybic` | TField |  | Identification of the creditor as a BIC. |
| 118 | `PPICI.TrxCrdIdOrgIdOthId` | `PpInCreditTransferInitiation_Trxcrdidorgidothid` |  |  |  |
| 119 | `PPICI.TrxCrdIdOrgIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxcrdidorgidothschnmcd` |  |  |  |
| 120 | `PPICI.TrxCrdIdOrgIdOthSchNmProp` | `PpInCreditTransferInitiation_Trxcrdidorgidothschnmprop` |  |  |  |
| 121 | `PPICI.TrxCrdIdOrgIdOthIssuer` | `PpInCreditTransferInitiation_Trxcrdidorgidothissuer` |  |  |  |
| 122 | `PPICI.TrxCrdIdPrvIdDtPlOfBrBrDt` | `PpInCreditTransferInitiation_Trxcrdidprviddtplofbrbrdt` | TField |  | Creditor birth date. |
| 123 | `PPICI.TrxCrdIdPrvIdDtPlOfBrProvOfBr` | `PpInCreditTransferInitiation_Trxcrdidprviddtplofbrprovofbr` | TField |  | Creditor province of birth. |
| 124 | `PPICI.TrxCrdIdPrvIdDtPlOfBrCityOfBr` | `PpInCreditTransferInitiation_Trxcrdidprviddtplofbrcityofbr` | TField |  | Creditor city of birth. |
| 125 | `PPICI.TrxCrdIdPrvIdDtPlOfBrCtryOfBr` | `PpInCreditTransferInitiation_Trxcrdidprviddtplofbrctryofbr` | TField |  | Creditor country of birth. ISO standard. |
| 126 | `PPICI.TrxCrdIdPrvIdOthId` | `PpInCreditTransferInitiation_Trxcrdidprvidothid` |  |  |  |
| 127 | `PPICI.TrxCrdIdPrvIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxcrdidprvidothschnmcd` |  |  |  |
| 128 | `PPICI.TrxCrdIdPrvIdOthSchNmProp` | `PpInCreditTransferInitiation_Trxcrdidprvidothschnmprop` |  |  |  |
| 129 | `PPICI.TrxCrdIdPrvIdOthIssuer` | `PpInCreditTransferInitiation_Trxcrdidprvidothissuer` |  |  |  |
| 130 | `PPICI.TrxCrdCtryOfResidence` | `PpInCreditTransferInitiation_Trxcrdctryofresidence` | TField |  | Country of the creditor (the place of a person's home or the country from which the affairs of a company are directed). ISO Standard. |
| 131 | `PPICI.TrxCrdContactDetNmPrefix` | `PpInCreditTransferInitiation_Trxcrdcontactdetnmprefix` | TField |  | Creditor contact details - name prefix. Example of values: DOCT (Doctor), MIST (Mister), MISS (Miss), MADM (Madam). |
| 132 | `PPICI.TrxCrdContactDetNm` | `PpInCreditTransferInitiation_Trxcrdcontactdetnm` | TField |  | Creditor contact details - name. |
| 133 | `PPICI.TrxCrdContactDetPhoneNr` | `PpInCreditTransferInitiation_Trxcrdcontactdetphonenr` | TField |  | Creditor contact details - phone number. |
| 134 | `PPICI.TrxCrdContactDetMobileNr` | `PpInCreditTransferInitiation_Trxcrdcontactdetmobilenr` | TField |  | Creditor contact details - mobile number. |
| 135 | `PPICI.TrxCrdContactDetFaxNr` | `PpInCreditTransferInitiation_Trxcrdcontactdetfaxnr` | TField |  | Creditor contact details - fax number. |
| 136 | `PPICI.TrxCrdContactDetEmailAdd` | `PpInCreditTransferInitiation_Trxcrdcontactdetemailadd` | TField |  | Creditor contact details - email address. |
| 137 | `PPICI.TrxCrdContactDetOth` | `PpInCreditTransferInitiation_Trxcrdcontactdetoth` | TField |  | Creditor contact details - in another free format. |
| 138 | `PPICI.TrxCrdAccIdIBAN` | `PpInCreditTransferInitiation_Trxcrdaccidiban` | TField |  | Unambiguous identification of the account of the creditor to which a credit entry will be posted as a result of the payment transaction. IBAN ISO Standard. In TPS: Creditor IBAN Account will be mapped to POR_PartyCredit (�BENFCY"). |
| 139 | `PPICI.TrxCrdAccIdOthId` | `PpInCreditTransferInitiation_Trxcrdaccidothid` | TField |  | Unique identification of an account, as assigned by the account servicer, using an identification scheme. This is the identification assigned by an institution. |
| 140 | `PPICI.TrxCrdAccIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxcrdaccidothschnmcd` | TField |  | Name of the identification scheme, in a coded form as published in an external list. |
| 141 | `PPICI.TrxCrdAccIdOthSchNmProp` | `PpInCreditTransferInitiation_Trxcrdaccidothschnmprop` | TField |  | Name of the identification scheme, in a free text form. |
| 142 | `PPICI.TrxCrdAccIdOthIssuer` | `PpInCreditTransferInitiation_Trxcrdaccidothissuer` | TField |  | Entity that assigns the identification. |
| 143 | `PPICI.TrxUltCrdNm` | `PpInCreditTransferInitiation_Trxultcrdnm` | TField |  | Ultimate creditor is the ultimate party to which an amount of money is due. This holds the ultimate creditor name. |
| 144 | `PPICI.TrxUltCrdIdOrgIdAnyBIC` | `PpInCreditTransferInitiation_Trxultcrdidorgidanybic` | TField |  | Ultimate Creditor identified by a BIC. ISO Standard. |
| 145 | `PPICI.TrxUltCrdIdOrgIdOthId` | `PpInCreditTransferInitiation_Trxultcrdidorgidothid` |  |  |  |
| 146 | `PPICI.TrxUltCrdIdOrgIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxultcrdidorgidothschnmcd` |  |  |  |
| 147 | `PPICI.TrxUltCrdIdOrgIdOtSchNmPro` | `PpInCreditTransferInitiation_Trxultcrdidorgidotschnmpro` |  |  |  |
| 148 | `PPICI.TrxUltCrdIdOrgIdOthIssuer` | `PpInCreditTransferInitiation_Trxultcrdidorgidothissuer` |  |  |  |
| 149 | `PPICI.TrxUltCrdIdPrvIdDtPlOfBrBrDt` | `PpInCreditTransferInitiation_Trxultcrdidprviddtplofbrbrdt` | TField |  | Ultimate creditor birth date. |
| 150 | `PPICI.TrxUltCrdIdPrvIdDtPlBrPvOfBr` | `PpInCreditTransferInitiation_Trxultcrdidprviddtplbrpvofbr` | TField |  | Ultimate creditor province of birth. |
| 151 | `PPICI.TrxUltCrdIdPrvIdDtPlBrCityBr` | `PpInCreditTransferInitiation_Trxultcrdidprviddtplbrcitybr` | TField |  | Ultimate creditor city of birth. |
| 152 | `PPICI.TrxUltCrdIdPrvIdDtPlBrCtryBr` | `PpInCreditTransferInitiation_Trxultcrdidprviddtplbrctrybr` | TField |  | Ultimate creditor country of birth. ISO standard. |
| 153 | `PPICI.TrxUltCrdIdPrvIdOthId` | `PpInCreditTransferInitiation_Trxultcrdidprvidothid` |  |  |  |
| 154 | `PPICI.TrxUltCrdIdPrvIdOthSchNmCd` | `PpInCreditTransferInitiation_Trxultcrdidprvidothschnmcd` |  |  |  |
| 155 | `PPICI.TrxUltCrdIdPrvIdOtSchNmPro` | `PpInCreditTransferInitiation_Trxultcrdidprvidotschnmpro` |  |  |  |
| 156 | `PPICI.TrxUltCrdIdPrvIdOthIssuer` | `PpInCreditTransferInitiation_Trxultcrdidprvidothissuer` |  |  |  |
| 157 | `PPICI.TrxPurpCd` | `PpInCreditTransferInitiation_Trxpurpcd` | TField |  | Underlying reason for the payment transaction, as published in an external purpose code list. |
| 158 | `PPICI.TrxPurpProp` | `PpInCreditTransferInitiation_Trxpurpprop` | TField |  | Purpose, in a proprietary form. |
| 159 | `PPICI.TrxRegRepDbCrRepInd` | `PpInCreditTransferInitiation_Trxregrepdbcrrepind` |  |  |  |
| 160 | `PPICI.TrxRegRepAuthorityNm` | `PpInCreditTransferInitiation_Trxregrepauthoritynm` |  |  |  |
| 161 | `PPICI.TrxRegRepAuthorityCtry` | `PpInCreditTransferInitiation_Trxregrepauthorityctry` |  |  |  |
| 162 | `PPICI.TrxRegRepDetTp` | `PpInCreditTransferInitiation_Trxregrepdettp` |  |  |  |
| 163 | `PPICI.TrxRegRepDetDt` | `PpInCreditTransferInitiation_Trxregrepdetdt` |  |  |  |
| 164 | `PPICI.TrxRegRepDetCtry` | `PpInCreditTransferInitiation_Trxregrepdetctry` |  |  |  |
| 165 | `PPICI.TrxRegRepDetCd` | `PpInCreditTransferInitiation_Trxregrepdetcd` |  |  |  |
| 166 | `PPICI.TrxRegRepDetAm` | `PpInCreditTransferInitiation_Trxregrepdetam` |  |  |  |
| 167 | `PPICI.TrxRegRepDetAmCcy` | `PpInCreditTransferInitiation_Trxregrepdetamccy` |  |  |  |
| 168 | `PPICI.TrxRegRepDetInfText` | `PpInCreditTransferInitiation_Trxregrepdetinftext` |  |  |  |
| 169 | `PPICI.TrxRemInfUnstrText` | `PpInCreditTransferInitiation_Trxreminfunstrtext` |  |  |  |
| 170 | `PPICI.RefDocInfTpCdOrPropCd` | `PpInCreditTransferInitiation_Refdocinftpcdorpropcd` |  |  |  |
| 171 | `PPICI.RefDocInfTpCdOrPropProp` | `PpInCreditTransferInitiation_Refdocinftpcdorpropprop` |  |  |  |
| 172 | `PPICI.RefDocInfTpIssuer` | `PpInCreditTransferInitiation_Refdocinftpissuer` |  |  |  |
| 173 | `PPICI.RefDocInfNr` | `PpInCreditTransferInitiation_Refdocinfnr` |  |  |  |
| 174 | `PPICI.RefDocInfRelatedDt` | `PpInCreditTransferInitiation_Refdocinfrelateddt` |  |  |  |
| 175 | `PPICI.RefDocAmDuePayableAm` | `PpInCreditTransferInitiation_Refdocamduepayableam` |  |  |  |
| 176 | `PPICI.RefDocAmDuePayableAmCcy` | `PpInCreditTransferInitiation_Refdocamduepayableamccy` |  |  |  |
| 177 | `PPICI.RefDocAmDiscApplAmTpCd` | `PpInCreditTransferInitiation_Refdocamdiscapplamtpcd` |  |  |  |
| 178 | `PPICI.RefDocAmDiscApplAmTpProp` | `PpInCreditTransferInitiation_Refdocamdiscapplamtpprop` |  |  |  |
| 179 | `PPICI.RefDocAmDiscApplAmAm` | `PpInCreditTransferInitiation_Refdocamdiscapplamam` |  |  |  |
| 180 | `PPICI.RefDocAmDiscApplAmAmCcy` | `PpInCreditTransferInitiation_Refdocamdiscapplamamccy` |  |  |  |
| 181 | `PPICI.RefDocAmCrNoteAm` | `PpInCreditTransferInitiation_Refdocamcrnoteam` |  |  |  |
| 182 | `PPICI.RefDocAmCrNoteAmCcy` | `PpInCreditTransferInitiation_Refdocamcrnoteamccy` |  |  |  |
| 183 | `PPICI.RefDocAmTaxAmTpCd` | `PpInCreditTransferInitiation_Refdocamtaxamtpcd` |  |  |  |
| 184 | `PPICI.RefDocAmTaxAmTpProp` | `PpInCreditTransferInitiation_Refdocamtaxamtpprop` |  |  |  |
| 185 | `PPICI.RefDocAmTaxAmAm` | `PpInCreditTransferInitiation_Refdocamtaxamam` |  |  |  |
| 186 | `PPICI.RefDocAmTaxAmAmCcy` | `PpInCreditTransferInitiation_Refdocamtaxamamccy` |  |  |  |
| 187 | `PPICI.RefDocAmAdjAmRsnAm` | `PpInCreditTransferInitiation_Refdocamadjamrsnam` |  |  |  |
| 188 | `PPICI.RefDocAmAdjAmRsnAmCcy` | `PpInCreditTransferInitiation_Refdocamadjamrsnamccy` |  |  |  |
| 189 | `PPICI.RefDocAmAdjAmRsnCrDbInd` | `PpInCreditTransferInitiation_Refdocamadjamrsncrdbind` |  |  |  |
| 190 | `PPICI.RefDocAmAdjAmRsnRsn` | `PpInCreditTransferInitiation_Refdocamadjamrsnrsn` |  |  |  |
| 191 | `PPICI.RefDocAmAdjAmRsnAdInf` | `PpInCreditTransferInitiation_Refdocamadjamrsnadinf` |  |  |  |
| 192 | `PPICI.RefDocAmRemittedAm` | `PpInCreditTransferInitiation_Refdocamremittedam` |  |  |  |
| 193 | `PPICI.RefDocAmRemittedAmCcy` | `PpInCreditTransferInitiation_Refdocamremittedamccy` |  |  |  |
| 194 | `PPICI.CrdRefInfTpCdOrPropCd` | `PpInCreditTransferInitiation_Crdrefinftpcdorpropcd` |  |  |  |
| 195 | `PPICI.CrdRefInfTpCdOrPropProp` | `PpInCreditTransferInitiation_Crdrefinftpcdorpropprop` |  |  |  |
| 196 | `PPICI.CrdRefInfTpIssuer` | `PpInCreditTransferInitiation_Crdrefinftpissuer` |  |  |  |
| 197 | `PPICI.CrdRefInfRef` | `PpInCreditTransferInitiation_Crdrefinfref` |  |  |  |
| 198 | `PPICI.InvrNm` | `PpInCreditTransferInitiation_Invrnm` |  |  |  |
| 199 | `PPICI.InvrPostAddTp` | `PpInCreditTransferInitiation_Invrpostaddtp` |  |  |  |
| 200 | `PPICI.InvrPostAddDep` | `PpInCreditTransferInitiation_Invrpostadddep` |  |  |  |
| 201 | `PPICI.InvrPostAddSubDep` | `PpInCreditTransferInitiation_Invrpostaddsubdep` |  |  |  |
| 202 | `PPICI.InvrPostAddStreetNm` | `PpInCreditTransferInitiation_Invrpostaddstreetnm` |  |  |  |
| 203 | `PPICI.InvrPostAddBuildingNr` | `PpInCreditTransferInitiation_Invrpostaddbuildingnr` |  |  |  |
| 204 | `PPICI.InvrPostAddPostCd` | `PpInCreditTransferInitiation_Invrpostaddpostcd` |  |  |  |
| 205 | `PPICI.InvrPostAddTownNm` | `PpInCreditTransferInitiation_Invrpostaddtownnm` |  |  |  |
| 206 | `PPICI.InvrPostAddCtrySubDiv` | `PpInCreditTransferInitiation_Invrpostaddctrysubdiv` |  |  |  |
| 207 | `PPICI.InvrPostAddCtry` | `PpInCreditTransferInitiation_Invrpostaddctry` |  |  |  |
| 208 | `PPICI.InvrPostAddLine1` | `PpInCreditTransferInitiation_Invrpostaddline1` |  |  |  |
| 209 | `PPICI.InvrPostAddLine2` | `PpInCreditTransferInitiation_Invrpostaddline2` |  |  |  |
| 210 | `PPICI.InvrPostAddLine3` | `PpInCreditTransferInitiation_Invrpostaddline3` |  |  |  |
| 211 | `PPICI.InvrPostAddLine4` | `PpInCreditTransferInitiation_Invrpostaddline4` |  |  |  |
| 212 | `PPICI.InvrPostAddLine5` | `PpInCreditTransferInitiation_Invrpostaddline5` |  |  |  |
| 213 | `PPICI.InvrPostAddLine6` | `PpInCreditTransferInitiation_Invrpostaddline6` |  |  |  |
| 214 | `PPICI.InvrPostAddLine7` | `PpInCreditTransferInitiation_Invrpostaddline7` |  |  |  |
| 215 | `PPICI.InvrIdOrgIdAnyBIC` | `PpInCreditTransferInitiation_Invridorgidanybic` |  |  |  |
| 216 | `PPICI.InvrIdOrgIdOthId` | `PpInCreditTransferInitiation_Invridorgidothid` |  |  |  |
| 217 | `PPICI.InvrIdOrgIdOthSchNmCd` | `PpInCreditTransferInitiation_Invridorgidothschnmcd` |  |  |  |
| 218 | `PPICI.InvrIdOrgIdOthSchNmProp` | `PpInCreditTransferInitiation_Invridorgidothschnmprop` |  |  |  |
| 219 | `PPICI.InvrIdOrgIdOthIssuer` | `PpInCreditTransferInitiation_Invridorgidothissuer` |  |  |  |
| 220 | `PPICI.InvrIdPrvIdDtPlOfBrBrDt` | `PpInCreditTransferInitiation_Invridprviddtplofbrbrdt` |  |  |  |
| 221 | `PPICI.InvrIdPrvIdDtPlOfBrProvBr` | `PpInCreditTransferInitiation_Invridprviddtplofbrprovbr` |  |  |  |
| 222 | `PPICI.InvrIdPrvIdDtPlOfBrCityBr` | `PpInCreditTransferInitiation_Invridprviddtplofbrcitybr` |  |  |  |
| 223 | `PPICI.InvrIdPrvIdDtPlOfBrCtryBr` | `PpInCreditTransferInitiation_Invridprviddtplofbrctrybr` |  |  |  |
| 224 | `PPICI.InvrIdPrvIdOthId` | `PpInCreditTransferInitiation_Invridprvidothid` |  |  |  |
| 225 | `PPICI.InvrIdPrvIdOthSchNmCd` | `PpInCreditTransferInitiation_Invridprvidothschnmcd` |  |  |  |
| 226 | `PPICI.InvrIdPrvIdOthSchNmProp` | `PpInCreditTransferInitiation_Invridprvidothschnmprop` |  |  |  |
| 227 | `PPICI.InvrIdPrvIdOthIssuer` | `PpInCreditTransferInitiation_Invridprvidothissuer` |  |  |  |
| 228 | `PPICI.InvrCtryOfResidence` | `PpInCreditTransferInitiation_Invrctryofresidence` |  |  |  |
| 229 | `PPICI.InvrContactDetNmPrefix` | `PpInCreditTransferInitiation_Invrcontactdetnmprefix` |  |  |  |
| 230 | `PPICI.InvrContactDetNm` | `PpInCreditTransferInitiation_Invrcontactdetnm` |  |  |  |
| 231 | `PPICI.InvrContactDetPhoneNr` | `PpInCreditTransferInitiation_Invrcontactdetphonenr` |  |  |  |
| 232 | `PPICI.InvrContactDetMobileNr` | `PpInCreditTransferInitiation_Invrcontactdetmobilenr` |  |  |  |
| 233 | `PPICI.InvrContactDetFaxNr` | `PpInCreditTransferInitiation_Invrcontactdetfaxnr` |  |  |  |
| 234 | `PPICI.InvrContactDetEmailAdd` | `PpInCreditTransferInitiation_Invrcontactdetemailadd` |  |  |  |
| 235 | `PPICI.InvrContactDetOth` | `PpInCreditTransferInitiation_Invrcontactdetoth` |  |  |  |
| 236 | `PPICI.InveNm` | `PpInCreditTransferInitiation_Invenm` |  |  |  |
| 237 | `PPICI.InvePostAddTp` | `PpInCreditTransferInitiation_Invepostaddtp` |  |  |  |
| 238 | `PPICI.InvePostAddDep` | `PpInCreditTransferInitiation_Invepostadddep` |  |  |  |
| 239 | `PPICI.InvePostAddSubDep` | `PpInCreditTransferInitiation_Invepostaddsubdep` |  |  |  |
| 240 | `PPICI.InvePostAddStreetNm` | `PpInCreditTransferInitiation_Invepostaddstreetnm` |  |  |  |
| 241 | `PPICI.InvePostAddBuildingNr` | `PpInCreditTransferInitiation_Invepostaddbuildingnr` |  |  |  |
| 242 | `PPICI.InvePostAddPostCd` | `PpInCreditTransferInitiation_Invepostaddpostcd` |  |  |  |
| 243 | `PPICI.InvePostAddTownNm` | `PpInCreditTransferInitiation_Invepostaddtownnm` |  |  |  |
| 244 | `PPICI.InvePostAddCtrySubDiv` | `PpInCreditTransferInitiation_Invepostaddctrysubdiv` |  |  |  |
| 245 | `PPICI.InvePostAddCtry` | `PpInCreditTransferInitiation_Invepostaddctry` |  |  |  |
| 246 | `PPICI.InvePostAddLine1` | `PpInCreditTransferInitiation_Invepostaddline1` |  |  |  |
| 247 | `PPICI.InvePostAddLine2` | `PpInCreditTransferInitiation_Invepostaddline2` |  |  |  |
| 248 | `PPICI.InvePostAddLine3` | `PpInCreditTransferInitiation_Invepostaddline3` |  |  |  |
| 249 | `PPICI.InvePostAddLine4` | `PpInCreditTransferInitiation_Invepostaddline4` |  |  |  |
| 250 | `PPICI.InvePostAddLine5` | `PpInCreditTransferInitiation_Invepostaddline5` |  |  |  |
| 251 | `PPICI.InvePostAddLine6` | `PpInCreditTransferInitiation_Invepostaddline6` |  |  |  |
| 252 | `PPICI.InvePostAddLine7` | `PpInCreditTransferInitiation_Invepostaddline7` |  |  |  |
| 253 | `PPICI.InveIdOrgIdAnyBIC` | `PpInCreditTransferInitiation_Inveidorgidanybic` |  |  |  |
| 254 | `PPICI.InveIdOrgIdOthId` | `PpInCreditTransferInitiation_Inveidorgidothid` |  |  |  |
| 255 | `PPICI.InveIdOrgIdOthSchNmCd` | `PpInCreditTransferInitiation_Inveidorgidothschnmcd` |  |  |  |
| 256 | `PPICI.InveIdOrgIdOthSchNmProp` | `PpInCreditTransferInitiation_Inveidorgidothschnmprop` |  |  |  |
| 257 | `PPICI.InveIdOrgIdOthIssuer` | `PpInCreditTransferInitiation_Inveidorgidothissuer` |  |  |  |
| 258 | `PPICI.InveIdPrvIdDtPlOfBrBrDt` | `PpInCreditTransferInitiation_Inveidprviddtplofbrbrdt` |  |  |  |
| 259 | `PPICI.InveIdPrvIdDtPlOfBrProvBr` | `PpInCreditTransferInitiation_Inveidprviddtplofbrprovbr` |  |  |  |
| 260 | `PPICI.InveIdPrvIdDtPlOfBrCityBr` | `PpInCreditTransferInitiation_Inveidprviddtplofbrcitybr` |  |  |  |
| 261 | `PPICI.InveIdPrvIdDtPlOfBrCtryBr` | `PpInCreditTransferInitiation_Inveidprviddtplofbrctrybr` |  |  |  |
| 262 | `PPICI.InveIdPrvIdOthId` | `PpInCreditTransferInitiation_Inveidprvidothid` |  |  |  |
| 263 | `PPICI.InveIdPrvIdOthSchNmCd` | `PpInCreditTransferInitiation_Inveidprvidothschnmcd` |  |  |  |
| 264 | `PPICI.InveIdPrvIdOthSchNmProp` | `PpInCreditTransferInitiation_Inveidprvidothschnmprop` |  |  |  |
| 265 | `PPICI.InveIdPrvIdOthIssuer` | `PpInCreditTransferInitiation_Inveidprvidothissuer` |  |  |  |
| 266 | `PPICI.InveCtryOfResidence` | `PpInCreditTransferInitiation_Invectryofresidence` |  |  |  |
| 267 | `PPICI.InveContactDetNmPrefix` | `PpInCreditTransferInitiation_Invecontactdetnmprefix` |  |  |  |
| 268 | `PPICI.InveContactDetNm` | `PpInCreditTransferInitiation_Invecontactdetnm` |  |  |  |
| 269 | `PPICI.InveContactDetPhoneNr` | `PpInCreditTransferInitiation_Invecontactdetphonenr` |  |  |  |
| 270 | `PPICI.InveContactDetMobileNr` | `PpInCreditTransferInitiation_Invecontactdetmobilenr` |  |  |  |
| 271 | `PPICI.InveContactDetFaxNr` | `PpInCreditTransferInitiation_Invecontactdetfaxnr` |  |  |  |
| 272 | `PPICI.InveContactDetEmailAdd` | `PpInCreditTransferInitiation_Invecontactdetemailadd` |  |  |  |
| 273 | `PPICI.InveContactDetOth` | `PpInCreditTransferInitiation_Invecontactdetoth` |  |  |  |
| 274 | `PPICI.AdRemittanceInf1` | `PpInCreditTransferInitiation_Adremittanceinf1` |  |  |  |
| 275 | `PPICI.AdRemittanceInf2` | `PpInCreditTransferInitiation_Adremittanceinf2` |  |  |  |
| 276 | `PPICI.AdRemittanceInf3` | `PpInCreditTransferInitiation_Adremittanceinf3` |  |  |  |
| 277 | `PPICI.PaymentNumber` | `PpInCreditTransferInitiation_Paymentnumber` | TField |  | Counter of a transaction within a bulk. |
| 278 | `PPICI.PmtInfPmtTpInfSrvLvProp` | `PpInCreditTransferInitiation_Pmtinfpmttpinfsrvlvprop` | TField |  | Indicates the agreement under which or rules under which the transaction should be processed, in a proprietary form. |
| 279 | `PPICI.PmtInfPmtTpInfLocalInsmtCd` | `PpInCreditTransferInitiation_Pmtinfpmttpinflocalinsmtcd` | TField |  | Used to specify a local instrument, local clearing option and/or further qualify the service or service level, in a coded form. |
| 280 | `PPICI.PmtInfPmtTpInfLocalInsmtProp` | `PpInCreditTransferInitiation_Pmtinfpmttpinflocalinsmtprop` | TField |  | Used to specify a local instrument, local clearing option and/or further qualify the service or service level, in a proprietary form. |
