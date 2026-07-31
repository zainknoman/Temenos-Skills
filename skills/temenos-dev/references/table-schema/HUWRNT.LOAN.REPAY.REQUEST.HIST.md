# HUWRNT.LOAN.REPAY.REQUEST.HIST — Table Schema

> Source: `INSERTS/I_F.HUWRNT.LOAN.REPAY.REQUEST.HIST` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWLRRH.QUEUE.REFERENCE` | `HuwrntLoanRepayRequestHist_QueueReference` | TField |  | Unique Reference Number given by EQ. Requests are differentiated for same settlement account number based on Unique Reference Number for various due date amount(s) |
| 2 | `HUWLRRH.REQUEST.TYPE` | `HuwrntLoanRepayRequestHist_RequestType` | TField |  | Message type sent by EQ. |
| 3 | `HUWLRRH.CUSTOMER.ID` | `HuwrntLoanRepayRequestHist_CustomerId` | TField |  | Specifies the customer ID as in EQ. |
| 4 | `HUWLRRH.REQUEST.DATE` | `HuwrntLoanRepayRequestHist_RequestDate` | TField |  | Date and Time of message request sent by EQ. |
| 5 | `HUWLRRH.REQUEST.CURRENCY` | `HuwrntLoanRepayRequestHist_RequestCurrency` | TField |  | Currency of requested amount. It will be same as currency of settlement account. |
| 6 | `HUWLRRH.REQUEST.AMOUNT` | `HuwrntLoanRepayRequestHist_RequestAmount` | TField |  | Requested Amount for loans from settlement account sent by EQ. |
| 7 | `HUWLRRH.REQUEST.VALUE.DATE` | `HuwrntLoanRepayRequestHist_RequestValueDate` | TField |  | Value date of request sent by EQ. For scheduled repayments this will be same as REQ.DATE.TIME. For repayment requests pertaining to DIP transactions, this field will hold the date for which credits happened in account(s) where value date = date in this field should be grouped and sent as balance confirmed to EQ. |
| 8 | `HUWLRRH.QUEUE.UPDATE` | `HuwrntLoanRepayRequestHist_QueueUpdate` | TField |  | Whether queue should be maintained or not. Default will be Y. No validations will be performed against this field. However data in the form of Y or N will be sent by EQ. |
| 9 | `HUWLRRH.FUND.REQUEST.TYPE` | `HuwrntLoanRepayRequestHist_FundRequestType` | TField |  | Fund Request Type sent by EQ. |
| 10 | `HUWLRRH.BALANCE.RESPONSE.STATUS` | `HuwrntLoanRepayRequestHist_BalanceResponseStatus` | TField |  | This field will be updated by system as records are processed. |
| 11 | `HUWLRRH.BOOKING.RESPONSE.STATUS` | `HuwrntLoanRepayRequestHist_BookingResponseStatus` | TField |  | This field will hold values from WARRANT.STATUS and will be updated by system as records are processed. |
| 12 | `HUWLRRH.UPDATE.RESPONSE.STATUS` | `HuwrntLoanRepayRequestHist_UpdateResponseStatus` | TField |  | This field will hold values from WARRANT.STATUS and will be updated by system as records are processed. |
| 13 | `HUWLRRH.REJECTION.REASON` | `HuwrntLoanRepayRequestHist_RejectionReason` |  |  |  |
| 14 | `HUWLRRH.BOOKING.REQUEST.AMOUNT` | `HuwrntLoanRepayRequestHist_BookingRequestAmount` | TField |  | This field will hold booking request amount as sent by EQ. The amount in this field will be validated against CONFIRMED.AMOUNT, which was sent to EQ as part of balance confirmation(M � BOOKING REQUEST) |
| 15 | `HUWLRRH.CONFIRMED.AMOUNT` | `HuwrntLoanRepayRequestHist_ConfirmedAmount` | TField |  | Balance amount as confirmed by T24 against EQ booking request. This amount will be typically locked in settlement and / or extended account(s) |
| 16 | `HUWLRRH.UPDATE.REQUEST.AMOUNT` | `HuwrntLoanRepayRequestHist_UpdateRequestAmount` | TField |  | This field will hold update request amount sent by EQ. This amount sent as part of UPDATE REQUEST will be new queued amount. (M � BOOKING REQUEST) |
| 17 | `HUWLRRH.NARRATIVE` | `HuwrntLoanRepayRequestHist_Narrative` |  |  |  |
| 18 | `HUWLRRH.STMT.NOS` | `HuwrntLoanRepayRequestHist_StmtNos` |  |  |  |
| 19 | `HUWLRRH.LOAN.ID` | `HuwrntLoanRepayRequestHist_LoanId` |  |  |  |
| 20 | `HUWLRRH.LOAN.COMPONENT` | `HuwrntLoanRepayRequestHist_LoanComponent` |  |  |  |
| 21 | `HUWLRRH.COMPONENT.AMOUNT` | `HuwrntLoanRepayRequestHist_ComponentAmount` |  |  |  |
| 22 | `HUWLRRH.RESERVED.11` | `HuwrntLoanRepayRequestHist_Reserved11` | TField |  | Reserved for future use. |
| 23 | `HUWLRRH.RESERVED.10` | `HuwrntLoanRepayRequestHist_Reserved10` | TField |  | Reserved for future use. |
| 24 | `HUWLRRH.RESERVED.9` | `HuwrntLoanRepayRequestHist_Reserved9` | TField |  | Reserved for future use. |
| 25 | `HUWLRRH.RESERVED.8` | `HuwrntLoanRepayRequestHist_Reserved8` | TField |  | Reserved for future use. |
| 26 | `HUWLRRH.RESERVED.7` | `HuwrntLoanRepayRequestHist_Reserved7` | TField |  | Reserved for future use. |
| 27 | `HUWLRRH.RESERVED.6` | `HuwrntLoanRepayRequestHist_Reserved6` | TField |  | Reserved for future use. |
| 28 | `HUWLRRH.RESERVED.5` | `HuwrntLoanRepayRequestHist_Reserved5` | TField |  | Reserved for future use. |
| 29 | `HUWLRRH.RESERVED.4` | `HuwrntLoanRepayRequestHist_Reserved4` | TField |  | Reserved for future use. |
| 30 | `HUWLRRH.RESERVED.3` | `HuwrntLoanRepayRequestHist_Reserved3` | TField |  | Reserved for future use. |
| 31 | `HUWLRRH.RESERVED.2` | `HuwrntLoanRepayRequestHist_Reserved2` | TField |  | Reserved for future use. |
| 32 | `HUWLRRH.RESERVED.1` | `HuwrntLoanRepayRequestHist_Reserved1` | TField |  | Reserved for future use. |
| 33 | `HUWLRRH.LOCAL.REF` | `HuwrntLoanRepayRequestHist_LocalRef` |  |  |  |
| 34 | `HUWLRRH.OVERRIDE` | `HuwrntLoanRepayRequestHist_Override` |  |  |  |
| 35 | `HUWLRRH.RECORD.STATUS` | `HuwrntLoanRepayRequestHist_RecordStatus` | String |  |  |
| 36 | `HUWLRRH.CURR.NO` | `HuwrntLoanRepayRequestHist_CurrNo` | String |  |  |
| 37 | `HUWLRRH.INPUTTER` | `HuwrntLoanRepayRequestHist_Inputter` |  |  |  |
| 38 | `HUWLRRH.DATE.TIME` | `HuwrntLoanRepayRequestHist_DateTime` |  |  |  |
| 39 | `HUWLRRH.AUTHORISER` | `HuwrntLoanRepayRequestHist_Authoriser` | String |  |  |
| 40 | `HUWLRRH.CO.CODE` | `HuwrntLoanRepayRequestHist_CoCode` | String |  |  |
| 41 | `HUWLRRH.DEPT.CODE` | `HuwrntLoanRepayRequestHist_DeptCode` | String |  |  |
| 42 | `HUWLRRH.AUDITOR.CODE` | `HuwrntLoanRepayRequestHist_AuditorCode` | String |  |  |
| 43 | `HUWLRRH.AUDIT.DATE.TIME` | `HuwrntLoanRepayRequestHist_AuditDateTime` | String |  |  |
| 44 | `HUWLRRH.LOAN.NARRATIVE1` | `HuwrntLoanRepayRequestHist_LoanNarrative1` |  |  |  |
| 45 | `HUWLRRH.LOAN.NARRATIVE2` | `HuwrntLoanRepayRequestHist_LoanNarrative2` |  |  |  |
| 46 | `HUWLRRH.LOAN.NARRATIVE3` | `HuwrntLoanRepayRequestHist_LoanNarrative3` |  |  |  |
| 47 | `HUWLRRH.LOAN.NARRATIVE4` | `HuwrntLoanRepayRequestHist_LoanNarrative4` |  |  |  |
