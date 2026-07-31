# POR.SUPPLEMENTARY.INFO — Table Schema

> Source: `INSERTS/I_F.POR.SUPPLEMENTARY.INFO` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PORID.MAIN.OR.CHARGE.ACCOUNT.TYPE` | `PorSupplementaryInfo_MainOrChargeAccountType` |  |  |  |
| 2 | `PORID.ACCOUNT.COMPANY.ID` | `PorSupplementaryInfo_AccountCompanyId` |  |  |  |
| 3 | `PORID.ACCOUNT.NUMBER` | `PorSupplementaryInfo_AccountNumber` |  |  |  |
| 4 | `PORID.ACCOUNT.CURRENCY` | `PorSupplementaryInfo_AccountCurrency` |  |  |  |
| 5 | `PORID.ACCOUNT.TYPE` | `PorSupplementaryInfo_AccountType` |  |  |  |
| 6 | `PORID.ACCOUNT.STATUS` | `PorSupplementaryInfo_AccountStatus` |  |  |  |
| 7 | `PORID.DBT.POST.RESTRICTION.CODE` | `PorSupplementaryInfo_DbtPostRestrictionCode` |  |  |  |
| 8 | `PORID.DBT.POST.RESTRICTION.DESC` | `PorSupplementaryInfo_DbtPostRestrictionDesc` |  |  |  |
| 9 | `PORID.CDT.POST.RESTRICTION.CODE` | `PorSupplementaryInfo_CdtPostRestrictionCode` |  |  |  |
| 10 | `PORID.CDT.POST.RESTRICTION.DESC` | `PorSupplementaryInfo_CdtPostRestrictionDesc` |  |  |  |
| 11 | `PORID.CUSTOMER.ID` | `PorSupplementaryInfo_CustomerId` |  |  |  |
| 12 | `PORID.CUSTOMER.NAME` | `PorSupplementaryInfo_CustomerName` |  |  |  |
| 13 | `PORID.CUSTOMER.ADDRESS` | `PorSupplementaryInfo_CustomerAddress` |  |  |  |
| 14 | `PORID.CUSTOMER.POSTAL.CODE` | `PorSupplementaryInfo_CustomerPostalCode` |  |  |  |
| 15 | `PORID.CUSTOMER.COUNTRY.CODE` | `PorSupplementaryInfo_CustomerCountryCode` |  |  |  |
| 16 | `PORID.CUSTOMER.RESIDENCY` | `PorSupplementaryInfo_CustomerResidency` |  |  |  |
| 17 | `PORID.CUSTOMER.LANGUAGE.ID` | `PorSupplementaryInfo_CustomerLanguageId` |  |  |  |
| 18 | `PORID.BUSINESS.LINE` | `PorSupplementaryInfo_BusinessLine` |  |  |  |
| 19 | `PORID.SECTOR.CODE` | `PorSupplementaryInfo_SectorCode` |  |  |  |
| 20 | `PORID.ACCOUNT.OFFICER` | `PorSupplementaryInfo_AccountOfficer` |  |  |  |
| 21 | `PORID.RELATED.IBAN` | `PorSupplementaryInfo_RelatedIban` |  |  |  |
| 22 | `PORID.BOOK.CODE` | `PorSupplementaryInfo_BookCode` |  |  |  |
| 23 | `PORID.ERROR.CODE` | `PorSupplementaryInfo_ErrorCode` |  |  |  |
| 24 | `PORID.CUSTOMER.PHONE.NUMBER` | `PorSupplementaryInfo_CustomerPhoneNumber` |  |  |  |
| 25 | `PORID.CUSTOMER.EMAIL.ID` | `PorSupplementaryInfo_CustomerEmailId` |  |  |  |
| 26 | `PORID.IDENTIFIER.CODE` | `PorSupplementaryInfo_IdentifierCode` |  |  |  |
| 27 | `PORID.OTHER.RESTRICTION.TYPE` | `PorSupplementaryInfo_OtherRestrictionType` |  |  |  |
| 28 | `PORID.OTHER.RESTRICTION.DESC` | `PorSupplementaryInfo_OtherRestrictionDesc` |  |  |  |
| 29 | `PORID.CATEGORY.CODE` | `PorSupplementaryInfo_CategoryCode` |  |  |  |
| 30 | `PORID.ACCOUNT.VALIDATION.DATE` | `PorSupplementaryInfo_AccountValidationDate` |  |  |  |
| 31 | `PORID.ACCOUNT.DDA.SYSTEM` | `PorSupplementaryInfo_AccountDdaSystem` |  |  |  |
| 32 | `PORID.OVER.ALL.DECISION` | `PorSupplementaryInfo_OverAllDecision` |  |  |  |
| 33 | `PORID.ACC.INF.BUILDING.NAME` | `PorSupplementaryInfo_AccInfBuildingName` |  |  |  |
| 34 | `PORID.ACC.INF.BUILDING.NUMBER` | `PorSupplementaryInfo_AccInfBuildingNumber` |  |  |  |
| 35 | `PORID.ACC.INF.PO.BOX.NUMBER` | `PorSupplementaryInfo_AccInfPoBoxNumber` |  |  |  |
| 36 | `PORID.ACC.INF.COUNTRY.SUBDIV` | `PorSupplementaryInfo_AccInfCountrySubdiv` |  |  |  |
| 37 | `PORID.ADDITIONAL.INFORMATION.CODE` | `PorSupplementaryInfo_AdditionalInformationCode` |  |  |  |
| 38 | `PORID.ADD.INF.TYPE.LINE.SEQ` | `PorSupplementaryInfo_AddInfTypeLineSeq` |  |  |  |
| 39 | `PORID.ADDITIONAL.INF.TAG` | `PorSupplementaryInfo_AdditionalInfTag` |  |  |  |
| 40 | `PORID.ADDITIONAL.INF.LINE` | `PorSupplementaryInfo_AdditionalInfLine` |  |  |  |
| 41 | `PORID.RESERVED.6` | `PorSupplementaryInfo_Reserved6` |  |  |  |
| 42 | `PORID.RESERVED.7` | `PorSupplementaryInfo_Reserved7` |  |  |  |
| 43 | `PORID.RESERVED.8` | `PorSupplementaryInfo_Reserved8` |  |  |  |
| 44 | `PORID.RESERVED.9` | `PorSupplementaryInfo_Reserved9` |  |  |  |
| 45 | `PORID.RESERVED.10` | `PorSupplementaryInfo_Reserved10` |  |  |  |
| 46 | `PORID.COVER.INFORMATION.CODE` | `PorSupplementaryInfo_CoverInformationCode` |  |  |  |
| 47 | `PORID.COVER.INF.TAG` | `PorSupplementaryInfo_CoverInfTag` |  |  |  |
| 48 | `PORID.COVER.INF.FREE.LINE` | `PorSupplementaryInfo_CoverInfFreeLine` |  |  |  |
| 49 | `PORID.RESERVED.11` | `PorSupplementaryInfo_Reserved11` |  |  |  |
| 50 | `PORID.RESERVED.12` | `PorSupplementaryInfo_Reserved12` |  |  |  |
| 51 | `PORID.RESERVED.13` | `PorSupplementaryInfo_Reserved13` |  |  |  |
| 52 | `PORID.RESERVED.14` | `PorSupplementaryInfo_Reserved14` |  |  |  |
| 53 | `PORID.RESERVED.15` | `PorSupplementaryInfo_Reserved15` |  |  |  |
| 54 | `PORID.PI.INFORMATIONCODE` | `PorSupplementaryInfo_PiInformationcode` |  |  |  |
| 55 | `PORID.PI.INF.TYPE.LINE.SEQ` | `PorSupplementaryInfo_PiInfTypeLineSeq` |  |  |  |
| 56 | `PORID.PI.INFORMATION.TAG` | `PorSupplementaryInfo_PiInformationTag` |  |  |  |
| 57 | `PORID.PI.INSTRUCTION.CODE` | `PorSupplementaryInfo_PiInstructionCode` |  |  |  |
| 58 | `PORID.PI.COUNTRY.CODE` | `PorSupplementaryInfo_PiCountryCode` |  |  |  |
| 59 | `PORID.PI.INFORMATION.LINE` | `PorSupplementaryInfo_PiInformationLine` |  |  |  |
| 60 | `PORID.OUTBOUND.CW.APP.FLAG` | `PorSupplementaryInfo_OutboundCwAppFlag` |  |  |  |
| 61 | `PORID.RESERVED.16` | `PorSupplementaryInfo_Reserved16` |  |  |  |
| 62 | `PORID.RESERVED.17` | `PorSupplementaryInfo_Reserved17` |  |  |  |
| 63 | `PORID.RESERVED.18` | `PorSupplementaryInfo_Reserved18` |  |  |  |
| 64 | `PORID.RESERVED.19` | `PorSupplementaryInfo_Reserved19` |  |  |  |
| 65 | `PORID.RESERVED.20` | `PorSupplementaryInfo_Reserved20` |  |  |  |
| 66 | `PORID.PO.INSTRUCTION.CODE` | `PorSupplementaryInfo_PoInstructionCode` |  |  |  |
| 67 | `PORID.PO.INF.TYPE.LINE.SEQUENCE` | `PorSupplementaryInfo_PoInfTypeLineSequence` |  |  |  |
| 68 | `PORID.PO.COUNTRY.CODE` | `PorSupplementaryInfo_PoCountryCode` |  |  |  |
| 69 | `PORID.PO.INFORMATION.LINE` | `PorSupplementaryInfo_PoInformationLine` |  |  |  |
| 70 | `PORID.PO.INFORMATION.CODE` | `PorSupplementaryInfo_PoInformationCode` |  |  |  |
| 71 | `PORID.RESERVED.21` | `PorSupplementaryInfo_Reserved21` |  |  |  |
| 72 | `PORID.RESERVED.22` | `PorSupplementaryInfo_Reserved22` |  |  |  |
| 73 | `PORID.RESERVED.23` | `PorSupplementaryInfo_Reserved23` |  |  |  |
| 74 | `PORID.RESERVED.24` | `PorSupplementaryInfo_Reserved24` |  |  |  |
| 75 | `PORID.RESERVED.25` | `PorSupplementaryInfo_Reserved25` |  |  |  |
| 76 | `PORID.PARTY.TYPE` | `PorSupplementaryInfo_PartyType` |  |  |  |
| 77 | `PORID.PARTY.ROLE` | `PorSupplementaryInfo_PartyRole` |  |  |  |
| 78 | `PORID.ROLE.INDICATOR` | `PorSupplementaryInfo_RoleIndicator` |  |  |  |
| 79 | `PORID.INFORMATION.TAG` | `PorSupplementaryInfo_InformationTag` |  |  |  |
| 80 | `PORID.NATIONAL.ID` | `PorSupplementaryInfo_NationalId` |  |  |  |
| 81 | `PORID.PARTY.IDENTIFIER.CODE` | `PorSupplementaryInfo_PartyIdentifierCode` |  |  |  |
| 82 | `PORID.PARTY.ACCOUNT.LINE` | `PorSupplementaryInfo_PartyAccountLine` |  |  |  |
| 83 | `PORID.PARTY.FREE.LINE` | `PorSupplementaryInfo_PartyFreeLine` |  |  |  |
| 84 | `PORID.DIRECT.PAYMENT.FLAG` | `PorSupplementaryInfo_DirectPaymentFlag` |  |  |  |
| 85 | `PORID.NAME` | `PorSupplementaryInfo_Name` |  |  |  |
| 86 | `PORID.COUNTRY` | `PorSupplementaryInfo_Country` |  |  |  |
| 87 | `PORID.ADDRESS.LINE` | `PorSupplementaryInfo_AddressLine` |  |  |  |
| 88 | `PORID.ORG.ID.OTHER.ID` | `PorSupplementaryInfo_OrgIdOtherId` |  |  |  |
| 89 | `PORID.ORG.ID.OTHER.SCH.CODE` | `PorSupplementaryInfo_OrgIdOtherSchCode` |  |  |  |
| 90 | `PORID.ORG.ID.OTHER.SCH.PROP` | `PorSupplementaryInfo_OrgIdOtherSchProp` |  |  |  |
| 91 | `PORID.ORG.ID.OTHER.ISSUER` | `PorSupplementaryInfo_OrgIdOtherIssuer` |  |  |  |
| 92 | `PORID.BIRTH.DATE` | `PorSupplementaryInfo_BirthDate` |  |  |  |
| 93 | `PORID.PROVINCE.OF.BIRTH` | `PorSupplementaryInfo_ProvinceOfBirth` |  |  |  |
| 94 | `PORID.CITY.OF.BIRTH` | `PorSupplementaryInfo_CityOfBirth` |  |  |  |
| 95 | `PORID.COUNTRY.OF.BIRTH` | `PorSupplementaryInfo_CountryOfBirth` |  |  |  |
| 96 | `PORID.PRV.ID.OTHER.ID` | `PorSupplementaryInfo_PrvIdOtherId` |  |  |  |
| 97 | `PORID.PRV.ID.OTHER.SCH.CODE` | `PorSupplementaryInfo_PrvIdOtherSchCode` |  |  |  |
| 98 | `PORID.PRV.ID.OTHER.SCH.PROP` | `PorSupplementaryInfo_PrvIdOtherSchProp` |  |  |  |
| 99 | `PORID.PRV.ID.OTHER.ISSUER` | `PorSupplementaryInfo_PrvIdOtherIssuer` |  |  |  |
| 100 | `PORID.CLEARING.SYSTEM.ID.CODE` | `PorSupplementaryInfo_ClearingSystemIdCode` |  |  |  |
| 101 | `PORID.CLEARING.MEMBER.ID` | `PorSupplementaryInfo_ClearingMemberId` |  |  |  |
| 102 | `PORID.CONTACT.NAME.PREFIX` | `PorSupplementaryInfo_ContactNamePrefix` |  |  |  |
| 103 | `PORID.CONTACT.NAME` | `PorSupplementaryInfo_ContactName` |  |  |  |
| 104 | `PORID.CONTACT.PHONE` | `PorSupplementaryInfo_ContactPhone` |  |  |  |
| 105 | `PORID.REVERSED.FROM` | `PorSupplementaryInfo_ReversedFrom` | TField |  | It indicates the status from which the payment is reversed. |
| 106 | `PORID.ENTRY.IDS` | `PorSupplementaryInfo_EntryIds` |  |  |  |
| 107 | `PORID.REVERSAL.ENTRYIDS` | `PorSupplementaryInfo_ReversalEntryids` |  |  |  |
| 108 | `PORID.BATCH.FEE.HOLD.INDICATOR` | `PorSupplementaryInfo_BatchFeeHoldIndicator` | TField |  | This field indicates whether the parent has to be held at fees till the fees of all the children are calculated. Possible values: Y, N or blank. N or blank - means that if no error is present for the parent when it is finalised then the children will be released at this moment. Y � means that the children will be released after fees have been calculated for the parent transaction. Example: For pain.008 (DDI) will be N or blank. |
| 109 | `PORID.SETTLEMENT.TYPE` | `PorSupplementaryInfo_SettlementType` | TField |  | Indicates whether the payment is post settled or pre settled. This field is an output of light weight and medium weight product tables. This is required to decide which dates API needs to be invoked for a direct debit instruction. This field can be left blank for non DDI payments. |
| 110 | `PORID.CLEARING.HOLIDAY` | `PorSupplementaryInfo_ClearingHoliday` | TField |  | Indicates for which clearing the non-working days must be looked up for the payment during dates calculation. This field is an output of light weight and medium weight product tables. This is required for DD Clearing Batch parent and batch child that are book payments but the settlement date must be calculated taking into consideration the clearing business date through which the child payments would be settled through. |
| 111 | `PORID.RET.REJ.ORIGINATED.BY` | `PorSupplementaryInfo_RetRejOriginatedBy` | TField |  | Indicates if the Return or Reject was Originated by the Bank or by the Debtor (Customer). Possible values: B � Return/Reject originated by the Bank D � Return/Reject originated by the Debtor empty - Payment was STP returned/rejected. |
| 112 | `PORID.AUTHORISED.MANDATE` | `PorSupplementaryInfo_AuthorisedMandate` | TField |  | Indicates if the Mandate is authorised or not. Possible values: Y � Mandate was authorised N � Mandate was unauthorised |
| 113 | `PORID.MANDATE.AUTO.REGISTERED` | `PorSupplementaryInfo_MandateAutoRegistered` | TField |  | Indicates if the Mandate was auto registered in the DD management system or not. Possible values: Y � Mandate was auto registered. blank � Mandate was not auto registered. |
| 114 | `PORID.CHG.RESERVATION.AMOUNT` | `PorSupplementaryInfo_ChgReservationAmount` | TField |  | Holds the Debit charge amount that is reserved. |
| 115 | `PORID.RES.DBT.CHG.ACC.CMP.ID` | `PorSupplementaryInfo_ResDbtChgAccCmpId` | TField |  | Holds Debit charge account company ID. |
| 116 | `PORID.RES.DBT.CHG.ACCOUNT` | `PorSupplementaryInfo_ResDbtChgAccount` | TField |  | Holds Debit charge account number. |
| 117 | `PORID.RES.DBT.CHG.ACC.CURR.CODE` | `PorSupplementaryInfo_ResDbtChgAccCurrCode` | TField |  | Holds Debit charge account currency. |
| 118 | `PORID.CHG.RESERVATION.REQ.DATE` | `PorSupplementaryInfo_ChgReservationReqDate` | TField |  | Holds the Date on which balance reservation was requested for on the debit charge account. |
| 119 | `PORID.CHG.RESERVATION.KEY` | `PorSupplementaryInfo_ChgReservationKey` | TField |  | Holds the Reservation key returned by the DDA after reserving balance on the debit charge account for debit charges. |
| 120 | `PORID.RISK.FILTER.CONDITION.ID` | `PorSupplementaryInfo_RiskFilterConditionId` |  |  |  |
| 121 | `PORID.DEBIT.INSTRUCT.AMOUNT` | `PorSupplementaryInfo_DebitInstructAmount` | TField |  |  |
| 122 | `PORID.MANUAL.RET.REJ.FLAG` | `PorSupplementaryInfo_ManualRetRejFlag` | TField |  | Indicates if the Payment is manually returned, rejected or refunded. Possible values: Y or blank. Y - Payment was manually returned, rejected or refunded. blank - Payment was not manually returned, rejected or refunded. |
| 123 | `PORID.REVERSE.RETURN.TXN.ID` | `PorSupplementaryInfo_ReverseReturnTxnId` | TField |  | Holds the Transaction ID of the new Return or Reverse transaction. |
| 124 | `PORID.RESERVE.WITH.CHARGES` | `PorSupplementaryInfo_ReserveWithCharges` | TField |  |  |
| 125 | `PORID.APPROVAL.CODE` | `PorSupplementaryInfo_ApprovalCode` | TField |  |  |
| 126 | `PORID.RECALL.INDICATOR` | `PorSupplementaryInfo_RecallIndicator` | TField |  | Indicates if the payment was returned due to a cancellation request received from clearing. Possible values: Y or blank. |
| 127 | `PORID.DEBIT.RETRIEVE.ACC.DET` | `PorSupplementaryInfo_DebitRetrieveAccDet` | TField |  |  |
| 128 | `PORID.CREDIT.RETRIEVE.ACC.DET` | `PorSupplementaryInfo_CreditRetrieveAccDet` | TField |  |  |
| 129 | `PORID.AMOUNT.TO.BE.RESERVED` | `PorSupplementaryInfo_AmountToBeReserved` | TField |  | This field is applicable only when the bank�s core system is external (ExternalCoreSystem is Y or H in PP.COMPANY.PROPERTIES table). If an asynchronous request is made to the external system for balance reservation then this field will hold the reservation amount that was calculated by the system ( taking into account charges, FX etc ). |
| 130 | `PORID.DEBIT.IBAN.ACC.NUMBER` | `PorSupplementaryInfo_DebitIbanAccNumber` | TField |  | This field holds the debit account IBAN number |
| 131 | `PORID.CRDIT.IBAN.ACC.NUMBER` | `PorSupplementaryInfo_CrditIbanAccNumber` | TField |  | This field holds the credit account IBAN number |
| 132 | `PORID.BILLING.INDICATOR` | `PorSupplementaryInfo_BillingIndicator` | TField |  |  |
| 133 | `PORID.SERVICE.TYPE.IDENTIFIER` | `PorSupplementaryInfo_ServiceTypeIdentifier` | TField |  | This will store the value of Tag 111 (Service Type Identifier) of basic header block of SWIFT message. Example 001 |
| 134 | `PORID.ORDER.ENTRY.ID` | `PorSupplementaryInfo_OrderEntryId` |  |  |  |
| 135 | `PORID.RETURN.PAYMENT.REFERENCE` | `PorSupplementaryInfo_ReturnPaymentReference` | TField |  |  |
| 136 | `PORID.SIMULATED.PAYMENT.FLAG` | `PorSupplementaryInfo_SimulatedPaymentFlag` | TField |  | Possible values: SIM � Payment is validated from Payment Order for the first time. RESIM - Payment is validated again from Payment Order. AUTH - Payment is authorised from Payment Order. |
| 137 | `PORID.INDICATIVE.RATE` | `PorSupplementaryInfo_IndicativeRate` | TField |  | When a payment is executed in a simulate mode, this rate is calculated either when there is a Debit FX breach or the payment is future dated with FX on debit side. This is an indicative rate and not the actual debit FX rate. |
| 138 | `PORID.EB.DUPLICATE.TYPE.ID` | `PorSupplementaryInfo_EbDuplicateTypeId` | TField |  | Holds the record id of the EB.DUPLICATE.TYPE application which is configured at the selected payment product |
| 139 | `PORID.PAYMENT.METHOD` | `PorSupplementaryInfo_PaymentMethod` | TField |  | Specifies whether the payment is an INSTant or a NearRealINSTant Payment Possible values: INST, NRINST or Blank. |
| 140 | `PORID.INST.ACCEPT.DATE.TIME` | `PorSupplementaryInfo_InstAcceptDateTime` |  |  |  |
| 141 | `PORID.REPAIR.REASON.CODE` | `PorSupplementaryInfo_RepairReasonCode` |  |  |  |
| 142 | `PORID.CLEARING.STATUS.MSG.TYPE` | `PorSupplementaryInfo_ClearingStatusMsgType` | TField |  | Indicates the message type that is used for the payment when sending staus confirmation to the Clearing House. Should be a valid value in PP.MSGPAYMENTTYPE |
| 143 | `PORID.CLEARING.INVEST.MSG.TYPE` | `PorSupplementaryInfo_ClearingInvestMsgType` | TField |  | Available only for instant payments Holds the message type that needs to be used when the originator bank wishes to send an investigation message to the Clearing House/Direct Participant. Investigation messages are sent when no response has been received for a credit transfer that has been sent out by the originator bank. Should be a valid value in PP.MSGPAYMENTTYPE Holds the message type (pacs.002) when the Beneficiary bank sends an investigation message to the Clearing House. Investigation message is sent by the beneficiary when final status report is not received from the clearing. |
| 144 | `PORID.INVEST.RETRY.TIME.COUNT` | `PorSupplementaryInfo_InvestRetryTimeCount` | TField |  | Holds the time stamp when the last automatic investigation message (pacs.002) was sent for an instant payment by the beneficiary along with the number of times such a message has been sent thus far. |
| 145 | `PORID.BENEFICIARY.ID` | `PorSupplementaryInfo_BeneficiaryId` | TField |  | This field is used to identify the beneficiary. Holds a valid ID from the T24 beneficary application |
| 146 | `PORID.COMPANY.NCC` | `PorSupplementaryInfo_CompanyNcc` | TField |  | Holds the processing company�s National clearing code for the clearing. This field is require to map the company�s sort code in the outgoing message to the clearing |
| 147 | `PORID.CHEQUE.STATUS` | `PorSupplementaryInfo_ChequeStatus` | TField |  | Holds the status of Cheque |
| 148 | `PORID.MANUALLY.VERIFIED` | `PorSupplementaryInfo_ManuallyVerified` | TField |  |  |
| 149 | `PORID.PREVIEW.REFERENCE.COV` | `PorSupplementaryInfo_PreviewReferenceCov` | TField |  | Field to maintain the reference for the cover payments. For MX Cover payments it is same as the serial payment reference |
| 150 | `PORID.PREVIEW.REFERENCE.210` | `PorSupplementaryInfo_PreviewReference210` | TField |  | Field to maintain the reference id for the advices For MX Advices the reference id will be same as the bulk reference and file reference. |
| 151 | `PORID.BENEFICIARY.PARTY.TAG.OPTION` | `PorSupplementaryInfo_BeneficiaryPartyTagOption` | TField |  |  |
| 152 | `PORID.LOCAL.REF` | `PorSupplementaryInfo_LocalRef` |  |  |  |
| 153 | `PORID.LOC.FIELD.NAME` | `PorSupplementaryInfo_LocFieldName` |  |  |  |
| 154 | `PORID.LOC.FIELD.VALUE` | `PorSupplementaryInfo_LocFieldValue` |  |  |  |
| 155 | `PORID.CLEARING.SYSTEM.ID.CD` | `PorSupplementaryInfo_ClearingSystemIdCd` | TField | Yes | This field indicates the National clearing system code for clearing This code can be used along with member Identification ID for different financial institutions present in the outgoing message. This field is populated from ClearingSystemIdCode in PP.CLEARING table Example GBDSC : For UK clearings where sort code is used. Validation Rules: - non mandatory field This field can hold upto 5 characters. |
| 156 | `PORID.RATE.FIXING` | `PorSupplementaryInfo_RateFixing` | TField |  | Field to indicate the different stages of the rate fixing functionality for the payment. Possible values: Y, RateRequested, RateRequestedWithReservation, RateReceived, RateNotRequired |
| 157 | `PORID.RATE.FIXING.DATE` | `PorSupplementaryInfo_RateFixingDate` | TField |  | Date on which User opts out of Rate Fixing Functionality. |
| 158 | `PORID.ACER.RECORD.ID` | `PorSupplementaryInfo_AcerRecordId` | TField |  | AC.EXPECTED.RECS ID created for the payment record In Hold for Cover functionality, it will be used to hold ACER Record Id of �Expected Cover�/�Received Cover� type record. This field will be used for both payment transaction and cover In MT210 Matching functionality, it will be used to hold ACER Record Id of 'Receipt' type record. |
| 159 | `PORID.ACER.MATCHED.ID` | `PorSupplementaryInfo_AcerMatchedId` | TField |  | AC.EXPECTED.RECS ID created for matched Id In Hold for Cover functionality, it will be used to hold ACER Matched Id of �Expected Cover�/�Received Cover� type record. This field will be used for both payment transaction and cover In MT210 Matching functionality, it will be used to hold ACER Record Id of 'Expected Receipt' type record. |
| 160 | `PORID.MATCH.STATUS` | `PorSupplementaryInfo_MatchStatus` | TField |  | Indicates Match status of ACER Record based on ACER Matched Record In Hold for Cover functionality, it will be used to hold Match status in AC.EXPECTED.RECS for �Expected Cover�/�Received Cover� In MT210 Matching functionality, it will be used to hold Match status in AC.EXPECTED.RECS for �Receipt�/�Expected Receipt� Can be Matched, Waiting, Manually Matched etc |
| 161 | `PORID.CANCEL.MSG.REFERENCE` | `PorSupplementaryInfo_CancelMsgReference` | TField |  | Stores the EBQA ID used for received or sent recall request,negative response or status update on recall Link between the tables EBQA and TPS transaction |
| 162 | `PORID.PAYMENT.STATUS.MSG.REF` | `PorSupplementaryInfo_PaymentStatusMsgRef` | TField |  | Stores the EBQA ID used for investigation messages received or sent for instant credit transfer payments that have not received final confirmation from the clearing or DP. Link between the tables EBQA and TPS transaction |
| 163 | `PORID.STATUS.ACCEPTANCE.CODE` | `PorSupplementaryInfo_StatusAcceptanceCode` | TField |  | This field will holds the pacs.002 status code ACSC/ACWC when an inward pacs.002 is received for an outward pacs.008 sent to clearing. This field will also store the status code(ACSC/ACWC) returned by API attached to the field EnrichOutMessageAPI in PP.CLEARING |
| 164 | `PORID.CONTACT.MOBILE.PHONE` | `PorSupplementaryInfo_ContactMobilePhone` |  |  |  |
| 165 | `PORID.CONTACT.FAX` | `PorSupplementaryInfo_ContactFax` |  |  |  |
| 166 | `PORID.CONTACT.EMAIL.ADDR` | `PorSupplementaryInfo_ContactEmailAddr` |  |  |  |
| 167 | `PORID.CONTACT.OTHR` | `PorSupplementaryInfo_ContactOthr` |  |  |  |
| 168 | `PORID.ORIGINAL.OR.RETURN.ID` | `PorSupplementaryInfo_OriginalOrReturnId` | TField |  | Auto populated by the system. Holds the FT Number. When a pacs.004 return message is initiated and processed the original payment reference should be update to this field. Similarly the return payment reference should also be update in the original payment in this field. |
| 169 | `PORID.MT210.RECEIVED.AFTER.CUTOFF` | `PorSupplementaryInfo_Mt210ReceivedAfterCutoff` | TField |  |  |
| 170 | `PORID.SOURCE.TYPE` | `PorSupplementaryInfo_SourceType` | TField |  |  |
| 171 | `PORID.SENDER.LIMIT.FOR.COVER.PYMT` | `PorSupplementaryInfo_SenderLimitForCoverPymt` | TField |  | It will be used to indicate whether payment processed based on Limit configured in ER.COVER.LIMIT when cover message is not received for the payment Possible values are : Y or N Y - When transaction amount is within the Limit configured, then this field will be updated with 'Y' N - When transaction amount is not within the Limit configured, then this field will be updated with 'N' |
| 172 | `PORID.WAIT.FOR.COVER.PAYMENTS` | `PorSupplementaryInfo_WaitForCoverPayments` | TField |  | Field to indicate whether payment should be put on hold for cover payment processing Possible values are : Y or N Y - Payment should be put oh Hold for Cover processing N - No need to put payment in Hold for Cover processing |
| 173 | `PORID.COVER.PAYMENT.RECEIVED` | `PorSupplementaryInfo_CoverPaymentReceived` | TField |  | Field to indicate if payment is a cover payment received for related payment transaction Possible values are : Y or R Y - Payment received is a cover payment R - MT202 is received as a cover payment for MT103/MT202 |
| 174 | `PORID.TXN.STOP.RESPONSE` | `PorSupplementaryInfo_TxnStopResponse` | TField |  | When TPH receives response from Transaction Stop check then the flag TxnStopResponse will be updated with value R, else it will be blank When the value is set to R, TPH will not perform Transaction Stop again on the payment provided the debit main account is not changed. Possible values are - R or Blank where, R - Received |
| 175 | `PORID.REQUEST.TYPE` | `PorSupplementaryInfo_RequestType` |  |  |  |
| 176 | `PORID.RECORD.KEY` | `PorSupplementaryInfo_RecordKey` |  |  |  |
| 177 | `PORID.CONSOLIDATE.REJECTS` | `PorSupplementaryInfo_ConsolidateRejects` | TField |  | This field will be updated with C if the respective transaction Iis rejected and a reject booking has to be performed as part of a consolidated reject transaction |
| 178 | `PORID.INSTRD.AGT.OTHR.ID` | `PorSupplementaryInfo_InstrdAgtOthrId` | TField |  | Field to store the Instructed Agent Other Id |
| 179 | `PORID.BTR.INDICATOR` | `PorSupplementaryInfo_BtrIndicator` | TField |  | Indicates if this is a bank transfer |
| 180 | `PORID.REG.DEBTOR.CREDITOR.RPT` | `PorSupplementaryInfo_RegDebtorCreditorRpt` |  |  |  |
| 181 | `PORID.REG.AUTHORITY.NAME` | `PorSupplementaryInfo_RegAuthorityName` |  |  |  |
| 182 | `PORID.REG.AUTHORITY.CTRY.CODE` | `PorSupplementaryInfo_RegAuthorityCtryCode` |  |  |  |
| 183 | `PORID.REG.REP.TYPE` | `PorSupplementaryInfo_RegRepType` |  |  |  |
| 184 | `PORID.REG.REP.DATE` | `PorSupplementaryInfo_RegRepDate` |  |  |  |
| 185 | `PORID.REG.REP.COUNTRY.CODE` | `PorSupplementaryInfo_RegRepCountryCode` |  |  |  |
| 186 | `PORID.REG.REP.CODE` | `PorSupplementaryInfo_RegRepCode` |  |  |  |
| 187 | `PORID.REG.REP.CCY` | `PorSupplementaryInfo_RegRepCcy` |  |  |  |
| 188 | `PORID.REG.REP.AMOUNT` | `PorSupplementaryInfo_RegRepAmount` |  |  |  |
| 189 | `PORID.REG.REP.INFORMATION` | `PorSupplementaryInfo_RegRepInformation` |  |  |  |
| 190 | `PORID.STAND.IN` | `PorSupplementaryInfo_StandIn` | TField |  | To indicate that the pacs.008 message is received from STAND IN Queue Possible value: "Y" , message from STANDIN Queue |
| 191 | `PORID.COUNTRY.CODE` | `PorSupplementaryInfo_CountryCode` |  |  |  |
| 192 | `PORID.CASE.TYPE` | `PorSupplementaryInfo_CaseType` |  |  |  |
| 193 | `PORID.CASE.ID` | `PorSupplementaryInfo_CaseId` |  |  |  |
| 194 | `PORID.ALIAS.TYPE` | `PorSupplementaryInfo_AliasType` |  |  |  |
| 195 | `PORID.RELEASE.ON.SYSTEM.DATE` | `PorSupplementaryInfo_ReleaseOnSystemDate` | TField |  | Indicates whether the payment can be released from output warehouse based on System date or not. Possible Values:Y, N and Blank Y or Blank - Release Payment only when System date matches with Send date Y - Release Payment when Current Business date matches Send date |
| 196 | `PORID.RECALL.STATUS` | `PorSupplementaryInfo_RecallStatus` | TField |  | This field indicates status of gSRP request received for a Payment from the Tracker. Possible Values: REQUESTED, ACCEPED and REJECTED REQUESTED - When gSRP request received , system will update this field value as REQUESTED ACCEPED - When gSRP request accepted , system will update this field value as ACCEPED REJECTED - When gSRP request rejected , system will update this field value as REJECTED And this field is also used to indicate status of camt.055 request received for a Payment. Possible Values for camt.055: CANCELLED CANCELLED - When camt.055 request received and positive response(camt.029) is sent out. |
| 197 | `PORID.REQUESTED.EXECUTION.TIME` | `PorSupplementaryInfo_RequestedExecutionTime` | TField |  | The execution time requested by the user by when the payment order should be processed by the system. |
| 198 | `PORID.EMANDATE.SERVICE` | `PorSupplementaryInfo_EMandateService` |  |  |  |
| 199 | `PORID.RESERVED.29` | `PorSupplementaryInfo_Reserved29` |  |  |  |
| 200 | `PORID.RESERVED.30` | `PorSupplementaryInfo_Reserved30` | TField |  | Reserved Field 30 |
| 201 | `PORID.RESERVED.31` | `PorSupplementaryInfo_Reserved31` | TField |  |  |
| 202 | `PORID.RESERVED.32` | `PorSupplementaryInfo_Reserved32` | TField |  |  |
| 203 | `PORID.RESERVED.33` | `PorSupplementaryInfo_Reserved33` | TField |  |  |
| 204 | `PORID.RESERVED.34` | `PorSupplementaryInfo_Reserved34` | TField |  |  |
| 205 | `PORID.PARTY.ACC.SCH.CODE` | `PorSupplementaryInfo_PartyAccSchCode` |  |  |  |
| 206 | `PORID.PARTY.ACC.SCH.ISSUER` | `PorSupplementaryInfo_PartyAccSchIssuer` |  |  |  |
| 207 | `PORID.PARTY.ACC.TYPE.CODE` | `PorSupplementaryInfo_PartyAccTypeCode` |  |  |  |
| 208 | `PORID.PARTY.ACC.TYPE.PROP` | `PorSupplementaryInfo_PartyAccTypeProp` |  |  |  |
| 209 | `PORID.PARTY.ACC.CURRENCY` | `PorSupplementaryInfo_PartyAccCurrency` |  |  |  |
| 210 | `PORID.PARTY.ACC.NAME` | `PorSupplementaryInfo_PartyAccName` |  |  |  |
| 211 | `PORID.PARTY.ACC.PROXY.TYPE.CODE` | `PorSupplementaryInfo_PartyAccProxyTypeCode` |  |  |  |
| 212 | `PORID.PARTY.ACC.PROXY.TYPE.PROP` | `PorSupplementaryInfo_PartyAccProxyTypeProp` |  |  |  |
| 213 | `PORID.PARTY.ACC.PROXY.ID` | `PorSupplementaryInfo_PartyAccProxyId` |  |  |  |
| 214 | `PORID.CLEARING.SYSTEM.ID.PROP` | `PorSupplementaryInfo_ClearingSystemIdProp` |  |  |  |
| 215 | `PORID.LEI` | `PorSupplementaryInfo_Lei` |  |  |  |
| 216 | `PORID.ADDR.DEPT` | `PorSupplementaryInfo_AddrDept` |  |  |  |
| 217 | `PORID.ADDR.SUBDEPT` | `PorSupplementaryInfo_AddrSubdept` |  |  |  |
| 218 | `PORID.ADDR.STREET.NAME` | `PorSupplementaryInfo_AddrStreetName` |  |  |  |
| 219 | `PORID.ADDR.BLDG.NO` | `PorSupplementaryInfo_AddrBldgNo` |  |  |  |
| 220 | `PORID.ADDR.BLDG.NAME` | `PorSupplementaryInfo_AddrBldgName` |  |  |  |
| 221 | `PORID.ADDR.BLDG.FLOOR` | `PorSupplementaryInfo_AddrBldgFloor` |  |  |  |
| 222 | `PORID.ADDR.POST.BOX` | `PorSupplementaryInfo_AddrPostBox` |  |  |  |
| 223 | `PORID.ADDR.ROOM` | `PorSupplementaryInfo_AddrRoom` |  |  |  |
| 224 | `PORID.ADDR.POST.CODE` | `PorSupplementaryInfo_AddrPostCode` |  |  |  |
| 225 | `PORID.ADDR.TOWN.NAME` | `PorSupplementaryInfo_AddrTownName` |  |  |  |
| 226 | `PORID.ADDR.TOWN.LOCATION` | `PorSupplementaryInfo_AddrTownLocation` |  |  |  |
| 227 | `PORID.ADDR.DISTRICT` | `PorSupplementaryInfo_AddrDistrict` |  |  |  |
| 228 | `PORID.ADDR.COUNTRY.SUB.DIV` | `PorSupplementaryInfo_AddrCountrySubDiv` |  |  |  |
| 229 | `PORID.COUNTRY.OF.RESIDENCE` | `PorSupplementaryInfo_CountryOfResidence` |  |  |  |
| 230 | `PORID.ACC.INF.POST.CODE` | `PorSupplementaryInfo_AccInfPostCode` |  |  |  |
| 231 | `PORID.ACC.INF.DISTRICT.NAME` | `PorSupplementaryInfo_AccInfDistrictName` |  |  |  |
| 232 | `PORID.REL.REMINF.RMTID` | `PorSupplementaryInfo_RelReminfRmtid` | TField |  | Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system |
| 233 | `PORID.REL.REMINF.RMTLOC.MTD` | `PorSupplementaryInfo_RelReminfRmtlocMtd` |  |  |  |
| 234 | `PORID.REL.REMINF.RMTLC.ELECTADD` | `PorSupplementaryInfo_RelReminfRmtlcElectadd` |  |  |  |
| 235 | `PORID.REL.REMINF.RMTLC.ADD.NM` | `PorSupplementaryInfo_RelReminfRmtlcAddNm` |  |  |  |
| 236 | `PORID.REL.REMNF.RMTLC.ADD.DEP` | `PorSupplementaryInfo_RelRemnfRmtlcAddDep` |  |  |  |
| 237 | `PORID.REL.REMNF.RMTLC.ADD.SDEP` | `PorSupplementaryInfo_RelRemnfRmtlcAddSdep` |  |  |  |
| 238 | `PORID.REL.REMNF.RMLC.ADD.ST.NM` | `PorSupplementaryInfo_RelRemnfRmlcAddStNm` |  |  |  |
| 239 | `PORID.REL.REMNF.RMLC.ADD.BG.NO` | `PorSupplementaryInfo_RelRemnfRmlcAddBgNo` |  |  |  |
| 240 | `PORID.REL.REMNF.RMLC.ADD.BG.NM` | `PorSupplementaryInfo_RelRemnfRmlcAddBgNm` |  |  |  |
| 241 | `PORID.REL.REMNF.RMLC.ADD.BG.FR` | `PorSupplementaryInfo_RelRemnfRmlcAddBgFr` |  |  |  |
| 242 | `PORID.REL.REMNF.RMLC.ADD.PO.BX` | `PorSupplementaryInfo_RelRemnfRmlcAddPoBx` |  |  |  |
| 243 | `PORID.REL.REMINF.RMTLC.ADD.RM` | `PorSupplementaryInfo_RelReminfRmtlcAddRm` |  |  |  |
| 244 | `PORID.REL.REMNF.RMLC.ADD.PO.CD` | `PorSupplementaryInfo_RelRemnfRmlcAddPoCd` |  |  |  |
| 245 | `PORID.REL.REMNF.RMLC.ADD.TW.NM` | `PorSupplementaryInfo_RelRemnfRmlcAddTwNm` |  |  |  |
| 246 | `PORID.REL.REMNF.RMLC.ADD.TN.LC` | `PorSupplementaryInfo_RelRemnfRmlcAddTnLc` |  |  |  |
| 247 | `PORID.REL.REMNF.RMTLC.ADD.DSCT` | `PorSupplementaryInfo_RelRemnfRmtlcAddDsct` |  |  |  |
| 248 | `PORID.REL.RMNF.RLC.AD.CY.SB.DV` | `PorSupplementaryInfo_RelRmnfRlcAdCySbDv` |  |  |  |
| 249 | `PORID.REL.REMINF.RMTLOC.CTRY` | `PorSupplementaryInfo_RelReminfRmtlocCtry` |  |  |  |
| 250 | `PORID.REL.REMINF.RMTLOC.ADDLINE` | `PorSupplementaryInfo_RelReminfRmtlocAddline` |  |  |  |
| 251 | `PORID.PARTY.CUSTOMER.ID` | `PorSupplementaryInfo_PartyCustomerId` |  |  |  |
| 252 | `PORID.CLEARING.SYSTEM.REFERENCE` | `PorSupplementaryInfo_ClearingSystemReference` | TField |  | Unique reference, as assigned by a clearing system, to unambiguously identify the Instruction. |
| 253 | `PORID.TIMEOUT.ACT.RETRY.TIME.COUNT` | `PorSupplementaryInfo_TimeoutActRetryTimeCount` | TField |  |  |
| 254 | `PORID.REVERSAL.INDICATOR` | `PorSupplementaryInfo_ReversalIndicator` | TField |  | Indicates if a reversal request was received from the Clearing for an inward CT/DD Request. This indicator would be set if "Original PMT ID" API is configured. For cases where the original CT/DD request was in an intermediate status when the reversal request was received, system would not perform posting on the original transaction, after it resumes processing. Possible Values: Y or Blank. |
| 255 | `PORID.ACC.INF.DEPARTMENT` | `PorSupplementaryInfo_AccInfDepartment` |  |  |  |
| 256 | `PORID.ACC.INF.SUBDEPARTMENT` | `PorSupplementaryInfo_AccInfSubdepartment` |  |  |  |
| 257 | `PORID.ACC.INF.STREET.NAME` | `PorSupplementaryInfo_AccInfStreetName` |  |  |  |
| 258 | `PORID.ACC.INF.BUILDING.FLOOR` | `PorSupplementaryInfo_AccInfBuildingFloor` |  |  |  |
| 259 | `PORID.ACC.INF.BUILDING.ROOM` | `PorSupplementaryInfo_AccInfBuildingRoom` |  |  |  |
| 260 | `PORID.ACC.INF.TOWN.NAME` | `PorSupplementaryInfo_AccInfTownName` |  |  |  |
| 261 | `PORID.ACC.INF.TOWN.LOCATION.NAME` | `PorSupplementaryInfo_AccInfTownLocationName` |  |  |  |
| 262 | `PORID.ACC.INF.ADDRESSLINE` | `PorSupplementaryInfo_AccInfAddressline` |  |  |  |
| 263 | `PORID.SYSTEM.GENERATED` | `PorSupplementaryInfo_SystemGenerated` | TField |  | To indicate Return was generated by TPH and not received from clearing or instructed bank. So that direction can be skipped if this value is set and also in mapping based on outgoing and redirect-different values can be populated. Possible Values: Y or Blank. |
| 270 | `PORID.MESSAGE.CONTENT.NAME` | `PorSupplementaryInfo_MessageContentName` |  |  |  |
| 271 | `PORID.MESSAGE.CONTENT` | `PorSupplementaryInfo_MessageContent` |  |  |  |
| 272 | `PORID.ADDR.TYPE.PROP` | `PorSupplementaryInfo_AddrTypeProp` |  |  |  |
| 273 | `PORID.ADDR.TYPE.PROP.ISSUER` | `PorSupplementaryInfo_AddrTypePropIssuer` |  |  |  |
| 274 | `PORID.ADDR.TYPE.PROP.SCHNAME` | `PorSupplementaryInfo_AddrTypePropSchname` |  |  |  |
| 275 | `PORID.CONTACT.EMAIL.PURP` | `PorSupplementaryInfo_ContactEmailPurp` |  |  |  |
| 276 | `PORID.CONTACT.JOB.TITLE` | `PorSupplementaryInfo_ContactJobTitle` |  |  |  |
| 277 | `PORID.CONTACT.RESPOSIBILITY` | `PorSupplementaryInfo_ContactResponsibility` |  |  |  |
| 278 | `PORID.CONTACT.DEPARTMENT` | `PorSupplementaryInfo_ContactDepartment` |  |  |  |
| 279 | `PORID.CONTACT.CHANNEL.TYPE` | `PorSupplementaryInfo_ContactChannelType` |  |  |  |
| 280 | `PORID.CONTACT.PREF.METHOD` | `PorSupplementaryInfo_ContactPrefMethod` |  |  |  |
| 281 | `PORID.FATF.WTR2.SKIP.FLAG` | `PorSupplementaryInfo_FatfWtr2SkipFlag` | TField |  | Flag used to skip the FATF and WTR2 check for the transaction. |
| 282 | `PORID.RESERVATION.TYPE` | `PorSupplementaryInfo_ReservationType` | TField |  | This is used to store whether partial Funds have been reserved for the cheque payment or represented partial cheque Allowed values are None, Partial, Represented |
| 283 | `PORID.RETURN.TYPE` | `PorSupplementaryInfo_ReturnType` | TField |  |  |
| 284 | `PORID.IN.SWITCH.DETS` | `PorSupplementaryInfo_InSwitchDets` | TField |  | Field used to store SwitchIn details at L2 level |
| 285 | `PORID.CUSTOMER.NAME.1` | `PorSupplementaryInfo_CustomerName1` |  |  |  |
| 286 | `PORID.CUSTOMER.ADDRESS1` | `PorSupplementaryInfo_CustomerAddress1` |  |  |  |
| 287 | `PORID.PrefCorrespondentID` | `PorSupplementaryInfo_Prefcorrespondentid` | TField |  | Field to Display the Preferred Correspondent ID of Nostro payments |
| 288 | `PORID.CUSTOMER.GROUP.ID` | `PorSupplementaryInfo_CustomerGroupId` |  |  |  |
| 289 | `PORID.CANCEL.COVR.MSG.REF` | `PorSupplementaryInfo_CancelCovrMsgRef` | TField |  | Stores the EBQA ID used for received or sent recall request for cover message /negative response for recall |
| 290 | `PORID.DELIVERY.REFERENCE` | `PorSupplementaryInfo_DeliveryReference` |  |  |  |
| 291 | `PORID.DATE.PRODUCT` | `PorSupplementaryInfo_Dateproduct` |  |  |  |
