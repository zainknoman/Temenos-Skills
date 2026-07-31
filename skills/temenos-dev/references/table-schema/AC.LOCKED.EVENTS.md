# AC.LOCKED.EVENTS — Table Schema

> Source: `INSERTS/I_F.AC.LOCKED.EVENTS` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.LCK.ACCOUNT.NUMBER` | `AcLockedEvents_AccountNumber` | TField | Yes | Identifies the Account on which funds are to be blocked (reserved). Validation Rules: Valid Standard numeric Account Number - Mandatory input |
| 2 | `AC.LCK.DESCRIPTION` | `AcLockedEvents_Description` | TField | No | A free format field, that should be meaningful to the user. Validation Rules: Up to 35 Characters for free format text. Optional input |
| 3 | `AC.LCK.FROM.DATE` | `AcLockedEvents_FromDate` | TField |  | The date that the LOCKED.AMOUNT will start. If this date is backdated the balance will only be checked from the system date, although the LOCKED.EVENTS ladder in ACCOUNT will be built from this date. If no date is input then the field will default to the system date (today&amp;#8217;s date). Validation Rules: Standard T24 date field |
| 4 | `AC.LCK.TO.DATE` | `AcLockedEvents_ToDate` | TField | No | The date the LOCKED.AMOUNT will end. The LOCKED.AMOUNT will be cleared from the account during the next &amp;#8216;start of day&amp;#8217; following the TO.DATE. If left blank then the event will have no end date. Validation Rules: Standard T24 date field Optional input |
| 5 | `AC.LCK.LOCKED.AMOUNT` | `AcLockedEvents_LockedAmount` | TField | Yes | The amount of funds that will be reserved for the period entered into the FROM.DATE to TO.DATE fields . If the balance of the account falls below this during the period (or is below this amount when the event is entered) then an override will be generated warning the user that the balance of the account is below the LOCKED.AMOUNT . It should be noted that the override ONLY displays that the account has fallen below the LOCKED.AMOUNT and not the actual amount that the account is below. So, for example, if you have a LOCKED.AMOUNT for 10,000.00 and if the account has a balance of 100 or 9,999.00 then the same override will be displayed . Whether the balance checked is WORKING.BALANCE or AVAILABLE.BALANCE depends upon the input into field CREDIT.CHECK on ACCOUNT , ACCOUNT.GENERAL.CONDITIONS, SEC.ACC.MASTER or ACCOUNT.PARAMETER. Validation Rules: 1-14 type AMT (standard amount format) characters plus a decimal point. - Mandatory input. The amount must be greater than Zero. |
| 6 | `AC.LCK.LOCAL.REF` | `AcLockedEvents_LocalRef` |  |  |  |
| 7 | `AC.LCK.RC.RETRY` | `AcLockedEvents_RcRetry` | TField | No | The 'YES' or 'NO' field To decide if a blocked funds transaction should be captured by RC framework and retried on pre-defined frequency or not The value once entered in this field cannot be changed When 'YES' This block on account would be handed over to RC framework and retried on pre-defined frequency This AC.LOCKED.EVENTS can be reversed and in turn in the corresponding RC.DETAIL record set STATUS = "TERMINATED", END.DATE='TODAY' and NEXT.RETRY.DATE= 'TODAY' During that day's COB, the corresponding RC.DETAIL is moved for tidyup processing and tidyup would either moved to history or delete the record as per condition When 'NO' This block on account would not be handed over to RC framework This field is optional |
| 8 | `AC.LCK.RC.DETAIL.ID` | `AcLockedEvents_RcDetailId` | TField |  |  |
| 9 | `AC.LCK.BLOCK.PRIORITY` | `AcLockedEvents_BlockPriority` | TField |  | Field to specify the priority of blocks Recycler while processing more than one blocked funds against a settlement account, would check this filed against the RC.PRIORITY setting and decide the priority of processing This field is user inputtable only when RC.RETRY field is set to 'YES' This field is not inputtable when RC.RETRY field is set to 'NO' This should be a valid id in EB.SYSTEM.ID table and must begin with either 'AC' or 'RC', otherwise throw validation error |
| 10 | `AC.LCK.TRANS.REF` | `AcLockedEvents_TransRef` | TField |  |  |
| 11 | `AC.LCK.PAYMENT.AMT` | `AcLockedEvents_PaymentAmt` | TField |  |  |
| 12 | `AC.LCK.PAYMENT.CCY` | `AcLockedEvents_PaymentCcy` | TField |  |  |
| 13 | `AC.LCK.ADD.DETAIL.REQ.SOURCE` | `AcLockedEvents_AddDetailReqSource` | TField | No | Store additional details request source from clearing Up to 65 Characters This field is optional This field is user inputtable field, and also updated on the clearing process |
| 14 | `AC.LCK.RESERVE.ALT.KEY` | `AcLockedEvents_ReserveAltKey` | TField | No | Alternate key for referring the record Up to 65 Characters This field is optional This field is user inputtable field |
| 15 | `AC.LCK.LOCKED.TYPE` | `AcLockedEvents_LockedType` | TField |  | The type of locked funds Must be a valid AC.LOCKED.EVENT.TYPE No change field |
| 16 | `AC.LCK.ACCOUNT.LINK` | `AcLockedEvents_AccountLink` | TField |  | Identifies if the locked amount must be applied to the single account or to all the accounts in the hierarchy Default from AC.LOCKED.EVENT.TYPE record No Input field |
| 17 | `AC.LCK.OVERRIDE` | `AcLockedEvents_Override` |  |  |  |
| 18 | `AC.LCK.RECORD.STATUS` | `AcLockedEvents_RecordStatus` | String |  |  |
| 19 | `AC.LCK.CURR.NO` | `AcLockedEvents_CurrNo` | String |  |  |
| 20 | `AC.LCK.INPUTTER` | `AcLockedEvents_Inputter` |  |  |  |
| 21 | `AC.LCK.DATE.TIME` | `AcLockedEvents_DateTime` |  |  |  |
| 22 | `AC.LCK.AUTHORISER` | `AcLockedEvents_Authoriser` | String |  |  |
| 23 | `AC.LCK.CO.CODE` | `AcLockedEvents_CoCode` | String |  |  |
| 24 | `AC.LCK.DEPT.CODE` | `AcLockedEvents_DeptCode` | String |  |  |
| 25 | `AC.LCK.AUDITOR.CODE` | `AcLockedEvents_AuditorCode` | String |  |  |
| 26 | `AC.LCK.AUDIT.DATE.TIME` | `AcLockedEvents_AuditDateTime` | String |  |  |
| 27 | `AC.LCK.LINK.STATUS` | `AcLockedEvents_LinkStatus` | TField |  |  |
| 28 | `AC.LCK.TXN.SIGN` | `AcLockedEvents_TxnSign` | TField |  | Identifies the type of reservation. Either DR for debit or CR for credit. No Input field Reserved for future use |
| 29 | `AC.LCK.FA.STATUS` | `AcLockedEvents_FaStatus` | TField |  | Used to identify the reservations from the FA Micro service No Input field Extern field Reserved for future use |
| 30 | `AC.LCK.RESERVATION.ID` | `AcLockedEvents_ReservationId` | TField |  | The unique identifier of the authorisation or a series of authorisations. In case of clearing this will be the value of RESERVATION.KEY data item passed in the string. NOCHANGE field Up to 65 Characters. |
| 31 | `AC.LCK.JOURNAL.ID` | `AcLockedEvents_JournalId` | TField |  | The unique identifier of the incremental authorisation. In case of clearing this will be the value of JOURNAL.ID data item passed in the string. NOCHANGE field Up to 35 Characters. |
| 32 | `AC.LCK.MERCHANT.FLAG` | `AcLockedEvents_MerchantFlag` | TField |  | Identifies if a reservation is flagged as merchant return type. Value defaulted from TRANSACTION table for the correspondent value in TRANSACTION.CODE field |
| 33 | `AC.LCK.TRANSACTION.CODE` | `AcLockedEvents_TransactionCode` | TField |  | Identifies the type of transaction the reservation is for. Validation Rules: Must be valid record in TRANSACTION table |
| 34 | `AC.LCK.FUNDS.APPROVED` | `AcLockedEvents_FundsApproved` | TField |  | When a clearing reservation request is suspended and moved to manual approval to bank user, based on bank user�s decision i.e. when approved the AC.LOCKED.EVENTS will be created. For the AC.LOCKED.EVENTS created through manual approval, this field will be updated with value as YES. NOINPUT field. Allowed values are YES / NULL. YES � Funds block created post approving the manual request. NULL - No funds blocking via ACFA. |
