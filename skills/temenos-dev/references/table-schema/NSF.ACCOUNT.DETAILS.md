# NSF.ACCOUNT.DETAILS — Table Schema

> Source: `INSERTS/I_F.NSF.ACCOUNT.DETAILS` in `NSFDES_Queue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NSFACC.ARRANGEMENT.ID` | `NsfAccountDetails_ArrangementId` | TField |  | Arrangement Number |
| 2 | `NSFACC.ACCOUNT.CCY` | `NsfAccountDetails_AccountCcy` | TField |  | Account Currency |
| 3 | `NSFACC.REVIEW.ALL` | `NsfAccountDetails_ReviewAll` | TField |  | Check box to determine is All items are to be marked as Reviewed. This field should be cleared every time a record is opened. If the field is set, the Review Flag in each multi-value set in ACFA records should be set as well. |
| 4 | `NSFACC.REVIEW.FLAG` | `NsfAccountDetails_ReviewFlag` |  |  |  |
| 5 | `NSFACC.ITEM.TYPE` | `NsfAccountDetails_ItemType` |  |  |  |
| 6 | `NSFACC.ACFA.ID` | `NsfAccountDetails_AcfaId` |  |  |  |
| 7 | `NSFACC.REQUEST.CCY` | `NsfAccountDetails_RequestCcy` |  |  |  |
| 8 | `NSFACC.TRANSACTION.AMT` | `NsfAccountDetails_TransactionAmt` |  |  |  |
| 9 | `NSFACC.TXN.NARRATIVE` | `NsfAccountDetails_TxnNarrative` |  |  |  |
| 10 | `NSFACC.OD.AMT` | `NsfAccountDetails_OdAmt` |  |  |  |
| 11 | `NSFACC.PAY.BALANCE` | `NsfAccountDetails_PayBalance` |  |  |  |
| 12 | `NSFACC.INIT.REQ.DATE` | `NsfAccountDetails_InitReqDate` |  |  |  |
| 13 | `NSFACC.INIT.REQ.TIME` | `NsfAccountDetails_InitReqTime` |  |  |  |
| 14 | `NSFACC.REQUEST.DATE` | `NsfAccountDetails_RequestDate` |  |  |  |
| 15 | `NSFACC.ORIG.TRANS.REF` | `NsfAccountDetails_OrigTransRef` |  |  |  |
| 16 | `NSFACC.FUNDS.DECISION` | `NsfAccountDetails_FundsDecision` |  |  |  |
| 17 | `NSFACC.REASON` | `NsfAccountDetails_Reason` |  |  |  |
| 18 | `NSFACC.CLR.CHANNEL` | `NsfAccountDetails_ClrChannel` |  |  |  |
| 19 | `NSFACC.REASON.CODE` | `NsfAccountDetails_ReasonCode` |  |  |  |
| 20 | `NSFACC.WAIVE.CHG` | `NsfAccountDetails_WaiveChg` |  |  |  |
| 21 | `NSFACC.CHG.AMT` | `NsfAccountDetails_ChgAmt` |  |  |  |
| 22 | `NSFACC.ADJ.CHG.AMT` | `NsfAccountDetails_AdjChgAmt` |  |  |  |
| 23 | `NSFACC.CHG.WAIVE.REASON` | `NsfAccountDetails_ChgWaiveReason` |  |  |  |
| 24 | `NSFACC.OFFICER.DECISION` | `NsfAccountDetails_OfficerDecision` |  |  |  |
| 25 | `NSFACC.SETTLEMENT.TYPE` | `NsfAccountDetails_SettlementType` |  |  |  |
| 26 | `NSFACC.FUNDS.AUTH.STATUS` | `NsfAccountDetails_FundsAuthStatus` |  |  |  |
| 27 | `NSFACC.CHARGE.NEGOTIABLE` | `NsfAccountDetails_ChargeNegotiable` |  |  |  |
| 28 | `NSFACC.SETTLEMENT.DECISION` | `NsfAccountDetails_SettlementDecision` |  |  |  |
| 29 | `NSFACC.CHARGE.DECISION` | `NsfAccountDetails_ChargeDecision` |  |  |  |
| 30 | `NSFACC.ORIG.AAA.ID` | `NsfAccountDetails_OrigAaaId` |  |  |  |
| 31 | `NSFACC.CLEARING.ID` | `NsfAccountDetails_ClearingId` |  |  |  |
| 32 | `NSFACC.TXN.SYSTEM.ID` | `NsfAccountDetails_TxnSystemId` |  |  |  |
| 33 | `NSFACC.STMT.ID` | `NsfAccountDetails_StmtId` |  |  |  |
| 34 | `NSFACC.CHEQUE.NUMBER` | `NsfAccountDetails_ChequeNumber` |  |  |  |
| 35 | `NSFACC.TRANSACTION.CODE` | `NsfAccountDetails_TransactionCode` |  |  |  |
| 36 | `NSFACC.RESERVED.29` | `NsfAccountDetails_Reserved29` | TField |  |  |
| 37 | `NSFACC.RESERVED.28` | `NsfAccountDetails_Reserved28` | TField |  |  |
| 38 | `NSFACC.RESERVED.27` | `NsfAccountDetails_Reserved27` | TField |  |  |
| 39 | `NSFACC.RESERVED.26` | `NsfAccountDetails_Reserved26` | TField |  |  |
| 40 | `NSFACC.RESERVED.25` | `NsfAccountDetails_Reserved25` | TField |  |  |
| 41 | `NSFACC.RESERVED.24` | `NsfAccountDetails_Reserved24` | TField |  |  |
| 42 | `NSFACC.RESERVED.23` | `NsfAccountDetails_Reserved23` | TField |  |  |
| 43 | `NSFACC.RESERVED.22` | `NsfAccountDetails_Reserved22` | TField |  |  |
| 44 | `NSFACC.RESERVED.21` | `NsfAccountDetails_Reserved21` | TField |  |  |
| 45 | `NSFACC.DAO.ID` | `NsfAccountDetails_DaoId` |  |  |  |
| 46 | `NSFACC.NSF.DESK.ID` | `NsfAccountDetails_NsfDeskId` | TField |  | ID of NSF Desk where the account belongs.Will be updated based on the NSF desk condition and desk definition available. |
| 47 | `NSFACC.NSF.DATE` | `NsfAccountDetails_NsfDate` | TField |  | System Date when the record is created(COB Date) |
| 48 | `NSFACC.FLOAT.BALANCE` | `NsfAccountDetails_FloatBalance` | TField |  | The uncollected funds available which could be used for clearing the exception. The balance will not displayed separtely if the balance component FLOAT is already included in AC.CREDIT.CHECK for NSF processing |
| 49 | `NSFACC.ACCOUNT.TITLE.1` | `NsfAccountDetails_AccountTitle1` |  |  |  |
| 50 | `NSFACC.CUSTOMER` | `NsfAccountDetails_Customer` |  |  |  |
| 51 | `NSFACC.DE.ADDRESS.ID` | `NsfAccountDetails_DeAddressId` |  |  |  |
| 52 | `NSFACC.EXPIRY.DATE` | `NsfAccountDetails_ExpiryDate` | TField |  | Expiry date of the ACFA record. Expiry date will be Request date from ACFA record plus the expiry days set for the Settlement type in ACFA.TYPE table(L1) |
| 53 | `NSFACC.SUPPRESS.NOTICE` | `NsfAccountDetails_SuppressNotice` | TField |  | Field to indicate if NSF Notice has to be suppressed by external mailing system for the Customer. |
| 54 | `NSFACC.STATEMENT.DATE` | `NsfAccountDetails_StatementDate` | TField |  | Next statement due date for the account |
| 55 | `NSFACC.CUTOFF.COMPLETE` | `NsfAccountDetails_CutoffComplete` | TField |  | Cutoff service indicator |
| 56 | `NSFACC.TOTAL.CHARGE` | `NsfAccountDetails_TotalCharge` | TField |  | sum of all charge amounts |
| 57 | `NSFACC.RESERVED.20` | `NsfAccountDetails_Reserved20` |  |  |  |
| 58 | `NSFACC.RESERVED.19` | `NsfAccountDetails_Reserved19` |  |  |  |
| 59 | `NSFACC.RESERVED.18` | `NsfAccountDetails_Reserved18` |  |  |  |
| 60 | `NSFACC.RESERVED.17` | `NsfAccountDetails_Reserved17` |  |  |  |
| 61 | `NSFACC.RESERVED.16` | `NsfAccountDetails_Reserved16` |  |  |  |
| 62 | `NSFACC.RESERVED.15` | `NsfAccountDetails_Reserved15` |  |  |  |
| 63 | `NSFACC.RESERVED.14` | `NsfAccountDetails_Reserved14` |  |  |  |
| 64 | `NSFACC.RESERVED.13` | `NsfAccountDetails_Reserved13` |  |  |  |
| 65 | `NSFACC.RESERVED.12` | `NsfAccountDetails_Reserved12` |  |  |  |
| 66 | `NSFACC.RESERVED.11` | `NsfAccountDetails_Reserved11` |  |  |  |
| 67 | `NSFACC.RESERVED.10` | `NsfAccountDetails_Reserved10` |  |  |  |
| 68 | `NSFACC.RESERVED.9` | `NsfAccountDetails_Reserved9` |  |  |  |
| 69 | `NSFACC.RESERVED.8` | `NsfAccountDetails_Reserved8` |  |  |  |
| 70 | `NSFACC.RESERVED.7` | `NsfAccountDetails_Reserved7` |  |  |  |
| 71 | `NSFACC.RESERVED.6` | `NsfAccountDetails_Reserved6` |  |  |  |
| 72 | `NSFACC.RESERVED.5` | `NsfAccountDetails_Reserved5` |  |  |  |
| 73 | `NSFACC.RESERVED.4` | `NsfAccountDetails_Reserved4` |  |  |  |
| 74 | `NSFACC.RESERVED.3` | `NsfAccountDetails_Reserved3` |  |  |  |
| 75 | `NSFACC.RESERVED.2` | `NsfAccountDetails_Reserved2` |  |  |  |
| 76 | `NSFACC.RESERVED.1` | `NsfAccountDetails_Reserved1` | TField |  |  |
| 77 | `NSFACC.LOCAL.REF` | `NsfAccountDetails_LocalRef` |  |  |  |
| 78 | `NSFACC.OVERRIDE` | `NsfAccountDetails_Override` |  |  |  |
| 79 | `NSFACC.RECORD.STATUS` | `NsfAccountDetails_RecordStatus` | String |  |  |
| 80 | `NSFACC.CURR.NO` | `NsfAccountDetails_CurrNo` | String |  |  |
| 81 | `NSFACC.INPUTTER` | `NsfAccountDetails_Inputter` |  |  |  |
| 82 | `NSFACC.DATE.TIME` | `NsfAccountDetails_DateTime` |  |  |  |
| 83 | `NSFACC.AUTHORISER` | `NsfAccountDetails_Authoriser` | String |  |  |
| 84 | `NSFACC.CO.CODE` | `NsfAccountDetails_CoCode` | String |  |  |
| 85 | `NSFACC.DEPT.CODE` | `NsfAccountDetails_DeptCode` | String |  |  |
| 86 | `NSFACC.AUDITOR.CODE` | `NsfAccountDetails_AuditorCode` | String |  |  |
| 87 | `NSFACC.AUDIT.DATE.TIME` | `NsfAccountDetails_AuditDateTime` | String |  |  |
