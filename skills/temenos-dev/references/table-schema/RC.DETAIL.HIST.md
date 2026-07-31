# RC.DETAIL.HIST — Table Schema

> Source: `INSERTS/I_F.RC.DETAIL.HIST` in `RC_TransactionCycler.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.DET.HIS.RETRY.FQU` | `RcDetailHist_RetryFqu` | TField |  | This system generated fields holds the retry frequency for the transaction being recycled. Validation rules No input field |
| 2 | `RC.DET.HIS.NO.OF.RETRIES` | `RcDetailHist_NoOfRetries` | TField |  | Number of retry attempts for that transaction based on RC.CONDITION attached for this type of transaction. System updated |
| 3 | `RC.DET.HIS.RETRY.ATTEMPTED` | `RcDetailHist_RetryAttempted` | TField |  | System generate field which holds the number of retry attempts for this transaction. Validation rules No Input |
| 4 | `RC.DET.HIS.DT.CONVENTION` | `RcDetailHist_DtConvention` | TField |  | Holds either FORWARD or BACKWARD By default, DT.CONVENTION is FORWARD This field is to indicate when RETRY.END.DATE falls on holiday, whether it needs to cycle to next or previous working day |
| 5 | `RC.DET.HIS.RESERVED.11` | `RcDetailHist_Reserved11` | TField |  |  |
| 6 | `RC.DET.HIS.RETRY.START.DATE` | `RcDetailHist_RetryStartDate` | TField |  | This field holds the date the entry was loaded into the cycler. System generated Validation rules No Input |
| 7 | `RC.DET.HIS.RETRY.END.DATE` | `RcDetailHist_RetryEndDate` | TField |  | This field holds the end date of the re try period. System generated Validation rules No input field |
| 8 | `RC.DET.HIS.NEXT.RETRY.DATE` | `RcDetailHist_NextRetryDate` | TField |  | The next date on which retry service would pick this transaction for processing FThis will be updated based on the frequency. System updated |
| 9 | `RC.DET.HIS.NEXT.RETRY.STAGE` | `RcDetailHist_NextRetryStage` | TField |  | This field indicates whether next retry to be done during SOD/EOD/online System updated |
| 10 | `RC.DET.HIS.SETTLE.OPTION` | `RcDetailHist_SettleOption` | TField |  | This field specifies the settlement conditions given in RC.CONDITION This can be PARTIAL/END.PARTIAL/NONE Default is none System updated |
| 11 | `RC.DET.HIS.TXN.TYPE` | `RcDetailHist_TxnType` | TField |  | Defaulted from RC.TYPE during capture of that transaction System updated |
| 12 | `RC.DET.HIS.RC.TYPE` | `RcDetailHist_RcType` | TField |  | System generated field which holds the link to the RC.TYPE record. Validation rules No input |
| 13 | `RC.DET.HIS.RC.CONDITION` | `RcDetailHist_RcCondition` | TField |  | This field links a RC.CONDITION reference to a transaction This field is updated during the capture of the transaction. |
| 14 | `RC.DET.HIS.CONTRACT.ID` | `RcDetailHist_ContractId` | TField |  | This field holds the original contract id, for accounts this will be the account number for multi-currency accounts the main account number; for AA this will be the key to AA.BILL.DETAILS, for contract based applications the transaction reference from the entry. System generated Validation rules No input |
| 15 | `RC.DET.HIS.AA.PRODUCT.GROUP` | `RcDetailHist_AaProductGroup` | TField |  | This field holds the AA.PRODUCT.GROUP System generated Validation rules No input field |
| 16 | `RC.DET.HIS.AA.PRODUCT` | `RcDetailHist_AaProduct` | TField |  | This field holds the AA.PRODUCT System generated field Validation rules No input |
| 17 | `RC.DET.HIS.ARRANGEMENT.ID` | `RcDetailHist_ArrangementId` | TField |  | This field is populated with the underlying arrangement id, if it is an AA&#160;contract. System generated Validation rules No input |
| 18 | `RC.DET.HIS.CONTRACT.CATEGORY` | `RcDetailHist_ContractCategory` | TField |  | This field holds the product category of the underlying contract if there is one. System generated Validation rules No input |
| 19 | `RC.DET.HIS.ORIG.ENTRY.TABLE` | `RcDetailHist_OrigEntryTable` |  |  |  |
| 20 | `RC.DET.HIS.ORIG.ENTRY.ID` | `RcDetailHist_OrigEntryId` |  |  |  |
| 21 | `RC.DET.HIS.TRANS.CCY` | `RcDetailHist_TransCcy` | TField |  | This field stores the transaction currency. System generated Validation rules No input field Valid record from CURRENCY table |
| 22 | `RC.DET.HIS.ORIG.AMT` | `RcDetailHist_OrigAmt` | TField |  |  |
| 23 | `RC.DET.HIS.ORIG.AMT.LCY` | `RcDetailHist_OrigAmtLcy` | TField |  | Original amount in local currency when transaction currency is foreign currency |
| 24 | `RC.DET.HIS.ORIG.EXCH.RATE` | `RcDetailHist_OrigExchRate` | TField |  | This field stores the exchange rate used for cross currency transaction during the capture No input field Validation rules System generated |
| 25 | `RC.DET.HIS.SUSPENSE.CATEGORY` | `RcDetailHist_SuspenseCategory` | TField |  | This field contains the suspense category used for suspensing this entry. System generated Validation rules No input field Valid CATEGORY code |
| 26 | `RC.DET.HIS.RETRY.AMT` | `RcDetailHist_RetryAmt` | TField |  | This is the amount that will be processed by the cycler. System generated Validation rules No input field |
| 27 | `RC.DET.HIS.RETRY.AMT.LCY` | `RcDetailHist_RetryAmtLcy` | TField |  | Retry amount in local currency when transaction currency is foreign currency |
| 28 | `RC.DET.HIS.TXN.SIGN` | `RcDetailHist_TxnSign` | TField |  | Holds the transaction sign value. By default, settlement account is debited. Validation Rules: CREDIT or DEBIT |
| 29 | `RC.DET.HIS.COMBINE.WITH` | `RcDetailHist_CombineWith` |  |  |  |
| 30 | `RC.DET.HIS.COMBINED.AMT` | `RcDetailHist_CombinedAmt` | TField |  |  |
| 31 | `RC.DET.HIS.RC.STATUS` | `RcDetailHist_RcStatus` | TField |  |  |
| 32 | `RC.DET.HIS.SETTLE.STATUS` | `RcDetailHist_SettleStatus` | TField |  | This status indicates the current settlement status of the transaction Various possible settlement statuses are PENDING no settlement has happened . Would updated during capture SETTLED Fully settled .once cycler settles the transaction fully PARTIAL Partially settled.During retry if transaction is settled partially REJECTED Transaction is settled outside of rc framework |
| 33 | `RC.DET.HIS.LAST.RETRY` | `RcDetailHist_LastRetry` |  |  |  |
| 34 | `RC.DET.HIS.LAST.RETRY.STAGE` | `RcDetailHist_LastRetryStage` |  |  |  |
| 35 | `RC.DET.HIS.LAST.RESULT` | `RcDetailHist_LastResult` |  |  |  |
| 36 | `RC.DET.HIS.RETRY.TRANS.TABLE` | `RcDetailHist_RetryTransTable` |  |  |  |
| 37 | `RC.DET.HIS.RETRY.TRANS.REF` | `RcDetailHist_RetryTransRef` |  |  |  |
| 38 | `RC.DET.HIS.LAST.RETRY.TRIGGER` | `RcDetailHist_LastRetryTrigger` |  |  |  |
| 39 | `RC.DET.HIS.RESERVED.09` | `RcDetailHist_Reserved09` |  |  |  |
| 40 | `RC.DET.HIS.RESERVED.08` | `RcDetailHist_Reserved08` |  |  |  |
| 41 | `RC.DET.HIS.RESERVED.07` | `RcDetailHist_Reserved07` |  |  |  |
| 42 | `RC.DET.HIS.RESERVED.06` | `RcDetailHist_Reserved06` |  |  |  |
| 43 | `RC.DET.HIS.RESERVED.05` | `RcDetailHist_Reserved05` |  |  |  |
| 44 | `RC.DET.HIS.RECOVERED.AMT` | `RcDetailHist_RecoveredAmt` |  |  |  |
| 45 | `RC.DET.HIS.INT.NAME` | `RcDetailHist_IntName` |  |  |  |
| 46 | `RC.DET.HIS.INT.VALUE` | `RcDetailHist_IntValue` |  |  |  |
| 47 | `RC.DET.HIS.CO.CODE` | `RcDetailHist_CoCode` | String |  | Company code of the company in which the RC.DETAIL is captured System updated |
| 48 | `RC.DET.HIS.PREDECESSOR.ID` | `RcDetailHist_PredecessorId` | TField |  | RC.DETAIL.ID which is dependent on this RC.DETAIL.ID System updated |
| 49 | `RC.DET.HIS.LOCAL.REF` | `RcDetailHist_LocalRef` |  |  |  |
| 50 | `RC.DET.HIS.AMEND.BY` | `RcDetailHist_AmendBy` |  |  |  |
| 51 | `RC.DET.HIS.AMEND.DATE.TIME` | `RcDetailHist_AmendDateTime` |  |  |  |
| 52 | `RC.DET.HIS.AMEND.REASON` | `RcDetailHist_AmendReason` |  |  |  |
| 53 | `RC.DET.HIS.RC.HANDOFF.SETTLE.TYPE` | `RcDetailHist_RcHandoffSettleType` | TField |  | This field will get updated with the initiation application. For example the reason can be 'POSTING.RESTRICT / AC.LOCKED.EVENTS / ACTIVITY.RESTRICTION' etc.. From AA if Handoff given the settlement types will be indicated. |
| 54 | `RC.DET.HIS.PROCESSING.STAGE` | `RcDetailHist_ProcessingStage` |  |  |  |
| 55 | `RC.DET.HIS.TXN.CODE` | `RcDetailHist_TxnCode` | TField |  | This field will be updated with the transaction code of the original entry or passed by the application that has raised this retry trigger. |
| 56 | `RC.DET.HIS.EXCL.FUT.PEN.TXNS` | `RcDetailHist_ExclFuturePenTxns` |  |  |  |
| 57 | `RC.DET.HIS.CUTOFF.TIME` | `RcDetailHist_CutoffTime` | TField |  | Cutoff Info for the Transaction if any available as per the RC.CONDITION setup |
| 58 | `RC.DET.HIS.ONLINE.RETRY.ATTEMPTS` | `RcDetailHist_OnlineRetryAttemps` |  |  |  |
| 59 | `RC.DET.HIS.RANK.INFO` | `RcDetailHist_RankInfo` | TField |  | Rank Info Passed from the Business Application which will be used in the Priority Processing of the current Recycler Record. |
| 60 | `RC.DET.HIS.MULTI.SETTLE` | `RcDetailHist_MultiSettle` | TField |  | YES/NO/NULL field YES Denotes whether the current Retry Record is a part of Multi PAYIN Settlement Account Group. NO/NULL Denotes that the current Retry Record is Not part of Multi Settlement Account Group. |
| 61 | `RC.DET.HIS.MULTI.SETTLE.ORDER` | `RcDetailHist_MultiSettleOrder` | TField |  | Order of the Settlement Account in the Multi Settlement Account Group, based on which the Priority is decided for settlements. |
| 62 | `RC.DET.HIS.TAKEOVER.DATE` | `RcDetailHist_TakeoverDate` | TField |  | The date when a pending request has been created following the update of the settlement property, taking over from pending requests on old pay in accounts. |
