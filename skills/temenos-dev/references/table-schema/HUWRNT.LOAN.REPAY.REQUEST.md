# HUWRNT.LOAN.REPAY.REQUEST — Table Schema

> Source: `INSERTS/I_F.HUWRNT.LOAN.REPAY.REQUEST` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWLRR.QUEUE.REFERENCE` | `HuwrntLoanRepayRequest_QueueReference` | TField |  | Unique Reference Number given by EQ. Requests are differentiated for same settlement account number based on Unique Reference Number for various due date amount(s) |
| 2 | `HUWLRR.REQUEST.TYPE` | `HuwrntLoanRepayRequest_RequestType` | TField |  | Message type sent by EQ. |
| 3 | `HUWLRR.CUSTOMER.ID` | `HuwrntLoanRepayRequest_CustomerId` | TField |  | Specifies the customer ID as in EQ. |
| 4 | `HUWLRR.REQUEST.DATE` | `HuwrntLoanRepayRequest_RequestDate` | TField |  | Date and Time of message request sent by EQ. |
| 5 | `HUWLRR.REQUEST.CURRENCY` | `HuwrntLoanRepayRequest_RequestCurrency` | TField |  | Currency of requested amount. It will be same as currency of settlement account. |
| 6 | `HUWLRR.REQUEST.AMOUNT` | `HuwrntLoanRepayRequest_RequestAmount` | TField |  | Requested Amount for loans from settlement account sent by EQ. |
| 7 | `HUWLRR.REQUEST.VALUE.DATE` | `HuwrntLoanRepayRequest_RequestValueDate` | TField |  | Value date of request sent by EQ. For scheduled repayments this will be same as REQ.DATE.TIME. For repayment requests pertaining to DIP transactions, this field will hold the date for which credits happened in account(s) where value date = date in this field should be grouped and sent as balance confirmed to EQ. |
| 8 | `HUWLRR.QUEUE.UPDATE` | `HuwrntLoanRepayRequest_QueueUpdate` | TField |  | Whether queue should be maintained or not. Default will be Y. No validations will be performed against this field. However data in the form of Y or N will be sent by EQ. |
| 9 | `HUWLRR.FUND.REQUEST.TYPE` | `HuwrntLoanRepayRequest_FundRequestType` | TField |  | Fund Request Type sent by EQ. |
| 10 | `HUWLRR.BALANCE.RESPONSE.STATUS` | `HuwrntLoanRepayRequest_BalanceResponseStatus` | TField |  | This field will be updated by system as records are processed. |
| 11 | `HUWLRR.BOOKING.RESPONSE.STATUS` | `HuwrntLoanRepayRequest_BookingResponseStatus` | TField |  | This field will hold values from WARRANT.STATUS and will be updated by system as records are processed. |
| 12 | `HUWLRR.UPDATE.RESPONSE.STATUS` | `HuwrntLoanRepayRequest_UpdateResponseStatus` | TField |  | This field will hold values from WARRANT.STATUS and will be updated by system as records are processed. |
| 13 | `HUWLRR.REJECTION.REASON` | `HuwrntLoanRepayRequest_RejectionReason` |  |  |  |
| 14 | `HUWLRR.BOOKING.REQUEST.AMOUNT` | `HuwrntLoanRepayRequest_BookingRequestAmount` | TField |  | This field will hold booking request amount as sent by EQ. The amount in this field will be validated against CONFIRMED.AMOUNT, which was sent to EQ as part of balance confirmation(M � BOOKING REQUEST) |
| 15 | `HUWLRR.CONFIRMED.AMOUNT` | `HuwrntLoanRepayRequest_ConfirmedAmount` | TField |  | Balance amount as confirmed by T24 against EQ booking request. This amount will be typically locked in settlement and / or extended account(s) |
| 16 | `HUWLRR.UPDATE.REQUEST.AMOUNT` | `HuwrntLoanRepayRequest_UpdateRequestAmount` | TField |  | This field will hold update request amount sent by EQ. This amount sent as part of UPDATE REQUEST will be new queued amount. (M � BOOKING REQUEST) |
| 17 | `HUWLRR.NARRATIVE` | `HuwrntLoanRepayRequest_Narrative` |  |  |  |
| 18 | `HUWLRR.STMT.NOS` | `HuwrntLoanRepayRequest_StmtNos` |  |  |  |
| 19 | `HUWLRR.LOAN.ID` | `HuwrntLoanRepayRequest_LoanId` |  |  |  |
| 20 | `HUWLRR.LOAN.COMPONENT` | `HuwrntLoanRepayRequest_LoanComponent` |  |  |  |
| 21 | `HUWLRR.COMPONENT.AMOUNT` | `HuwrntLoanRepayRequest_ComponentAmount` |  |  |  |
| 22 | `HUWLRR.RESERVED.11` | `HuwrntLoanRepayRequest_Reserved11` | TField |  | Reserved for future use. |
| 23 | `HUWLRR.RESERVED.10` | `HuwrntLoanRepayRequest_Reserved10` | TField |  | Reserved for future use. |
| 24 | `HUWLRR.RESERVED.9` | `HuwrntLoanRepayRequest_Reserved9` | TField |  | Reserved for future use. |
| 25 | `HUWLRR.RESERVED.8` | `HuwrntLoanRepayRequest_Reserved8` | TField |  | Reserved for future use. |
| 26 | `HUWLRR.RESERVED.7` | `HuwrntLoanRepayRequest_Reserved7` | TField |  | Reserved for future use. |
| 27 | `HUWLRR.RESERVED.6` | `HuwrntLoanRepayRequest_Reserved6` | TField |  | Reserved for future use. |
| 28 | `HUWLRR.RESERVED.5` | `HuwrntLoanRepayRequest_Reserved5` | TField |  | Reserved for future use. |
| 29 | `HUWLRR.RESERVED.4` | `HuwrntLoanRepayRequest_Reserved4` | TField |  | Reserved for future use. |
| 30 | `HUWLRR.RESERVED.3` | `HuwrntLoanRepayRequest_Reserved3` | TField |  | Reserved for future use. |
| 31 | `HUWLRR.RESERVED.2` | `HuwrntLoanRepayRequest_Reserved2` | TField |  | Reserved for future use. |
| 32 | `HUWLRR.RESERVED.1` | `HuwrntLoanRepayRequest_Reserved1` | TField |  | Reserved for future use. |
| 33 | `HUWLRR.LOCAL.REF` | `HuwrntLoanRepayRequest_LocalRef` |  |  |  |
| 34 | `HUWLRR.OVERRIDE` | `HuwrntLoanRepayRequest_Override` |  |  |  |
| 35 | `HUWLRR.RECORD.STATUS` | `HuwrntLoanRepayRequest_RecordStatus` | String |  |  |
| 36 | `HUWLRR.CURR.NO` | `HuwrntLoanRepayRequest_CurrNo` | String |  |  |
| 37 | `HUWLRR.INPUTTER` | `HuwrntLoanRepayRequest_Inputter` |  |  |  |
| 38 | `HUWLRR.DATE.TIME` | `HuwrntLoanRepayRequest_DateTime` |  |  |  |
| 39 | `HUWLRR.AUTHORISER` | `HuwrntLoanRepayRequest_Authoriser` | String |  |  |
| 40 | `HUWLRR.CO.CODE` | `HuwrntLoanRepayRequest_CoCode` | String |  |  |
| 41 | `HUWLRR.DEPT.CODE` | `HuwrntLoanRepayRequest_DeptCode` | String |  |  |
| 42 | `HUWLRR.AUDITOR.CODE` | `HuwrntLoanRepayRequest_AuditorCode` | String |  |  |
| 43 | `HUWLRR.AUDIT.DATE.TIME` | `HuwrntLoanRepayRequest_AuditDateTime` | String |  |  |
| 44 | `HUWLRR.LOAN.NARRATIVE1` | `HuwrntLoanRepayRequest_LoanNarrative1` |  |  |  |
| 45 | `HUWLRR.LOAN.NARRATIVE2` | `HuwrntLoanRepayRequest_LoanNarrative2` |  |  |  |
| 46 | `HUWLRR.LOAN.NARRATIVE3` | `HuwrntLoanRepayRequest_LoanNarrative3` |  |  |  |
| 47 | `HUWLRR.LOAN.NARRATIVE4` | `HuwrntLoanRepayRequest_LoanNarrative4` |  |  |  |
