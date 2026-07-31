# AC.HVT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AC.HVT.PARAMETER` in `AC_HighVolume.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.HVT.DEFAULT.HVT` | `AcHvtParameter_DefaultHvt` | TField |  |  |
| 2 | `AC.HVT.CATEG.START` | `AcHvtParameter_CategStart` |  |  |  |
| 3 | `AC.HVT.CATEG.END` | `AcHvtParameter_CategEnd` |  |  |  |
| 4 | `AC.HVT.CATEG.RESERVED.5` | `AcHvtParameter_CategReserved5` |  |  |  |
| 5 | `AC.HVT.CATEG.RESERVED.4` | `AcHvtParameter_CategReserved4` |  |  |  |
| 6 | `AC.HVT.CATEG.RESERVED.3` | `AcHvtParameter_CategReserved3` |  |  |  |
| 7 | `AC.HVT.CATEG.RESERVED.2` | `AcHvtParameter_CategReserved2` |  |  |  |
| 8 | `AC.HVT.CATEG.RESERVED.1` | `AcHvtParameter_CategReserved1` |  |  |  |
| 9 | `AC.HVT.NON.HVT.JOB` | `AcHvtParameter_NonHvtJob` |  |  |  |
| 10 | `AC.HVT.NON.HVT.JOB.RES.5` | `AcHvtParameter_NonHvtJobRes5` | TField |  |  |
| 11 | `AC.HVT.NON.HVT.JOB.RES.4` | `AcHvtParameter_NonHvtJobRes4` | TField |  |  |
| 12 | `AC.HVT.NON.HVT.JOB.RES.3` | `AcHvtParameter_NonHvtJobRes3` | TField |  |  |
| 13 | `AC.HVT.NON.HVT.JOB.RES.2` | `AcHvtParameter_NonHvtJobRes2` | TField |  |  |
| 14 | `AC.HVT.NON.HVT.JOB.RES.1` | `AcHvtParameter_NonHvtJobRes1` | TField |  |  |
| 15 | `AC.HVT.HVT.ACTIVE.TIME` | `AcHvtParameter_HvtActiveTime` | TField |  | Defines the length of time in minutes that the current AC.HVT.TRIGGER record is active. AC.HVT.TRIGGER stores consolidated account updates for a particular account for an individual online session. The active record will be the one currently updated by online T24 updates. Once a record ceases to be active it becomes available to the online HVT merge service which will update the actual account related tables. A balanced merge service should ensure that its "catch up" processing ensures that only the currently active records remain in the AC.HVT.TRIGGER table. The default value is 15 minutes, a company level value will override the system level default Validation Rules: Should accept a value from 5-99 (Minimum interval time is 5minutes) |
| 16 | `AC.HVT.MERGE.CHECK.REQD` | `AcHvtParameter_MergeCheckReqd` | TField |  | Based on the setup in this field,System should check ACCOUNT and ECB balances before and after merge If there is any balance mismatch during online merge or real merge,System should raise the exception error and stop the merge process Validation Rules: Input should allow YES or NO Default is blank (NO) If MERGE.CHECK.REQD field is set as YES then new balance check should get executed before and after merge |
| 17 | `AC.HVT.CREDIT.CHECK.ID` | `AcHvtParameter_CreditCheckId` | TField | Yes | Identifies the conditional credit check test, e.f "FTOut" for outgoing payments, "SEPA" for incoming SEPA payments. Validation Rules: Non mandatory option field 15 Alpha Numeric |
| 18 | `AC.HVT.DO.CHECK` | `AcHvtParameter_DoCheck` | TField | Yes | Indicates the default funds availability check for HVT Accounts. TXN.CODE or POSTING.TYPE are the exception to the default. Validation Rules: Non mandatory option field Options are "YES" or "NO" |
| 19 | `AC.HVT.TXN.CODE` | `AcHvtParameter_TxnCode` |  |  |  |
| 20 | `AC.HVT.POSTING.TYPE` | `AcHvtParameter_PostingType` |  |  |  |
| 21 | `AC.HVT.CR.RESERVED.1` | `AcHvtParameter_CrReserved1` | TField |  |  |
| 22 | `AC.HVT.DEFAULT.BULK.SIZE` | `AcHvtParameter_DefaultBulkSize` | TField |  | Defines the block size that limits the number of AC.HVT.TRIGGER records merged in a single database transaction. The default value is 50, a company level value will override the system level default Validation Rules: Should accept a value from 0 to 999 |
| 23 | `AC.HVT.ENT.PER.IF.EVENT` | `AcHvtParameter_EntPerIfEvent` | TField |  | Based on the number defined in this field, the system bulks the entries to be pushed to IF.EVENTS.INTERFACE.TABLE If no value is defined, all the entries are pushed together as one event. For example, if there are 10 entries created during a transaction and this field holds a value of 5, then two events containing the entries followed by one event containing the balances will be pushed to the Integration Framework Validation Rules: Accepts a value from 0 to 999 |
| 24 | `AC.HVT.VIRTUAL.LOCKED.TIME` | `AcHvtParameter_VirtualLockedTime` | TField |  | Defines the length of time in milliseconds that the current AC.RESERVATION record is active. Once the AC.RESERVATION record time crosses VIRTUAL.LOCKED.TIME, AC.RESERVATION.TIDY.UP.SERVICE running in the background will delete the record. The default value is 500 milliseconds, a company level value will override the system level default Validation Rules: Should accept a value from 1-9999 (Minimum interval time is 1 millisecond) |
| 25 | `AC.HVT.HVT.NO.LOCK` | `AcHvtParameter_HvtNoLock` | TField | No | If this field is set to YES and DO.CREDIT.CHECK is set to YES, then debit transactions to High volume customer accounts can be processed in parallel without locking. The shared caching must be enabled to utilize this functionality. Shared caching can currently be supported through Redis server or apache ignite. Validation Rules: Optional field. Valid values are: YES/NO YES - If DO.CREDIT.CHECK is YES and shared cache is enabled, HVT account transaction will be processed without locking. NO - If DO.CREDIT.CHECK is YES, HVT account transaction will be processed with locking. |
| 26 | `AC.HVT.LOCAL.REF` | `AcHvtParameter_LocalRef` |  |  |  |
| 27 | `AC.HVT.OVERRIDE` | `AcHvtParameter_Override` |  |  |  |
| 28 | `AC.HVT.RECORD.STATUS` | `AcHvtParameter_RecordStatus` | String |  |  |
| 29 | `AC.HVT.CURR.NO` | `AcHvtParameter_CurrNo` | String |  |  |
| 30 | `AC.HVT.INPUTTER` | `AcHvtParameter_Inputter` |  |  |  |
| 31 | `AC.HVT.DATE.TIME` | `AcHvtParameter_DateTime` |  |  |  |
| 32 | `AC.HVT.AUTHORISER` | `AcHvtParameter_Authoriser` | String |  |  |
| 33 | `AC.HVT.CO.CODE` | `AcHvtParameter_CoCode` | String |  |  |
| 34 | `AC.HVT.DEPT.CODE` | `AcHvtParameter_DeptCode` | String |  |  |
| 35 | `AC.HVT.AUDITOR.CODE` | `AcHvtParameter_AuditorCode` | String |  |  |
| 36 | `AC.HVT.AUDIT.DATE.TIME` | `AcHvtParameter_AuditDateTime` | String |  |  |
| 37 | `AC.HVT.DEFERRED.BALANCE.UPDATE` | `AcHvtParameter_DeferredBalanceUpdate` | TField |  | This field denotes whether the HVT Internal Account balance updates and entry posting are to be performed online or offline for GAI requests YES - Denotes balance updates, entry posting and other entry related updates will be performed offline - outside the transaction boundary NO or NULL - Denotes balance updates, entry posting and all other updates are performed within the transaction boundary |
| 38 | `AC.HVT.DEFERRED.IDS.TO.BATCH` | `AcHvtParameter_DeferredIdsToBatch` | TField |  | This field denotes the number of deferred entries that can be processed within one service transaction boundary of job AC.MERGE.STMT.ENTRY.PENDING Allowed value range - 1 to 999 when left blank, the number of deferred entries that will be processed by one service transaction boundary is 50 |
| 39 | `AC.HVT.DEFERRED.CONSOLIDATE.ENT` | `AcHvtParameter_DeferredConsolidateEnt` | TField |  | This field denotes the AC.CONSOLIDATE.COND definition that can be used for consolidation of deferred entries during offline service process This parameter level definition that will be used only when CONSOLIDATE.ENT in ACCOUNT is blank Validation Rules: Should be a valid record in AC.CONSOLIDATE.COND table |
