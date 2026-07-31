# FISTLN.KELA.TRANSACTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.FISTLN.KELA.TRANSACTION.DETAILS` in `FISTLN_LoansOrigination.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `KELA.TRANSACTION.ARRANGEMENT.ID` | `FistlnKelaTransactionDetails_ArrangementId` | TField |  | This field stores Arrangement id of the Student Loan |
| 2 | `KELA.TRANSACTION.CUSTOMER.NAME` | `FistlnKelaTransactionDetails_CustomerName` | TField |  | This field stores the name of the customer of the Student Loan |
| 3 | `KELA.TRANSACTION.RESERVATION.REASON` | `FistlnKelaTransactionDetails_ReservationReason` | TField |  | This field stores the reservation reason code of the Student Loan Values: 1 = guarantee reservation 2 = financial institution transfer |
| 4 | `KELA.TRANSACTION.STATUS` | `FistlnKelaTransactionDetails_Status` | TField |  | This field stores the reservation status of the Student Loan |
| 5 | `KELA.TRANSACTION.ACTUAL.RECORD.TYPE` | `FistlnKelaTransactionDetails_ActualRecordType` | TField |  | This field stores the actual record type of the Student Loan Values: V = P = |
| 6 | `KELA.TRANSACTION.CANCELLATION.REASON` | `FistlnKelaTransactionDetails_CancellationReason` | TField |  | This field stores the cancellation reason of the Student Loan |
| 7 | `KELA.TRANSACTION.CANCELLATION.STATUS` | `FistlnKelaTransactionDetails_CancellationStatus` | TField |  |  |
| 8 | `KELA.TRANSACTION.MESSAGE.TYPE` | `FistlnKelaTransactionDetails_MessageType` | TField |  | This field stores the message type of the Student Loan Values: V = Feedback of non-accepted guarantee reservation request T = Guarantee information N = Withdrawal Prohibition |
| 9 | `KELA.TRANSACTION.NEW.PERSONAL.IDENTITY.NUMBER` | `FistlnKelaTransactionDetails_NewPersonalIdentityNumber` | TField |  | This field stores the new personal identity number of the Student Loan |
| 10 | `KELA.TRANSACTION.GUARANTEE.TYPE` | `FistlnKelaTransactionDetails_GuaranteeType` | TField |  | This field stores the guarantee type of the Student Loan Values: V = Bank's successful State guarantee reservation and Kela's withdrawal plan for the reservation R = guarantee information, based on transferring the loan from another bank |
| 11 | `KELA.TRANSACTION.RESERVATION.NUMBER` | `FistlnKelaTransactionDetails_ReservationNumber` | TField |  | This field stores the reservation number of the Student Loan |
| 12 | `KELA.TRANSACTION.TOTAL.AMOUNT.OF.GUARANTEE` | `FistlnKelaTransactionDetails_TotalAmountOfGuarantee` | TField |  | This field stores the total amount of guarantee of the Student Loan |
| 13 | `KELA.TRANSACTION.DRAWDOWNS.LOT.NO` | `FistlnKelaTransactionDetails_DrawdownsLotNo` |  |  |  |
| 14 | `KELA.TRANSACTION.FIRST.WITHDRAWAL.DATE` | `FistlnKelaTransactionDetails_FirstWithdrawalDate` |  |  |  |
| 15 | `KELA.TRANSACTION.AMOUNT.TO.BE.WITHDRAWN` | `FistlnKelaTransactionDetails_AmountToBeWithdrawn` |  |  |  |
| 16 | `KELA.TRANSACTION.LAST.WITHDRAWAL.DATE` | `FistlnKelaTransactionDetails_LastWithdrawalDate` |  |  |  |
| 17 | `KELA.TRANSACTION.DRAWDOWN.TYPE` | `FistlnKelaTransactionDetails_DrawdownType` |  |  |  |
| 18 | `KELA.TRANSACTION.RESERVATION.END.DATE` | `FistlnKelaTransactionDetails_ReservationEndDate` | TField |  | This field stores the reservation end date of the Student Loan |
| 19 | `KELA.TRANSACTION.SPECIAL.REASON` | `FistlnKelaTransactionDetails_SpecialReason` | TField |  | This field stores special decision of the Student Loan |
| 20 | `KELA.TRANSACTION.DECISION.ON.PAPER` | `FistlnKelaTransactionDetails_DecisionOnPaper` | TField |  | This field stores decision on paper of the Student Loan |
| 21 | `KELA.TRANSACTION.REJECTION` | `FistlnKelaTransactionDetails_Rejection` | TField |  | This field stores rejection reason Values: 1 = guarantee has not been granted by Kela 2 = reservation is already in effect for the same bank 3 = reservation is already in effect for another bank 4 = several banks are making reservation 5 = withdrawal prohibition, withdrawal time remaining 6 = reservation must be made as financial institution transfer 7 = reservation cannot be made as financial institution transfer 9 = other reason |
| 22 | `KELA.TRANSACTION.RESERVATION.REJECTION.DETAILS` | `FistlnKelaTransactionDetails_ReservationRejectionDetails` | TField |  |  |
| 23 | `KELA.TRANSACTION.RESERVATION.APPROVED.DATE` | `FistlnKelaTransactionDetails_ReservationApprovedDate` | TField |  | This field stores date on which KELA response is received |
| 24 | `KELA.TRANSACTION.PLAN.CHANGE.DATE` | `FistlnKelaTransactionDetails_PlanChangeDate` | TField |  | This field stores plan change date |
| 25 | `KELA.TRANSACTION.CANCELLATION.DATE` | `FistlnKelaTransactionDetails_CancellationDate` | TField |  |  |
| 26 | `KELA.TRANSACTION.RESERVATION.STATUS` | `FistlnKelaTransactionDetails_ReservationStatus` | TField |  | This field stores the reservation status |
| 27 | `KELA.TRANSACTION.GUARANTEE.MOD.DATE` | `FistlnKelaTransactionDetails_GuaranteeModDate` | TField |  |  |
| 28 | `KELA.TRANSACTION.DISBURSEMENT.PROHIBITION` | `FistlnKelaTransactionDetails_DisbursementProhibition` | TField |  |  |
| 29 | `KELA.TRANSACTION.TRANSFERRED.AMOUNT` | `FistlnKelaTransactionDetails_TransferredAmount` | TField |  |  |
| 30 | `KELA.TRANSACTION.LAST.POSSIBLE.AMDT.DATE` | `FistlnKelaTransactionDetails_LastPossibleAmdtDate` | TField |  |  |
| 31 | `KELA.TRANSACTION.INCREASED.AMOUNT` | `FistlnKelaTransactionDetails_IncreasedAmount` | TField |  |  |
| 32 | `KELA.TRANSACTION.LAST.DISB.DATE.INCR.AMOUNT` | `FistlnKelaTransactionDetails_LastDisbDateIncrAmount` | TField |  |  |
| 33 | `KELA.TRANSACTION.RESERVED.8` | `FistlnKelaTransactionDetails_Reserved8` | TField |  |  |
| 34 | `KELA.TRANSACTION.RESERVED.7` | `FistlnKelaTransactionDetails_Reserved7` | TField |  |  |
| 35 | `KELA.TRANSACTION.RESERVED.6` | `FistlnKelaTransactionDetails_Reserved6` | TField |  |  |
| 36 | `KELA.TRANSACTION.RESERVED.5` | `FistlnKelaTransactionDetails_Reserved5` | TField |  |  |
| 37 | `KELA.TRANSACTION.RESERVED.4` | `FistlnKelaTransactionDetails_Reserved4` | TField |  |  |
| 38 | `KELA.TRANSACTION.RESERVED.3` | `FistlnKelaTransactionDetails_Reserved3` | TField |  |  |
| 39 | `KELA.TRANSACTION.RESERVED.2` | `FistlnKelaTransactionDetails_Reserved2` | TField |  |  |
| 40 | `KELA.TRANSACTION.RESERVED.1` | `FistlnKelaTransactionDetails_Reserved1` | TField |  |  |
| 41 | `KELA.TRANSACTION.LOCAL.REF` | `FistlnKelaTransactionDetails_LocalRef` |  |  |  |
| 42 | `KELA.TRANSACTION.OVERRIDE` | `FistlnKelaTransactionDetails_Override` |  |  |  |
| 43 | `KELA.TRANSACTION.RECORD.STATUS` | `FistlnKelaTransactionDetails_RecordStatus` | String |  |  |
| 44 | `KELA.TRANSACTION.CURR.NO` | `FistlnKelaTransactionDetails_CurrNo` | String |  |  |
| 45 | `KELA.TRANSACTION.INPUTTER` | `FistlnKelaTransactionDetails_Inputter` |  |  |  |
| 46 | `KELA.TRANSACTION.DATE.TIME` | `FistlnKelaTransactionDetails_DateTime` |  |  |  |
| 47 | `KELA.TRANSACTION.AUTHORISER` | `FistlnKelaTransactionDetails_Authoriser` | String |  |  |
| 48 | `KELA.TRANSACTION.CO.CODE` | `FistlnKelaTransactionDetails_CoCode` | String |  |  |
| 49 | `KELA.TRANSACTION.DEPT.CODE` | `FistlnKelaTransactionDetails_DeptCode` | String |  |  |
| 50 | `KELA.TRANSACTION.AUDITOR.CODE` | `FistlnKelaTransactionDetails_AuditorCode` | String |  |  |
| 51 | `KELA.TRANSACTION.AUDIT.DATE.TIME` | `FistlnKelaTransactionDetails_AuditDateTime` | String |  |  |
