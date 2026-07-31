# SC.CA.ERROR.LOG — Table Schema

> Source: `INSERTS/I_F.SC.CA.ERROR.LOG` in `SC_SccConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CAER.EVENT.TYPE` | `ScCaErrorLog_EventType` | TField |  | Holds the corporate action event being processed. This field is a single value field. |
| 2 | `SC.CAER.STP` | `ScCaErrorLog_Stp` | TField |  | This field will be set to YES if the corporate action event is being processed by Full Straight ThroughProcessing. This field is a single value field. |
| 3 | `SC.CAER.LOAN` | `ScCaErrorLog_Loan` | TField |  | This field will be set to YES if the corporate action event is being processed by Straight Through Processing forthe Lent portion of the security This field is a single value field. |
| 4 | `SC.CAER.DEPOSITORY` | `ScCaErrorLog_Depository` | TField |  | Depository is updated from Diary. |
| 5 | `SC.CAER.SECURITY.NO` | `ScCaErrorLog_SecurityNo` |  |  |  |
| 6 | `SC.CAER.PAY.DATE` | `ScCaErrorLog_PayDate` |  |  |  |
| 7 | `SC.CAER.EX.DATE` | `ScCaErrorLog_ExDate` |  |  |  |
| 8 | `SC.CAER.DELIV.REF` | `ScCaErrorLog_DelivRef` |  |  |  |
| 9 | `SC.CAER.RECEIVING.DATE` | `ScCaErrorLog_ReceivingDate` |  |  |  |
| 10 | `SC.CAER.MESSAGE.TYPE` | `ScCaErrorLog_MessageType` |  |  |  |
| 11 | `SC.CAER.SEME.REF` | `ScCaErrorLog_SemeRef` |  |  |  |
| 12 | `SC.CAER.CORP.REF` | `ScCaErrorLog_CorpRef` |  |  |  |
| 13 | `SC.CAER.ERRORS` | `ScCaErrorLog_Errors` |  |  |  |
| 14 | `SC.CAER.WARNINGS` | `ScCaErrorLog_Warnings` |  |  |  |
| 15 | `SC.CAER.STATUS` | `ScCaErrorLog_Status` |  |  |  |
| 16 | `SC.CAER.STAGE` | `ScCaErrorLog_Stage` |  |  |  |
| 17 | `SC.CAER.QUANTITY` | `ScCaErrorLog_Quantity` |  |  |  |
| 18 | `SC.CAER.NEW.SECURITY` | `ScCaErrorLog_NewSecurity` |  |  |  |
| 19 | `SC.CAER.PSTA.QTY` | `ScCaErrorLog_PstaQty` |  |  |  |
| 20 | `SC.CAER.NET.CASH` | `ScCaErrorLog_NetCash` |  |  |  |
| 21 | `SC.CAER.GROSS.CASH` | `ScCaErrorLog_GrossCash` |  |  |  |
| 22 | `SC.CAER.PSTA.CASH` | `ScCaErrorLog_PstaCash` |  |  |  |
| 23 | `SC.CAER.MSG.FUNC` | `ScCaErrorLog_MsgFunc` |  |  |  |
| 24 | `SC.CAER.PROC.STATUS` | `ScCaErrorLog_ProcStatus` |  |  |  |
| 25 | `SC.CAER.LINK.MT` | `ScCaErrorLog_LinkMt` |  |  |  |
| 26 | `SC.CAER.LINK.MT.REF` | `ScCaErrorLog_LinkMtRef` |  |  |  |
| 27 | `SC.CAER.LINK.CORP.REF` | `ScCaErrorLog_LinkCorpRef` |  |  |  |
| 28 | `SC.CAER.RESERVED.20` | `ScCaErrorLog_Reserved20` |  |  |  |
| 29 | `SC.CAER.RESERVED.19` | `ScCaErrorLog_Reserved19` |  |  |  |
| 30 | `SC.CAER.RESERVED.18` | `ScCaErrorLog_Reserved18` |  |  |  |
| 31 | `SC.CAER.RESERVED.17` | `ScCaErrorLog_Reserved17` |  |  |  |
| 32 | `SC.CAER.RESERVED.16` | `ScCaErrorLog_Reserved16` |  |  |  |
| 33 | `SC.CAER.RESERVED.15` | `ScCaErrorLog_Reserved15` |  |  |  |
| 34 | `SC.CAER.OPT.SEME.REF` | `ScCaErrorLog_OptSemeRef` |  |  |  |
| 35 | `SC.CAER.OPT.DELIV.REF` | `ScCaErrorLog_OptDelivRef` |  |  |  |
| 36 | `SC.CAER.OPT.MSG.FUNC` | `ScCaErrorLog_OptMsgFunc` |  |  |  |
| 37 | `SC.CAER.RESERVED.11` | `ScCaErrorLog_Reserved11` |  |  |  |
| 38 | `SC.CAER.OPTION` | `ScCaErrorLog_Option` |  |  |  |
| 39 | `SC.CAER.OPTION.DESC` | `ScCaErrorLog_OptionDesc` |  |  |  |
| 40 | `SC.CAER.STATUS.CODE` | `ScCaErrorLog_StatusCode` |  |  |  |
| 41 | `SC.CAER.REASON.CODE` | `ScCaErrorLog_ReasonCode` |  |  |  |
| 42 | `SC.CAER.REASON.NARR` | `ScCaErrorLog_ReasonNarr` |  |  |  |
| 43 | `SC.CAER.LINK.DIARY` | `ScCaErrorLog_LinkDiary` | TField |  | This field is only for manual intervention purpose. System does not perform any action on this field. |
| 44 | `SC.CAER.NARRATIVE` | `ScCaErrorLog_Narrative` |  |  |  |
| 45 | `SC.CAER.TOT.SECURITY` | `ScCaErrorLog_TotSecurity` |  |  |  |
| 46 | `SC.CAER.TOTAL.DEBIT` | `ScCaErrorLog_TotalDebit` |  |  |  |
| 47 | `SC.CAER.TOTAL.CREDIT` | `ScCaErrorLog_TotalCredit` |  |  |  |
| 48 | `SC.CAER.TOTAL.CASH` | `ScCaErrorLog_TotalCash` |  |  |  |
| 49 | `SC.CAER.TOTAL.CASH.CCY` | `ScCaErrorLog_TotalCashCcy` |  |  |  |
| 50 | `SC.CAER.LATEST.MSG` | `ScCaErrorLog_LatestMsg` | TField |  |  |
| 51 | `SC.CAER.LATEST.STATUS` | `ScCaErrorLog_LatestStatus` | TField |  |  |
| 52 | `SC.CAER.LATEST.STAGE` | `ScCaErrorLog_LatestStage` | TField |  |  |
| 53 | `SC.CAER.LATEST.WARN.ERROR` | `ScCaErrorLog_LatestWarnError` |  |  |  |
| 54 | `SC.CAER.LATEST.STATUS.CODE` | `ScCaErrorLog_LatestStatusCode` | TField |  |  |
| 55 | `SC.CAER.LATEST.REASON.CODE` | `ScCaErrorLog_LatestReasonCode` | TField |  |  |
| 56 | `SC.CAER.TRANSACTION.ID` | `ScCaErrorLog_TransactionId` | TField |  |  |
| 57 | `SC.CAER.LATEST.MSG.FUNC` | `ScCaErrorLog_LatestMsgFunc` | TField |  |  |
| 58 | `SC.CAER.RESERVED.8` | `ScCaErrorLog_Reserved8` |  |  |  |
| 59 | `SC.CAER.RESERVED.7` | `ScCaErrorLog_Reserved7` |  |  |  |
| 60 | `SC.CAER.RESERVED.6` | `ScCaErrorLog_Reserved6` |  |  |  |
| 61 | `SC.CAER.RESERVED.5` | `ScCaErrorLog_Reserved5` |  |  |  |
| 62 | `SC.CAER.RESERVED.4` | `ScCaErrorLog_Reserved4` |  |  |  |
| 63 | `SC.CAER.RESERVED.3` | `ScCaErrorLog_Reserved3` | TField |  |  |
| 64 | `SC.CAER.RESERVED.2` | `ScCaErrorLog_Reserved2` | TField |  |  |
| 65 | `SC.CAER.RESERVED.1` | `ScCaErrorLog_Reserved1` | TField |  |  |
| 66 | `SC.CAER.LOCAL.REF` | `ScCaErrorLog_LocalRef` |  |  |  |
| 67 | `SC.CAER.OVERRIDE` | `ScCaErrorLog_Override` |  |  |  |
| 68 | `SC.CAER.RECORD.STATUS` | `ScCaErrorLog_RecordStatus` | String |  |  |
| 69 | `SC.CAER.CURR.NO` | `ScCaErrorLog_CurrNo` | String |  |  |
| 70 | `SC.CAER.INPUTTER` | `ScCaErrorLog_Inputter` |  |  |  |
| 71 | `SC.CAER.DATE.TIME` | `ScCaErrorLog_DateTime` |  |  |  |
| 72 | `SC.CAER.AUTHORISER` | `ScCaErrorLog_Authoriser` | String |  |  |
| 73 | `SC.CAER.CO.CODE` | `ScCaErrorLog_CoCode` | String |  |  |
| 74 | `SC.CAER.DEPT.CODE` | `ScCaErrorLog_DeptCode` | String |  |  |
| 75 | `SC.CAER.AUDITOR.CODE` | `ScCaErrorLog_AuditorCode` | String |  |  |
| 76 | `SC.CAER.AUDIT.DATE.TIME` | `ScCaErrorLog_AuditDateTime` | String |  |  |
| 77 | `SC.CAER.INCOME.CODE` | `ScCaErrorLog_IncomeCode` |  |  |  |
| 78 | `SC.CAER.INCOME.RATE` | `ScCaErrorLog_IncomeRate` |  |  |  |
| 79 | `SC.CAER.INCOME.AMOUNT` | `ScCaErrorLog_IncomeAmount` |  |  |  |
| 80 | `SC.CAER.SYS.HOLDINGS` | `ScCaErrorLog_SysHoldings` | TField |  | This field will hold the system computed eligible holdings maintained per depository and sub account combination Updated by the system, no input field |
| 81 | `SC.CAER.SUB.ACCOUNT` | `ScCaErrorLog_SubAccount` | TField |  | Field to hold the SUB.ACCOUNT value and is updated by the system. Mapped from 97A of incoming MT message to hold the SUB.ACCOUNT corresponding to SUB.ACC.EXT.ID. Any Sub account defined at CUSTOMER.SECURITY is considered OMNIBUS sub account , otherwise its a SEGREGATED subaccount . Incase of Omnibus account in 97A tag, and SubAccount is defined in CUSTOMER.SECURITY, this field will hold theOmnibus Account value. Incase of Omnibus account in 97A tag and is found in DEP.EXT.ACC.ID of CUSTOMER.SECURITY, this field will holdthe value 'MAIN'. Incase of Segregated account in 97A tag, this field will hold the value 'SEGREGATED' |
| 82 | `SC.CAER.SUB.ACCT.EXT.ID` | `ScCaErrorLog_SubAcctExtId` | TField |  | Mapped from 97A of incoming MT message. |
