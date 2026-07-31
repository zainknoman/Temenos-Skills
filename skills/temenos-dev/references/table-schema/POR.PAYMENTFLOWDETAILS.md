# POR.PAYMENTFLOWDETAILS — Table Schema

> Source: `INSERTS/I_F.POR.PAYMENTFLOWDETAILS` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPFD.CompanyID` | `PorPaymentflowdetails_Companyid` |  |  |  |
| 2 | `PPPFD.FTNumber` | `PorPaymentflowdetails_Ftnumber` |  |  |  |
| 3 | `PPPFD.ReversedFrom` | `PorPaymentflowdetails_Reversedfrom` |  |  |  |
| 4 | `PPPFD.EntryIDs` | `PorPaymentflowdetails_Entryids` |  |  |  |
| 5 | `PPPFD.ReversalEntryIDs` | `PorPaymentflowdetails_Reversalentryids` |  |  |  |
| 6 | `PPPFD.BatchFeeHoldIndicator` | `PorPaymentflowdetails_Batchfeeholdindicator` |  |  |  |
| 7 | `PPPFD.SettlementType` | `PorPaymentflowdetails_Settlementtype` |  |  |  |
| 8 | `PPPFD.ClearingHoliday` | `PorPaymentflowdetails_Clearingholiday` |  |  |  |
| 9 | `PPPFD.RetRejOriginatedBy` | `PorPaymentflowdetails_Retrejoriginatedby` |  |  |  |
| 10 | `PPPFD.AuthorisedMandate` | `PorPaymentflowdetails_Authorisedmandate` |  |  |  |
| 11 | `PPPFD.MandateAutoRegistered` | `PorPaymentflowdetails_Mandateautoregistered` |  |  |  |
| 12 | `PPPFD.ChgReservationAmount` | `PorPaymentflowdetails_Chgreservationamount` |  |  |  |
| 13 | `PPPFD.ReservationDebitChgAccCmpID` | `PorPaymentflowdetails_Reservationdebitchgacccmpid` |  |  |  |
| 14 | `PPPFD.ReservationDebitChgAccount` | `PorPaymentflowdetails_Reservationdebitchgaccount` |  |  |  |
| 15 | `PPPFD.ReservationDebitChgAccCurrCode` | `PorPaymentflowdetails_Reservationdebitchgacccurrcode` |  |  |  |
| 16 | `PPPFD.ChgReservationReqDate` | `PorPaymentflowdetails_Chgreservationreqdate` |  |  |  |
| 17 | `PPPFD.ChgReservationKey` | `PorPaymentflowdetails_Chgreservationkey` |  |  |  |
| 18 | `PPPFD.RiskFilterConditionId` | `PorPaymentflowdetails_Riskfilterconditionid` |  |  |  |
| 19 | `PPPFD.DebitInstructAmount` | `PorPaymentflowdetails_Debitinstructamount` |  |  |  |
| 20 | `PPPFD.ManuallyRetRejFlag` | `PorPaymentflowdetails_Manuallyretrejflag` |  |  |  |
| 21 | `PPPFD.ReverseReturnTransactionID` | `PorPaymentflowdetails_Reversereturntransactionid` |  |  |  |
| 22 | `PPPFD.ReserveWithCharges` | `PorPaymentflowdetails_Reservewithcharges` |  |  |  |
| 23 | `PPPFD.ApprovalCode` | `PorPaymentflowdetails_Approvalcode` |  |  |  |
| 24 | `PPPFD.RecallIndicator` | `PorPaymentflowdetails_Recallindicator` |  |  |  |
| 25 | `PPPFD.DebitRetrieveAccountDetails` | `PorPaymentflowdetails_Debitretrieveaccountdetails` |  |  |  |
| 26 | `PPPFD.CreditRetrieveAccountDetails` | `PorPaymentflowdetails_Creditretrieveaccountdetails` |  |  |  |
| 27 | `PPPFD.AmountToBeReserved` | `PorPaymentflowdetails_Amounttobereserved` |  |  |  |
| 28 | `PPPFD.DebitIBANAccNumber` | `PorPaymentflowdetails_Debitibanaccnumber` |  |  |  |
| 29 | `PPPFD.CrditIBANAccNumber` | `PorPaymentflowdetails_Crditibanaccnumber` |  |  |  |
| 30 | `PPPFD.BillingIndicator` | `PorPaymentflowdetails_Billingindicator` |  |  |  |
| 31 | `PPPFD.ServiceTypeIdentifier` | `PorPaymentflowdetails_Servicetypeidentifier` |  |  |  |
| 32 | `PPPFD.OrderEntryID` | `PorPaymentflowdetails_Orderentryid` |  |  |  |
| 33 | `PPPFD.ReturnPaymentReference` | `PorPaymentflowdetails_Returnpaymentreference` |  |  |  |
| 34 | `PPPFD.SimulatedPaymentFlag` | `PorPaymentflowdetails_Simulatedpaymentflag` |  |  |  |
| 35 | `PPPFD.IndicativeRate` | `PorPaymentflowdetails_Indicativerate` |  |  |  |
| 36 | `PPPFD.EbDuplicateTypeId` | `PorPaymentflowdetails_Ebduplicatetypeid` |  |  |  |
| 37 | `PPPFD.PaymentMethod` | `PorPaymentflowdetails_Paymentmethod` |  |  |  |
| 38 | `PPPFD.InstAcceptDateTime` | `PorPaymentflowdetails_Instacceptdatetime` |  |  |  |
| 39 | `PPPFD.RepairReasonCode` | `PorPaymentflowdetails_Repairreasoncode` |  |  |  |
| 40 | `PPPFD.ClearingStatusMessageType` | `PorPaymentflowdetails_Clearingstatusmessagetype` |  |  |  |
| 41 | `PPPFD.ClearingInvestigationMsgType` | `PorPaymentflowdetails_Clearinginvestigationmsgtype` |  |  |  |
| 42 | `PPPFD.InvestigationRetryTimeAndCount` | `PorPaymentflowdetails_Investigationretrytimeandcount` |  |  |  |
| 43 | `PPPFD.BeneficiaryId` | `PorPaymentflowdetails_Beneficiaryid` |  |  |  |
| 44 | `PPPFD.CompanyNCC` | `PorPaymentflowdetails_Companyncc` |  |  |  |
| 45 | `PPPFD.ChequeStatus` | `PorPaymentflowdetails_Chequestatus` |  |  |  |
| 46 | `PPPFD.ManuallyVerified` | `PorPaymentflowdetails_Manuallyverified` |  |  |  |
| 47 | `PPPFD.PreviewReferenceCov` | `PorPaymentflowdetails_Previewreferencecov` |  |  |  |
| 48 | `PPPFD.PreviewReference210` | `PorPaymentflowdetails_Previewreference210` |  |  |  |
| 49 | `PPPFD.BeneficiaryPartyTagOption` | `PorPaymentflowdetails_Beneficiarypartytagoption` |  |  |  |
