# PA.CONNECTION.TRACKER — Table Schema

> Source: `INSERTS/I_F.PA.CONNECTION.TRACKER` in `PA_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CON.TRACK.CUSTOMER.ID` | `PaConnectionTracker_CustomerId` | TField |  |  |
| 2 | `CON.TRACK.BANK.ID` | `PaConnectionTracker_BankId` | TField |  |  |
| 3 | `CON.TRACK.BANK.CODE` | `PaConnectionTracker_BankCode` | TField |  |  |
| 4 | `CON.TRACK.OBCP.ID` | `PaConnectionTracker_ObcpId` | TField |  |  |
| 5 | `CON.TRACK.CONN.STATUS` | `PaConnectionTracker_ConnStatus` | TField |  |  |
| 6 | `CON.TRACK.SUB.STATUS` | `PaConnectionTracker_SubStatus` | TField |  |  |
| 7 | `CON.TRACK.STATE.HIST` | `PaConnectionTracker_StateHist` |  |  |  |
| 8 | `CON.TRACK.OBCP.CONNECTION.ID` | `PaConnectionTracker_ObcpConnectionId` | TField |  |  |
| 9 | `CON.TRACK.OBCP.BANK.ID` | `PaConnectionTracker_ObcpBankId` | TField |  |  |
| 10 | `CON.TRACK.BANK.NAME` | `PaConnectionTracker_BankName` | TField |  |  |
| 11 | `CON.TRACK.BANK.COUNTRY.CODE` | `PaConnectionTracker_BankCountryCode` | TField |  |  |
| 12 | `CON.TRACK.OBCP.CUSTOMER.ID` | `PaConnectionTracker_ObcpCustomerId` | TField |  |  |
| 13 | `CON.TRACK.DAILY.REFRESH` | `PaConnectionTracker_DailyRefresh` | TField |  |  |
| 14 | `CON.TRACK.NEXT.REF.AVAILABLE` | `PaConnectionTracker_NextRefAvailable` | TField |  |  |
| 15 | `CON.TRACK.CREATED.AT` | `PaConnectionTracker_CreatedAt` | TField |  |  |
| 16 | `CON.TRACK.UPDATED.AT` | `PaConnectionTracker_UpdatedAt` | TField |  |  |
| 17 | `CON.TRACK.LAST.SUCCESS.AT` | `PaConnectionTracker_LastSuccessAt` | TField |  |  |
| 18 | `CON.TRACK.CURRENT.STATE` | `PaConnectionTracker_CurrentState` | TField |  |  |
| 19 | `CON.TRACK.LATEST.TOKEN` | `PaConnectionTracker_LatestToken` |  |  |  |
| 20 | `CON.TRACK.LATEST.REDIRECT.URL` | `PaConnectionTracker_LatestRedirectUrl` |  |  |  |
| 21 | `CON.TRACK.DEF.CONSENT.ARR.ID` | `PaConnectionTracker_DefConsentArrId` | TField |  |  |
| 22 | `CON.TRACK.OUR.CONSENT.GIVEN.DATE` | `PaConnectionTracker_OurConsentGivenDate` | TField |  |  |
| 23 | `CON.TRACK.OUR.CONSENT.TYPES` | `PaConnectionTracker_OurConsentTypes` |  |  |  |
| 24 | `CON.TRACK.OUR.CONSENT.EXPIRED.AT` | `PaConnectionTracker_OurConsentExpiredAt` |  |  |  |
| 25 | `CON.TRACK.RESERVED.20` | `PaConnectionTracker_Reserved20` |  |  |  |
| 26 | `CON.TRACK.RESERVED.21` | `PaConnectionTracker_Reserved21` |  |  |  |
| 27 | `CON.TRACK.RESERVED.22` | `PaConnectionTracker_Reserved22` |  |  |  |
| 28 | `CON.TRACK.OUR.CONSENT.FROM.DATE` | `PaConnectionTracker_OurConsentFromDate` |  |  |  |
| 29 | `CON.TRACK.OUR.CONSENT.TO.DATE` | `PaConnectionTracker_OurConsentToDate` |  |  |  |
| 30 | `CON.TRACK.RESERVED.2` | `PaConnectionTracker_Reserved2` | TField |  |  |
| 31 | `CON.TRACK.RESERVED.3` | `PaConnectionTracker_Reserved3` | TField |  |  |
| 32 | `CON.TRACK.RESERVED.4` | `PaConnectionTracker_Reserved4` | TField |  |  |
| 33 | `CON.TRACK.RESERVED.5` | `PaConnectionTracker_Reserved5` | TField |  |  |
| 34 | `CON.TRACK.RESERVED.6` | `PaConnectionTracker_Reserved6` | TField |  |  |
| 35 | `CON.TRACK.RESERVED.7` | `PaConnectionTracker_Reserved7` | TField |  |  |
| 36 | `CON.TRACK.RESERVED.8` | `PaConnectionTracker_Reserved8` | TField |  |  |
| 37 | `CON.TRACK.OBCP.TOKEN` | `PaConnectionTracker_ObcpToken` |  |  |  |
| 38 | `CON.TRACK.OBCP.REDIRECT.URL` | `PaConnectionTracker_ObcpRedirectUrl` |  |  |  |
| 39 | `CON.TRACK.SHOW.CONSENT.CONFIRM` | `PaConnectionTracker_ShowConsentConfirm` | TField |  |  |
| 40 | `CON.TRACK.CONSENT.TYPES` | `PaConnectionTracker_ConsentTypes` |  |  |  |
| 41 | `CON.TRACK.CONSENT.PERIOD.DAYS` | `PaConnectionTracker_ConsentPeriodDays` | TField |  |  |
| 42 | `CON.TRACK.CONSENT.GIVEN.AT` | `PaConnectionTracker_ConsentGivenAt` | TField |  |  |
| 43 | `CON.TRACK.CONSENT.EXPIRES.AT` | `PaConnectionTracker_ConsentExpiresAt` | TField |  |  |
| 44 | `CON.TRACK.USER.PRESENT` | `PaConnectionTracker_UserPresent` | TField |  |  |
| 45 | `CON.TRACK.DEVICE.TYPE` | `PaConnectionTracker_DeviceType` | TField |  |  |
| 46 | `CON.TRACK.REMOTE.IP` | `PaConnectionTracker_RemoteIp` | TField |  |  |
| 47 | `CON.TRACK.ARRANGEMENT.ID` | `PaConnectionTracker_ArrangementId` |  |  |  |
| 48 | `CON.TRACK.OBCP.ACCOUNT.ID` | `PaConnectionTracker_ObcpAccountId` |  |  |  |
| 49 | `CON.TRACK.OBCP.STATUS` | `PaConnectionTracker_ObcpStatus` |  |  |  |
| 50 | `CON.TRACK.BALANCES.LAST.UPDATED` | `PaConnectionTracker_BalancesLastUpdated` |  |  |  |
| 51 | `CON.TRACK.TRANSACTIONS.LAST.UPDATED` | `PaConnectionTracker_TransactionsLastUpdated` |  |  |  |
| 52 | `CON.TRACK.ALL.TRANSACTIONS.RECEIVED` | `PaConnectionTracker_AllTransactionsReceived` |  |  |  |
| 53 | `CON.TRACK.TRANSACTION.NEXT.PAGE.ID` | `PaConnectionTracker_TransactionNextPageId` |  |  |  |
| 54 | `CON.TRACK.TRANSACTION.FROM.ID` | `PaConnectionTracker_TransactionFromId` |  |  |  |
| 55 | `CON.TRACK.ERROR.CODE` | `PaConnectionTracker_ErrorCode` |  |  |  |
| 56 | `CON.TRACK.ERROR.REASON` | `PaConnectionTracker_ErrorReason` |  |  |  |
| 57 | `CON.TRACK.RESERVED.9` | `PaConnectionTracker_Reserved9` |  |  |  |
| 58 | `CON.TRACK.RESERVED.10` | `PaConnectionTracker_Reserved10` |  |  |  |
| 59 | `CON.TRACK.RESERVED.11` | `PaConnectionTracker_Reserved11` |  |  |  |
| 60 | `CON.TRACK.RESERVED.12` | `PaConnectionTracker_Reserved12` |  |  |  |
| 61 | `CON.TRACK.RESERVED.13` | `PaConnectionTracker_Reserved13` |  |  |  |
| 62 | `CON.TRACK.BATCH.ID` | `PaConnectionTracker_BatchId` |  |  |  |
| 63 | `CON.TRACK.PROCESSED.FLAG` | `PaConnectionTracker_ProcessedFlag` |  |  |  |
| 64 | `CON.TRACK.RECEIVED.COUNT` | `PaConnectionTracker_ReceivedCount` |  |  |  |
| 65 | `CON.TRACK.SUCCESSFUL.COUNT` | `PaConnectionTracker_SuccessfulCount` |  |  |  |
| 66 | `CON.TRACK.FAILED.COUNT` | `PaConnectionTracker_FailedCount` |  |  |  |
| 67 | `CON.TRACK.SEQUENCE.REF` | `PaConnectionTracker_SequenceRef` |  |  |  |
| 68 | `CON.TRACK.RESERVED.15` | `PaConnectionTracker_Reserved15` |  |  |  |
| 69 | `CON.TRACK.RESERVED.16` | `PaConnectionTracker_Reserved16` |  |  |  |
| 70 | `CON.TRACK.RESERVED.17` | `PaConnectionTracker_Reserved17` |  |  |  |
| 71 | `CON.TRACK.RESERVED.18` | `PaConnectionTracker_Reserved18` |  |  |  |
| 72 | `CON.TRACK.CREATED.BY` | `PaConnectionTracker_CreatedBy` | TField |  |  |
| 73 | `CON.TRACK.CREATION.DATE` | `PaConnectionTracker_CreationDate` | TField |  |  |
| 74 | `CON.TRACK.CREATED.CHANNEL` | `PaConnectionTracker_CreatedChannel` | TField |  |  |
| 75 | `CON.TRACK.T.C.ACCEPTED` | `PaConnectionTracker_TCAccepted` | TField |  |  |
| 76 | `CON.TRACK.LAST.ERROR.ID` | `PaConnectionTracker_LastErrorId` |  |  |  |
| 77 | `CON.TRACK.LAST.ERROR.REASON` | `PaConnectionTracker_LastErrorReason` |  |  |  |
| 78 | `CON.TRACK.RECORD.STATUS` | `PaConnectionTracker_RecordStatus` | String |  |  |
| 79 | `CON.TRACK.CURR.NO` | `PaConnectionTracker_CurrNo` | String |  |  |
| 80 | `CON.TRACK.INPUTTER` | `PaConnectionTracker_Inputter` |  |  |  |
| 81 | `CON.TRACK.DATE.TIME` | `PaConnectionTracker_DateTime` |  |  |  |
| 82 | `CON.TRACK.AUTHORISER` | `PaConnectionTracker_Authoriser` | String |  |  |
| 83 | `CON.TRACK.CO.CODE` | `PaConnectionTracker_CoCode` | String |  |  |
| 84 | `CON.TRACK.DEPT.CODE` | `PaConnectionTracker_DeptCode` | String |  |  |
| 85 | `CON.TRACK.AUDITOR.CODE` | `PaConnectionTracker_AuditorCode` | String |  |  |
| 86 | `CON.TRACK.AUDIT.DATE.TIME` | `PaConnectionTracker_AuditDateTime` | String |  |  |
| 87 | `CON.TRACK.LOCAL.REF` | `PaConnectionTracker_LocalRef` |  |  |  |
| 88 | `CON.TRACK.OVERRIDE` | `PaConnectionTracker_Override` |  |  |  |
