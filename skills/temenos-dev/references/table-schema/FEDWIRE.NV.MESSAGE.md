# FEDWIRE.NV.MESSAGE — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.NV.MESSAGE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWNV.BUSINESS.FUNCTION` | `FedwireNvMessage_BusinessFunction` | TField | Yes | Fedwire Business function code. Limited to SVC code only.Mapped to tag {3600} Mandatory input. Must be a valid entry in FEDWIRE.BUSINESS.FUNCTION. |
| 2 | `FWNV.MESSAGE.TYPE` | `FedwireNvMessage_MessageType` | TField | Yes | Fedwire message type code associated with the business function. Input allowed only when BUSINESS.FUCNTION is entered. Mandatory input. Must be a valid entry in FEDWIRE.MESSAGE.TYPE |
| 3 | `FWNV.SUBTYPE.CODE` | `FedwireNvMessage_SubtypeCode` | TField | Yes | Fedwire message subtype code associated with message type. Combination of MESSAGE.TYPE and SUB.TYPE.CODE mapped to tag {1510} Mandatory input. Must be a valid entry in FEDWIRE.MESSAGE.SUBTYPE |
| 4 | `FWNV.IMAD.NUMBER` | `FedwireNvMessage_ImadNumber` | TField |  | IMAD number generated for this non-value message. Mapped to tag {1520} Noinput field. Auto generated when record is authorized. |
| 5 | `FWNV.AMOUNT` | `FedwireNvMessage_Amount` | TField | Yes | Dollar amount of the service message.Mapped to tag {2000} Mandatory Input. |
| 6 | `FWNV.SENDER.ABA` | `FedwireNvMessage_SenderAba` | TField | No | Sender ABA routing number. Mapped to tag {3100}. Optional input. If let blank, value is picked up from FEDWIRE.PARAMETER- SENDER.DI field. |
| 7 | `FWNV.SENDER.SHORT.NAME` | `FedwireNvMessage_SenderShortName` | TField | No | Sender &apos; s Short name. Mapped to the second element in tag {3100}. Optional input. |
| 8 | `FWNV.SENDER.REF` | `FedwireNvMessage_SenderRef` | TField | No | Reference to FEDWIRE.MESSAGE.TRACKER table. Sender DI to include its reference information for the message. This will be a new ID of FEDWIRE.MESSAGE.TRACKER. Mapped to tag {3320} Optional input. |
| 9 | `FWNV.RECEIVER.ABA` | `FedwireNvMessage_ReceiverAba` | TField | Yes | Valid BC.SORT.CODE of receiver DI of the service message. Mapped to tag {3400} Mandatory input. |
| 10 | `FWNV.RECEIVER.SHORT.NAME` | `FedwireNvMessage_ReceiverShortName` | TField | No | Receiver &apos; s Short name. Mapped to the second element in tag {3400}. Optional input. |
| 11 | `FWNV.PREVIOUS.MSG.ID` | `FedwireNvMessage_PreviousMsgId` | TField | Yes | Used to identify previous message being referenced. Mapped to tag {3500}. Input mandatory when SUBTYPE.CODE is either 02 or 08. |
| 12 | `FWNV.MSG.DUP.CODE` | `FedwireNvMessage_MsgDupCode` | TField |  | Indicates the original vs. duplicate status of a message sent by the sender. Mapped to 4th element in tag {1500} Possible values: P - Resend of a previous message from the DI. The resent message must be marked as P and contain the original IMAD. R - Retrieval of an original message. &quot; &quot; - Original Message |
| 13 | `FWNV.INT.FI.ID.CODE` | `FedwireNvMessage_IntFiIdCode` | TField | No | {4000} � The institution between the receiver DI and the beneficiary FI through which transfer must pass. If present, then tags {4100} and {4200} are required. &quot; Specifies the Identifier as one of the following types: B � Swift Bank Identifier Code (BIC) C � CHIPS Participant D � DDA Account Number F � Fed routing number U � CHIPS Identifier One of the above codes must be present if INT.FI.IDENT is present. &quot; Optional input. |
| 14 | `FWNV.INT.FI.IDENT` | `FedwireNvMessage_IntFiIdent` | TField | No | Indicates the identifier data associated with the INT.FI.ID.CODE. Optional input.Must be present if INT.FI.ID.CODE is present. |
| 15 | `FWNV.INT.FI.NAME` | `FedwireNvMessage_IntFiName` | TField | No | Intermediary Financial Institution name. Optional input. |
| 16 | `FWNV.INT.FI.ADDR` | `FedwireNvMessage_IntFiAddr` |  |  |  |
| 17 | `FWNV.BEN.FI.ID.CODE` | `FedwireNvMessage_BenFiIdCode` | TField | No | {4100} � Used to identify the financial institution that is to credit or pay the beneficiary. Should only be used when the institution is not the same as RECEIVER.DI field. If this tag is present then tag {4200} is required. &quot; Specifies the Identifier as one of the following types: B � Swift Bank Identifier Code (BIC) C � CHIPS Participant D � DDA Account Number F � Fed routing number U � CHIPS Identifier Optional input. |
| 18 | `FWNV.BEN.FI.IDENT` | `FedwireNvMessage_BenFiIdent` | TField | No | Indicates the identifier data associated with the BEN.FI.ID.CODE. Optional input. Must be present if BEN.FI.ID.CODE is present. |
| 19 | `FWNV.BEN.FI.NAME` | `FedwireNvMessage_BenFiName` | TField | No | Beneficiary Financial Institution name. Optional input. |
| 20 | `FWNV.BEN.FI.ADDR` | `FedwireNvMessage_BenFiAddr` |  |  |  |
| 21 | `FWNV.BEN.ID.CODE` | `FedwireNvMessage_BenIdCode` | TField | No | {4200} � Used to identify the ultimate party to be credited or paid as a result of the funds transfer. Must be present if TAG {3600} BUSINESS.FUNCTION is CTR, CTP, DRW or DRC; otherwise optional. &quot; Specifies the Identifier as one of the following types: B � Swift Bank Identifier Code (BIC) C � CHIPS Participant D � DDA Account Number F � Fed routing number T � Swift Bank Identifier Code (BIC) or Swift Business Entity Identifier (BEI) and account number ( only permitted when {3600} is CTR or CTP) U � CHIPS Identifier 1 � Passport number 2 � Tax identification number 3 � Driver�s license number 4 � Alien registration number 5 � Corporate identification 9 � Other identification Optional input. |
| 22 | `FWNV.BEN.IDENT` | `FedwireNvMessage_BenIdent` | TField | No | Indicates the identifier data associated with the BEN.ID.CODE. Optional input. Must be present if BEN.ID.CODE is present. |
| 23 | `FWNV.BEN.NAME` | `FedwireNvMessage_BenName` | TField | No | Beneficiary name. If BEN.ID.CODE is T then BEN.NAME must be present and should contain a Swift Bank Identifier Code (BIC) or Swift Business Entity Identifier (BEI) Optional input. |
| 24 | `FWNV.BEN.ADDR` | `FedwireNvMessage_BenAddr` |  |  |  |
| 25 | `FWNV.BEN.REFERENCE` | `FedwireNvMessage_BenReference` | TField | No | {4320} � Reference for Beneficiary Provides reference information for use by the beneficiary to identify transfer. Must be present when {3600} � BUSINESS.FUNCTION is CTP and {3610} � Local instrument code is COVS; otherwise optional. |
| 26 | `FWNV.DR.AC.ID.CODE` | `FedwireNvMessage_DrAcIdCode` | TField | No | {4400} � Account debited in drawdown. Used to identify the account to be debited in response to a drawdown request. Must be present when tag {3600} BUSINESS.FUNCTION is DRB or DRC, but can also be present for DRW or SVC; otherwise not permitted. Specifies the DR.AC.IDENT as the following type: D � DDA account number. Optional input. |
| 27 | `FWNV.DR.AC.IDENT` | `FedwireNvMessage_DrAcIdent` | TField | No | Indicate the identififer data associate with DR.AC.ID.CODE. must be present. Optional input. Must be present when DR.AC.ID.CODE is present. |
| 28 | `FWNV.DR.AC.NAME` | `FedwireNvMessage_DrAcName` | TField | No | Account debited in drawdown Name. Optional input. |
| 29 | `FWNV.DR.AC.ADDR` | `FedwireNvMessage_DrAcAddr` |  |  |  |
| 30 | `FWNV.ORG.ID.CODE` | `FedwireNvMessage_OrgIdCode` | TField | No | {5000} � Originator. Used to identify the originator of the payment order in a funds transfer. Must be present when {3600} BUSINESS.FUNCTION is DRW or either CTR , or CTP (when {5010} originator option F is not present) Specifies the Identifier as one of the following types: B � Swift Bank Identifier Code (BIC) C � CHIPS Participant D � DDA Account Number F � Fed routing number T � Swift Bank Identifier Code (BIC) or Swift Business Entity Identifier (BEI) and account number ( only permitted when {3600} is CTR or CTP) U � CHIPS Identifier 1 � Passport number 2 � Tax identification number 3 � Driver�s license number 4 � Alien registration number 5 � Corporate identification 9 � Other identification Optional input. |
| 31 | `FWNV.ORG.IDENT` | `FedwireNvMessage_OrgIdent` | TField | No | Indicates the identifier data associated with the ORG.ID.CODE. Optional input. If ORG.ID.CODE is D then ORG.IDENT must be present and should contain an account number. |
| 32 | `FWNV.ORG.NAME` | `FedwireNvMessage_OrgName` | TField |  | Originator�s name. If ORG.ID.CODE is T then ORG.NAME must be present and should contain a Swift Bank Identifier Code (BIC) or Swift Business Entity Identifier (BEI) |
| 33 | `FWNV.ORG.ADDR` | `FedwireNvMessage_OrgAddr` |  |  |  |
| 34 | `FWNV.PARTY.IDENT` | `FedwireNvMessage_PartyIdent` | TField | No | {5010} � Originator option F. Used to identify the originator of the payment order in the funds transfer. The format of this maps to SWIFT field 50 Option F. Must be present when {3600} BUSINESS.FUNCTION is CTP and {5000} Originator is not present; otherwise not permitted. Must be present and use on the following format options: 1) Account option � Use a slash �/� followed by atleast one valid non-space character (eg. /#12345) 2)Unique Identifier option � Use one of the unique identifier code s below followed by a slash �/� and then followed by at least one valid non-space character (e.g., SOSE/123-45-6789) ARNU � Alien Resgistration Number. CCPT � Passport Number CUST � Customer Identification Number DRLC � Driver�s License Number EMPL � Employer Number. NIDN � National Identity Number SOSE � Social Security Number TXID � Tax Identification Number Optional input. |
| 35 | `FWNV.PARTY.NAME` | `FedwireNvMessage_PartyName` | TField | No | Party Name. Optional input. Must be present and begins with Line code 1 (Name) followed by a slash �/� and then followed by at least one non-space character (e.g., 1/SMITH JOHN) |
| 36 | `FWNV.PARTY.ADDR` | `FedwireNvMessage_PartyAddr` |  |  |  |
| 37 | `FWNV.ORG.FI.ID.CODE` | `FedwireNvMessage_OrgFiIdCode` | TField | No | {5100} � Originator FI. Used to identify the financial institution that received the payment instructions from the ORIGINATOR. Should only be used when the institution is not the SENDER DI. If present tag {5000} (or tag {5010} if {3600} is CTP) is required. &quot; Specifies the Identifier as one of the following types: B � Swift Bank Identifier Code (BIC) C � CHIPS Participant D � DDA Account Number F � Fed routing number U � CHIPS Identifier &quot; Optional input. One of the above codes must be present if ORG.FI.IDENT is present. |
| 38 | `FWNV.ORG.FI.IDENT` | `FedwireNvMessage_OrgFiIdent` | TField | No | Indicates the identifier data associated with the ORG.FI.ID.CODE. Optional input. Must be present if ORG.ID.CODE is present. |
| 39 | `FWNV.ORG.FI.NAME` | `FedwireNvMessage_OrgFiName` | TField | No | Originator financial institution name. Optional input. |
| 40 | `FWNV.ORG.FI.ADDR` | `FedwireNvMessage_OrgFiAddr` |  |  |  |
| 41 | `FWNV.INS.FI.ID.CODE` | `FedwireNvMessage_InsFiIdCode` | TField | No | {5200} � Instructing FI. The institution between ORIGINATOR FI and the SENDER DI through which the payment instruction must pass. If present, tag {5000} (or tag {5010} if tag {3600} is CTP) are required. &quot; Specifies the Identifier as one of the following types: B � Swift Bank Identifier Code (BIC) C � CHIPS Participant D � DDA Account Number F � Fed routing number U � CHIPS Identifier &quot; Optional input. One of the above codes must be present if INS.FI.IDENT is present. |
| 42 | `FWNV.INS.FI.IDENT` | `FedwireNvMessage_InsFiIdent` | TField | No | Indicates the identifier data associated with the INS.FI.ID.CODE. Optional input. Must be present if INS.ID.CODE is present. |
| 43 | `FWNV.INS.FI.NAME` | `FedwireNvMessage_InsFiName` | TField | No | Instructing financial institution name. Optional input. |
| 44 | `FWNV.INS.FI.ADDR` | `FedwireNvMessage_InsFiAddr` |  |  |  |
| 45 | `FWNV.DRW.CR.AC.NO` | `FedwireNvMessage_DrwCrAcNo` | TField |  | {5400} � Account credited to drawdown. Used to identify the account to be credited in response to a drawdown request. Drawdown credit account number. The ABA number of the account to be credited in drawdown. |
| 46 | `FWNV.ORG.BEN.INFO` | `FedwireNvMessage_OrgBenInfo` |  |  |  |
| 47 | `FWNV.RECV.FI.INFO.1` | `FedwireNvMessage_RecvFiInfo1` | TField | No | {6100} - Receiver FI information. Information intended specifically for the RECEIVER.FI Receiving FI information line 1 Optional input. |
| 48 | `FWNV.RECV.FI.INFO.ADDL` | `FedwireNvMessage_RecvFiInfoAddl` |  |  |  |
| 49 | `FWNV.DRW.DR.AC.ADV.CODE` | `FedwireNvMessage_DrwDrAcAdvCode` | TField | No | {6110} � DRW Debit account advice information. Can only be used if tag {3600} is DRB, DRC, DRW, or SVC; otherwise not permitted. &quot; Identifies the method of notification for a drawdown transaction. Must be present. The valid codes are LTR � Letter PHN � Phone TLX � Telex WRE � Wire &quot; Optional input. |
| 50 | `FWNV.DRW.DR.AC.LINE.1` | `FedwireNvMessage_DrwDrAcLine1` | TField | No | Drawdown debit account advice information line 1 Optional input. |
| 51 | `FWNV.DRW.DR.AC.ADDL.INFO` | `FedwireNvMessage_DrwDrAcAddlInfo` |  |  |  |
| 52 | `FWNV.INT.FI.LINE.1` | `FedwireNvMessage_IntFiLine1` | TField | No | {6200} � Intermediary FI information. Information intended specifically for the intermediary FI. If present tag {4000}, {4100} and {4200} are required. Intermediary FI line 1. Optional input. |
| 53 | `FWNV.INT.FI.ADDL.INFO` | `FedwireNvMessage_IntFiAddlInfo` |  |  |  |
| 54 | `FWNV.INT.FI.ADV.CODE` | `FedwireNvMessage_IntFiAdvCode` | TField | No | {6210} � Intermediary FI advice information. Information intended specifically for the intermediary FI. If present tag {4000}, {4100} and {4200} are required. &quot; Identifies the method of notification for a drawdown transaction. Must be present. The valid codes are LTR � Letter PHN � Phone TLX � Telex WRE � Wire &quot; Optional input. |
| 55 | `FWNV.INT.FI.ADV.LINE.1` | `FedwireNvMessage_IntFiAdvLine1` | TField | No | Intermediary FI Advice Line 1. Optional input. |
| 56 | `FWNV.INT.FI.ADV.ADDL` | `FedwireNvMessage_IntFiAdvAddl` |  |  |  |
| 57 | `FWNV.BEN.FI.LINE.1` | `FedwireNvMessage_BenFiLine1` | TField | No | Intermediary FI advice line 1 Optional input. |
| 58 | `FWNV.BEN.FI.ADDL.INFO` | `FedwireNvMessage_BenFiAddlInfo` |  |  |  |
| 59 | `FWNV.BEN.FI.ADV.CODE` | `FedwireNvMessage_BenFiAdvCode` | TField | No | {6310} � Beneficiary�s FI advice information. Information intended specifically for the beneficiary FI. If present tag {4000}, {4100} and {4200} are required. &quot; Identifies the method of notification for a drawdown transaction. Must be present. The valid codes are LTR � Letter PHN � Phone TLX � Telex WRE � Wire &quot; Optional input. |
| 60 | `FWNV.BEN.FI.ADV.LINE.1` | `FedwireNvMessage_BenFiAdvLine1` | TField | No | Beneficiary &apos; s FI Advice Line 1. Optional input. |
| 61 | `FWNV.BEN.FI.ADV.ADDL` | `FedwireNvMessage_BenFiAdvAddl` |  |  |  |
| 62 | `FWNV.BEN.LINE.1` | `FedwireNvMessage_BenLine1` | TField | No | {6400} � Beneficiary information. Information intended specifically for the beneficiary. If present tag {4000}, {4100} and {4200} are required. Beneficiary�s information line 1. Optional input. |
| 63 | `FWNV.BEN.ADDL.INFO` | `FedwireNvMessage_BenAddlInfo` |  |  |  |
| 64 | `FWNV.BEN.ADV.CODE` | `FedwireNvMessage_BenAdvCode` | TField | No | {6410} � Beneficiary�s advice information. Information intended specifically for the beneficiary. If present tag {4000}, {4100} and {4200} are required. &quot; Identifies the method of notification for a drawdown transaction. Must be present. The valid codes are LTR � Letter PHN � Phone TLX � Telex WRE � Wire &quot; Optional input. |
| 65 | `FWNV.BEN.ADV.LINE.1` | `FedwireNvMessage_BenAdvLine1` | TField | No | Beneficiary�s advice information line 1 Optional input. |
| 66 | `FWNV.BEN.ADV.ADDL.INFO` | `FedwireNvMessage_BenAdvAddlInfo` |  |  |  |
| 67 | `FWNV.BEN.MTD.OF.PMT` | `FedwireNvMessage_BenMtdOfPmt` | TField |  | {6420} � Beneficiary method of payment. Used to specify how the payment is to be made to the beneficiary. If present, tags {6410} and {4200} are required. Beneficiary method of payment. The only code is CHECK. |
| 68 | `FWNV.BEN.PMT.ADDL.INFO` | `FedwireNvMessage_BenPmtAddlInfo` | TField | No | Beneficiary method of payment additional information Optional input. |
| 69 | `FWNV.FI.FI.LINE.1` | `FedwireNvMessage_FiFiLine1` | TField | No | {6500} � FI to FI information. Information that could not be formatted within the {6100} through {6410} tags. FI to FI information line 1 Optional input. |
| 70 | `FWNV.FI.FI.ADDL.INFO` | `FedwireNvMessage_FiFiAddlInfo` |  |  |  |
| 71 | `FWNV.FREE.FMT.TXT` | `FedwireNvMessage_FreeFmtTxt` |  |  |  |
| 72 | `FWNV.LOCAL.INS.CODE` | `FedwireNvMessage_LocalInsCode` | TField |  |  |
| 73 | `FWNV.PROPRIETARY.CODE` | `FedwireNvMessage_ProprietaryCode` | TField |  |  |
| 74 | `FWNV.PYMT.NOTIF.IND` | `FedwireNvMessage_PymtNotifInd` | TField |  |  |
| 75 | `FWNV.CONTACT.NOTIF.ADDR` | `FedwireNvMessage_ContactNotifAddr` |  |  |  |
| 76 | `FWNV.CONTACT.NAME` | `FedwireNvMessage_ContactName` | TField |  |  |
| 77 | `FWNV.CONTACT.PHONE.NO` | `FedwireNvMessage_ContactPhoneNo` | TField |  |  |
| 78 | `FWNV.CONTACT.MOBILE.NO` | `FedwireNvMessage_ContactMobileNo` | TField |  |  |
| 79 | `FWNV.CONTACT.FAX.NO` | `FedwireNvMessage_ContactFaxNo` | TField |  |  |
| 80 | `FWNV.END.TO.END.ID` | `FedwireNvMessage_EndToEndId` | TField |  |  |
| 81 | `FWNV.DETAILS.OF.CHGS` | `FedwireNvMessage_DetailsOfChgs` | TField |  |  |
| 82 | `FWNV.SENDER.CHARGES` | `FedwireNvMessage_SenderCharges` |  |  |  |
| 83 | `FWNV.INSTRUCTED.AMT` | `FedwireNvMessage_InstructedAmt` | TField |  |  |
| 84 | `FWNV.EXCH.RATE` | `FedwireNvMessage_ExchRate` | TField |  |  |
| 85 | `FWNV.SW.33B.INST.AMT` | `FedwireNvMessage_Sw33bInstAmt` | TField |  |  |
| 86 | `FWNV.SW.50A.LINE` | `FedwireNvMessage_Sw50aLine` |  |  |  |
| 87 | `FWNV.SW.52A.LINE` | `FedwireNvMessage_Sw52aLine` |  |  |  |
| 88 | `FWNV.SW.56A.LINE` | `FedwireNvMessage_Sw56aLine` |  |  |  |
| 89 | `FWNV.SW.57A.LINE` | `FedwireNvMessage_Sw57aLine` |  |  |  |
| 90 | `FWNV.SW.59A.LINE` | `FedwireNvMessage_Sw59aLine` |  |  |  |
| 91 | `FWNV.SW.70.LINE` | `FedwireNvMessage_Sw70Line` |  |  |  |
| 92 | `FWNV.SW.72.LINE` | `FedwireNvMessage_Sw72Line` |  |  |  |
| 93 | `FWNV.ADDENDA.LENGTH` | `FedwireNvMessage_AddendaLength` | TField |  |  |
| 94 | `FWNV.ADDENDA.INFO` | `FedwireNvMessage_AddendaInfo` |  |  |  |
| 95 | `FWNV.REM.IDENT` | `FedwireNvMessage_RemIdent` | TField |  |  |
| 96 | `FWNV.REM.LOC.MTHD` | `FedwireNvMessage_RemLocMthd` | TField |  |  |
| 97 | `FWNV.REM.LOC.ADDR` | `FedwireNvMessage_RemLocAddr` |  |  |  |
| 98 | `FWNV.REM.NAME` | `FedwireNvMessage_RemName` | TField |  |  |
| 99 | `FWNV.REM.ADDR.TYPE` | `FedwireNvMessage_RemAddrType` | TField |  |  |
| 100 | `FWNV.REM.DEPT` | `FedwireNvMessage_RemDept` | TField |  |  |
| 101 | `FWNV.REM.SUB.DEPT` | `FedwireNvMessage_RemSubDept` | TField |  |  |
| 102 | `FWNV.REM.STREET` | `FedwireNvMessage_RemStreet` | TField |  |  |
| 103 | `FWNV.REM.BLDG.NO` | `FedwireNvMessage_RemBldgNo` | TField |  |  |
| 104 | `FWNV.REM.POST.CODE` | `FedwireNvMessage_RemPostCode` | TField |  |  |
| 105 | `FWNV.REM.TOWN` | `FedwireNvMessage_RemTown` | TField |  |  |
| 106 | `FWNV.REM.CNTRY.SUBDIV` | `FedwireNvMessage_RemCntrySubdiv` | TField |  |  |
| 107 | `FWNV.REM.CNTRY` | `FedwireNvMessage_RemCntry` | TField |  |  |
| 108 | `FWNV.REM.ADDR` | `FedwireNvMessage_RemAddr` |  |  |  |
| 109 | `FWNV.REM.ORG.ID.TYPE` | `FedwireNvMessage_RemOrgIdType` | TField |  |  |
| 110 | `FWNV.REM.ORG.ID.CODE` | `FedwireNvMessage_RemOrgIdCode` | TField |  |  |
| 111 | `FWNV.REM.ORG.NAME` | `FedwireNvMessage_RemOrgName` | TField |  |  |
| 112 | `FWNV.REM.ORG.ID.NO` | `FedwireNvMessage_RemOrgIdNo` | TField |  |  |
| 113 | `FWNV.REM.ORG.ID.ISSUER` | `FedwireNvMessage_RemOrgIdIssuer` | TField |  |  |
| 114 | `FWNV.REM.ORG.DATE.BIRTH` | `FedwireNvMessage_RemOrgDateBirth` | TField |  |  |
| 115 | `FWNV.REM.ORG.ADDR.TYPE` | `FedwireNvMessage_RemOrgAddrType` | TField |  |  |
| 116 | `FWNV.REM.ORG.DEPT` | `FedwireNvMessage_RemOrgDept` | TField |  |  |
| 117 | `FWNV.REM.ORG.SUB.DEPT` | `FedwireNvMessage_RemOrgSubDept` | TField |  |  |
| 118 | `FWNV.REM.ORG.STREET` | `FedwireNvMessage_RemOrgStreet` | TField |  |  |
| 119 | `FWNV.REM.ORG.BLDG.NO` | `FedwireNvMessage_RemOrgBldgNo` | TField |  |  |
| 120 | `FWNV.REM.ORG.POST.CODE` | `FedwireNvMessage_RemOrgPostCode` | TField |  |  |
| 121 | `FWNV.REM.ORG.TOWN` | `FedwireNvMessage_RemOrgTown` | TField |  |  |
| 122 | `FWNV.REM.ORG.CNTRY.SUBDIV` | `FedwireNvMessage_RemOrgCntrySubdiv` | TField |  |  |
| 123 | `FWNV.REM.ORG.CNTRY` | `FedwireNvMessage_RemOrgCntry` | TField |  |  |
| 124 | `FWNV.REM.ORG.ADDR` | `FedwireNvMessage_RemOrgAddr` |  |  |  |
| 125 | `FWNV.REM.ORG.CNTRY.RES` | `FedwireNvMessage_RemOrgCntryRes` | TField |  |  |
| 126 | `FWNV.REM.ORG.CNT.NAME` | `FedwireNvMessage_RemOrgCntName` | TField |  |  |
| 127 | `FWNV.REM.ORG.CNT.PH` | `FedwireNvMessage_RemOrgCntPh` | TField |  |  |
| 128 | `FWNV.REM.ORG.CNT.MOBILE` | `FedwireNvMessage_RemOrgCntMobile` | TField |  |  |
| 129 | `FWNV.REM.ORG.CNT.FAX` | `FedwireNvMessage_RemOrgCntFax` | TField |  |  |
| 130 | `FWNV.REM.ORG.CNT.ADDR` | `FedwireNvMessage_RemOrgCntAddr` |  |  |  |
| 131 | `FWNV.REM.ORG.CNT.OTHR` | `FedwireNvMessage_RemOrgCntOthr` | TField |  |  |
| 132 | `FWNV.REM.BEN.NAME` | `FedwireNvMessage_RemBenName` | TField |  |  |
| 133 | `FWNV.REM.BEN.ID.TYPE` | `FedwireNvMessage_RemBenIdType` | TField |  |  |
| 134 | `FWNV.REM.BEN.ID.CODE` | `FedwireNvMessage_RemBenIdCode` | TField |  |  |
| 135 | `FWNV.REM.BEN.ID.NO` | `FedwireNvMessage_RemBenIdNo` | TField |  |  |
| 136 | `FWNV.REM.BEN.ID.ISSUER` | `FedwireNvMessage_RemBenIdIssuer` | TField |  |  |
| 137 | `FWNV.REM.BEN.DATE.BIRTH` | `FedwireNvMessage_RemBenDateBirth` | TField |  |  |
| 138 | `FWNV.REM.BEN.ADDR.TYPE` | `FedwireNvMessage_RemBenAddrType` | TField |  |  |
| 139 | `FWNV.REM.BEN.DEPT` | `FedwireNvMessage_RemBenDept` | TField |  |  |
| 140 | `FWNV.REM.BEN.SUB.DEPT` | `FedwireNvMessage_RemBenSubDept` | TField |  |  |
| 141 | `FWNV.REM.BEN.STREET` | `FedwireNvMessage_RemBenStreet` | TField |  |  |
| 142 | `FWNV.REM.BEN.BLDG.NO` | `FedwireNvMessage_RemBenBldgNo` | TField |  |  |
| 143 | `FWNV.REM.BEN.POST.CODE` | `FedwireNvMessage_RemBenPostCode` | TField |  |  |
| 144 | `FWNV.REM.BEN.TOWN` | `FedwireNvMessage_RemBenTown` | TField |  |  |
| 145 | `FWNV.REM.BEN.CNTRY.SUBDIV` | `FedwireNvMessage_RemBenCntrySubdiv` | TField |  |  |
| 146 | `FWNV.REM.BEN.CNTRY` | `FedwireNvMessage_RemBenCntry` | TField |  |  |
| 147 | `FWNV.REM.BEN.ADDR` | `FedwireNvMessage_RemBenAddr` |  |  |  |
| 148 | `FWNV.REM.BEN.CNTRY.RES` | `FedwireNvMessage_RemBenCntryRes` | TField |  |  |
| 149 | `FWNV.REM.DOC.TYPE` | `FedwireNvMessage_RemDocType` | TField |  |  |
| 150 | `FWNV.REM.DOC.TYPE.CODE` | `FedwireNvMessage_RemDocTypeCode` | TField |  |  |
| 151 | `FWNV.REM.DOC.ID.NO` | `FedwireNvMessage_RemDocIdNo` | TField |  |  |
| 152 | `FWNV.REM.DOC.ISSUER` | `FedwireNvMessage_RemDocIssuer` | TField |  |  |
| 153 | `FWNV.ACTUAL.AMT.PAID` | `FedwireNvMessage_ActualAmtPaid` | TField |  |  |
| 154 | `FWNV.GROSS.AMT.REM.DOC` | `FedwireNvMessage_GrossAmtRemDoc` | TField |  |  |
| 155 | `FWNV.AMT.NEGO.DISCNT` | `FedwireNvMessage_AmtNegoDiscnt` | TField |  |  |
| 156 | `FWNV.ADJ.REASON.CODE` | `FedwireNvMessage_AdjReasonCode` | TField |  |  |
| 157 | `FWNV.ADJ.CR.DR.IND` | `FedwireNvMessage_AdjCrDrInd` | TField |  |  |
| 158 | `FWNV.ADJUSTED.AMT` | `FedwireNvMessage_AdjustedAmt` | TField |  |  |
| 159 | `FWNV.ADJ.ADDL.INFO` | `FedwireNvMessage_AdjAddlInfo` | TField |  |  |
| 160 | `FWNV.REM.DATE` | `FedwireNvMessage_RemDate` | TField |  |  |
| 161 | `FWNV.REM.2DOC.TYPE` | `FedwireNvMessage_Rem2docType` | TField |  |  |
| 162 | `FWNV.REM.2DOC.TYPE.CODE` | `FedwireNvMessage_Rem2docTypeCode` | TField |  |  |
| 163 | `FWNV.REM.2DOC.ID.NO` | `FedwireNvMessage_Rem2docIdNo` | TField |  |  |
| 164 | `FWNV.REM.2DOC.ISSUER` | `FedwireNvMessage_Rem2docIssuer` | TField |  |  |
| 165 | `FWNV.REM.FREE.TXT` | `FedwireNvMessage_RemFreeTxt` |  |  |  |
| 166 | `FWNV.MANDATE.REFERENCE` | `FedwireNvMessage_MandateReference` | TField |  | To capture the reference of matched or expired mandate found in the system. Id of USRTGS.DRAWDOWN.MANDATE will be stored. |
| 167 | `FWNV.DRW.TRANS.REFERENCE` | `FedwireNvMessage_DrwTransReference` | TField |  | The payment reference of the drawdown transfer message generated by the system will be captured in this field. |
| 168 | `FWNV.OFAC.SCREENING.STATUS` | `FedwireNvMessage_OfacScreeningStatus` | TField |  | Holds the Non-Value transactions OFAC Screening Status.Input to this field is controlled by system and through inquiry to override OFAC status. Screening Status Possible values are : ERROR, FAILED, PENDING and SUCCESS |
| 169 | `FWNV.OFAC.OVERRIDE.REASON` | `FedwireNvMessage_OfacOverrideReason` |  |  |  |
| 170 | `FWNV.OFAC.SEND.DATE` | `FedwireNvMessage_OfacSendDate` | TField |  | Holds the OFAC Screening Request Date. |
| 171 | `FWNV.RESERVED.19` | `FedwireNvMessage_Reserved19` | TField |  |  |
| 172 | `FWNV.RESERVED.18` | `FedwireNvMessage_Reserved18` | TField |  |  |
| 173 | `FWNV.RESERVED.17` | `FedwireNvMessage_Reserved17` | TField |  |  |
| 174 | `FWNV.RESERVED.16` | `FedwireNvMessage_Reserved16` | TField |  |  |
| 175 | `FWNV.RESERVED.15` | `FedwireNvMessage_Reserved15` | TField |  |  |
| 176 | `FWNV.RESERVED.14` | `FedwireNvMessage_Reserved14` | TField |  |  |
| 177 | `FWNV.RESERVED.13` | `FedwireNvMessage_Reserved13` | TField |  |  |
| 178 | `FWNV.RESERVED.12` | `FedwireNvMessage_Reserved12` | TField |  |  |
| 179 | `FWNV.RESERVED.11` | `FedwireNvMessage_Reserved11` | TField |  |  |
| 180 | `FWNV.RESERVED.10` | `FedwireNvMessage_Reserved10` | TField |  |  |
| 181 | `FWNV.RESERVED.9` | `FedwireNvMessage_Reserved9` | TField |  |  |
| 182 | `FWNV.RESERVED.8` | `FedwireNvMessage_Reserved8` | TField |  |  |
| 183 | `FWNV.RESERVED.7` | `FedwireNvMessage_Reserved7` | TField |  |  |
| 184 | `FWNV.RESERVED.6` | `FedwireNvMessage_Reserved6` | TField |  |  |
| 185 | `FWNV.RESERVED.5` | `FedwireNvMessage_Reserved5` | TField |  |  |
| 186 | `FWNV.RESERVED.4` | `FedwireNvMessage_Reserved4` | TField |  |  |
| 187 | `FWNV.RESERVED.3` | `FedwireNvMessage_Reserved3` | TField |  |  |
| 188 | `FWNV.RESERVED.2` | `FedwireNvMessage_Reserved2` | TField |  |  |
| 189 | `FWNV.RESERVED.1` | `FedwireNvMessage_Reserved1` | TField |  |  |
| 190 | `FWNV.LOCAL.REF` | `FedwireNvMessage_LocalRef` |  |  |  |
| 191 | `FWNV.OVERRIDE` | `FedwireNvMessage_Override` |  |  |  |
| 192 | `FWNV.RECORD.STATUS` | `FedwireNvMessage_RecordStatus` | String |  |  |
| 193 | `FWNV.CURR.NO` | `FedwireNvMessage_CurrNo` | String |  |  |
| 194 | `FWNV.INPUTTER` | `FedwireNvMessage_Inputter` |  |  |  |
| 195 | `FWNV.DATE.TIME` | `FedwireNvMessage_DateTime` |  |  |  |
| 196 | `FWNV.AUTHORISER` | `FedwireNvMessage_Authoriser` | String |  |  |
| 197 | `FWNV.CO.CODE` | `FedwireNvMessage_CoCode` | String |  |  |
| 198 | `FWNV.DEPT.CODE` | `FedwireNvMessage_DeptCode` | String |  |  |
| 199 | `FWNV.AUDITOR.CODE` | `FedwireNvMessage_AuditorCode` | String |  |  |
| 200 | `FWNV.AUDIT.DATE.TIME` | `FedwireNvMessage_AuditDateTime` | String |  |  |
