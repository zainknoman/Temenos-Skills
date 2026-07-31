# AC.FUNDS.AUTHORISATION — Table Schema

> Source: `INSERTS/I_F.AC.FUNDS.AUTHORISATION` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFA.DEBIT.ACCOUNT` | `AcFundsAuthorisation_DebitAccount` | TField | Yes | Contains the account number to be debited. Validation Rules: No change field Mandatory field It has to be a valid record in ACCOUNT table |
| 2 | `ACFA.ACCOUNT.CCY` | `AcFundsAuthorisation_AccountCcy` | TField | Yes | Currency code of the account defaulted for specified debit account. Validation Rules: No Input field Mandatory field It has to be a valid record in CURRENCY table |
| 3 | `ACFA.REQUESTED.CCY` | `AcFundsAuthorisation_RequestedCcy` | TField | Yes | The currency the amount is requested in. Validation Rules: No change field Mandatory field It has to be a valid record in CURRENCY table |
| 4 | `ACFA.REQUESTED.AMT` | `AcFundsAuthorisation_RequestedAmt` | TField | Yes | Amount requested in REQUESTED.CCY. Validation Rules: No change field Mandatory field |
| 5 | `ACFA.REQUEST.DATE` | `AcFundsAuthorisation_RequestDate` | TField |  | The date on which the request was created. Validation Rules: No Change Field |
| 6 | `ACFA.DDA.INIT.REQ.DATE` | `AcFundsAuthorisation_DdaInitReqDate` | TField |  | System date in T24 DDA system when request was created. Validation Rules: No Input Field |
| 7 | `ACFA.DDA.INIT.REQ.TIME` | `AcFundsAuthorisation_DdaInitReqTime` | TField |  | Time in the T24 DDA system that the request was created. Validation Rules: No Input Field |
| 8 | `ACFA.ORIG.SYS.DATE` | `AcFundsAuthorisation_OrigSysDate` | TField | Yes | The date of the external system from which the request originated. Mandatory field in case the request is payment engine generated. |
| 9 | `ACFA.ORIG.SYS.TIME` | `AcFundsAuthorisation_OrigSysTime` | TField | Yes | The time that the request was created by the originating system. Mandatory field in case the request is payment engine generated. |
| 10 | `ACFA.ORIG.TRANS.REF` | `AcFundsAuthorisation_OrigTransRef` | TField | Yes | Transaction reference from the external system (i.e. the payment reference). Mandatory field in case the request is payment engine generated. If ORIG.TRANS.REF is present then reversal. |
| 11 | `ACFA.ORIG.TRANS.COMPANY` | `AcFundsAuthorisation_OrigTransCompany` | TField | Yes | Transaction processing company mnemonic. Mandatory field in case the request is payment engine generated. |
| 12 | `ACFA.LAST.RETRY.DATE` | `AcFundsAuthorisation_LastRetryDate` | TField |  | The date in the DDA system that the request was last retried automatically. Validation Rules: No Input Field |
| 13 | `ACFA.LAST.RETRY.TIME` | `AcFundsAuthorisation_LastRetryTime` | TField |  | The last time in the DDA system that the request was retried automatically. Validation Rules: No Input Field |
| 14 | `ACFA.RETRY.NUMBER` | `AcFundsAuthorisation_RetryNumber` | TField |  | The count of the number of times the request has been retried. Validation Rules: No Input Field |
| 15 | `ACFA.FUNDS.DECISION` | `AcFundsAuthorisation_FundsDecision` | TField | Yes | Contains the approval decision entered by the CAO. This field will be null initially and when picked by an user will be defaulted as "APPROVED"or "REJECTED" depending on funds available for debit amount in the account when displayed through enquiry. The option Approved-Partial indicates only partial amount of the requested funds is approved. Validation Rules: Mandatory field with options APPROVED or REJECTED or PRE-APPROVED or APPROVED-PARTIAL If originating transaction reference is present then 'PRE-APPROVED' decision not accepted If originating transaction reference is not present then 'APPROVED' decision not accepted 'Approved Partial' Status is restricted to funds request authorised by Recycler and is not applicable for Manual Funds (User) Authorisation. |
| 16 | `ACFA.DECISION.REASON` | `AcFundsAuthorisation_DecisionReason` |  |  |  |
| 17 | `ACFA.FUNDS.AUTH.STATUS` | `AcFundsAuthorisation_FundsAuthStatus` | TField |  | Contains the status of the request based on which level of authorisation, the request has gone through in its lifecycle. Value will be Defaulted as "CREATED" when the request is initiated "UNAUTHORISED" when the request is opened like when amendments are to be made "AUTHORISED" when request is authorized "BOOKED" when the posting for reservation amount is completed "CANCELLED"when the request is cancelled either manually or because of request initiated from external system. "Authorised-Partial"" indicates only partial amount of the requested funds is authorised. Validation Rules: No Input Field |
| 18 | `ACFA.RESERVATION.ID` | `AcFundsAuthorisation_ReservationId` | TField |  | It holds the ID of AC.LOCKED.EVENTS record. Validation Rules: No Input Field |
| 19 | `ACFA.RESERVATION.KEY` | `AcFundsAuthorisation_ReservationKey` | TField |  | It holds the ACFA reference ID. Validation Rules: No Input Field |
| 20 | `ACFA.REQUEST.SOURCE` | `AcFundsAuthorisation_RequestSource` | TField |  | The source product making the funds request. For Non Sufficient Funds processing exception records this field will hold value as 'AC' Validation Rules: No Input Field |
| 21 | `ACFA.REQUEST.CODE` | `AcFundsAuthorisation_RequestCode` | TField |  | Identifies the type of request. Linked to EB.LOOKUP this is the code passed to AC.FUNDS.AUTHORISATION by the calling system. For Non Sufficient Funds processing exception records this field will hold value as 'NSF' Validation Rules: Must have a valid code set up in EB.LOOKUP. No Input Field |
| 22 | `ACFA.REQUEST.DESC` | `AcFundsAuthorisation_RequestDesc` | TField |  | Description passed by the calling system describing the reason the request needs to be handled manually. Validation Rules: No Input Field |
| 23 | `ACFA.APPROVAL.CODE` | `AcFundsAuthorisation_ApprovalCode` | TField |  |  |
| 24 | `ACFA.SIGN` | `AcFundsAuthorisation_Sign` | TField |  | Indicates the sign of the transaction. Values can be Credit/Debit. Default is Debit. Currently only Debit supported. Validation Rules: No Input Field |
| 25 | `ACFA.SET.TYPE.OR.ORIG.DEC` | `AcFundsAuthorisation_SetTypeOrOrigDec` | TField |  | Indicates the original decision for which the AC.FUNDS.AUTHORISATION was created. PTL - Applicable for Non Sufficient Funds exception, represent underlying Debit transaction to the account was paid through the limit available at the time of transaction. POL - Applicable for Non Sufficient Funds exception, represent underlying Debit transaction to the account was paid in excess of the limit available at the time of transaction SET - Applicable for Non Sufficient Funds exception, represent underlying Debit transaction to the account was settled irrespective of account or limit balance available at the time of transaction SET - Applicable for Transaction Stop Processing, When all REL.DECISION values is Pay. Entries for the transaction are generated. REJ - Applicable for Transaction Stop Processing, When atleast one of the REL.DECISION value is Return.Transaction is stopped. Validation Rules: No Input Field |
| 26 | `ACFA.REL.INSTR.ID` | `AcFundsAuthorisation_RelInstrId` |  |  |  |
| 27 | `ACFA.REL.DECISION` | `AcFundsAuthorisation_RelDecision` |  |  |  |
| 28 | `ACFA.OD.AMT` | `AcFundsAuthorisation_OdAmt` | TField |  | Applicable for Non Sufficient Funds exception, Represents the overdrawn amount on account during the creation of the exception record Validation Rules: No Input Field |
| 29 | `ACFA.CHG.WAIVED` | `AcFundsAuthorisation_ChgWaived` | TField |  | Applicable for Non Sufficient Funds exception, Option to waive the Non Sufficient Funds exception charges. Validation Rules: Yes - Charges will be waived, i.e. CHG.AMT field will be defaulted with value as 0 |
| 30 | `ACFA.DEF.CHG.AMT` | `AcFundsAuthorisation_DefChgAmt` | TField |  | Applicable for Non Sufficient Funds exception, System calculated charge amount as applicable for the respective exception record. Validation Rules: No Input Field |
| 31 | `ACFA.CHG.AMT` | `AcFundsAuthorisation_ChgAmt` | TField |  | Applicable for Non Sufficient Funds exception, Represents the final charge amount that will be posted or charged as a result of a Non Sufficient Funds exception Field will be defaulted with DEF.CHG.AMT, which the user can negotiate based on negotiation rule defined in NSF.PARAMETER application for respective settlement type if not an override would be raised. Validation Rules: Should be a valid amount or zero Input Field |
| 32 | `ACFA.CHG.DECISION` | `AcFundsAuthorisation_ChgDecision` | TField |  | Applicable for Non Sufficient Funds exception, Represents if the charge amount was waived by the SYSTEM or by the USER Validation Rules: No Input Field |
| 33 | `ACFA.CHG.WAIVED.REASON` | `AcFundsAuthorisation_ChgWaivedReason` |  |  |  |
| 34 | `ACFA.ORG.AAA.ID` | `AcFundsAuthorisation_OrgAaaId` | TField |  | Applicable for Non Sufficient Funds exception, Holds the reference of Transaction Activity i.e. AA.ARRANGEMENT.ACTIVITY file, which caused the account to be overdrawn resulting in being classified as an exception. Validation Rules: No Input Field. |
| 35 | `ACFA.AAA.FOR.CHG` | `AcFundsAuthorisation_AaaForChg` | TField |  | Applicable for Non Sufficient Funds exception, Holds the reference of Charge Activity i.e. AA.ARRANGEMENT.ACTIVITY file Validation Rules: No Input Field |
| 36 | `ACFA.AAA.CHG.AMT` | `AcFundsAuthorisation_AaaChgAmt` | TField |  |  |
| 37 | `ACFA.CHG.RESV.REF` | `AcFundsAuthorisation_ChgResvRef` | TField |  |  |
| 38 | `ACFA.CHG.RESV.AMT` | `AcFundsAuthorisation_ChgResvAmt` | TField |  |  |
| 39 | `ACFA.REQUEST.TYPE.SUB.TYPE` | `AcFundsAuthorisation_RequestTypeSubType` | TField |  | Applications can pass the request type and sub type in the format REQ.TYPE-SUB.TYPE where REQ.TYPE should be a valid record in EB.SYSTEM.ID though we will have this validation anywhere example PP-SWIFT. Information in this field will be used for matching the RC.CONDITION through RC.CAPTURE application. |
| 40 | `ACFA.CUTOFF.DATE` | `AcFundsAuthorisation_CutoffDate` | TField |  | Applications can pass the valid date, which represents the date until the recycler should retry the pending transaction. |
| 41 | `ACFA.CUTOFF.TIME` | `AcFundsAuthorisation_CutoffTime` | TField |  | Applications can pass the valid time in the format HH:MM (00:00 TO 23:59), which represents the time on the cut off date until which the recycler should retry the pending transaction. |
| 42 | `ACFA.TRANSACTION.CODE` | `AcFundsAuthorisation_TransactionCode` | TField |  |  |
| 43 | `ACFA.AUTH.DATE` | `AcFundsAuthorisation_AuthDate` | TField |  | Date on which AC.FUNDS.AUTHORISATION is authorized. Validation Rule: System maintained field. |
| 44 | `ACFA.LOCAL.REF` | `AcFundsAuthorisation_LocalRef` |  |  |  |
| 45 | `ACFA.OVERRIDE` | `AcFundsAuthorisation_Override` |  |  |  |
| 46 | `ACFA.RECORD.STATUS` | `AcFundsAuthorisation_RecordStatus` | String |  |  |
| 47 | `ACFA.CURR.NO` | `AcFundsAuthorisation_CurrNo` | String |  |  |
| 48 | `ACFA.INPUTTER` | `AcFundsAuthorisation_Inputter` |  |  |  |
| 49 | `ACFA.DATE.TIME` | `AcFundsAuthorisation_DateTime` |  |  |  |
| 50 | `ACFA.AUTHORISER` | `AcFundsAuthorisation_Authoriser` | String |  |  |
| 51 | `ACFA.CO.CODE` | `AcFundsAuthorisation_CoCode` | String |  |  |
| 52 | `ACFA.DEPT.CODE` | `AcFundsAuthorisation_DeptCode` | String |  |  |
| 53 | `ACFA.AUDITOR.CODE` | `AcFundsAuthorisation_AuditorCode` | String |  |  |
| 54 | `ACFA.AUDIT.DATE.TIME` | `AcFundsAuthorisation_AuditDateTime` | String |  |  |
| 55 | `ACFA.RESERVED.AMOUNT` | `AcFundsAuthorisation_ReservedAmount` | TField |  | The fields indicates the partial amount approved for the funds request.. Validation Rules: This field is restricted to input by Recycler and is not applicable for Manual(User) input |
| 56 | `ACFA.ORIGINAL.RESERVATION.ID` | `AcFundsAuthorisation_OriginalReservationId` | TField |  | This field will be used as the alternate reservation Id. This will allow the ACFA to be identified by an alternative reference and will be passed through to update AC.LOCKED.EVENTS. |
